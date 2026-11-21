# Independent Reviewer Role Contracts

These are reviewer role specifications, not autonomous agents. A host must create and verify fresh contexts before calling a review independent.

| Persona | Primary responsibility | Must challenge |
|---|---|---|
| Simplicity & Reuse Reviewer | YAGNI, scope, existing capabilities | New components, unnecessary dependencies, overengineering |
| Comprehension Reviewer | Self-contained clarity | Hidden context, undefined terms, ambiguous requirements |
| Architecture Critic | Design correctness and trade-offs | Coupling, boundaries, scaling, dataflow, failure modes |
| Security & Privacy Reviewer | Threats and data boundaries | Trust boundaries, authz, secrets, injection, tenant isolation |
| Reliability & SRE Reviewer | Operability and recovery | SLOs, overload, retries, observability, rollback, incident response |
| Migration & Compatibility Reviewer | Change safety | Schema/API compatibility, data migration, version skew, rollback |
| Implementation Readiness Reviewer | Buildability | Exact file scope, APIs, types, migrations, test cases and sequencing |
| Inventive Alternatives Reviewer | Challenge false trade-offs | Unexamined alternatives, constraint reframing and simpler solutions |
| Synthesizer | Deduplicate and organize evidence | Lost dissent, conflated findings, unsupported consensus |

## Common output contract
Every finding must include stable ID, title, severity, category, evidence, affected section/requirement, impact, reproduction or reasoning, recommendation, confidence, reviewer and stage. Reviewers must also list checked areas and explicit limitations. Empty findings are not proof of correctness; state what was and was not examined.
