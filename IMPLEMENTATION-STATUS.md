# Implementation Status — v4.0.0

| Capability | Status | Evidence |
|---|---|---|
| 31 engineering domains | DOCUMENTED | `00-...` through `30-...` |
| 56 engine specifications | SPECIFIED | `engines/` |
| WF-001–WF-013 | SPECIFIED | `workflows/` |
| Specialist role catalogue | IMPLEMENTED AS CONTRACTS | `workforce/teams/` and `workforce/registry/` |
| Worker manifest validation | IMPLEMENTED | `runtime/aisdf_runtime/workforce.py` |
| Task DAG validation | IMPLEMENTED | runtime tests |
| Task state transitions | IMPLEMENTED | runtime tests |
| Permission policy checks | IMPLEMENTED | runtime tests |
| Human approval record | IMPLEMENTED | runtime tests |
| Task budgets | IMPLEMENTED | runtime tests |
| SQLite audit ledger | IMPLEMENTED | runtime tests |
| Model/provider execution | ADAPTER CONTRACT ONLY | `runtime/adapters/` |
| OS sandbox | NOT INCLUDED | external sandbox required |
| Persistent autonomous agents | NOT INCLUDED | requires configured execution adapter and scheduler |
| Security scanner execution | NOT INCLUDED BY DEFAULT | tool installation and certification required |
| Production deployment | NOT CERTIFIED | environment-specific validation required |

A role prompt or manifest does not establish autonomous capability. See `docs/v4/MATURITY-MODEL.md`.
