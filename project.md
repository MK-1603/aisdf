# PROJECT.md — AISDF Project Definition

> Status: DRAFT — repository maintainer review required  
> Project ID: AISDF  
> Version: 3.8.1  
> Owner: AISDF maintainers  
> Last reviewed: 2026-11-21

This file defines AISDF itself. For projects using AISDF, create a separate `PROJECT.md` in the target repository using `tools/aisdf_runtime/templates/PROJECT.md.template.md`.

## 1. Executive summary
AISDF (AI Software Development Framework) is a tool-independent methodology, governance system, workflow library, reusable artifact set, and limited portable validation toolkit for disciplined AI-assisted software engineering from problem discovery through operations and maintenance.

## 2. Problem statement
AI-assisted software development can accelerate code production while leaving the product problem, user needs, requirements, feature completeness, architecture, security, privacy, testing, operational readiness, and approval history fragmented across prompts, chat sessions, and repositories. This creates risks of misunderstood requirements, undocumented assumptions, scope drift, duplicated work, unverified claims, and unsafe changes.

AISDF addresses this by establishing a persistent project source of truth (`PROJECT.md`), agent operating instructions (`AGENTS.md` and host-native equivalents), governed workflows, traceable requirements and findings, explicit human approval gates, implementation plans, and evidence-based verification. AISDF does not itself guarantee correctness or replace human engineering judgment.

## 3. Vision and outcomes
- Make AI-assisted software development repeatable, auditable, and scope-controlled.
- Keep humans accountable for product decisions, approvals, security acceptance, and releases.
- Improve continuity across tools and sessions through stable project artifacts.
- Distinguish documented, implemented, tested, independently verified, and production-verified states.

## 4. Users and stakeholders
| User | Need | Responsibility |
|---|---|---|
| Individual developer | Reliable AI-assisted project workflow | Own project decisions and approvals |
| Engineering team | Shared process, traceability, review and quality gates | Maintain project truth and evidence |
| AI coding agent | Clear task context, rules, scope and verification expectations | Work only within delegated permissions |
| Maintainer | Govern framework releases and compatibility | Review changes, licensing and release readiness |

## 5. Functional capabilities
| ID | Capability | Status | Evidence |
|---|---|---|---|
| FR-001 | Problem discovery and project intake | DOCUMENTED | `engines/E-001*` through `E-010*`, workflows |
| FR-002 | Existing project X-Ray and feature inventory | DOCUMENTED + INVENTORY TOOLING | `WF-002`, `E-004`, project helper |
| FR-003 | Requirements, feature and acceptance traceability | DOCUMENTED | `engines/E-012*` through `E-016*` |
| FR-004 | Architecture and technology evaluation | DOCUMENTED | `engines/E-023*` through `E-030*` |
| FR-005 | AI-assisted implementation governance | DOCUMENTED | `AGENTS.md`, `00-GOVERNANCE/` |
| FR-006 | Verification, security and release governance | DOCUMENTED | `engines/E-043*` through `E-056*` |
| FR-007 | EGM-inspired concept/spec/review/drift workflow artifacts | LIMITED EXECUTABLE TOOLING | `WF-007` through `WF-012`, `tools/aisdf_runtime/aisdf.py` |
| FR-008 | Project definition, assessment, plan and gated prompt generation | LIMITED EXECUTABLE TOOLING | `WF-013`, `tools/aisdf_runtime/project.py` |
| FR-009 | Provider-specific AI tool adapters | PACKAGED; HOST CERTIFICATION PENDING | `adapters/` |

## 6. Non-functional requirements
- Provider-neutral core; provider-specific discovery remains isolated under `adapters/`.
- Portable tooling should prefer Python standard library and deterministic behavior.
- Generated planning artifacts must not modify target application source.
- Human approval must be explicit and attributable for material implementation scope.
- Claims must be evidence-backed; unavailable checks must be marked NOT_RUN or BLOCKED.
- No secrets or private project data may be emitted into public artifacts.

## 7. Architecture
AISDF consists of governance, methodology/domain documentation, engine contracts, operating modes, workflows, prompts, schemas, templates, registries, a portable Python workflow helper, validation tests, and host-specific adapter packages. The core is not an autonomous agent runtime or hosted service.

## 8. Approval and maturity
- Framework direction: maintainer review required.
- License: pending maintainer decision.
- Live adapter certification: not performed.
- Autonomous isolated reviewer orchestration: not implemented by portable runtime.
- Production readiness: not claimed.
