# Validation

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
