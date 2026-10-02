# Derived from python-idb; original copyright/license retained in ORIGIN.md.
"""Offline IDB access from a stable, bounded local snapshot."""
import idbmeadow.api_contract as _name_boundary
__boundary_names__ = {'netnode': 'node_records', 'fileformat': 'database_pages', 'typeinf': 'type_records', 'typeinf_flags': 'type_codes', 'analysis': 'semantic_views', 'idapython': 'ida_interfaces', 'shim': 'script_environment'}
import contextlib as meadow_contextlib
import six as meadow_six
from idbmeadow.ida_interfaces import meadow_IDAPython
from idbmeadow.bounded_io import (
    DEFAULT_LIMITS as meadow_DEFAULT_LIMITS,
    read_regular as meadow_read_regular,
)

@_name_boundary.callable_contract({'buf': 'meadow_buf'}, 'memview')
def meadow_memview(meadow_buf):
    # The public low-level helper keeps its borrowed-view contract. IDB owns
    # its own bytes independently of this helper and any caller mutation.
    return memoryview(meadow_buf)

@meadow_contextlib.contextmanager
@_name_boundary.callable_contract({'path': 'meadow_path', 'limits': 'meadow_limits'}, 'from_file')
def meadow_from_file(meadow_path, *, meadow_limits=meadow_DEFAULT_LIMITS):
    from idbmeadow.database_pages import meadow_IDB
    meadow_data = meadow_read_regular(meadow_path, meadow_limits)
    meadow_db = meadow_IDB(meadow_data, limits=meadow_limits)
    meadow_db.vsParse(meadow_data)
    yield meadow_db

@_name_boundary.callable_contract({'buf': 'meadow_buf', 'limits': 'meadow_limits'}, 'from_buffer')
def meadow_from_buffer(meadow_buf, *, meadow_limits=meadow_DEFAULT_LIMITS):
    from idbmeadow.database_pages import meadow_IDB
    meadow_db = meadow_IDB(meadow_buf, limits=meadow_limits)
    meadow_db.vsParse(meadow_db.buf)
    return meadow_db
_name_boundary.module_contract(globals(), {'from_file': 'meadow_from_file', 'IDAPython': 'meadow_IDAPython', 'contextlib': 'meadow_contextlib', 'from_buffer': 'meadow_from_buffer', 'six': 'meadow_six', 'memview': 'meadow_memview', 'netnode': 'node_records', 'fileformat': 'database_pages', 'typeinf': 'type_records', 'typeinf_flags': 'type_codes', 'analysis': 'semantic_views', 'idapython': 'ida_interfaces', 'shim': 'script_environment'})
