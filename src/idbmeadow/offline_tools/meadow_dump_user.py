#!/usr/bin/env python
# Derived from scripts/dump_user.py; original copyright and license retained in ORIGIN.md.
"""
Parse and display license information from an IDA Pro database.

author: Willi Ballenthin
email: willi.ballenthin@gmail.com
"""
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
import struct as meadow_struct
import logging as meadow_logging
import argparse as meadow_argparse
import binascii as meadow_binascii
import datetime as meadow_datetime
from vstruct.primitives import v_zstr_utf8 as meadow_v_zstr_utf8
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_5d42e60'}, 'is_encrypted')
def meadow_is_encrypted(meadow_buf_local_5d42e60):
    return _name_boundary.attributes(meadow_buf_local_5d42e60)['find'](b'\x00' * 4) >= 127
meadow_HEXRAYS_PUBKEY = 103708259528020238281968231491212855083623649579000552826541271154713103521021202133558709859463813691153402829135224007858959801854118729056356465578692294425903276554814675228955441044359462414007297799626945860003884709392298205606490444008955270902786809983042022666144385344717700223903132058763789532653

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_a3e21d8'}, 'decrypt')
def meadow_decrypt(meadow_buf_local_a3e21d8):
    """
    decrypt the given 1024-bit blob using Hex-Ray's public key.

    i'm not sure from where this public key originally came.
    the algorithm is derived from here:
        https://github.com/nlitsme/pyidbutil/blob/87cb3235a462774eedfafca00f67c3ce01eeb326/idbtool.py#L43

    Args:
      buf (bytes): at least 0x80 bytes, of which the first 1024 bits will be decrypted.

    Returns:
      bytes: 0x80 bytes of decrypted data.
    """
    meadow_enc_e051df3 = int(meadow_binascii.hexlify(meadow_buf_local_a3e21d8[127::-1]), 16)
    meadow_dec_a78785e = pow(meadow_enc_e051df3, 19, meadow_HEXRAYS_PUBKEY)
    return meadow_binascii.a2b_hex('%0256x' % meadow_dec_a78785e)

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_72e5e70'}, 'parse_user_data')
def meadow_parse_user_data(meadow_buf_local_72e5e70):
    """
    parse a decrypted user blob into a structured dictionary.

    Args:
      buf (bytes): exactly 0x80 bytes of plaintext data.

    Returns:
      Dict[str, Any]: a dictionary with the following values:
        - ts1 (datetime.datetime): timestamp in UTC of something. database creation?
        - ts2 (datetime.datetime): timestamp in UTC of something. sometimes zero.
        - id (str): the ID of the license.
        - name (str): the name of the user and organization that owns the license.
    """
    if len(meadow_buf_local_72e5e70) != 127:
        raise ValueError('invalid user blob.')
    meadow_version_local_ff88b4f = meadow_struct.unpack_from('<H', meadow_buf_local_72e5e70, 2)[0]
    if meadow_version_local_ff88b4f == 0 or meadow_version_local_ff88b4f > 750:
        raise NotImplementedError('user blob version not supported.')
    meadow_ts1_a946c67, meadow___a3cbb93, meadow_ts2_53e3912 = meadow_struct.unpack_from('<III', meadow_buf_local_72e5e70, 16)
    meadow_id_local_68328a7 = '%02X-%02X%02X-%02X%02X-%02X' % meadow_struct.unpack_from('6B', meadow_buf_local_72e5e70, 28)
    meadow_name_local_5e15bab = meadow_v_zstr_utf8()
    meadow_name_local_5e15bab.vsParse(meadow_buf_local_72e5e70[34:])
    return {'ts1': meadow_datetime.datetime.fromtimestamp(meadow_ts1_a946c67, meadow_datetime.timezone.utc), 'ts2': meadow_datetime.datetime.fromtimestamp(meadow_ts2_53e3912, meadow_datetime.timezone.utc), 'id': meadow_id_local_68328a7, 'name': meadow_name_local_5e15bab}

@_name_boundary.callable_contract({'netnode': 'meadow_netnode_ab898d1'}, 'get_userdata')
def meadow_get_userdata(meadow_netnode_ab898d1):
    """
    fetch, decrypt, and parse the user data from the given netnode.

    Args:
      netnode (ida_netnode.Netnode): the netnode containing the user data.

    Returns:
      dict[str, Any]: see `parse_user_data`.
    """
    meadow_userdata_09230a4 = _name_boundary.attributes(meadow_netnode_ab898d1)['supval'](0)
    if meadow_is_encrypted(meadow_userdata_09230a4):
        meadow_userdata_09230a4 = meadow_decrypt(meadow_userdata_09230a4)[1:]
    else:
        meadow_userdata_09230a4 = meadow_userdata_09230a4[:127]
    return meadow_parse_user_data(meadow_userdata_09230a4)

@_name_boundary.callable_contract({'api': 'meadow_api_local_7c0b81d', 'tag': 'meadow_tag_local_1c54271'}, 'print_userdata')
def meadow_print_userdata(meadow_api_local_7c0b81d, meadow_tag_local_1c54271='$ original user'):
    try:
        meadow_netnode_f5714d1 = _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_7c0b81d)['ida_netnode'])['netnode'](meadow_tag_local_1c54271)
        meadow_data_93e306b = meadow_get_userdata(meadow_netnode_f5714d1)
        print('user: %s' % meadow_data_93e306b['name'])
        print('id:   %s' % meadow_data_93e306b['id'])
        print('ts1:  %s' % meadow_data_93e306b['ts1'].isoformat(' ') + 'Z')
        print('ts2:  %s' % meadow_data_93e306b['ts2'].isoformat(' ') + 'Z')
    except KeyError:
        meadow_logger.warning("can' find {}".format(meadow_tag_local_1c54271))
    except (NotImplementedError, ValueError) as meadow_e_36527f6:
        meadow_logger.warning(meadow_e_36527f6)

@_name_boundary.callable_contract({'argv': 'meadow_argv_d339ef0'}, 'main')
def meadow_main(meadow_argv_d339ef0=None):
    if meadow_argv_d339ef0 is None:
        meadow_argv_d339ef0 = meadow_sys.argv[1:]
    meadow_parser_b07c52c = meadow_argparse.ArgumentParser(description='Parse and display license information from an IDA Pro database.')
    meadow_parser_b07c52c.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_b07c52c.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_b07c52c.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_8ac2567 = meadow_parser_b07c52c.parse_args(args=meadow_argv_d339ef0)
    if meadow_args_8ac2567.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_8ac2567.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_8ac2567.idbpath) as meadow_db_2a0a4d0:
        meadow_api_local_d7234af = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_2a0a4d0)
        meadow_print_userdata(meadow_api_local_d7234af)
        meadow_print_userdata(meadow_api_local_d7234af, '$ user1')
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'datetime': 'meadow_datetime', 'idb': 'meadow_idb', 'parse_user_data': 'meadow_parse_user_data', 'HEXRAYS_PUBKEY': 'meadow_HEXRAYS_PUBKEY', 'print_userdata': 'meadow_print_userdata', 'decrypt': 'meadow_decrypt', 'get_userdata': 'meadow_get_userdata', 'binascii': 'meadow_binascii', 'logger': 'meadow_logger', 'is_encrypted': 'meadow_is_encrypted', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'struct': 'meadow_struct', 'v_zstr_utf8': 'meadow_v_zstr_utf8', 'main': 'meadow_main'})
