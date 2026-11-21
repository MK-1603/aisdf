from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
def test_repository_validator_passes():
    result=subprocess.run([sys.executable, str(ROOT/'tools/validate_repository.py')],cwd=ROOT,capture_output=True,text=True)
    assert result.returncode == 0, result.stdout + result.stderr
def test_engine_contracts_are_specific():
    engines=list((ROOT/'engines').glob('E-*.md'))
    assert len(engines)==56
    assert all('## Engine-specific execution contract' in p.read_text(encoding='utf-8') for p in engines)
