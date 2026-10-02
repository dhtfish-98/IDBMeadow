#!/usr/bin/env python3
# Derived from scripts/dump_btree.py; original copyright and license retained in ORIGIN.md.
"""
some documentation

author: Willi Ballenthin
email: willi.ballenthin@gmail.com
"""
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
import logging as meadow_logging
import argparse as meadow_argparse
import hexdump as meadow_hexdump
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'argv': 'meadow_argv_b7843a0'}, 'main')
def meadow_main(meadow_argv_b7843a0=None):
    if meadow_argv_b7843a0 is None:
        meadow_argv_b7843a0 = meadow_sys.argv[1:]
    meadow_parser_d9288ec = meadow_argparse.ArgumentParser(description='Dump an IDB B-tree to a textual representation.')
    meadow_parser_d9288ec.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_d9288ec.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_d9288ec.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_c4252f3 = meadow_parser_d9288ec.parse_args(args=meadow_argv_b7843a0)
    if meadow_args_c4252f3.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_c4252f3.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_c4252f3.idbpath) as meadow_db_8f54983:
        meadow_cursor_e4a8c4d = _name_boundary.attributes(meadow_db_8f54983.id0)['get_min']()
        while True:
            if meadow_cursor_e4a8c4d.key[0] == 46:
                try:
                    meadow_k_f9f3978 = _name_boundary.attributes(meadow_idb)['netnode'].parse_key(meadow_cursor_e4a8c4d.key, wordsize=meadow_db_8f54983.wordsize)
                except UnicodeDecodeError:
                    meadow_hexdump.hexdump(meadow_cursor_e4a8c4d.key)
                else:
                    print('nodeid: %x tag: %s index: %s' % (_name_boundary.attributes(meadow_k_f9f3978)['nodeid'], meadow_k_f9f3978.tag, hex(_name_boundary.attributes(meadow_k_f9f3978)['index']) if _name_boundary.attributes(meadow_k_f9f3978)['index'] is not None else 'None'))
            else:
                meadow_hexdump.hexdump(meadow_cursor_e4a8c4d.key)
            meadow_hexdump.hexdump(bytes(meadow_cursor_e4a8c4d.value))
            print('--')
            try:
                _name_boundary.attributes(meadow_cursor_e4a8c4d)['next']()
            except IndexError:
                break
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'idb': 'meadow_idb', 'hexdump': 'meadow_hexdump', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
