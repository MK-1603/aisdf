# EGM Source Analysis and AISDF Gap Assessment

## Scope and method

Reviewed the public Google repository's README, architecture document, getting-started guide, design-document guidance, skill definitions for brainstorm/draft/review/review-loop/resolve/bootstrap/drift-report, reviewer personas, document standards and testing playbook. This is a repository-documentation review, not an execution or security audit of EGM.

## Source-derived EGM concepts

1. **Elephant / Goldfish context split:** a context-rich drafting role retains project history; reviewers are launched in fresh contexts and assess the artifact plus permitted references without the drafting conversation.
2. **Brainstorm:** iterative clarification, a readiness checkpoint, and multiple critique lenses (YAGNI/contrarian, cost/quota, UX/developer ergonomics, migration/compatibility, observability/SRE, long-term maintenance, inventive alternatives).
3. **Draft:** section-by-section specification writing with explicit user approval gates; design decisions with multiple defensible options are returned to the human rather than silently chosen.
4. **Review:** staged checks including simplicity/reuse, comprehension/self-containment, design critique, a second simplicity pass after revisions, and implementation readiness.
5. **Synthesis and resolution:** parallel reviewer findings are consolidated, duplicates handled, findings dispositioned and changes re-reviewed.
6. **Bootstrap:** bottom-up recursive repository documentation can establish a navigable codebase map; generated descriptions require human validation.
7. **Drift report:** checked-in design documents and README context are compared with the current codebase to detect divergence.
8. **Artifact-first workflow:** long-form briefs, specifications and reports live as files, not giant chat dumps.
9. **Implementation boundary:** design/review phases are kept separate from source-code changes; implementation is limited to an explicit target-file scope after readiness/approval.
10. **Host verification:** harness support is established by actual end-to-end workflow tests on a named host/version, not by a compatibility claim in documentation.

## AISDF existing coverage observed in the v3.7.1 package

| Capability | Existing AISDF asset | Assessment |
|---|---|---|
| Project baseline and intake | project brief, intake/discovery engines, existing-project X-Ray | Covered at foundation level |
| Requirements and architecture | requirements, acceptance criteria, architecture engines | Covered at foundation level |
| Context continuity | AKIS, persistent memory overlay, E-038, E-040, context protocols | Covered conceptually; runtime remains unimplemented |
| Human approval and scope | governance rules, E-042, scope lock, Change Only Law | Covered as governance; needs design-phase gates |
| Code review and quality | E-045, WF-004, reviewer prompts | Partial; not equivalent to isolated design review |
| Harness engineering | domain 13 and topic 50 | Specified; no host runtime certification |
| Testing | test strategy, verification and release gate | Covered as general quality process |

## Gaps identified before this extension

| Gap | Why existing assets do not fully close it | Extension response |
|---|---|---|
| Dedicated multi-lens concept shootdown | Problem discovery exists, but no single workflow mandates the lenses and produces an agreed concept artifact | WF-007 |
| Section-by-section spec drafting gates | Requirements/architecture engines define outputs, but not iterative section approval and revision protocol | WF-008 |
| Fresh-context reviewer isolation | Code/security reviewer prompts do not prove that reviewer context excludes drafting conversation | WF-009 plus isolation evidence requirements |
| Staged independent design review | WF-004 is a quality/release gate, not a five-stage design-document critique pipeline | WF-009 |
| Finding disposition and re-review | Code review/change impact exists, but design findings need stable IDs, severity, owner, disposition and closure evidence | WF-010 and finding schema |
| Recursive codebase documentation | Existing-project X-Ray is a discovery capability, not a bottom-up living documentation protocol | WF-011 |
| Spec-to-code drift detection | Freshness policy and change impact are not an explicit scheduled/document-to-source comparison | WF-012 |
| Exact implementation file allowlist | Scope governance exists, but a design artifact needs a generated exact file boundary and enforcement evidence | Design standard and WF-008/009 |
| Artifact-first authoring | Templates exist, but no unified requirement that long outputs are maintained as durable artifacts with approval checkpoints | WF-007–010 |
| Harness-specific end-to-end proof | Adapter specifications do not establish installed host/version support | Harness test matrix and WF-009 preflight |

## Integration decisions

- Reuse existing AISDF engines and governance; do not duplicate AKIS, project state, handoff or human approval systems.
- Add six workflow specifications, four artifact templates, one finding schema and role contracts.
- Treat the EGM repository as an inspiration/reference, not as a dependency or source-code bundle.
- Do not claim EGM's plugin or skill commands are part of AISDF.
- Keep fresh-context review as `BLOCKED` when the host cannot create and demonstrate an isolated reviewer context. Same-context self-review may be useful, but must be labeled `NON_INDEPENDENT_REVIEW`.

## Limitations

This assessment does not prove EGM runtime correctness, validate every supported harness, or certify its release artifacts. It does not prove AISDF implementation. The extension is a set of design/workflow specifications awaiting implementation and host-specific tests.
