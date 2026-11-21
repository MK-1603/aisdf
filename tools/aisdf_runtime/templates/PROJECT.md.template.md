# PROJECT.md — Project Source of Truth

> Status: DRAFT — NOT APPROVED  
> Project ID: `PROJECT-REPLACE`  
> Last reviewed: `YYYY-MM-DD`  
> Owner: `UNASSIGNED`  
> AISDF schema version: `1.0`

This document is the canonical, human-approved description of the product/project. Keep verified facts, approved decisions, assumptions, and unknowns clearly separated. Do not invent missing details. Link detailed specifications rather than duplicating them.

## 1. Executive summary
- Product/project name:
- One-sentence description:
- Current lifecycle stage:
- Existing system or greenfield:
- Repository / deployment references:

## 2. Problem statement
### 2.1 Full problem statement
Describe the problem in context: who experiences it, what happens today, why it matters, frequency/severity, current workaround, and consequences of doing nothing.

### 2.2 Evidence
| ID | Evidence / source | Date | What it supports | Confidence |
|---|---|---|---|---|
| EVD-001 | TBD | TBD | TBD | LOW/MEDIUM/HIGH |

### 2.3 Problem boundaries
- In-scope problem:
- Out-of-scope problem:
- Known constraints:

## 3. Vision, outcomes, and success measures
- Product vision:
- Desired user/business outcomes:
- Success metrics with baseline, target, measurement method, and owner:

## 4. Users and stakeholders
| Persona / stakeholder | Goals | Pain points | Permissions / responsibilities |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## 5. Existing-system baseline (required for existing projects)
- Repository revision / branch inspected:
- Languages/frameworks/runtime:
- Entry points and major modules:
- Data stores and migrations:
- APIs and external integrations:
- Authentication/authorization model:
- Build, test, lint, and deployment commands:
- Current behavior verified:
- Areas not inspected / inaccessible:

## 6. Functional requirements and feature inventory
For every feature, use a stable ID. State current status and evidence; do not describe planned features as implemented.

| ID | Feature / capability | User value | Inputs → behavior → outputs | Roles | Status | Evidence / source | Priority |
|---|---|---|---|---|---|---|---|
| FR-001 | TBD | TBD | TBD | TBD | PROPOSED | TBD | MUST/SHOULD/COULD |

## 7. User journeys and workflows
Describe primary journeys step-by-step, including alternate paths, errors, permissions, and completion states. Link diagrams where useful.

## 8. Non-functional requirements
| ID | Category | Requirement | Measure / threshold | Verification method |
|---|---|---|---|---|
| NFR-001 | Security/performance/reliability/accessibility/privacy/maintainability | TBD | TBD | TBD |

## 9. Business rules and domain logic
- Rules with IDs:
- Validation rules:
- State transitions:
- Calculations and invariants:
- Exceptions and edge cases:

## 10. Data and information lifecycle
- Entities and ownership:
- Data classification/sensitivity:
- Create/read/update/delete rules:
- Retention/deletion/export:
- Backup/recovery:
- Data migration and compatibility:

## 11. Architecture and technical baseline
- Current architecture (observed):
- Target architecture (proposed; approval required):
- Technology stack and versions (verified date/source):
- Module/service boundaries:
- API/event contracts:
- Deployment topology:
- Architecture decisions (ADR links):

## 12. Integrations and dependencies
| System / service | Purpose | Direction | Auth / data exchanged | Failure behavior | Owner |
|---|---|---|---|---|---|
| TBD | TBD | TBD | Never include secret values | TBD | TBD |

## 13. UX, UI, and accessibility
- Design principles and references:
- Navigation/information architecture:
- Responsive requirements:
- Accessibility requirements:
- Empty/loading/error/success states:

## 14. Security, privacy, and abuse considerations
- Threats and trust boundaries:
- Authentication and authorization:
- Secrets and configuration handling:
- Sensitive data processing:
- Abuse/rate limiting/audit requirements:
- Compliance obligations (verified or UNKNOWN):

## 15. Scope
### In scope
- TBD
### Explicitly out of scope
- TBD
### Constraints and assumptions
- Assumptions must be labeled and validated; never silently convert them into requirements.

## 16. Acceptance criteria
Use testable Given/When/Then or measurable statements. Link each criterion to requirement IDs and verification evidence.

| AC ID | Requirement IDs | Acceptance criterion | Verification | Status |
|---|---|---|---|---|
| AC-001 | FR-001 | TBD | TBD | NOT_VERIFIED |

## 17. Known gaps, conflicts, and open questions
| ID | Finding | Evidence | Impact | Severity | Owner | Resolution / decision |
|---|---|---|---|---|---|---|
| GAP-001 | TBD | TBD | TBD | HIGH/MEDIUM/LOW | TBD | OPEN |

## 18. Risks and mitigations
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| RISK-001 | TBD | TBD | TBD | TBD | TBD |

## 19. Release, operations, and support
- Environments:
- Observability and alerting:
- Backup/restore and incident response:
- Rollout/rollback:
- Support ownership:

## 20. Decisions and approval gates
### Decisions
| Decision ID | Decision | Status | Decision owner | Date | Evidence / ADR |
|---|---|---|---|---|---|
| DEC-001 | TBD | PROPOSED | TBD | TBD | TBD |

### Approval record
- Problem statement approved: NO
- Requirements/features approved: NO
- Scope approved: NO
- Architecture approved: NO
- Security/privacy review: NOT_STARTED
- Implementation plan approved: NO
- Approved by:
- Approval date:
- Approved revision/hash:

**No implementation authorization is granted by this document until the relevant approval fields are explicitly completed by an authorized human.**

## 21. Implementation traceability
| Work item | Requirement / AC IDs | Spec / plan | Files allowed | Tests | Status |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | NOT_PLANNED |

## 22. Change history
| Date | Version | Change | Author | Approval reference |
|---|---|---|---|---|
| YYYY-MM-DD | 0.1 | Initial draft | TBD | None |
