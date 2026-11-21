# Security Architecture

## Trust boundaries
Human operator, orchestrator, worker adapter, model provider, repository, external tools, secrets, sandbox, CI and deployment target are separate trust zones.

## Controls
Default-deny permissions; exact work scope; short-lived scoped credentials; secret redaction; signed/digested plans; external sandbox for untrusted code; process/network/resource limits; tool allowlists; immutable audit events; approval gates; cancellation; independent verification.

## Threats
Prompt injection, instruction/data confusion, tool misuse, confused deputy, privilege escalation, malicious dependency, poisoned memory, data exfiltration, unsafe code execution, budget exhaustion, compromised adapter and forged evidence.

## Limitation
The local reference runtime is not a security boundary against a malicious local process. OS-level sandboxing, container isolation, credential brokering and network egress controls must be supplied by the deployment environment.
