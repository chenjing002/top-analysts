#!/usr/bin/env python3
"""Build sessions/index.json for the static site.

The site loads index.json, then fetches round JSON files on demand. The index carries enough
text (questions, conclusions, participants) for client-side search without opening every round.

Usage: python3 scripts/build_index.py
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESS = ROOT / "sessions"


def expert_meta():
    out = {}
    for p in sorted((ROOT / "experts").glob("*.md")):
        if p.name.startswith("_"):
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        title = lines[0].lstrip("# ").strip()
        tagline = next((l.lstrip("> ").strip() for l in lines[1:8] if l.startswith(">")), "")
        version = ""
        for l in lines[:12]:
            if "**Version:**" in l:
                version = l.split("**Version:**")[1].split("·")[0].strip()
                break
        out[p.stem] = {"name": title, "tagline": tagline, "version": version, "file": f"experts/{p.name}"}
    return out


def main():
    companies = {}
    for sdir in sorted(SESS.glob("*/*/")):
        sj = sdir / "session.json"
        if not sj.exists():
            continue
        s = json.loads(sj.read_text(encoding="utf-8"))
        ts = s["company"]["ts_code"]
        rounds = []
        for rf in sorted((sdir / "rounds").glob("round-*.json")):
            r = json.loads(rf.read_text(encoding="utf-8"))
            rounds.append(
                {
                    "round": r["round"],
                    "question": r["question"],
                    "participants": r.get("participants", []),
                    "started_at": r.get("started_at"),
                    "ended_at": r.get("ended_at"),
                    "conclusion": r.get("conclusion", {}).get("answer", ""),
                    "confidence": r.get("conclusion", {}).get("confidence", ""),
                    "n_disagreements_open": sum(1 for d in r.get("disagreements", []) if d.get("status") == "open"),
                    "thinkers": [t.get("thinker") for t in r.get("thinkers_consulted", [])],
                    "json": str(rf.relative_to(ROOT)),
                    "md": str(rf.with_suffix(".md").relative_to(ROOT)),
                    "observer": str((sdir / "observer" / f"round-{r['round']:02d}.md").relative_to(ROOT))
                    if (sdir / "observer" / f"round-{r['round']:02d}.md").exists()
                    else None,
                }
            )
        c = companies.setdefault(ts, {"ts_code": ts, "name": s["company"]["name"], "industry": s["company"].get("industry", ""), "sessions": []})
        c["sessions"].append(
            {
                "session_id": s["session_id"],
                "started_at": s.get("started_at"),
                "status": s.get("status", "open"),
                "user_request": s.get("user_request", ""),
                "experts": s.get("experts", []),
                "factsheet": str((sdir / "data" / "factsheet.md").relative_to(ROOT)) if (sdir / "data" / "factsheet.md").exists() else None,
                "summary": str((sdir / "summary.md").relative_to(ROOT)) if (sdir / "summary.md").exists() else None,
                "rounds": rounds,
            }
        )
    index = {
        "built_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "experts": expert_meta(),
        "companies": sorted(companies.values(), key=lambda c: max((s["started_at"] or "" for s in c["sessions"]), default=""), reverse=True),
        "n_rounds": sum(len(s["rounds"]) for c in companies.values() for s in c["sessions"]),
    }
    (SESS / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"index: {len(companies)} companies, {index['n_rounds']} rounds → sessions/index.json")


if __name__ == "__main__":
    main()
