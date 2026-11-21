"""End-to-end smoke test for the portable WF-007–WF-012 CLI."""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CLI = REPO / "tools" / "aisdf_runtime" / "aisdf.py"


def run(project: Path, *args: str, expected: int = 0):
    result = subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=project,
        text=True,
        capture_output=True,
    )
    assert result.returncode == expected, result.stdout + result.stderr
    return result


def test_complete_wf007_to_wf012_artifact_lifecycle(tmp_path: Path):
    # Create a small Git project so WF-012 can inspect real working-tree changes.
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "aisdf-test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "AISDF Test"], cwd=tmp_path, check=True)
    source = tmp_path / "src" / "app.py"
    source.parent.mkdir()
    source.write_text('print("baseline")\n', encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "baseline"], cwd=tmp_path, check=True)

    run(tmp_path, "init", "--project", str(tmp_path))
    run(tmp_path, "challenge", "--project", str(tmp_path), "--title", "Test capability")
    run(tmp_path, "spec-create", "--project", str(tmp_path), "--title", "Test capability", "--id", "SPEC-001")

    spec_path = tmp_path / ".aisdf" / "specs" / "SPEC-001.md"
    spec_text = spec_path.read_text(encoding="utf-8")
    spec_text = spec_text.replace(
        "## 22. Implementation file allowlist\n\n- TBD",
        "## 22. Implementation file allowlist\n\n- src/app.py",
    )
    spec_path.write_text(spec_text, encoding="utf-8")
    run(tmp_path, "validate-spec", "--spec", str(spec_path))

    run(tmp_path, "review-init", "--project", str(tmp_path), "--spec-id", "SPEC-001")
    review = tmp_path / ".aisdf" / "reviews" / "SPEC-001-review.json"
    for stage in ("R1", "R2", "R3", "R4", "R5"):
        run(tmp_path, "review-stage", "--review", str(review), "--stage", stage,
            "--status", "COMPLETE", "--evidence", f"Evidence for {stage}")
    run(tmp_path, "review-independence", "--review", str(review), "--status", "NON_INDEPENDENT",
        "--evidence", "No isolated reviewer context was available")
    run(tmp_path, "review-validate", "--review", str(review))

    run(tmp_path, "finding-add", "--project", str(tmp_path), "--id", "FIND-001",
        "--spec-id", "SPEC-001", "--title", "Test finding", "--description", "A test finding",
        "--severity", "LOW", "--owner", "maintainer")
    finding = tmp_path / ".aisdf" / "findings" / "FIND-001.json"
    run(tmp_path, "finding-resolve", "--finding", str(finding), "--disposition", "FIXED",
        "--evidence", "Correction verified by test")
    run(tmp_path, "bootstrap", "--project", str(tmp_path))

    # Commit generated control artifacts so the next drift report isolates source changes.
    subprocess.run(["git", "add", ".aisdf"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "record AISDF artifacts"], cwd=tmp_path, check=True)
    source.write_text('print("changed")\n', encoding="utf-8")
    run(tmp_path, "drift", "--project", str(tmp_path), "--spec", str(spec_path))

    drift = json.loads((tmp_path / ".aisdf" / "reports" / "SPEC-001-drift.json").read_text())
    assert drift["changed_files"] == ["src/app.py"]
    assert drift["changed_outside_allowlist"] == []
