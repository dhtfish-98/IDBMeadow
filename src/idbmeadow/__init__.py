# Derived from idb/__init__.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
__boundary_names__ = {'netnode': 'node_records', 'fileformat': 'database_pages', 'typeinf': 'type_records', 'typeinf_flags': 'type_codes', 'analysis': 'semantic_views', 'idapython': 'ida_interfaces', 'shim': 'script_environment'}
import contextlib as meadow_contextlib
import six as meadow_six
from idbmeadow.ida_interfaces import meadow_IDAPython as meadow_IDAPython
if meadow_six.PY2:

    @_name_boundary.callable_contract({'buf': 'meadow_buf_local_7dd09cb'}, 'memview')
    def meadow_memview(meadow_buf_local_7dd09cb):
        return meadow_buf_local_7dd09cb
else:

    @_name_boundary.callable_contract({'buf': 'meadow_buf_local_e9988d5'}, 'memview')
    def meadow_memview(meadow_buf_local_e9988d5):
        return memoryview(meadow_buf_local_e9988d5)

@meadow_contextlib.contextmanager
@_name_boundary.callable_contract({'path': 'meadow_path_b39bcad'}, 'from_file')
def meadow_from_file(meadow_path_b39bcad):
    import idbmeadow.database_pages as _boundary_import_idb_fileformat
    import idbmeadow as meadow_idb
    with open(meadow_path_b39bcad, 'rb') as meadow_f_4bdc7c7:
        meadow_buf_local_502a9de = meadow_memview(_name_boundary.attributes(meadow_f_4bdc7c7)['read']())
        meadow_db_357c5df = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['fileformat'])['IDB'](meadow_buf_local_502a9de)
        meadow_db_357c5df.vsParse(meadow_buf_local_502a9de)
        yield meadow_db_357c5df

@_name_boundary.callable_contract({'buf': 'meadow_buf_local_9efcf72'}, 'from_buffer')
def meadow_from_buffer(meadow_buf_local_9efcf72):
    import idbmeadow.database_pages as _boundary_import_idb_fileformat
    import idbmeadow as meadow_idb
    meadow_buf_local_9efcf72 = meadow_memview(meadow_buf_local_9efcf72)
    meadow_db_bad0638 = _name_boundary.attributes(_name_boundary.attributes(meadow_idb)['fileformat'])['IDB'](meadow_buf_local_9efcf72)
    meadow_db_bad0638.vsParse(meadow_buf_local_9efcf72)
    return meadow_db_bad0638
_name_boundary.module_contract(globals(), {'from_file': 'meadow_from_file', 'IDAPython': 'meadow_IDAPython', 'contextlib': 'meadow_contextlib', 'from_buffer': 'meadow_from_buffer', 'six': 'meadow_six', 'memview': 'meadow_memview', 'netnode': 'node_records', 'fileformat': 'database_pages', 'typeinf': 'type_records', 'typeinf_flags': 'type_codes', 'analysis': 'semantic_views', 'idapython': 'ida_interfaces', 'shim': 'script_environment'})
