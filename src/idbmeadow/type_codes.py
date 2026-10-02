# Derived from idb/typeinf_flags.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
meadow_RESERVED_BYTE = 255
meadow_TYPE_BASE_MASK = 15
meadow_TYPE_FLAGS_MASK = 48
meadow_TYPE_MODIF_MASK = 192
meadow_TYPE_FULL_MASK = meadow_TYPE_BASE_MASK | meadow_TYPE_FLAGS_MASK
meadow_BT_UNK = 0
meadow_BT_VOID = 1
meadow_BTMT_SIZE0 = 0
meadow_BTMT_SIZE12 = 16
meadow_BTMT_SIZE48 = 32
meadow_BTMT_SIZE128 = 48
meadow_BT_INT8 = 2
meadow_BT_INT16 = 3
meadow_BT_INT32 = 4
meadow_BT_INT64 = 5
meadow_BT_INT128 = 6
meadow_BT_INT = 7
meadow_BTMT_UNKSIGN = 0
meadow_BTMT_SIGNED = 16
meadow_BTMT_USIGNED = 32
meadow_BTMT_UNSIGNED = meadow_BTMT_USIGNED
meadow_BTMT_CHAR = 48
meadow_BT_BOOL = 8
meadow_BTMT_DEFBOOL = 0
meadow_BTMT_BOOL1 = 16
meadow_BTMT_BOOL2 = 32
meadow_BTMT_BOOL4 = 48
meadow_BT_FLOAT = 9
meadow_BTMT_FLOAT = 0
meadow_BTMT_DOUBLE = 16
meadow_BTMT_LNGDBL = 32
meadow_BTMT_SPECFLT = 48
meadow__BT_LAST_BASIC = meadow_BT_FLOAT
meadow_BT_PTR = 10
meadow_BTMT_DEFPTR = 0
meadow_BTMT_NEAR = 16
meadow_BTMT_FAR = 32
meadow_BTMT_CLOSURE = 48
meadow_BT_ARRAY = 11
meadow_BTMT_NONBASED = 16
meadow_BTMT_ARRESERV = 32
meadow_BT_FUNC = 12
meadow_BTMT_DEFCALL = 0
meadow_BTMT_NEARCALL = 16
meadow_BTMT_FARCALL = 32
meadow_BTMT_INTCALL = 48
meadow_BT_COMPLEX = 13
meadow_BTMT_STRUCT = 0
meadow_BTMT_UNION = 16
meadow_BTMT_ENUM = 32
meadow_BTMT_TYPEDEF = 48
meadow_BT_BITFIELD = 14
meadow_BTMT_BFLDI8 = 0
meadow_BTMT_BFLDI16 = 16
meadow_BTMT_BFLDI32 = 32
meadow_BTMT_BFLDI64 = 48
meadow_BT_RESERVED = 15
meadow_BTM_CONST = 64
meadow_BTM_VOLATILE = 128
meadow_BTE_SIZE_MASK = 7
meadow_BTE_RESERVED = 8
meadow_BTE_BITFIELD = 16
meadow_BTE_OUT_MASK = 96
meadow_BTE_HEX = 0
meadow_BTE_CHAR = 32
meadow_BTE_SDEC = 64
meadow_BTE_UDEC = 96
meadow_BTE_ALWAYS = 128
meadow_BT_SEGREG = meadow_BT_INT | meadow_BTMT_CHAR
meadow_BT_UNK_BYTE = meadow_BT_VOID | meadow_BTMT_SIZE12
meadow_BT_UNK_WORD = meadow_BT_UNK | meadow_BTMT_SIZE12
meadow_BT_UNK_DWORD = meadow_BT_VOID | meadow_BTMT_SIZE48
meadow_BT_UNK_QWORD = meadow_BT_UNK | meadow_BTMT_SIZE48
meadow_BT_UNK_OWORD = meadow_BT_VOID | meadow_BTMT_SIZE128
meadow_BT_UNKNOWN = meadow_BT_UNK | meadow_BTMT_SIZE128
meadow_BTF_BYTE = meadow_BT_UNK_BYTE
meadow_BTF_UNK = meadow_BT_UNKNOWN
meadow_BTF_VOID = meadow_BT_VOID | meadow_BTMT_SIZE0
meadow_BTF_INT8 = meadow_BT_INT8 | meadow_BTMT_SIGNED
meadow_BTF_CHAR = meadow_BT_INT8 | meadow_BTMT_CHAR
meadow_BTF_UCHAR = meadow_BT_INT8 | meadow_BTMT_USIGNED
meadow_BTF_UINT8 = meadow_BT_INT8 | meadow_BTMT_USIGNED
meadow_BTF_INT16 = meadow_BT_INT16 | meadow_BTMT_SIGNED
meadow_BTF_UINT16 = meadow_BT_INT16 | meadow_BTMT_USIGNED
meadow_BTF_INT32 = meadow_BT_INT32 | meadow_BTMT_SIGNED
meadow_BTF_UINT32 = meadow_BT_INT32 | meadow_BTMT_USIGNED
meadow_BTF_INT64 = meadow_BT_INT64 | meadow_BTMT_SIGNED
meadow_BTF_UINT64 = meadow_BT_INT64 | meadow_BTMT_USIGNED
meadow_BTF_INT128 = meadow_BT_INT128 | meadow_BTMT_SIGNED
meadow_BTF_UINT128 = meadow_BT_INT128 | meadow_BTMT_USIGNED
meadow_BTF_INT = meadow_BT_INT | meadow_BTMT_UNKSIGN
meadow_BTF_UINT = meadow_BT_INT | meadow_BTMT_USIGNED
meadow_BTF_SINT = meadow_BT_INT | meadow_BTMT_SIGNED
meadow_BTF_BOOL = meadow_BT_BOOL
meadow_BTF_FLOAT = meadow_BT_FLOAT | meadow_BTMT_FLOAT
meadow_BTF_DOUBLE = meadow_BT_FLOAT | meadow_BTMT_DOUBLE
meadow_BTF_LDOUBLE = meadow_BT_FLOAT | meadow_BTMT_LNGDBL
meadow_BTF_TBYTE = meadow_BT_FLOAT | meadow_BTMT_SPECFLT
meadow_BTF_STRUCT = meadow_BT_COMPLEX | meadow_BTMT_STRUCT
meadow_BTF_UNION = meadow_BT_COMPLEX | meadow_BTMT_UNION
meadow_BTF_ENUM = meadow_BT_COMPLEX | meadow_BTMT_ENUM
meadow_BTF_TYPEDEF = meadow_BT_COMPLEX | meadow_BTMT_TYPEDEF
meadow_TAH_BYTE = 254
meadow_FAH_BYTE = 255
meadow_TAH_HASATTRS = 16
meadow_CM_MASK = 3
meadow_CM_UNKNOWN = 0
meadow_CM_N8_F16 = 1
meadow_CM_N64 = 1
meadow_CM_N16_F32 = 2
meadow_CM_N32_F48 = 3
meadow_CM_M_MASK = 12
meadow_CM_M_MN = 0
meadow_CM_M_FF = 4
meadow_CM_M_NF = 8
meadow_CM_M_FN = 12
meadow_CM_CC_MASK = 240
meadow_CM_CC_INVALID = 0
meadow_CM_CC_UNKNOWN = 16
meadow_CM_CC_VOIDARG = 32
meadow_CM_CC_CDECL = 48
meadow_CM_CC_ELLIPSIS = 64
meadow_CM_CC_STDCALL = 80
meadow_CM_CC_PASCAL = 96
meadow_CM_CC_FASTCALL = 112
meadow_CM_CC_THISCALL = 128
meadow_CM_CC_MANUAL = 144
meadow_CM_CC_SPOILED = 160
meadow_CM_CC_RESERVE4 = 176
meadow_CM_CC_RESERVE3 = 192
meadow_CM_CC_SPECIALE = 208
meadow_CM_CC_SPECIALP = 224
meadow_CM_CC_SPECIAL = 240
meadow_ALOC_NONE = 0
meadow_ALOC_STACK = 1
meadow_ALOC_DIST = 2
meadow_ALOC_REG1 = 3
meadow_ALOC_REG2 = 4
meadow_ALOC_RREL = 5
meadow_ALOC_STATIC = 6
meadow_ALOC_CUSTOM = 7
meadow_REGS_METAPC = ['eax', 'ecx', 'edx', 'ebx', 'esp', 'ebp', 'esi', 'edi', 'er8', 'er9', 'er10', 'er11', 'er12', 'er13', 'er14', 'er15', 'al', 'cl', 'dl', 'bl', 'ah', 'ch', 'dh', 'bh', 'spl', 'bpl', 'sil', 'dil', 'eip', 'ees', 'ecs', 'ess', 'eds', 'efs', 'egs', 'cf', 'zf', 'sf', 'of', 'epf', 'eaf', 'etf', 'eif', 'edf', 'eefl', 'st0', 'st1', 'st2', 'st3', 'st4', 'st5', 'st6', 'st7', 'fpctrl', 'fpstat', 'fptags', 'mm0', 'mm1', 'mm2', 'mm3', 'mm4', 'mm5', 'mm6', 'mm7', 'xmm0', 'xmm1', 'xmm2', 'xmm3', 'xmm4', 'xmm5', 'xmm6', 'xmm7', 'xmm8', 'xmm9', 'xmm10', 'xmm11', 'xmm12', 'xmm13', 'xmm14', 'xmm15', 'mxcsr', 'ymm0', 'ymm1', 'ymm2', 'ymm3', 'ymm4', 'ymm5', 'ymm6', 'ymm7', 'ymm8', 'ymm9', 'ymm10', 'ymm11', 'ymm12', 'ymm13', 'ymm14', 'ymm15', 'bnd0', 'bnd1', 'bnd2', 'bnd3', 'xmm16', 'xmm17', 'xmm18', 'xmm19', 'xmm20', 'xmm21', 'xmm22', 'xmm23', 'xmm24', 'xmm25', 'xmm26', 'xmm27', 'xmm28', 'xmm29', 'xmm30', 'xmm31', 'ymm16', 'ymm17', 'ymm18', 'ymm19', 'ymm20', 'ymm21', 'ymm22', 'ymm23', 'ymm24', 'ymm25', 'ymm26', 'ymm27', 'ymm28', 'ymm29', 'ymm30', 'ymm31', 'zmm0', 'zmm1', 'zmm2', 'zmm3', 'zmm4', 'zmm5', 'zmm6', 'zmm7', 'zmm8', 'zmm9', 'zmm10', 'zmm11', 'zmm12', 'zmm13', 'zmm14', 'zmm15', 'zmm16', 'zmm17', 'zmm18', 'zmm19', 'zmm20', 'zmm21', 'zmm22', 'zmm23', 'zmm24', 'zmm25', 'zmm26', 'zmm27', 'zmm28', 'zmm29', 'zmm30', 'zmm31', 'k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7']
meadow_REGS_ARM = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'SP', 'LR', 'PC', 'CPSR', 'CPSR_flg', 'SPSR', 'SPSR_flg', 'T', 'CS', 'DS', 'acc0', 'FPSID', 'FPSCR', 'FPEXC', 'FPINST', 'FPINST2', 'MVFR0', 'MVFR1', 'APSR', 'IAPSR', 'EAPSR', 'XPSR', 'IPSR', 'EPSR', 'IEPSR', 'MSP', 'PSP', 'PRIMASK', 'BASEPRI', 'BASEPRI_MAX', 'FAULTMASK', 'CONTROL', 'Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'CF', 'ZF', 'NF', 'VF', 'X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'X23', 'X24', 'X25', 'X26', 'X27', 'X28', 'X29', 'X30', 'XZR', 'SP', 'PC', 'V0', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31']
meadow_REGS = {'metapc': meadow_REGS_METAPC, 'ARM': meadow_REGS_ARM}

@_name_boundary.callable_contract({'t': 'meadow_t_51d6c97'}, 'is_type_const')
def meadow_is_type_const(meadow_t_51d6c97):
    return meadow_t_51d6c97 & meadow_BTM_CONST != 0

@_name_boundary.callable_contract({'t': 'meadow_t_4216461'}, 'is_type_volatile')
def meadow_is_type_volatile(meadow_t_4216461):
    return meadow_t_4216461 & meadow_BTM_VOLATILE != 0

@_name_boundary.callable_contract({'t': 'meadow_t_1a4903e'}, 'get_base_type')
def meadow_get_base_type(meadow_t_1a4903e):
    return meadow_t_1a4903e & meadow_TYPE_BASE_MASK

@_name_boundary.callable_contract({'t': 'meadow_t_1acc95d'}, 'get_type_flags')
def meadow_get_type_flags(meadow_t_1acc95d):
    return meadow_t_1acc95d & meadow_TYPE_FLAGS_MASK

@_name_boundary.callable_contract({'t': 'meadow_t_56af4ce'}, 'get_full_type')
def meadow_get_full_type(meadow_t_56af4ce):
    return meadow_t_56af4ce & meadow_TYPE_FULL_MASK

@_name_boundary.callable_contract({'t': 'meadow_t_0b8a606'}, 'is_typeid_last')
def meadow_is_typeid_last(meadow_t_0b8a606):
    return meadow_get_base_type(meadow_t_0b8a606) <= meadow__BT_LAST_BASIC

@_name_boundary.callable_contract({'t': 'meadow_t_fa0fe8f'}, 'is_type_partial')
def meadow_is_type_partial(meadow_t_fa0fe8f):
    return meadow_get_base_type(meadow_t_fa0fe8f) <= meadow_BT_VOID and meadow_get_type_flags(meadow_t_fa0fe8f) != 0

@_name_boundary.callable_contract({'t': 'meadow_t_3236e24'}, 'is_type_void')
def meadow_is_type_void(meadow_t_3236e24):
    return meadow_get_full_type(meadow_t_3236e24) == meadow_BTF_VOID

@_name_boundary.callable_contract({'t': 'meadow_t_96b850c'}, 'is_type_unknown')
def meadow_is_type_unknown(meadow_t_96b850c):
    return meadow_get_full_type(meadow_t_96b850c) == meadow_BT_UNKNOWN

@_name_boundary.callable_contract({'t': 'meadow_t_185117c'}, 'is_type_ptr')
def meadow_is_type_ptr(meadow_t_185117c):
    return meadow_get_base_type(meadow_t_185117c) == meadow_BT_PTR

@_name_boundary.callable_contract({'t': 'meadow_t_841c683'}, 'is_type_complex')
def meadow_is_type_complex(meadow_t_841c683):
    return meadow_get_base_type(meadow_t_841c683) == meadow_BT_COMPLEX

@_name_boundary.callable_contract({'t': 'meadow_t_2a1312a'}, 'is_type_func')
def meadow_is_type_func(meadow_t_2a1312a):
    return meadow_get_base_type(meadow_t_2a1312a) == meadow_BT_FUNC

@_name_boundary.callable_contract({'t': 'meadow_t_8bc30ff'}, 'is_type_array')
def meadow_is_type_array(meadow_t_8bc30ff):
    return meadow_get_base_type(meadow_t_8bc30ff) == meadow_BT_ARRAY

@_name_boundary.callable_contract({'t': 'meadow_t_ef8e77d'}, 'is_type_typedef')
def meadow_is_type_typedef(meadow_t_ef8e77d):
    return meadow_get_full_type(meadow_t_ef8e77d) == meadow_BTF_TYPEDEF

@_name_boundary.callable_contract({'t': 'meadow_t_7b01d0b'}, 'is_type_sue')
def meadow_is_type_sue(meadow_t_7b01d0b):
    return meadow_is_type_complex(meadow_t_7b01d0b) and (not meadow_is_type_typedef(meadow_t_7b01d0b))

@_name_boundary.callable_contract({'t': 'meadow_t_e856c6d'}, 'is_type_struct')
def meadow_is_type_struct(meadow_t_e856c6d):
    return meadow_get_full_type(meadow_t_e856c6d) == meadow_BTF_STRUCT

@_name_boundary.callable_contract({'t': 'meadow_t_7deb3d0'}, 'is_type_union')
def meadow_is_type_union(meadow_t_7deb3d0):
    return meadow_get_full_type(meadow_t_7deb3d0) == meadow_BTF_UNION

@_name_boundary.callable_contract({'t': 'meadow_t_bf9ccc0'}, 'is_type_struni')
def meadow_is_type_struni(meadow_t_bf9ccc0):
    return meadow_is_type_struct(meadow_t_bf9ccc0) or meadow_is_type_union(meadow_t_bf9ccc0)

@_name_boundary.callable_contract({'t': 'meadow_t_566eb9b'}, 'is_type_enum')
def meadow_is_type_enum(meadow_t_566eb9b):
    return meadow_get_full_type(meadow_t_566eb9b) == meadow_BTF_ENUM

@_name_boundary.callable_contract({'t': 'meadow_t_54186a1'}, 'is_type_bitfld')
def meadow_is_type_bitfld(meadow_t_54186a1):
    return meadow_get_base_type(meadow_t_54186a1) == meadow_BT_BITFIELD

@_name_boundary.callable_contract({'bt': 'meadow_bt_9014a2f'}, 'is_type_int')
def meadow_is_type_int(meadow_bt_9014a2f):
    meadow_bt_9014a2f = meadow_get_base_type(meadow_bt_9014a2f)
    return meadow_BT_INT8 <= meadow_bt_9014a2f <= meadow_BT_INT

@_name_boundary.callable_contract({'t': 'meadow_t_6941bee'}, 'is_type_int128')
def meadow_is_type_int128(meadow_t_6941bee):
    return meadow_get_full_type(meadow_t_6941bee) == meadow_BT_INT128 | meadow_BTMT_UNKSIGN or meadow_get_full_type(meadow_t_6941bee) == meadow_BT_INT128 | meadow_BTMT_SIGNED

@_name_boundary.callable_contract({'t': 'meadow_t_a8f0850'}, 'is_type_int64')
def meadow_is_type_int64(meadow_t_a8f0850):
    return meadow_get_full_type(meadow_t_a8f0850) == meadow_BT_INT64 | meadow_BTMT_UNKSIGN or meadow_get_full_type(meadow_t_a8f0850) == meadow_BT_INT64 | meadow_BTMT_SIGNED

@_name_boundary.callable_contract({'t': 'meadow_t_983ed2a'}, 'is_type_int32')
def meadow_is_type_int32(meadow_t_983ed2a):
    return meadow_get_full_type(meadow_t_983ed2a) == meadow_BT_INT32 | meadow_BTMT_UNKSIGN or meadow_get_full_type(meadow_t_983ed2a) == meadow_BT_INT32 | meadow_BTMT_SIGNED

@_name_boundary.callable_contract({'t': 'meadow_t_61a8396'}, 'is_type_int16')
def meadow_is_type_int16(meadow_t_61a8396):
    return meadow_get_full_type(meadow_t_61a8396) == meadow_BT_INT16 | meadow_BTMT_UNKSIGN or meadow_get_full_type(meadow_t_61a8396) == meadow_BT_INT16 | meadow_BTMT_SIGNED

@_name_boundary.callable_contract({'t': 'meadow_t_9244761'}, 'is_type_char')
def meadow_is_type_char(meadow_t_9244761):
    return meadow_get_full_type(meadow_t_9244761) == meadow_BT_INT8 | meadow_BTMT_CHAR or meadow_get_full_type(meadow_t_9244761) == meadow_BT_INT8 | meadow_BTMT_SIGNED

@_name_boundary.callable_contract({'t': 'meadow_t_480e925'}, 'is_type_paf')
def meadow_is_type_paf(meadow_t_480e925):
    meadow_t_480e925 = meadow_get_base_type(meadow_t_480e925)
    return meadow_BT_PTR <= meadow_t_480e925 <= meadow_BT_FUNC

@_name_boundary.callable_contract({'t': 'meadow_t_46cc445'}, 'is_type_ptr_or_array')
def meadow_is_type_ptr_or_array(meadow_t_46cc445):
    meadow_t_46cc445 = meadow_get_base_type(meadow_t_46cc445)
    return meadow_t_46cc445 == meadow_BT_PTR or meadow_t_46cc445 == meadow_BT_ARRAY

@_name_boundary.callable_contract({'t': 'meadow_t_cbd9c1d'}, 'is_type_floating')
def meadow_is_type_floating(meadow_t_cbd9c1d):
    return meadow_get_base_type(meadow_t_cbd9c1d) == meadow_BT_FLOAT

@_name_boundary.callable_contract({'t': 'meadow_t_b62609c'}, 'is_type_integral')
def meadow_is_type_integral(meadow_t_b62609c):
    return meadow_get_full_type(meadow_t_b62609c) > meadow_BT_VOID and meadow_get_base_type(meadow_t_b62609c) <= meadow_BT_BOOL

@_name_boundary.callable_contract({'t': 'meadow_t_bc2b909'}, 'is_type_ext_integral')
def meadow_is_type_ext_integral(meadow_t_bc2b909):
    return meadow_is_type_integral(meadow_t_bc2b909) or meadow_is_type_enum(meadow_t_bc2b909)

@_name_boundary.callable_contract({'t': 'meadow_t_e61abec'}, 'is_type_arithmetic')
def meadow_is_type_arithmetic(meadow_t_e61abec):
    return meadow_get_full_type(meadow_t_e61abec) > meadow_BT_VOID and meadow_get_base_type(meadow_t_e61abec) <= meadow_BT_FLOAT

@_name_boundary.callable_contract({'t': 'meadow_t_55572fd'}, 'is_type_ext_arithmetic')
def meadow_is_type_ext_arithmetic(meadow_t_55572fd):
    return meadow_is_type_arithmetic(meadow_t_55572fd) or meadow_is_type_enum(meadow_t_55572fd)

@_name_boundary.callable_contract({'t': 'meadow_t_fa57339'}, 'is_type_uint')
def meadow_is_type_uint(meadow_t_fa57339):
    return meadow_get_full_type(meadow_t_fa57339) == meadow_BTF_UINT

@_name_boundary.callable_contract({'t': 'meadow_t_0fba5f2'}, 'is_type_uchar')
def meadow_is_type_uchar(meadow_t_0fba5f2):
    return meadow_get_full_type(meadow_t_0fba5f2) == meadow_BTF_UCHAR

@_name_boundary.callable_contract({'t': 'meadow_t_a26f6de'}, 'is_type_uint16')
def meadow_is_type_uint16(meadow_t_a26f6de):
    return meadow_get_full_type(meadow_t_a26f6de) == meadow_BTF_UINT16

@_name_boundary.callable_contract({'t': 'meadow_t_afa0a53'}, 'is_type_uint32')
def meadow_is_type_uint32(meadow_t_afa0a53):
    return meadow_get_full_type(meadow_t_afa0a53) == meadow_BTF_UINT32

@_name_boundary.callable_contract({'t': 'meadow_t_6948bb6'}, 'is_type_uint64')
def meadow_is_type_uint64(meadow_t_6948bb6):
    return meadow_get_full_type(meadow_t_6948bb6) == meadow_BTF_UINT64

@_name_boundary.callable_contract({'t': 'meadow_t_6cfd6c5'}, 'is_type_uint128')
def meadow_is_type_uint128(meadow_t_6cfd6c5):
    return meadow_get_full_type(meadow_t_6cfd6c5) == meadow_BTF_UINT128

@_name_boundary.callable_contract({'t': 'meadow_t_26ceca2'}, 'is_type_ldouble')
def meadow_is_type_ldouble(meadow_t_26ceca2):
    return meadow_get_full_type(meadow_t_26ceca2) == meadow_BTF_LDOUBLE

@_name_boundary.callable_contract({'t': 'meadow_t_a39cefc'}, 'is_type_double')
def meadow_is_type_double(meadow_t_a39cefc):
    return meadow_get_full_type(meadow_t_a39cefc) == meadow_BTF_DOUBLE

@_name_boundary.callable_contract({'t': 'meadow_t_78359c9'}, 'is_type_float')
def meadow_is_type_float(meadow_t_78359c9):
    return meadow_get_full_type(meadow_t_78359c9) == meadow_BTF_FLOAT

@_name_boundary.callable_contract({'t': 'meadow_t_4726f28'}, 'is_type_bool')
def meadow_is_type_bool(meadow_t_4726f28):
    return meadow_get_base_type(meadow_t_4726f28) == meadow_BT_BOOL

@_name_boundary.callable_contract({'t': 'meadow_t_21b2f4d'}, 'is_tah_byte')
def meadow_is_tah_byte(meadow_t_21b2f4d):
    return meadow_t_21b2f4d == meadow_TAH_BYTE

@_name_boundary.callable_contract({'t': 'meadow_t_6593651'}, 'is_sdacl_byte')
def meadow_is_sdacl_byte(meadow_t_6593651):
    return meadow_t_6593651 & ~meadow_TYPE_FLAGS_MASK ^ meadow_TYPE_MODIF_MASK <= meadow_BT_VOID

@_name_boundary.callable_contract({'t': 'meadow_t_bb6dcf7'}, 'is_type_closure')
def meadow_is_type_closure(meadow_t_bb6dcf7):
    return meadow_get_type_flags(meadow_t_bb6dcf7) == meadow_BTMT_CLOSURE

@_name_boundary.callable_contract({'t': 'meadow_t_d5b0b11'}, 'is_cm_cc_voidarg')
def meadow_is_cm_cc_voidarg(meadow_t_d5b0b11):
    return meadow_t_d5b0b11 & meadow_CM_CC_MASK == meadow_CM_CC_VOIDARG

@_name_boundary.callable_contract({'t': 'meadow_t_9521693'}, 'is_cm_cc_special')
def meadow_is_cm_cc_special(meadow_t_9521693):
    return meadow_t_9521693 & meadow_CM_CC_MASK == meadow_CM_CC_SPECIAL

@_name_boundary.callable_contract({'t': 'meadow_t_c30acbc'}, 'is_cm_cc_special_pe')
def meadow_is_cm_cc_special_pe(meadow_t_c30acbc):
    return meadow_t_c30acbc & meadow_CM_CC_MASK in (meadow_CM_CC_SPECIAL, meadow_CM_CC_SPECIALP, meadow_CM_CC_SPECIALE)

@_name_boundary.callable_contract({'t': 'meadow_t_2e42345'}, 'is_cc_spoiled')
def meadow_is_cc_spoiled(meadow_t_2e42345):
    return meadow_get_cc(meadow_t_2e42345) == meadow_CM_CC_SPOILED

@_name_boundary.callable_contract({'cm': 'meadow_cm_local_2f781a9'}, 'get_cc')
def meadow_get_cc(meadow_cm_local_2f781a9):
    return meadow_cm_local_2f781a9 & meadow_CM_CC_MASK

@_name_boundary.callable_contract({'cm': 'meadow_cm_local_cbc7eda'}, 'is_user_cc')
def meadow_is_user_cc(meadow_cm_local_cbc7eda):
    meadow_cc_bee82c8 = meadow_get_cc(meadow_cm_local_cbc7eda)
    return meadow_cc_bee82c8 >= meadow_CM_CC_SPECIALE

@_name_boundary.callable_contract({'cm': 'meadow_cm_local_47e6b86'}, 'is_vararg_cc')
def meadow_is_vararg_cc(meadow_cm_local_47e6b86):
    meadow_cc_59ee05b = meadow_get_cc(meadow_cm_local_47e6b86)
    return meadow_cc_59ee05b in (meadow_CM_CC_ELLIPSIS, meadow_CM_CC_SPECIALE)

@_name_boundary.callable_contract({'cm': 'meadow_cm_local_28b8d7c'}, 'is_purging_cc')
def meadow_is_purging_cc(meadow_cm_local_28b8d7c):
    meadow_cc_4240e0d = meadow_get_cc(meadow_cm_local_28b8d7c)
    return meadow_cc_4240e0d in (meadow_CM_CC_STDCALL, meadow_CM_CC_PASCAL, meadow_CM_CC_SPECIALP, meadow_CM_CC_FASTCALL, meadow_CM_CC_THISCALL)
_name_boundary.module_contract(globals(), {'REGS': 'meadow_REGS', 'BTF_TYPEDEF': 'meadow_BTF_TYPEDEF', 'is_type_func': 'meadow_is_type_func', 'BTMT_UNSIGNED': 'meadow_BTMT_UNSIGNED', 'BTF_LDOUBLE': 'meadow_BTF_LDOUBLE', 'TYPE_MODIF_MASK': 'meadow_TYPE_MODIF_MASK', 'is_type_paf': 'meadow_is_type_paf', 'is_type_ldouble': 'meadow_is_type_ldouble', 'BTMT_NONBASED': 'meadow_BTMT_NONBASED', 'BTMT_SIZE128': 'meadow_BTMT_SIZE128', 'BTMT_BOOL2': 'meadow_BTMT_BOOL2', 'is_vararg_cc': 'meadow_is_vararg_cc', 'BTF_INT64': 'meadow_BTF_INT64', 'BTMT_LNGDBL': 'meadow_BTMT_LNGDBL', 'BTMT_SIZE0': 'meadow_BTMT_SIZE0', 'BTMT_BFLDI32': 'meadow_BTMT_BFLDI32', 'BTF_FLOAT': 'meadow_BTF_FLOAT', 'REGS_METAPC': 'meadow_REGS_METAPC', 'BTE_OUT_MASK': 'meadow_BTE_OUT_MASK', 'is_type_int128': 'meadow_is_type_int128', 'BT_INT8': 'meadow_BT_INT8', 'is_type_char': 'meadow_is_type_char', 'ALOC_RREL': 'meadow_ALOC_RREL', 'CM_MASK': 'meadow_CM_MASK', 'is_type_typedef': 'meadow_is_type_typedef', 'CM_CC_SPOILED': 'meadow_CM_CC_SPOILED', 'BTMT_FAR': 'meadow_BTMT_FAR', 'is_type_integral': 'meadow_is_type_integral', 'get_full_type': 'meadow_get_full_type', 'BTF_VOID': 'meadow_BTF_VOID', 'BTF_INT8': 'meadow_BTF_INT8', 'is_cc_spoiled': 'meadow_is_cc_spoiled', 'BTMT_CHAR': 'meadow_BTMT_CHAR', 'is_cm_cc_special': 'meadow_is_cm_cc_special', 'is_type_struct': 'meadow_is_type_struct', 'is_cm_cc_voidarg': 'meadow_is_cm_cc_voidarg', 'BTF_INT32': 'meadow_BTF_INT32', 'TYPE_BASE_MASK': 'meadow_TYPE_BASE_MASK', 'BTM_CONST': 'meadow_BTM_CONST', 'BTF_UNK': 'meadow_BTF_UNK', 'BTMT_NEAR': 'meadow_BTMT_NEAR', 'BTMT_DOUBLE': 'meadow_BTMT_DOUBLE', 'BTM_VOLATILE': 'meadow_BTM_VOLATILE', 'is_type_ptr': 'meadow_is_type_ptr', 'BTF_ENUM': 'meadow_BTF_ENUM', 'BTE_UDEC': 'meadow_BTE_UDEC', 'is_type_floating': 'meadow_is_type_floating', 'BT_INT32': 'meadow_BT_INT32', 'ALOC_CUSTOM': 'meadow_ALOC_CUSTOM', 'is_type_partial': 'meadow_is_type_partial', 'BTMT_ARRESERV': 'meadow_BTMT_ARRESERV', 'is_type_const': 'meadow_is_type_const', 'CM_N32_F48': 'meadow_CM_N32_F48', 'BTF_UNION': 'meadow_BTF_UNION', 'BTMT_DEFCALL': 'meadow_BTMT_DEFCALL', 'FAH_BYTE': 'meadow_FAH_BYTE', 'CM_CC_RESERVE3': 'meadow_CM_CC_RESERVE3', 'ALOC_REG1': 'meadow_ALOC_REG1', 'BTMT_BFLDI8': 'meadow_BTMT_BFLDI8', 'is_type_enum': 'meadow_is_type_enum', 'BT_UNK_BYTE': 'meadow_BT_UNK_BYTE', 'TAH_HASATTRS': 'meadow_TAH_HASATTRS', 'BT_VOID': 'meadow_BT_VOID', 'BTF_UINT128': 'meadow_BTF_UINT128', 'BT_COMPLEX': 'meadow_BT_COMPLEX', 'BTF_BOOL': 'meadow_BTF_BOOL', 'BTMT_DEFBOOL': 'meadow_BTMT_DEFBOOL', 'is_type_ext_arithmetic': 'meadow_is_type_ext_arithmetic', 'is_user_cc': 'meadow_is_user_cc', 'BTF_UINT': 'meadow_BTF_UINT', 'is_type_double': 'meadow_is_type_double', 'is_purging_cc': 'meadow_is_purging_cc', 'BTF_SINT': 'meadow_BTF_SINT', 'is_type_int16': 'meadow_is_type_int16', 'BT_UNKNOWN': 'meadow_BT_UNKNOWN', 'CM_N16_F32': 'meadow_CM_N16_F32', 'CM_CC_SPECIALE': 'meadow_CM_CC_SPECIALE', 'BTMT_BFLDI16': 'meadow_BTMT_BFLDI16', 'CM_CC_RESERVE4': 'meadow_CM_CC_RESERVE4', 'CM_CC_MANUAL': 'meadow_CM_CC_MANUAL', 'BTF_TBYTE': 'meadow_BTF_TBYTE', 'is_type_bool': 'meadow_is_type_bool', 'BTE_CHAR': 'meadow_BTE_CHAR', 'BTMT_SIGNED': 'meadow_BTMT_SIGNED', 'BTF_BYTE': 'meadow_BTF_BYTE', 'is_tah_byte': 'meadow_is_tah_byte', 'CM_N8_F16': 'meadow_CM_N8_F16', 'is_type_sue': 'meadow_is_type_sue', 'is_cm_cc_special_pe': 'meadow_is_cm_cc_special_pe', 'BTMT_TYPEDEF': 'meadow_BTMT_TYPEDEF', 'ALOC_REG2': 'meadow_ALOC_REG2', 'BTMT_UNKSIGN': 'meadow_BTMT_UNKSIGN', 'is_type_closure': 'meadow_is_type_closure', 'BTMT_SIZE48': 'meadow_BTMT_SIZE48', 'BTMT_UNION': 'meadow_BTMT_UNION', 'BT_PTR': 'meadow_BT_PTR', 'BT_UNK_OWORD': 'meadow_BT_UNK_OWORD', 'ALOC_NONE': 'meadow_ALOC_NONE', 'BTE_BITFIELD': 'meadow_BTE_BITFIELD', 'ALOC_STATIC': 'meadow_ALOC_STATIC', 'get_base_type': 'meadow_get_base_type', 'is_type_uchar': 'meadow_is_type_uchar', 'is_type_uint32': 'meadow_is_type_uint32', 'get_cc': 'meadow_get_cc', 'CM_CC_MASK': 'meadow_CM_CC_MASK', 'CM_CC_ELLIPSIS': 'meadow_CM_CC_ELLIPSIS', 'CM_UNKNOWN': 'meadow_CM_UNKNOWN', 'CM_CC_FASTCALL': 'meadow_CM_CC_FASTCALL', 'ALOC_STACK': 'meadow_ALOC_STACK', 'BT_BOOL': 'meadow_BT_BOOL', 'TYPE_FULL_MASK': 'meadow_TYPE_FULL_MASK', 'BTMT_BFLDI64': 'meadow_BTMT_BFLDI64', 'BTMT_BOOL4': 'meadow_BTMT_BOOL4', 'BTF_UINT8': 'meadow_BTF_UINT8', 'BTF_UINT32': 'meadow_BTF_UINT32', 'REGS_ARM': 'meadow_REGS_ARM', 'BTMT_DEFPTR': 'meadow_BTMT_DEFPTR', 'CM_CC_PASCAL': 'meadow_CM_CC_PASCAL', 'is_type_uint64': 'meadow_is_type_uint64', 'BTF_UINT64': 'meadow_BTF_UINT64', 'BTMT_BOOL1': 'meadow_BTMT_BOOL1', 'CM_CC_VOIDARG': 'meadow_CM_CC_VOIDARG', 'BTMT_INTCALL': 'meadow_BTMT_INTCALL', 'CM_N64': 'meadow_CM_N64', 'BTE_SIZE_MASK': 'meadow_BTE_SIZE_MASK', 'CM_CC_INVALID': 'meadow_CM_CC_INVALID', 'is_type_uint128': 'meadow_is_type_uint128', 'BTF_INT128': 'meadow_BTF_INT128', 'BTF_UCHAR': 'meadow_BTF_UCHAR', 'TAH_BYTE': 'meadow_TAH_BYTE', 'TYPE_FLAGS_MASK': 'meadow_TYPE_FLAGS_MASK', 'BT_BITFIELD': 'meadow_BT_BITFIELD', '_BT_LAST_BASIC': 'meadow__BT_LAST_BASIC', 'CM_CC_SPECIALP': 'meadow_CM_CC_SPECIALP', 'is_sdacl_byte': 'meadow_is_sdacl_byte', 'BT_INT64': 'meadow_BT_INT64', 'BT_ARRAY': 'meadow_BT_ARRAY', 'is_type_volatile': 'meadow_is_type_volatile', 'BT_FUNC': 'meadow_BT_FUNC', 'BTMT_STRUCT': 'meadow_BTMT_STRUCT', 'is_type_struni': 'meadow_is_type_struni', 'is_type_int': 'meadow_is_type_int', 'RESERVED_BYTE': 'meadow_RESERVED_BYTE', 'BTMT_FLOAT': 'meadow_BTMT_FLOAT', 'CM_CC_CDECL': 'meadow_CM_CC_CDECL', 'CM_M_FN': 'meadow_CM_M_FN', 'is_type_uint': 'meadow_is_type_uint', 'is_type_ext_integral': 'meadow_is_type_ext_integral', 'BTE_ALWAYS': 'meadow_BTE_ALWAYS', 'BTMT_SPECFLT': 'meadow_BTMT_SPECFLT', 'BT_INT128': 'meadow_BT_INT128', 'is_type_bitfld': 'meadow_is_type_bitfld', 'BTE_HEX': 'meadow_BTE_HEX', 'BT_FLOAT': 'meadow_BT_FLOAT', 'BTE_RESERVED': 'meadow_BTE_RESERVED', 'is_type_void': 'meadow_is_type_void', 'BT_UNK_QWORD': 'meadow_BT_UNK_QWORD', 'is_type_int32': 'meadow_is_type_int32', 'is_type_unknown': 'meadow_is_type_unknown', 'BTF_INT16': 'meadow_BTF_INT16', 'is_type_uint16': 'meadow_is_type_uint16', 'CM_CC_UNKNOWN': 'meadow_CM_CC_UNKNOWN', 'ALOC_DIST': 'meadow_ALOC_DIST', 'CM_CC_STDCALL': 'meadow_CM_CC_STDCALL', 'is_type_float': 'meadow_is_type_float', 'BTF_STRUCT': 'meadow_BTF_STRUCT', 'CM_M_MASK': 'meadow_CM_M_MASK', 'is_type_array': 'meadow_is_type_array', 'CM_CC_SPECIAL': 'meadow_CM_CC_SPECIAL', 'is_type_int64': 'meadow_is_type_int64', 'BTF_INT': 'meadow_BTF_INT', 'get_type_flags': 'meadow_get_type_flags', 'BTMT_FARCALL': 'meadow_BTMT_FARCALL', 'CM_M_FF': 'meadow_CM_M_FF', 'BT_UNK_WORD': 'meadow_BT_UNK_WORD', 'BTMT_SIZE12': 'meadow_BTMT_SIZE12', 'BTE_SDEC': 'meadow_BTE_SDEC', 'is_type_ptr_or_array': 'meadow_is_type_ptr_or_array', 'BT_INT': 'meadow_BT_INT', 'BT_UNK': 'meadow_BT_UNK', 'BTMT_USIGNED': 'meadow_BTMT_USIGNED', 'BT_UNK_DWORD': 'meadow_BT_UNK_DWORD', 'BTF_CHAR': 'meadow_BTF_CHAR', 'is_type_arithmetic': 'meadow_is_type_arithmetic', 'BTMT_NEARCALL': 'meadow_BTMT_NEARCALL', 'CM_M_MN': 'meadow_CM_M_MN', 'CM_M_NF': 'meadow_CM_M_NF', 'BTMT_CLOSURE': 'meadow_BTMT_CLOSURE', 'BTF_DOUBLE': 'meadow_BTF_DOUBLE', 'CM_CC_THISCALL': 'meadow_CM_CC_THISCALL', 'is_type_complex': 'meadow_is_type_complex', 'is_type_union': 'meadow_is_type_union', 'BTMT_ENUM': 'meadow_BTMT_ENUM', 'is_typeid_last': 'meadow_is_typeid_last', 'BTF_UINT16': 'meadow_BTF_UINT16', 'BT_INT16': 'meadow_BT_INT16', 'BT_SEGREG': 'meadow_BT_SEGREG', 'BT_RESERVED': 'meadow_BT_RESERVED'})
