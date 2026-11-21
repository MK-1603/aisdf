# WF-009 — Independent Multi-Stage Design Review

**Purpose:** Find omissions and implementation risks using reviewers that do not inherit the drafting conversation's assumptions.

## Isolation preflight

- Each reviewer must start in a new context/session with no conversation history from the drafter.
- Provide only the target design, reviewer persona/rubric and explicitly permitted source materials.
- Record host, model, reviewer identity, context-construction method and evidence that parent conversation was excluded.
- If the host cannot establish or verify this boundary, stop independent review and mark `BLOCKED_ISOLATION_UNAVAILABLE`. A same-context critique is not a substitute.

## Five-stage review pipeline

1. **Zoom-out / simplicity review:** YAGNI, reuse existing infrastructure, scope, unnecessary complexity and alternatives.
2. **Comprehension review:** a reader unfamiliar with the discussion checks self-containment, definitions, assumptions, missing background and ambiguous requirements.
3. **Design critique:** architecture, interfaces, data, scale, security, privacy, reliability, migration, observability, cost and failure modes.
4. **Second zoom-out review:** re-evaluate changes introduced during comprehension and design critique; detect scope creep and contradictions.
5. **Implementation-readiness review:** exact file boundaries, component ownership, APIs/types/schema, migration plan, ordered implementation steps, tests and acceptance criteria.

## Reviewer execution

- Run independent reviewers in parallel only where the host can guarantee fresh contexts and concurrency limits.
- Give each reviewer a narrow rubric and request finding IDs, severity, evidence, impact, reproducible scenario and recommendation.
- Do not let a reviewer silently edit or approve the design it is reviewing.
- A synthesizer may deduplicate equivalent findings, but must preserve distinct evidence and minority disagreements.

## Outputs
Stage reports, consolidated findings register, isolation evidence, readiness verdict and unresolved risk summary.

## Verdicts
`PASS`, `PASS_WITH_ACTIONS`, `CHANGES_REQUIRED`, `BLOCKED`, `NOT_RUN`. `PASS` requires all mandatory stages and no unresolved blocking/critical finding. Human approval remains mandatory.

## Non-claims
Passing design review does not prove code correctness, security, performance or production readiness. Those require implementation tests and independent verification.
