# Security Tooling

- `scanners.lock.json` - the 12 catalogued tools and the CI actions, each resolved to an exact commit SHA on the date shown. Regenerate with `python tools/pin_scanners.py` (needs network). A pin proves a ref existed, **not** that it is safe: read the project's advisories first, and verify release signatures/checksums when installing.
- `policies/release-gate.json` - which checks the default release gate requires.

## How each tool plugs in
Tools are **not bundled or executed by AISDF**. Install the pinned version yourself, add its executable to `allowed_executables` in `.aisdf/policy.json`, then record results as gate checks:

```bash
python aisdf.py check run --project P --id secrets-scan --tool trufflehog --tool-version 3.x --pinned-ref <sha> -- trufflehog filesystem . --fail
python aisdf.py check run --project P --id dependency-scan --tool trivy --pinned-ref <sha> -- trivy fs --exit-code 1 .
python aisdf.py check run --project P --id sast --tool semgrep --pinned-ref <sha> -- semgrep scan --error
```
`check run` marks PASS only on exit code 0 and stores redacted logs with hashes. Exit-code conventions differ per tool; confirm yours.

| Tool | Gate check | Use and caveats |
|---|---|---|
| TruffleHog | `secrets-scan` | Leaked secrets. AGPL: call as an external program, do not vendor |
| Trivy | `dependency-scan` | Dependencies/containers/IaC. **Pin by SHA; a 2026 supply-chain compromise hit its GitHub Action** (GHSA-69fq-xp46-6x23) |
| Semgrep | `sast` | Static analysis. Check rule-pack licenses |
| NVIDIA SkillSpector | `skill-supply-chain` | Scan third-party agent skills before use. A "safe" verdict is a floor, not proof |
| Nuclei / Strix | `dast` | Dynamic testing. **Authorized targets only**; Strix uses LLM API credits |
| Microsoft PyRIT | `llm-red-team` | Only when the product contains an LLM |
| Cloudflare security-audit-skill | pattern for `independent-review` | Its key idea (the finder never validates its own findings) is what the EGM Goldfish reviewer implements |
| OpenAI Codex Security | optional | Requires OpenAI access; never a mandatory dependency |
| Claude Code Security Review | optional | Not hardened against prompt injection: trusted pull requests only |
| ClamAV | optional | Malware scan of downloaded artifacts |
| BLA (Blind LLM Agents) | optional, release hardening | **Not a scanner.** It protects shipped binaries against AI reverse-engineering; obfuscation reduces auditability, so apply it only after the audit |
