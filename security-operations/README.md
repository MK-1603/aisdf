# AISDF Security Operations

Security is a specialist engineering department and a release assurance function. It covers governance, threat modeling, secure design, application security, code review, authorized penetration testing, cloud/container/IaC security, IAM, API security, supply chain, privacy, AI/agent security, incident response, remediation and independent retesting.

## Security team
`workforce/teams/SECURITY/` contains role contracts and manifests for Security Lead, Application Security Engineer, Security Code Reviewer, Penetration Tester, Cloud Security Engineer, IAM Security Engineer, DevSecOps Engineer, Supply Chain Security Engineer, AI Security Engineer, Privacy Engineer, Incident Response Engineer and Independent Security Auditor.

## Required workflow
1. Obtain written authorization and target scope.
2. Inventory assets and trust boundaries.
3. Threat model and define risk acceptance.
4. Run applicable static, dependency, secret, infrastructure and dynamic checks using installed tools.
5. Validate findings and remove false positives with evidence.
6. Prioritize by severity, exploitability and impact.
7. Propose remediation and obtain approval for changes.
8. Implement within approved scope.
9. Retest independently.
10. Record residual risk and human security decision.

## Safety boundaries
No testing against third-party systems without explicit written authorization. No credential theft, persistence, destructive testing, denial of service, or uncontrolled exploit execution. Scope, time, rate, environment and stop conditions must be recorded. This repository does not bundle a scanner engine or sandbox. Tool registry entries are not proof of installation or certification.
