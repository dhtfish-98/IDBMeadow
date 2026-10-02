# Derived from tests/fixtures.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os as meadow_os
import os.path as _boundary_import_os_path
import os as meadow_os
import six as meadow_six
import pytest as meadow_pytest
import idbmeadow as meadow_idb
if meadow_six.PY2:
    from functools32 import lru_cache as meadow_lru_cache
else:
    from functools import lru_cache as meadow_lru_cache
try:
    import capstone as meadow_capstone
    meadow_no_capstone = False
except:
    meadow_no_capstone = True
meadow_CD = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'empty_idb')
def empty_idb():
    meadow_path_601b22f = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'empty', 'empty.idb')
    with meadow_idb.from_file(meadow_path_601b22f) as meadow_db_2845b4e:
        yield meadow_db_2845b4e

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'kernel32_idb')
def kernel32_idb():
    meadow_path_a57723a = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'v6.95', 'x32', 'kernel32.idb')
    with meadow_idb.from_file(meadow_path_a57723a) as meadow_db_e792078:
        yield meadow_db_e792078

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'small_idb')
def small_idb():
    meadow_path_004a591 = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'small', 'small-colored.idb')
    with meadow_idb.from_file(meadow_path_004a591) as meadow_db_5fae4d2:
        yield meadow_db_5fae4d2

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'compressed_idb')
def compressed_idb():
    meadow_path_331108f = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'compressed', 'kernel32.idb')
    with meadow_idb.from_file(meadow_path_331108f) as meadow_db_a23b00f:
        yield meadow_db_a23b00f

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'compressed_i64')
def compressed_i64():
    meadow_path_d3cde45 = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'compressed', 'kernel32.i64')
    with meadow_idb.from_file(meadow_path_d3cde45) as meadow_db_2325c0c:
        yield meadow_db_2325c0c

@meadow_pytest.fixture
@_name_boundary.callable_contract({}, 'elf_idb')
def elf_idb():
    meadow_path_62f6a25 = _name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'elf', 'ls.idb')
    with meadow_idb.from_file(meadow_path_62f6a25) as meadow_db_d23b816:
        yield meadow_db_d23b816

@meadow_lru_cache(maxsize=64)
@_name_boundary.callable_contract({'path': 'meadow_path_83292d0'}, 'load_idb')
def meadow_load_idb(meadow_path_83292d0):
    with open(meadow_path_83292d0, 'rb') as meadow_f_75380d2:
        return meadow_idb.from_buffer(_name_boundary.attributes(meadow_f_75380d2)['read']())

@_name_boundary.callable_contract({'spec': 'meadow_spec_fa783ff'}, 'xfail')
def meadow_xfail(*meadow_spec_fa783ff):
    return ('xfail', meadow_spec_fa783ff)

@_name_boundary.callable_contract({'spec': 'meadow_spec_e3afac3'}, 'skip')
def meadow_skip(*meadow_spec_e3afac3):
    return ('skip', meadow_spec_e3afac3)

@_name_boundary.callable_contract({'spec': 'meadow_spec_11e4e17'}, 'if_exists')
def meadow_if_exists(*meadow_spec_11e4e17):
    return ('if_exists', meadow_spec_11e4e17)

@meadow_pytest.fixture
@_name_boundary.callable_contract({'request': 'meadow_request_8c2945e'}, 'runslow')
def runslow(meadow_request_8c2945e):
    return meadow_request_8c2945e.config.getoption('--runslow')

@meadow_pytest.fixture
@_name_boundary.callable_contract({'request': 'meadow_request_337a8de'}, 'rundebug')
def rundebug(meadow_request_337a8de):
    return meadow_request_337a8de.config.getoption('--rundebug')
meadow_VersionMap = {500: 'v5.0', 600: 'v6.0', 610: 'v6.1', 620: 'v6.2', 630: 'v6.3', 640: 'v6.4', 650: 'v6.5', 660: 'v6.6', 670: 'v6.7', 680: 'v6.8', 690: 'v6.9', 695: 'v6.95', 700: 'v7.0b', 710: 'v7.1', 720: 'v7.2', 730: 'v7.3', 740: 'v7.4', 750: 'v7.5', 760: 'v7.6'}
meadow_DefaultKern32Specs = [(500, 32, None), (630, 32, None), (630, 64, None), (640, 32, None), (640, 64, None), (650, 32, None), (650, 64, None), (660, 32, None), (660, 64, None), (670, 32, None), (670, 64, None), (680, 32, None), (680, 64, None), (695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None), (720, 32, None), (720, 64, None), (730, 32, None), (730, 64, None), (740, 32, None), (740, 64, None), (750, 32, None), (750, 64, None), (760, 32, None)]

@_name_boundary.callable_contract({'bitness': 'meadow_bitness_7231f35', 'version': 'meadow_version_local_5629a69'}, 'get_kern32_path')
def meadow_get_kern32_path(meadow_version_local_5629a69, meadow_bitness_7231f35):
    meadow_sversion_703c1d1 = meadow_VersionMap[meadow_version_local_5629a69] if meadow_version_local_5629a69 in meadow_VersionMap else str(meadow_version_local_5629a69)
    meadow_sbitness_6190c79, meadow_filename_e71eced = {32: ('x32', 'kernel32.idb'), 64: ('x64', 'kernel32.i64')}[meadow_bitness_7231f35]
    return (_name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', meadow_sversion_703c1d1, meadow_sbitness_6190c79, meadow_filename_e71eced), meadow_sversion_703c1d1, meadow_sbitness_6190c79)

@_name_boundary.callable_contract({'specs': 'meadow_specs_d34b669'}, 'kern32_test')
def meadow_kern32_test(meadow_specs_d34b669=None):
    """
    Example::

        @kern32_test([
                 (695, 32, 'bar'),
                 (695, 64, 'bar'),
            xfail(700, 32, 'bar'),
        ])
        def test_foo(kernel32_idb, version, bitness, expected):
            assert 'bar' == expected
    """
    if meadow_specs_d34b669 is None:
        meadow_specs_d34b669 = meadow_DefaultKern32Specs
    meadow_ids_a252034 = []
    meadow_params_c542467 = []
    for meadow_spec_a000336 in meadow_specs_d34b669:
        meadow_version_local_ac34bb6, meadow_bitness_399fa05, meadow_expected_acb20a2 = meadow_spec_a000336 if isinstance(meadow_spec_a000336[0], float) or isinstance(meadow_spec_a000336[0], int) else meadow_spec_a000336[1]
        meadow_path_372ed45, meadow_sversion_48323b4, meadow_sbitness_ed04f84 = meadow_get_kern32_path(meadow_version_local_ac34bb6, meadow_bitness_399fa05)
        meadow_skipped_23ac895 = False
        if meadow_spec_a000336[0] == 'xfail':
            meadow_marks_ed56a87 = meadow_pytest.mark.xfail
        elif meadow_spec_a000336[0] == 'skip':
            meadow_skipped_23ac895 = True
            meadow_marks_ed56a87 = meadow_pytest.mark.skip
        elif meadow_spec_a000336[0] == 'if_exists':
            meadow_skipped_23ac895 = not _name_boundary.attributes(meadow_os)['path'].exists(meadow_path_372ed45)
            meadow_marks_ed56a87 = meadow_pytest.mark.skipif(condition=meadow_skipped_23ac895, reason='not exists idb file: ' + meadow_path_372ed45)
        else:
            meadow_marks_ed56a87 = None
        meadow_db_5bc85dc = meadow_load_idb(meadow_path_372ed45) if not meadow_skipped_23ac895 else None
        if meadow_marks_ed56a87:
            meadow_params_c542467.append(meadow_pytest.param(meadow_db_5bc85dc, meadow_version_local_ac34bb6, meadow_bitness_399fa05, meadow_expected_acb20a2, marks=meadow_marks_ed56a87))
        else:
            meadow_params_c542467.append(meadow_pytest.param(meadow_db_5bc85dc, meadow_version_local_ac34bb6, meadow_bitness_399fa05, meadow_expected_acb20a2))
        meadow_ids_a252034.append(meadow_sversion_48323b4 + '/' + meadow_sbitness_ed04f84)
    return meadow_pytest.mark.parametrize('kernel32_idb,version,bitness,expected', meadow_params_c542467, ids=meadow_ids_a252034)

@_name_boundary.callable_contract({}, 'kern32_test_v7')
def meadow_kern32_test_v7():
    return meadow_kern32_test([(695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None), (720, 32, None), (720, 64, None), (730, 32, None), (730, 64, None)])
meadow_requires_capstone = meadow_pytest.mark.skipif(meadow_no_capstone, reason='capstone not installed')
_name_boundary.module_contract(globals(), {'kern32_test': 'meadow_kern32_test', 'DefaultKern32Specs': 'meadow_DefaultKern32Specs', 'load_idb': 'meadow_load_idb', 'CD': 'meadow_CD', 'pytest': 'meadow_pytest', 'get_kern32_path': 'meadow_get_kern32_path', 'os': 'meadow_os', 'if_exists': 'meadow_if_exists', 'xfail': 'meadow_xfail', 'VersionMap': 'meadow_VersionMap', 'six': 'meadow_six', 'requires_capstone': 'meadow_requires_capstone', 'idb': 'meadow_idb', 'skip': 'meadow_skip', 'kern32_test_v7': 'meadow_kern32_test_v7', 'lru_cache': 'meadow_lru_cache', 'capstone': 'meadow_capstone', 'no_capstone': 'meadow_no_capstone'})
