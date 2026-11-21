# WF-005 — Layered Security Assurance

**Status:** Proposed workflow. Requires project-owner authorization and maintainer approval before becoming a mandatory release gate.

## Objective
Assess an application using a risk-based combination of source, dependency, secret, configuration, artifact, dynamic and AI-specific security checks.

## Inputs
- Approved project baseline and repository commit SHA
- Asset inventory and architecture
- Language/package-manager/container/IaC inventory
- Threat model and data classification
- Written scan authorization and target allowlist
- Tool versions, editions, credentials and execution environment
- Exclusions, rate limits, scan window and emergency stop contact

## Phase 0 — Authorization and safety preflight
1. Confirm ownership or written authorization.
2. Define exact repository, branch, commit, endpoints, accounts and cloud resources in scope.
3. Exclude production and third-party systems unless separately authorized.
4. Define sandbox, network policy, resource ceilings and output directory.
5. Confirm no real customer data or production credentials are present in test fixtures.
6. Stop if scope or permission is ambiguous.

**Gate:** `AUTHORIZED` or `BLOCKED`. No scanning before authorization.

## Phase 1 — Baseline inventory
Record:
- Languages and frameworks
- Direct and transitive dependencies
- Lockfiles and SBOM availability
- Container images and base images
- IaC and cloud configuration
- Secret locations and Git history scope
- Agent skills, MCP servers, plugins and CI actions
- AI model/application endpoints
- Uploadable or externally supplied artifacts

## Phase 2 — Low-risk repository checks
Select relevant tools:
- Semgrep for static rules and code patterns.
- Trivy filesystem/repository scans for dependency vulnerabilities, secrets, misconfiguration and licenses.
- TruffleHog for secrets in authorized source/history.
- SkillSpector for agent skill bundles before installation.
- Cloudflare Security Audit Skill or Codex Security for deeper review when execution and access prerequisites are satisfied.

Record exact command/configuration, tool version, commit SHA, exit code, artifacts and exclusions. Never paste raw secrets into the report.

## Phase 3 — Build and artifact checks
- Scan container images and deployment configuration with Trivy.
- Use ClamAV for applicable untrusted files or release artifacts in an isolated environment.
- Generate/inspect SBOM where appropriate.
- Evaluate BLA only when protecting owned release artifacts against reverse engineering is a stated requirement; run functional equivalence and performance tests after hardening.

## Phase 4 — Authorized dynamic checks
- Run Nuclei against explicitly allowlisted staging URLs/IPs with reviewed templates and safe rate limits.
- Run Strix against the owned test application in an isolated environment.
- Do not use broad internet targets, wildcard domains, third-party services, or production by default.
- Stop on unexpected instability, data modification, service degradation or scope ambiguity.

## Phase 5 — AI application red team
If the product contains LLM/agent functionality:
- Use PyRIT against dedicated test endpoints and synthetic data.
- Test prompt injection, data leakage, unsafe tool use, excessive agency, refusal/safety boundaries and output handling as relevant.
- Apply bounded requests, spend limits, rate limits and stop conditions.
- Treat outputs as potentially sensitive; redact before sharing.

## Phase 6 — Independent triage
For every candidate:
1. Deduplicate by root cause and affected component.
2. Verify source location and reachable data/control flow.
3. Attempt to disprove the candidate independently.
4. Separate severity from confidence.
5. Classify as `confirmed`, `needs_validation`, `false_positive`, or `accepted_risk`.
6. Assign remediation owner and due date.
7. Record evidence without exposing credentials.

## Phase 7 — Remediation and retest
- Fix one approved work unit at a time.
- Review the diff and threat impact.
- Run targeted regression tests and the relevant scanner again.
- Record before/after evidence and commit SHA.
- Do not auto-merge or auto-deploy scanner-generated patches.

## Phase 8 — Release decision
Release gate requires:
- Scope and authorization record
- Tool/version/configuration inventory
- Coverage and exclusions
- Findings and dispositions
- Remediation/retest evidence
- Unresolved risks and waivers
- Human security/release approval

Possible outcomes: `PASS_WITHIN_DECLARED_SCOPE`, `FAIL`, `BLOCKED`, `INCOMPLETE`, `NOT_APPLICABLE`.

A zero-finding report is not proof of security. State what was not tested.
