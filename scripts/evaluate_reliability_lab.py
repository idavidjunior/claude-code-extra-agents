import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT / "reliability-lab"
SCENARIOS = LAB / "scenarios"
RESULTS = LAB / "results"
REPORTS = LAB / "reports"
RUBRIC = LAB / "rubric.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def contains_any(text: str, terms):
    t = text.lower()
    return any(term.lower() in t for term in terms)


def evaluate():
    rubric = read_json(RUBRIC)
    scenarios = [read_json(p) for p in sorted(SCENARIOS.glob("*.json"))]

    rows = []
    for sc in scenarios:
        out_file = RESULTS / f"{sc['id']}.md"
        if not out_file.exists():
            rows.append({
                "scenario": sc["id"],
                "agent": sc["agent"],
                "status": "missing_result",
                "score": 0,
                "details": ["missing output file"],
            })
            continue

        text = out_file.read_text(encoding="utf-8").lower()
        details = []
        score = 0.0

        # must include
        must_ok = 0
        for term in sc.get("must_include", []):
            if term.lower() in text:
                must_ok += 1
            else:
                details.append(f"missing must_include: {term}")

        must_ratio = must_ok / max(len(sc.get("must_include", [])), 1)

        # forbidden penalties
        forbidden_hits = 0
        for term in sc.get("forbidden", []):
            if term.lower() in text:
                forbidden_hits += 1
                details.append(f"forbidden found: {term}")

        # dimensions
        dim_score = 0.0
        for dim in rubric["dimensions"]:
            reqs = dim.get("required_sections", [])
            hit = 0
            for r in reqs:
                if r.lower() in text:
                    hit += 1
                else:
                    details.append(f"missing section marker ({dim['id']}): {r}")
            ratio = hit / max(len(reqs), 1)
            dim_score += ratio * float(dim["weight"])

        score = (0.6 * must_ratio + 0.4 * dim_score) * 100.0
        score -= forbidden_hits * 10.0
        score = max(0.0, min(100.0, score))

        rows.append({
            "scenario": sc["id"],
            "agent": sc["agent"],
            "status": "ok",
            "score": round(score, 2),
            "details": details,
        })

    valid_scores = [r["score"] for r in rows if r["status"] == "ok"]
    overall = round(sum(valid_scores) / max(len(valid_scores), 1), 2)

    scorecard = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scenarios_total": len(rows),
        "scenarios_with_results": len(valid_scores),
        "overall_score": overall,
        "rows": rows,
    }

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "scorecard.json").write_text(json.dumps(scorecard, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# Reliability Scorecard",
        "",
        f"- Generated at: {scorecard['generated_at']}",
        f"- Scenarios total: {scorecard['scenarios_total']}",
        f"- Scenarios with results: {scorecard['scenarios_with_results']}",
        f"- Overall score: {scorecard['overall_score']}",
        "",
        "| Scenario | Agent | Status | Score |",
        "|---|---|---|---:|",
    ]
    for r in rows:
        md.append(f"| {r['scenario']} | {r['agent']} | {r['status']} | {r['score']} |")

    (REPORTS / "scorecard.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    lb_path = REPORTS / "leaderboard.json"
    leaderboard = []
    if lb_path.exists():
        leaderboard = read_json(lb_path)

    version = "dev"
    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    if plugin_path.exists():
        try:
            version = read_json(plugin_path).get("version", "dev")
        except Exception:
            version = "dev"

    leaderboard.append({
        "version": version,
        "generated_at": scorecard["generated_at"],
        "overall_score": overall,
        "scenarios_with_results": scorecard["scenarios_with_results"],
    })

    # keep latest unique by (version, generated_at)
    seen = set()
    compact = []
    for item in reversed(leaderboard):
        key = (item.get("version"), item.get("generated_at"))
        if key in seen:
            continue
        seen.add(key)
        compact.append(item)
    compact = list(reversed(compact))

    lb_path.write_text(json.dumps(compact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Reliability lab evaluated. Overall score: {overall}")


if __name__ == "__main__":
    evaluate()
