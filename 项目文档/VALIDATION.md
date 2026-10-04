# Validation

## Historical renamed baseline (before 1.0.2)

Recorded environment: macOS Apple Silicon, Python 3.12.13, Capstone 5.0.6, pytest 9.1.1. IDB dependencies: vivisect-vstruct-wb 1.0.3, six 1.17.0, cached-property 2.0.1, hexdump 3.3.

PASS: complete 800-case emulated IDA API suite. PASS: 47 database fixtures plus 4 malformed buffers, comparing metadata, segment fields, sampled functions/names, address bounds and errors; process-specific memoryview addresses in error messages are normalized. The pinned original complete suite with slow tests recorded 1651 passes and one IDA 7.6 function-name extraction failure. The final renamed complete suite with --runslow records 1651 passes and one strict XFAIL, zero unexpected failures/errors, in 793.91 seconds.

## Limits and pre-existing gaps

- OPEN: The upstream repository is archived (GitHub archived=true checked on 2026-10-02). Its documented database scope is IDA 5.0–7.5. IDA 7.6 function-name extraction fails in the pinned original and remains unsupported; IDA 8/9 formats are not claimed.
- OPEN: Some upstream signature assertions use truthy singleton tuples; their warning is retained and separate exact observation comparisons cover representative recovered values.
- OPEN: The parser is read-only. No embedded sample was executed, no live IDA database was changed, and arbitrary user scripts/live IDA integration were not validated.

Local automated checks, installable-package consumption, source identity and remote GitHub workflow results are distinct evidence. Remote CI is not presumed from a local pass. No application/verification-program approval or independent authorship claim follows from these checks.

GitHub Actions runs the default bounded test suite plus pinned upstream observations and wheel identity. The complete `--runslow` suite required about 13 minutes on the recorded local Mac; one remote attempt was canceled after 10 minutes, so its local result above is separate evidence rather than a remote full-suite pass.

Fixture provenance: the bundled database files come from the pinned upstream tests/data, retain those original bytes and embedded source metadata, and are not claimed as newly authored samples.

PASS: lexical name audit of 32 mapped owned Python files; 4059 binding-map records and zero ordinary unrenamed function/comprehension bindings. PASS: two independent wheel-consumer checks in a fresh temporary environment, with every installed Python source file compared byte-for-byte. NAME_AUDIT.json records the permitted fixed global contracts.

## 2026-10-02 capability review

The current runtime entry points, file/process/network capabilities and attribution were reviewed. See DEFENSIVE_SCOPE.md for the exact paths and remaining limitations. This documentation update does not claim another execution of the historical full test suite, a rewrite of every upstream algorithm, or CVP eligibility. GitHub CI for the new commit is separate evidence.

## 1.0.2 current parser phase

PASS: 116 owned boundary cases cover exact and truncated headers, regular-file
and mutable-buffer input, read failure descriptor closure, concurrent file
changes, declared-size allocation prevention, complete/limited zlib members,
shared section/TIL budgets, type record fields and ordinal widths, physical
section overlaps, independent flag values and finite name tables.

PASS: all 47 retained database observations exactly match the fixed upstream.
The four malformed observations have individually asserted old and new error
messages. The 98 owned header/section/bucket/page observations include 80 exact
matches, two fixed layout validation corrections, ten actual-consumed page end
corrections and six compressed TIL cases whose old length exception is replaced
by independently asserted record names, ordinals, type bytes, comments and
consumed lengths. No generic difference exemption is permitted.

PASS: the final current runtime complete suite returned process exit 0 with
1,767 passes and one retained strict XFAIL in 937.21 seconds. Its 22 runtime
source hashes were checked identical before and after execution.

The 1.0.2 complete slow-suite status, runtime file hashes, source identity and
package consumption are preserved in
`历史/1.0.2/CURRENT_VALIDATION.json` and the release evidence. The historical
1,651-case results above are not silently reused as this phase's execution.

OPEN: the runtime is only partially rewritten. Inherited B-tree strategies,
cursors, semantic and IDAPython queries, type-language recursion and script
tools remain for later phases. The finite section budget does not establish
a universal memory/CPU/output bound for those operations. Legacy flag padding
and NAM interpretation are retained for observation compatibility, not newly
proven for all legacy IDA versions. The original strict 7.6 XFAIL remains.

## 1.0.3 verifier patch (2026-10-04)

The old `ROOT / 'build'` cleanup could resolve to a retained `Build` directory
on a case-insensitive filesystem if the full verifier reached that step from a
root containing `Build`. No prior deletion was observed. The normal staged
`Build/源码` workflow and the existing Ubuntu CI run had no observed deletion.
The verifier now removes only a real directory entry named exactly `build` and
refuses a symlink or non-directory entry.

Four focused cleanup tests passed on the local case-insensitive macOS volume.
They check that an uppercase `Build` sentinel survives, a real lowercase
`build` is removed, and symlink and regular-file entries are rejected. The
first local source candidate's default suite passed with 1,612 passes and 160
skips in 71.58 seconds.
A fresh staged 1.0.3 candidate also passed the complete slow suite with 1,771
passes, one strict XFAIL and 13 warnings in 1000.57 seconds, followed by the
pinned observations, package identity and isolated wheel-consumer checks. That
candidate preceded the final wheel change that adds the archived validation
JSON. The final package is rebuilt and checked separately with the default
suite; the slow result does not claim execution against its final wheel bytes.

The 13 warnings identify pre-existing `assert (condition,)` expressions in
`checks/test_meadow_analysis.py`. Each asserts a nonempty tuple, so those
signature equalities remain OPEN despite the suite passes. Correcting those
tests and rerunning them is separate work. The 22 runtime Python files remain
byte-identical to 1.0.2. Current patch results are in CURRENT_VALIDATION.json;
the original 1.0.2 complete slow-suite record is preserved byte-for-byte at
`历史/1.0.2/CURRENT_VALIDATION.json`. Remote CI is separate.
