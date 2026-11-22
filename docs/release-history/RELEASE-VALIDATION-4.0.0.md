# AISDF v4.0.0 — Local Release Validation

Validation was executed against this extracted repository on the build host.

| Check | Result | Notes |
|---|---|---|
| Existing repository validator | PASS | JSON Schema meta-validation, 56 engine specs, legacy schemas and required root files |
| Python unit/integration tests | PASS | 15 tests passed |
| Workforce manifest registry | PASS | 72 unique worker manifests and matching role contracts |
| Team registry consistency | PASS | All registered worker IDs resolve |
| Worker action boundary tests | PASS | Penetration testing and deployment remain explicitly gated |
| Task dependency graph | PASS | Ordering, missing dependencies and cycles tested |
| SQLite audit ledger | PASS | Event persistence tested |
| CLI initialization | PASS | PROJECT.md and AGENTS.md created in disposable project |
| CLI planning | PASS | 3-task DAG planned in disposable project |
| CLI human approval | PASS | Approval event and task digest recorded |
| CLI status | PASS | Task state and event count displayed |
| Root README and v4 guide links | PASS | Local relative links checked |
| ZIP integrity | To be recorded after packaging | See final package checksum |

## Explicit limitations

- No LLM/provider adapter is bundled or certified.
- No autonomous code execution is enabled.
- No OS-level sandbox is included.
- Security scanners are not installed or certified by this package.
- Role catalogue maturity is L1_DEFINED; role manifests do not establish autonomous specialist competence.
- No remote GitHub Actions run or production deployment was performed.

This report is a local validation record, not a production certification.
