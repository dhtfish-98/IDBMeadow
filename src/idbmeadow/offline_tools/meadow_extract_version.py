#!/usr/bin/env python3
# Derived from scripts/extract_version.py; original copyright and license retained in ORIGIN.md.
"""
Extract the IDA Pro version used to create the IDB.

author: Willi Ballenthin
email: willi.ballenthin@gmail.com
"""
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
import logging as meadow_logging
import argparse as meadow_argparse
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'argv': 'meadow_argv_ddb482f'}, 'main')
def meadow_main(meadow_argv_ddb482f=None):
    if meadow_argv_ddb482f is None:
        meadow_argv_ddb482f = meadow_sys.argv[1:]
    meadow_parser_b076337 = meadow_argparse.ArgumentParser(description='Extract the IDA Pro version used to create the IDB.')
    meadow_parser_b076337.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_b076337.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_b076337.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_4156fd1 = meadow_parser_b076337.parse_args(args=meadow_argv_ddb482f)
    if meadow_args_4156fd1.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_4156fd1.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_4156fd1.idbpath) as meadow_db_423cf25:
        meadow_root_4bdb6a4 = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_db_423cf25)
        print(meadow_root_4bdb6a4.version)
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'idb': 'meadow_idb', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
