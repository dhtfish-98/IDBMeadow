# Derived from idb/shim.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import sys as meadow_sys
if meadow_sys.version_info[0] == 2:
    import imp as meadow_imp
    import sys as meadow_sys
    import logging as meadow_logging
    import idbmeadow as meadow_idb
    meadow_logger = meadow_logging.getLogger(__name__)

    @_name_boundary.class_contract('HookedImporter', {'find_module': 'meadow_find_module', 'load_module': 'meadow_load_module', 'install': 'meadow_install', 'hooks': 'meadow_hooks'})
    class meadow_HookedImporter(object):

        @_name_boundary.callable_contract({'self': 'meadow_self_ec86adc', 'hooks': 'meadow_hooks_ad63887'}, '__init__')
        def __init__(meadow_self_ec86adc, meadow_hooks_ad63887=None):
            super(meadow_HookedImporter, meadow_self_ec86adc).__init__()
            _name_boundary.attributes(meadow_self_ec86adc)['hooks'] = meadow_hooks_ad63887

        @_name_boundary.callable_contract({'self': 'meadow_self_e31c60a', 'fullname': 'meadow_fullname_5a0ddbc', 'path': 'meadow_path_c4872e4'}, 'find_module')
        def meadow_find_module(meadow_self_e31c60a, meadow_fullname_5a0ddbc, meadow_path_c4872e4=None):
            meadow_logger.info('find_module: fullname: %s, path=%s', meadow_fullname_5a0ddbc, meadow_path_c4872e4)
            if meadow_fullname_5a0ddbc not in _name_boundary.attributes(meadow_self_e31c60a)['hooks']:
                return None
            return meadow_self_e31c60a

        @_name_boundary.callable_contract({'self': 'meadow_self_ce9f3f4', 'fullname': 'meadow_fullname_a750387'}, 'load_module')
        def meadow_load_module(meadow_self_ce9f3f4, meadow_fullname_a750387):
            meadow_logger.info('load_module: fullname: %s', meadow_fullname_a750387)
            meadow_mod_1476761 = _name_boundary.attributes(meadow_self_ce9f3f4)['hooks'][meadow_fullname_a750387]
            meadow_newmod_d4ff636 = meadow_sys.modules.setdefault(meadow_fullname_a750387, meadow_imp.new_module(meadow_fullname_a750387))
            meadow_newmod_d4ff636.__file__ = meadow_sys.modules[meadow_mod_1476761.__module__].__file__
            meadow_newmod_d4ff636.__loader__ = meadow_self_ce9f3f4
            meadow_newmod_d4ff636.__package__ = ''
            for meadow_attr_1e11789 in _name_boundary.public_names(meadow_mod_1476761):
                if meadow_attr_1e11789.startswith('__') and meadow_attr_1e11789 != '__EA64__':
                    continue
                _name_boundary.namespace_view(meadow_newmod_d4ff636)[meadow_attr_1e11789] = _name_boundary.read_attribute(meadow_mod_1476761, meadow_attr_1e11789)
            return meadow_newmod_d4ff636

        @_name_boundary.callable_contract({'self': 'meadow_self_c007ade'}, 'install')
        def meadow_install(meadow_self_c007ade):
            meadow_sys.meta_path.insert(0, meadow_self_c007ade)
elif meadow_sys.version_info[0] == 3:
    import sys as meadow_sys
    import types as meadow_types
    import logging as meadow_logging
    import importlib.abc as _boundary_import_importlib_abc
    import importlib as meadow_importlib
    import importlib.util as _boundary_import_importlib_util
    import importlib as meadow_importlib
    import idbmeadow as meadow_idb
    meadow_logger = meadow_logging.getLogger(__name__)

    @_name_boundary.class_contract('HookedImporter', {'find_spec': 'meadow_find_spec', 'create_module': 'meadow_create_module', 'exec_module': 'meadow_exec_module', 'install': 'meadow_install', 'hooks': 'meadow_hooks'})
    class meadow_HookedImporter(meadow_importlib.abc.MetaPathFinder, meadow_importlib.abc.Loader):

        @_name_boundary.callable_contract({'self': 'meadow_self_3076ca3', 'hooks': 'meadow_hooks_05e455b'}, '__init__')
        def __init__(meadow_self_3076ca3, meadow_hooks_05e455b=None):
            _name_boundary.attributes(meadow_self_3076ca3)['hooks'] = meadow_hooks_05e455b

        @_name_boundary.callable_contract({'self': 'meadow_self_173cd6b', 'path': 'meadow_path_d65b346', 'target': 'meadow_target_2a3cf7d', 'name': 'meadow_name_local_89f3e47'}, 'find_spec')
        def meadow_find_spec(meadow_self_173cd6b, meadow_name_local_89f3e47, meadow_path_d65b346, meadow_target_2a3cf7d=None):
            if meadow_name_local_89f3e47 not in _name_boundary.attributes(meadow_self_173cd6b)['hooks']:
                return None
            meadow_spec_0023e26 = meadow_importlib.util.spec_from_loader(meadow_name_local_89f3e47, meadow_self_173cd6b)
            return meadow_spec_0023e26

        @_name_boundary.callable_contract({'self': 'meadow_self_00803b8', 'spec': 'meadow_spec_aa3a824'}, 'create_module')
        def meadow_create_module(meadow_self_00803b8, meadow_spec_aa3a824):
            meadow_logger.info('hooking import: %s', meadow_spec_aa3a824.name)
            meadow_module_67a670d = meadow_types.ModuleType(meadow_spec_aa3a824.name)
            meadow_module_67a670d.__loader__ = meadow_self_00803b8
            meadow_module_67a670d.__package__ = ''
            meadow_mod_fed9117 = _name_boundary.attributes(meadow_self_00803b8)['hooks'][meadow_spec_aa3a824.name]
            for meadow_attr_7e5fba3 in _name_boundary.public_names(meadow_mod_fed9117):
                if meadow_attr_7e5fba3.startswith('__') and meadow_attr_7e5fba3 != '__EA64__':
                    continue
                _name_boundary.namespace_view(meadow_module_67a670d)[meadow_attr_7e5fba3] = _name_boundary.read_attribute(meadow_mod_fed9117, meadow_attr_7e5fba3)
            return meadow_module_67a670d

        @_name_boundary.callable_contract({'self': 'meadow_self_57b61d1', 'module': 'meadow_module_273f058'}, 'exec_module')
        def meadow_exec_module(meadow_self_57b61d1, meadow_module_273f058):
            return

        @_name_boundary.callable_contract({'self': 'meadow_self_532f591'}, 'install')
        def meadow_install(meadow_self_532f591):
            meadow_sys.meta_path.insert(0, meadow_self_532f591)

@_name_boundary.callable_contract({'db': 'meadow_db_2dae853', 'ScreenEA': 'meadow_ScreenEA_f410e66'}, 'install')
def meadow_install(meadow_db_2dae853, meadow_ScreenEA_f410e66=None):
    if meadow_ScreenEA_f410e66 is None:
        meadow_ScreenEA_f410e66 = list(sorted(_name_boundary.attributes(_name_boundary.attributes(meadow_idb)['analysis'])['Segments'](meadow_db_2dae853).segments.keys()))[0]
    meadow_api_local_1d6fa8b = _name_boundary.attributes(meadow_idb)['IDAPython'](meadow_db_2dae853, ScreenEA=meadow_ScreenEA_f410e66)
    meadow_hooks_234b71e = {'idc': _name_boundary.attributes(meadow_api_local_1d6fa8b)['idc'], 'idaapi': _name_boundary.attributes(meadow_api_local_1d6fa8b)['idaapi'], 'idautils': _name_boundary.attributes(meadow_api_local_1d6fa8b)['idautils'], 'ida_funcs': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_funcs'], 'ida_bytes': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_bytes'], 'ida_netnode': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_netnode'], 'ida_nalt': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_nalt'], 'ida_name': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_name'], 'ida_entry': _name_boundary.attributes(meadow_api_local_1d6fa8b)['ida_entry']}
    meadow_importer_4963521 = meadow_HookedImporter(hooks=meadow_hooks_234b71e)
    _name_boundary.attributes(meadow_importer_4963521)['install']()
    return meadow_hooks_234b71e
_name_boundary.module_contract(globals(), {'install': 'meadow_install', 'imp': 'meadow_imp', 'logging': 'meadow_logging', 'idb': 'meadow_idb', 'logger': 'meadow_logger', 'HookedImporter': 'meadow_HookedImporter', 'types': 'meadow_types', 'importlib': 'meadow_importlib', 'sys': 'meadow_sys'})
