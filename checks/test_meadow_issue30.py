# Derived from tests/test_issue30.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os.path as _boundary_import_os_path
import os as meadow_os
import idbmeadow as meadow_idb

@_name_boundary.callable_contract({}, 'test_issue30')
def meadow_test_issue30():
    """
    demonstrate get_func_cmt().
    see github issue #30 for the backstory.
    """
    meadow_cd_ac08f8a = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_cd61608 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_ac08f8a, 'data', 'issue30', 'issue30.i64')
    with meadow_idb.from_file(meadow_idbpath_cd61608) as meadow_db_61d116b:
        meadow_api_local_b8f25c2 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_61d116b)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_b8f25c2)['idc'])['GetCommentEx'](4199832, 0) == 'local cmt'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_b8f25c2)['idc'])['GetCommentEx'](4199832, 1) == ''
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_b8f25c2)['ida_funcs'])['get_func_cmt'](4199832, 0) == 'rep cmt'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_b8f25c2)['ida_funcs'])['get_func_cmt'](4199832, 1) == 'rep cmt'
_name_boundary.module_contract(globals(), {'test_issue30': 'meadow_test_issue30', 'os': 'meadow_os', 'idb': 'meadow_idb'})
