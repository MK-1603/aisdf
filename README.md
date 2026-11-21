# AISDF — AI Software Development Framework

**From problem statement to production software, with AI tools kept under control.**
Version **3.3.0** (consolidated build with a worked example) · Status: **specification and local-validation foundation, not production-proven**

---

## 1. What is AISDF? (plain words)

AISDF is a **rulebook, playbook and toolkit** for building or improving software together with AI tools (Claude, ChatGPT, Cursor, GitHub Copilot, Claude Code and similar) or with a human team.

It is **not** an app, an AI model, an IDE or a hosted service. It is a set of documents, prompts, templates, JSON schemas and a small Python checker. You give the AI these rules and a filled-in [`project.md`](project.md); the AI then works in small, approved, evidence-backed steps instead of guessing.

## 2. The problem it solves

When people ask an AI to "build me an app", the usual failures are: invented features, skipped tests, "it works" claims with no proof, forgotten decisions between chat sessions, and unrequested rewrites of existing code. AISDF prevents these with:

- **One source of truth** — [`project.md`](project.md) holds the problem, existing-solutions check, solution, functionalities, upgrade analysis and building plan.
- **Fixed rules** — 20 mandatory rules (scope lock, evidence over claims, approval first, least privilege, no AI slope, and more).
- **Gated workflows** — nothing moves to the next phase until the required evidence exists and the approver says yes.
- **Handoff and checkpoints** — a new chat or a new AI can resume from the recorded project state.

## 3. Download the project brief: `project.md`

| | |
|---|---|
| **File** | [`project.md`](project.md) (root of this repository / zip) |
| **What it is** | One complete, fill-in project brief that any AI tool can read |
| **Sections** | AI rules · identity · **problem statement** · **existing solutions check** · **proposed solution (and upgrade over existing)** · **functionalities** · users · existing-project X-Ray · tech stack and architecture · security · constraints · decisions, assumptions, unknowns, risks · UI notes · **building plan** · testing · release · AI permissions · status/handoff · change log · starter prompts |
| **Check and update** | Appendix B (baseline completeness checklist), Appendix C (check-and-update routine) and prompts C1–C3 keep the file true while you build |
| **Works with** | Claude, ChatGPT, Cursor, Copilot, Claude Code, or any assistant that can read a pasted or attached file |

**How to download it**
- From the zip: open the repository folder and take `project.md` from the top level.
- From GitHub (after you publish this repository): open `project.md`, click **Raw**, then save the page, or use the download button on the file view.
- Copy it into **your own project's folder**, rename nothing, and fill it in. Keep the `AI OPERATING INSTRUCTIONS` section at the top.

### See a complete example first
[`examples/EXAMPLE-AI-SAAS-PROJECT.md`](examples/EXAMPLE-AI-SAAS-PROJECT.md) is a fully filled-in `project.md` for a simple AI SaaS (NoteDigest: paste text, get a structured summary, with login, monthly quota and history). It shows the problem statement, an existing-solutions check with sources and dates, the proposed solution, 11 functionalities with acceptance criteria, stack and architecture, security, risks, a 15-step work-unit build plan, tests and a release checklist. Copy it, replace the example values with yours, and build it yourself one work unit at a time. The existing-solutions research in it was done on 2026-11-21; everything else is a proposed plan, not a verified fact.

## 4. How to use it (three ways)

### A. In a chat tool (Claude or ChatGPT)
1. Fill in [`project.md`](project.md) (at least Sections 1, 2, 4 and 5).
2. Start a new chat. Attach or paste the whole `project.md`.
3. Paste starter prompt **A1** from the bottom of `project.md` (summary, facts, unknowns, risks, smallest next step, no code yet).
4. Approve or correct. Then use prompts **A2** (existing-solutions research), **A3** (upgrade an existing project), **A4** (build one work unit), **A5** (resume later), **A6** (pre-release review).
5. When the chat ends, copy the AI's updated Section 17 (Status and Handoff) back into your file.

### B. In an IDE assistant (Cursor, Copilot Chat, Windsurf and similar)
1. Put `project.md` in the project root.
2. Reference it in chat (for example `@project.md` in tools that support file mentions) or attach it, and use prompt **A4** for one work unit at a time.
3. For tools that read a rules file automatically, copy Section 0 of `project.md` into that tool's rules file so the rules load every session. Check your tool's documentation for the exact file name.

### C. With the full framework (recommended for larger projects)
1. Read [`AISDF-MISSION-AND-SCOPE.md`](AISDF-MISSION-AND-SCOPE.md), [`AISDF-CORE-PRINCIPLES.md`](AISDF-CORE-PRINCIPLES.md) and [`00-GOVERNANCE/AISDF-RULEBOOK.md`](00-GOVERNANCE/AISDF-RULEBOOK.md).
2. Choose a mode in [`modes/`](modes/) (see Section 6).
3. Fill in `project.md` and, if you want machine-readable records, `templates/PROJECT-PROFILE.template.yaml`.
4. Give the AI [`prompts/MASTER-ENTRY-PROMPT.md`](prompts/MASTER-ENTRY-PROMPT.md) plus the role prompt it needs from [`prompts/roles/`](prompts/roles/).
5. Follow the matching workflow in [`workflows/`](workflows/). Approve each gate.
6. Record real commands, diffs, test output, approvals and evidence. Close with a completion report.
7. Run the repository quality gate (Section 12) before you publish changes to the framework itself.

## 5. Step-by-step: from idea to release

| Step | What you do | Where |
|---|---|---|
| 1 | Choose the mode: Discover, New Build or Upgrade Existing | `project.md` §1, `modes/` |
| 2 | Write the problem statement with evidence | `project.md` §2 |
| 3 | Check existing solutions and write down the gap | `project.md` §3 (prompt A2) |
| 4 | Describe the solution and what it improves | `project.md` §4 |
| 5 | List functionalities with testable acceptance criteria | `project.md` §5 |
| 6 | If upgrading, X-Ray the existing code first | `project.md` §7 (prompt A3) |
| 7 | Choose stack and architecture; record unknowns and risks | `project.md` §8–11 |
| 8 | **Check and approve the baseline** — run the completeness checklist (prompt C1); nothing is built before this | `project.md` Appendix B, §13 Phase 0 |
| 9 | Build one small work unit at a time | `project.md` §13.2 (prompt A4) |
| 10 | Test, review independently, trace each requirement to a test | `project.md` §14, `workflows/WF-004-QUALITY-AND-RELEASE-GATE.md` |
| 11 | Release only with authorization; record rollback | `project.md` §15 |
| 12 | Keep §17 Status and Handoff current after every task; re-check and update weekly and before each phase gate (prompts C2, C3) | `project.md` §17, Appendix C |

## 6. Operating modes

| Mode | Use when | Outcome | File |
|---|---|---|---|
| **1. Problem Discovery** | You are not sure the problem is real | Decision: PROCEED, INVESTIGATE, PIVOT, DEFER or STOP | [`modes/MODE-1-PROBLEM-DISCOVERY.md`](modes/MODE-1-PROBLEM-DISCOVERY.md) |
| **2. New Project** | You have an idea or document to turn into software | Approved baseline, then gated build and release | [`modes/MODE-2-NEW-PROJECT.md`](modes/MODE-2-NEW-PROJECT.md) |
| **3. Existing Project X-Ray** | You already have a codebase to inspect and improve | Evidence-based gaps and controlled upgrades | [`modes/MODE-3-EXISTING-PROJECT.md`](modes/MODE-3-EXISTING-PROJECT.md) |

Lifecycle overview: Intake → Analyze and validate → Define → Design → Plan → Build → Test and verify → Deploy → Operate and maintain. See [`AISDF-LIFECYCLE-OVERVIEW.md`](AISDF-LIFECYCLE-OVERVIEW.md) and [`AISDF-FUNCTIONAL-MAP.md`](AISDF-FUNCTIONAL-MAP.md).

## 7. What is in this repository (names and purpose)

### Root documents
| File | Purpose |
|---|---|
| `README.md` | This guide |
| [`project.md`](project.md) | **Downloadable project brief template** |
| [`examples/EXAMPLE-AI-SAAS-PROJECT.md`](examples/EXAMPLE-AI-SAAS-PROJECT.md) | **Worked example:** a complete filled-in plan for a simple AI SaaS |
| `QUICK-START.md` | Short numbered start guide |
| `AISDF-MISSION-AND-SCOPE.md` | What AISDF does and does not do |
| `AISDF-CORE-PRINCIPLES.md` | The 12 core principles |
| `AISDF-LIFECYCLE-OVERVIEW.md` | Nine-phase lifecycle |
| `AISDF-FUNCTIONAL-MAP.md` | Eight capability systems (A–H) |
| `DOMAIN-MAP.md` | List of the 31 numbered domain folders |
| `MASTER-ENTRY-PROMPT.md` | Master prompt (same text as `prompts/MASTER-ENTRY-PROMPT.md`) |
| `IMPLEMENTATION-STATUS.md`, `RELEASE-READINESS.md` | Honest status and release checklist |
| `CHANGELOG.md`, `VERSION`, `CITATION.cff` | Version history, current version, citation data |
| `GOVERNANCE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`, `LICENSE-DECISION.md` | Project governance and community files |

### Folders
| Folder | What it holds |
|---|---|
| `00-GOVERNANCE/` | Rulebook (20 rules), precedence, definitions, policies, standards, checklists |
| `01-` … `30-` | Domain guides by engineering area; with `00-GOVERNANCE` these are the 31 domain folders (see Section 9) |
| `engines/` | 56 capability specifications, `E-001` … `E-056` |
| `modes/` | The three operating modes |
| `workflows/` | WF-001 New Project from Document · WF-002 Existing Project X-Ray · WF-003 Work Unit and Handoff · WF-004 Quality and Release Gate |
| `prompts/` | Master prompt, phase prompts (requirements, UX, architecture, implementation, testing, release), recovery prompts, handoff prompt |
| `prompts/roles/` | Ten role prompts: Analyst, Product Engineer, Requirements Engineer, UX Designer, Software Architect, Implementer, Test Engineer, Code Reviewer, Security Reviewer, Release Engineer |
| `schemas/` | 8 JSON Schemas: work unit, checkpoint, completion report, knowledge entry, source evidence, rule check result, tool capability profile, alternative evaluation |
| `templates/` | Project profile, work unit and checkpoint YAML templates |
| `registries/` | Engine, rule, technology and adapter registers |
| `REFERENCE-PROJECTS/DEVTRACK/` | Specification and validation plan for a demo project (**not implemented**) |
| `ASSESSMENT/` | Maturity rubric, dated assessment, and the consolidation report |
| `tools/`, `tests/` | Repository validator and pytest checks |
| `.github/workflows/` | GitHub Actions validation workflow |
| `reference/` | Blueprint source notes |
| `examples/` | Guidance for examples, plus the worked AI SaaS example plan (a plan only; the app has not been built) |

### Governance files (`00-GOVERNANCE/`)
- **Rules and precedence:** `AISDF-RULEBOOK.md`, `RULE-PRECEDENCE-AND-CONFLICT-RESOLUTION.md`, `AISDF-DEFINITIONS.md`
- **Evidence and knowledge:** `EVIDENCE-AND-PROVENANCE-POLICY.md`, `KNOWLEDGE-FRESHNESS-AND-REVIEW-POLICY.md`
- **Policies (PROPOSED until approved):** change management, deprecation, privacy, security, versioning
- **Standards:** documentation, engine specification, schema, workflow, file naming, file format, contribution, release rules
- **Checklists and registers:** governance review, release readiness, policy exception register

## 8. The 20 mandatory rules (short names)

1 Source of Truth · 2 User Intent · 3 Scope Lock · 4 Change Only Law · 5 No AI Slope · 6 Evidence over Claims · 7 Approval First · 8 Least Privilege · 9 Secret Safety · 10 Privacy by Design · 11 Freshness · 12 Provenance · 13 Alternatives · 14 Compatibility · 15 Traceability · 16 Full Completion · 17 Independent Verification · 18 Failure Transparency · 19 Recovery · 20 Right-Sized Engineering.
Full text: [`00-GOVERNANCE/AISDF-RULEBOOK.md`](00-GOVERNANCE/AISDF-RULEBOOK.md).

## 9. The 31 domain folders

`00` Governance · `01` Methodology · `02` Project Intelligence · `03` Requirements Engineering · `04` Product Engineering · `05` UX/UI Engineering · `06` Technology Intelligence · `07` Engineering Knowledge · `08` Software Architecture · `09` Platform Engineering · `10` AI and Model Engineering · `11` Agent Engineering · `12` Orchestration and Context · `13` Harness and Execution · `14` Security and Privacy · `15` Data and Database Engineering · `16` API and Integration Engineering · `17` Testing and Verification · `18` DevOps and Cloud Engineering · `19` Deployment and Operations · `20` Reliability and Observability · `21` Distributed Systems and Scalability · `22` Cost and Resource Governance · `23` Legal and Compliance · `24` Product Analytics and Support · `25` Framework Maintenance · `26` Distribution and Extensions · `27` Standards and Compatibility · `28` Templates and Examples · `29` Benchmarks and Evaluation · `30` Agent Rules and Verification.

Most domain folders contain a short guide only; the detailed contracts live in `engines/` and `00-GOVERNANCE/`. Folders `06`, `07`, `12`, `27` and `30` also hold specific policies and protocols.

## 10. The 56 engines (capability specifications)

An engine is a documented capability contract, **not** a program, agent or service. Each file has purpose, scope, inputs, outputs, procedure, decision rules, approvals, failure behaviour, evidence and test scenarios.

| Group | Engines |
|---|---|
| Intake and discovery | E-001 Intake and Mode Selection · E-002 Document Ingestion · E-003 Problem Discovery · E-004 Existing Project X-Ray · E-005 Feature Inventory |
| Problem, product and requirements | E-006 Problem Validation · E-007 Product/Market Validation · E-008 Gap, Conflict and Ambiguity · E-009 Risk, Inversion and Premortem · E-010 Scope and Kill-Criteria · E-011 User and Stakeholder Intelligence · E-012 Requirements Engineering · E-013 Feature Prioritization · E-014 Product Specification · E-015 Acceptance Criteria · E-016 Traceability |
| UX/UI | E-017 UX Research and Journey · E-018 Information Architecture · E-019 Interaction and Flow Design · E-020 UI and Design System · E-021 Design Tool Selection and Handoff · E-022 Usability and Accessibility Review |
| Technology and architecture | E-023 Technology Research · E-024 Stack Selection · E-025 Architecture Design · E-026 Data and Database Design · E-027 API and Integration Design · E-028 Infrastructure and Scaling Design · E-029 Cost and Capacity Analysis · E-030 Architecture Decision and Change Control |
| Knowledge and tool intelligence | E-031 AKIS Knowledge Intelligence · E-032 AFIAE Feature and Tool Discovery · E-033 Tool/Service Evaluation · E-034 Compatibility Verification |
| Planning and execution | E-035 Execution Planning · E-036 Task and Dependency Orchestration · E-037 Agent Role and Delegation · E-038 Context and Handoff · E-039 Tool/IDE Adapter · E-040 Project State and Continuity · E-041 Git and Change Orchestration · E-042 Human Approval and Escalation |
| Quality and verification | E-043 Test Strategy and Generation · E-044 Build, Test and Debug · E-045 Code Review and Change Impact · E-046 Security and Privacy · E-047 Performance and Load · E-048 Independent Verification · E-049 UX and Accessibility Verification · E-050 Release Readiness |
| Delivery and lifecycle | E-051 CI/CD Pipeline Design · E-052 Deployment and Environment · E-053 Production Verification · E-054 Observability and Incident Readiness · E-055 Maintenance and Change Governance · E-056 Project Closeout and Learning |

Registry table: [`registries/ENGINE-REGISTRY.md`](registries/ENGINE-REGISTRY.md).

## 11. Common ways to use it

| Goal | What to do |
|---|---|
| Plan a college or personal project | Fill `project.md` §1–5, get the AI to fill §3 (existing solutions), approve, then build work units |
| Compare against existing products | Prompt **A2** in `project.md`; every row needs a source link and date, or is marked "unverified" |
| Upgrade an old project | Mode 3 + `project.md` §7 + prompt **A3**; no code changes until you approve the upgrade list |
| Continue after a long break or new chat | Prompt **A5**; the AI reads §17 and resumes |
| Hand work from one AI to another | `prompts/HANDOFF-AGENT-TO-AGENT.md` and `workflows/WF-003-WORK-UNIT-HANDOFF.md` |
| Check work before release | Prompt **A6** and `workflows/WF-004-QUALITY-AND-RELEASE-GATE.md` |
| See a complete filled-in plan for a small AI SaaS | `examples/EXAMPLE-AI-SAAS-PROJECT.md` |
| Check that `project.md` is complete and still true | Appendix B checklist; prompts **C1** (check), **C2** (update), **C3** (re-check existing solutions) |
| Recover when the AI is stuck or lost context | `prompts/RECOVERY-BLOCKED-TASK.md`, `prompts/RECOVERY-CONTEXT-LOSS.md` |

## 12. Repository quality gate

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_repository.py
python -m pytest
```

The validator checks required files (including `project.md`), engine numbering and contracts, JSON Schema validity, fixtures and internal Markdown links. It is a **documentation quality gate**; it does not prove that any software built with AISDF is correct, secure or production-ready.

## 13. Honest status and limits

- Engines are specifications, not running agents. No hosted AISDF runtime exists.
- No external AI tool, IDE, API or MCP adapter has been certified; a listed adapter is not a verified one.
- The DevTrack reference project is a specification only; no application has been built through AISDF yet.
- The GitHub Actions workflow has not been run on a real remote repository in this build.
- **License is not selected.** See `LICENSE-DECISION.md`. Do not assume this repository is open-source licensed. The maintainer, license and monitored security contact must be set before public release.
- Policies marked PROPOSED are advisory until approved by maintainers.
- See `IMPLEMENTATION-STATUS.md`, `RELEASE-READINESS.md` and `ASSESSMENT/` for details.

## 14. Version history

| Version | Summary |
|---|---|
| 3.3.0 | Adds the worked AI SaaS example plan (`examples/EXAMPLE-AI-SAAS-PROJECT.md`) and `project.md` Appendices B and C (completeness check, check-and-update routine, prompts C1–C3) |
| 3.2.0 | **Consolidated build.** Based on 3.1.0; adds `project.md`, merges unique policies, standards and checklists from 3.0.1, restores fuller starter text that 3.1.0 had condensed, adds `CITATION.cff`, fixes domain README titles. See `ASSESSMENT/CONSOLIDATION-REPORT-3.2.0.md` |
| 3.1.0 | Engine-specific contracts, DevTrack specification, maturity rubric, validator and tests |
| 3.0.1 | Nested governance folders (policies, rules, compliance checklists, foundation definitions). Its changelog was never updated, and engine filenames still contained commas |
| 3.0.0 | Foundation: 31 domains, 56 engine files, modes, workflows, schemas, validator |
| Starter | Initial small seed (governance core, schemas, CITATION.cff, YAML registries) |

## 15. Contributing and support

Read `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md` and `SUPPORT.md`. Contributions must not claim verification without reproducible evidence.
