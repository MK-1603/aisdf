---
name: aisdf
description: Runs AISDF's gated spec-driven engineering lifecycle WF-007 through WF-012, including concept challenge, specification drafting, independent review, finding resolution, codebase context bootstrap, and specification drift checks.
---

# AISDF workflow skill for Google Antigravity

## Start-up
1. Read repository `AGENTS.md`/`GEMINI.md` and the AISDF governance documents.
2. Locate the AISDF runtime script. If installed at `.aisdf-tools/aisdf.py`, run `python .aisdf-tools/aisdf.py --help` first. Otherwise use the AISDF distribution's `runtime/tools/aisdf.py`.
3. Keep durable artifacts under `.aisdf/`. Never treat chat output as the sole record.
4. Execute only the requested workflow stage; preserve the stage gates WF-007 → WF-008 → WF-009 → WF-010 → human approval → implementation → WF-012.

## WF-007 — Concept challenge
Create a challenge artifact and examine user value, scope/YAGNI, reuse, architecture/operations, security/privacy/abuse, failure/recovery, alternatives, and kill criteria. Preserve dissent. Do not convert a challenge into approval.

## WF-008 — Specification drafting
Draft the complete AISDF design specification section by section. Ask for human approval at the required checkpoints. The implementation file allowlist must name exact paths and operations (create/modify/delete). Validate the artifact with the runtime.

## WF-009 — Independent design review
Use Antigravity custom subagents where available. Each reviewer must run in a genuinely separate context/worktree/session and receive only the approved spec plus explicitly permitted source references. Do not provide the originating conversation, prior agent conclusions, or hidden context. Assign separate lenses: simplicity/comprehension, architecture/reliability/security, and implementation readiness. Record reviewer identity, session/worktree evidence, inputs, outputs, and timestamp. If separation cannot be evidenced, mark `NON_INDEPENDENT` or `BLOCKED`; never simulate independence.

## WF-010 — Findings
Assign stable finding IDs, severity, owner, disposition, evidence, and re-review status. Deduplicate without erasing dissent. A finding is not resolved merely because an agent says so; require linked implementation/test/review evidence.

## WF-011 — Codebase context bootstrap
Run the deterministic inventory tool. Treat generated maps as snapshots with timestamps and hashes, not authoritative semantic documentation. Inspect important files and record exclusions/limits.

## WF-012 — Specification drift
After approved implementation, run the drift command and project tests. Compare actual changed paths to the approved allowlist. Stop and request approval for out-of-scope changes. Report missing tests and semantic drift risks separately; path comparison alone cannot detect semantic drift.

## Safety and authority
- Human approval is mandatory before application source edits and before widening the allowlist.
- Prefer Antigravity's isolated Git worktree mode for reviewer separation; verify the actual worktree/session rather than assuming isolation.
- Keep tool permissions least-privilege. Do not request broad filesystem or network access without a concrete need.
- Never expose secrets in artifacts, prompts, logs, screenshots, or reports.
- Do not run destructive commands, migrations, deployments, or external writes without explicit approval.
- Report specified, executed, tested, independently reviewed, and unverified work separately.
