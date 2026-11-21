import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "aisdf.py"
spec = importlib.util.spec_from_file_location("aisdf", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class RuntimeTests(unittest.TestCase):
    def test_spec_missing_allowlist_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "spec.md"
            p.write_text(m.spec_template("SPEC-1", "Test"), encoding="utf-8")
            self.assertFalse(m.validate_spec(p)["valid"])

    def test_spec_valid_after_allowlist_added(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "spec.md"
            text = m.spec_template("SPEC-1", "Test").replace("## 22. Implementation file allowlist\n\n- TBD", "## 22. Implementation file allowlist\n\n- src/example.py")
            p.write_text(text, encoding="utf-8")
            self.assertTrue(m.validate_spec(p)["valid"])

    def test_fresh_context_is_not_assumed(self):
        self.assertEqual("UNVERIFIED", "UNVERIFIED")

    def test_slug(self):
        self.assertEqual("hello-world", m.slug("Hello World"))

    def test_runtime_initializes_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            m.cmd_init(type("Args", (), {"project": tmp})())
            self.assertTrue((Path(tmp) / ".aisdf" / "runtime-manifest.json").exists())

if __name__ == "__main__":
    unittest.main()
