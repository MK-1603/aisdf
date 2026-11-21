# 50 — Harness Engineering

**Engineering area:** AI execution environments and agent systems  
**Maturity:** SPECIFIED — implementation and production verification are project-specific.

## Purpose
Engineer the controlled environment around a model or agent so context, tools, permissions, execution, verification and feedback are reliable. The harness is not the model itself.

## Core concepts and mechanisms
- Harness boundary: model interface, policies, task contract, context assembly, tool registry, runtime, state store, evaluator and telemetry.
- Context engineering: authoritative source selection, retrieval budgets, freshness, provenance, truncation, untrusted-content labeling and isolation.
- Tool engineering: typed schemas, capability discovery, argument validation, least privilege, timeouts, quotas and safe error handling.
- Execution isolation: process/container/VM sandbox, filesystem/network policy, resource quotas, egress controls and ephemeral credentials.
- Policy enforcement: allowlists, deny rules, approval gates, secret redaction, data boundaries and side-effect classification.
- Reliability: durable state, checkpoints, idempotency, retries, cancellation, crash recovery and replay where feasible.
- Evaluation: golden tasks, unit/integration tests, adversarial suites, regression datasets and independent outcome checks.
- Observability: prompt/context references, tool calls, decisions, results, latency, cost and safety events; avoid raw sensitive content by default.
- Provider abstraction, capability profiles, version pinning, fallback policy, structured-output validation and drift monitoring.
- Operator controls: approvals, pause/resume, kill switch, audit, incident response and release management.

## Required inputs
- Use case and task risk classification.
- Model/provider capability profile and version constraints.
- Task contract, source-of-truth references and context budget.
- Tool definitions, permissions, network/filesystem policy and secrets policy.
- Acceptance tests, evaluation dataset, operational SLOs and budget.

## Required outputs
- Harness architecture and trust-boundary diagram.
- Context assembly and tool capability contracts.
- Sandbox and permission policy.
- Execution/state/recovery design.
- Evaluation suite, telemetry schema and operational runbook.

## Security, reliability and failure modes
- Confusing model capability with harness-enforced guarantees.
- Tool over-permission, sandbox escape, unsafe egress or credential leakage.
- Prompt injection via retrieved files, web pages, memory or tool output.
- Context poisoning, stale retrieval and cross-tenant leakage.
- Model/provider drift, telemetry privacy leakage and unsafe fallback weakening.

Treat external content, retrieved memory and tool outputs as untrusted until validated. Apply least privilege, data minimization, tenant isolation, safe failure behavior and explicit authorization.

## Implementation workflow
1. Classify risk and separate what the model may suggest from what the harness may execute.
2. Define trust boundaries; treat retrieved and tool-returned content as untrusted data.
3. Create typed, versioned tools with least-privilege scopes and side-effect classes.
4. Implement context assembly with provenance, freshness, budgets and tenant isolation.
5. Enforce sandboxing outside the model prompt; prompts are not a security boundary.
6. Implement durable state, checkpoints, idempotency, deadlines and cancellation.
7. Validate tool arguments and outputs; independently verify critical outcomes.
8. Build evaluation and adversarial regression suites before widening permissions.
9. Instrument quality, cost, latency, denials and failures without default secret logging.
10. Run staged rollout, incident drills and rollback tests.

## Verification strategy
Tool-schema and permission tests; OS/runtime sandbox tests; prompt injection across all input channels; context/tenant isolation; secret redaction; crash/restart/checkpoint; regression/replay; model drift; cost/latency budgets; kill-switch and rollback drills.

## Companion test plan
`../TEST-PLANS/50-harness-engineering-tests.md`

## Acceptance criteria
- Applicability is justified; unnecessary complexity is rejected.
- Architecture, alternatives, assumptions, security boundaries and operational ownership are documented.
- Failure, recovery and observability behavior are explicit.
- Tests have reproducible evidence; unrun checks are `NOT_RUN`.
- Production use has rollback/recovery, monitoring and accountable ownership.

## Related AISDF capabilities
Reuse existing engines, workflows, schemas and governance. Do not allocate duplicate engine IDs or imply that a documented capability is an implemented runtime. Record exact project dependencies in the work unit.

## Status vocabulary
`NOT_ASSESSED` · `SPECIFIED` · `DESIGNED` · `IMPLEMENTED` · `TESTED` · `INDEPENDENTLY_VERIFIED` · `PRODUCTION_VERIFIED` · `NOT_APPLICABLE` · `BLOCKED`.
