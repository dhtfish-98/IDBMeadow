# Derived from idb/fileformat.py; original copyright and license retained in ORIGIN.md.
"""
lots of inspiration from: https://github.com/nlitsme/pyidbutil
"""
import idbmeadow.api_contract as _name_boundary
from idbmeadow.bounded_io import (
    DEFAULT_LIMITS as meadow_DEFAULT_LIMITS, ParseBudget as meadow_ParseBudget,
    IDBFormatError as meadow_FormatError, owned_buffer as meadow_owned_buffer,
    checked_span as meadow_checked_span, materialize as meadow_materialize,
)
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
    """The fixed 64/88 byte database header; offsets are rebuilt on each parse."""
    @_name_boundary.callable_contract({'self': 'meadow_self', 'buf': 'meadow_buf'}, '__init__')
    def __init__(meadow_self, meadow_buf):
        meadow_vstruct.VStruct.__init__(meadow_self)
        meadow_checked_span(meadow_buf, 0, 32, 'database header')
        meadow_self.version = struct.unpack_from('<H', meadow_buf, 30)[0]
        if meadow_self.version not in (1, 4, 5, 6):
            raise meadow_FormatError('unsupported database version')
        meadow_self.offsets = []
        meadow_self.checksums = []
        meadow_self.signature = v_bytes(size=4)
        meadow_self.unk04 = v_uint16()
        if meadow_self.version <= 4:
            for meadow_index in range(1, 6):
                meadow_self.vsAddField('offset' + str(meadow_index), v_uint32())
        else:
            meadow_self.offset1 = v_uint64()
            meadow_self.offset2 = v_uint64()
            meadow_self.unk16 = v_uint32()
        meadow_self.sig2 = v_uint32()
        meadow_self._version = v_uint16()
        if meadow_self.version <= 4:
            meadow_self.unk20 = v_uint32()
        else:
            for meadow_index in range(3, 6):
                meadow_self.vsAddField('offset' + str(meadow_index), v_uint64())
        for meadow_index in range(1, 6):
            meadow_self.vsAddField('checksum' + str(meadow_index), v_uint32())
        meadow_self.offset6 = v_uint32() if meadow_self.version <= 4 else v_uint64()
        meadow_self.checksum6 = v_uint32()

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        meadow_checked_span(meadow_data, meadow_offset, len(meadow_self), 'database header')
        if struct.unpack_from('<H', meadow_data, meadow_offset + 30)[0] != meadow_self.version:
            raise meadow_FormatError('database header version changed')
        meadow_end = meadow_vstruct.VStruct.vsParse(meadow_self, meadow_data, meadow_offset, False)
        meadow_self.offsets = [getattr(meadow_self, 'offset' + str(meadow_index)) for meadow_index in range(1, 7)]
        meadow_self.checksums = [getattr(meadow_self, 'checksum' + str(meadow_index)) for meadow_index in range(1, 7)]
        return meadow_end

    def validate(meadow_self):
        if meadow_self.signature not in (b'IDA0', b'IDA1', b'IDA2'):
            raise meadow_FormatError('bad database signature')
        if meadow_self.sig2 != 0xaabbccdd:
            raise meadow_FormatError('bad database secondary signature')
        if meadow_self.version not in (1, 4, 5, 6):
            raise meadow_FormatError('unsupported database version')
        return True
    meadow_validate = validate

@_name_boundary.class_contract('COMPRESSION_METHOD', {'NONE': 'meadow_NONE', 'ZLIB': 'meadow_ZLIB'})
class meadow_COMPRESSION_METHOD:
    meadow_NONE = 0
    meadow_ZLIB = 2

class meadow_SectionHeader(meadow_vstruct.VStruct):
    @_name_boundary.callable_contract({'self': 'meadow_self', 'version': 'meadow_version'}, '__init__')
    def __init__(meadow_self, meadow_version):
        meadow_vstruct.VStruct.__init__(meadow_self)
        if meadow_version not in (1, 4, 5, 6):
            raise meadow_FormatError('unsupported database version')
        meadow_self.version = meadow_version
        meadow_self.compression_method = v_uint8()
        meadow_self.length = v_uint32() if meadow_version <= 4 else v_uint64()
        meadow_self.is_compressed = False

    def pcb_compression_method(meadow_self):
        if meadow_self.compression_method not in (0, 2):
            raise meadow_FormatError('unsupported section compression method')
        meadow_self.is_compressed = meadow_self.compression_method == 2

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        meadow_checked_span(meadow_data, meadow_offset, len(meadow_self), 'section header')
        return meadow_vstruct.VStruct.vsParse(meadow_self, meadow_data, meadow_offset, False)

class meadow_Section(meadow_vstruct.VStruct):
    @_name_boundary.callable_contract({'self': 'meadow_self', 'version': 'meadow_version', 'budget': 'meadow_budget'}, '__init__')
    def __init__(meadow_self, meadow_version, *, meadow_budget=None):
        meadow_vstruct.VStruct.__init__(meadow_self)
        meadow_self.version = meadow_version
        meadow_self.header = meadow_SectionHeader(meadow_version)
        meadow_self._contents = v_bytes()
        meadow_self.contents = b''
        meadow_self._parse_budget = meadow_budget or meadow_ParseBudget()

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        meadow_data = meadow_owned_buffer(meadow_data, meadow_self._parse_budget.limits.max_input_bytes)
        # Preflight precedes v_bytes length/allocation. Only the declared bytes
        # belong to this member; the next section must never satisfy truncation.
        meadow_start = meadow_self.header.vsParse(meadow_data, meadow_offset)
        meadow_end = meadow_checked_span(meadow_data, meadow_start, meadow_self.header.length, 'section contents')
        if meadow_self.header.length > meadow_self._parse_budget.limits.max_input_bytes:
            raise meadow_FormatError('section encoded byte limit exceeded')
        meadow_payload = bytes(meadow_data[meadow_start:meadow_end])
        meadow_contents = meadow_materialize(meadow_payload, meadow_self.header.is_compressed, meadow_self._parse_budget)
        meadow_self.vsSetField('_contents', v_bytes(vbytes=meadow_payload))
        meadow_self.contents = meadow_contents
        return meadow_end

    def validate(meadow_self):
        if not meadow_self.header.length:
            raise meadow_FormatError('zero size')
        return True
    meadow_validate = validate

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
    """Finite flag-page table with the retained version-specific byte layout."""
    PAGE_SIZE = 8192
    SegmentDescriptor = _name_boundary.named_record('SegmentDescriptor', ['bounds', 'offset'])
    SignatureV6 = b'Va4\x00'
    Signature = b'VA*\x00'

    @_name_boundary.callable_contract({'self': 'meadow_self', 'wordsize': 'meadow_wordsize', 'buf': 'meadow_buf'}, '__init__')
    def __init__(meadow_self, meadow_wordsize, meadow_buf=None):
        meadow_vstruct.VStruct.__init__(meadow_self)
        if meadow_wordsize not in (4, 8):
            raise meadow_FormatError('unexpected wordsize')
        meadow_self.wordsize = meadow_wordsize
        meadow_self.v_word = v_uint32 if meadow_wordsize == 4 else v_uint64
        meadow_self.segments = []
        meadow_self.signature = v_bytes(size=4)

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        meadow_data = meadow_owned_buffer(meadow_data, meadow_DEFAULT_LIMITS.max_section_bytes)
        meadow_checked_span(meadow_data, meadow_offset, 4, 'flag page signature')
        meadow_signature = meadow_data[meadow_offset:meadow_offset + 4]
        if meadow_signature == meadow_self.Signature:
            meadow_checked_span(meadow_data, meadow_offset, 20, 'flag page header')
            meadow_unk04, meadow_count, meadow_unk0c, meadow_pages = struct.unpack_from('<IIII', meadow_data, meadow_offset + 4)
            meadow_prefix = 20
            meadow_words = 2
        elif meadow_signature == meadow_self.SignatureV6:
            meadow_checked_span(meadow_data, meadow_offset, 8, 'legacy flag page header')
            meadow_count, meadow_pages = struct.unpack_from('<HH', meadow_data, meadow_offset + 4)
            meadow_prefix = 8
            meadow_words = 3
        else:
            raise meadow_FormatError('unsupported flag page signature')
        # Preserve the earlier decoder's legacy padding convention. A modern
        # SDK interpretation of all legacy flags is not claimed by this phase.
        meadow_padding = meadow_self.PAGE_SIZE - (20 + meadow_count * 2 * meadow_self.wordsize)
        if meadow_padding < 0:
            raise meadow_FormatError('flag segment table exceeds header page')
        meadow_table_end = meadow_checked_span(meadow_data, meadow_offset + meadow_prefix, meadow_count * meadow_words * meadow_self.wordsize, 'flag segment table')
        meadow_body = meadow_checked_span(meadow_data, meadow_table_end, meadow_padding, 'flag page padding')
        if meadow_pages > (len(meadow_data) - meadow_offset) // meadow_self.PAGE_SIZE:
            raise meadow_FormatError('flag page count exceeds available pages')
        meadow_end = min(len(meadow_data), meadow_body + meadow_pages * meadow_self.PAGE_SIZE)
        meadow_segments = []
        meadow_array = meadow_vstruct.VArray()
        meadow_cursor = meadow_offset + meadow_prefix
        meadow_flags_offset = 0
        for meadow_index in range(meadow_count):
            meadow_bounds = meadow_SegmentBounds(meadow_self.wordsize, meadow_signature)
            meadow_cursor = meadow_bounds.vsParse(meadow_data, meadow_cursor)
            if meadow_bounds.end < meadow_bounds.start:
                raise meadow_FormatError('segment ends before it starts')
            meadow_length = 4 * (meadow_bounds.end - meadow_bounds.start)
            if meadow_length > meadow_end - meadow_body - meadow_flags_offset:
                raise meadow_FormatError('segment flags exceed available bytes')
            meadow_segments.append(meadow_self.SegmentDescriptor(meadow_bounds, meadow_flags_offset))
            meadow_array.vsAddElement(meadow_bounds)
            meadow_flags_offset += meadow_length
        meadow_vstruct.VStruct.__init__(meadow_self)
        meadow_self.signature = v_bytes(vbytes=meadow_signature)
        if meadow_signature == meadow_self.Signature:
            meadow_self.unk04 = v_uint32(meadow_unk04)
            meadow_self.segment_count = v_uint32(meadow_count)
            meadow_self.unk0C = v_uint32(meadow_unk0c)
            meadow_self.page_count = v_uint32(meadow_pages)
        else:
            meadow_self.segment_count = v_uint16(meadow_count)
            meadow_self.page_count = v_uint16(meadow_pages)
        meadow_self._segments = meadow_array
        meadow_self.padding = v_bytes(vbytes=memoryview(meadow_data)[meadow_table_end:meadow_body])
        meadow_self.buffer = v_bytes(vbytes=memoryview(meadow_data)[meadow_body:meadow_end])
        meadow_self.segments = meadow_segments
        return meadow_end

    @_name_boundary.callable_contract({'self': 'meadow_self', 'ea': 'meadow_ea'}, 'get_segment')
    def meadow_get_segment(meadow_self, meadow_ea):
        for meadow_segment in meadow_self.segments:
            if meadow_segment.bounds.start <= meadow_ea < meadow_segment.bounds.end:
                return meadow_segment
        raise KeyError(meadow_ea)

    @_name_boundary.callable_contract({'self': 'meadow_self', 'ea': 'meadow_ea'}, 'get_next_segment')
    def meadow_get_next_segment(meadow_self, meadow_ea):
        for meadow_index, meadow_segment in enumerate(meadow_self.segments):
            if meadow_segment.bounds.start <= meadow_ea < meadow_segment.bounds.end:
                if meadow_index + 1 >= len(meadow_self.segments):
                    raise IndexError(meadow_ea)
                return meadow_self.segments[meadow_index + 1]
        raise KeyError(meadow_ea)

    @_name_boundary.callable_contract({'self': 'meadow_self', 'ea': 'meadow_ea'}, 'get_flags')
    def meadow_get_flags(meadow_self, meadow_ea):
        meadow_segment = meadow_self.meadow_get_segment(meadow_ea)
        meadow_offset = meadow_segment.offset + 4 * (meadow_ea - meadow_segment.bounds.start)
        meadow_checked_span(meadow_self.buffer, meadow_offset, 4, 'address flags')
        return struct.unpack_from('<I', meadow_self.buffer, meadow_offset)[0]

    def meadow_validate(meadow_self):
        if meadow_self.signature not in (meadow_self.Signature, meadow_self.SignatureV6):
            raise meadow_FormatError('bad signature')
        for meadow_segment in meadow_self.segments:
            if meadow_segment.bounds.start > meadow_segment.bounds.end:
                raise meadow_FormatError('segment ends before it starts')
        return True
    get_segment = meadow_get_segment
    get_next_segment = meadow_get_next_segment
    get_flags = meadow_get_flags
    validate = meadow_validate

class meadow_NAM(meadow_vstruct.VStruct):
    """Fixed header and bounded name addresses without declared-size allocation."""
    PAGE_SIZE = 8192

    @_name_boundary.callable_contract({'self': 'meadow_self', 'wordsize': 'meadow_wordsize', 'buf': 'meadow_buf'}, '__init__')
    def __init__(meadow_self, meadow_wordsize, meadow_buf=None):
        meadow_vstruct.VStruct.__init__(meadow_self)
        if meadow_wordsize not in (4, 8):
            raise meadow_FormatError('unexpected wordsize')
        meadow_self.wordsize = meadow_wordsize
        meadow_self.v_word = v_uint32 if meadow_wordsize == 4 else v_uint64
        meadow_self.word_fmt = 'I' if meadow_wordsize == 4 else 'Q'
        meadow_self.name_count = 0

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        meadow_data = meadow_owned_buffer(meadow_data, meadow_DEFAULT_LIMITS.max_section_bytes)
        meadow_body = meadow_checked_span(meadow_data, meadow_offset, meadow_self.PAGE_SIZE, 'name header page')
        meadow_signature, meadow_unk04, meadow_nonempty, meadow_unk0c, meadow_pages = struct.unpack_from('<4sIIII', meadow_data, meadow_offset)
        meadow_unk14, meadow_count = struct.unpack_from('<' + meadow_self.word_fmt + 'I', meadow_data, meadow_offset + 20)
        meadow_prefix = meadow_offset + 24 + meadow_self.wordsize
        # Older NAM layouts expose historical header values differently.
        # Retain those values but never allocate their declared virtual size.
        meadow_end = min(len(meadow_data), meadow_body + meadow_pages * meadow_self.PAGE_SIZE)
        meadow_vstruct.VStruct.__init__(meadow_self)
        meadow_self.signature = v_bytes(vbytes=meadow_signature)
        meadow_self.unk04 = v_uint32(meadow_unk04)
        meadow_self.non_empty = v_uint32(meadow_nonempty)
        meadow_self.unk0C = v_uint32(meadow_unk0c)
        meadow_self.page_count = v_uint32(meadow_pages)
        meadow_self.unk14 = meadow_self.v_word(meadow_unk14)
        meadow_self.dword_count = v_uint32(meadow_count)
        meadow_self.name_count = meadow_count // (2 if meadow_self.wordsize == 8 else 1)
        meadow_self.padding = v_bytes(vbytes=memoryview(meadow_data)[meadow_prefix:meadow_body])
        meadow_self.buffer = v_bytes(vbytes=memoryview(meadow_data)[meadow_body:meadow_end])
        return meadow_end

    def meadow_validate(meadow_self):
        if meadow_self.signature != b'VA*\x00':
            raise meadow_FormatError('bad signature')
        if meadow_self.unk04 != 3:
            raise meadow_FormatError('unexpected unk04 value')
        if meadow_self.non_empty not in (0, 1):
            raise meadow_FormatError('unexpected non_empty value')
        if meadow_self.unk0C != 2048:
            raise meadow_FormatError('unexpected unk0C value')
        if meadow_self.unk14 != 0:
            raise meadow_FormatError('unexpected unk14 value')
        return True

    def meadow_names(meadow_self):
        meadow_count = meadow_self.dword_count // (2 if meadow_self.wordsize == 8 else 1)
        meadow_size = meadow_count * meadow_self.wordsize
        meadow_checked_span(meadow_self.buffer, 0, meadow_size, 'name address table')
        return tuple(meadow_item[0] for meadow_item in struct.iter_unpack('<' + meadow_self.word_fmt, meadow_self.buffer[:meadow_size]))
    validate = meadow_validate
    names = meadow_names
meadow_SectionDescriptor = _name_boundary.named_record('SectionDescriptor', ['name', 'cls'])
meadow_SECTIONS = [meadow_SectionDescriptor('id0', meadow_ID0), meadow_SectionDescriptor('id1', meadow_ID1), meadow_SectionDescriptor('nam', meadow_NAM), meadow_SectionDescriptor('seg', None), meadow_SectionDescriptor('til', meadow_TIL), meadow_SectionDescriptor('id2', None)]

class meadow_IDB(meadow_vstruct.VStruct):
    """Own one immutable snapshot and one aggregate materialization budget."""
    @_name_boundary.callable_contract({'self': 'meadow_self', 'buf': 'meadow_buf', 'limits': 'meadow_limits'}, '__init__')
    def __init__(meadow_self, meadow_buf, *, meadow_limits=meadow_DEFAULT_LIMITS):
        meadow_vstruct.VStruct.__init__(meadow_self)
        meadow_self._parse_budget = meadow_ParseBudget(meadow_limits)
        meadow_self.buf = meadow_owned_buffer(meadow_buf, meadow_limits.max_input_bytes)
        meadow_self.sections = []
        for meadow_section in meadow_SECTIONS:
            object.__setattr__(meadow_self, meadow_section.name, None)
        meadow_self.header = meadow_FileHeader(meadow_self.buf)
        meadow_self.wordsize = 0
        meadow_self.uint = ValueError

    @_name_boundary.callable_contract({'self': 'meadow_self', 'sbytes': 'meadow_data', 'offset': 'meadow_offset', 'fast': 'meadow_fast'}, 'vsParse')
    def vsParse(meadow_self, meadow_data, meadow_offset=0, meadow_fast=False):
        if meadow_offset != 0:
            raise meadow_FormatError('database parsing requires offset zero')
        meadow_self.buf = meadow_owned_buffer(meadow_data, meadow_self._parse_budget.limits.max_input_bytes)
        meadow_self._parse_budget = meadow_ParseBudget(meadow_self._parse_budget.limits)
        meadow_self.sections = []
        for meadow_section in meadow_SECTIONS:
            object.__setattr__(meadow_self, meadow_section.name, None)
        meadow_self.vsSetField('header', meadow_FileHeader(meadow_self.buf))
        return meadow_vstruct.VStruct.vsParse(meadow_self, meadow_self.buf, 0, False)

    def pcb_header(meadow_self):
        meadow_self.header.validate()
        if meadow_self.header.signature == b'IDA1':
            meadow_self.wordsize = 4
            meadow_self.uint = _name_boundary.attributes(meadow_idb)['netnode'].uint32
        elif meadow_self.header.signature == b'IDA2':
            meadow_self.wordsize = 8
            meadow_self.uint = _name_boundary.attributes(meadow_idb)['netnode'].uint64
        else:
            raise meadow_FormatError('unsupported database signature')
        meadow_spans = []
        for meadow_offset in meadow_self.header.offsets:
            if meadow_offset == 0:
                meadow_self.sections.append(None)
                continue
            if meadow_offset < (62 if meadow_self.header.version == 1 else len(meadow_self.header)):
                raise meadow_FormatError('section overlaps database header')
            meadow_header = meadow_SectionHeader(meadow_self.header.version)
            meadow_start = meadow_header.vsParse(meadow_self.buf, meadow_offset)
            meadow_end = meadow_checked_span(meadow_self.buf, meadow_start, meadow_header.length, 'section contents')
            for meadow_previous_start, meadow_previous_end in meadow_spans:
                if meadow_offset < meadow_previous_end and meadow_end > meadow_previous_start:
                    raise meadow_FormatError('overlapping database sections')
            meadow_spans.append((meadow_offset, meadow_end))
            meadow_section = meadow_Section(meadow_self.header.version, budget=meadow_self._parse_budget)
            meadow_section.vsParse(meadow_self.buf, meadow_offset)
            meadow_self.sections.append(meadow_section)
        for meadow_descriptor, meadow_section in zip(meadow_SECTIONS, meadow_self.sections):
            if meadow_section is None or meadow_descriptor.cls is None:
                continue
            meadow_parsed = meadow_descriptor.cls(buf=meadow_section.contents, wordsize=meadow_self.wordsize)
            if isinstance(meadow_parsed, meadow_TIL):
                meadow_parsed._parse_budget = meadow_self._parse_budget
            meadow_parsed.vsParse(meadow_section.contents)
            if isinstance(meadow_parsed, meadow_TIL):
                meadow_parsed.inf = meadow_Root(meadow_self).idainfo
            object.__setattr__(meadow_self, meadow_descriptor.name, meadow_parsed)

    def validate(meadow_self):
        meadow_self.header.validate()
        for meadow_name in ('id0', 'id1', 'nam'):
            meadow_section = getattr(meadow_self, meadow_name)
            if meadow_section is None:
                raise meadow_FormatError('missing required section: ' + meadow_name)
            _name_boundary.attributes(meadow_section)['validate']()
        return True
    meadow_validate = validate
_name_boundary.module_contract(globals(), {'FileHeader': 'meadow_FileHeader', 'MaxKeyStrategy': 'meadow_MaxKeyStrategy', 'abc': 'meadow_abc', 're': 'meadow_re', 'BranchEntryPointer': 'meadow_BranchEntryPointer', 'EXACT_MATCH': 'meadow_EXACT_MATCH', 'SECTIONS': 'meadow_SECTIONS', 'logger': 'meadow_logger', 'IDB': 'meadow_IDB', 'MIN_KEY': 'meadow_MIN_KEY', 'ExactMatchStrategy': 'meadow_ExactMatchStrategy', 'namedtuple': 'meadow_namedtuple', 'PrefixMatchStrategy': 'meadow_PrefixMatchStrategy', 'functools': 'meadow_functools', 'COMPRESSION_METHOD': 'meadow_COMPRESSION_METHOD', 'ID0': 'meadow_ID0', 'SectionHeader': 'meadow_SectionHeader', 'NAM': 'meadow_NAM', 'PREFIX_MATCH': 'meadow_PREFIX_MATCH', 'BranchEntry': 'meadow_BranchEntry', 'vstruct': 'meadow_vstruct', 'MAX_KEY': 'meadow_MAX_KEY', 'zlib': 'meadow_zlib', 'Page': 'meadow_Page', 'LeafEntry': 'meadow_LeafEntry', 'logging': 'meadow_logging', 'LeafEntryPointer': 'meadow_LeafEntryPointer', 'SIZEOF_ENTRY': 'meadow_SIZEOF_ENTRY', 'FindStrategy': 'meadow_FindStrategy', 'SectionDescriptor': 'meadow_SectionDescriptor', 'idb': 'meadow_idb', 'Cursor': 'meadow_Cursor', 'ID1': 'meadow_ID1', 'ROUND_DOWN_MATCH': 'meadow_ROUND_DOWN_MATCH', 'TIL': 'meadow_TIL', 'Section': 'meadow_Section', 'RoundDownMatchStrategy': 'meadow_RoundDownMatchStrategy', 'Root': 'meadow_Root', 'MinKeyStrategy': 'meadow_MinKeyStrategy', 'SegmentBounds': 'meadow_SegmentBounds', 'fullmatch': 'meadow_fullmatch'})
