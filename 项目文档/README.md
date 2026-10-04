> 目录已整理：文档在「项目文档」，构建、缓存与暂存输入在「Build」。从仓库根目录运行 `python3 构建.py --build`；如需使用本文原有源码命令，先运行 `python3 构建.py --stage --ci`，再进入 `Build/源码`。暂存会恢复原输入路径。现有版本和历史验证记录按各自提交理解。

# IDBMeadow

防御用途、实际能力及本轮验证范围见 [DEFENSIVE_SCOPE.md](<DEFENSIVE_SCOPE.md>)。

Offline IDA .idb/.i64 database pages, netnodes, types and emulated IDAPython views. Library parsing reads local bytes; the separately selected script runner executes caller-provided Python and is not a script sandbox. This is an attributed, reorganized derivative of python-idb, with scope-resolved binding/file/module renaming and explicit API/schema adapters. It supports lawful offline security research and static analysis. Upstream algorithms and history remain credited.

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

The verifier downloads the pinned python-idb source, compares the same offline inputs, builds a wheel/source distribution, verifies source, license and provenance bytes and consumes the wheel in an isolated temporary environment. Supply `--baseline PATH` to reuse a Git checkout of the exact recorded upstream commit. No binary fixture is executed. `--audit-only` checks the frozen source/asset bytes and executable modes. The workflow checks out its triggering commit before running the same command.

## Structure

bounded_io owns stable local input and aggregate materialization limits; database_pages owns containers and B-tree pages; node_records owns netnode keys; type_records/type_codes own type metadata; semantic_views exposes recovered objects; ida_interfaces exposes offline IDA API views; script_environment and offline_tools isolate existing script integration. api_contract separates wire/schema/IDA display labels from renamed bindings.

See [ORIGIN.md](<ORIGIN.md>), [VALIDATION.md](<VALIDATION.md>), `SYMBOL_MAP.json`, `FILE_MAP.json`, `NAME_AUDIT.json` and `SOURCE_MANIFEST.json` for source/licensing, measured evidence, exact naming exceptions and file hashes.

## 1.0.3 verifier patch

The verifier now checks the actual directory entry name before clearing generated
`build` output. On a case-insensitive filesystem, `build` can otherwise resolve
to the retained `Build` tree when the full verifier runs from a root containing
that tree. The cleanup also refuses symlinks and non-directory entries. This
patch changes verification and packaging metadata; the 22 runtime Python files
and their public API are unchanged. The complete 1.0.2 validation record is
preserved at [历史/1.0.2/CURRENT_VALIDATION.json](<历史/1.0.2/CURRENT_VALIDATION.json>).
The wheel includes that archive beside this README under the same relative
path. The current patch's measured results are in `CURRENT_VALIDATION.json`.

## 1.0.2 parser phase

The public `from_file` / `from_buffer` calls now own bounded immutable bytes.
`from_file` requires a local regular file, rejects a final symlink, and checks
observed identity/size/timestamps before and after the read. This is not proof
of an atomic filesystem snapshot against a concurrent writer. `memview` remains
a borrowed-view helper for compatibility.

Headers, physical section spans, complete zlib members, flag/name page storage,
and TIL bucket records have new implementations. A single parse budget covers
all sections and nested type buckets. Defaults are 256 MiB encoded input,
1 GiB decoded bytes per section/bucket, 2 GiB aggregate materialized bytes and
1,000,000 type definitions. These explicit ceilings are configurable using
`idbmeadow.bounded_io.ParseLimits` and `limits=` on either public entry point.
The high-address upstream fixture genuinely contains more than 512 MiB of
decoded flag pages; smaller limits intentionally reject it.

Malformed/truncated input and exceeded limits raise `IDBFormatError`, a
`ValueError` subclass. Database parsing starts at offset zero; standalone
section/bucket parsing accepts a checked offset. Encoded compression methods
other than 0 and 2 and trailing bytes after a zlib member are rejected.
The fixed physical header layouts 1/4 and 5/6 are exercised by the retained
fixtures. Legacy flag-page padding and legacy NAM header interpretation are
preserved for compatibility, with declared allocation sizes replaced by actual
bounded bytes; this does not validate every legacy format interpretation.

This phase is partial. B-tree search/cursor semantics, netnode/semantic readers,
type-language recursion, IDAPython views and script/export tools still contain
inherited algorithms. Query CPU, all cached objects, report length and explicit
script execution are not governed by the section materialization budget.
See `历史/1.0.2/CURRENT_VALIDATION.json` for that version's exact source and
measured results.
