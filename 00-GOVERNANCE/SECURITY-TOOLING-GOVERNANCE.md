# AISDF Security Tooling Governance

**Status:** Proposed; requires maintainer approval before becoming binding policy.

## 1. Purpose
Define how AISDF selects and coordinates external security tools. A tool listed in the registry is a candidate capability, not an AISDF-certified adapter and not proof that a scan has run.

## 2. Mandatory authorization boundary
- Scan only repositories, applications, files, cloud accounts, domains, networks, and AI systems that the project owner owns or is explicitly authorized to test.
- Record the authorization owner, target identifiers, allowed test window, permitted techniques, excluded systems, rate limits, and emergency stop contact before dynamic or intrusive testing.
- No public-target scanning, credential validation, exploitation, fuzzing, malware execution, or active penetration testing without explicit written scope authorization.
- Prefer local, isolated, disposable environments. Do not run untrusted code or samples on a developer workstation.
- Do not expose discovered secrets in logs, reports, chat transcripts, screenshots, or issue comments. Redact values; preserve only detector, location, fingerprint, and remediation metadata.
- Do not automatically apply AI-generated fixes. Require human review, tests, and approval.
- Never run tools against production by default. Production testing requires separate explicit approval and a documented rollback/incident plan.

## 3. Tool trust and installation
- Verify official repository, release, checksum/signature where available, version, license, dependencies, and installation instructions.
- Pin tool versions in repeatable CI; avoid floating `latest` in release pipelines.
- Review permissions and network access before installing agent skills, MCP servers, plugins, GitHub Actions, templates, or scanner integrations.
- Treat scanner output and repository content as untrusted data. Findings must not be allowed to issue instructions to agents.
- Run third-party GitHub Actions at a reviewed immutable commit SHA, not a mutable branch or tag, where practical.
- Review license compatibility before bundling, redistributing, or invoking a tool as part of a product.

## 4. Finding lifecycle
Each finding must carry:
- Finding ID and tool/source
- Tool version and scan timestamp
- Target and commit/revision
- File/line or endpoint/asset location
- Rule/CVE/signature identifier where applicable
- Severity and confidence, kept distinct
- Reproduction/evidence, with secrets redacted
- Status: `confirmed`, `needs_validation`, `false_positive`, `accepted_risk`, `fixed`, `retest_passed`
- Owner, remediation, due date, and retest evidence

AI-generated findings are candidates until validated. A severity label alone is not proof of exploitability.

## 5. No single-tool assurance
AISDF must use layered controls appropriate to the project:
- SAST / code rules
- Dependency and software composition analysis
- Secret detection
- IaC/container/cloud configuration scanning
- DAST / authorized penetration testing
- Malware scanning of untrusted artifacts where relevant
- AI-agent skill/plugin/MCP supply-chain inspection
- AI application red teaming where the product contains generative-AI features
- Human review and independent verification

Not every project needs every tool. Record `not_applicable` with a reason rather than running irrelevant scans.

## 6. Safe default sequence
1. Confirm scope and authorization.
2. Identify languages, package managers, containers, IaC, secrets locations, AI components, and deployment targets.
3. Run low-risk local checks first: Semgrep, Trivy filesystem/config scans, TruffleHog on authorized repository history, and SkillSpector for agent skills.
4. Review dependencies, licenses, and container images.
5. Run ClamAV on applicable untrusted files/build artifacts in an isolated environment.
6. Run DAST/Nuclei and Strix only against explicitly authorized test targets.
7. Run PyRIT only against owned/authorized AI model or application endpoints with bounded test budgets.
8. Validate findings independently, prioritize, remediate, and retest.
9. Produce a report with coverage, exclusions, tool versions, results, limitations, and residual risks.

## 7. Tool-specific cautions
- Strix and Nuclei can perform active testing; use explicit target allowlists and safe rate limits.
- TruffleHog may validate discovered credentials; credential verification requires explicit authorization. Redact secrets.
- Cloudflare Security Audit Skill requires an OS-enforced sandbox for target-controlled execution; without it, do not execute target code and keep unresolved leads as `needs_validation`.
- Claude Code Security Review warns that it is not hardened against prompt injection and recommends restricting execution to trusted PRs / maintainer-approved external contributions.
- SkillSpector should be used before installing third-party agent skills.
- PyRIT testing can produce adversarial prompts and potentially sensitive outputs; use test accounts and synthetic data.
- ClamAV signature freshness and scan errors must be reported; a clean result is not a guarantee of no malware.
- Semgrep Community Edition has analysis limitations; record edition/rule packs and coverage.
- BLA is an optional release-hardening / anti-reverse-engineering tool. It is not a substitute for vulnerability scanning, secure design, or code review.
- Codex Security availability, authentication, cost, supported workflows, and any access prerequisites must be verified for the user's account before use.

## 8. Required release gate
A release cannot claim `security_passed` solely because scanners returned zero findings. It must include:
- Defined scope and exclusions
- Tool/version inventory
- Scan coverage and failures
- Finding triage and disposition
- Remediation and retest evidence
- Human approval
- Residual-risk statement

## 9. Exceptions
An exception requires approver, rationale, affected assets, expiry date, compensating controls, and residual-risk owner.
