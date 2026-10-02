"""Owned input snapshots and bounded IDB/TIL materialization.

These limits apply to input and section/type bucket materialization. They do
not bound every inherited semantic query, script, or formatted report.
"""
from dataclasses import dataclass, fields
import os
import stat
import zlib


class IDBFormatError(ValueError):
    """The input cannot be completely parsed within the selected limits."""


@dataclass(frozen=True)
class ParseLimits:
    max_input_bytes: int = 256 * 1024 * 1024
    max_section_bytes: int = 1024 * 1024 * 1024
    max_materialized_bytes: int = 2 * 1024 * 1024 * 1024
    max_type_definitions: int = 1_000_000

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if type(value) is not int or value <= 0:
                raise ValueError(field.name + ' must be a positive integer')


DEFAULT_LIMITS = ParseLimits()


class ParseBudget:
    """One budget shared by the six sections and three nested TIL buckets."""
    def __init__(self, limits=DEFAULT_LIMITS):
        if not isinstance(limits, ParseLimits):
            raise TypeError('limits must be ParseLimits')
        self.limits = limits
        self.materialized_bytes = 0
        self.type_definitions = 0

    @property
    def remaining_bytes(self):
        return self.limits.max_materialized_bytes - self.materialized_bytes

    def charge_bytes(self, size):
        if type(size) is not int or size < 0 or size > self.remaining_bytes:
            raise IDBFormatError('aggregate materialization byte limit exceeded')
        self.materialized_bytes += size

    def charge_definitions(self, count):
        if count < 0 or count > self.limits.max_type_definitions - self.type_definitions:
            raise IDBFormatError('aggregate type definition limit exceeded')
        self.type_definitions += count


def owned_buffer(value, limit=DEFAULT_LIMITS.max_input_bytes):
    """Copy mutable/noncontiguous exporters after checking their byte count."""
    if type(value) is bytes:
        if len(value) > limit:
            raise IDBFormatError('input byte limit exceeded')
        return value
    try:
        view = memoryview(value)
    except TypeError as error:
        raise TypeError('input must support the buffer protocol') from error
    try:
        if view.nbytes > limit:
            raise IDBFormatError('input byte limit exceeded')
        return view.tobytes()
    finally:
        view.release()


def checked_span(data, offset, size, label='record'):
    if (type(offset) is not int or type(size) is not int or offset < 0 or
            size < 0 or offset > len(data) or size > len(data) - offset):
        raise IDBFormatError('truncated or invalid ' + label)
    return offset + size


def _identity(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def read_regular(path, limits=DEFAULT_LIMITS):
    """Read a local regular file and check observed identity before/after.

    This detects observed replacement or metadata changes, but cannot prove
    an atomic filesystem snapshot against a writer restoring that metadata.
    """
    ParseBudget(limits)
    before = os.lstat(path)
    if not stat.S_ISREG(before.st_mode):
        raise IDBFormatError('input must be a regular file, not a final symlink')
    flags = os.O_RDONLY
    for option in ('O_NOFOLLOW', 'O_NONBLOCK', 'O_BINARY'):
        flags |= getattr(os, option, 0)
    descriptor = os.open(path, flags)
    try:
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode) or _identity(before) != _identity(opened):
            raise IDBFormatError('input changed while opening')
        if opened.st_size > limits.max_input_bytes:
            raise IDBFormatError('input byte limit exceeded')
        chunks = []
        total = 0
        while True:
            chunk = os.read(descriptor, min(65536, limits.max_input_bytes - total + 1))
            if not chunk:
                break
            total += len(chunk)
            if total > limits.max_input_bytes:
                raise IDBFormatError('input byte limit exceeded')
            chunks.append(chunk)
        if _identity(opened) != _identity(os.fstat(descriptor)) or total != opened.st_size:
            raise IDBFormatError('input changed while reading')
        return b''.join(chunks)
    finally:
        os.close(descriptor)


def materialize(data, compressed, budget, expected_size=None):
    """Materialize one complete zlib member with a strict output ceiling."""
    ceiling = min(budget.limits.max_section_bytes, budget.remaining_bytes)
    if expected_size is not None:
        if expected_size < 0 or expected_size > ceiling:
            raise IDBFormatError('declared section size exceeds materialization limit')
        ceiling = expected_size
    if not compressed:
        if len(data) > ceiling:
            raise IDBFormatError('section materialization byte limit exceeded')
        result = bytes(data)
    else:
        decoder = zlib.decompressobj()
        chunks = []
        total = 0
        try:
            # max_length is always positive; 0 would silently mean unlimited.
            for position in range(0, len(data), 65536):
                if decoder.eof:
                    raise IDBFormatError('trailing bytes after compressed section')
                chunk = decoder.decompress(data[position:position + 65536], ceiling - total + 1)
                total += len(chunk)
                if total > ceiling or decoder.unconsumed_tail:
                    raise IDBFormatError('section materialization byte limit exceeded')
                chunks.append(chunk)
                if decoder.unused_data:
                    raise IDBFormatError('trailing bytes after compressed section')
        except zlib.error as error:
            raise IDBFormatError('invalid compressed section') from error
        if not decoder.eof:
            raise IDBFormatError('truncated compressed section')
        result = b''.join(chunks)
    if expected_size is not None and len(result) != expected_size:
        raise IDBFormatError('uncompressed section size differs from declaration')
    budget.charge_bytes(len(result))
    return result


def til_record_end(data, offset, format):
    """Preflight the finite variable strings of one type record before vstruct."""
    import struct
    checked_span(data, offset, 4, 'type flags')
    flags = struct.unpack_from('<I', data, offset)[0]
    if format < 18:
        flags &= 0x7fffffff
    if flags not in (0x7fffffff, 0xffffffff):
        raise IDBFormatError('unsupported type record flags')
    cursor = offset + 4
    # name, type_info, comment, fields_buf, field_comments are NUL terminated.
    for index in range(5):
        end = data.find(b'\0', cursor)
        if end < 0:
            raise IDBFormatError('unterminated type record field')
        cursor = end + 1
        if index == 0:
            cursor = checked_span(data, cursor, 8 if flags >> 31 else 4, 'type ordinal')
    return checked_span(data, cursor, 1, 'type storage class')
