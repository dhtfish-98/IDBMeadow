# Derived from idb/fileformat.py; original copyright and license retained in ORIGIN.md.
"""
lots of inspiration from: https://github.com/nlitsme/pyidbutil
"""
import idbmeadow.api_contract as _name_boundary
import re as meadow_re
import abc as meadow_abc
import zlib as meadow_zlib
import logging as meadow_logging
import functools as meadow_functools
from collections import namedtuple as meadow_namedtuple
import vstruct as meadow_vstruct
from vstruct.primitives import *
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
from idbmeadow.type_records import meadow_TIL as meadow_TIL
from idbmeadow.semantic_views import meadow_Root as meadow_Root
try:
    from re import fullmatch as meadow_fullmatch
except ImportError:

    @_name_boundary.callable_contract({'regex': 'meadow_regex_4200140', 'string': 'meadow_string_local_21a3319', 'flags': 'meadow_flags_local_818f5d5'}, 'fullmatch')
    def meadow_fullmatch(meadow_regex_4200140, meadow_string_local_21a3319, meadow_flags_local_818f5d5=0):
        """Emulate python-3.4 re.fullmatch()."""
        return meadow_re.match('(?:' + meadow_regex_4200140 + ')\\Z', meadow_string_local_21a3319, flags=meadow_flags_local_818f5d5)
meadow_logger = meadow_logging.getLogger(__name__)

class meadow_FileHeader(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_c1ebf90', 'buf': 'meadow_buf_local_cfa7b73'}, '__init__')
    def __init__(meadow_self_c1ebf90, meadow_buf_local_cfa7b73):
        meadow_vstruct.VStruct.__init__(meadow_self_c1ebf90)
        meadow_self_c1ebf90.buf = meadow_buf_local_cfa7b73
        meadow_self_c1ebf90.offsets = []
        meadow_self_c1ebf90.checksums = []
        meadow_self_c1ebf90.version = struct.unpack_from('<H', meadow_buf_local_cfa7b73, 30)[0]
        meadow_self_c1ebf90.signature = v_bytes(size=4)
        meadow_self_c1ebf90.unk04 = v_uint16()
        if meadow_self_c1ebf90.version <= 4:
            meadow_self_c1ebf90.offset1 = v_uint32()
            meadow_self_c1ebf90.offset2 = v_uint32()
            meadow_self_c1ebf90.offset3 = v_uint32()
            meadow_self_c1ebf90.offset4 = v_uint32()
            meadow_self_c1ebf90.offset5 = v_uint32()
            meadow_self_c1ebf90.sig2 = v_uint32()
            meadow_self_c1ebf90._version = v_uint16()
            meadow_self_c1ebf90.unk20 = v_uint32()
            meadow_self_c1ebf90.checksum1 = v_uint32()
            meadow_self_c1ebf90.checksum2 = v_uint32()
            meadow_self_c1ebf90.checksum3 = v_uint32()
            meadow_self_c1ebf90.checksum4 = v_uint32()
            meadow_self_c1ebf90.checksum5 = v_uint32()
            meadow_self_c1ebf90.offset6 = v_uint32()
            meadow_self_c1ebf90.checksum6 = v_uint32()
        else:
            meadow_self_c1ebf90.offset1 = v_uint64()
            meadow_self_c1ebf90.offset2 = v_uint64()
            meadow_self_c1ebf90.unk16 = v_uint32()
            meadow_self_c1ebf90.sig2 = v_uint32()
            meadow_self_c1ebf90._version = v_uint16()
            meadow_self_c1ebf90.offset3 = v_uint64()
            meadow_self_c1ebf90.offset4 = v_uint64()
            meadow_self_c1ebf90.offset5 = v_uint64()
            meadow_self_c1ebf90.checksum1 = v_uint32()
            meadow_self_c1ebf90.checksum2 = v_uint32()
            meadow_self_c1ebf90.checksum3 = v_uint32()
            meadow_self_c1ebf90.checksum4 = v_uint32()
            meadow_self_c1ebf90.checksum5 = v_uint32()
            meadow_self_c1ebf90.offset6 = v_uint64()
            meadow_self_c1ebf90.checksum6 = v_uint32()

    @_name_boundary.callable_contract({'self': 'meadow_self_c5dd42c', 'fast': 'meadow_fast_1a242da', 'sbytes': 'meadow_sbytes_local_e35f0b8', 'offset': 'meadow_offset_local_4070909'}, 'vsParse')
    def vsParse(meadow_self_c5dd42c, meadow_sbytes_local_e35f0b8, meadow_offset_local_4070909=0, meadow_fast_1a242da=False):
        meadow_result_local_aa5c245 = meadow_vstruct.VStruct.vsParse(meadow_self_c5dd42c, meadow_sbytes_local_e35f0b8, meadow_offset_local_4070909, meadow_fast_1a242da)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset1)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset2)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset3)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset4)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset5)
        meadow_self_c5dd42c.offsets.append(meadow_self_c5dd42c.offset6)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum1)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum2)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum3)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum4)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum5)
        meadow_self_c5dd42c.checksums.append(meadow_self_c5dd42c.checksum6)
        return meadow_result_local_aa5c245

    @_name_boundary.callable_contract({'self': 'meadow_self_0c082b8'}, 'validate')
    def meadow_validate(meadow_self_0c082b8):
        if meadow_self_0c082b8.signature not in (b'IDA0', b'IDA1', b'IDA2'):
            raise ValueError('bad signature')
        if meadow_self_0c082b8.sig2 != 2864434397:
            raise ValueError('bad sig2')
        if meadow_self_0c082b8.version not in (6, 4):
            raise ValueError('unsupported version')
        return True
    validate = meadow_validate

@_name_boundary.class_contract('COMPRESSION_METHOD', {'NONE': 'meadow_NONE', 'ZLIB': 'meadow_ZLIB'})
class meadow_COMPRESSION_METHOD:
    meadow_NONE = 0
    meadow_ZLIB = 2

class meadow_SectionHeader(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_c7b3f76', 'version': 'meadow_version_local_74a98a3'}, '__init__')
    def __init__(meadow_self_c7b3f76, meadow_version_local_74a98a3):
        meadow_vstruct.VStruct.__init__(meadow_self_c7b3f76)
        meadow_self_c7b3f76.version = meadow_version_local_74a98a3
        meadow_self_c7b3f76.compression_method = v_uint8()
        if meadow_self_c7b3f76.version <= 4:
            meadow_self_c7b3f76.length = v_uint32()
        else:
            meadow_self_c7b3f76.length = v_uint64()
        meadow_self_c7b3f76.is_compressed = False

    @_name_boundary.callable_contract({'self': 'meadow_self_8467161'}, 'pcb_compression_method')
    def pcb_compression_method(meadow_self_8467161):
        if meadow_self_8467161.compression_method == _name_boundary.attributes(meadow_COMPRESSION_METHOD)['NONE']:
            meadow_self_8467161.is_compressed = False
        else:
            meadow_self_8467161.is_compressed = True

class meadow_Section(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_05232df', 'version': 'meadow_version_local_5a155c9'}, '__init__')
    def __init__(meadow_self_05232df, meadow_version_local_5a155c9):
        meadow_vstruct.VStruct.__init__(meadow_self_05232df)
        meadow_self_05232df.version = meadow_version_local_5a155c9
        meadow_self_05232df.header = meadow_SectionHeader(meadow_self_05232df.version)
        meadow_self_05232df._contents = v_bytes()
        meadow_self_05232df.contents = b''

    @_name_boundary.callable_contract({'self': 'meadow_self_28bb169'}, 'pcb_header')
    def pcb_header(meadow_self_28bb169):
        meadow_self_28bb169['_contents'].vsSetLength(meadow_self_28bb169.header.length)

    @_name_boundary.callable_contract({'self': 'meadow_self_ee0db27'}, 'pcb__contents')
    def pcb__contents(meadow_self_ee0db27):
        if not meadow_self_ee0db27.header.is_compressed:
            meadow_self_ee0db27.contents = meadow_self_ee0db27._contents
        else:
            meadow_self_ee0db27.contents = meadow_zlib.decompress(meadow_self_ee0db27._contents)
            meadow_logger.debug('decompressed parsed section.')

    @_name_boundary.callable_contract({'self': 'meadow_self_9ed0ae3'}, 'validate')
    def meadow_validate(meadow_self_9ed0ae3):
        if meadow_self_9ed0ae3.header.length == 0:
            raise ValueError('zero size')
        return True
    validate = meadow_validate
meadow_SIZEOF_ENTRY = {2.0: 6, 1.6: 6, 1.5: 4}

class meadow_BranchEntryPointer(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_07e9469', 'btree_version': 'meadow_btree_version_local_d07d616'}, '__init__')
    def __init__(meadow_self_07e9469, meadow_btree_version_local_d07d616):
        meadow_vstruct.VStruct.__init__(meadow_self_07e9469)
        meadow_self_07e9469.btree_version = meadow_btree_version_local_d07d616
        meadow_self_07e9469.offset = None
        if meadow_self_07e9469.btree_version in (1.6, 2.0):
            meadow_self_07e9469.page = v_uint32()
            meadow_self_07e9469._offset = v_uint16()
        elif meadow_self_07e9469.btree_version == 1.5:
            meadow_self_07e9469.page = v_uint16()
            meadow_self_07e9469._offset = v_uint16()
        else:
            raise ValueError('unsupported version')

    @_name_boundary.callable_contract({'self': 'meadow_self_db76e12'}, 'pcb__offset')
    def pcb__offset(meadow_self_db76e12):
        meadow_self_db76e12.offset = meadow_self_db76e12._offset if meadow_self_db76e12.btree_version == 2.0 else meadow_self_db76e12._offset + 1

class meadow_BranchEntry(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_2d000b2', 'page': 'meadow_page_local_66b5e34'}, '__init__')
    def __init__(meadow_self_2d000b2, meadow_page_local_66b5e34):
        meadow_vstruct.VStruct.__init__(meadow_self_2d000b2)
        meadow_self_2d000b2.page = meadow_page_local_66b5e34
        meadow_self_2d000b2.key_length = v_uint16()
        meadow_self_2d000b2.key = v_bytes()
        meadow_self_2d000b2.value_length = v_uint16()
        meadow_self_2d000b2.value = v_bytes()

    @_name_boundary.callable_contract({'self': 'meadow_self_eff2110'}, 'pcb_key_length')
    def pcb_key_length(meadow_self_eff2110):
        meadow_self_eff2110['key'].vsSetLength(meadow_self_eff2110.key_length)

    @_name_boundary.callable_contract({'self': 'meadow_self_94542cf'}, 'pcb_value_length')
    def pcb_value_length(meadow_self_94542cf):
        meadow_self_94542cf['value'].vsSetLength(meadow_self_94542cf.value_length)

class meadow_LeafEntryPointer(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_3da8c22', 'btree_version': 'meadow_btree_version_local_d507733'}, '__init__')
    def __init__(meadow_self_3da8c22, meadow_btree_version_local_d507733):
        meadow_vstruct.VStruct.__init__(meadow_self_3da8c22)
        meadow_self_3da8c22.btree_version = meadow_btree_version_local_d507733
        meadow_self_3da8c22.offset = None
        if meadow_self_3da8c22.btree_version == 2.0:
            meadow_self_3da8c22.common_prefix = v_uint16()
            meadow_self_3da8c22.unk02 = v_uint16()
        elif meadow_self_3da8c22.btree_version == 1.6:
            meadow_self_3da8c22.common_prefix = v_uint8()
            meadow_self_3da8c22.unk01 = v_uint8()
            meadow_self_3da8c22.unk02 = v_uint16()
        elif meadow_self_3da8c22.btree_version == 1.5:
            meadow_self_3da8c22.common_prefix = v_uint8()
            meadow_self_3da8c22.unk01 = v_uint8()
        else:
            raise ValueError('unsupported version')
        meadow_self_3da8c22._offset = v_uint16()

    @_name_boundary.callable_contract({'self': 'meadow_self_e38cb76'}, 'pcb__offset')
    def pcb__offset(meadow_self_e38cb76):
        meadow_self_e38cb76.offset = meadow_self_e38cb76._offset if meadow_self_e38cb76.btree_version == 2.0 else meadow_self_e38cb76._offset + 1

class meadow_LeafEntry(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_3ab9614', 'key': 'meadow_key_local_c7c855f', 'common_prefix': 'meadow_common_prefix_local_7aa1d9a'}, '__init__')
    def __init__(meadow_self_3ab9614, meadow_key_local_c7c855f, meadow_common_prefix_local_7aa1d9a):
        meadow_vstruct.VStruct.__init__(meadow_self_3ab9614)
        meadow_self_3ab9614.pkey = meadow_key_local_c7c855f
        meadow_self_3ab9614.common_prefix = meadow_common_prefix_local_7aa1d9a
        meadow_self_3ab9614.key_length = v_uint16()
        meadow_self_3ab9614._key = v_bytes()
        meadow_self_3ab9614.value_length = v_uint16()
        meadow_self_3ab9614.value = v_bytes()
        meadow_self_3ab9614.key = None

    @_name_boundary.callable_contract({'self': 'meadow_self_7726155'}, 'pcb_key_length')
    def pcb_key_length(meadow_self_7726155):
        meadow_self_7726155['_key'].vsSetLength(meadow_self_7726155.key_length)

    @_name_boundary.callable_contract({'self': 'meadow_self_ae31fed'}, 'pcb_value_length')
    def pcb_value_length(meadow_self_ae31fed):
        meadow_self_ae31fed['value'].vsSetLength(meadow_self_ae31fed.value_length)

    @_name_boundary.callable_contract({'self': 'meadow_self_b04dd39'}, 'pcb__key')
    def pcb__key(meadow_self_b04dd39):
        meadow_self_b04dd39.key = meadow_self_b04dd39.pkey[:meadow_self_b04dd39.common_prefix] + meadow_self_b04dd39._key

class meadow_Page(meadow_vstruct.VStruct):
    """
    single node in the b-tree.
    has a bunch of key-value entries that may point to other pages.
    binary search these keys and traverse pointers to efficienty query the index.

    branch node::

                                      +-------------+
        +-----------------------------+ ppointer    |  ----> [ node with keys less than entry1.key]
        | entry1.key | entry1.value   |-------------+
        +-----------------------------+ entry1.page |  ----> [ node with entry1.key < X < entry2.key]
        | entry2.key | entry2.value   |-------------+
        +-----------------------------+ entry2.page |  ----> [ node with entry2.key < X < entry3.key]
        | ...        | ...            |-------------+
        +-----------------------------+ ...         |
        | entryN.key | entryN.value   |-------------+
        +-----------------------------+ entryN.key  |  ----> [ node with keys greater than entryN.key]
                                      +-------------+

    leaf node::

        +-----------------------------+
        | entry1.key | entry1.value   |
        +-----------------------------+
        | entry2.key | entry2.value   |
        +-----------------------------+
        | ...        | ...            |
        +-----------------------------+
        | entryN.key | entryN.value   |
        +-----------------------------+

    """

    @_name_boundary.callable_contract({'self': 'meadow_self_29a4075', 'page_size': 'meadow_page_size_local_39fb012', 'page_number': 'meadow_page_number_local_9e3abb8', 'btree_version': 'meadow_btree_version_local_bdbf0d4'}, '__init__')
    def __init__(meadow_self_29a4075, meadow_page_size_local_39fb012, meadow_page_number_local_9e3abb8, meadow_btree_version_local_bdbf0d4):
        meadow_vstruct.VStruct.__init__(meadow_self_29a4075)
        meadow_self_29a4075.page_number = meadow_page_number_local_9e3abb8
        meadow_self_29a4075.btree_version = meadow_btree_version_local_bdbf0d4
        if meadow_self_29a4075.btree_version >= 1.6:
            meadow_self_29a4075.ppointer = v_uint32()
        else:
            meadow_self_29a4075.ppointer = v_uint16()
        meadow_self_29a4075.entry_count = v_uint16()
        meadow_self_29a4075.contents = v_bytes(meadow_page_size_local_39fb012)
        meadow_self_29a4075._entries = []

    @_name_boundary.callable_contract({'self': 'meadow_self_a487485'}, 'is_leaf')
    def meadow_is_leaf(meadow_self_a487485):
        """
        return True if this is a leaf node.

        Returns:
          bool: True if this is a leaf node.
        """
        return meadow_self_a487485.ppointer == 0

    @_name_boundary.callable_contract({'self': 'meadow_self_f2d6486'}, '_load_entries')
    def meadow__load_entries(meadow_self_f2d6486):
        if not meadow_self_f2d6486._entries:
            meadow_key_local_acf4254 = b''
            meadow_sizeof_entry_local_fa5df57 = meadow_SIZEOF_ENTRY[meadow_self_f2d6486.btree_version]
            for meadow_i_c597d25 in range(meadow_self_f2d6486.entry_count):
                if _name_boundary.attributes(meadow_self_f2d6486)['is_leaf']():
                    meadow_ptr_local_5625189 = meadow_LeafEntryPointer(meadow_self_f2d6486.btree_version)
                    meadow_ptr_local_5625189.vsParse(meadow_self_f2d6486.contents, offset=meadow_i_c597d25 * meadow_sizeof_entry_local_fa5df57)
                    meadow_entry_local_7df0602 = meadow_LeafEntry(meadow_key_local_acf4254, meadow_ptr_local_5625189.common_prefix)
                else:
                    meadow_ptr_local_5625189 = meadow_BranchEntryPointer(meadow_self_f2d6486.btree_version)
                    meadow_ptr_local_5625189.vsParse(meadow_self_f2d6486.contents, offset=meadow_i_c597d25 * meadow_sizeof_entry_local_fa5df57)
                    meadow_entry_local_7df0602 = meadow_BranchEntry(int(meadow_ptr_local_5625189.page))
                meadow_entry_local_7df0602.vsParse(meadow_self_f2d6486.contents, offset=meadow_ptr_local_5625189.offset - meadow_sizeof_entry_local_fa5df57)
                meadow_self_f2d6486._entries.append(meadow_entry_local_7df0602)
                meadow_key_local_acf4254 = meadow_entry_local_7df0602.key

    @_name_boundary.callable_contract({'self': 'meadow_self_2427544'}, 'get_entries')
    def meadow_get_entries(meadow_self_2427544):
        """
        generate the entries from this page in order.
        each entry is guaranteed to have the following fields:
          - key
          - value

        Yields:
          Union[BranchEntry, LeafEntry]: the b-tree entries from this page.
        """
        _name_boundary.attributes(meadow_self_2427544)['_load_entries']()
        for meadow_entry_local_de54665 in meadow_self_2427544._entries:
            yield meadow_entry_local_de54665

    @_name_boundary.callable_contract({'self': 'meadow_self_88fc068', 'key': 'meadow_key_local_16a988c'}, 'find_index')
    def meadow_find_index(meadow_self_88fc068, meadow_key_local_16a988c):
        """
        find the index of the exact match, or in the case of a branch node,
         the index of the least-greater entry.
        """
        if _name_boundary.attributes(meadow_self_88fc068)['is_leaf']():
            for meadow_i_c84de36, meadow_entry_local_b3b65ca in enumerate(_name_boundary.attributes(meadow_self_88fc068)['get_entries']()):
                if meadow_key_local_16a988c == bytes(meadow_entry_local_b3b65ca.key):
                    return meadow_i_c84de36
        else:
            for meadow_i_c84de36, meadow_entry_local_b3b65ca in enumerate(_name_boundary.attributes(meadow_self_88fc068)['get_entries']()):
                meadow_entry_key_local_227f425 = bytes(meadow_entry_local_b3b65ca.key)
                if meadow_key_local_16a988c == meadow_entry_key_local_227f425:
                    return meadow_i_c84de36
                elif meadow_key_local_16a988c < meadow_entry_key_local_227f425:
                    return meadow_i_c84de36
                else:
                    continue
        raise KeyError(meadow_key_local_16a988c)

    @_name_boundary.callable_contract({'self': 'meadow_self_bb5cb54', 'entry_number': 'meadow_entry_number_73550e7'}, 'get_entry')
    def meadow_get_entry(meadow_self_bb5cb54, meadow_entry_number_73550e7):
        """
        get the entry at the given index.

        Arguments:
          entry_number (int): the entry index.

        Returns:
          Union[BranchEntry, LeafEntry]: the b-tree entry.

        Raises:
          KeyError: if the entry number is not in the range of entries.
        """
        _name_boundary.attributes(meadow_self_bb5cb54)['_load_entries']()
        if meadow_entry_number_73550e7 >= len(meadow_self_bb5cb54._entries):
            raise KeyError(meadow_entry_number_73550e7)
        return meadow_self_bb5cb54._entries[meadow_entry_number_73550e7]

    @_name_boundary.callable_contract({'self': 'meadow_self_a53aeab'}, 'validate')
    def meadow_validate(meadow_self_a53aeab):
        meadow_last_local_07f6a42 = None
        for meadow_entry_local_357d961 in _name_boundary.attributes(meadow_self_a53aeab)['get_entries']():
            if meadow_last_local_07f6a42 is None:
                continue
            if meadow_last_local_07f6a42.key >= meadow_entry_local_357d961.key:
                raise ValueError('bad page entry sort order')
            meadow_last_local_07f6a42 = meadow_entry_local_357d961
        return True
    is_leaf = meadow_is_leaf
    _load_entries = meadow__load_entries
    get_entries = meadow_get_entries
    find_index = meadow_find_index
    get_entry = meadow_get_entry
    validate = meadow_validate

@_name_boundary.class_contract('FindStrategy', {'find': 'meadow_find'})
class meadow_FindStrategy(object):
    """
    defines the interface for strategies of searching the btree.

    implementors will provide a `.find()` method that operates on a `Cursor` instance.
    the method will update the cursor as it navigates the btree.
    """
    __meta__ = meadow_abc.ABCMeta

    @meadow_abc.abstractmethod
    @_name_boundary.callable_contract({'self': 'meadow_self_2331398', 'cursor': 'meadow_cursor_8a5030d', 'key': 'meadow_key_local_01647c0'}, 'find')
    def meadow_find(meadow_self_2331398, meadow_cursor_8a5030d, meadow_key_local_01647c0):
        raise NotImplementedError()

@_name_boundary.class_contract('ExactMatchStrategy', {'_find': 'meadow__find', 'find': 'meadow_find'})
class meadow_ExactMatchStrategy(meadow_FindStrategy):
    """
    strategy used to find the entry with exactly the key provided.
    if the exact key is not found, `KeyError` is raised.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_583baa2', 'cursor': 'meadow_cursor_1bbc541', 'page_number': 'meadow_page_number_local_cb04926', 'key': 'meadow_key_local_ee080ba'}, '_find')
    def meadow__find(meadow_self_583baa2, meadow_cursor_1bbc541, meadow_page_number_local_cb04926, meadow_key_local_ee080ba):
        meadow_page_local_1822137 = _name_boundary.attributes(_name_boundary.attributes(meadow_cursor_1bbc541)['index'])['get_page'](meadow_page_number_local_cb04926)
        _name_boundary.attributes(meadow_cursor_1bbc541)['path'].append(meadow_page_local_1822137)
        meadow_is_largest_202ff03 = False
        try:
            meadow_entry_number_ab3daf4 = _name_boundary.attributes(meadow_page_local_1822137)['find_index'](meadow_key_local_ee080ba)
        except KeyError:
            meadow_is_largest_202ff03 = True
            meadow_entry_number_ab3daf4 = meadow_page_local_1822137.entry_count - 1
        meadow_entry_local_ccc5ee5 = _name_boundary.attributes(meadow_page_local_1822137)['get_entry'](meadow_entry_number_ab3daf4)
        if bytes(meadow_entry_local_ccc5ee5.key) == meadow_key_local_ee080ba:
            meadow_cursor_1bbc541.entry = meadow_entry_local_ccc5ee5
            _name_boundary.attributes(meadow_cursor_1bbc541)['entry_number'] = meadow_entry_number_ab3daf4
            return
        elif _name_boundary.attributes(meadow_page_local_1822137)['is_leaf']():
            raise KeyError(meadow_key_local_ee080ba)
        else:
            if meadow_is_largest_202ff03:
                meadow_next_page_number_8678cf3 = _name_boundary.attributes(meadow_page_local_1822137)['get_entry'](meadow_page_local_1822137.entry_count - 1).page
            elif meadow_entry_number_ab3daf4 == 0:
                meadow_next_page_number_8678cf3 = meadow_page_local_1822137.ppointer
            else:
                meadow_next_page_number_8678cf3 = _name_boundary.attributes(meadow_page_local_1822137)['get_entry'](meadow_entry_number_ab3daf4 - 1).page
            _name_boundary.attributes(meadow_self_583baa2)['_find'](meadow_cursor_1bbc541, meadow_next_page_number_8678cf3, meadow_key_local_ee080ba)
            return

    @_name_boundary.callable_contract({'self': 'meadow_self_aa12ba5', 'cursor': 'meadow_cursor_dae7b26', 'key': 'meadow_key_local_597ea45'}, 'find')
    def meadow_find(meadow_self_aa12ba5, meadow_cursor_dae7b26, meadow_key_local_597ea45):
        _name_boundary.attributes(meadow_self_aa12ba5)['_find'](meadow_cursor_dae7b26, _name_boundary.attributes(meadow_cursor_dae7b26)['index'].root_page, meadow_key_local_597ea45)

@_name_boundary.class_contract('PrefixMatchStrategy', {'_find': 'meadow__find', 'find': 'meadow_find'})
class meadow_PrefixMatchStrategy(meadow_FindStrategy):
    """
    strategy used to find the first entry that begins with the given key.
    it may be an exact match, or an exact match does not exist, and the result starts with the given key.
    if no entries start with the given key, `KeyError` is raised.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_5680995', 'cursor': 'meadow_cursor_997487e', 'page_number': 'meadow_page_number_local_aa09528', 'key': 'meadow_key_local_2b935e3'}, '_find')
    def meadow__find(meadow_self_5680995, meadow_cursor_997487e, meadow_page_number_local_aa09528, meadow_key_local_2b935e3):
        meadow_page_local_478bd40 = _name_boundary.attributes(_name_boundary.attributes(meadow_cursor_997487e)['index'])['get_page'](meadow_page_number_local_aa09528)
        _name_boundary.attributes(meadow_cursor_997487e)['path'].append(meadow_page_local_478bd40)
        if _name_boundary.attributes(meadow_page_local_478bd40)['is_leaf']():
            for meadow_i_5c305eb, meadow_entry_local_eab2f52 in enumerate(_name_boundary.attributes(meadow_page_local_478bd40)['get_entries']()):
                meadow_entry_key_local_2c61d0e = bytes(meadow_entry_local_eab2f52.key)
                if meadow_entry_key_local_2c61d0e.startswith(meadow_key_local_2b935e3):
                    meadow_cursor_997487e.entry = meadow_entry_local_eab2f52
                    _name_boundary.attributes(meadow_cursor_997487e)['entry_number'] = meadow_i_5c305eb
                    return
                elif meadow_entry_key_local_2c61d0e > meadow_key_local_2b935e3:
                    break
            _name_boundary.attributes(meadow_cursor_997487e)['path'] = _name_boundary.attributes(meadow_cursor_997487e)['path'][:-1]
            raise KeyError(meadow_key_local_2b935e3)
        else:
            meadow_next_page_f364648 = meadow_page_local_478bd40.ppointer
            for meadow_i_5c305eb, meadow_entry_local_eab2f52 in enumerate(_name_boundary.attributes(meadow_page_local_478bd40)['get_entries']()):
                meadow_entry_key_local_2c61d0e = bytes(meadow_entry_local_eab2f52.key)
                if meadow_entry_key_local_2c61d0e == meadow_key_local_2b935e3:
                    meadow_cursor_997487e.entry = meadow_entry_local_eab2f52
                    _name_boundary.attributes(meadow_cursor_997487e)['entry_number'] = meadow_i_5c305eb
                    return
                elif meadow_entry_key_local_2c61d0e.startswith(meadow_key_local_2b935e3):
                    try:
                        return _name_boundary.attributes(meadow_self_5680995)['_find'](meadow_cursor_997487e, meadow_next_page_f364648, meadow_key_local_2b935e3)
                    except KeyError:
                        meadow_cursor_997487e.entry = meadow_entry_local_eab2f52
                        _name_boundary.attributes(meadow_cursor_997487e)['entry_number'] = meadow_i_5c305eb
                        return
                elif meadow_entry_key_local_2c61d0e > meadow_key_local_2b935e3:
                    return _name_boundary.attributes(meadow_self_5680995)['_find'](meadow_cursor_997487e, meadow_next_page_f364648, meadow_key_local_2b935e3)
                else:
                    meadow_next_page_f364648 = meadow_entry_local_eab2f52.page
            meadow_last_entry_5573ab3 = _name_boundary.attributes(meadow_page_local_478bd40)['get_entry'](meadow_page_local_478bd40.entry_count - 1)
            return _name_boundary.attributes(meadow_self_5680995)['_find'](meadow_cursor_997487e, meadow_last_entry_5573ab3.page, meadow_key_local_2b935e3)

    @_name_boundary.callable_contract({'self': 'meadow_self_0d28028', 'cursor': 'meadow_cursor_a7ff58c', 'key': 'meadow_key_local_5ccbde5'}, 'find')
    def meadow_find(meadow_self_0d28028, meadow_cursor_a7ff58c, meadow_key_local_5ccbde5):
        _name_boundary.attributes(meadow_self_0d28028)['_find'](meadow_cursor_a7ff58c, _name_boundary.attributes(meadow_cursor_a7ff58c)['index'].root_page, meadow_key_local_5ccbde5)

@_name_boundary.class_contract('RoundDownMatchStrategy', {'_find': 'meadow__find', 'find': 'meadow_find'})
class meadow_RoundDownMatchStrategy(meadow_FindStrategy):
    """
    strategy used to find the matching key, or the key just less than the given key.
    it may be an exact match, or an exact match does not exist,
     and the result is less than the given key.
    if no entries are less than the given key, `KeyError` is raised.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_fd921e0', 'cursor': 'meadow_cursor_ad30fc2', 'page_number': 'meadow_page_number_local_0bed387', 'key': 'meadow_key_local_0d42507'}, '_find')
    def meadow__find(meadow_self_fd921e0, meadow_cursor_ad30fc2, meadow_page_number_local_0bed387, meadow_key_local_0d42507):
        meadow_page_local_e94bd24 = _name_boundary.attributes(_name_boundary.attributes(meadow_cursor_ad30fc2)['index'])['get_page'](meadow_page_number_local_0bed387)
        _name_boundary.attributes(meadow_cursor_ad30fc2)['path'].append(meadow_page_local_e94bd24)
        if _name_boundary.attributes(meadow_page_local_e94bd24)['is_leaf']():
            for meadow_i_19a1996, meadow_entry_local_4de97fd in enumerate(_name_boundary.attributes(meadow_page_local_e94bd24)['get_entries']()):
                meadow_entry_key_local_7e8b355 = bytes(meadow_entry_local_4de97fd.key)
                if meadow_entry_key_local_7e8b355 == meadow_key_local_0d42507:
                    meadow_cursor_ad30fc2.entry = meadow_entry_local_4de97fd
                    _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_i_19a1996
                    return
                elif meadow_entry_key_local_7e8b355 > meadow_key_local_0d42507:
                    if meadow_i_19a1996 == 0:
                        raise KeyError(meadow_key_local_0d42507)
                    else:
                        meadow_cursor_ad30fc2.entry = _name_boundary.attributes(meadow_page_local_e94bd24)['get_entry'](meadow_i_19a1996 - 1)
                        _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_i_19a1996 - 1
            meadow_entry_number_96293ea = meadow_page_local_e94bd24.entry_count - 1
            meadow_cursor_ad30fc2.entry = _name_boundary.attributes(meadow_page_local_e94bd24)['get_entry'](meadow_entry_number_96293ea)
            _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_entry_number_96293ea
        else:
            for meadow_i_19a1996, meadow_entry_local_4de97fd in enumerate(_name_boundary.attributes(meadow_page_local_e94bd24)['get_entries']()):
                meadow_entry_key_local_7e8b355 = bytes(meadow_entry_local_4de97fd.key)
                if meadow_entry_key_local_7e8b355 == meadow_key_local_0d42507:
                    meadow_cursor_ad30fc2.entry = meadow_entry_local_4de97fd
                    _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_i_19a1996
                    return
                elif meadow_entry_key_local_7e8b355 > meadow_key_local_0d42507:
                    if meadow_i_19a1996 == 0:
                        return _name_boundary.attributes(meadow_self_fd921e0)['_find'](meadow_cursor_ad30fc2, meadow_page_local_e94bd24.ppointer, meadow_key_local_0d42507)
                    else:
                        try:
                            meadow_entry_local_4de97fd = _name_boundary.attributes(meadow_page_local_e94bd24)['get_entry'](meadow_i_19a1996 - 1)
                            return _name_boundary.attributes(meadow_self_fd921e0)['_find'](meadow_cursor_ad30fc2, meadow_entry_local_4de97fd.page, meadow_key_local_0d42507)
                        except KeyError:
                            meadow_cursor_ad30fc2.entry = meadow_entry_local_4de97fd
                            _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_i_19a1996 - 1
                            return
                else:
                    continue
            try:
                meadow_entry_local_4de97fd = _name_boundary.attributes(meadow_page_local_e94bd24)['get_entry'](meadow_page_local_e94bd24.entry_count - 1)
                return _name_boundary.attributes(meadow_self_fd921e0)['_find'](meadow_cursor_ad30fc2, meadow_entry_local_4de97fd.page, meadow_key_local_0d42507)
            except KeyError:
                meadow_cursor_ad30fc2.entry = meadow_entry_local_4de97fd
                _name_boundary.attributes(meadow_cursor_ad30fc2)['entry_number'] = meadow_page_local_e94bd24.entry_count - 1
                return

    @_name_boundary.callable_contract({'self': 'meadow_self_a5313fd', 'cursor': 'meadow_cursor_0b28c62', 'key': 'meadow_key_local_2d5d431'}, 'find')
    def meadow_find(meadow_self_a5313fd, meadow_cursor_0b28c62, meadow_key_local_2d5d431):
        _name_boundary.attributes(meadow_self_a5313fd)['_find'](meadow_cursor_0b28c62, _name_boundary.attributes(meadow_cursor_0b28c62)['index'].root_page, meadow_key_local_2d5d431)

@_name_boundary.class_contract('MinKeyStrategy', {'_find': 'meadow__find', 'find': 'meadow_find'})
class meadow_MinKeyStrategy(meadow_FindStrategy):
    """
    strategy used to find the minimum key in the index.
    note: this completely ignores the provided key.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_a471869', 'cursor': 'meadow_cursor_44f9150', 'page_number': 'meadow_page_number_local_5b030f3'}, '_find')
    def meadow__find(meadow_self_a471869, meadow_cursor_44f9150, meadow_page_number_local_5b030f3):
        meadow_page_local_85443ad = _name_boundary.attributes(_name_boundary.attributes(meadow_cursor_44f9150)['index'])['get_page'](meadow_page_number_local_5b030f3)
        _name_boundary.attributes(meadow_cursor_44f9150)['path'].append(meadow_page_local_85443ad)
        if _name_boundary.attributes(meadow_page_local_85443ad)['is_leaf']():
            meadow_entry_local_0b67392 = _name_boundary.attributes(meadow_page_local_85443ad)['get_entry'](0)
            meadow_cursor_44f9150.entry = meadow_entry_local_0b67392
            _name_boundary.attributes(meadow_cursor_44f9150)['entry_number'] = 0
        else:
            return _name_boundary.attributes(meadow_self_a471869)['_find'](meadow_cursor_44f9150, meadow_page_local_85443ad.ppointer)

    @_name_boundary.callable_contract({'self': 'meadow_self_516df92', 'cursor': 'meadow_cursor_1b7c0d2', '_': 'meadow___00b1190'}, 'find')
    def meadow_find(meadow_self_516df92, meadow_cursor_1b7c0d2, meadow___00b1190):
        _name_boundary.attributes(meadow_self_516df92)['_find'](meadow_cursor_1b7c0d2, _name_boundary.attributes(meadow_cursor_1b7c0d2)['index'].root_page)

@_name_boundary.class_contract('MaxKeyStrategy', {'_find': 'meadow__find', 'find': 'meadow_find'})
class meadow_MaxKeyStrategy(meadow_FindStrategy):
    """
    strategy used to find the maximum key in the index.
    note: this completely ignores the provided key.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_7441249', 'cursor': 'meadow_cursor_b08df13', 'page_number': 'meadow_page_number_local_13cf403'}, '_find')
    def meadow__find(meadow_self_7441249, meadow_cursor_b08df13, meadow_page_number_local_13cf403):
        meadow_page_local_05f5994 = _name_boundary.attributes(_name_boundary.attributes(meadow_cursor_b08df13)['index'])['get_page'](meadow_page_number_local_13cf403)
        _name_boundary.attributes(meadow_cursor_b08df13)['path'].append(meadow_page_local_05f5994)
        if _name_boundary.attributes(meadow_page_local_05f5994)['is_leaf']():
            meadow_entry_number_8639838 = meadow_page_local_05f5994.entry_count - 1
            meadow_entry_local_a2dd7cb = _name_boundary.attributes(meadow_page_local_05f5994)['get_entry'](meadow_entry_number_8639838)
            meadow_cursor_b08df13.entry = meadow_entry_local_a2dd7cb
            _name_boundary.attributes(meadow_cursor_b08df13)['entry_number'] = meadow_entry_number_8639838
        else:
            meadow_entry_number_8639838 = meadow_page_local_05f5994.entry_count - 1
            meadow_entry_local_a2dd7cb = _name_boundary.attributes(meadow_page_local_05f5994)['get_entry'](meadow_entry_number_8639838)
            return _name_boundary.attributes(meadow_self_7441249)['_find'](meadow_cursor_b08df13, meadow_entry_local_a2dd7cb.page)

    @_name_boundary.callable_contract({'self': 'meadow_self_fa63c17', 'cursor': 'meadow_cursor_c9ad643', '_': 'meadow___41b702b'}, 'find')
    def meadow_find(meadow_self_fa63c17, meadow_cursor_c9ad643, meadow___41b702b):
        _name_boundary.attributes(meadow_self_fa63c17)['_find'](meadow_cursor_c9ad643, _name_boundary.attributes(meadow_cursor_c9ad643)['index'].root_page)
meadow_EXACT_MATCH = meadow_ExactMatchStrategy
meadow_PREFIX_MATCH = meadow_PrefixMatchStrategy
meadow_ROUND_DOWN_MATCH = meadow_RoundDownMatchStrategy
meadow_MIN_KEY = meadow_MinKeyStrategy
meadow_MAX_KEY = meadow_MaxKeyStrategy

@_name_boundary.class_contract('Cursor', {'next': 'meadow_next', 'prev': 'meadow_prev', 'index': 'meadow_index', 'path': 'meadow_path', 'entry_number': 'meadow_entry_number'})
class meadow_Cursor(object):
    """
    represents a particular location in the b-tree.
    can be navigated "forward" and "backwards".
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_2f50d7f', 'index': 'meadow_index_eb6499c'}, '__init__')
    def __init__(meadow_self_2f50d7f, meadow_index_eb6499c):
        super(meadow_Cursor, meadow_self_2f50d7f).__init__()
        _name_boundary.attributes(meadow_self_2f50d7f)['index'] = meadow_index_eb6499c
        _name_boundary.attributes(meadow_self_2f50d7f)['path'] = []
        meadow_self_2f50d7f.entry = None
        _name_boundary.attributes(meadow_self_2f50d7f)['entry_number'] = None

    @_name_boundary.callable_contract({'self': 'meadow_self_3d48aed'}, 'next')
    def meadow_next(meadow_self_3d48aed):
        """
        traverse to the next entry.
        updates this current cursor instance.

        Raises:
          IndexError: if the entry does not exist. the cursor is in an unknown state afterwards.
        """
        meadow_current_page_945681a = _name_boundary.attributes(meadow_self_3d48aed)['path'][-1]
        if _name_boundary.attributes(meadow_current_page_945681a)['is_leaf']():
            if _name_boundary.attributes(meadow_self_3d48aed)['entry_number'] == meadow_current_page_945681a.entry_count - 1:
                meadow_start_key_7c13fd6 = meadow_self_3d48aed.entry.key
                while True:
                    if len(_name_boundary.attributes(meadow_self_3d48aed)['path']) <= 1:
                        raise IndexError()
                    _name_boundary.attributes(meadow_self_3d48aed)['path'] = _name_boundary.attributes(meadow_self_3d48aed)['path'][:-1]
                    meadow_current_page_945681a = _name_boundary.attributes(meadow_self_3d48aed)['path'][-1]
                    try:
                        meadow_entry_number_339de0d = _name_boundary.attributes(meadow_current_page_945681a)['find_index'](meadow_start_key_7c13fd6)
                    except KeyError:
                        continue
                    else:
                        break
                meadow_self_3d48aed.entry = _name_boundary.attributes(meadow_current_page_945681a)['get_entry'](meadow_entry_number_339de0d)
                _name_boundary.attributes(meadow_self_3d48aed)['entry_number'] = meadow_entry_number_339de0d
                return
            else:
                meadow_next_entry_number_8ad3a12 = _name_boundary.attributes(meadow_self_3d48aed)['entry_number'] + 1
                meadow_next_entry_0cc66a8 = _name_boundary.attributes(meadow_current_page_945681a)['get_entry'](meadow_next_entry_number_8ad3a12)
                meadow_self_3d48aed.entry = meadow_next_entry_0cc66a8
                _name_boundary.attributes(meadow_self_3d48aed)['entry_number'] = meadow_next_entry_number_8ad3a12
                return
        else:
            meadow_next_page_30330cf = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3d48aed)['index'])['get_page'](meadow_self_3d48aed.entry.page)
            while not _name_boundary.attributes(meadow_next_page_30330cf)['is_leaf']():
                _name_boundary.attributes(meadow_self_3d48aed)['path'].append(meadow_next_page_30330cf)
                meadow_next_page_30330cf = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3d48aed)['index'])['get_page'](meadow_next_page_30330cf.ppointer)
            _name_boundary.attributes(meadow_self_3d48aed)['path'].append(meadow_next_page_30330cf)
            meadow_self_3d48aed.entry = _name_boundary.attributes(meadow_next_page_30330cf)['get_entry'](0)
            _name_boundary.attributes(meadow_self_3d48aed)['entry_number'] = 0
            return

    @_name_boundary.callable_contract({'self': 'meadow_self_24cc0d5'}, 'prev')
    def meadow_prev(meadow_self_24cc0d5):
        """
        traverse to the previous entry.
        updates this current cursor instance.

        Raises:
          IndexError: if the entry does not exist. the cursor is in an unknown state afterwards.
        """
        meadow_current_page_4b6ad1e = _name_boundary.attributes(meadow_self_24cc0d5)['path'][-1]
        if _name_boundary.attributes(meadow_current_page_4b6ad1e)['is_leaf']():
            if _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] == 0:
                meadow_start_key_9d5c5e7 = meadow_self_24cc0d5.entry.key
                while True:
                    if len(_name_boundary.attributes(meadow_self_24cc0d5)['path']) <= 1:
                        raise IndexError()
                    _name_boundary.attributes(meadow_self_24cc0d5)['path'] = _name_boundary.attributes(meadow_self_24cc0d5)['path'][:-1]
                    meadow_current_page_4b6ad1e = _name_boundary.attributes(meadow_self_24cc0d5)['path'][-1]
                    try:
                        meadow_entry_number_92035f0 = _name_boundary.attributes(meadow_current_page_4b6ad1e)['find_index'](meadow_start_key_9d5c5e7)
                    except KeyError:
                        meadow_entry_number_92035f0 = meadow_current_page_4b6ad1e.entry_count
                    if meadow_entry_number_92035f0 == 0:
                        continue
                    else:
                        break
                meadow_self_24cc0d5.entry = _name_boundary.attributes(meadow_current_page_4b6ad1e)['get_entry'](meadow_entry_number_92035f0 - 1)
                _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] = meadow_entry_number_92035f0 - 1
                return
            else:
                meadow_next_entry_number_9314709 = _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] - 1
                meadow_next_entry_9c7add4 = _name_boundary.attributes(meadow_current_page_4b6ad1e)['get_entry'](meadow_next_entry_number_9314709)
                meadow_self_24cc0d5.entry = meadow_next_entry_9c7add4
                _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] = meadow_next_entry_number_9314709
                return
        else:
            meadow_current_page_4b6ad1e = _name_boundary.attributes(meadow_self_24cc0d5)['path'][-1]
            if _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] == 0:
                meadow_next_page_number_47c396c = meadow_current_page_4b6ad1e.ppointer
            else:
                meadow_next_page_number_47c396c = _name_boundary.attributes(meadow_current_page_4b6ad1e)['get_entry'](_name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] - 1).page
            meadow_next_page_04dd98a = _name_boundary.attributes(_name_boundary.attributes(meadow_self_24cc0d5)['index'])['get_page'](meadow_next_page_number_47c396c)
            while not _name_boundary.attributes(meadow_next_page_04dd98a)['is_leaf']():
                _name_boundary.attributes(meadow_self_24cc0d5)['path'].append(meadow_next_page_04dd98a)
                meadow_next_page_04dd98a = _name_boundary.attributes(_name_boundary.attributes(meadow_self_24cc0d5)['index'])['get_page'](_name_boundary.attributes(meadow_next_page_04dd98a)['get_entry'](meadow_next_page_04dd98a.entry_count - 1).page)
            _name_boundary.attributes(meadow_self_24cc0d5)['path'].append(meadow_next_page_04dd98a)
            meadow_self_24cc0d5.entry = _name_boundary.attributes(meadow_next_page_04dd98a)['get_entry'](meadow_next_page_04dd98a.entry_count - 1)
            _name_boundary.attributes(meadow_self_24cc0d5)['entry_number'] = meadow_next_page_04dd98a.entry_count - 1
            return

    @property
    @_name_boundary.callable_contract({'self': 'meadow_self_f322336'}, 'key')
    def key(meadow_self_f322336):
        return meadow_self_f322336.entry.key

    @property
    @_name_boundary.callable_contract({'self': 'meadow_self_7d8679e'}, 'value')
    def value(meadow_self_7d8679e):
        return meadow_self_7d8679e.entry.value

class meadow_ID0(meadow_vstruct.VStruct):
    """
    a b-tree index.
    keys and values are arbitrary byte strings.

    use `.find()` to identify a matching entry, and use the resulting cursor
     instance to access the value, or traverse to less/greater entries.
    """
    SignatureV6 = b'B-tree v 1.6 (C) Pol 1990'
    Signature = b'B-tree v2'
    SignaturePattern = b'B-tree v\\W?(\\d+(\\.\\d+)?).*'

    @_name_boundary.callable_contract({'self': 'meadow_self_3048846', 'buf': 'meadow_buf_local_fc87a65', 'wordsize': 'meadow_wordsize_local_ec21d02'}, '__init__')
    def __init__(meadow_self_3048846, meadow_buf_local_fc87a65, meadow_wordsize_local_ec21d02):
        meadow_vstruct.VStruct.__init__(meadow_self_3048846)
        meadow_self_3048846.buf = meadow_idb.memview(meadow_buf_local_fc87a65)
        meadow_self_3048846.wordsize = meadow_wordsize_local_ec21d02
        meadow_self_3048846.btree_version = None
        meadow_self_3048846.next_free_offset = v_uint32()
        meadow_self_3048846.page_size = v_uint16()
        meadow_self_3048846.root_page = v_uint32()
        meadow_self_3048846.record_count = v_uint32()
        meadow_self_3048846.page_count = v_uint32()
        meadow_self_3048846.unk12 = v_uint8()
        meadow_self_3048846.signature = v_bytes(max(len(meadow_ID0.SignatureV6), len(meadow_ID0.Signature)))
        meadow_self_3048846._page_cache = {}

    @_name_boundary.callable_contract({'self': 'meadow_self_b6a349d'}, 'pcb_signature')
    def pcb_signature(meadow_self_b6a349d):
        meadow_btree_vs_local_a627d71 = meadow_re.match(meadow_ID0.SignaturePattern, meadow_self_b6a349d.signature).group(1)
        meadow_self_b6a349d.btree_version = float(meadow_btree_vs_local_a627d71)

    @_name_boundary.callable_contract({'self': 'meadow_self_deaeee4'}, 'validate')
    def meadow_validate(meadow_self_deaeee4):
        if meadow_fullmatch(meadow_ID0.SignaturePattern, meadow_self_deaeee4.signature) is None:
            raise ValueError('bad signature')
        return True

    @_name_boundary.callable_contract({'self': 'meadow_self_c8fbd18', 'page_number': 'meadow_page_number_local_014ad12'}, 'get_page_buffer')
    def meadow_get_page_buffer(meadow_self_c8fbd18, meadow_page_number_local_014ad12):
        if meadow_page_number_local_014ad12 < 1:
            meadow_logger.warning('unexpected page number requested: %d', meadow_page_number_local_014ad12)
        meadow_offset_local_82c9e3b = meadow_self_c8fbd18.page_size * meadow_page_number_local_014ad12
        return meadow_self_c8fbd18.buf[meadow_offset_local_82c9e3b:meadow_offset_local_82c9e3b + meadow_self_c8fbd18.page_size]

    @_name_boundary.callable_contract({'self': 'meadow_self_2757450', 'page_number': 'meadow_page_number_local_770cafe'}, 'get_page')
    def meadow_get_page(meadow_self_2757450, meadow_page_number_local_770cafe):
        meadow_page_local_dcd8d4a = _name_boundary.attributes(meadow_self_2757450._page_cache)['get'](meadow_page_number_local_770cafe, None)
        if meadow_page_local_dcd8d4a is not None:
            return meadow_page_local_dcd8d4a
        meadow_buf_local_73a5c0d = _name_boundary.attributes(meadow_self_2757450)['get_page_buffer'](meadow_page_number_local_770cafe)
        meadow_page_local_dcd8d4a = meadow_Page(meadow_self_2757450.page_size, meadow_page_number_local_770cafe, meadow_self_2757450.btree_version)
        meadow_page_local_dcd8d4a.vsParse(meadow_buf_local_73a5c0d)
        meadow_self_2757450._page_cache[meadow_page_number_local_770cafe] = meadow_page_local_dcd8d4a
        return meadow_page_local_dcd8d4a

    @_name_boundary.callable_contract({'self': 'meadow_self_5efd780', 'strategy': 'meadow_strategy_b4dddc2', 'key': 'meadow_key_local_055600a'}, 'find')
    def meadow_find(meadow_self_5efd780, meadow_key_local_055600a, meadow_strategy_b4dddc2=meadow_EXACT_MATCH):
        """
        Args:
          key (bytes): the index key for which to search.
          strategy (Type[MatchStrategy]): the strategy to use to do the search.
            some possible strategies:
              - EXACT_MATCH (default)
              - PREFIX_MATCH

        Returns:
          cursor: the cursor that points to the match.

        Raises:
          KeyError: if the match failes to find a result.
        """
        meadow_c_local_82be237 = meadow_Cursor(meadow_self_5efd780)
        meadow_s_local_775c968 = meadow_strategy_b4dddc2()
        _name_boundary.attributes(meadow_s_local_775c968)['find'](meadow_c_local_82be237, meadow_key_local_055600a)
        return meadow_c_local_82be237

    @_name_boundary.callable_contract({'self': 'meadow_self_19575e9', 'key': 'meadow_key_local_6bf782b'}, 'find_prefix')
    def meadow_find_prefix(meadow_self_19575e9, meadow_key_local_6bf782b):
        """
        convenience shortcut for prefix match search.
        """
        return _name_boundary.attributes(meadow_self_19575e9)['find'](meadow_key_local_6bf782b, strategy=meadow_PREFIX_MATCH)

    @_name_boundary.callable_contract({'self': 'meadow_self_4f9394c'}, 'get_min')
    def meadow_get_min(meadow_self_4f9394c):
        """
        find the minimum entry in the index.

        Returns:
          cursor: the cursor that points to the match.
        """
        return _name_boundary.attributes(meadow_self_4f9394c)['find'](None, strategy=meadow_MIN_KEY)

    @_name_boundary.callable_contract({'self': 'meadow_self_48c5da5'}, 'get_max')
    def meadow_get_max(meadow_self_48c5da5):
        """
        find the maximum entry in the index.

        Returns:
          cursor: the cursor that points to the match.
        """
        return _name_boundary.attributes(meadow_self_48c5da5)['find'](None, strategy=meadow_MAX_KEY)
    validate = meadow_validate
    get_page_buffer = meadow_get_page_buffer
    get_page = meadow_get_page
    find = meadow_find
    find_prefix = meadow_find_prefix
    get_min = meadow_get_min
    get_max = meadow_get_max

class meadow_SegmentBounds(meadow_vstruct.VStruct):
    """
    specifies the range of a segment.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_57310b2', 'sig': 'meadow_sig_bc5dbe6', 'wordsize': 'meadow_wordsize_local_8cce521'}, '__init__')
    def __init__(meadow_self_57310b2, meadow_wordsize_local_8cce521, meadow_sig_bc5dbe6):
        meadow_vstruct.VStruct.__init__(meadow_self_57310b2)
        meadow_self_57310b2.wordsize = meadow_wordsize_local_8cce521
        if meadow_wordsize_local_8cce521 == 4:
            meadow_self_57310b2.v_word = v_uint32
        elif meadow_wordsize_local_8cce521 == 8:
            meadow_self_57310b2.v_word = v_uint64
        else:
            raise RuntimeError('unexpected wordsize')
        meadow_self_57310b2.start = meadow_self_57310b2.v_word()
        meadow_self_57310b2.end = meadow_self_57310b2.v_word()
        if meadow_sig_bc5dbe6 == meadow_ID1.SignatureV6:
            meadow_self_57310b2.ofs = meadow_self_57310b2.v_word()

class meadow_ID1(meadow_vstruct.VStruct):
    """
    contains flags for each byte.
    """
    PAGE_SIZE = 8192
    SegmentDescriptor = _name_boundary.named_record('SegmentDescriptor', ['bounds', 'offset'])
    SignatureV6 = b'Va4\x00'
    Signature = b'VA*\x00'

    @_name_boundary.callable_contract({'self': 'meadow_self_83d5ee7', 'wordsize': 'meadow_wordsize_local_5c7cc49', 'buf': 'meadow_buf_local_8698144'}, '__init__')
    def __init__(meadow_self_83d5ee7, meadow_wordsize_local_5c7cc49, meadow_buf_local_8698144=None):
        meadow_vstruct.VStruct.__init__(meadow_self_83d5ee7)
        meadow_self_83d5ee7.wordsize = meadow_wordsize_local_5c7cc49
        if meadow_wordsize_local_5c7cc49 == 4:
            meadow_self_83d5ee7.v_word = v_uint32
        elif meadow_wordsize_local_5c7cc49 == 8:
            meadow_self_83d5ee7.v_word = v_uint64
        else:
            raise RuntimeError('unexpected wordsize')
        meadow_self_83d5ee7.segments = []
        meadow_self_83d5ee7.signature = v_bytes(size=4)

    @_name_boundary.callable_contract({'self': 'meadow_self_a073751'}, 'pcb_signature')
    def pcb_signature(meadow_self_a073751):
        if meadow_self_a073751.signature == meadow_ID1.Signature:
            meadow_self_a073751.vsAddField('unk04', v_uint32())
            meadow_self_a073751.vsAddField('segment_count', v_uint32())
            meadow_self_a073751.vsAddField('unk0C', v_uint32())
            meadow_self_a073751.vsAddField('page_count', v_uint32())
        elif meadow_self_a073751.signature == meadow_ID1.SignatureV6:
            meadow_self_a073751.vsAddField('segment_count', v_uint16())
            meadow_self_a073751.vsAddField('page_count', v_uint16())
        else:
            raise ValueError('unsupported version')
        meadow_self_a073751.vsAddField('_segments', meadow_vstruct.VArray())
        meadow_self_a073751.vsAddField('padding', v_bytes())
        meadow_self_a073751.vsAddField('buffer', v_bytes())

    @_name_boundary.callable_contract({'self': 'meadow_self_2406f4a'}, 'pcb_segment_count')
    def pcb_segment_count(meadow_self_2406f4a):
        meadow_self_2406f4a['_segments'].vsAddElements(meadow_self_2406f4a.segment_count, meadow_functools.partial(meadow_SegmentBounds, meadow_self_2406f4a.wordsize, meadow_self_2406f4a.signature))

    @_name_boundary.callable_contract({'self': 'meadow_self_702ea18'}, 'pcb__segments')
    def pcb__segments(meadow_self_702ea18):
        meadow_offset_local_02b2c31 = 0
        for meadow_i_ceafd3f in range(meadow_self_702ea18.segment_count):
            meadow_segment_local_c5de5f1 = meadow_self_702ea18._segments[meadow_i_ceafd3f]
            meadow_segment_byte_count_local_b45e091 = meadow_segment_local_c5de5f1.end - meadow_segment_local_c5de5f1.start
            meadow_segment_length_local_1c3cc6c = 4 * meadow_segment_byte_count_local_b45e091
            meadow_self_702ea18.segments.append(meadow_ID1.SegmentDescriptor(meadow_segment_local_c5de5f1, meadow_offset_local_02b2c31))
            meadow_offset_local_02b2c31 += meadow_segment_length_local_1c3cc6c
        meadow_offset_local_02b2c31 = 20 + meadow_self_702ea18.segment_count * (2 * meadow_self_702ea18.wordsize)
        meadow_padsize_local_346cfe5 = meadow_ID1.PAGE_SIZE - meadow_offset_local_02b2c31
        meadow_self_702ea18['padding'].vsSetLength(meadow_padsize_local_346cfe5)

    @_name_boundary.callable_contract({'self': 'meadow_self_1707caf'}, 'pcb_page_count')
    def pcb_page_count(meadow_self_1707caf):
        meadow_self_1707caf['buffer'].vsSetLength(meadow_ID1.PAGE_SIZE * meadow_self_1707caf.page_count)

    @_name_boundary.callable_contract({'self': 'meadow_self_f2b8bc3', 'ea': 'meadow_ea_7e688ef'}, 'get_segment')
    def meadow_get_segment(meadow_self_f2b8bc3, meadow_ea_7e688ef):
        """
        find the segment that contains the given effective address.

        Returns:
          SegmentDescriptor: segment metadata and location.

        Raises:
          KeyError: if the given address is not in a segment.
        """
        for meadow_segment_local_0648ad0 in meadow_self_f2b8bc3.segments:
            if meadow_segment_local_0648ad0.bounds.start <= meadow_ea_7e688ef < meadow_segment_local_0648ad0.bounds.end:
                return meadow_segment_local_0648ad0
        raise KeyError(meadow_ea_7e688ef)

    @_name_boundary.callable_contract({'self': 'meadow_self_0a803f5', 'ea': 'meadow_ea_6bbcf3b'}, 'get_next_segment')
    def meadow_get_next_segment(meadow_self_0a803f5, meadow_ea_6bbcf3b):
        """
        Fetch the next segment.

        Arguments:
          ea (int): an effective address that should fall within a segment.

        Returns:
          int: the effective address of the start of a segment.

        Raises:
          IndexError: if no more segments are found after the given segment.
          KeyError: if the given effective address does not fall within a segment.
        """
        for meadow_i_43c296b, meadow_segment_local_f0eeb36 in enumerate(meadow_self_0a803f5.segments):
            if meadow_segment_local_f0eeb36.bounds.start <= meadow_ea_6bbcf3b < meadow_segment_local_f0eeb36.bounds.end:
                if meadow_i_43c296b == len(meadow_self_0a803f5.segments):
                    raise IndexError(meadow_ea_6bbcf3b)
                else:
                    return meadow_self_0a803f5.segments[meadow_i_43c296b + 1]
        raise KeyError(meadow_ea_6bbcf3b)

    @_name_boundary.callable_contract({'self': 'meadow_self_907c07b', 'ea': 'meadow_ea_fe2610c'}, 'get_flags')
    def meadow_get_flags(meadow_self_907c07b, meadow_ea_fe2610c):
        """
        Fetch the flags for the given effective address.

        > Each byte of the program has 32-bit flags (low 8 bits keep the byte value).
        > These 32 bits are used in GetFlags/SetFlags functions.
        via: https://www.hex-rays.com/products/ida/support/idapython_docs/idc-module.html

        Arguments:
          ea (int): the effective address.

        Returns:
          int: the flags for the given address.

        Raises:
          KeyError: if the given address does not fall within a segment.
        """
        meadow_seg_local_41fb58f = _name_boundary.attributes(meadow_self_907c07b)['get_segment'](meadow_ea_fe2610c)
        meadow_offset_local_8b70750 = meadow_seg_local_41fb58f.offset + 4 * (meadow_ea_fe2610c - meadow_seg_local_41fb58f.bounds.start)
        return struct.unpack_from('<I', meadow_self_907c07b.buffer, meadow_offset_local_8b70750)[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_986f59d'}, 'validate')
    def meadow_validate(meadow_self_986f59d):
        if meadow_self_986f59d.signature not in (meadow_ID1.Signature, meadow_ID1.SignatureV6):
            raise ValueError('bad signature')
        for meadow_segment_local_0e65011 in meadow_self_986f59d.segments:
            if meadow_segment_local_0e65011.bounds.start > meadow_segment_local_0e65011.bounds.end:
                raise ValueError('segment ends before it starts')
        return True
    get_segment = meadow_get_segment
    get_next_segment = meadow_get_next_segment
    get_flags = meadow_get_flags
    validate = meadow_validate

class meadow_NAM(meadow_vstruct.VStruct):
    """
    contains pointers to named items.
    """
    PAGE_SIZE = 8192

    @_name_boundary.callable_contract({'self': 'meadow_self_db908a8', 'wordsize': 'meadow_wordsize_local_1849491', 'buf': 'meadow_buf_local_e846a3a'}, '__init__')
    def __init__(meadow_self_db908a8, meadow_wordsize_local_1849491, meadow_buf_local_e846a3a=None):
        meadow_vstruct.VStruct.__init__(meadow_self_db908a8)
        meadow_self_db908a8.wordsize = meadow_wordsize_local_1849491
        if meadow_wordsize_local_1849491 == 4:
            meadow_self_db908a8.v_word = v_uint32
            meadow_self_db908a8.word_fmt = 'I'
        elif meadow_wordsize_local_1849491 == 8:
            meadow_self_db908a8.v_word = v_uint64
            meadow_self_db908a8.word_fmt = 'Q'
        else:
            raise RuntimeError('unexpected wordsize')
        meadow_self_db908a8.signature = v_bytes(size=4)
        meadow_self_db908a8.unk04 = v_uint32()
        meadow_self_db908a8.non_empty = v_uint32()
        meadow_self_db908a8.unk0C = v_uint32()
        meadow_self_db908a8.page_count = v_uint32()
        meadow_self_db908a8.unk14 = meadow_self_db908a8.v_word()
        meadow_self_db908a8.dword_count = v_uint32()
        meadow_self_db908a8.name_count = 0
        meadow_self_db908a8.padding = v_bytes(size=meadow_NAM.PAGE_SIZE - (6 * 4 + meadow_wordsize_local_1849491))
        meadow_self_db908a8.buffer = v_bytes()

    @_name_boundary.callable_contract({'self': 'meadow_self_6183a47'}, 'pcb_page_count')
    def pcb_page_count(meadow_self_6183a47):
        meadow_self_6183a47['buffer'].vsSetLength(meadow_self_6183a47.page_count * meadow_NAM.PAGE_SIZE)

    @_name_boundary.callable_contract({'self': 'meadow_self_77448ce'}, 'pcb_dword_count')
    def pcb_dword_count(meadow_self_77448ce):
        meadow_count_local_eb428ca = meadow_self_77448ce.dword_count
        if meadow_self_77448ce.wordsize == 8:
            meadow_count_local_eb428ca //= 2
        meadow_self_77448ce.name_count = meadow_count_local_eb428ca

    @_name_boundary.callable_contract({'self': 'meadow_self_2e67f63'}, 'validate')
    def meadow_validate(meadow_self_2e67f63):
        if meadow_self_2e67f63.signature != b'VA*\x00':
            raise ValueError('bad signature')
        if meadow_self_2e67f63.unk04 != 3:
            raise ValueError('unexpected unk04 value')
        if meadow_self_2e67f63.non_empty not in (0, 1):
            raise ValueError('unexpected non_empty value')
        if meadow_self_2e67f63.unk0C != 2048:
            raise ValueError('unexpected unk0C value')
        if meadow_self_2e67f63.unk14 != 0:
            raise ValueError('unexpected unk14 value')
        return True

    @_name_boundary.callable_contract({'self': 'meadow_self_ee50701'}, 'names')
    def meadow_names(meadow_self_ee50701):
        meadow_count_local_0f28230 = meadow_self_ee50701.dword_count
        if meadow_self_ee50701.wordsize == 8:
            meadow_count_local_0f28230 //= 2
        meadow_fmt_local_6a13835 = '<{count:d}{word_fmt:s}'.format(count=meadow_count_local_0f28230, word_fmt=meadow_self_ee50701.word_fmt)
        meadow_size_local_27c3739 = struct.calcsize(meadow_fmt_local_6a13835)
        if meadow_size_local_27c3739 > len(meadow_self_ee50701.buffer):
            raise ValueError('buffer too small')
        return _name_boundary.attributes(struct)['unpack'](meadow_fmt_local_6a13835, meadow_self_ee50701.buffer[:meadow_size_local_27c3739])
    validate = meadow_validate
    names = meadow_names
meadow_SectionDescriptor = _name_boundary.named_record('SectionDescriptor', ['name', 'cls'])
meadow_SECTIONS = [meadow_SectionDescriptor('id0', meadow_ID0), meadow_SectionDescriptor('id1', meadow_ID1), meadow_SectionDescriptor('nam', meadow_NAM), meadow_SectionDescriptor('seg', None), meadow_SectionDescriptor('til', meadow_TIL), meadow_SectionDescriptor('id2', None)]

class meadow_IDB(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_7700f28', 'buf': 'meadow_buf_local_b2e1c20'}, '__init__')
    def __init__(meadow_self_7700f28, meadow_buf_local_b2e1c20):
        meadow_vstruct.VStruct.__init__(meadow_self_7700f28)
        meadow_self_7700f28.buf = meadow_idb.memview(meadow_buf_local_b2e1c20)
        meadow_self_7700f28.sections = []
        meadow_self_7700f28.id0 = None
        meadow_self_7700f28.id1 = None
        meadow_self_7700f28.nam = None
        meadow_self_7700f28.seg = None
        meadow_self_7700f28.til = None
        meadow_self_7700f28.id2 = None
        meadow_self_7700f28.header = meadow_FileHeader(meadow_self_7700f28.buf)
        meadow_self_7700f28.wordsize = 0
        meadow_self_7700f28.uint = ValueError

    @_name_boundary.callable_contract({'self': 'meadow_self_19c74d5'}, 'pcb_header')
    def pcb_header(meadow_self_19c74d5):
        if meadow_self_19c74d5.header.signature == b'IDA1':
            meadow_self_19c74d5.wordsize = 4
            meadow_self_19c74d5.uint = _name_boundary.attributes(meadow_idb)['netnode'].uint32
        elif meadow_self_19c74d5.header.signature == b'IDA2':
            meadow_self_19c74d5.wordsize = 8
            meadow_self_19c74d5.uint = _name_boundary.attributes(meadow_idb)['netnode'].uint64
        else:
            raise RuntimeError('unexpected file signature: %s' % meadow_self_19c74d5.header.signature)
        for meadow_offset_local_3f08edd in meadow_self_19c74d5.header.offsets:
            if meadow_offset_local_3f08edd == 0:
                meadow_self_19c74d5.sections.append(None)
                continue
            meadow_sectionbuf_local_6351c2d = meadow_self_19c74d5.buf[meadow_offset_local_3f08edd:]
            meadow_section_local_f33652d = meadow_Section(meadow_self_19c74d5.header.version)
            meadow_section_local_f33652d.vsParse(meadow_sectionbuf_local_6351c2d)
            meadow_self_19c74d5.sections.append(meadow_section_local_f33652d)
        for meadow_i_0927fbd, meadow_sectiondef_72e6698 in enumerate(meadow_SECTIONS):
            if meadow_i_0927fbd > len(meadow_self_19c74d5.sections):
                meadow_logger.debug('missing section: %s', meadow_sectiondef_72e6698.name)
                continue
            meadow_section_local_f33652d = meadow_self_19c74d5.sections[meadow_i_0927fbd]
            if not meadow_section_local_f33652d:
                meadow_logger.debug('missing section: %s', meadow_sectiondef_72e6698.name)
                continue
            if not meadow_sectiondef_72e6698.cls:
                meadow_logger.warning('section class not implemented: %s', meadow_sectiondef_72e6698.name)
                continue
            meadow_s_local_06ebcf3 = meadow_sectiondef_72e6698.cls(buf=meadow_section_local_f33652d.contents, wordsize=meadow_self_19c74d5.wordsize)
            meadow_s_local_06ebcf3.vsParse(meadow_section_local_f33652d.contents)
            if isinstance(meadow_s_local_06ebcf3, meadow_TIL):
                meadow_s_local_06ebcf3.inf = meadow_Root(meadow_self_19c74d5).idainfo
            object.__setattr__(meadow_self_19c74d5, meadow_sectiondef_72e6698.name, meadow_s_local_06ebcf3)
            meadow_logger.debug('parsed section: %s', meadow_sectiondef_72e6698.name)

    @_name_boundary.callable_contract({'self': 'meadow_self_790566a'}, 'validate')
    def meadow_validate(meadow_self_790566a):
        _name_boundary.attributes(meadow_self_790566a.header)['validate']()
        _name_boundary.attributes(meadow_self_790566a.id0)['validate']()
        _name_boundary.attributes(meadow_self_790566a.id1)['validate']()
        _name_boundary.attributes(meadow_self_790566a.nam)['validate']()
        _name_boundary.attributes(meadow_self_790566a.til)['validate']()
        return True
    validate = meadow_validate
_name_boundary.module_contract(globals(), {'FileHeader': 'meadow_FileHeader', 'MaxKeyStrategy': 'meadow_MaxKeyStrategy', 'abc': 'meadow_abc', 're': 'meadow_re', 'BranchEntryPointer': 'meadow_BranchEntryPointer', 'EXACT_MATCH': 'meadow_EXACT_MATCH', 'SECTIONS': 'meadow_SECTIONS', 'logger': 'meadow_logger', 'IDB': 'meadow_IDB', 'MIN_KEY': 'meadow_MIN_KEY', 'ExactMatchStrategy': 'meadow_ExactMatchStrategy', 'namedtuple': 'meadow_namedtuple', 'PrefixMatchStrategy': 'meadow_PrefixMatchStrategy', 'functools': 'meadow_functools', 'COMPRESSION_METHOD': 'meadow_COMPRESSION_METHOD', 'ID0': 'meadow_ID0', 'SectionHeader': 'meadow_SectionHeader', 'NAM': 'meadow_NAM', 'PREFIX_MATCH': 'meadow_PREFIX_MATCH', 'BranchEntry': 'meadow_BranchEntry', 'vstruct': 'meadow_vstruct', 'MAX_KEY': 'meadow_MAX_KEY', 'zlib': 'meadow_zlib', 'Page': 'meadow_Page', 'LeafEntry': 'meadow_LeafEntry', 'logging': 'meadow_logging', 'LeafEntryPointer': 'meadow_LeafEntryPointer', 'SIZEOF_ENTRY': 'meadow_SIZEOF_ENTRY', 'FindStrategy': 'meadow_FindStrategy', 'SectionDescriptor': 'meadow_SectionDescriptor', 'idb': 'meadow_idb', 'Cursor': 'meadow_Cursor', 'ID1': 'meadow_ID1', 'ROUND_DOWN_MATCH': 'meadow_ROUND_DOWN_MATCH', 'TIL': 'meadow_TIL', 'Section': 'meadow_Section', 'RoundDownMatchStrategy': 'meadow_RoundDownMatchStrategy', 'Root': 'meadow_Root', 'MinKeyStrategy': 'meadow_MinKeyStrategy', 'SegmentBounds': 'meadow_SegmentBounds', 'fullmatch': 'meadow_fullmatch'})
