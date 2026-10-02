# Derived from idb/idapython.py; original copyright and license retained in ORIGIN.md.
# -*- coding: utf-8 -*-
import idbmeadow.api_contract as _name_boundary
import os as meadow_os
import re as meadow_re
import struct as meadow_struct
import logging as meadow_logging
import weakref as meadow_weakref
import collections as meadow_collections
import six as meadow_six
from idbmeadow.node_records import meadow_Netnode as meadow_Netnode
from idbmeadow.type_records import meadow_TIL as meadow_TIL
from idbmeadow.semantic_views import meadow_Struct as meadow_Struct, meadow_StructMember as meadow_StructMember
if meadow_six.PY2:
    import functools32 as meadow_functools
else:
    import functools as meadow_functools
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
import idbmeadow.semantic_views as _boundary_import_idb_analysis
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'lru_args': 'meadow_lru_args_6f406a2', 'lru_kwargs': 'meadow_lru_kwargs_9783634'}, 'memoized_method')
def meadow_memoized_method(*meadow_lru_args_6f406a2, **meadow_lru_kwargs_9783634):

    @_name_boundary.callable_contract({'func': 'meadow_func_8c98312'}, 'decorator')
    def meadow_decorator_3e26b42(meadow_func_8c98312):

        @meadow_functools.wraps(meadow_func_8c98312)
        @_name_boundary.callable_contract({'self': 'meadow_self_41fc402', 'args': 'meadow_args_3d7ee64', 'kwargs': 'meadow_kwargs_961732b'}, 'wrapped_func')
        def meadow_wrapped_func_9b9fa8d(meadow_self_41fc402, *meadow_args_3d7ee64, **meadow_kwargs_961732b):
            meadow_self_weak_d47af39 = _name_boundary.attributes(meadow_weakref)['ref'](meadow_self_41fc402)

            @meadow_functools.wraps(meadow_func_8c98312)
            @meadow_functools.lru_cache(*meadow_lru_args_6f406a2, **meadow_lru_kwargs_9783634)
            @_name_boundary.callable_contract({'args': 'meadow_args_9cc6b54', 'kwargs': 'meadow_kwargs_a602fec'}, 'cached_method')
            def meadow_cached_method_b06bd97(*meadow_args_9cc6b54, **meadow_kwargs_a602fec):
                return meadow_func_8c98312(meadow_self_weak_d47af39(), *meadow_args_9cc6b54, **meadow_kwargs_a602fec)
            _name_boundary.write_attribute(meadow_self_41fc402, _name_boundary.attributes(meadow_func_8c98312)['__name__'], meadow_cached_method_b06bd97)
            return meadow_cached_method_b06bd97(*meadow_args_3d7ee64, **meadow_kwargs_961732b)
        return meadow_wrapped_func_9b9fa8d
    return meadow_decorator_3e26b42

@_name_boundary.callable_contract({'into': 'meadow_into_a3442c9', 'full': 'meadow_full_8466d0c'}, 'wrap_module')
def meadow_wrap_module(meadow_into_a3442c9, meadow_full_8466d0c=True):

    @_name_boundary.callable_contract({'func': 'meadow_func_7d3abb4'}, 'decorator')
    def meadow_decorator_6eab91c(meadow_func_7d3abb4):

        @meadow_functools.wraps(meadow_func_7d3abb4)
        @_name_boundary.callable_contract({'self': 'meadow_self_84129f8', 'args': 'meadow_args_c568c9a', 'kwargs': 'meadow_kwargs_8724e10'}, 'wrapped_func')
        def meadow_wrapped_func_82d1f9a(meadow_self_84129f8, *meadow_args_c568c9a, **meadow_kwargs_8724e10):
            meadow_func_7d3abb4(meadow_self_84129f8, *meadow_args_c568c9a, **meadow_kwargs_8724e10)
            meadow_mod_9d29852 = _name_boundary.namespace_view(meadow_self_84129f8.api)[meadow_into_a3442c9]
            for meadow_attr_56da47e in _name_boundary.public_names(meadow_self_84129f8):
                if meadow_attr_56da47e.startswith('_') or meadow_attr_56da47e == 'api' or meadow_attr_56da47e == 'idb':
                    continue
                meadow_obj_99a0634 = _name_boundary.read_attribute(meadow_self_84129f8, meadow_attr_56da47e)
                if not meadow_full_8466d0c and callable(meadow_obj_99a0634):
                    continue
                _name_boundary.write_attribute(meadow_mod_9d29852, meadow_attr_56da47e, meadow_obj_99a0634)
        return meadow_wrapped_func_82d1f9a
    return meadow_decorator_6eab91c

@_name_boundary.callable_contract({'flag': 'meadow_flag_8a7dff5', 'flags': 'meadow_flags_local_0e47dc2'}, 'is_flag_set')
def meadow_is_flag_set(meadow_flags_local_0e47dc2, meadow_flag_8a7dff5):
    return meadow_flags_local_0e47dc2 & meadow_flag_8a7dff5 == meadow_flag_8a7dff5

@_name_boundary.class_contract('FLAGS', {'OPND_OUTER': 'meadow_OPND_OUTER', 'OPND_MASK': 'meadow_OPND_MASK', 'OPND_ALL': 'meadow_OPND_ALL', 'MS_CLS': 'meadow_MS_CLS', 'FF_CODE': 'meadow_FF_CODE', 'FF_DATA': 'meadow_FF_DATA', 'FF_TAIL': 'meadow_FF_TAIL', 'FF_UNK': 'meadow_FF_UNK', 'MS_COMM': 'meadow_MS_COMM', 'FF_COMM': 'meadow_FF_COMM', 'FF_REF': 'meadow_FF_REF', 'FF_LINE': 'meadow_FF_LINE', 'FF_NAME': 'meadow_FF_NAME', 'FF_LABL': 'meadow_FF_LABL', 'FF_FLOW': 'meadow_FF_FLOW', 'FF_SIGN': 'meadow_FF_SIGN', 'FF_BNOT': 'meadow_FF_BNOT', 'FF_VAR': 'meadow_FF_VAR', 'MS_0TYPE': 'meadow_MS_0TYPE', 'FF_0VOID': 'meadow_FF_0VOID', 'FF_0NUMH': 'meadow_FF_0NUMH', 'FF_0NUMD': 'meadow_FF_0NUMD', 'FF_0CHAR': 'meadow_FF_0CHAR', 'FF_0SEG': 'meadow_FF_0SEG', 'FF_0OFF': 'meadow_FF_0OFF', 'FF_0NUMB': 'meadow_FF_0NUMB', 'FF_0NUMO': 'meadow_FF_0NUMO', 'FF_0ENUM': 'meadow_FF_0ENUM', 'FF_0FOP': 'meadow_FF_0FOP', 'FF_0STRO': 'meadow_FF_0STRO', 'FF_0STK': 'meadow_FF_0STK', 'FF_0FLT': 'meadow_FF_0FLT', 'FF_0CUST': 'meadow_FF_0CUST', 'MS_1TYPE': 'meadow_MS_1TYPE', 'FF_1VOID': 'meadow_FF_1VOID', 'FF_1NUMH': 'meadow_FF_1NUMH', 'FF_1NUMD': 'meadow_FF_1NUMD', 'FF_1CHAR': 'meadow_FF_1CHAR', 'FF_1SEG': 'meadow_FF_1SEG', 'FF_1OFF': 'meadow_FF_1OFF', 'FF_1NUMB': 'meadow_FF_1NUMB', 'FF_1NUMO': 'meadow_FF_1NUMO', 'FF_1ENUM': 'meadow_FF_1ENUM', 'FF_1FOP': 'meadow_FF_1FOP', 'FF_1STRO': 'meadow_FF_1STRO', 'FF_1STK': 'meadow_FF_1STK', 'FF_1FLT': 'meadow_FF_1FLT', 'FF_1CUST': 'meadow_FF_1CUST', 'MS_CODE': 'meadow_MS_CODE', 'FF_FUNC': 'meadow_FF_FUNC', 'FF_IMMD': 'meadow_FF_IMMD', 'FF_JUMP': 'meadow_FF_JUMP', 'DT_TYPE': 'meadow_DT_TYPE', 'FF_BYTE': 'meadow_FF_BYTE', 'FF_WORD': 'meadow_FF_WORD', 'FF_DWRD': 'meadow_FF_DWRD', 'FF_QWRD': 'meadow_FF_QWRD', 'FF_TBYT': 'meadow_FF_TBYT', 'FF_ASCI': 'meadow_FF_ASCI', 'FF_STRU': 'meadow_FF_STRU', 'FF_OWRD': 'meadow_FF_OWRD', 'FF_FLOAT': 'meadow_FF_FLOAT', 'FF_DOUBLE': 'meadow_FF_DOUBLE', 'FF_PACKREAL': 'meadow_FF_PACKREAL', 'FF_ALIGN': 'meadow_FF_ALIGN', 'FF_3BYTE': 'meadow_FF_3BYTE', 'FF_CUSTOM': 'meadow_FF_CUSTOM', 'FF_YWRD': 'meadow_FF_YWRD', 'MS_VAL': 'meadow_MS_VAL', 'FF_IVL': 'meadow_FF_IVL'})
class meadow_FLAGS:
    meadow_OPND_OUTER = 128
    meadow_OPND_MASK = 7
    meadow_OPND_ALL = meadow_OPND_MASK
    meadow_MS_CLS = 1536
    meadow_FF_CODE = 1536
    meadow_FF_DATA = 1024
    meadow_FF_TAIL = 512
    meadow_FF_UNK = 0
    meadow_MS_COMM = 1046528
    meadow_FF_COMM = 2048
    meadow_FF_REF = 4096
    meadow_FF_LINE = 8192
    meadow_FF_NAME = 16384
    meadow_FF_LABL = 32768
    meadow_FF_FLOW = 65536
    meadow_FF_SIGN = 131072
    meadow_FF_BNOT = 262144
    meadow_FF_VAR = 524288
    meadow_MS_0TYPE = 15728640
    meadow_FF_0VOID = 0
    meadow_FF_0NUMH = 1048576
    meadow_FF_0NUMD = 2097152
    meadow_FF_0CHAR = 3145728
    meadow_FF_0SEG = 4194304
    meadow_FF_0OFF = 5242880
    meadow_FF_0NUMB = 6291456
    meadow_FF_0NUMO = 7340032
    meadow_FF_0ENUM = 8388608
    meadow_FF_0FOP = 9437184
    meadow_FF_0STRO = 10485760
    meadow_FF_0STK = 11534336
    meadow_FF_0FLT = 12582912
    meadow_FF_0CUST = 13631488
    meadow_MS_1TYPE = 251658240
    meadow_FF_1VOID = 0
    meadow_FF_1NUMH = 16777216
    meadow_FF_1NUMD = 33554432
    meadow_FF_1CHAR = 50331648
    meadow_FF_1SEG = 67108864
    meadow_FF_1OFF = 83886080
    meadow_FF_1NUMB = 100663296
    meadow_FF_1NUMO = 117440512
    meadow_FF_1ENUM = 134217728
    meadow_FF_1FOP = 150994944
    meadow_FF_1STRO = 167772160
    meadow_FF_1STK = 184549376
    meadow_FF_1FLT = 201326592
    meadow_FF_1CUST = 218103808
    meadow_MS_CODE = 4026531840
    meadow_FF_FUNC = 268435456
    meadow_FF_IMMD = 1073741824
    meadow_FF_JUMP = 2147483648
    meadow_DT_TYPE = 4026531840
    meadow_FF_BYTE = 0
    meadow_FF_WORD = 268435456
    meadow_FF_DWRD = 536870912
    meadow_FF_QWRD = 805306368
    meadow_FF_TBYT = 1073741824
    meadow_FF_ASCI = 1342177280
    meadow_FF_STRU = 1610612736
    meadow_FF_OWRD = 1879048192
    meadow_FF_FLOAT = 2147483648
    meadow_FF_DOUBLE = 2415919104
    meadow_FF_PACKREAL = 2684354560
    meadow_FF_ALIGN = 2952790016
    meadow_FF_3BYTE = 3221225472
    meadow_FF_CUSTOM = 3489660928
    meadow_FF_YWRD = 3758096384
    meadow_MS_VAL = 255
    meadow_FF_IVL = 256

@_name_boundary.class_contract('AFLAGS', {'AFL_LINNUM': 'meadow_AFL_LINNUM', 'AFL_USERSP': 'meadow_AFL_USERSP', 'AFL_PUBNAM': 'meadow_AFL_PUBNAM', 'AFL_WEAKNAM': 'meadow_AFL_WEAKNAM', 'AFL_HIDDEN': 'meadow_AFL_HIDDEN', 'AFL_MANUAL': 'meadow_AFL_MANUAL', 'AFL_NOBRD': 'meadow_AFL_NOBRD', 'AFL_ZSTROFF': 'meadow_AFL_ZSTROFF', 'AFL_BNOT0': 'meadow_AFL_BNOT0', 'AFL_BNOT1': 'meadow_AFL_BNOT1', 'AFL_LIB': 'meadow_AFL_LIB', 'AFL_TI': 'meadow_AFL_TI', 'AFL_TI0': 'meadow_AFL_TI0', 'AFL_TI1': 'meadow_AFL_TI1', 'AFL_LNAME': 'meadow_AFL_LNAME', 'AFL_TILCMT': 'meadow_AFL_TILCMT', 'AFL_LZERO0': 'meadow_AFL_LZERO0', 'AFL_LZERO1': 'meadow_AFL_LZERO1', 'AFL_COLORED': 'meadow_AFL_COLORED', 'AFL_TERSESTR': 'meadow_AFL_TERSESTR', 'AFL_SIGN0': 'meadow_AFL_SIGN0', 'AFL_SIGN1': 'meadow_AFL_SIGN1', 'AFL_NORET': 'meadow_AFL_NORET', 'AFL_FIXEDSPD': 'meadow_AFL_FIXEDSPD', 'AFL_ALIGNFLOW': 'meadow_AFL_ALIGNFLOW', 'AFL_USERTI': 'meadow_AFL_USERTI', 'AFL_RETFP': 'meadow_AFL_RETFP', 'AFL_USEMODSP': 'meadow_AFL_USEMODSP', 'AFL_NOTCODE': 'meadow_AFL_NOTCODE'})
class meadow_AFLAGS:
    meadow_AFL_LINNUM = 1
    meadow_AFL_USERSP = 2
    meadow_AFL_PUBNAM = 4
    meadow_AFL_WEAKNAM = 8
    meadow_AFL_HIDDEN = 16
    meadow_AFL_MANUAL = 32
    meadow_AFL_NOBRD = 64
    meadow_AFL_ZSTROFF = 128
    meadow_AFL_BNOT0 = 256
    meadow_AFL_BNOT1 = 512
    meadow_AFL_LIB = 1024
    meadow_AFL_TI = 2048
    meadow_AFL_TI0 = 4096
    meadow_AFL_TI1 = 8192
    meadow_AFL_LNAME = 16384
    meadow_AFL_TILCMT = 32768
    meadow_AFL_LZERO0 = 65536
    meadow_AFL_LZERO1 = 131072
    meadow_AFL_COLORED = 262144
    meadow_AFL_TERSESTR = 524288
    meadow_AFL_SIGN0 = 1048576
    meadow_AFL_SIGN1 = 2097152
    meadow_AFL_NORET = 4194304
    meadow_AFL_FIXEDSPD = 8388608
    meadow_AFL_ALIGNFLOW = 16777216
    meadow_AFL_USERTI = 33554432
    meadow_AFL_RETFP = 67108864
    meadow_AFL_USEMODSP = 134217728
    meadow_AFL_NOTCODE = 268435456

@_name_boundary.class_contract('ida_netnode', {'netnode': 'meadow_netnode', 'idb': 'meadow_idb'})
class meadow_ida_netnode:

    @meadow_wrap_module('idaapi')
    @_name_boundary.callable_contract({'self': 'meadow_self_47c9a80', 'db': 'meadow_db_a27494e', 'api': 'meadow_api_local_2485c18'}, '__init__')
    def __init__(meadow_self_47c9a80, meadow_db_a27494e, meadow_api_local_2485c18):
        _name_boundary.attributes(meadow_self_47c9a80)['idb'] = meadow_db_a27494e
        meadow_self_47c9a80.api = meadow_api_local_2485c18

    @_name_boundary.callable_contract({'self': 'meadow_self_e64c54b', 'args': 'meadow_args_7f52879', 'kwargs': 'meadow_kwargs_b40fe8c'}, 'netnode')
    def meadow_netnode(meadow_self_e64c54b, *meadow_args_7f52879, **meadow_kwargs_b40fe8c):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](_name_boundary.attributes(meadow_self_e64c54b)['idb'], *meadow_args_7f52879, **meadow_kwargs_b40fe8c)

@_name_boundary.class_contract('ida_ida', {'idb': 'meadow_idb', 'f_EXE_old': 'meadow_f_EXE_old', 'f_COM_old': 'meadow_f_COM_old', 'f_BIN': 'meadow_f_BIN', 'f_DRV': 'meadow_f_DRV', 'f_WIN': 'meadow_f_WIN', 'f_HEX': 'meadow_f_HEX', 'f_MEX': 'meadow_f_MEX', 'f_LX': 'meadow_f_LX', 'f_LE': 'meadow_f_LE', 'f_NLM': 'meadow_f_NLM', 'f_COFF': 'meadow_f_COFF', 'f_PE': 'meadow_f_PE', 'f_OMF': 'meadow_f_OMF', 'f_SREC': 'meadow_f_SREC', 'f_ZIP': 'meadow_f_ZIP', 'f_OMFLIB': 'meadow_f_OMFLIB', 'f_AR': 'meadow_f_AR', 'f_LOADER': 'meadow_f_LOADER', 'f_ELF': 'meadow_f_ELF', 'f_W32RUN': 'meadow_f_W32RUN', 'f_AOUT': 'meadow_f_AOUT', 'f_PRC': 'meadow_f_PRC', 'f_EXE': 'meadow_f_EXE', 'f_COM': 'meadow_f_COM', 'f_AIXAR': 'meadow_f_AIXAR', 'f_MACHO': 'meadow_f_MACHO', 'STT_CUR': 'meadow_STT_CUR', 'STT_VA': 'meadow_STT_VA', 'STT_MM': 'meadow_STT_MM', 'STT_DBG': 'meadow_STT_DBG', 'INFFL_AUTO': 'meadow_INFFL_AUTO', 'INFFL_ALLASM': 'meadow_INFFL_ALLASM', 'INFFL_LOADIDC': 'meadow_INFFL_LOADIDC', 'INFFL_NOUSER': 'meadow_INFFL_NOUSER', 'INFFL_READONLY': 'meadow_INFFL_READONLY', 'INFFL_CHKOPS': 'meadow_INFFL_CHKOPS', 'INFFL_NMOPS': 'meadow_INFFL_NMOPS', 'INFFL_GRAPH_VIEW': 'meadow_INFFL_GRAPH_VIEW', 'LFLG_PC_FPP': 'meadow_LFLG_PC_FPP', 'LFLG_PC_FLAT': 'meadow_LFLG_PC_FLAT', 'LFLG_64BIT': 'meadow_LFLG_64BIT', 'LFLG_IS_DLL': 'meadow_LFLG_IS_DLL', 'LFLG_FLAT_OFF32': 'meadow_LFLG_FLAT_OFF32', 'LFLG_MSF': 'meadow_LFLG_MSF', 'LFLG_WIDE_HBF': 'meadow_LFLG_WIDE_HBF', 'LFLG_DBG_NOPATH': 'meadow_LFLG_DBG_NOPATH', 'LFLG_SNAPSHOT': 'meadow_LFLG_SNAPSHOT', 'LFLG_PACK': 'meadow_LFLG_PACK', 'LFLG_COMPRESS': 'meadow_LFLG_COMPRESS', 'LFLG_KERNMODE': 'meadow_LFLG_KERNMODE', 'IDB_UNPACKED': 'meadow_IDB_UNPACKED', 'IDB_PACKED': 'meadow_IDB_PACKED', 'IDB_COMPRESSED': 'meadow_IDB_COMPRESSED', 'AF_CODE': 'meadow_AF_CODE', 'AF_MARKCODE': 'meadow_AF_MARKCODE', 'AF_JUMPTBL': 'meadow_AF_JUMPTBL', 'AF_PURDAT': 'meadow_AF_PURDAT', 'AF_USED': 'meadow_AF_USED', 'AF_UNK': 'meadow_AF_UNK', 'AF_PROCPTR': 'meadow_AF_PROCPTR', 'AF_PROC': 'meadow_AF_PROC', 'AF_FTAIL': 'meadow_AF_FTAIL', 'AF_LVAR': 'meadow_AF_LVAR', 'AF_STKARG': 'meadow_AF_STKARG', 'AF_REGARG': 'meadow_AF_REGARG', 'AF_TRACE': 'meadow_AF_TRACE', 'AF_VERSP': 'meadow_AF_VERSP', 'AF_ANORET': 'meadow_AF_ANORET', 'AF_MEMFUNC': 'meadow_AF_MEMFUNC', 'AF_TRFUNC': 'meadow_AF_TRFUNC', 'AF_STRLIT': 'meadow_AF_STRLIT', 'AF_CHKUNI': 'meadow_AF_CHKUNI', 'AF_FIXUP': 'meadow_AF_FIXUP', 'AF_DREFOFF': 'meadow_AF_DREFOFF', 'AF_IMMOFF': 'meadow_AF_IMMOFF', 'AF_DATOFF': 'meadow_AF_DATOFF', 'AF_FLIRT': 'meadow_AF_FLIRT', 'AF_SIGCMT': 'meadow_AF_SIGCMT', 'AF_SIGMLT': 'meadow_AF_SIGMLT', 'AF_HFLIRT': 'meadow_AF_HFLIRT', 'AF_JFUNC': 'meadow_AF_JFUNC', 'AF_NULLSUB': 'meadow_AF_NULLSUB', 'AF_DODATA': 'meadow_AF_DODATA', 'AF_DOCODE': 'meadow_AF_DOCODE', 'AF_FINAL': 'meadow_AF_FINAL', 'AF2_DOEH': 'meadow_AF2_DOEH', 'AF2_DORTTI': 'meadow_AF2_DORTTI', 'NM_REL_OFF': 'meadow_NM_REL_OFF', 'NM_PTR_OFF': 'meadow_NM_PTR_OFF', 'NM_NAM_OFF': 'meadow_NM_NAM_OFF', 'NM_REL_EA': 'meadow_NM_REL_EA', 'NM_PTR_EA': 'meadow_NM_PTR_EA', 'NM_NAM_EA': 'meadow_NM_NAM_EA', 'NM_EA': 'meadow_NM_EA', 'NM_EA4': 'meadow_NM_EA4', 'NM_EA8': 'meadow_NM_EA8', 'NM_SHORT': 'meadow_NM_SHORT', 'NM_SERIAL': 'meadow_NM_SERIAL', 'ABI_8ALIGN4': 'meadow_ABI_8ALIGN4', 'ABI_PACK_STKARGS': 'meadow_ABI_PACK_STKARGS', 'ABI_BIGARG_ALIGN': 'meadow_ABI_BIGARG_ALIGN', 'ABI_STACK_LDBL': 'meadow_ABI_STACK_LDBL', 'ABI_STACK_VARARGS': 'meadow_ABI_STACK_VARARGS', 'ABI_HARD_FLOAT': 'meadow_ABI_HARD_FLOAT', 'ABI_SET_BY_USER': 'meadow_ABI_SET_BY_USER', 'ABI_GCC_LAYOUT': 'meadow_ABI_GCC_LAYOUT', 'UA_MAXOP': 'meadow_UA_MAXOP', 'MAXADDR': 'meadow_MAXADDR', 'IDB_EXT32': 'meadow_IDB_EXT32', 'IDB_EXT64': 'meadow_IDB_EXT64', 'IDB_EXT': 'meadow_IDB_EXT'})
class meadow_ida_ida:

    @meadow_wrap_module('idaapi')
    @meadow_wrap_module('idc', full=False)
    @_name_boundary.callable_contract({'self': 'meadow_self_e619978', 'db': 'meadow_db_37bcb78', 'api': 'meadow_api_local_ec1f699'}, '__init__')
    def __init__(meadow_self_e619978, meadow_db_37bcb78, meadow_api_local_ec1f699):
        _name_boundary.attributes(meadow_self_e619978)['idb'] = meadow_db_37bcb78
        meadow_self_e619978.api = meadow_api_local_ec1f699
        _name_boundary.attributes(meadow_self_e619978)['f_EXE_old'] = 0
        _name_boundary.attributes(meadow_self_e619978)['f_COM_old'] = 1
        _name_boundary.attributes(meadow_self_e619978)['f_BIN'] = 2
        _name_boundary.attributes(meadow_self_e619978)['f_DRV'] = 3
        _name_boundary.attributes(meadow_self_e619978)['f_WIN'] = 4
        _name_boundary.attributes(meadow_self_e619978)['f_HEX'] = 5
        _name_boundary.attributes(meadow_self_e619978)['f_MEX'] = 6
        _name_boundary.attributes(meadow_self_e619978)['f_LX'] = 7
        _name_boundary.attributes(meadow_self_e619978)['f_LE'] = 8
        _name_boundary.attributes(meadow_self_e619978)['f_NLM'] = 9
        _name_boundary.attributes(meadow_self_e619978)['f_COFF'] = 10
        _name_boundary.attributes(meadow_self_e619978)['f_PE'] = 11
        _name_boundary.attributes(meadow_self_e619978)['f_OMF'] = 12
        _name_boundary.attributes(meadow_self_e619978)['f_SREC'] = 13
        _name_boundary.attributes(meadow_self_e619978)['f_ZIP'] = 14
        _name_boundary.attributes(meadow_self_e619978)['f_OMFLIB'] = 15
        _name_boundary.attributes(meadow_self_e619978)['f_AR'] = 16
        _name_boundary.attributes(meadow_self_e619978)['f_LOADER'] = 17
        _name_boundary.attributes(meadow_self_e619978)['f_ELF'] = 18
        _name_boundary.attributes(meadow_self_e619978)['f_W32RUN'] = 19
        _name_boundary.attributes(meadow_self_e619978)['f_AOUT'] = 20
        _name_boundary.attributes(meadow_self_e619978)['f_PRC'] = 21
        _name_boundary.attributes(meadow_self_e619978)['f_EXE'] = 22
        _name_boundary.attributes(meadow_self_e619978)['f_COM'] = 23
        _name_boundary.attributes(meadow_self_e619978)['f_AIXAR'] = 24
        _name_boundary.attributes(meadow_self_e619978)['f_MACHO'] = 25
        _name_boundary.attributes(meadow_self_e619978)['STT_CUR'] = -1
        _name_boundary.attributes(meadow_self_e619978)['STT_VA'] = 0
        _name_boundary.attributes(meadow_self_e619978)['STT_MM'] = 1
        _name_boundary.attributes(meadow_self_e619978)['STT_DBG'] = 2
        _name_boundary.attributes(meadow_self_e619978)['INFFL_AUTO'] = 1
        _name_boundary.attributes(meadow_self_e619978)['INFFL_ALLASM'] = 2
        _name_boundary.attributes(meadow_self_e619978)['INFFL_LOADIDC'] = 4
        _name_boundary.attributes(meadow_self_e619978)['INFFL_NOUSER'] = 8
        _name_boundary.attributes(meadow_self_e619978)['INFFL_READONLY'] = 16
        _name_boundary.attributes(meadow_self_e619978)['INFFL_CHKOPS'] = 32
        _name_boundary.attributes(meadow_self_e619978)['INFFL_NMOPS'] = 64
        _name_boundary.attributes(meadow_self_e619978)['INFFL_GRAPH_VIEW'] = 128
        _name_boundary.attributes(meadow_self_e619978)['LFLG_PC_FPP'] = 1
        _name_boundary.attributes(meadow_self_e619978)['LFLG_PC_FLAT'] = 2
        _name_boundary.attributes(meadow_self_e619978)['LFLG_64BIT'] = 4
        _name_boundary.attributes(meadow_self_e619978)['LFLG_IS_DLL'] = 8
        _name_boundary.attributes(meadow_self_e619978)['LFLG_FLAT_OFF32'] = 16
        _name_boundary.attributes(meadow_self_e619978)['LFLG_MSF'] = 32
        _name_boundary.attributes(meadow_self_e619978)['LFLG_WIDE_HBF'] = 64
        _name_boundary.attributes(meadow_self_e619978)['LFLG_DBG_NOPATH'] = 128
        _name_boundary.attributes(meadow_self_e619978)['LFLG_SNAPSHOT'] = 256
        _name_boundary.attributes(meadow_self_e619978)['LFLG_PACK'] = 512
        _name_boundary.attributes(meadow_self_e619978)['LFLG_COMPRESS'] = 1024
        _name_boundary.attributes(meadow_self_e619978)['LFLG_KERNMODE'] = 2048
        _name_boundary.attributes(meadow_self_e619978)['IDB_UNPACKED'] = 0
        _name_boundary.attributes(meadow_self_e619978)['IDB_PACKED'] = 1
        _name_boundary.attributes(meadow_self_e619978)['IDB_COMPRESSED'] = 2
        _name_boundary.attributes(meadow_self_e619978)['AF_CODE'] = 1
        _name_boundary.attributes(meadow_self_e619978)['AF_MARKCODE'] = 2
        _name_boundary.attributes(meadow_self_e619978)['AF_JUMPTBL'] = 4
        _name_boundary.attributes(meadow_self_e619978)['AF_PURDAT'] = 8
        _name_boundary.attributes(meadow_self_e619978)['AF_USED'] = 16
        _name_boundary.attributes(meadow_self_e619978)['AF_UNK'] = 32
        _name_boundary.attributes(meadow_self_e619978)['AF_PROCPTR'] = 64
        _name_boundary.attributes(meadow_self_e619978)['AF_PROC'] = 128
        _name_boundary.attributes(meadow_self_e619978)['AF_FTAIL'] = 256
        _name_boundary.attributes(meadow_self_e619978)['AF_LVAR'] = 512
        _name_boundary.attributes(meadow_self_e619978)['AF_STKARG'] = 1024
        _name_boundary.attributes(meadow_self_e619978)['AF_REGARG'] = 2048
        _name_boundary.attributes(meadow_self_e619978)['AF_TRACE'] = 4096
        _name_boundary.attributes(meadow_self_e619978)['AF_VERSP'] = 8192
        _name_boundary.attributes(meadow_self_e619978)['AF_ANORET'] = 16384
        _name_boundary.attributes(meadow_self_e619978)['AF_MEMFUNC'] = 32768
        _name_boundary.attributes(meadow_self_e619978)['AF_TRFUNC'] = 65536
        _name_boundary.attributes(meadow_self_e619978)['AF_STRLIT'] = 131072
        _name_boundary.attributes(meadow_self_e619978)['AF_CHKUNI'] = 262144
        _name_boundary.attributes(meadow_self_e619978)['AF_FIXUP'] = 524288
        _name_boundary.attributes(meadow_self_e619978)['AF_DREFOFF'] = 1048576
        _name_boundary.attributes(meadow_self_e619978)['AF_IMMOFF'] = 2097152
        _name_boundary.attributes(meadow_self_e619978)['AF_DATOFF'] = 4194304
        _name_boundary.attributes(meadow_self_e619978)['AF_FLIRT'] = 8388608
        _name_boundary.attributes(meadow_self_e619978)['AF_SIGCMT'] = 16777216
        _name_boundary.attributes(meadow_self_e619978)['AF_SIGMLT'] = 33554432
        _name_boundary.attributes(meadow_self_e619978)['AF_HFLIRT'] = 67108864
        _name_boundary.attributes(meadow_self_e619978)['AF_JFUNC'] = 134217728
        _name_boundary.attributes(meadow_self_e619978)['AF_NULLSUB'] = 268435456
        _name_boundary.attributes(meadow_self_e619978)['AF_DODATA'] = 536870912
        _name_boundary.attributes(meadow_self_e619978)['AF_DOCODE'] = 1073741824
        _name_boundary.attributes(meadow_self_e619978)['AF_FINAL'] = -2147483648
        _name_boundary.attributes(meadow_self_e619978)['AF2_DOEH'] = 1
        _name_boundary.attributes(meadow_self_e619978)['AF2_DORTTI'] = 2
        _name_boundary.attributes(meadow_self_e619978)['NM_REL_OFF'] = 0
        _name_boundary.attributes(meadow_self_e619978)['NM_PTR_OFF'] = 1
        _name_boundary.attributes(meadow_self_e619978)['NM_NAM_OFF'] = 2
        _name_boundary.attributes(meadow_self_e619978)['NM_REL_EA'] = 3
        _name_boundary.attributes(meadow_self_e619978)['NM_PTR_EA'] = 4
        _name_boundary.attributes(meadow_self_e619978)['NM_NAM_EA'] = 5
        _name_boundary.attributes(meadow_self_e619978)['NM_EA'] = 6
        _name_boundary.attributes(meadow_self_e619978)['NM_EA4'] = 7
        _name_boundary.attributes(meadow_self_e619978)['NM_EA8'] = 8
        _name_boundary.attributes(meadow_self_e619978)['NM_SHORT'] = 9
        _name_boundary.attributes(meadow_self_e619978)['NM_SERIAL'] = 10
        _name_boundary.attributes(meadow_self_e619978)['ABI_8ALIGN4'] = 1
        _name_boundary.attributes(meadow_self_e619978)['ABI_PACK_STKARGS'] = 2
        _name_boundary.attributes(meadow_self_e619978)['ABI_BIGARG_ALIGN'] = 4
        _name_boundary.attributes(meadow_self_e619978)['ABI_STACK_LDBL'] = 8
        _name_boundary.attributes(meadow_self_e619978)['ABI_STACK_VARARGS'] = 16
        _name_boundary.attributes(meadow_self_e619978)['ABI_HARD_FLOAT'] = 32
        _name_boundary.attributes(meadow_self_e619978)['ABI_SET_BY_USER'] = 64
        _name_boundary.attributes(meadow_self_e619978)['ABI_GCC_LAYOUT'] = 128
        _name_boundary.attributes(meadow_self_e619978)['UA_MAXOP'] = 8
        _name_boundary.attributes(meadow_self_e619978)['MAXADDR'] = 4278190080
        _name_boundary.attributes(meadow_self_e619978)['IDB_EXT32'] = 'idb'
        _name_boundary.attributes(meadow_self_e619978)['IDB_EXT64'] = 'i64'
        _name_boundary.attributes(meadow_self_e619978)['IDB_EXT'] = 'idb'

@_name_boundary.class_contract('ida_ua', {'o_void': 'meadow_o_void', 'o_reg': 'meadow_o_reg', 'o_mem': 'meadow_o_mem', 'o_phrase': 'meadow_o_phrase', 'o_displ': 'meadow_o_displ', 'o_imm': 'meadow_o_imm', 'o_far': 'meadow_o_far', 'o_near': 'meadow_o_near', 'o_idpspec0': 'meadow_o_idpspec0', 'o_idpspec1': 'meadow_o_idpspec1', 'o_idpspec2': 'meadow_o_idpspec2', 'o_idpspec3': 'meadow_o_idpspec3', 'o_idpspec4': 'meadow_o_idpspec4', 'o_idpspec5': 'meadow_o_idpspec5', 'idb': 'meadow_idb'})
class meadow_ida_ua:
    meadow_o_void = 0
    meadow_o_reg = 1
    meadow_o_mem = 2
    meadow_o_phrase = 3
    meadow_o_displ = 4
    meadow_o_imm = 5
    meadow_o_far = 6
    meadow_o_near = 7
    meadow_o_idpspec0 = 8
    meadow_o_idpspec1 = 9
    meadow_o_idpspec2 = 10
    meadow_o_idpspec3 = 11
    meadow_o_idpspec4 = 12
    meadow_o_idpspec5 = 13

    @meadow_wrap_module('idaapi')
    @meadow_wrap_module('idc', full=False)
    @_name_boundary.callable_contract({'self': 'meadow_self_39f55c5', 'db': 'meadow_db_9973417', 'api': 'meadow_api_local_295ac2a'}, '__init__')
    def __init__(meadow_self_39f55c5, meadow_db_9973417, meadow_api_local_295ac2a):
        _name_boundary.attributes(meadow_self_39f55c5)['idb'] = meadow_db_9973417
        meadow_self_39f55c5.api = meadow_api_local_295ac2a

@_name_boundary.class_contract('idc', {'SEGPERM_EXEC': 'meadow_SEGPERM_EXEC', 'SEGPERM_WRITE': 'meadow_SEGPERM_WRITE', 'SEGPERM_READ': 'meadow_SEGPERM_READ', 'SEGPERM_MAXVAL': 'meadow_SEGPERM_MAXVAL', 'SFL_COMORG': 'meadow_SFL_COMORG', 'SFL_OBOK': 'meadow_SFL_OBOK', 'SFL_HIDDEN': 'meadow_SFL_HIDDEN', 'SFL_DEBUG': 'meadow_SFL_DEBUG', 'SFL_LOADER': 'meadow_SFL_LOADER', 'SFL_HIDETYPE': 'meadow_SFL_HIDETYPE', 'ScreenEA': 'meadow_ScreenEA', '_get_segment': 'meadow__get_segment', 'SegStart': 'meadow_SegStart', 'SegEnd': 'meadow_SegEnd', 'FirstSeg': 'meadow_FirstSeg', 'NextSeg': 'meadow_NextSeg', 'SegName': 'meadow_SegName', 'GetSegmentAttr': 'meadow_GetSegmentAttr', 'MinEA': 'meadow_MinEA', 'MaxEA': 'meadow_MaxEA', 'GetFlags': 'meadow_GetFlags', 'IdbByte': 'meadow_IdbByte', 'Head': 'meadow_Head', 'ItemSize': 'meadow_ItemSize', 'NextHead': 'meadow_NextHead', 'PrevHead': 'meadow_PrevHead', 'GetManyBytes': 'meadow_GetManyBytes', '_load_dis': 'meadow__load_dis', '_disassemble': 'meadow__disassemble', 'print_insn_mnem': 'meadow_print_insn_mnem', 'GetDisasm': 'meadow_GetDisasm', 'print_operand': 'meadow_print_operand', 'get_operand_type': 'meadow_get_operand_type', 'CIC_ITEM': 'meadow_CIC_ITEM', 'CIC_FUNC': 'meadow_CIC_FUNC', 'CIC_SEGM': 'meadow_CIC_SEGM', 'DEFCOLOR': 'meadow_DEFCOLOR', 'GetColor': 'meadow_GetColor', 'GetFunctionFlags': 'meadow_GetFunctionFlags', 'GetFunctionAttr': 'meadow_GetFunctionAttr', 'GetFunctionName': 'meadow_GetFunctionName', 'find_func_end': 'meadow_find_func_end', 'LocByName': 'meadow_LocByName', 'GetInputMD5': 'meadow_GetInputMD5', 'GetInputSHA256': 'meadow_GetInputSHA256', 'GetInputFile': 'meadow_GetInputFile', 'Comment': 'meadow_Comment', 'RptCmt': 'meadow_RptCmt', 'GetCommentEx': 'meadow_GetCommentEx', 'GetType': 'meadow_GetType', 'hasValue': 'meadow_hasValue', 'isDefArg0': 'meadow_isDefArg0', 'isDefArg1': 'meadow_isDefArg1', 'isOff0': 'meadow_isOff0', 'isOff1': 'meadow_isOff1', 'isChar0': 'meadow_isChar0', 'isChar1': 'meadow_isChar1', 'isSeg0': 'meadow_isSeg0', 'isSeg1': 'meadow_isSeg1', 'isEnum0': 'meadow_isEnum0', 'isEnum1': 'meadow_isEnum1', 'isStroff0': 'meadow_isStroff0', 'isStroff1': 'meadow_isStroff1', 'isStkvar0': 'meadow_isStkvar0', 'isStkvar1': 'meadow_isStkvar1', 'isFloat0': 'meadow_isFloat0', 'isFloat1': 'meadow_isFloat1', 'isCustFmt0': 'meadow_isCustFmt0', 'isCustFmt1': 'meadow_isCustFmt1', 'isNum0': 'meadow_isNum0', 'isNum1': 'meadow_isNum1', 'get_optype_flags0': 'meadow_get_optype_flags0', 'get_optype_flags1': 'meadow_get_optype_flags1', 'LineA': 'meadow_LineA', 'LineB': 'meadow_LineB', 'idb': 'meadow_idb', 'bit_dis': 'meadow_bit_dis', 'seg_dis': 'meadow_seg_dis', 'ARGV': 'meadow_ARGV', 'GetMnem': 'meadow_GetMnem', 'GetOpnd': 'meadow_GetOpnd', 'GetOpType': 'meadow_GetOpType', 'FindFuncEnd': 'meadow_FindFuncEnd', 'FUNCATTR_START': 'meadow_FUNCATTR_START', 'FUNCATTR_END': 'meadow_FUNCATTR_END', 'FUNCATTR_FLAGS': 'meadow_FUNCATTR_FLAGS', 'FUNCATTR_FRAME': 'meadow_FUNCATTR_FRAME', 'FUNCATTR_FRSIZE': 'meadow_FUNCATTR_FRSIZE', 'FUNCATTR_FRREGS': 'meadow_FUNCATTR_FRREGS', 'FUNCATTR_ARGSIZE': 'meadow_FUNCATTR_ARGSIZE', 'FUNCATTR_FPD': 'meadow_FUNCATTR_FPD', 'FUNCATTR_COLOR': 'meadow_FUNCATTR_COLOR', 'SEGATTR_START': 'meadow_SEGATTR_START', 'SEGATTR_END': 'meadow_SEGATTR_END', 'SEGATTR_ORGBASE': 'meadow_SEGATTR_ORGBASE', 'SEGATTR_ALIGN': 'meadow_SEGATTR_ALIGN', 'SEGATTR_COMB': 'meadow_SEGATTR_COMB', 'SEGATTR_PERM': 'meadow_SEGATTR_PERM', 'SEGATTR_BITNESS': 'meadow_SEGATTR_BITNESS', 'SEGATTR_FLAGS': 'meadow_SEGATTR_FLAGS', 'SEGATTR_SEL': 'meadow_SEGATTR_SEL', 'SEGATTR_ES': 'meadow_SEGATTR_ES', 'SEGATTR_CS': 'meadow_SEGATTR_CS', 'SEGATTR_SS': 'meadow_SEGATTR_SS', 'SEGATTR_DS': 'meadow_SEGATTR_DS', 'SEGATTR_FS': 'meadow_SEGATTR_FS', 'SEGATTR_GS': 'meadow_SEGATTR_GS', 'SEGATTR_TYPE': 'meadow_SEGATTR_TYPE', 'SEGATTR_COLOR': 'meadow_SEGATTR_COLOR', 'BADADDR': 'meadow_BADADDR', 'FUNCATTR_OWNER': 'meadow_FUNCATTR_OWNER', 'FUNCATTR_REFQTY': 'meadow_FUNCATTR_REFQTY'})
class meadow_idc:
    meadow_SEGPERM_EXEC = 1
    meadow_SEGPERM_WRITE = 2
    meadow_SEGPERM_READ = 4
    meadow_SEGPERM_MAXVAL = 7
    meadow_SFL_COMORG = 1
    meadow_SFL_OBOK = 2
    meadow_SFL_HIDDEN = 4
    meadow_SFL_DEBUG = 8
    meadow_SFL_LOADER = 16
    meadow_SFL_HIDETYPE = 32

    @_name_boundary.callable_contract({'self': 'meadow_self_8989054', 'db': 'meadow_db_29ab53f', 'api': 'meadow_api_local_e6148a5'}, '__init__')
    def __init__(meadow_self_8989054, meadow_db_29ab53f, meadow_api_local_e6148a5):
        _name_boundary.attributes(meadow_self_8989054)['idb'] = meadow_db_29ab53f
        meadow_self_8989054.api = meadow_api_local_e6148a5
        _name_boundary.attributes(meadow_self_8989054)['bit_dis'] = None
        _name_boundary.attributes(meadow_self_8989054)['seg_dis'] = None
        if _name_boundary.attributes(meadow_self_8989054)['idb'].wordsize == 4:
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_START'] = 0
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_END'] = 4
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FLAGS'] = 8
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRAME'] = 10
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRSIZE'] = 14
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRREGS'] = 18
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_ARGSIZE'] = 20
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FPD'] = 24
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_COLOR'] = 28
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_START'] = 0
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_END'] = 4
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ORGBASE'] = 16
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ALIGN'] = 20
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_COMB'] = 21
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_PERM'] = 22
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_BITNESS'] = 23
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_FLAGS'] = 24
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_SEL'] = 28
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ES'] = 32
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_CS'] = 36
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_SS'] = 40
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_DS'] = 44
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_FS'] = 48
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_GS'] = 52
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_TYPE'] = 96
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_COLOR'] = 100
            _name_boundary.attributes(meadow_self_8989054)['BADADDR'] = 4294967295
            meadow_self_8989054.__EA64__ = False
        elif _name_boundary.attributes(meadow_self_8989054)['idb'].wordsize == 8:
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_START'] = 0
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_END'] = 8
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FLAGS'] = 16
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRAME'] = 18
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRSIZE'] = 26
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FRREGS'] = 34
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_ARGSIZE'] = 36
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_FPD'] = 44
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_COLOR'] = 52
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_OWNER'] = 18
            _name_boundary.attributes(meadow_self_8989054)['FUNCATTR_REFQTY'] = 26
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_START'] = 0
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_END'] = 8
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ORGBASE'] = 32
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ALIGN'] = 40
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_COMB'] = 41
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_PERM'] = 42
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_BITNESS'] = 43
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_FLAGS'] = 44
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_SEL'] = 48
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_ES'] = 56
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_CS'] = 64
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_SS'] = 72
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_DS'] = 80
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_FS'] = 88
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_GS'] = 96
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_TYPE'] = 184
            _name_boundary.attributes(meadow_self_8989054)['SEGATTR_COLOR'] = 188
            _name_boundary.attributes(meadow_self_8989054)['BADADDR'] = 18446744073709551615
            meadow_self_8989054.__EA64__ = True
        else:
            raise RuntimeError('unexpected wordsize')
        _name_boundary.attributes(meadow_self_8989054)['ARGV'] = []
        _name_boundary.attributes(meadow_self_8989054)['GetMnem'] = _name_boundary.attributes(meadow_self_8989054)['print_insn_mnem']
        _name_boundary.attributes(meadow_self_8989054)['GetOpnd'] = _name_boundary.attributes(meadow_self_8989054)['print_operand']
        _name_boundary.attributes(meadow_self_8989054)['GetOpType'] = _name_boundary.attributes(meadow_self_8989054)['get_operand_type']
        _name_boundary.attributes(meadow_self_8989054)['FindFuncEnd'] = _name_boundary.attributes(meadow_self_8989054)['find_func_end']

    @_name_boundary.callable_contract({'self': 'meadow_self_e9a1c35'}, 'ScreenEA')
    def meadow_ScreenEA(meadow_self_e9a1c35):
        return _name_boundary.attributes(meadow_self_e9a1c35.api)['ScreenEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_f8a43a0', 'ea': 'meadow_ea_e6f5eb4'}, '_get_segment')
    def meadow__get_segment(meadow_self_f8a43a0, meadow_ea_e6f5eb4):
        meadow_segs_687a9e3 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_f8a43a0)['idb']).segments
        for meadow_seg_local_b99383d in meadow_segs_687a9e3.values():
            if _name_boundary.attributes(meadow_seg_local_b99383d)['startEA'] <= meadow_ea_e6f5eb4 < _name_boundary.attributes(meadow_seg_local_b99383d)['endEA']:
                return meadow_seg_local_b99383d

    @_name_boundary.callable_contract({'self': 'meadow_self_430a8e9', 'ea': 'meadow_ea_2eb8c19'}, 'SegStart')
    def meadow_SegStart(meadow_self_430a8e9, meadow_ea_2eb8c19):
        meadow_seg_local_2e827e4 = _name_boundary.attributes(meadow_self_430a8e9)['_get_segment'](meadow_ea_2eb8c19)
        if meadow_seg_local_2e827e4 is None:
            return None
        return _name_boundary.attributes(meadow_seg_local_2e827e4)['startEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_9c682f9', 'ea': 'meadow_ea_42373d2'}, 'SegEnd')
    def meadow_SegEnd(meadow_self_9c682f9, meadow_ea_42373d2):
        meadow_seg_local_a1e3b20 = _name_boundary.attributes(meadow_self_9c682f9)['_get_segment'](meadow_ea_42373d2)
        if meadow_seg_local_a1e3b20 is None:
            return None
        return _name_boundary.attributes(meadow_seg_local_a1e3b20)['endEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_9f6ecf1'}, 'FirstSeg')
    def meadow_FirstSeg(meadow_self_9f6ecf1):
        meadow_segs_af01a53 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_9f6ecf1)['idb']).segments
        for meadow_startEA_f5cee3b in sorted(meadow_segs_af01a53.keys()):
            return meadow_startEA_f5cee3b

    @_name_boundary.callable_contract({'self': 'meadow_self_f3cc917', 'ea': 'meadow_ea_25990c4'}, 'NextSeg')
    def meadow_NextSeg(meadow_self_f3cc917, meadow_ea_25990c4):
        meadow_segs_d0abb1e = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_f3cc917)['idb']).segments.values()
        meadow_segs_d0abb1e = sorted(meadow_segs_d0abb1e, key=_name_boundary.callable_contract({'s': 'meadow_s_local_06c7d12'}, '<lambda>')(lambda meadow_s_local_06c7d12: _name_boundary.attributes(meadow_s_local_06c7d12)['startEA']))
        for meadow_i_3a06571, meadow_seg_local_7387e44 in enumerate(meadow_segs_d0abb1e):
            if _name_boundary.attributes(meadow_seg_local_7387e44)['startEA'] <= meadow_ea_25990c4 < _name_boundary.attributes(meadow_seg_local_7387e44)['endEA']:
                if meadow_i_3a06571 < len(meadow_segs_d0abb1e) - 1:
                    return _name_boundary.attributes(meadow_segs_d0abb1e[meadow_i_3a06571 + 1])['startEA']
                else:
                    return _name_boundary.attributes(meadow_self_f3cc917)['BADADDR']

    @_name_boundary.callable_contract({'self': 'meadow_self_edb3097', 'ea': 'meadow_ea_01f30a7'}, 'SegName')
    def meadow_SegName(meadow_self_edb3097, meadow_ea_01f30a7):
        meadow_segstrings_1141dd5 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'].SegStrings(_name_boundary.attributes(meadow_self_edb3097)['idb']))['strings']
        return meadow_segstrings_1141dd5[_name_boundary.attributes(_name_boundary.attributes(meadow_self_edb3097)['_get_segment'](meadow_ea_01f30a7))['name_index']]

    @_name_boundary.callable_contract({'self': 'meadow_self_f42cbdc', 'ea': 'meadow_ea_9aa1a71', 'attr': 'meadow_attr_5f2bd7f'}, 'GetSegmentAttr')
    def meadow_GetSegmentAttr(meadow_self_f42cbdc, meadow_ea_9aa1a71, meadow_attr_5f2bd7f):
        if meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_START']:
            return _name_boundary.attributes(meadow_self_f42cbdc)['SegStart'](meadow_ea_9aa1a71)
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_END']:
            return _name_boundary.attributes(meadow_self_f42cbdc)['SegEnd'](meadow_ea_9aa1a71)
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_ORGBASE']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['orgbase']
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_ALIGN']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['align']
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_COMB']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['comb']
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_PERM']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['perm']
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_BITNESS']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['bitness']
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_FLAGS']:
            return _name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71).flags
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_TYPE']:
            return _name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71).type
        elif meadow_attr_5f2bd7f == _name_boundary.attributes(meadow_self_f42cbdc)['SEGATTR_COLOR']:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f42cbdc)['_get_segment'](meadow_ea_9aa1a71))['color']
        else:
            raise NotImplementedError('segment attribute %d not yet implemented' % meadow_attr_5f2bd7f)

    @_name_boundary.callable_contract({'self': 'meadow_self_2687445'}, 'MinEA')
    def meadow_MinEA(meadow_self_2687445):
        meadow_segs_97a6221 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_2687445)['idb']).segments.values()
        meadow_segs_97a6221 = list(sorted(meadow_segs_97a6221, key=_name_boundary.callable_contract({'s': 'meadow_s_local_b4a2415'}, '<lambda>')(lambda meadow_s_local_b4a2415: _name_boundary.attributes(meadow_s_local_b4a2415)['startEA'])))
        return _name_boundary.attributes(meadow_segs_97a6221[0])['startEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_d550d00'}, 'MaxEA')
    def meadow_MaxEA(meadow_self_d550d00):
        meadow_segs_c7e6693 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_d550d00)['idb']).segments.values()
        meadow_segs_c7e6693 = list(sorted(meadow_segs_c7e6693, key=_name_boundary.callable_contract({'s': 'meadow_s_local_21e5bff'}, '<lambda>')(lambda meadow_s_local_21e5bff: _name_boundary.attributes(meadow_s_local_21e5bff)['startEA'])))
        return _name_boundary.attributes(meadow_segs_c7e6693[-1])['endEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_8fcffe0', 'ea': 'meadow_ea_8f2ca53'}, 'GetFlags')
    def meadow_GetFlags(meadow_self_8fcffe0, meadow_ea_8f2ca53):
        try:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_8fcffe0)['idb'].id1)['get_flags'](meadow_ea_8f2ca53)
        except KeyError:
            return 0

    @_name_boundary.callable_contract({'self': 'meadow_self_62ff5e4', 'ea': 'meadow_ea_c70f29c'}, 'IdbByte')
    def meadow_IdbByte(meadow_self_62ff5e4, meadow_ea_c70f29c):
        meadow_flags_local_2d0112d = _name_boundary.attributes(meadow_self_62ff5e4)['GetFlags'](meadow_ea_c70f29c)
        if _name_boundary.attributes(meadow_self_62ff5e4)['hasValue'](meadow_flags_local_2d0112d):
            return meadow_flags_local_2d0112d & _name_boundary.attributes(meadow_FLAGS)['MS_VAL']
        else:
            raise KeyError(meadow_ea_c70f29c)

    @_name_boundary.callable_contract({'self': 'meadow_self_3dac39c', 'ea': 'meadow_ea_02e7b0f'}, 'Head')
    def meadow_Head(meadow_self_3dac39c, meadow_ea_02e7b0f):
        meadow_flags_local_9245b5b = _name_boundary.attributes(meadow_self_3dac39c)['GetFlags'](meadow_ea_02e7b0f)
        while not _name_boundary.attributes(_name_boundary.attributes(meadow_self_3dac39c.api)['ida_bytes'])['is_head'](meadow_flags_local_9245b5b):
            meadow_ea_02e7b0f -= 1
            meadow_flags_local_9245b5b = _name_boundary.attributes(meadow_self_3dac39c)['GetFlags'](meadow_ea_02e7b0f)
        return meadow_ea_02e7b0f

    @_name_boundary.callable_contract({'self': 'meadow_self_91b3b79', 'ea': 'meadow_ea_2362127'}, 'ItemSize')
    def meadow_ItemSize(meadow_self_91b3b79, meadow_ea_2362127):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_91b3b79.api)['ida_bytes'])['get_item_end'](meadow_ea_2362127) - meadow_ea_2362127

    @_name_boundary.callable_contract({'self': 'meadow_self_728fa55', 'ea': 'meadow_ea_eacdb2c'}, 'NextHead')
    def meadow_NextHead(meadow_self_728fa55, meadow_ea_eacdb2c):
        meadow_ea_eacdb2c += 1
        meadow_flags_local_b5b7d89 = _name_boundary.attributes(meadow_self_728fa55)['GetFlags'](meadow_ea_eacdb2c)
        while meadow_flags_local_b5b7d89 is not None and meadow_flags_local_b5b7d89 != 0 and (not _name_boundary.attributes(_name_boundary.attributes(meadow_self_728fa55.api)['ida_bytes'])['is_head'](meadow_flags_local_b5b7d89)):
            meadow_ea_eacdb2c += 1
            meadow_flags_local_b5b7d89 = _name_boundary.attributes(meadow_self_728fa55)['GetFlags'](meadow_ea_eacdb2c)
        return meadow_ea_eacdb2c

    @_name_boundary.callable_contract({'self': 'meadow_self_073bb92', 'ea': 'meadow_ea_f31d414'}, 'PrevHead')
    def meadow_PrevHead(meadow_self_073bb92, meadow_ea_f31d414):
        meadow_ea_f31d414 = _name_boundary.attributes(meadow_self_073bb92)['Head'](meadow_ea_f31d414)
        meadow_ea_f31d414 -= 1
        return _name_boundary.attributes(meadow_self_073bb92)['Head'](meadow_ea_f31d414)

    @_name_boundary.callable_contract({'self': 'meadow_self_cebe694', 'ea': 'meadow_ea_fcbc738', 'use_dbg': 'meadow_use_dbg_353d5dc', 'size': 'meadow_size_local_cd87fa2'}, 'GetManyBytes')
    def meadow_GetManyBytes(meadow_self_cebe694, meadow_ea_fcbc738, meadow_size_local_cd87fa2, meadow_use_dbg_353d5dc=False):
        """
        Raises:
          IndexError: if the range extends beyond a segment.
          KeyError: if a byte is not defined.
        """
        if meadow_use_dbg_353d5dc:
            raise NotImplementedError()
        if _name_boundary.attributes(meadow_self_cebe694)['SegStart'](meadow_ea_fcbc738) != _name_boundary.attributes(meadow_self_cebe694)['SegStart'](meadow_ea_fcbc738 + meadow_size_local_cd87fa2):
            if meadow_ea_fcbc738 + meadow_size_local_cd87fa2 == _name_boundary.attributes(meadow_self_cebe694)['SegEnd'](meadow_ea_fcbc738):
                pass
            else:
                raise IndexError((meadow_ea_fcbc738, meadow_ea_fcbc738 + meadow_size_local_cd87fa2))
        meadow_ret_local_366c513 = []
        try:
            for meadow_i_9a521db in range(meadow_ea_fcbc738, meadow_ea_fcbc738 + meadow_size_local_cd87fa2):
                meadow_ret_local_366c513.append(_name_boundary.attributes(meadow_self_cebe694)['IdbByte'](meadow_i_9a521db))
        except KeyError:
            meadow_ret_local_366c513.extend([0 for meadow___4463b3e in range(meadow_size_local_cd87fa2 - len(meadow_ret_local_366c513))])
        if meadow_six.PY2:
            return ''.join(map(chr, meadow_ret_local_366c513))
        else:
            return bytes(meadow_ret_local_366c513)

    @_name_boundary.callable_contract({'self': 'meadow_self_0b8fb6e', 'arch': 'meadow_arch_b953b26', 'mode': 'meadow_mode_0d68961'}, '_load_dis')
    def meadow__load_dis(meadow_self_0b8fb6e, meadow_arch_b953b26, meadow_mode_0d68961):
        import capstone as meadow_capstone_41c0b05
        if _name_boundary.attributes(meadow_self_0b8fb6e)['bit_dis'] is None:
            _name_boundary.attributes(meadow_self_0b8fb6e)['bit_dis'] = {}
        if _name_boundary.attributes(_name_boundary.attributes(meadow_self_0b8fb6e)['bit_dis'])['get']((meadow_arch_b953b26, meadow_mode_0d68961)) is None:
            meadow_r_6d81a4a = meadow_capstone_41c0b05.Cs(meadow_arch_b953b26, meadow_mode_0d68961)
            _name_boundary.attributes(meadow_self_0b8fb6e)['bit_dis'][meadow_arch_b953b26, meadow_mode_0d68961] = meadow_r_6d81a4a
        return _name_boundary.attributes(meadow_self_0b8fb6e)['bit_dis'][meadow_arch_b953b26, meadow_mode_0d68961]

    @_name_boundary.callable_contract({'self': 'meadow_self_ad8d09e', 'ea': 'meadow_ea_e153f14'}, '_disassemble')
    def meadow__disassemble(meadow_self_ad8d09e, meadow_ea_e153f14):
        import capstone as meadow_capstone_6bb5fb4
        meadow_size_local_b776d01 = _name_boundary.attributes(meadow_self_ad8d09e)['ItemSize'](meadow_ea_e153f14)
        meadow_inst_buf_6647ed1 = _name_boundary.attributes(meadow_self_ad8d09e)['GetManyBytes'](meadow_ea_e153f14, meadow_size_local_b776d01)
        meadow_segment_local_675e7d2 = _name_boundary.attributes(meadow_self_ad8d09e)['_get_segment'](meadow_ea_e153f14)
        meadow_bitness_84a64d0 = 16 << _name_boundary.attributes(meadow_segment_local_675e7d2)['bitness']
        meadow_procname_local_1108968 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_ad8d09e.api)['idaapi'])['get_inf_structure']().procname.lower()
        meadow_dis_3d181ce = None
        if meadow_procname_local_1108968 == 'arm' and meadow_bitness_84a64d0 == 64:
            meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_ARM64, meadow_capstone_6bb5fb4.CS_MODE_ARM)
        elif meadow_procname_local_1108968 == 'arm' and meadow_bitness_84a64d0 == 32:
            if meadow_size_local_b776d01 == 2:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_ARM, meadow_capstone_6bb5fb4.CS_MODE_THUMB)
            else:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_ARM, meadow_capstone_6bb5fb4.CS_MODE_ARM)
        elif meadow_procname_local_1108968 in ['metapc', '8086', '80286r', '80286p', '80386r', '80386p', '80486r', '80486p', '80586r', '80586p', '80686p', 'k62', 'p2', 'p3', 'athlon', 'p4', '8085']:
            if meadow_bitness_84a64d0 == 16:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_X86, meadow_capstone_6bb5fb4.CS_MODE_16)
            elif meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_X86, meadow_capstone_6bb5fb4.CS_MODE_32)
            elif meadow_bitness_84a64d0 == 64:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_X86, meadow_capstone_6bb5fb4.CS_MODE_64)
        elif meadow_procname_local_1108968 == 'mipsb':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_MIPS, meadow_capstone_6bb5fb4.CS_MODE_MIPS32 | meadow_capstone_6bb5fb4.CS_MODE_BIG_ENDIAN)
            elif meadow_bitness_84a64d0 == 64:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_MIPS, meadow_capstone_6bb5fb4.CS_MODE_MIPS64 | meadow_capstone_6bb5fb4.CS_MODE_BIG_ENDIAN)
        elif meadow_procname_local_1108968 == 'mipsl':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_MIPS, meadow_capstone_6bb5fb4.CS_MODE_MIPS32 | meadow_capstone_6bb5fb4.CS_MODE_LITTLE_ENDIAN)
            elif meadow_bitness_84a64d0 == 64:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_MIPS, meadow_capstone_6bb5fb4.CS_MODE_MIPS64 | meadow_capstone_6bb5fb4.CS_MODE_LITTLE_ENDIAN)
        elif meadow_procname_local_1108968 == 'ppc':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_PPC, meadow_capstone_6bb5fb4.CS_MODE_32 | meadow_capstone_6bb5fb4.CS_MODE_BIG_ENDIAN)
            elif meadow_bitness_84a64d0 == 64:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_PPC, meadow_capstone_6bb5fb4.CS_MODE_64 | meadow_capstone_6bb5fb4.CS_MODE_BIG_ENDIAN)
        elif meadow_procname_local_1108968 == 'ppcl':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_PPC, meadow_capstone_6bb5fb4.CS_MODE_32 | meadow_capstone_6bb5fb4.CS_MODE_LITTLE_ENDIAN)
            elif meadow_bitness_84a64d0 == 64:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_PPC, meadow_capstone_6bb5fb4.CS_MODE_64 | meadow_capstone_6bb5fb4.CS_MODE_LITTLE_ENDIAN)
        elif meadow_procname_local_1108968 == 'sparcb':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_SPARC, meadow_capstone_6bb5fb4.CS_MODE_BIG_ENDIAN)
        elif meadow_procname_local_1108968 == 'sparcl':
            if meadow_bitness_84a64d0 == 32:
                meadow_dis_3d181ce = _name_boundary.attributes(meadow_self_ad8d09e)['_load_dis'](meadow_capstone_6bb5fb4.CS_ARCH_SPARC, meadow_capstone_6bb5fb4.CS_MODE_LITTLE_ENDIAN)
        if meadow_dis_3d181ce is None:
            raise NotImplementedError('unknown arch %s bit:%s inst_len:%d' % (meadow_procname_local_1108968, meadow_bitness_84a64d0, len(meadow_inst_buf_6647ed1)))
        meadow_dis_3d181ce.detail = True
        try:
            meadow_op_0f07c4b = next(meadow_dis_3d181ce.disasm(meadow_inst_buf_6647ed1, meadow_ea_e153f14))
        except StopIteration:
            raise RuntimeError('failed to disassemble %s' % hex(meadow_ea_e153f14))
        else:
            return meadow_op_0f07c4b

    @_name_boundary.callable_contract({'self': 'meadow_self_e8ea94e', 'ea': 'meadow_ea_835b01c'}, 'print_insn_mnem')
    def meadow_print_insn_mnem(meadow_self_e8ea94e, meadow_ea_835b01c):
        meadow_op_81897a7 = _name_boundary.attributes(meadow_self_e8ea94e)['_disassemble'](meadow_ea_835b01c)
        return meadow_op_81897a7.mnemonic

    @_name_boundary.callable_contract({'self': 'meadow_self_a642d4f', 'ea': 'meadow_ea_a070394'}, 'GetDisasm')
    def meadow_GetDisasm(meadow_self_a642d4f, meadow_ea_a070394):
        meadow_op_290149c = _name_boundary.attributes(meadow_self_a642d4f)['_disassemble'](meadow_ea_a070394)
        return '%s\t%s' % (meadow_op_290149c.mnemonic, meadow_op_290149c.op_str)

    @_name_boundary.callable_contract({'self': 'meadow_self_9a4e3bc', 'ea': 'meadow_ea_32c6d2e', 'n': 'meadow_n_e8ddb87'}, 'print_operand')
    def meadow_print_operand(meadow_self_9a4e3bc, meadow_ea_32c6d2e, meadow_n_e8ddb87):
        meadow_op_4a09794 = _name_boundary.attributes(meadow_self_9a4e3bc)['_disassemble'](meadow_ea_32c6d2e)
        meadow_opnds_78b1cd9 = meadow_op_4a09794.op_str.split(', ')
        meadow_n_opnds_918ed09 = len(meadow_opnds_78b1cd9)
        if 0 <= meadow_n_e8ddb87 < meadow_n_opnds_918ed09:
            return meadow_opnds_78b1cd9[meadow_n_e8ddb87]
        else:
            return ''

    @_name_boundary.callable_contract({'self': 'meadow_self_f7b2c0f', 'ea': 'meadow_ea_021fb1f', 'n': 'meadow_n_151cc93'}, 'get_operand_type')
    def meadow_get_operand_type(meadow_self_f7b2c0f, meadow_ea_021fb1f, meadow_n_151cc93):
        from capstone import CS_OP_IMM as meadow_CS_OP_IMM_ce8d9b9, CS_OP_MEM as meadow_CS_OP_MEM_d1cb238, CS_OP_REG as meadow_CS_OP_REG_9fc4ab7, CS_OP_INVALID as meadow_CS_OP_INVALID_2feeac3
        meadow_op_33f1a37 = _name_boundary.attributes(meadow_self_f7b2c0f)['_disassemble'](meadow_ea_021fb1f)
        meadow_opnds_733def3 = meadow_op_33f1a37.operands
        meadow_n_opnds_e7bf892 = len(meadow_opnds_733def3)
        meadow_is_far_1014b27 = False
        if meadow_op_33f1a37.mnemonic in ['ljmp', 'lcall']:
            meadow_n_opnds_e7bf892 = 1
            meadow_is_far_1014b27 = True
        if 0 <= meadow_n_151cc93 < meadow_n_opnds_e7bf892:
            meadow_op_n_5740050 = meadow_opnds_733def3[meadow_n_151cc93]
            if meadow_op_n_5740050.type == meadow_CS_OP_INVALID_2feeac3:
                return -1
            elif meadow_op_n_5740050.type == meadow_CS_OP_REG_9fc4ab7:
                return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_reg']
            elif meadow_op_n_5740050.type == meadow_CS_OP_MEM_d1cb238:
                meadow_op_mem_52e8ef7 = meadow_op_n_5740050.value.mem
                if meadow_op_mem_52e8ef7.base == 0:
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_mem']
                if meadow_op_mem_52e8ef7.base != 0 and meadow_op_mem_52e8ef7.disp == 0:
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_phrase']
                if meadow_op_mem_52e8ef7.base != 0 and meadow_op_mem_52e8ef7.disp != 0:
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_displ']
            elif meadow_op_n_5740050.type == meadow_CS_OP_IMM_ce8d9b9:
                if meadow_is_far_1014b27:
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_far']
                elif _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_bytes'])['is_code'](_name_boundary.attributes(meadow_self_f7b2c0f)['GetFlags'](meadow_op_n_5740050.value.imm)):
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_near']
                else:
                    return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_imm']
        else:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_f7b2c0f.api)['ida_ua'])['o_void']
    meadow_CIC_ITEM = 1
    meadow_CIC_FUNC = 2
    meadow_CIC_SEGM = 3
    meadow_DEFCOLOR = 4294967295

    @_name_boundary.callable_contract({'self': 'meadow_self_45de772', 'ea': 'meadow_ea_f277ac3', 'what': 'meadow_what_cd1f341'}, 'GetColor')
    def meadow_GetColor(meadow_self_45de772, meadow_ea_f277ac3, meadow_what_cd1f341):
        """
        Args:
          ea (int): effective address of thing.
          what (int): one of:
            - idc.CIC_ITEM
            - idc.CIC_FUNC
            - idc.CIC_SEGM

        Returns:
          int: the color in RGB. possibly idc.DEFCOLOR if not set.
        """
        if meadow_what_cd1f341 != _name_boundary.attributes(meadow_idc)['CIC_ITEM']:
            raise NotImplementedError()
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_45de772.api)['ida_nalt'])['is_colored_item'](meadow_ea_f277ac3):
            return _name_boundary.attributes(meadow_idc)['DEFCOLOR']
        meadow_nn_0971152 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_45de772.api)['ida_netnode'])['netnode'](meadow_ea_f277ac3)
        try:
            return _name_boundary.attributes(meadow_nn_0971152)['altval'](tag='A', index=20) - 1
        except KeyError:
            return _name_boundary.attributes(meadow_idc)['DEFCOLOR']

    @_name_boundary.callable_contract({'self': 'meadow_self_6962519', 'ea': 'meadow_ea_3e6ea54'}, 'GetFunctionFlags')
    def meadow_GetFunctionFlags(meadow_self_6962519, meadow_ea_3e6ea54):
        meadow_func_3be4396 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_6962519.api)['ida_funcs'])['get_func'](meadow_ea_3e6ea54)
        return meadow_func_3be4396.flags

    @_name_boundary.callable_contract({'self': 'meadow_self_7f03d13', 'ea': 'meadow_ea_d2619fc', 'attr': 'meadow_attr_d4ad97e'}, 'GetFunctionAttr')
    def meadow_GetFunctionAttr(meadow_self_7f03d13, meadow_ea_d2619fc, meadow_attr_d4ad97e):
        meadow_func_427e1f6 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_7f03d13.api)['ida_funcs'])['get_func'](meadow_ea_d2619fc)
        if meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_START']:
            return _name_boundary.attributes(meadow_func_427e1f6)['startEA']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_END']:
            return _name_boundary.attributes(meadow_func_427e1f6)['endEA']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_FLAGS']:
            return meadow_func_427e1f6.flags
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_FRAME']:
            return _name_boundary.attributes(meadow_func_427e1f6)['frame']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_FRSIZE']:
            return _name_boundary.attributes(meadow_func_427e1f6)['frsize']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_FRREGS']:
            return _name_boundary.attributes(meadow_func_427e1f6)['frregs']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_ARGSIZE']:
            return _name_boundary.attributes(meadow_func_427e1f6)['argsize']
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_FPD']:
            return meadow_func_427e1f6.fpd
        elif meadow_attr_d4ad97e == _name_boundary.attributes(meadow_self_7f03d13)['FUNCATTR_COLOR']:
            return _name_boundary.attributes(meadow_func_427e1f6)['color']
        else:
            raise ValueError('unknown attr: %x' % meadow_attr_d4ad97e)

    @_name_boundary.callable_contract({'self': 'meadow_self_0164aaf', 'ea': 'meadow_ea_9b6a606'}, 'GetFunctionName')
    def meadow_GetFunctionName(meadow_self_0164aaf, meadow_ea_9b6a606):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_0164aaf.api)['ida_funcs'])['get_func_name'](meadow_ea_9b6a606)

    @_name_boundary.callable_contract({'self': 'meadow_self_f00ad7d', 'ea': 'meadow_ea_972e3a6'}, 'find_func_end')
    def meadow_find_func_end(meadow_self_f00ad7d, meadow_ea_972e3a6):
        meadow_func_f68abb6 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_f00ad7d.api)['ida_funcs'])['get_func'](meadow_ea_972e3a6)
        if not meadow_func_f68abb6:
            return _name_boundary.attributes(meadow_self_f00ad7d)['BADADDR']
        else:
            return _name_boundary.attributes(meadow_func_f68abb6)['endEA']

    @_name_boundary.callable_contract({'self': 'meadow_self_d8d3d22', 'name': 'meadow_name_local_8df6c9e'}, 'LocByName')
    def meadow_LocByName(meadow_self_d8d3d22, meadow_name_local_8df6c9e):
        try:
            meadow_key_local_10179bf = ('N' + meadow_name_local_8df6c9e).encode('utf-8')
            meadow_cursor_990bca7 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d8d3d22)['idb'].id0)['find'](meadow_key_local_10179bf)
            return _name_boundary.attributes(meadow_idb)['netnode'].as_uint(meadow_cursor_990bca7.value)
        except KeyError:
            return -1

    @_name_boundary.callable_contract({'self': 'meadow_self_00e930d'}, 'GetInputMD5')
    def meadow_GetInputMD5(meadow_self_00e930d):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_00e930d.api)['ida_nalt'])['retrieve_input_file_md5']()

    @_name_boundary.callable_contract({'self': 'meadow_self_2b97804'}, 'GetInputSHA256')
    def meadow_GetInputSHA256(meadow_self_2b97804):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_2b97804.api)['ida_nalt'])['retrieve_input_file_sha256']()

    @_name_boundary.callable_contract({'self': 'meadow_self_00bb868'}, 'GetInputFile')
    def meadow_GetInputFile(meadow_self_00bb868):
        return _name_boundary.attributes(meadow_os)['path'].basename(_name_boundary.attributes(_name_boundary.attributes(meadow_self_00bb868.api)['ida_nalt'])['get_input_file_path']())

    @_name_boundary.callable_contract({'self': 'meadow_self_d074791', 'ea': 'meadow_ea_c4227c0'}, 'Comment')
    def meadow_Comment(meadow_self_d074791, meadow_ea_c4227c0):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_d074791.api)['ida_bytes'])['get_cmt'](meadow_ea_c4227c0, False)

    @_name_boundary.callable_contract({'self': 'meadow_self_e1cafd0', 'ea': 'meadow_ea_fd601f5'}, 'RptCmt')
    def meadow_RptCmt(meadow_self_e1cafd0, meadow_ea_fd601f5):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_e1cafd0.api)['ida_bytes'])['get_cmt'](meadow_ea_fd601f5, True)

    @_name_boundary.callable_contract({'self': 'meadow_self_4b61135', 'ea': 'meadow_ea_166c7b8', 'repeatable': 'meadow_repeatable_6572692'}, 'GetCommentEx')
    def meadow_GetCommentEx(meadow_self_4b61135, meadow_ea_166c7b8, meadow_repeatable_6572692):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_4b61135.api)['ida_bytes'])['get_cmt'](meadow_ea_166c7b8, meadow_repeatable_6572692)

    @_name_boundary.callable_contract({'self': 'meadow_self_783cb09', 'ea': 'meadow_ea_8750460'}, 'GetType')
    def meadow_GetType(meadow_self_783cb09, meadow_ea_8750460):
        try:
            meadow_f_993d8fd = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](_name_boundary.attributes(meadow_self_783cb09)['idb'], meadow_ea_8750460)
        except Exception as meadow_e_494c3c9:
            meadow_logger.warning('failed to fetch function for GetType: %s', meadow_e_494c3c9)
            return None
        meadow_sig_1d56f6e = _name_boundary.attributes(meadow_f_993d8fd)['get_signature']()
        return _name_boundary.attributes(meadow_sig_1d56f6e)['get_typestr']() if meadow_sig_1d56f6e is not None else None

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_625bdcb'}, 'hasValue')
    def meadow_hasValue(meadow_flags_local_625bdcb):
        return meadow_flags_local_625bdcb & _name_boundary.attributes(meadow_FLAGS)['FF_IVL'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_5d27bc8'}, 'isDefArg0')
    def meadow_isDefArg0(meadow_flags_local_5d27bc8):
        return meadow_flags_local_5d27bc8 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_b298bb1'}, 'isDefArg1')
    def meadow_isDefArg1(meadow_flags_local_b298bb1):
        return meadow_flags_local_b298bb1 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_9fa8e06'}, 'isOff0')
    def meadow_isOff0(meadow_flags_local_9fa8e06):
        return meadow_flags_local_9fa8e06 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0CUST']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_a4b15f0'}, 'isOff1')
    def meadow_isOff1(meadow_flags_local_a4b15f0):
        return meadow_flags_local_a4b15f0 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1CUST']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_6b11f84'}, 'isChar0')
    def meadow_isChar0(meadow_flags_local_6b11f84):
        return meadow_flags_local_6b11f84 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0CHAR']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_97ee7af'}, 'isChar1')
    def meadow_isChar1(meadow_flags_local_97ee7af):
        return meadow_flags_local_97ee7af & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1CHAR']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_165eed0'}, 'isSeg0')
    def meadow_isSeg0(meadow_flags_local_165eed0):
        return meadow_flags_local_165eed0 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0SEG']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_4180150'}, 'isSeg1')
    def meadow_isSeg1(meadow_flags_local_4180150):
        return meadow_flags_local_4180150 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1SEG']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_c82dc28'}, 'isEnum0')
    def meadow_isEnum0(meadow_flags_local_c82dc28):
        return meadow_flags_local_c82dc28 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0ENUM']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_eed4f2f'}, 'isEnum1')
    def meadow_isEnum1(meadow_flags_local_eed4f2f):
        return meadow_flags_local_eed4f2f & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1ENUM']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_53f10b1'}, 'isStroff0')
    def meadow_isStroff0(meadow_flags_local_53f10b1):
        return meadow_flags_local_53f10b1 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0STRO']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_58552db'}, 'isStroff1')
    def meadow_isStroff1(meadow_flags_local_58552db):
        return meadow_flags_local_58552db & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1STRO']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_50c10b8'}, 'isStkvar0')
    def meadow_isStkvar0(meadow_flags_local_50c10b8):
        return meadow_flags_local_50c10b8 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0STK']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_f87bb67'}, 'isStkvar1')
    def meadow_isStkvar1(meadow_flags_local_f87bb67):
        return meadow_flags_local_f87bb67 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1STK']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_45c7c66'}, 'isFloat0')
    def meadow_isFloat0(meadow_flags_local_45c7c66):
        return meadow_flags_local_45c7c66 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0FLT']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_9a6cd0f'}, 'isFloat1')
    def meadow_isFloat1(meadow_flags_local_9a6cd0f):
        return meadow_flags_local_9a6cd0f & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1FLT']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_f46b126'}, 'isCustFmt0')
    def meadow_isCustFmt0(meadow_flags_local_f46b126):
        return meadow_flags_local_f46b126 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_0CUST']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_e465101'}, 'isCustFmt1')
    def meadow_isCustFmt1(meadow_flags_local_e465101):
        return meadow_flags_local_e465101 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_1CUST']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_8c3b136'}, 'isNum0')
    def meadow_isNum0(meadow_flags_local_8c3b136):
        meadow_t_698bffe = meadow_flags_local_8c3b136 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE']
        return meadow_t_698bffe == _name_boundary.attributes(meadow_FLAGS)['FF_0NUMB'] or meadow_t_698bffe == _name_boundary.attributes(meadow_FLAGS)['FF_0NUMO'] or meadow_t_698bffe == _name_boundary.attributes(meadow_FLAGS)['FF_0NUMD'] or (meadow_t_698bffe == _name_boundary.attributes(meadow_FLAGS)['FF_0NUMH'])

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_25402a4'}, 'isNum1')
    def meadow_isNum1(meadow_flags_local_25402a4):
        meadow_t_8252bbd = meadow_flags_local_25402a4 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE']
        return meadow_t_8252bbd == _name_boundary.attributes(meadow_FLAGS)['FF_1NUMB'] or meadow_t_8252bbd == _name_boundary.attributes(meadow_FLAGS)['FF_1NUMO'] or meadow_t_8252bbd == _name_boundary.attributes(meadow_FLAGS)['FF_1NUMD'] or (meadow_t_8252bbd == _name_boundary.attributes(meadow_FLAGS)['FF_1NUMH'])

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_7c44aa4'}, 'get_optype_flags0')
    def meadow_get_optype_flags0(meadow_flags_local_7c44aa4):
        return meadow_flags_local_7c44aa4 & _name_boundary.attributes(meadow_FLAGS)['MS_0TYPE']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_36a7ee2'}, 'get_optype_flags1')
    def meadow_get_optype_flags1(meadow_flags_local_36a7ee2):
        return meadow_flags_local_36a7ee2 & _name_boundary.attributes(meadow_FLAGS)['MS_1TYPE']

    @_name_boundary.callable_contract({'self': 'meadow_self_5cb9f67', 'ea': 'meadow_ea_4370303', 'num': 'meadow_num_aa09f12'}, 'LineA')
    def meadow_LineA(meadow_self_5cb9f67, meadow_ea_4370303, meadow_num_aa09f12):
        meadow_nn_e85bd62 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_5cb9f67.api)['ida_netnode'])['netnode'](meadow_ea_4370303)
        try:
            return _name_boundary.attributes(meadow_nn_e85bd62)['supstr'](tag='S', index=1000 + meadow_num_aa09f12)
        except KeyError:
            return ''

    @_name_boundary.callable_contract({'self': 'meadow_self_64b0a78', 'ea': 'meadow_ea_7890a25', 'num': 'meadow_num_999f63b'}, 'LineB')
    def meadow_LineB(meadow_self_64b0a78, meadow_ea_7890a25, meadow_num_999f63b):
        meadow_nn_d7129e2 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_64b0a78.api)['ida_netnode'])['netnode'](meadow_ea_7890a25)
        try:
            return _name_boundary.attributes(meadow_nn_d7129e2)['supstr'](tag='S', index=2000 + meadow_num_999f63b)
        except KeyError:
            return ''

@_name_boundary.class_contract('ida_bytes', {'get_cmt': 'meadow_get_cmt', 'get_flags': 'meadow_get_flags', 'is_func': 'meadow_is_func', 'has_immd': 'meadow_has_immd', 'is_code': 'meadow_is_code', 'is_data': 'meadow_is_data', 'is_tail': 'meadow_is_tail', 'is_not_tail': 'meadow_is_not_tail', 'is_unknown': 'meadow_is_unknown', 'is_head': 'meadow_is_head', 'is_flow': 'meadow_is_flow', 'is_var': 'meadow_is_var', 'has_extra_cmts': 'meadow_has_extra_cmts', 'has_cmt': 'meadow_has_cmt', 'has_ref': 'meadow_has_ref', 'has_name': 'meadow_has_name', 'has_dummy_name': 'meadow_has_dummy_name', 'has_auto_name': 'meadow_has_auto_name', 'has_any_name': 'meadow_has_any_name', 'has_user_name': 'meadow_has_user_name', 'is_invsign': 'meadow_is_invsign', 'is_bnot': 'meadow_is_bnot', 'has_value': 'meadow_has_value', 'is_byte': 'meadow_is_byte', 'is_word': 'meadow_is_word', 'is_dword': 'meadow_is_dword', 'is_qword': 'meadow_is_qword', 'is_oword': 'meadow_is_oword', 'is_yword': 'meadow_is_yword', 'is_tbyte': 'meadow_is_tbyte', 'is_float': 'meadow_is_float', 'is_double': 'meadow_is_double', 'is_pack_real': 'meadow_is_pack_real', 'is_strlit': 'meadow_is_strlit', 'is_struct': 'meadow_is_struct', 'is_align': 'meadow_is_align', 'is_custom': 'meadow_is_custom', 'get_bytes': 'meadow_get_bytes', 'next_that': 'meadow_next_that', 'next_not_tail': 'meadow_next_not_tail', 'next_inited': 'meadow_next_inited', 'get_item_end': 'meadow_get_item_end', 'get_byte': 'meadow_get_byte', 'get_word': 'meadow_get_word', 'get_dword': 'meadow_get_dword', 'get_qword': 'meadow_get_qword', 'idb': 'meadow_idb', 'get_long': 'meadow_get_long'})
class meadow_ida_bytes:

    @meadow_wrap_module('idaapi')
    @_name_boundary.callable_contract({'self': 'meadow_self_83026ae', 'db': 'meadow_db_869cb0d', 'api': 'meadow_api_local_844921c'}, '__init__')
    def __init__(meadow_self_83026ae, meadow_db_869cb0d, meadow_api_local_844921c):
        _name_boundary.attributes(meadow_self_83026ae)['idb'] = meadow_db_869cb0d
        meadow_self_83026ae.api = meadow_api_local_844921c
        _name_boundary.attributes(meadow_self_83026ae)['get_long'] = _name_boundary.attributes(meadow_self_83026ae)['get_dword']

    @_name_boundary.callable_contract({'self': 'meadow_self_a015858', 'ea': 'meadow_ea_7b71b39', 'repeatable': 'meadow_repeatable_668329a'}, 'get_cmt')
    def meadow_get_cmt(meadow_self_a015858, meadow_ea_7b71b39, meadow_repeatable_668329a):
        meadow_flags_local_b50b8ff = _name_boundary.attributes(_name_boundary.attributes(meadow_self_a015858.api)['idc'])['GetFlags'](meadow_ea_7b71b39)
        if not _name_boundary.attributes(meadow_self_a015858)['has_cmt'](meadow_flags_local_b50b8ff):
            return ''
        try:
            meadow_nn_cdcc9fe = _name_boundary.attributes(_name_boundary.attributes(meadow_self_a015858.api)['ida_netnode'])['netnode'](meadow_ea_7b71b39)
            if meadow_repeatable_668329a:
                return _name_boundary.attributes(meadow_nn_cdcc9fe)['supstr'](tag='S', index=1)
            else:
                return _name_boundary.attributes(meadow_nn_cdcc9fe)['supstr'](tag='S', index=0)
        except KeyError:
            return ''

    @_name_boundary.callable_contract({'self': 'meadow_self_51ec9fd', 'ea': 'meadow_ea_5fdd9dc'}, 'get_flags')
    def meadow_get_flags(meadow_self_51ec9fd, meadow_ea_5fdd9dc):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_51ec9fd.api)['idc'])['GetFlags'](meadow_ea_5fdd9dc)

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_c62ccc5'}, 'is_func')
    def meadow_is_func(meadow_flags_local_c62ccc5):
        return meadow_flags_local_c62ccc5 & _name_boundary.attributes(meadow_FLAGS)['MS_CODE'] == _name_boundary.attributes(meadow_FLAGS)['FF_FUNC']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_97d8f94'}, 'has_immd')
    def meadow_has_immd(meadow_flags_local_97d8f94):
        return meadow_flags_local_97d8f94 & _name_boundary.attributes(meadow_FLAGS)['MS_CODE'] == _name_boundary.attributes(meadow_FLAGS)['FF_IMMD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_6e4813a'}, 'is_code')
    def meadow_is_code(meadow_flags_local_6e4813a):
        return meadow_flags_local_6e4813a & _name_boundary.attributes(meadow_FLAGS)['MS_CLS'] == _name_boundary.attributes(meadow_FLAGS)['FF_CODE']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_097581e'}, 'is_data')
    def meadow_is_data(meadow_flags_local_097581e):
        return meadow_flags_local_097581e & _name_boundary.attributes(meadow_FLAGS)['MS_CLS'] == _name_boundary.attributes(meadow_FLAGS)['FF_DATA']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_4e98c7a'}, 'is_tail')
    def meadow_is_tail(meadow_flags_local_4e98c7a):
        return meadow_flags_local_4e98c7a & _name_boundary.attributes(meadow_FLAGS)['MS_CLS'] == _name_boundary.attributes(meadow_FLAGS)['FF_TAIL']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_c8595bf'}, 'is_not_tail')
    def meadow_is_not_tail(meadow_flags_local_c8595bf):
        return not _name_boundary.attributes(meadow_ida_bytes)['is_tail'](meadow_flags_local_c8595bf)

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_76aaa43'}, 'is_unknown')
    def meadow_is_unknown(meadow_flags_local_76aaa43):
        return meadow_flags_local_76aaa43 & _name_boundary.attributes(meadow_FLAGS)['MS_CLS'] == _name_boundary.attributes(meadow_FLAGS)['FF_UNK']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_4bf07ce'}, 'is_head')
    def meadow_is_head(meadow_flags_local_4bf07ce):
        return _name_boundary.attributes(meadow_ida_bytes)['is_code'](meadow_flags_local_4bf07ce) or _name_boundary.attributes(meadow_ida_bytes)['is_data'](meadow_flags_local_4bf07ce)

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_1c204fd'}, 'is_flow')
    def meadow_is_flow(meadow_flags_local_1c204fd):
        return meadow_flags_local_1c204fd & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_FLOW'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_3f047da'}, 'is_var')
    def meadow_is_var(meadow_flags_local_3f047da):
        return meadow_flags_local_3f047da & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_VAR'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_9049eef'}, 'has_extra_cmts')
    def meadow_has_extra_cmts(meadow_flags_local_9049eef):
        return meadow_flags_local_9049eef & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_LINE'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_fd308d6'}, 'has_cmt')
    def meadow_has_cmt(meadow_flags_local_fd308d6):
        return meadow_flags_local_fd308d6 & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_COMM'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_e5cf063'}, 'has_ref')
    def meadow_has_ref(meadow_flags_local_e5cf063):
        return meadow_flags_local_e5cf063 & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_REF'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_8fcafdd'}, 'has_name')
    def meadow_has_name(meadow_flags_local_8fcafdd):
        return meadow_flags_local_8fcafdd & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_NAME'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_842be5e'}, 'has_dummy_name')
    def meadow_has_dummy_name(meadow_flags_local_842be5e):
        return meadow_flags_local_842be5e & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_LABL'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_f070bc5'}, 'has_auto_name')
    def meadow_has_auto_name(meadow_flags_local_f070bc5):
        raise NotImplementedError()

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_7214887'}, 'has_any_name')
    def meadow_has_any_name(meadow_flags_local_7214887):
        raise NotImplementedError()

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_e7f5709'}, 'has_user_name')
    def meadow_has_user_name(meadow_flags_local_e7f5709):
        raise NotImplementedError()

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_9c0b01e'}, 'is_invsign')
    def meadow_is_invsign(meadow_flags_local_9c0b01e):
        return meadow_flags_local_9c0b01e & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_SIGN'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_167698f'}, 'is_bnot')
    def meadow_is_bnot(meadow_flags_local_167698f):
        return meadow_flags_local_167698f & _name_boundary.attributes(meadow_FLAGS)['MS_COMM'] & _name_boundary.attributes(meadow_FLAGS)['FF_BNOT'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_af1b6f2'}, 'has_value')
    def meadow_has_value(meadow_flags_local_af1b6f2):
        return meadow_flags_local_af1b6f2 & _name_boundary.attributes(meadow_FLAGS)['FF_IVL'] > 0

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_cbb6236'}, 'is_byte')
    def meadow_is_byte(meadow_flags_local_cbb6236):
        return meadow_flags_local_cbb6236 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_BYTE']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_bc2b72e'}, 'is_word')
    def meadow_is_word(meadow_flags_local_bc2b72e):
        return meadow_flags_local_bc2b72e & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_WORD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_3c411ce'}, 'is_dword')
    def meadow_is_dword(meadow_flags_local_3c411ce):
        return meadow_flags_local_3c411ce & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_DWRD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_99f2ef8'}, 'is_qword')
    def meadow_is_qword(meadow_flags_local_99f2ef8):
        return meadow_flags_local_99f2ef8 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_QWRD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_d6111a4'}, 'is_oword')
    def meadow_is_oword(meadow_flags_local_d6111a4):
        return meadow_flags_local_d6111a4 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_OWRD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_eb339c6'}, 'is_yword')
    def meadow_is_yword(meadow_flags_local_eb339c6):
        return meadow_flags_local_eb339c6 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_YWRD']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_3b78a82'}, 'is_tbyte')
    def meadow_is_tbyte(meadow_flags_local_3b78a82):
        return meadow_flags_local_3b78a82 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_TBYT']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_4318f5f'}, 'is_float')
    def meadow_is_float(meadow_flags_local_4318f5f):
        return meadow_flags_local_4318f5f & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_FLOAT']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_f72284e'}, 'is_double')
    def meadow_is_double(meadow_flags_local_f72284e):
        return meadow_flags_local_f72284e & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_DOUBLE']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_6edeb4f'}, 'is_pack_real')
    def meadow_is_pack_real(meadow_flags_local_6edeb4f):
        return meadow_flags_local_6edeb4f & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_PACKREAL']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_93cb223'}, 'is_strlit')
    def meadow_is_strlit(meadow_flags_local_93cb223):
        return meadow_flags_local_93cb223 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_ASCI']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_620aa3d'}, 'is_struct')
    def meadow_is_struct(meadow_flags_local_620aa3d):
        return meadow_flags_local_620aa3d & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_STRU']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_3b17bd4'}, 'is_align')
    def meadow_is_align(meadow_flags_local_3b17bd4):
        return meadow_flags_local_3b17bd4 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_ALIGN']

    @staticmethod
    @_name_boundary.callable_contract({'flags': 'meadow_flags_local_90dd5c7'}, 'is_custom')
    def meadow_is_custom(meadow_flags_local_90dd5c7):
        return meadow_flags_local_90dd5c7 & _name_boundary.attributes(meadow_FLAGS)['DT_TYPE'] == _name_boundary.attributes(meadow_FLAGS)['FF_CUSTOM']

    @_name_boundary.callable_contract({'self': 'meadow_self_ae71fad', 'ea': 'meadow_ea_3ac8635', 'count': 'meadow_count_local_26825cf'}, 'get_bytes')
    def meadow_get_bytes(meadow_self_ae71fad, meadow_ea_3ac8635, meadow_count_local_26825cf):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_ae71fad.api)['idc'])['GetManyBytes'](meadow_ea_3ac8635, meadow_count_local_26825cf)

    @_name_boundary.callable_contract({'self': 'meadow_self_ac0964e', 'ea': 'meadow_ea_949e028', 'maxea': 'meadow_maxea_c13689f', 'testf': 'meadow_testf_b317138'}, 'next_that')
    def meadow_next_that(meadow_self_ac0964e, meadow_ea_949e028, meadow_maxea_c13689f, meadow_testf_b317138):
        for meadow_i_d654b3e in range(meadow_ea_949e028 + 1, meadow_maxea_c13689f):
            meadow_flags_local_2bd4ddb = _name_boundary.attributes(meadow_self_ac0964e)['get_flags'](meadow_i_d654b3e)
            if meadow_testf_b317138(meadow_flags_local_2bd4ddb):
                return meadow_i_d654b3e
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_ac0964e.api)['idc'])['BADADDR']

    @_name_boundary.callable_contract({'self': 'meadow_self_498acb2', 'ea': 'meadow_ea_674d315'}, 'next_not_tail')
    def meadow_next_not_tail(meadow_self_498acb2, meadow_ea_674d315):
        while True:
            meadow_ea_674d315 += 1
            meadow_flags_local_af382ac = _name_boundary.attributes(meadow_self_498acb2)['get_flags'](meadow_ea_674d315)
            if not _name_boundary.attributes(meadow_self_498acb2)['is_tail'](meadow_flags_local_af382ac):
                break
        return meadow_ea_674d315

    @_name_boundary.callable_contract({'self': 'meadow_self_9e97cc5', 'ea': 'meadow_ea_83edc72', 'maxea': 'meadow_maxea_aa2c7c9'}, 'next_inited')
    def meadow_next_inited(meadow_self_9e97cc5, meadow_ea_83edc72, meadow_maxea_aa2c7c9):
        return _name_boundary.attributes(meadow_self_9e97cc5)['next_that'](meadow_ea_83edc72, meadow_maxea_aa2c7c9, _name_boundary.callable_contract({'flags': 'meadow_flags_local_54c1593'}, '<lambda>')(lambda meadow_flags_local_54c1593: _name_boundary.attributes(meadow_ida_bytes)['has_value'](meadow_flags_local_54c1593)))

    @_name_boundary.callable_contract({'self': 'meadow_self_d04668a', 'ea': 'meadow_ea_a550638'}, 'get_item_end')
    def meadow_get_item_end(meadow_self_d04668a, meadow_ea_a550638):
        meadow_ea_a550638 += 1
        meadow_flags_local_80cd011 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d04668a.api)['idc'])['GetFlags'](meadow_ea_a550638)
        while meadow_flags_local_80cd011 is not None and (not _name_boundary.attributes(_name_boundary.attributes(meadow_self_d04668a.api)['ida_bytes'])['is_head'](meadow_flags_local_80cd011)) and _name_boundary.attributes(_name_boundary.attributes(meadow_self_d04668a.api)['idc'])['SegEnd'](meadow_ea_a550638):
            meadow_ea_a550638 += 1
            meadow_flags_local_80cd011 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d04668a.api)['idc'])['GetFlags'](meadow_ea_a550638)
        return meadow_ea_a550638

    @_name_boundary.callable_contract({'self': 'meadow_self_38697b1', 'ea': 'meadow_ea_a47c7e7'}, 'get_byte')
    def meadow_get_byte(meadow_self_38697b1, meadow_ea_a47c7e7):
        return ord(_name_boundary.attributes(meadow_self_38697b1)['get_bytes'](meadow_ea_a47c7e7, 1))

    @_name_boundary.callable_contract({'self': 'meadow_self_118c100', 'ea': 'meadow_ea_e596e3b'}, 'get_word')
    def meadow_get_word(meadow_self_118c100, meadow_ea_e596e3b):
        if _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_self_118c100.api)['idaapi'])['get_inf_structure']())['is_be']:
            meadow_fmt_local_03bf10b = '>H'
        else:
            meadow_fmt_local_03bf10b = '<H'
        return _name_boundary.attributes(meadow_struct)['unpack'](meadow_fmt_local_03bf10b, _name_boundary.attributes(meadow_self_118c100)['get_bytes'](meadow_ea_e596e3b, 2))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_b3956b0', 'ea': 'meadow_ea_d395617'}, 'get_dword')
    def meadow_get_dword(meadow_self_b3956b0, meadow_ea_d395617):
        if _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_self_b3956b0.api)['idaapi'])['get_inf_structure']())['is_be']:
            meadow_fmt_local_e1ad2b4 = '>I'
        else:
            meadow_fmt_local_e1ad2b4 = '<I'
        return _name_boundary.attributes(meadow_struct)['unpack'](meadow_fmt_local_e1ad2b4, _name_boundary.attributes(meadow_self_b3956b0)['get_bytes'](meadow_ea_d395617, 4))[0]

    @_name_boundary.callable_contract({'self': 'meadow_self_c220ee4', 'ea': 'meadow_ea_2de3b20'}, 'get_qword')
    def meadow_get_qword(meadow_self_c220ee4, meadow_ea_2de3b20):
        if _name_boundary.attributes(_name_boundary.attributes(_name_boundary.attributes(meadow_self_c220ee4.api)['idaapi'])['get_inf_structure']())['is_be']:
            meadow_fmt_local_8d9962c = '>Q'
        else:
            meadow_fmt_local_8d9962c = '<Q'
        return _name_boundary.attributes(meadow_struct)['unpack'](meadow_fmt_local_8d9962c, _name_boundary.attributes(meadow_self_c220ee4)['get_bytes'](meadow_ea_2de3b20, 8))[0]

@_name_boundary.class_contract('ida_nalt', {'get_aflags': 'meadow_get_aflags', 'is_hidden_item': 'meadow_is_hidden_item', 'is_hidden_border': 'meadow_is_hidden_border', 'uses_modsp': 'meadow_uses_modsp', 'is_zstroff': 'meadow_is_zstroff', 'is__bnot0': 'meadow_is__bnot0', 'is__bnot1': 'meadow_is__bnot1', 'is_libitem': 'meadow_is_libitem', 'has_ti': 'meadow_has_ti', 'has_ti0': 'meadow_has_ti0', 'has_ti1': 'meadow_has_ti1', 'has_lname': 'meadow_has_lname', 'is_tilcmt': 'meadow_is_tilcmt', 'is_usersp': 'meadow_is_usersp', 'is_lzero0': 'meadow_is_lzero0', 'is_lzero1': 'meadow_is_lzero1', 'is_colored_item': 'meadow_is_colored_item', 'is_terse_struc': 'meadow_is_terse_struc', 'is__invsign0': 'meadow_is__invsign0', 'is__invsign1': 'meadow_is__invsign1', 'is_noret': 'meadow_is_noret', 'is_fixed_spd': 'meadow_is_fixed_spd', 'is_align_flow': 'meadow_is_align_flow', 'is_userti': 'meadow_is_userti', 'is_retfp': 'meadow_is_retfp', 'is_notcode': 'meadow_is_notcode', 'get_import_module_qty': 'meadow_get_import_module_qty', 'get_import_module_name': 'meadow_get_import_module_name', 'enum_import_names': 'meadow_enum_import_names', 'get_imagebase': 'meadow_get_imagebase', 'retrieve_input_file_sha256': 'meadow_retrieve_input_file_sha256', 'retrieve_input_file_md5': 'meadow_retrieve_input_file_md5', 'get_input_file_path': 'meadow_get_input_file_path', 'idb': 'meadow_idb'})
class meadow_ida_nalt:

    @meadow_wrap_module('idaapi')
    @_name_boundary.callable_contract({'self': 'meadow_self_2d99355', 'db': 'meadow_db_ff2c057', 'api': 'meadow_api_local_44bfcfc'}, '__init__')
    def __init__(meadow_self_2d99355, meadow_db_ff2c057, meadow_api_local_44bfcfc):
        _name_boundary.attributes(meadow_self_2d99355)['idb'] = meadow_db_ff2c057
        meadow_self_2d99355.api = meadow_api_local_44bfcfc

    @_name_boundary.callable_contract({'self': 'meadow_self_a10ad50', 'ea': 'meadow_ea_694ff72'}, 'get_aflags')
    def meadow_get_aflags(meadow_self_a10ad50, meadow_ea_694ff72):
        meadow_nn_eed1cd9 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_a10ad50.api)['ida_netnode'])['netnode'](meadow_ea_694ff72)
        try:
            return _name_boundary.attributes(meadow_nn_eed1cd9)['altval'](tag='A', index=8)
        except KeyError:
            return 0

    @_name_boundary.callable_contract({'self': 'meadow_self_1fab2e6', 'ea': 'meadow_ea_8fd896d'}, 'is_hidden_item')
    def meadow_is_hidden_item(meadow_self_1fab2e6, meadow_ea_8fd896d):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_1fab2e6)['get_aflags'](meadow_ea_8fd896d), _name_boundary.attributes(meadow_AFLAGS)['AFL_HIDDEN'])

    @_name_boundary.callable_contract({'self': 'meadow_self_49145bd', 'ea': 'meadow_ea_6b68ea5'}, 'is_hidden_border')
    def meadow_is_hidden_border(meadow_self_49145bd, meadow_ea_6b68ea5):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_49145bd)['get_aflags'](meadow_ea_6b68ea5), _name_boundary.attributes(meadow_AFLAGS)['AFL_NOBRD'])

    @_name_boundary.callable_contract({'self': 'meadow_self_12291ed', 'ea': 'meadow_ea_8814cd7'}, 'uses_modsp')
    def meadow_uses_modsp(meadow_self_12291ed, meadow_ea_8814cd7):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_12291ed)['get_aflags'](meadow_ea_8814cd7), _name_boundary.attributes(meadow_AFLAGS)['AFL_USEMODSP'])

    @_name_boundary.callable_contract({'self': 'meadow_self_41ffeb6', 'ea': 'meadow_ea_eb6e455'}, 'is_zstroff')
    def meadow_is_zstroff(meadow_self_41ffeb6, meadow_ea_eb6e455):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_41ffeb6)['get_aflags'](meadow_ea_eb6e455), _name_boundary.attributes(meadow_AFLAGS)['AFL_ZSTROFF'])

    @_name_boundary.callable_contract({'self': 'meadow_self_a3ddb76', 'ea': 'meadow_ea_5baccfd'}, 'is__bnot0')
    def meadow_is__bnot0(meadow_self_a3ddb76, meadow_ea_5baccfd):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_a3ddb76)['get_aflags'](meadow_ea_5baccfd), _name_boundary.attributes(meadow_AFLAGS)['AFL_BNOT0'])

    @_name_boundary.callable_contract({'self': 'meadow_self_238de47', 'ea': 'meadow_ea_a0bd935'}, 'is__bnot1')
    def meadow_is__bnot1(meadow_self_238de47, meadow_ea_a0bd935):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_238de47)['get_aflags'](meadow_ea_a0bd935), _name_boundary.attributes(meadow_AFLAGS)['AFL_BNOT1'])

    @_name_boundary.callable_contract({'self': 'meadow_self_cbb3e1e', 'ea': 'meadow_ea_6ce3205'}, 'is_libitem')
    def meadow_is_libitem(meadow_self_cbb3e1e, meadow_ea_6ce3205):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_cbb3e1e)['get_aflags'](meadow_ea_6ce3205), _name_boundary.attributes(meadow_AFLAGS)['AFL_LIB'])

    @_name_boundary.callable_contract({'self': 'meadow_self_33c6c5c', 'ea': 'meadow_ea_dbcbb14'}, 'has_ti')
    def meadow_has_ti(meadow_self_33c6c5c, meadow_ea_dbcbb14):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_33c6c5c)['get_aflags'](meadow_ea_dbcbb14), _name_boundary.attributes(meadow_AFLAGS)['AFL_TI'])

    @_name_boundary.callable_contract({'self': 'meadow_self_506574a', 'ea': 'meadow_ea_d1dd093'}, 'has_ti0')
    def meadow_has_ti0(meadow_self_506574a, meadow_ea_d1dd093):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_506574a)['get_aflags'](meadow_ea_d1dd093), _name_boundary.attributes(meadow_AFLAGS)['AFL_TI0'])

    @_name_boundary.callable_contract({'self': 'meadow_self_fa78a94', 'ea': 'meadow_ea_d907763'}, 'has_ti1')
    def meadow_has_ti1(meadow_self_fa78a94, meadow_ea_d907763):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_fa78a94)['get_aflags'](meadow_ea_d907763), _name_boundary.attributes(meadow_AFLAGS)['AFL_TI1'])

    @_name_boundary.callable_contract({'self': 'meadow_self_2a3dd01', 'ea': 'meadow_ea_f6a203d'}, 'has_lname')
    def meadow_has_lname(meadow_self_2a3dd01, meadow_ea_f6a203d):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_2a3dd01)['get_aflags'](meadow_ea_f6a203d), _name_boundary.attributes(meadow_AFLAGS)['AFL_LNAME'])

    @_name_boundary.callable_contract({'self': 'meadow_self_d097520', 'ea': 'meadow_ea_a281c61'}, 'is_tilcmt')
    def meadow_is_tilcmt(meadow_self_d097520, meadow_ea_a281c61):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_d097520)['get_aflags'](meadow_ea_a281c61), _name_boundary.attributes(meadow_AFLAGS)['AFL_TILCMT'])

    @_name_boundary.callable_contract({'self': 'meadow_self_941ec90', 'ea': 'meadow_ea_b34b73e'}, 'is_usersp')
    def meadow_is_usersp(meadow_self_941ec90, meadow_ea_b34b73e):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_941ec90)['get_aflags'](meadow_ea_b34b73e), _name_boundary.attributes(meadow_AFLAGS)['AFL_USERSP'])

    @_name_boundary.callable_contract({'self': 'meadow_self_0d8084b', 'ea': 'meadow_ea_793beae'}, 'is_lzero0')
    def meadow_is_lzero0(meadow_self_0d8084b, meadow_ea_793beae):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_0d8084b)['get_aflags'](meadow_ea_793beae), _name_boundary.attributes(meadow_AFLAGS)['AFL_LZERO0'])

    @_name_boundary.callable_contract({'self': 'meadow_self_754a239', 'ea': 'meadow_ea_5f84ce4'}, 'is_lzero1')
    def meadow_is_lzero1(meadow_self_754a239, meadow_ea_5f84ce4):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_754a239)['get_aflags'](meadow_ea_5f84ce4), _name_boundary.attributes(meadow_AFLAGS)['AFL_LZERO1'])

    @_name_boundary.callable_contract({'self': 'meadow_self_b23e1ee', 'ea': 'meadow_ea_da6af0f'}, 'is_colored_item')
    def meadow_is_colored_item(meadow_self_b23e1ee, meadow_ea_da6af0f):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_b23e1ee)['get_aflags'](meadow_ea_da6af0f), _name_boundary.attributes(meadow_AFLAGS)['AFL_COLORED'])

    @_name_boundary.callable_contract({'self': 'meadow_self_02326f1', 'ea': 'meadow_ea_64dfd61'}, 'is_terse_struc')
    def meadow_is_terse_struc(meadow_self_02326f1, meadow_ea_64dfd61):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_02326f1)['get_aflags'](meadow_ea_64dfd61), _name_boundary.attributes(meadow_AFLAGS)['AFL_TERSESTR'])

    @_name_boundary.callable_contract({'self': 'meadow_self_40edd88', 'ea': 'meadow_ea_3d8a47d'}, 'is__invsign0')
    def meadow_is__invsign0(meadow_self_40edd88, meadow_ea_3d8a47d):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_40edd88)['get_aflags'](meadow_ea_3d8a47d), _name_boundary.attributes(meadow_AFLAGS)['AFL_SIGN0'])

    @_name_boundary.callable_contract({'self': 'meadow_self_961ace9', 'ea': 'meadow_ea_64d739b'}, 'is__invsign1')
    def meadow_is__invsign1(meadow_self_961ace9, meadow_ea_64d739b):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_961ace9)['get_aflags'](meadow_ea_64d739b), _name_boundary.attributes(meadow_AFLAGS)['AFL_SIGN1'])

    @_name_boundary.callable_contract({'self': 'meadow_self_57b1f53', 'ea': 'meadow_ea_27eca11'}, 'is_noret')
    def meadow_is_noret(meadow_self_57b1f53, meadow_ea_27eca11):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_57b1f53)['get_aflags'](meadow_ea_27eca11), _name_boundary.attributes(meadow_AFLAGS)['AFL_NORET'])

    @_name_boundary.callable_contract({'self': 'meadow_self_ee3b916', 'ea': 'meadow_ea_8a56160'}, 'is_fixed_spd')
    def meadow_is_fixed_spd(meadow_self_ee3b916, meadow_ea_8a56160):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_ee3b916)['get_aflags'](meadow_ea_8a56160), _name_boundary.attributes(meadow_AFLAGS)['AFL_FIXEDSPD'])

    @_name_boundary.callable_contract({'self': 'meadow_self_a0e30f3', 'ea': 'meadow_ea_b73d7b3'}, 'is_align_flow')
    def meadow_is_align_flow(meadow_self_a0e30f3, meadow_ea_b73d7b3):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_a0e30f3)['get_aflags'](meadow_ea_b73d7b3), _name_boundary.attributes(meadow_AFLAGS)['AFL_ALIGNFLOW'])

    @_name_boundary.callable_contract({'self': 'meadow_self_1a9b508', 'ea': 'meadow_ea_0da3108'}, 'is_userti')
    def meadow_is_userti(meadow_self_1a9b508, meadow_ea_0da3108):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_1a9b508)['get_aflags'](meadow_ea_0da3108), _name_boundary.attributes(meadow_AFLAGS)['AFL_USERTI'])

    @_name_boundary.callable_contract({'self': 'meadow_self_91984dc', 'ea': 'meadow_ea_04ceccc'}, 'is_retfp')
    def meadow_is_retfp(meadow_self_91984dc, meadow_ea_04ceccc):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_91984dc)['get_aflags'](meadow_ea_04ceccc), _name_boundary.attributes(meadow_AFLAGS)['AFL_RETFP'])

    @_name_boundary.callable_contract({'self': 'meadow_self_428a254', 'ea': 'meadow_ea_c258c34'}, 'is_notcode')
    def meadow_is_notcode(meadow_self_428a254, meadow_ea_c258c34):
        return meadow_is_flag_set(_name_boundary.attributes(meadow_self_428a254)['get_aflags'](meadow_ea_c258c34), _name_boundary.attributes(meadow_AFLAGS)['AFL_NOTCODE'])

    @_name_boundary.callable_contract({'self': 'meadow_self_b59de78'}, 'get_import_module_qty')
    def meadow_get_import_module_qty(meadow_self_b59de78):
        return max(_name_boundary.attributes(meadow_idb)['analysis'].Imports(_name_boundary.attributes(meadow_self_b59de78)['idb']).lib_names.keys())

    @_name_boundary.callable_contract({'self': 'meadow_self_6d5cb0d', 'mod_index': 'meadow_mod_index_aabf5d9'}, 'get_import_module_name')
    def meadow_get_import_module_name(meadow_self_6d5cb0d, meadow_mod_index_aabf5d9):
        return _name_boundary.attributes(meadow_idb)['analysis'].Imports(_name_boundary.attributes(meadow_self_6d5cb0d)['idb']).lib_names[meadow_mod_index_aabf5d9]

    @_name_boundary.callable_contract({'self': 'meadow_self_f87a226', 'mod_index': 'meadow_mod_index_ce57c93', 'py_cb': 'meadow_py_cb_de8c315'}, 'enum_import_names')
    def meadow_enum_import_names(meadow_self_f87a226, meadow_mod_index_ce57c93, meadow_py_cb_de8c315):
        meadow_imps_ed4ed7f = _name_boundary.attributes(meadow_idb)['analysis'].Imports(_name_boundary.attributes(meadow_self_f87a226)['idb'])
        meadow_nnref_77b3a97 = meadow_imps_ed4ed7f.lib_netnodes[meadow_mod_index_ce57c93]
        meadow_nn_5183c53 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['netnode'])['Netnode'](_name_boundary.attributes(meadow_self_f87a226)['idb'], meadow_nnref_77b3a97)
        for meadow_funcaddr_8aa5663 in _name_boundary.attributes(meadow_nn_5183c53)['sups']():
            meadow_funcname_2ccc206 = _name_boundary.attributes(meadow_nn_5183c53)['supstr'](meadow_funcaddr_8aa5663)
            if not meadow_py_cb_de8c315(meadow_funcaddr_8aa5663, meadow_funcname_2ccc206, None):
                return

    @_name_boundary.callable_contract({'self': 'meadow_self_7a89205'}, 'get_imagebase')
    def meadow_get_imagebase(meadow_self_7a89205):
        try:
            return _name_boundary.attributes(meadow_idb)['analysis'].Root(_name_boundary.attributes(meadow_self_7a89205)['idb']).imagebase
        except KeyError:
            return 0

    @_name_boundary.callable_contract({'self': 'meadow_self_7c9265a'}, 'retrieve_input_file_sha256')
    def meadow_retrieve_input_file_sha256(meadow_self_7c9265a):
        return _name_boundary.attributes(meadow_idb)['analysis'].Root(_name_boundary.attributes(meadow_self_7c9265a)['idb']).sha256

    @_name_boundary.callable_contract({'self': 'meadow_self_327ec17'}, 'retrieve_input_file_md5')
    def meadow_retrieve_input_file_md5(meadow_self_327ec17):
        return _name_boundary.attributes(meadow_idb)['analysis'].Root(_name_boundary.attributes(meadow_self_327ec17)['idb']).md5

    @_name_boundary.callable_contract({'self': 'meadow_self_b92fc87'}, 'get_input_file_path')
    def meadow_get_input_file_path(meadow_self_b92fc87):
        return _name_boundary.attributes(meadow_idb)['analysis'].Root(_name_boundary.attributes(meadow_self_b92fc87)['idb']).input_file_path

@_name_boundary.class_contract('ida_funcs', {'FUNC_NORET': 'meadow_FUNC_NORET', 'FUNC_FAR': 'meadow_FUNC_FAR', 'FUNC_LIB': 'meadow_FUNC_LIB', 'FUNC_STATICDEF': 'meadow_FUNC_STATICDEF', 'FUNC_FRAME': 'meadow_FUNC_FRAME', 'FUNC_USERFAR': 'meadow_FUNC_USERFAR', 'FUNC_HIDDEN': 'meadow_FUNC_HIDDEN', 'FUNC_THUNK': 'meadow_FUNC_THUNK', 'FUNC_BOTTOMBP': 'meadow_FUNC_BOTTOMBP', 'FUNC_NORET_PENDING': 'meadow_FUNC_NORET_PENDING', 'FUNC_SP_READY': 'meadow_FUNC_SP_READY', 'FUNC_PURGED_OK': 'meadow_FUNC_PURGED_OK', 'FUNC_TAIL': 'meadow_FUNC_TAIL', 'get_func': 'meadow_get_func', 'get_func_cmt': 'meadow_get_func_cmt', 'get_func_name': 'meadow_get_func_name', 'get_func_qty': 'meadow_get_func_qty', 'getn_func': 'meadow_getn_func', 'idb': 'meadow_idb'})
class meadow_ida_funcs:
    meadow_FUNC_NORET = 1
    meadow_FUNC_FAR = 2
    meadow_FUNC_LIB = 4
    meadow_FUNC_STATICDEF = 8
    meadow_FUNC_FRAME = 16
    meadow_FUNC_USERFAR = 32
    meadow_FUNC_HIDDEN = 64
    meadow_FUNC_THUNK = 128
    meadow_FUNC_BOTTOMBP = 256
    meadow_FUNC_NORET_PENDING = 512
    meadow_FUNC_SP_READY = 1024
    meadow_FUNC_PURGED_OK = 16384
    meadow_FUNC_TAIL = 32768

    @meadow_wrap_module('idaapi')
    @meadow_wrap_module('idc', full=False)
    @_name_boundary.callable_contract({'self': 'meadow_self_a9fe8a5', 'db': 'meadow_db_884967d', 'api': 'meadow_api_local_ed24974'}, '__init__')
    def __init__(meadow_self_a9fe8a5, meadow_db_884967d, meadow_api_local_ed24974):
        _name_boundary.attributes(meadow_self_a9fe8a5)['idb'] = meadow_db_884967d
        meadow_self_a9fe8a5.api = meadow_api_local_ed24974

    @_name_boundary.callable_contract({'self': 'meadow_self_dcdd884', 'ea': 'meadow_ea_d2ef8f5'}, 'get_func')
    def meadow_get_func(meadow_self_dcdd884, meadow_ea_d2ef8f5):
        """
        get the func_t associated with the given address.
        if the address is not the start of a function (or function tail), then searches
         for a function that contains the given address.
        note: the range search is pretty slow, since we parse everything on-demand.
        """
        meadow_nn_ce2b175 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_dcdd884.api)['ida_netnode'])['netnode']('$ funcs')
        try:
            meadow_v_979433f = _name_boundary.attributes(meadow_nn_ce2b175)['supval'](tag='S', index=meadow_ea_d2ef8f5)
        except KeyError:
            for meadow_func_57beff6 in _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](_name_boundary.attributes(meadow_self_dcdd884)['idb']).functions.values():
                if not _name_boundary.attributes(meadow_func_57beff6)['startEA'] <= meadow_ea_d2ef8f5 < _name_boundary.attributes(meadow_func_57beff6)['endEA']:
                    continue
                if meadow_is_flag_set(meadow_func_57beff6.flags, _name_boundary.attributes(meadow_self_dcdd884)['FUNC_TAIL']):
                    return _name_boundary.attributes(meadow_self_dcdd884)['get_func'](_name_boundary.attributes(meadow_func_57beff6)['owner'])
                else:
                    return meadow_func_57beff6
            return None
        else:
            meadow_func_57beff6 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['func_t'](meadow_v_979433f, wordsize=_name_boundary.attributes(meadow_self_dcdd884)['idb'].wordsize)
            if meadow_is_flag_set(meadow_func_57beff6.flags, _name_boundary.attributes(meadow_self_dcdd884)['FUNC_TAIL']):
                return _name_boundary.attributes(meadow_self_dcdd884)['get_func'](_name_boundary.attributes(meadow_func_57beff6)['owner'])
            else:
                return meadow_func_57beff6

    @_name_boundary.callable_contract({'self': 'meadow_self_4679d60', 'ea': 'meadow_ea_99a751c', 'repeatable': 'meadow_repeatable_8e33aba'}, 'get_func_cmt')
    def meadow_get_func_cmt(meadow_self_4679d60, meadow_ea_99a751c, meadow_repeatable_8e33aba):
        meadow_func_6e5b8b3 = _name_boundary.attributes(meadow_self_4679d60)['get_func'](meadow_ea_99a751c)
        if meadow_func_6e5b8b3 is None:
            return ''
        meadow_nn_c311e87 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_4679d60.api)['ida_netnode'])['netnode']('$ funcs')
        try:
            if meadow_repeatable_8e33aba:
                meadow_tag_local_402c2ff = 'R'
            else:
                meadow_tag_local_402c2ff = 'C'
            return _name_boundary.attributes(meadow_nn_c311e87)['supstr'](tag=meadow_tag_local_402c2ff, index=_name_boundary.attributes(meadow_func_6e5b8b3)['startEA'])
        except KeyError:
            return ''

    @_name_boundary.callable_contract({'self': 'meadow_self_48710a5', 'ea': 'meadow_ea_7240a29'}, 'get_func_name')
    def meadow_get_func_name(meadow_self_48710a5, meadow_ea_7240a29):
        meadow_func_223b218 = _name_boundary.attributes(meadow_self_48710a5)['get_func'](meadow_ea_7240a29)
        if meadow_func_223b218 is None:
            return ''
        if meadow_is_flag_set(meadow_func_223b218.flags, _name_boundary.attributes(meadow_func_223b218)['FUNC_TAIL']) or meadow_ea_7240a29 != _name_boundary.attributes(meadow_func_223b218)['startEA']:
            raise KeyError(meadow_ea_7240a29)
        meadow_ea_7240a29 = _name_boundary.attributes(meadow_func_223b218)['startEA']
        meadow_nn_7c6cb72 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_48710a5.api)['ida_netnode'])['netnode'](meadow_ea_7240a29)
        try:
            return meadow_nn_7c6cb72.name()
        except:
            if _name_boundary.attributes(meadow_self_48710a5)['idb'].wordsize == 4:
                return 'sub_%04x' % meadow_ea_7240a29
            elif _name_boundary.attributes(meadow_self_48710a5)['idb'].wordsize == 8:
                return 'sub_%08x' % meadow_ea_7240a29
            else:
                raise RuntimeError('unexpected wordsize')

    @_name_boundary.callable_contract({'self': 'meadow_self_63d0dce'}, 'get_func_qty')
    def meadow_get_func_qty(meadow_self_63d0dce):
        return len(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](_name_boundary.attributes(meadow_self_63d0dce)['idb']).functions)

    @_name_boundary.callable_contract({'self': 'meadow_self_b1b52c6', 'n': 'meadow_n_111ad76'}, 'getn_func')
    def meadow_getn_func(meadow_self_b1b52c6, meadow_n_111ad76):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](_name_boundary.attributes(meadow_self_b1b52c6)['idb']).functions.values()[meadow_n_111ad76]

@_name_boundary.class_contract('BasicBlock', {'preds': 'meadow_preds', 'succs': 'meadow_succs', 'fc': 'meadow_fc', 'startEA': 'meadow_startEA', 'lastInstEA': 'meadow_lastInstEA', 'endEA': 'meadow_endEA'})
class meadow_BasicBlock(object):
    """
    interface extracted from: https://raw.githubusercontent.com/gabtremblay/idabearclean/master/idaapi.py
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_c49b497', 'flowchart': 'meadow_flowchart_e12e717', 'startEA': 'meadow_startEA_3207353', 'lastInstEA': 'meadow_lastInstEA_d810f28', 'endEA': 'meadow_endEA_19a5cba'}, '__init__')
    def __init__(meadow_self_c49b497, meadow_flowchart_e12e717, meadow_startEA_3207353, meadow_lastInstEA_d810f28, meadow_endEA_19a5cba):
        _name_boundary.attributes(meadow_self_c49b497)['fc'] = meadow_flowchart_e12e717
        meadow_self_c49b497.id = meadow_startEA_3207353
        _name_boundary.attributes(meadow_self_c49b497)['startEA'] = meadow_startEA_3207353
        _name_boundary.attributes(meadow_self_c49b497)['lastInstEA'] = meadow_lastInstEA_d810f28
        _name_boundary.attributes(meadow_self_c49b497)['endEA'] = meadow_endEA_19a5cba
        meadow_self_c49b497.type = NotImplementedError()

    @_name_boundary.callable_contract({'self': 'meadow_self_5358dd6'}, 'preds')
    def meadow_preds(meadow_self_5358dd6):
        for meadow_pred_01e96eb in _name_boundary.attributes(_name_boundary.attributes(meadow_self_5358dd6)['fc'])['preds'][_name_boundary.attributes(meadow_self_5358dd6)['startEA']]:
            yield _name_boundary.attributes(_name_boundary.attributes(meadow_self_5358dd6)['fc'])['bbs'][meadow_pred_01e96eb]

    @_name_boundary.callable_contract({'self': 'meadow_self_7862658'}, 'succs')
    def meadow_succs(meadow_self_7862658):
        for meadow_succ_a8c9073 in _name_boundary.attributes(_name_boundary.attributes(meadow_self_7862658)['fc'])['succs'][_name_boundary.attributes(meadow_self_7862658)['startEA']]:
            yield _name_boundary.attributes(_name_boundary.attributes(meadow_self_7862658)['fc'])['bbs'][meadow_succ_a8c9073]

    @_name_boundary.callable_contract({'self': 'meadow_self_71ff02a'}, '__str__')
    def __str__(meadow_self_71ff02a):
        return 'BasicBlock(startEA: 0x%x, endEA: 0x%x)' % (_name_boundary.attributes(meadow_self_71ff02a)['startEA'], _name_boundary.attributes(meadow_self_71ff02a)['endEA'])

@_name_boundary.callable_contract({'s': 'meadow_s_local_32afc1a'}, 'is_empty')
def meadow_is_empty(meadow_s_local_32afc1a):
    for meadow_c_local_66df87e in meadow_s_local_32afc1a:
        return False
    return True

@_name_boundary.class_contract('idaapi', {'fl_U': 'meadow_fl_U', 'fl_CF': 'meadow_fl_CF', 'fl_CN': 'meadow_fl_CN', 'fl_JF': 'meadow_fl_JF', 'fl_JN': 'meadow_fl_JN', 'fl_USobsolete': 'meadow_fl_USobsolete', 'fl_F': 'meadow_fl_F', 'dr_U': 'meadow_dr_U', 'dr_O': 'meadow_dr_O', 'dr_W': 'meadow_dr_W', 'dr_R': 'meadow_dr_R', 'dr_T': 'meadow_dr_T', 'dr_I': 'meadow_dr_I', 'XREF_ALL': 'meadow_XREF_ALL', 'XREF_FAR': 'meadow_XREF_FAR', 'XREF_DATA': 'meadow_XREF_DATA', '_find_bb_end': 'meadow__find_bb_end', '_find_bb_start': 'meadow__find_bb_start', '_get_flow_preds': 'meadow__get_flow_preds', '_get_flow_succs': 'meadow__get_flow_succs', 'FlowChart': 'meadow_FlowChart', 'get_next_fixup_ea': 'meadow_get_next_fixup_ea', 'contains_fixups': 'meadow_contains_fixups', 'getseg': 'meadow_getseg', 'get_segm_name': 'meadow_get_segm_name', 'get_segm_end': 'meadow_get_segm_end', 'IdaInfo': 'meadow_IdaInfo', 'get_inf_structure': 'meadow_get_inf_structure', 'get_imagebase': 'meadow_get_imagebase', 'TYPE_NAMES': 'meadow_TYPE_NAMES', 'get_file_type_name': 'meadow_get_file_type_name', 'idb': 'meadow_idb', 'BADADDR': 'meadow_BADADDR', 'preds': 'meadow_preds', 'succs': 'meadow_succs', 'bbs': 'meadow_bbs'})
class meadow_idaapi:
    meadow_fl_U = 0
    meadow_fl_CF = 16
    meadow_fl_CN = 17
    meadow_fl_JF = 18
    meadow_fl_JN = 19
    meadow_fl_USobsolete = 20
    meadow_fl_F = 21
    meadow_dr_U = 0
    meadow_dr_O = 1
    meadow_dr_W = 2
    meadow_dr_R = 3
    meadow_dr_T = 4
    meadow_dr_I = 5
    meadow_XREF_ALL = 0
    meadow_XREF_FAR = 1
    meadow_XREF_DATA = 2

    @_name_boundary.callable_contract({'self': 'meadow_self_8a1276d', 'db': 'meadow_db_86a40a2', 'api': 'meadow_api_local_594af34'}, '__init__')
    def __init__(meadow_self_8a1276d, meadow_db_86a40a2, meadow_api_local_594af34):
        _name_boundary.attributes(meadow_self_8a1276d)['idb'] = meadow_db_86a40a2
        meadow_self_8a1276d.api = meadow_api_local_594af34
        _name_boundary.attributes(meadow_self_8a1276d)['BADADDR'] = _name_boundary.attributes(_name_boundary.attributes(meadow_self_8a1276d.api)['idc'])['BADADDR']

    @_name_boundary.callable_contract({'self': 'meadow_self_9e78017', 'ea': 'meadow_ea_4e5d3fd'}, '_find_bb_end')
    def meadow__find_bb_end(meadow_self_9e78017, meadow_ea_4e5d3fd):
        """
        Args:
          ea (int): address at which a basic block begins. behavior undefined if its not a block start.

        Returns:
          int: the address of the final instruction in the basic block. it may be the same as the start.
        """
        if not meadow_is_empty(_name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_9e78017)['idb'], meadow_ea_4e5d3fd, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F']])):
            return meadow_ea_4e5d3fd
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['idc'])['GetFlags'](meadow_ea_4e5d3fd):
            return meadow_ea_4e5d3fd
        while True:
            meadow_last_ea_f28489d = meadow_ea_4e5d3fd
            meadow_ea_4e5d3fd = _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['idc'])['NextHead'](meadow_ea_4e5d3fd)
            meadow_flags_local_9f48450 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['idc'])['GetFlags'](meadow_ea_4e5d3fd)
            if meadow_flags_local_9f48450 == 0:
                return meadow_last_ea_f28489d
            if _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['ida_bytes'])['has_ref'](meadow_flags_local_9f48450):
                return meadow_last_ea_f28489d
            if _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['ida_bytes'])['is_func'](meadow_flags_local_9f48450):
                return meadow_last_ea_f28489d
            if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_9e78017.api)['ida_bytes'])['is_flow'](meadow_flags_local_9f48450):
                return meadow_last_ea_f28489d
            if not meadow_is_empty(_name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_9e78017)['idb'], meadow_ea_4e5d3fd, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F']])):
                return meadow_ea_4e5d3fd

    @_name_boundary.callable_contract({'self': 'meadow_self_7e2c135', 'ea': 'meadow_ea_66d3116'}, '_find_bb_start')
    def meadow__find_bb_start(meadow_self_7e2c135, meadow_ea_66d3116):
        """
        Args:
          ea (int): address at which a basic block ends. behavior undefined if its not a block end.

        Returns:
          int: the address of the first instruction in the basic block. it may be the same as the end.
        """
        while True:
            meadow_flags_local_3703200 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e2c135.api)['idc'])['GetFlags'](meadow_ea_66d3116)
            if _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e2c135.api)['ida_bytes'])['has_ref'](meadow_flags_local_3703200):
                return meadow_ea_66d3116
            if _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e2c135.api)['ida_bytes'])['is_func'](meadow_flags_local_3703200):
                return meadow_ea_66d3116
            meadow_last_ea_41891b1 = meadow_ea_66d3116
            meadow_ea_66d3116 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e2c135.api)['idc'])['PrevHead'](meadow_ea_66d3116)
            if not meadow_is_empty(_name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_7e2c135)['idb'], meadow_ea_66d3116, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F']])):
                return meadow_last_ea_41891b1
            if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e2c135.api)['ida_bytes'])['is_flow'](meadow_flags_local_3703200):
                return meadow_last_ea_41891b1

    @_name_boundary.callable_contract({'self': 'meadow_self_1760a6e', 'ea': 'meadow_ea_52289ca'}, '_get_flow_preds')
    def meadow__get_flow_preds(meadow_self_1760a6e, meadow_ea_52289ca):
        meadow_flags_local_4e27b8d = _name_boundary.attributes(_name_boundary.attributes(meadow_self_1760a6e.api)['idc'])['GetFlags'](meadow_ea_52289ca)
        if meadow_flags_local_4e27b8d is not None and _name_boundary.attributes(_name_boundary.attributes(meadow_self_1760a6e.api)['ida_bytes'])['is_flow'](meadow_flags_local_4e27b8d):
            yield _name_boundary.attributes(meadow_idb)['analysis'].Xref(_name_boundary.attributes(_name_boundary.attributes(meadow_self_1760a6e.api)['idc'])['PrevHead'](meadow_ea_52289ca), meadow_ea_52289ca, _name_boundary.attributes(meadow_idaapi)['fl_F'])
        for meadow_xref_f88f001 in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_to(_name_boundary.attributes(meadow_self_1760a6e)['idb'], meadow_ea_52289ca, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F']]):
            yield meadow_xref_f88f001

    @_name_boundary.callable_contract({'self': 'meadow_self_d554f40', 'ea': 'meadow_ea_900c13e'}, '_get_flow_succs')
    def meadow__get_flow_succs(meadow_self_d554f40, meadow_ea_900c13e):
        meadow_nextea_895ec9f = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d554f40.api)['idc'])['NextHead'](meadow_ea_900c13e)
        meadow_nextflags_a37616c = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d554f40.api)['idc'])['GetFlags'](meadow_nextea_895ec9f)
        if meadow_nextflags_a37616c is not None and _name_boundary.attributes(_name_boundary.attributes(meadow_self_d554f40.api)['ida_bytes'])['is_flow'](meadow_nextflags_a37616c):
            yield _name_boundary.attributes(meadow_idb)['analysis'].Xref(meadow_ea_900c13e, meadow_nextea_895ec9f, _name_boundary.attributes(meadow_idaapi)['fl_F'])
        for meadow_xref_7b39a3b in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_d554f40)['idb'], meadow_ea_900c13e, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F']]):
            yield meadow_xref_7b39a3b

    @_name_boundary.callable_contract({'self': 'meadow_self_00acee1', 'func': 'meadow_func_d00e214'}, 'FlowChart')
    def meadow_FlowChart(meadow_self_00acee1, meadow_func_d00e214):
        """
        Example::

            f = idaapi.FlowChart(idaapi.get_func(here()))
            for block in f:
                if p:
                    print "%x - %x [%d]:" % (block.startEA, block.endEA, block.id)
                for succ_block in block.succs():
                    if p:
                        print "  %x - %x [%d]:" % (succ_block.startEA, succ_block.endEA, succ_block.id)

                for pred_block in block.preds():
                    if p:
                        print "  %x - %x [%d]:" % (pred_block.startEA, pred_block.endEA, pred_block.id)

        via: https://github.com/EiNSTeiN-/idapython/blob/master/examples/ex_gdl_qflow_chart.py
        """

        @_name_boundary.class_contract('_FlowChart', {'idb': 'meadow_idb', 'preds': 'meadow_preds', 'succs': 'meadow_succs', 'bbs': 'meadow_bbs'})
        class meadow__FlowChart_c982a00:

            @_name_boundary.callable_contract({'self': 'meadow_self_57c8440', 'db': 'meadow_db_6859ed6', 'ea': 'meadow_ea_27d8b75', 'api': 'meadow_api_local_d873f44'}, '__init__')
            def __init__(meadow_self_57c8440, meadow_db_6859ed6, meadow_api_local_d873f44, meadow_ea_27d8b75):
                _name_boundary.attributes(meadow_self_57c8440)['idb'] = meadow_db_6859ed6
                meadow_logger.debug('creating flowchart for %x', meadow_ea_27d8b75)
                meadow_seen_e6af865 = set([])
                meadow_bbs_by_start_da5450e = {}
                meadow_bbs_by_end_df26ba4 = {}
                meadow_preds_d6b1ab2 = meadow_collections.defaultdict(lambda: set([]))
                meadow_succs_f6e3953 = meadow_collections.defaultdict(lambda: set([]))
                meadow_lastInstEA_4a24aa3 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idaapi'])['_find_bb_end'](meadow_ea_27d8b75)
                meadow_logger.debug('found end. %x -> %x', meadow_ea_27d8b75, meadow_lastInstEA_4a24aa3)
                meadow_block_ceff641 = meadow_BasicBlock(meadow_self_57c8440, meadow_ea_27d8b75, meadow_lastInstEA_4a24aa3, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idc'])['NextHead'](meadow_lastInstEA_4a24aa3))
                meadow_bbs_by_start_da5450e[meadow_ea_27d8b75] = meadow_block_ceff641
                meadow_bbs_by_end_df26ba4[meadow_lastInstEA_4a24aa3] = meadow_block_ceff641
                meadow_q_872ac9a = [meadow_block_ceff641]
                while meadow_q_872ac9a:
                    meadow_logger.debug('iteration')
                    meadow_logger.debug('queue: [%s]', ', '.join(map(str, meadow_q_872ac9a)))
                    meadow_block_ceff641 = meadow_q_872ac9a[0]
                    meadow_q_872ac9a = meadow_q_872ac9a[1:]
                    meadow_logger.debug('exploring %s', meadow_block_ceff641)
                    if _name_boundary.attributes(meadow_block_ceff641)['startEA'] in meadow_seen_e6af865:
                        meadow_logger.debug('already seen!')
                        continue
                    meadow_logger.debug('new!')
                    meadow_seen_e6af865.add(_name_boundary.attributes(meadow_block_ceff641)['startEA'])
                    for meadow_xref_de65965 in _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idaapi'])['_get_flow_preds'](_name_boundary.attributes(meadow_block_ceff641)['startEA']):
                        if meadow_xref_de65965.frm not in meadow_bbs_by_end_df26ba4:
                            meadow_pred_start_39136be = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idaapi'])['_find_bb_start'](meadow_xref_de65965.frm)
                            meadow_pred_9bc1449 = meadow_BasicBlock(meadow_self_57c8440, meadow_pred_start_39136be, meadow_xref_de65965.frm, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idc'])['NextHead'](meadow_xref_de65965.frm))
                            meadow_bbs_by_start_da5450e[_name_boundary.attributes(meadow_pred_9bc1449)['startEA']] = meadow_pred_9bc1449
                            meadow_bbs_by_end_df26ba4[_name_boundary.attributes(meadow_pred_9bc1449)['lastInstEA']] = meadow_pred_9bc1449
                        else:
                            meadow_pred_9bc1449 = meadow_bbs_by_end_df26ba4[meadow_xref_de65965.frm]
                        meadow_logger.debug('pred: %s', meadow_pred_9bc1449)
                        meadow_preds_d6b1ab2[_name_boundary.attributes(meadow_block_ceff641)['startEA']].add(_name_boundary.attributes(meadow_pred_9bc1449)['startEA'])
                        meadow_succs_f6e3953[_name_boundary.attributes(meadow_pred_9bc1449)['startEA']].add(_name_boundary.attributes(meadow_block_ceff641)['startEA'])
                        meadow_q_872ac9a.append(meadow_pred_9bc1449)
                    for meadow_xref_de65965 in _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idaapi'])['_get_flow_succs'](_name_boundary.attributes(meadow_block_ceff641)['lastInstEA']):
                        if meadow_xref_de65965.to not in meadow_bbs_by_start_da5450e:
                            meadow_succ_end_e15a270 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idaapi'])['_find_bb_end'](meadow_xref_de65965.to)
                            meadow_succ_05cb834 = meadow_BasicBlock(meadow_self_57c8440, meadow_xref_de65965.to, meadow_succ_end_e15a270, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_d873f44)['idc'])['NextHead'](meadow_succ_end_e15a270))
                            meadow_bbs_by_start_da5450e[_name_boundary.attributes(meadow_succ_05cb834)['startEA']] = meadow_succ_05cb834
                            meadow_bbs_by_end_df26ba4[_name_boundary.attributes(meadow_succ_05cb834)['lastInstEA']] = meadow_succ_05cb834
                        else:
                            meadow_succ_05cb834 = meadow_bbs_by_start_da5450e[meadow_xref_de65965.to]
                        meadow_logger.debug('succ: %s', meadow_succ_05cb834)
                        meadow_succs_f6e3953[_name_boundary.attributes(meadow_block_ceff641)['startEA']].add(_name_boundary.attributes(meadow_succ_05cb834)['startEA'])
                        meadow_preds_d6b1ab2[_name_boundary.attributes(meadow_succ_05cb834)['startEA']].add(_name_boundary.attributes(meadow_block_ceff641)['startEA'])
                        meadow_q_872ac9a.append(meadow_succ_05cb834)
                _name_boundary.attributes(meadow_self_57c8440)['preds'] = meadow_preds_d6b1ab2
                _name_boundary.attributes(meadow_self_57c8440)['succs'] = meadow_succs_f6e3953
                _name_boundary.attributes(meadow_self_57c8440)['bbs'] = meadow_bbs_by_start_da5450e

            @_name_boundary.callable_contract({'self': 'meadow_self_86ef379'}, '__iter__')
            def __iter__(meadow_self_86ef379):
                for meadow_bb_c73e119 in _name_boundary.attributes(meadow_self_86ef379)['bbs'].values():
                    yield meadow_bb_c73e119
        return meadow__FlowChart_c982a00(_name_boundary.attributes(meadow_self_00acee1)['idb'], meadow_self_00acee1.api, _name_boundary.attributes(meadow_func_d00e214)['startEA'])

    @_name_boundary.callable_contract({'self': 'meadow_self_967e0d1', 'ea': 'meadow_ea_23fcc92'}, 'get_next_fixup_ea')
    def meadow_get_next_fixup_ea(meadow_self_967e0d1, meadow_ea_23fcc92):
        meadow_nn_0542ce6 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_967e0d1.api)['ida_netnode'])['netnode']('$ fixups')
        for meadow_index_124ae47 in _name_boundary.attributes(meadow_nn_0542ce6)['sups'](tag='S'):
            if meadow_ea_23fcc92 <= meadow_index_124ae47:
                return meadow_index_124ae47
        raise KeyError(meadow_ea_23fcc92)

    @_name_boundary.callable_contract({'self': 'meadow_self_1f98f36', 'ea': 'meadow_ea_4cc431a', 'size': 'meadow_size_local_fc74ca1'}, 'contains_fixups')
    def meadow_contains_fixups(meadow_self_1f98f36, meadow_ea_4cc431a, meadow_size_local_fc74ca1):
        try:
            meadow_next_fixup_3ba48c6 = _name_boundary.attributes(meadow_self_1f98f36)['get_next_fixup_ea'](meadow_ea_4cc431a)
        except KeyError:
            return False
        else:
            if meadow_next_fixup_3ba48c6 < meadow_ea_4cc431a + meadow_size_local_fc74ca1:
                return True
            else:
                return False

    @_name_boundary.callable_contract({'self': 'meadow_self_71d4722', 'ea': 'meadow_ea_cc28393'}, 'getseg')
    def meadow_getseg(meadow_self_71d4722, meadow_ea_cc28393):
        meadow_segs_bdb75eb = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_71d4722)['idb']).segments
        for meadow_seg_local_95e31e7 in meadow_segs_bdb75eb.values():
            if _name_boundary.attributes(meadow_seg_local_95e31e7)['startEA'] <= meadow_ea_cc28393 < _name_boundary.attributes(meadow_seg_local_95e31e7)['endEA']:
                return meadow_seg_local_95e31e7

    @_name_boundary.callable_contract({'self': 'meadow_self_d32c106', 'ea': 'meadow_ea_d2df121'}, 'get_segm_name')
    def meadow_get_segm_name(meadow_self_d32c106, meadow_ea_d2df121):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_d32c106.api)['idc'])['SegName'](meadow_ea_d2df121)

    @_name_boundary.callable_contract({'self': 'meadow_self_7f79cca', 'ea': 'meadow_ea_aa905ff'}, 'get_segm_end')
    def meadow_get_segm_end(meadow_self_7f79cca, meadow_ea_aa905ff):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_7f79cca.api)['idc'])['SegEnd'](meadow_ea_aa905ff)

    class meadow_IdaInfo(object):

        @_name_boundary.callable_contract({'self': 'meadow_self_9e86957', 'api': 'meadow_api_local_bca0194', 'inf': 'meadow_inf_local_b6a80a0'}, '__init__')
        def __init__(meadow_self_9e86957, meadow_api_local_bca0194, meadow_inf_local_b6a80a0):
            meadow_self_9e86957.api = meadow_api_local_bca0194
            meadow_self_9e86957.inf = meadow_inf_local_b6a80a0

        @property
        @_name_boundary.callable_contract({'self': 'meadow_self_d7d6d83'}, 'tag')
        def tag(meadow_self_d7d6d83):
            return meadow_self_d7d6d83.inf.tag

        @property
        @_name_boundary.callable_contract({'self': 'meadow_self_99adb10'}, 'version')
        def version(meadow_self_99adb10):
            return meadow_self_99adb10.inf.version

        @property
        @_name_boundary.callable_contract({'self': 'meadow_self_c46b6ef'}, 'procname')
        def procname(meadow_self_c46b6ef):
            return meadow_self_c46b6ef.inf.procname

        @property
        @_name_boundary.callable_contract({'self': 'meadow_self_62c4190'}, 'lflags')
        def lflags(meadow_self_62c4190):
            return meadow_self_62c4190.inf.lflags

        @property
        @_name_boundary.callable_contract({'self': 'meadow_self_a93f793'}, 'filetype')
        def filetype(meadow_self_a93f793):
            return meadow_self_a93f793.inf.filetype

        @_name_boundary.callable_contract({'self': 'meadow_self_be7acb3'}, 'is_32bit')
        def meadow_is_32bit(meadow_self_be7acb3):
            return meadow_self_be7acb3.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_be7acb3.api)['ida_ida'])['LFLG_PC_FLAT'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_1879711'}, 'is_64bit')
        def meadow_is_64bit(meadow_self_1879711):
            return meadow_self_1879711.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_1879711.api)['ida_ida'])['LFLG_64BIT'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_8386269'}, 'is_snapshot')
        def meadow_is_snapshot(meadow_self_8386269):
            return meadow_self_8386269.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_8386269.api)['ida_ida'])['LFLG_SNAPSHOT'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_0e90eaf'}, 'is_dll')
        def meadow_is_dll(meadow_self_0e90eaf):
            return meadow_self_0e90eaf.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_0e90eaf.api)['ida_ida'])['LFLG_IS_DLL'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_02aee81'}, 'is_flat_off32')
        def meadow_is_flat_off32(meadow_self_02aee81):
            return meadow_self_02aee81.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_02aee81.api)['ida_ida'])['LFLG_FLAT_OFF32'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_3eb1e98'}, 'is_be')
        def meadow_is_be(meadow_self_3eb1e98):
            return meadow_self_3eb1e98.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_3eb1e98.api)['ida_ida'])['LFLG_MSF'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_5cd8d4d'}, 'is_wide_high_byte_first')
        def meadow_is_wide_high_byte_first(meadow_self_5cd8d4d):
            return meadow_self_5cd8d4d.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_5cd8d4d.api)['ida_ida'])['LFLG_WIDE_HBF'] > 0

        @_name_boundary.callable_contract({'self': 'meadow_self_375c444'}, 'is_kernel_mode')
        def meadow_is_kernel_mode(meadow_self_375c444):
            return meadow_self_375c444.lflags & _name_boundary.attributes(_name_boundary.attributes(meadow_self_375c444.api)['ida_ida'])['LFLG_KERNMODE'] > 0
        is_32bit = meadow_is_32bit
        is_64bit = meadow_is_64bit
        is_snapshot = meadow_is_snapshot
        is_dll = meadow_is_dll
        is_flat_off32 = meadow_is_flat_off32
        is_be = meadow_is_be
        is_wide_high_byte_first = meadow_is_wide_high_byte_first
        is_kernel_mode = meadow_is_kernel_mode

    @_name_boundary.callable_contract({'self': 'meadow_self_bd1ab28'}, 'get_inf_structure')
    def meadow_get_inf_structure(meadow_self_bd1ab28):
        return _name_boundary.attributes(meadow_self_bd1ab28)['IdaInfo'](meadow_self_bd1ab28.api, _name_boundary.attributes(meadow_idb)['analysis'].Root(_name_boundary.attributes(meadow_self_bd1ab28)['idb']).idainfo)

    @_name_boundary.callable_contract({'self': 'meadow_self_252f73c'}, 'get_imagebase')
    def meadow_get_imagebase(meadow_self_252f73c):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_252f73c.api)['ida_nalt'])['get_imagebase']()
    meadow_TYPE_NAMES = {0: 'MS DOS EXE File', 1: 'MS DOS COM File', 2: 'Binary file', 3: 'MS DOS Driver', 4: 'New Executable (NE)', 5: 'Intel Hex Object File', 6: 'MOS Technology Hex Object File', 7: 'Linear Executable (LX)', 8: 'Linear Executable (LE)', 9: 'Netware Loadable Module (NLM)', 10: 'Common Object File Format (COFF)', 11: 'Portable Executable (PE)', 12: 'Object Module Format', 13: 'R-records', 14: 'ZIP file', 15: 'Library of OMF Modules', 16: 'ar library', 17: 'file is loaded using LOADER DLL', 18: 'Executable and Linkable Format (ELF)', 19: 'Watcom DOS32 Extender (W32RUN)', 20: 'Linux a.out (AOUT)', 21: 'PalmPilot program file', 22: 'MS DOS EXE File', 23: 'MS DOS COM File', 24: 'AIX ar library'}

    @_name_boundary.callable_contract({'self': 'meadow_self_984bc10'}, 'get_file_type_name')
    def meadow_get_file_type_name(meadow_self_984bc10):
        return _name_boundary.attributes(meadow_self_984bc10)['TYPE_NAMES'][_name_boundary.attributes(meadow_self_984bc10)['get_inf_structure']().filetype]

@_name_boundary.class_contract('StringItem', {'ea': 'meadow_ea'})
class meadow_StringItem:

    @_name_boundary.callable_contract({'self': 'meadow_self_cdd2512', 'ea': 'meadow_ea_3545f7a', 'length': 'meadow_length_local_98ddb34', 'strtype': 'meadow_strtype_local_f6ba2f9', 's': 'meadow_s_local_7f1594d'}, '__init__')
    def __init__(meadow_self_cdd2512, meadow_ea_3545f7a, meadow_length_local_98ddb34, meadow_strtype_local_f6ba2f9, meadow_s_local_7f1594d):
        _name_boundary.attributes(meadow_self_cdd2512)['ea'] = meadow_ea_3545f7a
        meadow_self_cdd2512.length = meadow_length_local_98ddb34
        meadow_self_cdd2512.strtype = meadow_strtype_local_f6ba2f9
        meadow_self_cdd2512.s = meadow_s_local_7f1594d

    @_name_boundary.callable_contract({'self': 'meadow_self_a8978a3'}, '__str__')
    def __str__(meadow_self_a8978a3):
        return meadow_self_a8978a3.s

@_name_boundary.class_contract('_Strings', {'C': 'meadow_C', 'C_16': 'meadow_C_16', 'C_32': 'meadow_C_32', 'PASCAL': 'meadow_PASCAL', 'PASCAL_16': 'meadow_PASCAL_16', 'LEN2': 'meadow_LEN2', 'LEN2_16': 'meadow_LEN2_16', 'LEN4': 'meadow_LEN4', 'LEN4_16': 'meadow_LEN4_16', 'ASCII_BYTE': 'meadow_ASCII_BYTE', 'clear_cache': 'meadow_clear_cache', 'get_seg_data': 'meadow_get_seg_data', 'parse_C_strings': 'meadow_parse_C_strings', 'parse_C_16_strings': 'meadow_parse_C_16_strings', 'parse_C_32_strings': 'meadow_parse_C_32_strings', 'parse_PASCAL_strings': 'meadow_parse_PASCAL_strings', 'parse_PASCAL_16_strings': 'meadow_parse_PASCAL_16_strings', 'parse_LEN2_strings': 'meadow_parse_LEN2_strings', 'parse_LEN2_16_strings': 'meadow_parse_LEN2_16_strings', 'parse_LEN4_strings': 'meadow_parse_LEN4_strings', 'parse_LEN4_16_strings': 'meadow_parse_LEN4_16_strings', 'refresh': 'meadow_refresh', 'setup': 'meadow_setup', 'db': 'meadow_db', 'cache': 'meadow_cache', 'strtypes': 'meadow_strtypes', 'minlen': 'meadow_minlen', 'only_7bit': 'meadow_only_7bit', 'ignore_instructions': 'meadow_ignore_instructions', 'display_only_existing_strings': 'meadow_display_only_existing_strings'})
class meadow__Strings:
    meadow_C = 0
    meadow_C_16 = 1
    meadow_C_32 = 2
    meadow_PASCAL = 4
    meadow_PASCAL_16 = 5
    meadow_LEN2 = 8
    meadow_LEN2_16 = 9
    meadow_LEN4 = 12
    meadow_LEN4_16 = 13
    meadow_ASCII_BYTE = b' !"#\\$%&\'\\(\\)\\*\\+,-\\./0123456789:;<=>\\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\[\\]\\^_`abcdefghijklmnopqrstuvwxyz\\{\\|\\}\\\\~\t'

    @_name_boundary.callable_contract({'self': 'meadow_self_9b636f1', 'db': 'meadow_db_1756c4b', 'api': 'meadow_api_local_ebb5309'}, '__init__')
    def __init__(meadow_self_9b636f1, meadow_db_1756c4b, meadow_api_local_ebb5309):
        _name_boundary.attributes(meadow_self_9b636f1)['db'] = meadow_db_1756c4b
        meadow_self_9b636f1.api = meadow_api_local_ebb5309
        _name_boundary.attributes(meadow_self_9b636f1)['cache'] = None
        _name_boundary.attributes(meadow_self_9b636f1)['strtypes'] = [0]
        _name_boundary.attributes(meadow_self_9b636f1)['minlen'] = 5
        _name_boundary.attributes(meadow_self_9b636f1)['only_7bit'] = True
        _name_boundary.attributes(meadow_self_9b636f1)['ignore_instructions'] = False
        _name_boundary.attributes(meadow_self_9b636f1)['display_only_existing_strings'] = False

    @_name_boundary.callable_contract({'self': 'meadow_self_b841220'}, 'clear_cache')
    def meadow_clear_cache(meadow_self_b841220):
        _name_boundary.attributes(meadow_self_b841220)['cache'] = None

    @meadow_memoized_method()
    @_name_boundary.callable_contract({'self': 'meadow_self_d1701c8', 'seg': 'meadow_seg_local_ee23b69'}, 'get_seg_data')
    def meadow_get_seg_data(meadow_self_d1701c8, meadow_seg_local_ee23b69):
        meadow_start_local_5b9121e = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d1701c8.api)['idc'])['SegStart'](meadow_seg_local_ee23b69)
        meadow_end_local_44b6033 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d1701c8.api)['idc'])['SegEnd'](meadow_start_local_5b9121e)
        meadow_IdbByte_ffbd08f = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d1701c8.api)['idc'])['IdbByte']
        meadow_get_flags_48e72d9 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d1701c8.api)['ida_bytes'])['get_flags']
        meadow_has_value_1af6203 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_d1701c8.api)['ida_bytes'])['has_value']
        meadow_data_4f8144e = []
        for meadow_i_3585b2a in range(meadow_start_local_5b9121e, meadow_end_local_44b6033):
            try:
                meadow_b_local_e900a8d = meadow_IdbByte_ffbd08f(meadow_i_3585b2a)
            except KeyError:
                break
            if meadow_b_local_e900a8d == 0:
                meadow_flags_local_39d7f61 = meadow_get_flags_48e72d9(meadow_i_3585b2a)
                if not meadow_has_value_1af6203(meadow_flags_local_39d7f61):
                    break
            meadow_data_4f8144e.append(meadow_b_local_e900a8d)
        if meadow_six.PY2:
            return ''.join(map(chr, meadow_data_4f8144e))
        else:
            return bytes(meadow_data_4f8144e)

    @_name_boundary.callable_contract({'self': 'meadow_self_30cdf70', 'va': 'meadow_va_9ff7374', 'buf': 'meadow_buf_local_bb964d4'}, 'parse_C_strings')
    def meadow_parse_C_strings(meadow_self_30cdf70, meadow_va_9ff7374, meadow_buf_local_bb964d4):
        meadow_reg_3c96e66 = b'([%s]{%d,})' % (_name_boundary.attributes(meadow__Strings)['ASCII_BYTE'], _name_boundary.attributes(meadow_self_30cdf70)['minlen'])
        meadow_ascii_re_40f5bbd = meadow_re.compile(meadow_reg_3c96e66)
        for meadow_match_f1fefe5 in meadow_ascii_re_40f5bbd.finditer(meadow_buf_local_bb964d4):
            meadow_s_local_401a742 = meadow_match_f1fefe5.group().decode('ascii')
            yield meadow_StringItem(meadow_va_9ff7374 + meadow_match_f1fefe5.start(), len(meadow_s_local_401a742), _name_boundary.attributes(meadow__Strings)['C'], meadow_s_local_401a742)

    @_name_boundary.callable_contract({'self': 'meadow_self_f057b14', 'va': 'meadow_va_224a194', 'buf': 'meadow_buf_local_f3c791e'}, 'parse_C_16_strings')
    def meadow_parse_C_16_strings(meadow_self_f057b14, meadow_va_224a194, meadow_buf_local_f3c791e):
        meadow_reg_f108f46 = b'((?:[%s]\x00){%d,})' % (_name_boundary.attributes(meadow__Strings)['ASCII_BYTE'], _name_boundary.attributes(meadow_self_f057b14)['minlen'])
        meadow_uni_re_f1e7555 = meadow_re.compile(meadow_reg_f108f46)
        for meadow_match_be7028c in meadow_uni_re_f1e7555.finditer(meadow_buf_local_f3c791e):
            try:
                meadow_s_local_aa3391a = meadow_match_be7028c.group().decode('utf-16')
            except UnicodeDecodeError:
                continue
            else:
                yield meadow_StringItem(meadow_va_224a194 + meadow_match_be7028c.start(), len(meadow_s_local_aa3391a), _name_boundary.attributes(meadow__Strings)['C_16'], meadow_s_local_aa3391a)

    @_name_boundary.callable_contract({'self': 'meadow_self_9290af4', 'va': 'meadow_va_d64b929', 'buf': 'meadow_buf_local_79fe283'}, 'parse_C_32_strings')
    def meadow_parse_C_32_strings(meadow_self_9290af4, meadow_va_d64b929, meadow_buf_local_79fe283):
        meadow_reg_1927ebe = b'((?:[%s]\x00\x00\x00){%d,})' % (_name_boundary.attributes(meadow__Strings)['ASCII_BYTE'], _name_boundary.attributes(meadow_self_9290af4)['minlen'])
        meadow_uni_re_14026d4 = meadow_re.compile(meadow_reg_1927ebe)
        for meadow_match_d43457c in meadow_uni_re_14026d4.finditer(meadow_buf_local_79fe283):
            try:
                meadow_s_local_591811c = meadow_match_d43457c.group().decode('utf-32')
            except UnicodeDecodeError:
                continue
            else:
                yield meadow_StringItem(meadow_va_d64b929 + meadow_match_d43457c.start(), len(meadow_s_local_591811c), _name_boundary.attributes(meadow__Strings)['C_32'], meadow_s_local_591811c)

    @_name_boundary.callable_contract({'self': 'meadow_self_d85b36c', 'va': 'meadow_va_e72fc1a', 'buf': 'meadow_buf_local_f4231be'}, 'parse_PASCAL_strings')
    def meadow_parse_PASCAL_strings(meadow_self_d85b36c, meadow_va_e72fc1a, meadow_buf_local_f4231be):
        raise NotImplementedError('parse PASCAL strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_b809237', 'va': 'meadow_va_958447a', 'buf': 'meadow_buf_local_d58d724'}, 'parse_PASCAL_16_strings')
    def meadow_parse_PASCAL_16_strings(meadow_self_b809237, meadow_va_958447a, meadow_buf_local_d58d724):
        raise NotImplementedError('parse PASCAL_16 strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_e9427ed', 'va': 'meadow_va_aa07d9b', 'buf': 'meadow_buf_local_bc58392'}, 'parse_LEN2_strings')
    def meadow_parse_LEN2_strings(meadow_self_e9427ed, meadow_va_aa07d9b, meadow_buf_local_bc58392):
        raise NotImplementedError('parse LEN2 strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_f422f2d', 'va': 'meadow_va_a0b86df', 'buf': 'meadow_buf_local_2adb740'}, 'parse_LEN2_16_strings')
    def meadow_parse_LEN2_16_strings(meadow_self_f422f2d, meadow_va_a0b86df, meadow_buf_local_2adb740):
        raise NotImplementedError('parse LEN2_16 strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_3c58d38', 'va': 'meadow_va_aab73ce', 'buf': 'meadow_buf_local_bd544d1'}, 'parse_LEN4_strings')
    def meadow_parse_LEN4_strings(meadow_self_3c58d38, meadow_va_aab73ce, meadow_buf_local_bd544d1):
        raise NotImplementedError('parse LEN4 strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_50456f6', 'va': 'meadow_va_271d581', 'buf': 'meadow_buf_local_055646c'}, 'parse_LEN4_16_strings')
    def meadow_parse_LEN4_16_strings(meadow_self_50456f6, meadow_va_271d581, meadow_buf_local_055646c):
        raise NotImplementedError('parse LEN4_16 strings')

    @_name_boundary.callable_contract({'self': 'meadow_self_21814dc'}, 'refresh')
    def meadow_refresh(meadow_self_21814dc):
        meadow_ret_local_44c929b = []
        for meadow_seg_local_88782b3 in _name_boundary.attributes(_name_boundary.attributes(meadow_self_21814dc.api)['idautils'])['Segments']():
            meadow_buf_local_58688c6 = _name_boundary.attributes(meadow_self_21814dc)['get_seg_data'](meadow_seg_local_88782b3)
            for meadow_parser_03aad39 in (_name_boundary.attributes(meadow_self_21814dc)['parse_C_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_C_16_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_C_32_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_PASCAL_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_PASCAL_16_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_LEN2_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_LEN2_16_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_LEN4_strings'], _name_boundary.attributes(meadow_self_21814dc)['parse_LEN4_16_strings']):
                try:
                    meadow_ret_local_44c929b.extend(list(meadow_parser_03aad39(meadow_seg_local_88782b3, meadow_buf_local_58688c6)))
                except NotImplementedError as meadow_e_7ed83e9:
                    meadow_logger.warning('warning: %s', meadow_e_7ed83e9)
        _name_boundary.attributes(meadow_self_21814dc)['cache'] = meadow_ret_local_44c929b[:]
        return meadow_ret_local_44c929b

    @_name_boundary.callable_contract({'self': 'meadow_self_93e1946', 'strtypes': 'meadow_strtypes_4b344f6', 'minlen': 'meadow_minlen_8667f74', 'only_7bit': 'meadow_only_7bit_62bc55a', 'ignore_instructions': 'meadow_ignore_instructions_0884ce8', 'display_only_existing_strings': 'meadow_display_only_existing_strings_c77458e'}, 'setup')
    def meadow_setup(meadow_self_93e1946, meadow_strtypes_4b344f6=[0], meadow_minlen_8667f74=5, meadow_only_7bit_62bc55a=True, meadow_ignore_instructions_0884ce8=False, meadow_display_only_existing_strings_c77458e=False):
        _name_boundary.attributes(meadow_self_93e1946)['strtypes'] = meadow_strtypes_4b344f6
        _name_boundary.attributes(meadow_self_93e1946)['minlen'] = meadow_minlen_8667f74
        _name_boundary.attributes(meadow_self_93e1946)['only_7bit'] = meadow_only_7bit_62bc55a
        _name_boundary.attributes(meadow_self_93e1946)['ignore_instructions'] = meadow_ignore_instructions_0884ce8
        _name_boundary.attributes(meadow_self_93e1946)['display_only_existing_strings'] = meadow_display_only_existing_strings_c77458e

    @_name_boundary.callable_contract({'self': 'meadow_self_7166a27'}, '__iter__')
    def __iter__(meadow_self_7166a27):
        if _name_boundary.attributes(meadow_self_7166a27)['cache'] is None:
            _name_boundary.attributes(meadow_self_7166a27)['refresh']()
        for meadow_s_local_0b0aae3 in _name_boundary.attributes(meadow_self_7166a27)['cache']:
            yield meadow_s_local_0b0aae3

    @_name_boundary.callable_contract({'self': 'meadow_self_db91609', 'index': 'meadow_index_db39d4d'}, '__getitem__')
    def __getitem__(meadow_self_db91609, meadow_index_db39d4d):
        if _name_boundary.attributes(meadow_self_db91609)['cache'] is None:
            _name_boundary.attributes(meadow_self_db91609)['refresh']()
        return _name_boundary.attributes(meadow_self_db91609)['cache'][meadow_index_db39d4d]

@_name_boundary.class_contract('idautils', {'GetInputFileMD5': 'meadow_GetInputFileMD5', 'Segments': 'meadow_Segments', 'Functions': 'meadow_Functions', 'Chunks': 'meadow_Chunks', 'Heads': 'meadow_Heads', '_get_fallthrough_xref_to': 'meadow__get_fallthrough_xref_to', 'CodeRefsTo': 'meadow_CodeRefsTo', '_get_fallthrough_xref_from': 'meadow__get_fallthrough_xref_from', 'CodeRefsFrom': 'meadow_CodeRefsFrom', 'ALL_DREF_TYPES': 'meadow_ALL_DREF_TYPES', 'ALL_CREF_TYPES': 'meadow_ALL_CREF_TYPES', 'DataRefsFrom': 'meadow_DataRefsFrom', 'DataRefsTo': 'meadow_DataRefsTo', 'XrefsTo': 'meadow_XrefsTo', 'XrefsFrom': 'meadow_XrefsFrom', 'Strings': 'meadow_Strings', 'Names': 'meadow_Names', 'Entries': 'meadow_Entries', 'idb': 'meadow_idb', 'strings': 'meadow_strings'})
class meadow_idautils:

    @_name_boundary.callable_contract({'self': 'meadow_self_254fe25', 'db': 'meadow_db_4e6640d', 'api': 'meadow_api_local_d341a33'}, '__init__')
    def __init__(meadow_self_254fe25, meadow_db_4e6640d, meadow_api_local_d341a33):
        _name_boundary.attributes(meadow_self_254fe25)['idb'] = meadow_db_4e6640d
        meadow_self_254fe25.api = meadow_api_local_d341a33
        _name_boundary.attributes(meadow_self_254fe25)['strings'] = meadow__Strings(meadow_db_4e6640d, meadow_api_local_d341a33)

    @_name_boundary.callable_contract({'self': 'meadow_self_7e18a65'}, 'GetInputFileMD5')
    def meadow_GetInputFileMD5(meadow_self_7e18a65):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_7e18a65.api)['idc'])['GetInputMD5']()

    @_name_boundary.callable_contract({'self': 'meadow_self_de71e3f'}, 'Segments')
    def meadow_Segments(meadow_self_de71e3f):
        return sorted(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](_name_boundary.attributes(meadow_self_de71e3f)['idb']).segments.keys())

    @_name_boundary.callable_contract({'self': 'meadow_self_4ffd584', 'start': 'meadow_start_local_8d85b08', 'end': 'meadow_end_local_4148bbd'}, 'Functions')
    def meadow_Functions(meadow_self_4ffd584, meadow_start_local_8d85b08=None, meadow_end_local_4148bbd=None):
        meadow_ret_local_ef58649 = []
        for meadow_ea_9711b24, meadow_func_7b97899 in _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](_name_boundary.attributes(meadow_self_4ffd584)['idb']).functions.items():
            if meadow_start_local_8d85b08 and meadow_start_local_8d85b08 > meadow_ea_9711b24:
                continue
            if meadow_end_local_4148bbd and meadow_end_local_4148bbd <= meadow_ea_9711b24:
                continue
            if meadow_is_flag_set(meadow_func_7b97899.flags, _name_boundary.attributes(meadow_func_7b97899)['FUNC_TAIL']):
                continue
            meadow_ret_local_ef58649.append(_name_boundary.attributes(meadow_func_7b97899)['startEA'])
        return list(sorted(meadow_ret_local_ef58649))

    @_name_boundary.callable_contract({'self': 'meadow_self_94d8f28', 'fva': 'meadow_fva_824d7b7'}, 'Chunks')
    def meadow_Chunks(meadow_self_94d8f28, meadow_fva_824d7b7):
        try:
            meadow_func_t_2e194bf = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Functions'](_name_boundary.attributes(meadow_self_94d8f28)['idb']).functions[meadow_fva_824d7b7]
        except KeyError:
            meadow_logger.debug('failed to fetch func_t: 0x%x', meadow_fva_824d7b7)
            return
        yield (_name_boundary.attributes(meadow_func_t_2e194bf)['startEA'], _name_boundary.attributes(meadow_func_t_2e194bf)['endEA'])
        try:
            meadow_f_f5a2cae = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Function'](_name_boundary.attributes(meadow_self_94d8f28)['idb'], meadow_fva_824d7b7)
        except KeyError:
            meadow_logger.debug('failed to fetch Function: 0x%x', meadow_fva_824d7b7)
            return
        try:
            for meadow_start_local_e271626, meadow_size_local_1dd374d in _name_boundary.attributes(meadow_f_f5a2cae)['get_chunks']():
                yield (meadow_start_local_e271626, meadow_start_local_e271626 + meadow_size_local_1dd374d)
        except KeyError:
            return

    @_name_boundary.callable_contract({'self': 'meadow_self_2c1d8d8', 'start': 'meadow_start_local_e66a93c', 'end': 'meadow_end_local_20c5eb7'}, 'Heads')
    def meadow_Heads(meadow_self_2c1d8d8, meadow_start_local_e66a93c, meadow_end_local_20c5eb7):
        meadow_ea_79b8a28 = meadow_start_local_e66a93c
        while not _name_boundary.attributes(_name_boundary.attributes(meadow_self_2c1d8d8.api)['ida_bytes'])['is_head'](_name_boundary.attributes(_name_boundary.attributes(meadow_self_2c1d8d8.api)['idc'])['GetFlags'](meadow_ea_79b8a28)):
            meadow_ea_79b8a28 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_2c1d8d8.api)['idc'])['NextHead'](meadow_ea_79b8a28)
            if meadow_ea_79b8a28 >= meadow_end_local_20c5eb7:
                return
        while meadow_ea_79b8a28 != _name_boundary.attributes(_name_boundary.attributes(meadow_self_2c1d8d8.api)['idc'])['BADADDR']:
            yield meadow_ea_79b8a28
            meadow_ea_79b8a28 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_2c1d8d8.api)['idc'])['NextHead'](meadow_ea_79b8a28)
            if meadow_ea_79b8a28 >= meadow_end_local_20c5eb7:
                return

    @_name_boundary.callable_contract({'self': 'meadow_self_a057a0f', 'ea': 'meadow_ea_f919802'}, '_get_fallthrough_xref_to')
    def meadow__get_fallthrough_xref_to(meadow_self_a057a0f, meadow_ea_f919802):
        meadow_flags_local_a33457b = _name_boundary.attributes(_name_boundary.attributes(meadow_self_a057a0f.api)['idc'])['GetFlags'](meadow_ea_f919802)
        if meadow_flags_local_a33457b is None:
            return None
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_a057a0f.api)['ida_bytes'])['is_flow'](meadow_flags_local_a33457b):
            return None
        return _name_boundary.attributes(meadow_idb)['analysis'].Xref(_name_boundary.attributes(_name_boundary.attributes(meadow_self_a057a0f.api)['idc'])['PrevHead'](meadow_ea_f919802), meadow_ea_f919802, 21)

    @_name_boundary.callable_contract({'self': 'meadow_self_6ef1a62', 'ea': 'meadow_ea_345f25b', 'flow': 'meadow_flow_f0bbe49'}, 'CodeRefsTo')
    def meadow_CodeRefsTo(meadow_self_6ef1a62, meadow_ea_345f25b, meadow_flow_f0bbe49):
        if meadow_flow_f0bbe49:
            meadow_ftf_3ebd170 = _name_boundary.attributes(meadow_self_6ef1a62)['_get_fallthrough_xref_to'](meadow_ea_345f25b)
            if meadow_ftf_3ebd170 is not None:
                yield meadow_ftf_3ebd170.frm
        for meadow_xref_531e064 in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_to(_name_boundary.attributes(meadow_self_6ef1a62)['idb'], meadow_ea_345f25b, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F'], _name_boundary.attributes(meadow_idaapi)['fl_CN'], _name_boundary.attributes(meadow_idaapi)['fl_CF']]):
            yield meadow_xref_531e064.frm

    @_name_boundary.callable_contract({'self': 'meadow_self_3f68794', 'ea': 'meadow_ea_f606b2c'}, '_get_fallthrough_xref_from')
    def meadow__get_fallthrough_xref_from(meadow_self_3f68794, meadow_ea_f606b2c):
        meadow_nextea_3a92801 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3f68794.api)['idc'])['NextHead'](meadow_ea_f606b2c)
        meadow_nextflags_a3ec19f = _name_boundary.attributes(_name_boundary.attributes(meadow_self_3f68794.api)['idc'])['GetFlags'](meadow_nextea_3a92801)
        if meadow_nextflags_a3ec19f is None:
            return None
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_3f68794.api)['ida_bytes'])['is_flow'](meadow_nextflags_a3ec19f):
            return None
        return _name_boundary.attributes(meadow_idb)['analysis'].Xref(meadow_ea_f606b2c, meadow_nextea_3a92801, 21)

    @_name_boundary.callable_contract({'self': 'meadow_self_d75510d', 'ea': 'meadow_ea_88639da', 'flow': 'meadow_flow_e986048'}, 'CodeRefsFrom')
    def meadow_CodeRefsFrom(meadow_self_d75510d, meadow_ea_88639da, meadow_flow_e986048):
        if meadow_flow_e986048:
            meadow_ftf_def2893 = _name_boundary.attributes(meadow_self_d75510d)['_get_fallthrough_xref_from'](meadow_ea_88639da)
            if meadow_ftf_def2893 is not None:
                yield meadow_ftf_def2893.to
        for meadow_xref_58be3a9 in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_d75510d)['idb'], meadow_ea_88639da, types=[_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F'], _name_boundary.attributes(meadow_idaapi)['fl_CN'], _name_boundary.attributes(meadow_idaapi)['fl_CF']]):
            yield meadow_xref_58be3a9.to
    meadow_ALL_DREF_TYPES = (_name_boundary.attributes(meadow_idaapi)['dr_U'], _name_boundary.attributes(meadow_idaapi)['dr_O'], _name_boundary.attributes(meadow_idaapi)['dr_W'], _name_boundary.attributes(meadow_idaapi)['dr_R'], _name_boundary.attributes(meadow_idaapi)['dr_T'], _name_boundary.attributes(meadow_idaapi)['dr_I'])
    meadow_ALL_CREF_TYPES = (_name_boundary.attributes(meadow_idaapi)['fl_JN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_F'], _name_boundary.attributes(meadow_idaapi)['fl_CN'], _name_boundary.attributes(meadow_idaapi)['fl_CF'])

    @_name_boundary.callable_contract({'self': 'meadow_self_58f6bbb', 'ea': 'meadow_ea_0ed424c'}, 'DataRefsFrom')
    def meadow_DataRefsFrom(meadow_self_58f6bbb, meadow_ea_0ed424c):
        for meadow_xref_0ae7083 in _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_from(_name_boundary.attributes(meadow_self_58f6bbb)['idb'], meadow_ea_0ed424c, types=_name_boundary.attributes(meadow_self_58f6bbb)['ALL_DREF_TYPES']):
            yield meadow_xref_0ae7083.to

    @_name_boundary.callable_contract({'self': 'meadow_self_e476f82', 'ea': 'meadow_ea_49a4cf1'}, 'DataRefsTo')
    def meadow_DataRefsTo(meadow_self_e476f82, meadow_ea_49a4cf1):
        for meadow_xref_b7b9fb5 in _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_to(_name_boundary.attributes(meadow_self_e476f82)['idb'], meadow_ea_49a4cf1, types=_name_boundary.attributes(meadow_self_e476f82)['ALL_DREF_TYPES']):
            yield meadow_xref_b7b9fb5.frm

    @_name_boundary.callable_contract({'self': 'meadow_self_cff9739', 'ea': 'meadow_ea_f401037', 'flags': 'meadow_flags_local_befe8dc'}, 'XrefsTo')
    def meadow_XrefsTo(meadow_self_cff9739, meadow_ea_f401037, meadow_flags_local_befe8dc=_name_boundary.attributes(meadow_idaapi)['XREF_ALL']):
        if meadow_flags_local_befe8dc == _name_boundary.attributes(meadow_idaapi)['XREF_ALL']:
            meadow_typef_f744062 = _name_boundary.attributes(meadow_self_cff9739)['ALL_CREF_TYPES']
            meadow_typed_0435dfd = _name_boundary.attributes(meadow_self_cff9739)['ALL_DREF_TYPES']
        elif meadow_flags_local_befe8dc == _name_boundary.attributes(meadow_idaapi)['XREF_FAR']:
            meadow_typef_f744062 = [_name_boundary.attributes(meadow_idaapi)['fl_CF'], _name_boundary.attributes(meadow_idaapi)['fl_CN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_JN']]
            meadow_typed_0435dfd = _name_boundary.attributes(meadow_self_cff9739)['ALL_DREF_TYPES']
        elif meadow_flags_local_befe8dc == _name_boundary.attributes(meadow_idaapi)['XREF_DATA']:
            meadow_typef_f744062 = None
            meadow_typed_0435dfd = _name_boundary.attributes(meadow_self_cff9739)['ALL_DREF_TYPES']
        else:
            raise ValueError('unexpected flags value')
        if meadow_typef_f744062:
            for meadow_xref_f2c8edb in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_to(_name_boundary.attributes(meadow_self_cff9739)['idb'], meadow_ea_f401037, meadow_typef_f744062):
                yield meadow_xref_f2c8edb
            if _name_boundary.attributes(meadow_idaapi)['fl_F'] in meadow_typef_f744062:
                meadow_ftf_c33ebde = _name_boundary.attributes(meadow_self_cff9739)['_get_fallthrough_xref_to'](meadow_ea_f401037)
                if meadow_ftf_c33ebde is not None:
                    yield meadow_ftf_c33ebde
        if meadow_typed_0435dfd:
            for meadow_xref_f2c8edb in _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_to(_name_boundary.attributes(meadow_self_cff9739)['idb'], meadow_ea_f401037, meadow_typed_0435dfd):
                yield meadow_xref_f2c8edb

    @_name_boundary.callable_contract({'self': 'meadow_self_7ddfa4c', 'ea': 'meadow_ea_09fa3dd', 'flags': 'meadow_flags_local_8101280'}, 'XrefsFrom')
    def meadow_XrefsFrom(meadow_self_7ddfa4c, meadow_ea_09fa3dd, meadow_flags_local_8101280=_name_boundary.attributes(meadow_idaapi)['XREF_ALL']):
        if meadow_flags_local_8101280 == _name_boundary.attributes(meadow_idaapi)['XREF_ALL']:
            meadow_typef_444eaec = _name_boundary.attributes(meadow_self_7ddfa4c)['ALL_CREF_TYPES']
            meadow_typed_e072c6f = _name_boundary.attributes(meadow_self_7ddfa4c)['ALL_DREF_TYPES']
        elif meadow_flags_local_8101280 == _name_boundary.attributes(meadow_idaapi)['XREF_FAR']:
            meadow_typef_444eaec = [_name_boundary.attributes(meadow_idaapi)['fl_CF'], _name_boundary.attributes(meadow_idaapi)['fl_CN'], _name_boundary.attributes(meadow_idaapi)['fl_JF'], _name_boundary.attributes(meadow_idaapi)['fl_JN']]
            meadow_typed_e072c6f = _name_boundary.attributes(meadow_self_7ddfa4c)['ALL_DREF_TYPES']
        elif meadow_flags_local_8101280 == _name_boundary.attributes(meadow_idaapi)['XREF_DATA']:
            meadow_typef_444eaec = None
            meadow_typed_e072c6f = _name_boundary.attributes(meadow_self_7ddfa4c)['ALL_DREF_TYPES']
        else:
            raise ValueError('unexpected flags value')
        if meadow_typef_444eaec:
            for meadow_xref_29ee662 in _name_boundary.attributes(meadow_idb)['analysis'].get_crefs_from(_name_boundary.attributes(meadow_self_7ddfa4c)['idb'], meadow_ea_09fa3dd, meadow_typef_444eaec):
                yield meadow_xref_29ee662
            if _name_boundary.attributes(meadow_idaapi)['fl_F'] in meadow_typef_444eaec:
                meadow_ftf_ed0acfd = _name_boundary.attributes(meadow_self_7ddfa4c)['_get_fallthrough_xref_from'](meadow_ea_09fa3dd)
                if meadow_ftf_ed0acfd is not None:
                    yield meadow_ftf_ed0acfd
        if meadow_typed_e072c6f:
            for meadow_xref_29ee662 in _name_boundary.attributes(meadow_idb)['analysis'].get_drefs_from(_name_boundary.attributes(meadow_self_7ddfa4c)['idb'], meadow_ea_09fa3dd, meadow_typed_e072c6f):
                yield meadow_xref_29ee662

    @_name_boundary.callable_contract({'self': 'meadow_self_cbf1aa8', 'default_setup': 'meadow_default_setup_f30f70b'}, 'Strings')
    def meadow_Strings(meadow_self_cbf1aa8, meadow_default_setup_f30f70b=False):
        return _name_boundary.attributes(meadow_self_cbf1aa8)['strings']

    @_name_boundary.callable_contract({'self': 'meadow_self_831767c'}, 'Names')
    def meadow_Names(meadow_self_831767c):
        for meadow_i_adb0d50 in range(_name_boundary.attributes(_name_boundary.attributes(meadow_self_831767c.api)['ida_name'])['get_nlist_size']()):
            meadow_ea_63cb599 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_831767c.api)['ida_name'])['get_nlist_ea'](meadow_i_adb0d50)
            meadow_name_local_828c37e = _name_boundary.attributes(_name_boundary.attributes(meadow_self_831767c.api)['ida_name'])['get_nlist_name'](meadow_i_adb0d50)
            yield (meadow_ea_63cb599, meadow_name_local_828c37e)

    @_name_boundary.callable_contract({'self': 'meadow_self_1e05dcb'}, 'Entries')
    def meadow_Entries(meadow_self_1e05dcb):
        for meadow_i_d5257a7 in range(_name_boundary.attributes(_name_boundary.attributes(meadow_self_1e05dcb.api)['ida_entry'])['get_entry_qty']()):
            meadow_ordinal_local_59de68b = _name_boundary.attributes(_name_boundary.attributes(meadow_self_1e05dcb.api)['ida_entry'])['get_entry_ordinal'](meadow_i_d5257a7)
            yield (meadow_i_d5257a7, meadow_ordinal_local_59de68b, _name_boundary.attributes(_name_boundary.attributes(meadow_self_1e05dcb.api)['ida_entry'])['get_entry'](meadow_ordinal_local_59de68b), _name_boundary.attributes(_name_boundary.attributes(meadow_self_1e05dcb.api)['ida_entry'])['get_entry_name'](meadow_ordinal_local_59de68b))

@_name_boundary.class_contract('ida_entry', {'get_entry_qty': 'meadow_get_entry_qty', 'get_entry_ordinal': 'meadow_get_entry_ordinal', 'get_entry': 'meadow_get_entry', 'get_entry_name': 'meadow_get_entry_name', 'get_entry_forwarder': 'meadow_get_entry_forwarder', 'idb': 'meadow_idb'})
class meadow_ida_entry:

    @meadow_wrap_module('idaapi')
    @_name_boundary.callable_contract({'self': 'meadow_self_a9eca1a', 'db': 'meadow_db_894c7ca', 'api': 'meadow_api_local_d863cc3'}, '__init__')
    def __init__(meadow_self_a9eca1a, meadow_db_894c7ca, meadow_api_local_d863cc3):
        _name_boundary.attributes(meadow_self_a9eca1a)['idb'] = meadow_db_894c7ca
        meadow_self_a9eca1a.api = meadow_api_local_d863cc3

    @_name_boundary.callable_contract({'self': 'meadow_self_9a9ceef'}, 'get_entry_qty')
    def meadow_get_entry_qty(meadow_self_9a9ceef):
        meadow_ents_a4d6a85 = _name_boundary.attributes(meadow_idb)['analysis'].EntryPoints(_name_boundary.attributes(meadow_self_9a9ceef)['idb'])
        return len(meadow_ents_a4d6a85.functions) + len(meadow_ents_a4d6a85.main_entry)

    @_name_boundary.callable_contract({'self': 'meadow_self_4f8c167', 'index': 'meadow_index_9d5658c'}, 'get_entry_ordinal')
    def meadow_get_entry_ordinal(meadow_self_4f8c167, meadow_index_9d5658c):
        meadow_ents_37fcddc = _name_boundary.attributes(meadow_idb)['analysis'].EntryPoints(_name_boundary.attributes(meadow_self_4f8c167)['idb'])
        try:
            return meadow_ents_37fcddc.ordinals[meadow_index_9d5658c + 1]
        except KeyError:
            return sorted(meadow_ents_37fcddc.main_entry)[meadow_index_9d5658c - len(meadow_ents_37fcddc.functions) - 1]

    @_name_boundary.callable_contract({'self': 'meadow_self_42c8b70', 'ordinal': 'meadow_ordinal_local_023f222'}, 'get_entry')
    def meadow_get_entry(meadow_self_42c8b70, meadow_ordinal_local_023f222):
        meadow_ents_88896c5 = _name_boundary.attributes(meadow_idb)['analysis'].EntryPoints(_name_boundary.attributes(meadow_self_42c8b70)['idb'])
        return meadow_ents_88896c5.functions[meadow_ordinal_local_023f222]

    @_name_boundary.callable_contract({'self': 'meadow_self_8b4e087', 'ordinal': 'meadow_ordinal_local_cfa258b'}, 'get_entry_name')
    def meadow_get_entry_name(meadow_self_8b4e087, meadow_ordinal_local_cfa258b):
        meadow_ents_c275884 = _name_boundary.attributes(meadow_idb)['analysis'].EntryPoints(_name_boundary.attributes(meadow_self_8b4e087)['idb'])
        try:
            return meadow_ents_c275884.function_names[meadow_ordinal_local_cfa258b]
        except KeyError:
            return meadow_ents_c275884.main_entry_name[meadow_ordinal_local_cfa258b]

    @_name_boundary.callable_contract({'self': 'meadow_self_77367c1', 'ordinal': 'meadow_ordinal_local_881bca7'}, 'get_entry_forwarder')
    def meadow_get_entry_forwarder(meadow_self_77367c1, meadow_ordinal_local_881bca7):
        meadow_ents_39724ac = _name_boundary.attributes(meadow_idb)['analysis'].EntryPoints(_name_boundary.attributes(meadow_self_77367c1)['idb'])
        return _name_boundary.attributes(meadow_ents_39724ac.forwarded_symbols)['get'](meadow_ordinal_local_881bca7)

@_name_boundary.class_contract('ida_name', {'get_name': 'meadow_get_name', '_get_name_ptrs': 'meadow__get_name_ptrs', 'get_nlist_size': 'meadow_get_nlist_size', 'get_nlist_ea': 'meadow_get_nlist_ea', 'get_nlist_name': 'meadow_get_nlist_name', 'idb': 'meadow_idb'})
class meadow_ida_name:

    @meadow_wrap_module('idaapi')
    @_name_boundary.callable_contract({'self': 'meadow_self_5b3ebf0', 'db': 'meadow_db_4da2031', 'api': 'meadow_api_local_59f503b'}, '__init__')
    def __init__(meadow_self_5b3ebf0, meadow_db_4da2031, meadow_api_local_59f503b):
        _name_boundary.attributes(meadow_self_5b3ebf0)['idb'] = meadow_db_4da2031
        meadow_self_5b3ebf0.api = meadow_api_local_59f503b

    @_name_boundary.callable_contract({'self': 'meadow_self_67d6f85', 'ea': 'meadow_ea_d0ec034'}, 'get_name')
    def meadow_get_name(meadow_self_67d6f85, meadow_ea_d0ec034):
        meadow_flags_local_a9b8669 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['ida_bytes'])['get_flags'](meadow_ea_d0ec034)
        if not _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['ida_bytes'])['has_name'](meadow_flags_local_a9b8669):
            meadow_func_d9fbf07 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['ida_funcs'])['get_func'](meadow_ea_d0ec034)
            if meadow_func_d9fbf07 and _name_boundary.attributes(meadow_func_d9fbf07)['startEA'] == meadow_ea_d0ec034:
                return _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['ida_funcs'])['get_func_name'](meadow_ea_d0ec034)
            meadow_refs_843a1e5 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['idautils'])['CodeRefsTo'](meadow_ea_d0ec034, 0)
            if next(meadow_refs_843a1e5, None):
                return 'loc_%X' % meadow_ea_d0ec034
            return ''
        try:
            meadow_nn_9616b4f = _name_boundary.attributes(_name_boundary.attributes(meadow_self_67d6f85.api)['ida_netnode'])['netnode'](meadow_ea_d0ec034)
            return meadow_nn_9616b4f.name()
        except KeyError:
            return ''

    @meadow_memoized_method()
    @_name_boundary.callable_contract({'self': 'meadow_self_079ca7b'}, '_get_name_ptrs')
    def meadow__get_name_ptrs(meadow_self_079ca7b):
        """
        a wrapper for the NAM section parser that caches the results on first access.
        """
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_079ca7b)['idb'].nam)['names']()

    @_name_boundary.callable_contract({'self': 'meadow_self_72b9526'}, 'get_nlist_size')
    def meadow_get_nlist_size(meadow_self_72b9526):
        return _name_boundary.attributes(meadow_self_72b9526)['idb'].nam.name_count

    @_name_boundary.callable_contract({'self': 'meadow_self_2fd75fb', 'i': 'meadow_i_d1d0af1'}, 'get_nlist_ea')
    def meadow_get_nlist_ea(meadow_self_2fd75fb, meadow_i_d1d0af1):
        return _name_boundary.attributes(meadow_self_2fd75fb)['_get_name_ptrs']()[meadow_i_d1d0af1]

    @_name_boundary.callable_contract({'self': 'meadow_self_2e2d2c8', 'i': 'meadow_i_39b02d7'}, 'get_nlist_name')
    def meadow_get_nlist_name(meadow_self_2e2d2c8, meadow_i_39b02d7):
        meadow_ea_8a1f386 = _name_boundary.attributes(meadow_self_2e2d2c8)['get_nlist_ea'](meadow_i_39b02d7)
        return _name_boundary.attributes(meadow_self_2e2d2c8)['get_name'](meadow_ea_8a1f386)

@_name_boundary.class_contract('ida_struct', {'_load_structs': 'meadow__load_structs', 'get_member_by_fullname': 'meadow_get_member_by_fullname', 'get_member_by_id': 'meadow_get_member_by_id', 'get_member_by_name': 'meadow_get_member_by_name', 'get_member_cmt': 'meadow_get_member_cmt', 'get_member_fullname': 'meadow_get_member_fullname', 'get_member_name': 'meadow_get_member_name', 'get_member_size': 'meadow_get_member_size', 'get_member_struc': 'meadow_get_member_struc', 'get_member_tinfo': 'meadow_get_member_tinfo', 'get_struc_id': 'meadow_get_struc_id', 'get_first_struc_idx': 'meadow_get_first_struc_idx', 'get_last_struc_idx': 'meadow_get_last_struc_idx', 'get_struc': 'meadow_get_struc', 'get_struc_by_idx': 'meadow_get_struc_by_idx', 'get_struc_name': 'meadow_get_struc_name', 'get_struc_idx': 'meadow_get_struc_idx', 'idb': 'meadow_idb', '_struct_ids': 'meadow__struct_ids'})
class meadow_ida_struct:

    @_name_boundary.callable_contract({'self': 'meadow_self_604577d', 'db': 'meadow_db_8902879', 'api': 'meadow_api_local_16c95f0'}, '__init__')
    def __init__(meadow_self_604577d, meadow_db_8902879, meadow_api_local_16c95f0):
        _name_boundary.attributes(meadow_self_604577d)['idb'] = meadow_db_8902879
        meadow_self_604577d.api = meadow_api_local_16c95f0
        _name_boundary.attributes(meadow_self_604577d)['_struct_ids'] = []
        _name_boundary.attributes(meadow_self_604577d)['_load_structs']()

    @_name_boundary.callable_contract({'self': 'meadow_self_867ff9d'}, '_load_structs')
    def meadow__load_structs(meadow_self_867ff9d):
        meadow_node_a2ca370 = meadow_Netnode(_name_boundary.attributes(meadow_self_867ff9d)['idb'], '$ structs')
        for meadow_entry_local_2707ea6 in _name_boundary.attributes(meadow_node_a2ca370)['altentries']():
            _name_boundary.attributes(meadow_self_867ff9d)['_struct_ids'].append(_name_boundary.attributes(meadow_idb)['netnode'].as_uint(meadow_entry_local_2707ea6.value) - 1)

    @_name_boundary.callable_contract({'self': 'meadow_self_9ac105f', 'fullname': 'meadow_fullname_95a716f'}, 'get_member_by_fullname')
    def meadow_get_member_by_fullname(meadow_self_9ac105f, meadow_fullname_95a716f):
        """Get a member by its fully qualified name, "struct.field"."""
        return meadow_StructMember(_name_boundary.attributes(meadow_self_9ac105f)['idb'], meadow_fullname_95a716f)

    @_name_boundary.callable_contract({'self': 'meadow_self_d6ec679', 'mid': 'meadow_mid_bad5d96'}, 'get_member_by_id')
    def meadow_get_member_by_id(meadow_self_d6ec679, meadow_mid_bad5d96):
        """Check if the specified member id points to a struct member."""
        return meadow_StructMember(_name_boundary.attributes(meadow_self_d6ec679)['idb'], meadow_mid_bad5d96)

    @_name_boundary.callable_contract({'self': 'meadow_self_5938085', 'sptr': 'meadow_sptr_4ff30ea', 'membername': 'meadow_membername_2dba63c'}, 'get_member_by_name')
    def meadow_get_member_by_name(meadow_self_5938085, meadow_sptr_4ff30ea, meadow_membername_2dba63c):
        """Get a member by its name, like "field44"."""
        return _name_boundary.attributes(meadow_sptr_4ff30ea)['find_member_by_name'](meadow_membername_2dba63c)

    @_name_boundary.callable_contract({'self': 'meadow_self_4c79787', 'mid': 'meadow_mid_012d299', 'repeatable': 'meadow_repeatable_e01a550'}, 'get_member_cmt')
    def meadow_get_member_cmt(meadow_self_4c79787, meadow_mid_012d299, meadow_repeatable_e01a550):
        """Get comment of structure member."""
        meadow_m_bf85eeb = _name_boundary.attributes(meadow_self_4c79787)['get_member_by_id'](meadow_mid_012d299)
        if meadow_repeatable_e01a550:
            return _name_boundary.attributes(meadow_m_bf85eeb)['get_repeatable_member_comment']()
        else:
            return _name_boundary.attributes(meadow_m_bf85eeb)['get_member_comment']()

    @_name_boundary.callable_contract({'self': 'meadow_self_5b22093', 'mid': 'meadow_mid_451d6a1'}, 'get_member_fullname')
    def meadow_get_member_fullname(meadow_self_5b22093, meadow_mid_451d6a1):
        """Get a member's fully qualified name, "struct.field"."""
        meadow_m_51451e4 = _name_boundary.attributes(meadow_self_5b22093)['get_member_by_id'](meadow_mid_451d6a1)
        return _name_boundary.attributes(meadow_m_51451e4)['get_fullname']()

    @_name_boundary.callable_contract({'self': 'meadow_self_5505ac4', 'mid': 'meadow_mid_ff805e5'}, 'get_member_name')
    def meadow_get_member_name(meadow_self_5505ac4, meadow_mid_ff805e5):
        """Get name of structure member."""
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_5505ac4)['get_member_by_id'](meadow_mid_ff805e5))['get_name']()

    @_name_boundary.callable_contract({'self': 'meadow_self_8f0626b', 'nonnul_mptr': 'meadow_nonnul_mptr_ff0a7f5'}, 'get_member_size')
    def meadow_get_member_size(meadow_self_8f0626b, meadow_nonnul_mptr_ff0a7f5):
        """Get size of structure member."""
        meadow_tinfo_1473074 = _name_boundary.attributes(meadow_self_8f0626b)['get_member_tinfo'](meadow_nonnul_mptr_ff0a7f5)
        if not meadow_tinfo_1473074:
            return None
        else:
            return _name_boundary.attributes(meadow_tinfo_1473074)['get_size']()

    @_name_boundary.callable_contract({'self': 'meadow_self_3132677', 'fullname': 'meadow_fullname_2d1c849'}, 'get_member_struc')
    def meadow_get_member_struc(meadow_self_3132677, meadow_fullname_2d1c849):
        """Get containing structure of member by its full name "struct.field"."""
        return meadow_Struct(_name_boundary.attributes(meadow_self_3132677)['idb'], meadow_fullname_2d1c849)

    @_name_boundary.callable_contract({'self': 'meadow_self_2448f81', 'mptr': 'meadow_mptr_7c1dda7'}, 'get_member_tinfo')
    def meadow_get_member_tinfo(meadow_self_2448f81, meadow_mptr_7c1dda7):
        """Get tinfo for given member."""
        meadow__type_local_b34b555 = _name_boundary.attributes(meadow_mptr_7c1dda7)['get_typeinfo']()
        if not meadow__type_local_b34b555:
            return None
        meadow_ordinal_local_b7d6722 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_2448f81.api)['ida_typeinf'])['get_ordinal_from_idb_type'](_name_boundary.attributes(meadow_mptr_7c1dda7)['get_name'](), meadow__type_local_b34b555)
        if meadow_ordinal_local_b7d6722 == -1:
            return None
        else:
            return _name_boundary.attributes(_name_boundary.attributes(meadow_self_2448f81.api)['ida_typeinf'])['get_numbered_type'](meadow_ordinal_local_b7d6722)

    @_name_boundary.callable_contract({'self': 'meadow_self_5c86d8c', 'name': 'meadow_name_local_4d8767a'}, 'get_struc_id')
    def meadow_get_struc_id(meadow_self_5c86d8c, meadow_name_local_4d8767a):
        """Get struct id by name."""
        return _name_boundary.attributes(meadow_Struct(_name_boundary.attributes(meadow_self_5c86d8c)['idb'], meadow_name_local_4d8767a))['nodeid']

    @_name_boundary.callable_contract({'self': 'meadow_self_5a9ad3e'}, 'get_first_struc_idx')
    def meadow_get_first_struc_idx(meadow_self_5a9ad3e):
        return 0 if len(_name_boundary.attributes(meadow_self_5a9ad3e)['_struct_ids']) > 0 else _name_boundary.attributes(_name_boundary.attributes(meadow_self_5a9ad3e.api)['idc'])['BADADDR']

    @_name_boundary.callable_contract({'self': 'meadow_self_db51a52'}, 'get_last_struc_idx')
    def meadow_get_last_struc_idx(meadow_self_db51a52):
        return _name_boundary.attributes(meadow_self_db51a52)['_struct_ids'][-1] if len(_name_boundary.attributes(meadow_self_db51a52)['_struct_ids']) > 0 else _name_boundary.attributes(_name_boundary.attributes(meadow_self_db51a52.api)['idc'])['BADADDR']

    @_name_boundary.callable_contract({'self': 'meadow_self_045e124', 'id': 'meadow_id_local_4aa969a'}, 'get_struc')
    def meadow_get_struc(meadow_self_045e124, meadow_id_local_4aa969a):
        """Get pointer to struct type info."""
        return meadow_Struct(_name_boundary.attributes(meadow_self_045e124)['idb'], meadow_id_local_4aa969a)

    @_name_boundary.callable_contract({'self': 'meadow_self_512203f', 'idx': 'meadow_idx_122ec22'}, 'get_struc_by_idx')
    def meadow_get_struc_by_idx(meadow_self_512203f, meadow_idx_122ec22):
        return meadow_Struct(_name_boundary.attributes(meadow_self_512203f)['idb'], _name_boundary.attributes(meadow_self_512203f)['_struct_ids'][meadow_idx_122ec22])

    @_name_boundary.callable_contract({'self': 'meadow_self_e3f3588', 'id': 'meadow_id_local_4bb5442', 'flags': 'meadow_flags_local_aaa9bca'}, 'get_struc_name')
    def meadow_get_struc_name(meadow_self_e3f3588, meadow_id_local_4bb5442, meadow_flags_local_aaa9bca=0):
        """Get struct name by id"""
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_e3f3588)['get_struc'](meadow_id_local_4bb5442))['get_name']()

    @_name_boundary.callable_contract({'self': 'meadow_self_103288a', 'id': 'meadow_id_local_f743f25'}, 'get_struc_idx')
    def meadow_get_struc_idx(meadow_self_103288a, meadow_id_local_f743f25):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_103288a)['_struct_ids'])['index'](meadow_id_local_f743f25)

    @_name_boundary.callable_contract({'self': 'meadow_self_7214485', 'name': 'meadow_name_local_b7fae7a'}, 'get_struc_id')
    def meadow_get_struc_id(meadow_self_7214485, meadow_name_local_b7fae7a):
        return _name_boundary.attributes(meadow_Netnode(_name_boundary.attributes(meadow_self_7214485)['idb'], meadow_name_local_b7fae7a))['nodeid']

@_name_boundary.class_contract('ida_typeinf', {'get_named_type': 'meadow_get_named_type', 'get_type_flags': 'meadow_get_type_flags', 'get_base_flags': 'meadow_get_base_flags', 'get_numbered_type': 'meadow_get_numbered_type', 'get_ordinal_from_idb_type': 'meadow_get_ordinal_from_idb_type', 'idb': 'meadow_idb', 'types': 'meadow_types'})
class meadow_ida_typeinf:

    @_name_boundary.callable_contract({'self': 'meadow_self_d5ee6fc', 'db': 'meadow_db_b7e459b', 'api': 'meadow_api_local_43302e2'}, '__init__')
    def __init__(meadow_self_d5ee6fc, meadow_db_b7e459b, meadow_api_local_43302e2):
        _name_boundary.attributes(meadow_self_d5ee6fc)['idb'] = meadow_db_b7e459b
        meadow_self_d5ee6fc.api = meadow_api_local_43302e2
        _name_boundary.attributes(meadow_self_d5ee6fc)['types'] = _name_boundary.attributes(meadow_db_b7e459b.til)['types']

    @_name_boundary.callable_contract({'self': 'meadow_self_5f4bd4d', 'ntf_flags': 'meadow_ntf_flags_b0ae009', 'name': 'meadow_name_local_3380096'}, 'get_named_type')
    def meadow_get_named_type(meadow_self_5f4bd4d, meadow_name_local_3380096, meadow_ntf_flags_b0ae009=None):
        """Get a type data by its name."""
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_5f4bd4d)['types'])['find_by_name'](meadow_name_local_3380096)

    @_name_boundary.callable_contract({'self': 'meadow_self_2ed0ab2', 't': 'meadow_t_b3af6f8'}, 'get_type_flags')
    def meadow_get_type_flags(meadow_self_2ed0ab2, meadow_t_b3af6f8):
        """Get type flags ( 'TYPE_FLAGS_MASK' )"""
        return _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['typeinf'])['get_type_flags'](meadow_t_b3af6f8)

    @_name_boundary.callable_contract({'self': 'meadow_self_9889525', 't': 'meadow_t_6a0e255'}, 'get_base_flags')
    def meadow_get_base_flags(meadow_self_9889525, meadow_t_6a0e255):
        return _name_boundary.attributes(meadow_idb)['typeinf'].get_base_type(meadow_t_6a0e255)

    @_name_boundary.callable_contract({'self': 'meadow_self_45e773b', 'ordinal': 'meadow_ordinal_local_2564f8a'}, 'get_numbered_type')
    def meadow_get_numbered_type(meadow_self_45e773b, meadow_ordinal_local_2564f8a):
        """Get type ordinal by its name."""
        if 0 < meadow_ordinal_local_2564f8a < len(_name_boundary.attributes(meadow_self_45e773b)['types']):
            return _name_boundary.attributes(meadow_self_45e773b)['types'][meadow_ordinal_local_2564f8a]
        else:
            return None

    @_name_boundary.callable_contract({'self': 'meadow_self_df81ea3', 'name': 'meadow_name_local_4578404', '_type': 'meadow__type_local_216b07c'}, 'get_ordinal_from_idb_type')
    def meadow_get_ordinal_from_idb_type(meadow_self_df81ea3, meadow_name_local_4578404, meadow__type_local_216b07c):
        """Get ordinal number of an idb type (struct/enum).
        The 'type' parameter is used only to determine the kind of the type (struct or enum).
        Use this function to find out the correspondence between idb types and til types"""
        if not meadow__type_local_216b07c or len(meadow__type_local_216b07c) == 0:
            return -1
        meadow_typ_local_0882351 = _name_boundary.attributes(meadow_self_df81ea3)['get_named_type'](meadow_name_local_4578404)
        if _name_boundary.attributes(meadow_self_df81ea3)['get_base_flags'](_name_boundary.attributes(meadow_typ_local_0882351.type)['base_type']) == _name_boundary.attributes(meadow_self_df81ea3)['get_base_flags'](ord(meadow__type_local_216b07c[0])):
            return meadow_typ_local_0882351.ordinal
        else:
            return -1

@_name_boundary.class_contract('IDAPython', {'idb': 'meadow_idb', 'ScreenEA': 'meadow_ScreenEA', 'idc': 'meadow_idc', 'idaapi': 'meadow_idaapi', 'idautils': 'meadow_idautils', 'ida_ida': 'meadow_ida_ida', 'ida_funcs': 'meadow_ida_funcs', 'ida_bytes': 'meadow_ida_bytes', 'ida_netnode': 'meadow_ida_netnode', 'ida_nalt': 'meadow_ida_nalt', 'ida_entry': 'meadow_ida_entry', 'ida_name': 'meadow_ida_name', 'ida_struct': 'meadow_ida_struct', 'ida_typeinf': 'meadow_ida_typeinf', 'ida_ua': 'meadow_ida_ua'})
class meadow_IDAPython:

    @_name_boundary.callable_contract({'self': 'meadow_self_73c84ae', 'db': 'meadow_db_426af32', 'ScreenEA': 'meadow_ScreenEA_51c81d6'}, '__init__')
    def __init__(meadow_self_73c84ae, meadow_db_426af32, meadow_ScreenEA_51c81d6=None):
        _name_boundary.attributes(meadow_self_73c84ae)['idb'] = meadow_db_426af32
        _name_boundary.attributes(meadow_self_73c84ae)['ScreenEA'] = meadow_ScreenEA_51c81d6
        _name_boundary.attributes(meadow_self_73c84ae)['idc'] = meadow_idc(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['idaapi'] = meadow_idaapi(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['idautils'] = meadow_idautils(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_ida'] = meadow_ida_ida(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_funcs'] = meadow_ida_funcs(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_bytes'] = meadow_ida_bytes(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_netnode'] = meadow_ida_netnode(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_nalt'] = meadow_ida_nalt(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_entry'] = meadow_ida_entry(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_name'] = meadow_ida_name(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_struct'] = meadow_ida_struct(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_typeinf'] = meadow_ida_typeinf(meadow_db_426af32, meadow_self_73c84ae)
        _name_boundary.attributes(meadow_self_73c84ae)['ida_ua'] = meadow_ida_ua(meadow_db_426af32, meadow_self_73c84ae)
_name_boundary.module_contract(globals(), {'BasicBlock': 'meadow_BasicBlock', 'ida_struct': 'meadow_ida_struct', 'is_flag_set': 'meadow_is_flag_set', 're': 'meadow_re', 'idc': 'meadow_idc', 'IDAPython': 'meadow_IDAPython', 'idaapi': 'meadow_idaapi', 'ida_ida': 'meadow_ida_ida', 'os': 'meadow_os', 'logger': 'meadow_logger', 'collections': 'meadow_collections', 'Struct': 'meadow_Struct', 'is_empty': 'meadow_is_empty', 'wrap_module': 'meadow_wrap_module', 'ida_bytes': 'meadow_ida_bytes', 'ida_entry': 'meadow_ida_entry', 'ida_netnode': 'meadow_ida_netnode', 'AFLAGS': 'meadow_AFLAGS', 'memoized_method': 'meadow_memoized_method', 'StringItem': 'meadow_StringItem', '_Strings': 'meadow__Strings', 'weakref': 'meadow_weakref', 'ida_nalt': 'meadow_ida_nalt', 'ida_name': 'meadow_ida_name', 'ida_typeinf': 'meadow_ida_typeinf', 'StructMember': 'meadow_StructMember', 'six': 'meadow_six', 'logging': 'meadow_logging', 'idb': 'meadow_idb', 'Netnode': 'meadow_Netnode', 'TIL': 'meadow_TIL', 'ida_ua': 'meadow_ida_ua', 'ida_funcs': 'meadow_ida_funcs', 'idautils': 'meadow_idautils', 'FLAGS': 'meadow_FLAGS', 'functools': 'meadow_functools', 'struct': 'meadow_struct'})
