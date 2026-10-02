#!/usr/bin/env python
# Derived from scripts/explore_btree.py; original copyright and license retained in ORIGIN.md.
"""
Interactively explore an IDB B-Tree like a file system.

author: Willi Ballenthin
email: willi.ballenthin@gmail.com
"""
import idbmeadow.api_contract as _name_boundary
import cmd as meadow_cmd
import sys as meadow_sys
import logging as meadow_logging
import argparse as meadow_argparse
import hexdump as meadow_hexdump
import tabulate as meadow_tabulate
import idbmeadow as meadow_idb
import idbmeadow.node_records as _boundary_import_idb_netnode
import idbmeadow as meadow_idb
meadow_logger = meadow_logging.getLogger(__name__)

@_name_boundary.callable_contract({'i': 'meadow_i_65ce7d5'}, 'h')
def meadow_h(meadow_i_65ce7d5):
    return '%x' % meadow_i_65ce7d5

@_name_boundary.callable_contract({'key': 'meadow_key_local_e84c98f', 'wordsize': 'meadow_wordsize_local_dc70233'}, 'render_key')
def meadow_render_key(meadow_key_local_e84c98f, meadow_wordsize_local_dc70233):
    if meadow_key_local_e84c98f[0] == 46:
        meadow_k_fedc863 = _name_boundary.attributes(meadow_idb)['netnode'].parse_key(meadow_key_local_e84c98f, meadow_wordsize_local_dc70233)
        return 'nodeid: %x tag: %s index: %s' % (_name_boundary.attributes(meadow_k_fedc863)['nodeid'], meadow_k_fedc863.tag, hex(_name_boundary.attributes(meadow_k_fedc863)['index']) if _name_boundary.attributes(meadow_k_fedc863)['index'] is not None else 'None')
    else:
        return bytes(meadow_key_local_e84c98f).decode('ascii')

@_name_boundary.class_contract('BTreeExplorer', {'current_page': 'meadow_current_page', 'db': 'meadow_db', 'path': 'meadow_path'})
class meadow_BTreeExplorer(meadow_cmd.Cmd):

    @_name_boundary.callable_contract({'self': 'meadow_self_2f8ec39', 'db': 'meadow_db_d33ff09'}, '__init__')
    def __init__(meadow_self_2f8ec39, meadow_db_d33ff09):
        super(meadow_BTreeExplorer, meadow_self_2f8ec39).__init__()
        _name_boundary.attributes(meadow_self_2f8ec39)['db'] = meadow_db_d33ff09
        _name_boundary.attributes(meadow_self_2f8ec39)['path'] = [meadow_db_d33ff09.id0.root_page]

    @property
    @_name_boundary.callable_contract({'self': 'meadow_self_0b4ebe6'}, 'prompt')
    def prompt(meadow_self_0b4ebe6):
        return '/'.join(map(meadow_h, _name_boundary.attributes(meadow_self_0b4ebe6)['path'])) + '/ > '

    @property
    @_name_boundary.callable_contract({'self': 'meadow_self_a321024'}, 'current_page')
    def meadow_current_page(meadow_self_a321024):
        return _name_boundary.attributes(_name_boundary.attributes(meadow_self_a321024)['db'].id0)['get_page'](_name_boundary.attributes(meadow_self_a321024)['path'][-1])

    @_name_boundary.callable_contract({'self': 'meadow_self_b032feb', 'line': 'meadow_line_05b7871'}, 'do_ls')
    def do_ls(meadow_self_b032feb, meadow_line_05b7871):
        """
        list the entries in the current B-tree page.
        """
        meadow_page_local_b465b92 = _name_boundary.attributes(meadow_self_b032feb)['current_page']
        meadow_rows_2e80a46 = []
        if _name_boundary.attributes(meadow_page_local_b465b92)['is_leaf']():
            print('leaf: true')
            for meadow_i_6233972, meadow_entry_local_9a8c91a in enumerate(_name_boundary.attributes(meadow_page_local_b465b92)['get_entries']()):
                meadow_rows_2e80a46.append((hex(meadow_i_6233972), meadow_render_key(meadow_entry_local_9a8c91a.key, _name_boundary.attributes(meadow_self_b032feb)['db'].wordsize)))
        else:
            print('leaf: false')
            meadow_rows_2e80a46.append(('', 'ppointer', hex(meadow_page_local_b465b92.ppointer)))
            for meadow_i_6233972, meadow_entry_local_9a8c91a in enumerate(_name_boundary.attributes(meadow_page_local_b465b92)['get_entries']()):
                meadow_rows_2e80a46.append((hex(meadow_i_6233972), meadow_render_key(meadow_entry_local_9a8c91a.key, _name_boundary.attributes(meadow_self_b032feb)['db'].wordsize), hex(meadow_entry_local_9a8c91a.page)))
        print(meadow_tabulate.tabulate(meadow_rows_2e80a46, headers=['entry', 'key', 'page number']))

    @_name_boundary.callable_contract({'self': 'meadow_self_c7b01df', 'line': 'meadow_line_dc5e921'}, 'do_cd')
    def do_cd(meadow_self_c7b01df, meadow_line_dc5e921):
        """
        traverse the B-tree.

        you may only traverse to child nodes, or to the parent node.

        traverse to child node::

            > ls
            entry    key                                 page number
            -------  ----------------------------------  -------------
                     ppointer                            0x3

            > cd 0x3

        traverse to parent::

            > cd ..
        """
        if ' ' in meadow_line_dc5e921:
            meadow_part_11efc47 = meadow_line_dc5e921.partition(' ')[0]
        else:
            meadow_part_11efc47 = meadow_line_dc5e921
        if meadow_part_11efc47 == '..':
            if len(_name_boundary.attributes(meadow_self_c7b01df)['path']) == 1:
                print('error: cannot go up, already at root node.')
                return
            _name_boundary.attributes(meadow_self_c7b01df)['path'] = _name_boundary.attributes(meadow_self_c7b01df)['path'][:-1]
            return
        meadow_page_local_9d111b3 = _name_boundary.attributes(meadow_self_c7b01df)['current_page']
        meadow_target_a85718d = int(meadow_part_11efc47, 16)
        if not (meadow_target_a85718d == meadow_page_local_9d111b3.ppointer or meadow_target_a85718d in map(lambda meadow_e_9f1c72b: meadow_e_9f1c72b.page, _name_boundary.attributes(meadow_page_local_9d111b3)['get_entries']())):
            print('error: invalid page number.')
            return
        _name_boundary.attributes(meadow_self_c7b01df)['path'].append(meadow_target_a85718d)

    @_name_boundary.callable_contract({'self': 'meadow_self_2385618', 'line': 'meadow_line_61656cd'}, 'do_cat')
    def do_cat(meadow_self_2385618, meadow_line_61656cd):
        """
        display the contents of an entry.

        example::

            > ls
            leaf: true
            entry    key
            -------  -----------------------------------------
            0x0      b'$ MAX LINK'
            0x1      b'$ MAX NODE'
            0x2      b'$ NET DESC'
            0x3      nodeid: 0 tag: S index: 0x3e8
            0x4      nodeid: 0 tag: S index: 0x3e9
            ...
            ----  ------------------------------------------------------------------------------------------
            > cat 3
            00000000: 3B 20 46 69 6C 65 20 4E  61 6D 65 20 20 20 3A 20  ; File Name   :
            00000010: 5A 3A 5C 68 6F 6D 65 5C  75 73 65 72 5C 44 6F 63  Z:\\home\\user\\Doc
            00000020: 75 6D 65 6E 74 73 5C 63  6F 64 65 5C 70 79 74 68  uments\\code\\pyth
            00000030: 6F 6E 2D 69 64 62 5C 74  65 73 74 73 5C 64 61 74  on-idb\\tests\\dat
            00000040: 61 5C 73 6D 61 6C 6C 5C  73 6D 61 6C 6C 2E 62 69  a\\small\\small.bi
            00000050: 6E 00
        """
        if ' ' in meadow_line_61656cd:
            meadow_part_059bb14 = meadow_line_61656cd.partition(' ')[0]
        else:
            meadow_part_059bb14 = meadow_line_61656cd
        meadow_target_02ea0f3 = int(meadow_part_059bb14, 16)
        meadow_entry_local_e188607 = _name_boundary.attributes(_name_boundary.attributes(meadow_self_2385618)['current_page'])['get_entry'](meadow_target_02ea0f3)
        meadow_hexdump.hexdump(meadow_entry_local_e188607.value)

    @_name_boundary.callable_contract({'self': 'meadow_self_9321f3b', 'line': 'meadow_line_ad54427'}, 'do_exit')
    def do_exit(meadow_self_9321f3b, meadow_line_ad54427):
        return True

    @_name_boundary.callable_contract({'self': 'meadow_self_f154576', 'line': 'meadow_line_6f455b1'}, 'do_quit')
    def do_quit(meadow_self_f154576, meadow_line_6f455b1):
        return True

    @_name_boundary.callable_contract({'self': 'meadow_self_2dd7691', 'line': 'meadow_line_c939cdf'}, 'do_EOF')
    def do_EOF(meadow_self_2dd7691, meadow_line_c939cdf):
        return True

@_name_boundary.callable_contract({'argv': 'meadow_argv_bb2fccd'}, 'main')
def meadow_main(meadow_argv_bb2fccd=None):
    if meadow_argv_bb2fccd is None:
        meadow_argv_bb2fccd = meadow_sys.argv[1:]
    meadow_parser_5a9041e = meadow_argparse.ArgumentParser(description='Interactively explore an IDB B-tree like a file system.')
    meadow_parser_5a9041e.add_argument('idbpath', type=str, help='Path to input idb file')
    meadow_parser_5a9041e.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    meadow_parser_5a9041e.add_argument('-q', '--quiet', action='store_true', help='Disable all output but errors')
    meadow_args_eef3c54 = meadow_parser_5a9041e.parse_args(args=meadow_argv_bb2fccd)
    if meadow_args_eef3c54.verbose:
        meadow_logging.basicConfig(level=meadow_logging.DEBUG)
        meadow_logging.getLogger().setLevel(meadow_logging.DEBUG)
    elif meadow_args_eef3c54.quiet:
        meadow_logging.basicConfig(level=meadow_logging.ERROR)
        meadow_logging.getLogger().setLevel(meadow_logging.ERROR)
    else:
        meadow_logging.basicConfig(level=meadow_logging.INFO)
        meadow_logging.getLogger().setLevel(meadow_logging.INFO)
    with meadow_idb.from_file(meadow_args_eef3c54.idbpath) as meadow_db_f18530e:
        meadow_explorer_17feeda = meadow_BTreeExplorer(meadow_db_f18530e)
        meadow_explorer_17feeda.cmdloop()
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'BTreeExplorer': 'meadow_BTreeExplorer', 'idb': 'meadow_idb', 'h': 'meadow_h', 'render_key': 'meadow_render_key', 'tabulate': 'meadow_tabulate', 'hexdump': 'meadow_hexdump', 'cmd': 'meadow_cmd', 'logger': 'meadow_logger', 'logging': 'meadow_logging', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'main': 'meadow_main'})
