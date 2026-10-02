# Derived from tests/test_issue29.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os.path as _boundary_import_os_path
import os as meadow_os
import idbmeadow as meadow_idb

@_name_boundary.callable_contract({}, 'test_issue29')
def meadow_test_issue29():
    """
    demonstrate GetManyBytes can retrieve the entire .text section
    see github issue #29 for the backstory.
    """
    meadow_cd_6912a1e = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_de29d11 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_6912a1e, 'data', 'issue29', 'issue29.i64')
    with meadow_idb.from_file(meadow_idbpath_de29d11) as meadow_db_d5b4e9f:
        meadow_api_local_22a51ce = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_d5b4e9f)
        meadow_seg_local_8481923 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['FirstSeg']()
        while meadow_seg_local_8481923 != _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['BADADDR']:
            meadow_name_local_f747e67 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['SegName'](meadow_seg_local_8481923)
            meadow_start_local_9103a12 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['SegStart'](meadow_seg_local_8481923)
            meadow_end_local_d9b53c0 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['SegEnd'](meadow_seg_local_8481923)
            if meadow_name_local_f747e67 == '.text':
                meadow_textBytes_0f1a13a = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['GetManyBytes'](meadow_start_local_9103a12, meadow_end_local_d9b53c0 - meadow_start_local_9103a12)
                assert len(meadow_textBytes_0f1a13a) == meadow_end_local_d9b53c0 - meadow_start_local_9103a12
            meadow_seg_local_8481923 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_22a51ce)['idc'])['NextSeg'](meadow_seg_local_8481923)
_name_boundary.module_contract(globals(), {'os': 'meadow_os', 'idb': 'meadow_idb', 'test_issue29': 'meadow_test_issue29'})
