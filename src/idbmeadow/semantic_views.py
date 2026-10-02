# Derived from idb/analysis.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import types as meadow_types
import logging as meadow_logging
import binascii as meadow_binascii
import datetime as meadow_datetime
import itertools as meadow_itertools
from random import randint as meadow_randint
from collections import Counter as meadow_Counter, namedtuple as meadow_namedtuple
import six as meadow_six
import vstruct as meadow_vstruct
from vstruct.primitives import *
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
import idbmeadow.type_records as _boundary_import_idb_typeinf
import idbmeadow as meadow_idb
import idbmeadow.type_codes as _boundary_import_idb_typeinf_flags
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)
meadow__counter = meadow_Counter()

@_name_boundary.callable_contract({'prefix': 'meadow_prefix_69b8d5d'}, 'name_generator')
def meadow_name_generator(meadow_prefix_69b8d5d='unknown'):

    @_name_boundary.callable_contract({'index': 'meadow_index_13c68c0'}, 'inner')
    def meadow_inner_f3c31a2(meadow_index_13c68c0=meadow_randint(0, 4294967295)):
        meadow__counter[meadow_index_13c68c0] += 1
        return '{}{}'.format(meadow_prefix_69b8d5d, meadow__counter[meadow_index_13c68c0])
    return meadow_inner_f3c31a2

@_name_boundary.callable_contract({'flag': 'meadow_flag_37420b2', 'flags': 'meadow_flags_local_e8aab3d'}, 'is_flag_set')
def meadow_is_flag_set(meadow_flags_local_e8aab3d, meadow_flag_37420b2):
    return meadow_flags_local_e8aab3d & meadow_flag_37420b2 == meadow_flag_37420b2

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_f43dea5', 'wordsize': 'meadow_wordsize_local_70726b5'}, 'as_unix_timestamp')
def meadow_as_unix_timestamp(meadow_buf_local_f43dea5, meadow_wordsize_local_70726b5=None):
    """
    parse unix timestamp bytes into a timestamp.
    """
    meadow_q_67fdcb6 = struct.unpack_from('<I', meadow_buf_local_f43dea5, 0)[0]
    return meadow_datetime.datetime.fromtimestamp(meadow_q_67fdcb6, meadow_datetime.timezone.utc)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_a3b62c2', 'wordsize': 'meadow_wordsize_local_5f6ff53'}, 'as_md5')
def meadow_as_md5(meadow_buf_local_a3b62c2, meadow_wordsize_local_5f6ff53=None):
    """
    parse raw md5 bytes into a hex-formatted string.
    """
    return meadow_binascii.hexlify(meadow_buf_local_a3b62c2).decode('ascii')

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_3ef8169', 'wordsize': 'meadow_wordsize_local_09e4f92'}, 'as_sha256')
def meadow_as_sha256(meadow_buf_local_3ef8169, meadow_wordsize_local_09e4f92=None):
    """
    parse raw sha256 bytes into a hex-formatted string.
    """
    return meadow_binascii.hexlify(meadow_buf_local_3ef8169).decode('ascii')

@_name_boundary.callable_contract({'V': 'meadow_V_67a71cd', 'buf': 'meadow_buf_local_c4b7b8d', 'wordsize': 'meadow_wordsize_local_8cb7027'}, 'cast')
def meadow_cast(meadow_buf_local_c4b7b8d, meadow_V_67a71cd, meadow_wordsize_local_8cb7027=None):
    """
    apply a vstruct class to a sequence of bytes.

    Args:
        buf (bytes): the bytes to parse.
        V (type[vstruct.VStruct]): the vstruct class.

    Returns:
        V: the parsed instance of V.

    Example::

        s = cast(buf, Stat)
        assert s.gid == 0x1000
    """
    meadow_v_b7e8a23 = meadow_V_67a71cd(wordsize=meadow_wordsize_local_8cb7027)
    meadow_v_b7e8a23.vsParse(meadow_buf_local_c4b7b8d)
    return meadow_v_b7e8a23

@_name_boundary.callable_contract({'V': 'meadow_V_c8351a1'}, 'as_cast')
def meadow_as_cast(meadow_V_c8351a1):
    """
    create a partial function that casts buffers to the given vstruct.

    Args:
        V (type[vstruct.VStruct]): the vstruct class.

    Returns:
        callable[bytes]->V: the function that parses buffers into V instances.

    Example::

        S = as_cast(Stat)
        s = S(buf)
        assert s.gid == 0x1000
    """

    @_name_boundary.callable_contract({'buf': 'meadow_buf_local_a113e80', 'wordsize': 'meadow_wordsize_local_d3ce8d6'}, 'inner')
    def meadow_inner_7b527eb(meadow_buf_local_a113e80, meadow_wordsize_local_d3ce8d6=None):
        return meadow_cast(meadow_buf_local_a113e80, meadow_V_c8351a1, wordsize=meadow_wordsize_local_d3ce8d6)
    _name_boundary.write_attribute(meadow_inner_7b527eb, 'V', _name_boundary.attributes(meadow_V_c8351a1)['__name__'])
    return meadow_inner_7b527eb

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_ec504e5', 'offset': 'meadow_offset_local_ee47565'}, 'unpack_dd')
def meadow_unpack_dd(meadow_buf_local_ec504e5, meadow_offset_local_ee47565=0):
    """
    unpack up to 32-bits using the IDA-specific data packing format.

    Args:
      buf (bytes): the region to parse.
      offset (int): the offset into the region from which to unpack. default: 0.

    Returns:
      (int, int): the parsed dword, and the number of bytes consumed.

    Raises:
      KeyError: if the bounds of the region are exceeded.
    """
    if meadow_offset_local_ee47565 != 0:
        meadow_buf_local_ec504e5 = meadow_buf_local_ec504e5[meadow_offset_local_ee47565:]
    meadow_header_local_2489aa6 = meadow_six.indexbytes(meadow_buf_local_ec504e5, 0)
    if meadow_header_local_2489aa6 & 128 == 0:
        return (meadow_header_local_2489aa6, 1)
    elif meadow_header_local_2489aa6 & 192 != 192:
        return (((meadow_header_local_2489aa6 & 127) << 8) + meadow_six.indexbytes(meadow_buf_local_ec504e5, 1), 2)
    else:
        if meadow_header_local_2489aa6 & 224 == 224:
            meadow_hi_local_3a5ac70 = (meadow_six.indexbytes(meadow_buf_local_ec504e5, 1) << 8) + meadow_six.indexbytes(meadow_buf_local_ec504e5, 2)
            meadow_low_cb8bc5d = (meadow_six.indexbytes(meadow_buf_local_ec504e5, 3) << 8) + meadow_six.indexbytes(meadow_buf_local_ec504e5, 4)
            meadow_size_local_a9dccf5 = 5
        else:
            meadow_hi_local_3a5ac70 = ((meadow_header_local_2489aa6 & 63) << 8) + meadow_six.indexbytes(meadow_buf_local_ec504e5, 1)
            meadow_low_cb8bc5d = (meadow_six.indexbytes(meadow_buf_local_ec504e5, 2) << 8) + meadow_six.indexbytes(meadow_buf_local_ec504e5, 3)
            meadow_size_local_a9dccf5 = 4
        return ((meadow_hi_local_3a5ac70 << 16) + meadow_low_cb8bc5d, meadow_size_local_a9dccf5)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_865de04', 'offset': 'meadow_offset_local_11e6b4c'}, 'unpack_dw')
def meadow_unpack_dw(meadow_buf_local_865de04, meadow_offset_local_11e6b4c=0):
    """
    unpack word.
    """
    if meadow_offset_local_11e6b4c != 0:
        meadow_buf_local_865de04 = meadow_buf_local_865de04[meadow_offset_local_11e6b4c:]
    meadow_header_local_63c52d8 = meadow_six.indexbytes(meadow_buf_local_865de04, 0)
    if meadow_header_local_63c52d8 & 128 == 0:
        return (meadow_header_local_63c52d8, 1)
    elif meadow_header_local_63c52d8 & 192 != 192:
        return ((meadow_header_local_63c52d8 << 8) + meadow_six.indexbytes(meadow_buf_local_865de04, 1) & 32767, 2)
    else:
        return ((meadow_six.indexbytes(meadow_buf_local_865de04, 1) << 8) + meadow_six.indexbytes(meadow_buf_local_865de04, 2), 3)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_3b398b3', 'offset': 'meadow_offset_local_41cc7fc'}, 'unpack_dq')
def meadow_unpack_dq(meadow_buf_local_3b398b3, meadow_offset_local_41cc7fc=0):
    """
    unpack qword.
    """
    if meadow_offset_local_41cc7fc != 0:
        meadow_buf_local_3b398b3 = meadow_buf_local_3b398b3[meadow_offset_local_41cc7fc:]
    meadow_dw1_0a47117, meadow_d1_b57d349 = meadow_unpack_dd(meadow_buf_local_3b398b3)
    meadow_dw2_641188b, meadow_d2_77aea7d = meadow_unpack_dd(meadow_buf_local_3b398b3, offset=meadow_d1_b57d349)
    return ((meadow_dw2_641188b << 32) + meadow_dw1_0a47117, meadow_d1_b57d349 + meadow_d2_77aea7d)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_fb443d0'}, 'unpack_dds')
def meadow_unpack_dds(meadow_buf_local_fb443d0):
    meadow_offset_local_c78a8a7 = 0
    while meadow_offset_local_c78a8a7 < len(meadow_buf_local_fb443d0):
        meadow_val_local_f1a0f5f, meadow_size_local_766ef99 = meadow_unpack_dd(meadow_buf_local_fb443d0, offset=meadow_offset_local_c78a8a7)
        yield meadow_val_local_f1a0f5f
        meadow_offset_local_c78a8a7 += meadow_size_local_766ef99

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_23834bb'}, 'unpack_dqs')
def meadow_unpack_dqs(meadow_buf_local_23834bb):
    meadow_offset_local_99671a7 = 0
    while meadow_offset_local_99671a7 < len(meadow_buf_local_23834bb):
        meadow_val_local_174dcb5, meadow_size_local_72928c4 = meadow_unpack_dq(meadow_buf_local_23834bb, offset=meadow_offset_local_99671a7)
        yield meadow_val_local_174dcb5
        meadow_offset_local_99671a7 += meadow_size_local_72928c4

@_name_boundary.class_contract('Unpacker', {'_do_unpack': 'meadow__do_unpack', 'dd': 'meadow_dd', 'dq': 'meadow_dq', 'dw': 'meadow_dw', 'addr': 'meadow_addr', 'off': 'meadow_off', 'should_log': 'meadow_should_log'})
class meadow_Unpacker:

    @_name_boundary.callable_contract({'self': 'meadow_self_0cc9284', 'should_log': 'meadow_should_log_6c9902e', 'buf': 'meadow_buf_local_bfc933e', 'wordsize': 'meadow_wordsize_local_e337000', 'offset': 'meadow_offset_local_d99278e'}, '__init__')
    def __init__(meadow_self_0cc9284, meadow_buf_local_bfc933e, meadow_wordsize_local_e337000, meadow_offset_local_d99278e=0, meadow_should_log_6c9902e=False):
        meadow_self_0cc9284.offset = meadow_offset_local_d99278e
        meadow_self_0cc9284.wordsize = meadow_wordsize_local_e337000
        meadow_self_0cc9284.buf = meadow_buf_local_bfc933e
        _name_boundary.attributes(meadow_self_0cc9284)['should_log'] = meadow_should_log_6c9902e

    @_name_boundary.callable_contract({'self': 'meadow_self_cb76165', 'unpack_fn': 'meadow_unpack_fn_20b0a75'}, '_do_unpack')
    def meadow__do_unpack(meadow_self_cb76165, meadow_unpack_fn_20b0a75):
        meadow_v_fa5b7b0, meadow_delta_d91e6ce = meadow_unpack_fn_20b0a75(meadow_self_cb76165.buf, offset=meadow_self_cb76165.offset)
        if _name_boundary.attributes(meadow_self_cb76165)['should_log']:
            meadow_logger.debug('%s at %x: %x', _name_boundary.attributes(meadow_unpack_fn_20b0a75)['__name__'], meadow_self_cb76165.offset, meadow_v_fa5b7b0)
        meadow_self_cb76165.offset += meadow_delta_d91e6ce
        return meadow_v_fa5b7b0

    @_name_boundary.callable_contract({'self': 'meadow_self_1e0f1e9'}, 'dd')
    def meadow_dd(meadow_self_1e0f1e9):
        return _name_boundary.attributes(meadow_self_1e0f1e9)['_do_unpack'](meadow_unpack_dd)

    @_name_boundary.callable_contract({'self': 'meadow_self_da34351'}, 'dq')
    def meadow_dq(meadow_self_da34351):
        return _name_boundary.attributes(meadow_self_da34351)['_do_unpack'](meadow_unpack_dq)

    @_name_boundary.callable_contract({'self': 'meadow_self_f1df3ca'}, 'dw')
    def meadow_dw(meadow_self_f1df3ca):
        return _name_boundary.attributes(meadow_self_f1df3ca)['_do_unpack'](meadow_unpack_dw)

    @_name_boundary.callable_contract({'self': 'meadow_self_92ce90a'}, 'addr')
    def meadow_addr(meadow_self_92ce90a):
        if meadow_self_92ce90a.wordsize == 4:
            return _name_boundary.attributes(meadow_self_92ce90a)['_do_unpack'](meadow_unpack_dd)
        elif meadow_self_92ce90a.wordsize == 8:
            return _name_boundary.attributes(meadow_self_92ce90a)['_do_unpack'](meadow_unpack_dq)
        else:
            raise RuntimeError('unexpected wordsize')

    @_name_boundary.callable_contract({'self': 'meadow_self_c0aa8c4'}, 'off')
    def meadow_off(meadow_self_c0aa8c4):
        meadow_offset_local_bfd5eac = _name_boundary.attributes(meadow_self_c0aa8c4)['addr']()
        meadow_mask_6528446 = 2 ** (meadow_self_c0aa8c4.wordsize * 8) - 1
        if meadow_offset_local_bfd5eac & 1 << meadow_self_c0aa8c4.wordsize * 8 - 1:
            return meadow_offset_local_bfd5eac | ~meadow_mask_6528446
        else:
            return meadow_offset_local_bfd5eac
meadow_Field = _name_boundary.named_record('Field', ['name', 'tag', 'index', 'cast', 'minver'])
meadow_Field.__new__.__defaults__ = (None,) * len(meadow_Field._fields)

@_name_boundary.class_contract('IndexType', {'str': 'meadow_str'})
class meadow_IndexType:

    @_name_boundary.callable_contract({'self': 'meadow_self_fb0d314', 'name': 'meadow_name_local_fd1a285'}, '__init__')
    def __init__(meadow_self_fb0d314, meadow_name_local_fd1a285):
        meadow_self_fb0d314.name = meadow_name_local_fd1a285

    @_name_boundary.callable_contract({'self': 'meadow_self_61e21f2'}, 'str')
    def meadow_str(meadow_self_61e21f2):
        return meadow_self_61e21f2.name.upper()
meadow_ALL = meadow_IndexType('all')
meadow_ADDRESSES = meadow_IndexType('addresses')
meadow_NUMBERS = meadow_IndexType('numbers')
meadow_NODES = meadow_IndexType('nodes')
meadow_VARIABLE_INDEXES = (meadow_ALL, meadow_ADDRESSES, meadow_NUMBERS, meadow_NODES)

@_name_boundary.class_contract('_Analysis', {'_is_address': 'meadow__is_address', '_is_node': 'meadow__is_node', '_is_number': 'meadow__is_number', 'get_field_tag': 'meadow_get_field_tag', 'get_field_index': 'meadow_get_field_index', 'idb': 'meadow_idb', 'nodeid': 'meadow_nodeid', 'netnode': 'meadow_netnode', '_fields_by_name': 'meadow__fields_by_name'})
class meadow__Analysis(object):
    """
    this is basically a metaclass for analyzers of IDA Pro netnode namespaces (named nodeid).
    provide set of fields, and parse them from netnodes (nodeid, tag, and optional index)
     when accessed.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_574d1a0', 'db': 'meadow_db_22fd1cb', 'nodeid': 'meadow_nodeid_f34e4a1', 'fields': 'meadow_fields_local_6470c77'}, '__init__')
    def __init__(meadow_self_574d1a0, meadow_db_22fd1cb, meadow_nodeid_f34e4a1, meadow_fields_local_6470c77):
        _name_boundary.attributes(meadow_self_574d1a0)['idb'] = meadow_db_22fd1cb
        _name_boundary.attributes(meadow_self_574d1a0)['nodeid'] = meadow_nodeid_f34e4a1
        _name_boundary.attributes(meadow_self_574d1a0)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_22fd1cb, meadow_nodeid_f34e4a1)
        meadow_self_574d1a0.fields = meadow_fields_local_6470c77
        meadow_idb_version_e36e75d = _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_22fd1cb, 'Root Node'))['altval'](index=-1)
        _name_boundary.attributes(meadow_self_574d1a0)['_fields_by_name'] = {meadow_f_cd58a8c.name: meadow_f_cd58a8c for meadow_f_cd58a8c in meadow_self_574d1a0.fields if not meadow_f_cd58a8c.minver or (meadow_f_cd58a8c.minver and meadow_idb_version_e36e75d >= meadow_f_cd58a8c.minver)}

    @_name_boundary.callable_contract({'self': 'meadow_self_322a4b4', 'index': 'meadow_index_76eb97d'}, '_is_address')
    def meadow__is_address(meadow_self_322a4b4, meadow_index_76eb97d):
        """
        does the given index fall within a segment?
        """
        try:
            _name_boundary.attributes(_name_boundary.attributes(meadow_self_322a4b4)['idb'].id1)['get_segment'](meadow_index_76eb97d)
            return True
        except KeyError:
            return False

    @_name_boundary.callable_contract({'self': 'meadow_self_28fa8a5', 'index': 'meadow_index_c363568'}, '_is_node')
    def meadow__is_node(meadow_self_28fa8a5, meadow_index_c363568):
        """
        does the index look like a raw nodeid?
        """
        if _name_boundary.attributes(meadow_self_28fa8a5)['idb'].wordsize == 4:
            return meadow_index_c363568 & 4278190080 == 4278190080
        elif _name_boundary.attributes(meadow_self_28fa8a5)['idb'].wordsize == 8:
            return meadow_index_c363568 & 18374686479671623680 == 18374686479671623680
        else:
            raise RuntimeError('unexpected wordsize')

    @_name_boundary.callable_contract({'self': 'meadow_self_97549a2', 'index': 'meadow_index_9b5f06a'}, '_is_number')
    def meadow__is_number(meadow_self_97549a2, meadow_index_9b5f06a):
        """
        does the index look like not (address or node)?
        """
        if _name_boundary.attributes(meadow_self_97549a2)['_is_node'](meadow_index_9b5f06a):
            return False
        if meadow_index_9b5f06a < 4096:
            return True
        if _name_boundary.attributes(meadow_self_97549a2)['_is_address'](meadow_index_9b5f06a):
            return False
        return True

    @_name_boundary.callable_contract({'self': 'meadow_self_0863627', 'key': 'meadow_key_local_4ded397'}, '__getattr__')
    def __getattr__(meadow_self_0863627, meadow_key_local_4ded397):
        """
        for the given field name, fetch the value from the appropriate netnode.
        if the field matches multiple indices, then return a mapping from index to value.

        Example::

            assert root.version == 695

        Example::

            assert 0x401000 in entrypoints.ordinals

        Example::

            assert entrypoints.ordinals[0] == 'DllMain'

        Args:
          key (str): the name of the field to fetch.

        Returns:
          any: if a parser was provided, then the parsed data.
            otherwise, the bytes associatd with the field.
            if the field matches multiple indices, then the result is mapping from index to value.

        Raises:
          KeyError: if the field does not exist.
        """
        if meadow_key_local_4ded397 not in _name_boundary.attributes(meadow_self_0863627)['_fields_by_name']:
            return _name_boundary.read_attribute(super(meadow__Analysis, meadow_self_0863627), meadow_key_local_4ded397)
        meadow_field_4c946ed = _name_boundary.attributes(meadow_self_0863627)['_fields_by_name'][meadow_key_local_4ded397]
        if _name_boundary.attributes(meadow_field_4c946ed)['index'] in meadow_VARIABLE_INDEXES:
            if _name_boundary.attributes(meadow_field_4c946ed)['index'] == meadow_ADDRESSES:
                meadow_nfilter_4235006 = _name_boundary.attributes(meadow_self_0863627)['_is_address']
            elif _name_boundary.attributes(meadow_field_4c946ed)['index'] == meadow_NUMBERS:
                meadow_nfilter_4235006 = _name_boundary.attributes(meadow_self_0863627)['_is_number']
            elif _name_boundary.attributes(meadow_field_4c946ed)['index'] == meadow_NODES:
                meadow_nfilter_4235006 = _name_boundary.attributes(meadow_self_0863627)['_is_node']
            elif _name_boundary.attributes(meadow_field_4c946ed)['index'] == meadow_ALL:
                meadow_nfilter_4235006 = lambda meadow_x_3e2a4b8: True
            else:
                raise ValueError('unexpected index')
            meadow_ret_local_d4485a2 = {}
            for meadow_sup_77e789f in _name_boundary.attributes(_name_boundary.attributes(meadow_self_0863627)['netnode'])['supentries'](tag=meadow_field_4c946ed.tag):
                if not meadow_nfilter_4235006(_name_boundary.attributes(meadow_sup_77e789f.parsed_key)['index']):
                    continue
                if meadow_field_4c946ed.cast is None:
                    meadow_ret_local_d4485a2[_name_boundary.attributes(meadow_sup_77e789f.parsed_key)['index']] = bytes(meadow_sup_77e789f.value)
                else:
                    meadow_v_7108dc2 = meadow_field_4c946ed.cast(bytes(meadow_sup_77e789f.value), wordsize=_name_boundary.attributes(meadow_self_0863627)['idb'].wordsize)
                    meadow_ret_local_d4485a2[_name_boundary.attributes(meadow_sup_77e789f.parsed_key)['index']] = meadow_v_7108dc2
            return meadow_ret_local_d4485a2
        else:
            meadow_v_7108dc2 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_0863627)['netnode'])['supval'](_name_boundary.attributes(meadow_field_4c946ed)['index'], tag=meadow_field_4c946ed.tag)
            if meadow_field_4c946ed.cast is None:
                return bytes(meadow_v_7108dc2)
            else:
                return meadow_field_4c946ed.cast(bytes(meadow_v_7108dc2), wordsize=_name_boundary.attributes(meadow_self_0863627)['idb'].wordsize)

    @_name_boundary.callable_contract({'self': 'meadow_self_5c977ee', 'name': 'meadow_name_local_2d5b6e1'}, 'get_field_tag')
    def meadow_get_field_tag(meadow_self_5c977ee, meadow_name_local_2d5b6e1):
        """
        get the tag associated with the given field name.

        Example::

            assert root.get_field_tag('version') == 'A'

        Args:
          key (str): the name of the field to fetch.

        Returns:
          str: a single character string tag.
        """
        return _name_boundary.attributes(meadow_self_5c977ee)['_fields_by_name'][meadow_name_local_2d5b6e1].tag

    @_name_boundary.callable_contract({'self': 'meadow_self_da3739c', 'name': 'meadow_name_local_3ee3a88'}, 'get_field_index')
    def meadow_get_field_index(meadow_self_da3739c, meadow_name_local_3ee3a88):
        """
        get the index associated with the given field name.
        Example::

            assert root.get_field_index('version') == root.db.uint(-1)

        Args:
          key (str): the name of the field to fetch.

        Returns:
          int or IndexType: the index, if its specified.
            otherwise, this will be an `IndexType` that indicates what indices are expected.
        """
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_da3739c)['_fields_by_name'][meadow_name_local_3ee3a88])['index']

@_name_boundary.callable_contract({'nodeid': 'meadow_nodeid_3cd9d71', 'fields': 'meadow_fields_local_37c4037'}, 'Analysis')
def meadow_Analysis(meadow_nodeid_3cd9d71, meadow_fields_local_37c4037):
    """
    build a partial constructor for _Analysis with the given nodeid and fields.

    Example::

        Root = Analysis('Root Node', [Field(...), ...])
        root = Root(some_idb)
        assert root.version == 695
    """

    @_name_boundary.callable_contract({'db': 'meadow_db_a105946'}, 'inner')
    def meadow_inner_aa69b35(meadow_db_a105946):
        return meadow__Analysis(meadow_db_a105946, meadow_nodeid_3cd9d71, meadow_fields_local_37c4037)
    return meadow_inner_aa69b35

class meadow_Reader(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['TypeString']):

    @_name_boundary.callable_contract({'self': 'meadow_self_259467c', 'buf': 'meadow_buf_local_b13f8c8', 'wordsize': 'meadow_wordsize_local_4c69416'}, '__init__')
    def __init__(meadow_self_259467c, meadow_buf_local_b13f8c8, meadow_wordsize_local_4c69416):
        _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['TypeString'].__init__(meadow_self_259467c, meadow_buf_local_b13f8c8)
        meadow_self_259467c.word = meadow_self_259467c.u32 if meadow_wordsize_local_4c69416 == 4 else meadow_self_259467c.u64
        meadow_self_259467c.word_ = _name_boundary.attributes(meadow_self_259467c)['u32_'] if meadow_wordsize_local_4c69416 == 4 else _name_boundary.attributes(meadow_self_259467c)['u64_']

    @_name_boundary.callable_contract({'self': 'meadow_self_614c8f5', 'size': 'meadow_size_local_657a817'}, 'bytes')
    def meadow_bytes(meadow_self_614c8f5, meadow_size_local_657a817):
        return _name_boundary.attributes(meadow_self_614c8f5)['read'](meadow_size_local_657a817)

    @_name_boundary.callable_contract({'self': 'meadow_self_0fcbb25', 'encoding': 'meadow_encoding_3ea2957', 'size': 'meadow_size_local_06f8eac'}, 'str')
    def meadow_str(meadow_self_0fcbb25, meadow_size_local_06f8eac, meadow_encoding_3ea2957='utf-8'):
        return _name_boundary.attributes(meadow_self_0fcbb25)['read'](meadow_size_local_06f8eac).decode(meadow_encoding_3ea2957)

    @_name_boundary.callable_contract({'self': 'meadow_self_bfc5433', 'big': 'meadow_big_75b7eb5'}, 'u16')
    def u16(meadow_self_bfc5433, meadow_big_75b7eb5=False):
        if meadow_big_75b7eb5:
            return _name_boundary.attributes(struct)['unpack']('>H', _name_boundary.attributes(meadow_self_bfc5433)['read'](2))[0]
        return _name_boundary.attributes(struct)['unpack']('<H', _name_boundary.attributes(meadow_self_bfc5433)['read'](2))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_a610672', 'big': 'meadow_big_c9d101f'}, 'u32')
    def u32(meadow_self_a610672, meadow_big_c9d101f=False):
        if meadow_big_c9d101f:
            return _name_boundary.attributes(struct)['unpack']('>L', _name_boundary.attributes(meadow_self_a610672)['read'](4))[0]
        return _name_boundary.attributes(struct)['unpack']('<L', _name_boundary.attributes(meadow_self_a610672)['read'](4))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_aa6a3ef', 'big': 'meadow_big_c344152'}, 'u64')
    def u64(meadow_self_aa6a3ef, meadow_big_c344152=False):
        if meadow_big_c344152:
            return _name_boundary.attributes(struct)['unpack']('>Q', _name_boundary.attributes(meadow_self_aa6a3ef)['read'](8))[0]
        return _name_boundary.attributes(struct)['unpack']('<Q', _name_boundary.attributes(meadow_self_aa6a3ef)['read'](8))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_276712f'}, 'u8_')
    def meadow_u8_(meadow_self_276712f):
        return meadow_self_276712f.u8()

    @_name_boundary.callable_contract({'self': 'meadow_self_901f2a2'}, 'u16_')
    def meadow_u16_(meadow_self_901f2a2):
        meadow_val_local_1f6ce83 = meadow_self_901f2a2.u8()
        if meadow_val_local_1f6ce83 == 255:
            meadow_val_local_1f6ce83 = meadow_self_901f2a2.u16(big=True)
        elif meadow_val_local_1f6ce83 & 128:
            meadow_val_local_1f6ce83 = (meadow_val_local_1f6ce83 & 63) << 8 | meadow_self_901f2a2.u8()
        return meadow_val_local_1f6ce83

    @_name_boundary.callable_contract({'self': 'meadow_self_7ce3ea7'}, 'u32_')
    def meadow_u32_(meadow_self_7ce3ea7):
        meadow_val_local_5cd64dc = meadow_self_7ce3ea7.u8()
        if meadow_val_local_5cd64dc == 255:
            meadow_val_local_5cd64dc = meadow_self_7ce3ea7.u32(big=True)
        elif meadow_val_local_5cd64dc & 192 == 192:
            meadow_val_local_5cd64dc = (meadow_val_local_5cd64dc & 31) << 24 | meadow_self_7ce3ea7.u8() << 16 | meadow_self_7ce3ea7.u8() << 8 | meadow_self_7ce3ea7.u8()
        elif meadow_val_local_5cd64dc & 128:
            meadow_val_local_5cd64dc = (meadow_val_local_5cd64dc & 63) << 8 | meadow_self_7ce3ea7.u8()
        return meadow_val_local_5cd64dc

    @_name_boundary.callable_contract({'self': 'meadow_self_dd0abd1'}, 'u64_')
    def meadow_u64_(meadow_self_dd0abd1):
        meadow_val_local_45c781e = _name_boundary.attributes(meadow_self_dd0abd1)['u32_']()
        meadow_val_local_45c781e = meadow_val_local_45c781e | _name_boundary.attributes(meadow_self_dd0abd1)['u32_']() << 32
        return meadow_val_local_45c781e
    bytes = meadow_bytes
    str = meadow_str
    u8_ = meadow_u8_
    u16_ = meadow_u16_
    u32_ = meadow_u32_
    u64_ = meadow_u64_

class meadow_IdaInfo(meadow_vstruct.VStruct):
    """
    did not use vstruct to parse, but for compatibility, just inherit VStruct, and parse in vsParse()
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_600af6a', 'wordsize': 'meadow_wordsize_local_4217de2'}, '__init__')
    def __init__(meadow_self_600af6a, meadow_wordsize_local_4217de2):
        meadow_vstruct.VStruct.__init__(meadow_self_600af6a)
        if meadow_wordsize_local_4217de2 in (4, 8):
            meadow_self_600af6a.wordsize = meadow_wordsize_local_4217de2
        else:
            raise ValueError('unexpected wordsize')
        '\n        v7.0:\n        nodeid: ff000002 tag: S index: 0x41b994\n        00000000: 69 64 61 00 BC 02 6D 65  74 61 70 63 00 00 00 00  ida...metapc....\n        00000010: 00 00 00 00 00 00 A3 00  0B 02 00 00 14 00 00 00  ................\n        00000020: 0B 00 00 00 00 00 00 00  F7 FF FF DF 03 00 00 00  ................\n        00000030: 00 00 00 00 FF FF FF FF  01 00 00 00 95 16 90 68  ...............h\n        00000040: 95 16 90 68 FF FF FF FF  FF FF FF FF 00 10 90 68  ...h...........h\n        00000050: 30 E2 9D 68 00 10 90 68  30 E2 9D 68 00 10 90 68  0..h...h0..h...h\n        00000060: 00 70 9E 68 10 00 00 00  00 00 00 FF 00 00 10 FF  .p.h............\n        00000070: 00 00 00 00 00 02 01 0F  0F 00 40 40 00 00 00 00  ..........@@....\n        00000080: 00 00 00 00 00 00 00 00  00 00 02 06 67 BE A3 0E  ............g...\n        00000090: 07 00 40 06 00 07 00 18  28 00 50 00 54 03 00 00  ..@.....(.P.T...\n        000000A0: 01 00 00 00 01 1B 0A 00  00 00 00 00 61 00 00 00  ............a...\n        000000B0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................\n        000000C0: 07 00 00 00 00 01 33 04  01 04 00 02 04 08 08 00  ......3.........\n        000000D0: 00 00 00 00 00 00 00 00                           ........\n\n        v6.95:\n        00000000: 49 44 41 B7 02 6D 65 74  61 70 63 00 00 23 00 0B  IDA..metapc..#..\n        00000010: 00 00 00 00 00 00 00 00  00 00 00 00 00 FF FF FF  ................\n        00000020: FF FF FF 95 16 90 68 95  16 90 68 00 10 90 68 30  ......h...h...h0\n        00000030: E2 9D 68 00 10 90 68 30  E2 9D 68 00 10 90 68 00  ..h...h0..h...h.\n        00000040: 70 9E 68 10 00 00 00 0A  00 00 18 00 01 00 00 02  p.h.............\n        00000050: 01 01 00 01 02 01 01 00  00 00 00 00 0F 08 00 09  ................\n        00000060: 06 00 01 01 1B 07 61 00  00 00 00 00 00 00 00 00  ......a.........\n        00000070: 00 00 00 00 00 00 00 00  00 00 00 01 00 00 00 01  ................\n        00000080: 01 01 FF FF FF FF 01 00  00 00 FF FF FF FF 67 BE  ..............g.\n        00000090: A3 0E 07 00 40 06 07 00  00 00 00 00 00 00 FD BF  ....@...........\n        000000A0: 0F 00 28 00 50 00 40 40  00 00 00 00 00 00 00 00  ..(.P.@@........\n        000000B0: 00 00 00 00 00 00 02 01  33 04 01 04 00 02 04 08  ........3.......\n        000000C0: 14 00 00 00 08 00 00 00  00 00 00 00 00 00 00 00  ................\n        000000D0: 00 00 00 00 00 00 00 00  00 00 00 00 00 01 00 00  ................\n        000000E0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................\n        000000F0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................\n        '
        meadow_self_600af6a.tag = None
        meadow_self_600af6a.zero = None
        meadow_self_600af6a.version = None
        meadow_self_600af6a.procname_size = None
        meadow_self_600af6a.procname = None
        meadow_self_600af6a.lflags = None
        meadow_self_600af6a.demnames = None
        meadow_self_600af6a.filetype = None
        meadow_self_600af6a.fcoresize = None
        meadow_self_600af6a.corestart = None
        meadow_self_600af6a.ostype = None
        meadow_self_600af6a.apptype = None
        meadow_self_600af6a.start_sp = None
        meadow_self_600af6a.af = None
        meadow_self_600af6a.start_ip = None
        meadow_self_600af6a.begin_ea = None
        meadow_self_600af6a.min_ea = None
        meadow_self_600af6a.max_ea = None
        meadow_self_600af6a.omin_ea = None
        meadow_self_600af6a.omax_ea = None
        meadow_self_600af6a.lowoff = None
        meadow_self_600af6a.highoff = None
        meadow_self_600af6a.maxref = None
        meadow_self_600af6a.ascii_break = None
        meadow_self_600af6a.wide_high_byte_first = None
        meadow_self_600af6a.indent = None
        meadow_self_600af6a.comment = None
        meadow_self_600af6a.xrefnum = None
        meadow_self_600af6a.entab = None
        meadow_self_600af6a.specsegs = None
        meadow_self_600af6a.voids = None
        meadow_self_600af6a.showauto = None
        meadow_self_600af6a.auto = None
        meadow_self_600af6a.border = None
        meadow_self_600af6a.null = None
        meadow_self_600af6a.genflags = None
        meadow_self_600af6a.showpref = None
        meadow_self_600af6a.prefseg = None
        meadow_self_600af6a.asmtype = None
        meadow_self_600af6a.xrefs = None
        meadow_self_600af6a.binpref = None
        meadow_self_600af6a.cmtflag = None
        meadow_self_600af6a.nametype = None
        meadow_self_600af6a.showbads = None
        meadow_self_600af6a.prefflag = None
        meadow_self_600af6a.packbase = None
        meadow_self_600af6a.asciiflags = None
        meadow_self_600af6a.listnames = None
        meadow_self_600af6a.asciipref = None
        meadow_self_600af6a.asciisernum = None
        meadow_self_600af6a.asciizeroes = None
        meadow_self_600af6a.tribyte_order = None
        meadow_self_600af6a.mf = None
        meadow_self_600af6a.org = None
        meadow_self_600af6a.assume = None
        meadow_self_600af6a.checkarg = None
        meadow_self_600af6a.start_ss = None
        meadow_self_600af6a.start_cs = None
        meadow_self_600af6a.main = None
        meadow_self_600af6a.short_dn = None
        meadow_self_600af6a.long_dn = None
        meadow_self_600af6a.datatypes = None
        meadow_self_600af6a.strtype = None
        meadow_self_600af6a.af2 = None
        meadow_self_600af6a.namelen = None
        meadow_self_600af6a.margin = None
        meadow_self_600af6a.lenxref = None
        meadow_self_600af6a.lprefix = None
        meadow_self_600af6a.lprefixlen = None
        meadow_self_600af6a.compiler = None
        meadow_self_600af6a.model = None
        meadow_self_600af6a.sizeof_int = None
        meadow_self_600af6a.sizeof_bool = None
        meadow_self_600af6a.sizeof_enum = None
        meadow_self_600af6a.sizeof_algn = None
        meadow_self_600af6a.sizeof_short = None
        meadow_self_600af6a.sizeof_long = None
        meadow_self_600af6a.sizeof_llong = None
        meadow_self_600af6a.change_counter = None
        meadow_self_600af6a.sizeof_ldbl = None
        meadow_self_600af6a.abiname = None
        meadow_self_600af6a.abibits = None
        meadow_self_600af6a.refcmts = None
        meadow_self_600af6a.database_change_count = None

    @_name_boundary.callable_contract({'self': 'meadow_self_45156e0', 'fast': 'meadow_fast_f6f577b', 'sbytes': 'meadow_sbytes_local_14e355e', 'offset': 'meadow_offset_local_1b2c98b'}, 'vsParse')
    def vsParse(meadow_self_45156e0, meadow_sbytes_local_14e355e, meadow_offset_local_1b2c98b=0, meadow_fast_f6f577b=False):
        meadow_reader_local_1252b8a = meadow_Reader(meadow_sbytes_local_14e355e, wordsize=meadow_self_45156e0.wordsize)
        meadow_reader_local_1252b8a.pos = meadow_offset_local_1b2c98b
        meadow_u8_local_5bda507 = meadow_reader_local_1252b8a.u8
        meadow_u16_local_4258752 = meadow_reader_local_1252b8a.u16
        meadow_u32_local_dae8b89 = meadow_reader_local_1252b8a.u32
        meadow_u64_local_d5d672a = meadow_reader_local_1252b8a.u64
        meadow_word_local_2886c2b = meadow_reader_local_1252b8a.word
        meadow_self_45156e0.tag = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](3)
        if meadow_self_45156e0.tag == 'ida':
            meadow_self_45156e0.zero = meadow_u8_local_5bda507()
        elif meadow_self_45156e0.tag != 'IDA':
            raise NotImplementedError('raise unknown database tag: ' + meadow_self_45156e0.tag)
        meadow_self_45156e0.version = meadow_u16_local_4258752()
        if meadow_self_45156e0.version >= 700 and meadow_self_45156e0.tag == 'IDA':
            meadow_self_45156e0.procname_size = meadow_u8_local_5bda507()
        if meadow_self_45156e0.procname_size is not None:
            meadow_self_45156e0.procname = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](meadow_self_45156e0.procname_size)
        elif meadow_self_45156e0.version < 700:
            meadow_self_45156e0.procname = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](8)
        elif meadow_self_45156e0.version >= 700:
            meadow_self_45156e0.procname = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](16)
        import re as meadow_re_58f3abc
        meadow_self_45156e0.procname = meadow_re_58f3abc.sub('\\x00.*', '', meadow_self_45156e0.procname)
        if meadow_self_45156e0.version < 700:
            meadow_self_45156e0.lflags = meadow_u8_local_5bda507()
            meadow_self_45156e0.demnames = meadow_u8_local_5bda507()
            meadow_self_45156e0.filetype = meadow_u16_local_4258752()
            meadow_self_45156e0.fcoresize = meadow_word_local_2886c2b()
            meadow_self_45156e0.corestart = meadow_word_local_2886c2b()
            meadow_self_45156e0.ostype = meadow_u16_local_4258752()
            meadow_self_45156e0.apptype = meadow_u16_local_4258752()
            meadow_self_45156e0.start_sp = meadow_word_local_2886c2b()
            meadow_self_45156e0.af = meadow_u16_local_4258752()
            meadow_self_45156e0.start_ip = meadow_word_local_2886c2b()
            meadow_self_45156e0.begin_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.min_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.max_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.omin_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.omax_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.lowoff = meadow_word_local_2886c2b()
            meadow_self_45156e0.highoff = meadow_word_local_2886c2b()
            meadow_self_45156e0.maxref = meadow_word_local_2886c2b()
            meadow_self_45156e0.ascii_break = meadow_u8_local_5bda507()
            meadow_self_45156e0.wide_high_byte_first = meadow_u8_local_5bda507()
            meadow_self_45156e0.indent = meadow_u8_local_5bda507()
            meadow_self_45156e0.comment = meadow_u8_local_5bda507()
            meadow_self_45156e0.xrefnum = meadow_u8_local_5bda507()
            meadow_self_45156e0.entab = meadow_u8_local_5bda507()
            meadow_self_45156e0.specsegs = meadow_u8_local_5bda507()
            meadow_self_45156e0.voids = meadow_u8_local_5bda507()
            _name_boundary.attributes(meadow_reader_local_1252b8a)['seek'](1)
            meadow_self_45156e0.showauto = meadow_u8_local_5bda507()
            meadow_self_45156e0.auto = meadow_u8_local_5bda507()
            meadow_self_45156e0.border = meadow_u8_local_5bda507()
            meadow_self_45156e0.null = meadow_u8_local_5bda507()
            meadow_self_45156e0.genflags = meadow_u8_local_5bda507()
            meadow_self_45156e0.showpref = meadow_u8_local_5bda507()
            meadow_self_45156e0.prefseg = meadow_u8_local_5bda507()
            meadow_self_45156e0.asmtype = meadow_u8_local_5bda507()
            meadow_self_45156e0.baseaddr = meadow_word_local_2886c2b()
            meadow_self_45156e0.xrefs = meadow_u8_local_5bda507()
            meadow_self_45156e0.binpref = meadow_u16_local_4258752()
            meadow_self_45156e0.cmtflag = meadow_u8_local_5bda507()
            meadow_self_45156e0.nametype = meadow_u8_local_5bda507()
            meadow_self_45156e0.showbads = meadow_u8_local_5bda507()
            meadow_self_45156e0.prefflag = meadow_u8_local_5bda507()
            meadow_self_45156e0.packbase = meadow_u8_local_5bda507()
            meadow_self_45156e0.asciiflags = meadow_u8_local_5bda507()
            meadow_self_45156e0.listnames = meadow_u8_local_5bda507()
            meadow_self_45156e0.asciipref = _name_boundary.attributes(meadow_reader_local_1252b8a)['bytes'](16)
            meadow_self_45156e0.asciisernum = meadow_word_local_2886c2b()
            meadow_self_45156e0.asciizeroes = meadow_u8_local_5bda507()
            _name_boundary.attributes(meadow_reader_local_1252b8a)['seek'](2)
            meadow_self_45156e0.tribyte_order = meadow_u8_local_5bda507()
            meadow_self_45156e0.mf = meadow_u8_local_5bda507()
            meadow_self_45156e0.org = meadow_u8_local_5bda507()
            meadow_self_45156e0.assume = meadow_u8_local_5bda507()
            meadow_self_45156e0.checkarg = meadow_u8_local_5bda507()
            meadow_self_45156e0.start_ss = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_cs = meadow_word_local_2886c2b()
            meadow_self_45156e0.main = meadow_word_local_2886c2b()
            meadow_self_45156e0.short_dn = meadow_word_local_2886c2b()
            meadow_self_45156e0.long_dn = meadow_word_local_2886c2b()
            meadow_self_45156e0.datatypes = meadow_word_local_2886c2b()
            meadow_self_45156e0.strtype = meadow_word_local_2886c2b()
            meadow_self_45156e0.af2 = meadow_u16_local_4258752()
            meadow_self_45156e0.namelen = meadow_u16_local_4258752()
            meadow_self_45156e0.margin = meadow_u16_local_4258752()
            meadow_self_45156e0.lenxref = meadow_u16_local_4258752()
            meadow_self_45156e0.lprefix = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](16)
            meadow_self_45156e0.lprefixlen = meadow_u8_local_5bda507()
            meadow_self_45156e0.compiler = meadow_u8_local_5bda507()
            meadow_self_45156e0.model = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_int = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_bool = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_enum = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_algn = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_short = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_long = meadow_u8_local_5bda507()
            meadow_self_45156e0.sizeof_llong = meadow_u8_local_5bda507()
            if len(meadow_sbytes_local_14e355e) < 193:
                return meadow_reader_local_1252b8a.pos
            meadow_self_45156e0.change_counter = meadow_u32_local_dae8b89()
            meadow_self_45156e0.sizeof_ldbl = meadow_u8_local_5bda507()
            _name_boundary.attributes(meadow_reader_local_1252b8a)['seek'](4)
            meadow_self_45156e0.abiname = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](size=16)
            meadow_self_45156e0.abibits = meadow_u32_local_dae8b89()
            meadow_self_45156e0.refcmts = meadow_u8_local_5bda507()
        else:
            if meadow_self_45156e0.tag == 'IDA':
                meadow_u8_local_5bda507 = _name_boundary.attributes(meadow_reader_local_1252b8a)['u8_']
                meadow_u16_local_4258752 = _name_boundary.attributes(meadow_reader_local_1252b8a)['u16_']
                meadow_u32_local_dae8b89 = _name_boundary.attributes(meadow_reader_local_1252b8a)['u32_']
                meadow_u64_local_d5d672a = _name_boundary.attributes(meadow_reader_local_1252b8a)['u64_']
                meadow_word_local_2886c2b = meadow_reader_local_1252b8a.word_
            meadow_self_45156e0.genflags = meadow_u16_local_4258752()
            meadow_self_45156e0.lflags = meadow_u32_local_dae8b89()
            meadow_self_45156e0.database_change_count = meadow_u32_local_dae8b89()
            meadow_self_45156e0.filetype = meadow_u16_local_4258752()
            meadow_self_45156e0.ostype = meadow_u16_local_4258752()
            meadow_self_45156e0.apptype = meadow_u16_local_4258752()
            meadow_self_45156e0.asmtype = meadow_u8_local_5bda507()
            meadow_self_45156e0.specsegs = meadow_u8_local_5bda507()
            meadow_self_45156e0.af = meadow_u32_local_dae8b89()
            meadow_self_45156e0.af2 = meadow_u32_local_dae8b89()
            meadow_self_45156e0.baseaddr = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_ss = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_cs = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_ip = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.start_sp = meadow_word_local_2886c2b()
            meadow_self_45156e0.main = meadow_word_local_2886c2b()
            meadow_self_45156e0.min_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.max_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.omin_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.omax_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.lowoff = meadow_word_local_2886c2b()
            meadow_self_45156e0.highoff = meadow_word_local_2886c2b()
            meadow_self_45156e0.maxref = meadow_word_local_2886c2b()
            meadow_self_45156e0.privrange_start_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.privrange_end_ea = meadow_word_local_2886c2b()
            meadow_self_45156e0.netdelta = meadow_word_local_2886c2b()
            meadow_self_45156e0.xrefnum = meadow_u8_local_5bda507()
            meadow_self_45156e0.type_xrefnum = meadow_u8_local_5bda507()
            meadow_self_45156e0.refcmtnum = meadow_u8_local_5bda507()
            meadow_self_45156e0.xrefflag = meadow_u8_local_5bda507()
            meadow_self_45156e0.max_autoname_len = meadow_u16_local_4258752()
            if meadow_self_45156e0.tag == 'ida':
                _name_boundary.attributes(meadow_reader_local_1252b8a)['seek'](17)
            meadow_self_45156e0.nametype = meadow_u8_local_5bda507()
            meadow_self_45156e0.short_demnames = meadow_u32_local_dae8b89()
            meadow_self_45156e0.long_demnames = meadow_u32_local_dae8b89()
            meadow_self_45156e0.demnames = meadow_u8_local_5bda507()
            meadow_self_45156e0.listnames = meadow_u8_local_5bda507()
            meadow_self_45156e0.indent = meadow_u8_local_5bda507()
            meadow_self_45156e0.comment = meadow_u8_local_5bda507()
            meadow_self_45156e0.marzgin = meadow_u16_local_4258752()
            meadow_self_45156e0.lenxref = meadow_u16_local_4258752()
            meadow_self_45156e0.outflags = meadow_u32_local_dae8b89()
            meadow_self_45156e0.cmtflg = meadow_u8_local_5bda507()
            meadow_self_45156e0.limiter = meadow_u8_local_5bda507()
            meadow_self_45156e0.bin_prefix_size = meadow_u16_local_4258752()
            meadow_self_45156e0.prefflag = meadow_u8_local_5bda507()
            meadow_self_45156e0.strlit_flags = meadow_u8_local_5bda507()
            meadow_self_45156e0.strlit_break = meadow_u8_local_5bda507()
            meadow_self_45156e0.strlit_zeroes = meadow_u8_local_5bda507()
            meadow_self_45156e0.strtype = meadow_u32_local_dae8b89()
            meadow_self_45156e0.strlit_pref_size = meadow_u8_local_5bda507()
            if meadow_self_45156e0.tag == 'ida':
                meadow_self_45156e0.strlit_pref = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](16)
            else:
                meadow_self_45156e0.strlit_pref = _name_boundary.attributes(meadow_reader_local_1252b8a)['str'](meadow_self_45156e0.strlit_pref_size)
            meadow_self_45156e0.strlit_sernum = meadow_word_local_2886c2b()
            meadow_self_45156e0.datatypes = meadow_word_local_2886c2b()
            meadow_self_45156e0.cc_id = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_cm = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_i = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_b = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_e = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_defalign = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_s = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_l = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_ll = meadow_u8_local_5bda507()
            meadow_self_45156e0.cc_size_ldbl = meadow_u8_local_5bda507()
            meadow_self_45156e0.abibits = meadow_u32_local_dae8b89()
            meadow_self_45156e0.appcall_options = meadow_u32_local_dae8b89()
        return meadow_reader_local_1252b8a.pos
meadow_Root = meadow_Analysis('Root Node', [meadow_Field('imagebase', 'A', -6, _name_boundary.attributes(meadow_idb)['netnode'].as_int), meadow_Field('crc', 'A', -5, _name_boundary.attributes(meadow_idb)['netnode'].as_int), meadow_Field('open_count', 'A', -4, _name_boundary.attributes(meadow_idb)['netnode'].as_int), meadow_Field('created', 'A', -2, meadow_as_unix_timestamp), meadow_Field('version', 'A', -1, _name_boundary.attributes(meadow_idb)['netnode'].as_int), meadow_Field('md5', 'S', 1302, meadow_as_md5), meadow_Field('version_string', 'S', 1303, _name_boundary.attributes(meadow_idb)['netnode'].as_string), meadow_Field('sha256', 'S', 1349, meadow_as_sha256), meadow_Field('idainfo', 'S', 4307348, meadow_as_cast(meadow_IdaInfo)), meadow_Field('input_file_path', 'V', None, _name_boundary.attributes(meadow_idb)['netnode'].as_string)])
meadow_Loader = meadow_Analysis('$ loader name', [meadow_Field('plugin', 'S', 0, _name_boundary.attributes(meadow_idb)['netnode'].as_string), meadow_Field('format', 'S', 1, _name_boundary.attributes(meadow_idb)['netnode'].as_string)])
meadow_OriginalUser = meadow_Analysis('$ original user', [meadow_Field('data', 'S', 0, bytes)])
meadow_User = meadow_Analysis('$ user1', [meadow_Field('data', 'S', 0, bytes)])

class meadow_FileRegion(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_8a69f18', 'wordsize': 'meadow_wordsize_local_9a855a6'}, '__init__')
    def __init__(meadow_self_8a69f18, meadow_wordsize_local_9a855a6):
        meadow_vstruct.VStruct.__init__(meadow_self_8a69f18)
        if meadow_wordsize_local_9a855a6 == 4:
            meadow_v_word_local_cd29984 = v_uint32
        elif meadow_wordsize_local_9a855a6 == 8:
            meadow_v_word_local_cd29984 = v_uint64
        else:
            raise ValueError('unexpected wordsize')
        meadow_self_8a69f18.start = meadow_v_word_local_cd29984()
        meadow_self_8a69f18.end = meadow_v_word_local_cd29984()
        meadow_self_8a69f18.rva = v_uint32()

@_name_boundary.class_contract('FileRegionV70', {})
class meadow_FileRegionV70:

    @_name_boundary.callable_contract({'self': 'meadow_self_79060e7', 'buf': 'meadow_buf_local_fbd3306', 'wordsize': 'meadow_wordsize_local_8cf8608'}, '__init__')
    def __init__(meadow_self_79060e7, meadow_buf_local_fbd3306, meadow_wordsize_local_8cf8608):
        meadow_self_79060e7.buf = meadow_buf_local_fbd3306
        meadow_u_7e1fe7a = meadow_Unpacker(meadow_buf_local_fbd3306, wordsize=meadow_wordsize_local_8cf8608)
        meadow_self_79060e7.start = _name_boundary.attributes(meadow_u_7e1fe7a)['addr']()
        meadow_self_79060e7.end = meadow_self_79060e7.start + _name_boundary.attributes(meadow_u_7e1fe7a)['addr']()
        meadow_self_79060e7.rva = _name_boundary.attributes(meadow_u_7e1fe7a)['addr']()
meadow_FileRegions = meadow_Analysis('$ fileregions', [meadow_Field('regions', 'S', meadow_ADDRESSES, meadow_as_cast(meadow_FileRegion)), meadow_Field('regions', 'S', meadow_ADDRESSES, meadow_FileRegionV70, minver=700)])

@_name_boundary.class_contract('func_t', {'FUNC_TAIL': 'meadow_FUNC_TAIL', 'startEA': 'meadow_startEA', 'endEA': 'meadow_endEA', 'frame': 'meadow_frame', 'frsize': 'meadow_frsize', 'frregs': 'meadow_frregs', 'argsize': 'meadow_argsize', 'owner': 'meadow_owner', 'refqty': 'meadow_refqty'})
class meadow_func_t:
    meadow_FUNC_TAIL = 32768

    @_name_boundary.callable_contract({'self': 'meadow_self_eb9ca61', 'buf': 'meadow_buf_local_cb17baf', 'wordsize': 'meadow_wordsize_local_232bfbb'}, '__init__')
    def __init__(meadow_self_eb9ca61, meadow_buf_local_cb17baf, meadow_wordsize_local_232bfbb):
        meadow_self_eb9ca61.buf = meadow_buf_local_cb17baf
        meadow_u_3647050 = meadow_Unpacker(meadow_buf_local_cb17baf, wordsize=meadow_wordsize_local_232bfbb)
        _name_boundary.attributes(meadow_self_eb9ca61)['startEA'] = _name_boundary.attributes(meadow_u_3647050)['addr']()
        _name_boundary.attributes(meadow_self_eb9ca61)['endEA'] = _name_boundary.attributes(meadow_self_eb9ca61)['startEA'] + _name_boundary.attributes(meadow_u_3647050)['addr']()
        meadow_self_eb9ca61.flags = _name_boundary.attributes(meadow_u_3647050)['dw']()
        _name_boundary.attributes(meadow_self_eb9ca61)['frame'] = None
        _name_boundary.attributes(meadow_self_eb9ca61)['frsize'] = None
        _name_boundary.attributes(meadow_self_eb9ca61)['frregs'] = None
        _name_boundary.attributes(meadow_self_eb9ca61)['argsize'] = None
        _name_boundary.attributes(meadow_self_eb9ca61)['owner'] = None
        _name_boundary.attributes(meadow_self_eb9ca61)['refqty'] = None
        if not meadow_is_flag_set(meadow_self_eb9ca61.flags, _name_boundary.attributes(meadow_func_t)['FUNC_TAIL']):
            try:
                _name_boundary.attributes(meadow_self_eb9ca61)['frame'] = _name_boundary.attributes(meadow_u_3647050)['addr']()
                _name_boundary.attributes(meadow_self_eb9ca61)['frsize'] = _name_boundary.attributes(meadow_u_3647050)['addr']()
                _name_boundary.attributes(meadow_self_eb9ca61)['frregs'] = _name_boundary.attributes(meadow_u_3647050)['dw']()
                _name_boundary.attributes(meadow_self_eb9ca61)['argsize'] = _name_boundary.attributes(meadow_u_3647050)['addr']()
            except IndexError:
                pass
        else:
            try:
                _name_boundary.attributes(meadow_self_eb9ca61)['owner'] = _name_boundary.attributes(meadow_self_eb9ca61)['startEA'] - _name_boundary.attributes(meadow_u_3647050)['off']()
                _name_boundary.attributes(meadow_self_eb9ca61)['refqty'] = _name_boundary.attributes(meadow_u_3647050)['dd']()
            except IndexError:
                pass
meadow_Functions = meadow_Analysis('$ funcs', [meadow_Field('functions', 'S', meadow_ADDRESSES, meadow_func_t), meadow_Field('comments', 'C', meadow_ADDRESSES, _name_boundary.attributes(meadow_idb)['netnode'].as_string), meadow_Field('repeatable_comments', 'R', meadow_ADDRESSES, _name_boundary.attributes(meadow_idb)['netnode'].as_string)])

class meadow_PString(meadow_vstruct.VStruct):
    """
    short pascal string, prefixed with single byte length.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_d7c6661', 'length_is_total': 'meadow_length_is_total_local_9855704'}, '__init__')
    def __init__(meadow_self_d7c6661, meadow_length_is_total_local_9855704=True):
        meadow_vstruct.VStruct.__init__(meadow_self_d7c6661)
        meadow_self_d7c6661.length = v_uint8()
        meadow_self_d7c6661.s = v_str()
        meadow_self_d7c6661.length_is_total = meadow_length_is_total_local_9855704

    @_name_boundary.callable_contract({'self': 'meadow_self_3c65e94'}, 'pcb_length')
    def pcb_length(meadow_self_3c65e94):
        meadow_length_local_7d8c452 = meadow_self_3c65e94.length
        if meadow_self_3c65e94.length_is_total:
            meadow_length_local_7d8c452 = meadow_length_local_7d8c452 - 1
        meadow_self_3c65e94['s'].vsSetLength(meadow_length_local_7d8c452)

class meadow_TypeString(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_1945ff9'}, '__init__')
    def __init__(meadow_self_1945ff9):
        meadow_vstruct.VStruct.__init__(meadow_self_1945ff9)
        meadow_self_1945ff9.header = v_uint8()
        meadow_self_1945ff9.length = v_uint8()
        meadow_self_1945ff9.s = v_str()

    @_name_boundary.callable_contract({'self': 'meadow_self_8fed3e3'}, 'pcb_header')
    def pcb_header(meadow_self_8fed3e3):
        if meadow_self_8fed3e3.header != 61:
            raise RuntimeError('unexpected type header')

    @_name_boundary.callable_contract({'self': 'meadow_self_8772b74'}, 'pcb_length')
    def pcb_length(meadow_self_8772b74):
        meadow_length_local_5223976 = meadow_self_8772b74.length
        meadow_self_8772b74['s'].vsSetLength(meadow_length_local_5223976 - 1)

@_name_boundary.class_contract('StructMember', {'get_fullname': 'meadow_get_fullname', 'get_name': 'meadow_get_name', 'get_typeinfo': 'meadow_get_typeinfo', 'get_type': 'meadow_get_type', 'get_enum_id': 'meadow_get_enum_id', 'get_struct_id': 'meadow_get_struct_id', 'get_member_comment': 'meadow_get_member_comment', 'get_repeatable_member_comment': 'meadow_get_repeatable_member_comment', 'idb': 'meadow_idb', 'netnode': 'meadow_netnode', 'nodeid': 'meadow_nodeid'})
class meadow_StructMember:

    @_name_boundary.callable_contract({'self': 'meadow_self_bdbdf39', 'db': 'meadow_db_4fba50a', 'identity': 'meadow_identity_67215f3'}, '__init__')
    def __init__(meadow_self_bdbdf39, meadow_db_4fba50a, meadow_identity_67215f3):
        _name_boundary.attributes(meadow_self_bdbdf39)['idb'] = meadow_db_4fba50a
        if isinstance(meadow_identity_67215f3, meadow_six.integer_types):
            meadow_nodebase_4bfd868 = _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'])['get_nodebase'](meadow_db_4fba50a)
            if meadow_identity_67215f3 < meadow_nodebase_4bfd868:
                meadow_identity_67215f3 += meadow_nodebase_4bfd868
            _name_boundary.attributes(meadow_self_bdbdf39)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_4fba50a, meadow_identity_67215f3)
            _name_boundary.attributes(meadow_self_bdbdf39)['nodeid'] = meadow_identity_67215f3
        elif isinstance(meadow_identity_67215f3, meadow_six.string_types):
            _name_boundary.attributes(meadow_self_bdbdf39)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_4fba50a, meadow_identity_67215f3)
            _name_boundary.attributes(meadow_self_bdbdf39)['nodeid'] = _name_boundary.attributes(_name_boundary.attributes(meadow_self_bdbdf39)['netnode'])['nodeid']
        else:
            raise ValueError('Expected identify is integer or string')

    @_name_boundary.callable_contract({'self': 'meadow_self_bc5193d'}, 'get_fullname')
    def meadow_get_fullname(meadow_self_bc5193d):
        return _name_boundary.attributes(meadow_self_bc5193d)['netnode'].name()

    @_name_boundary.callable_contract({'self': 'meadow_self_9e63f46'}, 'get_name')
    def meadow_get_name(meadow_self_9e63f46):
        return _name_boundary.attributes(meadow_self_9e63f46)['netnode'].name().partition('.')[2]

    @_name_boundary.callable_contract({'self': 'meadow_self_e405f90'}, 'get_typeinfo')
    def meadow_get_typeinfo(meadow_self_e405f90):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_e405f90)['netnode'])['supval'](tag='S', index=12288)

    @_name_boundary.callable_contract({'self': 'meadow_self_7392976'}, 'get_type')
    def meadow_get_type(meadow_self_7392976):
        try:
            meadow_v_99fd694 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_7392976)['netnode'])['supval'](tag='S', index=12288)
            meadow_s_local_697ab38 = meadow_TypeString()
            meadow_s_local_697ab38.vsParse(meadow_v_99fd694)
            return meadow_s_local_697ab38.s
        except KeyError:
            return None

    @_name_boundary.callable_contract({'self': 'meadow_self_f85f92d'}, 'get_enum_id')
    def meadow_get_enum_id(meadow_self_f85f92d):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f85f92d)['netnode'])['altval'](tag='A', index=11)

    @_name_boundary.callable_contract({'self': 'meadow_self_b3cf7ba'}, 'get_struct_id')
    def meadow_get_struct_id(meadow_self_b3cf7ba):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_b3cf7ba)['netnode'])['altval'](tag='A', index=3)

    @_name_boundary.callable_contract({'self': 'meadow_self_a6ea3d2'}, 'get_member_comment')
    def meadow_get_member_comment(meadow_self_a6ea3d2):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_a6ea3d2)['netnode'])['supstr'](tag='S', index=0)

    @_name_boundary.callable_contract({'self': 'meadow_self_8bc8b2a'}, 'get_repeatable_member_comment')
    def meadow_get_repeatable_member_comment(meadow_self_8bc8b2a):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_8bc8b2a)['netnode'])['supstr'](tag='S', index=1)

    @_name_boundary.callable_contract({'self': 'meadow_self_6546154'}, '__str__')
    def __str__(meadow_self_6546154):
        try:
            meadow_typ_local_31b906d = _name_boundary.attributes(meadow_self_6546154)['get_type']()
        except KeyError:
            return 'StructMember(name: %s)' % _name_boundary.attributes(meadow_self_6546154)['get_name']()
        else:
            return 'StructMember(name: %s, type: %s)' % (_name_boundary.attributes(meadow_self_6546154)['get_name'](), meadow_typ_local_31b906d)

@_name_boundary.class_contract('STRUCT_FLAGS', {'SF_VAR': 'meadow_SF_VAR', 'SF_UNION': 'meadow_SF_UNION', 'SF_HASUNI': 'meadow_SF_HASUNI', 'SF_NOLIST': 'meadow_SF_NOLIST', 'SF_TYPLIB': 'meadow_SF_TYPLIB', 'SF_HIDDEN': 'meadow_SF_HIDDEN', 'SF_FRAME': 'meadow_SF_FRAME', 'SF_ALIGN': 'meadow_SF_ALIGN', 'SF_GHOST': 'meadow_SF_GHOST'})
class meadow_STRUCT_FLAGS:
    meadow_SF_VAR = 1
    meadow_SF_UNION = 2
    meadow_SF_HASUNI = 4
    meadow_SF_NOLIST = 8
    meadow_SF_TYPLIB = 16
    meadow_SF_HIDDEN = 32
    meadow_SF_FRAME = 64
    meadow_SF_ALIGN = 3968
    meadow_SF_GHOST = 4096

@_name_boundary.class_contract('Struct', {'get_name': 'meadow_get_name', 'get_members': 'meadow_get_members', 'find_member_by_name': 'meadow_find_member_by_name', 'Unpacker': 'meadow_Unpacker', '_do_unpack': 'meadow__do_unpack', 'dd': 'meadow_dd', 'dq': 'meadow_dq', 'dw': 'meadow_dw', 'addr': 'meadow_addr', 'off': 'meadow_off', 'IndexType': 'meadow_IndexType', 'str': 'meadow_str', '_Analysis': 'meadow__Analysis', '_is_address': 'meadow__is_address', '_is_node': 'meadow__is_node', '_is_number': 'meadow__is_number', 'get_field_tag': 'meadow_get_field_tag', 'get_field_index': 'meadow_get_field_index', 'Reader': 'meadow_Reader', 'bytes': 'meadow_bytes', 'u8_': 'meadow_u8_', 'u16_': 'meadow_u16_', 'u32_': 'meadow_u32_', 'u64_': 'meadow_u64_', 'IdaInfo': 'meadow_IdaInfo', 'FileRegion': 'meadow_FileRegion', 'FileRegionV70': 'meadow_FileRegionV70', 'func_t': 'meadow_func_t', 'FUNC_TAIL': 'meadow_FUNC_TAIL', 'PString': 'meadow_PString', 'TypeString': 'meadow_TypeString', 'StructMember': 'meadow_StructMember', 'get_fullname': 'meadow_get_fullname', 'get_typeinfo': 'meadow_get_typeinfo', 'get_type': 'meadow_get_type', 'get_enum_id': 'meadow_get_enum_id', 'get_struct_id': 'meadow_get_struct_id', 'get_member_comment': 'meadow_get_member_comment', 'get_repeatable_member_comment': 'meadow_get_repeatable_member_comment', 'STRUCT_FLAGS': 'meadow_STRUCT_FLAGS', 'SF_VAR': 'meadow_SF_VAR', 'SF_UNION': 'meadow_SF_UNION', 'SF_HASUNI': 'meadow_SF_HASUNI', 'SF_NOLIST': 'meadow_SF_NOLIST', 'SF_TYPLIB': 'meadow_SF_TYPLIB', 'SF_HIDDEN': 'meadow_SF_HIDDEN', 'SF_FRAME': 'meadow_SF_FRAME', 'SF_ALIGN': 'meadow_SF_ALIGN', 'SF_GHOST': 'meadow_SF_GHOST', 'Struct': 'meadow_Struct', 'Function': 'meadow_Function', 'get_signature': 'meadow_get_signature', 'get_chunks': 'meadow_get_chunks', 'get_stack_change_points': 'meadow_get_stack_change_points', 'Fixup': 'meadow_Fixup', 'get_fixup_length': 'meadow_get_fixup_length', 'FixupV70': 'meadow_FixupV70', 'Seg': 'meadow_Seg', 'should_log': 'meadow_should_log', 'idb': 'meadow_idb', 'nodeid': 'meadow_nodeid', 'netnode': 'meadow_netnode', '_fields_by_name': 'meadow__fields_by_name', 'startEA': 'meadow_startEA', 'endEA': 'meadow_endEA', 'frame': 'meadow_frame', 'frsize': 'meadow_frsize', 'frregs': 'meadow_frregs', 'argsize': 'meadow_argsize', 'owner': 'meadow_owner', 'refqty': 'meadow_refqty', 'unk1': 'meadow_unk1', 'unk2': 'meadow_unk2', 'name_index': 'meadow_name_index', 'orgbase': 'meadow_orgbase', 'align': 'meadow_align', 'comb': 'meadow_comb', 'perm': 'meadow_perm', 'bitness': 'meadow_bitness', 'sel': 'meadow_sel', 'defsr': 'meadow_defsr', 'color': 'meadow_color', 'FileHeader': 'meadow_FileHeader', 'validate': 'meadow_validate', 'COMPRESSION_METHOD': 'meadow_COMPRESSION_METHOD', 'NONE': 'meadow_NONE', 'ZLIB': 'meadow_ZLIB', 'SectionHeader': 'meadow_SectionHeader', 'Section': 'meadow_Section', 'BranchEntryPointer': 'meadow_BranchEntryPointer', 'BranchEntry': 'meadow_BranchEntry', 'LeafEntryPointer': 'meadow_LeafEntryPointer', 'LeafEntry': 'meadow_LeafEntry', 'Page': 'meadow_Page', 'is_leaf': 'meadow_is_leaf', '_load_entries': 'meadow__load_entries', 'get_entries': 'meadow_get_entries', 'find_index': 'meadow_find_index', 'get_entry': 'meadow_get_entry', 'FindStrategy': 'meadow_FindStrategy', 'find': 'meadow_find', 'ExactMatchStrategy': 'meadow_ExactMatchStrategy', '_find': 'meadow__find', 'PrefixMatchStrategy': 'meadow_PrefixMatchStrategy', 'RoundDownMatchStrategy': 'meadow_RoundDownMatchStrategy', 'MinKeyStrategy': 'meadow_MinKeyStrategy', 'MaxKeyStrategy': 'meadow_MaxKeyStrategy', 'Cursor': 'meadow_Cursor', 'next': 'meadow_next', 'prev': 'meadow_prev', 'ID0': 'meadow_ID0', 'get_page_buffer': 'meadow_get_page_buffer', 'get_page': 'meadow_get_page', 'find_prefix': 'meadow_find_prefix', 'get_min': 'meadow_get_min', 'get_max': 'meadow_get_max', 'SegmentBounds': 'meadow_SegmentBounds', 'ID1': 'meadow_ID1', 'get_segment': 'meadow_get_segment', 'get_next_segment': 'meadow_get_next_segment', 'get_flags': 'meadow_get_flags', 'NAM': 'meadow_NAM', 'names': 'meadow_names', 'IDB': 'meadow_IDB', 'index': 'meadow_index', 'path': 'meadow_path', 'entry_number': 'meadow_entry_number', 'FLAGS': 'meadow_FLAGS', 'OPND_OUTER': 'meadow_OPND_OUTER', 'OPND_MASK': 'meadow_OPND_MASK', 'OPND_ALL': 'meadow_OPND_ALL', 'MS_CLS': 'meadow_MS_CLS', 'FF_CODE': 'meadow_FF_CODE', 'FF_DATA': 'meadow_FF_DATA', 'FF_TAIL': 'meadow_FF_TAIL', 'FF_UNK': 'meadow_FF_UNK', 'MS_COMM': 'meadow_MS_COMM', 'FF_COMM': 'meadow_FF_COMM', 'FF_REF': 'meadow_FF_REF', 'FF_LINE': 'meadow_FF_LINE', 'FF_NAME': 'meadow_FF_NAME', 'FF_LABL': 'meadow_FF_LABL', 'FF_FLOW': 'meadow_FF_FLOW', 'FF_SIGN': 'meadow_FF_SIGN', 'FF_BNOT': 'meadow_FF_BNOT', 'FF_VAR': 'meadow_FF_VAR', 'MS_0TYPE': 'meadow_MS_0TYPE', 'FF_0VOID': 'meadow_FF_0VOID', 'FF_0NUMH': 'meadow_FF_0NUMH', 'FF_0NUMD': 'meadow_FF_0NUMD', 'FF_0CHAR': 'meadow_FF_0CHAR', 'FF_0SEG': 'meadow_FF_0SEG', 'FF_0OFF': 'meadow_FF_0OFF', 'FF_0NUMB': 'meadow_FF_0NUMB', 'FF_0NUMO': 'meadow_FF_0NUMO', 'FF_0ENUM': 'meadow_FF_0ENUM', 'FF_0FOP': 'meadow_FF_0FOP', 'FF_0STRO': 'meadow_FF_0STRO', 'FF_0STK': 'meadow_FF_0STK', 'FF_0FLT': 'meadow_FF_0FLT', 'FF_0CUST': 'meadow_FF_0CUST', 'MS_1TYPE': 'meadow_MS_1TYPE', 'FF_1VOID': 'meadow_FF_1VOID', 'FF_1NUMH': 'meadow_FF_1NUMH', 'FF_1NUMD': 'meadow_FF_1NUMD', 'FF_1CHAR': 'meadow_FF_1CHAR', 'FF_1SEG': 'meadow_FF_1SEG', 'FF_1OFF': 'meadow_FF_1OFF', 'FF_1NUMB': 'meadow_FF_1NUMB', 'FF_1NUMO': 'meadow_FF_1NUMO', 'FF_1ENUM': 'meadow_FF_1ENUM', 'FF_1FOP': 'meadow_FF_1FOP', 'FF_1STRO': 'meadow_FF_1STRO', 'FF_1STK': 'meadow_FF_1STK', 'FF_1FLT': 'meadow_FF_1FLT', 'FF_1CUST': 'meadow_FF_1CUST', 'MS_CODE': 'meadow_MS_CODE', 'FF_FUNC': 'meadow_FF_FUNC', 'FF_IMMD': 'meadow_FF_IMMD', 'FF_JUMP': 'meadow_FF_JUMP', 'DT_TYPE': 'meadow_DT_TYPE', 'FF_BYTE': 'meadow_FF_BYTE', 'FF_WORD': 'meadow_FF_WORD', 'FF_DWRD': 'meadow_FF_DWRD', 'FF_QWRD': 'meadow_FF_QWRD', 'FF_TBYT': 'meadow_FF_TBYT', 'FF_ASCI': 'meadow_FF_ASCI', 'FF_STRU': 'meadow_FF_STRU', 'FF_OWRD': 'meadow_FF_OWRD', 'FF_FLOAT': 'meadow_FF_FLOAT', 'FF_DOUBLE': 'meadow_FF_DOUBLE', 'FF_PACKREAL': 'meadow_FF_PACKREAL', 'FF_ALIGN': 'meadow_FF_ALIGN', 'FF_3BYTE': 'meadow_FF_3BYTE', 'FF_CUSTOM': 'meadow_FF_CUSTOM', 'FF_YWRD': 'meadow_FF_YWRD', 'MS_VAL': 'meadow_MS_VAL', 'FF_IVL': 'meadow_FF_IVL', 'AFLAGS': 'meadow_AFLAGS', 'AFL_LINNUM': 'meadow_AFL_LINNUM', 'AFL_USERSP': 'meadow_AFL_USERSP', 'AFL_PUBNAM': 'meadow_AFL_PUBNAM', 'AFL_WEAKNAM': 'meadow_AFL_WEAKNAM', 'AFL_HIDDEN': 'meadow_AFL_HIDDEN', 'AFL_MANUAL': 'meadow_AFL_MANUAL', 'AFL_NOBRD': 'meadow_AFL_NOBRD', 'AFL_ZSTROFF': 'meadow_AFL_ZSTROFF', 'AFL_BNOT0': 'meadow_AFL_BNOT0', 'AFL_BNOT1': 'meadow_AFL_BNOT1', 'AFL_LIB': 'meadow_AFL_LIB', 'AFL_TI': 'meadow_AFL_TI', 'AFL_TI0': 'meadow_AFL_TI0', 'AFL_TI1': 'meadow_AFL_TI1', 'AFL_LNAME': 'meadow_AFL_LNAME', 'AFL_TILCMT': 'meadow_AFL_TILCMT', 'AFL_LZERO0': 'meadow_AFL_LZERO0', 'AFL_LZERO1': 'meadow_AFL_LZERO1', 'AFL_COLORED': 'meadow_AFL_COLORED', 'AFL_TERSESTR': 'meadow_AFL_TERSESTR', 'AFL_SIGN0': 'meadow_AFL_SIGN0', 'AFL_SIGN1': 'meadow_AFL_SIGN1', 'AFL_NORET': 'meadow_AFL_NORET', 'AFL_FIXEDSPD': 'meadow_AFL_FIXEDSPD', 'AFL_ALIGNFLOW': 'meadow_AFL_ALIGNFLOW', 'AFL_USERTI': 'meadow_AFL_USERTI', 'AFL_RETFP': 'meadow_AFL_RETFP', 'AFL_USEMODSP': 'meadow_AFL_USEMODSP', 'AFL_NOTCODE': 'meadow_AFL_NOTCODE', 'ida_netnode': 'meadow_ida_netnode', 'ida_ida': 'meadow_ida_ida', 'ida_ua': 'meadow_ida_ua', 'o_void': 'meadow_o_void', 'o_reg': 'meadow_o_reg', 'o_mem': 'meadow_o_mem', 'o_phrase': 'meadow_o_phrase', 'o_displ': 'meadow_o_displ', 'o_imm': 'meadow_o_imm', 'o_far': 'meadow_o_far', 'o_near': 'meadow_o_near', 'o_idpspec0': 'meadow_o_idpspec0', 'o_idpspec1': 'meadow_o_idpspec1', 'o_idpspec2': 'meadow_o_idpspec2', 'o_idpspec3': 'meadow_o_idpspec3', 'o_idpspec4': 'meadow_o_idpspec4', 'o_idpspec5': 'meadow_o_idpspec5', 'idc': 'meadow_idc', 'SEGPERM_EXEC': 'meadow_SEGPERM_EXEC', 'SEGPERM_WRITE': 'meadow_SEGPERM_WRITE', 'SEGPERM_READ': 'meadow_SEGPERM_READ', 'SEGPERM_MAXVAL': 'meadow_SEGPERM_MAXVAL', 'SFL_COMORG': 'meadow_SFL_COMORG', 'SFL_OBOK': 'meadow_SFL_OBOK', 'SFL_HIDDEN': 'meadow_SFL_HIDDEN', 'SFL_DEBUG': 'meadow_SFL_DEBUG', 'SFL_LOADER': 'meadow_SFL_LOADER', 'SFL_HIDETYPE': 'meadow_SFL_HIDETYPE', 'ScreenEA': 'meadow_ScreenEA', '_get_segment': 'meadow__get_segment', 'SegStart': 'meadow_SegStart', 'SegEnd': 'meadow_SegEnd', 'FirstSeg': 'meadow_FirstSeg', 'NextSeg': 'meadow_NextSeg', 'SegName': 'meadow_SegName', 'GetSegmentAttr': 'meadow_GetSegmentAttr', 'MinEA': 'meadow_MinEA', 'MaxEA': 'meadow_MaxEA', 'GetFlags': 'meadow_GetFlags', 'IdbByte': 'meadow_IdbByte', 'Head': 'meadow_Head', 'ItemSize': 'meadow_ItemSize', 'NextHead': 'meadow_NextHead', 'PrevHead': 'meadow_PrevHead', 'GetManyBytes': 'meadow_GetManyBytes', '_load_dis': 'meadow__load_dis', '_disassemble': 'meadow__disassemble', 'print_insn_mnem': 'meadow_print_insn_mnem', 'GetDisasm': 'meadow_GetDisasm', 'print_operand': 'meadow_print_operand', 'get_operand_type': 'meadow_get_operand_type', 'CIC_ITEM': 'meadow_CIC_ITEM', 'CIC_FUNC': 'meadow_CIC_FUNC', 'CIC_SEGM': 'meadow_CIC_SEGM', 'DEFCOLOR': 'meadow_DEFCOLOR', 'GetColor': 'meadow_GetColor', 'GetFunctionFlags': 'meadow_GetFunctionFlags', 'GetFunctionAttr': 'meadow_GetFunctionAttr', 'GetFunctionName': 'meadow_GetFunctionName', 'find_func_end': 'meadow_find_func_end', 'LocByName': 'meadow_LocByName', 'GetInputMD5': 'meadow_GetInputMD5', 'GetInputSHA256': 'meadow_GetInputSHA256', 'GetInputFile': 'meadow_GetInputFile', 'Comment': 'meadow_Comment', 'RptCmt': 'meadow_RptCmt', 'GetCommentEx': 'meadow_GetCommentEx', 'GetType': 'meadow_GetType', 'hasValue': 'meadow_hasValue', 'isDefArg0': 'meadow_isDefArg0', 'isDefArg1': 'meadow_isDefArg1', 'isOff0': 'meadow_isOff0', 'isOff1': 'meadow_isOff1', 'isChar0': 'meadow_isChar0', 'isChar1': 'meadow_isChar1', 'isSeg0': 'meadow_isSeg0', 'isSeg1': 'meadow_isSeg1', 'isEnum0': 'meadow_isEnum0', 'isEnum1': 'meadow_isEnum1', 'isStroff0': 'meadow_isStroff0', 'isStroff1': 'meadow_isStroff1', 'isStkvar0': 'meadow_isStkvar0', 'isStkvar1': 'meadow_isStkvar1', 'isFloat0': 'meadow_isFloat0', 'isFloat1': 'meadow_isFloat1', 'isCustFmt0': 'meadow_isCustFmt0', 'isCustFmt1': 'meadow_isCustFmt1', 'isNum0': 'meadow_isNum0', 'isNum1': 'meadow_isNum1', 'get_optype_flags0': 'meadow_get_optype_flags0', 'get_optype_flags1': 'meadow_get_optype_flags1', 'LineA': 'meadow_LineA', 'LineB': 'meadow_LineB', 'ida_bytes': 'meadow_ida_bytes', 'get_cmt': 'meadow_get_cmt', 'is_func': 'meadow_is_func', 'has_immd': 'meadow_has_immd', 'is_code': 'meadow_is_code', 'is_data': 'meadow_is_data', 'is_tail': 'meadow_is_tail', 'is_not_tail': 'meadow_is_not_tail', 'is_unknown': 'meadow_is_unknown', 'is_head': 'meadow_is_head', 'is_flow': 'meadow_is_flow', 'is_var': 'meadow_is_var', 'has_extra_cmts': 'meadow_has_extra_cmts', 'has_cmt': 'meadow_has_cmt', 'has_ref': 'meadow_has_ref', 'has_name': 'meadow_has_name', 'has_dummy_name': 'meadow_has_dummy_name', 'has_auto_name': 'meadow_has_auto_name', 'has_any_name': 'meadow_has_any_name', 'has_user_name': 'meadow_has_user_name', 'is_invsign': 'meadow_is_invsign', 'is_bnot': 'meadow_is_bnot', 'has_value': 'meadow_has_value', 'is_byte': 'meadow_is_byte', 'is_word': 'meadow_is_word', 'is_dword': 'meadow_is_dword', 'is_qword': 'meadow_is_qword', 'is_oword': 'meadow_is_oword', 'is_yword': 'meadow_is_yword', 'is_tbyte': 'meadow_is_tbyte', 'is_float': 'meadow_is_float', 'is_double': 'meadow_is_double', 'is_pack_real': 'meadow_is_pack_real', 'is_strlit': 'meadow_is_strlit', 'is_struct': 'meadow_is_struct', 'is_align': 'meadow_is_align', 'is_custom': 'meadow_is_custom', 'get_bytes': 'meadow_get_bytes', 'next_that': 'meadow_next_that', 'next_not_tail': 'meadow_next_not_tail', 'next_inited': 'meadow_next_inited', 'get_item_end': 'meadow_get_item_end', 'get_byte': 'meadow_get_byte', 'get_word': 'meadow_get_word', 'get_dword': 'meadow_get_dword', 'get_qword': 'meadow_get_qword', 'ida_nalt': 'meadow_ida_nalt', 'get_aflags': 'meadow_get_aflags', 'is_hidden_item': 'meadow_is_hidden_item', 'is_hidden_border': 'meadow_is_hidden_border', 'uses_modsp': 'meadow_uses_modsp', 'is_zstroff': 'meadow_is_zstroff', 'is__bnot0': 'meadow_is__bnot0', 'is__bnot1': 'meadow_is__bnot1', 'is_libitem': 'meadow_is_libitem', 'has_ti': 'meadow_has_ti', 'has_ti0': 'meadow_has_ti0', 'has_ti1': 'meadow_has_ti1', 'has_lname': 'meadow_has_lname', 'is_tilcmt': 'meadow_is_tilcmt', 'is_usersp': 'meadow_is_usersp', 'is_lzero0': 'meadow_is_lzero0', 'is_lzero1': 'meadow_is_lzero1', 'is_colored_item': 'meadow_is_colored_item', 'is_terse_struc': 'meadow_is_terse_struc', 'is__invsign0': 'meadow_is__invsign0', 'is__invsign1': 'meadow_is__invsign1', 'is_noret': 'meadow_is_noret', 'is_fixed_spd': 'meadow_is_fixed_spd', 'is_align_flow': 'meadow_is_align_flow', 'is_userti': 'meadow_is_userti', 'is_retfp': 'meadow_is_retfp', 'is_notcode': 'meadow_is_notcode', 'get_import_module_qty': 'meadow_get_import_module_qty', 'get_import_module_name': 'meadow_get_import_module_name', 'enum_import_names': 'meadow_enum_import_names', 'get_imagebase': 'meadow_get_imagebase', 'retrieve_input_file_sha256': 'meadow_retrieve_input_file_sha256', 'retrieve_input_file_md5': 'meadow_retrieve_input_file_md5', 'get_input_file_path': 'meadow_get_input_file_path', 'ida_funcs': 'meadow_ida_funcs', 'FUNC_NORET': 'meadow_FUNC_NORET', 'FUNC_FAR': 'meadow_FUNC_FAR', 'FUNC_LIB': 'meadow_FUNC_LIB', 'FUNC_STATICDEF': 'meadow_FUNC_STATICDEF', 'FUNC_FRAME': 'meadow_FUNC_FRAME', 'FUNC_USERFAR': 'meadow_FUNC_USERFAR', 'FUNC_HIDDEN': 'meadow_FUNC_HIDDEN', 'FUNC_THUNK': 'meadow_FUNC_THUNK', 'FUNC_BOTTOMBP': 'meadow_FUNC_BOTTOMBP', 'FUNC_NORET_PENDING': 'meadow_FUNC_NORET_PENDING', 'FUNC_SP_READY': 'meadow_FUNC_SP_READY', 'FUNC_PURGED_OK': 'meadow_FUNC_PURGED_OK', 'get_func': 'meadow_get_func', 'get_func_cmt': 'meadow_get_func_cmt', 'get_func_name': 'meadow_get_func_name', 'get_func_qty': 'meadow_get_func_qty', 'getn_func': 'meadow_getn_func', 'BasicBlock': 'meadow_BasicBlock', 'preds': 'meadow_preds', 'succs': 'meadow_succs', 'idaapi': 'meadow_idaapi', 'fl_U': 'meadow_fl_U', 'fl_CF': 'meadow_fl_CF', 'fl_CN': 'meadow_fl_CN', 'fl_JF': 'meadow_fl_JF', 'fl_JN': 'meadow_fl_JN', 'fl_USobsolete': 'meadow_fl_USobsolete', 'fl_F': 'meadow_fl_F', 'dr_U': 'meadow_dr_U', 'dr_O': 'meadow_dr_O', 'dr_W': 'meadow_dr_W', 'dr_R': 'meadow_dr_R', 'dr_T': 'meadow_dr_T', 'dr_I': 'meadow_dr_I', 'XREF_ALL': 'meadow_XREF_ALL', 'XREF_FAR': 'meadow_XREF_FAR', 'XREF_DATA': 'meadow_XREF_DATA', '_find_bb_end': 'meadow__find_bb_end', '_find_bb_start': 'meadow__find_bb_start', '_get_flow_preds': 'meadow__get_flow_preds', '_get_flow_succs': 'meadow__get_flow_succs', 'FlowChart': 'meadow_FlowChart', 'get_next_fixup_ea': 'meadow_get_next_fixup_ea', 'contains_fixups': 'meadow_contains_fixups', 'getseg': 'meadow_getseg', 'get_segm_name': 'meadow_get_segm_name', 'get_segm_end': 'meadow_get_segm_end', 'get_inf_structure': 'meadow_get_inf_structure', 'TYPE_NAMES': 'meadow_TYPE_NAMES', 'get_file_type_name': 'meadow_get_file_type_name', 'StringItem': 'meadow_StringItem', '_Strings': 'meadow__Strings', 'C': 'meadow_C', 'C_16': 'meadow_C_16', 'C_32': 'meadow_C_32', 'PASCAL': 'meadow_PASCAL', 'PASCAL_16': 'meadow_PASCAL_16', 'LEN2': 'meadow_LEN2', 'LEN2_16': 'meadow_LEN2_16', 'LEN4': 'meadow_LEN4', 'LEN4_16': 'meadow_LEN4_16', 'ASCII_BYTE': 'meadow_ASCII_BYTE', 'clear_cache': 'meadow_clear_cache', 'get_seg_data': 'meadow_get_seg_data', 'parse_C_strings': 'meadow_parse_C_strings', 'parse_C_16_strings': 'meadow_parse_C_16_strings', 'parse_C_32_strings': 'meadow_parse_C_32_strings', 'parse_PASCAL_strings': 'meadow_parse_PASCAL_strings', 'parse_PASCAL_16_strings': 'meadow_parse_PASCAL_16_strings', 'parse_LEN2_strings': 'meadow_parse_LEN2_strings', 'parse_LEN2_16_strings': 'meadow_parse_LEN2_16_strings', 'parse_LEN4_strings': 'meadow_parse_LEN4_strings', 'parse_LEN4_16_strings': 'meadow_parse_LEN4_16_strings', 'refresh': 'meadow_refresh', 'setup': 'meadow_setup', 'idautils': 'meadow_idautils', 'GetInputFileMD5': 'meadow_GetInputFileMD5', 'Segments': 'meadow_Segments', 'Functions': 'meadow_Functions', 'Chunks': 'meadow_Chunks', 'Heads': 'meadow_Heads', '_get_fallthrough_xref_to': 'meadow__get_fallthrough_xref_to', 'CodeRefsTo': 'meadow_CodeRefsTo', '_get_fallthrough_xref_from': 'meadow__get_fallthrough_xref_from', 'CodeRefsFrom': 'meadow_CodeRefsFrom', 'ALL_DREF_TYPES': 'meadow_ALL_DREF_TYPES', 'ALL_CREF_TYPES': 'meadow_ALL_CREF_TYPES', 'DataRefsFrom': 'meadow_DataRefsFrom', 'DataRefsTo': 'meadow_DataRefsTo', 'XrefsTo': 'meadow_XrefsTo', 'XrefsFrom': 'meadow_XrefsFrom', 'Strings': 'meadow_Strings', 'Names': 'meadow_Names', 'Entries': 'meadow_Entries', 'ida_entry': 'meadow_ida_entry', 'get_entry_qty': 'meadow_get_entry_qty', 'get_entry_ordinal': 'meadow_get_entry_ordinal', 'get_entry_name': 'meadow_get_entry_name', 'get_entry_forwarder': 'meadow_get_entry_forwarder', 'ida_name': 'meadow_ida_name', '_get_name_ptrs': 'meadow__get_name_ptrs', 'get_nlist_size': 'meadow_get_nlist_size', 'get_nlist_ea': 'meadow_get_nlist_ea', 'get_nlist_name': 'meadow_get_nlist_name', 'ida_struct': 'meadow_ida_struct', '_load_structs': 'meadow__load_structs', 'get_member_by_fullname': 'meadow_get_member_by_fullname', 'get_member_by_id': 'meadow_get_member_by_id', 'get_member_by_name': 'meadow_get_member_by_name', 'get_member_cmt': 'meadow_get_member_cmt', 'get_member_fullname': 'meadow_get_member_fullname', 'get_member_name': 'meadow_get_member_name', 'get_member_size': 'meadow_get_member_size', 'get_member_struc': 'meadow_get_member_struc', 'get_member_tinfo': 'meadow_get_member_tinfo', 'get_struc_id': 'meadow_get_struc_id', 'get_first_struc_idx': 'meadow_get_first_struc_idx', 'get_last_struc_idx': 'meadow_get_last_struc_idx', 'get_struc': 'meadow_get_struc', 'get_struc_by_idx': 'meadow_get_struc_by_idx', 'get_struc_name': 'meadow_get_struc_name', 'get_struc_idx': 'meadow_get_struc_idx', 'ida_typeinf': 'meadow_ida_typeinf', 'get_named_type': 'meadow_get_named_type', 'get_type_flags': 'meadow_get_type_flags', 'get_base_flags': 'meadow_get_base_flags', 'get_numbered_type': 'meadow_get_numbered_type', 'get_ordinal_from_idb_type': 'meadow_get_ordinal_from_idb_type', 'IDAPython': 'meadow_IDAPython', 'is_32bit': 'meadow_is_32bit', 'is_64bit': 'meadow_is_64bit', 'is_snapshot': 'meadow_is_snapshot', 'is_dll': 'meadow_is_dll', 'is_flat_off32': 'meadow_is_flat_off32', 'is_be': 'meadow_is_be', 'is_wide_high_byte_first': 'meadow_is_wide_high_byte_first', 'is_kernel_mode': 'meadow_is_kernel_mode', '_FlowChart': 'meadow__FlowChart', 'f_EXE_old': 'meadow_f_EXE_old', 'f_COM_old': 'meadow_f_COM_old', 'f_BIN': 'meadow_f_BIN', 'f_DRV': 'meadow_f_DRV', 'f_WIN': 'meadow_f_WIN', 'f_HEX': 'meadow_f_HEX', 'f_MEX': 'meadow_f_MEX', 'f_LX': 'meadow_f_LX', 'f_LE': 'meadow_f_LE', 'f_NLM': 'meadow_f_NLM', 'f_COFF': 'meadow_f_COFF', 'f_PE': 'meadow_f_PE', 'f_OMF': 'meadow_f_OMF', 'f_SREC': 'meadow_f_SREC', 'f_ZIP': 'meadow_f_ZIP', 'f_OMFLIB': 'meadow_f_OMFLIB', 'f_AR': 'meadow_f_AR', 'f_LOADER': 'meadow_f_LOADER', 'f_ELF': 'meadow_f_ELF', 'f_W32RUN': 'meadow_f_W32RUN', 'f_AOUT': 'meadow_f_AOUT', 'f_PRC': 'meadow_f_PRC', 'f_EXE': 'meadow_f_EXE', 'f_COM': 'meadow_f_COM', 'f_AIXAR': 'meadow_f_AIXAR', 'f_MACHO': 'meadow_f_MACHO', 'STT_CUR': 'meadow_STT_CUR', 'STT_VA': 'meadow_STT_VA', 'STT_MM': 'meadow_STT_MM', 'STT_DBG': 'meadow_STT_DBG', 'INFFL_AUTO': 'meadow_INFFL_AUTO', 'INFFL_ALLASM': 'meadow_INFFL_ALLASM', 'INFFL_LOADIDC': 'meadow_INFFL_LOADIDC', 'INFFL_NOUSER': 'meadow_INFFL_NOUSER', 'INFFL_READONLY': 'meadow_INFFL_READONLY', 'INFFL_CHKOPS': 'meadow_INFFL_CHKOPS', 'INFFL_NMOPS': 'meadow_INFFL_NMOPS', 'INFFL_GRAPH_VIEW': 'meadow_INFFL_GRAPH_VIEW', 'LFLG_PC_FPP': 'meadow_LFLG_PC_FPP', 'LFLG_PC_FLAT': 'meadow_LFLG_PC_FLAT', 'LFLG_64BIT': 'meadow_LFLG_64BIT', 'LFLG_IS_DLL': 'meadow_LFLG_IS_DLL', 'LFLG_FLAT_OFF32': 'meadow_LFLG_FLAT_OFF32', 'LFLG_MSF': 'meadow_LFLG_MSF', 'LFLG_WIDE_HBF': 'meadow_LFLG_WIDE_HBF', 'LFLG_DBG_NOPATH': 'meadow_LFLG_DBG_NOPATH', 'LFLG_SNAPSHOT': 'meadow_LFLG_SNAPSHOT', 'LFLG_PACK': 'meadow_LFLG_PACK', 'LFLG_COMPRESS': 'meadow_LFLG_COMPRESS', 'LFLG_KERNMODE': 'meadow_LFLG_KERNMODE', 'IDB_UNPACKED': 'meadow_IDB_UNPACKED', 'IDB_PACKED': 'meadow_IDB_PACKED', 'IDB_COMPRESSED': 'meadow_IDB_COMPRESSED', 'AF_CODE': 'meadow_AF_CODE', 'AF_MARKCODE': 'meadow_AF_MARKCODE', 'AF_JUMPTBL': 'meadow_AF_JUMPTBL', 'AF_PURDAT': 'meadow_AF_PURDAT', 'AF_USED': 'meadow_AF_USED', 'AF_UNK': 'meadow_AF_UNK', 'AF_PROCPTR': 'meadow_AF_PROCPTR', 'AF_PROC': 'meadow_AF_PROC', 'AF_FTAIL': 'meadow_AF_FTAIL', 'AF_LVAR': 'meadow_AF_LVAR', 'AF_STKARG': 'meadow_AF_STKARG', 'AF_REGARG': 'meadow_AF_REGARG', 'AF_TRACE': 'meadow_AF_TRACE', 'AF_VERSP': 'meadow_AF_VERSP', 'AF_ANORET': 'meadow_AF_ANORET', 'AF_MEMFUNC': 'meadow_AF_MEMFUNC', 'AF_TRFUNC': 'meadow_AF_TRFUNC', 'AF_STRLIT': 'meadow_AF_STRLIT', 'AF_CHKUNI': 'meadow_AF_CHKUNI', 'AF_FIXUP': 'meadow_AF_FIXUP', 'AF_DREFOFF': 'meadow_AF_DREFOFF', 'AF_IMMOFF': 'meadow_AF_IMMOFF', 'AF_DATOFF': 'meadow_AF_DATOFF', 'AF_FLIRT': 'meadow_AF_FLIRT', 'AF_SIGCMT': 'meadow_AF_SIGCMT', 'AF_SIGMLT': 'meadow_AF_SIGMLT', 'AF_HFLIRT': 'meadow_AF_HFLIRT', 'AF_JFUNC': 'meadow_AF_JFUNC', 'AF_NULLSUB': 'meadow_AF_NULLSUB', 'AF_DODATA': 'meadow_AF_DODATA', 'AF_DOCODE': 'meadow_AF_DOCODE', 'AF_FINAL': 'meadow_AF_FINAL', 'AF2_DOEH': 'meadow_AF2_DOEH', 'AF2_DORTTI': 'meadow_AF2_DORTTI', 'NM_REL_OFF': 'meadow_NM_REL_OFF', 'NM_PTR_OFF': 'meadow_NM_PTR_OFF', 'NM_NAM_OFF': 'meadow_NM_NAM_OFF', 'NM_REL_EA': 'meadow_NM_REL_EA', 'NM_PTR_EA': 'meadow_NM_PTR_EA', 'NM_NAM_EA': 'meadow_NM_NAM_EA', 'NM_EA': 'meadow_NM_EA', 'NM_EA4': 'meadow_NM_EA4', 'NM_EA8': 'meadow_NM_EA8', 'NM_SHORT': 'meadow_NM_SHORT', 'NM_SERIAL': 'meadow_NM_SERIAL', 'ABI_8ALIGN4': 'meadow_ABI_8ALIGN4', 'ABI_PACK_STKARGS': 'meadow_ABI_PACK_STKARGS', 'ABI_BIGARG_ALIGN': 'meadow_ABI_BIGARG_ALIGN', 'ABI_STACK_LDBL': 'meadow_ABI_STACK_LDBL', 'ABI_STACK_VARARGS': 'meadow_ABI_STACK_VARARGS', 'ABI_HARD_FLOAT': 'meadow_ABI_HARD_FLOAT', 'ABI_SET_BY_USER': 'meadow_ABI_SET_BY_USER', 'ABI_GCC_LAYOUT': 'meadow_ABI_GCC_LAYOUT', 'UA_MAXOP': 'meadow_UA_MAXOP', 'MAXADDR': 'meadow_MAXADDR', 'IDB_EXT32': 'meadow_IDB_EXT32', 'IDB_EXT64': 'meadow_IDB_EXT64', 'IDB_EXT': 'meadow_IDB_EXT', 'bit_dis': 'meadow_bit_dis', 'seg_dis': 'meadow_seg_dis', 'ARGV': 'meadow_ARGV', 'GetMnem': 'meadow_GetMnem', 'GetOpnd': 'meadow_GetOpnd', 'GetOpType': 'meadow_GetOpType', 'FindFuncEnd': 'meadow_FindFuncEnd', 'get_long': 'meadow_get_long', 'fc': 'meadow_fc', 'lastInstEA': 'meadow_lastInstEA', 'BADADDR': 'meadow_BADADDR', 'ea': 'meadow_ea', 'db': 'meadow_db', 'cache': 'meadow_cache', 'strtypes': 'meadow_strtypes', 'minlen': 'meadow_minlen', 'only_7bit': 'meadow_only_7bit', 'ignore_instructions': 'meadow_ignore_instructions', 'display_only_existing_strings': 'meadow_display_only_existing_strings', 'strings': 'meadow_strings', '_struct_ids': 'meadow__struct_ids', 'types': 'meadow_types', 'FUNCATTR_START': 'meadow_FUNCATTR_START', 'FUNCATTR_END': 'meadow_FUNCATTR_END', 'FUNCATTR_FLAGS': 'meadow_FUNCATTR_FLAGS', 'FUNCATTR_FRAME': 'meadow_FUNCATTR_FRAME', 'FUNCATTR_FRSIZE': 'meadow_FUNCATTR_FRSIZE', 'FUNCATTR_FRREGS': 'meadow_FUNCATTR_FRREGS', 'FUNCATTR_ARGSIZE': 'meadow_FUNCATTR_ARGSIZE', 'FUNCATTR_FPD': 'meadow_FUNCATTR_FPD', 'FUNCATTR_COLOR': 'meadow_FUNCATTR_COLOR', 'SEGATTR_START': 'meadow_SEGATTR_START', 'SEGATTR_END': 'meadow_SEGATTR_END', 'SEGATTR_ORGBASE': 'meadow_SEGATTR_ORGBASE', 'SEGATTR_ALIGN': 'meadow_SEGATTR_ALIGN', 'SEGATTR_COMB': 'meadow_SEGATTR_COMB', 'SEGATTR_PERM': 'meadow_SEGATTR_PERM', 'SEGATTR_BITNESS': 'meadow_SEGATTR_BITNESS', 'SEGATTR_FLAGS': 'meadow_SEGATTR_FLAGS', 'SEGATTR_SEL': 'meadow_SEGATTR_SEL', 'SEGATTR_ES': 'meadow_SEGATTR_ES', 'SEGATTR_CS': 'meadow_SEGATTR_CS', 'SEGATTR_SS': 'meadow_SEGATTR_SS', 'SEGATTR_DS': 'meadow_SEGATTR_DS', 'SEGATTR_FS': 'meadow_SEGATTR_FS', 'SEGATTR_GS': 'meadow_SEGATTR_GS', 'SEGATTR_TYPE': 'meadow_SEGATTR_TYPE', 'SEGATTR_COLOR': 'meadow_SEGATTR_COLOR', 'FUNCATTR_OWNER': 'meadow_FUNCATTR_OWNER', 'FUNCATTR_REFQTY': 'meadow_FUNCATTR_REFQTY', 'bbs': 'meadow_bbs', 'TAGS': 'meadow_TAGS', 'ALTVAL': 'meadow_ALTVAL', 'SUPVAL': 'meadow_SUPVAL', 'CHARVAL': 'meadow_CHARVAL', 'HASHVAL': 'meadow_HASHVAL', 'VALUE': 'meadow_VALUE', 'NAME': 'meadow_NAME', 'LINK': 'meadow_LINK', 'Netnode': 'meadow_Netnode', 'get_nodebase': 'meadow_get_nodebase', 'get_tag_entries': 'meadow_get_tag_entries', 'get_val': 'meadow_get_val', 'supval': 'meadow_supval', 'supstr': 'meadow_supstr', 'sups': 'meadow_sups', 'supentries': 'meadow_supentries', 'altval': 'meadow_altval', 'alts': 'meadow_alts', 'altentries': 'meadow_altentries', 'charval': 'meadow_charval', 'chars': 'meadow_chars', 'charentries': 'meadow_charentries', 'hashval': 'meadow_hashval', 'hashes': 'meadow_hashes', 'hashentries': 'meadow_hashentries', 'valobj': 'meadow_valobj', 'valstr': 'meadow_valstr', 'value_exists': 'meadow_value_exists', 'long_value': 'meadow_long_value', 'blobsize': 'meadow_blobsize', 'getblob': 'meadow_getblob', 'nodebase': 'meadow_nodebase', 'HookedImporter': 'meadow_HookedImporter', 'find_module': 'meadow_find_module', 'load_module': 'meadow_load_module', 'install': 'meadow_install', 'find_spec': 'meadow_find_spec', 'create_module': 'meadow_create_module', 'exec_module': 'meadow_exec_module', 'hooks': 'meadow_hooks', 'seek': 'meadow_seek', 'read': 'meadow_read', 'unpack': 'meadow_unpack', 'peek_u8': 'meadow_peek_u8', 'peek_u16': 'meadow_peek_u16', 'dt': 'meadow_dt', 'de': 'meadow_de', 'pstring': 'meadow_pstring', 'pbytes': 'meadow_pbytes', 'type_attr': 'meadow_type_attr', 'tah_attr': 'meadow_tah_attr', 'sdacl_attr': 'meadow_sdacl_attr', 'get': 'meadow_get', 'ref': 'meadow_ref', 'rest': 'meadow_rest', 'has_next': 'meadow_has_next', 'TypeData': 'meadow_TypeData', 'deserialize': 'meadow_deserialize', 'TInfo': 'meadow_TInfo', 'get_refname': 'meadow_get_refname', 'get_next_tinfo': 'meadow_get_next_tinfo', 'get_final_tinfo': 'meadow_get_final_tinfo', 'get_arr_object': 'meadow_get_arr_object', 'get_pointed_object': 'meadow_get_pointed_object', 'get_ptrarr_object': 'meadow_get_ptrarr_object', 'get_cc': 'meadow_get_cc', 'get_rettype': 'meadow_get_rettype', 'get_size': 'meadow_get_size', 'get_conv': 'meadow_get_conv', 'get_typename': 'meadow_get_typename', 'get_typedeclare': 'meadow_get_typedeclare', 'get_typestr': 'meadow_get_typestr', 'has_details': 'meadow_has_details', 'has_vftable': 'meadow_has_vftable', 'get_decltype': 'meadow_get_decltype', 'get_realtype': 'meadow_get_realtype', 'is_decl_typedef': 'meadow_is_decl_typedef', 'is_decl_array': 'meadow_is_decl_array', 'is_decl_bitfield': 'meadow_is_decl_bitfield', 'is_decl_bool': 'meadow_is_decl_bool', 'is_decl_char': 'meadow_is_decl_char', 'is_decl_complex': 'meadow_is_decl_complex', 'is_decl_const': 'meadow_is_decl_const', 'is_decl_double': 'meadow_is_decl_double', 'is_decl_enum': 'meadow_is_decl_enum', 'is_decl_float': 'meadow_is_decl_float', 'is_decl_floating': 'meadow_is_decl_floating', 'is_decl_func': 'meadow_is_decl_func', 'is_decl_int': 'meadow_is_decl_int', 'is_decl_int128': 'meadow_is_decl_int128', 'is_decl_int16': 'meadow_is_decl_int16', 'is_decl_int32': 'meadow_is_decl_int32', 'is_decl_int64': 'meadow_is_decl_int64', 'is_decl_paf': 'meadow_is_decl_paf', 'is_decl_partial': 'meadow_is_decl_partial', 'is_decl_ptr': 'meadow_is_decl_ptr', 'is_decl_ptr_or_array': 'meadow_is_decl_ptr_or_array', 'is_decl_struct': 'meadow_is_decl_struct', 'is_decl_sue': 'meadow_is_decl_sue', 'is_decl_uchar': 'meadow_is_decl_uchar', 'is_decl_udt': 'meadow_is_decl_udt', 'is_decl_uint': 'meadow_is_decl_uint', 'is_decl_uint128': 'meadow_is_decl_uint128', 'is_decl_uint16': 'meadow_is_decl_uint16', 'is_decl_uint32': 'meadow_is_decl_uint32', 'is_decl_uint64': 'meadow_is_decl_uint64', 'is_decl_union': 'meadow_is_decl_union', 'is_decl_unknown': 'meadow_is_decl_unknown', 'is_decl_void': 'meadow_is_decl_void', 'is_decl_volatile': 'meadow_is_decl_volatile', 'is_arithmetic': 'meadow_is_arithmetic', 'is_array': 'meadow_is_array', 'is_bitfield': 'meadow_is_bitfield', 'is_bool': 'meadow_is_bool', 'is_castable_to': 'meadow_is_castable_to', 'is_char': 'meadow_is_char', 'is_complex': 'meadow_is_complex', 'is_const': 'meadow_is_const', 'is_correct': 'meadow_is_correct', 'is_empty_udt': 'meadow_is_empty_udt', 'is_enum': 'meadow_is_enum', 'is_ext_arithmetic': 'meadow_is_ext_arithmetic', 'is_ext_integral': 'meadow_is_ext_integral', 'is_floating': 'meadow_is_floating', 'is_forward_decl': 'meadow_is_forward_decl', 'is_from_subtil': 'meadow_is_from_subtil', 'is_funcptr': 'meadow_is_funcptr', 'is_high_func': 'meadow_is_high_func', 'is_int': 'meadow_is_int', 'is_int128': 'meadow_is_int128', 'is_int16': 'meadow_is_int16', 'is_int32': 'meadow_is_int32', 'is_int64': 'meadow_is_int64', 'is_integral': 'meadow_is_integral', 'is_ldouble': 'meadow_is_ldouble', 'is_manually_castable_to': 'meadow_is_manually_castable_to', 'is_one_fpval': 'meadow_is_one_fpval', 'is_paf': 'meadow_is_paf', 'is_partial': 'meadow_is_partial', 'is_ptr': 'meadow_is_ptr', 'is_ptr_or_array': 'meadow_is_ptr_or_array', 'is_purging_cc': 'meadow_is_purging_cc', 'is_pvoid': 'meadow_is_pvoid', 'is_scalar': 'meadow_is_scalar', 'is_shifted_ptr': 'meadow_is_shifted_ptr', 'is_signed': 'meadow_is_signed', 'is_small_udt': 'meadow_is_small_udt', 'is_sse_type': 'meadow_is_sse_type', 'is_sue': 'meadow_is_sue', 'is_uchar': 'meadow_is_uchar', 'is_udt': 'meadow_is_udt', 'is_uint': 'meadow_is_uint', 'is_uint128': 'meadow_is_uint128', 'is_uint16': 'meadow_is_uint16', 'is_uint32': 'meadow_is_uint32', 'is_uint64': 'meadow_is_uint64', 'is_union': 'meadow_is_union', 'is_unsigned': 'meadow_is_unsigned', 'is_user_cc': 'meadow_is_user_cc', 'is_vararg_cc': 'meadow_is_vararg_cc', 'is_varstruct': 'meadow_is_varstruct', 'is_vftable': 'meadow_is_vftable', 'is_void': 'meadow_is_void', 'is_volatile': 'meadow_is_volatile', 'ErrorTInfo': 'meadow_ErrorTInfo', 'PointerTypeData': 'meadow_PointerTypeData', 'ArrayTypeData': 'meadow_ArrayTypeData', 'FuncArg': 'meadow_FuncArg', 'RRel': 'meadow_RRel', 'ArgLoc': 'meadow_ArgLoc', 'get_reg1': 'meadow_get_reg1', 'get_reg2': 'meadow_get_reg2', 'get_reginfo': 'meadow_get_reginfo', 'get_stkoff': 'meadow_get_stkoff', 'ArgPart': 'meadow_ArgPart', 'RegInfo': 'meadow_RegInfo', 'FuncTypeData': 'meadow_FuncTypeData', 'deserialize_argloc': 'meadow_deserialize_argloc', 'UdtMember': 'meadow_UdtMember', 'is_unaligned': 'meadow_is_unaligned', 'is_baseclass': 'meadow_is_baseclass', 'is_virtbase': 'meadow_is_virtbase', 'UdtTypeData': 'meadow_UdtTypeData', 'EnumMember': 'meadow_EnumMember', 'EnumTypeData': 'meadow_EnumTypeData', 'calc_mask': 'meadow_calc_mask', 'TypedefTypeData': 'meadow_TypedefTypeData', 'BitfieldTypeData': 'meadow_BitfieldTypeData', 'v_zbytes': 'meadow_v_zbytes', 'TILTypeInfo': 'meadow_TILTypeInfo', 'TILBucket': 'meadow_TILBucket', 'find_by_name': 'meadow_find_by_name', 'ordinal_defs': 'meadow_ordinal_defs', 'get_by_ordinal': 'meadow_get_by_ordinal', 'TIL': 'meadow_TIL', 'deserialize_bucket': 'meadow_deserialize_bucket', 'base_type': 'meadow_base_type', 'type_details': 'meadow_type_details', '_types': 'meadow__types', 'obj_type': 'meadow_obj_type', 'closure': 'meadow_closure', 'based_ptr_size': 'meadow_based_ptr_size', 'taptr_bits': 'meadow_taptr_bits', 'elem_type': 'meadow_elem_type', 'n_elems': 'meadow_n_elems', 'argloc': 'meadow_argloc', 'reg': 'meadow_reg', 'sval': 'meadow_sval', 'reginfo': 'meadow_reginfo', 'rrel': 'meadow_rrel', 'dist': 'meadow_dist', 'custom': 'meadow_custom', 'biggest': 'meadow_biggest', 'args': 'meadow_args', 'rettype': 'meadow_rettype', 'retloc': 'meadow_retloc', 'stkargs': 'meadow_stkargs', 'spoiled': 'meadow_spoiled', 'cc': 'meadow_cc', 'effalign': 'meadow_effalign', 'tafld_bits': 'meadow_tafld_bits', 'fda': 'meadow_fda', 'members': 'meadow_members', 'total_size': 'meadow_total_size', 'unpadded_size': 'meadow_unpadded_size', 'taudt_bits': 'meadow_taudt_bits', 'sda': 'meadow_sda', 'pack': 'meadow_pack', 'group_sizes': 'meadow_group_sizes', 'taenum_bits': 'meadow_taenum_bits', 'bte': 'meadow_bte', 'is_ordref': 'meadow_is_ordref', 'resolve': 'meadow_resolve', 'nbytes': 'meadow_nbytes', 'width': 'meadow_width', 'TILEncoder': 'meadow_TILEncoder', 'BTreeExplorer': 'meadow_BTreeExplorer', 'current_page': 'meadow_current_page', 'TestDidntRunError': 'meadow_TestDidntRunError', 'fileformat': 'database_pages', 'typeinf': 'type_records', 'typeinf_flags': 'type_codes', 'analysis': 'semantic_views', 'idapython': 'ida_interfaces', 'shim': 'script_environment', 'dump_btree': 'meadow_dump_btree', 'dump_scripts': 'meadow_dump_scripts', 'dump_section_list': 'meadow_dump_section_list', 'dump_types': 'meadow_dump_types', 'dump_user': 'meadow_dump_user', 'explore_btree': 'meadow_explore_btree', 'extract_function_names': 'meadow_extract_function_names', 'extract_md5': 'meadow_extract_md5', 'extract_version': 'meadow_extract_version', 'run_ida_script': 'meadow_run_ida_script', 'yara_fn': 'meadow_yara_fn', 'conftest': 'conftest', 'fixtures': 'fixture_registry', 'test_analysis': 'test_meadow_analysis', 'test_idaapi': 'test_meadow_idaapi', 'test_idb': 'test_meadow_idb', 'test_issue22': 'test_meadow_issue22', 'test_issue28': 'test_meadow_issue28', 'test_issue29': 'test_meadow_issue29', 'test_issue30': 'test_meadow_issue30', 'test_multiarch_disasm': 'test_meadow_multiarch_disasm', 'test_netnode': 'test_meadow_netnode', 'test_scripts': 'test_meadow_scripts'})
class meadow_Struct:
    """
    Example::

        struc = Struct(idb, 0xFF000075)
        assert struc.get_name() == 'EXCEPTION_INFO'
        assert len(struc.get_members()) == 5
        assert list(struc.get_members())[0].get_type() == 'DWORD'
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_c519d4a', 'db': 'meadow_db_5140e7c', 'identity': 'meadow_identity_222591c'}, '__init__')
    def __init__(meadow_self_c519d4a, meadow_db_5140e7c, meadow_identity_222591c):
        """from https://github.com/nlitsme/pyidbutil/blob/7705bcde167fd34a5800bfe54ba99d195b44bbbb/idblib.py#L1380
        Decodes info for structures
        (structnode, N)          = structname
        (structnode, D, address) = xref-type
        (structnode, M, 0)       = packed struct info
        (structnode, S, 27)      = packed value(addr, byte)
        """
        _name_boundary.attributes(meadow_self_c519d4a)['idb'] = meadow_db_5140e7c
        if isinstance(meadow_identity_222591c, meadow_six.integer_types):
            meadow_nodebase_d4758c7 = _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'])['get_nodebase'](meadow_db_5140e7c)
            if meadow_identity_222591c < meadow_nodebase_d4758c7:
                meadow_identity_222591c += meadow_nodebase_d4758c7
            _name_boundary.attributes(meadow_self_c519d4a)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_5140e7c, meadow_identity_222591c)
            _name_boundary.attributes(meadow_self_c519d4a)['nodeid'] = meadow_identity_222591c
        elif isinstance(meadow_identity_222591c, meadow_six.string_types):
            _name_boundary.attributes(meadow_self_c519d4a)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_5140e7c, meadow_identity_222591c)
            _name_boundary.attributes(meadow_self_c519d4a)['nodeid'] = _name_boundary.attributes(_name_boundary.attributes(meadow_self_c519d4a)['netnode'])['nodeid']
        else:
            raise ValueError('Expected identify is integer or string')

    @_name_boundary.callable_contract({'self': 'meadow_self_8daf440'}, 'get_name')
    def meadow_get_name(meadow_self_8daf440):
        return _name_boundary.attributes(meadow_self_8daf440)['netnode'].name()

    @_name_boundary.callable_contract({'self': 'meadow_self_1abd8ae'}, 'get_members')
    def meadow_get_members(meadow_self_1abd8ae):
        meadow_v_5787685 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_1abd8ae)['netnode'])['supval'](tag='M', index=0)
        meadow_u_185b62f = meadow_Unpacker(meadow_v_5787685, wordsize=_name_boundary.attributes(meadow_self_1abd8ae)['idb'].wordsize)
        meadow_flags_local_7f48b25 = _name_boundary.attributes(meadow_u_185b62f)['dd']()
        meadow_count_local_ef235e4 = _name_boundary.attributes(meadow_u_185b62f)['dd']()
        for meadow_i_41cde04 in range(meadow_count_local_ef235e4):
            meadow_nodeid_offset_4c58e9e = _name_boundary.attributes(meadow_u_185b62f)['addr']()
            meadow___5420dc3 = _name_boundary.attributes(meadow_u_185b62f)['addr']()
            meadow___5420dc3 = _name_boundary.attributes(meadow_u_185b62f)['addr']()
            meadow___5420dc3 = _name_boundary.attributes(meadow_u_185b62f)['dd']()
            meadow___5420dc3 = _name_boundary.attributes(meadow_u_185b62f)['dd']()
            meadow_member_nodeid_eb45033 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_1abd8ae)['netnode'])['nodebase'] + meadow_nodeid_offset_4c58e9e
            yield meadow_StructMember(_name_boundary.attributes(meadow_self_1abd8ae)['idb'], meadow_member_nodeid_eb45033)

    @_name_boundary.callable_contract({'self': 'meadow_self_47438fd', 'name': 'meadow_name_local_ad2848b'}, 'find_member_by_name')
    def meadow_find_member_by_name(meadow_self_47438fd, meadow_name_local_ad2848b):
        for meadow_m_b80d4de in _name_boundary.attributes(meadow_self_47438fd)['get_members']():
            if _name_boundary.attributes(meadow_m_b80d4de)['get_name']() == meadow_name_local_ad2848b:
                return meadow_m_b80d4de
        return None

@_name_boundary.callable_contract({'l': 'meadow_l_dbb070e', 'n': 'meadow_n_f3747d0'}, 'chunks')
def meadow_chunks(meadow_l_dbb070e, meadow_n_f3747d0):
    """
    Yield successive n-sized chunks from l.
    via: https://stackoverflow.com/a/312464/87207
    """
    if isinstance(meadow_l_dbb070e, meadow_types.GeneratorType):
        while True:
            meadow_v_2bd63b3 = list(meadow_itertools.islice(meadow_l_dbb070e, meadow_n_f3747d0))
            if not meadow_v_2bd63b3:
                return
            yield meadow_v_2bd63b3
    else:
        meadow_i_868085b = 0
        while True:
            try:
                meadow_v_2bd63b3 = meadow_l_dbb070e[meadow_i_868085b:meadow_i_868085b + meadow_n_f3747d0]
                yield meadow_v_2bd63b3
            except IndexError:
                return
            meadow_i_868085b += meadow_n_f3747d0

@_name_boundary.callable_contract({'l': 'meadow_l_604d9af'}, 'pairs')
def meadow_pairs(meadow_l_604d9af):
    return meadow_chunks(meadow_l_604d9af, 2)
meadow_Chunk = _name_boundary.named_record('Chunk', ['effective_address', 'length'])
meadow_FunctionParameter = _name_boundary.named_record('FunctionParameter', ['type', 'name'])
meadow_FunctionSignature = _name_boundary.named_record('FunctionSignature', ['calling_convention', 'rtype', 'unk', 'parameters'])
meadow_StackChangePoint = _name_boundary.named_record('StackChangePoint', ['effective_address', 'change'])

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_2331408'}, 'create_pstring_list')
def meadow_create_pstring_list(meadow_buf_local_2331408):
    meadow__lst_9b8ab66 = []
    meadow_ofs_local_c706e5b = 0
    while meadow_ofs_local_c706e5b < len(meadow_buf_local_2331408.strip(b'\x00')):
        meadow__len_db52ef0 = struct.unpack_from('<B', meadow_buf_local_2331408, meadow_ofs_local_c706e5b)[0]
        meadow__lst_9b8ab66.append(meadow_buf_local_2331408[meadow_ofs_local_c706e5b:meadow_ofs_local_c706e5b + meadow__len_db52ef0][1:].decode('utf-8'))
        meadow_ofs_local_c706e5b += meadow__len_db52ef0
        if meadow__len_db52ef0 == 0:
            meadow_ofs_local_c706e5b += 1
    return meadow__lst_9b8ab66

@_name_boundary.class_contract('Function', {'get_name': 'meadow_get_name', 'get_signature': 'meadow_get_signature', 'get_chunks': 'meadow_get_chunks', 'get_stack_change_points': 'meadow_get_stack_change_points', 'idb': 'meadow_idb', 'nodeid': 'meadow_nodeid', 'netnode': 'meadow_netnode'})
class meadow_Function:
    """
    Example::

        func = Function(idb, 0x401000)
        assert func.get_name() == 'DllEntryPoint'
        assert func.get_signature() == '... DllEntryPoint(...)'
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_7e43f0c', 'db': 'meadow_db_a3a8502', 'fva': 'meadow_fva_1d0eb7a'}, '__init__')
    def __init__(meadow_self_7e43f0c, meadow_db_a3a8502, meadow_fva_1d0eb7a):
        _name_boundary.attributes(meadow_self_7e43f0c)['idb'] = meadow_db_a3a8502
        _name_boundary.attributes(meadow_self_7e43f0c)['nodeid'] = meadow_fva_1d0eb7a
        _name_boundary.attributes(meadow_self_7e43f0c)['netnode'] = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_a3a8502, _name_boundary.attributes(meadow_self_7e43f0c)['nodeid'])

    @_name_boundary.callable_contract({'self': 'meadow_self_d388fac'}, 'get_name')
    def meadow_get_name(meadow_self_d388fac):
        try:
            return _name_boundary.attributes(meadow_self_d388fac)['netnode'].name()
        except KeyError:
            return 'sub_%X' % _name_boundary.attributes(meadow_self_d388fac)['nodeid']

    @_name_boundary.callable_contract({'self': 'meadow_self_5eeec34'}, 'get_signature')
    def meadow_get_signature(meadow_self_5eeec34):
        try:
            meadow_typebuf_93314be = _name_boundary.attributes(_name_boundary.attributes(meadow_self_5eeec34)['netnode'])['supval'](tag='S', index=12288)
            meadow_namebuf_b7a89b6 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_5eeec34)['netnode'])['supval'](tag='S', index=12289)
            meadow_typ_local_87d885b = meadow_six.indexbytes(meadow_typebuf_93314be, 0)
            if not _name_boundary.attributes(meadow_idb)['typeinf_flags'].is_type_func(meadow_typ_local_87d885b):
                raise RuntimeError('is not function')
            meadow_names_add2a25 = meadow_create_pstring_list(meadow_namebuf_b7a89b6)
            meadow_typedata_a94850b = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['FuncTypeData']()
            meadow_ts_96acd2b = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['TypeString'](meadow_typebuf_93314be)
            _name_boundary.attributes(meadow_typedata_a94850b)['deserialize'](_name_boundary.attributes(meadow_self_5eeec34)['idb'].til, meadow_ts_96acd2b, meadow_names_add2a25, [])
            meadow_inf_local_8aa0014 = meadow_Root(_name_boundary.attributes(meadow_self_5eeec34)['idb']).idainfo
            return _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['TInfo'](meadow_typ_local_87d885b, meadow_typedata_a94850b, til=_name_boundary.attributes(meadow_self_5eeec34)['idb'].til, name=_name_boundary.attributes(meadow_self_5eeec34)['get_name'](), inf=meadow_inf_local_8aa0014)
        except KeyError:
            return None

    @_name_boundary.callable_contract({'self': 'meadow_self_76bc15e'}, 'get_chunks')
    def meadow_get_chunks(meadow_self_76bc15e):
        meadow_v_68fffe7 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_76bc15e)['netnode'])['supval'](tag='S', index=28672)
        meadow_last_ea_dfa5681 = 0
        meadow_last_length_6dcaa5d = 0
        if _name_boundary.attributes(meadow_self_76bc15e)['idb'].wordsize == 4:
            meadow_unpacker_f00c4e2 = meadow_unpack_dds
        elif _name_boundary.attributes(meadow_self_76bc15e)['idb'].wordsize == 8:
            meadow_unpacker_f00c4e2 = meadow_unpack_dqs
        else:
            raise RuntimeError('unexpected wordsize')
        for meadow_delta_f1c1eca, meadow_length_local_d630502 in meadow_pairs(meadow_unpacker_f00c4e2(meadow_v_68fffe7)):
            meadow_ea_824de5a = meadow_last_ea_dfa5681 + meadow_last_length_6dcaa5d + meadow_delta_f1c1eca
            yield meadow_Chunk(meadow_ea_824de5a, meadow_length_local_d630502)
            meadow_last_ea_dfa5681 = meadow_ea_824de5a
            meadow_last_length_6dcaa5d = meadow_length_local_d630502

    @_name_boundary.callable_contract({'self': 'meadow_self_2abf4df'}, 'get_stack_change_points')
    def meadow_get_stack_change_points(meadow_self_2abf4df):
        try:
            meadow_v_3714483 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_2abf4df)['netnode'])['supval'](tag='S', index=4096)
        except KeyError:
            return
        meadow_offset_local_7cc8417 = _name_boundary.attributes(meadow_self_2abf4df)['nodeid']
        if _name_boundary.attributes(meadow_self_2abf4df)['idb'].wordsize == 4:
            meadow_unpacker_81c88cb = meadow_unpack_dds
        elif _name_boundary.attributes(meadow_self_2abf4df)['idb'].wordsize == 8:
            meadow_unpacker_81c88cb = meadow_unpack_dqs
        else:
            raise RuntimeError('unexpected wordsize')
        for meadow_delta_944c4c3, meadow_change_b21fc62 in meadow_pairs(meadow_unpacker_81c88cb(meadow_v_3714483)):
            meadow_offset_local_7cc8417 += meadow_delta_944c4c3
            if meadow_change_b21fc62 & 1:
                meadow_change_b21fc62 = meadow_change_b21fc62 >> 1
            else:
                meadow_change_b21fc62 = -(meadow_change_b21fc62 >> 1)
            yield meadow_StackChangePoint(meadow_offset_local_7cc8417, meadow_change_b21fc62)
meadow_Xref = _name_boundary.named_record('Xref', ['frm', 'to', 'type'])

@_name_boundary.callable_contract({'db': 'meadow_db_a46d4d8', 'src': 'meadow_src_92cb8a8', 'dst': 'meadow_dst_4d8d15a', 'types': 'meadow_types_a9cec5b', 'tag': 'meadow_tag_local_7914704'}, '_get_xrefs')
def meadow__get_xrefs(meadow_db_a46d4d8, meadow_tag_local_7914704, meadow_src_92cb8a8=None, meadow_dst_4d8d15a=None, meadow_types_a9cec5b=None):
    if meadow_src_92cb8a8 is None and meadow_dst_4d8d15a is None:
        raise ValueError('one of src or dst must be provided')
    meadow_nn_2e6f657 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_a46d4d8, meadow_src_92cb8a8 if meadow_dst_4d8d15a is None else meadow_dst_4d8d15a)
    try:
        for meadow_entry_local_8e60148 in _name_boundary.attributes(meadow_nn_2e6f657)['charentries'](tag=meadow_tag_local_7914704):
            if meadow_types_a9cec5b and meadow_entry_local_8e60148.value in meadow_types_a9cec5b or not meadow_types_a9cec5b:
                if meadow_src_92cb8a8 is not None:
                    yield meadow_Xref(meadow_src_92cb8a8, _name_boundary.attributes(meadow_entry_local_8e60148.parsed_key)['index'], meadow_entry_local_8e60148.value)
                else:
                    yield meadow_Xref(_name_boundary.attributes(meadow_entry_local_8e60148.parsed_key)['index'], meadow_dst_4d8d15a, meadow_entry_local_8e60148.value)
    except KeyError:
        return

@_name_boundary.callable_contract({'db': 'meadow_db_feda48e', 'ea': 'meadow_ea_fcb7c4a', 'types': 'meadow_types_4934b9b'}, 'get_crefs_to')
def meadow_get_crefs_to(meadow_db_feda48e, meadow_ea_fcb7c4a, meadow_types_4934b9b=None):
    """
    fetches the code references to the given address.

    Args:
      db (idb.IDB): the database.
      ea (int): the effective address from which to fetch xrefs.
      types (collection of int): if provided, a whitelist collection of xref types to include.

    Yields:
      int: xref address.
    """
    return meadow__get_xrefs(meadow_db_feda48e, dst=meadow_ea_fcb7c4a, tag='X', types=meadow_types_4934b9b)

@_name_boundary.callable_contract({'db': 'meadow_db_12027f1', 'ea': 'meadow_ea_a889fce', 'types': 'meadow_types_be40de0'}, 'get_crefs_from')
def meadow_get_crefs_from(meadow_db_12027f1, meadow_ea_a889fce, meadow_types_be40de0=None):
    """
    fetches the code references from the given address.

    Args:
      db (idb.IDB): the database.
      ea (int): the effective address from which to fetch xrefs.
      types (collection of int): if provided, a whitelist collection of xref types to include.

    Yields:
      int: xref address.
    """
    return meadow__get_xrefs(meadow_db_12027f1, src=meadow_ea_a889fce, tag='x', types=meadow_types_be40de0)

@_name_boundary.callable_contract({'db': 'meadow_db_dd555bc', 'ea': 'meadow_ea_8556195', 'types': 'meadow_types_14e452e'}, 'get_drefs_to')
def meadow_get_drefs_to(meadow_db_dd555bc, meadow_ea_8556195, meadow_types_14e452e=None):
    """
    fetches the data references to the given address.

    Args:
      db (idb.IDB): the database.
      ea (int): the effective address from which to fetch xrefs.
      types (collection of int): if provided, a whitelist collection of xref types to include.

    Yields:
      int: xref address.
    """
    return meadow__get_xrefs(meadow_db_dd555bc, dst=meadow_ea_8556195, tag='D', types=meadow_types_14e452e)

@_name_boundary.callable_contract({'db': 'meadow_db_0356a84', 'ea': 'meadow_ea_19a8ce9', 'types': 'meadow_types_89a7b54'}, 'get_drefs_from')
def meadow_get_drefs_from(meadow_db_0356a84, meadow_ea_19a8ce9, meadow_types_89a7b54=None):
    """
    fetches the data references from the given address.

    Args:
      db (idb.IDB): the database.
      ea (int): the effective address from which to fetch xrefs.
      types (collection of int): if provided, a whitelist collection of xref types to include.

    Yields:
      int: xref address.
    """
    return meadow__get_xrefs(meadow_db_0356a84, src=meadow_ea_19a8ce9, tag='d', types=meadow_types_89a7b54)

class meadow_Fixup(meadow_vstruct.VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_2bda63a', 'wordsize': 'meadow_wordsize_local_14cc86f'}, '__init__')
    def __init__(meadow_self_2bda63a, meadow_wordsize_local_14cc86f):
        meadow_vstruct.VStruct.__init__(meadow_self_2bda63a)
        meadow_self_2bda63a.type = v_uint8()
        meadow_self_2bda63a.unk01 = v_uint16()
        if meadow_wordsize_local_14cc86f == 4:
            meadow_self_2bda63a.offset = v_uint32()
            meadow_self_2bda63a.unk07 = v_uint32()
        elif meadow_wordsize_local_14cc86f == 8:
            meadow_self_2bda63a.unk03 = v_uint32()
            meadow_self_2bda63a.unk07 = v_uint16()
            meadow_self_2bda63a.offset = v_uint64()
        else:
            raise ValueError('unexpected wordsize')

    @_name_boundary.callable_contract({'self': 'meadow_self_c612257'}, 'pcb_type')
    def pcb_type(meadow_self_c612257):
        if meadow_self_c612257.type != 4:
            raise NotImplementedError('fixup type %x not yet supported' % meadow_self_c612257.type)

    @_name_boundary.callable_contract({'self': 'meadow_self_2639b26'}, 'get_fixup_length')
    def meadow_get_fixup_length(meadow_self_2639b26):
        if meadow_self_2639b26.type == 4:
            return 4
        else:
            raise NotImplementedError('fixup type %x not yet supported' % meadow_self_2639b26.type)
    get_fixup_length = meadow_get_fixup_length

@_name_boundary.class_contract('FixupV70', {'get_fixup_length': 'meadow_get_fixup_length', 'unk1': 'meadow_unk1', 'unk2': 'meadow_unk2'})
class meadow_FixupV70:

    @_name_boundary.callable_contract({'self': 'meadow_self_b9cbdf7', 'buf': 'meadow_buf_local_ec45584', 'wordsize': 'meadow_wordsize_local_0ba5070'}, '__init__')
    def __init__(meadow_self_b9cbdf7, meadow_buf_local_ec45584, meadow_wordsize_local_0ba5070):
        meadow_self_b9cbdf7.buf = meadow_buf_local_ec45584
        meadow_u_88000a2 = meadow_Unpacker(meadow_buf_local_ec45584, wordsize=meadow_wordsize_local_0ba5070)
        meadow_self_b9cbdf7.type = _name_boundary.attributes(meadow_u_88000a2)['dw']()
        _name_boundary.attributes(meadow_self_b9cbdf7)['unk1'] = _name_boundary.attributes(meadow_u_88000a2)['dd']()
        _name_boundary.attributes(meadow_self_b9cbdf7)['unk2'] = _name_boundary.attributes(meadow_u_88000a2)['addr']()
        meadow_self_b9cbdf7.offset = _name_boundary.attributes(meadow_u_88000a2)['dd']()
        if meadow_self_b9cbdf7.type != 8:
            raise NotImplementedError('fixup type %x not yet supported' % meadow_self_b9cbdf7.type)

    @_name_boundary.callable_contract({'self': 'meadow_self_99a7cdf'}, 'get_fixup_length')
    def meadow_get_fixup_length(meadow_self_99a7cdf):
        if meadow_self_99a7cdf.type == 8:
            return 4
        else:
            raise NotImplementedError('fixup type %x not yet supported' % meadow_self_99a7cdf.type)
meadow_Fixups = meadow_Analysis('$ fixups', [meadow_Field('fixups', 'S', meadow_ADDRESSES, meadow_as_cast(meadow_Fixup)), meadow_Field('fixups', 'S', meadow_ADDRESSES, meadow_FixupV70, minver=700)])

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_02026c6', 'wordsize': 'meadow_wordsize_local_9b75e28'}, 'parse_seg_strings')
def meadow_parse_seg_strings(meadow_buf_local_02026c6, meadow_wordsize_local_9b75e28=None):
    meadow_strings_c40b10f = []
    meadow_offset_local_db13c92 = 0
    while meadow_offset_local_db13c92 < len(meadow_buf_local_02026c6):
        if meadow_buf_local_02026c6[meadow_offset_local_db13c92] == 0:
            break
        meadow_string_local_6018195 = meadow_PString(length_is_total=False)
        meadow_string_local_6018195.vsParse(meadow_buf_local_02026c6, offset=meadow_offset_local_db13c92)
        meadow_offset_local_db13c92 += len(meadow_string_local_6018195)
        meadow_strings_c40b10f.append(meadow_string_local_6018195.s)
    return meadow_strings_c40b10f
meadow_SegStrings = meadow_Analysis('$ segstrings', [meadow_Field('strings', 'S', 0, meadow_parse_seg_strings)])

@_name_boundary.class_contract('Seg', {'startEA': 'meadow_startEA', 'endEA': 'meadow_endEA', 'name_index': 'meadow_name_index', 'orgbase': 'meadow_orgbase', 'align': 'meadow_align', 'comb': 'meadow_comb', 'perm': 'meadow_perm', 'bitness': 'meadow_bitness', 'sel': 'meadow_sel', 'defsr': 'meadow_defsr', 'color': 'meadow_color'})
class meadow_Seg:

    @_name_boundary.callable_contract({'self': 'meadow_self_125d1c9', 'buf': 'meadow_buf_local_98e8290', 'wordsize': 'meadow_wordsize_local_65295ba'}, '__init__')
    def __init__(meadow_self_125d1c9, meadow_buf_local_98e8290, meadow_wordsize_local_65295ba):
        meadow_self_125d1c9.buf = meadow_buf_local_98e8290
        meadow_u_0302457 = meadow_Unpacker(meadow_buf_local_98e8290, wordsize=meadow_wordsize_local_65295ba)
        _name_boundary.attributes(meadow_self_125d1c9)['startEA'] = _name_boundary.attributes(meadow_u_0302457)['addr']()
        _name_boundary.attributes(meadow_self_125d1c9)['endEA'] = _name_boundary.attributes(meadow_self_125d1c9)['startEA'] + _name_boundary.attributes(meadow_u_0302457)['addr']()
        _name_boundary.attributes(meadow_self_125d1c9)['name_index'] = _name_boundary.attributes(meadow_u_0302457)['addr']()
        meadow_self_125d1c9.sclass = _name_boundary.attributes(meadow_u_0302457)['addr']()
        _name_boundary.attributes(meadow_self_125d1c9)['orgbase'] = _name_boundary.attributes(meadow_u_0302457)['addr']()
        meadow_self_125d1c9.flags = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['align'] = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['comb'] = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['perm'] = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['bitness'] = _name_boundary.attributes(meadow_u_0302457)['dd']()
        meadow_self_125d1c9.type = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['sel'] = _name_boundary.attributes(meadow_u_0302457)['dd']()
        _name_boundary.attributes(meadow_self_125d1c9)['defsr'] = NotImplementedError()
        _name_boundary.attributes(meadow_self_125d1c9)['color'] = _name_boundary.attributes(meadow_u_0302457)['dd']() - 1 & 4294967295
meadow_Segments = meadow_Analysis('$ segs', [meadow_Field('segments', 'S', meadow_ALL, meadow_Seg)])
meadow_Imports = meadow_Analysis('$ imports', [meadow_Field('lib_netnodes', 'A', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_uint), meadow_Field('lib_names', 'S', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_string)])
meadow_Import = _name_boundary.named_record('Import', ['library', 'function_name', 'function_address'])

@_name_boundary.callable_contract({'db': 'meadow_db_ad76cc9'}, 'enumerate_imports')
def meadow_enumerate_imports(meadow_db_ad76cc9):
    """
    enumerate the functions imported by the module in the given database.

    yields:
      Tuple[str, str, int]: library name, function name, function address
    """
    meadow_imps_033e7c4 = meadow_Imports(meadow_db_ad76cc9)
    for meadow_index_d960d0d, meadow_libname_9199686 in meadow_imps_033e7c4.lib_names.items():
        if meadow_index_d960d0d == 4294967295:
            continue
        meadow_nnref_afbff9c = meadow_imps_033e7c4.lib_netnodes[meadow_index_d960d0d]
        meadow_nn_4949efe = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_ad76cc9, meadow_nnref_afbff9c)
        for meadow_funcaddr_b939528 in _name_boundary.attributes(meadow_nn_4949efe)['sups']():
            try:
                meadow_funcname_a61081b = _name_boundary.attributes(meadow_nn_4949efe)['supstr'](meadow_funcaddr_b939528)
                yield meadow_Import(meadow_libname_9199686, meadow_funcname_a61081b, meadow_funcaddr_b939528)
            except KeyError:
                meadow_logger.warning('failed to find import supval: %x', meadow_funcaddr_b939528)
                continue
meadow_EntryPoints = meadow_Analysis('$ entry points', [meadow_Field('functions', 'A', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_uint), meadow_Field('main_entry', 'A', meadow_ADDRESSES, _name_boundary.attributes(meadow_idb)['netnode'].as_uint), meadow_Field('ordinals', 'I', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_uint), meadow_Field('forwarded_symbols', 'F', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_string), meadow_Field('function_names', 'S', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_string), meadow_Field('main_entry_name', 'S', meadow_ADDRESSES, _name_boundary.attributes(meadow_idb)['netnode'].as_string)])
meadow_EntryPoint = _name_boundary.named_record('EntryPoint', ['name', 'address', 'ordinal', 'forwarded_symbol'])

@_name_boundary.callable_contract({'db': 'meadow_db_8e90a7e'}, 'enumerate_entrypoints')
def meadow_enumerate_entrypoints(meadow_db_8e90a7e):
    """
    enumerate the entry point functions in the given database.

    yields:
      Tuple[str, int, int, str]: function name, address, ordinal (optional), and forwarded symbol (optional)
    """
    meadow_ents_699e68d = meadow_EntryPoints(meadow_db_8e90a7e)
    meadow_ordinals_d166d92 = meadow_ents_699e68d.ordinals
    meadow_forwarded_symbols_d871841 = meadow_ents_699e68d.forwarded_symbols
    meadow_names_794952f = meadow_ents_699e68d.function_names
    meadow_names_794952f.update(meadow_ents_699e68d.main_entry_name)
    for meadow_index_e681ad4, meadow_addr_c76f0c3 in meadow_ents_699e68d.functions.items():
        if meadow_index_e681ad4 == meadow_db_8e90a7e.uint(-1):
            break
        yield meadow_EntryPoint(_name_boundary.attributes(meadow_names_794952f)['get'](meadow_index_e681ad4), meadow_addr_c76f0c3, _name_boundary.attributes(meadow_ordinals_d166d92)['get'](meadow_index_e681ad4), _name_boundary.attributes(meadow_forwarded_symbols_d871841)['get'](meadow_index_e681ad4))
    for meadow_index_e681ad4, meadow_addr_c76f0c3 in meadow_ents_699e68d.main_entry.items():
        yield meadow_EntryPoint(_name_boundary.attributes(meadow_names_794952f)['get'](meadow_index_e681ad4), meadow_addr_c76f0c3, _name_boundary.attributes(meadow_ordinals_d166d92)['get'](meadow_index_e681ad4), _name_boundary.attributes(meadow_forwarded_symbols_d871841)['get'](meadow_index_e681ad4))
meadow_ScriptSnippets = meadow_Analysis('$ scriptsnippets', [meadow_Field('tabsize', 'Y', 0, _name_boundary.attributes(meadow_idb)['netnode'].as_uint), meadow_Field('scripts', 'A', meadow_NUMBERS, _name_boundary.attributes(meadow_idb)['netnode'].as_uint)])
meadow_ScriptSnippet = _name_boundary.named_record('ScriptSnippet', ['name', 'language', 'code'])

@_name_boundary.callable_contract({'db': 'meadow_db_adc9134'}, 'enumerate_script_snippets')
def meadow_enumerate_script_snippets(meadow_db_adc9134):
    """
    enumerate script snippets stored in the given database.

    yields:
      Tuple[str, str, str]: filename, language (Python or IDC), and source code
    """
    meadow_scripts_4d27312 = meadow_ScriptSnippets(meadow_db_adc9134)
    for meadow_nnid_986cb48 in meadow_scripts_4d27312.scripts.values():
        meadow_nn_5693c4d = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](meadow_db_adc9134, meadow_nnid_986cb48 - 1)
        meadow_name_local_9d2767b = _name_boundary.attributes(meadow_nn_5693c4d)['supstr'](0, tag='S')
        meadow_language_55d5b4c = _name_boundary.attributes(meadow_nn_5693c4d)['supstr'](1, tag='S')
        meadow_code_12a04e4 = _name_boundary.attributes(meadow_nn_5693c4d)['supstr'](0, tag='X')
        yield meadow_ScriptSnippet(meadow_name_local_9d2767b, meadow_language_55d5b4c, meadow_code_12a04e4)
_name_boundary.module_contract(globals(), {'as_sha256': 'meadow_as_sha256', 'User': 'meadow_User', 'VARIABLE_INDEXES': 'meadow_VARIABLE_INDEXES', 'TypeString': 'meadow_TypeString', 'ALL': 'meadow_ALL', 'Imports': 'meadow_Imports', 'logger': 'meadow_logger', 'as_cast': 'meadow_as_cast', 'Struct': 'meadow_Struct', 'SegStrings': 'meadow_SegStrings', 'Import': 'meadow_Import', 'Field': 'meadow_Field', 'Fixup': 'meadow_Fixup', 'get_drefs_to': 'meadow_get_drefs_to', 'types': 'meadow_types', 'OriginalUser': 'meadow_OriginalUser', 'enumerate_script_snippets': 'meadow_enumerate_script_snippets', 'as_unix_timestamp': 'meadow_as_unix_timestamp', 'ScriptSnippets': 'meadow_ScriptSnippets', 'name_generator': 'meadow_name_generator', '_counter': 'meadow__counter', 'Fixups': 'meadow_Fixups', '_get_xrefs': 'meadow__get_xrefs', 'StructMember': 'meadow_StructMember', 'idb': 'meadow_idb', 'STRUCT_FLAGS': 'meadow_STRUCT_FLAGS', 'pairs': 'meadow_pairs', 'EntryPoint': 'meadow_EntryPoint', 'cast': 'meadow_cast', 'Root': 'meadow_Root', 'PString': 'meadow_PString', 'Chunk': 'meadow_Chunk', 'binascii': 'meadow_binascii', 'ScriptSnippet': 'meadow_ScriptSnippet', 'namedtuple': 'meadow_namedtuple', 'unpack_dq': 'meadow_unpack_dq', 'NODES': 'meadow_NODES', 'Counter': 'meadow_Counter', 'vstruct': 'meadow_vstruct', 'FileRegions': 'meadow_FileRegions', 'chunks': 'meadow_chunks', 'datetime': 'meadow_datetime', 'FixupV70': 'meadow_FixupV70', 'Xref': 'meadow_Xref', 'unpack_dqs': 'meadow_unpack_dqs', 'get_crefs_to': 'meadow_get_crefs_to', 'is_flag_set': 'meadow_is_flag_set', 'EntryPoints': 'meadow_EntryPoints', 'FunctionParameter': 'meadow_FunctionParameter', 'func_t': 'meadow_func_t', 'Seg': 'meadow_Seg', 'randint': 'meadow_randint', 'FunctionSignature': 'meadow_FunctionSignature', 'six': 'meadow_six', 'create_pstring_list': 'meadow_create_pstring_list', 'NUMBERS': 'meadow_NUMBERS', 'Segments': 'meadow_Segments', 'StackChangePoint': 'meadow_StackChangePoint', 'unpack_dw': 'meadow_unpack_dw', 'enumerate_imports': 'meadow_enumerate_imports', 'ADDRESSES': 'meadow_ADDRESSES', 'get_crefs_from': 'meadow_get_crefs_from', 'Functions': 'meadow_Functions', 'IdaInfo': 'meadow_IdaInfo', 'unpack_dds': 'meadow_unpack_dds', 'itertools': 'meadow_itertools', 'parse_seg_strings': 'meadow_parse_seg_strings', 'unpack_dd': 'meadow_unpack_dd', 'Reader': 'meadow_Reader', 'get_drefs_from': 'meadow_get_drefs_from', 'enumerate_entrypoints': 'meadow_enumerate_entrypoints', 'Loader': 'meadow_Loader', 'Unpacker': 'meadow_Unpacker', 'FileRegion': 'meadow_FileRegion', 'FileRegionV70': 'meadow_FileRegionV70', 'as_md5': 'meadow_as_md5', 'logging': 'meadow_logging', 'Analysis': 'meadow_Analysis', '_Analysis': 'meadow__Analysis', 'IndexType': 'meadow_IndexType', 'Function': 'meadow_Function'})
