# AISDF Security Tool Registry — 12 Candidate Repositories

**Registry status:** Researched from the projects' public README files on 2026-11-21. Capabilities and terms can change; verify official documentation and exact release before adoption. Inclusion does not imply endorsement, certification, installation, or a tested AISDF adapter.

| # | Project | Primary role in AISDF | Best-fit stage | Important boundary |
|---:|---|---|---|---|
| 1 | [Strix](https://github.com/usestrix/strix) | AI-assisted dynamic application penetration testing with proof-oriented findings | Authorized DAST / pre-release | Active testing only on explicitly authorized targets; Docker and model/API credentials may be required |
| 2 | [Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill) | Multi-phase, coverage-led code security audit with independent candidate validation and structured reports | Deep code audit | Requires an OS-enforced sandbox for target-controlled execution; without it, findings remain unresolved |
| 3 | [Trivy](https://github.com/aquasecurity/trivy) | Filesystem, repository, container, VM and Kubernetes scanning for vulnerabilities, misconfigurations, secrets and licenses | SCA / container / IaC / baseline | Select scanners and targets deliberately; distinguish vulnerability, misconfiguration, secret and license findings |
| 4 | [Nuclei](https://github.com/projectdiscovery/nuclei) | Template-based vulnerability scanning across HTTP, network and other supported protocols | Authorized DAST / attack-surface checks | Templates can send active requests; strict allowlist, rate limits and authorization required |
| 5 | [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Secret discovery, classification and (for supported detectors) credential validation/analysis | Secret scanning | Validation may contact providers; obtain authorization and never publish raw secret values |
| 6 | [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) | Static and optional LLM-assisted analysis of AI-agent skills for malicious patterns and supply-chain risks | Before installing skills/plugins | Treat skill bundles and analyzer output as untrusted; review findings before installation |
| 7 | [Semgrep](https://github.com/semgrep/semgrep) | Static code analysis and security-rule enforcement; ecosystem offerings include SAST/SCA/secrets capabilities | SAST / pre-commit / CI | Community Edition has documented analysis limits; record edition, rules and language coverage |
| 8 | [OpenAI Codex Security](https://github.com/openai/codex-security) | AI-assisted repository security scans, finding validation, patch proposals and verification workflows | Deep review / remediation support | Requires supported CLI/authentication and possibly account access; verify cost, scope and access before automation |
| 9 | [ClamAV](https://github.com/Cisco-Talos/clamav) | Antivirus/malware detection for files and artifacts | Artifact / upload scanning | Not a source-code vulnerability scanner; keep signatures current and isolate untrusted samples |
| 10 | [Claude Code Security Review](https://github.com/anthropics/claude-code-security-review) | AI-assisted, diff-aware security review for GitHub pull requests | PR security review | Project README warns it is not hardened against prompt injection; restrict to trusted/approved PRs |
| 11 | [BLA — Blind LLM Agents](https://github.com/qybaihe/bla) | Defensive hardening of release artifacts against AI reverse-engineering agents | Optional IP / artifact hardening | Not a general vulnerability scanner; validate runtime equivalence and test promoted artifacts |
| 12 | [Microsoft PyRIT](https://github.com/microsoft/pyrit) | Red-team testing of generative-AI models and applications using repeatable/adaptive assessments | AI application security testing | Use owned/authorized test endpoints, synthetic data, bounded budgets and human review |

## Capability grouping

| Security layer | Candidate tools |
|---|---|
| Static code analysis (SAST) | Semgrep; Cloudflare Security Audit Skill; Codex Security; Claude Code Security Review |
| Dependency / container / IaC / license scanning | Trivy |
| Secret detection | TruffleHog; Trivy (secret scanner) |
| Dynamic application / network testing | Strix; Nuclei |
| Agent skill / plugin supply-chain review | NVIDIA SkillSpector |
| Malware / artifact scanning | ClamAV |
| Generative-AI red teaming | Microsoft PyRIT |
| Defensive anti-reverse-engineering hardening | BLA |

## Suggested baseline for a typical web application

- Pull request: Semgrep + Trivy filesystem/dependency checks + TruffleHog secret scan.
- Agent skill installation: SkillSpector before installation.
- Build artifacts/container: Trivy image scan; ClamAV only where untrusted file scanning is relevant.
- Staging: Nuclei and/or Strix after written scope authorization.
- AI features: PyRIT against a dedicated test environment.
- High-risk code changes: Cloudflare Security Audit Skill or Codex Security as a deeper review; Claude Code Security Review only for trusted PR workflows.
- Release artifact IP protection: evaluate BLA separately if reverse-engineering resistance is a genuine requirement.

Do not run all 12 on every project. Select by architecture and risk, and document why each tool is used or not applicable.
