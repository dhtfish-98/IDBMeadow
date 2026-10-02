"""Owned ordinary records observed with either pinned or maintained modules."""
import importlib
import json
import struct
import sys
import zlib

pages = importlib.import_module(sys.argv[1])
types = importlib.import_module(sys.argv[2])
results = []
for version in (1, 4, 5, 6):
    raw = bytearray(64 if version <= 4 else 88)
    raw[:4] = b'IDA1'
    struct.pack_into('<IH', raw, 26, 0xaabbccdd, version)
    struct.pack_into('<I' if version <= 4 else '<Q', raw, 6, 0x1234)
    parsed = pages.FileHeader(raw)
    end = parsed.vsParse(raw)
    try:
        validated = parsed.validate()
    except Exception as error:
        validated = [type(error).__name__, str(error)]
    results.append({'header': version, 'end': end, 'offsets': parsed.offsets, 'checksums': parsed.checksums, 'magic': bytes(parsed.signature).hex(), 'validated': validated})
    for compressed in (False, True):
        for size in (0, 1, 7, 8, 31, 128, 256, 1024, 65537):
            payload = bytes((index * 17 + 3) % 256 for index in range(size))
            encoded = zlib.compress(payload) if compressed else payload
            raw = struct.pack('<BI' if version <= 4 else '<BQ', 2 if compressed else 0, len(encoded)) + encoded
            parsed = pages.Section(version)
            end = parsed.vsParse(raw)
            assert bytes(parsed.contents) == payload
            results.append({'section': [version, compressed, size], 'end': end, 'length': parsed.header.length, 'contents': bytes(parsed.contents).hex()})
for format in (17, 18):
    for compressed in (False, True):
        for count in (0, 1, 3):
            records = []
            for index in range(count):
                records.append(struct.pack('<I', 0x7fffffff) + ('name%d' % index).encode() + b'\0' + struct.pack('<I', index + 1) + b'\x01\0comment\0\0\0\x02')
            payload = b''.join(records)
            raw = struct.pack('<II', count, len(payload))
            raw += struct.pack('<I', len(zlib.compress(payload))) + zlib.compress(payload) if compressed else payload
            parsed = types.TILBucket(1 if compressed else 0, format)
            try:
                end = parsed.vsParse(raw)
            except Exception as error:
                results.append({'bucket': [format, compressed, count], 'error': [type(error).__name__, str(error)]})
                continue
            results.append({'bucket': [format, compressed, count], 'end': end, 'defs': [(d.name, d.ordinal, bytes(d.type_info).hex(), d.cmt, d.sclass) for d in parsed.defs]})
for width in (4, 8):
    for count in (1, 2, 3):
        raw = bytearray(2 * 8192)
        struct.pack_into('<4sIIII', raw, 0, b'VA*\0', 3, count, 2048, 2)
        for index in range(count):
            struct.pack_into('<' + ('II' if width == 4 else 'QQ'), raw, 20 + index * 2 * width, 0x1000 + index * 16, 0x1002 + index * 16)
            struct.pack_into('<II', raw, 8192 + index * 8, 0xa000 + index, 0xb000 + index)
        parsed = pages.ID1(width)
        end = parsed.vsParse(raw)
        values = [(segment.bounds.start, segment.bounds.end, segment.offset) for segment in parsed.segments]
        flags = [parsed.get_flags(0x1000 + index * 16) for index in range(count)]
        results.append({'flag_pages': [width, count], 'segments': values, 'flags': flags, 'end': end})
    for count in (0, 2):
        raw = bytearray(8192 + count * width)
        struct.pack_into('<4sIIII', raw, 0, b'VA*\0', 3, bool(count), 2048, 1)
        struct.pack_into('<' + ('I' if width == 4 else 'Q') + 'I', raw, 20, 0, count * width // 4)
        for index in range(count):
            struct.pack_into('<I' if width == 4 else '<Q', raw, 8192 + index * width, 0x1000 + index * 16)
        parsed = pages.NAM(width)
        end = parsed.vsParse(raw)
        results.append({'name_pages': [width, count], 'names': list(parsed.names()), 'end': end})
print(json.dumps(results, sort_keys=True))
