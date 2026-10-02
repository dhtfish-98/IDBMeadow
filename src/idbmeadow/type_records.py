# Derived from idb/typeinf.py; original copyright and license retained in ORIGIN.md.
"""
migrate from ida sdk and https://github.com/aerosoul94/tilutil
"""
import idbmeadow.api_contract as _name_boundary
import zlib as meadow_zlib
from abc import ABCMeta as meadow_ABCMeta, abstractmethod as meadow_abstractmethod
from vstruct import VStruct as meadow_VStruct
from cached_property import cached_property as meadow_cached_property
from vstruct.primitives import *
from idbmeadow.type_codes import *

class meadow_TypeString:

    @_name_boundary.callable_contract({'self': 'meadow_self_f1e67d0', 'buf': 'meadow_buf_local_1d9a496', 'pos': 'meadow_pos_local_695fb41', 'parent': 'meadow_parent_local_0634426'}, '__init__')
    def __init__(meadow_self_f1e67d0, meadow_buf_local_1d9a496, meadow_pos_local_695fb41=0, meadow_parent_local_0634426=None):
        meadow_self_f1e67d0.buf = meadow_buf_local_1d9a496
        meadow_self_f1e67d0.pos = meadow_pos_local_695fb41
        meadow_self_f1e67d0.parent = meadow_parent_local_0634426

    @_name_boundary.callable_contract({'self': 'meadow_self_a18460d', 'n': 'meadow_n_0c4face'}, 'seek')
    def meadow_seek(meadow_self_a18460d, meadow_n_0c4face):
        meadow_self_a18460d.pos += meadow_n_0c4face
        if meadow_self_a18460d.parent is not None:
            _name_boundary.attributes(meadow_self_a18460d.parent)['seek'](meadow_n_0c4face)
        if meadow_self_a18460d.pos > len(meadow_self_a18460d.buf) or meadow_self_a18460d.pos < 0:
            raise OverflowError('at offset {}'.format(meadow_self_a18460d.pos))

    @_name_boundary.callable_contract({'self': 'meadow_self_001f1d4', 'n': 'meadow_n_d2d4486'}, 'read')
    def meadow_read(meadow_self_001f1d4, meadow_n_d2d4486):
        meadow_val_local_3cc4438 = meadow_self_001f1d4.buf[meadow_self_001f1d4.pos:meadow_self_001f1d4.pos + meadow_n_d2d4486]
        _name_boundary.attributes(meadow_self_001f1d4)['seek'](meadow_n_d2d4486)
        return meadow_val_local_3cc4438

    @_name_boundary.callable_contract({'self': 'meadow_self_ba4d316', 'unpack_fn': 'meadow_unpack_fn_6324a19', 'size': 'meadow_size_local_daf47bc'}, 'unpack')
    def meadow_unpack(meadow_self_ba4d316, meadow_unpack_fn_6324a19, meadow_size_local_daf47bc=0):
        meadow_ret_local_022c07d = meadow_unpack_fn_6324a19(meadow_self_ba4d316.buf[meadow_self_ba4d316.pos:])
        if isinstance(meadow_ret_local_022c07d, tuple):
            meadow_ret_local_022c07d, meadow__size_e3717c8 = meadow_ret_local_022c07d
            _name_boundary.attributes(meadow_self_ba4d316)['seek'](meadow__size_e3717c8 if meadow_size_local_daf47bc == 0 else meadow_size_local_daf47bc)
        else:
            _name_boundary.attributes(meadow_self_ba4d316)['seek'](meadow_size_local_daf47bc)
        return meadow_ret_local_022c07d

    @_name_boundary.callable_contract({'self': 'meadow_self_ae964d8'}, 'peek_u8')
    def meadow_peek_u8(meadow_self_ae964d8):
        return _name_boundary.attributes(struct)['unpack']('<B', meadow_self_ae964d8.buf[meadow_self_ae964d8.pos:meadow_self_ae964d8.pos + 1])[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_0ba0aab'}, 'peek_u16')
    def meadow_peek_u16(meadow_self_0ba0aab):
        return _name_boundary.attributes(struct)['unpack']('<H', meadow_self_0ba0aab.buf[meadow_self_0ba0aab.pos:meadow_self_0ba0aab.pos + 2])[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_8884a52'}, 'u8')
    def u8(meadow_self_8884a52):
        return _name_boundary.attributes(struct)['unpack']('<B', _name_boundary.attributes(meadow_self_8884a52)['read'](1))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_7dad28f'}, 'u16')
    def u16(meadow_self_7dad28f):
        return _name_boundary.attributes(struct)['unpack']('<H', _name_boundary.attributes(meadow_self_7dad28f)['read'](2))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_3c49857'}, 'db')
    def meadow_db(meadow_self_3c49857):
        """read 1 byte as u8"""
        return meadow_self_3c49857.u8()

    @_name_boundary.callable_contract({'self': 'meadow_self_fff1ff1'}, 'dt')
    def meadow_dt(meadow_self_fff1ff1):
        """Reads 1 to 2 bytes.
        Value Range: 0-0xFFFE
        Usage: 16bit numbers
        :return: int
        """
        meadow_val_local_d15e267 = meadow_self_fff1ff1.u8()
        if meadow_val_local_d15e267 & 128:
            meadow_val_local_d15e267 = meadow_val_local_d15e267 & 127 | meadow_self_fff1ff1.u8() << 7
        return meadow_val_local_d15e267 - 1

    @_name_boundary.callable_contract({'self': 'meadow_self_a260983'}, 'de')
    def meadow_de(meadow_self_a260983):
        """Reads 1 to 5 bytes
        Value Range: 0-0xFFFFFFFF
        Usage: Enum Deltas
        :return: int
        """
        meadow_val_local_d5dcb82 = 0
        while True:
            meadow_hi_local_99b4090 = meadow_val_local_d5dcb82 << 6
            meadow_b_local_e103346 = meadow_self_a260983.u8()
            meadow_sign_local_af5710a = meadow_b_local_e103346 & 128
            if not meadow_sign_local_af5710a:
                meadow_lo_local_1400d08 = meadow_b_local_e103346 & 63
                meadow_val_local_d5dcb82 = meadow_lo_local_1400d08 | meadow_hi_local_99b4090
                break
            else:
                meadow_lo_local_1400d08 = 2 * meadow_hi_local_99b4090
                meadow_hi_local_99b4090 = meadow_b_local_e103346 & 127
                meadow_val_local_d5dcb82 = meadow_lo_local_1400d08 | meadow_hi_local_99b4090
        return meadow_val_local_d5dcb82

    @_name_boundary.callable_contract({'self': 'meadow_self_3b74bc7'}, 'da')
    def da(meadow_self_3b74bc7):
        """Reads 1 to 9 bytes.
        ValueRange: 0x-0x7FFFFFFF, 0-0xFFFFFFFF
        Usage: Arrays
        :return: (int, int)
        """
        meadow_a_local_77877bc = 0
        meadow_b_local_d518b36 = 0
        meadow_da_local_c45d13c = 0
        meadow_base_local_ac32e85 = 0
        meadow_nelem_local_a3f47b9 = 0
        while True:
            meadow_typ_local_1053f1a = _name_boundary.attributes(meadow_self_3b74bc7)['peek_u8']()
            if meadow_typ_local_1053f1a & 128 == 0:
                break
            _name_boundary.attributes(meadow_self_3b74bc7)['seek'](1)
            meadow_da_local_c45d13c = meadow_da_local_c45d13c << 7 | meadow_typ_local_1053f1a & 127
            meadow_b_local_d518b36 += 1
            if meadow_b_local_d518b36 >= 4:
                meadow_z_local_1387c16 = _name_boundary.attributes(meadow_self_3b74bc7)['peek_u8']()
                if meadow_z_local_1387c16 != 0:
                    meadow_base_local_ac32e85 = 16 * meadow_da_local_c45d13c | meadow_z_local_1387c16 & 15
                meadow_nelem_local_a3f47b9 = meadow_self_3b74bc7.u8() >> 4 & 7
                while True:
                    meadow_y_local_9ba2521 = _name_boundary.attributes(meadow_self_3b74bc7)['peek_u8']()
                    if meadow_y_local_9ba2521 & 128 == 0:
                        break
                    _name_boundary.attributes(meadow_self_3b74bc7)['seek'](1)
                    meadow_nelem_local_a3f47b9 = meadow_nelem_local_a3f47b9 << 7 | meadow_y_local_9ba2521 & 127
                    meadow_a_local_77877bc += 1
                    if meadow_a_local_77877bc >= 4:
                        return (True, meadow_nelem_local_a3f47b9, meadow_base_local_ac32e85)
        return (False, meadow_nelem_local_a3f47b9, meadow_base_local_ac32e85)

    @_name_boundary.callable_contract({'self': 'meadow_self_cc2710c'}, 'pstring')
    def meadow_pstring(meadow_self_cc2710c):
        meadow_length_local_6e26a46 = _name_boundary.attributes(meadow_self_cc2710c)['dt']()
        meadow_buf_local_634ec96 = _name_boundary.attributes(meadow_self_cc2710c)['read'](meadow_length_local_6e26a46)
        return meadow_buf_local_634ec96.decode('ascii')

    @_name_boundary.callable_contract({'self': 'meadow_self_5624025'}, 'pbytes')
    def meadow_pbytes(meadow_self_5624025):
        meadow_length_local_f9c9e9e = _name_boundary.attributes(meadow_self_5624025)['dt']()
        meadow_buf_local_0d77db1 = _name_boundary.attributes(meadow_self_5624025)['read'](meadow_length_local_f9c9e9e)
        return meadow_buf_local_0d77db1

    @_name_boundary.callable_contract({'self': 'meadow_self_6cc11ae'}, 'type_attr')
    def meadow_type_attr(meadow_self_6cc11ae):
        meadow_val_local_a2547d6 = 0
        meadow_tah_local_fd687fe = meadow_self_6cc11ae.u8()
        meadow_tmp_local_63b26c3 = (meadow_tah_local_fd687fe & 1 | meadow_tah_local_fd687fe >> 3 & 6) + 1
        if meadow_is_tah_byte(meadow_tah_local_fd687fe) or meadow_tmp_local_63b26c3 == 8:
            if meadow_tmp_local_63b26c3 == 8:
                meadow_val_local_a2547d6 = meadow_tmp_local_63b26c3
            meadow_shift_local_d9980cd = 0
            while True:
                meadow_next_byte_local_1be0597 = meadow_self_6cc11ae.u8()
                if meadow_next_byte_local_1be0597 == 0:
                    raise ValueError('type_attr(): failed to parse')
                meadow_val_local_a2547d6 |= (meadow_next_byte_local_1be0597 & 127) << meadow_shift_local_d9980cd
                if meadow_next_byte_local_1be0597 & 128 == 0:
                    break
                meadow_shift_local_d9980cd += 7
        meadow_unk_local_2ef34b0 = []
        if meadow_val_local_a2547d6 & meadow_TAH_HASATTRS:
            meadow_val_local_a2547d6 = _name_boundary.attributes(meadow_self_6cc11ae)['dt']()
            for meadow___9c1e84f in range(meadow_val_local_a2547d6):
                meadow_string_local_a191345 = _name_boundary.attributes(meadow_self_6cc11ae)['pstring']()
                _name_boundary.attributes(meadow_self_6cc11ae)['seek'](_name_boundary.attributes(meadow_self_6cc11ae)['dt']())
                meadow_unk_local_2ef34b0.append(meadow_string_local_a191345)
        return meadow_val_local_a2547d6

    @_name_boundary.callable_contract({'self': 'meadow_self_a26d824'}, 'tah_attr')
    def meadow_tah_attr(meadow_self_a26d824):
        if _name_boundary.attributes(meadow_self_a26d824)['has_next']() and meadow_is_tah_byte(_name_boundary.attributes(meadow_self_a26d824)['peek_u8']()):
            return _name_boundary.attributes(meadow_self_a26d824)['type_attr']()
        return 0

    @_name_boundary.callable_contract({'self': 'meadow_self_bcf1db2'}, 'sdacl_attr')
    def meadow_sdacl_attr(meadow_self_bcf1db2):
        if _name_boundary.attributes(meadow_self_bcf1db2)['has_next']() and meadow_is_sdacl_byte(_name_boundary.attributes(meadow_self_bcf1db2)['peek_u8']()):
            return _name_boundary.attributes(meadow_self_bcf1db2)['type_attr']()
        return 0

    @_name_boundary.callable_contract({'self': 'meadow_self_b2eff0d'}, 'get')
    def meadow_get(meadow_self_b2eff0d):
        return meadow_TypeString(_name_boundary.attributes(meadow_self_b2eff0d)['rest']())

    @_name_boundary.callable_contract({'self': 'meadow_self_bce0e4e'}, 'ref')
    def meadow_ref(meadow_self_bce0e4e):
        return meadow_TypeString(_name_boundary.attributes(meadow_self_bce0e4e)['rest'](), parent=meadow_self_bce0e4e)

    @_name_boundary.callable_contract({'self': 'meadow_self_8c196cd'}, 'rest')
    def meadow_rest(meadow_self_8c196cd):
        return meadow_self_8c196cd.buf[meadow_self_8c196cd.pos:]

    @_name_boundary.callable_contract({'self': 'meadow_self_24fd972'}, 'has_next')
    def meadow_has_next(meadow_self_24fd972):
        return meadow_self_24fd972.pos < len(meadow_self_24fd972.buf)
    seek = meadow_seek
    read = meadow_read
    unpack = meadow_unpack
    peek_u8 = meadow_peek_u8
    peek_u16 = meadow_peek_u16
    db = meadow_db
    dt = meadow_dt
    de = meadow_de
    pstring = meadow_pstring
    pbytes = meadow_pbytes
    type_attr = meadow_type_attr
    tah_attr = meadow_tah_attr
    sdacl_attr = meadow_sdacl_attr
    get = meadow_get
    ref = meadow_ref
    rest = meadow_rest
    has_next = meadow_has_next

@_name_boundary.callable_contract({'n': 'meadow_n_bfa1615'}, 'serialize_dt')
def meadow_serialize_dt(meadow_n_bfa1615):
    if meadow_n_bfa1615 > 32766:
        raise ValueError('Value too high for append_dt')
    meadow_lo_local_bca6fc6 = meadow_n_bfa1615 + 1
    meadow_hi_local_ecb474f = meadow_n_bfa1615 + 1
    meadow_result_local_62f343f = bytearray()
    if meadow_lo_local_bca6fc6 > 127:
        meadow_result_local_62f343f += _name_boundary.attributes(struct)['pack']('<B', meadow_lo_local_bca6fc6 & 127 | 128)
        meadow_hi_local_ecb474f = meadow_lo_local_bca6fc6 >> 7 & 255
    meadow_result_local_62f343f += _name_boundary.attributes(struct)['pack']('<B', meadow_hi_local_ecb474f)
    return meadow_result_local_62f343f

@_name_boundary.class_contract('TypeData', {'deserialize': 'meadow_deserialize'})
class meadow_TypeData:
    __metaclass__ = meadow_ABCMeta

    @meadow_abstractmethod
    @_name_boundary.callable_contract({'self': 'meadow_self_475c2c4', 'type_string': 'meadow_type_string_9aeddb2', 'til': 'meadow_til_local_69b84a8', 'fields': 'meadow_fields_local_a063e8f', 'fieldcmts': 'meadow_fieldcmts_local_44e0679'}, 'deserialize')
    def meadow_deserialize(meadow_self_475c2c4, meadow_til_local_69b84a8, meadow_type_string_9aeddb2, meadow_fields_local_a063e8f, meadow_fieldcmts_local_44e0679):
        pass
meadow_global_inf = None

@_name_boundary.class_contract('TInfo', {'get_refname': 'meadow_get_refname', 'get_name': 'meadow_get_name', 'get_next_tinfo': 'meadow_get_next_tinfo', 'get_final_tinfo': 'meadow_get_final_tinfo', 'get_arr_object': 'meadow_get_arr_object', 'get_pointed_object': 'meadow_get_pointed_object', 'get_ptrarr_object': 'meadow_get_ptrarr_object', 'get_cc': 'meadow_get_cc', 'get_rettype': 'meadow_get_rettype', 'get_size': 'meadow_get_size', 'get_conv': 'meadow_get_conv', 'get_typename': 'meadow_get_typename', 'get_typedeclare': 'meadow_get_typedeclare', 'get_typestr': 'meadow_get_typestr', 'has_details': 'meadow_has_details', 'has_vftable': 'meadow_has_vftable', 'get_decltype': 'meadow_get_decltype', 'get_realtype': 'meadow_get_realtype', 'is_decl_typedef': 'meadow_is_decl_typedef', 'is_decl_array': 'meadow_is_decl_array', 'is_decl_bitfield': 'meadow_is_decl_bitfield', 'is_decl_bool': 'meadow_is_decl_bool', 'is_decl_char': 'meadow_is_decl_char', 'is_decl_complex': 'meadow_is_decl_complex', 'is_decl_const': 'meadow_is_decl_const', 'is_decl_double': 'meadow_is_decl_double', 'is_decl_enum': 'meadow_is_decl_enum', 'is_decl_float': 'meadow_is_decl_float', 'is_decl_floating': 'meadow_is_decl_floating', 'is_decl_func': 'meadow_is_decl_func', 'is_decl_int': 'meadow_is_decl_int', 'is_decl_int128': 'meadow_is_decl_int128', 'is_decl_int16': 'meadow_is_decl_int16', 'is_decl_int32': 'meadow_is_decl_int32', 'is_decl_int64': 'meadow_is_decl_int64', 'is_decl_paf': 'meadow_is_decl_paf', 'is_decl_partial': 'meadow_is_decl_partial', 'is_decl_ptr': 'meadow_is_decl_ptr', 'is_decl_ptr_or_array': 'meadow_is_decl_ptr_or_array', 'is_decl_struct': 'meadow_is_decl_struct', 'is_decl_sue': 'meadow_is_decl_sue', 'is_decl_uchar': 'meadow_is_decl_uchar', 'is_decl_udt': 'meadow_is_decl_udt', 'is_decl_uint': 'meadow_is_decl_uint', 'is_decl_uint128': 'meadow_is_decl_uint128', 'is_decl_uint16': 'meadow_is_decl_uint16', 'is_decl_uint32': 'meadow_is_decl_uint32', 'is_decl_uint64': 'meadow_is_decl_uint64', 'is_decl_union': 'meadow_is_decl_union', 'is_decl_unknown': 'meadow_is_decl_unknown', 'is_decl_void': 'meadow_is_decl_void', 'is_decl_volatile': 'meadow_is_decl_volatile', 'is_arithmetic': 'meadow_is_arithmetic', 'is_array': 'meadow_is_array', 'is_bitfield': 'meadow_is_bitfield', 'is_bool': 'meadow_is_bool', 'is_castable_to': 'meadow_is_castable_to', 'is_char': 'meadow_is_char', 'is_complex': 'meadow_is_complex', 'is_const': 'meadow_is_const', 'is_correct': 'meadow_is_correct', 'is_double': 'meadow_is_double', 'is_empty_udt': 'meadow_is_empty_udt', 'is_enum': 'meadow_is_enum', 'is_ext_arithmetic': 'meadow_is_ext_arithmetic', 'is_ext_integral': 'meadow_is_ext_integral', 'is_float': 'meadow_is_float', 'is_floating': 'meadow_is_floating', 'is_forward_decl': 'meadow_is_forward_decl', 'is_from_subtil': 'meadow_is_from_subtil', 'is_func': 'meadow_is_func', 'is_funcptr': 'meadow_is_funcptr', 'is_high_func': 'meadow_is_high_func', 'is_int': 'meadow_is_int', 'is_int128': 'meadow_is_int128', 'is_int16': 'meadow_is_int16', 'is_int32': 'meadow_is_int32', 'is_int64': 'meadow_is_int64', 'is_integral': 'meadow_is_integral', 'is_ldouble': 'meadow_is_ldouble', 'is_manually_castable_to': 'meadow_is_manually_castable_to', 'is_one_fpval': 'meadow_is_one_fpval', 'is_paf': 'meadow_is_paf', 'is_partial': 'meadow_is_partial', 'is_ptr': 'meadow_is_ptr', 'is_ptr_or_array': 'meadow_is_ptr_or_array', 'is_purging_cc': 'meadow_is_purging_cc', 'is_pvoid': 'meadow_is_pvoid', 'is_scalar': 'meadow_is_scalar', 'is_shifted_ptr': 'meadow_is_shifted_ptr', 'is_signed': 'meadow_is_signed', 'is_small_udt': 'meadow_is_small_udt', 'is_sse_type': 'meadow_is_sse_type', 'is_struct': 'meadow_is_struct', 'is_sue': 'meadow_is_sue', 'is_uchar': 'meadow_is_uchar', 'is_udt': 'meadow_is_udt', 'is_uint': 'meadow_is_uint', 'is_uint128': 'meadow_is_uint128', 'is_uint16': 'meadow_is_uint16', 'is_uint32': 'meadow_is_uint32', 'is_uint64': 'meadow_is_uint64', 'is_union': 'meadow_is_union', 'is_unknown': 'meadow_is_unknown', 'is_unsigned': 'meadow_is_unsigned', 'is_user_cc': 'meadow_is_user_cc', 'is_vararg_cc': 'meadow_is_vararg_cc', 'is_varstruct': 'meadow_is_varstruct', 'is_vftable': 'meadow_is_vftable', 'is_void': 'meadow_is_void', 'is_volatile': 'meadow_is_volatile', 'base_type': 'meadow_base_type', 'type_details': 'meadow_type_details', '_types': 'meadow__types'})
class meadow_TInfo:

    @_name_boundary.callable_contract({'self': 'meadow_self_c6c5549', 'base_type': 'meadow_base_type_e3a5449', 'type_details': 'meadow_type_details_7094c62', 'til': 'meadow_til_local_ab6b318', 'name': 'meadow_name_local_79a7ab1', 'inf': 'meadow_inf_local_daa50e4'}, '__init__')
    def __init__(meadow_self_c6c5549, meadow_base_type_e3a5449=meadow_BT_UNK, meadow_type_details_7094c62=None, meadow_til_local_ab6b318=None, meadow_name_local_79a7ab1=None, meadow_inf_local_daa50e4=None):
        _name_boundary.attributes(meadow_self_c6c5549)['base_type'] = meadow_base_type_e3a5449
        meadow_self_c6c5549.flags = 0
        _name_boundary.attributes(meadow_self_c6c5549)['type_details'] = meadow_type_details_7094c62
        meadow_self_c6c5549.til = meadow_til_local_ab6b318
        meadow_self_c6c5549.name = meadow_name_local_79a7ab1 if meadow_name_local_79a7ab1 is not None else ''
        meadow_self_c6c5549.inf = meadow_inf_local_daa50e4
        _name_boundary.attributes(meadow_self_c6c5549)['_types'] = _name_boundary.attributes(meadow_til_local_ab6b318)['types'] if meadow_til_local_ab6b318 is not None else None

    @_name_boundary.callable_contract({'self': 'meadow_self_ce6b8ff'}, 'get_refname')
    def meadow_get_refname(meadow_self_ce6b8ff):
        if _name_boundary.attributes(meadow_self_ce6b8ff)['is_decl_typedef']():
            meadow_nex_81d3450 = _name_boundary.attributes(meadow_self_ce6b8ff)['get_next_tinfo']()
            if _name_boundary.attributes(meadow_nex_81d3450)['base_type'] == 0:
                return '#{}'.format(_name_boundary.attributes(meadow_self_ce6b8ff)['type_details'].ordinal) if _name_boundary.attributes(_name_boundary.attributes(meadow_self_ce6b8ff)['type_details'])['is_ordref'] else _name_boundary.attributes(meadow_self_ce6b8ff)['type_details'].name
            else:
                return _name_boundary.attributes(meadow_nex_81d3450)['get_name']()
        raise ValueError

    @_name_boundary.callable_contract({'self': 'meadow_self_e08dc8f'}, 'get_name')
    def meadow_get_name(meadow_self_e08dc8f):
        if meadow_self_e08dc8f.name == '' and _name_boundary.attributes(meadow_self_e08dc8f)['is_decl_typedef']():
            return _name_boundary.attributes(meadow_self_e08dc8f)['get_refname']()
        return meadow_self_e08dc8f.name

    @_name_boundary.callable_contract({'self': 'meadow_self_3a5a0f1'}, 'get_next_tinfo')
    def meadow_get_next_tinfo(meadow_self_3a5a0f1):
        if _name_boundary.attributes(meadow_self_3a5a0f1)['is_decl_typedef']() and _name_boundary.attributes(meadow_self_3a5a0f1)['_types'] is not None:
            meadow_typedef_detail_e85c5ea = _name_boundary.attributes(meadow_self_3a5a0f1)['type_details']
            if _name_boundary.attributes(meadow_typedef_detail_e85c5ea)['is_ordref']:
                meadow__def_local_2c5b936 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3a5a0f1)['_types'])['get_by_ordinal'](meadow_typedef_detail_e85c5ea.ordinal)
            else:
                meadow__def_local_2c5b936 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3a5a0f1)['_types'])['find_by_name'](meadow_typedef_detail_e85c5ea.name)
            if meadow__def_local_2c5b936 is not None:
                return meadow__def_local_2c5b936.type
            else:
                return meadow_TInfo()
        return meadow_TInfo()

    @_name_boundary.callable_contract({'self': 'meadow_self_5e3d05a'}, 'get_final_tinfo')
    def meadow_get_final_tinfo(meadow_self_5e3d05a):
        if _name_boundary.attributes(meadow_self_5e3d05a)['is_decl_typedef']() and _name_boundary.attributes(meadow_self_5e3d05a)['_types'] is not None:
            meadow__type_local_81d4991 = _name_boundary.attributes(meadow_self_5e3d05a)['get_next_tinfo']()
            while _name_boundary.attributes(meadow__type_local_81d4991)['is_decl_typedef']():
                meadow__type_local_81d4991 = _name_boundary.attributes(meadow__type_local_81d4991)['get_next_tinfo']()
            return meadow__type_local_81d4991
        return meadow_self_5e3d05a

    @_name_boundary.callable_contract({'self': 'meadow_self_81716a8'}, 'get_arr_object')
    def meadow_get_arr_object(meadow_self_81716a8):
        if _name_boundary.attributes(meadow_self_81716a8)['is_decl_array']():
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_81716a8)['type_details'])['elem_type']
        return meadow_TInfo()

    @_name_boundary.callable_contract({'self': 'meadow_self_79e7d47'}, 'get_pointed_object')
    def meadow_get_pointed_object(meadow_self_79e7d47):
        if _name_boundary.attributes(meadow_self_79e7d47)['is_decl_ptr']():
            meadow_pt_27b2b3c = _name_boundary.attributes(meadow_self_79e7d47)['type_details']
            if _name_boundary.attributes(meadow_pt_27b2b3c)['closure'] is not None:
                return _name_boundary.attributes(meadow_pt_27b2b3c)['closure']
            else:
                return _name_boundary.attributes(meadow_pt_27b2b3c)['obj_type']
        return meadow_TInfo()

    @_name_boundary.callable_contract({'self': 'meadow_self_f90a7ce'}, 'get_ptrarr_object')
    def meadow_get_ptrarr_object(meadow_self_f90a7ce):
        if _name_boundary.attributes(meadow_self_f90a7ce)['is_decl_ptr_or_array']():
            if _name_boundary.attributes(meadow_self_f90a7ce)['is_decl_array']():
                return _name_boundary.attributes(meadow_self_f90a7ce)['get_arr_object']()
            else:
                return _name_boundary.attributes(meadow_self_f90a7ce)['get_pointed_object']()
        return meadow_TInfo()

    @_name_boundary.callable_contract({'self': 'meadow_self_4f52044'}, 'get_cc')
    def meadow_get_cc(meadow_self_4f52044):
        if _name_boundary.attributes(meadow_self_4f52044)['is_decl_func']():
            return meadow_get_cc(_name_boundary.attributes(_name_boundary.attributes(meadow_self_4f52044)['type_details'])['cc'])
        elif _name_boundary.attributes(meadow_self_4f52044)['is_funcptr']():
            return _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_self_4f52044)['get_pointed_object']())['type_details'])['cc']

    @_name_boundary.callable_contract({'self': 'meadow_self_6015712'}, 'get_rettype')
    def meadow_get_rettype(meadow_self_6015712):
        if _name_boundary.attributes(meadow_self_6015712)['is_decl_func']():
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_6015712)['type_details'])['rettype']
        elif _name_boundary.attributes(meadow_self_6015712)['is_funcptr']():
            return _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_self_6015712)['get_pointed_object']())['type_details'])['rettype']

    @_name_boundary.callable_contract({'self': 'meadow_self_61bd9d4'}, 'get_size')
    def meadow_get_size(meadow_self_61bd9d4):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_1a9fb3d'}, 'get_conv')
    def meadow_get_conv(meadow_self_1a9fb3d):
        if not _name_boundary.attributes(meadow_self_1a9fb3d)['is_func']():
            return ''
        meadow_cc_e5ef855 = _name_boundary.attributes(meadow_self_1a9fb3d)['get_cc']()
        meadow_conv_bb435e0 = ''
        if meadow_cc_e5ef855 == meadow_CM_CC_INVALID:
            meadow_conv_bb435e0 += '__bad_cc'
        if meadow_cc_e5ef855 == meadow_CM_CC_CDECL:
            meadow_conv_bb435e0 = '__cdecl'
        elif meadow_cc_e5ef855 == meadow_CM_CC_STDCALL:
            meadow_conv_bb435e0 = '__stdcall'
        elif meadow_cc_e5ef855 == meadow_CM_CC_PASCAL:
            meadow_conv_bb435e0 = '__pascal'
        elif meadow_cc_e5ef855 == meadow_CM_CC_FASTCALL:
            meadow_conv_bb435e0 = '__fastcall'
        elif meadow_cc_e5ef855 == meadow_CM_CC_THISCALL:
            meadow_conv_bb435e0 = '__thiscall'
        elif meadow_cc_e5ef855 == meadow_CM_CC_SPOILED:
            meadow_conv_bb435e0 = '__spoiled'
        elif meadow_cc_e5ef855 in (meadow_CM_CC_SPECIALE, meadow_CM_CC_SPECIAL):
            meadow_conv_bb435e0 += '__usercall'
        elif meadow_cc_e5ef855 == meadow_CM_CC_SPECIALP:
            meadow_conv_bb435e0 += '__userpurge'
        return meadow_conv_bb435e0

    @_name_boundary.callable_contract({'self': 'meadow_self_6bc00ba'}, 'get_typename')
    def meadow_get_typename(meadow_self_6bc00ba):
        global meadow_global_inf
        meadow_global_inf = meadow_self_6bc00ba.inf if meadow_self_6bc00ba.inf is not None else meadow_global_inf
        meadow_t_59016f8 = ''
        meadow_base_local_20949d5 = meadow_get_base_type(_name_boundary.attributes(meadow_self_6bc00ba)['get_decltype']())
        meadow_flags_local_5b4e252 = meadow_get_type_flags(_name_boundary.attributes(meadow_self_6bc00ba)['get_decltype']())
        if meadow_is_typeid_last(_name_boundary.attributes(meadow_self_6bc00ba)['base_type']):
            if meadow_base_local_20949d5 == meadow_BT_UNK:
                meadow_t_59016f8 += 'unknown'
            elif meadow_base_local_20949d5 == meadow_BT_VOID:
                meadow_t_59016f8 += 'void'
            elif meadow_BT_INT8 <= meadow_base_local_20949d5 <= meadow_BT_INT:
                if _name_boundary.attributes(meadow_self_6bc00ba)['is_unsigned']():
                    meadow_t_59016f8 += 'unsigned '
                if meadow_base_local_20949d5 == meadow_BT_INT8:
                    meadow_t_59016f8 += 'int8'
                elif meadow_base_local_20949d5 == meadow_BT_INT16:
                    meadow_t_59016f8 += 'int16'
                elif meadow_base_local_20949d5 == meadow_BT_INT32:
                    meadow_t_59016f8 += 'int32'
                elif meadow_base_local_20949d5 == meadow_BT_INT64:
                    meadow_t_59016f8 += 'int64'
                elif meadow_base_local_20949d5 == meadow_BT_INT128:
                    meadow_t_59016f8 += 'int128'
                elif meadow_base_local_20949d5 == meadow_BT_INT:
                    meadow_t_59016f8 += 'int'
            elif meadow_base_local_20949d5 == meadow_BT_BOOL:
                meadow_t_59016f8 += 'bool'
            elif meadow_base_local_20949d5 == meadow_BT_FLOAT:
                if meadow_flags_local_5b4e252 == meadow_BTMT_FLOAT:
                    meadow_t_59016f8 += 'float'
                elif meadow_flags_local_5b4e252 == meadow_BTMT_FLOAT:
                    meadow_t_59016f8 += 'double'
                elif meadow_flags_local_5b4e252 == meadow_BTMT_LNGDBL:
                    meadow_t_59016f8 += 'long double'
                elif meadow_flags_local_5b4e252 == meadow_BTMT_SPECFLT:
                    meadow_t_59016f8 += 'special float'
                else:
                    meadow_t_59016f8 += 'unknown float'
        elif _name_boundary.attributes(meadow_self_6bc00ba)['is_funcptr']() or _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_func']():
            if _name_boundary.attributes(meadow_self_6bc00ba)['is_funcptr']():
                meadow_func_408b119 = _name_boundary.attributes(meadow_self_6bc00ba)['get_pointed_object']()
                meadow_star_f7bb451 = '*'
            else:
                meadow_func_408b119 = meadow_self_6bc00ba
                meadow_star_f7bb451 = ''
            meadow_t_59016f8 += _name_boundary.attributes(_name_boundary.attributes(meadow_func_408b119)['get_rettype']())['get_typename']() + ' '
            meadow_conv_ee95943 = _name_boundary.attributes(meadow_func_408b119)['get_conv']()
            meadow_t_59016f8 += '(' + meadow_conv_ee95943
            if meadow_conv_ee95943 != '':
                meadow_t_59016f8 += ' '
            meadow_t_59016f8 += meadow_star_f7bb451 + _name_boundary.attributes(meadow_self_6bc00ba)['get_name']()
            if _name_boundary.attributes(meadow_func_408b119)['is_user_cc']() and (not _name_boundary.attributes(_name_boundary.attributes(meadow_func_408b119)['get_rettype']())['is_void']()):
                meadow_loc_de90d02 = meadow_print_argloc(_name_boundary.attributes(_name_boundary.attributes(meadow_func_408b119)['type_details'])['retloc'])
                if meadow_loc_de90d02 is not None:
                    meadow_t_59016f8 += '@<{}>'.format(meadow_loc_de90d02)
            meadow_t_59016f8 += ')'
            meadow_args_fdfd9cf = _name_boundary.attributes(_name_boundary.attributes(meadow_func_408b119)['type_details'])['args']
            meadow_t_59016f8 += '('
            for meadow_i_9737285 in range(len(meadow_args_fdfd9cf)):
                meadow_arg_2392d31 = meadow_args_fdfd9cf[meadow_i_9737285]
                meadow_argtype_28d9b61 = meadow_arg_2392d31.type
                meadow_t_59016f8 += _name_boundary.attributes(meadow_argtype_28d9b61)['get_typename']()
                meadow_t_59016f8 += ' ' + meadow_arg_2392d31.name if meadow_arg_2392d31.name != '' else ''
                if _name_boundary.attributes(meadow_self_6bc00ba)['is_user_cc']():
                    meadow_loc_de90d02 = meadow_print_argloc(_name_boundary.attributes(meadow_arg_2392d31)['argloc'])
                    if meadow_loc_de90d02 is not None:
                        meadow_t_59016f8 += '@<{}>'.format(meadow_loc_de90d02)
                if meadow_i_9737285 < len(meadow_args_fdfd9cf) - 1:
                    meadow_t_59016f8 += ', '
            meadow_t_59016f8 += ')'
        elif _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_ptr']():
            meadow_ptr_local_1fcb51f = _name_boundary.attributes(meadow_self_6bc00ba)['get_pointed_object']()
            meadow_t_59016f8 += '{}*'.format(_name_boundary.attributes(meadow_ptr_local_1fcb51f)['get_typename']())
        elif _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_array']():
            meadow_n_elems_438f696 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_6bc00ba)['type_details'])['n_elems']
            meadow_arrobj_15723f7 = _name_boundary.attributes(meadow_self_6bc00ba)['get_arr_object']()
            meadow_t_59016f8 += '{}[]'.format(_name_boundary.attributes(meadow_arrobj_15723f7)['get_typename']()) if meadow_n_elems_438f696 == 0 else '{}[{}]'.format(_name_boundary.attributes(_name_boundary.attributes(meadow_self_6bc00ba)['get_arr_object']())['get_typename'](), meadow_n_elems_438f696)
        elif _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_udt']() or _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_enum']():
            meadow_ref_88011eb = _name_boundary.attributes(_name_boundary.attributes(meadow_self_6bc00ba)['type_details'])['ref']
            meadow_refname_0a99e79 = '' if meadow_ref_88011eb is None else _name_boundary.attributes(meadow_ref_88011eb)['get_refname']()
            meadow_t_59016f8 += _name_boundary.attributes(meadow_self_6bc00ba)['get_name']() if meadow_refname_0a99e79 == '' else meadow_refname_0a99e79
        elif _name_boundary.attributes(meadow_self_6bc00ba)['is_decl_bitfield']():
            if _name_boundary.attributes(_name_boundary.attributes(meadow_self_6bc00ba)['type_details'])['is_unsigned']:
                meadow_t_59016f8 += 'unsigned '
            meadow_t_59016f8 += 'int{}'.format(_name_boundary.attributes(_name_boundary.attributes(meadow_self_6bc00ba)['type_details'])['nbytes'] * 8)
        else:
            meadow_t_59016f8 += _name_boundary.attributes(meadow_self_6bc00ba)['get_name']()
        return meadow_t_59016f8

    @_name_boundary.callable_contract({'self': 'meadow_self_20dd93e'}, 'get_typedeclare')
    def meadow_get_typedeclare(meadow_self_20dd93e):
        meadow_t_3b85eb4 = ''
        if _name_boundary.attributes(meadow_self_20dd93e)['is_decl_typedef']():
            meadow_t_3b85eb4 += 'typedef {} {}'.format(_name_boundary.attributes(meadow_self_20dd93e)['get_typename'](), _name_boundary.attributes(meadow_self_20dd93e)['get_refname']())
        elif _name_boundary.attributes(meadow_self_20dd93e)['is_decl_enum']():
            meadow_t_3b85eb4 += 'enum {}'.format(_name_boundary.attributes(meadow_self_20dd93e)['get_name']())
        elif _name_boundary.attributes(meadow_self_20dd93e)['is_decl_udt']():
            if _name_boundary.attributes(meadow_self_20dd93e)['is_decl_union']():
                meadow_t_3b85eb4 += 'union '
            elif _name_boundary.attributes(meadow_self_20dd93e)['is_decl_struct']():
                meadow_t_3b85eb4 += 'struct '
            meadow_t_3b85eb4 += _name_boundary.attributes(meadow_self_20dd93e)['get_typename']()
        else:
            meadow_t_3b85eb4 += _name_boundary.attributes(meadow_self_20dd93e)['get_typename']()
        return meadow_t_3b85eb4

    @_name_boundary.callable_contract({'self': 'meadow_self_f8cb927', 'indent': 'meadow_indent_local_8725387'}, 'get_typestr')
    def meadow_get_typestr(meadow_self_f8cb927, meadow_indent_local_8725387=2):
        meadow_typestr_548d726 = _name_boundary.attributes(meadow_self_f8cb927)['get_typedeclare']()
        if _name_boundary.attributes(meadow_self_f8cb927)['is_decl_sue']():
            meadow_members_ea84edb = _name_boundary.attributes(_name_boundary.attributes(meadow_self_f8cb927)['type_details'])['members']
            if _name_boundary.attributes(meadow_self_f8cb927)['is_decl_udt']():
                if len(meadow_members_ea84edb) > 0 and _name_boundary.attributes(meadow_members_ea84edb[0])['is_baseclass']():
                    meadow_typestr_548d726 += ' : {}'.format(_name_boundary.attributes(meadow_members_ea84edb[0].type)['get_name']())
                    meadow_members_ea84edb = meadow_members_ea84edb[1:]
                if len(meadow_members_ea84edb) == 0:
                    meadow_typestr_548d726 += ' { }'
                else:
                    meadow_typestr_548d726 += '\n{\n'
                    for meadow_m_09b20f2 in meadow_members_ea84edb:
                        meadow_typestr_548d726 += ' ' * meadow_indent_local_8725387
                        meadow_typename_ea77f5e = _name_boundary.attributes(meadow_m_09b20f2.type)['get_typename']()
                        if _name_boundary.attributes(meadow_m_09b20f2.type)['is_funcptr']():
                            meadow_typestr_548d726 += meadow_typename_ea77f5e.replace('{name}', meadow_m_09b20f2.name) if meadow_m_09b20f2.name is not None else meadow_typename_ea77f5e
                            meadow_typestr_548d726 += ';\n'
                        elif _name_boundary.attributes(meadow_m_09b20f2.type)['is_decl_bitfield']():
                            meadow_typestr_548d726 += '{} {} : {};\n'.format(meadow_typename_ea77f5e, meadow_m_09b20f2.name, _name_boundary.attributes(_name_boundary.attributes(meadow_m_09b20f2.type)['type_details'])['width'])
                        else:
                            meadow_typestr_548d726 += '{} {};\n'.format(meadow_typename_ea77f5e, meadow_m_09b20f2.name)
                    meadow_typestr_548d726 += '}'
            else:
                meadow_typestr_548d726 += '\n{\n'
                for meadow_m_09b20f2 in meadow_members_ea84edb:
                    meadow_typestr_548d726 += ' ' * meadow_indent_local_8725387
                    meadow_typestr_548d726 += '{} = 0x{:X},\n'.format(meadow_m_09b20f2.name, meadow_m_09b20f2.value)
                meadow_typestr_548d726 += '}'
        return meadow_typestr_548d726

    @_name_boundary.callable_contract({'self': 'meadow_self_212f18c'}, 'has_details')
    def meadow_has_details(meadow_self_212f18c):
        return _name_boundary.attributes(meadow_self_212f18c)['type_details'] is not None

    @_name_boundary.callable_contract({'self': 'meadow_self_462b490'}, 'has_vftable')
    def meadow_has_vftable(meadow_self_462b490):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_a19f31c'}, 'get_decltype')
    def meadow_get_decltype(meadow_self_a19f31c):
        return _name_boundary.attributes(meadow_self_a19f31c)['base_type']

    @_name_boundary.callable_contract({'self': 'meadow_self_511bfb7', 'full': 'meadow_full_a9e8e40'}, 'get_realtype')
    def meadow_get_realtype(meadow_self_511bfb7, meadow_full_a9e8e40=True):
        if meadow_full_a9e8e40:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_511bfb7)['get_final_tinfo']())['get_decltype']()
        return _name_boundary.attributes(meadow_self_511bfb7)['get_decltype']()

    @_name_boundary.callable_contract({'self': 'meadow_self_8731d5f'}, 'is_decl_typedef')
    def meadow_is_decl_typedef(meadow_self_8731d5f):
        return meadow_is_type_typedef(_name_boundary.attributes(meadow_self_8731d5f)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_67092ce'}, 'is_decl_array')
    def meadow_is_decl_array(meadow_self_67092ce):
        return meadow_is_type_array(_name_boundary.attributes(meadow_self_67092ce)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_27fcfff'}, 'is_decl_bitfield')
    def meadow_is_decl_bitfield(meadow_self_27fcfff):
        return meadow_is_type_bitfld(_name_boundary.attributes(meadow_self_27fcfff)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_6e4cc17'}, 'is_decl_bool')
    def meadow_is_decl_bool(meadow_self_6e4cc17):
        return meadow_is_type_bool(_name_boundary.attributes(meadow_self_6e4cc17)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_917a7d0'}, 'is_decl_char')
    def meadow_is_decl_char(meadow_self_917a7d0):
        return meadow_is_type_char(_name_boundary.attributes(meadow_self_917a7d0)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_7d82646'}, 'is_decl_complex')
    def meadow_is_decl_complex(meadow_self_7d82646):
        return meadow_is_type_complex(_name_boundary.attributes(meadow_self_7d82646)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_435b598'}, 'is_decl_const')
    def meadow_is_decl_const(meadow_self_435b598):
        return meadow_is_type_const(_name_boundary.attributes(meadow_self_435b598)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_9f0a21f'}, 'is_decl_double')
    def meadow_is_decl_double(meadow_self_9f0a21f):
        return meadow_is_type_double(_name_boundary.attributes(meadow_self_9f0a21f)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_0bbfaa4'}, 'is_decl_enum')
    def meadow_is_decl_enum(meadow_self_0bbfaa4):
        return meadow_is_type_enum(_name_boundary.attributes(meadow_self_0bbfaa4)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_fac2ca8'}, 'is_decl_float')
    def meadow_is_decl_float(meadow_self_fac2ca8):
        return meadow_is_type_float(_name_boundary.attributes(meadow_self_fac2ca8)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_c93b2d3'}, 'is_decl_floating')
    def meadow_is_decl_floating(meadow_self_c93b2d3):
        return meadow_is_type_floating(_name_boundary.attributes(meadow_self_c93b2d3)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_bd033b3'}, 'is_decl_func')
    def meadow_is_decl_func(meadow_self_bd033b3):
        return meadow_is_type_func(_name_boundary.attributes(meadow_self_bd033b3)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_8effa9c'}, 'is_decl_int')
    def meadow_is_decl_int(meadow_self_8effa9c):
        return meadow_is_type_int(_name_boundary.attributes(meadow_self_8effa9c)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_42e1e48'}, 'is_decl_int128')
    def meadow_is_decl_int128(meadow_self_42e1e48):
        return meadow_is_type_int128(_name_boundary.attributes(meadow_self_42e1e48)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_2b98cea'}, 'is_decl_int16')
    def meadow_is_decl_int16(meadow_self_2b98cea):
        return meadow_is_type_int16(_name_boundary.attributes(meadow_self_2b98cea)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_fdda69c'}, 'is_decl_int32')
    def meadow_is_decl_int32(meadow_self_fdda69c):
        return meadow_is_type_int32(_name_boundary.attributes(meadow_self_fdda69c)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_a20c9b6'}, 'is_decl_int64')
    def meadow_is_decl_int64(meadow_self_a20c9b6):
        return meadow_is_type_int64(_name_boundary.attributes(meadow_self_a20c9b6)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_76aa778'}, 'is_decl_paf')
    def meadow_is_decl_paf(meadow_self_76aa778):
        return meadow_is_type_paf(_name_boundary.attributes(meadow_self_76aa778)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_2ac5f97'}, 'is_decl_partial')
    def meadow_is_decl_partial(meadow_self_2ac5f97):
        return meadow_is_type_partial(_name_boundary.attributes(meadow_self_2ac5f97)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_7d7cd22'}, 'is_decl_ptr')
    def meadow_is_decl_ptr(meadow_self_7d7cd22):
        return meadow_is_type_ptr(_name_boundary.attributes(meadow_self_7d7cd22)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_0b3d7c2'}, 'is_decl_ptr_or_array')
    def meadow_is_decl_ptr_or_array(meadow_self_0b3d7c2):
        return meadow_is_type_ptr_or_array(_name_boundary.attributes(meadow_self_0b3d7c2)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_7281e9e'}, 'is_decl_struct')
    def meadow_is_decl_struct(meadow_self_7281e9e):
        return meadow_is_type_struct(_name_boundary.attributes(meadow_self_7281e9e)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_08abba3'}, 'is_decl_sue')
    def meadow_is_decl_sue(meadow_self_08abba3):
        return meadow_is_type_sue(_name_boundary.attributes(meadow_self_08abba3)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_06ba9bb'}, 'is_decl_uchar')
    def meadow_is_decl_uchar(meadow_self_06ba9bb):
        return meadow_is_type_uchar(_name_boundary.attributes(meadow_self_06ba9bb)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_20acee8'}, 'is_decl_udt')
    def meadow_is_decl_udt(meadow_self_20acee8):
        return meadow_is_type_struni(_name_boundary.attributes(meadow_self_20acee8)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_871968f'}, 'is_decl_uint')
    def meadow_is_decl_uint(meadow_self_871968f):
        return meadow_is_type_uint(_name_boundary.attributes(meadow_self_871968f)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_9425063'}, 'is_decl_uint128')
    def meadow_is_decl_uint128(meadow_self_9425063):
        return meadow_is_type_uint128(_name_boundary.attributes(meadow_self_9425063)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_e501b51'}, 'is_decl_uint16')
    def meadow_is_decl_uint16(meadow_self_e501b51):
        return meadow_is_type_uint16(_name_boundary.attributes(meadow_self_e501b51)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_56276b5'}, 'is_decl_uint32')
    def meadow_is_decl_uint32(meadow_self_56276b5):
        return meadow_is_type_uint32(_name_boundary.attributes(meadow_self_56276b5)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_8c39883'}, 'is_decl_uint64')
    def meadow_is_decl_uint64(meadow_self_8c39883):
        return meadow_is_type_uint64(_name_boundary.attributes(meadow_self_8c39883)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_4f75ba8'}, 'is_decl_union')
    def meadow_is_decl_union(meadow_self_4f75ba8):
        return meadow_is_type_union(_name_boundary.attributes(meadow_self_4f75ba8)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_8c98436'}, 'is_decl_unknown')
    def meadow_is_decl_unknown(meadow_self_8c98436):
        return meadow_is_type_unknown(_name_boundary.attributes(meadow_self_8c98436)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_00388dd'}, 'is_decl_void')
    def meadow_is_decl_void(meadow_self_00388dd):
        return meadow_is_type_void(_name_boundary.attributes(meadow_self_00388dd)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_741fdff'}, 'is_decl_volatile')
    def meadow_is_decl_volatile(meadow_self_741fdff):
        return meadow_is_type_volatile(_name_boundary.attributes(meadow_self_741fdff)['get_decltype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_f84a17c'}, 'is_arithmetic')
    def meadow_is_arithmetic(meadow_self_f84a17c):
        return meadow_is_type_arithmetic(_name_boundary.attributes(meadow_self_f84a17c)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_85077fc'}, 'is_array')
    def meadow_is_array(meadow_self_85077fc):
        return meadow_is_type_array(_name_boundary.attributes(meadow_self_85077fc)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_db153e8'}, 'is_bitfield')
    def meadow_is_bitfield(meadow_self_db153e8):
        return meadow_is_type_bitfld(_name_boundary.attributes(meadow_self_db153e8)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_653246a'}, 'is_bool')
    def meadow_is_bool(meadow_self_653246a):
        return meadow_is_type_bool(_name_boundary.attributes(meadow_self_653246a)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_faaa4ff', 'target': 'meadow_target_a1f9015'}, 'is_castable_to')
    def meadow_is_castable_to(meadow_self_faaa4ff, meadow_target_a1f9015):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_d8f1e56'}, 'is_char')
    def meadow_is_char(meadow_self_d8f1e56):
        return meadow_is_type_char(_name_boundary.attributes(meadow_self_d8f1e56)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_2f1b9d2'}, 'is_complex')
    def meadow_is_complex(meadow_self_2f1b9d2):
        return meadow_is_type_complex(_name_boundary.attributes(meadow_self_2f1b9d2)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_e1932ee'}, 'is_const')
    def meadow_is_const(meadow_self_e1932ee):
        return meadow_is_type_const(_name_boundary.attributes(meadow_self_e1932ee)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_78f0a11'}, 'is_correct')
    def meadow_is_correct(meadow_self_78f0a11):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_51550bd'}, 'is_double')
    def meadow_is_double(meadow_self_51550bd):
        return meadow_is_type_double(_name_boundary.attributes(meadow_self_51550bd)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_2095524'}, 'is_empty_udt')
    def meadow_is_empty_udt(meadow_self_2095524):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_1f51118'}, 'is_enum')
    def meadow_is_enum(meadow_self_1f51118):
        return meadow_is_type_enum(_name_boundary.attributes(meadow_self_1f51118)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_205450f'}, 'is_ext_arithmetic')
    def meadow_is_ext_arithmetic(meadow_self_205450f):
        return meadow_is_type_ext_arithmetic(_name_boundary.attributes(meadow_self_205450f)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_6e119ce'}, 'is_ext_integral')
    def meadow_is_ext_integral(meadow_self_6e119ce):
        return meadow_is_type_ext_integral(_name_boundary.attributes(meadow_self_6e119ce)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_466120e'}, 'is_float')
    def meadow_is_float(meadow_self_466120e):
        return meadow_is_type_float(_name_boundary.attributes(meadow_self_466120e)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_7978dbd'}, 'is_floating')
    def meadow_is_floating(meadow_self_7978dbd):
        return meadow_is_type_floating(_name_boundary.attributes(meadow_self_7978dbd)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_5f85fe4'}, 'is_forward_decl')
    def meadow_is_forward_decl(meadow_self_5f85fe4):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_89ee4e7'}, 'is_from_subtil')
    def meadow_is_from_subtil(meadow_self_89ee4e7):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_e475072'}, 'is_func')
    def meadow_is_func(meadow_self_e475072):
        return meadow_is_type_func(_name_boundary.attributes(meadow_self_e475072)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_ed3c38f'}, 'is_funcptr')
    def meadow_is_funcptr(meadow_self_ed3c38f):
        if not _name_boundary.attributes(meadow_self_ed3c38f)['is_decl_ptr']():
            return False
        meadow_typ_local_c7065aa = _name_boundary.attributes(meadow_self_ed3c38f)['get_pointed_object']()
        while _name_boundary.attributes(meadow_typ_local_c7065aa)['is_decl_ptr']():
            meadow_typ_local_c7065aa = _name_boundary.attributes(meadow_typ_local_c7065aa)['get_pointed_object']()
        return _name_boundary.attributes(meadow_typ_local_c7065aa)['is_decl_func']()

    @_name_boundary.callable_contract({'self': 'meadow_self_668287b'}, 'is_high_func')
    def meadow_is_high_func(meadow_self_668287b):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_3812e5f'}, 'is_int')
    def meadow_is_int(meadow_self_3812e5f):
        return meadow_is_type_int(_name_boundary.attributes(meadow_self_3812e5f)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_2cc7173'}, 'is_int128')
    def meadow_is_int128(meadow_self_2cc7173):
        return meadow_is_type_int128(_name_boundary.attributes(meadow_self_2cc7173)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_4564adc'}, 'is_int16')
    def meadow_is_int16(meadow_self_4564adc):
        return meadow_is_type_int16(_name_boundary.attributes(meadow_self_4564adc)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_4f74767'}, 'is_int32')
    def meadow_is_int32(meadow_self_4f74767):
        return meadow_is_type_int32(_name_boundary.attributes(meadow_self_4f74767)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_bdc811f'}, 'is_int64')
    def meadow_is_int64(meadow_self_bdc811f):
        return meadow_is_type_int64(_name_boundary.attributes(meadow_self_bdc811f)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_78e5077'}, 'is_integral')
    def meadow_is_integral(meadow_self_78e5077):
        return meadow_is_type_integral(_name_boundary.attributes(meadow_self_78e5077)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_9e20f5d'}, 'is_ldouble')
    def meadow_is_ldouble(meadow_self_9e20f5d):
        return meadow_is_type_ldouble(_name_boundary.attributes(meadow_self_9e20f5d)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_869c588', 'target': 'meadow_target_9ab40dd'}, 'is_manually_castable_to')
    def meadow_is_manually_castable_to(meadow_self_869c588, meadow_target_9ab40dd):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_5f28819'}, 'is_one_fpval')
    def meadow_is_one_fpval(meadow_self_5f28819):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_7a25721'}, 'is_paf')
    def meadow_is_paf(meadow_self_7a25721):
        return meadow_is_type_paf(_name_boundary.attributes(meadow_self_7a25721)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_e170697'}, 'is_partial')
    def meadow_is_partial(meadow_self_e170697):
        return meadow_is_type_partial(_name_boundary.attributes(meadow_self_e170697)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_ee79ce9'}, 'is_ptr')
    def meadow_is_ptr(meadow_self_ee79ce9):
        return meadow_is_type_ptr(_name_boundary.attributes(meadow_self_ee79ce9)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_ec60af7'}, 'is_ptr_or_array')
    def meadow_is_ptr_or_array(meadow_self_ec60af7):
        return meadow_is_type_ptr_or_array(_name_boundary.attributes(meadow_self_ec60af7)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_38879ca'}, 'is_purging_cc')
    def meadow_is_purging_cc(meadow_self_38879ca):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_a7b18d4'}, 'is_pvoid')
    def meadow_is_pvoid(meadow_self_a7b18d4):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_2e57970'}, 'is_scalar')
    def meadow_is_scalar(meadow_self_2e57970):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_2259a15'}, 'is_shifted_ptr')
    def meadow_is_shifted_ptr(meadow_self_2259a15):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_8d17767'}, 'is_signed')
    def meadow_is_signed(meadow_self_8d17767):
        return meadow_get_type_flags(_name_boundary.attributes(meadow_self_8d17767)['get_realtype']()) == meadow_BTMT_SIGNED

    @_name_boundary.callable_contract({'self': 'meadow_self_1a5a787'}, 'is_small_udt')
    def meadow_is_small_udt(meadow_self_1a5a787):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_ce23bae'}, 'is_sse_type')
    def meadow_is_sse_type(meadow_self_ce23bae):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_24897a3'}, 'is_struct')
    def meadow_is_struct(meadow_self_24897a3):
        return meadow_is_type_struct(_name_boundary.attributes(meadow_self_24897a3)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_80292d3'}, 'is_sue')
    def meadow_is_sue(meadow_self_80292d3):
        return meadow_is_type_sue(_name_boundary.attributes(meadow_self_80292d3)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_c228413'}, 'is_uchar')
    def meadow_is_uchar(meadow_self_c228413):
        return meadow_is_type_uchar(_name_boundary.attributes(meadow_self_c228413)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_3f4a694'}, 'is_udt')
    def meadow_is_udt(meadow_self_3f4a694):
        return meadow_is_type_struni(_name_boundary.attributes(meadow_self_3f4a694)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_0f4feb2'}, 'is_uint')
    def meadow_is_uint(meadow_self_0f4feb2):
        return meadow_is_type_uint(_name_boundary.attributes(meadow_self_0f4feb2)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_cf11050'}, 'is_uint128')
    def meadow_is_uint128(meadow_self_cf11050):
        return meadow_is_type_uint128(_name_boundary.attributes(meadow_self_cf11050)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_e85e65c'}, 'is_uint16')
    def meadow_is_uint16(meadow_self_e85e65c):
        return meadow_is_type_uint16(_name_boundary.attributes(meadow_self_e85e65c)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_c1e8e0b'}, 'is_uint32')
    def meadow_is_uint32(meadow_self_c1e8e0b):
        return meadow_is_type_uint32(_name_boundary.attributes(meadow_self_c1e8e0b)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_f14e26b'}, 'is_uint64')
    def meadow_is_uint64(meadow_self_f14e26b):
        return meadow_is_type_uint64(_name_boundary.attributes(meadow_self_f14e26b)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_dcbd642'}, 'is_union')
    def meadow_is_union(meadow_self_dcbd642):
        return meadow_is_type_union(_name_boundary.attributes(meadow_self_dcbd642)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_d0e72f3'}, 'is_unknown')
    def meadow_is_unknown(meadow_self_d0e72f3):
        return meadow_is_type_unknown(_name_boundary.attributes(meadow_self_d0e72f3)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_03f83bc'}, 'is_unsigned')
    def meadow_is_unsigned(meadow_self_03f83bc):
        return meadow_get_type_flags(_name_boundary.attributes(meadow_self_03f83bc)['get_realtype']()) == meadow_BTMT_UNSIGNED

    @_name_boundary.callable_contract({'self': 'meadow_self_27e93dd'}, 'is_user_cc')
    def meadow_is_user_cc(meadow_self_27e93dd):
        return meadow_is_user_cc(_name_boundary.attributes(meadow_self_27e93dd)['get_cc']())

    @_name_boundary.callable_contract({'self': 'meadow_self_5ccbd9c'}, 'is_vararg_cc')
    def meadow_is_vararg_cc(meadow_self_5ccbd9c):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_9f5aa04'}, 'is_varstruct')
    def meadow_is_varstruct(meadow_self_9f5aa04):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_c0f0cbd'}, 'is_vftable')
    def meadow_is_vftable(meadow_self_c0f0cbd):
        raise NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_b0b40c4'}, 'is_void')
    def meadow_is_void(meadow_self_b0b40c4):
        return meadow_is_type_void(_name_boundary.attributes(meadow_self_b0b40c4)['get_realtype']())

    @_name_boundary.callable_contract({'self': 'meadow_self_07e08d4'}, 'is_volatile')
    def meadow_is_volatile(meadow_self_07e08d4):
        return meadow_is_type_volatile(_name_boundary.attributes(meadow_self_07e08d4)['get_realtype']())

@_name_boundary.class_contract('ErrorTInfo', {'get_typestr': 'meadow_get_typestr'})
class meadow_ErrorTInfo:

    @_name_boundary.callable_contract({'self': 'meadow_self_4d19426', 'name': 'meadow_name_local_d0d8d86'}, '__init__')
    def __init__(meadow_self_4d19426, meadow_name_local_d0d8d86):
        meadow_self_4d19426.name = meadow_name_local_d0d8d86

    @_name_boundary.callable_contract({'self': 'meadow_self_24cb05c', 'indent': 'meadow_indent_local_097f61f'}, 'get_typestr')
    def meadow_get_typestr(meadow_self_24cb05c, meadow_indent_local_097f61f=2):
        return '{} Error'.format(meadow_self_24cb05c.name)

@_name_boundary.callable_contract({'til': 'meadow_til_local_24f63b2', 'type_info': 'meadow_type_info_local_aa26723', 'fields': 'meadow_fields_local_a19d559', 'fieldcmts': 'meadow_fieldcmts_local_2372bd8', 'name': 'meadow_name_local_60e23dd', 'inf': 'meadow_inf_local_e14c606'}, 'create_tinfo')
def meadow_create_tinfo(meadow_til_local_24f63b2, meadow_type_info_local_aa26723, meadow_fields_local_a19d559=None, meadow_fieldcmts_local_2372bd8=None, meadow_name_local_60e23dd=None, meadow_inf_local_e14c606=None):
    meadow_type_string_cfd6888 = meadow_type_info_local_aa26723 if isinstance(meadow_type_info_local_aa26723, meadow_TypeString) else meadow_TypeString(meadow_type_info_local_aa26723)
    meadow_typ_local_741d9d5 = _name_boundary.attributes(meadow_type_string_cfd6888)['peek_u8']()
    meadow_tinfo_381c0d7 = meadow_TInfo(meadow_typ_local_741d9d5, til=meadow_til_local_24f63b2, name=meadow_name_local_60e23dd, inf=meadow_inf_local_e14c606)
    if meadow_is_typeid_last(meadow_typ_local_741d9d5) or meadow_get_base_type(meadow_typ_local_741d9d5) == meadow_BT_RESERVED:
        _name_boundary.attributes(meadow_type_string_cfd6888)['seek'](1)
    else:
        meadow_type_data_f6ecc71 = None
        if meadow_is_type_ptr(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_PointerTypeData()
        elif meadow_is_type_func(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_FuncTypeData()
        elif meadow_is_type_array(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_ArrayTypeData()
        elif meadow_is_type_typedef(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_TypedefTypeData()
        elif meadow_is_type_struni(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_UdtTypeData()
        elif meadow_is_type_enum(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_EnumTypeData()
        elif meadow_is_type_bitfld(meadow_typ_local_741d9d5):
            meadow_type_data_f6ecc71 = meadow_BitfieldTypeData()
        _name_boundary.attributes(meadow_type_data_f6ecc71)['deserialize'](meadow_til_local_24f63b2, meadow_type_string_cfd6888, meadow_fields_local_a19d559, meadow_fieldcmts_local_2372bd8)
        _name_boundary.attributes(meadow_tinfo_381c0d7)['type_details'] = meadow_type_data_f6ecc71
    return meadow_tinfo_381c0d7

@_name_boundary.callable_contract({'til': 'meadow_til_local_13033a5', 'type_info': 'meadow_type_info_local_cda5d5e', 'inf': 'meadow_inf_local_ba7bc57'}, 'create_ref')
def meadow_create_ref(meadow_til_local_13033a5, meadow_type_info_local_cda5d5e, meadow_inf_local_ba7bc57=None):
    if not meadow_type_info_local_cda5d5e.startswith(b'='):
        meadow_type_info_local_cda5d5e = b'=' + meadow_serialize_dt(len(meadow_type_info_local_cda5d5e)) + meadow_type_info_local_cda5d5e
    return meadow_create_tinfo(meadow_til_local_13033a5, meadow_type_info_local_cda5d5e, inf=meadow_inf_local_ba7bc57)

@_name_boundary.class_contract('PointerTypeData', {'deserialize': 'meadow_deserialize', 'obj_type': 'meadow_obj_type', 'closure': 'meadow_closure', 'based_ptr_size': 'meadow_based_ptr_size', 'taptr_bits': 'meadow_taptr_bits'})
class meadow_PointerTypeData(meadow_TypeData):
    """Representation of ptr_type_data_t"""

    @_name_boundary.callable_contract({'self': 'meadow_self_89ef4c0'}, '__init__')
    def __init__(meadow_self_89ef4c0):
        meadow_TypeData.__init__(meadow_self_89ef4c0)
        _name_boundary.attributes(meadow_self_89ef4c0)['obj_type'] = None
        _name_boundary.attributes(meadow_self_89ef4c0)['closure'] = None
        _name_boundary.attributes(meadow_self_89ef4c0)['based_ptr_size'] = 0
        _name_boundary.attributes(meadow_self_89ef4c0)['taptr_bits'] = 0

    @_name_boundary.callable_contract({'self': 'meadow_self_70b48f8', 'ts': 'meadow_ts_fb00902', 'til': 'meadow_til_local_f4627e2', 'fields': 'meadow_fields_local_70defdc', 'fieldcmts': 'meadow_fieldcmts_local_b705a06'}, 'deserialize')
    def meadow_deserialize(meadow_self_70b48f8, meadow_til_local_f4627e2, meadow_ts_fb00902, meadow_fields_local_70defdc, meadow_fieldcmts_local_b705a06):
        meadow_typ_local_23b0fa8 = meadow_ts_fb00902.u8()
        if meadow_is_type_closure(meadow_typ_local_23b0fa8):
            if meadow_ts_fb00902.u8() == meadow_RESERVED_BYTE:
                _name_boundary.attributes(meadow_self_70b48f8)['closure'] = meadow_create_tinfo(meadow_til_local_f4627e2, _name_boundary.attributes(meadow_ts_fb00902)['ref']())
            else:
                _name_boundary.attributes(meadow_self_70b48f8)['based_ptr_size'] = meadow_ts_fb00902.u8()
        _name_boundary.attributes(meadow_self_70b48f8)['taptr_bits'] = _name_boundary.attributes(meadow_ts_fb00902)['tah_attr']()
        _name_boundary.attributes(meadow_self_70b48f8)['obj_type'] = meadow_create_tinfo(meadow_til_local_f4627e2, _name_boundary.attributes(meadow_ts_fb00902)['ref'](), meadow_fields_local_70defdc, meadow_fieldcmts_local_b705a06)
        return meadow_self_70b48f8

@_name_boundary.class_contract('ArrayTypeData', {'deserialize': 'meadow_deserialize', 'elem_type': 'meadow_elem_type', 'n_elems': 'meadow_n_elems'})
class meadow_ArrayTypeData(meadow_TypeData):

    @_name_boundary.callable_contract({'self': 'meadow_self_8941be0'}, '__init__')
    def __init__(meadow_self_8941be0):
        meadow_TypeData.__init__(meadow_self_8941be0)
        _name_boundary.attributes(meadow_self_8941be0)['elem_type'] = None
        meadow_self_8941be0.base = None
        _name_boundary.attributes(meadow_self_8941be0)['n_elems'] = 0

    @_name_boundary.callable_contract({'self': 'meadow_self_00f3d0a', 'ts': 'meadow_ts_e60cb6b', 'til': 'meadow_til_local_742577a', 'fields': 'meadow_fields_local_d0aee8e', 'fieldcmts': 'meadow_fieldcmts_local_bcdf49d'}, 'deserialize')
    def meadow_deserialize(meadow_self_00f3d0a, meadow_til_local_742577a, meadow_ts_e60cb6b, meadow_fields_local_d0aee8e, meadow_fieldcmts_local_bcdf49d):
        meadow_typ_local_e221a25 = meadow_ts_e60cb6b.u8()
        if meadow_get_type_flags(meadow_typ_local_e221a25) & meadow_BTMT_NONBASED:
            meadow_self_00f3d0a.base = 0
            _name_boundary.attributes(meadow_self_00f3d0a)['n_elems'] = _name_boundary.attributes(meadow_ts_e60cb6b)['dt']()
        else:
            meadow___a9bd992, _name_boundary.attributes(meadow_self_00f3d0a)['n_elems'], meadow_self_00f3d0a.base = meadow_ts_e60cb6b.da()
        _name_boundary.attributes(meadow_ts_e60cb6b)['tah_attr']()
        _name_boundary.attributes(meadow_self_00f3d0a)['elem_type'] = meadow_create_tinfo(meadow_til_local_742577a, _name_boundary.attributes(meadow_ts_e60cb6b)['ref'](), meadow_fields_local_d0aee8e, meadow_fieldcmts_local_bcdf49d)
        return meadow_self_00f3d0a

@_name_boundary.class_contract('FuncArg', {'argloc': 'meadow_argloc'})
class meadow_FuncArg:

    @_name_boundary.callable_contract({'self': 'meadow_self_8da854c'}, '__init__')
    def __init__(meadow_self_8da854c):
        _name_boundary.attributes(meadow_self_8da854c)['argloc'] = None
        meadow_self_8da854c.name = ''
        meadow_self_8da854c.cmt = ''
        meadow_self_8da854c.type = None
        meadow_self_8da854c.flags = 0

@_name_boundary.class_contract('RRel', {'off': 'meadow_off', 'reg': 'meadow_reg'})
class meadow_RRel:

    @_name_boundary.callable_contract({'self': 'meadow_self_3a1531d'}, '__init__')
    def __init__(meadow_self_3a1531d):
        _name_boundary.attributes(meadow_self_3a1531d)['off'] = 0
        _name_boundary.attributes(meadow_self_3a1531d)['reg'] = 0

@_name_boundary.class_contract('ArgLoc', {'get_reg1': 'meadow_get_reg1', 'get_reg2': 'meadow_get_reg2', 'get_reginfo': 'meadow_get_reginfo', 'get_stkoff': 'meadow_get_stkoff', 'sval': 'meadow_sval', 'reginfo': 'meadow_reginfo', 'rrel': 'meadow_rrel', 'dist': 'meadow_dist', 'custom': 'meadow_custom', 'biggest': 'meadow_biggest'})
class meadow_ArgLoc:

    @_name_boundary.callable_contract({'self': 'meadow_self_4bd6f14'}, '__init__')
    def __init__(meadow_self_4bd6f14):
        meadow_self_4bd6f14.type = 0
        _name_boundary.attributes(meadow_self_4bd6f14)['sval'] = 0
        _name_boundary.attributes(meadow_self_4bd6f14)['reginfo'] = 0
        _name_boundary.attributes(meadow_self_4bd6f14)['rrel'] = None
        _name_boundary.attributes(meadow_self_4bd6f14)['dist'] = []
        _name_boundary.attributes(meadow_self_4bd6f14)['custom'] = None
        _name_boundary.attributes(meadow_self_4bd6f14)['biggest'] = None

    @_name_boundary.callable_contract({'self': 'meadow_self_a2c9d55'}, 'get_reg1')
    def meadow_get_reg1(meadow_self_a2c9d55):
        return _name_boundary.attributes(meadow_self_a2c9d55)['reginfo'] & 65535

    @_name_boundary.callable_contract({'self': 'meadow_self_0f124e4'}, 'get_reg2')
    def meadow_get_reg2(meadow_self_0f124e4):
        return _name_boundary.attributes(meadow_self_0f124e4)['reginfo'] >> 16 & 65535

    @_name_boundary.callable_contract({'self': 'meadow_self_02eab67'}, 'get_reginfo')
    def meadow_get_reginfo(meadow_self_02eab67):
        return _name_boundary.attributes(meadow_self_02eab67)['reginfo']

    @_name_boundary.callable_contract({'self': 'meadow_self_202b028'}, 'get_stkoff')
    def meadow_get_stkoff(meadow_self_202b028):
        return _name_boundary.attributes(meadow_self_202b028)['sval']

@_name_boundary.class_contract('ArgPart', {'off': 'meadow_off'})
class meadow_ArgPart(meadow_ArgLoc):

    @_name_boundary.callable_contract({'self': 'meadow_self_689ea27'}, '__init__')
    def __init__(meadow_self_689ea27):
        meadow_ArgLoc.__init__(meadow_self_689ea27)
        _name_boundary.attributes(meadow_self_689ea27)['off'] = 0
        meadow_self_689ea27.size = 0

@_name_boundary.callable_contract({'ind': 'meadow_ind_58b2b2a'}, 'print_reg')
def meadow_print_reg(meadow_ind_58b2b2a):
    global meadow_global_inf
    meadow_regs_31beda6 = meadow_REGS[meadow_global_inf.procname] if meadow_global_inf is not None else meadow_REGS_METAPC
    meadow_r_267cb88 = meadow_regs_31beda6[meadow_ind_58b2b2a] if meadow_ind_58b2b2a < len(meadow_regs_31beda6) else None
    return 'R{}'.format(meadow_ind_58b2b2a) if meadow_r_267cb88 is None else meadow_r_267cb88

@_name_boundary.callable_contract({'argloc': 'meadow_argloc_0edf079'}, 'print_argloc')
def meadow_print_argloc(meadow_argloc_0edf079):
    meadow_typ_local_829db65 = meadow_argloc_0edf079.type
    meadow_t_3fd2c01 = ''
    if meadow_typ_local_829db65 in (meadow_ALOC_STATIC, meadow_ALOC_STACK):
        return None
    elif meadow_typ_local_829db65 == meadow_ALOC_REG1:
        meadow_t_3fd2c01 += meadow_print_reg(_name_boundary.attributes(meadow_argloc_0edf079)['get_reg1']())
    elif meadow_typ_local_829db65 == meadow_ALOC_REG2:
        meadow_t_3fd2c01 += '{}:{}'.format(meadow_print_reg(_name_boundary.attributes(meadow_argloc_0edf079)['get_reg2']()), meadow_print_reg(_name_boundary.attributes(meadow_argloc_0edf079)['get_reg1']()))
    elif meadow_typ_local_829db65 == meadow_ALOC_DIST:
        meadow_dst_9020e50 = []
        for meadow_d_4b2ffb8 in _name_boundary.attributes(meadow_argloc_0edf079)['dist']:
            meadow_dst_9020e50.append('{}:{}'.format(_name_boundary.attributes(meadow_d_4b2ffb8)['off'], meadow_print_argloc(meadow_d_4b2ffb8)))
        meadow_t_3fd2c01 += ', '.join(meadow_dst_9020e50)
    else:
        raise NotImplementedError
    return meadow_t_3fd2c01

@_name_boundary.class_contract('RegInfo', {'reg': 'meadow_reg'})
class meadow_RegInfo:

    @_name_boundary.callable_contract({'self': 'meadow_self_5d740cb'}, '__init__')
    def __init__(meadow_self_5d740cb):
        _name_boundary.attributes(meadow_self_5d740cb)['reg'] = 0
        meadow_self_5d740cb.size = 0

@_name_boundary.class_contract('FuncTypeData', {'deserialize': 'meadow_deserialize', 'deserialize_argloc': 'meadow_deserialize_argloc', 'args': 'meadow_args', 'rettype': 'meadow_rettype', 'retloc': 'meadow_retloc', 'stkargs': 'meadow_stkargs', 'spoiled': 'meadow_spoiled', 'cc': 'meadow_cc'})
class meadow_FuncTypeData(meadow_TypeData):

    @_name_boundary.callable_contract({'self': 'meadow_self_87aee00'}, '__init__')
    def __init__(meadow_self_87aee00):
        meadow_TypeData.__init__(meadow_self_87aee00)
        _name_boundary.attributes(meadow_self_87aee00)['args'] = []
        meadow_self_87aee00.flags = 0
        _name_boundary.attributes(meadow_self_87aee00)['rettype'] = None
        _name_boundary.attributes(meadow_self_87aee00)['retloc'] = None
        _name_boundary.attributes(meadow_self_87aee00)['stkargs'] = None
        _name_boundary.attributes(meadow_self_87aee00)['spoiled'] = []
        _name_boundary.attributes(meadow_self_87aee00)['cc'] = 0

    @_name_boundary.callable_contract({'self': 'meadow_self_6ab873b', 'ts': 'meadow_ts_d52ec96', 'til': 'meadow_til_local_95ffd2a', 'fields': 'meadow_fields_local_e1b1073', 'fieldcmts': 'meadow_fieldcmts_local_cc6ec7e'}, 'deserialize')
    def meadow_deserialize(meadow_self_6ab873b, meadow_til_local_95ffd2a, meadow_ts_d52ec96, meadow_fields_local_e1b1073, meadow_fieldcmts_local_cc6ec7e):
        meadow_typ_local_d10822c = meadow_ts_d52ec96.u8()
        meadow_self_6ab873b.flags |= 4 * meadow_get_type_flags(meadow_typ_local_d10822c)
        meadow_cm_local_648f9d9 = _name_boundary.attributes(meadow_ts_d52ec96)['peek_u8']()
        if meadow_is_cc_spoiled(meadow_cm_local_648f9d9):
            while meadow_is_cc_spoiled(meadow_cm_local_648f9d9):
                _name_boundary.attributes(meadow_ts_d52ec96)['seek'](1)
                meadow_nspoiled_0c933ca = meadow_cm_local_648f9d9 & ~meadow_CM_CC_MASK
                if meadow_nspoiled_0c933ca == 15:
                    meadow_f_e52f8e7 = 2 * (meadow_ts_d52ec96.u8() & 31)
                else:
                    for meadow_n_2069964 in range(meadow_nspoiled_0c933ca):
                        meadow_reginfo_73bff35 = meadow_RegInfo()
                        meadow_b_local_edf18d4 = meadow_ts_d52ec96.read_db()
                        if bool(meadow_b_local_edf18d4 & 128):
                            meadow_size_local_99a6dcf = meadow_ts_d52ec96.u8()
                            meadow_reg_247a77d = meadow_b_local_edf18d4 & 127
                        else:
                            meadow_size_local_99a6dcf = (meadow_b_local_edf18d4 >> 4) + 1
                            meadow_reg_247a77d = (meadow_b_local_edf18d4 & 15) - 1
                        meadow_reginfo_73bff35.size = meadow_size_local_99a6dcf
                        _name_boundary.attributes(meadow_reginfo_73bff35)['reg'] = meadow_reg_247a77d
                        _name_boundary.attributes(meadow_self_6ab873b)['spoiled'].append(meadow_reginfo_73bff35)
                    meadow_f_e52f8e7 = 1
                meadow_cm_local_648f9d9 = _name_boundary.attributes(meadow_ts_d52ec96)['peek_u8']()
                meadow_self_6ab873b.flags |= meadow_f_e52f8e7
        _name_boundary.attributes(meadow_self_6ab873b)['cc'] = meadow_ts_d52ec96.u8()
        _name_boundary.attributes(meadow_ts_d52ec96)['tah_attr']()
        _name_boundary.attributes(meadow_self_6ab873b)['rettype'] = meadow_create_tinfo(meadow_til_local_95ffd2a, _name_boundary.attributes(meadow_ts_d52ec96)['ref'](), meadow_fields_local_e1b1073, meadow_fieldcmts_local_cc6ec7e)
        if meadow_is_cm_cc_special_pe(_name_boundary.attributes(meadow_self_6ab873b)['cc']) and (not _name_boundary.attributes(_name_boundary.attributes(meadow_self_6ab873b)['rettype'])['is_void']()):
            _name_boundary.attributes(meadow_self_6ab873b)['retloc'] = _name_boundary.attributes(meadow_self_6ab873b)['deserialize_argloc'](_name_boundary.attributes(meadow_ts_d52ec96)['ref']())
        if meadow_is_cm_cc_voidarg(_name_boundary.attributes(meadow_self_6ab873b)['cc']):
            return meadow_self_6ab873b
        meadow_n_2069964 = _name_boundary.attributes(meadow_ts_d52ec96)['dt']()
        for meadow_i_a54267e in range(meadow_n_2069964):
            meadow_arg_ecf51de = meadow_FuncArg()
            if _name_boundary.attributes(meadow_ts_d52ec96)['has_next']() and _name_boundary.attributes(meadow_ts_d52ec96)['peek_u8']() == meadow_FAH_BYTE:
                _name_boundary.attributes(meadow_ts_d52ec96)['seek'](1)
                meadow_arg_ecf51de.flags = _name_boundary.attributes(meadow_ts_d52ec96)['de']()
            if meadow_fields_local_e1b1073 is not None and meadow_i_a54267e < len(meadow_fields_local_e1b1073):
                meadow_arg_ecf51de.name = meadow_fields_local_e1b1073[meadow_i_a54267e]
            if meadow_fieldcmts_local_cc6ec7e is not None and meadow_i_a54267e < len(meadow_fieldcmts_local_cc6ec7e):
                meadow_arg_ecf51de.cmt = meadow_fieldcmts_local_cc6ec7e[meadow_i_a54267e]
            meadow_arg_ecf51de.type = meadow_create_tinfo(meadow_til_local_95ffd2a, _name_boundary.attributes(meadow_ts_d52ec96)['ref'](), meadow_fields_local_e1b1073, meadow_fieldcmts_local_cc6ec7e)
            if meadow_is_cm_cc_special_pe(_name_boundary.attributes(meadow_self_6ab873b)['cc']):
                _name_boundary.attributes(meadow_arg_ecf51de)['argloc'] = _name_boundary.attributes(meadow_self_6ab873b)['deserialize_argloc'](_name_boundary.attributes(meadow_ts_d52ec96)['ref']())
            _name_boundary.attributes(meadow_self_6ab873b)['args'].append(meadow_arg_ecf51de)
        return meadow_self_6ab873b

    @_name_boundary.callable_contract({'self': 'meadow_self_f958cd5', 'ts': 'meadow_ts_dad41f6'}, 'deserialize_argloc')
    def meadow_deserialize_argloc(meadow_self_f958cd5, meadow_ts_dad41f6):
        meadow_argloc_0d69f50 = meadow_ArgLoc()
        meadow_t_affbf36 = meadow_ts_dad41f6.u8()
        if meadow_t_affbf36 == 255:
            meadow_typ_local_fd45293 = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
            meadow_typ0_39980a2 = meadow_typ_local_fd45293 & 15
            meadow_argloc_0d69f50.type = meadow_typ0_39980a2
            if meadow_typ0_39980a2 in (meadow_ALOC_STACK, meadow_ALOC_STATIC):
                _name_boundary.attributes(meadow_argloc_0d69f50)['sval'] = _name_boundary.attributes(meadow_ts_dad41f6)['de']()
            elif meadow_typ0_39980a2 == meadow_ALOC_DIST:
                meadow_N_31f1cca = meadow_typ_local_fd45293 >> 5 & 7
                for meadow___a66e012 in range(meadow_N_31f1cca):
                    meadow_argpart_b24d7d3 = meadow_ArgPart()
                    meadow_argpart_b24d7d3.type = meadow_ALOC_REG1
                    _name_boundary.attributes(meadow_argpart_b24d7d3)['reginfo'] = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
                    _name_boundary.attributes(meadow_argpart_b24d7d3)['off'] = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
                    meadow_argpart_b24d7d3.size = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
                    _name_boundary.attributes(meadow_argloc_0d69f50)['dist'].append(meadow_argpart_b24d7d3)
            elif meadow_typ0_39980a2 == meadow_ALOC_REG1:
                _name_boundary.attributes(meadow_argloc_0d69f50)['reginfo'] = _name_boundary.attributes(meadow_ts_dad41f6)['dt']() | _name_boundary.attributes(meadow_ts_dad41f6)['dt'] << 256
            elif meadow_typ0_39980a2 == meadow_ALOC_REG2:
                _name_boundary.attributes(meadow_argloc_0d69f50)['reginfo'] = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
            elif meadow_typ0_39980a2 == meadow_ALOC_RREL:
                meadow_rrel_31a5fbb = meadow_RRel()
                _name_boundary.attributes(meadow_rrel_31a5fbb)['reg'] = _name_boundary.attributes(meadow_ts_dad41f6)['dt']()
                _name_boundary.attributes(meadow_rrel_31a5fbb)['off'] = _name_boundary.attributes(meadow_ts_dad41f6)['de']()
                _name_boundary.attributes(meadow_argloc_0d69f50)['rrel'] = meadow_rrel_31a5fbb
            elif meadow_typ0_39980a2 == meadow_ALOC_CUSTOM:
                raise NotImplementedError
        else:
            meadow_b_local_a99bb31 = (meadow_t_affbf36 & 127) - 1
            if meadow_t_affbf36 <= 128:
                if meadow_b_local_a99bb31 >= 0:
                    meadow_argloc_0d69f50.type = meadow_ALOC_REG1
                    _name_boundary.attributes(meadow_argloc_0d69f50)['reginfo'] = meadow_b_local_a99bb31
                else:
                    meadow_argloc_0d69f50.type = meadow_ALOC_STACK
            else:
                meadow_c_local_f693bf1 = meadow_ts_dad41f6.u8() - 1
                if meadow_c_local_f693bf1 != -1:
                    meadow_argloc_0d69f50.type = meadow_ALOC_REG2
                    _name_boundary.attributes(meadow_argloc_0d69f50)['reginfo'] = meadow_b_local_a99bb31 | meadow_c_local_f693bf1 << 16
        return meadow_argloc_0d69f50
meadow_TAFLD_BASECLASS = 32
meadow_TAFLD_UNALIGNED = 64
meadow_TAFLD_VIRTBASE = 128

@_name_boundary.class_contract('UdtMember', {'is_unaligned': 'meadow_is_unaligned', 'is_baseclass': 'meadow_is_baseclass', 'is_virtbase': 'meadow_is_virtbase', 'effalign': 'meadow_effalign', 'tafld_bits': 'meadow_tafld_bits', 'fda': 'meadow_fda'})
class meadow_UdtMember:

    @_name_boundary.callable_contract({'self': 'meadow_self_ef5d262'}, '__init__')
    def __init__(meadow_self_ef5d262):
        meadow_self_ef5d262.offset = 0
        meadow_self_ef5d262.size = 0
        meadow_self_ef5d262.name = ''
        meadow_self_ef5d262.cmt = ''
        meadow_self_ef5d262.type = None
        _name_boundary.attributes(meadow_self_ef5d262)['effalign'] = 0
        _name_boundary.attributes(meadow_self_ef5d262)['tafld_bits'] = 0
        _name_boundary.attributes(meadow_self_ef5d262)['fda'] = 0

    @_name_boundary.callable_contract({'self': 'meadow_self_f0803f3'}, 'is_unaligned')
    def meadow_is_unaligned(meadow_self_f0803f3):
        return bool(_name_boundary.attributes(meadow_self_f0803f3)['tafld_bits'] & meadow_TAFLD_UNALIGNED)

    @_name_boundary.callable_contract({'self': 'meadow_self_c28fb36'}, 'is_baseclass')
    def meadow_is_baseclass(meadow_self_c28fb36):
        return bool(_name_boundary.attributes(meadow_self_c28fb36)['tafld_bits'] & meadow_TAFLD_BASECLASS)

    @_name_boundary.callable_contract({'self': 'meadow_self_d212d2b'}, 'is_virtbase')
    def meadow_is_virtbase(meadow_self_d212d2b):
        return bool(_name_boundary.attributes(meadow_self_d212d2b)['tafld_bits'] & meadow_TAFLD_VIRTBASE)
meadow_TAUDT_UNALIGNED = 64
meadow_TAUDT_MSSTRUCT = 32
meadow_TAUDT_CPPOBJ = 128

@_name_boundary.class_contract('UdtTypeData', {'deserialize': 'meadow_deserialize', 'members': 'meadow_members', 'total_size': 'meadow_total_size', 'unpadded_size': 'meadow_unpadded_size', 'effalign': 'meadow_effalign', 'taudt_bits': 'meadow_taudt_bits', 'sda': 'meadow_sda', 'pack': 'meadow_pack', 'is_union': 'meadow_is_union', 'ref': 'meadow_ref'})
class meadow_UdtTypeData(meadow_TypeData):
    """An object to represent struct or union types"""

    @_name_boundary.callable_contract({'self': 'meadow_self_9ae0575'}, '__init__')
    def __init__(meadow_self_9ae0575):
        meadow_TypeData.__init__(meadow_self_9ae0575)
        _name_boundary.attributes(meadow_self_9ae0575)['members'] = []
        _name_boundary.attributes(meadow_self_9ae0575)['total_size'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['unpadded_size'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['effalign'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['taudt_bits'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['sda'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['pack'] = 0
        _name_boundary.attributes(meadow_self_9ae0575)['is_union'] = False
        _name_boundary.attributes(meadow_self_9ae0575)['ref'] = None

    @_name_boundary.callable_contract({'self': 'meadow_self_14019fa', 'ts': 'meadow_ts_0dba219', 'til': 'meadow_til_local_e640938', 'fields': 'meadow_fields_local_15a1614', 'fieldcmts': 'meadow_fieldcmts_local_78a3ba4'}, 'deserialize')
    def meadow_deserialize(meadow_self_14019fa, meadow_til_local_e640938, meadow_ts_0dba219, meadow_fields_local_15a1614, meadow_fieldcmts_local_78a3ba4):
        meadow_typ_local_6f0e1cc = meadow_ts_0dba219.u8()
        _name_boundary.attributes(meadow_self_14019fa)['is_union'] = meadow_is_type_union(meadow_typ_local_6f0e1cc)
        meadow_n_38405b1 = _name_boundary.attributes(meadow_ts_0dba219)['dt']()
        if meadow_n_38405b1 == 0:
            _name_boundary.attributes(meadow_self_14019fa)['ref'] = meadow_create_ref(meadow_til_local_e640938, _name_boundary.attributes(meadow_ts_0dba219)['pbytes']())
            _name_boundary.attributes(meadow_self_14019fa)['taudt_bits'] = _name_boundary.attributes(meadow_ts_0dba219)['sdacl_attr']()
        else:
            if meadow_n_38405b1 == 32766:
                meadow_n_38405b1 = _name_boundary.attributes(meadow_ts_0dba219)['de']()
            meadow_alpow_20d66ba = meadow_n_38405b1 & 7
            meadow_member_cnt_8d351c8 = meadow_n_38405b1 >> 3
            if meadow_alpow_20d66ba == 0:
                _name_boundary.attributes(meadow_self_14019fa)['effalign'] = 0
            else:
                _name_boundary.attributes(meadow_self_14019fa)['effalign'] = 1 << meadow_alpow_20d66ba - 1
            _name_boundary.attributes(meadow_self_14019fa)['taudt_bits'] = _name_boundary.attributes(meadow_ts_0dba219)['sdacl_attr']()
            meadow_field_i_dc799d9 = 0
            for meadow_i_607794e in range(meadow_member_cnt_8d351c8):
                meadow_member_d7a7c1b = meadow_UdtMember()
                meadow_member_d7a7c1b.type = meadow_create_tinfo(meadow_til_local_e640938, _name_boundary.attributes(meadow_ts_0dba219)['ref'](), meadow_fields_local_15a1614, meadow_fieldcmts_local_78a3ba4)
                meadow_attr_e250aec = _name_boundary.attributes(meadow_ts_0dba219)['sdacl_attr']() if not _name_boundary.attributes(meadow_self_14019fa)['is_union'] else 0
                _name_boundary.attributes(meadow_member_d7a7c1b)['tafld_bits'] = meadow_attr_e250aec
                _name_boundary.attributes(meadow_member_d7a7c1b)['fda'] = meadow_attr_e250aec
                if not _name_boundary.attributes(meadow_member_d7a7c1b)['is_baseclass']():
                    if len(meadow_fields_local_15a1614) > meadow_field_i_dc799d9:
                        meadow_member_d7a7c1b.name = meadow_fields_local_15a1614[meadow_field_i_dc799d9]
                    if meadow_n_38405b1 < len(meadow_fieldcmts_local_78a3ba4):
                        meadow_member_d7a7c1b.cmt = meadow_fieldcmts_local_78a3ba4[meadow_field_i_dc799d9]
                    meadow_field_i_dc799d9 += 1
                _name_boundary.attributes(meadow_self_14019fa)['members'].append(meadow_member_d7a7c1b)
        return meadow_self_14019fa
meadow_TAENUM_64BIT = 32

@_name_boundary.class_contract('EnumMember', {})
class meadow_EnumMember:

    @_name_boundary.callable_contract({'self': 'meadow_self_48c3cf3', 'name': 'meadow_name_local_0f3a718', 'value': 'meadow_value_local_496f019', 'cmt': 'meadow_cmt_local_8a47587'}, '__init__')
    def __init__(meadow_self_48c3cf3, meadow_name_local_0f3a718, meadow_value_local_496f019=0, meadow_cmt_local_8a47587=''):
        meadow_self_48c3cf3.name = meadow_name_local_0f3a718
        meadow_self_48c3cf3.cmt = meadow_cmt_local_8a47587
        meadow_self_48c3cf3.value = meadow_value_local_496f019

@_name_boundary.class_contract('EnumTypeData', {'deserialize': 'meadow_deserialize', 'calc_mask': 'meadow_calc_mask', 'group_sizes': 'meadow_group_sizes', 'taenum_bits': 'meadow_taenum_bits', 'bte': 'meadow_bte', 'members': 'meadow_members', 'ref': 'meadow_ref'})
class meadow_EnumTypeData(meadow_TypeData):
    """Representation of enum_type_data_t"""

    @_name_boundary.callable_contract({'self': 'meadow_self_45ceffc'}, '__init__')
    def __init__(meadow_self_45ceffc):
        meadow_TypeData.__init__(meadow_self_45ceffc)
        _name_boundary.attributes(meadow_self_45ceffc)['group_sizes'] = []
        _name_boundary.attributes(meadow_self_45ceffc)['taenum_bits'] = 0
        _name_boundary.attributes(meadow_self_45ceffc)['bte'] = 0
        _name_boundary.attributes(meadow_self_45ceffc)['members'] = []
        _name_boundary.attributes(meadow_self_45ceffc)['ref'] = None

    @_name_boundary.callable_contract({'self': 'meadow_self_51c174f', 'ts': 'meadow_ts_3212c33', 'til': 'meadow_til_local_6679912', 'fields': 'meadow_fields_local_84365cb', 'fieldcmts': 'meadow_fieldcmts_local_06174c6'}, 'deserialize')
    def meadow_deserialize(meadow_self_51c174f, meadow_til_local_6679912, meadow_ts_3212c33, meadow_fields_local_84365cb, meadow_fieldcmts_local_06174c6):
        meadow_typ_local_3c5fb23 = meadow_ts_3212c33.u8()
        meadow_n_c57aa6d = _name_boundary.attributes(meadow_ts_3212c33)['dt']()
        if meadow_n_c57aa6d == 0:
            _name_boundary.attributes(meadow_self_51c174f)['ref'] = meadow_create_ref(meadow_til_local_6679912, _name_boundary.attributes(meadow_ts_3212c33)['pbytes']())
            _name_boundary.attributes(meadow_self_51c174f)['taenum_bits'] = _name_boundary.attributes(meadow_ts_3212c33)['sdacl_attr']()
        else:
            if meadow_n_c57aa6d == 32766:
                meadow_n_c57aa6d = _name_boundary.attributes(meadow_ts_3212c33)['de']()
            _name_boundary.attributes(meadow_self_51c174f)['taenum_bits'] = _name_boundary.attributes(meadow_ts_3212c33)['tah_attr']()
            _name_boundary.attributes(meadow_self_51c174f)['bte'] = meadow_ts_3212c33.u8()
            meadow_cur_218b3cc = 0
            meadow_hi_local_ae547ec = 0
            meadow_mask_555f080 = _name_boundary.attributes(meadow_self_51c174f)['calc_mask'](meadow_til_local_6679912)
            for meadow_i_ef8575d in range(meadow_n_c57aa6d):
                meadow_lo_local_929f226 = _name_boundary.attributes(meadow_ts_3212c33)['de']()
                if _name_boundary.attributes(meadow_self_51c174f)['taenum_bits'] & meadow_TAENUM_64BIT:
                    meadow_hi_local_ae547ec = _name_boundary.attributes(meadow_ts_3212c33)['de']()
                if _name_boundary.attributes(meadow_self_51c174f)['bte'] & meadow_BTE_BITFIELD:
                    _name_boundary.attributes(meadow_self_51c174f)['group_sizes'].append(_name_boundary.attributes(meadow_ts_3212c33)['dt']())
                meadow_cur_218b3cc += meadow_lo_local_929f226 | meadow_hi_local_ae547ec << 32 & meadow_mask_555f080
                meadow_member_4036cc5 = meadow_EnumMember(meadow_fields_local_84365cb[meadow_i_ef8575d], value=meadow_cur_218b3cc)
                _name_boundary.attributes(meadow_self_51c174f)['members'].append(meadow_member_4036cc5)
        return meadow_self_51c174f

    @_name_boundary.callable_contract({'self': 'meadow_self_b647238', 'til': 'meadow_til_local_8db68fa'}, 'calc_mask')
    def meadow_calc_mask(meadow_self_b647238, meadow_til_local_8db68fa):
        meadow_emsize_e538a93 = _name_boundary.attributes(meadow_self_b647238)['bte'] & meadow_BTE_SIZE_MASK
        if meadow_emsize_e538a93 != 0:
            meadow_bytesize_ea52570 = 1 << meadow_emsize_e538a93 - 1
        elif meadow_til_local_8db68fa is not None:
            meadow_bytesize_ea52570 = meadow_til_local_8db68fa.size_e
        else:
            meadow_bytesize_ea52570 = 4
        meadow_bitsize_af5201b = meadow_bytesize_ea52570 * 8
        if meadow_bitsize_af5201b < 64:
            return (1 << meadow_bitsize_af5201b) - 1
        return 18446744073709551615

@_name_boundary.class_contract('TypedefTypeData', {'deserialize': 'meadow_deserialize', 'is_ordref': 'meadow_is_ordref', 'resolve': 'meadow_resolve'})
class meadow_TypedefTypeData(meadow_TypeData):
    """Representation of typedef_type_data_t"""

    @_name_boundary.callable_contract({'self': 'meadow_self_9c63063'}, '__init__')
    def __init__(meadow_self_9c63063):
        meadow_TypeData.__init__(meadow_self_9c63063)
        meadow_self_9c63063.til = None
        meadow_self_9c63063.name = None
        meadow_self_9c63063.ordinal = 0
        _name_boundary.attributes(meadow_self_9c63063)['is_ordref'] = False
        _name_boundary.attributes(meadow_self_9c63063)['resolve'] = False

    @_name_boundary.callable_contract({'self': 'meadow_self_bf5f03a', 'type_string': 'meadow_type_string_e6c28b4', 'til': 'meadow_til_local_bcd936d', 'fields': 'meadow_fields_local_59757ec', 'fieldcmts': 'meadow_fieldcmts_local_a0af29a'}, 'deserialize')
    def meadow_deserialize(meadow_self_bf5f03a, meadow_til_local_bcd936d, meadow_type_string_e6c28b4, meadow_fields_local_59757ec, meadow_fieldcmts_local_a0af29a):
        meadow_self_bf5f03a.til = meadow_til_local_bcd936d
        meadow_typ_local_6b7a088 = meadow_type_string_e6c28b4.u8()
        meadow_buf_local_1c4b971 = _name_boundary.attributes(meadow_type_string_e6c28b4)['pbytes']()
        if meadow_buf_local_1c4b971.startswith(b'#'):
            _name_boundary.attributes(meadow_self_bf5f03a)['is_ordref'] = True
            meadow_self_bf5f03a.ordinal = _name_boundary.attributes(meadow_TypeString(meadow_buf_local_1c4b971[1:]))['de']()
        else:
            meadow_self_bf5f03a.name = meadow_buf_local_1c4b971.decode('ascii')
        return meadow_self_bf5f03a

@_name_boundary.class_contract('BitfieldTypeData', {'deserialize': 'meadow_deserialize', 'nbytes': 'meadow_nbytes', 'width': 'meadow_width', 'is_unsigned': 'meadow_is_unsigned'})
class meadow_BitfieldTypeData(meadow_TypeData):
    """Representation of bitfield_type_data_t"""

    @_name_boundary.callable_contract({'self': 'meadow_self_925bc31'}, '__init__')
    def __init__(meadow_self_925bc31):
        meadow_TypeData.__init__(meadow_self_925bc31)
        _name_boundary.attributes(meadow_self_925bc31)['nbytes'] = 0
        _name_boundary.attributes(meadow_self_925bc31)['width'] = 0
        _name_boundary.attributes(meadow_self_925bc31)['is_unsigned'] = False

    @_name_boundary.callable_contract({'self': 'meadow_self_badd16e', 'type_string': 'meadow_type_string_9fd869d', 'til': 'meadow_til_local_4cd786e', 'fields': 'meadow_fields_local_5ac4c71', 'fieldcmts': 'meadow_fieldcmts_local_f64e031'}, 'deserialize')
    def meadow_deserialize(meadow_self_badd16e, meadow_til_local_4cd786e, meadow_type_string_9fd869d, meadow_fields_local_5ac4c71, meadow_fieldcmts_local_f64e031):
        meadow_typ_local_21a6b99 = meadow_type_string_9fd869d.u8()
        _name_boundary.attributes(meadow_self_badd16e)['nbytes'] = 1 << (meadow_get_type_flags(meadow_typ_local_21a6b99) >> 4)
        meadow_dt_83257a1 = _name_boundary.attributes(meadow_type_string_9fd869d)['dt']()
        _name_boundary.attributes(meadow_self_badd16e)['width'] = meadow_dt_83257a1 >> 1
        _name_boundary.attributes(meadow_self_badd16e)['is_unsigned'] = bool(meadow_dt_83257a1 & 1)
        _name_boundary.attributes(meadow_type_string_9fd869d)['tah_attr']()
        return meadow_self_badd16e

@_name_boundary.class_contract('v_zbytes', {})
class meadow_v_zbytes(v_zstr):
    """
    A v_zbytes placeholder class which will automatically return
    up to a null terminator bytes dynamically.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_5f68efc'}, 'vsGetValue')
    def vsGetValue(meadow_self_5f68efc):
        return meadow_self_5f68efc._vs_value[:-meadow_self_5f68efc._vs_align_pad]

class meadow_TILTypeInfo(meadow_VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_bbee0ff', 'format': 'meadow_format_local_896d13c'}, '__init__')
    def __init__(meadow_self_bbee0ff, meadow_format_local_896d13c):
        meadow_VStruct.__init__(meadow_self_bbee0ff)
        meadow_self_bbee0ff.format = meadow_format_local_896d13c
        meadow_self_bbee0ff.flags = v_uint32()
        meadow_self_bbee0ff.name = v_zstr_utf8()
        meadow_self_bbee0ff.ordinal = v_uint32()
        meadow_self_bbee0ff.type_info = meadow_v_zbytes()
        meadow_self_bbee0ff.cmt = v_zstr_utf8()
        meadow_self_bbee0ff.fields_buf = meadow_v_zbytes()
        meadow_self_bbee0ff.fieldcmts = meadow_v_zbytes()
        meadow_self_bbee0ff.sclass = v_uint8()

    @_name_boundary.callable_contract({'self': 'meadow_self_db5b477'}, 'pcb_flags')
    def pcb_flags(meadow_self_db5b477):
        if meadow_self_db5b477.format < 18:
            meadow_self_db5b477.flags &= 2147483647
        if meadow_self_db5b477.flags >> 31:
            meadow_self_db5b477.vsSetField('ordinal', v_uint64())
        if meadow_self_db5b477.flags not in (2147483647, 4294967295):
            raise Exception('unsupported format {}'.format(meadow_self_db5b477.flags))

    @_name_boundary.callable_contract({'self': 'meadow_self_538406b', 'til': 'meadow_til_local_80b3b82', 'inf': 'meadow_inf_local_799e3c6'}, 'deserialize')
    def meadow_deserialize(meadow_self_538406b, meadow_til_local_80b3b82, meadow_inf_local_799e3c6):
        try:
            meadow__type_local_029935b = meadow_create_tinfo(meadow_til_local_80b3b82, meadow_self_538406b.type_info, meadow_self_538406b.fields, meadow_self_538406b.fieldcmts, name=meadow_self_538406b.name, inf=meadow_inf_local_799e3c6)
        except OverflowError:
            meadow__type_local_029935b = meadow_ErrorTInfo(meadow_self_538406b.name)
        object.__setattr__(meadow_self_538406b, 'type', meadow__type_local_029935b)

    @meadow_cached_property
    @_name_boundary.callable_contract({'self': 'meadow_self_5112c32'}, 'fields')
    def fields(meadow_self_5112c32):
        meadow_fields_local_fba0d4c = []
        meadow_pos_local_406ef8f = 0
        while meadow_pos_local_406ef8f < len(meadow_self_5112c32.fields_buf):
            meadow_length_local_5b94dc0 = _name_boundary.attributes(struct)['unpack']('<B', meadow_self_5112c32.fields_buf[meadow_pos_local_406ef8f:meadow_pos_local_406ef8f + 1])[0]
            meadow_fields_local_fba0d4c.append(meadow_self_5112c32.fields_buf[meadow_pos_local_406ef8f + 1:meadow_pos_local_406ef8f + meadow_length_local_5b94dc0].decode('ascii'))
            meadow_pos_local_406ef8f += meadow_length_local_5b94dc0
        meadow_fields_local_fba0d4c = list(filter(lambda meadow_x_0b483f2: meadow_x_0b483f2 != '', meadow_fields_local_fba0d4c))
        return meadow_fields_local_fba0d4c
    deserialize = meadow_deserialize

class meadow_TILBucket(meadow_VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_c918ac0', 'flags': 'meadow_flags_local_5eae997', 'format': 'meadow_format_local_35e60e3'}, '__init__')
    def __init__(meadow_self_c918ac0, meadow_flags_local_5eae997, meadow_format_local_35e60e3):
        meadow_VStruct.__init__(meadow_self_c918ac0)
        meadow_self_c918ac0.flags = meadow_flags_local_5eae997
        meadow_self_c918ac0.format = meadow_format_local_35e60e3
        meadow_self_c918ac0.defs = None
        meadow_self_c918ac0.ndefs = v_uint32()
        meadow_self_c918ac0.size = v_uint32()
        if meadow_self_c918ac0.flags & meadow_TIL_ZIP:
            meadow_self_c918ac0.csize = v_uint32()
        else:
            meadow_self_c918ac0.csize = None
        meadow_self_c918ac0.buf = v_bytes()

    @_name_boundary.callable_contract({'self': 'meadow_self_7820766'}, 'pcb_size')
    def pcb_size(meadow_self_7820766):
        meadow_self_7820766['buf'].vsSetLength(meadow_self_7820766.size)

    @_name_boundary.callable_contract({'self': 'meadow_self_36659dc'}, 'pcb_csize')
    def pcb_csize(meadow_self_36659dc):
        if meadow_self_36659dc.csize is not None:
            meadow_self_36659dc['buf'].vsSetLength(meadow_self_36659dc.csize)

    @_name_boundary.callable_contract({'self': 'meadow_self_da60f34'}, 'pcb_buf')
    def pcb_buf(meadow_self_da60f34):
        if meadow_self_da60f34.csize is not None:
            meadow_buf_local_0fb969c = meadow_zlib.decompress(meadow_self_da60f34.buf)
            meadow_self_da60f34.vsSetField('buf', meadow_buf_local_0fb969c)
        else:
            meadow_buf_local_0fb969c = meadow_self_da60f34.buf.tobytes() if isinstance(meadow_self_da60f34.buf, memoryview) else meadow_self_da60f34.buf
        meadow_defs_local_48dcd2a = []
        meadow_offset_local_5fdbe1b = 0
        for meadow___e7ab9ca in range(meadow_self_da60f34.ndefs):
            meadow__def_local_46e94cc = meadow_TILTypeInfo(meadow_self_da60f34.format)
            meadow_offset_local_5fdbe1b = meadow__def_local_46e94cc.vsParse(meadow_buf_local_0fb969c, offset=meadow_offset_local_5fdbe1b)
            meadow_defs_local_48dcd2a.append(meadow__def_local_46e94cc)
        meadow_self_da60f34.defs = meadow_defs_local_48dcd2a

    @_name_boundary.callable_contract({'self': 'meadow_self_874f10a', 'name': 'meadow_name_local_5aa10c7'}, 'find_by_name')
    def meadow_find_by_name(meadow_self_874f10a, meadow_name_local_5aa10c7):
        if not meadow_self_874f10a.defs:
            return None
        meadow__def_local_3efa7f1 = list(filter(lambda meadow_x_57b3b2f: meadow_x_57b3b2f.name == meadow_name_local_5aa10c7, meadow_self_874f10a.defs))
        if len(meadow__def_local_3efa7f1) == 0:
            return None
        return meadow__def_local_3efa7f1[0]

    @meadow_cached_property
    @_name_boundary.callable_contract({'self': 'meadow_self_f3c44a8'}, 'ordinal_defs')
    def meadow_ordinal_defs(meadow_self_f3c44a8):
        return {meadow_i_b29e915.ordinal: meadow_i_b29e915 for meadow_i_b29e915 in meadow_self_f3c44a8.defs}

    @_name_boundary.callable_contract({'self': 'meadow_self_a6f1d31', 'ordinal': 'meadow_ordinal_local_fd8e37d'}, 'get_by_ordinal')
    def meadow_get_by_ordinal(meadow_self_a6f1d31, meadow_ordinal_local_fd8e37d):
        if meadow_ordinal_local_fd8e37d not in _name_boundary.attributes(meadow_self_a6f1d31)['ordinal_defs']:
            return None
        return _name_boundary.attributes(meadow_self_a6f1d31)['ordinal_defs'][meadow_ordinal_local_fd8e37d]
    find_by_name = meadow_find_by_name
    ordinal_defs = meadow_ordinal_defs
    get_by_ordinal = meadow_get_by_ordinal
meadow_TIL_ZIP = 1
meadow_TIL_MAC = 2
meadow_TIL_ESI = 4
meadow_TIL_UNI = 8
meadow_TIL_ORD = 16
meadow_TIL_ALI = 32
meadow_TIL_MOD = 64
meadow_TIL_STM = 128
meadow_TIL_SLD = 256

class meadow_TIL(meadow_VStruct):

    @_name_boundary.callable_contract({'self': 'meadow_self_6a1ac5d', 'buf': 'meadow_buf_local_d720882', 'wordsize': 'meadow_wordsize_local_644171e', 'inf': 'meadow_inf_local_89b0b2d'}, '__init__')
    def __init__(meadow_self_6a1ac5d, meadow_buf_local_d720882=None, meadow_wordsize_local_644171e=4, meadow_inf_local_89b0b2d=None):
        meadow_VStruct.__init__(meadow_self_6a1ac5d)
        meadow_self_6a1ac5d.wordsize = meadow_wordsize_local_644171e
        meadow_self_6a1ac5d.inf = meadow_inf_local_89b0b2d
        meadow_self_6a1ac5d.signature = v_str(size=6)
        meadow_self_6a1ac5d.format = v_uint32()
        meadow_self_6a1ac5d.flags = v_uint32()
        meadow_self_6a1ac5d.title_len = v_uint8()
        meadow_self_6a1ac5d.title = v_str()
        meadow_self_6a1ac5d.base_len = v_uint8()
        meadow_self_6a1ac5d.base = v_str()
        meadow_self_6a1ac5d.id = v_uint8()
        meadow_self_6a1ac5d.cm = v_uint8()
        meadow_self_6a1ac5d.size_i = v_uint8()
        meadow_self_6a1ac5d.size_b = v_uint8()
        meadow_self_6a1ac5d.size_e = v_uint8()
        meadow_self_6a1ac5d.def_align = v_uint8()

    @_name_boundary.callable_contract({'self': 'meadow_self_d97b9c6'}, 'pcb_flags')
    def pcb_flags(meadow_self_d97b9c6):
        if meadow_self_d97b9c6.flags & meadow_TIL_ESI:
            meadow_self_d97b9c6.vsAddField('size_s', v_uint8())
            meadow_self_d97b9c6.vsAddField('size_l', v_uint8())
            meadow_self_d97b9c6.vsAddField('size_ll', v_uint8())
        if meadow_self_d97b9c6.flags & meadow_TIL_SLD:
            meadow_self_d97b9c6.vsAddField('size_ldbl', v_uint8())
        meadow_self_d97b9c6.vsAddField('syms', meadow_TILBucket(meadow_self_d97b9c6.flags, meadow_self_d97b9c6.format))
        if meadow_self_d97b9c6.flags & meadow_TIL_ORD:
            meadow_self_d97b9c6.vsAddField('type_ordinal_numbers', v_uint32())
        meadow_self_d97b9c6.vsAddField('types', meadow_TILBucket(meadow_self_d97b9c6.flags, meadow_self_d97b9c6.format))
        meadow_self_d97b9c6.vsAddField('macros', meadow_TILBucket(meadow_self_d97b9c6.flags, meadow_self_d97b9c6.format))

    @_name_boundary.callable_contract({'self': 'meadow_self_45e0005'}, 'pcb_title_len')
    def pcb_title_len(meadow_self_45e0005):
        meadow_self_45e0005['title'].vsSetLength(meadow_self_45e0005.title_len)

    @_name_boundary.callable_contract({'self': 'meadow_self_e292641'}, 'pcb_base_len')
    def pcb_base_len(meadow_self_e292641):
        meadow_self_e292641['base'].vsSetLength(meadow_self_e292641.base_len)

    @_name_boundary.callable_contract({'self': 'meadow_self_c17b3eb', 'fast': 'meadow_fast_ad83959', 'sbytes': 'meadow_sbytes_local_b456f42', 'offset': 'meadow_offset_local_6ece6db'}, 'vsParse')
    def vsParse(meadow_self_c17b3eb, meadow_sbytes_local_b456f42, meadow_offset_local_6ece6db=0, meadow_fast_ad83959=False):
        meadow_sbytes_local_b456f42 = meadow_sbytes_local_b456f42.tobytes() if isinstance(meadow_sbytes_local_b456f42, memoryview) else meadow_sbytes_local_b456f42
        meadow_result_local_8a5d9cc = meadow_VStruct.vsParse(meadow_self_c17b3eb, meadow_sbytes_local_b456f42, meadow_offset_local_6ece6db, meadow_fast_ad83959)
        _name_boundary.attributes(meadow_self_c17b3eb)['types'].defs.sort(key=lambda meadow_x_99966d6: meadow_x_99966d6.ordinal)
        _name_boundary.attributes(meadow_self_c17b3eb)['deserialize_bucket'](meadow_self_c17b3eb.syms)
        _name_boundary.attributes(meadow_self_c17b3eb)['deserialize_bucket'](_name_boundary.attributes(meadow_self_c17b3eb)['types'])
        return meadow_result_local_8a5d9cc

    @_name_boundary.callable_contract({'self': 'meadow_self_f7cfd92', 'bucket': 'meadow_bucket_1ff5972'}, 'deserialize_bucket')
    def meadow_deserialize_bucket(meadow_self_f7cfd92, meadow_bucket_1ff5972):
        for meadow_t_dcf1c2b in meadow_bucket_1ff5972.defs:
            _name_boundary.attributes(meadow_t_dcf1c2b)['deserialize'](meadow_self_f7cfd92, meadow_self_f7cfd92.inf)

    @_name_boundary.callable_contract({'self': 'meadow_self_de5bc4c'}, 'validate')
    def meadow_validate(meadow_self_de5bc4c):
        if meadow_self_de5bc4c.signature != 'IDATIL':
            raise ValueError('bad signature')
        return True
    deserialize_bucket = meadow_deserialize_bucket
    validate = meadow_validate
_name_boundary.module_contract(globals(), {'TAENUM_64BIT': 'meadow_TAENUM_64BIT', 'ArgPart': 'meadow_ArgPart', 'create_ref': 'meadow_create_ref', 'TypeString': 'meadow_TypeString', 'TIL_SLD': 'meadow_TIL_SLD', 'TInfo': 'meadow_TInfo', 'PointerTypeData': 'meadow_PointerTypeData', 'ArgLoc': 'meadow_ArgLoc', 'RRel': 'meadow_RRel', 'v_zbytes': 'meadow_v_zbytes', 'TIL_STM': 'meadow_TIL_STM', 'TAUDT_UNALIGNED': 'meadow_TAUDT_UNALIGNED', 'TILBucket': 'meadow_TILBucket', 'TAFLD_VIRTBASE': 'meadow_TAFLD_VIRTBASE', 'ErrorTInfo': 'meadow_ErrorTInfo', 'TIL_MAC': 'meadow_TIL_MAC', 'ArrayTypeData': 'meadow_ArrayTypeData', 'BitfieldTypeData': 'meadow_BitfieldTypeData', 'global_inf': 'meadow_global_inf', 'FuncArg': 'meadow_FuncArg', 'TIL_ORD': 'meadow_TIL_ORD', 'RegInfo': 'meadow_RegInfo', 'TIL_MOD': 'meadow_TIL_MOD', 'print_reg': 'meadow_print_reg', 'VStruct': 'meadow_VStruct', 'ABCMeta': 'meadow_ABCMeta', 'TAUDT_CPPOBJ': 'meadow_TAUDT_CPPOBJ', 'TypeData': 'meadow_TypeData', 'create_tinfo': 'meadow_create_tinfo', 'EnumMember': 'meadow_EnumMember', 'zlib': 'meadow_zlib', 'EnumTypeData': 'meadow_EnumTypeData', 'TAFLD_UNALIGNED': 'meadow_TAFLD_UNALIGNED', 'cached_property': 'meadow_cached_property', 'TAUDT_MSSTRUCT': 'meadow_TAUDT_MSSTRUCT', 'TIL_ESI': 'meadow_TIL_ESI', 'print_argloc': 'meadow_print_argloc', 'UdtMember': 'meadow_UdtMember', 'TIL_ZIP': 'meadow_TIL_ZIP', 'TIL': 'meadow_TIL', 'TAFLD_BASECLASS': 'meadow_TAFLD_BASECLASS', 'abstractmethod': 'meadow_abstractmethod', 'UdtTypeData': 'meadow_UdtTypeData', 'TIL_ALI': 'meadow_TIL_ALI', 'FuncTypeData': 'meadow_FuncTypeData', 'TILTypeInfo': 'meadow_TILTypeInfo', 'serialize_dt': 'meadow_serialize_dt', 'TypedefTypeData': 'meadow_TypedefTypeData', 'TIL_UNI': 'meadow_TIL_UNI'})
