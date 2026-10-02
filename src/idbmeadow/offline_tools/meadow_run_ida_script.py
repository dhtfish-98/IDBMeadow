#!/usr/bin/env python3
# Derived from scripts/run_ida_script.py; original copyright and license retained in ORIGIN.md.
"""
some documentation

author: Willi Ballenthin
email: willi.ballenthin@gmail.com
"""
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
import shlex as meadow_shlex
import logging as meadow_logging
import os.path as _boundary_import_os_path
import os as meadow_os
import argparse as meadow_argparse
import idbmeadow as meadow_idb
import idbmeadow.script_environment as _boundary_import_idb_shim
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'argv': 'meadow_argv_5eff585'}, 'main')
def meadow_main(meadow_argv_5eff585=None):
    if meadow_argv_5eff585 is None:
        meadow_argv_5eff585 = meadow_sys.argv[1:]
    meadow_parser_16670ec = meadow_argparse.ArgumentParser(description='Dump an IDB B-tree to a textual representation.')
    meadow_parser_16670ec.add_argument('script_path', type=str, help='Path to script file.\n                Command line arguments can be passed using quotes:\n                "myscrypt.py arg1 arg2 "arg3 arg3""\n        ')
    meadow_parser_16670ec.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_16670ec.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_16670ec.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_parser_16670ec.add_argument('--ScreenEA', type=str, help='Prepare value of ScreenEA()')
    meadow_args_ae55411 = meadow_parser_16670ec.parse_args(args=meadow_argv_5eff585)
    if meadow_args_ae55411.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_ae55411.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
        meadow_logging.getLogger('idb.netnode').setLevel(meadow_logging.ERROR)
        meadow_logging.getLogger('idb.fileformat').setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
        meadow_logging.getLogger('idb.netnode').setLevel(meadow_logging.ERROR)
        meadow_logging.getLogger('idb.fileformat').setLevel(meadow_logging.ERROR)
    with meadow_idb.from_file(meadow_args_ae55411.idbpath) as meadow_db_88ee154:
        if _name_boundary.attributes(meadow_args_ae55411)['ScreenEA']:
            if _name_boundary.attributes(meadow_args_ae55411)['ScreenEA'].startswith('0x'):
                meadow_screenea_9640aae = int(_name_boundary.attributes(meadow_args_ae55411)['ScreenEA'], 16)
            else:
                meadow_screenea_9640aae = int(_name_boundary.attributes(meadow_args_ae55411)['ScreenEA'])
        else:
            meadow_screenea_9640aae = list(sorted(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](meadow_db_88ee154).segments.keys()))[0]
        meadow_hooks_f44eb2c = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['shim'])['install'](meadow_db_88ee154, ScreenEA=meadow_screenea_9640aae)
        meadow_script_args_1ecec79 = meadow_shlex.split(meadow_args_ae55411.script_path)
        meadow_script_dir_555ce05 = _name_boundary.attributes(meadow_os)['path'].dirname(meadow_script_args_1ecec79[0])
        _name_boundary.attributes(meadow_sys)['path'].insert(0, meadow_script_dir_555ce05)
        _name_boundary.attributes(meadow_hooks_f44eb2c['idc'])['ARGV'] = meadow_script_args_1ecec79
        with open(meadow_script_args_1ecec79[0], 'rb') as meadow_f_8971224:
            meadow_g_72f6b53 = {'__name__': '__main__'}
            meadow_g_72f6b53.update(meadow_hooks_f44eb2c)
            exec(_name_boundary.attributes(meadow_f_8971224)['read'](), meadow_g_72f6b53)
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'idb': 'meadow_idb', 'shlex': 'meadow_shlex', 'os': 'meadow_os', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
