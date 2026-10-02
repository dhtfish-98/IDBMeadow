# Derived from tests/test_netnode.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
from checks.fixture_registry import *
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
meadow_debug = meadow_pytest.mark.skipif(not rundebug, reason='need --rundebug option to run')
meadow_ROOT_NODEID = 'Root Node'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_4b8d3d8', 'expected': 'meadow_expected_4e6920b', 'kernel32_idb': 'meadow_kernel32_idb_local_0c7282f', 'version': 'meadow_version_local_ca141c1'}, 'test_name')
def meadow_test_name(meadow_kernel32_idb_local_0c7282f, meadow_version_local_ca141c1, meadow_bitness_4b8d3d8, meadow_expected_4e6920b):
    meadow_root_8fd79c8 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_0c7282f, meadow_ROOT_NODEID)
    assert meadow_root_8fd79c8.name() == meadow_ROOT_NODEID
    meadow_nn_397efed = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_0c7282f, 4198400)
    with meadow_pytest.raises(KeyError):
        meadow___2116cac = meadow_nn_397efed.name()

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_89a3386', 'expected': 'meadow_expected_dae9150', 'kernel32_idb': 'meadow_kernel32_idb_local_122cafb', 'version': 'meadow_version_local_e2ac207'}, 'test_valobj')
def meadow_test_valobj(meadow_kernel32_idb_local_122cafb, meadow_version_local_e2ac207, meadow_bitness_89a3386, meadow_expected_dae9150):
    meadow_root_44a8f80 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_122cafb, meadow_ROOT_NODEID)
    assert _name_boundary.attributes(meadow_root_44a8f80)['value_exists']() is True
    if meadow_version_local_e2ac207 == 760:
        assert _name_boundary.attributes(meadow_root_44a8f80)['valobj']().endswith(b'00bf1bf1b779ce1af41371426821e0c2\x00')
        assert _name_boundary.attributes(meadow_root_44a8f80)['valstr']().endswith('00bf1bf1b779ce1af41371426821e0c2')
    elif 740 <= meadow_version_local_e2ac207 < 760 or meadow_version_local_e2ac207 == 500:
        assert _name_boundary.attributes(meadow_root_44a8f80)['valobj']().endswith(b'ba1bc09b7bb290656582b4e4d896105caf00825b557ce45621e76741cd5dc262\x00')
        assert _name_boundary.attributes(meadow_root_44a8f80)['valstr']().endswith('ba1bc09b7bb290656582b4e4d896105caf00825b557ce45621e76741cd5dc262')
    else:
        assert _name_boundary.attributes(meadow_root_44a8f80)['valobj']().endswith(b'kernel32.dll\x00')
        assert _name_boundary.attributes(meadow_root_44a8f80)['valstr']().endswith('kernel32.dll')

@meadow_kern32_test([(695, 32, [1, 2, 65, 66, 1300, 1301, 1302, 1303, 1305, 1349, 4307348]), (695, 64, [1, 2, 65, 66, 1300, 1301, 1302, 1303, 1305, 1349, 4307348]), (700, 32, [1, 2, 65, 66, 1300, 1301, 1302, 1303, 1305, 1349, 1352, 4307348]), (700, 64, [1, 2, 65, 66, 1300, 1301, 1302, 1303, 1305, 1349, 1352, 4307348])])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_4f7c853', 'expected': 'meadow_expected_4c9d000', 'kernel32_idb': 'meadow_kernel32_idb_local_dbb693a', 'version': 'meadow_version_local_fde76ef'}, 'test_sups')
def meadow_test_sups(meadow_kernel32_idb_local_dbb693a, meadow_version_local_fde76ef, meadow_bitness_4f7c853, meadow_expected_4c9d000):
    meadow_root_19b0f62 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_dbb693a, meadow_ROOT_NODEID)
    assert list(_name_boundary.attributes(meadow_root_19b0f62)['sups']()) == meadow_expected_4c9d000

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_8d2e3b3', 'expected': 'meadow_expected_1ad7e45', 'kernel32_idb': 'meadow_kernel32_idb_local_056eb78', 'version': 'meadow_version_local_7f553d8'}, 'test_alts')
def meadow_test_alts(meadow_kernel32_idb_local_056eb78, meadow_version_local_7f553d8, meadow_bitness_8d2e3b3, meadow_expected_1ad7e45):
    meadow_root_9a9d8b6 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_056eb78, meadow_ROOT_NODEID)
    meadow_uint_local_76343d8 = meadow_kernel32_idb_local_056eb78.uint
    meadow_alts_8a5e624 = list(_name_boundary.attributes(meadow_root_9a9d8b6)['alts']())
    if meadow_version_local_7f553d8 > 680:
        assert meadow_alts_8a5e624 == [meadow_uint_local_76343d8(-8), meadow_uint_local_76343d8(-6), meadow_uint_local_76343d8(-5), meadow_uint_local_76343d8(-4), meadow_uint_local_76343d8(-3), meadow_uint_local_76343d8(-2), meadow_uint_local_76343d8(-1)]
    elif meadow_version_local_7f553d8 >= 630:
        assert meadow_alts_8a5e624 == [meadow_uint_local_76343d8(-6), meadow_uint_local_76343d8(-5), meadow_uint_local_76343d8(-4), meadow_uint_local_76343d8(-3), meadow_uint_local_76343d8(-2), meadow_uint_local_76343d8(-1)]
    else:
        assert meadow_alts_8a5e624 == [meadow_uint_local_76343d8(-5), meadow_uint_local_76343d8(-4), meadow_uint_local_76343d8(-3), meadow_uint_local_76343d8(-2), meadow_uint_local_76343d8(-1)]

@_name_boundary.callable_contract({'small_idb': 'meadow_small_idb_local_d8e9a27'}, 'test_small')
def meadow_test_small(meadow_small_idb_local_d8e9a27):
    meadow_root_e09ad07 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_small_idb_local_d8e9a27, meadow_ROOT_NODEID)
    meadow_uint32_b36332d = meadow_small_idb_local_d8e9a27.uint
    assert list(_name_boundary.attributes(meadow_root_e09ad07)['alts']()) == [meadow_uint32_b36332d(-8), meadow_uint32_b36332d(-5), meadow_uint32_b36332d(-4), meadow_uint32_b36332d(-3), meadow_uint32_b36332d(-2), meadow_uint32_b36332d(-1)]
_name_boundary.module_contract(globals(), {'ROOT_NODEID': 'meadow_ROOT_NODEID', 'idb': 'meadow_idb', 'debug': 'meadow_debug', 'test_valobj': 'meadow_test_valobj', 'test_small': 'meadow_test_small', 'test_name': 'meadow_test_name', 'test_alts': 'meadow_test_alts', 'test_sups': 'meadow_test_sups'})
