#!/usr/bin/env python3
"""Structural validation gate. Run before committing; the sync script refuses to push if this fails.

Checks
  experts/*.md        all 9 template sections present; version in header matches last changelog entry;
                      source-anchors section non-trivial; no unresolved TODO/FIXME
  Thinkers/*.md       sections 1–4 present
  knowledge/**        every entry line has an id, date, confidence and source; ids unique;
                      hypotheses never carry confidence "high"
  sessions/**/round-*.json  required keys; every evidence item has a source; statements have expert in
                      participants; participants exist in experts/
  observer/proposals/*.md   status is one of proposed|validated|applied|rejected; applied proposals
                      reference a validation note

Usage: python3 scripts/validate.py [--quiet]
Exit code 1 on any error.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERR, WARN = [], []

EXPERT_SECTIONS = [
    "## 1. Identity and scope", "## 2. Core questions", "## 3. Method", "## 4. Evidence standards",
    "## 5. Characteristic moves in debate", "## 6. Known blind spots", "## 7. Vocabulary and formulas",
    "## 8. Source anchors", "## 9. Changelog",
]
THINKER_SECTIONS = ["## 1. When to consult", "## 2. Methods", "## 3. Anti-patterns", "Source anchors"]
KB_LINE = re.compile(
    r"^- \[(?P<id>[A-Z]+-[A-Za-z0-9.]+-\d{3})\] \((?P<date>\d{4}-\d{2}-\d{2}), confidence: (?P<conf>high|medium|low), source: (?P<src>[^)]+)\) (?P<text>.+)$"
)


def err(m):
    ERR.append(m)


def warn(m):
    WARN.append(m)


def check_experts():
    slugs = set()
    for p in sorted((ROOT / "experts").glob("*.md")):
        if p.name.startswith("_"):
            continue
        slugs.add(p.stem)
        t = p.read_text(encoding="utf-8")
        for s in EXPERT_SECTIONS:
            if s not in t:
                err(f"{p.name}: missing section '{s}'")
        m = re.search(r"\*\*Version:\*\*\s*([\d.]+)", t)
        if not m:
            err(f"{p.name}: no **Version:** in header")
        else:
            v = m.group(1)
            chlog = t.split("## 9. Changelog")[-1] if "## 9. Changelog" in t else ""
            versions = re.findall(r"^- ([\d.]+) \(", chlog, flags=re.M)
            if not versions:
                err(f"{p.name}: changelog has no entries")
            elif versions[-1] != v:
                err(f"{p.name}: header version {v} != last changelog entry {versions[-1]}")
        if "## 8. Source anchors" in t:
            anchors = t.split("## 8. Source anchors")[1].split("## 9.")[0]
            if len([l for l in anchors.splitlines() if l.strip().startswith(("-", "|"))]) < 8:
                err(f"{p.name}: fewer than 8 source anchors")
        if re.search(r"\b(TODO|FIXME|XXX)\b", t):
            err(f"{p.name}: unresolved TODO/FIXME")
        n = len(t.splitlines())
        if n < 100 or n > 600:
            warn(f"{p.name}: {n} lines (expected 100–600)")
    return slugs


def check_thinkers():
    for p in sorted((ROOT / "Thinkers").glob("*.md")):
        if p.name == "README.md":
            continue
        t = p.read_text(encoding="utf-8")
        for s in THINKER_SECTIONS:
            if s not in t:
                err(f"Thinkers/{p.name}: missing section '{s}'")


def check_knowledge():
    ids = {}
    for p in sorted((ROOT / "knowledge").rglob("*.md")):
        if p.name == "README.md":
            continue
        is_hyp = "hypotheses" in p.parts
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if not line.startswith("- ["):
                continue
            m = KB_LINE.match(line)
            if not m:
                err(f"{p.relative_to(ROOT)}:{i}: entry does not match '- [ID] (YYYY-MM-DD, confidence: x, source: y) text'")
                continue
            kid = m.group("id")
            if kid in ids:
                err(f"{p.relative_to(ROOT)}:{i}: duplicate id {kid} (also in {ids[kid]})")
            ids[kid] = str(p.relative_to(ROOT))
            if is_hyp and m.group("conf") == "high":
                err(f"{p.relative_to(ROOT)}:{i}: hypothesis with confidence high — verify it and move to facts/, or lower it")
            if not is_hyp and kid.startswith("H-"):
                err(f"{p.relative_to(ROOT)}:{i}: H- id outside hypotheses/")


def check_sessions(slugs):
    req = ["round", "session_id", "ts_code", "question", "participants", "statements", "conclusion"]
    for rf in sorted((ROOT / "sessions").glob("*/*/rounds/round-*.json")):
        rel = rf.relative_to(ROOT)
        try:
            r = json.loads(rf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            err(f"{rel}: invalid JSON ({e})")
            continue
        for k in req:
            if k not in r:
                err(f"{rel}: missing key '{k}'")
        for p in r.get("participants", []):
            if p not in slugs:
                err(f"{rel}: participant '{p}' has no experts/{p}.md")
        for i, s in enumerate(r.get("statements", [])):
            if s.get("expert") not in r.get("participants", []):
                err(f"{rel}: statement {i} by '{s.get('expert')}' who is not a participant")
            if s.get("phase") not in ("discussion", "opening", "rebuttal", "closing"):
                err(f"{rel}: statement {i} has phase '{s.get('phase')}'")
            for j, e in enumerate(s.get("evidence", [])):
                if not e.get("source"):
                    err(f"{rel}: statement {i} evidence {j} has no source")
            if s.get("phase") == "opening" and not s.get("evidence"):
                warn(f"{rel}: opening statement by {s.get('expert')} cites no evidence")
        if r.get("conclusion", {}).get("confidence") not in ("high", "medium", "low"):
            err(f"{rel}: conclusion.confidence must be high|medium|low")
        if not rf.with_suffix(".md").exists():
            err(f"{rel}: not rendered — run scripts/render_round.py")
        sj = rf.parent.parent / "session.json"
        if not sj.exists():
            err(f"{rel}: no session.json")


def check_proposals():
    for p in sorted((ROOT / "observer" / "proposals").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        m = re.search(r"^\*\*Status:\*\*\s*(proposed|validated|applied|rejected)", t, flags=re.M)
        if not m:
            err(f"observer/proposals/{p.name}: missing '**Status:** proposed|validated|applied|rejected'")
            continue
        if m.group(1) in ("validated", "applied") and "## Validation" not in t:
            err(f"observer/proposals/{p.name}: status {m.group(1)} but no '## Validation' section")
        if "**Target:**" not in t or "**Evidence:**" not in t:
            err(f"observer/proposals/{p.name}: needs **Target:** and **Evidence:** lines")


def main():
    quiet = "--quiet" in sys.argv
    slugs = check_experts()
    check_thinkers()
    check_knowledge()
    check_sessions(slugs)
    check_proposals()
    for w in WARN:
        print("WARN ", w)
    for e in ERR:
        print("ERROR", e)
    if not quiet or ERR:
        print(f"validate: {len(ERR)} errors, {len(WARN)} warnings")
    sys.exit(1 if ERR else 0)


if __name__ == "__main__":
    main()
