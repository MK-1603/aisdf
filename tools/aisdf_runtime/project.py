#!/usr/bin/env python3
"""AISDF project definition and planning helper; read-only against application source."""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

IGNORE={'.git','node_modules','.next','dist','build','.venv','venv','__pycache__','.turbo','.idea','.vscode','coverage','.aisdf'}
ROOT=Path(__file__).resolve().parents[2]
TEMPLATE=ROOT/'tools'/'aisdf_runtime'/'templates'/'PROJECT.md.template.md'
AGENT_TEMPLATE=ROOT/'templates'/'AGENTS.template.md'

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def write_new(path:Path, text:str):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists(): raise SystemExit(f'Refusing to overwrite existing file: {path}. Review and merge manually.')
    path.write_text(text,encoding='utf-8'); print(path)
def git(p:Path,*args):
    try:
        r=subprocess.run(['git','-C',str(p),*args],capture_output=True,text=True,check=True,timeout=20)
        return r.stdout.strip()
    except Exception: return None

def init(a):
    p=Path(a.project).resolve()
    if not p.is_dir(): raise SystemExit(f'Project directory does not exist: {p}')
    project=p/'PROJECT.md'
    content=TEMPLATE.read_text(encoding='utf-8').replace('PROJECT-REPLACE',a.project_id or p.name.upper().replace(' ','-'))
    if a.name: content=content.replace('Project/project name:',f'Project/project name: {a.name}')
    write_new(project,content)
    aisdf=p/'.aisdf'
    for d in ('assessment','findings','plans','prompts','reports','context'): (aisdf/d).mkdir(parents=True,exist_ok=True)
    manifest={'runtime':'AISDF Project Lifecycle Helper','version':'1.0.0','created_at':now(),'project_root':str(p),'project_definition':'PROJECT.md','agent_instructions':'AGENTS.md','source_editing_by_runtime':False,'human_approval_required':True}
    mp=aisdf/'project-manifest.json'
    if not mp.exists(): mp.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    else: print(f'Preserved existing {mp}')
    if a.add_agents and not (p/'AGENTS.md').exists(): write_new(p/'AGENTS.md',AGENT_TEMPLATE.read_text(encoding='utf-8'))
    elif (p/'AGENTS.md').exists(): print(f'Preserved existing {p/"AGENTS.md"}; inspect and merge template manually.')
    print('Created AISDF project workspace. No application source files were changed.')

def inventory(p):
    files=[]
    for f in sorted(p.rglob('*')):
        if not f.is_file(): continue
        rel=f.relative_to(p)
        if any(part in IGNORE for part in rel.parts): continue
        try: size=f.stat().st_size
        except OSError: continue
        files.append((rel.as_posix(),size))
    return files

def assess(a):
    p=Path(a.project).resolve()
    if not p.is_dir(): raise SystemExit(f'Project directory does not exist: {p}')
    files=inventory(p); branch=git(p,'branch','--show-current'); commit=git(p,'rev-parse','HEAD'); status=git(p,'status','--short')
    top={}
    for rel,_ in files: top.setdefault(rel.split('/',1)[0] if '/' in rel else '(root)',0); top[rel.split('/',1)[0] if '/' in rel else '(root)']+=1
    known=['README.md','PROJECT.md','AGENTS.md','CLAUDE.md','package.json','pyproject.toml','requirements.txt','Cargo.toml','go.mod','pom.xml','build.gradle','Dockerfile','docker-compose.yml','.github/workflows','tests','test','src','app','pages','migrations','prisma','drizzle']
    present=[x for x in known if (p/x).exists()]
    lines=['# Existing Project Assessment', '',f'- Generated: {now()}',f'- Repository root: `{p}`',f'- Git branch: `{branch or "NOT_AVAILABLE"}`',f'- Git revision: `{commit or "NOT_AVAILABLE"}`',f'- Working tree: `{"DIRTY" if status else "CLEAN/UNKNOWN"}`',f'- Files inventoried: {len(files)}','', '> This report is a deterministic repository inventory, not an AI semantic audit. Feature implementation status must be confirmed by inspecting source and tests.', '', '## Detected project artifacts']
    lines += [f'- `{x}`: {"PRESENT" if x in present else "NOT_FOUND"}' for x in known]
    lines += ['', '## Top-level inventory']+[f'- `{k}` — {v} files' for k,v in sorted(top.items())]
    lines += ['', '## Full file inventory']+[f'- `{r}` ({s} bytes)' for r,s in files]
    lines += ['', '## Agent instruction files to inspect']
    instr=[r for r,_ in files if Path(r).name in ('AGENTS.md','AGENTS.override.md','CLAUDE.md','GEMINI.md') or r.startswith('.cursor/rules/') or r.startswith('.agents/rules/') or r.startswith('.claude/rules/')]
    lines += [f'- `{r}`' for r in instr] or ['- NONE FOUND']
    lines += ['', '## Semantic assessment — agent/reviewer must complete', '- Problem statement accurately reflects current users and pain: NOT_ASSESSED', '- Feature/function inventory mapped to code and tests: NOT_ASSESSED', '- Business rules and role/permission behavior: NOT_ASSESSED', '- Architecture/data/API/integration map: NOT_ASSESSED', '- NFRs/security/privacy/accessibility/performance: NOT_ASSESSED', '- Missing/partial/conflicting features: NOT_ASSESSED', '- Build/test/deploy commands verified: NOT_ASSESSED', '- Risks, assumptions, unknowns, and dependencies: NOT_ASSESSED', '', '## Required next actions', '1. Read PROJECT.md and all applicable agent instruction files.', '2. Inspect source, docs, manifests, tests, migrations, CI and deployment configuration.', '3. Build an evidence-linked feature matrix with statuses defined in WF-013.', '4. Update PROJECT.md as a proposed draft; preserve user-approved content.', '5. Create a plan and stop for explicit approval before source changes.', '', '## Limitations', '- File presence does not prove a feature works.', '- No source files were modified.', '- No build, test, security scan, deployment, or runtime behavior was executed by this command.']
    out=p/'.aisdf'/'assessment'/'EXISTING-PROJECT-ASSESSMENT.md'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text('\n'.join(lines)+'\n',encoding='utf-8'); print(out)

def plan_create(a):
    p=Path(a.project).resolve(); pid=a.id.upper(); out=p/'.aisdf'/'plans'/f'IMPLEMENTATION-PLAN-{pid}.md'
    body=f'''# Implementation Plan — {pid}: {a.title}\n\n- Status: DRAFT — NOT APPROVED\n- Created: {now()}\n- Project definition: `PROJECT.md`\n- Assessment: `.aisdf/assessment/EXISTING-PROJECT-ASSESSMENT.md`\n- Project revision at planning: `{git(p,"rev-parse","HEAD") or "NOT_AVAILABLE"}`\n\n## 1. Problem and desired outcome\n- Problem statement / evidence:\n- Desired outcome:\n- User impact:\n\n## 2. Traceability\n| Work item | PROJECT.md FR/AC IDs | Current state evidence | Target behavior | Priority |\n|---|---|---|---|---|\n| WI-001 | TBD | TBD | TBD | TBD |\n\n## 3. Findings addressed\n| Finding ID | Severity | Resolution approach |\n|---|---|---|\n| TBD | TBD | TBD |\n\n## 4. Phases and dependencies\n| Phase | Work units | Dependencies | Exit criteria |\n|---|---|---|---|\n| P1 | TBD | None | TBD |\n\n## 5. Exact file allowlist\nList every file that may be created, modified, or deleted. No wildcard paths.\n- TBD\n\n## 6. Data/API/migration impact\n- Data changes:\n- API/contracts:\n- Migration and backward compatibility:\n\n## 7. Verification plan\n| Check | Command / method | Expected result |\n|---|---|---|\n| Tests | TBD | PASS |\n\n## 8. Security, privacy, performance, accessibility and reliability risks\n- TBD\n\n## 9. Rollout and rollback\n- Rollout:\n- Rollback:\n- Monitoring:\n\n## 10. Out of scope\n- TBD\n\n## 11. Approval record — human must complete\n- Approval status: NOT_APPROVED\n- Approved by: NOT_SET\n- Approval date: NOT_SET\n- Approved plan revision/SHA-256: NOT_SET\n- Approved exact file allowlist: NOT_SET\n- Notes/conditions: NOT_SET\n\n**No implementation prompt or source modification is authorized until this approval record is completed by an authorized human for this exact plan revision and allowlist.**\n'''
    write_new(out,body)

def approval_digest(txt:str)->str:
    # Approval block is excluded so the human can record this digest inside that block.
    pre=txt.split('## 11. Approval record',1)[0]
    return hashlib.sha256(pre.encode()).hexdigest()

def plan_hash(a):
    p=Path(a.project).resolve(); candidate=Path(a.plan); plan=(candidate if candidate.is_absolute() else p/candidate).resolve()
    if not plan.is_file() or not plan.is_relative_to((p/'.aisdf'/'plans').resolve()): raise SystemExit('Plan must be inside .aisdf/plans.')
    print('sha256:'+approval_digest(plan.read_text(encoding='utf-8')))

def prompt_create(a):
    p=Path(a.project).resolve(); candidate=Path(a.plan); plan=(candidate if candidate.is_absolute() else p/candidate).resolve()
    if not plan.is_file() or not plan.is_relative_to((p/'.aisdf'/'plans').resolve()): raise SystemExit('Plan must be an existing file inside this project .aisdf/plans directory.')
    txt=plan.read_text(encoding='utf-8')
    import re
    fields={key:re.search(rf'^- {re.escape(key)}: (.+)$',txt,re.M) for key in ('Approval status','Approved by','Approval date','Approved plan revision/SHA-256')}
    if any(v is None for v in fields.values()): raise SystemExit('Plan approval block is incomplete.')
    values={k:v.group(1).strip() for k,v in fields.items()}
    if values['Approval status']!='APPROVED' or any(not v or v in ('NOT_SET','TBD','UNSET') for k,v in values.items() if k!='Approval status'):
        raise SystemExit('Plan must be APPROVED with a named human approver, date, and digest.')
    if '## 5. Exact file allowlist' not in txt or '## 6.' not in txt: raise SystemExit('Exact file allowlist section is missing.')
    allow=txt.split('## 5. Exact file allowlist',1)[1].split('## 6.',1)[0]
    entries=[line.strip()[2:].strip().strip('`') for line in allow.splitlines() if line.strip().startswith('- ')]
    if not entries or any(x in ('TBD','- TBD','') or '*' in x or x.startswith('/') or '..' in Path(x).parts for x in entries): raise SystemExit('Exact file allowlist is empty, contains placeholders, wildcards, or unsafe paths.')
    digest='sha256:'+approval_digest(txt)
    if '- Approved plan revision/SHA-256: '+digest not in txt: raise SystemExit('Approval digest mismatch. Run plan-hash after finalizing plan sections, then record its output in the approval block. Re-approve if the plan changes.')
    sha=hashlib.sha256(txt.encode()).hexdigest()
    out=p/'.aisdf'/'prompts'/f'IMPLEMENTATION-PROMPT-{plan.stem.replace("IMPLEMENTATION-PLAN-","")}.md'
    body=f'''# Approved Implementation Execution Prompt\n\nYou are implementing an explicitly approved AISDF work plan in the real project repository.\n\n## Mandatory context\n1. Read root and applicable nested `AGENTS.md`, plus native host instruction files.\n2. Read `PROJECT.md` as product/engineering source of truth.\n3. Read the complete approved plan: `{plan.relative_to(p).as_posix()}`.\n4. Approved plan SHA-256 at prompt generation: `{sha}`. Recompute before edits; if it differs, STOP and request re-approval.\n5. Read linked requirements, ADRs, tests and findings referenced by the plan.\n\n## Authorization boundary\n- Implement only the exact file allowlist in section 5 of the approved plan.\n- Do not expand scope, add unrelated dependencies, rewrite architecture, or change behavior not tied to approved requirement IDs.\n- Ask before destructive actions, production data changes, migrations against shared environments, external communications, pushes, merges, deployments, or costs.\n- Preserve all existing user changes and instruction files.\n\n## Execution protocol\n1. Confirm repository root, branch, clean/dirty state, and current revision.\n2. Inspect relevant implementation and tests before editing.\n3. Translate plan work units into small steps and maintain traceability to PROJECT.md FR/AC IDs.\n4. Implement the smallest coherent diff.\n5. Run the exact verification commands from the plan and relevant regression tests.\n6. Review security, privacy, error handling, accessibility, performance and compatibility as applicable.\n7. Compare Git changes against the approved file allowlist; stop on out-of-scope changes.\n8. Update PROJECT.md feature/acceptance statuses only when supported by evidence; do not rewrite approved requirements silently.\n9. Produce a completion report listing changed files, requirement IDs, commands/results, unrun checks, residual findings, and rollback notes.\n\n## Truthfulness\nNever claim a test, review, security scan, host integration, or deployment succeeded unless actually executed. Use PASS, FAIL, NOT_RUN, BLOCKED, or NOT_APPLICABLE with evidence. Do not mark production verified based on local tests.\n\n## Stop conditions\nStop and report BLOCKED if approval/hash/allowlist is invalid, required context is missing, a conflict changes scope, a destructive action is needed, or a critical acceptance criterion cannot be met.\n'''
    write_new(out,body)

def main():
    ap=argparse.ArgumentParser(description='AISDF project definition, assessment, planning and approved-prompt helper'); sp=ap.add_subparsers(dest='cmd',required=True)
    x=sp.add_parser('init',help='create PROJECT.md and .aisdf workspace without overwriting existing files'); x.add_argument('--project',default='.'); x.add_argument('--name'); x.add_argument('--project-id'); x.add_argument('--add-agents',action='store_true'); x.set_defaults(fn=init)
    x=sp.add_parser('assess',help='create deterministic existing-repository inventory; does not edit source'); x.add_argument('--project',default='.'); x.set_defaults(fn=assess)
    x=sp.add_parser('plan-create',help='create a draft implementation plan'); x.add_argument('--project',default='.'); x.add_argument('--id',required=True); x.add_argument('--title',required=True); x.set_defaults(fn=plan_create)
    x=sp.add_parser('plan-hash',help='print the plan content digest to be signed in the approval block'); x.add_argument('--project',default='.'); x.add_argument('--plan',required=True); x.set_defaults(fn=plan_hash)
    x=sp.add_parser('prompt-create',help='generate execution prompt only from explicitly approved plan'); x.add_argument('--project',default='.'); x.add_argument('--plan',required=True); x.set_defaults(fn=prompt_create)
    a=ap.parse_args(); a.fn(a)
if __name__=='__main__': main()
