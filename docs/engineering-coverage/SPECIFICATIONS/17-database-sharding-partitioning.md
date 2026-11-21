# 17 — Database Sharding & Partitioning

**Engineering area:** Data engineering  
**Maturity:** SPECIFIED — implementation and production verification are project-specific.

## Purpose
Divides data to manage scale, locality and maintenance.

## Core mechanisms
Range/hash/list partitioning, shard keys, routing, rebalancing and hot partitions.

## Design and decision criteria
Choose stable shard key; plan cross-shard queries, resharding, tenant isolation and migrations.

## Required inputs
- Product requirements, traffic/workload assumptions and critical user journeys.
- Existing architecture, deployment topology, data classification and trust boundaries.
- Availability, latency, throughput, consistency, recovery and cost objectives.
- Team capability, operational ownership, vendor constraints and lifecycle requirements.

## Required outputs
- Architecture decision record with alternatives and rationale.
- Component/data-flow diagram and trust-boundary description.
- Selected configuration and version/compatibility evidence, if applicable.
- Threat/failure analysis, operational runbook and rollback/recovery plan.
- Test evidence, telemetry requirements, ownership and residual risks.

## Security and failure modes
Hot shards, uneven distribution, cross-shard transaction complexity and data leakage.

Apply least privilege, secure defaults, data minimization, tenant isolation, safe failure behavior and explicit authorization. Treat external configuration and discovered metadata as untrusted until validated.

## Observability requirements
Shard skew, query latency, rebalance duration, storage and cross-shard traffic.

Every production deployment must define service-level signals, dashboards or equivalent inspection, alert ownership, and diagnostic correlation appropriate to risk. Avoid sensitive payload logging and unbounded metric labels.

## Implementation workflow
1. Confirm the requirement and prove that this capability is needed; record `NOT_APPLICABLE` with rationale when it is not.
2. Inspect current architecture and constraints; do not introduce distributed complexity by default.
3. Compare at least one viable alternative for material decisions; record costs and operational burden.
4. Define security, failure, capacity, compatibility and recovery behavior before implementation.
5. Implement the smallest reversible change behind approved scope and permissions.
6. Validate locally, in CI, and in a production-like environment as appropriate.
7. Record evidence, limitations, owner, rollback trigger and follow-up actions.

## Verification strategy
Skew, rebalance, shard outage, key migration, tenant isolation and query plan tests.

Use the companion test plan `../TEST-PLANS/17-database-sharding-partitioning-tests.md`. Tests must include positive, negative, boundary, failure/recovery and security cases as relevant.

## Acceptance criteria
- Requirement and applicability decision are traceable to an approved project baseline.
- Architecture, alternatives, assumptions and operational ownership are documented.
- Security and failure behavior are explicitly designed.
- Tests pass with reproducible evidence; unrun checks are marked `NOT_RUN`, not implied complete.
- Rollback/recovery and monitoring are ready before production release.

## Related AISDF capabilities
Use relevant capabilities from `engines/` rather than creating duplicate engines. Likely touchpoints include E-023 through E-030 (technology and architecture), E-035/E-036 (planning and orchestration), E-041/E-042 (change and approval), E-043 through E-048 (quality/security/verification), and E-051 through E-055 (delivery/operations). Select only applicable dependencies.

## Status vocabulary
`NOT_ASSESSED` · `SPECIFIED` · `DESIGNED` · `IMPLEMENTED` · `TESTED` · `INDEPENDENTLY_VERIFIED` · `PRODUCTION_VERIFIED` · `NOT_APPLICABLE` · `BLOCKED`. A higher state requires evidence from every preceding gate.
