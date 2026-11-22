# Release Validation - 1.0.0

Validated on 2026-11-22, Python 3.12.3, Linux. Everything below was executed; nothing is estimated.

## Results
| Check | Command | Result |
|---|---|---|
| Repository validator (incl. JSON Schema meta-validation, version consistency, scanner pins, CI SHA pinning, Markdown links) | `python tools/validate_repository.py` | PASS |
| Test suite | `python -m unittest discover -s tests -v` | 49 tests, 0 failures |
| End-to-end demo | `bash examples/demo.sh` | Behaves as documented (see `docs/demo/TRANSCRIPT.md`) |
| Clean-copy run | Extracted archive into a fresh directory, re-ran validator and tests | PASS |

Tests by group:

| Test class | Tests |
|---|---|
| `test_project_lifecycle.ProjectLifecycleTests` | 5 |
| `test_runtime_hardening.ApprovalTests` | 4 |
| `test_runtime_hardening.ExecutionTests` | 6 |
| `test_runtime_hardening.GateAndFindingTests` | 8 |
| `test_runtime_hardening.ReadinessTests` | 7 |
| `test_runtime_hardening.RegistryAndReleaseTests` | 6 |
| `test_runtime_hardening.ReviewAndMemoryTests` | 3 |
| `test_workforce_registry.WorkforceRegistryTests` | 4 |
| `test_workforce_runtime.WorkforceTests` | 6 |

## Defects in 4.0.0 reproduced, fixed and covered by a regression test
1. Approval accepted any name (`--approver claude`).
2. Task moved to READY while its dependency was still PLANNED.
3. Approval digest stored but never re-checked; changed scope was not tied to approval.
4. Success could be declared with no evidence path.
5. Audit events could be edited without detection.
6. Quick-start command path did not exist; entry prompt contradicted README.
7. Test roles could not request `execute`; "independent" reviewers could request `write`.
8. Gate evidence logs could be altered after recording (found during this validation; fixed).
9. Re-submitting a plan failed whenever any finished task was included (found during this validation; fixed).

## Security-tool pins (resolved 2026-11-22 via `git ls-remote`)
| ID | Tool | Ref | Commit | License (keyword-detected) |
|---|---|---|---|---|
| SEC-001 | Strix | v1.7.1 | `685bbc8138d3` | Apache-2.0 |
| SEC-002 | Cloudflare Security Audit Skill | default branch HEAD | `c1c8a8c14710` | MIT-style |
| SEC-003 | Trivy | v0.76.2 | `3f6334d223b5` | Apache-2.0 |
| SEC-004 | Nuclei | v3.11.1 | `a8c88feb4a1c` | MIT-style |
| SEC-005 | TruffleHog | v3.100.0 | `d232362a64a0` | AGPL-3.0 |
| SEC-006 | NVIDIA SkillSpector | v2.13.6 | `e2674da339b0` | Apache-2.0 |
| SEC-007 | Semgrep | v1.186.0 | `a5844e7c2d9d` | LGPL |
| SEC-008 | OpenAI Codex Security | default branch HEAD | `dcb270ceb2ee` | Apache-2.0 |
| SEC-009 | ClamAV | clamav-1.5.5 | `fef3d620025b` | UNRESOLVED: read the repository license before use |
| SEC-010 | Claude Code Security Review | default branch HEAD | `0c6a49f1fa56` | MIT-style |
| SEC-011 | BLA - Blind LLM Agents | v3.2.3 | `889f7ea5caa3` | MIT-style |
| SEC-012 | Microsoft PyRIT | v1.2.1 | `c7b5789d7443` | MIT-style |
| CI-001 | actions/checkout | v7.0.1 | `3d3c42e5aac5` | MIT-style |
| CI-002 | actions/setup-python | v7.1.0 | `6d4fd22b2046` | MIT-style |

Pins prove a ref existed on that date. They do not prove the tool is safe; signatures/checksums were not verified.

## NOT validated (do not claim these)
- Behaviour on Windows/macOS (process limits use POSIX `resource`; `examples/demo.sh` uses GNU `sed -i`).
- Python 3.10 and 3.11 (only 3.12 was available; CI runs the matrix).
- Real interactive-terminal approvals (tested with a mocked TTY).
- Running any of the 12 security tools; only their pinning and the `check run` wiring.
- Any AI tool (Claude Code, Cursor, Antigravity, Kimi, Qwen, ChatGPT...) following the rules; the conformance matrix is empty by design.
- Independence of a reviewer: `review-package` builds the input; isolation is the host's job.
- Sandboxing, network isolation, concurrency with multiple writers, large projects, performance.

## Residual limits
The ledger is tamper-evident, not tamper-proof; `policy.json` is a plain file; `--non-interactive` can be typed by anyone (it is recorded and the default gate rejects it for sensitive actions). See `docs/framework/RULES-AND-ENFORCEMENT.md` section 5.
