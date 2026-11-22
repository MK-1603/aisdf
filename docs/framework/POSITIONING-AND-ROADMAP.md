# Positioning and Roadmap

## What AISDF is (and is not)
AISDF is a **governance and verification layer above AI coding tools**: shared rules, specialist role contracts, approval-bound task plans, evidence, independent review and a release gate. It is not a coding agent, an LLM, a sandbox or an IDE.

## Category and honest claim
The agent runtimes (OpenCode, OpenHands, Cline, Aider and similar) are different products: AISDF should integrate with them, not compete. Its peers are the spec-driven-development frameworks (for example GitHub Spec Kit, BMAD-METHOD, OpenSpec, Superpowers). They largely provide spec and workflow structure for many tools; **AISDF's differentiator is verification**: approval bound to content, evidence that cannot be typed in, tamper-evident history, an independent-review package, pinned security tooling and a release gate.

"Top 1 in the world" is not a measurable claim and AISDF does not make it. The defensible target is: **the most verifiable multi-tool AI engineering framework**, proven by published results rather than adjectives.

## Measurable criteria (publish results, including failures)
1. **Conformance matrix** filled in for at least 5 tools (`adapters/COMPATIBILITY.md`).
2. **Benchmark:** the same 10 small tasks run (a) without AISDF and (b) with AISDF in the same tool and model; compare false completion claims, scope violations, secrets leaked, defects found by independent review, and human minutes.
3. **Rule enforcement coverage:** raise the code-enforced share in `RULES-AND-ENFORCEMENT.md` (today 3 full + 5 partial of 20).
4. **Interop:** import/export of spec artifacts from Spec Kit and OpenSpec so AISDF can sit above them.
5. **Security:** every release publishes `verify-ledger` + `gate` output and the scanner lock used.
6. **Adoption signals** (stars, forks, contributors) are tracked but not treated as proof of quality.

## Roadmap
| Milestone | Content | Exit test |
|---|---|---|
| 1.0.0 (this release) | Hardened control plane, governed executor, gate, findings, review package, memory checker, scanner pins | All tests + validator pass; documented limits |
| 1.1 | Reference adapter for one open-source agent; real conformance run; sandbox profile (container) | I3/I4 evidence committed |
| 1.2 | Requirement-to-test traceability checker; file-level scope enforcement from task allow-lists | R03/R15 move to CODE |
| 1.3 | Goldfish runner that launches a fresh read-only reviewer and verifies isolation | R17 moves to CODE |
| 1.4 | Scanner wrappers that execute pinned tools and parse their output into checks | Gate evidence from real scanners |
| 2.0 | Stable adapter API, signed releases, published benchmark | Third-party adapters exist |
