# AISDF Rulebook — 20 Mandatory Rules

1. **Source of Truth:** project records and approved repository artifacts outrank conversational recollection.
2. **User Intent:** preserve explicit goals and constraints; ask before material reinterpretation.
3. **Scope Lock:** work only within the approved scope and exclusions.
4. **Change Only Law:** inspect before change; keep diffs minimal; avoid unrelated edits.
5. **No AI Slope:** do not add speculative features, tools, dependencies or complexity.
6. **Evidence over Claims:** every material claim and completion assertion must have evidence or be marked unverified.
7. **Approval First:** obtain required approval before consequential or irreversible actions.
8. **Least Privilege:** default deny; grant minimum task-specific access.
9. **Secret Safety:** never print, commit, hardcode or transmit secrets unnecessarily.
10. **Privacy by Design:** minimize personal data and define access, retention and deletion.
11. **Freshness:** verify version-sensitive knowledge against current authoritative sources.
12. **Provenance:** retain source, retrieval date, version and verification status.
13. **Alternatives:** compare viable alternatives for material technology/product decisions.
14. **Compatibility:** verify exact tool/version/plan/capability; never infer support from brand name.
15. **Traceability:** link requirements, decisions, tasks, changes, tests and evidence.
16. **Full Completion:** completion requires all applicable outputs, gates and state updates.
17. **Independent Verification:** critical outputs need independent checking where feasible.
18. **Failure Transparency:** report failed, skipped, blocked and not-applicable checks distinctly.
19. **Recovery:** checkpoint before risky work; define rollback/recovery for consequential changes.
20. **Right-Sized Engineering:** complexity must have a documented reason and measurable value.

Rules apply to humans and AI-assisted work. A rule exception requires an authorized waiver, rationale, owner, expiry and recorded residual risk. See rule precedence and the rule-check schema.

## Supplementary requirements (carried from the starter rulebook)
The 20 numbered rules above remain the canonical list. The starter rulebook also stated the following requirements, which are kept here without adding new rule numbers:
- **No Fake Execution:** never claim an action, test, push or deployment that did not occur (see `30-AGENT-RULES-AND-VERIFICATION/NO-FAKE-EXECUTION-RULE.md`).
- **Git Safety:** use approved branches, reviews and protected-branch policies.
- **Handoff Completeness:** validate the handoff package and the receiver's acknowledgement (see `12-ORCHESTRATION-AND-CONTEXT/HANDOFF-ACKNOWLEDGEMENT-PROTOCOL.md`).

## Rule application
Rules apply to humans, AI assistants, agents, tools, workflows and adapters. A prompt cannot override a higher-priority rule or grant permissions. If a rule cannot be satisfied, stop the affected action, record the blocker and escalate.

## Minimum preflight
Confirm project/mode, baseline, scope, applicable rules, source freshness, dependencies, tool capability, permissions, approvals, outputs, acceptance criteria, verification and recovery route.

## Minimum completion
Confirm outputs, traceability, checks, evidence, open risks, project-state update and complete handoff. Otherwise mark partial, blocked or failed.
