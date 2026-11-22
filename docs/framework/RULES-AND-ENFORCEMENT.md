# How AISDF Rules Actually Work

AISDF has **two enforcement systems**. Confusing them is the most common way to overclaim.

| System | What it is | Who enforces it | Strength |
|---|---|---|---|
| **A. Written rules** | Markdown the AI must read and follow: entry prompt, 12 principles, 20 rules, precedence, role contracts, 56 engines, 13 workflows | The AI tool itself, then a human or an independent reviewer | Depends on the model obeying; **not** machine-checked |
| **B. The runtime** | `python aisdf.py ...` (`runtime/aisdf_runtime/workforce.py`) | Code, plus a SQLite ledger and the release gate | Deterministic and tested, but a local tool, **not** an OS security boundary |

## 1. The instruction stack (System A)

1. **Entry:** `AGENTS.md` / `MASTER-ENTRY-PROMPT.md` tell any AI tool to read `PROJECT.md`, choose a mode, state its role and permissions, and separate facts, decisions, assumptions and unknowns before acting.
2. **Principles** (`AISDF-CORE-PRINCIPLES.md`): evidence over claims, approval first, least privilege, independent verification, honest limitations.
3. **Rules R01–R20** (`00-GOVERNANCE/AISDF-RULEBOOK.md`), applied to humans and AI.
4. **Precedence** (`RULE-PRECEDENCE-AND-CONFLICT-RESOLUTION.md`): law > platform safety > organization policy > AISDF rules > project baseline > workflow > task > chat. A lower level can never override a higher one. An equal-level conflict stops the work for a human decision.
5. **Waivers:** need rule ID, owner, rationale, compensating controls, residual risk and an expiry date. Safety and legal rules cannot be waived. The runtime enforces this for gate checks (`check record --status WAIVED`).
6. **No-fake-execution** (`30-AGENT-RULES-AND-VERIFICATION/`): an AI may only report PLANNED, ATTEMPTED, SUCCEEDED, FAILED, NOT_RUN, BLOCKED or NOT_VERIFIED, and only with evidence.
7. **Process:** modes, engines and workflows WF-001…WF-013 say *how* to do each kind of work and what shape the output takes.

## 2. What the runtime enforces (System B)

| Control | How it works | Tested in |
|---|---|---|
| Worker permissions | `plan` rejects an action the worker may not request; each role has a permission profile in its manifest | `test_workforce_registry`, `test_runtime_hardening` |
| Human approver allow-list | Only people in `.aisdf/policy.json` can approve, complete tasks, disposition findings or waive checks | `ApprovalTests` |
| Approval assurance | A terminal session is recorded as `interactive_tty`; unattended use needs `--non-interactive` and is recorded as weaker. The release gate refuses weaker approval for sensitive actions | `ApprovalTests`, `GateAndFindingTests` |
| Approval bound to content | Each task has a SHA-256 digest of its full content. Changing a task revokes its approval (`APPROVAL_REVOKED`) | `ReadinessTests` |
| Dependencies | A task cannot become READY until every dependency is SUCCEEDED | `ReadinessTests` |
| No fake success | `SUCCEEDED`/`FAILED` can only come from `run` (runtime-executed) or `complete` (human-attested, evidence file required) | `ReadinessTests` |
| Tamper-evident ledger | Events are hash-chained; `verify-ledger` detects edited or reordered history and edited task content | `test_ledger_tampering_detected` |
| Governed execution | `run` / `check run`: argv list only (no shell), executable allow-list (deny by default), cwd confined to project, scrubbed environment, timeout, CPU/file-size limits on POSIX, redacted logs, hashed evidence | `ExecutionTests` |
| Findings | Reviewer findings must match the EGM schema; only a registered human can dispose of them | `GateAndFindingTests` |
| Release gate | Blocks on non-terminal tasks, missing/failed/altered checks, unpinned tools, open serious findings, broken ledger, weak approvals | `GateAndFindingTests` |
| Independent-review input | `review-package` builds hashed reviewer input from requirements, tasks, evidence and diff, and excludes implementer memory/chat | `ReviewAndMemoryTests` |
| Memory hygiene | `memory-check` requires provenance, forbids unsupported `verified` authority, flags injection phrases | `ReviewAndMemoryTests` |

## 3. Rule-by-rule enforcement map

`CODE` = enforced by the runtime. `GATE` = checked at release from recorded evidence. `PROCESS` = instruction only; a reviewer or human must check it. "Partial" says what the code does *not* cover.

| Rule | Level | What is actually enforced |
|---|---|---|
| R01 Source of Truth | PROCESS | `review-package` and `memory-check` favour canonical sources; nothing stops an AI ignoring `PROJECT.md` |
| R02 User Intent | PROCESS | — |
| R03 Scope Lock | CODE (partial) | Approved task digest + revocation on change; cwd confinement. File-level diff scoping is **not** enforced |
| R04 Change Only Law | PROCESS | The reviewer receives the real diff |
| R05 No AI Slope | PROCESS | — |
| R06 Evidence over Claims | CODE | No success without runtime evidence or attached human evidence; hashed; gate re-verifies hashes |
| R07 Approval First | CODE | Allow-list, digest binding, revocation, assurance level |
| R08 Least Privilege | CODE (partial) | Per-role permissions, deny-by-default executables/env, read-only independent reviewers. **Not** OS isolation |
| R09 Secret Safety | CODE (partial) | Scrubbed env, log redaction of common token formats; `secrets-scan` is a required gate check. Redaction is pattern-based and can miss secrets |
| R10 Privacy by Design | PROCESS | — |
| R11 Freshness | PROCESS | `scanners.lock.json` records resolution date |
| R12 Provenance | CODE (partial) | Evidence has hash, time, git HEAD; memory notes need `source_refs`; tool pins recorded |
| R13 Alternatives | PROCESS | — |
| R14 Compatibility | PROCESS | `adapters/COMPATIBILITY.md` labels untested integrations as untested |
| R15 Traceability | CODE (partial) | Ledger links tasks, approvals, evidence, findings. No automatic requirement↔test matrix |
| R16 Full Completion | GATE | All tasks terminal and all required checks recorded |
| R17 Independent Verification | GATE (partial) | `independent-review` check + `review-package`. The runtime **cannot prove** the reviewer was actually independent |
| R18 Failure Transparency | CODE | PASS/FAIL/NOT_RUN/BLOCKED/NOT_APPLICABLE/WAIVED are distinct; every blocker is printed |
| R19 Recovery | PROCESS | Git HEAD is recorded in evidence; rollback plans are a human responsibility |
| R20 Right-Sized Engineering | PROCESS | — |

Honest summary: 3 rules fully code-enforced, 5 partially code-enforced, 2 checked at the gate, 10 instruction-only. Making more of them machine-checkable is the main roadmap item (`docs/framework/POSITIONING-AND-ROADMAP.md`).

## 4. End-to-end flow with enforcement points

```
PROJECT.md + AGENTS.md ──► AI reads rules (System A)
        │
 plan ──┤ validates workers, actions, budgets, DAG, argv commands          [CODE]
        ▼
 approve ─ registered human, assurance recorded, digest bound              [CODE]
        ▼
 transition READY ─ dependencies SUCCEEDED, digest + approval re-verified  [CODE]
        ▼
 run / complete ─ evidence required, no sandbox claim                      [CODE]
        ▼
 check run / record ─ unit tests, secrets, deps, SAST, DAST, LLM red-team  [CODE + external tools]
        ▼
 review-package ─► fresh read-only reviewer ─► findings (schema)           [CODE + host isolation]
        ▼
 findings resolve ─ human only, rationale/evidence required                [CODE]
        ▼
 gate ─ BLOCKED or PASS (never proves "secure")                            [GATE]
        ▼
 human release decision
```

## 5. Threat model: what this does and does not stop

**Stops:** an AI agent approving its own work through the runtime; skipping dependencies; faking success; silently widening an approved task; editing history without detection; typing "tests passed" without running them; running a non-allow-listed program through the runtime.

**Does not stop:**
- A malicious or compromised process with write access to the project directory can edit `.aisdf/policy.json`, replace the whole ledger, or run commands outside the runtime. The ledger is **tamper-evident, not tamper-proof**.
- Approver identity is a name in a file. `--non-interactive` can be typed by anyone; it only lowers the recorded assurance, which the gate then rejects for sensitive actions.
- Executed commands run with the user's OS privileges. Process limits are **not a sandbox**: no network blocking, no filesystem isolation.
- Prompt injection against a connected model.

**Hardening you should apply in real use:** run AI tools as a separate OS user that cannot write `.aisdf/policy.json`; protect `policy.json` and `security/` with CODEOWNERS and branch protection; run `verify-ledger` and `gate` in CI under a different identity than the agent; use an external sandbox (container/VM without credentials) for anything untrusted.
