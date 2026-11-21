# AISDF v4.0 Architecture

## Layers
1. Governance: rules, approvals, evidence and release authority.
2. Project intelligence: PROJECT.md, repository inventory, requirements and state.
3. Workforce catalogue: teams, roles, capabilities and maturity.
4. Planning: work units, dependency DAG, routing metadata and budgets.
5. Control plane: policy checks, state machine, approval records and audit ledger.
6. Execution adapters: optional human, deterministic tool or model provider integration.
7. Verification: tests, security checks, independent review and evidence.
8. Operations: monitoring, incident response, maintenance and learning.

## Data flow
Human intent is converted into approved requirements and work units. The planner validates dependencies and role capability. Policy checks requested actions. Human approval is recorded for gated actions. A configured adapter may execute only within its grant. Results and audit events are persisted. Independent verification evaluates artifacts. Human authority makes release decisions.

## Local reference runtime
Python standard library + SQLite. The runtime is deliberately local and deterministic. A distributed control plane, multi-tenant service, scheduler, secret manager and sandbox are extension projects, not claimed as part of this release.
