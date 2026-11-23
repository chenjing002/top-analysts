#!/usr/bin/env python3
"""Render rounds/round-NN.json → rounds/round-NN.md (deterministic; never hand-edit the .md).

Usage: python3 scripts/render_round.py sessions/600519.SH/2026-11-23-01/rounds/round-01.json [...]
       python3 scripts/render_round.py --all
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPERT_NAMES = {}
for p in (ROOT / "experts").glob("*.md"):
    if p.name.startswith("_"):
        continue
    first = p.read_text(encoding="utf-8").splitlines()[0]
    EXPERT_NAMES[p.stem] = first.lstrip("# ").strip()


def name(slug):
    return EXPERT_NAMES.get(slug, slug)


def render(r: dict) -> str:
    L = [f"# Round {r['round']} — {r['question']}", ""]
    L.append(f"**Session** {r['ts_code']} / {r['session_id']} · **started** {r.get('started_at','')} · **ended** {r.get('ended_at','')}")
    L.append(f"**Participants** {', '.join(name(p) for p in r.get('participants', []))}")
    if r.get("why_this_question"):
        L += ["", f"> {r['why_this_question']}"]
    for phase in ["opening", "rebuttal", "closing"]:
        sts = [s for s in r.get("statements", []) if s.get("phase") == phase]
        if not sts:
            continue
        L += ["", f"## {phase.capitalize()} statements", ""]
        for s in sts:
            L.append(f"### {name(s['expert'])} · confidence {s.get('confidence','?')} · {s.get('timestamp','')}")
            L += ["", s["text"].strip(), ""]
            if s.get("evidence"):
                L.append("**Evidence**")
                for e in s["evidence"]:
                    vals = f" — {json.dumps(e['values'], ensure_ascii=False)}" if e.get("values") else ""
                    L.append(f"- {e['claim']} _(source: {e['source']})_{vals}")
                L.append("")
            if s.get("challenges"):
                L.append("**Challenges**")
                for c in s["challenges"]:
                    L.append(f"- → {name(c['to'])}: {c['point']}")
                L.append("")
            if s.get("concessions"):
                L.append("**Concessions**")
                for c in s["concessions"]:
                    L.append(f"- ← {name(c['to'])}: {c['point']}")
                L.append("")
            if s.get("thinker_used"):
                t = s["thinker_used"]
                L.append(f"_[reasoning method, not evidence — {t.get('thinker')} · {t.get('method')}]_")
                L.append("")
    if r.get("disagreements"):
        L += ["## Disagreements", ""]
        for d in r["disagreements"]:
            L.append(f"- **{d['topic']}** — {d.get('status','open')}")
            for who, pos in d.get("positions", {}).items():
                L.append(f"  - {name(who)}: {pos}")
            if d.get("resolution"):
                L.append(f"  - _resolution_: {d['resolution']}")
        L.append("")
    c = r.get("conclusion", {})
    L += ["## Conclusion", "", f"**Answer ({c.get('confidence','?')} confidence):** {c.get('answer','')}", ""]
    if c.get("what_would_change_our_mind"):
        L.append("**What would change our mind**")
        L += [f"- {x}" for x in c["what_would_change_our_mind"]] + [""]
    if c.get("open_questions"):
        L.append("**Open questions**")
        L += [f"- {x}" for x in c["open_questions"]] + [""]
    if r.get("thinkers_consulted"):
        L += ["## Thinkers consulted (reasoning methods, not evidence)", ""]
        L += [f"- {t['thinker']} · {t['method']} — {t['used_for']}" for t in r["thinkers_consulted"]] + [""]
    if r.get("next_question_candidates"):
        L += ["## Candidate questions for the next round", ""]
        L += [f"- {q}" for q in r["next_question_candidates"]] + [""]
    if r.get("knowledge_candidates"):
        L += ["## Knowledge candidates (to be validated before entering knowledge/)", ""]
        L += [f"- [{k['kind']}, {k.get('confidence','?')}] {k['text']} _(source: {k.get('source','')})_" for k in r["knowledge_candidates"]] + [""]
    return "\n".join(L)


def main(argv):
    if "--all" in argv:
        files = sorted((ROOT / "sessions").glob("*/*/rounds/round-*.json"))
    else:
        files = [Path(a) for a in argv if a.endswith(".json")]
    for f in files:
        r = json.loads(f.read_text(encoding="utf-8"))
        out = f.with_suffix(".md")
        out.write_text(render(r), encoding="utf-8")
        print(f"rendered {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
