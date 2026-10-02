# Derived from scripts/dump_types.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
import json as meadow_json
import argparse as meadow_argparse
from vstruct import VStruct as meadow_VStruct
from vstruct.primitives import v_prim as meadow_v_prim
import idbmeadow as meadow_idb
from idbmeadow.type_records import meadow_TInfo as meadow_TInfo, meadow_TILBucket as meadow_TILBucket, meadow_TILTypeInfo as meadow_TILTypeInfo

@_name_boundary.class_contract('TILEncoder', {})
class meadow_TILEncoder(meadow_json.JSONEncoder):

    @_name_boundary.callable_contract({'self': 'meadow_self_28f087d', 'obj': 'meadow_obj_5be1665'}, 'default')
    def default(meadow_self_28f087d, meadow_obj_5be1665):
        if isinstance(meadow_obj_5be1665, meadow_TILBucket):
            meadow__dict_9267782 = {meadow_k_ed487a7: meadow_v_a228654 for meadow_k_ed487a7, meadow_v_a228654 in meadow_obj_5be1665 if meadow_k_ed487a7 != 'buf'}
            meadow__dict_9267782['defs'] = meadow_obj_5be1665.defs
            return meadow__dict_9267782
        elif isinstance(meadow_obj_5be1665, meadow_TILTypeInfo):
            meadow__dict_9267782 = {meadow_k_6ab71b7: meadow_v_a0dfe56 for meadow_k_6ab71b7, meadow_v_a0dfe56 in meadow_obj_5be1665 if meadow_k_6ab71b7 != 'fields_buf'}
            meadow__dict_9267782['fields'] = meadow_obj_5be1665.fields
            meadow__dict_9267782['type'] = _name_boundary.attributes(meadow_obj_5be1665.type)['get_typedeclare']()
            return meadow__dict_9267782
        elif isinstance(meadow_obj_5be1665, meadow_TInfo):
            return _name_boundary.attributes(meadow_obj_5be1665)['get_typestr']()
        elif isinstance(meadow_obj_5be1665, meadow_VStruct):
            return {meadow_k_6626582: meadow_v_21b914d for meadow_k_6626582, meadow_v_21b914d in meadow_obj_5be1665}
        elif isinstance(meadow_obj_5be1665, meadow_v_prim):
            return str(meadow_obj_5be1665)
        elif isinstance(meadow_obj_5be1665, memoryview):
            return meadow_obj_5be1665.hex()
        return meadow_json.JSONEncoder.default(meadow_self_28f087d, meadow_obj_5be1665)

@_name_boundary.callable_contract({'argv': 'meadow_argv_2cd0577'}, 'main')
def meadow_main(meadow_argv_2cd0577=None):
    if meadow_argv_2cd0577 is None:
        meadow_argv_2cd0577 = meadow_sys.argv[1:]
    meadow_parser_5ad91fb = meadow_argparse.ArgumentParser(description='Parse and display type information from an IDA Pro database.')
    meadow_parser_5ad91fb.add_argument('idb', type=meadow_argparse.FileType('rb'), help='Path to input idb file')
    meadow_args_f68ec95 = meadow_parser_5ad91fb.parse_args(args=meadow_argv_2cd0577)
    meadow_til_local_6cca4bd = meadow_idb.from_buffer(_name_boundary.attributes(_name_boundary.attributes(meadow_args_f68ec95)['idb'])['read']()).til
    for meadow__def_local_bbdc9c9 in _name_boundary.attributes(meadow_til_local_6cca4bd)['types'].defs:
        print(_name_boundary.attributes(meadow__def_local_bbdc9c9.type)['get_typestr']())
    return 0
if __name__ == '__main__':
    meadow_sys.exit(meadow_main())
_name_boundary.module_contract(globals(), {'VStruct': 'meadow_VStruct', 'idb': 'meadow_idb', 'TILBucket': 'meadow_TILBucket', 'json': 'meadow_json', 'TInfo': 'meadow_TInfo', 'TILTypeInfo': 'meadow_TILTypeInfo', 'TILEncoder': 'meadow_TILEncoder', 'argparse': 'meadow_argparse', 'sys': 'meadow_sys', 'v_prim': 'meadow_v_prim', 'main': 'meadow_main'})
