# Derived from tests/test_multiarch_disasm.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import os.path as _boundary_import_os_path
import os as meadow_os
from checks.fixture_registry import *
import idbmeadow as meadow_idb

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_armel_disasm')
def meadow_test_armel_disasm():
    meadow_cd_3a4b55a = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_99c6d25 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_3a4b55a, 'data', 'armel', 'ls.idb')
    with meadow_idb.from_file(meadow_idbpath_99c6d25) as meadow_db_18edba5:
        meadow_api_local_75a3280 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_18edba5)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_75a3280)['idc'])['GetDisasm'](9624) == 'push\t{r4, r5, r6, r7, r8, sb, sl, fp, lr}'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_75a3280)['idc'])['GetDisasm'](73744) == 'b\t#0x12014'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_thumb_disasm')
def meadow_test_thumb_disasm():
    meadow_cd_5504f00 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_829d2c5 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_5504f00, 'data', 'thumb', 'ls.idb')
    with meadow_idb.from_file(meadow_idbpath_829d2c5) as meadow_db_5494b42:
        meadow_api_local_46870e5 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_5494b42)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_46870e5)['idc'])['GetDisasm'](73388) == 'strb\tr4, [r3, r5]'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_46870e5)['idc'])['GetDisasm'](73390) == 'b\t#0x11ebc'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_arm64_disasm')
def meadow_test_arm64_disasm():
    meadow_cd_6e01fe9 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_61c709f = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_6e01fe9, 'data', 'arm64', 'ls.i64')
    with meadow_idb.from_file(meadow_idbpath_61c709f) as meadow_db_d8df945:
        meadow_api_local_8be1ce4 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_d8df945)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8be1ce4)['idc'])['GetDisasm'](23856) == 'cmp\tw5, #0x74'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8be1ce4)['idc'])['GetDisasm'](23860) == 'csel\tw5, w5, w12, ne'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8be1ce4)['idc'])['GetDisasm'](23864) == 'b\t#0x5c30'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_mips_disasm')
def meadow_test_mips_disasm():
    meadow_cd_cc73b54 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_810c57b = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_cc73b54, 'data', 'mips', 'ls.idb')
    with meadow_idb.from_file(meadow_idbpath_810c57b) as meadow_db_e628794:
        meadow_api_local_d1d2ba0 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_e628794)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d1d2ba0)['idc'])['GetDisasm'](21568) == 'sb\t$t2, ($t1)'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d1d2ba0)['idc'])['GetDisasm'](21572) == 'addiu\t$t3, $t3, 1'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d1d2ba0)['idc'])['GetDisasm'](21576) == 'b\t0x523c'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_mipsel_disasm')
def meadow_test_mipsel_disasm():
    meadow_cd_d68f288 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_233c64c = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_d68f288, 'data', 'mipsel', 'ls.idb')
    with meadow_idb.from_file(meadow_idbpath_233c64c) as meadow_db_4d5129d:
        meadow_api_local_838c052 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_4d5129d)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_838c052)['idc'])['GetDisasm'](21564) == 'sb\t$t2, ($t1)'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_838c052)['idc'])['GetDisasm'](21568) == 'addiu\t$t3, $t3, 1'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_838c052)['idc'])['GetDisasm'](21572) == 'b\t0x5238'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_mips64el_disasm')
def meadow_test_mips64el_disasm():
    meadow_cd_4d174d1 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_4aa8dba = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_4d174d1, 'data', 'mips64el', 'ls.i64')
    with meadow_idb.from_file(meadow_idbpath_4aa8dba) as meadow_db_0de1db9:
        meadow_api_local_be192a6 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_0de1db9)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_be192a6)['idc'])['GetDisasm'](47304) == 'addiu\t$s0, $s0, -0x57'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_be192a6)['idc'])['GetDisasm'](47308) == 'daddiu\t$v1, $v1, 1'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_be192a6)['idc'])['GetDisasm'](47312) == 'b\t0xb760'
_name_boundary.module_contract(globals(), {'test_armel_disasm': 'meadow_test_armel_disasm', 'test_mipsel_disasm': 'meadow_test_mipsel_disasm', 'idb': 'meadow_idb', 'test_mips64el_disasm': 'meadow_test_mips64el_disasm', 'test_mips_disasm': 'meadow_test_mips_disasm', 'test_arm64_disasm': 'meadow_test_arm64_disasm', 'test_thumb_disasm': 'meadow_test_thumb_disasm', 'os': 'meadow_os'})
