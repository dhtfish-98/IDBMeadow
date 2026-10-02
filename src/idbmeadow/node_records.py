# Derived from idb/netnode.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import struct as meadow_struct
import logging as meadow_logging
from collections import namedtuple as meadow_namedtuple
import six as meadow_six
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'i': 'meadow_i_a82d741'}, 'uint32')
def meadow_uint32(meadow_i_a82d741):
    """
    Convert the given signed number into its 32-bit little endian unsigned number value.

    Example::

        assert uint32(-1) == 0xFFFFFFFF


    Example::

        assert uint32(1) == 1
    """
    return _name_boundary.attributes(meadow_struct)['unpack']('>I', _name_boundary.attributes(meadow_struct)['pack']('>i', meadow_i_a82d741))[0]

@_name_boundary.callable_contract({'i': 'meadow_i_d637926'}, 'uint64')
def meadow_uint64(meadow_i_d637926):
    """
    Convert the given signed number into its 64-bit little endian unsigned number value.

    Example::

        assert uint64(-1) == 0xFFFFFFFFFFFFFFFF


    Example::

        assert uint64(1) == 1
    """
    return _name_boundary.attributes(meadow_struct)['unpack']('>Q', _name_boundary.attributes(meadow_struct)['pack']('>q', meadow_i_d637926))[0]

@_name_boundary.class_contract('TAGS', {'ALTVAL': 'meadow_ALTVAL', 'SUPVAL': 'meadow_SUPVAL', 'CHARVAL': 'meadow_CHARVAL', 'HASHVAL': 'meadow_HASHVAL', 'VALUE': 'meadow_VALUE', 'NAME': 'meadow_NAME', 'LINK': 'meadow_LINK'})
class meadow_TAGS:
    """
    via: https://www.hex-rays.com/products/ida/support/sdkdoc/group__nn__res.html#gaedcc558fe55e19ebc6e304ba7ad8c4d6
    """
    meadow_ALTVAL = 'A'
    meadow_SUPVAL = 'S'
    meadow_CHARVAL = 'C'
    meadow_HASHVAL = 'H'
    meadow_VALUE = 'V'
    meadow_NAME = 'N'
    meadow_LINK = 'L'

@_name_boundary.callable_contract({'nodeid': 'meadow_nodeid_efa030a', 'index': 'meadow_index_1829289', 'tag': 'meadow_tag_local_62b181f', 'wordsize': 'meadow_wordsize_local_69dced3'}, 'make_key')
def meadow_make_key(meadow_nodeid_efa030a, meadow_tag_local_62b181f=None, meadow_index_1829289=None, meadow_wordsize_local_69dced3=4):
    """

    Example::

        k = make_key('Root Node')


    Example::

        k = make_key(0x401000, 'X')

    Example::

        k = make_key(0x401000, 'X', 0x4010A24)
    """
    if meadow_wordsize_local_69dced3 == 4:
        meadow_wordformat_9434ff4 = 'I'
    elif meadow_wordsize_local_69dced3 == 8:
        meadow_wordformat_9434ff4 = 'Q'
    else:
        raise ValueError('unexpected wordsize')
    if isinstance(meadow_nodeid_efa030a, meadow_six.string_types):
        return b'N' + meadow_nodeid_efa030a.encode('utf-8')
    elif isinstance(meadow_nodeid_efa030a, meadow_six.integer_types):
        if meadow_tag_local_62b181f is None:
            raise ValueError('tag required')
        if not isinstance(meadow_tag_local_62b181f, str):
            raise ValueError('tag must be a string')
        if len(meadow_tag_local_62b181f) != 1:
            raise ValueError('tag must be a single character string')
        meadow_tag_local_62b181f = meadow_tag_local_62b181f.encode('ascii')
        if meadow_index_1829289 is None:
            return b'.' + _name_boundary.attributes(meadow_struct)['pack']('>' + meadow_wordformat_9434ff4 + 'c', meadow_nodeid_efa030a, meadow_tag_local_62b181f)
        elif meadow_index_1829289 < 0:
            return b'.' + _name_boundary.attributes(meadow_struct)['pack']('>' + meadow_wordformat_9434ff4 + 'c' + meadow_wordformat_9434ff4.lower(), meadow_nodeid_efa030a, meadow_tag_local_62b181f, meadow_index_1829289)
        else:
            return b'.' + _name_boundary.attributes(meadow_struct)['pack']('>' + meadow_wordformat_9434ff4 + 'c' + meadow_wordformat_9434ff4, meadow_nodeid_efa030a, meadow_tag_local_62b181f, meadow_index_1829289)
    else:
        raise ValueError('unexpected type of nodeid: ' + str(type(meadow_nodeid_efa030a)))
meadow_ComplexKey = _name_boundary.named_record('ComplexKey', ['nodeid', 'tag', 'index'])
meadow_TAG_LENGTH = 1
meadow_KEY_HEADER_LENGTH = 1

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_c1f31f4', 'wordsize': 'meadow_wordsize_local_bddd541'}, 'parse_key')
def meadow_parse_key(meadow_buf_local_c1f31f4, meadow_wordsize_local_bddd541=4):
    if meadow_six.indexbytes(meadow_buf_local_c1f31f4, 0) != 46:
        raise ValueError('buf is not a complex key')
    if meadow_wordsize_local_bddd541 == 4:
        meadow_wordformat_74296dc = 'I'
    elif meadow_wordsize_local_bddd541 == 8:
        meadow_wordformat_74296dc = 'Q'
    else:
        raise ValueError('unexpected wordsize')
    meadow_nodeid_f9b261d, meadow_tag_local_618d5e1 = meadow_struct.unpack_from('>' + meadow_wordformat_74296dc + 'c', meadow_buf_local_c1f31f4, 1)
    meadow_tag_local_618d5e1 = meadow_tag_local_618d5e1.decode('ascii')
    if len(meadow_buf_local_c1f31f4) >= meadow_TAG_LENGTH + 2 * meadow_wordsize_local_bddd541 + meadow_KEY_HEADER_LENGTH:
        meadow_offset_local_b99ee0d = meadow_TAG_LENGTH + meadow_KEY_HEADER_LENGTH + meadow_wordsize_local_bddd541
        meadow_index_f5f1e52 = meadow_struct.unpack_from('>' + meadow_wordformat_74296dc, meadow_buf_local_c1f31f4, meadow_offset_local_b99ee0d)[0]
    else:
        meadow_index_f5f1e52 = None
    return meadow_ComplexKey(meadow_nodeid_f9b261d, meadow_tag_local_618d5e1, meadow_index_f5f1e52)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_2179751', 'wordsize': 'meadow_wordsize_local_e00ebde'}, 'as_uint')
def meadow_as_uint(meadow_buf_local_2179751, meadow_wordsize_local_e00ebde=None):
    if len(meadow_buf_local_2179751) == 1:
        return _name_boundary.attributes(meadow_struct)['unpack']('<B', meadow_buf_local_2179751)[0]
    elif len(meadow_buf_local_2179751) == 2:
        return _name_boundary.attributes(meadow_struct)['unpack']('<H', meadow_buf_local_2179751)[0]
    elif len(meadow_buf_local_2179751) == 4:
        return _name_boundary.attributes(meadow_struct)['unpack']('<L', meadow_buf_local_2179751)[0]
    elif len(meadow_buf_local_2179751) == 8:
        return _name_boundary.attributes(meadow_struct)['unpack']('<Q', meadow_buf_local_2179751)[0]
    else:
        return RuntimeError('unexpected buf size')

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_3f5580a', 'wordsize': 'meadow_wordsize_local_f33ffec'}, 'as_int')
def meadow_as_int(meadow_buf_local_3f5580a, meadow_wordsize_local_f33ffec=None):
    if len(meadow_buf_local_3f5580a) == 1:
        return _name_boundary.attributes(meadow_struct)['unpack']('<b', meadow_buf_local_3f5580a)[0]
    elif len(meadow_buf_local_3f5580a) == 2:
        return _name_boundary.attributes(meadow_struct)['unpack']('<h', meadow_buf_local_3f5580a)[0]
    elif len(meadow_buf_local_3f5580a) == 4:
        return _name_boundary.attributes(meadow_struct)['unpack']('<l', meadow_buf_local_3f5580a)[0]
    elif len(meadow_buf_local_3f5580a) == 8:
        return _name_boundary.attributes(meadow_struct)['unpack']('<q', meadow_buf_local_3f5580a)[0]
    else:
        return RuntimeError('unexpected buf size')

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_372be86', 'wordsize': 'meadow_wordsize_local_ee7583a'}, 'as_string')
def meadow_as_string(meadow_buf_local_372be86, meadow_wordsize_local_ee7583a=None):
    return bytes(meadow_buf_local_372be86).rstrip(b'\x00').decode('utf-8').rstrip('\x00')
meadow_Entry = _name_boundary.named_record('Entry', ['key', 'parsed_key', 'value'])

@_name_boundary.class_contract('Netnode', {'get_nodebase': 'meadow_get_nodebase', 'get_tag_entries': 'meadow_get_tag_entries', 'get_val': 'meadow_get_val', 'supval': 'meadow_supval', 'supstr': 'meadow_supstr', 'sups': 'meadow_sups', 'supentries': 'meadow_supentries', 'altval': 'meadow_altval', 'alts': 'meadow_alts', 'altentries': 'meadow_altentries', 'charval': 'meadow_charval', 'chars': 'meadow_chars', 'charentries': 'meadow_charentries', 'hashval': 'meadow_hashval', 'hashes': 'meadow_hashes', 'hashentries': 'meadow_hashentries', 'valobj': 'meadow_valobj', 'valstr': 'meadow_valstr', 'value_exists': 'meadow_value_exists', 'long_value': 'meadow_long_value', 'blobsize': 'meadow_blobsize', 'getblob': 'meadow_getblob', 'idb': 'meadow_idb', 'nodebase': 'meadow_nodebase', 'nodeid': 'meadow_nodeid'})
class meadow_Netnode(object):

    @_name_boundary.callable_contract({'self': 'meadow_self_66cbaf7', 'db': 'meadow_db_6d0b812', 'nodeid': 'meadow_nodeid_865e059'}, '__init__')
    def __init__(meadow_self_66cbaf7, meadow_db_6d0b812, meadow_nodeid_865e059):
        """
        Args:
          db (idb.IDB): the IDA Pro database.
          nodeid (Union[str, int]): the node id used to identify the netnode.


        Example::

            nn = Netnode("Root Node")
            print(nn.supval(1303))  # --> "6.95"

        Example::

            nn = Netnode(0x401000)
            for xref in nn.alts(tag='X'):
                print(xref)

        TODO: how to address the following keys:
          - $ MAX LINK
          - $ MAX NODE
          - $ MAX DESC

        these are unaddressable via IDA Pro netnodes, too.
        """
        _name_boundary.attributes(meadow_self_66cbaf7)['idb'] = meadow_db_6d0b812
        meadow_self_66cbaf7.wordsize = _name_boundary.attributes(meadow_self_66cbaf7)['idb'].wordsize
        if meadow_self_66cbaf7.wordsize == 4:
            _name_boundary.attributes(meadow_self_66cbaf7)['nodebase'] = 4278190080
        elif meadow_self_66cbaf7.wordsize == 8:
            _name_boundary.attributes(meadow_self_66cbaf7)['nodebase'] = 18374686479671623680
        else:
            raise RuntimeError('unexpected wordsize')
        if isinstance(meadow_nodeid_865e059, meadow_six.string_types):
            meadow_key_local_8bfdc9a = meadow_make_key(meadow_nodeid_865e059, wordsize=meadow_self_66cbaf7.wordsize)
            meadow_cursor_b3c500a = _name_boundary.attributes(_name_boundary.attributes(meadow_self_66cbaf7)['idb'].id0)['find'](meadow_key_local_8bfdc9a)
            _name_boundary.attributes(meadow_self_66cbaf7)['nodeid'] = meadow_as_uint(meadow_cursor_b3c500a.value)
            meadow_logger.info('resolved string netnode %s to %x', meadow_nodeid_865e059, _name_boundary.attributes(meadow_self_66cbaf7)['nodeid'])
        elif isinstance(meadow_nodeid_865e059, meadow_six.integer_types):
            _name_boundary.attributes(meadow_self_66cbaf7)['nodeid'] = meadow_nodeid_865e059
        else:
            raise ValueError('unexpected type for nodeid')

    @staticmethod
    @_name_boundary.callable_contract({'db': 'meadow_db_a054c44'}, 'get_nodebase')
    def meadow_get_nodebase(meadow_db_a054c44):
        if meadow_db_a054c44.wordsize == 4:
            return 4278190080
        elif meadow_db_a054c44.wordsize == 8:
            return 18374686479671623680

    @_name_boundary.callable_contract({'self': 'meadow_self_4840882'}, 'name')
    def name(meadow_self_4840882):
        """
        fetch the name associated with the netnode.
        basically supval(tag='N')

        Returns:
          str: the name stored in the netnode.

        Raises:
          KeyError: if the name for the netnode does not exist.
        """
        meadow_key_local_11b2bb0 = meadow_make_key(_name_boundary.attributes(meadow_self_4840882)['nodeid'], _name_boundary.attributes(meadow_TAGS)['NAME'], wordsize=meadow_self_4840882.wordsize)
        meadow_cursor_fd68959 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_4840882)['idb'].id0)['find'](meadow_key_local_11b2bb0)
        return meadow_as_string(meadow_cursor_fd68959.value)

    @_name_boundary.callable_contract({'self': 'meadow_self_e4a0b5f', 'tag': 'meadow_tag_local_b6aed96'}, 'get_tag_entries')
    def meadow_get_tag_entries(meadow_self_e4a0b5f, meadow_tag_local_b6aed96=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        """
        generate the entries for the given tag in this netnode.

        this replaces:
          - *1st
          - *nxt
          - *last
          - *prev

        Yields:
          Entry: an entry (with key and value) under the given tag in this netnode.
        """
        meadow_key_local_95d90e5 = meadow_make_key(_name_boundary.attributes(meadow_self_e4a0b5f)['nodeid'], meadow_tag_local_b6aed96, wordsize=meadow_self_e4a0b5f.wordsize)
        try:
            meadow_cursor_e264465 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_e4a0b5f)['idb'].id0)['find_prefix'](meadow_key_local_95d90e5)
        except KeyError:
            return
        while bytes(meadow_cursor_e264465.key).startswith(meadow_key_local_95d90e5):
            meadow_parsed_key_6a8560b = meadow_parse_key(meadow_cursor_e264465.key, wordsize=_name_boundary.attributes(meadow_self_e4a0b5f)['idb'].wordsize)
            yield meadow_Entry(meadow_cursor_e264465.key, meadow_parsed_key_6a8560b, bytes(meadow_cursor_e264465.value))
            try:
                _name_boundary.attributes(meadow_cursor_e264465)['next']()
            except IndexError:
                break

    @_name_boundary.callable_contract({'self': 'meadow_self_68925ad', 'index': 'meadow_index_cccbab2', 'tag': 'meadow_tag_local_e99fa4e'}, 'get_val')
    def meadow_get_val(meadow_self_68925ad, meadow_index_cccbab2, meadow_tag_local_e99fa4e=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        """
        fetch a sup/alt/hash/etc value from the netnode.
        the nodeid for this netnode must be an integer/effective address.

        Args:
          index (int): the index of the data to fetch.
          tag (str): single character tag.

        Returns:
          bytes: the raw data.
        """
        meadow_key_local_3ee6f66 = meadow_make_key(_name_boundary.attributes(meadow_self_68925ad)['nodeid'], meadow_tag_local_e99fa4e, meadow_index_cccbab2, wordsize=meadow_self_68925ad.wordsize)
        meadow_cursor_6682497 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_68925ad)['idb'].id0)['find'](meadow_key_local_3ee6f66)
        return bytes(meadow_cursor_6682497.value)

    @_name_boundary.callable_contract({'self': 'meadow_self_7db3df8', 'index': 'meadow_index_1811f7f', 'tag': 'meadow_tag_local_68195a1'}, 'supval')
    def meadow_supval(meadow_self_7db3df8, meadow_index_1811f7f, meadow_tag_local_68195a1=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        return _name_boundary.attributes(meadow_self_7db3df8)['get_val'](meadow_index_1811f7f, meadow_tag_local_68195a1)

    @_name_boundary.callable_contract({'self': 'meadow_self_3c87bfd', 'index': 'meadow_index_3a7ce5a', 'tag': 'meadow_tag_local_0e2fbc3'}, 'supstr')
    def meadow_supstr(meadow_self_3c87bfd, meadow_index_3a7ce5a, meadow_tag_local_0e2fbc3=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        return meadow_as_string(_name_boundary.attributes(meadow_self_3c87bfd)['supval'](meadow_index_3a7ce5a, meadow_tag_local_0e2fbc3))

    @_name_boundary.callable_contract({'self': 'meadow_self_f0905bf', 'tag': 'meadow_tag_local_22bd8fa'}, 'sups')
    def meadow_sups(meadow_self_f0905bf, meadow_tag_local_22bd8fa=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        """
        this replaces:
          - sup1st
          - supnxt
          - suplast
          - supprev
        """
        for meadow_entry_local_3f9aadd in _name_boundary.attributes(meadow_self_f0905bf)['get_tag_entries'](tag=meadow_tag_local_22bd8fa):
            yield _name_boundary.attributes(meadow_entry_local_3f9aadd.parsed_key)['index']

    @_name_boundary.callable_contract({'self': 'meadow_self_361ad3e', 'tag': 'meadow_tag_local_dfaec2a'}, 'supentries')
    def meadow_supentries(meadow_self_361ad3e, meadow_tag_local_dfaec2a=_name_boundary.attributes(meadow_TAGS)['SUPVAL']):
        for meadow_entry_local_133b106 in _name_boundary.attributes(meadow_self_361ad3e)['get_tag_entries'](tag=meadow_tag_local_dfaec2a):
            yield meadow_entry_local_133b106

    @_name_boundary.callable_contract({'self': 'meadow_self_962e982', 'index': 'meadow_index_ed79c5e', 'tag': 'meadow_tag_local_affae70'}, 'altval')
    def meadow_altval(meadow_self_962e982, meadow_index_ed79c5e, meadow_tag_local_affae70=_name_boundary.attributes(meadow_TAGS)['ALTVAL']):
        return meadow_as_int(_name_boundary.attributes(meadow_self_962e982)['get_val'](meadow_index_ed79c5e, meadow_tag_local_affae70))

    @_name_boundary.callable_contract({'self': 'meadow_self_6a01b69', 'tag': 'meadow_tag_local_b55b282'}, 'alts')
    def meadow_alts(meadow_self_6a01b69, meadow_tag_local_b55b282=_name_boundary.attributes(meadow_TAGS)['ALTVAL']):
        """
        this replaces:
          - alt1st
          - altnxt
          - altlast
          - altprev
        """
        for meadow_entry_local_468bc36 in _name_boundary.attributes(meadow_self_6a01b69)['get_tag_entries'](tag=meadow_tag_local_b55b282):
            yield _name_boundary.attributes(meadow_entry_local_468bc36.parsed_key)['index']

    @_name_boundary.callable_contract({'self': 'meadow_self_813ec09', 'tag': 'meadow_tag_local_f1bda1b'}, 'altentries')
    def meadow_altentries(meadow_self_813ec09, meadow_tag_local_f1bda1b=_name_boundary.attributes(meadow_TAGS)['ALTVAL']):
        for meadow_entry_local_82a3346 in _name_boundary.attributes(meadow_self_813ec09)['get_tag_entries'](tag=meadow_tag_local_f1bda1b):
            yield meadow_entry_local_82a3346

    @_name_boundary.callable_contract({'self': 'meadow_self_14b6ace', 'index': 'meadow_index_28a39f8', 'tag': 'meadow_tag_local_74a0736'}, 'charval')
    def meadow_charval(meadow_self_14b6ace, meadow_index_28a39f8, meadow_tag_local_74a0736=_name_boundary.attributes(meadow_TAGS)['CHARVAL']):
        return meadow_as_int(_name_boundary.attributes(meadow_self_14b6ace)['get_val'](meadow_index_28a39f8, meadow_tag_local_74a0736))

    @_name_boundary.callable_contract({'self': 'meadow_self_6b48322', 'tag': 'meadow_tag_local_adf86e9'}, 'chars')
    def meadow_chars(meadow_self_6b48322, meadow_tag_local_adf86e9=_name_boundary.attributes(meadow_TAGS)['ALTVAL']):
        """
        this replaces:
          - char1st
          - charnxt
          - charlast
          - charprev
        """
        for meadow_entry_local_b0a7698 in _name_boundary.attributes(meadow_self_6b48322)['get_tag_entries'](tag=meadow_tag_local_adf86e9):
            yield _name_boundary.attributes(meadow_entry_local_b0a7698.parsed_key)['index']

    @_name_boundary.callable_contract({'self': 'meadow_self_c90af51', 'tag': 'meadow_tag_local_d4807b4'}, 'charentries')
    def meadow_charentries(meadow_self_c90af51, meadow_tag_local_d4807b4=_name_boundary.attributes(meadow_TAGS)['CHARVAL']):
        for meadow_entry_local_325f3cc in _name_boundary.attributes(meadow_self_c90af51)['get_tag_entries'](tag=meadow_tag_local_d4807b4):
            yield meadow_Entry(meadow_entry_local_325f3cc.key, meadow_entry_local_325f3cc.parsed_key, meadow_as_int(meadow_entry_local_325f3cc.value))

    @_name_boundary.callable_contract({'self': 'meadow_self_c1cdd07', 'index': 'meadow_index_26af828', 'tag': 'meadow_tag_local_083c67b'}, 'hashval')
    def meadow_hashval(meadow_self_c1cdd07, meadow_index_26af828, meadow_tag_local_083c67b=_name_boundary.attributes(meadow_TAGS)['HASHVAL']):
        """
        TODO: how is this different from a supval?
        """
        return _name_boundary.attributes(meadow_self_c1cdd07)['get_val'](meadow_index_26af828, meadow_tag_local_083c67b)

    @_name_boundary.callable_contract({'self': 'meadow_self_f4c6376', 'tag': 'meadow_tag_local_5134394'}, 'hashes')
    def meadow_hashes(meadow_self_f4c6376, meadow_tag_local_5134394=_name_boundary.attributes(meadow_TAGS)['HASHVAL']):
        """
        this replaces:
          - hash1st
          - hashnxt
          - hashlast
          - hashprev
        """
        for meadow_entry_local_7e07d0e in _name_boundary.attributes(meadow_self_f4c6376)['get_tag_entries'](tag=meadow_tag_local_5134394):
            yield _name_boundary.attributes(meadow_entry_local_7e07d0e.parsed_key)['index']

    @_name_boundary.callable_contract({'self': 'meadow_self_d06e875', 'tag': 'meadow_tag_local_ee0029b'}, 'hashentries')
    def meadow_hashentries(meadow_self_d06e875, meadow_tag_local_ee0029b=_name_boundary.attributes(meadow_TAGS)['HASHVAL']):
        for meadow_entry_local_1c8f6af in _name_boundary.attributes(meadow_self_d06e875)['get_tag_entries'](tag=meadow_tag_local_ee0029b):
            yield meadow_entry_local_1c8f6af

    @_name_boundary.callable_contract({'self': 'meadow_self_a46e7ca'}, 'valobj')
    def meadow_valobj(meadow_self_a46e7ca):
        """
        fetch the default netnode value.
        this is basically supval(tag='V').
        """
        meadow_key_local_cc3a22e = meadow_make_key(_name_boundary.attributes(meadow_self_a46e7ca)['nodeid'], _name_boundary.attributes(meadow_TAGS)['VALUE'], wordsize=meadow_self_a46e7ca.wordsize)
        meadow_cursor_29eb24e = _name_boundary.attributes(_name_boundary.attributes(meadow_self_a46e7ca)['idb'].id0)['find'](meadow_key_local_cc3a22e)
        return bytes(meadow_cursor_29eb24e.value)

    @_name_boundary.callable_contract({'self': 'meadow_self_3a34aaf'}, 'valstr')
    def meadow_valstr(meadow_self_3a34aaf):
        return meadow_as_string(_name_boundary.attributes(meadow_self_3a34aaf)['valobj']())

    @_name_boundary.callable_contract({'self': 'meadow_self_56e503a'}, 'value_exists')
    def meadow_value_exists(meadow_self_56e503a):
        try:
            return _name_boundary.attributes(meadow_self_56e503a)['valobj']() is not None
        except KeyError:
            return False

    @_name_boundary.callable_contract({'self': 'meadow_self_65b50e6'}, 'long_value')
    def meadow_long_value(meadow_self_65b50e6):
        return meadow_as_uint(_name_boundary.attributes(meadow_self_65b50e6)['valobj']())

    @_name_boundary.callable_contract({'self': 'meadow_self_8ac02fe'}, 'blobsize')
    def meadow_blobsize(meadow_self_8ac02fe):
        """
        TODO: how is this arbitrary data stored?
        """
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_f2c1641'}, 'getblob')
    def meadow_getblob(meadow_self_f2c1641):
        raise NotImplementedError()
_name_boundary.module_contract(globals(), {'ComplexKey': 'meadow_ComplexKey', 'parse_key': 'meadow_parse_key', 'namedtuple': 'meadow_namedtuple', 'Entry': 'meadow_Entry', 'Netnode': 'meadow_Netnode', 'uint32': 'meadow_uint32', 'uint64': 'meadow_uint64', 'TAGS': 'meadow_TAGS', 'as_uint': 'meadow_as_uint', 'as_string': 'meadow_as_string', 'make_key': 'meadow_make_key', 'TAG_LENGTH': 'meadow_TAG_LENGTH', 'as_int': 'meadow_as_int', 'six': 'meadow_six', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'KEY_HEADER_LENGTH': 'meadow_KEY_HEADER_LENGTH', 'struct': 'meadow_struct'})
