# PROJECT.md — Project Source of Truth

> **Document status:** DRAFT — NOT APPROVED  
> **Project ID:** `PROJECT-REPLACE`  
> **Project name:** `REPLACE-WITH-PROJECT-NAME`  
> **Project type:** `UNKNOWN`  
> **Owner / maintainer:** `UNASSIGNED`  
> **Last reviewed:** `YYYY-MM-DD`  
> **AISDF template version:** `3.8.3`

> This file describes the actual project. It is not automatically approved because an AI agent generated it. Keep observed facts, evidence, assumptions, proposals, decisions, and unknowns separate. Never invent functionality, metrics, users, architecture, or approvals.

## How to maintain this file

- For an existing repository, inspect source code, tests, docs, manifests, migrations, CI, deployment configuration, and actual behavior before filling claims.
- For a new repository, label unknowns as `UNKNOWN` and proposed behavior as `PROPOSED`.
- Every feature must have a stable ID, a status, and evidence or an explicit evidence gap.
- Never mark a feature `IMPLEMENTED_VERIFIED` from documentation or file presence alone.
- Detailed technical designs belong in linked documents under `docs/`; this file is the index and canonical summary.
- Update the change history after approved changes. AI-generated edits remain `DRAFT` until reviewed by an authorized human.

## Status vocabulary

Use only the most accurate status:

- `IMPLEMENTED_VERIFIED` — behavior was exercised and evidence is linked.
- `IMPLEMENTED_UNVERIFIED` — code appears present but behavior has not been verified.
- `PARTIAL` — only some required behavior exists.
- `DOCUMENTED_ONLY` — described in docs but implementation not found.
- `PLANNED` — approved or proposed future work, not implemented.
- `MISSING` — required capability not found after the stated inspection.
- `BROKEN` — observed behavior fails an identified expectation.
- `UNKNOWN` — insufficient evidence or not inspected.
- `NOT_APPLICABLE` — genuinely irrelevant, with rationale.

## 1. Executive summary
- Project name:
- One-sentence description:
- Project type:
- Current lifecycle stage: `IDEA / DISCOVERY / DESIGN / DEVELOPMENT / DEMO / MAINTENANCE / ARCHIVED / UNKNOWN`
- Existing system or greenfield:
- Repository URL / local path:
- Default branch and inspected revision:
- License (verified from LICENSE file or `UNKNOWN`):
- Primary documentation links:

## 2. Full problem statement
### 2.1 Problem narrative
Describe who experiences the problem, the context, what happens today, frequency and severity, current workaround, why existing alternatives are insufficient, and consequences of doing nothing. If this is an educational/demo project, explain the learning or demonstration problem honestly.

### 2.2 Evidence register
| Evidence ID | Source / observation | Date | Supports which claim? | Confidence | Link / location |
|---|---|---|---|---|---|
| EVD-001 | UNKNOWN | UNKNOWN | UNKNOWN | LOW | UNKNOWN |

### 2.3 Problem boundaries
- In-scope problem:
- Explicitly out-of-scope problem:
- Known constraints:
- Claims not yet validated:

## 3. Purpose, vision, objectives, and outcomes
- Purpose:
- Vision:
- Primary objectives:
- Expected user/developer/learning outcomes:
- Success measures (baseline, target, method, owner):
- If no quantitative metric is appropriate, explain the qualitative completion criteria:

## 4. Users, actors, and stakeholders
| Actor / persona | Context and goals | Pain points | Permissions / responsibilities | Evidence |
|---|---|---|---|---|
| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Include end users, maintainers, contributors, administrators, external systems, and automated agents where applicable. Do not invent personas.

## 5. Existing repository and system baseline
> Required for existing projects. For greenfield projects, state `GREENFIELD — no existing implementation inspected`.

- Inspected repository path / URL:
- Branch, commit SHA, and working-tree state:
- Inspection date and tools:
- Languages, frameworks, runtimes, and versions (with evidence):
- Entry points and startup commands:
- Major modules and responsibilities:
- Data stores, schemas, migrations, and seed data:
- APIs, events, and external integrations:
- Authentication and authorization model:
- Build, test, lint, type-check, and packaging commands:
- CI workflows and deployment targets:
- Behavior actually executed and observed:
- Files/directories not inspected or inaccessible:

## 6. Complete feature and function inventory
Record user-visible features, internal capabilities, commands, endpoints, background jobs, integrations, and administrative functions. Split large features into testable capabilities.

| Feature ID | Feature / function | User value / purpose | Inputs → behavior → outputs | Actor / permission | Status | Evidence (file, test, run) | Priority |
|---|---|---|---|---|---|---|---|
| FR-001 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | MUST / SHOULD / COULD |

Rules:
- Do not combine unrelated functions into one row.
- Map UI actions to API/service/data behavior where applicable.
- Record error, empty, loading, retry, permission-denied, and success behavior.
- Separate implemented behavior from intended behavior.

## 7. User journeys and operational workflows
For each primary journey, document trigger, preconditions, steps, decisions, alternate paths, errors, permissions, data changes, and completion state.

| Journey ID | Actor | Trigger | Main steps | Failure / alternate paths | Completion evidence |
|---|---|---|---|---|---|
| UJ-001 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

## 8. Functional requirements
| Requirement ID | Requirement statement (shall) | Rationale | Related feature IDs | Priority | Source / evidence | Approval status |
|---|---|---|---|---|---|---|
| FRQ-001 | TBD | TBD | TBD | MUST / SHOULD / COULD | TBD | PROPOSED |

Requirements must be atomic, unambiguous, testable, and traceable. Do not use this table as a substitute for the feature inventory.

## 9. Non-functional requirements
| NFR ID | Category | Requirement | Measure / threshold | Verification method | Status |
|---|---|---|---|---|---|
| NFR-001 | Security / performance / reliability / accessibility / privacy / portability / maintainability | TBD | TBD | TBD | PROPOSED |

Include only relevant categories and explain `NOT_APPLICABLE` decisions.

## 10. Domain rules and application logic
- Domain concepts and glossary:
- Business/application rules with stable IDs:
- Validation rules:
- State machines and allowed transitions:
- Calculations, invariants, and constraints:
- Role and permission rules:
- Edge cases and exception behavior:
- Rules that are inferred but not confirmed:

## 11. Data model and information lifecycle
- Entities / objects and ownership:
- Relationships and cardinality:
- Data stores and schema evidence:
- Data classification and sensitivity:
- Create/read/update/delete rules:
- Retention, deletion, export, and portability:
- Backups, recovery, and data-loss considerations:
- Migrations, compatibility, and rollback:
- Test/sample data policy:
- Secrets and personal data that must never enter repository artifacts:

## 12. Architecture and technical design
- Observed current architecture (evidence-linked):
- Proposed target architecture (label as proposal until approved):
- Components and responsibilities:
- Module/service boundaries:
- Request, event, and data flows:
- API and integration contracts:
- Deployment topology (if applicable):
- Architecture Decision Records (ADR links):
- Known architecture debt and constraints:

## 13. Technology stack and dependencies
| Technology / dependency | Purpose | Version / range | Direct or transitive | License | Support / compatibility evidence | Decision |
|---|---|---|---|---|---|---|
| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Include runtime, frameworks, build tools, databases, packages, external services, models, and developer tools. Do not claim a version is current without checking.

## 14. API, integration, and interface contracts
- Public/internal APIs:
- Routes / commands / events:
- Request and response formats:
- Authentication and authorization:
- Rate limits and quotas:
- Error contracts and retries:
- External services and failure behavior:
- Backward compatibility and versioning:

## 15. UX, UI, accessibility, and documentation
- Information architecture and navigation:
- Screen/page/component inventory:
- Interaction and state behavior:
- Responsive requirements:
- Accessibility target and verification:
- Empty/loading/error/success states:
- Content, localization, and documentation requirements:
- Design references and approved design system:

For CLI/library projects, document command UX, API ergonomics, examples, installation, and error messages instead of UI screens.

## 16. Security, privacy, safety, and abuse cases
- Assets and trust boundaries:
- Threats and abuse cases:
- Authentication / authorization:
- Input validation and output encoding:
- Secrets and configuration handling:
- Sensitive data processing and retention:
- Dependency and supply-chain risks:
- Logging, audit, and rate-limiting requirements:
- Security testing performed and evidence:
- Compliance obligations: `VERIFIED / UNKNOWN / NOT_APPLICABLE_WITH_REASON`:

## 17. Scope and constraints
### In scope
- TBD
### Explicitly out of scope
- TBD
### Constraints
- Technical:
- Time / resource:
- Platform / compatibility:
- Legal / license:
### Assumptions
| Assumption ID | Assumption | Validation method | Owner | Status |
|---|---|---|---|---|
| ASM-001 | TBD | TBD | TBD | UNVALIDATED |

## 18. Acceptance criteria and verification matrix
Use observable, testable Given/When/Then or measurable criteria. Each criterion must link to feature/requirement IDs and an evidence location.

| AC ID | Related FR/FRQ/NFR IDs | Given / When / Then or measurable condition | Verification method | Evidence | Status |
|---|---|---|---|---|---|
| AC-001 | FR-001 | TBD | TBD | TBD | NOT_VERIFIED |

## 19. Missing functionality, defects, conflicts, and open questions
| Finding ID | Type | Finding | Evidence | Impact | Severity | Owner | Status / resolution |
|---|---|---|---|---|---|---|---|
| GAP-001 | MISSING / PARTIAL / BROKEN / CONFLICT / QUESTION | TBD | TBD | TBD | HIGH / MEDIUM / LOW | TBD | OPEN |

Do not label a feature missing until the relevant code and evidence sources have been inspected. If inspection is incomplete, use `UNKNOWN`.

## 20. Risks and mitigations
| Risk ID | Risk | Likelihood | Impact | Detectability | Mitigation / contingency | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |

## 21. Build, test, release, operations, and support
- Prerequisites and local setup:
- Build / run commands:
- Test / lint / type-check commands:
- Packaging and distribution:
- Environments and configuration:
- CI/CD behavior:
- Deployment and rollback (if applicable):
- Observability, diagnostics, and incident handling:
- Backup/restore (if data is persisted):
- Support and maintenance ownership:
- Known operational limitations:

## 22. Project-specific agent rules and permissions
- Applicable root/nested `AGENTS.md` and host instruction files:
- Allowed read actions:
- Allowed write paths:
- Prohibited paths/actions:
- Commands that require approval:
- External network/API permissions:
- Destructive operation restrictions:
- Required review and verification steps:

Detailed reusable rules live in `AGENTS.md`; do not duplicate the full agent policy here.

## 23. Decisions and approval gates
### Decision register
| Decision ID | Decision / alternatives | Status | Owner | Date | Evidence / ADR |
|---|---|---|---|---|---|
| DEC-001 | TBD | PROPOSED | TBD | TBD | TBD |

### Approval record
- Problem statement approved: `NO`
- Feature/functional requirements approved: `NO`
- Non-functional requirements approved: `NO`
- Scope approved: `NO`
- UX/design approved: `NO / NOT_APPLICABLE_WITH_REASON`
- Architecture/technology approved: `NO`
- Security/privacy review: `NOT_STARTED`
- Implementation plan approved: `NO`
- Release approval: `NO`
- Approved by:
- Approval date:
- Approved repository revision / document hash:

**This file alone does not authorize implementation. The exact implementation plan, file allowlist, and approval must also be current and explicit.**

## 24. Implementation plan and traceability
| Work item | Requirement / AC / finding IDs | Plan / spec | Exact files allowed | Tests / verification | Dependency | Status |
|---|---|---|---|---|---|---|
| WI-001 | TBD | TBD | TBD | TBD | TBD | NOT_PLANNED |

## 25. Change history
| Date | Version | Change | Author | Approval reference |
|---|---|---|---|---|
| YYYY-MM-DD | 0.1 | Initial draft | TBD | None |
