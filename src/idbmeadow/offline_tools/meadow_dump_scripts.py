#!/usr/bin/env python3
# Derived from scripts/dump_scripts.py; original copyright and license retained in ORIGIN.md.
"""
Extract scripts embedded within IDA Pro databases.

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

@_name_boundary.callable_contract({'argv': 'meadow_argv_7c7aae0'}, 'main')
def meadow_main(meadow_argv_7c7aae0=None):
    if meadow_argv_7c7aae0 is None:
        meadow_argv_7c7aae0 = meadow_sys.argv[1:]
    meadow_parser_e07f3e5 = meadow_argparse.ArgumentParser(description='Extract scripts embedded within IDA Pro databases.')
    meadow_parser_e07f3e5.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_e07f3e5.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_e07f3e5.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_d332811 = meadow_parser_e07f3e5.parse_args(args=meadow_argv_7c7aae0)
    if meadow_args_d332811.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_d332811.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_d332811.idbpath) as meadow_db_950172f:
        try:
            for meadow_script_99bc30c in _name_boundary.attributes(meadow_idb)['analysis'].enumerate_script_snippets(meadow_db_950172f):
                meadow_logger.debug('script: %s', meadow_script_99bc30c.name)
                meadow_logger.debug('language: %s', meadow_script_99bc30c.language)
                meadow_logger.debug('code: \n%s', meadow_script_99bc30c.code)
                if meadow_script_99bc30c.language == 'Python':
                    meadow_ext_8744e99 = '.py'
                elif meadow_script_99bc30c.language == 'IDC':
                    meadow_ext_8744e99 = '.idc'
                else:
                    raise ValueError('unexpected script language: ' + meadow_script_99bc30c.language)
                meadow_filename_5272db8 = meadow_script_99bc30c.name + meadow_ext_8744e99
                meadow_logger.info('writing %s script %s to %s', meadow_script_99bc30c.language, meadow_script_99bc30c.name, meadow_filename_5272db8)
                with open(meadow_filename_5272db8, 'wb') as meadow_f_b6adbd1:
                    meadow_f_b6adbd1.write(meadow_script_99bc30c.code.encode('utf-8'))
        except KeyError:
            meadow_logger.warning('not found script snippets')
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'idb': 'meadow_idb', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
