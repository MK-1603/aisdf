# WF-007 — Multi-Lens Concept Challenge

**Purpose:** Turn an initial idea into an evidence-aware, human-approved concept brief before committing to a design.

## Inputs
Idea/problem statement, project baseline, constraints, user evidence and known alternatives.

## Procedure
1. Inspect project source of truth, existing decisions and known system constraints.
2. Ask focused clarification questions until problem, users, trigger, desired outcome, constraints and non-goals are sufficiently clear. Do not spawn reviewers before the human confirms the working hypothesis.
3. Produce a short hypothesis and ask for explicit readiness approval.
4. Run independent critique lenses where the host supports genuinely fresh contexts: (a) YAGNI/reuse, (b) cost/quota/capacity, (c) UX/developer ergonomics, (d) migration/backward compatibility, (e) observability/SRE, (f) long-term maintenance/technical debt, (g) inventive alternatives/contradiction resolution.
5. If fresh-context reviewers are unavailable, mark the review `NON_INDEPENDENT` and do not represent it as independent validation.
6. Synthesize findings without erasing disagreements. Distinguish evidence, assumption, inference and opinion.
7. Create `concepts_brief.md` using the template. Include options and open decisions.
8. Obtain human approval to proceed to WF-008, revise, investigate further or stop.

## Outputs
Concept brief, lens findings, unresolved questions and explicit proceed/revise/stop decision.

## Gates
No reviewer fan-out before readiness approval. No design drafting before concept approval. No implementation in this workflow.

## Failure behavior
If source context is incomplete, reviewers cannot be isolated, or critical requirements conflict, mark `BLOCKED`/`NEEDS_CLARIFICATION`; do not guess.
