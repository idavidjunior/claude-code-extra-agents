import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

manifest = ROOT / "core-spec" / "manifest.json"
if not manifest.exists():
    raise SystemExit("Missing core-spec/manifest.json. Run build_core_and_targets.py first.")

m = json.loads(manifest.read_text(encoding="utf-8"))
ac = m["counts"]["agents"]
sc = m["counts"]["skills"]

required = [
    ROOT / "dist" / "claude-code" / "manifest.json",
    ROOT / "dist" / "ollama" / "README.md",
    ROOT / "dist" / "openwebui" / "agents",
    ROOT / "dist" / "continue" / "prompts",
]

for p in required:
    if not p.exists():
        raise SystemExit(f"Missing generated target: {p}")

print(f"Core spec validated: {ac} agents, {sc} skills.")
