# AISDF Master Engineering Coverage Catalogue

**Coverage scope:** 51 engineering topics, with a specification and companion verification plan for each. These are knowledge/design contracts, not prebuilt implementations.

| ID | Topic | Area | Specification | Test plan |
|---|---|---|---|---|
| 01 | Rate Limiting | Traffic management | [Spec](SPECIFICATIONS/01-rate-limiting.md) | [Tests](TEST-PLANS/01-rate-limiting-tests.md) |
| 02 | Caching | Performance | [Spec](SPECIFICATIONS/02-caching.md) | [Tests](TEST-PLANS/02-caching-tests.md) |
| 03 | Load Balancing | Traffic management | [Spec](SPECIFICATIONS/03-load-balancing.md) | [Tests](TEST-PLANS/03-load-balancing-tests.md) |
| 04 | Reverse Proxy | Network architecture | [Spec](SPECIFICATIONS/04-reverse-proxy.md) | [Tests](TEST-PLANS/04-reverse-proxy-tests.md) |
| 05 | API Gateway | API architecture | [Spec](SPECIFICATIONS/05-api-gateway.md) | [Tests](TEST-PLANS/05-api-gateway-tests.md) |
| 06 | CI/CD | Delivery engineering | [Spec](SPECIFICATIONS/06-ci-cd.md) | [Tests](TEST-PLANS/06-ci-cd-tests.md) |
| 07 | Docker | Containerization | [Spec](SPECIFICATIONS/07-docker.md) | [Tests](TEST-PLANS/07-docker-tests.md) |
| 08 | Kubernetes | Orchestration | [Spec](SPECIFICATIONS/08-kubernetes.md) | [Tests](TEST-PLANS/08-kubernetes-tests.md) |
| 09 | Service Discovery | Distributed systems | [Spec](SPECIFICATIONS/09-service-discovery.md) | [Tests](TEST-PLANS/09-service-discovery-tests.md) |
| 10 | Circuit Breaker | Resilience | [Spec](SPECIFICATIONS/10-circuit-breaker.md) | [Tests](TEST-PLANS/10-circuit-breaker-tests.md) |
| 11 | Authentication & Authorization | Security | [Spec](SPECIFICATIONS/11-authentication-authorization.md) | [Tests](TEST-PLANS/11-authentication-authorization-tests.md) |
| 12 | DNS & CDN | Networking | [Spec](SPECIFICATIONS/12-dns-cdn.md) | [Tests](TEST-PLANS/12-dns-cdn-tests.md) |
| 13 | TLS/HTTPS & Certificate Management | Security | [Spec](SPECIFICATIONS/13-tls-https-certificates.md) | [Tests](TEST-PLANS/13-tls-https-certificates-tests.md) |
| 14 | Message Queues | Distributed systems | [Spec](SPECIFICATIONS/14-message-queues.md) | [Tests](TEST-PLANS/14-message-queues-tests.md) |
| 15 | Event-Driven Architecture | Application architecture | [Spec](SPECIFICATIONS/15-event-driven-architecture.md) | [Tests](TEST-PLANS/15-event-driven-architecture-tests.md) |
| 16 | Database Replication | Data engineering | [Spec](SPECIFICATIONS/16-database-replication.md) | [Tests](TEST-PLANS/16-database-replication-tests.md) |
| 17 | Database Sharding & Partitioning | Data engineering | [Spec](SPECIFICATIONS/17-database-sharding-partitioning.md) | [Tests](TEST-PLANS/17-database-sharding-partitioning-tests.md) |
| 18 | Database Connection Pooling | Data engineering | [Spec](SPECIFICATIONS/18-database-connection-pooling.md) | [Tests](TEST-PLANS/18-database-connection-pooling-tests.md) |
| 19 | Distributed Transactions | Distributed systems | [Spec](SPECIFICATIONS/19-distributed-transactions.md) | [Tests](TEST-PLANS/19-distributed-transactions-tests.md) |
| 20 | Idempotency | API & reliability | [Spec](SPECIFICATIONS/20-idempotency.md) | [Tests](TEST-PLANS/20-idempotency-tests.md) |
| 21 | Timeouts, Retries & Backoff | Reliability | [Spec](SPECIFICATIONS/21-timeouts-retries-backoff.md) | [Tests](TEST-PLANS/21-timeouts-retries-backoff-tests.md) |
| 22 | Bulkheads & Backpressure | Reliability | [Spec](SPECIFICATIONS/22-bulkheads-backpressure.md) | [Tests](TEST-PLANS/22-bulkheads-backpressure-tests.md) |
| 23 | Concurrency Control | Application architecture | [Spec](SPECIFICATIONS/23-concurrency-control.md) | [Tests](TEST-PLANS/23-concurrency-control-tests.md) |
| 24 | Distributed Caching | Performance | [Spec](SPECIFICATIONS/24-distributed-caching.md) | [Tests](TEST-PLANS/24-distributed-caching-tests.md) |
| 25 | Observability | Operations | [Spec](SPECIFICATIONS/25-observability.md) | [Tests](TEST-PLANS/25-observability-tests.md) |
| 26 | Centralized Logging | Operations | [Spec](SPECIFICATIONS/26-centralized-logging.md) | [Tests](TEST-PLANS/26-centralized-logging-tests.md) |
| 27 | Metrics & Monitoring | Operations | [Spec](SPECIFICATIONS/27-metrics-monitoring.md) | [Tests](TEST-PLANS/27-metrics-monitoring-tests.md) |
| 28 | Distributed Tracing | Operations | [Spec](SPECIFICATIONS/28-distributed-tracing.md) | [Tests](TEST-PLANS/28-distributed-tracing-tests.md) |
| 29 | Alerting & Incident Management | Operations | [Spec](SPECIFICATIONS/29-alerting-incident-management.md) | [Tests](TEST-PLANS/29-alerting-incident-management-tests.md) |
| 30 | SLI, SLO & SLA | Reliability | [Spec](SPECIFICATIONS/30-sli-slo-sla.md) | [Tests](TEST-PLANS/30-sli-slo-sla-tests.md) |
| 31 | Backup & Disaster Recovery | Operations | [Spec](SPECIFICATIONS/31-backup-disaster-recovery.md) | [Tests](TEST-PLANS/31-backup-disaster-recovery-tests.md) |
| 32 | Infrastructure as Code | Platform engineering | [Spec](SPECIFICATIONS/32-infrastructure-as-code.md) | [Tests](TEST-PLANS/32-infrastructure-as-code-tests.md) |
| 33 | Configuration Management | Platform engineering | [Spec](SPECIFICATIONS/33-configuration-management.md) | [Tests](TEST-PLANS/33-configuration-management-tests.md) |
| 34 | Secrets Management | Security | [Spec](SPECIFICATIONS/34-secrets-management.md) | [Tests](TEST-PLANS/34-secrets-management-tests.md) |
| 35 | Blue-Green & Canary Deployment | Delivery engineering | [Spec](SPECIFICATIONS/35-deployment-strategies.md) | [Tests](TEST-PLANS/35-deployment-strategies-tests.md) |
| 36 | Horizontal & Vertical Scaling | Performance | [Spec](SPECIFICATIONS/36-scaling-strategies.md) | [Tests](TEST-PLANS/36-scaling-strategies-tests.md) |
| 37 | Monolith, Modular Monolith & Microservices | Application architecture | [Spec](SPECIFICATIONS/37-architecture-styles.md) | [Tests](TEST-PLANS/37-architecture-styles-tests.md) |
| 38 | Domain-Driven Design | Application architecture | [Spec](SPECIFICATIONS/38-domain-driven-design.md) | [Tests](TEST-PLANS/38-domain-driven-design-tests.md) |
| 39 | Clean Architecture | Application architecture | [Spec](SPECIFICATIONS/39-clean-architecture.md) | [Tests](TEST-PLANS/39-clean-architecture-tests.md) |
| 40 | CQRS | Data architecture | [Spec](SPECIFICATIONS/40-cqrs.md) | [Tests](TEST-PLANS/40-cqrs-tests.md) |
| 41 | Event Sourcing | Data architecture | [Spec](SPECIFICATIONS/41-event-sourcing.md) | [Tests](TEST-PLANS/41-event-sourcing-tests.md) |
| 42 | API Versioning | API engineering | [Spec](SPECIFICATIONS/42-api-versioning.md) | [Tests](TEST-PLANS/42-api-versioning-tests.md) |
| 43 | WebSockets & Real-Time Communication | API engineering | [Spec](SPECIFICATIONS/43-realtime-communication.md) | [Tests](TEST-PLANS/43-realtime-communication-tests.md) |
| 44 | REST & GraphQL API Design | API engineering | [Spec](SPECIFICATIONS/44-api-paradigms.md) | [Tests](TEST-PLANS/44-api-paradigms-tests.md) |
| 45 | Multi-Tenant Architecture | Application architecture | [Spec](SPECIFICATIONS/45-multi-tenancy.md) | [Tests](TEST-PLANS/45-multi-tenancy-tests.md) |
| 46 | Data Consistency Models | Distributed systems | [Spec](SPECIFICATIONS/46-consistency-models.md) | [Tests](TEST-PLANS/46-consistency-models-tests.md) |
| 47 | Schema Evolution & Database Migrations | Data engineering | [Spec](SPECIFICATIONS/47-schema-evolution-migrations.md) | [Tests](TEST-PLANS/47-schema-evolution-migrations-tests.md) |
| 48 | API Security & Abuse Prevention | Security | [Spec](SPECIFICATIONS/48-api-security.md) | [Tests](TEST-PLANS/48-api-security-tests.md) |

| 49 | Loop Engineering | Agent control loops & feedback systems | [Spec](SPECIFICATIONS/49-loop-engineering.md) | [Tests](TEST-PLANS/49-loop-engineering-tests.md) |
| 50 | Harness Engineering | AI execution environments & agent systems | [Spec](SPECIFICATIONS/50-harness-engineering.md) | [Tests](TEST-PLANS/50-harness-engineering-tests.md) |
| 51 | Graph Engineering | Graph data, knowledge graphs & graph computation | [Spec](SPECIFICATIONS/51-graph-engineering.md) | [Tests](TEST-PLANS/51-graph-engineering-tests.md) |

## Coverage rules

- Select capabilities from project needs; do not force every technology into every project.
- `NOT_APPLICABLE` requires a reason and approval where the capability is normally expected.
- Documentation presence is not implementation evidence.
- Production verification requires environment-specific evidence, monitoring, rollback, ownership and independent review.
- Review version-sensitive technical claims against authoritative documentation before project adoption.
