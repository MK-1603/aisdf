#!/usr/bin/env python3
"""AISDF portable workflow runtime. Python stdlib only; does not edit app source."""
from __future__ import annotations
import argparse, json, hashlib, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

VERSION = "0.1.0"

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def project_path(s): return Path(s).resolve()
def aisdf_dir(project): return project / ".aisdf"
def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content, encoding="utf-8"); print(path)
def read_json(p): return json.loads(p.read_text(encoding="utf-8"))
def dump_json(p, obj): write(p, json.dumps(obj, indent=2, ensure_ascii=False)+"\n")
def slug(s): return "-".join("".join(c.lower() if c.isalnum() else " " for c in s).split())[:60] or "untitled"

def cmd_init(a):
    p=project_path(a.project); d=aisdf_dir(p)
    for x in ["concepts","specs","reviews","findings","context","reports"]: (d/x).mkdir(parents=True,exist_ok=True)
    manifest={"runtime":"AISDF EGM Workflow Runtime","version":VERSION,"created_at":now(),"project_root":str(p),"human_approval_required":True,"source_editing_by_runtime":False}
    dump_json(d/"runtime-manifest.json",manifest)
    write(d/"README.md","# AISDF project workspace\n\nGenerated workflow artifacts live here. Treat all AI-generated content as draft until explicitly approved by an authorized human.\n")

def cmd_challenge(a):
    p=project_path(a.project); d=aisdf_dir(p)/"concepts"/(a.id or slug(a.title)+".md")
    body=f"""# Concept Challenge: {a.title}\n\n- ID: {a.id or slug(a.title)}\n- Created: {now()}\n- Status: DRAFT — NOT APPROVED\n\n## Problem and evidence\n- User/problem statement:\n- Evidence/source:\n- Who experiences it and how often:\n- Current workaround:\n\n## Challenge lenses\n### User value\n- Strongest case:\n- Disconfirming evidence:\n### Product and scope\n- Smallest valuable outcome:\n- YAGNI / scope risks:\n### Architecture and operations\n- Reuse before build:\n- Complexity and operational cost:\n### Security, privacy, and abuse\n- Data touched:\n- Threats / misuse cases:\n### Failure and recovery\n- Failure modes:\n- Recovery / rollback:\n### Alternatives and kill criteria\n- Build / buy / reuse / defer alternatives:\n- Kill or defer conditions:\n\n## Dissenting views (preserve, do not erase)\n-\n\n## Decision\n- Decision: UNDECIDED\n- Human decision owner:\n- Rationale:\n- Approval evidence:\n"""
    write(d,body)

def spec_template(sid,title):
    sections=["Executive summary","Problem and evidence","Goals and non-goals","Users and use cases","Requirements and acceptance criteria","Constraints and assumptions","Existing system and reuse analysis","Proposed architecture","Data model and lifecycle","API and integration contracts","UX and accessibility","Security, privacy, and abuse prevention","Reliability and failure handling","Performance and scalability","Observability and operations","Migration and compatibility","Testing and verification strategy","Rollout, rollback, and recovery","Risks and mitigations","Alternatives considered","Open questions and dissent","Implementation file allowlist"]
    out=[f"# Design Specification: {title}",f"\n- ID: {sid}",f"- Created: {now()}","- Status: DRAFT — HUMAN APPROVAL REQUIRED","- Source concept: .aisdf/concepts/ (link exact artifact)","\n> Do not implement until the spec is approved and the exact file allowlist is authorized."]
    for i,s in enumerate(sections,1): out += [f"\n## {i}. {s}\n", "- TBD"]
    out += ["\n## Approval record\n- Product owner: PENDING\n- Technical owner: PENDING\n- Security/privacy review: PENDING / NOT APPLICABLE WITH RATIONALE\n- Approved version/hash: PENDING\n- Approval timestamp: PENDING\n"]
    return "\n".join(out)

def cmd_spec_create(a):
    p=project_path(a.project); sid=a.id.upper(); write(aisdf_dir(p)/"specs"/(sid+".md"),spec_template(sid,a.title))

def validate_spec(path):
    txt=path.read_text(encoding="utf-8"); required=["Executive summary","Problem and evidence","Goals and non-goals","Requirements and acceptance criteria","Proposed architecture","Security, privacy, and abuse prevention","Testing and verification strategy","Implementation file allowlist","Approval record"]
    missing=[x for x in required if x.lower() not in txt.lower()]
    allow=txt.split("## 22. Implementation file allowlist",1)[-1].split("## Approval record",1)[0] if "## 22. Implementation file allowlist" in txt else ""
    placeholders=allow.strip() in ("- TBD","TBD","")
    return {"valid":not missing and not placeholders,"missing_sections":missing,"file_allowlist_placeholder":placeholders,"human_approval_required":True,"spec_sha256":hashlib.sha256(txt.encode()).hexdigest()}
def cmd_validate_spec(a):
    r=validate_spec(project_path(a.spec)); print(json.dumps(r,indent=2)); sys.exit(0 if r["valid"] else 2)

def cmd_review_init(a):
    p=project_path(a.project); sid=a.spec_id.upper(); d=aisdf_dir(p)/"reviews"/(sid+"-review.json")
    obj={"spec_id":sid,"created_at":now(),"status":"PENDING","independence":{"status":"UNVERIFIED","reviewer_session_ids":[],"evidence":None,"rule":"Do not mark independent without proof of a fresh context with no access to prior discussion or hidden deliberation."},"stages":[{"id":"R1","name":"Zoom-out: simplicity, YAGNI, reuse","status":"PENDING"},{"id":"R2","name":"Comprehension and self-containment","status":"PENDING"},{"id":"R3","name":"Architecture, scale, security, failure critique","status":"PENDING"},{"id":"R4","name":"Second zoom-out after revisions","status":"PENDING"},{"id":"R5","name":"Implementation readiness and file allowlist","status":"PENDING"}],"finding_ids":[],"human_decision":"PENDING"}
    dump_json(d,obj)

def cmd_review_validate(a):
    f=project_path(a.review); o=read_json(f); errors=[]
    if len(o.get("stages",[]))!=5: errors.append("exactly five review stages required")
    if any(s.get("status")!="COMPLETE" for s in o.get("stages",[])): errors.append("all five stages must be COMPLETE")
    ind=o.get("independence",{})
    if ind.get("status")=="VERIFIED" and (not ind.get("reviewer_session_ids") or not ind.get("evidence")): errors.append("independence VERIFIED requires session IDs and evidence")
    if ind.get("status") not in ("VERIFIED","NON_INDEPENDENT","BLOCKED","UNVERIFIED"): errors.append("invalid independence status")
    print(json.dumps({"valid":not errors,"errors":errors,"independence_status":ind.get("status"),"human_decision":o.get("human_decision")},indent=2)); sys.exit(0 if not errors else 2)

def cmd_review_stage(a):
    f=project_path(a.review); o=read_json(f)
    stage=next((x for x in o.get("stages",[]) if x.get("id")==a.stage.upper()),None)
    if stage is None: raise SystemExit("Unknown stage; use R1 through R5")
    if a.status not in ("PENDING","IN_PROGRESS","COMPLETE","BLOCKED"): raise SystemExit("Invalid stage status")
    if a.status=="COMPLETE" and not a.evidence.strip(): raise SystemExit("Completion evidence is required")
    stage.update({"status":a.status,"evidence":a.evidence or None,"updated_at":now()})
    o["status"]="IN_PROGRESS" if any(x["status"]!="COMPLETE" for x in o["stages"]) else "REVIEW_STAGES_COMPLETE"
    dump_json(f,o)

def cmd_review_independence(a):
    f=project_path(a.review); o=read_json(f)
    if a.status not in ("VERIFIED","NON_INDEPENDENT","BLOCKED"): raise SystemExit("Invalid independence status")
    if a.status=="VERIFIED" and (not a.session_id or not a.evidence.strip()): raise SystemExit("VERIFIED requires session ID and evidence")
    o["independence"]={"status":a.status,"reviewer_session_ids":[a.session_id] if a.session_id else [],"evidence":a.evidence or None,"recorded_at":now(),"rule":"Verification is an operator assertion backed by supplied evidence; runtime cannot inspect host context isolation."}
    dump_json(f,o)

def cmd_finding_add(a):
    p=project_path(a.project); fid=a.id.upper(); f=aisdf_dir(p)/"findings"/(fid+".json")
    obj={"id":fid,"spec_id":a.spec_id.upper(),"title":a.title,"description":a.description,"severity":a.severity,"status":"OPEN","owner":a.owner,"created_at":now(),"disposition":None,"resolution_evidence":None,"re_review_status":"PENDING"}
    dump_json(f,obj)
def cmd_finding_resolve(a):
    f=project_path(a.finding); o=read_json(f)
    if a.disposition not in ("FIXED","ACCEPTED_RISK","WONT_FIX","DUPLICATE","NOT_A_BUG"): raise SystemExit("Invalid disposition")
    if not a.evidence.strip(): raise SystemExit("Resolution evidence is required")
    o.update({"status":"RESOLVED","disposition":a.disposition,"resolution_evidence":a.evidence,"re_review_status":"PENDING" if a.disposition=="FIXED" else "NOT_REQUIRED_WITH_RATIONALE","resolved_at":now()})
    dump_json(f,o)

def cmd_bootstrap(a):
    p=project_path(a.project); ignored={".git","node_modules",".next","dist","build",".venv","venv","__pycache__",".turbo"}; files=[]
    for f in sorted(p.rglob("*")):
        if not f.is_file() or any(part in ignored for part in f.relative_to(p).parts) or ".aisdf" in f.parts: continue
        rel=f.relative_to(p).as_posix(); files.append((rel,f.stat().st_size))
    groups={}
    for rel,size in files: groups.setdefault(rel.split("/",1)[0] if "/" in rel else "(root)",[]).append((rel,size))
    lines=["# Codebase Context Map",f"\n- Generated: {now()}",f"- Root: `{p}`",f"- Files inventoried: {len(files)}","\n> Deterministic inventory only. It does not infer architecture, runtime behavior, ownership, or security properties.","\n## Top-level structure"]
    for group,items in groups.items(): lines.append(f"- **{group}** — {len(items)} files")
    lines += ["\n## File inventory"]+[f"- `{r}` ({s} bytes)" for r,s in files]
    lines += ["\n## Human/agent enrichment required","- Languages and frameworks:","- Entrypoints and runtime topology:","- Data stores and data flows:","- External integrations:","- Build/test/deploy commands:","- Security boundaries and sensitive data:","- Unknowns and evidence links:"]
    write(aisdf_dir(p)/"context/CODEBASE-MAP.md","\n".join(lines)+"\n")

def git_changed(p):
    try:
        r=subprocess.run(["git","-C",str(p),"status","--porcelain","--untracked-files=all"],capture_output=True,text=True,check=True)
        return [line[3:].strip() for line in r.stdout.splitlines() if len(line)>=4]
    except (FileNotFoundError,subprocess.CalledProcessError): return None

def cmd_drift(a):
    p=project_path(a.project); spec=project_path(a.spec); txt=spec.read_text(encoding="utf-8")
    marker="## 22. Implementation file allowlist"; block=txt.split(marker,1)[-1].split("## Approval record",1)[0] if marker in txt else ""
    allowed=[]
    for line in block.splitlines():
        line=line.strip().lstrip("-* ").strip("` ")
        if line and line not in ("TBD","- TBD") and not line.startswith("<!--"): allowed.append(line)
    changed=git_changed(p)
    if changed is None: print("Git unavailable; cannot compute drift."); sys.exit(3)
    outside=sorted(set(changed)-set(allowed)); missing=sorted(set(allowed)-set(changed))
    report={"spec":str(spec.relative_to(p)) if spec.is_relative_to(p) else str(spec),"generated_at":now(),"allowlist":allowed,"changed_files":changed,"changed_outside_allowlist":outside,"allowlisted_files_not_changed":missing,"status":"DRIFT_DETECTED" if outside else "NO_OUT_OF_SCOPE_CHANGES","note":"Git working-tree comparison only; does not prove semantic implementation conformance."}
    out=aisdf_dir(p)/"reports"/(spec.stem+"-drift.json"); dump_json(out,report)
    print(json.dumps(report,indent=2)); sys.exit(1 if outside else 0)

def parser():
    ap=argparse.ArgumentParser(description="AISDF portable EGM workflow runtime"); ap.add_argument("--version",action="version",version=VERSION); sub=ap.add_subparsers(dest="cmd",required=True)
    def add(name,fn,help):
        x=sub.add_parser(name,help=help); fn(x); return x
    def project(x): x.add_argument("--project",default=".")
    x=add("init",lambda x:project(x),"initialize .aisdf workspace"); x.set_defaults(func=cmd_init)
    def challenge(x): project(x); x.add_argument("--title",required=True); x.add_argument("--id")
    add("challenge",challenge,"create WF-007 challenge artifact").set_defaults(func=cmd_challenge)
    def spec(x): project(x); x.add_argument("--title",required=True); x.add_argument("--id",required=True)
    add("spec-create",spec,"create WF-008 design spec").set_defaults(func=cmd_spec_create)
    x=add("validate-spec",lambda x:x.add_argument("--spec",required=True),"validate spec structure"); x.set_defaults(func=cmd_validate_spec)
    def review(x): project(x); x.add_argument("--spec-id",required=True)
    add("review-init",review,"create WF-009 review record").set_defaults(func=cmd_review_init)
    x=add("review-validate",lambda x:x.add_argument("--review",required=True),"validate review completeness"); x.set_defaults(func=cmd_review_validate)
    def stage(x): x.add_argument("--review",required=True); x.add_argument("--stage",required=True); x.add_argument("--status",required=True); x.add_argument("--evidence",default="")
    add("review-stage",stage,"record a review stage and its evidence").set_defaults(func=cmd_review_stage)
    def independence(x): x.add_argument("--review",required=True); x.add_argument("--status",required=True); x.add_argument("--session-id"); x.add_argument("--evidence",default="")
    add("review-independence",independence,"record independent-review isolation evidence").set_defaults(func=cmd_review_independence)
    def finding(x): project(x); x.add_argument("--id",required=True); x.add_argument("--spec-id",required=True); x.add_argument("--title",required=True); x.add_argument("--description",required=True); x.add_argument("--severity",choices=["CRITICAL","HIGH","MEDIUM","LOW","INFO"],required=True); x.add_argument("--owner",required=True)
    add("finding-add",finding,"create WF-010 review finding").set_defaults(func=cmd_finding_add)
    def resolve(x): x.add_argument("--finding",required=True); x.add_argument("--disposition",required=True); x.add_argument("--evidence",required=True)
    add("finding-resolve",resolve,"resolve a finding with evidence").set_defaults(func=cmd_finding_resolve)
    add("bootstrap",lambda x:project(x),"create deterministic WF-011 codebase inventory").set_defaults(func=cmd_bootstrap)
    def drift(x): project(x); x.add_argument("--spec",required=True)
    add("drift",drift,"generate WF-012 git drift report").set_defaults(func=cmd_drift)
    return ap
if __name__=="__main__":
    a=parser().parse_args(); a.func(a)
