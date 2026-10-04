# Derived from tests/test_analysis.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import re as meadow_re
import functools as meadow_functools
from checks.fixture_registry import *
import idbmeadow.semantic_views as _boundary_import_idb_analysis
import idbmeadow as meadow_idb
from idbmeadow.type_codes import *
try:
    from re import fullmatch as meadow_fullmatch
except ImportError:

    @_name_boundary.callable_contract({'regex': 'meadow_regex_7094b8b', 'string': 'meadow_string_local_06280a9', 'flags': 'meadow_flags_local_ece05ff'}, 'fullmatch')
    def meadow_fullmatch(meadow_regex_7094b8b, meadow_string_local_06280a9, meadow_flags_local_ece05ff=0):
        """Emulate python-3.4 re.fullmatch()."""
        return meadow_re.match('(?:' + meadow_regex_7094b8b + ')\\Z', meadow_string_local_06280a9, flags=meadow_flags_local_ece05ff)

@_name_boundary.callable_contract({'prop': 'meadow_prop_04707e0', 's': 'meadow_s_local_5180ad1'}, 'pluck')
def meadow_pluck(meadow_prop_04707e0, meadow_s_local_5180ad1):
    """
    generate the values from the given attribute with name `prop` from the given sequence of items `s`.

    Args:
      prop (str): the name of an attribute.
      s (sequnce): a bunch of objects.

    Yields:
      any: the values of the requested field across the sequence
    """
    for meadow_x_e313430 in meadow_s_local_5180ad1:
        yield _name_boundary.read_attribute(meadow_x_e313430, meadow_prop_04707e0)

@_name_boundary.callable_contract({'prop': 'meadow_prop_f45caf9', 's': 'meadow_s_local_a449d54'}, 'lpluck')
def meadow_lpluck(meadow_prop_f45caf9, meadow_s_local_a449d54):
    """
    like `pluck`, but returns the result in a single list.
    """
    return list(meadow_pluck(meadow_prop_f45caf9, meadow_s_local_a449d54))

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_17f44ec', 'expected': 'meadow_expected_8e9cb4f', 'kernel32_idb': 'meadow_kernel32_idb_local_8a1962d', 'version': 'meadow_version_local_8609504'}, 'test_root')
def meadow_test_root(meadow_kernel32_idb_local_8a1962d, meadow_version_local_8609504, meadow_bitness_17f44ec, meadow_expected_8e9cb4f):
    meadow_root_341fd34 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_kernel32_idb_local_8a1962d)
    assert meadow_root_341fd34.version in (480, 610, 640, 650, 670, 680, 695, 700, 760)
    assert _name_boundary.attributes(meadow_root_341fd34)['get_field_tag']('version') == 'A'
    assert _name_boundary.attributes(meadow_root_341fd34)['get_field_index']('version') == -1
    meadow_vs_e613495 = str(meadow_version_local_8609504 / 100)
    assert meadow_root_341fd34.version_string == meadow_vs_e613495 if len(meadow_vs_e613495) == 4 else meadow_vs_e613495 + '0'
    assert meadow_root_341fd34.open_count in (1, 2)
    assert meadow_root_341fd34.md5 == '00bf1bf1b779ce1af41371426821e0c2'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a1db2fb', 'expected': 'meadow_expected_ae38050', 'kernel32_idb': 'meadow_kernel32_idb_local_f8c6c8f', 'version': 'meadow_version_local_70f5bd5'}, 'test_root_timestamp')
def meadow_test_root_timestamp(meadow_kernel32_idb_local_f8c6c8f, meadow_version_local_70f5bd5, meadow_bitness_a1db2fb, meadow_expected_ae38050):
    meadow_root_429e028 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_kernel32_idb_local_f8c6c8f)
    meadow_actual_dbf1e99 = meadow_root_429e028.created.isoformat()
    meadow_pattern_11a12bd = '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\+00:00'
    assert meadow_fullmatch(meadow_pattern_11a12bd, meadow_actual_dbf1e99) is not None

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_83b5097', 'expected': 'meadow_expected_f47d2ec', 'kernel32_idb': 'meadow_kernel32_idb_local_eef4e7e', 'version': 'meadow_version_local_a8990ac'}, 'test_root_open_count')
def meadow_test_root_open_count(meadow_kernel32_idb_local_eef4e7e, meadow_version_local_a8990ac, meadow_bitness_83b5097, meadow_expected_f47d2ec):
    meadow_root_a9deba8 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_kernel32_idb_local_eef4e7e)
    assert meadow_root_a9deba8.open_count in (2, 1)

@meadow_kern32_test([(695, 32, 'pe.ldw'), (695, 64, 'pe64.l64'), (700, 32, 'pe.dll'), (700, 64, 'pe64.dll')])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_08b81c6', 'expected': 'meadow_expected_5072f69', 'kernel32_idb': 'meadow_kernel32_idb_local_563ed86', 'version': 'meadow_version_local_a8efed2'}, 'test_loader')
def meadow_test_loader(meadow_kernel32_idb_local_563ed86, meadow_version_local_a8efed2, meadow_bitness_08b81c6, meadow_expected_5072f69):
    meadow_loader_e1059aa = _name_boundary.attributes(meadow_idb)['analysis'].Loader(meadow_kernel32_idb_local_563ed86)
    assert meadow_loader_e1059aa.format.startswith('Portable executable') is True
    assert meadow_loader_e1059aa.plugin == meadow_expected_5072f69

@meadow_kern32_test([(695, 32, 117), (695, 64, 117), (700, 32, 122), (700, 64, 122)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_22fe420', 'expected': 'meadow_expected_464b0f6', 'kernel32_idb': 'meadow_kernel32_idb_local_da803db', 'version': 'meadow_version_local_d7172f9'}, 'test_fileregions')
def meadow_test_fileregions(meadow_kernel32_idb_local_da803db, meadow_version_local_d7172f9, meadow_bitness_22fe420, meadow_expected_464b0f6):
    meadow_fileregions_0af1f83 = _name_boundary.attributes(meadow_idb)['analysis'].FileRegions(meadow_kernel32_idb_local_da803db)
    meadow_regions_962dbf2 = meadow_fileregions_0af1f83.regions
    assert len(meadow_regions_962dbf2) == 3
    assert list(meadow_regions_962dbf2.keys()) == [1754271744, 1755164672, 1755172864]
    assert meadow_regions_962dbf2[1754271744].start == 1754271744
    assert meadow_regions_962dbf2[1754271744].end == 1755164672
    assert meadow_regions_962dbf2[1754271744].rva == 4096

@meadow_kern32_test([(695, 32, 4776), (695, 64, 4776), (700, 32, 4752), (700, 64, 4752)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_e6112a6', 'expected': 'meadow_expected_58a37c3', 'kernel32_idb': 'meadow_kernel32_idb_local_9f8f6a0', 'version': 'meadow_version_local_8d9ffa7'}, 'test_functions')
def meadow_test_functions(meadow_kernel32_idb_local_9f8f6a0, meadow_version_local_8d9ffa7, meadow_bitness_e6112a6, meadow_expected_58a37c3):
    meadow_functions_5897ce7 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](meadow_kernel32_idb_local_9f8f6a0)
    meadow_funcs_2cf510e = meadow_functions_5897ce7.functions
    for meadow_addr_3868190, meadow_func_ad652bb in meadow_funcs_2cf510e.items():
        assert meadow_addr_3868190 == _name_boundary.attributes(meadow_func_ad652bb)['startEA']
    assert len(meadow_funcs_2cf510e) == meadow_expected_58a37c3

@meadow_kern32_test([(695, 32, 117), (695, 64, 117), (700, 32, 122), (700, 64, 122)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_9f2d15f', 'expected': 'meadow_expected_2215bbc', 'kernel32_idb': 'meadow_kernel32_idb_local_6f96064', 'version': 'meadow_version_local_fff087d'}, 'test_function_frame')
def meadow_test_function_frame(meadow_kernel32_idb_local_6f96064, meadow_version_local_fff087d, meadow_bitness_9f2d15f, meadow_expected_2215bbc):
    meadow_DllEntryPoint_e04d1c8 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](meadow_kernel32_idb_local_6f96064).functions[1754273429]
    assert _name_boundary.attributes(meadow_DllEntryPoint_e04d1c8)['startEA'] == 1754273429
    assert _name_boundary.attributes(meadow_DllEntryPoint_e04d1c8)['endEA'] == 1754273456
    assert _name_boundary.attributes(meadow_DllEntryPoint_e04d1c8)['frame'] == meadow_expected_2215bbc

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_859b8e0', 'expected': 'meadow_expected_05e1771', 'kernel32_idb': 'meadow_kernel32_idb_local_3c686e6', 'version': 'meadow_version_local_c4bf571'}, 'test_struct')
def meadow_test_struct(meadow_kernel32_idb_local_3c686e6, meadow_version_local_c4bf571, meadow_bitness_859b8e0, meadow_expected_05e1771):
    meadow_DllEntryPoint_4c7b64a = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](meadow_kernel32_idb_local_3c686e6).functions[1754273429]
    meadow_struc_14cf78c = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Struct'](meadow_kernel32_idb_local_3c686e6, _name_boundary.attributes(meadow_DllEntryPoint_4c7b64a)['frame'])
    meadow_members_5eea306 = list(_name_boundary.attributes(meadow_struc_14cf78c)['get_members']())
    assert list(map(lambda meadow_m_81ced73: _name_boundary.attributes(meadow_m_81ced73)['get_name'](), meadow_members_5eea306)) == [' s', ' r', 'hinstDLL', 'fdwReason', 'lpReserved']
    assert _name_boundary.attributes(meadow_members_5eea306[2])['get_type']() == ('HINSTANCE' if meadow_version_local_c4bf571 > 500 else None)

@_name_boundary.callable_contract({'db': 'meadow_db_2053e4f', 'fva': 'meadow_fva_a2d3238'}, 'get_fn_signature')
def meadow_get_fn_signature(meadow_db_2053e4f, meadow_fva_a2d3238):
    return _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](meadow_db_2053e4f, meadow_fva_a2d3238))['get_signature']())['get_typestr']()

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_bccefe1', 'expected': 'meadow_expected_a58b793', 'kernel32_idb': 'meadow_kernel32_idb_local_534f982', 'version': 'meadow_version_local_79286f8'}, 'test_function')
def meadow_test_function(meadow_kernel32_idb_local_534f982, meadow_version_local_79286f8, meadow_bitness_bccefe1, meadow_expected_a58b793):
    meadow_sub_689016B5_25392f3 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](meadow_kernel32_idb_local_534f982, 1754273461)
    if 500 < meadow_version_local_79286f8 <= 700 or meadow_version_local_79286f8 >= 760:
        assert _name_boundary.attributes(meadow_sub_689016B5_25392f3)['get_name']() == 'sub_689016B5'
    else:
        assert _name_boundary.attributes(meadow_sub_689016B5_25392f3)['get_name']() == '__BaseDllInitialize@12'
    meadow_chunks_71b76f5 = list(_name_boundary.attributes(meadow_sub_689016B5_25392f3)['get_chunks']())
    assert meadow_chunks_71b76f5 == [(1754280921, 23), (1754284615, 163), (1754292665, 606), (1754347700, 31), (1754446880, 33), (1754460472, 21), (1754460775, 41), (1754484069, 61), (1754494727, 132)]
    meadow_DllEntryPoint_6bff236 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](meadow_kernel32_idb_local_534f982, 1754273429)
    meadow_sig_22132a0 = _name_boundary.attributes(meadow_DllEntryPoint_6bff236)['get_signature']()
    if meadow_version_local_79286f8 <= 700 or meadow_version_local_79286f8 >= 760:
        assert _name_boundary.attributes(meadow_sig_22132a0)['get_typestr']() == 'BOOL (__stdcall DllEntryPoint)(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)'
    else:
        assert _name_boundary.attributes(meadow_sig_22132a0)['get_typestr']() == 'BOOL (__stdcall _BaseDllInitialize@12)(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)'
    assert _name_boundary.attributes(meadow_sig_22132a0)['get_cc']() == meadow_CM_CC_STDCALL
    assert _name_boundary.attributes(_name_boundary.attributes(meadow_sig_22132a0)['get_rettype']())['get_typename']() == 'BOOL'
    assert len(_name_boundary.attributes(_name_boundary.attributes(meadow_sig_22132a0)['type_details'])['args']) == 3
    meadow__get_fn_signature_d10c02a = meadow_functools.partial(meadow_get_fn_signature, meadow_kernel32_idb_local_534f982)
    if meadow_version_local_79286f8 >= 760:
        assert meadow__get_fn_signature_d10c02a(1754273105) == 'void (__fastcall @__security_check_cookie@4)(uintptr_t StackCookie)'
        assert meadow__get_fn_signature_d10c02a(1754273335) == 'void* (__cdecl memset)(void*, int Val, size_t Size)'
        # The only bundled >=760 case is v7.6/x32; pinned upstream reads the same undecorated signature.
        assert meadow__get_fn_signature_d10c02a(1754280366) == 'int (__stdcall sub_689031AE)(PRTL_CRITICAL_SECTION CriticalSection, int, int, int)'
    elif 760 > meadow_version_local_79286f8 >= 730:
        assert meadow__get_fn_signature_d10c02a(1754273105) == 'void (__fastcall @__security_check_cookie@4)(uintptr_t StackCookie)'
        assert meadow__get_fn_signature_d10c02a(1754273335) == 'void* (__cdecl _memset)(void*, int Val, size_t Size)'
        assert meadow__get_fn_signature_d10c02a(1754280366) == 'int (__thiscall ?NotifyLoadStringResource@CMessageMapper@FSPErrorMessages@@QAEJPAUHINSTANCE__@@IPBGKPAPAX@Z)(FSPErrorMessages::CMessageMapper* this, HINSTANCE CriticalSection, unsigned int, unsigned int16*, unsigned int, void**)'
    elif meadow_version_local_79286f8 >= 720:
        assert meadow__get_fn_signature_d10c02a(1754491628) == 'int (__stdcall _BasepProcessInvalidImage@84)(NTSTATUS Status, int, int, int, int, int, int, int, int, int, int, int, int, int, PUNICODE_STRING, int, int, int, int, int, int)'
        assert meadow__get_fn_signature_d10c02a(1754273335) == 'void* (__cdecl _memset)(void* Dst, int Val, size_t Size)'
        assert meadow__get_fn_signature_d10c02a(1754280366) == 'int (__thiscall ?NotifyLoadStringResource@CMessageMapper@FSPErrorMessages@@QAEJPAUHINSTANCE__@@IPBGKPAPAX@Z)(FSPErrorMessages::CMessageMapper* this, HINSTANCE CriticalSection, unsigned int, unsigned int16*, unsigned int, void**)'
    elif meadow_version_local_79286f8 >= 700:
        assert meadow__get_fn_signature_d10c02a(1754491628) == 'int (__cdecl BasepProcessInvalidImage)(NTSTATUS NtStatus, int, int, int, int, int, int, int, int, int, int, int, int, int, PUNICODE_STRING, int, int, int, int, int, int)'
        assert meadow__get_fn_signature_d10c02a(1754286829) == 'int (__thiscall sub_68904AED)(HANDLE FileHandle, int, int)'
    elif meadow_version_local_79286f8 > 630:
        assert meadow__get_fn_signature_d10c02a(1754354985) == 'int (__cdecl sub_68915529)(LPCWSTR lpString1, int, int)'
        assert meadow__get_fn_signature_d10c02a(1754286829) == 'int (__thiscall sub_68904AED)(HANDLE FileHandle, int, int)'
    elif 630 == meadow_version_local_79286f8:
        assert meadow__get_fn_signature_d10c02a(1754354985) == 'int (__cdecl sub_68915529)(PCNZWCH Buf1, int, int)'
        assert meadow__get_fn_signature_d10c02a(1754362575) == 'int (__thiscall sub_689172CF)(DWORD Size, int, int, int, int)'
    elif meadow_version_local_79286f8 == 500:
        assert meadow__get_fn_signature_d10c02a(1754280280) == 'int (__fastcall _BasepNotifyLoadStringResource@16)(int, int, int, int, int, int)'
        assert meadow__get_fn_signature_d10c02a(1754293521) == 'int (__cdecl _StringCbPrintfW)(wchar_t*, int, wchar_t*, int8)'

@_name_boundary.callable_contract({}, 'test_function_usercall')
def meadow_test_function_usercall():
    meadow__db_2ba68ce = meadow_load_idb(_name_boundary.attributes(meadow_os)['path'].join(meadow_CD, 'data', 'thumb', 'ls.idb'))
    meadow__get_fn_signature_cdb819c = meadow_functools.partial(meadow_get_fn_signature, meadow__db_2ba68ce)
    assert meadow__get_fn_signature_cdb819c(98808) == 'unsigned int8* (__usercall human_readable@<R0>)(uintmax_t n@<0:R0, 4:R1>, unsigned int8* buf@<R2>, int opts@<R3>, uintmax_t from_block_size, uintmax_t to_block_size)'
    assert meadow__get_fn_signature_cdb819c(101780) == 'unsigned int8* (__usercall imaxtostr@<R0>)(intmax_t i@<0:R0, 4:R1>, unsigned int8* buf@<R2>)'
    assert meadow__get_fn_signature_cdb819c(101888) == 'unsigned int8* (__usercall umaxtostr@<R0>)(uintmax_t i@<0:R0, 4:R1>, unsigned int8* buf@<R2>)'
    assert meadow__get_fn_signature_cdb819c(112964) == 'uintmax_t (__usercall xnumtoumax@<R1:R0>)(unsigned int8* n_str@<R0>, int base@<R1>, uintmax_t min@<0:R2, 4:R3>, uintmax_t max, unsigned int8* suffixes, unsigned int8* err, int err_exit)'
    assert meadow__get_fn_signature_cdb819c(113236) == 'uintmax_t (__usercall xdectoumax@<R1:R0>)(unsigned int8* n_str@<R0>, uintmax_t min@<0:R2, 4:R3>, uintmax_t max, unsigned int8* suffixes, unsigned int8* err, int err_exit)'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f338ef3', 'expected': 'meadow_expected_c255219', 'kernel32_idb': 'meadow_kernel32_idb_local_fc78e59', 'version': 'meadow_version_local_84e71cd'}, 'test_stack_change_points')
def meadow_test_stack_change_points(meadow_kernel32_idb_local_fc78e59, meadow_version_local_84e71cd, meadow_bitness_f338ef3, meadow_expected_c255219):
    meadow_CreateThread_8e091e7 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](meadow_kernel32_idb_local_fc78e59, 1754274538)
    meadow_change_points_52be5b1 = list(_name_boundary.attributes(meadow_CreateThread_8e091e7)['get_stack_change_points']())
    assert meadow_change_points_52be5b1 == [(1754274541, -4), (1754274546, -4), (1754274551, -4), (1754274557, -4), (1754274560, -4), (1754274563, -4), (1754274566, -4), (1754274569, -4), (1754274571, -4), (1754274577, 32), (1754274578, 4)]
    meadow_GetCurrentProcess_051e611 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](meadow_kernel32_idb_local_fc78e59, 1754272915)
    assert list(_name_boundary.attributes(meadow_GetCurrentProcess_051e611)['get_stack_change_points']()) == []

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_4722d04', 'expected': 'meadow_expected_0942808', 'kernel32_idb': 'meadow_kernel32_idb_local_a080997', 'version': 'meadow_version_local_e094a9f'}, 'test_xrefs')
def meadow_test_xrefs(meadow_kernel32_idb_local_a080997, meadow_version_local_e094a9f, meadow_bitness_4722d04, meadow_expected_0942808):
    assert meadow_lpluck('to', _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(meadow_kernel32_idb_local_a080997, 1754273429)) == []
    assert meadow_lpluck('to', _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(meadow_kernel32_idb_local_a080997, 1754273438)) == [1754292566]
    assert meadow_lpluck('frm', _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_to(meadow_kernel32_idb_local_a080997, 1754273438)) == []
    assert meadow_lpluck('frm', _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_to(meadow_kernel32_idb_local_a080997, 1754292566)) == [1754273438]
    meadow_security_cookie_8a97166 = 1755165552
    assert meadow_lpluck('to', _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_from(meadow_kernel32_idb_local_a080997, 1754273472)) == [meadow_security_cookie_8a97166]
    assert meadow_lpluck('frm', _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_to(meadow_kernel32_idb_local_a080997, 1754273472)) == []
    assert 1754273472 in meadow_pluck('frm', _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_to(meadow_kernel32_idb_local_a080997, meadow_security_cookie_8a97166))
    assert meadow_lpluck('to', _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_from(meadow_kernel32_idb_local_a080997, meadow_security_cookie_8a97166)) == []

@meadow_pytest.mark.skipif(meadow_six.PY2, reason='it consumes too much memory')
@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_009a176', 'expected': 'meadow_expected_be25647', 'kernel32_idb': 'meadow_kernel32_idb_local_c0bb7dd', 'version': 'meadow_version_local_019078d'}, 'test_fixups')
def meadow_test_fixups(meadow_kernel32_idb_local_c0bb7dd, meadow_version_local_019078d, meadow_bitness_009a176, meadow_expected_be25647):
    meadow_fixups_44e53d0 = _name_boundary.attributes(meadow_idb)['analysis'].Fixups(meadow_kernel32_idb_local_c0bb7dd).fixups
    assert len(meadow_fixups_44e53d0) == 31608
    assert meadow_fixups_44e53d0[1754271779 + 2].offset == 1755165080
    assert _name_boundary.attributes(meadow_fixups_44e53d0[1754271779 + 2])['get_fixup_length']() == 4

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_bcf0851', 'expected': 'meadow_expected_d626461', 'kernel32_idb': 'meadow_kernel32_idb_local_a51e74c', 'version': 'meadow_version_local_0aa5d50'}, 'test_segments')
def meadow_test_segments(meadow_kernel32_idb_local_a51e74c, meadow_version_local_0aa5d50, meadow_bitness_bcf0851, meadow_expected_d626461):
    meadow_segs_695cd92 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](meadow_kernel32_idb_local_a51e74c).segments
    meadow_start_ea_local_9681db3 = list(sorted(map(_name_boundary.callable_contract({'s': 'meadow_s_local_860645e'}, '<lambda>')(lambda meadow_s_local_860645e: _name_boundary.attributes(meadow_s_local_860645e)['startEA']), meadow_segs_695cd92.values())))
    meadow_expect_start_ea_1717fba = [1754271744, 1755164672, 1755172864] if meadow_version_local_0aa5d50 < 760 else [1754267648, 1754271744, 1755164672, 1755172864, 1755213824, 1755217920]
    assert meadow_start_ea_local_9681db3 == meadow_expect_start_ea_1717fba
    meadow_end_ea_4d93131 = list(sorted(map(_name_boundary.callable_contract({'s': 'meadow_s_local_0616a79'}, '<lambda>')(lambda meadow_s_local_0616a79: _name_boundary.attributes(meadow_s_local_0616a79)['endEA']), meadow_segs_695cd92.values())))
    meadow_expect_end_ea_d65afbb = None
    if meadow_version_local_0aa5d50 >= 760:
        meadow_expect_end_ea_d65afbb = [1754271744, 1755164672, 1755172864, 1755177520, 1755217920, 1755283456]
    elif 500 < meadow_version_local_0aa5d50 < 760:
        meadow_expect_end_ea_d65afbb = [1755164672, 1755172864, 1755177520]
    else:
        meadow_expect_end_ea_d65afbb = [1755164672, 1755169504, 1755177520]
    assert meadow_end_ea_4d93131 == meadow_expect_end_ea_d65afbb

@meadow_kern32_test([(680, 32, None), (680, 64, None), (695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None), (720, 32, None), (720, 64, None), (730, 32, None), (730, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_5bd7b7e', 'expected': 'meadow_expected_cc97411', 'kernel32_idb': 'meadow_kernel32_idb_local_b8d7e9a', 'version': 'meadow_version_local_195fc22'}, 'test_segstrings')
def meadow_test_segstrings(meadow_kernel32_idb_local_b8d7e9a, meadow_version_local_195fc22, meadow_bitness_5bd7b7e, meadow_expected_cc97411):
    meadow_strs_19ef813 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'].SegStrings(meadow_kernel32_idb_local_b8d7e9a))['strings']
    assert meadow_strs_19ef813[1:] == ['.text', 'CODE', '.data', 'DATA', '.idata']

@_name_boundary.callable_contract({'elf_idb': 'meadow_elf_idb_local_46c7521'}, 'test_segments2')
def meadow_test_segments2(meadow_elf_idb_local_46c7521):
    meadow_EXPECTED_a0db5ab = {'.init': {'startEA': 134518444, 'sclass': 2, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 5, 'bitness': 1, 'flags': 16, 'sel': 1, 'type': 2, 'color': 4294967295}, '.plt': {'startEA': 134518480, 'sclass': 2, 'orgbase': 0, 'align': 3, 'comb': 2, 'perm': 5, 'bitness': 1, 'flags': 16, 'sel': 2, 'type': 2, 'color': 4294967295}, '.plt.got': {'startEA': 134520288, 'sclass': 2, 'orgbase': 0, 'align': 10, 'comb': 2, 'perm': 5, 'bitness': 1, 'flags': 16, 'sel': 3, 'type': 2, 'color': 4294967295}, '.text': {'startEA': 134520304, 'sclass': 2, 'orgbase': 0, 'align': 3, 'comb': 2, 'perm': 5, 'bitness': 1, 'flags': 16, 'sel': 4, 'type': 2, 'color': 4294967295}, '.fini': {'startEA': 134592052, 'sclass': 2, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 5, 'bitness': 1, 'flags': 16, 'sel': 5, 'type': 2, 'color': 4294967295}, '.rodata': {'startEA': 134592096, 'sclass': 8, 'orgbase': 0, 'align': 8, 'comb': 2, 'perm': 4, 'bitness': 1, 'flags': 16, 'sel': 6, 'type': 3, 'color': 4294967295}, '.eh_frame_hdr': {'startEA': 134614036, 'sclass': 8, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 4, 'bitness': 1, 'flags': 16, 'sel': 7, 'type': 3, 'color': 4294967295}, '.eh_frame': {'startEA': 134616112, 'sclass': 8, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 4, 'bitness': 1, 'flags': 16, 'sel': 8, 'type': 3, 'color': 4294967295}, '.init_array': {'startEA': 134643456, 'sclass': 12, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 9, 'type': 3, 'color': 4294967295}, '.fini_array': {'startEA': 134643460, 'sclass': 12, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 10, 'type': 3, 'color': 4294967295}, '.jcr': {'startEA': 134643464, 'sclass': 12, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 11, 'type': 3, 'color': 4294967295}, '.got': {'startEA': 134643708, 'sclass': 12, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 12, 'type': 3, 'color': 4294967295}, '.got.plt': {'startEA': 134643712, 'sclass': 12, 'orgbase': 0, 'align': 5, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 13, 'type': 3, 'color': 4294967295}, '.data': {'startEA': 134644192, 'sclass': 12, 'orgbase': 0, 'align': 8, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 14, 'type': 3, 'color': 4294967295}, '.bss': {'startEA': 134644608, 'sclass': 19, 'orgbase': 0, 'align': 9, 'comb': 2, 'perm': 6, 'bitness': 1, 'flags': 16, 'sel': 15, 'type': 9, 'color': 4294967295}, 'extern': {'startEA': 134647736, 'sclass': 0, 'orgbase': 0, 'align': 3, 'comb': 2, 'perm': 0, 'bitness': 1, 'flags': 16, 'sel': 16, 'type': 1, 'color': 4294967295}}
    meadow_segs_b63eb1f = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](meadow_elf_idb_local_46c7521).segments
    meadow_strs_2eac2ed = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'].SegStrings(meadow_elf_idb_local_46c7521))['strings']
    for meadow_seg_local_29f004f in meadow_segs_b63eb1f.values():
        meadow_segname_ef89c04 = meadow_strs_2eac2ed[_name_boundary.attributes(meadow_seg_local_29f004f)['name_index']]
        meadow_expected_seg_78a0dbd = meadow_EXPECTED_a0db5ab[meadow_segname_ef89c04]
        for meadow_k_b4d95ff, meadow_v_10701fb in meadow_expected_seg_78a0dbd.items():
            assert meadow_v_10701fb == _name_boundary.read_attribute(meadow_seg_local_29f004f, meadow_k_b4d95ff)

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a579e15', 'expected': 'meadow_expected_1933be4', 'kernel32_idb': 'meadow_kernel32_idb_local_c49441e', 'version': 'meadow_version_local_607bffe'}, 'test_imports')
def meadow_test_imports(meadow_kernel32_idb_local_c49441e, meadow_version_local_607bffe, meadow_bitness_a579e15, meadow_expected_1933be4):
    meadow_imports_c8f1db1 = list(_name_boundary.attributes(meadow_idb)['analysis'].enumerate_imports(meadow_kernel32_idb_local_c49441e))
    assert len(meadow_imports_c8f1db1) == 1116
    assert ('api-ms-win-core-rtlsupport-l1-2-0', 'RtlCaptureContext', 1755172864) in meadow_imports_c8f1db1
    meadow_libs_abc7cc2 = set([])
    for meadow_imp_c5adac4 in meadow_imports_c8f1db1:
        meadow_libs_abc7cc2.add(meadow_imp_c5adac4.library)
    assert 'KERNELBASE' in meadow_libs_abc7cc2
    assert 'ntdll' in meadow_libs_abc7cc2

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_afa6da2', 'expected': 'meadow_expected_d194863', 'kernel32_idb': 'meadow_kernel32_idb_local_48c57f6', 'version': 'meadow_version_local_063bdd4'}, 'test_entrypoints2')
def meadow_test_entrypoints2(meadow_kernel32_idb_local_48c57f6, meadow_version_local_063bdd4, meadow_bitness_afa6da2, meadow_expected_d194863):
    meadow_entrypoints_17ef4a2 = list(_name_boundary.attributes(meadow_idb)['analysis'].enumerate_entrypoints(meadow_kernel32_idb_local_48c57f6))
    assert len(meadow_entrypoints_17ef4a2) == 1572
    assert meadow_entrypoints_17ef4a2[0] == ('BaseThreadInitThunk', 1754273581, 1, None)
    if meadow_version_local_063bdd4 > 680:
        assert meadow_entrypoints_17ef4a2[-100] == ('WaitForThreadpoolWorkCallbacks', 1755163473, 1473, 'NTDLL.TpWaitForWork')
    else:
        assert meadow_entrypoints_17ef4a2[-100] == ('WaitForThreadpoolWorkCallbacks', 1755163473, 1473, None)
    if meadow_version_local_063bdd4 <= 700 or meadow_version_local_063bdd4 >= 760:
        assert meadow_entrypoints_17ef4a2[-1] == ('DllEntryPoint', 1754273430, None, None)
    else:
        assert meadow_entrypoints_17ef4a2[-1] == ('_BaseDllInitialize@12', 1754273430, None, None)

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_ea73ca9', 'expected': 'meadow_expected_fd41d8d', 'kernel32_idb': 'meadow_kernel32_idb_local_115437b', 'version': 'meadow_version_local_b6bfa83'}, 'test_idainfo')
def meadow_test_idainfo(meadow_kernel32_idb_local_115437b, meadow_version_local_b6bfa83, meadow_bitness_ea73ca9, meadow_expected_fd41d8d):
    meadow_idainfo_7dcb470 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_kernel32_idb_local_115437b).idainfo
    if meadow_version_local_b6bfa83 == 695:
        assert meadow_idainfo_7dcb470.tag == 'IDA'
    elif meadow_version_local_b6bfa83 == 700:
        assert meadow_idainfo_7dcb470.tag == 'ida'
    assert 480 <= meadow_idainfo_7dcb470.version <= 760
    assert meadow_idainfo_7dcb470.procname == 'metapc'
    assert meadow_idainfo_7dcb470.filetype == 11
    if meadow_version_local_b6bfa83 <= 695:
        assert meadow_idainfo_7dcb470.af == 65535
        assert meadow_idainfo_7dcb470.ascii_break == ord('\n')
        if meadow_version_local_b6bfa83 == 630:
            assert meadow_idainfo_7dcb470.compiler == 129
        else:
            assert meadow_idainfo_7dcb470.compiler == 1
        assert meadow_idainfo_7dcb470.sizeof_int == 4
        assert meadow_idainfo_7dcb470.sizeof_bool in (1, 4)
        assert meadow_idainfo_7dcb470.sizeof_long == 4
        assert meadow_idainfo_7dcb470.sizeof_llong == 8
        if meadow_version_local_b6bfa83 > 500:
            assert meadow_idainfo_7dcb470.sizeof_ldbl == 8
    elif meadow_version_local_b6bfa83 >= 700:
        assert meadow_idainfo_7dcb470.af == 3758096375
        assert meadow_idainfo_7dcb470.strlit_break == ord('\n')
        assert meadow_idainfo_7dcb470.maxref == 16
        assert meadow_idainfo_7dcb470.netdelta == 0
        assert meadow_idainfo_7dcb470.xrefflag == 15
        assert meadow_idainfo_7dcb470.cc_id == 1
        assert meadow_idainfo_7dcb470.cc_size_i == 4
        assert meadow_idainfo_7dcb470.cc_size_b == 1
        assert meadow_idainfo_7dcb470.cc_size_l == 4
        assert meadow_idainfo_7dcb470.cc_size_ll == 8
        assert meadow_idainfo_7dcb470.cc_size_ldbl == 8

@_name_boundary.callable_contract({}, 'test_idainfo_multibitness')
def meadow_test_idainfo_multibitness():
    meadow_cd_9260673 = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_af11115 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_9260673, 'data', 'multibitness', 'multibitness.idb')
    with meadow_idb.from_file(meadow_idbpath_af11115) as meadow_db_280bc6c:
        meadow_idainfo_3269e60 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_db_280bc6c).idainfo
        assert meadow_idainfo_3269e60.tag == 'IDA'
        assert meadow_idainfo_3269e60.version == 700
        assert meadow_idainfo_3269e60.procname == 'metapc'
_name_boundary.module_contract(globals(), {'test_root': 'meadow_test_root', 'pluck': 'meadow_pluck', 're': 'meadow_re', 'test_root_timestamp': 'meadow_test_root_timestamp', 'functools': 'meadow_functools', 'test_stack_change_points': 'meadow_test_stack_change_points', 'test_idainfo': 'meadow_test_idainfo', 'test_function': 'meadow_test_function', 'test_segments2': 'meadow_test_segments2', 'test_function_usercall': 'meadow_test_function_usercall', 'lpluck': 'meadow_lpluck', 'test_struct': 'meadow_test_struct', 'test_xrefs': 'meadow_test_xrefs', 'test_root_open_count': 'meadow_test_root_open_count', 'test_entrypoints2': 'meadow_test_entrypoints2', 'test_idainfo_multibitness': 'meadow_test_idainfo_multibitness', 'test_segstrings': 'meadow_test_segstrings', 'idb': 'meadow_idb', 'get_fn_signature': 'meadow_get_fn_signature', 'test_loader': 'meadow_test_loader', 'test_fileregions': 'meadow_test_fileregions', 'test_function_frame': 'meadow_test_function_frame', 'test_functions': 'meadow_test_functions', 'test_fixups': 'meadow_test_fixups', 'test_imports': 'meadow_test_imports', 'test_segments': 'meadow_test_segments', 'fullmatch': 'meadow_fullmatch'})
