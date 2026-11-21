"""Deterministic local AISDF workforce control-plane reference runtime."""
from __future__ import annotations
import argparse, json, sqlite3, hashlib, uuid, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict, deque

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "workforce" / "registry" / "workers"
SENSITIVE_ACTIONS = {"write", "execute", "external_access", "destructive_change", "release", "deploy", "security_test"}
TRANSITIONS = {"DRAFT": {"PLANNED", "CANCELLED"}, "PLANNED": {"APPROVED", "BLOCKED", "CANCELLED"}, "APPROVED": {"READY", "BLOCKED", "CANCELLED"}, "READY": {"RUNNING", "BLOCKED", "CANCELLED"}, "RUNNING": {"SUCCEEDED", "FAILED", "BLOCKED", "CANCELLED"}, "FAILED": {"READY", "CANCELLED"}, "BLOCKED": {"READY", "CANCELLED"}, "SUCCEEDED": set(), "CANCELLED": set()}

def utc(): return datetime.now(timezone.utc).isoformat()
def digest(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def load_workers():
    workers={}
    for p in sorted(REGISTRY.glob("*.json")):
        data=json.loads(p.read_text(encoding="utf-8"))
        if data.get("worker_id") in workers: raise ValueError(f"duplicate worker_id: {data['worker_id']}")
        workers[data["worker_id"]]=data
    return workers

def topo(tasks):
    ids={t["task_id"] for t in tasks}
    if len(ids)!=len(tasks): raise ValueError("duplicate task_id")
    indeg={i:0 for i in ids}; edges=defaultdict(list)
    for t in tasks:
        for dep in t.get("depends_on",[]):
            if dep not in ids: raise ValueError(f"{t['task_id']}: unknown dependency {dep}")
            edges[dep].append(t["task_id"]); indeg[t["task_id"]]+=1
    q=deque(sorted(i for i,d in indeg.items() if d==0)); order=[]
    while q:
        n=q.popleft(); order.append(n)
        for nxt in sorted(edges[n]):
            indeg[nxt]-=1
            if indeg[nxt]==0: q.append(nxt)
    if len(order)!=len(ids): raise ValueError("task dependency cycle detected")
    return order

class Ledger:
    def __init__(self, project):
        base=Path(project).resolve(); base.mkdir(parents=True,exist_ok=True)
        self.db=base/".aisdf"/"workforce.sqlite3"; self.db.parent.mkdir(parents=True,exist_ok=True)
        self.conn=sqlite3.connect(self.db); self.conn.row_factory=sqlite3.Row
        self.conn.executescript("""CREATE TABLE IF NOT EXISTS tasks(task_id TEXT PRIMARY KEY, project_id TEXT NOT NULL, title TEXT NOT NULL, worker_id TEXT NOT NULL, status TEXT NOT NULL, action TEXT NOT NULL, budget_usd REAL NOT NULL, estimated_cost_usd REAL NOT NULL, depends_on TEXT NOT NULL, approval_digest TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL); CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY, task_id TEXT, event_type TEXT NOT NULL, actor TEXT NOT NULL, payload TEXT NOT NULL, created_at TEXT NOT NULL);""")
    def event(self, task_id, kind, actor, payload):
        self.conn.execute('INSERT INTO events VALUES(?,?,?,?,?,?)',(str(uuid.uuid4()),task_id,kind,actor,json.dumps(payload,sort_keys=True),utc())); self.conn.commit()
    def close(self): self.conn.close()

def init_project(a):
    p=Path(a.project).resolve(); p.mkdir(parents=True,exist_ok=True); (p/'.aisdf').mkdir(exist_ok=True)
    for name,src in [('PROJECT.md',ROOT/'templates/PROJECT.template.md'),('AGENTS.md',ROOT/'templates/AGENTS.template.md')]:
        target=p/name
        if target.exists(): print(f"PRESERVED: {target}")
        else: target.write_text(src.read_text(encoding='utf-8').replace('{{PROJECT_NAME}}',a.name),encoding='utf-8'); print(f"CREATED: {target}")
    print(f"READY: {p}")

def list_workers(a):
    for wid,w in load_workers().items(): print(f"{wid:38} {w['team']:22} {w['maturity']:16} {w['display_name']}")
    print(f"TOTAL: {len(load_workers())} worker contracts")

def plan(a):
    project=Path(a.project).resolve(); tasks=json.loads(Path(a.tasks).read_text(encoding='utf-8'))
    if not isinstance(tasks,list) or not tasks: raise ValueError("tasks file must contain a non-empty JSON array")
    workers=load_workers(); order=topo(tasks); planned=[]
    for t in tasks:
        for field in ('task_id','title','worker_id','action','acceptance_criteria'):
            if not t.get(field): raise ValueError(f"task missing required field: {field}")
        if t['worker_id'] not in workers: raise ValueError(f"unknown worker: {t['worker_id']}")
        w=workers[t['worker_id']]
        if t['action'] not in w['allowed_actions'] and t['action'] not in w['approval_required_for']:
            raise PermissionError(f"worker {t['worker_id']} is not permitted to request action {t['action']}")
        est=float(t.get('estimated_cost_usd',0)); budget=float(t.get('budget_usd',0))
        if est<0 or budget<0 or est>budget: raise ValueError(f"{t['task_id']}: invalid or exceeded task budget")
        if t['action'] in SENSITIVE_ACTIONS and not t.get('human_approval_required',True): raise PermissionError(f"{t['task_id']}: sensitive action cannot disable human approval")
        planned.append({**t,'status':'PLANNED','approval_digest':digest(t)})
    ledger=Ledger(project)
    try:
        for t in planned:
            ledger.conn.execute('INSERT OR REPLACE INTO tasks VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(t['task_id'],a.project_id,t['title'],t['worker_id'],'PLANNED',t['action'],float(t.get('budget_usd',0)),float(t.get('estimated_cost_usd',0)),json.dumps(t.get('depends_on',[])),t['approval_digest'],utc(),utc()))
            ledger.event(t['task_id'],'TASK_PLANNED','aisdf-runtime',{'worker_id':t['worker_id'],'action':t['action'],'approval_digest':t['approval_digest']})
        ledger.conn.commit()
    finally: ledger.close()
    report={'project':str(project),'project_id':a.project_id,'task_order':order,'tasks':planned,'plan_digest':digest(planned),'note':'Planning only. No worker/model/tool was executed. Human approval is required before sensitive actions.'}
    out=project/'.aisdf'/'workforce-plan.json'; out.write_text(json.dumps(report,indent=2),encoding='utf-8'); print(f"PLAN_CREATED: {out}\nTASKS: {len(planned)}\nORDER: {' -> '.join(order)}\nDIGEST: {report['plan_digest']}\nEXECUTION: NOT_RUN")

def approve(a):
    p=Path(a.project).resolve(); ledger=Ledger(p)
    try:
        row=ledger.conn.execute('SELECT * FROM tasks WHERE task_id=?',(a.task_id,)).fetchone()
        if not row: raise ValueError('unknown task_id')
        if row['status']!='PLANNED': raise ValueError('only PLANNED tasks can be approved')
        if not a.approver.strip(): raise ValueError('approver is required')
        ledger.conn.execute("UPDATE tasks SET status='APPROVED',updated_at=? WHERE task_id=?",(utc(),a.task_id)); ledger.event(a.task_id,'HUMAN_APPROVED',a.approver,{'approval_digest':row['approval_digest'],'reason':a.reason}); ledger.conn.commit()
        print(f"APPROVED: {a.task_id}\nAPPROVER: {a.approver}\nDIGEST: {row['approval_digest']}")
    finally: ledger.close()

def transition(a):
    p=Path(a.project).resolve(); ledger=Ledger(p)
    try:
        row=ledger.conn.execute('SELECT * FROM tasks WHERE task_id=?',(a.task_id,)).fetchone()
        if not row: raise ValueError('unknown task_id')
        target=a.to.upper()
        if target not in TRANSITIONS.get(row['status'],set()): raise ValueError(f"invalid transition {row['status']} -> {target}")
        if target=='READY' and row['status'] not in ('APPROVED','FAILED','BLOCKED'): raise ValueError('task must be approved or recoverable before READY')
        if target=='RUNNING': raise ValueError('direct RUNNING transition is disabled: use a configured execution adapter; no adapter is bundled')
        ledger.conn.execute('UPDATE tasks SET status=?,updated_at=? WHERE task_id=?',(target,utc(),a.task_id)); ledger.event(a.task_id,'STATUS_CHANGED',a.actor,{'from':row['status'],'to':target,'note':a.note}); ledger.conn.commit(); print(f"STATUS: {a.task_id} {row['status']} -> {target}")
    finally: ledger.close()

def status(a):
    p=Path(a.project).resolve(); ledger=Ledger(p)
    try:
        for r in ledger.conn.execute('SELECT task_id,title,worker_id,status,action,budget_usd,estimated_cost_usd FROM tasks ORDER BY created_at,task_id'):
            print(f"{r['task_id']:16} {r['status']:10} {r['worker_id']:34} {r['action']:18} {r['title']}")
        print('AUDIT EVENTS:',ledger.conn.execute('SELECT COUNT(*) FROM events').fetchone()[0])
    finally: ledger.close()

def main():
    ap=argparse.ArgumentParser(description='AISDF v4 local workforce control-plane reference runtime'); sp=ap.add_subparsers(dest='cmd',required=True)
    x=sp.add_parser('init'); x.add_argument('--project',required=True); x.add_argument('--name',required=True); x.set_defaults(fn=init_project)
    x=sp.add_parser('workers'); x.set_defaults(fn=list_workers)
    x=sp.add_parser('plan'); x.add_argument('--project',required=True); x.add_argument('--tasks',required=True); x.add_argument('--project-id',default='LOCAL-PROJECT'); x.set_defaults(fn=plan)
    x=sp.add_parser('approve'); x.add_argument('--project',required=True); x.add_argument('--task-id',required=True); x.add_argument('--approver',required=True); x.add_argument('--reason',default='Human approval'); x.set_defaults(fn=approve)
    x=sp.add_parser('transition'); x.add_argument('--project',required=True); x.add_argument('--task-id',required=True); x.add_argument('--to',required=True); x.add_argument('--actor',default='human'); x.add_argument('--note',default=''); x.set_defaults(fn=transition)
    x=sp.add_parser('status'); x.add_argument('--project',required=True); x.set_defaults(fn=status)
    a=ap.parse_args()
    try: a.fn(a)
    except Exception as e: print(f"ERROR: {e}",file=sys.stderr); raise SystemExit(1)
if __name__=='__main__': main()
