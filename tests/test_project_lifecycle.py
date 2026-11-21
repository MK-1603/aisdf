import subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CLI=ROOT/'tools'/'aisdf_runtime'/'project.py'
class ProjectLifecycleTests(unittest.TestCase):
    def run_cli(self,*args,ok=True):
        r=subprocess.run([sys.executable,str(CLI),*map(str,args)],capture_output=True,text=True)
        if ok: self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        else: self.assertNotEqual(r.returncode,0,r.stdout+r.stderr)
        return r
    def test_init_assess_plan_and_prompt_gate(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td); (p/'src').mkdir(); (p/'src'/'main.py').write_text('print("hi")')
            self.run_cli('init','--project',p,'--name','Demo','--add-agents')
            self.assertTrue((p/'PROJECT.md').exists()); self.assertTrue((p/'AGENTS.md').exists())
            self.run_cli('assess','--project',p)
            self.assertTrue((p/'.aisdf'/'assessment'/'EXISTING-PROJECT-ASSESSMENT.md').exists())
            self.run_cli('plan-create','--project',p,'--id','P1','--title','Improve demo')
            plan=p/'.aisdf'/'plans'/'IMPLEMENTATION-PLAN-P1.md'
            self.run_cli('prompt-create','--project',p,'--plan',plan.relative_to(p),ok=False)
            t=plan.read_text().replace('- TBD\n\n## 6. Data/API/migration impact','- `src/main.py`\n\n## 6. Data/API/migration impact')
            plan.write_text(t)
            digest=self.run_cli('plan-hash','--project',p,'--plan',plan.relative_to(p)).stdout.strip()
            t=plan.read_text().replace('- Approval status: NOT_APPROVED','- Approval status: APPROVED').replace('- Approved by: NOT_SET','- Approved by: Human Owner').replace('- Approval date: NOT_SET','- Approval date: 2026-11-21').replace('- Approved plan revision/SHA-256: NOT_SET','- Approved plan revision/SHA-256: '+digest)
            plan.write_text(t)
            self.run_cli('prompt-create','--project',p,'--plan',plan.relative_to(p))
            self.assertTrue((p/'.aisdf'/'prompts'/'IMPLEMENTATION-PROMPT-P1.md').exists())
    def test_init_never_overwrites_project_file(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td); (p/'PROJECT.md').write_text('owned content')
            self.run_cli('init','--project',p,ok=False)
            self.assertEqual((p/'PROJECT.md').read_text(),'owned content')
if __name__=='__main__': unittest.main()
