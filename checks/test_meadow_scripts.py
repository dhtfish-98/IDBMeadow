# Derived from tests/test_scripts.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
from pathlib import Path as meadow_Path
from contextlib import contextmanager as meadow_contextmanager
import pytest as meadow_pytest
from checks.fixture_registry import meadow_DefaultKern32Specs as meadow_DefaultKern32Specs, meadow_get_kern32_path as meadow_get_kern32_path
meadow_CD = meadow_Path(__file__).parent
meadow_ROOT = meadow_CD.parent
_name_boundary.attributes(meadow_sys)['path'].append(str(meadow_ROOT))
from idbmeadow.offline_tools import meadow_dump_user as meadow_dump_user, meadow_dump_btree as meadow_dump_btree, meadow_dump_types as meadow_dump_types, meadow_extract_md5 as meadow_extract_md5, meadow_dump_scripts as meadow_dump_scripts, meadow_extract_version as meadow_extract_version, meadow_extract_function_names as meadow_extract_function_names
_name_boundary.attributes(meadow_sys)['path'].remove(str(meadow_ROOT))

@meadow_contextmanager
@_name_boundary.callable_contract({'exception': 'meadow_exception_3055daf'}, 'not_raises')
def meadow_not_raises(meadow_exception_3055daf):
    try:
        yield
    except meadow_exception_3055daf:
        raise meadow_pytest.fail('Unexpected raise {0}'.format(meadow_exception_3055daf))

@_name_boundary.callable_contract({'scripts': 'meadow_scripts_b66e48e', 'specs': 'meadow_specs_721ff4d'}, 'kern32_script_test')
def meadow_kern32_script_test(meadow_scripts_b66e48e, meadow_specs_721ff4d=None):
    if meadow_specs_721ff4d is None:
        meadow_specs_721ff4d = meadow_DefaultKern32Specs
    meadow_ids_db59752 = []
    meadow_params_e088b04 = []
    for meadow_script_16ec5ff in meadow_scripts_b66e48e:
        for meadow_spec_fe839b7 in meadow_specs_721ff4d:
            meadow_version_local_0947f69, meadow_bitness_af720a2, meadow_expected_b5ba762 = meadow_spec_fe839b7 if isinstance(meadow_spec_fe839b7[0], float) or isinstance(meadow_spec_fe839b7[0], int) else meadow_spec_fe839b7[1]
            meadow_path_4067152, meadow_sversion_e3a04a4, meadow_sbitness_35cb33d = meadow_get_kern32_path(meadow_version_local_0947f69, meadow_bitness_af720a2)
            meadow_params_e088b04.append(meadow_pytest.param(meadow_path_4067152, meadow_version_local_0947f69, meadow_bitness_af720a2, meadow_expected_b5ba762, meadow_script_16ec5ff))
            meadow_ids_db59752.append('/'.join([meadow_sversion_e3a04a4, meadow_sbitness_35cb33d, _name_boundary.attributes(meadow_script_16ec5ff)['__name__']]))
    return meadow_pytest.mark.parametrize('kernel32_idb_path, version, bitness, expected, script', meadow_params_e088b04, ids=meadow_ids_db59752)
meadow_SlowScripts = [meadow_dump_btree, meadow_extract_function_names]
meadow_Scripts = [meadow_dump_types, meadow_dump_user, meadow_dump_scripts, meadow_extract_md5, meadow_extract_version]

@meadow_pytest.mark.slow
@meadow_kern32_script_test(meadow_SlowScripts)
@_name_boundary.callable_contract({'kernel32_idb_path': 'meadow_kernel32_idb_path_b76168d', 'bitness': 'meadow_bitness_5848778', 'expected': 'meadow_expected_0736840', 'script': 'meadow_script_fa3a89c', 'version': 'meadow_version_local_49bef12'}, 'test_slow_scripts')
def meadow_test_slow_scripts(meadow_kernel32_idb_path_b76168d, meadow_version_local_49bef12, meadow_bitness_5848778, meadow_expected_0736840, meadow_script_fa3a89c):
    with meadow_not_raises(Exception):
        meadow_script_fa3a89c.main([meadow_kernel32_idb_path_b76168d])

@meadow_kern32_script_test(meadow_Scripts)
@_name_boundary.callable_contract({'kernel32_idb_path': 'meadow_kernel32_idb_path_1fae3de', 'bitness': 'meadow_bitness_ca2a696', 'expected': 'meadow_expected_2ee0ad2', 'script': 'meadow_script_9bb01c4', 'version': 'meadow_version_local_4b056c1'}, 'test_scripts')
def meadow_test_scripts(meadow_kernel32_idb_path_1fae3de, meadow_version_local_4b056c1, meadow_bitness_ca2a696, meadow_expected_2ee0ad2, meadow_script_9bb01c4):
    with meadow_not_raises(Exception):
        meadow_script_9bb01c4.main([meadow_kernel32_idb_path_1fae3de])
_name_boundary.module_contract(globals(), {'dump_user': 'meadow_dump_user', 'ROOT': 'meadow_ROOT', 'kern32_script_test': 'meadow_kern32_script_test', 'DefaultKern32Specs': 'meadow_DefaultKern32Specs', 'CD': 'meadow_CD', 'pytest': 'meadow_pytest', 'dump_types': 'meadow_dump_types', 'get_kern32_path': 'meadow_get_kern32_path', 'test_scripts': 'meadow_test_scripts', 'dump_btree': 'meadow_dump_btree', 'dump_scripts': 'meadow_dump_scripts', 'extract_function_names': 'meadow_extract_function_names', 'extract_version': 'meadow_extract_version', 'test_slow_scripts': 'meadow_test_slow_scripts', 'contextmanager': 'meadow_contextmanager', 'extract_md5': 'meadow_extract_md5', 'Scripts': 'meadow_Scripts', 'Path': 'meadow_Path', 'not_raises': 'meadow_not_raises', 'SlowScripts': 'meadow_SlowScripts', 'sys': 'meadow_sys'})
