import json
import unittest
from pathlib import Path
from runtime.aisdf_runtime.workforce import load_workers, topo

ROOT = Path(__file__).resolve().parents[1]

class WorkforceRegistryTests(unittest.TestCase):
    def test_all_worker_manifests_are_unique_and_have_role_contracts(self):
        workers = load_workers()
        self.assertEqual(len(workers), 72)
        for worker_id, manifest in workers.items():
            self.assertEqual(worker_id, manifest['worker_id'])
            self.assertEqual(manifest['maturity'], 'L1_DEFINED')
            role_files = list((ROOT / 'workforce' / 'teams').glob(f'*/roles/{worker_id.upper()}.md'))
            self.assertEqual(len(role_files), 1, worker_id)
            self.assertTrue(manifest['mission'])
            self.assertIn('observe', manifest['allowed_actions'])

    def test_penetration_testing_is_explicitly_gated(self):
        worker = load_workers()['penetration-tester']
        self.assertIn('security_test', worker['approval_required_for'])
        self.assertIn('external_access', worker['approval_required_for'])

    def test_deploy_is_only_gated_for_release_role(self):
        workers = load_workers()
        self.assertIn('deploy', workers['release-engineer']['approval_required_for'])
        self.assertNotIn('deploy', workers['frontend-engineer']['approval_required_for'])

    def test_all_team_registry_ids_exist(self):
        teams = json.loads((ROOT / 'workforce/registry/teams.json').read_text())['teams']
        all_ids = {wid for members in teams.values() for wid in members}
        self.assertEqual(all_ids, set(load_workers()))

if __name__ == '__main__':
    unittest.main()
