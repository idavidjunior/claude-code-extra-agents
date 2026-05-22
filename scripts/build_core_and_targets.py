import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
SKILLS_DIR = ROOT / "skills"
CORE_AGENTS = ROOT / "core-spec" / "agents"
CORE_SKILLS = ROOT / "core-spec" / "skills"
DIST = ROOT / "dist"


def read_text(path: Path) -> str:
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def parse_frontmatter(md: str):
    if not md.startswith("---"):
        return {}, md

    end = md.find("\n---", 3)
    if end == -1:
        return {}, md

    raw = md[3:end].strip("\n")
    body = md[end + 4 :].lstrip("\n")

    data = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue

        key, val = line.split(":", 1)
        key = key.strip()
        val = val.rstrip()

        if val.strip() == "|":
            i += 1
            block = []
            while i < len(lines):
                nxt = lines[i]
                if nxt.startswith("  "):
                    block.append(nxt[2:])
                    i += 1
                elif not nxt.strip():
                    block.append("")
                    i += 1
                else:
                    break
            data[key] = "\n".join(block).strip()
            continue

        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            parts = [p.strip() for p in val[1:-1].split(",") if p.strip()]
            data[key] = [p.strip('"\'') for p in parts]
        else:
            data[key] = val.strip('"\'')
        i += 1

    return data, body


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.strip().startswith("#"):
            return line.strip().lstrip("#").strip()
    return fallback


def as_yaml_scalar(value):
    if isinstance(value, list):
        return "[" + ", ".join(value) + "]"
    if isinstance(value, str):
        if any(ch in value for ch in [":", "#", "[", "]", "{", "}", "\n"]):
            return json.dumps(value, ensure_ascii=False)
        return value
    return str(value)


def dump_yaml(doc: dict) -> str:
    lines = []
    for key, value in doc.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            for sk, sv in value.items():
                lines.append(f"  {sk}: {as_yaml_scalar(sv)}")
        else:
            lines.append(f"{key}: {as_yaml_scalar(value)}")
    return "\n".join(lines) + "\n"


def normalize_name(name: str) -> str:
    return re.sub(r"[^a-z0-9\-]+", "-", name.lower()).strip("-")


def build_core_specs():
    agents = []
    skills = []

    for path in sorted(AGENTS_DIR.glob("*.md")):
        raw = read_text(path)
        fm, body = parse_frontmatter(raw)
        name = normalize_name(fm.get("name", path.stem))
        description = fm.get("description", "").strip() or first_heading(body, name)
        version = str(fm.get("version", "1.0.0"))
        allowed = fm.get("allowed-tools", [])
        if isinstance(allowed, str):
            allowed = [x.strip() for x in allowed.split(",") if x.strip()]

        agent_doc = {
            "id": name,
            "kind": "agent",
            "version": version,
            "source": str(path.relative_to(ROOT)).replace("\\", "/"),
            "title": first_heading(body, name),
            "description": description,
            "allowed_tools": allowed,
            "platforms": ["claude-code", "ollama", "openwebui", "continue"],
        }
        write_text(CORE_AGENTS / f"{name}.agent.yaml", dump_yaml(agent_doc))
        agents.append(agent_doc)

    for path in sorted(SKILLS_DIR.glob("*/skill.md")):
        raw = read_text(path)
        fm, body = parse_frontmatter(raw)
        name = normalize_name(fm.get("name", path.parent.name))
        description = fm.get("description", "").strip() or first_heading(body, name)
        version = str(fm.get("version", "1.0.0"))
        allowed = fm.get("allowed-tools", [])
        if isinstance(allowed, str):
            allowed = [x.strip() for x in allowed.split(",") if x.strip()]

        skill_doc = {
            "id": name,
            "kind": "skill",
            "version": version,
            "source": str(path.relative_to(ROOT)).replace("\\", "/"),
            "title": first_heading(body, name),
            "description": description,
            "allowed_tools": allowed,
            "platforms": ["claude-code", "ollama", "openwebui", "continue"],
        }
        write_text(CORE_SKILLS / f"{name}.skill.yaml", dump_yaml(skill_doc))
        skills.append(skill_doc)

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": {"agents": len(agents), "skills": len(skills)},
        "agents": [a["id"] for a in agents],
        "skills": [s["id"] for s in skills],
    }
    write_text(ROOT / "core-spec" / "manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    return agents, skills


def generate_claude_code(agents, skills):
    payload = {
        "platform": "claude-code",
        "agents": [a["id"] for a in agents],
        "skills": [s["id"] for s in skills],
        "notes": "Uses native markdown agent/skill files from source folders.",
    }
    write_text(DIST / "claude-code" / "manifest.json", json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def generate_ollama(agents):
    out = DIST / "ollama" / "modelfiles"
    for a in agents:
        modelfile = (
            "FROM llama3\n"
            f"SYSTEM You are the '{a['id']}' specialist from claude-code-extra-agents. "
            f"Purpose: {a['description']}\n"
            "PARAMETER temperature 0.2\n"
        )
        write_text(out / f"{a['id']}.Modelfile", modelfile)

    readme = """# Ollama Export

Generated Modelfiles for each agent.

## Build example
```bash
ollama create agent-debug-forensic -f dist/ollama/modelfiles/debug-forensic.Modelfile
```
"""
    write_text(DIST / "ollama" / "README.md", readme)


def generate_openwebui(agents):
    out = DIST / "openwebui" / "agents"
    for a in agents:
        obj = {
            "id": a["id"],
            "name": a["title"],
            "description": a["description"],
            "system_prompt": f"You are {a['id']}. Focus on: {a['description']}",
            "source": a["source"],
        }
        write_text(out / f"{a['id']}.json", json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def generate_continue(agents):
    out = DIST / "continue" / "prompts"
    for a in agents:
        prompt = (
            f"# {a['id']}\n\n"
            f"Purpose: {a['description']}\n\n"
            "Use this prompt in Continue/Cline as a role preset.\n"
        )
        write_text(out / f"{a['id']}.prompt.md", prompt)


def main():
    agents, skills = build_core_specs()
    generate_claude_code(agents, skills)
    generate_ollama(agents)
    generate_openwebui(agents)
    generate_continue(agents)
    print(f"Generated core spec and exports: {len(agents)} agents, {len(skills)} skills.")


if __name__ == "__main__":
    main()

