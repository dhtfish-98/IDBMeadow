# Derived from tests/test_issue22.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os.path as _boundary_import_os_path
import os as meadow_os
import idbmeadow as meadow_idb

@_name_boundary.callable_contract({}, 'test_issue22')
def meadow_test_issue22():
    """
    demonstrate that functions found at addresses with the high bit set are no problem.
    see github issue #22 for the backstory.
    """
    meadow_cd_80b3f2f = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_496083c = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_80b3f2f, 'data', 'highaddr', 'highaddr.idb')
    with meadow_idb.from_file(meadow_idbpath_496083c) as meadow_db_eae43af:
        meadow_api_local_60aa752 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_eae43af)
        assert len(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_60aa752)['idautils'])['Functions']()) == 1
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_60aa752)['idautils'])['Functions']()[0] == 4160749567
_name_boundary.module_contract(globals(), {'test_issue22': 'meadow_test_issue22', 'os': 'meadow_os', 'idb': 'meadow_idb'})
