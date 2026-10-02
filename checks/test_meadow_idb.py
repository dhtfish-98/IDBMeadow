# Derived from tests/test_idb.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import binascii as meadow_binascii
from checks.fixture_registry import *
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
import idbmeadow.database_pages as _boundary_import_idb_fileformat
import idbmeadow as meadow_idb

@_name_boundary.callable_contract({'somehex': 'meadow_somehex_b5eb3d2'}, 'h2b')
def meadow_h2b(meadow_somehex_b5eb3d2):
    """
    convert the given hex string into bytes.

    binascii.unhexlify is many more characters to type :-).
    """
    return meadow_binascii.unhexlify(meadow_somehex_b5eb3d2)

@_name_boundary.callable_contract({'somebytes': 'meadow_somebytes_b4d39b3'}, 'b2h')
def meadow_b2h(meadow_somebytes_b4d39b3):
    """
    convert the given bytes into a hex *string*.

    binascii.hexlify returns a bytes, which is slightly annoying.
    also, its many more characters to type.
    """
    return meadow_binascii.hexlify(meadow_somebytes_b4d39b3).decode('ascii')

@_name_boundary.callable_contract({'number': 'meadow_number_b63cf06'}, 'h')
def meadow_h(meadow_number_b63cf06):
    """
    convert a number to a hex representation, with no leading '0x'.

    Example::

        assert h(16)   == '10'
        assert hex(16) == '0x10'
    """
    return '%02x' % meadow_number_b63cf06

@meadow_kern32_test([(695, 32, 4), (695, 64, 8), (700, 32, 4), (700, 64, 8)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_76f5a6a', 'expected': 'meadow_expected_15059dd', 'kernel32_idb': 'meadow_kernel32_idb_local_de180b2', 'version': 'meadow_version_local_741aec5'}, 'test_wordsize')
def meadow_test_wordsize(meadow_kernel32_idb_local_de180b2, meadow_version_local_741aec5, meadow_bitness_76f5a6a, meadow_expected_15059dd):
    assert meadow_kernel32_idb_local_de180b2.wordsize == meadow_expected_15059dd

@meadow_kern32_test([(695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_d0b83ca', 'expected': 'meadow_expected_c86f8ad', 'kernel32_idb': 'meadow_kernel32_idb_local_f4b8f73', 'version': 'meadow_version_local_66b5133'}, 'test_validate')
def meadow_test_validate(meadow_kernel32_idb_local_f4b8f73, meadow_version_local_66b5133, meadow_bitness_d0b83ca, meadow_expected_c86f8ad):
    assert _name_boundary.attributes(meadow_kernel32_idb_local_f4b8f73)['validate']() is True

@_name_boundary.callable_contract({'db': 'meadow_db_6936115'}, 'do_test_compressed')
def meadow_do_test_compressed(meadow_db_6936115):
    for meadow_section_local_a0fcdb0 in meadow_db_6936115.sections:
        if meadow_section_local_a0fcdb0 is None:
            continue
        assert meadow_section_local_a0fcdb0.header.is_compressed is True
        assert meadow_section_local_a0fcdb0.header.compression_method == _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['fileformat'])['COMPRESSION_METHOD'])['ZLIB']
    assert _name_boundary.attributes(meadow_db_6936115)['validate']() is True

@_name_boundary.callable_contract({'compressed_idb': 'meadow_compressed_idb_local_032f28b', 'compressed_i64': 'meadow_compressed_i64_local_2c6b99f'}, 'test_compressed')
def meadow_test_compressed(meadow_compressed_idb_local_032f28b, meadow_compressed_i64_local_2c6b99f):
    meadow_do_test_compressed(meadow_compressed_idb_local_032f28b)
    meadow_do_test_compressed(meadow_compressed_i64_local_2c6b99f)

@meadow_kern32_test([(695, 32, b'IDA1'), (695, 64, b'IDA2'), (700, 32, b'IDA1'), (700, 64, b'IDA2')])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_b71b1a2', 'expected': 'meadow_expected_571f485', 'kernel32_idb': 'meadow_kernel32_idb_local_2701f54', 'version': 'meadow_version_local_2b3a513'}, 'test_header_magic')
def meadow_test_header_magic(meadow_kernel32_idb_local_2701f54, meadow_version_local_2b3a513, meadow_bitness_b71b1a2, meadow_expected_571f485):
    assert meadow_kernel32_idb_local_2701f54.header.signature == meadow_expected_571f485
    assert meadow_kernel32_idb_local_2701f54.header.sig2 == 2864434397

@meadow_kern32_test([(695, 32, 8192), (695, 64, 8192), (700, 32, 8192), (700, 64, 8192)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_eac0eb5', 'expected': 'meadow_expected_a1a055e', 'kernel32_idb': 'meadow_kernel32_idb_local_69f5faa', 'version': 'meadow_version_local_c6237fb'}, 'test_id0_page_size')
def meadow_test_id0_page_size(meadow_kernel32_idb_local_69f5faa, meadow_version_local_c6237fb, meadow_bitness_eac0eb5, meadow_expected_a1a055e):
    assert meadow_kernel32_idb_local_69f5faa.id0.page_size == meadow_expected_a1a055e

@meadow_kern32_test([(695, 32, 1), (695, 64, 1), (700, 32, 1), (700, 64, 1)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_452f228', 'expected': 'meadow_expected_ad58529', 'kernel32_idb': 'meadow_kernel32_idb_local_3b066c0', 'version': 'meadow_version_local_e03baaa'}, 'test_id0_root_page')
def meadow_test_id0_root_page(meadow_kernel32_idb_local_3b066c0, meadow_version_local_e03baaa, meadow_bitness_452f228, meadow_expected_ad58529):
    assert meadow_kernel32_idb_local_3b066c0.id0.root_page == meadow_expected_ad58529

@meadow_kern32_test([(695, 32, 1592), (695, 64, 1979), (700, 32, 1566), (700, 64, 1884)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_4883fa5', 'expected': 'meadow_expected_775a1e9', 'kernel32_idb': 'meadow_kernel32_idb_local_3964e44', 'version': 'meadow_version_local_f5aa964'}, 'test_id0_page_count')
def meadow_test_id0_page_count(meadow_kernel32_idb_local_3964e44, meadow_version_local_f5aa964, meadow_bitness_4883fa5, meadow_expected_775a1e9):
    assert meadow_kernel32_idb_local_3964e44.id0.page_count == meadow_expected_775a1e9

@meadow_kern32_test([(695, 32, 422747), (695, 64, 422753), (700, 32, 426644), (700, 64, 426647)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_cb35c54', 'expected': 'meadow_expected_f0a1579', 'kernel32_idb': 'meadow_kernel32_idb_local_8719f96', 'version': 'meadow_version_local_4e6be2c'}, 'test_id0_record_count')
def meadow_test_id0_record_count(meadow_kernel32_idb_local_8719f96, meadow_version_local_4e6be2c, meadow_bitness_cb35c54, meadow_expected_f0a1579):
    assert meadow_kernel32_idb_local_8719f96.id0.record_count == meadow_expected_f0a1579

@meadow_kern32_test([(695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f2f605f', 'expected': 'meadow_expected_d396b62', 'kernel32_idb': 'meadow_kernel32_idb_local_904e136', 'version': 'meadow_version_local_7fa962e'}, 'test_id0_root_entries')
def meadow_test_id0_root_entries(meadow_kernel32_idb_local_904e136, meadow_version_local_7fa962e, meadow_bitness_f2f605f, meadow_expected_d396b62):
    """
    Args:
      expected: ignored
    """
    for meadow_entry_local_8a384cf in _name_boundary.attributes(_name_boundary.attributes(meadow_kernel32_idb_local_904e136.id0)['get_page'](meadow_kernel32_idb_local_904e136.id0.root_page))['get_entries']():
        assert meadow_entry_local_8a384cf.key is not None

@meadow_kern32_test([(695, 32, '24204d4158204c494e4b'), (695, 64, '24204d4158204c494e4b'), (700, 32, '24204d4158204c494e4b'), (700, 64, '24204d4158204c494e4b')])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_552a716', 'expected': 'meadow_expected_7d2f471', 'kernel32_idb': 'meadow_kernel32_idb_local_eeb4e1e', 'version': 'meadow_version_local_90ac0dd'}, 'test_cursor_min')
def meadow_test_cursor_min(meadow_kernel32_idb_local_eeb4e1e, meadow_version_local_90ac0dd, meadow_bitness_552a716, meadow_expected_7d2f471):
    meadow_minkey_56fb792 = _name_boundary.attributes(meadow_kernel32_idb_local_eeb4e1e.id0)['get_min']().key
    assert meadow_minkey_56fb792 == meadow_h2b(meadow_expected_7d2f471)
    meadow_cursor_20c7ca8 = _name_boundary.attributes(meadow_kernel32_idb_local_eeb4e1e.id0)['find'](meadow_minkey_56fb792)
    _name_boundary.attributes(meadow_cursor_20c7ca8)['next']()
    assert meadow_b2h(meadow_cursor_20c7ca8.key) == '24204d4158204e4f4445'
    _name_boundary.attributes(meadow_cursor_20c7ca8)['prev']()
    assert meadow_b2h(meadow_cursor_20c7ca8.key) == '24204d4158204c494e4b'
    with meadow_pytest.raises(IndexError):
        _name_boundary.attributes(meadow_cursor_20c7ca8)['prev']()

@meadow_kern32_test([(695, 32, '4e776373737472'), (695, 64, '4e776373737472'), (700, 32, '4e776373737472'), (700, 64, '4e776373737472')])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_47c00a3', 'expected': 'meadow_expected_a4ba928', 'kernel32_idb': 'meadow_kernel32_idb_local_8a628d5', 'version': 'meadow_version_local_c37f021'}, 'test_cursor_max')
def meadow_test_cursor_max(meadow_kernel32_idb_local_8a628d5, meadow_version_local_c37f021, meadow_bitness_47c00a3, meadow_expected_a4ba928):
    meadow_maxkey_e4eb438 = _name_boundary.attributes(meadow_kernel32_idb_local_8a628d5.id0)['get_max']().key
    assert meadow_maxkey_e4eb438 == meadow_h2b(meadow_expected_a4ba928)
    meadow_cursor_bf915f1 = _name_boundary.attributes(meadow_kernel32_idb_local_8a628d5.id0)['find'](meadow_maxkey_e4eb438)
    _name_boundary.attributes(meadow_cursor_bf915f1)['prev']()
    assert meadow_b2h(meadow_cursor_bf915f1.key) == '4e77637372636872'
    _name_boundary.attributes(meadow_cursor_bf915f1)['next']()
    assert meadow_b2h(meadow_cursor_bf915f1.key) == '4e776373737472'
    with meadow_pytest.raises(IndexError):
        _name_boundary.attributes(meadow_cursor_bf915f1)['next']()

@meadow_kern32_test([(695, 32, None), (700, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_3982d6d', 'expected': 'meadow_expected_9164778', 'kernel32_idb': 'meadow_kernel32_idb_local_702a5d7', 'version': 'meadow_version_local_9ca88a1'}, 'test_find_exact_match1')
def meadow_test_find_exact_match1(meadow_kernel32_idb_local_702a5d7, meadow_version_local_9ca88a1, meadow_bitness_3982d6d, meadow_expected_9164778):
    meadow_key_local_6c720a4 = meadow_h2b('2e6892663778689c4fb7')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_702a5d7.id0)['find'](meadow_key_local_6c720a4).key == meadow_key_local_6c720a4
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_702a5d7.id0)['find'](meadow_key_local_6c720a4).value) == '13'

@meadow_kern32_test([(695, 32, None), (700, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_bcb52c2', 'expected': 'meadow_expected_b64453e', 'kernel32_idb': 'meadow_kernel32_idb_local_797711d', 'version': 'meadow_version_local_4b6580e'}, 'test_find_exact_match2')
def meadow_test_find_exact_match2(meadow_kernel32_idb_local_797711d, meadow_version_local_4b6580e, meadow_bitness_bcb52c2, meadow_expected_b64453e):
    meadow_key_local_6356db9 = meadow_h2b('2e689017765300000009')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_797711d.id0)['find'](meadow_key_local_6356db9).key == meadow_key_local_6356db9
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_797711d.id0)['find'](meadow_key_local_6356db9).value) == '02'

@meadow_kern32_test([(695, 32, '24204636383931344133462e6c705375624b6579'), (700, 32, '24204636383931344132452e6c705265736572766564')])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a18adff', 'expected': 'meadow_expected_67fce36', 'kernel32_idb': 'meadow_kernel32_idb_local_9ae6b1e', 'version': 'meadow_version_local_95047f1'}, 'test_find_exact_match3')
def meadow_test_find_exact_match3(meadow_kernel32_idb_local_9ae6b1e, meadow_version_local_95047f1, meadow_bitness_a18adff, meadow_expected_67fce36):
    meadow_key_local_165decc = meadow_h2b('2eff001bc44e')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_9ae6b1e.id0)['find'](meadow_key_local_165decc).key == meadow_key_local_165decc
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_9ae6b1e.id0)['find'](meadow_key_local_165decc).value) == meadow_expected_67fce36

@meadow_kern32_test([(695, 32, None), (700, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_a65be40', 'expected': 'meadow_expected_4f01c59', 'kernel32_idb': 'meadow_kernel32_idb_local_6283713', 'version': 'meadow_version_local_64e2736'}, 'test_find_exact_match4')
def meadow_test_find_exact_match4(meadow_kernel32_idb_local_6283713, meadow_version_local_64e2736, meadow_bitness_a65be40, meadow_expected_4f01c59):
    meadow_key_local_d064b82 = meadow_h2b('2e6890142c5300001000')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_6283713.id0)['find'](meadow_key_local_d064b82).key == meadow_key_local_d064b82
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_6283713.id0)['find'](meadow_key_local_d064b82).value) == '01080709'

@meadow_kern32_test([(695, 32, None), (700, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_1c87a60', 'expected': 'meadow_expected_8847c6e', 'kernel32_idb': 'meadow_kernel32_idb_local_01f2415', 'version': 'meadow_version_local_38a7cf4'}, 'test_find_exact_match5')
def meadow_test_find_exact_match5(meadow_kernel32_idb_local_01f2415, meadow_version_local_38a7cf4, meadow_bitness_1c87a60, meadow_expected_8847c6e):
    meadow_key_local_de1a856 = meadow_h2b('2e689a288c530000000a')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_01f2415.id0)['find'](meadow_key_local_de1a856).key == meadow_key_local_de1a856
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_01f2415.id0)['find'](meadow_key_local_de1a856).value) == '02'

@meadow_kern32_test([(695, 32, None), (700, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_5eb92a6', 'expected': 'meadow_expected_f327597', 'kernel32_idb': 'meadow_kernel32_idb_local_e910e06', 'version': 'meadow_version_local_966b933'}, 'test_find_exact_match6')
def meadow_test_find_exact_match6(meadow_kernel32_idb_local_e910e06, meadow_version_local_966b933, meadow_bitness_5eb92a6, meadow_expected_f327597):
    meadow_key_local_31d9b63 = meadow_h2b('2e6890157f5300000009')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_e910e06.id0)['find'](meadow_key_local_31d9b63).key == meadow_key_local_31d9b63
    assert meadow_b2h(_name_boundary.attributes(meadow_kernel32_idb_local_e910e06.id0)['find'](meadow_key_local_31d9b63).value) == '02'

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_7644c4e', 'expected': 'meadow_expected_3fac73a', 'kernel32_idb': 'meadow_kernel32_idb_local_bea12d4', 'version': 'meadow_version_local_6d600c2'}, 'test_find_exact_match_min')
def meadow_test_find_exact_match_min(meadow_kernel32_idb_local_bea12d4, meadow_version_local_6d600c2, meadow_bitness_7644c4e, meadow_expected_3fac73a):
    meadow_minkey_1ab6853 = meadow_h2b('24204d4158204c494e4b')
    assert _name_boundary.attributes(meadow_kernel32_idb_local_bea12d4.id0)['find'](meadow_minkey_1ab6853).key == meadow_minkey_1ab6853

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_662caa9', 'expected': 'meadow_expected_b17eac2', 'kernel32_idb': 'meadow_kernel32_idb_local_27579f7', 'version': 'meadow_version_local_f4a8ce6'}, 'test_find_exact_match_max')
def meadow_test_find_exact_match_max(meadow_kernel32_idb_local_27579f7, meadow_version_local_f4a8ce6, meadow_bitness_662caa9, meadow_expected_b17eac2):
    if 500 < meadow_version_local_f4a8ce6 <= 700:
        meadow_maxkey_71bcb9d = meadow_h2b('4e776373737472')
        assert _name_boundary.attributes(meadow_kernel32_idb_local_27579f7.id0)['find'](meadow_maxkey_71bcb9d).key == meadow_maxkey_71bcb9d

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_e9f389f', 'expected': 'meadow_expected_2763ffe', 'kernel32_idb': 'meadow_kernel32_idb_local_ed8c8bb', 'version': 'meadow_version_local_5870be2'}, 'test_find_exact_match_error')
def meadow_test_find_exact_match_error(meadow_kernel32_idb_local_ed8c8bb, meadow_version_local_5870be2, meadow_bitness_e9f389f, meadow_expected_2763ffe):
    with meadow_pytest.raises(KeyError):
        _name_boundary.attributes(meadow_kernel32_idb_local_ed8c8bb.id0)['find'](b'does not exist!')

@meadow_kern32_test([(695, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_9984109', 'expected': 'meadow_expected_35875e4', 'kernel32_idb': 'meadow_kernel32_idb_local_7ac81d3', 'version': 'meadow_version_local_8a072ec'}, 'test_find_prefix')
def meadow_test_find_prefix(meadow_kernel32_idb_local_7ac81d3, meadow_version_local_8a072ec, meadow_bitness_9984109, meadow_expected_35875e4):
    meadow_fixup_nodeid_4a0e677 = '2eff000006'
    meadow_key_local_09f2eca = meadow_h2b(meadow_fixup_nodeid_4a0e677)
    meadow_cursor_0b008da = _name_boundary.attributes(meadow_kernel32_idb_local_7ac81d3.id0)['find_prefix'](meadow_key_local_09f2eca)
    assert meadow_b2h(meadow_cursor_0b008da.key) == meadow_fixup_nodeid_4a0e677 + meadow_h(ord('N'))
    meadow_supvals_8bd97ab = meadow_fixup_nodeid_4a0e677 + meadow_h(ord('S'))
    meadow_key_local_09f2eca = meadow_h2b(meadow_supvals_8bd97ab)
    meadow_cursor_0b008da = _name_boundary.attributes(meadow_kernel32_idb_local_7ac81d3.id0)['find_prefix'](meadow_key_local_09f2eca)
    assert meadow_b2h(meadow_cursor_0b008da.key) == meadow_fixup_nodeid_4a0e677 + meadow_h(ord('S')) + '68901025'
    with meadow_pytest.raises(KeyError):
        meadow_cursor_0b008da = _name_boundary.attributes(meadow_kernel32_idb_local_7ac81d3.id0)['find_prefix'](b'does not exist')

@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f112741', 'expected': 'meadow_expected_6ccf176', 'kernel32_idb': 'meadow_kernel32_idb_local_8e96abe', 'version': 'meadow_version_local_41dd1bc'}, 'test_find_prefix2')
def meadow_test_find_prefix2(meadow_kernel32_idb_local_8e96abe, meadow_version_local_41dd1bc, meadow_bitness_f112741, meadow_expected_6ccf176):
    """
    this test is derived from some issues encountered while doing import analysis.
    ultimately, we're checking prefix matching when the first match is found
     in a branch node.
    """
    meadow_impnn_e6f700a = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_8e96abe, '$ imports')
    meadow_expected_alts_a5ccdd0 = list(range(48))
    meadow_expected_alts_a5ccdd0.append(meadow_kernel32_idb_local_8e96abe.uint(-1))
    assert list(_name_boundary.attributes(meadow_impnn_e6f700a)['alts']()) == meadow_expected_alts_a5ccdd0
    assert list(_name_boundary.attributes(meadow_impnn_e6f700a)['sups']()) == list(range(48))
    meadow_dist_0cdce38 = []
    for meadow_alt_6bae1af in _name_boundary.attributes(meadow_impnn_e6f700a)['alts']():
        if meadow_alt_6bae1af == meadow_kernel32_idb_local_8e96abe.uint(-1):
            break
        meadow_ref_55d847a = _name_boundary.attributes(meadow_idb)['netnode'].as_uint(_name_boundary.attributes(meadow_impnn_e6f700a)['get_val'](meadow_alt_6bae1af, tag='A'))
        meadow_nn_4314605 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_kernel32_idb_local_8e96abe, meadow_ref_55d847a)
        meadow_dist_0cdce38.append((meadow_alt_6bae1af, len(list(_name_boundary.attributes(meadow_nn_4314605)['sups']()))))
    assert meadow_dist_0cdce38 == [(0, 4), (1, 388), (2, 77), (3, 50), (4, 42), (5, 13), (6, 28), (7, 4), (8, 33), (9, 68), (10, 1), (11, 9), (12, 1), (13, 7), (14, 1), (15, 24), (16, 9), (17, 6), (18, 26), (19, 9), (20, 54), (21, 24), (22, 8), (23, 9), (24, 7), (25, 5), (26, 1), (27, 2), (28, 26), (29, 1), (30, 18), (31, 5), (32, 3), (33, 2), (34, 3), (35, 6), (36, 11), (37, 11), (38, 5), (39, 6), (40, 11), (41, 7), (42, 10), (43, 14), (44, 38), (45, 16), (46, 6), (47, 7)]

@meadow_kern32_test([(695, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_7a894ba', 'expected': 'meadow_expected_950e45c', 'kernel32_idb': 'meadow_kernel32_idb_local_acfc442', 'version': 'meadow_version_local_371d5bd'}, 'test_cursor_easy_leaf')
def meadow_test_cursor_easy_leaf(meadow_kernel32_idb_local_acfc442, meadow_version_local_371d5bd, meadow_bitness_7a894ba, meadow_expected_950e45c):
    meadow_key_local_d98912b = meadow_h2b('2eff00002253689cc99b')
    meadow_cursor_e3a3a2e = _name_boundary.attributes(meadow_kernel32_idb_local_acfc442.id0)['find'](meadow_key_local_d98912b)
    _name_boundary.attributes(meadow_cursor_e3a3a2e)['next']()
    assert meadow_b2h(meadow_cursor_e3a3a2e.key) == '2eff00002253689cc9cd'
    _name_boundary.attributes(meadow_cursor_e3a3a2e)['prev']()
    _name_boundary.attributes(meadow_cursor_e3a3a2e)['prev']()
    assert meadow_b2h(meadow_cursor_e3a3a2e.key) == '2eff00002253689cc95b'

@meadow_kern32_test([(695, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_25d051b', 'expected': 'meadow_expected_2c5f03c', 'kernel32_idb': 'meadow_kernel32_idb_local_9736498', 'version': 'meadow_version_local_5bb945d'}, 'test_cursor_branch')
def meadow_test_cursor_branch(meadow_kernel32_idb_local_9736498, meadow_version_local_5bb945d, meadow_bitness_25d051b, meadow_expected_2c5f03c):
    meadow_key_local_386653e = meadow_h2b('2eff00002253689bea8e')
    meadow_cursor_9cc54f2 = _name_boundary.attributes(meadow_kernel32_idb_local_9736498.id0)['find'](meadow_key_local_386653e)
    _name_boundary.attributes(meadow_cursor_9cc54f2)['next']()
    assert meadow_b2h(meadow_cursor_9cc54f2.key) == '2eff00002253689bece5'
    meadow_key_local_386653e = meadow_h2b('2eff00002253689bea8e')
    meadow_cursor_9cc54f2 = _name_boundary.attributes(meadow_kernel32_idb_local_9736498.id0)['find'](meadow_key_local_386653e)
    _name_boundary.attributes(meadow_cursor_9cc54f2)['prev']()
    assert meadow_b2h(meadow_cursor_9cc54f2.key) == '2eff00002253689bea26'

@meadow_kern32_test([(695, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_3bee000', 'expected': 'meadow_expected_5d168fc', 'kernel32_idb': 'meadow_kernel32_idb_local_243f591', 'version': 'meadow_version_local_1e27a7e'}, 'test_cursor_complex_leaf_next')
def meadow_test_cursor_complex_leaf_next(meadow_kernel32_idb_local_243f591, meadow_version_local_1e27a7e, meadow_bitness_3bee000, meadow_expected_5d168fc):
    meadow_key_local_a28d037 = meadow_h2b('2eff00002253689bea26')
    meadow_cursor_ed1e818 = _name_boundary.attributes(meadow_kernel32_idb_local_243f591.id0)['find'](meadow_key_local_a28d037)
    _name_boundary.attributes(meadow_cursor_ed1e818)['next']()
    assert meadow_b2h(meadow_cursor_ed1e818.key) == '2eff00002253689bea8e'

@meadow_kern32_test([(695, 32, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_10580bb', 'expected': 'meadow_expected_698b19a', 'kernel32_idb': 'meadow_kernel32_idb_local_ced7659', 'version': 'meadow_version_local_d66a2da'}, 'test_cursor_complex_leaf_prev')
def meadow_test_cursor_complex_leaf_prev(meadow_kernel32_idb_local_ced7659, meadow_version_local_d66a2da, meadow_bitness_10580bb, meadow_expected_698b19a):
    meadow_key_local_7c8e7bc = meadow_h2b('2eff00002253689bece5')
    meadow_cursor_46c820d = _name_boundary.attributes(meadow_kernel32_idb_local_ced7659.id0)['find'](meadow_key_local_7c8e7bc)
    _name_boundary.attributes(meadow_cursor_46c820d)['prev']()
    assert meadow_b2h(meadow_cursor_46c820d.key) == '2eff00002253689bea8e'

@meadow_pytest.mark.slow
@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_f60a5e3', 'expected': 'meadow_expected_8e3644c', 'kernel32_idb': 'meadow_kernel32_idb_local_6fddae5', 'version': 'meadow_version_local_ccb49ac'}, 'test_cursor_enum_all_asc')
def meadow_test_cursor_enum_all_asc(meadow_kernel32_idb_local_6fddae5, meadow_version_local_ccb49ac, meadow_bitness_f60a5e3, meadow_expected_8e3644c):
    meadow_minkey_92b3464 = _name_boundary.attributes(meadow_kernel32_idb_local_6fddae5.id0)['get_min']().key
    meadow_cursor_7d1048b = _name_boundary.attributes(meadow_kernel32_idb_local_6fddae5.id0)['find'](meadow_minkey_92b3464)
    meadow_count_local_be9e370 = 1
    while True:
        try:
            _name_boundary.attributes(meadow_cursor_7d1048b)['next']()
        except IndexError:
            break
        meadow_count_local_be9e370 += 1
    assert meadow_kernel32_idb_local_6fddae5.id0.record_count == meadow_count_local_be9e370

@meadow_pytest.mark.slow
@meadow_kern32_test()
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_75f442e', 'expected': 'meadow_expected_46d32cb', 'kernel32_idb': 'meadow_kernel32_idb_local_aa14e6b', 'version': 'meadow_version_local_44eb523'}, 'test_cursor_enum_all_desc')
def meadow_test_cursor_enum_all_desc(meadow_kernel32_idb_local_aa14e6b, meadow_version_local_44eb523, meadow_bitness_75f442e, meadow_expected_46d32cb):
    meadow_maxkey_eebf67d = _name_boundary.attributes(meadow_kernel32_idb_local_aa14e6b.id0)['get_max']().key
    meadow_cursor_6496300 = _name_boundary.attributes(meadow_kernel32_idb_local_aa14e6b.id0)['find'](meadow_maxkey_eebf67d)
    meadow_count_local_afee06a = 1
    while True:
        try:
            _name_boundary.attributes(meadow_cursor_6496300)['prev']()
        except IndexError:
            break
        meadow_count_local_afee06a += 1
    assert meadow_kernel32_idb_local_aa14e6b.id0.record_count == meadow_count_local_afee06a

@meadow_kern32_test([(695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_df9e6e7', 'expected': 'meadow_expected_2f47c64', 'kernel32_idb': 'meadow_kernel32_idb_local_f4eef68', 'version': 'meadow_version_local_ba6bd47'}, 'test_id1')
def meadow_test_id1(meadow_kernel32_idb_local_f4eef68, meadow_version_local_ba6bd47, meadow_bitness_df9e6e7, meadow_expected_2f47c64):
    meadow_id1_local_0f5751a = meadow_kernel32_idb_local_f4eef68.id1
    meadow_segments_local_0fae1bc = meadow_id1_local_0f5751a.segments
    assert len(meadow_segments_local_0fae1bc) == 2
    for meadow_segment_local_709422d in meadow_segments_local_0fae1bc:
        assert meadow_segment_local_709422d.bounds.start < meadow_segment_local_709422d.bounds.end
    assert meadow_segments_local_0fae1bc[0].bounds.start == 1754271744
    assert meadow_segments_local_0fae1bc[1].bounds.start == 1755172864
    assert _name_boundary.attributes(meadow_id1_local_0f5751a)['get_segment'](1754271744).bounds.start == 1754271744
    assert _name_boundary.attributes(meadow_id1_local_0f5751a)['get_segment'](1754271745).bounds.start == 1754271744
    assert _name_boundary.attributes(meadow_id1_local_0f5751a)['get_segment'](1755168768 - 1).bounds.start == 1754271744
    assert _name_boundary.attributes(meadow_id1_local_0f5751a)['get_next_segment'](1754271744).bounds.start == 1755172864
    assert _name_boundary.attributes(meadow_id1_local_0f5751a)['get_flags'](1754271744) == 9616

@_name_boundary.callable_contract({'elf_idb': 'meadow_elf_idb_local_f3d97a4'}, 'test_id1_2')
def meadow_test_id1_2(meadow_elf_idb_local_f3d97a4):
    assert list(map(_name_boundary.callable_contract({'s': 'meadow_s_local_318424e'}, '<lambda>')(lambda meadow_s_local_318424e: meadow_s_local_318424e.offset), meadow_elf_idb_local_f3d97a4.id1.segments)) == [0, 140, 7404, 294476, 473132, 473180, 475036]

@meadow_kern32_test([(695, 32, 14252), (695, 64, 14252), (700, 32, 14247), (700, 64, 14247)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_0a62aaf', 'expected': 'meadow_expected_7d2537d', 'kernel32_idb': 'meadow_kernel32_idb_local_d0a223e', 'version': 'meadow_version_local_2df2176'}, 'test_nam_name_count')
def meadow_test_nam_name_count(meadow_kernel32_idb_local_d0a223e, meadow_version_local_2df2176, meadow_bitness_0a62aaf, meadow_expected_7d2537d):
    assert meadow_kernel32_idb_local_d0a223e.nam.name_count == meadow_expected_7d2537d

@meadow_kern32_test([(695, 32, 8), (695, 64, 15), (700, 32, 8), (700, 64, 15)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_6b84e93', 'expected': 'meadow_expected_8e13a83', 'kernel32_idb': 'meadow_kernel32_idb_local_9c88f54', 'version': 'meadow_version_local_51b352f'}, 'test_nam_page_count')
def meadow_test_nam_page_count(meadow_kernel32_idb_local_9c88f54, meadow_version_local_51b352f, meadow_bitness_6b84e93, meadow_expected_8e13a83):
    assert meadow_kernel32_idb_local_9c88f54.nam.page_count == meadow_expected_8e13a83
    meadow_nam_local_6fecd81 = meadow_kernel32_idb_local_9c88f54.nam
    if meadow_bitness_6b84e93 == 32:
        assert meadow_nam_local_6fecd81.name_count < len(meadow_nam_local_6fecd81.buffer)
    elif meadow_bitness_6b84e93 == 64:
        assert meadow_nam_local_6fecd81.name_count < len(meadow_nam_local_6fecd81.buffer)

@meadow_kern32_test([(695, 32, 14252), (695, 64, 14252), (700, 32, 14247), (700, 64, 14247)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_8d872b5', 'expected': 'meadow_expected_1b68e03', 'kernel32_idb': 'meadow_kernel32_idb_local_b4fa005', 'version': 'meadow_version_local_b6c868f'}, 'test_nam_names')
def meadow_test_nam_names(meadow_kernel32_idb_local_b4fa005, meadow_version_local_b6c868f, meadow_bitness_8d872b5, meadow_expected_1b68e03):
    meadow_names_867e8a3 = _name_boundary.attributes(meadow_kernel32_idb_local_b4fa005.nam)['names']()
    assert len(meadow_names_867e8a3) == meadow_expected_1b68e03
    assert meadow_names_867e8a3[0] == 1754271760
    assert meadow_names_867e8a3[-1] == 1755177512

@meadow_kern32_test([(695, 32, None), (695, 64, None), (700, 32, None), (700, 64, None)])
@_name_boundary.callable_contract({'bitness': 'meadow_bitness_dfaa7cb', 'expected': 'meadow_expected_1bf3134', 'kernel32_idb': 'meadow_kernel32_idb_local_0f4ed36', 'version': 'meadow_version_local_2904820'}, 'test_til')
def meadow_test_til(meadow_kernel32_idb_local_0f4ed36, meadow_version_local_2904820, meadow_bitness_dfaa7cb, meadow_expected_1bf3134):
    meadow_til_local_21ff282 = meadow_kernel32_idb_local_0f4ed36.til
    assert meadow_til_local_21ff282.signature == 'IDATIL'
    assert meadow_til_local_21ff282.size_i == 4
    assert meadow_til_local_21ff282.size_b == 1
    assert meadow_til_local_21ff282.size_e == 4
    meadow_syms_4cf574a = meadow_til_local_21ff282.syms.defs
    meadow_types_e3b389d = _name_boundary.attributes(meadow_til_local_21ff282)['types'].defs
    assert len(meadow_types_e3b389d) == 106
    assert len(meadow_syms_4cf574a) == 61
    assert meadow_types_e3b389d[0].name == 'GUID'
    assert meadow_types_e3b389d[1].name == '_GUID'
    assert meadow_types_e3b389d[1].fields == ['Data1', 'Data2', 'Data3', 'Data4']
    assert meadow_types_e3b389d[4].name == 'JOBOBJECTINFOCLASS'
    assert meadow_types_e3b389d[5].name == '_JOBOBJECTINFOCLASS'
    assert meadow_types_e3b389d[5].fields == ['JobObjectBasicAccountingInformation', 'JobObjectBasicLimitInformation', 'JobObjectBasicProcessIdList', 'JobObjectBasicUIRestrictions', 'JobObjectSecurityLimitInformation', 'JobObjectEndOfJobTimeInformation', 'JobObjectAssociateCompletionPortInformation', 'MaxJobObjectInfoClass']
    assert meadow_syms_4cf574a[0].name == 'JobObjectBasicAccountingInformation'
    assert meadow_syms_4cf574a[1].name == 'JobObjectBasicLimitInformation'
    assert meadow_syms_4cf574a[2].name == 'JobObjectBasicProcessIdList'
    assert meadow_syms_4cf574a[3].name == 'JobObjectBasicUIRestrictions'
    assert meadow_syms_4cf574a[4].name == 'JobObjectSecurityLimitInformation'
    assert meadow_syms_4cf574a[5].name == 'JobObjectEndOfJobTimeInformation'
    assert meadow_syms_4cf574a[6].name == 'JobObjectAssociateCompletionPortInformation'
    assert meadow_syms_4cf574a[7].name == 'MaxJobObjectInfoClass'
    assert meadow_syms_4cf574a[0].ordinal == 1
    assert meadow_syms_4cf574a[1].ordinal == 2
    assert meadow_syms_4cf574a[2].ordinal == 3
    assert meadow_syms_4cf574a[3].ordinal == 4
    assert meadow_syms_4cf574a[4].ordinal == 5
    assert meadow_syms_4cf574a[5].ordinal == 6
    assert meadow_syms_4cf574a[6].ordinal == 7
    assert meadow_syms_4cf574a[7].ordinal == 8
    assert meadow_syms_4cf574a[0].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[1].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[2].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[3].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[4].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[5].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[6].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_syms_4cf574a[7].type_info == b'=\x14_JOBOBJECTINFOCLASS'
    assert meadow_types_e3b389d[58].name == 'ULARGE_INTEGER'
    assert meadow_types_e3b389d[59].name == '_ULARGE_INTEGER'
    assert meadow_types_e3b389d[59].fields == ['u', 'QuadPart']
    assert meadow_types_e3b389d[60].name == '_ULARGE_INTEGER::$0354AA9C204208F00D0965D07BBE7FAC'
    assert meadow_types_e3b389d[60].fields == ['LowPart', 'HighPart']

@_name_boundary.callable_contract({}, 'test_til_affix')
def meadow_test_til_affix():
    meadow_cd_2b181ec = _name_boundary.attributes(meadow_os)['path'].dirname(__file__)
    meadow_idbpath_da61cb5 = _name_boundary.attributes(meadow_os)['path'].join(meadow_cd_2b181ec, 'data', 'til', 'TILTest.dll.i64')
    with meadow_idb.from_file(meadow_idbpath_da61cb5) as meadow_db_5b4f054:
        meadow_til_local_fa0fe3b = meadow_db_5b4f054.til
        assert meadow_til_local_fa0fe3b.signature == 'IDATIL'
        assert meadow_til_local_fa0fe3b.size_i == 4
        assert meadow_til_local_fa0fe3b.size_b == 1
        assert meadow_til_local_fa0fe3b.size_e == 4
        meadow_syms_1620a9d = meadow_til_local_fa0fe3b.syms.defs
        meadow_types_ebb626b = _name_boundary.attributes(meadow_til_local_fa0fe3b)['types'].defs
        meadow_base_local_13d181f = meadow_types_ebb626b[23]
        assert meadow_base_local_13d181f.name == 'Base'
        assert meadow_base_local_13d181f.fields == ['field0_', 'field1_', 'field2_']
        assert _name_boundary.attributes(meadow_base_local_13d181f.type)['is_struct']()
        meadow_base_members_c1d4486 = _name_boundary.attributes(_name_boundary.attributes(meadow_base_local_13d181f.type)['type_details'])['members']
        assert _name_boundary.attributes(meadow_base_members_c1d4486[0].type)['is_int']()
        assert _name_boundary.attributes(meadow_base_members_c1d4486[1].type)['is_int']()
        assert _name_boundary.attributes(meadow_base_members_c1d4486[2].type)['is_int']()
        meadow_derive_b77b6cf = meadow_types_ebb626b[24]
        assert meadow_derive_b77b6cf.name == 'Derive'
        assert meadow_derive_b77b6cf.fields == ['field3_', 'field4_', 'field5_']
        assert _name_boundary.attributes(meadow_derive_b77b6cf.type)['is_struct']()
        meadow_derive_members_129ab87 = _name_boundary.attributes(_name_boundary.attributes(meadow_derive_b77b6cf.type)['type_details'])['members']
        assert _name_boundary.attributes(meadow_derive_members_129ab87[0])['is_baseclass']()
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_derive_members_129ab87[0].type)['get_final_tinfo']())['get_name']() == _name_boundary.attributes(meadow_base_local_13d181f.type)['get_name']()
        assert _name_boundary.attributes(meadow_derive_members_129ab87[1].type)['is_int']()
        assert _name_boundary.attributes(meadow_derive_members_129ab87[2].type)['is_int']()
        assert _name_boundary.attributes(meadow_derive_members_129ab87[3].type)['is_int']()
        meadow_t34_65f4e94 = meadow_types_ebb626b[33]
        assert meadow_t34_65f4e94.name == 'Outside::<unnamed_type_inside>'
        assert meadow_t34_65f4e94.fields == ['field0', 'field1', 'field2']
        assert _name_boundary.attributes(meadow_t34_65f4e94.type)['is_struct']()
        meadow_t35_ff1b532 = meadow_types_ebb626b[34]
        assert meadow_t35_ff1b532.name == 'Outside'
        assert meadow_t35_ff1b532.fields == ['inside', 'foo', 'bar']
        assert _name_boundary.attributes(meadow_t35_ff1b532.type)['is_struct']()
        meadow_members_9a4e8d8 = _name_boundary.attributes(_name_boundary.attributes(meadow_t35_ff1b532.type)['type_details'])['members']
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_members_9a4e8d8[0].type)['get_final_tinfo']())['is_struct']()
        meadow_t52_856fcd7 = meadow_types_ebb626b[51]
        assert meadow_t52_856fcd7.name == 'Sorter'
        assert meadow_t52_856fcd7.fields == ['__vftable']
        assert _name_boundary.attributes(meadow_t52_856fcd7.type)['is_struct']()
        meadow_t52_typ_bf70023 = _name_boundary.attributes(_name_boundary.attributes(meadow_t52_856fcd7.type)['type_details'])['members'][0].type
        assert _name_boundary.attributes(meadow_t52_typ_bf70023)['is_ptr']()
        assert _name_boundary.attributes(_name_boundary.attributes(meadow_t52_typ_bf70023)['get_pointed_object']())['is_decl_typedef']()
        assert _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_t52_typ_bf70023)['get_pointed_object']())['get_final_tinfo']())['is_struct']()
        meadow_t53_d9822d5 = meadow_types_ebb626b[52]
        assert meadow_t53_d9822d5.name == 'Sorter_vtbl'
        assert meadow_t53_d9822d5.fields == ['compare', 'this']
        assert _name_boundary.attributes(meadow_t53_d9822d5.type)['is_struct']()
        meadow_t209_19de257 = meadow_types_ebb626b[208]
        assert meadow_t209_19de257.name == 'PTP_CLEANUP_GROUP_CANCEL_CALLBACK'
        assert _name_boundary.attributes(meadow_t209_19de257.type)['is_funcptr']()
        assert _name_boundary.attributes(meadow_t209_19de257.type)['get_typestr']() == 'void (__fastcall *PTP_CLEANUP_GROUP_CANCEL_CALLBACK)(void*, void*)'
        assert _name_boundary.attributes(meadow_types_ebb626b[78].type)['get_typestr']() == 'struct _TP_CALLBACK_ENVIRON_V3::<unnamed_type_u>::<unnamed_type_s>\n{\n  unsigned int32 LongFunction : 1;\n  unsigned int32 Persistent : 1;\n  unsigned int32 Private : 30;\n}'
        assert _name_boundary.attributes(meadow_types_ebb626b[114].type)['get_typestr']() == 'struct _TypeDescriptor\n{\n  void* pVFTable;\n  void* spare;\n  int8[] name;\n}'
_name_boundary.module_contract(globals(), {'test_til': 'meadow_test_til', 'test_id0_record_count': 'meadow_test_id0_record_count', 'test_find_prefix': 'meadow_test_find_prefix', 'test_id0_page_size': 'meadow_test_id0_page_size', 'test_find_exact_match6': 'meadow_test_find_exact_match6', 'test_cursor_min': 'meadow_test_cursor_min', 'test_cursor_complex_leaf_prev': 'meadow_test_cursor_complex_leaf_prev', 'test_validate': 'meadow_test_validate', 'test_find_exact_match4': 'meadow_test_find_exact_match4', 'test_find_exact_match3': 'meadow_test_find_exact_match3', 'test_find_prefix2': 'meadow_test_find_prefix2', 'binascii': 'meadow_binascii', 'test_find_exact_match_error': 'meadow_test_find_exact_match_error', 'test_compressed': 'meadow_test_compressed', 'test_cursor_max': 'meadow_test_cursor_max', 'test_find_exact_match_max': 'meadow_test_find_exact_match_max', 'test_id1_2': 'meadow_test_id1_2', 'test_find_exact_match5': 'meadow_test_find_exact_match5', 'test_id0_root_entries': 'meadow_test_id0_root_entries', 'test_cursor_enum_all_asc': 'meadow_test_cursor_enum_all_asc', 'test_find_exact_match_min': 'meadow_test_find_exact_match_min', 'test_nam_page_count': 'meadow_test_nam_page_count', 'test_cursor_branch': 'meadow_test_cursor_branch', 'test_wordsize': 'meadow_test_wordsize', 'test_id0_root_page': 'meadow_test_id0_root_page', 'test_id1': 'meadow_test_id1', 'test_header_magic': 'meadow_test_header_magic', 'test_nam_name_count': 'meadow_test_nam_name_count', 'test_cursor_enum_all_desc': 'meadow_test_cursor_enum_all_desc', 'test_cursor_easy_leaf': 'meadow_test_cursor_easy_leaf', 'test_find_exact_match1': 'meadow_test_find_exact_match1', 'idb': 'meadow_idb', 'h': 'meadow_h', 'test_nam_names': 'meadow_test_nam_names', 'test_id0_page_count': 'meadow_test_id0_page_count', 'test_find_exact_match2': 'meadow_test_find_exact_match2', 'test_til_affix': 'meadow_test_til_affix', 'test_cursor_complex_leaf_next': 'meadow_test_cursor_complex_leaf_next', 'b2h': 'meadow_b2h', 'h2b': 'meadow_h2b', 'do_test_compressed': 'meadow_do_test_compressed'})
