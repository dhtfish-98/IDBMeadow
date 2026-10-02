# Origin

- Upstream: [python-idb](https://github.com/williballenthin/python-idb)
- Frozen commit: `5a313f27cf6200e2454eb08ef3b557227fc2e9d7`
- Frozen tree: `595a7dadafaf1260ee30764a0c9c098114940236`
- License: Apache-2.0; complete original license, author notices and retained source headers are included.

This project derives from upstream code and does not claim its original algorithms as newly invented. The original source checkout was read-only. Renaming uses LibCST assignment/reference scope identities, including a guard against same-spelling local/global shadowing, followed by AST routing of known module/member identities. Owned source files/modules and custom implementation bindings are renamed; reusable mechanisms are separated from format/API labels in api_contract.py.

## Required compatibility exceptions

- vstruct field labels, field order, vs*/pcb_* callbacks, binary flags, IDA module/member names and named-record fields remain data/framework contracts.
- Public IDA interfaces and schema names are explicit aliases/views. The namespace adapter preserves old labels for __dict__/dir operations without retaining an old implementation copy.
- Pytest hooks/fixture/parameter labels and standard Python interpreter conventions remain fixed.
- The single upstream IDA 7.6 function-name-extraction failure is strict XFAIL in the new suite; an unexpected pass fails that check.

Binary fixture filenames and bytes remain fixed comparison inputs. Required __init__.py, conftest.py, pyproject.toml and license filenames remain conventional tool/API contracts. Original executable modes and script shebang placement are preserved.

Ordinary local bindings are renamed even when their old spelling also appears in a fixed schema field. Scope-resolved local/global refinements are listed in SYMBOL_MAP.json. NAME_AUDIT.json and checks/naming_audit.py repeat the owned-source lexical audit.

Upstream packaging configuration is expressed in the new pyproject.toml. Distribution/module identity changes deliberately; parsing behavior, CLI flags and external data contracts are verified separately.
