# MK Framework — Venture-to-Software Execution Method

**Flow:** Idea → Validated Venture → Verified Software → Systemized Business

**Purpose:** Reduce avoidable venture risk before building, translate a validated opportunity into a disciplined software delivery plan, and use evidence to decide whether to continue, pivot, stop, reinvest, defend an advantage, or systemize.

> This is a decision framework, not a guarantee of commercial success. A gate is passed only when its evidence and decision criteria are recorded. If evidence is insufficient, mark the gate **UNRESOLVED** rather than assuming it passed.

## 1. Operating principles

1. Validate the problem before committing to a solution.
2. Prefer demonstrated demand and working models over novelty alone.
3. Identify real founder advantages and the moat being pursued.
4. Imagine failure before execution and define kill criteria before sunk costs accumulate.
5. Treat market timing as a hypothesis to test, not a prediction to trust.
6. Define a clear offer before building the full product.
7. Build in small, inspectable increments with human approval and evidence.
8. Use feedback and pre-committed thresholds to decide what happens next.
9. Reinvest only when evidence supports the next investment.
10. Systemize repeatable work before delegating it.

## 2. Venture validation gates

### 0. Problem / crowd check — starving crowd check

**Question:** Is there a sufficiently important problem and an identifiable group that urgently wants it solved?

Examine:
- Pain: frequency, severity, urgency, and current workarounds.
- Budget: ability and willingness to pay, or another credible adoption commitment where payment is not relevant.
- Reach: whether the group can be identified and reached through practical channels.
- Growth: whether the audience or need is stable, growing, or otherwise strategically attractive.

**Evidence examples:** interviews, observed workflows, waitlists with qualified intent, pilot commitments, usage data, purchase behavior, support requests, or credible domain research.

**Gate output:** target crowd, problem statement, evidence, unresolved assumptions, and a go / defer / stop decision.

### 0.5 Proven-model check — model a proven winner

Study an existing working model where one exists. Understand:
- Who it serves and what job it performs.
- How it reaches users and delivers value.
- Its economics, operating model, and constraints where data is available.
- What moat type or defensible advantage supports it.
- Which parts are transferable and which depend on context, timing, regulation, brand, or scale.

Do not copy surface features without understanding the underlying mechanism. If no proven analogue exists, document that uncertainty and use experiments rather than inventing proof.

**Gate output:** reference model, transferable mechanisms, non-transferable assumptions, and candidate moat type.

### 0.75 Founder–market fit check

Prove at least three concrete founder advantages. Possible dimensions include:
- Access to the target users or distribution.
- First-hand insight into the problem.
- Rare technical, operational, or domain capability.
- Credibility, relationships, or execution speed.
- A cost, data, workflow, or ecosystem advantage.

Each claimed edge needs evidence and a reason it matters to this market. Personal enthusiasm alone is not proof.

**Gate output:** three or more evidenced edges, gaps, and a founder–market fit assessment.

### 1. Inversion thinking

Ask: **How could this venture fail?** List failure causes across demand, distribution, economics, product, technology, security, legal constraints, execution, and competition. Prioritize by likelihood, impact, and detectability. Convert preventable causes into controls or experiments.

**Gate output:** ranked failure-cause register and mitigations.

### 2. Premortem analysis

Write a plausible future story in which the venture failed. Explain what happened, when warning signs appeared, and why the team missed them. This complements inversion thinking: inversion lists causes; the premortem connects them into a realistic failure narrative.

**Gate output:** failure narrative, early-warning signals, and preventive actions.

### 3. Pre-commit kill criteria

Before substantial building or spending, define measurable **CONTINUE / PIVOT / STOP** thresholds. Use hard numbers wherever measurable.

Specify:
- Metric and exact definition.
- Baseline and target/threshold.
- Measurement method and evidence source.
- Evaluation window and sample-size caveats.
- Decision owner and decision date.
- What action follows each result.

Examples include qualified conversion, repeated usage, retention, willingness-to-pay, pilot completion, acquisition cost, delivery cost, or reliability. Choose metrics appropriate to the project; do not copy example thresholds blindly.

The original framework reference uses a short decision cycle (noted as 20 hours in its first diagram). Treat that as a project-specific cadence, not a universal rule. Set a realistic evaluation window before execution and do not move the threshold after seeing results without recording a formal decision.

**Gate output:** dated, approved kill-criteria record.

### 4. Market timing analysis

Evaluate whether the market is too early, ready, or late:
- Demand and user readiness.
- Enabling technology, infrastructure, regulation, and ecosystem maturity.
- Existing alternatives and competitive intensity.
- Adoption friction and switching costs.
- Distribution access and urgency of the need.

Identify what changed recently and what evidence would invalidate the timing thesis.

**Gate output:** timing thesis, evidence, risks, and timing-sensitive assumptions.

### 5. Build the offer

Define the offer before expanding the build:
- Target audience and use case.
- Outcome/value promise.
- Product or service scope.
- Price or non-monetary exchange, if applicable.
- Guarantee, risk reversal, or trust mechanism where appropriate and supportable.
- Delivery sequence, onboarding, and support expectations.
- Explicit exclusions and limitations.

For a free demo or open-source project, replace pricing and guarantee with the intended user value, contribution/use model, license status, support boundaries, and adoption path. Do not invent a commercial model.

**Gate output:** one-page offer definition and testable value proposition.

## 3. Disciplined product and software execution

This is the build stage. Use AISDF as the engineering control system. Do not jump from an offer directly into uncontrolled coding.

### 6.0 Project X-Ray

Inspect the existing repository and reality before changing it. Map the structure, features, dependencies, data, APIs, architecture, tests, deployment, security posture, known defects, and operational constraints. For a new project, record that no existing implementation is present and establish the baseline.

**Output:** evidence-backed current-state assessment and risks.

### 6.1 Scope freeze

Classify each candidate item:
- **MUST BUILD:** necessary for the approved outcome or acceptance criteria.
- **SHOULD BUILD:** valuable but not a release blocker.
- **LATER:** explicitly deferred.
- **DO NOT BUILD:** out of scope, unjustified, or harmful to focus.

Define non-goals, dependencies, and change-control rules. A scope change requires impact analysis and approval.

**Output:** approved scope baseline.

### 6.2 UX blueprint

Define target users, journeys, screens, states, navigation, responsive behavior, accessibility expectations, content, and design-system rules. Include empty, loading, error, permission, and success states where relevant.

**Output:** reviewable UX specification or prototypes and acceptance criteria.

### 6.3 Stack and architecture lock

Choose technologies based on constraints, team capability, ecosystem maturity, security, maintainability, cost, and deployment environment. Document architecture, boundaries, data flows, API contracts, authentication/authorization, integrations, and key trade-offs.

A lock is a controlled baseline, not an excuse to ignore new evidence. Changes require documented rationale and impact review.

**Output:** approved architecture decisions and technical baseline.

### 6.4 Source-of-truth documents

Maintain the project definition and engineering contracts, including where relevant:
- `PROJECT.md` — problem, users, requirements, features, constraints, acceptance criteria, gaps, and decisions.
- `AGENTS.md` — instructions and safety rules for coding agents.
- Domain model, business rules, workflows, permissions, and data definitions.
- API contracts, architecture decisions, and operational requirements.

Keep documents synchronized with verified implementation; do not claim planned features are implemented.

**Output:** approved, traceable project documentation.

### 6.5 Implementation map

Break scope into dependency-aware feature slices. For each slice, define requirements, exact file allowlist, data/API impact, migration needs, acceptance criteria, tests, risks, and rollback/recovery considerations. Obtain human approval before implementation.

**Output:** approved implementation plan.

### 6.6 Build in feature slices

Implement small, reviewable increments. AI may assist within the approved scope and permissions. Inspect diffs, protect secrets, avoid unrelated refactors, and stop when requirements are ambiguous or scope must change.

**Output:** implementation with traceable changes.

### 6.7 Functional testing

Verify each approved requirement and user journey. Include positive, negative, boundary, regression, and integration cases as appropriate. Record commands, results, and failures.

**Output:** requirement-linked functional test evidence.

### 6.8 Security and data validation

Review authentication, authorization, secrets, input validation, privacy, data handling, dependency risks, logging, and integrity. Confirm least privilege and safe failure behavior. Security acceptance belongs to an authorized human.

**Output:** security findings, remediation evidence, and explicit residual-risk decisions.

### 6.9 Performance and failure testing

Test relevant load, latency, resource use, edge cases, timeouts, retries, recovery, and resilience. Right-size testing to the project's actual deployment and risk profile.

**Output:** performance/failure evidence and known limits.

### 6.10 Deploy, observe, and launch

Use controlled deployment appropriate to the project. Validate configuration, migrations, rollback, health checks, logs/metrics, privacy-safe telemetry, and real user-facing behavior. For a local demo or library, document the applicable release, packaging, installation, or distribution process instead of inventing production operations.

**Output:** deployment/release record and operational checks.

### 6.11 Final audit

Check requirements traceability, approved scope, test evidence, security findings, documentation, release artifacts, and unresolved risks. Report **PASS**, **BLOCKED**, or **FAIL** with evidence. Do not turn missing evidence into a pass.

**Output:** final audit and human release decision.

## 4. Feedback and venture decision loop

### 7. Feedback loops

Collect real signals from users, customers, contributors, maintainers, support, usage, defects, and operations. Use a weekly signal review and a monthly constraint review as a starting cadence; adapt to project scale. Separate anecdotes from repeated patterns and quantitative evidence.

Feed validated learning back into the offer (stage 5), product scope/execution (stage 6), or market thesis (stage 4). Record what changed and why.

### 8. Check against kill criteria

Compare observed evidence with the pre-committed thresholds from stage 3. Decide:
- **CONTINUE:** thresholds are met and key risks are acceptable.
- **PIVOT:** evidence rejects a material assumption but supports a revised crowd, offer, channel, or approach.
- **STOP:** the pre-agreed stop condition is met or the opportunity is no longer justified.

Do not move goalposts silently. If criteria need revision due to new evidence, preserve the old criteria, document the reason, and approve the new baseline before the next measurement period.

### 9. Resource reinvestment

Reinvest time, money, and people only where evidence supports the expected value. Prioritize the binding constraint: product quality, distribution, onboarding, reliability, support, capability, or another demonstrated bottleneck. Preserve runway and define what the next investment is expected to prove.

### 10. Defend the moat

Strengthen the advantage diagnosed at stage 0.5 and supported by stage 0.75. Possible moat types include distribution, network effects, data advantages, workflow integration, switching costs, brand/trust, scale economics, specialized know-how, or ecosystem position. A moat is not a label; track whether it is real, durable, lawful, and valuable to users.

### 11. Systemize and delegate

Turn repeatable work into documented standard operating procedures (SOPs), checklists, quality gates, metrics, and ownership. Hire or delegate only when the work is sufficiently understood and can be measured. Transfer authority with clear boundaries, escalation paths, and feedback.

**Graduation condition:** the venture or project can operate through reliable systems without constant founder intervention. The founder steps back from routine execution while retaining appropriate governance.

## 5. Decision outcomes and loops

At the end of a review, choose and record one outcome:

1. **Graduate / systemize:** repeatable operations are working; delegate and step back.
2. **Return to 0:** begin a new venture or validate a genuinely different crowd/problem.
3. **Stop / pivot:** stop or change direction based on the pre-committed criteria and evidence.

A pivot may return to the relevant earlier stage rather than restarting everything. For example, new user evidence may change the crowd (0), the offer (5), or the product scope (6). Preserve the learning and decision history.

## 6. Required decision record

For each gate, maintain a compact record:

| Field | Required content |
|---|---|
| Stage | Number and name |
| Decision | PASS / FAIL / UNRESOLVED / NOT APPLICABLE |
| Evidence | Links, observations, data, test results, or artifacts |
| Assumptions | What remains unproven |
| Threshold | Measurable condition where applicable |
| Risks | Material downside and mitigation |
| Owner | Person accountable for the decision |
| Date | When the decision was made |
| Next action | Continue, experiment, pivot, stop, or defer |

## 7. How MK Framework connects to AISDF

Use MK Framework to decide whether and why to pursue an opportunity and how to manage its venture lifecycle. When software is part of the offer, use AISDF to engineer it:

1. Stage 5 defines the offer and intended outcome.
2. Stage 6.0 performs project X-Ray.
3. Stage 6.1–6.5 establishes approved requirements, architecture, source-of-truth documents, and implementation plan.
4. Human approval authorizes the work.
5. Stage 6.6–6.11 builds and verifies the software.
6. Stages 7–11 use real-world evidence to improve, reinvest, defend the advantage, and systemize.

**Non-negotiable:** evidence before transitions; AI assists, humans control; no unnecessary feature/architecture/token expansion (No AI Slope); verify before moving forward.

## 8. Limits and cautions

- This framework cannot prove market demand without real evidence.
- A competitor's success does not prove the same model will work in a different context.
- Founder advantages must be demonstrated, not merely asserted.
- Kill criteria should be measurable but should account for sample size, timing, and external shocks.
- A software release passing tests does not prove product-market fit.
- A moat must create durable user value and comply with law and ethical constraints.
- Systemization should not remove necessary human judgment or accountability.
