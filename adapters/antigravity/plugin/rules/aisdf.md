---
trigger: always_on
---

# AISDF governance rules

- Preserve user intent, source-of-truth, scope lock, and Change Only Law.
- No application source changes before explicit human approval of the specification and exact file allowlist.
- Use `.aisdf/` for durable artifacts; validate with the AISDF runtime.
- Independent review requires fresh context and verifiable session/worktree evidence. Otherwise label it `NON_INDEPENDENT` or `BLOCKED`.
- Preserve dissent; findings require evidence-based disposition and re-review.
- Use least privilege and request approval for risky or irreversible actions.
- Distinguish structural validation, tests, independent review, host certification, and production verification.
