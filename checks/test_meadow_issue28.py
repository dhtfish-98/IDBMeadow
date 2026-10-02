# Derived from tests/test_issue28.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os.path as _boundary_import_os_path
import os as meadow_os
import idbmeadow as meadow_idb

@_name_boundary.callable_contract({}, 'test_issue28')
def meadow_test_issue28():
    """
    demonstrate parsing of section metadata.
    see github issue #28 for the backstory.
    """
    meadow_cd_c601e35 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_af2a0af = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_c601e35, 'data', 'elf', 'cat.i64')
    with meadow_idb.from_file(meadow_idbpath_af2a0af) as meadow_db_25a7248:
        meadow_api_local_49eae0c = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_25a7248)
        assert [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] == [_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_49eae0c)['idc'])['GetSegmentAttr'](meadow_s_local_32a6b81, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_49eae0c)['idc'])['SEGATTR_BITNESS']) for meadow_s_local_32a6b81 in _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_49eae0c)['idautils'])['Segments']()]
_name_boundary.module_contract(globals(), {'os': 'meadow_os', 'idb': 'meadow_idb', 'test_issue28': 'meadow_test_issue28'})
