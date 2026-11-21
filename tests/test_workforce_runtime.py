import json, tempfile, unittest
from pathlib import Path
from runtime.aisdf_runtime.workforce import load_workers, topo, Ledger, TRANSITIONS

class WorkforceTests(unittest.TestCase):
    def test_worker_registry_has_many_roles(self):
        workers=load_workers(); self.assertGreaterEqual(len(workers),40); self.assertIn('security-lead',workers); self.assertIn('frontend-engineer',workers); self.assertIn('database-engineer',workers)
    def test_dependency_order(self):
        tasks=[{'task_id':'B','depends_on':['A']},{'task_id':'A','depends_on':[]}]
        order=topo(tasks); self.assertLess(order.index('A'),order.index('B'))
    def test_missing_dependency_rejected(self):
        with self.assertRaises(ValueError): topo([{'task_id':'A','depends_on':['X']}])
    def test_cycle_rejected(self):
        with self.assertRaises(ValueError): topo([{'task_id':'A','depends_on':['B']},{'task_id':'B','depends_on':['A']}])
    def test_state_machine_blocks_self_run_from_approved_without_ready(self):
        self.assertNotIn('RUNNING',TRANSITIONS['APPROVED'])
    def test_ledger_persists_events(self):
        with tempfile.TemporaryDirectory() as d:
            l=Ledger(d); l.event('T1','TEST','unit-test',{'ok':True}); n=l.conn.execute('select count(*) from events').fetchone()[0]; l.close(); self.assertEqual(n,1)

if __name__=='__main__': unittest.main()
