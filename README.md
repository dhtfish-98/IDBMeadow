# IDBMeadow

防御用途、实际能力及本轮验证范围见 [DEFENSIVE_SCOPE.md](DEFENSIVE_SCOPE.md)。

Read-only offline IDA .idb/.i64 database pages, netnodes, types and emulated IDAPython views. This is an attributed, reorganized derivative of python-idb, with scope-resolved binding/file/module renaming and explicit API/schema adapters. It supports lawful offline security research and static analysis. Upstream algorithms and history remain credited.

## Install and use

Runtime package metadata supports Python >=3.9. The pinned verification dependencies require Python >=3.10; use Python 3.12 for the commands below. Recorded checks use Python 3.12.13; Python 3.9 execution has not been measured.

```python
import idbmeadow
from idbmeadow import semantic_views
with idbmeadow.meadow_from_file("sample.idb") as database:
    root = semantic_views.meadow_Root(database)
    print(database.wordsize, root.version, root.md5)
```

## Verification

```sh
python -m pip install '.[test]'
python verify.py --runslow
```

The verifier downloads pinned upstream source (and the pinned PE test repository for PEQuarry), compares the same offline inputs, builds a wheel/source distribution, verifies every Python file inside the wheel and consumes that wheel in a separate temporary environment. Supply `--baseline PATH` and `--pe-tests PATH` to reuse existing local checkouts. No binary fixture is executed. `--audit-only` checks the frozen source/asset bytes and executable modes. The workflow checks out its triggering commit before running the same command.

## Structure

database_pages owns containers and B-tree pages; node_records owns netnode keys; type_records/type_codes own type metadata; semantic_views exposes recovered objects; ida_interfaces exposes offline IDA API views; script_environment and offline_tools isolate existing script integration. api_contract separates wire/schema/IDA display labels from renamed bindings.

See [ORIGIN.md](ORIGIN.md), [VALIDATION.md](VALIDATION.md), `SYMBOL_MAP.json`, `FILE_MAP.json`, `NAME_AUDIT.json` and `SOURCE_MANIFEST.json` for source/licensing, measured evidence, exact naming exceptions and file hashes.
