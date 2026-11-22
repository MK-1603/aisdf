#!/usr/bin/env python3
"""Resolve security-tool / CI-action repositories to exact commit SHAs and write security/scanners.lock.json.

Run by a maintainer (needs network access to github.com + api.github.com). The lock records WHAT was resolved
and WHEN; it does not prove a release is safe. Always read the project's current security advisories first.
"""
import json, re, subprocess, sys, urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = [
    ("SEC-001", "Strix", "usestrix/strix"), ("SEC-002", "Cloudflare Security Audit Skill", "cloudflare/security-audit-skill"),
    ("SEC-003", "Trivy", "aquasecurity/trivy"), ("SEC-004", "Nuclei", "projectdiscovery/nuclei"),
    ("SEC-005", "TruffleHog", "trufflesecurity/trufflehog"), ("SEC-006", "NVIDIA SkillSpector", "NVIDIA/SkillSpector"),
    ("SEC-007", "Semgrep", "semgrep/semgrep"), ("SEC-008", "OpenAI Codex Security", "openai/codex-security"),
    ("SEC-009", "ClamAV", "Cisco-Talos/clamav"), ("SEC-010", "Claude Code Security Review", "anthropics/claude-code-security-review"),
    ("SEC-011", "BLA - Blind LLM Agents", "qybaihe/bla"), ("SEC-012", "Microsoft PyRIT", "microsoft/PyRIT"),
    ("CI-001", "actions/checkout", "actions/checkout"), ("CI-002", "actions/setup-python", "actions/setup-python"),
]
STABLE = re.compile(r"^(?:v|clamav-)?(\d+)\.(\d+)(?:\.(\d+))?$")

def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, timeout=90)

def resolve(repo):
    url = f"https://github.com/{repo}.git"
    head = git("ls-remote", url, "HEAD")
    head_sha = head.stdout.split()[0] if head.returncode == 0 and head.stdout.strip() else None
    tags = {}
    r = git("ls-remote", "--tags", url)
    if r.returncode == 0:
        for line in r.stdout.splitlines():
            sha, ref = line.split("\t")
            name = ref[len("refs/tags/"):]
            peeled = name.endswith("^{}")
            name = name[:-3] if peeled else name
            m = STABLE.match(name)
            if m:
                key = tuple(int(x or 0) for x in m.groups())
                if name not in tags or peeled:  # prefer peeled commit sha for annotated tags
                    tags[name] = (key, sha)
    latest = max(tags.items(), key=lambda kv: kv[1][0]) if tags else None
    lic = None
    ref = (latest[1][1] if latest else head_sha)
    for fname in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"):
        try:
            req = urllib.request.Request(f"https://raw.githubusercontent.com/{repo}/{ref}/{fname}", headers={"User-Agent": "aisdf-pin"})
            text = urllib.request.urlopen(req, timeout=30).read(6000).decode("utf-8", "replace").lower()
        except Exception:
            continue
        if "gnu affero general public license" in text: lic = "AGPL-3.0 (detected from license file)"
        elif "gnu lesser general public license" in text: lic = "LGPL (detected from license file)"
        elif "gnu general public license" in text: lic = "GPL (detected from license file)"
        elif "apache license" in text: lic = "Apache-2.0 (detected from license file)"
        elif "permission is hereby granted, free of charge" in text: lic = "MIT-style (detected from license file)"
        else: lic = "OTHER: read the license file"
        break
    return {"head_sha": head_sha, "latest_stable_tag": latest[0] if latest else None, "latest_stable_tag_commit": latest[1][1] if latest else None, "license_detected": lic or "UNRESOLVED: read the repository license before use"}

def main():
    entries = []
    for tid, name, repo in TOOLS:
        try:
            info = resolve(repo)
        except Exception as e:
            info = {"error": str(e)}
        pin = info.get("latest_stable_tag_commit") or info.get("head_sha")
        entries.append({"id": tid, "name": name, "repository": f"https://github.com/{repo}", **info,
                        "pinned_ref": pin, "pinned_ref_kind": "release_tag_commit" if info.get("latest_stable_tag_commit") else ("default_branch_head" if pin else "UNRESOLVED")})
        print(f"{tid} {name:34} {entries[-1]['pinned_ref_kind']:20} {pin} {info.get('latest_stable_tag')} {info.get('license_detected')}")
    lock = {"schema": "aisdf.scanners-lock/1", "resolved_on": date.today().isoformat(), "resolved_via": "git ls-remote + raw LICENSE file keyword detection",
            "limitations": ["Resolution proves a ref existed on that date, not that it is safe: read the project's security advisories before use.",
                            "Release signatures/checksums were NOT verified by this script; verify them when installing.",
                            "Trivy had a March 2026 supply-chain compromise (GHSA-69fq-xp46-6x23 / CVE-2026-33634): never use floating tags or actions for it; pin by SHA and review the advisory.",
                            "Licenses are keyword-detected from the LICENSE file, not legally verified; confirm before redistributing. Call GPL/AGPL tools as external programs; do not vendor them into this MIT repo."],
            "entries": entries}
    out = ROOT / "security" / "scanners.lock.json"
    out.write_text(json.dumps(lock, indent=2), encoding="utf-8")
    print("WROTE", out)

if __name__ == "__main__":
    main()
