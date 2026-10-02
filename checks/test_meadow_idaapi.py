# Derived from tests/test_idaapi.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
from checks.fixture_registry import *

@_name_boundary.callable_contract({'prop': 'meadow_prop_6d1f0aa', 's': 'meadow_s_local_6675efc'}, 'pluck')
def meadow_pluck(meadow_prop_6d1f0aa, meadow_s_local_6675efc):
    """
    generate the values from the given attribute with name `prop` from the given sequence of items `s`.

    Args:
      prop (str): the name of an attribute.
      s (sequnce): a bunch of objects.

    Yields:
      any: the values of the requested field across the sequence
    """
    for meadow_x_201ad9f in meadow_s_local_6675efc:
        yield _name_boundary.read_attribute(meadow_x_201ad9f, meadow_prop_6d1f0aa)

@_name_boundary.callable_contract({'prop': 'meadow_prop_e3fc16b', 's': 'meadow_s_local_bfdf472'}, 'lpluck')
def meadow_lpluck(meadow_prop_e3fc16b, meadow_s_local_bfdf472):
    """
    like `pluck`, but returns the result in a single list.
    """
    return list(meadow_pluck(meadow_prop_e3fc16b, meadow_s_local_bfdf472))

@_name_boundary.callable_contract({}, 'kern32_test_gt_v640')
def meadow_kern32_test_gt_v640():
    return meadow_kern32_test([(650, 32, None), (650, 64, None), (660, 32, None), (660, 64, None), (670, 32, None), (670, 64, None), (680, 32, None), (680, 64, None), (695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None), (720, 32, None), (720, 64, None), (730, 32, None), (730, 64, None)])

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_0fbf915', 'expected': 'meadow_expected_0dfd1a0', 'kernel32_idb': 'meadow_kernel32_idb_local_7caced7', 'version': 'meadow_version_local_d1017e1'}, 'test_heads')
def meadow_test_heads(meadow_kernel32_idb_local_7caced7, meadow_version_local_d1017e1, meadow_bitness_0fbf915, meadow_expected_0dfd1a0):
    meadow_idc_0ae5420 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_7caced7))['idc']
    meadow_first_ea_337b8b9 = 1754271760
    assert _name_boundary.attributes(meadow_idc_0ae5420)['Head'](meadow_first_ea_337b8b9) == 1754271760
    assert _name_boundary.attributes(meadow_idc_0ae5420)['Head'](meadow_first_ea_337b8b9 + 1) == 1754271760
    assert _name_boundary.attributes(meadow_idc_0ae5420)['NextHead'](meadow_first_ea_337b8b9) == 1754271762
    assert _name_boundary.attributes(meadow_idc_0ae5420)['PrevHead'](meadow_first_ea_337b8b9 + 2) == meadow_first_ea_337b8b9

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_87ab5ed', 'expected': 'meadow_expected_4b05624', 'kernel32_idb': 'meadow_kernel32_idb_local_2e88c92', 'version': 'meadow_version_local_0f0ecd0'}, 'test_bytes')
def meadow_test_bytes(meadow_kernel32_idb_local_2e88c92, meadow_version_local_0f0ecd0, meadow_bitness_87ab5ed, meadow_expected_4b05624):
    meadow_idc_f1bda14 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2e88c92))['idc']
    meadow_flags_local_1393b72 = _name_boundary.attributes(meadow_idc_f1bda14)['GetFlags'](1754271760)
    assert _name_boundary.attributes(meadow_idc_f1bda14)['hasValue'](meadow_flags_local_1393b72) is True
    meadow_byte_ebc8c96 = _name_boundary.attributes(meadow_idc_f1bda14)['IdbByte'](1754271760)
    assert meadow_byte_ebc8c96 == 139
    assert not _name_boundary.attributes(meadow_idc_f1bda14)['GetFlags'](2290649224)
    assert _name_boundary.attributes(meadow_idc_f1bda14)['ItemSize'](1754271760) == 2
    assert _name_boundary.attributes(meadow_idc_f1bda14)['ItemSize'](1754271761) == 1
    assert _name_boundary.attributes(meadow_idc_f1bda14)['ItemSize'](1754271762) == 1
    assert _name_boundary.attributes(meadow_idc_f1bda14)['GetManyBytes'](1754271760, 3) == b'\x8b\xffU'

@_name_boundary.callable_contract({'elf_idb': 'meadow_elf_idb_local_01b20e2'}, 'test_bytes_2')
def meadow_test_bytes_2(meadow_elf_idb_local_01b20e2):
    """
    Demonstrate issue reported as #12.
    Thanks to @binoopang.

    This exercises fetching of flags/bytes from a segment that is not the first.
    """
    meadow_api_local_a23d55d = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_elf_idb_local_01b20e2)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a23d55d)['idc'])['GetManyBytes'](134520304, 16) == b'\x8dL$\x04\x83\xe4\xf0\xffq\xfcU\x89\xe5WVS'

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a8bbcb6', 'expected': 'meadow_expected_821d141', 'kernel32_idb': 'meadow_kernel32_idb_local_f598faf', 'version': 'meadow_version_local_75aa7b0'}, 'test_state')
def meadow_test_state(meadow_kernel32_idb_local_f598faf, meadow_version_local_75aa7b0, meadow_bitness_a8bbcb6, meadow_expected_821d141):
    meadow_idc_debc863 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f598faf))['idc']
    meadow_ida_bytes_1dfbfb2 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f598faf))['ida_bytes']
    meadow_flags_local_30daa36 = _name_boundary.attributes(meadow_idc_debc863)['GetFlags'](1754271760)
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_code'](meadow_flags_local_30daa36) is True
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_data'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_tail'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_not_tail'](meadow_flags_local_30daa36) is True
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_unknown'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_head'](meadow_flags_local_30daa36) is True
    meadow_flags_local_30daa36 = _name_boundary.attributes(meadow_idc_debc863)['GetFlags'](1754271761)
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_code'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_data'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_tail'](meadow_flags_local_30daa36) is True
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_not_tail'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_unknown'](meadow_flags_local_30daa36) is False
    assert _name_boundary.attributes(meadow_ida_bytes_1dfbfb2)['is_head'](meadow_flags_local_30daa36) is False

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_0e3bc14', 'expected': 'meadow_expected_705b07f', 'kernel32_idb': 'meadow_kernel32_idb_local_2c53053', 'version': 'meadow_version_local_46b3750'}, 'test_specific_state')
def meadow_test_specific_state(meadow_kernel32_idb_local_2c53053, meadow_version_local_46b3750, meadow_bitness_0e3bc14, meadow_expected_705b07f):
    meadow_idc_173663d = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2c53053))['idc']
    meadow_ida_bytes_d543a55 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2c53053))['ida_bytes']
    meadow_flags_local_96510cc = _name_boundary.attributes(meadow_idc_173663d)['GetFlags'](1754271760)
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['is_flow'](meadow_flags_local_96510cc) is False
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['is_var'](meadow_flags_local_96510cc) is False
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_extra_cmts'](meadow_flags_local_96510cc) is True
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_cmt'](meadow_flags_local_96510cc) is False
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_ref'](meadow_flags_local_96510cc) is True
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_name'](meadow_flags_local_96510cc) is True
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_dummy_name'](meadow_flags_local_96510cc) is False
    meadow_flags_local_96510cc = _name_boundary.attributes(meadow_idc_173663d)['GetFlags'](1754271812)
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['is_flow'](meadow_flags_local_96510cc) is True
    assert _name_boundary.attributes(meadow_ida_bytes_d543a55)['has_cmt'](meadow_flags_local_96510cc) is True

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_0fea5f9', 'expected': 'meadow_expected_d5b3e18', 'kernel32_idb': 'meadow_kernel32_idb_local_f107217', 'version': 'meadow_version_local_d699125'}, 'test_code')
def meadow_test_code(meadow_kernel32_idb_local_f107217, meadow_version_local_d699125, meadow_bitness_0fea5f9, meadow_expected_d5b3e18):
    meadow_idc_21683b9 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f107217))['idc']
    meadow_ida_bytes_9fcac35 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f107217))['ida_bytes']
    meadow_flags_local_dca031e = _name_boundary.attributes(meadow_idc_21683b9)['GetFlags'](1754271760)
    assert _name_boundary.attributes(meadow_ida_bytes_9fcac35)['is_func'](meadow_flags_local_dca031e) is True
    assert _name_boundary.attributes(meadow_ida_bytes_9fcac35)['has_immd'](meadow_flags_local_dca031e) is False
    meadow_flags_local_dca031e = _name_boundary.attributes(meadow_idc_21683b9)['GetFlags'](1754271762)
    assert _name_boundary.attributes(meadow_ida_bytes_9fcac35)['is_func'](meadow_flags_local_dca031e) is False
    assert _name_boundary.attributes(meadow_ida_bytes_9fcac35)['has_immd'](meadow_flags_local_dca031e) is False

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_b5cc7bd', 'expected': 'meadow_expected_49832e6', 'kernel32_idb': 'meadow_kernel32_idb_local_f39a250', 'version': 'meadow_version_local_f8b844f'}, 'test_data')
def meadow_test_data(meadow_kernel32_idb_local_f39a250, meadow_version_local_f8b844f, meadow_bitness_b5cc7bd, meadow_expected_49832e6):
    meadow_idc_fedd54a = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f39a250))['idc']
    meadow_ida_bytes_2279997 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_f39a250))['ida_bytes']
    meadow_flags_local_15f2883 = _name_boundary.attributes(meadow_idc_fedd54a)['GetFlags'](1754272235)
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_byte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_word'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_dword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_qword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_oword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_yword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_tbyte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_float'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_double'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_pack_real'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_strlit'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_struct'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_align'](meadow_flags_local_15f2883) is True
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_custom'](meadow_flags_local_15f2883) is False
    meadow_flags_local_15f2883 = _name_boundary.attributes(meadow_idc_fedd54a)['GetFlags'](1754272919)
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_byte'](meadow_flags_local_15f2883) is True
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_word'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_dword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_qword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_oword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_yword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_tbyte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_float'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_double'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_pack_real'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_strlit'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_struct'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_align'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_custom'](meadow_flags_local_15f2883) is False
    meadow_flags_local_15f2883 = _name_boundary.attributes(meadow_idc_fedd54a)['GetFlags'](1754507196)
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_byte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_word'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_dword'](meadow_flags_local_15f2883) is True
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_qword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_oword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_yword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_tbyte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_float'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_double'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_pack_real'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_strlit'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_struct'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_align'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_custom'](meadow_flags_local_15f2883) is False
    meadow_flags_local_15f2883 = _name_boundary.attributes(meadow_idc_fedd54a)['GetFlags'](1754507328)
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_byte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_word'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_dword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_qword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_oword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_yword'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_tbyte'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_float'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_double'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_pack_real'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_strlit'](meadow_flags_local_15f2883) is True
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_struct'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_align'](meadow_flags_local_15f2883) is False
    assert _name_boundary.attributes(meadow_ida_bytes_2279997)['is_custom'](meadow_flags_local_15f2883) is False

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_3bfe31d', 'expected': 'meadow_expected_0e4ac99', 'kernel32_idb': 'meadow_kernel32_idb_local_3480893', 'version': 'meadow_version_local_565185e'}, 'test_function_name')
def meadow_test_function_name(meadow_kernel32_idb_local_3480893, meadow_version_local_565185e, meadow_bitness_3bfe31d, meadow_expected_0e4ac99):
    meadow_api_local_2b5c853 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_3480893)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_2b5c853)['idc'])['GetFunctionName'](1754273429) == 'DllEntryPoint' if meadow_version_local_565185e <= 700 else '_BaseDllInitialize@12'

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_d9c5268', 'expected': 'meadow_expected_e653916', 'kernel32_idb': 'meadow_kernel32_idb_local_fa5e5ad', 'version': 'meadow_version_local_5a87870'}, 'test_operand_types')
def meadow_test_operand_types(meadow_kernel32_idb_local_fa5e5ad, meadow_version_local_5a87870, meadow_bitness_d9c5268, meadow_expected_e653916):
    meadow_idc_54cc0c0 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_fa5e5ad))['idc']
    meadow_flags_local_0f97452 = _name_boundary.attributes(meadow_idc_54cc0c0)['GetFlags'](1754271762)
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isOff0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isChar0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isSeg0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isEnum0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStroff0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStkvar0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isFloat0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isCustFmt0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isNum0'](meadow_flags_local_0f97452) is False
    meadow_flags_local_0f97452 = _name_boundary.attributes(meadow_idc_54cc0c0)['GetFlags'](1754271771)
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg1'](meadow_flags_local_0f97452) is True
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isOff1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isChar1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isSeg1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isEnum1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStroff1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStkvar1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isFloat1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isCustFmt1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isNum1'](meadow_flags_local_0f97452) is True
    meadow_flags_local_0f97452 = _name_boundary.attributes(meadow_idc_54cc0c0)['GetFlags'](1754274148)
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg0'](meadow_flags_local_0f97452) is True
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isDefArg1'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isOff0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isChar0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isSeg0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isEnum0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStroff0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isStkvar0'](meadow_flags_local_0f97452) is True
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isFloat0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isCustFmt0'](meadow_flags_local_0f97452) is False
    assert _name_boundary.attributes(meadow_idc_54cc0c0)['isNum0'](meadow_flags_local_0f97452) is False

@_name_boundary.callable_contract({'small_idb': 'meadow_small_idb_local_fce014f'}, 'test_colors')
def meadow_test_colors(meadow_small_idb_local_fce014f):
    meadow_api_local_a3ecaf6 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_small_idb_local_fce014f)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a3ecaf6)['ida_nalt'])['is_colored_item'](0) is True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a3ecaf6)['idc'])['GetColor'](0, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a3ecaf6)['idc'])['CIC_ITEM']) == 8947848

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_37001b3', 'expected': 'meadow_expected_2003859', 'kernel32_idb': 'meadow_kernel32_idb_local_b190267', 'version': 'meadow_version_local_f040d15'}, 'test_func_t')
def meadow_test_func_t(meadow_kernel32_idb_local_b190267, meadow_version_local_f040d15, meadow_bitness_37001b3, meadow_expected_2003859):
    meadow_api_local_99452d6 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_b190267)
    meadow_DllEntryPoint_478f6ff = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['get_func'](1754273429)
    assert _name_boundary.attributes(meadow_DllEntryPoint_478f6ff)['startEA'] == 1754273429
    assert _name_boundary.attributes(meadow_DllEntryPoint_478f6ff)['endEA'] == 1754273456
    assert _name_boundary.attributes(meadow_DllEntryPoint_478f6ff)['frsize'] == 0
    assert _name_boundary.attributes(meadow_DllEntryPoint_478f6ff)['frregs'] == 4
    assert _name_boundary.attributes(meadow_DllEntryPoint_478f6ff)['argsize'] == 12
    meadow_flags_local_9de8f01 = meadow_DllEntryPoint_478f6ff.flags
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_NORET']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_FAR']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_LIB']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_STATICDEF']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_FRAME']) is True
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_USERFAR']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_HIDDEN']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_THUNK']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_BOTTOMBP']) is False
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_NORET_PENDING']) is False
    if meadow_version_local_f040d15 > 500:
        assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_SP_READY']) is True
        assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_PURGED_OK']) is True
    assert _name_boundary.attributes(meadow_idb)['idapython'].is_flag_set(meadow_flags_local_9de8f01, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['FUNC_TAIL']) is False
    assert _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['get_func'](1754273429 + 1))['startEA'] == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['get_func'](1754292566))['startEA'] == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_99452d6)['ida_funcs'])['get_func'](1754292566 + 1))['startEA'] == 1754273429

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_6e8f4fc', 'expected': 'meadow_expected_4c76a56', 'kernel32_idb': 'meadow_kernel32_idb_local_38b7602', 'version': 'meadow_version_local_1523310'}, 'test_find_bb_end')
def meadow_test_find_bb_end(meadow_kernel32_idb_local_38b7602, meadow_version_local_1523310, meadow_bitness_6e8f4fc, meadow_expected_4c76a56):
    meadow_api_local_71091fc = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_38b7602)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273429) == 1754273438
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273431) == 1754273438
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273432) == 1754273438
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273434) == 1754273438
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273438) == 1754273438
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754292775) == 1754292775
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_71091fc)['idaapi'])['_find_bb_end'](1754273444) == 1754273453

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_fa2593c', 'expected': 'meadow_expected_46bf306', 'kernel32_idb': 'meadow_kernel32_idb_local_05217b3', 'version': 'meadow_version_local_8b5cf6c'}, 'test_find_bb_start')
def meadow_test_find_bb_start(meadow_kernel32_idb_local_05217b3, meadow_version_local_8b5cf6c, meadow_bitness_fa2593c, meadow_expected_46bf306):
    meadow_api_local_361ae71 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_05217b3)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754273429) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754273431) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754273432) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754273434) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754273438) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_361ae71)['idaapi'])['_find_bb_start'](1754292775) == 1754292775

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_3d11482', 'expected': 'meadow_expected_9ba8ab2', 'kernel32_idb': 'meadow_kernel32_idb_local_1625f01', 'version': 'meadow_version_local_1177f23'}, 'test_flow_preds')
def meadow_test_flow_preds(meadow_kernel32_idb_local_1625f01, meadow_version_local_1177f23, meadow_bitness_3d11482, meadow_expected_9ba8ab2):
    meadow_api_local_426f799 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_1625f01)
    assert meadow_lpluck('frm', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['_get_flow_preds'](1754273429)) == []
    assert meadow_lpluck('frm', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['_get_flow_preds'](1754273431)) == [1754273429]
    assert meadow_lpluck('frm', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['_get_flow_preds'](1754273432)) == [1754273431]
    assert meadow_lpluck('frm', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['_get_flow_preds'](1754292566)) == [1754273438]
    assert meadow_lpluck('type', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['_get_flow_preds'](1754292566)) == [_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_426f799)['idaapi'])['fl_JN']]

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_1381607', 'expected': 'meadow_expected_18423ba', 'kernel32_idb': 'meadow_kernel32_idb_local_408ba04', 'version': 'meadow_version_local_af7179d'}, 'test_flow_succs')
def meadow_test_flow_succs(meadow_kernel32_idb_local_408ba04, meadow_version_local_af7179d, meadow_bitness_1381607, meadow_expected_18423ba):
    meadow_api_local_e1efdde = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_408ba04)
    assert meadow_lpluck('to', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['_get_flow_succs'](1754273429)) == [1754273431]
    assert meadow_lpluck('to', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['_get_flow_succs'](1754273431)) == [1754273432]
    assert meadow_lpluck('to', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['_get_flow_succs'](1754273432)) == [1754273434]
    assert meadow_lpluck('to', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['_get_flow_succs'](1754273438)) == [1754273444, 1754292566]
    assert meadow_lpluck('type', _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['_get_flow_succs'](1754273438)) == [_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['fl_F'], _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e1efdde)['idaapi'])['fl_JN']]

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_0183f50', 'expected': 'meadow_expected_75c2a99', 'kernel32_idb': 'meadow_kernel32_idb_local_9da06e4', 'version': 'meadow_version_local_095c318'}, 'test_flow_chart')
def meadow_test_flow_chart(meadow_kernel32_idb_local_9da06e4, meadow_version_local_095c318, meadow_bitness_0183f50, meadow_expected_75c2a99):
    meadow_api_local_2eb6f96 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_9da06e4)
    meadow_DllEntryPoint_ce91641 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_2eb6f96)['ida_funcs'])['get_func'](1754273429)
    meadow_bbs_02d2330 = list(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_2eb6f96)['idaapi'])['FlowChart'](meadow_DllEntryPoint_ce91641))
    assert list(sorted(meadow_lpluck('startEA', meadow_bbs_02d2330))) == [1754273429, 1754273444, 1754292566]
    for meadow_bb_ff4abd6 in meadow_bbs_02d2330:
        if _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754273429:
            assert list(sorted(meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['succs']()))) == [1754273444, 1754292566]
        elif _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754273444:
            assert meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['succs']()) == []
        elif _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754292566:
            assert meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['succs']()) == [1754273444]
    for meadow_bb_ff4abd6 in meadow_bbs_02d2330:
        if _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754273429:
            assert meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['preds']()) == []
        elif _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754273444:
            assert list(sorted(meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['preds']()))) == [1754273429, 1754292566]
        elif _name_boundary.attributes(meadow_bb_ff4abd6)['startEA'] == 1754292566:
            assert meadow_lpluck('startEA', _name_boundary.attributes(meadow_bb_ff4abd6)['preds']()) == [1754273429]

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f740a1f', 'expected': 'meadow_expected_2ec29a1', 'kernel32_idb': 'meadow_kernel32_idb_local_939d60d', 'version': 'meadow_version_local_24ac169'}, 'test_fixups')
def meadow_test_fixups(meadow_kernel32_idb_local_939d60d, meadow_version_local_24ac169, meadow_bitness_f740a1f, meadow_expected_2ec29a1):
    meadow_api_local_da2a5c7 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_939d60d)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 1) is False
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 2) is False
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 5) is False
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 7) is False
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 8) is True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271774, 9) is True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271779 + 2, 1) is True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['contains_fixups'](1754271779 + 2, 16) is True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['get_next_fixup_ea'](1754271774) == 1754271781
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['get_next_fixup_ea'](1754271779) == 1754271781
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['get_next_fixup_ea'](1754271781) == 1754271781
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_da2a5c7)['idaapi'])['get_next_fixup_ea'](1754271781 + 1) == 1754271796

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_037a322', 'expected': 'meadow_expected_e03ea3d', 'kernel32_idb': 'meadow_kernel32_idb_local_71fd69c', 'version': 'meadow_version_local_d54d629'}, 'test_input_md5')
def meadow_test_input_md5(meadow_kernel32_idb_local_71fd69c, meadow_version_local_d54d629, meadow_bitness_037a322, meadow_expected_e03ea3d):
    meadow_api_local_3f3af22 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_71fd69c)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3f3af22)['idc'])['GetInputMD5']() == '00bf1bf1b779ce1af41371426821e0c2'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3f3af22)['idautils'])['GetInputFileMD5']() == '00bf1bf1b779ce1af41371426821e0c2'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3f3af22)['ida_nalt'])['retrieve_input_file_md5']() == '00bf1bf1b779ce1af41371426821e0c2'

@meadow_kern32_test_v7()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_8d4a1d6', 'expected': 'meadow_expected_1203a39', 'kernel32_idb': 'meadow_kernel32_idb_local_3597aaa', 'version': 'meadow_version_local_c0c97b7'}, 'test_input_sha256')
def meadow_test_input_sha256(meadow_kernel32_idb_local_3597aaa, meadow_version_local_c0c97b7, meadow_bitness_8d4a1d6, meadow_expected_1203a39):
    meadow_api_local_6a273c7 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_3597aaa)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_6a273c7)['idc'])['GetInputSHA256']() == 'ba1bc09b7bb290656582b4e4d896105caf00825b557ce45621e76741cd5dc262'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_6a273c7)['ida_nalt'])['retrieve_input_file_sha256']() == 'ba1bc09b7bb290656582b4e4d896105caf00825b557ce45621e76741cd5dc262'

@meadow_kern32_test([(680, 32, None), (680, 64, None), (695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None), (720, 32, None), (720, 64, None), (730, 32, None), (730, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_29b4ae5', 'expected': 'meadow_expected_14baa48', 'kernel32_idb': 'meadow_kernel32_idb_local_ba84212', 'version': 'meadow_version_local_345b8c5'}, 'test_segments')
def meadow_test_segments(meadow_kernel32_idb_local_ba84212, meadow_version_local_345b8c5, meadow_bitness_29b4ae5, meadow_expected_14baa48):
    meadow_api_local_cc5d1f5 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_ba84212)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['FirstSeg']() == 1754271744
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['NextSeg'](1754271744) == 1755164672
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['NextSeg'](1755164672) == 1755172864
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegName'](1754271744) == '.text'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegName'](1755164672) == '.data'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegName'](1755172864) == '.idata'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegStart'](1754271744) == 1754271744
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegStart'](1754271744 + 1) == 1754271744
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegStart'](1755164672 - 1) == 1754271744
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegStart'](1755164672) == 1755164672
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegEnd'](1754271744) == 1755164672
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegEnd'](1755164672) == 1755172864
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idc'])['SegEnd'](1755172864) == 1755177520
    meadow_seg_local_e1834b9 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_cc5d1f5)['idaapi'])['getseg'](1754271744)
    assert _name_boundary.attributes(meadow_seg_local_e1834b9)['startEA'] == 1754271744
    assert _name_boundary.attributes(meadow_seg_local_e1834b9)['endEA'] == 1755164672

@meadow_kern32_test_gt_v640()
@meadow_requires_capstone
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_04e104a', 'expected': 'meadow_expected_018f8ef', 'kernel32_idb': 'meadow_kernel32_idb_local_00d79a2', 'version': 'meadow_version_local_8d5c110'}, 'test_get_mnem')
def meadow_test_get_mnem(meadow_kernel32_idb_local_00d79a2, meadow_version_local_8d5c110, meadow_bitness_04e104a, meadow_expected_018f8ef):
    meadow_api_local_8a91a05 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_00d79a2)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8a91a05)['idc'])['GetMnem'](1754273429) == 'mov'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_e446dcf', 'expected': 'meadow_expected_c902918', 'kernel32_idb': 'meadow_kernel32_idb_local_bf32afc', 'version': 'meadow_version_local_71fbc82'}, 'test_functions')
def meadow_test_functions(meadow_kernel32_idb_local_bf32afc, meadow_version_local_71fbc82, meadow_bitness_e446dcf, meadow_expected_c902918):
    meadow_api_local_f6c2cc6 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_bf32afc)
    meadow_funcs_c424970 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_f6c2cc6)['idautils'])['Functions']()
    assert meadow_funcs_c424970[0] == 1754271760
    assert meadow_funcs_c424970[-1] == 1755042832 if meadow_version_local_71fbc82 > 500 else 1755109050
    if meadow_version_local_71fbc82 > 500:
        assert 1754274021 not in meadow_funcs_c424970

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_64b71c6', 'expected': 'meadow_expected_384f3aa', 'kernel32_idb': 'meadow_kernel32_idb_local_2b19200', 'version': 'meadow_version_local_3eccbf4'}, 'test_function_names')
def meadow_test_function_names(meadow_kernel32_idb_local_2b19200, meadow_version_local_3eccbf4, meadow_bitness_64b71c6, meadow_expected_384f3aa):
    meadow_api_local_43d0813 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2b19200)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_43d0813)['idc'])['GetFunctionName'](1754273429) == 'DllEntryPoint' if meadow_version_local_3eccbf4 <= 700 else '_BaseDllInitialize@12'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_43d0813)['idc'])['GetFunctionName'](1754273461) == 'sub_689016b5' if 500 < meadow_version_local_3eccbf4 <= 700 else '__BaseDllInitialize@12'
    if meadow_version_local_3eccbf4 > 500:
        with meadow_pytest.raises(KeyError):
            _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_43d0813)['idc'])['GetFunctionName'](1754274021)
    else:
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_43d0813)['idc'])['GetFunctionName'](1754274021) == 'sub_689018e5'

@meadow_pytest.mark.slow
@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_e3cbf73', 'expected': 'meadow_expected_fb25711', 'kernel32_idb': 'meadow_kernel32_idb_local_d2e887f', 'version': 'meadow_version_local_5ea8783'}, 'test_all_function_names')
def meadow_test_all_function_names(meadow_kernel32_idb_local_d2e887f, meadow_version_local_5ea8783, meadow_bitness_e3cbf73, meadow_expected_fb25711):
    meadow_api_local_0e0e0b3 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_d2e887f)
    meadow_funcs_4cc9da1 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e0e0b3)['idautils'])['Functions']()
    for meadow_func_ea3a81a in meadow_funcs_4cc9da1:
        meadow___2321a69 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e0e0b3)['idc'])['GetFunctionName'](meadow_func_ea3a81a)

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a3057ab', 'expected': 'meadow_expected_7f5479f', 'kernel32_idb': 'meadow_kernel32_idb_local_a264a3f', 'version': 'meadow_version_local_f34b120'}, 'test_comments')
def meadow_test_comments(meadow_kernel32_idb_local_a264a3f, meadow_version_local_f34b120, meadow_bitness_a3057ab, meadow_expected_7f5479f):
    meadow_api_local_a5227a0 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_a264a3f)
    meadow_expected_7f5479f = 'jumptable 6892FF97 default case' if meadow_version_local_f34b120 <= 700 else 'jumptable 6892FF97 default case, cases 3,5-7'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['ida_bytes'])['get_cmt'](1754271804, False) == 'Flags'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['ida_bytes'])['get_cmt'](1754276788, True) == meadow_expected_7f5479f
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['Comment'](1754271804) == 'Flags'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['RptCmt'](1754271804) == ''
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['RptCmt'](1754276788) == meadow_expected_7f5479f
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['Comment'](1754276788) == ''
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['GetCommentEx'](1754271804, False) == 'Flags'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a5227a0)['idc'])['GetCommentEx'](1754276788, True) == meadow_expected_7f5479f

@meadow_pytest.mark.slow
@meadow_kern32_test([(695, 32, (13369, 283)), (695, 64, (13369, 283)), (700, 32, (13368, 283)), (700, 64, (13368, 283))])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_1323635', 'expected': 'meadow_expected_6a8e95a', 'kernel32_idb': 'meadow_kernel32_idb_local_1c1563e', 'version': 'meadow_version_local_1dd5e45'}, 'test_all_comments')
def meadow_test_all_comments(meadow_kernel32_idb_local_1c1563e, meadow_version_local_1dd5e45, meadow_bitness_1323635, meadow_expected_6a8e95a):
    meadow_api_local_3429e70 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_1c1563e)
    meadow_regcmts_0598fe1 = []
    meadow_repcmts_fd63c7a = []
    meadow_textseg_b883414 = 1754271744
    for meadow_ea_ea0338c in range(meadow_textseg_b883414, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3429e70)['idc'])['SegEnd'](meadow_textseg_b883414)):
        meadow_flags_local_66a6886 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3429e70)['idc'])['GetFlags'](meadow_ea_ea0338c)
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3429e70)['ida_bytes'])['has_cmt'](meadow_flags_local_66a6886):
            continue
        meadow_regcmts_0598fe1.append(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3429e70)['ida_bytes'])['get_cmt'](meadow_ea_ea0338c, False))
        meadow_repcmts_fd63c7a.append(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_3429e70)['ida_bytes'])['get_cmt'](meadow_ea_ea0338c, True))
    assert len(meadow_regcmts_0598fe1), len(meadow_repcmts_fd63c7a) == meadow_expected_6a8e95a

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_330ca0d', 'expected': 'meadow_expected_5a7097f', 'kernel32_idb': 'meadow_kernel32_idb_local_0b2afd2', 'version': 'meadow_version_local_e22dd35'}, 'test_LocByName')
def meadow_test_LocByName(meadow_kernel32_idb_local_0b2afd2, meadow_version_local_e22dd35, meadow_bitness_330ca0d, meadow_expected_5a7097f):
    meadow_api_local_0e259e9 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_0b2afd2)
    if 500 < meadow_version_local_e22dd35 <= 700:
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e259e9)['idc'])['LocByName']('CancelIo') == 1754457866
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e259e9)['idc'])['GetFunctionName'](_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e259e9)['idc'])['LocByName']('CancelIo')) == 'CancelIo'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_0e259e9)['idc'])['LocByName']('__does not exist__') == -1

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_42e0e0c', 'expected': 'meadow_expected_8b8cc89', 'kernel32_idb': 'meadow_kernel32_idb_local_1ae0768', 'version': 'meadow_version_local_3284da3'}, 'test_MinMaxEA')
def meadow_test_MinMaxEA(meadow_kernel32_idb_local_1ae0768, meadow_version_local_3284da3, meadow_bitness_42e0e0c, meadow_expected_8b8cc89):
    meadow_api_local_89939a2 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_1ae0768)
    if meadow_version_local_3284da3 < 760:
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_89939a2)['idc'])['MinEA']() == 1754271744
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_89939a2)['idc'])['MaxEA']() == 1755177520
    else:
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_89939a2)['idc'])['MinEA']() == 1754267648
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_89939a2)['idc'])['MaxEA']() == 1755283456

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_c63d933', 'expected': 'meadow_expected_d9c7008', 'kernel32_idb': 'meadow_kernel32_idb_local_3aa9f3f', 'version': 'meadow_version_local_d9771b6'}, 'test_CodeRefsTo')
def meadow_test_CodeRefsTo(meadow_kernel32_idb_local_3aa9f3f, meadow_version_local_d9771b6, meadow_bitness_c63d933, meadow_expected_d9c7008):
    meadow_api_local_575fbbc = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_3aa9f3f)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_575fbbc)['idautils'])['CodeRefsTo'](1754978676, True)) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_575fbbc)['idautils'])['CodeRefsTo'](1754271793, True)) == {1754271787}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_575fbbc)['idautils'])['CodeRefsTo'](1754271762, True)) == {1754271760}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_575fbbc)['idautils'])['CodeRefsTo'](1754271762, False)) == set([])

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_d4c7e65', 'expected': 'meadow_expected_22843b3', 'kernel32_idb': 'meadow_kernel32_idb_local_48b9ea7', 'version': 'meadow_version_local_8814d2e'}, 'test_CodeRefsFrom')
def meadow_test_CodeRefsFrom(meadow_kernel32_idb_local_48b9ea7, meadow_version_local_8814d2e, meadow_bitness_d4c7e65, meadow_expected_22843b3):
    meadow_api_local_716f15f = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_48b9ea7)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_716f15f)['idautils'])['CodeRefsFrom'](1754271760, True)) == {1754271762}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_716f15f)['idautils'])['CodeRefsFrom'](1754271760, False)) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_716f15f)['idautils'])['CodeRefsFrom'](1754272178, True)) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_716f15f)['idautils'])['CodeRefsFrom'](1754271787, True)) == {1754272059, 1754271793}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_716f15f)['idautils'])['CodeRefsFrom'](1754271787, False)) == {1754272059}

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f3d781f', 'expected': 'meadow_expected_461571c', 'kernel32_idb': 'meadow_kernel32_idb_local_d26173d', 'version': 'meadow_version_local_8b981cd'}, 'test_DataRefsFrom')
def meadow_test_DataRefsFrom(meadow_kernel32_idb_local_d26173d, meadow_version_local_8b981cd, meadow_bitness_f3d781f, meadow_expected_461571c):
    meadow_api_local_69a9336 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_d26173d)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_69a9336)['idautils'])['DataRefsFrom'](1754292622)) == {1755165552}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_69a9336)['idautils'])['DataRefsFrom'](1754292651)) == {1755165552}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_69a9336)['idautils'])['DataRefsFrom'](1754292658)) == {1755164756}

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_fcbf687', 'expected': 'meadow_expected_f0d0393', 'kernel32_idb': 'meadow_kernel32_idb_local_7e6b44b', 'version': 'meadow_version_local_969c5bd'}, 'test_DataRefsTo')
def meadow_test_DataRefsTo(meadow_kernel32_idb_local_7e6b44b, meadow_version_local_969c5bd, meadow_bitness_fcbf687, meadow_expected_f0d0393):
    meadow_api_local_616ca25 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_7e6b44b)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_616ca25)['idautils'])['DataRefsTo'](1755165616)) == {1754825204, 1754825264}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_616ca25)['idautils'])['DataRefsTo'](1755165556)) == {1754344828, 1754878063, 1755054468}

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_8088aa8', 'expected': 'meadow_expected_a885456', 'kernel32_idb': 'meadow_kernel32_idb_local_a6576a0', 'version': 'meadow_version_local_07ba79d'}, 'test_XrefsTo')
def meadow_test_XrefsTo(meadow_kernel32_idb_local_a6576a0, meadow_version_local_07ba79d, meadow_bitness_8088aa8, meadow_expected_a885456):
    meadow_api_local_5ae2719 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_a6576a0)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754273461, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_ALL'])) == {(1754273447, 1754273461, 17)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754273461, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_FAR'])) == {(1754273447, 1754273461, 17)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754273461, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_DATA'])) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754284631, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_ALL'])) == {(1754284625, 1754284631, 21), (1754347713, 1754284631, 19)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754284631, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_FAR'])) == {(1754347713, 1754284631, 19)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1754284631, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_DATA'])) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1755164696, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_ALL'])) == {(1754284631, 1755164696, 3), (1754293072, 1755164696, 2), (1754494844, 1755164696, 2)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1755164696, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_FAR'])) == {(1754284631, 1755164696, 3), (1754293072, 1755164696, 2), (1754494844, 1755164696, 2)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idautils'])['XrefsTo'](1755164696, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_5ae2719)['idaapi'])['XREF_DATA'])) == {(1754284631, 1755164696, 3), (1754293072, 1755164696, 2), (1754494844, 1755164696, 2)}

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_70b52ab', 'expected': 'meadow_expected_6b3e487', 'kernel32_idb': 'meadow_kernel32_idb_local_6dfdc63', 'version': 'meadow_version_local_e729ff4'}, 'test_XrefsFrom')
def meadow_test_XrefsFrom(meadow_kernel32_idb_local_6dfdc63, meadow_version_local_e729ff4, meadow_bitness_70b52ab, meadow_expected_6b3e487):
    meadow_api_local_35b7f7f = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_6dfdc63)
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273472, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_ALL'])) == {(1754273472, 1754273477, 21), (1754273472, 1755165552, 3)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273472, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_FAR'])) == {(1754273472, 1755165552, 3)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273472, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_DATA'])) == {(1754273472, 1755165552, 3)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273511, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_ALL'])) == {(1754273511, 1754273517, 21), (1754273511, 1754284615, 19)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273511, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_FAR'])) == {(1754273511, 1754284615, 19)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754273511, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_DATA'])) == set([])
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754592444, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_ALL'])) == {(1754592444, 1754980828, 1)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754592444, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_FAR'])) == {(1754592444, 1754980828, 1)}
    assert set(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idautils'])['XrefsFrom'](1754592444, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_35b7f7f)['idaapi'])['XREF_DATA'])) == {(1754592444, 1754980828, 1)}

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_8ff42d2', 'expected': 'meadow_expected_d8ef93e', 'kernel32_idb': 'meadow_kernel32_idb_local_ea4962f', 'version': 'meadow_version_local_1170418'}, 'test_FindFuncEnd')
def meadow_test_FindFuncEnd(meadow_kernel32_idb_local_ea4962f, meadow_version_local_1170418, meadow_bitness_8ff42d2, meadow_expected_d8ef93e):
    meadow_api_local_8ed5228 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_ea4962f)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8ed5228)['idc'])['FindFuncEnd'](1754274865) == 1754274877
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8ed5228)['idc'])['FindFuncEnd'](1754285119) == 1754285148
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8ed5228)['idc'])['FindFuncEnd'](1754721268) == _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_8ed5228)['idc'])['BADADDR']

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_4006612', 'expected': 'meadow_expected_7b76c62', 'kernel32_idb': 'meadow_kernel32_idb_local_29274d1', 'version': 'meadow_version_local_ac6b194'}, 'test_imports')
def meadow_test_imports(meadow_kernel32_idb_local_29274d1, meadow_version_local_ac6b194, meadow_bitness_4006612, meadow_expected_7b76c62):
    meadow_api_local_67ae32c = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_29274d1)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_67ae32c)['ida_nalt'])['get_import_module_qty']() == 47
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_67ae32c)['ida_nalt'])['get_import_module_name'](0) == 'api-ms-win-core-rtlsupport-l1-2-0'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_67ae32c)['ida_nalt'])['get_import_module_name'](1) == 'ntdll'
    meadow_names_28956ab = []

    @_name_boundary.callable_contract({'addr': 'meadow_addr_db5b338', 'name': 'meadow_name_local_738521b', 'ordinal': 'meadow_ordinal_local_dfef209'}, 'cb')
    def meadow_cb_861bb42(meadow_addr_db5b338, meadow_name_local_738521b, meadow_ordinal_local_dfef209):
        meadow_names_28956ab.append((meadow_addr_db5b338, meadow_name_local_738521b, meadow_ordinal_local_dfef209))
        return True
    _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_67ae32c)['ida_nalt'])['enum_import_names'](1, meadow_cb_861bb42)
    assert len(meadow_names_28956ab) == 388
    assert meadow_names_28956ab[0] == (1755172884, 'NtMapUserPhysicalPagesScatter', None)

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_e6377aa', 'expected': 'meadow_expected_e4daf42', 'kernel32_idb': 'meadow_kernel32_idb_local_2babb78', 'version': 'meadow_version_local_9686b68'}, 'test_exports')
def meadow_test_exports(meadow_kernel32_idb_local_2babb78, meadow_version_local_9686b68, meadow_bitness_e6377aa, meadow_expected_e4daf42):
    meadow_api_local_9fc123e = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2babb78)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_qty']() == 1572
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_ordinal'](0) == 1
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry'](_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_ordinal'](0)) == 1754273581
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_name'](_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_ordinal'](0)) == 'BaseThreadInitThunk'
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_forwarder'](_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_ordinal'](16)) is None
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_ordinal'](1572) == 1754273429
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_9fc123e)['ida_entry'])['get_entry_name'](1754273429) == 'DllEntryPoint' if meadow_version_local_9686b68 <= 700 else '_BaseDllInitialize@12'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_23c0901', 'expected': 'meadow_expected_139a333', 'kernel32_idb': 'meadow_kernel32_idb_local_bbf3485', 'version': 'meadow_version_local_649836a'}, 'test_GetType')
def meadow_test_GetType(meadow_kernel32_idb_local_bbf3485, meadow_version_local_649836a, meadow_bitness_23c0901, meadow_expected_139a333):
    meadow_api_local_30ccb3d = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_bbf3485)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_30ccb3d)['idc'])['GetType'](1754273429) == 'BOOL (__stdcall DllEntryPoint)(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)' if meadow_version_local_649836a <= 700 else 'BOOL (__stdcall _BaseDllInitialize@12)(HINSTANCE hinstDLL, #5 fdwReason, LPVOID lpReserved)'
    if meadow_version_local_649836a <= 700:
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_30ccb3d)['idc'])['GetType'](1754902017) is None

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_dc7bc9f', 'expected': 'meadow_expected_83f9da4', 'kernel32_idb': 'meadow_kernel32_idb_local_378a84b', 'version': 'meadow_version_local_36196d0'}, 'test_inf_structure')
def meadow_test_inf_structure(meadow_kernel32_idb_local_378a84b, meadow_version_local_36196d0, meadow_bitness_dc7bc9f, meadow_expected_83f9da4):
    meadow_api_local_c7cfece = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_378a84b)
    meadow_inf_structure_e485c37 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_c7cfece)['idaapi'])['get_inf_structure']()
    assert meadow_inf_structure_e485c37.procname == 'metapc'

@meadow_requires_capstone
@_name_boundary.callable_contract({}, 'test_multi_bitness')
def meadow_test_multi_bitness():
    meadow_cd_7c25df9 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_089e600 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_7c25df9, 'data', 'multibitness', 'multibitness.idb')
    with meadow_idb.from_file(meadow_idbpath_089e600) as meadow_db_3b7dbbc:
        meadow_api_local_1da4206 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_3b7dbbc)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_1da4206)['idc'])['GetDisasm'](0) == 'xor\tdx, dx'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_1da4206)['idc'])['GetDisasm'](4096) == 'xor\tedx, edx'

@meadow_kern32_test_gt_v640()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_c8e2271', 'expected': 'meadow_expected_515c78b', 'kernel32_idb': 'meadow_kernel32_idb_local_2770652', 'version': 'meadow_version_local_ed7798c'}, 'test_name')
def meadow_test_name(meadow_kernel32_idb_local_2770652, meadow_version_local_ed7798c, meadow_bitness_c8e2271, meadow_expected_515c78b):
    meadow_api_local_e9b633b = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_2770652)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e9b633b)['ida_bytes'])['has_name'](_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e9b633b)['ida_bytes'])['get_flags'](1755165072)) == True
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_e9b633b)['ida_name'])['get_name'](1755165072) == 'FinestResolution' if meadow_version_local_ed7798c <= 700 else '_MinimumTime'

@meadow_pytest.mark.slow
@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_908091b', 'expected': 'meadow_expected_59a530e', 'kernel32_idb': 'meadow_kernel32_idb_local_b6522d1', 'version': 'meadow_version_local_b83b33d'}, 'test_names')
def meadow_test_names(meadow_kernel32_idb_local_b6522d1, meadow_version_local_b83b33d, meadow_bitness_908091b, meadow_expected_59a530e):
    meadow_api_local_10efbe9 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_b6522d1)
    if meadow_version_local_b83b33d == 695:
        assert len(list(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_10efbe9)['idautils'])['Names']())) == 14252
    elif meadow_version_local_b83b33d == 700:
        assert len(list(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_10efbe9)['idautils'])['Names']())) == 14247
    elif meadow_version_local_b83b33d == 720:
        assert len(list(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_10efbe9)['idautils'])['Names']())) == 16457
    elif meadow_version_local_b83b33d == 730:
        assert len(list(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_10efbe9)['idautils'])['Names']())) == 16455

@_name_boundary.callable_contract({}, 'test_anterior_lines')
def meadow_test_anterior_lines():
    meadow_cd_1055e1e = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_cea8599 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_1055e1e, 'data', 'ant-post-comments', 'small.idb')
    with meadow_idb.from_file(meadow_idbpath_cea8599) as meadow_db_d3c280c:
        meadow_api_local_def893f = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_d3c280c)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_def893f)['idc'])['LineA'](1, 0) == 'anterior line 1'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_def893f)['idc'])['LineA'](1, 1) == 'anterior line 2'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_def893f)['idc'])['LineA'](1, 2) == ''

@_name_boundary.callable_contract({}, 'test_posterior_lines')
def meadow_test_posterior_lines():
    meadow_cd_0101531 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_7411a0b = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_0101531, 'data', 'ant-post-comments', 'small.idb')
    with meadow_idb.from_file(meadow_idbpath_7411a0b) as meadow_db_105edd8:
        meadow_api_local_6a900cd = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_105edd8)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_6a900cd)['idc'])['LineB'](1, 0) == 'posterior line 1'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_6a900cd)['idc'])['LineB'](1, 1) == 'posterior line 2'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_6a900cd)['idc'])['LineB'](1, 2) == ''

@_name_boundary.callable_contract({}, 'test_function_comment')
def meadow_test_function_comment():
    meadow_cd_704343f = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_188cbfe = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_704343f, 'data', 'func-comment', 'small.idb')
    with meadow_idb.from_file(meadow_idbpath_188cbfe) as meadow_db_f85a56f:
        meadow_api_local_a17ec44 = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_f85a56f)
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a17ec44)['ida_funcs'])['get_func_cmt'](3, False) == 'function comment'
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_a17ec44)['ida_funcs'])['get_func_cmt'](3, True) == 'repeatable function comment'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_630126a', 'expected': 'meadow_expected_af7b6e9', 'kernel32_idb': 'meadow_kernel32_idb_local_729ff1e', 'version': 'meadow_version_local_18b92d7'}, 'test_ida_structs')
def meadow_test_ida_structs(meadow_kernel32_idb_local_729ff1e, meadow_version_local_18b92d7, meadow_bitness_630126a, meadow_expected_af7b6e9):
    meadow_idapy_834492d = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_kernel32_idb_local_729ff1e)
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_idapy_834492d)['ida_struct'])['get_first_struc_idx']() == 0
    meadow_last_idx_435c6d2 = _name_boundary.attributes(_name_boundary.attributes(meadow_idapy_834492d)['ida_struct'])['get_last_struc_idx']()
    if meadow_version_local_18b92d7 == 500:
        assert meadow_last_idx_435c6d2 == 23
    elif meadow_version_local_18b92d7 <= 630:
        assert meadow_last_idx_435c6d2 == 31
    elif meadow_version_local_18b92d7 <= 700:
        assert meadow_last_idx_435c6d2 == 41
    elif meadow_version_local_18b92d7 == 720:
        assert meadow_last_idx_435c6d2 == 68
    elif meadow_version_local_18b92d7 == 730:
        assert meadow_last_idx_435c6d2 == 80
_name_boundary.module_contract(globals(), {'test_bytes_2': 'meadow_test_bytes_2', 'kern32_test_gt_v640': 'meadow_kern32_test_gt_v640', 'test_GetType': 'meadow_test_GetType', 'test_function_names': 'meadow_test_function_names', 'test_DataRefsFrom': 'meadow_test_DataRefsFrom', 'pluck': 'meadow_pluck', 'test_bytes': 'meadow_test_bytes', 'test_names': 'meadow_test_names', 'test_find_bb_start': 'meadow_test_find_bb_start', 'test_func_t': 'meadow_test_func_t', 'test_FindFuncEnd': 'meadow_test_FindFuncEnd', 'test_colors': 'meadow_test_colors', 'test_MinMaxEA': 'meadow_test_MinMaxEA', 'test_posterior_lines': 'meadow_test_posterior_lines', 'test_data': 'meadow_test_data', 'test_state': 'meadow_test_state', 'test_CodeRefsTo': 'meadow_test_CodeRefsTo', 'test_flow_succs': 'meadow_test_flow_succs', 'test_multi_bitness': 'meadow_test_multi_bitness', 'test_input_sha256': 'meadow_test_input_sha256', 'test_ida_structs': 'meadow_test_ida_structs', 'test_function_comment': 'meadow_test_function_comment', 'test_get_mnem': 'meadow_test_get_mnem', 'test_inf_structure': 'meadow_test_inf_structure', 'test_exports': 'meadow_test_exports', 'test_operand_types': 'meadow_test_operand_types', 'test_code': 'meadow_test_code', 'test_LocByName': 'meadow_test_LocByName', 'test_all_comments': 'meadow_test_all_comments', 'test_comments': 'meadow_test_comments', 'lpluck': 'meadow_lpluck', 'test_DataRefsTo': 'meadow_test_DataRefsTo', 'test_fixups': 'meadow_test_fixups', 'test_input_md5': 'meadow_test_input_md5', 'test_CodeRefsFrom': 'meadow_test_CodeRefsFrom', 'test_name': 'meadow_test_name', 'test_anterior_lines': 'meadow_test_anterior_lines', 'test_flow_preds': 'meadow_test_flow_preds', 'test_heads': 'meadow_test_heads', 'test_flow_chart': 'meadow_test_flow_chart', 'test_specific_state': 'meadow_test_specific_state', 'test_XrefsTo': 'meadow_test_XrefsTo', 'test_find_bb_end': 'meadow_test_find_bb_end', 'test_functions': 'meadow_test_functions', 'test_all_function_names': 'meadow_test_all_function_names', 'test_function_name': 'meadow_test_function_name', 'test_imports': 'meadow_test_imports', 'test_segments': 'meadow_test_segments', 'test_XrefsFrom': 'meadow_test_XrefsFrom'})
