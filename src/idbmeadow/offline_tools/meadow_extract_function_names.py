#!/usr/bin/env python3
# Derived from scripts/extract_function_names.py; original copyright and license retained in ORIGIN.md.
"""
Extract the names of functions within the given IDA Pro database.

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
import idbmeadow.semantic_views as _boundary_import_idb_analysis
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'argv': 'meadow_argv_299387e'}, 'main')
def meadow_main(meadow_argv_299387e=None):
    if meadow_argv_299387e is None:
        meadow_argv_299387e = meadow_sys.argv[1:]
    meadow_parser_073d23d = meadow_argparse.ArgumentParser(description='Extract the names of functions within the given IDA Pro database.')
    meadow_parser_073d23d.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_073d23d.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_073d23d.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_99aec66 = meadow_parser_073d23d.parse_args(args=meadow_argv_299387e)
    if meadow_args_99aec66.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_99aec66.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_99aec66.idbpath) as meadow_db_4acd54b:
        meadow_root_7ef85df = _name_boundary.attributes(meadow_idb)['analysis'].Root(meadow_db_4acd54b)
        meadow_api_local_08010ba = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_4acd54b)
        for meadow_fva_c82c483 in _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_08010ba)['idautils'])['Functions']():
            print('%s:0x%x:%s' % (meadow_root_7ef85df.md5, meadow_fva_c82c483, _name_boundary.attributes(_name_boundary.attributes(meadow_api_local_08010ba)['idc'])['GetFunctionName'](meadow_fva_c82c483)))
            print(_name_boundary.attributes(_name_boundary.attributes(meadow_api_local_08010ba)['idc'])['GetType'](meadow_fva_c82c483))
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'idb': 'meadow_idb', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
