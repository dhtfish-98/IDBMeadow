#!/usr/bin/env python
# Derived from scripts/dump_section_list.py; original copyright and license retained in ORIGIN.md.
import idbmeadow.api_contract as _name_boundary
import idc as meadow_idc
import idaapi as meadow_idaapi
import idautils as meadow_idautils

@_name_boundary.callable_contract({}, 'print_section_list')
def meadow_print_section_list():
    for meadow_s_local_5953b94 in _name_boundary.attributes(meadow_idautils)['Segments']():
        meadow_seg_local_6174a36 = _name_boundary.attributes(meadow_idaapi)['getseg'](meadow_s_local_5953b94)
        print('%s' % _name_boundary.attributes(meadow_idc)['SegName'](meadow_s_local_5953b94))
        print(' - start address: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['startEA'])
        print(' - sclass: 0x%x' % meadow_seg_local_6174a36.sclass)
        print(' - orgbase: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['orgbase'])
        print(' - flags: 0x%x' % meadow_seg_local_6174a36.flags)
        print(' - align: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['align'])
        print(' - comb: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['comb'])
        print(' - perm: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['perm'])
        print(' - bitness: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['bitness'])
        print(' - sel: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['sel'])
        print(' - type: 0x%x' % meadow_seg_local_6174a36.type)
        print(' - color: 0x%x' % _name_boundary.attributes(meadow_seg_local_6174a36)['color'])
meadow_print_section_list()
_name_boundary.module_contract(globals(), {'idc': 'meadow_idc', 'print_section_list': 'meadow_print_section_list', 'idautils': 'meadow_idautils', 'idaapi': 'meadow_idaapi'})
