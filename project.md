# PROJECT.md — AISDF 1.0.0 Project Source of Truth

- Project: AI Software Development Framework (AISDF)
- Version: 1.0.0
- Type: OPEN_SOURCE_FRAMEWORK_AND_LOCAL_REFERENCE_RUNTIME
- Status: 1.0.0 — stable local control-plane interface; model adapters, sandboxing and scanner execution are out of scope and clearly labeled
- License: MIT (subject to provenance and third-party license review)

## 1. Problem
AI-assisted software work is fragmented across prompts, tools, agents, repositories and human decisions. Projects lack a consistent mechanism to preserve requirements, assign specialist responsibility, constrain actions, coordinate dependencies, retain evidence and independently verify results.

## 2. Mission
Provide a self-hostable, provider-independent framework and executable reference runtime for governed software engineering work across the full lifecycle.

## 3. Intended users
Individual developers, students, open-source maintainers, product teams, software engineering organizations, security teams and educators.

## 4. Product boundaries
AISDF is a framework, specification set, role/workforce catalogue and local control-plane reference runtime. It is not an LLM, IDE, hosted SaaS, autonomous coding model, or built-in secure sandbox.

## 5. Core capabilities
- Project source-of-truth generation and validation.
- Specialist worker catalogue and machine-readable manifests.
- Task/work-unit contracts and dependency graph validation.
- Capability-based routing metadata.
- Permission policy checks and approval gates.
- Task budgets, execution state and audit ledger.
- Security engineering workflows and tool adapter contracts.
- Engineering standards, tests, templates and documentation.
- Optional MK Framework venture methodology.
- Enforced approvals (human allow-list, digest-bound), dependency gating, hash-chained audit ledger.
- Governed local command execution with hashed evidence (not a sandbox).
- Schema-validated review findings, release gate, independent-review package.
- Memory vault template and checker; pinned security-tool lock.

## 6. Non-functional objectives
Portable Python 3.10+ core; standard-library runtime; explicit filesystem boundaries; deterministic state transitions; auditable decisions; extensible adapters; testable contracts; no mandatory network calls; no secret values in manifests or logs.

## 7. Architecture
See `docs/framework/ARCHITECTURE.md`, `docs/framework/WORKFORCE-MODEL.md`, `docs/framework/SECURITY-ARCHITECTURE.md`, and `runtime/README.md`.

## 8. Scope exclusions for 1.0.0
No bundled model weights, no provider API credentials, no built-in autonomous model calls, no production OS sandbox, no guaranteed vulnerability detection, no automatic production deployment, and no claim of benchmark leadership.

## 9. Acceptance criteria
- Repository validator passes.
- Unit and integration tests pass.
- Worker manifests validate against schema.
- Task DAG rejects missing dependencies and cycles.
- State transitions reject invalid transitions.
- Permission checks deny unauthorized actions by default.
- Human approval is required for gated actions.
- Budget checks reject over-budget tasks.
- Audit ledger records task and approval events and is hash-chained; tampering is detected.
- Only registered humans can approve; unregistered or AI-named approvers are rejected.
- A task cannot be READY before its dependencies SUCCEEDED, and cannot succeed without evidence.
- The release gate blocks on missing, failed or altered evidence and on open serious findings.
- Documentation distinguishes specified, implemented, tested and certified maturity.

## 10. Risks
Provider incompatibility, prompt injection, untrusted code execution, privilege escalation, incomplete evidence, model nondeterminism, supply-chain risk, false-positive/negative security findings, and overclaiming maturity.

## 11. Decisions
- Core runtime uses Python standard library and SQLite.
- Provider/model execution is adapter-based and opt-in.
- Human approval remains authoritative for sensitive actions.
- Role contracts are separate from runtime capabilities.
- MK Framework remains a distinct optional methodology.
