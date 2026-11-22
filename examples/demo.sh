#!/usr/bin/env bash
# Real end-to-end demonstration of the AISDF 1.0 control plane. Output is unedited.
# Usage: bash examples/demo.sh   (writes a throwaway project under a temp dir)
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
P="$(mktemp -d)/demo-project"
A() { echo "\$ python aisdf.py $*"; python3 "$ROOT/aisdf.py" "$@" 2>&1; echo "[exit $?]"; echo; }
say() { echo; echo "## $*"; echo; }

cat > "$P.tasks.json" <<'JSON'
[
 {"task_id":"DESIGN","title":"Design the API","worker_id":"api-architect","action":"propose","acceptance_criteria":["Design reviewed"]},
 {"task_id":"BUILD","title":"Build the API","worker_id":"api-engineer","action":"write","acceptance_criteria":["Tests pass"],"depends_on":["DESIGN"]},
 {"task_id":"TEST","title":"Run the test command","worker_id":"devops-engineer","action":"execute","command":["python3","-c","print('15 tests passed'); print('api_key=sk-ABCDEFGHIJKLMNOPQRSTUV')"],"timeout_s":20,"acceptance_criteria":["Exit code 0"]}
]
JSON

say "1. Initialise a project and register the first human approver"
A init --project "$P" --name "Demo" --owner "Mk" --non-interactive
A plan --project "$P" --tasks "$P.tasks.json"

say "2. An AI-named approver is refused; a registered human can approve"
A approve --project "$P" --task-id BUILD --approver claude --non-interactive
A approve --project "$P" --task-id BUILD --approver Mk --non-interactive

say "3. BUILD cannot start before DESIGN has succeeded"
A transition --project "$P" --task-id BUILD --to READY

say "4. Success cannot be declared without evidence"
A approve --project "$P" --task-id DESIGN --approver Mk --non-interactive
A transition --project "$P" --task-id DESIGN --to READY
A transition --project "$P" --task-id DESIGN --to SUCCEEDED
A complete --project "$P" --task-id DESIGN --actor Mk --result SUCCEEDED --non-interactive
echo "design reviewed and accepted" > "$P.design-review.txt"
A complete --project "$P" --task-id DESIGN --actor Mk --result SUCCEEDED --evidence "$P.design-review.txt" --non-interactive
A transition --project "$P" --task-id BUILD --to READY

say "5. Changing an approved task's scope revokes its approval"
sed -i 's/"Build the API"/"Build the API and deploy to production"/' "$P.tasks.json"
A plan --project "$P" --tasks "$P.tasks.json"
A status --project "$P"

say "6. Governed execution: deny-by-default, then allow-listed, with redacted evidence"
A approve --project "$P" --task-id TEST --approver Mk --non-interactive
A transition --project "$P" --task-id TEST --to READY
A run --project "$P" --task-id TEST
python3 - "$P" <<'PY'
import json, sys
p = sys.argv[1] + "/.aisdf/policy.json"
d = json.load(open(p)); d["allowed_executables"] = ["python3"]; json.dump(d, open(p, "w"), indent=2)
print("(project owner edits .aisdf/policy.json: allowed_executables = [python3])")
PY
echo
A transition --project "$P" --task-id TEST --to READY --note "retry after owner allow-listed python3"
A run --project "$P" --task-id TEST
echo "\$ cat .aisdf/evidence/TEST/*.stdout.log   # note the redaction"
cat "$P"/.aisdf/evidence/TEST/*.stdout.log; echo

say "7. The release gate blocks until everything required is evidenced"
A gate --project "$P"

say "8. Tampering with the audit ledger is detected"
A verify-ledger --project "$P"
python3 - "$P" <<'PY'
import sqlite3, sys
c = sqlite3.connect(sys.argv[1] + "/.aisdf/workforce.sqlite3")
c.execute("update events set actor='someone-else' where event_type='HUMAN_APPROVED' and rowid=(select min(rowid) from events where event_type='HUMAN_APPROVED')")
c.commit()
print("(an attacker edits one approval event directly in the database)")
PY
echo
A verify-ledger --project "$P"
