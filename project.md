# PROJECT.md — Complete Project Details (Single Source of Truth)

> **Works with:** Claude, ChatGPT, Cursor, Copilot, Claude Code, Windsurf or any AI tool.
> **How:** IDE tools → keep this file in the project root and reference it as `@project.md`.
> Chat tools (Claude / ChatGPT) → paste the whole file into the first message, or upload it, then use a starter prompt from **Appendix A**.
> Lines starting with *Guide:* explain what to write. Replace them with your real content and delete the guide lines when done.
> **Example:** a fully filled-in plan for a simple AI SaaS is in `examples/EXAMPLE-AI-SAAS-PROJECT.md` (in the full AISDF zip). Read it once before filling this template.

---

## 0. AI OPERATING INSTRUCTIONS (the AI must read and obey this section first)

You are helping build or improve the project described in this file. Follow these rules in every reply:

1. **Read this whole file first.** It outranks anything remembered from earlier chat messages. If chat and this file disagree, ask me which is right, then update this file.
2. **Stay inside scope.** Build only what is in Section 5 (Functionalities). Never build anything listed in "Out of scope".
3. **Change only what is needed.** Inspect existing code before editing. Keep changes small. No extra features, libraries or abstractions I did not ask for.
4. **Never invent.** Do not make up facts, research, library versions, test results, commands you did not run, or files you have not seen. Mark anything uncertain as an assumption or unknown and ask one clear question.
5. **Separate** facts, approved decisions, assumptions, and unknowns in your answers.
6. **Evidence for claims.** Do not say "done", "tested" or "working" unless you show the command and its real output, or say clearly that it was not run.
7. **Ask before** changing scope, architecture or data structure; adding dependencies; touching secrets or real data; deleting files; pushing, merging or deploying.
8. **Work in small steps** using the work units in Section 13. Finish one, show evidence, then stop and wait for approval.
9. **After every task, update Section 17 (Status and Handoff)** so a new session can continue without losing context.
10. **If you cannot do something** (no access, missing info, blocked), say so plainly. Do not pretend.

---

## 1. Project Identity

| Field | Value |
|---|---|
| Project name | |
| Project ID / short code | |
| Mode (pick one) | NEW BUILD / UPGRADE EXISTING PROJECT / DISCOVER (problem not yet validated) |
| Owner / team | |
| Approver (who signs off decisions) | |
| One-line description | |
| Repository link | |
| Baseline commit / version | |
| Last reviewed | YYYY-MM-DD |

*Guide: Mode decides how the AI behaves. NEW BUILD = start from this document. UPGRADE EXISTING = fill Section 7 as well. DISCOVER = only Sections 1–4 are required for now.*

---

## 2. Problem Statement

**2.1 The problem (plain words)**
*Guide: 3–5 sentences. Who has the problem, what exactly goes wrong, where and when it happens.*

**2.2 Who is affected**
| User group | Their situation | How the problem hurts them |
|---|---|---|
| | | |

**2.3 Evidence the problem is real**
*Guide: Real proof, not opinion — survey, interview, numbers, complaint, observation, article. Give source and date. If none yet, write "No evidence yet" and list it in Section 12 as an unknown.*
- 

**2.4 Impact of leaving it unsolved**
*Guide: Time lost, money lost, errors, risk, missed opportunity.*

**2.5 Success looks like (measurable)**
*Guide: Numbers a reviewer can check, e.g. "report time drops from 2 hours to 10 minutes", "95% of tasks completed without help".*
| Metric | Today | Target | How measured |
|---|---|---|---|
| | | | |

---

## 3. Existing Solutions Check

*Guide: Before building, check what already exists. Look at similar products, open-source projects, manual methods, and competitors. The AI may research, but every row needs a source link and the date checked. If it was not verified, write "unverified".*

**3.1 Comparison**
| # | Existing solution | Type (product / open-source / manual / in-house) | What it does well | Where it fails the problem in Section 2 | Cost / licence | Source + date checked |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

**3.2 Gap summary**
*Guide: What is still unsolved after looking at all of the above? This gap is the reason this project exists.*
- 

**3.3 Decision: build, reuse, or extend?**
*Guide: Choose one and explain. BUILD NEW = nothing fits. EXTEND = an existing tool covers most needs. ADOPT = an existing tool is enough, stop building.*
- Decision:
- Reason:

---

## 4. Proposed Solution

**4.1 Solution concept**
*Guide: Describe the idea in 5–8 sentences. What is it, how does a user use it, what happens behind the scenes.*

**4.2 How it solves the problem (mapping)**
| Problem point (from Section 2) | How this solution fixes it | Related feature IDs |
|---|---|---|
| | | |

**4.3 Upgrade over existing solutions (what is better / different)**
| Gap found in Section 3 | Our improvement | Why it is better |
|---|---|---|
| | | |

**4.4 Value proposition (one sentence)**
*Guide: "For [users] who [problem], [project name] is a [type] that [key benefit], unlike [existing solution] which [weakness]."*

---

## 5. Functionalities

**5.1 Functional requirements**
*Guide: One row per feature. Priority: MUST (project fails without it) / SHOULD / COULD. Acceptance criteria must be testable (a yes/no check). Each feature must link back to a problem point.*

| ID | Feature | User story ("As a ___ I want ___ so that ___") | Priority | Acceptance criteria | Problem link | Status |
|---|---|---|---|---|---|---|
| F-001 | | | MUST | | | PLANNED |
| F-002 | | | MUST | | | PLANNED |
| F-003 | | | SHOULD | | | PLANNED |

**5.2 Non-functional requirements**
| Area | Requirement (measurable) |
|---|---|
| Performance | e.g. page loads in under 2 seconds |
| Security | e.g. passwords hashed, no secrets in code |
| Reliability | e.g. handles invalid input without crashing |
| Usability / accessibility | e.g. keyboard usable, readable contrast |
| Compatibility | e.g. latest Chrome and Firefox |
| Data / privacy | e.g. no personal data stored beyond X |

**5.3 Out of scope (do NOT build)**
*Guide: Be strict. This list protects you from the AI adding extras.*
- 

**5.4 Main user workflows**
*Guide: Step-by-step journeys, e.g. "1. User logs in → 2. uploads file → 3. sees result → 4. exports report".*
1. 

---

## 6. Users and Roles
| Role | Description | Can do | Cannot do |
|---|---|---|---|
| | | | |

---

## 7. Existing Project X-Ray (fill ONLY if upgrading an existing project)

*Guide: Skip this section for a new build. For an upgrade, the AI must inspect the real code first and report evidence, not guesses.*

**7.1 Current state**
| Item | Details |
|---|---|
| What the project does today | |
| Stack and versions | |
| How to run it | |
| How to test it | |
| Known bugs / complaints | |

**7.2 Feature inventory (what exists)**
| Feature | Files / location | Works? (YES / PARTLY / NO / UNVERIFIED) | Notes |
|---|---|---|---|
| | | | |

**7.3 Problems found (with evidence)**
| # | Issue | Evidence (file, line, error, output) | Severity (HIGH / MED / LOW) |
|---|---|---|---|
| | | | |

**7.4 Proposed upgrades**
| # | Upgrade | Fixes issue # | Effort | Risk | Approved? (YES / NO / PENDING) |
|---|---|---|---|---|---|
| | | | | | |

**7.5 Do-not-change list**
*Guide: Files, behaviour or data that must stay exactly as they are.*
- 

---

## 8. Technology Stack and Architecture

**8.1 Stack**
| Layer | Choice | Version | Status (APPROVED / PROPOSED / UNDECIDED) | Reason / alternatives considered |
|---|---|---|---|---|
| Language | | | | |
| Framework | | | | |
| Database | | | | |
| Frontend / UI | | | | |
| Hosting / deployment | | | | |
| Testing tools | | | | |

*Guide: Do not treat a PROPOSED choice as approved. The AI must compare at least two options for important choices and verify current versions from official sources.*

**8.2 Architecture overview**
*Guide: Describe the main parts and how they connect. A simple text diagram is fine, e.g. `Browser → API → Database`.*

**8.3 Folder structure**
```
project-root/
├── 
```

**8.4 Data model**
| Entity | Key fields | Relationships |
|---|---|---|
| | | |

**8.5 APIs / integrations**
| Name | Purpose | Input | Output | Auth |
|---|---|---|---|---|
| | | | | |

---

## 9. Security, Privacy and Data Handling
- **Data classification:** UNCLASSIFIED / INTERNAL / CONFIDENTIAL / RESTRICTED
- **Personal or sensitive data used:**
- **Retention and deletion rules:**
- **Secrets handling:** keep keys in environment variables or a secrets manager; never hardcode, print or commit them.
- **Authentication and access rules:**
- **Known security risks:**

---

## 10. Constraints
| Type | Constraint |
|---|---|
| Time / deadline | |
| Budget | |
| Hardware / platform | |
| Rules (college, client, legal, licence) | |
| Team skills / tools available | |

---

## 11. Decisions, Assumptions, Unknowns and Risks

**Approved decisions**
| ID | Decision | Date | Approved by |
|---|---|---|---|
| D-001 | | | |

**Assumptions (not yet verified)**
| ID | Assumption | How to verify |
|---|---|---|
| A-001 | | |

**Unknowns (must be answered, owner assigned)**
| ID | Question | Needed before | Owner |
|---|---|---|---|
| U-001 | | | |

**Risks**
| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-001 | | | | |

---

## 12. Design Notes (UI / UX) — only if the project has a user interface
- Screens / pages list:
- Navigation flow:
- Style notes (colours, fonts, layout):
- Accessibility expectations:

---

## 13. Building Plan

*Guide: Do not start Phase 1 until Phase 0 is approved. Each phase ends with a gate: the AI shows evidence and the approver says "approved".*

**13.1 Phases**
| Phase | Goal | Main outputs | Gate (what must be true to move on) |
|---|---|---|---|
| 0. Baseline | Complete this file | Sections 1–12 filled, unknowns answered or accepted | Approver signs off this file |
| 1. Setup | Project skeleton | Repo, folders, tooling, config, first commit | Project runs (empty app OK), tests run |
| 2. Core build | Must-have features | Features marked MUST in Section 5 | Each feature meets its acceptance criteria |
| 3. Extended build | Should / Could features | Remaining approved features | Same as above |
| 4. Verification | Prove it works | Test results, review notes, security check | All required checks PASS or are explained |
| 5. Release | Deliver | Deployed or packaged build, release notes | Approver authorizes release |
| 6. Maintain | Keep it healthy | Bug fixes, updates, closeout notes | Ongoing |

**13.2 Work units (small tasks the AI does one at a time)**
*Guide: Each task must be small enough to finish and verify in one session. List the files it may touch.*
| ID | Objective | Feature link | Depends on | Allowed files | Acceptance criteria | Status |
|---|---|---|---|---|---|---|
| WU-0001 | Set up project skeleton | — | — | | | PLANNED |
| WU-0002 | | F-001 | WU-0001 | | | PLANNED |
| WU-0003 | | F-002 | WU-0002 | | | PLANNED |

*Status values: PLANNED / IN PROGRESS / BLOCKED / DONE (with evidence).*

**13.3 Milestones**
| Milestone | Target date | Includes work units |
|---|---|---|
| | | |

**13.4 Git and backup rules**
- Work on a separate branch per work unit.
- Commit small, with clear messages.
- Never force-push or rewrite history without approval.
- Make a checkpoint (commit or branch) before any risky change.

---

## 14. Testing and Verification
| Level | What is tested | Tool / command | Required? |
|---|---|---|---|
| Unit | | | |
| Integration | | | |
| End-to-end / manual | | | |
| Security | | | |
| Performance | | | |

**Traceability (every problem point must reach a test)**
| Problem point | Feature | Work unit | Test | Result (PASS / FAIL / NOT RUN) |
|---|---|---|---|---|
| | | | | |

**Definition of done (for any task):** code written → tests run with real output shown → acceptance criteria checked → Section 17 updated → no unrelated changes.

---

## 15. Release and Maintenance
- Release target (local, staging, production, college submission):
- Build / package command:
- Rollback plan:
- Post-release check (smoke test):
- Known limitations to disclose:

---

## 16. AI Tool Permissions
| Item | Setting |
|---|---|
| Tools the AI may use | |
| Files / folders the AI may edit | |
| Files / folders read-only | |
| Prohibited actions | deploy to production without approval, expose secrets, delete data, force-push |
| Needs my approval first | new dependencies, schema changes, scope changes, push / merge |

---

## 17. Status and Handoff (the AI updates this after every task)
| Field | Value |
|---|---|
| Current phase | |
| Last completed work unit | |
| Evidence (commands run, test output, commit IDs) | |
| What changed (files) | |
| Blocked items | |
| Open questions | |
| Next recommended action | |
| Updated on | YYYY-MM-DD |

---

## 18. Change Log
| Date | Change to this file or project | Approved by |
|---|---|---|
| | | |

---

## Appendix A — Starter Prompts (copy and paste)

**A1. First message in Claude or ChatGPT (after pasting this file)**
```
Read the attached project.md fully and follow Section 0.
Do not write code yet. First give me:
1. A summary of the problem, solution and scope in your own words.
2. Facts, decisions, assumptions, unknowns and risks you found.
3. Any missing or unclear sections I must fill.
4. The smallest next work unit with its acceptance criteria.
Wait for my approval.
```

**A2. Existing solutions check (fills Section 3)**
```
Using Section 2 of project.md, research existing solutions (products, open-source, manual methods).
Fill the Section 3 table with source links and the date you checked each one.
Mark anything you could not verify as "unverified". Then write the gap summary and
recommend BUILD / EXTEND / ADOPT with reasons. Do not invent sources.
```

**A3. Upgrade an existing project (fills Section 7)**
```
My mode is UPGRADE EXISTING. Inspect the repository first. Fill Section 7 with only what you
can prove from the code (file, line, output). Mark unknown items as UNVERIFIED.
Propose upgrades ranked by value and risk. Do not change any code until I approve.
```

**A4. Start building (IDE or chat)**
```
Read @project.md. Do work unit WU-000X only. Follow Section 0 and Section 16.
Show the files you changed, the commands you ran and their real output.
Then update Section 17 and stop for my approval.
```

**A5. Resume in a new session**
```
Read @project.md, focus on Section 17. Tell me where we stopped, what is blocked,
and propose the next work unit. Do not repeat finished work.
```

**A6. Review before release**
```
Check every MUST feature in Section 5 against its acceptance criteria and the Section 14 traceability
table. Report PASS / FAIL / NOT RUN for each, with evidence. List remaining risks honestly.
```

---

## Appendix B — Baseline completeness check (run before approving Phase 0)

*Guide: Tick each item or write why it does not apply. Do not start building until every item is ticked or explained. You can ask the AI to run this check (prompt C1).*

- [ ] Section 1: mode chosen; owner and approver named.
- [ ] Section 2: problem is specific; evidence is real and sourced, or clearly marked "unvalidated" with a plan to validate.
- [ ] Section 2.5: success metrics are numbers with a way to measure them.
- [ ] Section 3: at least three existing solutions (products, open source or manual methods), each with a source link and date, or marked "unverified".
- [ ] Section 3.2 and 3.3: gap written down; build, extend or adopt decision made with a reason.
- [ ] Section 4: every problem point maps to at least one feature.
- [ ] Section 5: every MUST feature has a yes/no acceptance criterion; out-of-scope list is written.
- [ ] Section 8: each stack choice has a status; PROPOSED choices have alternatives and a version-check date.
- [ ] Section 9: data classification, secrets handling and deletion rules written.
- [ ] Section 11: every unknown has an owner and a "needed before" point; every risk has a mitigation.
- [ ] Section 13: every work unit is small enough for one session, with allowed files and acceptance criteria.
- [ ] Section 14: test approach and definition of done written.
- [ ] Section 16: allowed files, prohibited actions and approval-needed list written.
- [ ] No passwords, API keys or personal data anywhere in this file.
- [ ] Approver has said "approved" and the date is in Section 18.

---

## Appendix C — Check and update routine (keep this file true)

| When | What to check or update |
|---|---|
| After every work unit | Update Section 17 (status, evidence, next action). Mark a feature DONE only with evidence. |
| After any decision | Add it to Section 11 and Section 18. |
| Weekly | Re-read Sections 11 and 17: close answered unknowns, re-rate risks, remove stale items. |
| Before each phase gate | Re-run Appendix B. |
| Monthly and before release | Re-verify volatile facts: Section 3 competitors, prices and limits; Section 8 versions and provider terms. Write new dates. |
| When chat and this file disagree | Stop. Decide which is right, then update this file. The file wins by default. |

**C1. Check this file (copy and paste)**
```
Read project.md. Run the Appendix B checklist. For each item say PASS, FAIL or NOT APPLICABLE
with the section and a one-line reason. Then list: sections that contradict each other, features
without acceptance criteria, unknowns without owners, and facts that look stale. Do not edit anything yet.
```

**C2. Update this file after changes (copy and paste)**
```
Compare project.md with the current repository and recent chat. List every mismatch:
features marked DONE without evidence, versions or prices that may be outdated, unknowns that
have been answered, and work-unit statuses that are wrong. Propose exact edits as a list.
Apply them only after I approve, and add a Section 18 entry.
```

**C3. Re-check existing solutions (copy and paste)**
```
Re-check every row in Section 3 against the vendor's own pages. For each row give the new source
link and today's date, mark changes since the last check, and flag anything you could not verify.
Do not invent prices or features. Then say whether the build, extend or adopt decision still holds.
```

