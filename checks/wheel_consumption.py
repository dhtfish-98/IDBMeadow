"""Check wheel-installed source identity and representative offline operations."""
from pathlib import Path as ConsumptionPath
import hashlib as consumption_hashlib
import importlib as consumption_importlib
import json as consumption_json
import subprocess as consumption_subprocess
import sys as consumption_sys

consumption_root = ConsumptionPath(consumption_sys.argv[1]).resolve()
consumption_name = consumption_sys.argv[2]
consumption_package = consumption_name.lower()
consumption_module = consumption_importlib.import_module(consumption_package)
consumption_location = ConsumptionPath(consumption_module.__file__).resolve()
assert 'site-packages' in str(consumption_location), str(consumption_location)
consumption_file_count = 0
for consumption_file in (consumption_root / 'src' / consumption_package).rglob('*.py'):
    consumption_relative = consumption_file.relative_to(consumption_root / 'src' / consumption_package)
    consumption_installed = consumption_location.parent / consumption_relative
    assert consumption_installed.read_bytes() == consumption_file.read_bytes(), str(consumption_relative)
    assert bool(consumption_installed.stat().st_mode & 0o111) == bool(consumption_file.stat().st_mode & 0o111), str(consumption_relative)+' executable mode differs'
    consumption_file_count += 1
consumption_cases = []
consumption_views = consumption_importlib.import_module('idbmeadow.semantic_views')
consumption_examples = [('empty/empty.idb','d41d8cd98f00b204e9800998ecf8427e',(0,1)),('v6.95/x32/kernel32.idb','00bf1bf1b779ce1af41371426821e0c2',(1754271744,1755177520))]
for consumption_relative, consumption_md5, consumption_bounds in consumption_examples:
    with consumption_module.meadow_from_file(path=str(consumption_root/'checks/data'/consumption_relative)) as consumption_database:
        consumption_metadata = consumption_views.meadow_Root(consumption_database)
        assert consumption_database.wordsize == 4
        assert consumption_metadata.version == 695
        assert consumption_metadata.md5 == consumption_md5
        consumption_api = consumption_module.meadow_IDAPython(consumption_database)
        assert (consumption_api.idc.MinEA(),consumption_api.idc.MaxEA()) == consumption_bounds
        consumption_cases.append('installed database metadata and emulated address bounds: '+consumption_relative)
from dataclasses import replace as consumption_replace
from idbmeadow.bounded_io import DEFAULT_LIMITS as consumption_limits, IDBFormatError as ConsumptionFormatError
import struct as consumption_struct
import zlib as consumption_zlib
consumption_pages = consumption_importlib.import_module('idbmeadow.database_pages')
consumption_types = consumption_importlib.import_module('idbmeadow.type_records')
consumption_record = consumption_struct.pack('<I', 0x7fffffff) + b'installed\0' + consumption_struct.pack('<I', 7) + b'\x01\0\0\0\0\x02'
consumption_encoded = consumption_zlib.compress(consumption_record)
consumption_wire = consumption_struct.pack('<III', 1, len(consumption_record), len(consumption_encoded)) + consumption_encoded
consumption_bucket = consumption_types.TILBucket(1, 18)
consumption_bucket.vsParse(consumption_wire)
assert consumption_bucket.defs[0].name == 'installed' and consumption_bucket.defs[0].ordinal == 7
consumption_cases.append('installed compressed TIL definition recovered')
try:
    consumption_pages.Section(6).vsParse(consumption_struct.pack('<BQ', 0, 2**63))
except ConsumptionFormatError:
    consumption_cases.append('installed declared section length rejected before allocation')
else:
    raise AssertionError('oversized declaration accepted')
consumption_path = consumption_root / 'checks/data/empty/empty.idb'
try:
    with consumption_module.from_file(consumption_path, limits=consumption_replace(consumption_limits, max_input_bytes=16)):
        raise AssertionError('oversized file accepted')
except ConsumptionFormatError:
    consumption_cases.append('installed input byte limit enforced')

print(consumption_json.dumps({'project':consumption_name,'status':'PASS','installed_source_files_identical':consumption_file_count,'consumer_checks_passed':len(consumption_cases),'checks':consumption_cases}))
