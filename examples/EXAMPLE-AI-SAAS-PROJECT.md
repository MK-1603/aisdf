# PROJECT.md — EXAMPLE: NoteDigest (a simple AI SaaS)

> **This is a filled-in example of `project.md`.** It shows how to plan a small AI SaaS (a paste-in text summarizer with login, quota and history) from problem statement to release, using the AISDF template.
> **How to use it:** copy this file, rename it `project.md`, replace every example value with your own, then follow the "Your build checklist" at the end. Do not treat any example number, tool or price as verified for your project.
> **What is real and what is example:** the existing-solutions research in Section 3 was done on 2026-11-21 with the sources listed. Everything else (feature list, limits, stack, timeline) is a proposed plan, not an approved decision.
> Works with Claude, ChatGPT, Cursor, Copilot, Claude Code or any AI tool: paste or attach the whole file.

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
| Project name | NoteDigest (example name, change it) |
| Project ID / short code | ND |
| Mode (pick one) | NEW BUILD |
| Owner / team | [Your name], solo builder |
| Approver (who signs off decisions) | [Your name] (add a reviewer or guide if you have one) |
| One-line description | A small web app where a signed-in user pastes text (meeting transcript, email thread, notes) and gets a structured digest: summary, decisions, action items, open questions |
| Repository link | [add after creating the repo] |
| Baseline commit / version | none yet (Phase 0) |
| Last reviewed | 2026-11-21 |

---

## 2. Problem Statement

**2.1 The problem (plain words)**
People often end up with long, unstructured text: a meeting transcript, a chat export, an email thread, lecture notes. To find out what was decided and who must do what, they re-read everything by hand. This is slow, and action items get missed. Existing note-taker tools mostly focus on recording meetings with a bot and charge per seat or with usage caps, which is more than someone needs when they already have the text.

**2.2 Who is affected**
| User group | Their situation | How the problem hurts them |
|---|---|---|
| Students and project teams | Long group-chat or meeting notes after a session | Tasks and deadlines get lost in the text |
| Freelancers and small-team members | Email threads and call transcripts from clients | Time spent re-reading; missed follow-ups |
| Anyone with exported transcripts | Already has the text, no need for a recording bot | Pays for or learns tools built for another workflow |

**2.3 Evidence the problem is real**
- Secondary evidence only (pricing structures of existing tools, see Section 3). **No primary evidence yet.**
- Action required (U-001): interview or survey 5 people from the groups above and record what they do today, how long it takes, and what they would pay. Until then this problem is **unvalidated**.

**2.4 Impact of leaving it unsolved**
Time lost re-reading, missed action items, and inconsistent notes. Size of impact is unknown until U-001 is done.

**2.5 Success looks like (measurable)**
| Metric | Today | Target | How measured |
|---|---|---|---|
| Time to get a digest from existing text | measure manually on 5 samples (U-002) | under 30 seconds for input up to 20,000 characters | Timer in the app and manual stopwatch on the evaluation set |
| Action-item accuracy | not measured | at least 80% of action items judged correct on the evaluation set | Manual rubric on 10 synthetic samples (Section 14) |
| Cost per digest | unknown | below a cap you set after verifying provider pricing (U-003) | Log input and output tokens per digest and multiply by the verified price |
| Task completion | not measured | 4 of 5 test users finish "paste text, read digest" without help | Observed usability test |

---

## 3. Existing Solutions Check

*Date checked: 2026-11-21. Rows marked "third-party" come from review sites, not the vendor, so treat the numbers as unverified until you open the vendor's own page. Prices and limits change often.*

**3.1 Comparison**
| # | Existing solution | Type | What it does well | Where it fails the problem in Section 2 | Cost / licence | Source + date checked |
|---|---|---|---|---|---|---|
| 1 | Otter.ai | SaaS meeting notetaker | Real-time transcription and AI summaries of meetings; searchable notes; has a free tier | Built around recording or importing meetings; free tier reported at 300 minutes per month, 30 minutes per conversation, 3 lifetime file imports; paid plans are per user. Whether it accepts plain pasted text is **unverified** | Free; reported Pro $16.99 monthly or $8.33 annual per user, Business $30 monthly or $19.99 annual | Third-party: https://meetergo.com/en/magazine/otter-ai-pricing (free-tier limits, that site checked 2026-08-11) and https://www.castmagic.io/blog/otter-ai-pricing (paid prices, as of Aug 2026). Official page https://otter.ai/pricing not yet verified. Checked 2026-11-21 |
| 2 | Fireflies.ai | SaaS meeting notetaker | Transcription on all plans; AI summaries and action items; many integrations | Per-seat pricing; advanced AI features are metered by AI credits; free tier storage reported at 400 minutes per team | Free; Pro $10 annual or $18 monthly per user; Business $19 annual or $29 monthly (vendor help center) | Official: https://guide.fireflies.ai/articles/3734844560-learn-about-the-fi (updated 2026-02-03) and https://guide.fireflies.ai/articles/9606045468-fireflies-billing-terms (one-time credits 20 / 20 / 30 / 50 by plan, updated 2026-10-16). Third-party for storage: https://www.castmagic.io/blog/fireflies-pricing. Some third-party sites describe credits as monthly, the official page says one-time. Checked 2026-11-21 |
| 3 | General AI chatbot, paste text and write your own prompt | Manual method | Flexible, handles any pasted text, nothing new to learn | You retype the prompt each time; output format varies; no history, quotas or one-click export | Varies by tool | Not researched (general knowledge). Add specific tools and prices yourself |
| 4 | [add more, for example Notion AI, Fathom, tl;dv] | | | | | Research with starter prompt A2 in `project.md` |

**3.2 Gap summary (hypothesis, needs validation)**
- The researched tools centre on capturing meetings and charge per seat or with caps. Someone who already has text may not need that.
- A general chatbot works but gives no consistent structure, history or usage control.
- Possible gap: paste-in text, a consistent structured digest, simple usage limits, no meeting bot. This is **not proven**; confirm with U-001.

**3.3 Decision: build, reuse, or extend?**
- Decision: **BUILD NEW as a learning MVP.**
- Reason: the goal is to learn to build and ship a small AI SaaS end to end. Honest caution: the difference from existing tools is small and unvalidated. If the aim were purely to get meeting notes for yourself, ADOPT (use an existing tool) would be cheaper. Revisit this decision after U-001.

---

## 4. Proposed Solution

**4.1 Solution concept**
NoteDigest is a small web app. A user signs up, pastes text or uploads a .txt or .md file, chooses a template (meeting notes, email thread, article), and clicks Generate. The server checks the user's login and monthly quota, validates the input size, and sends the text to an LLM provider with a fixed prompt that asks for JSON. The server validates the JSON against a schema, stores it, and the user sees a clean digest with a summary, decisions, action items (task, owner, due date if stated, short evidence quote) and open questions. The user can copy it as Markdown, review history, and delete any digest or their whole account.

**4.2 How it solves the problem (mapping)**
| Problem point (Section 2) | How this solution fixes it | Related feature IDs |
|---|---|---|
| Re-reading long text by hand | One-click structured digest | F-002, F-003 |
| Action items missed | Dedicated action-item list with owner, due date and evidence quote | F-003 |
| Inconsistent notes | Fixed output schema and templates | F-003, F-004 |
| Paying for features not needed | Usage-based free quota, no per-seat plan, no meeting bot | F-008 |
| Lost or scattered notes | History and export | F-005, F-007 |
| Privacy worry about pasted text | Delete digest and delete account | F-006 |

**4.3 Upgrade over existing solutions**
| Gap found (Section 3) | Our improvement | Why it is better (hypothesis) |
|---|---|---|
| Tools centred on recording | Text-in only | Simpler for people who already have the text |
| Per-seat or credit pricing | Simple monthly quota per user | Easier to understand for light users |
| Manual chatbot has no structure | Fixed schema, templates, history, export | Consistent and reusable output |

**4.4 Value proposition**
For students and freelancers who already have meeting or email text, NoteDigest is a simple web app that turns it into decisions and action items in seconds, unlike meeting-bot tools that need recordings, seats or credits.

---

## 5. Functionalities

**5.1 Functional requirements**
| ID | Feature | User story | Priority | Acceptance criteria | Problem link | Status |
|---|---|---|---|---|---|---|
| F-001 | Sign up, log in, log out | As a visitor I want an account so that my digests are private | MUST | Valid email and password creates an account; wrong password is rejected; logged-out users are redirected from private pages; one user cannot read another user's data | Privacy | PLANNED |
| F-002 | Submit text | As a user I want to paste text or upload .txt/.md so that I can get a digest | MUST | Empty input rejected with a clear message; input over 20,000 characters rejected before any LLM call; only .txt/.md accepted; file over 200 KB rejected | Re-reading | PLANNED |
| F-003 | Generate structured digest | As a user I want a summary, decisions, action items and open questions so that I do not re-read | MUST | Output validates against the schema; fields are empty arrays or null when the text has no such content; action items include an evidence quote of at most 25 words or null; result shown within 30 s for a 10,000-character input in 8 of 10 test runs | Re-reading, missed items | PLANNED |
| F-004 | Choose template | As a user I want meeting, email or article templates so that output fits the text | SHOULD | Three templates exist; selected template changes the prompt; invalid template rejected | Inconsistent notes | PLANNED |
| F-005 | History | As a user I want to list and open past digests so that I can find them again | MUST | List shows only my digests, newest first; opening one shows the full digest; another user's ID returns not found | Lost notes | PLANNED |
| F-006 | Delete digest and delete account | As a user I want to remove my data so that I control it | MUST | Delete removes the digest and its input; account deletion removes all my rows and my login; both confirmed by a second click | Privacy | PLANNED |
| F-007 | Copy or download as Markdown | As a user I want to export a digest so that I can paste it elsewhere | SHOULD | Button copies Markdown containing all fields; download gives a .md file | Lost notes | PLANNED |
| F-008 | Monthly quota | As the owner I want a limit per user so that cost stays under control | MUST | Quota (default 20 digests per month, editable constant) enforced on the server; the 21st request is rejected with a clear message and no LLM call; usage page shows used and remaining | Cost, pricing | PLANNED |
| F-009 | Loading, errors, retry | As a user I want clear feedback so that I know what happened | MUST | Loading state while generating; provider error or timeout shows a friendly message and does not consume quota; retry works | Usability | PLANNED |
| F-010 | Rate limiting | As the owner I want abuse protection so that the app stays available | SHOULD | More than 10 requests per minute per user is rejected with a 429 response | Cost, security | PLANNED |
| F-011 | Paid plans with test payments | As the owner I want to test payments so that I learn billing | COULD | Only after MVP; test mode only | Pricing | PLANNED |

**5.2 Non-functional requirements**
| Area | Requirement (measurable) |
|---|---|
| Performance | Digest within 30 s for up to 20,000 characters (target, measure it); pages load under 2 s on a normal connection |
| Security | API key only on the server; every API route checks login; no secrets in the repo; dependency audit has no known high or critical issues at release |
| Reliability | Provider failure never crashes the app and never uses quota |
| Usability / accessibility | Keyboard usable; form labels; readable contrast; loading and error messages announced |
| Compatibility | Latest two versions of Chrome, Firefox, Edge; mobile width 360 px works |
| Data / privacy | Only email, input text and digests stored; delete works; no real personal data in tests |

**5.3 Out of scope (do NOT build)**
- Meeting bots, audio or video upload, speech-to-text
- Team workspaces, sharing links, comments
- Integrations (Slack, Google, Notion, calendars)
- Mobile apps, browser extensions
- Fine-tuning or training any model
- Real payments in the MVP (F-011 is test mode only, later)
- Admin dashboard (use the database console for now)

**5.4 Main user workflows**
1. Visitor opens the landing page, clicks Sign up, creates an account, lands on the dashboard.
2. User pastes text, picks a template, clicks Generate, sees a loading state, then the digest.
3. User clicks Copy Markdown and pastes it into their own notes.
4. User opens History, picks an older digest, or deletes it.
5. User opens Settings, checks usage, or deletes the account.

---

## 6. Users and Roles
| Role | Description | Can do | Cannot do |
|---|---|---|---|
| Visitor | Not logged in | See landing page, sign up, log in | Use any digest feature |
| User | Logged in | Create, view, export and delete own digests; see own usage; delete own account | See other users' data; exceed quota |
| Owner | You | Run the database console and logs | (not an in-app role in the MVP) |

---

## 7. Existing Project X-Ray

Not applicable (new build). Fill this section only when upgrading an existing codebase.

---

## 8. Technology Stack and Architecture

**8.1 Stack (all PROPOSED; none approved yet)**
| Layer | Choice | Version | Status | Reason / alternatives considered |
|---|---|---|---|---|
| Language | TypeScript | verify latest stable at WU-0001 | PROPOSED | Type safety for API contracts. Alternative: Python (FastAPI) |
| Framework | Next.js (App Router) | verify at WU-0001 | PROPOSED | One codebase for UI and API routes. Alternatives: React + Express; Django |
| Database + auth | Hosted Postgres with built-in auth (for example Supabase) | verify at WU-0003 | PROPOSED | Row-level security, free tier. Alternatives: Firebase; self-managed Postgres plus Auth.js. Verify free-tier limits (U-004) |
| LLM provider | One hosted LLM API, called from the server only | model name and price: verify on the provider's official docs (U-003) | UNDECIDED | Compare at least two providers on price, quality on your evaluation set, data-retention terms |
| Validation | Zod (or equivalent schema library) | verify | PROPOSED | Validate input and LLM output |
| Hosting | A managed platform with a free tier (for example Vercel) | verify limits | PROPOSED | Simple deploy from Git. Alternative: a small VPS |
| Testing | Vitest (unit, integration), Playwright (end to end) | verify | PROPOSED | Common for this stack |

*Rule: do not treat a PROPOSED choice as approved. At WU-0001 look up current versions on official sites and write them in this table with the date checked.*

**8.2 Architecture overview**
```
Browser (Next.js UI)
   |  HTTPS
Next.js server routes  /api/*
   |-- 1. check login
   |-- 2. validate input (type, size)
   |-- 3. check rate limit and monthly quota
   |-- 4. call LLM provider (server-side key)
   |-- 5. validate JSON output against schema
   |-- 6. save digest + update usage
Postgres (users, digests, usage) with row-level security
```

**8.3 Folder structure**
```
notedigest/
├── project.md
├── .env.example            (names of variables only, never real keys)
├── db/migrations/
├── src/
│   ├── app/
│   │   ├── page.tsx                 (landing)
│   │   ├── login/page.tsx
│   │   ├── dashboard/page.tsx       (new digest + history)
│   │   ├── digests/[id]/page.tsx
│   │   ├── settings/page.tsx
│   │   └── api/
│   │       ├── digests/route.ts            (POST create, GET list)
│   │       ├── digests/[id]/route.ts       (GET one, DELETE)
│   │       ├── usage/route.ts              (GET)
│   │       └── account/route.ts            (DELETE)
│   ├── lib/
│   │   ├── validation.ts   (input checks)
│   │   ├── schema.ts       (digest output schema)
│   │   ├── prompts.ts      (templates)
│   │   ├── llm.ts          (server-only provider client)
│   │   ├── quota.ts
│   │   ├── rateLimit.ts
│   │   └── db.ts
│   └── components/
└── tests/
    ├── unit/
    ├── integration/
    ├── e2e/
    └── fixtures/           (synthetic sample texts only)
```

**8.4 Data model**
| Entity | Key fields | Relationships |
|---|---|---|
| users | id, email, created_at (managed by the auth provider) | has many digests |
| digests | id, user_id, title, template, input_text, output_json, status (OK / FAILED), model, tokens_in, tokens_out, created_at | belongs to user; row-level rule: user_id = current user |
| usage | user_id, month (YYYY-MM), digests_count | one row per user per month |

**8.5 APIs**
| Name | Purpose | Input | Output | Auth |
|---|---|---|---|---|
| POST /api/digests | Create a digest | template, text | 201 with digest; 400 invalid; 401 not logged in; 402/429 quota or rate limit; 502 provider error | Required |
| GET /api/digests | List my digests | none | list (id, title, template, created_at) | Required |
| GET /api/digests/:id | One digest | id | digest or 404 | Required |
| DELETE /api/digests/:id | Delete one | id | 204 or 404 | Required |
| GET /api/usage | Show quota | none | used, limit, month | Required |
| DELETE /api/account | Delete everything | none | 204 | Required |

**8.6 LLM design**
- Output schema: `summary` (string, at most 150 words), `decisions` (array of strings), `action_items` (array of {task, owner or null, due or null, evidence_quote or null, at most 25 words}), `open_questions` (array of strings).
- The prompt tells the model to use only the supplied text, to return JSON only, to use null when unknown, and to treat the text as data, never as instructions.
- The server parses and validates the JSON. On failure it retries once, then returns an error and does not consume quota.
- Limits: max input 20,000 characters, max output tokens set in config, one request at a time per user.

---

## 9. Security, Privacy and Data Handling
- **Data classification:** CONFIDENTIAL (users paste private text).
- **Personal or sensitive data used:** email address, pasted text, generated digests. Tell users not to paste passwords, medical or financial identifiers.
- **Retention and deletion:** keep until the user deletes; account deletion removes everything (retention period is an open decision, U-005).
- **Secrets handling:** provider key and database service key only in server environment variables; `.env` is git-ignored; `.env.example` lists names only.
- **Authentication and access rules:** every API route checks the session; row-level security so a user can only read their own rows; test it with two accounts.
- **Prompt injection:** pasted text may contain instructions. The prompt treats it as data, output is schema-validated, and output is rendered as plain text (no HTML injection).
- **Known security risks:** key leak, cost abuse, cross-user data access, prompt injection, vulnerable dependencies.

---

## 10. Constraints
| Type | Constraint |
|---|---|
| Time / deadline | Example: 6 weeks part-time (replace with yours) |
| Budget | Infrastructure on free tiers; LLM API spend capped by you (set the number in U-003) |
| Hardware / platform | Any laptop that runs Node; deploy to a managed host |
| Rules (college, client, legal, licence) | Choose a licence for your code; follow the provider's terms of use; no real personal data in tests |
| Team skills / tools available | Solo; learning the stack as you go |

---

## 11. Decisions, Assumptions, Unknowns and Risks

**Approved decisions**
| ID | Decision | Date | Approved by |
|---|---|---|---|
| D-001 | None yet. Approve the Section 8 choices at the Phase 0 gate | | |

**Assumptions (not yet verified)**
| ID | Assumption | How to verify |
|---|---|---|
| A-001 | People with existing text want a paste-in tool | Interviews (U-001) |
| A-002 | 20 digests per month is a sensible free quota | Check provider cost per digest, then adjust |
| A-003 | 20,000 characters covers typical inputs | Test on your own non-sensitive samples |

**Unknowns (must be answered, owner assigned)**
| ID | Question | Needed before | Owner |
|---|---|---|---|
| U-001 | Do 5 target users confirm the problem and the paste-in workflow? | Phase 0 approval | You |
| U-002 | How long does the manual process take on 5 samples? | Phase 0 approval | You |
| U-003 | Which LLM provider and model, and what are the verified price and data-retention terms? What spending cap? | WU-0006 | You |
| U-004 | What are the current free-tier limits of the chosen database and host? | WU-0003 | You |
| U-005 | How long should input text be kept? | WU-0003 | You |

**Risks**
| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-001 | LLM invents action items or owners | Medium | High | Evidence quote field, null when unknown, "check against the original" notice, accuracy test on the evaluation set |
| R-002 | Cost runs away | Medium | High | Input cap, output token cap, per-user quota, rate limit, provider spending limit |
| R-003 | Cross-user data leak | Low | High | Row-level security, two-account test, API checks |
| R-004 | Provider outage or API change | Medium | Medium | Isolate in `llm.ts`; friendly errors; do not consume quota on failure |
| R-005 | Scope creep (bots, integrations, payments) | High | Medium | Out-of-scope list, Phase gates |
| R-006 | Problem not real or not different enough | Medium | Medium | U-001 before building; decide ADOPT if so |

---

## 12. Design Notes (UI / UX)
- **Screens:** Landing, Sign up / Log in, Dashboard (new digest form plus history list), Digest detail, Settings (usage, delete account).
- **Navigation flow:** Landing → Sign up → Dashboard → Digest detail; Settings from the top bar.
- **Style notes:** simple single-column layout, one accent colour, large readable text, results in clear sections with headings.
- **Accessibility:** labelled inputs, visible focus, sufficient contrast, status messages that screen readers announce, works with keyboard only.

---

## 13. Building Plan

**13.1 Phases**
| Phase | Goal | Main outputs | Gate |
|---|---|---|---|
| 0. Baseline | Finish this file and validate the problem | Sections 1–12 reviewed with Appendix B of `project.md`; U-001 to U-005 answered or accepted; stack choices approved | Approver signs off |
| 1. Setup | Skeleton and tooling | WU-0001 to WU-0003 | App runs, tests run, database tables exist |
| 2. Core build | MUST features | WU-0004 to WU-0012 | Every MUST feature meets its acceptance criteria |
| 3. Hardening | SHOULD features, security, tests | WU-0013, WU-0014 | Tests PASS or are explained; security checklist done |
| 4. Release | Staging or public deploy | WU-0015 | Smoke test passes; approver authorizes release |
| 5. Maintain | Updates | Re-verify prices, versions and Section 3 monthly | Ongoing |

**13.2 Work units (one at a time)**
| ID | Objective | Feature | Depends on | Allowed files | Acceptance criteria | Status |
|---|---|---|---|---|---|---|
| WU-0001 | Create repo, framework skeleton, lint, test runner, git-ignore | none | Phase 0 | project root config files, `src/app/page.tsx`, `tests/` | App starts locally; one sample test passes; `.env` ignored by git; versions recorded in Section 8.1 | PLANNED |
| WU-0002 | Environment config and secret handling | none | WU-0001 | `.env.example`, `src/lib/config.ts` | App reads settings from environment; missing required variable fails fast with a clear message; no real secret in the repo | PLANNED |
| WU-0003 | Database schema and row-level rules | F-001, F-005 | WU-0002, U-004, U-005 | `db/migrations/*`, `src/lib/db.ts` | Tables created; migration can be applied to an empty database; two-user test shows user A cannot read user B rows | PLANNED |
| WU-0004 | Authentication | F-001 | WU-0003 | `src/app/login/*`, auth helpers | Sign up, log in, log out work; private pages redirect when logged out | PLANNED |
| WU-0005 | Input validation module | F-002 | WU-0001 | `src/lib/validation.ts`, `tests/unit/validation.test.ts` | Unit tests cover empty, too long, wrong file type, too large file, valid input; all PASS | PLANNED |
| WU-0006 | LLM service and output schema | F-003, F-004 | WU-0002, U-003 | `src/lib/llm.ts`, `schema.ts`, `prompts.ts`, tests | With a mocked provider, valid JSON is accepted, invalid JSON triggers one retry then an error; real key never reaches client code (check build output) | PLANNED |
| WU-0007 | Create-digest endpoint | F-002, F-003, F-009 | WU-0004, WU-0005, WU-0006 | `src/app/api/digests/route.ts` | 401 when logged out; 400 on bad input; 201 on success with stored digest; provider error returns 502 and stores no OK digest | PLANNED |
| WU-0008 | Quota and usage | F-008 | WU-0007 | `src/lib/quota.ts`, `src/app/api/usage/route.ts`, tests | The request after the limit is rejected and makes no LLM call; failed generation does not count; month rollover tested | PLANNED |
| WU-0009 | List, read, delete endpoints | F-005, F-006 | WU-0007 | `src/app/api/digests/[id]/route.ts` and list route | Only own digests visible; delete removes row; other user's ID returns 404 | PLANNED |
| WU-0010 | Dashboard UI: form, loading, errors | F-002, F-003, F-009 | WU-0007 | `src/app/dashboard/*`, `src/components/*` | Generate works end to end in the browser; loading and error states visible; keyboard usable | PLANNED |
| WU-0011 | History and detail UI, export | F-005, F-007 | WU-0009, WU-0010 | `src/app/digests/[id]/*`, components | History lists digests; detail shows all fields; Copy Markdown and download work | PLANNED |
| WU-0012 | Settings: usage and account deletion | F-006, F-008 | WU-0008, WU-0009 | `src/app/settings/*`, `src/app/api/account/route.ts` | Usage shown; account deletion removes all rows and login after confirmation | PLANNED |
| WU-0013 | Rate limiting and security hardening | F-010 | WU-0007 | `src/lib/rateLimit.ts`, headers config | 11th request within a minute gets 429; dependency audit run and result recorded; output rendered as text only | PLANNED |
| WU-0014 | Full tests and evaluation run | all | WU-0001–WU-0013 | `tests/*` | Unit, integration, end-to-end suites run with real output saved; evaluation set scored; traceability table filled | PLANNED |
| WU-0015 | Deploy and smoke test | all | WU-0014, approval | hosting config | Deployed version passes the smoke list in Section 15; rollback tested once | PLANNED |

**13.3 Milestones (example, adjust to your time)**
| Milestone | Target | Includes |
|---|---|---|
| M0 Baseline approved | Week 1 | Phase 0 |
| M1 Skeleton and database | Week 2 | WU-0001 to WU-0003 |
| M2 Digest works end to end | Week 4 | WU-0004 to WU-0010 |
| M3 Complete MVP | Week 5 | WU-0011 to WU-0014 |
| M4 Released | Week 6 | WU-0015 |

**13.4 Git and backup rules**
- One branch per work unit, small commits with clear messages, merge only after the acceptance criteria pass.
- Never force-push; never commit `.env` or keys.
- Make a commit or tag before risky changes such as database migrations.

---

## 14. Testing and Verification
| Level | What is tested | Tool / command | Required? |
|---|---|---|---|
| Unit | validation, schema parsing, quota logic | `npm test` (typical; confirm in WU-0001) | Yes |
| Integration | API routes with a mocked LLM and a test database | test runner | Yes |
| End to end | sign up → generate → view → delete | Playwright | Yes |
| Security | two-account access test, key not in client bundle, dependency audit | manual plus audit command | Yes |
| Performance | time for a 10,000-character input, 10 runs | script or manual timing | Yes |
| Accuracy | 10 synthetic samples scored with a rubric | manual | Yes |

**Evaluation set (create in WU-0014):** 10 synthetic texts only (4 meeting transcripts, 3 email threads, 3 article or lecture notes). Each has a hand-written list of the real decisions and action items. Score: correct, missing, invented. No real personal data.

**Traceability**
| Problem point | Feature | Work unit | Test | Result |
|---|---|---|---|---|
| Re-reading long text | F-002, F-003 | WU-0005, WU-0006, WU-0007 | unit + integration + timing | NOT RUN |
| Action items missed | F-003 | WU-0006 | evaluation set | NOT RUN |
| Cost control | F-008, F-010 | WU-0008, WU-0013 | quota and rate-limit tests | NOT RUN |
| Privacy | F-001, F-006 | WU-0003, WU-0004, WU-0009, WU-0012 | two-account test, deletion test | NOT RUN |
| Lost notes | F-005, F-007 | WU-0009, WU-0011 | e2e | NOT RUN |

**Definition of done (any task):** code written → tests run with real output shown → acceptance criteria checked → Section 17 updated → no unrelated changes.

---

## 15. Release and Maintenance
- **Release target:** staging first; public only if you decide to (add privacy notice and terms first).
- **Build / package command:** the framework's production build command (record in WU-0001).
- **Rollback plan:** redeploy the previous version; migrations must be reversible or backed up first.
- **Smoke test list:** sign up; generate a digest; open history; delete the digest; check usage; log out.
- **Known limitations to disclose:** LLM output can be wrong; only text input; English-first until tested otherwise.
- **Maintenance routine:** monthly, re-verify provider price, model availability, hosting limits and Section 3 competitors (see Appendix C of `project.md`).

---

## 16. AI Tool Permissions
| Item | Setting |
|---|---|
| Tools the AI may use | file read/write in the project, run tests and lint, git (local commits on a work-unit branch) |
| Files / folders the AI may edit | `src/`, `tests/`, `db/migrations/`, `project.md` Sections 8.1, 13.2, 14, 17, 18 |
| Files / folders read-only | the rest of `project.md`, `.github/` unless the work unit says so |
| Never read or edit | `.env`, `.env.*` (except `.env.example`) |
| Prohibited actions | deploy to production without approval, expose or log secrets, delete data, force-push, call the real LLM API in automated tests |
| Needs my approval first | new dependencies, schema changes, scope changes, push or merge, choosing the LLM provider, raising any spending cap |

---

## 17. Status and Handoff
| Field | Value |
|---|---|
| Current phase | 0. Baseline (plan drafted, nothing built) |
| Last completed work unit | none |
| Evidence | existing-solutions research done 2026-11-21 (sources in Section 3) |
| What changed (files) | none |
| Blocked items | Phase 0 gate needs U-001 to U-005 |
| Open questions | U-001 to U-005 |
| Next recommended action | Run Appendix B of `project.md`, answer the unknowns, approve the baseline, then start WU-0001 |
| Updated on | 2026-11-21 |

---

## 18. Change Log
| Date | Change | Approved by |
|---|---|---|
| 2026-11-21 | Example plan created for a simple AI SaaS | n/a (example) |

---

## Appendix — Your build checklist for this example

1. Copy this file to a new project folder and rename it `project.md`. Replace the example name, owner and dates.
2. Do U-001 and U-002 (talk to five people, time the manual process). If the problem is not real, stop or choose ADOPT in Section 3.3.
3. Pick an LLM provider by comparing at least two on price, quality on your own test texts and data terms (U-003). Write the verified price and the date in Section 8.1.
4. Run Appendix B (completeness check) from `project.md`. Fix gaps, then approve the baseline in Section 11 and Section 18.
5. Open Claude or ChatGPT, paste the whole file, and send starter prompt A1. Read the answer. Correct anything wrong in the file.
6. Build one work unit at a time with prompt A4. Example: "Read project.md. Do work unit WU-0001 only. Follow Section 0 and Section 16. Show files changed and real command output. Update Section 17 and stop."
7. After each unit, check the acceptance criteria yourself, run the tests, and only then mark the unit DONE with evidence in Section 17.
8. Use Appendix C (check and update routine) weekly, and before each phase gate.
9. When every MUST feature passes, run prompt A6 (pre-release review), then do WU-0015.
