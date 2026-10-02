"""Owned wire fixtures and resource failure checks, without executing inputs."""
from array import array
from dataclasses import replace
from pathlib import Path
import os
import struct
import zlib

import pytest
import idbmeadow
from idbmeadow import database_pages as pages
from idbmeadow import type_records as types
from idbmeadow.bounded_io import (
    DEFAULT_LIMITS, IDBFormatError, ParseBudget, ParseLimits,
    materialize, owned_buffer, read_regular,
)


def header(version=6, magic=b'IDA1'):
    raw = bytearray(64 if version <= 4 else 88)
    raw[:4] = magic
    struct.pack_into('<IH', raw, 26, 0xaabbccdd, version)
    return raw


def section(payload, compressed=False, version=6):
    encoded = zlib.compress(payload) if compressed else payload
    return struct.pack('<BI' if version <= 4 else '<BQ', 2 if compressed else 0, len(encoded)) + encoded


def type_record(name=b'record', ordinal=7):
    return struct.pack('<I', 0x7fffffff) + name + b'\0' + struct.pack('<I', ordinal) + b'\x01\0comment\0\0\0\x02'


def bucket(records, compressed=False):
    payload = b''.join(records)
    raw = struct.pack('<II', len(records), len(payload))
    return raw + (struct.pack('<I', len(zlib.compress(payload))) + zlib.compress(payload) if compressed else payload)


@pytest.mark.parametrize('size', range(32))
def test_short_database_headers_raise_defined_error(size):
    with pytest.raises(IDBFormatError, match='database header'):
        idbmeadow.from_buffer(bytes(size))


@pytest.mark.parametrize('version', [1, 4, 5, 6])
def test_header_wire_fields_and_repeat_parse(version):
    raw = header(version)
    width = 'I' if version <= 4 else 'Q'
    struct.pack_into('<' + width, raw, 6, 0x1234)
    parsed = pages.FileHeader(raw)
    assert parsed.vsParse(raw) == len(raw)
    assert parsed.offsets == [0x1234, 0, 0, 0, 0, 0]
    assert parsed.sig2 == 0xaabbccdd and parsed.validate()
    parsed.vsParse(raw)
    assert len(parsed.offsets) == len(parsed.checksums) == 6


@pytest.mark.parametrize('version', [1, 4, 5, 6])
@pytest.mark.parametrize('compressed', [False, True])
def test_section_complete_independent_bytes(version, compressed):
    payload = b'bounded\0section\xff' * 31
    raw = b'prefix' + section(payload, compressed, version) + b'next record'
    parsed = pages.Section(version)
    end = parsed.vsParse(raw, offset=6, fast=True)
    assert parsed.contents == payload
    assert raw[end:] == b'next record'
    assert parsed.header.is_compressed is compressed


@pytest.mark.parametrize('cut', range(21))
def test_section_truncation_before_materialization(cut):
    raw = section(b'hello world!')
    with pytest.raises(IDBFormatError, match='section'):
        pages.Section(6).vsParse(raw[:cut])


def test_section_large_declaration_rejected_without_allocation():
    with pytest.raises(IDBFormatError, match='contents'):
        pages.Section(6).vsParse(struct.pack('<BQ', 0, 2**63))


@pytest.mark.parametrize('method', [1, 3, 255])
def test_unknown_compression_is_not_guessed(method):
    with pytest.raises(IDBFormatError, match='compression method'):
        pages.Section(6).vsParse(struct.pack('<BQ', method, 0))


@pytest.mark.parametrize('cut', range(1, 12))
def test_zlib_truncated_trailer_and_body_rejected(cut):
    encoded = zlib.compress(b'repeated' * 128)
    with pytest.raises(IDBFormatError, match='compressed'):
        materialize(encoded[:-cut], True, ParseBudget())


@pytest.mark.parametrize('suffix', [b'x', zlib.compress(b'second')])
def test_zlib_extra_member_or_trailing_bytes_rejected(suffix):
    with pytest.raises(IDBFormatError, match='trailing'):
        materialize(zlib.compress(b'first') + suffix, True, ParseBudget())


def test_inflation_limit_checked_before_large_output():
    limits = replace(DEFAULT_LIMITS, max_section_bytes=128)
    with pytest.raises(IDBFormatError, match='materialization byte limit'):
        materialize(zlib.compress(b'A' * 1_000_000), True, ParseBudget(limits))
    assert materialize(zlib.compress(b'A' * 128), True, ParseBudget(limits)) == b'A' * 128
    assert materialize(zlib.compress(b''), True, ParseBudget(limits), expected_size=0) == b''


def test_aggregate_budget_shared_by_sections_and_type_buckets():
    record = type_record()
    budget = ParseBudget(replace(DEFAULT_LIMITS, max_materialized_bytes=len(record) + 4))
    pages.Section(6, budget=budget).vsParse(section(b'four'))
    parsed = types.TILBucket(0, 18, budget=budget)
    parsed.vsParse(bucket([record]))
    assert parsed.defs[0].ordinal == 7
    with pytest.raises(IDBFormatError, match='materialization'):
        pages.Section(6, budget=budget).vsParse(section(b'x'))


@pytest.mark.parametrize('compressed', [False, True])
def test_bucket_ordinary_records_and_lookup(compressed):
    records = [type_record(), type_record(b'second', 19)]
    parsed = types.TILBucket(types.TIL_ZIP if compressed else 0, 18)
    raw = bucket(records, compressed)
    assert parsed.vsParse(raw) == len(raw)
    assert [(d.name, d.ordinal, d.type_info, d.cmt, d.sclass) for d in parsed.defs] == [
        ('record', 7, b'\x01', 'comment', 2), ('second', 19, b'\x01', 'comment', 2)]
    assert parsed.find_by_name('second') is parsed.get_by_ordinal(19)
    assert parsed.find_by_name('absent') is None
    assert parsed.get_by_ordinal(999) is None


def test_bucket_truncated_fields_and_oversized_count():
    with pytest.raises(IDBFormatError, match='definition count'):
        types.TILBucket(0, 18).vsParse(struct.pack('<II', 2**32 - 1, 0))
    raw = struct.pack('<I', 0x7fffffff) + b'nonterminated name'
    with pytest.raises(IDBFormatError, match='unterminated'):
        types.TILBucket(0, 18).vsParse(struct.pack('<II', 1, len(raw)) + raw)


def test_bucket_size_and_cumulative_definition_limits():
    raw = bytearray(bucket([type_record()], True))
    struct.pack_into('<I', raw, 4, len(type_record()) + 1)
    with pytest.raises(IDBFormatError, match='differs from declaration'):
        types.TILBucket(1, 18).vsParse(raw)
    budget = ParseBudget(replace(DEFAULT_LIMITS, max_type_definitions=1))
    types.TILBucket(0, 18, budget=budget).vsParse(bucket([type_record()]))
    with pytest.raises(IDBFormatError, match='type definition limit'):
        types.TILBucket(0, 18, budget=budget).vsParse(bucket([type_record()]))


@pytest.mark.parametrize('format,flags,ordinal,width', [(17, 0xffffffff, 7, 'I'), (18, 0x7fffffff, 7, 'I'), (18, 0xffffffff, 2**40, 'Q')])
@pytest.mark.parametrize('compressed', [False, True])
def test_type_record_ordinal_width_contract(format, flags, ordinal, width, compressed):
    record = struct.pack('<I', flags) + b'wide\0' + struct.pack('<' + width, ordinal) + b'\x01\0\0\0\0\x02'
    parsed = types.TILBucket(1 if compressed else 0, format)
    parsed.vsParse(bucket([record], compressed))
    assert parsed.defs[0].ordinal == ordinal


def test_section_raw_typed_memoryview_uses_byte_extent():
    raw = section(b'abc')
    words = array('I')
    words.frombytes(raw)
    parsed = pages.Section(6)
    parsed.vsParse(memoryview(words))
    assert parsed.contents == b'abc'


def test_database_owns_mutable_and_strided_byte_input():
    source = header()
    database = idbmeadow.from_buffer(source)
    source[:4] = b'xxxx'
    assert database.buf[:4] == database.header.signature == b'IDA1'
    interleaved = bytearray(byte for value in header() for byte in (value, 0))
    assert idbmeadow.from_buffer(memoryview(interleaved)[::2]).header.signature == b'IDA1'
    words = array('I', [0x12345678])
    assert owned_buffer(words) == words.tobytes()
    with pytest.raises(IDBFormatError, match='input byte limit'):
        owned_buffer(words, 3)


def test_database_new_parse_replaces_snapshot_and_resets_sections():
    raw = header()
    struct.pack_into('<Q', raw, 40, len(raw))  # unimplemented seg still bounded
    raw += section(b'first')
    parsed = idbmeadow.from_buffer(raw)
    assert parsed.sections[3].contents == b'first'
    parsed.vsParse(header(magic=b'IDA2'))
    assert parsed.wordsize == 8 and parsed.sections == [None] * 6
    assert parsed._parse_budget.materialized_bytes == 0


@pytest.mark.parametrize('offset', [1, 31, 87, 89, 2**63])
def test_invalid_section_offsets_rejected(offset):
    raw = header()
    struct.pack_into('<Q', raw, 40, offset)
    with pytest.raises(IDBFormatError):
        idbmeadow.from_buffer(raw)


def test_overlapping_sections_rejected():
    raw = header()
    struct.pack_into('<Q', raw, 40, len(raw))
    struct.pack_into('<Q', raw, 76, len(raw))
    with pytest.raises(IDBFormatError, match='overlapping'):
        idbmeadow.from_buffer(raw + section(b'data'))


def test_file_type_size_and_unchanged_bytes(tmp_path):
    path = tmp_path / 'data.idb'
    raw = bytes(header())
    path.write_bytes(raw)
    with idbmeadow.from_file(path) as parsed:
        assert parsed.wordsize == 4
    assert path.read_bytes() == raw
    with pytest.raises(IDBFormatError, match='input byte limit'):
        read_regular(path, replace(DEFAULT_LIMITS, max_input_bytes=32))
    link = tmp_path / 'link'
    link.symlink_to(path)
    with pytest.raises(IDBFormatError, match='regular file'):
        read_regular(link)
    with pytest.raises(IDBFormatError, match='regular file'):
        read_regular(tmp_path)
    if hasattr(os, 'mkfifo'):
        pipe = tmp_path / 'pipe'
        os.mkfifo(pipe)
        with pytest.raises(IDBFormatError, match='regular file'):
            read_regular(pipe)


def test_file_read_failure_closes_owned_descriptor(tmp_path, monkeypatch):
    path = tmp_path / 'data'
    path.write_bytes(b'data')
    descriptors = []
    real_open = os.open
    def observed_open(*args):
        descriptor = real_open(*args)
        descriptors.append(descriptor)
        return descriptor
    def fail_read(*args):
        raise OSError('injected read failure')
    monkeypatch.setattr(os, 'open', observed_open)
    monkeypatch.setattr(os, 'read', fail_read)
    with pytest.raises(OSError, match='injected'):
        read_regular(path)
    assert len(descriptors) == 1
    with pytest.raises(OSError):
        os.fstat(descriptors[0])


def test_file_changed_during_read_is_incomplete(tmp_path, monkeypatch):
    path = tmp_path / 'data'
    path.write_bytes(b'original')
    real_read = os.read
    altered = False
    def change_once(fd, count):
        nonlocal altered
        data = real_read(fd, count)
        if not altered:
            altered = True
            path.write_bytes(b'replaced longer')
        return data
    monkeypatch.setattr(os, 'read', change_once)
    with pytest.raises(IDBFormatError, match='changed while reading'):
        read_regular(path)


def flags_fixture(wordsize=4):
    raw = bytearray(2 * 8192)
    struct.pack_into('<4sIIII', raw, 0, b'VA*\0', 3, 1, 2048, 2)
    struct.pack_into('<' + ('II' if wordsize == 4 else 'QQ'), raw, 20, 0x1000, 0x1002)
    struct.pack_into('<II', raw, 8192, 0xdeadbeef, 0x12345678)
    return raw


@pytest.mark.parametrize('wordsize', [4, 8])
def test_flag_pages_have_independent_values_and_finite_segments(wordsize):
    parsed = pages.ID1(wordsize)
    raw = flags_fixture(wordsize)
    assert parsed.vsParse(raw) == len(raw)
    assert parsed.get_flags(0x1000) == 0xdeadbeef
    assert parsed.get_flags(0x1001) == 0x12345678
    with pytest.raises(KeyError):
        parsed.get_flags(0x1002)
    with pytest.raises(IndexError):
        parsed.get_next_segment(0x1000)


@pytest.mark.parametrize('field', [8, 16])
def test_flag_counts_rejected_before_vstruct_allocates(field):
    raw = flags_fixture()
    struct.pack_into('<I', raw, field, 0xffffffff)
    with pytest.raises(IDBFormatError):
        pages.ID1(4).vsParse(raw)


def test_name_page_never_allocates_declared_virtual_page_count():
    raw = bytearray(8192 + 8)
    struct.pack_into('<4sIIIIII', raw, 0, b'VA*\0', 3, 1, 2048, 0xffffffff, 0, 2)
    struct.pack_into('<II', raw, 8192, 0x1000, 0x2000)
    parsed = pages.NAM(4)
    assert parsed.vsParse(raw) == len(raw)
    assert len(parsed.buffer) == 8 and parsed.names() == (0x1000, 0x2000)
    parsed.dword_count = 0xffffffff
    with pytest.raises(IDBFormatError, match='name address table'):
        parsed.names()


@pytest.mark.parametrize('value', [0, -1, True, 1.5, None])
def test_limits_require_positive_integers(value):
    with pytest.raises(ValueError):
        ParseLimits(max_input_bytes=value)
