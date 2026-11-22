#!/usr/bin/env python3
"""AISDF repository quality gate. Validates structure, names, schemas, fixtures and internal Markdown links."""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]
required=['README.md','PROJECT.md','AGENTS.md','LICENSE','LICENSE-DECISION.md','templates/PROJECT.template.md','templates/AGENTS.template.md','workflows/WF-013-PROJECT-DEFINITION-ASSESSMENT-AND-IMPLEMENTATION-PLANNING.md','tools/aisdf_runtime/project.py','tools/aisdf_runtime/templates/PROJECT.md.template.md','AISDF-MISSION-AND-SCOPE.md','00-GOVERNANCE/AISDF-RULEBOOK.md','modes/MODE-1-PROBLEM-DISCOVERY.md','modes/MODE-2-NEW-PROJECT.md','modes/MODE-3-EXISTING-PROJECT.md','prompts/MASTER-ENTRY-PROMPT.md','REFERENCE-PROJECTS/DEVTRACK/README.md','RELEASE-READINESS.md','docs/project-lifecycle/PROJECT-AND-AGENT-FILES.md']
for rel in required:
 if not (ROOT/rel).is_file(): errors.append(f'Missing required file: {rel}')
engines=sorted((ROOT/'engines').glob('E-*.md')); schemas=sorted((ROOT/'schemas').glob('*.schema.json'))
if len(engines)!=56: errors.append(f'Expected 56 engine specs; found {len(engines)}')
ids=[]
for p in engines:
 m=re.match(r'E-(\d{3})-',p.name)
 if not m: errors.append(f'Invalid engine filename: {p.relative_to(ROOT)}')
 else: ids.append(int(m.group(1)))
 if '## Engine-specific execution contract' not in p.read_text(encoding='utf-8'): errors.append(f'Missing engine-specific contract: {p.name}')
if sorted(ids)!=list(range(1,57)): errors.append('Engine IDs must be exactly E-001 through E-056')
if len(schemas)<8: errors.append(f'Expected at least 8 schemas; found {len(schemas)}')
for p in schemas:
 try:
  data=json.loads(p.read_text(encoding='utf-8'))
  if data.get('$schema')!='https://json-schema.org/draft/2020-12/schema': errors.append(f'{p.name}: incorrect JSON Schema draft')
 except Exception as e: errors.append(f'{p.name}: invalid JSON: {e}')
fixtures=list((ROOT/'tests/fixtures').glob('*.json'))
for p in fixtures:
 try: json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{p.relative_to(ROOT)}: invalid JSON: {e}')
# Every major directory has README.md (root exceptions are explicit).
for d in [p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith('.')]:
 if any(d.iterdir()) and not (d/'README.md').is_file(): warnings.append(f'Major directory has no README.md: {d.name}')
# Internal markdown links (ignore anchors-only and external URLs).
for md in ROOT.rglob('*.md'):
 txt=md.read_text(encoding='utf-8')
 for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',txt):
  target=target.split('#',1)[0]
  if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'): continue
  resolved=(md.parent/target).resolve()
  if not resolved.exists(): errors.append(f'Broken Markdown link in {md.relative_to(ROOT)}: {target}')
# --- 1.0 additions: single version everywhere, pinned scanners, required hardening artefacts
ver=(ROOT/'VERSION').read_text().strip()
if json.loads((ROOT/'aisdf.manifest.json').read_text())['version']!=ver: errors.append('aisdf.manifest.json version differs from VERSION')
if f'Version: {ver}' not in (ROOT/'PROJECT.md').read_text(): errors.append('PROJECT.md version differs from VERSION')
if ver not in (ROOT/'README.md').read_text(): errors.append('README.md does not mention the current VERSION')
lock=ROOT/'security/scanners.lock.json'
if not lock.is_file(): errors.append('missing security/scanners.lock.json')
else:
 for e in json.loads(lock.read_text())['entries']:
  if not re.fullmatch(r'[0-9a-f]{40}',e.get('pinned_ref') or ''): errors.append(f"scanner lock entry {e.get('id')} is not pinned to a 40-char commit SHA")
for rel in ('aisdf.py','docs/framework/RULES-AND-ENFORCEMENT.md','security/policies/release-gate.json','adapters/COMPATIBILITY.md','adapters/CONFORMANCE.md','memory/README.md','examples/demo.sh','docs/demo/TRANSCRIPT.md'):
 if not (ROOT/rel).is_file(): errors.append(f'missing required file: {rel}')
wf_txt=(ROOT/'.github/workflows/validate.yml').read_text()
for ref in re.findall(r'uses:\s*(\S+)',wf_txt):
 if not re.search(r'@[0-9a-f]{40}$',ref): errors.append(f'CI action not pinned by commit SHA: {ref}')
try:
 import jsonschema
 for p in schemas: jsonschema.Draft202012Validator.check_schema(json.loads(p.read_text(encoding='utf-8')))
 mapping={'work-unit.valid.json':'work-unit.schema.json','completion-report.valid.json':'completion-report.schema.json'}
 for fixture,schema in mapping.items():
  fp=ROOT/'tests/fixtures'/fixture
  if fp.exists(): jsonschema.validate(json.loads(fp.read_text()),json.loads((ROOT/'schemas'/schema).read_text()))
 print('PASS: JSON Schema meta-validation and mapped fixture conformance.')
except ImportError: warnings.append('Install requirements-dev.txt for JSON Schema meta-validation and fixture conformance.')
except Exception as e: errors.append(f'JSON Schema validation: {e}')
if warnings:
 print('WARN:'); [print(' - '+w) for w in warnings]
if errors:
 print('FAIL:'); [print(' - '+e) for e in errors]; sys.exit(1)
print(f'PASS: {len(engines)} uniquely numbered engine specifications with specific contracts.')
print(f'PASS: {len(schemas)} JSON Schema files; {len(fixtures)} JSON fixtures parse.')
print('PASS: required project definition, agent instructions, reusable templates, license, WF-013 tooling, governance and release-readiness documents present.')
print(f'PASS: version {ver} consistent; scanner lock fully pinned; CI actions pinned by SHA; hardening artefacts present.')
print('NOTE: This does not prove external adapters, autonomous orchestration, or end-to-end software delivery.')
