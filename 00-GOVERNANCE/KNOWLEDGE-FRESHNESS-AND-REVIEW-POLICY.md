# Knowledge Freshness and Review Policy

Knowledge records carry source, publication/version date when known, retrieval date, verification date, confidence, status and next review date. Version-sensitive topics (framework releases, APIs, pricing, security advisories, cloud limits and tool capabilities) must be checked against current authoritative sources before a consequential decision.

Suggested review cadence: critical security/tool compatibility monthly or on major release; fast-moving platform/API details quarterly or before use; stable principles annually. These are default review targets, not proof of automatic monitoring.

Statuses: CURRENT, REVIEW_DUE, STALE, SUPERSEDED, DISPUTED, UNVERIFIED. Stale knowledge may be retained for history but must not be presented as current guidance. Record changed facts and affected downstream decisions.

## Additional detail (carried from the starter seed)
## Scope
Applies to AI models, IDEs, frameworks, SDKs, APIs, libraries, cloud services, pricing, standards, security guidance and any knowledge likely to change.

## Required metadata
Record source URL/reference, source owner, product/standard, version/release, publication/update date if known, verified date, verification method, support status, confidence, limitations, next review and supersession links.

## Source hierarchy
1. Official documentation, release notes, advisories and API references.
2. Standards bodies and project maintainers.
3. Official vendor engineering/security sources.
4. Reputable independent research.
5. Community discussions as supporting signals.
6. Model knowledge as preliminary or stable background only.

## Review defaults
- Highly volatile: verify at each selection/use and before implementation.
- Fast changing: project start and before major upgrade/release.
- Moderate: project start and release/security review.
- Slow changing: scheduled review or when challenged.
- Historical: review when new evidence challenges it.

These are defaults, not freshness guarantees. Mark stale, superseded, unverified or conflicted knowledge explicitly. Never invent dates or versions.
