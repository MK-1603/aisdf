# Changelog

## 1.0.0 - Governed control plane
Versioning note: the public version is reset to 1.0.0. The earlier internal numbering (3.x, 4.0.0) is preserved in `docs/release-history/`; tag the old state `legacy-v4.0.0` before publishing. 1.0.0 stabilizes the CLI, ledger schema v2 and the task/evidence/finding/check formats. Provider adapters are **not** part of the 1.0 stability promise.

### Fixed (gaps found by testing 4.0.0)
- Approvals accepted any string, including AI names. Now only registered humans, with recorded assurance.
- Tasks could become READY before their dependencies succeeded. Now enforced.
- Approval digest was stored but never re-checked. Now re-verified at READY and RUN; changing a task revokes approval; completed tasks cannot be silently re-planned.
- Success could be asserted without evidence. Now only `run` or `complete --evidence` can record it.
- Audit events could be edited undetected. Now hash-chained; `verify-ledger` detects tampering.
- README quick start pointed at a non-existent `tools/aisdf_runtime/workforce.py`. Now `python aisdf.py`.
- `MASTER-ENTRY-PROMPT.md` contradicted the README about being a runtime. Reconciled.
- Test roles could not request `execute`; "independent" reviewers could request `write`. Permission profiles corrected and role docs generated from manifests.
- CI used a floating action tag. Now pinned by commit SHA.

### Added
- Governed local command executor (`run`, `check run`), release gate, findings workflow, independent-review package, memory checker and Obsidian-compatible vault template, `security/scanners.lock.json`, `security/policies/release-gate.json`, `adapters/COMPATIBILITY.md` and `CONFORMANCE.md`, `docs/framework/RULES-AND-ENFORCEMENT.md`, `docs/framework/POSITIONING-AND-ROADMAP.md`.

### Changed
- `docs/v4` -> `docs/framework`; old demo screenshots moved to `docs/demo/legacy-v4-captures/` (they predate the hardening); old release validations moved to `docs/release-history/`.

### Known limits
No sandbox, no model adapter, no bundled scanner execution, no multi-tool conformance results yet. See `IMPLEMENTATION-STATUS.md`.

## 4.0.0 (legacy numbering) - Workforce foundation
- Introduced specialist workforce catalogue with machine-readable worker manifests and role contracts.
- Added provider-neutral task, worker, capability and permission contracts.
- Added local Python control-plane runtime with registry, DAG validation, task lifecycle, policy checks, approval records, budgets and SQLite audit ledger.
- Added dedicated security operations architecture and authorized testing controls.
- Preserved prior AISDF domains, engines, workflows, EGM-inspired specifications, project lifecycle tools and MK Framework.
- Clarified maturity boundaries: no bundled LLM, no production sandbox, no certified security scanner integrations, and no claim of fully autonomous operation.
