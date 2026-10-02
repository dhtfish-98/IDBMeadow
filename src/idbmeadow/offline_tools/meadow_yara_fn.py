# Derived from scripts/yara_fn.py; original copyright and license retained in ORIGIN.md.
"""
IDAPython script that generates a YARA rule to match against the
basic blocks of the current function. It masks out relocation bytes
and ignores jump instructions (given that we're already trying to
match compiler-specific bytes, this is of arguable benefit).

If python-yara is installed, the IDAPython script also validates that
the generated rule matches at least one segment in the current file.

author: Willi Ballenthin <william.ballenthin@fireeye.com>
"""
import idbmeadow.api_contract as _name_boundary
import logging as meadow_logging
from collections import namedtuple as meadow_namedtuple
import idc as meadow_idc
import idaapi as meadow_idaapi
import idautils as meadow_idautils
import ida_funcs as meadow_ida_funcs
meadow_logger = meadow_logging.getLogger(__name__)
meadow_BasicBlock = _name_boundary.named_record('BasicBlock', ['va', 'size'])
meadow_MIN_BB_BYTE_COUNT = 4

@_name_boundary.callable_contract({'fva': 'meadow_fva_74d8206'}, 'get_basic_blocks')
def meadow_get_basic_blocks(meadow_fva_74d8206):
    """
    return sequence of `BasicBlock` instances for given function.
    """
    meadow_ret_local_738808b = []
    meadow_func_f78e23d = _name_boundary.attributes(meadow_ida_funcs)['get_func'](meadow_fva_74d8206)
    if meadow_func_f78e23d is None:
        return meadow_ret_local_738808b
    for meadow_bb_3fefc28 in _name_boundary.attributes(meadow_idaapi)['FlowChart'](meadow_func_f78e23d):
        meadow_ret_local_738808b.append(meadow_BasicBlock(va=_name_boundary.attributes(meadow_bb_3fefc28)['startEA'], size=_name_boundary.attributes(meadow_bb_3fefc28)['endEA'] - _name_boundary.attributes(meadow_bb_3fefc28)['startEA']))
    return meadow_ret_local_738808b

@_name_boundary.callable_contract({'va': 'meadow_va_d93b5d1'}, 'get_function')
def meadow_get_function(meadow_va_d93b5d1):
    """
    return va for first instruction in function that contains given va.
    """
    return _name_boundary.attributes(_name_boundary.attributes(meadow_ida_funcs)['get_func'](meadow_va_d93b5d1))['startEA']
meadow_Rule = _name_boundary.named_record('Rule', ['name', 'bytes', 'masked_bytes'])

@_name_boundary.callable_contract({'va': 'meadow_va_b42ed42'}, 'is_jump')
def meadow_is_jump(meadow_va_b42ed42):
    """
    return True if the instruction at the given address appears to be a jump.
    """
    return _name_boundary.attributes(meadow_idc)['GetMnem'](meadow_va_b42ed42).startswith('j')

@_name_boundary.callable_contract({'b': 'meadow_b_local_fbb5b10'}, 'bord')
def meadow_bord(meadow_b_local_fbb5b10):
    if isinstance(meadow_b_local_fbb5b10, int):
        return meadow_b_local_fbb5b10
    else:
        return ord(meadow_b_local_fbb5b10)

@_name_boundary.callable_contract({'bb': 'meadow_bb_cf686e7'}, 'get_basic_block_rule')
def meadow_get_basic_block_rule(meadow_bb_cf686e7):
    """
    create and format a YARA rule for a single basic block.
    mask relocation bytes into unknown bytes (like '??').
    do not include final instructions if they are jumps.
    """
    meadow_insns_abf8acb = []
    meadow_va_7660ae4 = meadow_bb_cf686e7.va
    while meadow_va_7660ae4 < meadow_bb_cf686e7.va + meadow_bb_cf686e7.size:
        meadow_insns_abf8acb.append(meadow_va_7660ae4)
        meadow_va_7660ae4 = _name_boundary.attributes(meadow_idc)['NextHead'](meadow_va_7660ae4)
    if meadow_is_jump(meadow_insns_abf8acb[-1]):
        meadow_insns_abf8acb = meadow_insns_abf8acb[:-1]
    meadow_bytes_becb323 = []
    meadow_masked_bytes_b238129 = []
    for meadow_va_7660ae4 in meadow_insns_abf8acb:
        meadow_size_local_8fa9f87 = _name_boundary.attributes(meadow_idc)['ItemSize'](meadow_va_7660ae4)
        if _name_boundary.attributes(meadow_idaapi)['contains_fixups'](meadow_va_7660ae4, meadow_size_local_8fa9f87):
            meadow_fixups_104c043 = []
            meadow_fixupva_41ef110 = _name_boundary.attributes(meadow_idaapi)['get_next_fixup_ea'](meadow_va_7660ae4)
            meadow_fixups_104c043.append(meadow_fixupva_41ef110)
            meadow_fixupva_41ef110 += 4
            while meadow_fixupva_41ef110 < meadow_va_7660ae4 + meadow_size_local_8fa9f87:
                meadow_fixupva_41ef110 = _name_boundary.attributes(meadow_idaapi)['get_next_fixup_ea'](meadow_fixupva_41ef110)
                meadow_fixups_104c043.append(meadow_fixupva_41ef110)
                meadow_fixupva_41ef110 += 4
            meadow_fixup_byte_addrs_3d02dc4 = set([])
            for meadow_fixup_a101042 in meadow_fixups_104c043:
                for meadow_i_6c6a789 in range(meadow_fixup_a101042, meadow_fixup_a101042 + 4):
                    meadow_fixup_byte_addrs_3d02dc4.add(meadow_i_6c6a789)
            for meadow_i_6c6a789, meadow_byte_d58ba16 in enumerate(_name_boundary.attributes(meadow_idc)['GetManyBytes'](meadow_va_7660ae4, meadow_size_local_8fa9f87)):
                meadow_byte_addr_161b59c = meadow_i_6c6a789 + meadow_va_7660ae4
                if meadow_byte_addr_161b59c in meadow_fixup_byte_addrs_3d02dc4:
                    meadow_bytes_becb323.append(meadow_bord(meadow_byte_d58ba16))
                    meadow_masked_bytes_b238129.append('??')
                else:
                    meadow_bytes_becb323.append(meadow_bord(meadow_byte_d58ba16))
                    meadow_masked_bytes_b238129.append('%02X' % meadow_bord(meadow_byte_d58ba16))
        elif 'call' in _name_boundary.attributes(meadow_idc)['GetMnem'](meadow_va_7660ae4):
            for meadow_i_6c6a789, meadow_byte_d58ba16 in enumerate(_name_boundary.attributes(meadow_idc)['GetManyBytes'](meadow_va_7660ae4, meadow_size_local_8fa9f87)):
                meadow_bytes_becb323.append(meadow_bord(meadow_byte_d58ba16))
                meadow_masked_bytes_b238129.append('??')
        else:
            for meadow_byte_d58ba16 in _name_boundary.attributes(meadow_idc)['GetManyBytes'](meadow_va_7660ae4, meadow_size_local_8fa9f87):
                meadow_bytes_becb323.append(meadow_bord(meadow_byte_d58ba16))
                meadow_masked_bytes_b238129.append('%02X' % meadow_bord(meadow_byte_d58ba16))
    return meadow_Rule('$0x%x' % meadow_bb_cf686e7.va, meadow_bytes_becb323, meadow_masked_bytes_b238129)

@_name_boundary.callable_contract({'fva': 'meadow_fva_4635cad', 'rules': 'meadow_rules_154e791'}, 'format_rules')
def meadow_format_rules(meadow_fva_4635cad, meadow_rules_154e791):
    """
    given the address of a function, and the byte signatures for basic blocks in
     the function, format a complete YARA rule that matches all of the
     basic block signatures.
    """
    meadow_name_local_84fe0d0 = _name_boundary.attributes(meadow_idc)['GetFunctionName'](meadow_fva_4635cad)
    meadow_safe_name_7558a43 = meadow_name_local_84fe0d0
    meadow_BAD_CHARS_5633602 = '@ /\\!@#$%^&*()[]{};:\'",./<>?'
    for meadow_c_local_4bb9473 in meadow_BAD_CHARS_5633602:
        meadow_safe_name_7558a43 = meadow_safe_name_7558a43.replace(meadow_c_local_4bb9473, '')
    meadow_md5_8345d97 = _name_boundary.attributes(meadow_idautils)['GetInputFileMD5']()
    meadow_ret_local_f1d4b1e = []
    meadow_ret_local_f1d4b1e.append('rule a_%s_%s {' % (meadow_md5_8345d97, meadow_safe_name_7558a43))
    meadow_ret_local_f1d4b1e.append('  meta:')
    meadow_ret_local_f1d4b1e.append('    sample_md5 = "%s"' % meadow_md5_8345d97)
    meadow_ret_local_f1d4b1e.append('    function_address = "0x%x"' % meadow_fva_4635cad)
    meadow_ret_local_f1d4b1e.append('    function_name = "%s"' % meadow_name_local_84fe0d0)
    meadow_ret_local_f1d4b1e.append('  strings:')
    for meadow_rule_646455b in meadow_rules_154e791:
        meadow_formatted_rule_26d1c8b = ' '.join(meadow_rule_646455b.masked_bytes)
        meadow_ret_local_f1d4b1e.append('    %s = { %s }' % (meadow_rule_646455b.name, meadow_formatted_rule_26d1c8b))
    meadow_ret_local_f1d4b1e.append('  condition:')
    meadow_ret_local_f1d4b1e.append('    all of them')
    meadow_ret_local_f1d4b1e.append('}')
    return '\n'.join(meadow_ret_local_f1d4b1e)

@_name_boundary.callable_contract({'fva': 'meadow_fva_03a9fc8'}, 'create_yara_rule_for_function')
def meadow_create_yara_rule_for_function(meadow_fva_03a9fc8):
    """
    given the address of a function, generate and format a complete YARA rule
     that matches the basic blocks.
    """
    meadow_rules_0f5d4cc = []
    for meadow_bb_2b25175 in meadow_get_basic_blocks(meadow_fva_03a9fc8):
        meadow_rule_a2b08bd = meadow_get_basic_block_rule(meadow_bb_2b25175)
        meadow_unmasked_count_db76d1e = len(list(filter(_name_boundary.callable_contract({'b': 'meadow_b_local_553a59c'}, '<lambda>')(lambda meadow_b_local_553a59c: meadow_b_local_553a59c != '??'), meadow_rule_a2b08bd.masked_bytes)))
        if meadow_unmasked_count_db76d1e < meadow_MIN_BB_BYTE_COUNT:
            continue
        meadow_rules_0f5d4cc.append(meadow_rule_a2b08bd)
    return meadow_format_rules(meadow_fva_03a9fc8, meadow_rules_0f5d4cc)

@_name_boundary.callable_contract({'segstart': 'meadow_segstart_2ce8e74'}, 'get_segment_buffer')
def meadow_get_segment_buffer(meadow_segstart_2ce8e74):
    """
    fetch the bytes of the section that starts at the given address.
    if the entire section cannot be accessed, try smaller regions until it works.
    """
    meadow_segend_23c52c9 = _name_boundary.attributes(_name_boundary.attributes(meadow_idaapi)['getseg'](meadow_segstart_2ce8e74))['endEA']
    meadow_buf_local_d385f21 = None
    meadow_segsize_15166d0 = meadow_segend_23c52c9 - meadow_segstart_2ce8e74
    while meadow_buf_local_d385f21 is None:
        meadow_buf_local_d385f21 = _name_boundary.attributes(meadow_idc)['GetManyBytes'](meadow_segstart_2ce8e74, meadow_segsize_15166d0 - 1)
        if meadow_buf_local_d385f21 is None:
            meadow_segsize_15166d0 -= 4096
    return meadow_buf_local_d385f21
meadow_Segment = _name_boundary.named_record('Segment', ['start', 'size', 'name', 'buf'])

@_name_boundary.callable_contract({}, 'get_segments')
def meadow_get_segments():
    """
    fetch the segments in the current executable.
    """
    for meadow_segstart_6d23d76 in _name_boundary.attributes(meadow_idautils)['Segments']():
        meadow_segend_7922df3 = _name_boundary.attributes(_name_boundary.attributes(meadow_idaapi)['getseg'](meadow_segstart_6d23d76))['endEA']
        meadow_segsize_188bc6c = meadow_segend_7922df3 - meadow_segstart_6d23d76
        meadow_segname_e7f8142 = str(_name_boundary.attributes(meadow_idc)['SegName'](meadow_segstart_6d23d76)).rstrip('\x00')
        meadow_segbuf_b40dc8c = meadow_get_segment_buffer(meadow_segstart_6d23d76)
        yield meadow_Segment(meadow_segstart_6d23d76, meadow_segend_7922df3, meadow_segname_e7f8142, meadow_segbuf_b40dc8c)

@_name_boundary.class_contract('TestDidntRunError', {})
class meadow_TestDidntRunError(Exception):
    pass

@_name_boundary.callable_contract({'rule': 'meadow_rule_7276971'}, 'test_yara_rule')
def meadow_test_yara_rule(meadow_rule_7276971):
    """
    try to match the given rule against each segment in the current exectuable.
    raise TestDidntRunError if its not possible to import the YARA library.
    return True if there's at least one match, False otherwise.
    """
    try:
        import yara as meadow_yara_49c29b0
    except ImportError:
        meadow_logger.warning("can't test rule: failed to import python-yara")
        raise meadow_TestDidntRunError('python-yara not available')
    meadow_r_4a51b02 = meadow_yara_49c29b0.compile(source=meadow_rule_7276971)
    for meadow_segment_local_0f7d30e in meadow_get_segments():
        meadow_matches_c745b9a = meadow_r_4a51b02.match(data=meadow_segment_local_0f7d30e.buf)
        if len(meadow_matches_c745b9a) > 0:
            meadow_logger.info('generated rule matches section: {:s}'.format(meadow_segment_local_0f7d30e.name))
            return True
    return False

@_name_boundary.callable_contract({}, 'main')
def meadow_main():
    meadow_va_b774944 = _name_boundary.attributes(meadow_idc)['ScreenEA']()
    meadow_fva_aff8c28 = meadow_get_function(meadow_va_b774944)
    meadow_rule_086521b = meadow_create_yara_rule_for_function(meadow_fva_aff8c28)
    print(meadow_rule_086521b)
    if meadow_test_yara_rule(meadow_rule_086521b):
        print('success: validated the generated rule')
    else:
        print('error: failed to validate generated rule')
if __name__ == '__main__':
    meadow_logging.basicConfig(level=meadow_logging.INFO)
    meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    meadow_main()
_name_boundary.module_contract(globals(), {'BasicBlock': 'meadow_BasicBlock', 'format_rules': 'meadow_format_rules', 'idc': 'meadow_idc', 'idaapi': 'meadow_idaapi', 'logger': 'meadow_logger', 'TestDidntRunError': 'meadow_TestDidntRunError', 'namedtuple': 'meadow_namedtuple', 'MIN_BB_BYTE_COUNT': 'meadow_MIN_BB_BYTE_COUNT', 'get_segment_buffer': 'meadow_get_segment_buffer', 'bord': 'meadow_bord', 'create_yara_rule_for_function': 'meadow_create_yara_rule_for_function', 'get_function': 'meadow_get_function', 'Rule': 'meadow_Rule', 'Segment': 'meadow_Segment', 'get_basic_blocks': 'meadow_get_basic_blocks', 'is_jump': 'meadow_is_jump', 'test_yara_rule': 'meadow_test_yara_rule', 'get_basic_block_rule': 'meadow_get_basic_block_rule', 'get_segments': 'meadow_get_segments', 'logging': 'meadow_logging', 'ida_funcs': 'meadow_ida_funcs', 'idautils': 'meadow_idautils', 'main': 'meadow_main'})
