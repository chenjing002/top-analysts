#!/usr/bin/env python3
"""The improvement loop: turn each reviewed round into memory, knowledge, playbook and proposals.

  python3 scripts/improve.py ingest <round.json | session dir> [--force]   one round or a session
  python3 scripts/improve.py ingest --all [--force]                         every reviewed round
  python3 scripts/improve.py proposals                                      draft card proposals from the log
  python3 scripts/improve.py report                                         trend table (run at session start)

ingest, per round (idempotent):
  1. runs scripts/check_round.py and records errors/warnings;
  2. reads the observer note: severity counts and the `## Log` jsonl block (tags, see observer/TAGS.md);
  3. appends to observer/log.jsonl and observer/metrics.jsonl;
  4. writes knowledge candidates into knowledge/: a `fact` whose every figure the checker verified
     keeps its confidence (never above medium if it rests on a default); an unverified fact is
     demoted to a hypothesis at confidence low; methods and hypotheses go in as proposed; a
     candidate the observer logged as `drop` is withheld;
  5. promotes playbook entries: a pattern tag, or a workflow-level weakness tag, seen in two rounds.

proposals: a weakness tag on one expert in two different rounds, with no proposal yet for that
expert/tag, becomes observer/proposals/<date>-<expert>-<tag>.md at status `drafting`, evidence
filled from the log. A tag that reaches the threshold on two or more experts is a shared problem:
it goes to the playbook as a pitfall (and to the checklist) instead of to each card. The orchestrator writes the Change and Risk, sets `proposed`, and hands it to
an independent reviewer (skills/observe/SKILL.md).
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_round  # noqa: E402

LOG = ROOT / "observer" / "log.jsonl"
METRICS = ROOT / "observer" / "metrics.jsonl"
PLAYBOOK = ROOT / "knowledge" / "playbook.md"
TAGS_MD = ROOT / "observer" / "TAGS.md"
PROPOSALS = ROOT / "observer" / "proposals"
THRESHOLD = 2
FACT_CAP, METHOD_CAP = 40, 60
TODAY = date.today().isoformat()


# ---------- small io ----------

def read_jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def write_jsonl(p: Path, rows: list[dict]):
    p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def tag_table() -> dict[str, dict]:
    tags = {}
    if not TAGS_MD.exists():
        return tags
    for line in TAGS_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| `([a-z0-9-]+)` \| (.+?) \|(?: (.+?) \| (.+?) \|)?$", line)
        if m:
            tags[m.group(1)] = {"meaning": m.group(2), "target": (m.group(3) or "").strip(), "check": (m.group(4) or "").strip()}
    return tags


def observer_note(round_path: Path) -> Path:
    return round_path.parent.parent / "observer" / round_path.name.replace(".json", ".md")


def parse_observer(md: str) -> tuple[Counter, list[dict], str | None]:
    sev = Counter()
    body = md.split("## Weaknesses", 1)[1].split("\n## ", 1)[0] if "## Weaknesses" in md else ""
    for line in body.splitlines():
        m = re.search(r"\[(?:severity:\s*)?(high|medium|low|major|minor)\]", line)
        if line.lstrip().startswith("-") and m:
            sev[{"major": "high", "minor": "low"}.get(m.group(1), m.group(1))] += 1
    entries = []
    m = re.search(r"```jsonl\s*\n(.*?)```", md, re.S)
    if m:
        for l in m.group(1).splitlines():
            l = l.strip()
            if l:
                entries.append(json.loads(l))
    ts = re.search(r"·\s*(\d{4}-\d{2}-\d{2})", md)
    return sev, entries, (ts.group(1) if ts else None)


# ---------- knowledge ----------

def next_id(prefix: str, files: list[Path]) -> int:
    n = 0
    for f in files:
        if f.exists():
            for m in re.finditer(rf"\[{re.escape(prefix)}(\d{{3}})\]", f.read_text(encoding="utf-8")):
                n = max(n, int(m.group(1)))
    return n + 1


def kb_file(kind: str, ts_code: str) -> Path:
    code = ts_code.split(".")[0]
    return {"fact": ROOT / "knowledge" / "facts" / f"{code}.md",
            "hypothesis": ROOT / "knowledge" / "hypotheses" / f"{code}.md",
            "method": ROOT / "knowledge" / "methods" / "panel.md"}[kind]


def kb_header(kind: str, ts_code: str, name: str) -> str:
    title = {"fact": f"# Facts — {ts_code} {name}", "hypothesis": f"# Hypotheses — {ts_code} {name}",
             "method": "# Methods — reusable checks the panel has used"}[kind]
    return title + "\n\nOne line, one claim; see knowledge/README.md for the admission rules.\n\n"


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("(", "[").replace(")", "]")).strip()


def write_candidates(r: dict, summary: dict, drops: set[int], verified: set[int], name: str, out: list[str]):
    ts_code, sid, rn = r["ts_code"], r["session_id"], int(r["round"])
    ref = f"Session {ts_code}/{sid} r{rn}."
    status = {c["index"]: c for c in summary["candidates"]}
    for i, c in enumerate(r.get("knowledge_candidates", []) or []):
        if (i + 1) in drops:
            out.append(f"  withheld candidate {i + 1} (observer drop)")
            continue
        kind = c.get("kind")
        conf = c.get("confidence", "low")
        text = clean(c.get("text", ""))
        src = clean(c.get("source", "panel"))
        note = ""
        if kind == "fact":
            st = status.get(i, {})
            if st.get("status") != "verified" and (i + 1) not in verified:
                kind, conf = "hypothesis", "low"
                note = f" [demoted from fact: figures {st.get('unverified', [])[:3]} not verified; observer did not audit them]"
            elif conf == "high" and check_round.DEFAULT_PARAMS.search(text):
                conf = "medium"
                note = " [capped at medium: rests on a model default or an estimate]"
        if kind not in ("fact", "hypothesis", "method"):
            out.append(f"  skipped candidate {i + 1}: unknown kind {kind!r}")
            continue
        if kind == "hypothesis" and conf == "high":
            conf = "medium"
        target = kb_file(kind, ts_code)
        existing = target.read_text(encoding="utf-8") if target.exists() else ""
        if ref in existing and text[:60] in existing:
            continue
        n_entries = existing.count("\n- [")
        if (kind == "fact" and n_entries >= FACT_CAP) or (kind == "method" and n_entries >= METHOD_CAP):
            out.append(f"  cap reached for {target.relative_to(ROOT)}; consolidate before adding candidate {i + 1}")
            continue
        code = ts_code.split(".")[0]
        prefix = {"fact": f"F-{code}-", "hypothesis": f"H-{code}-", "method": "M-"}[kind]
        nid = next_id(prefix, [target] + ([kb_file("fact", ts_code), kb_file("hypothesis", ts_code)] if kind != "method" else []))
        line = f"- [{prefix}{nid:03d}] ({TODAY}, confidence: {conf}, source: {src}) {text}{note} {ref}\n"
        if not existing:
            target.parent.mkdir(parents=True, exist_ok=True)
            existing = kb_header(kind, ts_code, name)
        target.write_text(existing.rstrip("\n") + "\n" + line, encoding="utf-8")
        out.append(f"  + {prefix}{nid:03d} ({kind}, {conf}) → {target.relative_to(ROOT)}")


# ---------- playbook ----------

def promote_playbook(log: list[dict], out: list[str]):
    tags = tag_table()
    text = PLAYBOOK.read_text(encoding="utf-8") if PLAYBOOK.exists() else "# Panel playbook\n\n## Entries\n\n"
    have = set(re.findall(r"tag: ([a-z0-9-]+)", text))
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    # a weakness tag that recurs on two or more experts is a shared pitfall, whoever it was logged on
    by_tag: dict[str, set] = defaultdict(set)
    for e in log:
        if e.get("kind") == "weakness" and e.get("tag") and e.get("expert"):
            by_tag[e["tag"]].add(e["expert"])
    shared = {tag for tag, ex in by_tag.items() if len(ex) >= 2}
    for e in log:
        if e.get("kind") == "pattern" and e.get("tag"):
            groups[("pattern", e["tag"])].append(e)
        elif e.get("kind") == "weakness" and e.get("tag") and (not e.get("expert") or e["tag"] in shared):
            groups[("pitfall", e["tag"])].append(e)
    nid = next_id("P-", [PLAYBOOK])
    for (kind, tag), es in sorted(groups.items()):
        rounds = sorted({(e["session"], e["round"]) for e in es})
        if len(rounds) < THRESHOLD or tag in have:
            continue
        latest = sorted(es, key=lambda e: (e["session"], e["round"]))[-1]
        src = "; ".join(f"{s} r{r}" for s, r in rounds)
        meaning = clean(tags.get(tag, {}).get("meaning", "")) or tag
        example = clean(latest.get("note", ""))
        if kind == "pitfall":
            rule = f"Pitfall: {meaning}. Seen as: {example}"
        else:
            rule = f"{meaning} Example: {example}"
        text = text.rstrip("\n") + f"\n- [P-{nid:03d}] ({TODAY}, kind: {kind}, tag: {tag}, source: {src}) {rule}\n"
        out.append(f"  + P-{nid:03d} ({kind}: {tag}) from {src}")
        have.add(tag)
        nid += 1
    PLAYBOOK.write_text(text, encoding="utf-8")


# ---------- ingest ----------

def ingest_round(round_path: Path, force: bool, out: list[str]):
    r = json.loads(round_path.read_text(encoding="utf-8"))
    sid, rn, ts_code = r["session_id"], int(r["round"]), r["ts_code"]
    key = {"session": f"{ts_code}/{sid}", "round": rn}
    metrics = read_jsonl(METRICS)
    if any(m["session"] == key["session"] and m["round"] == rn for m in metrics) and not force:
        out.append(f"{key['session']} r{rn}: already ingested (use --force to redo)")
        return
    note_path = observer_note(round_path)
    if not note_path.exists():
        out.append(f"{key['session']} r{rn}: no observer note yet — run the Observe workflow first")
        return
    rep, summary = check_round.run(round_path)
    sev, entries, note_date = parse_observer(note_path.read_text(encoding="utf-8"))
    sess = json.loads((round_path.parent.parent / "session.json").read_text(encoding="utf-8"))
    name = sess.get("company", {}).get("name", "")
    day = note_date or (r.get("ended_at") or TODAY)[:10]
    blob = json.dumps(r, ensure_ascii=False)
    kb_cited = len(re.findall(r"\bKB [FMH]-[A-Za-z0-9.-]+|\bP-\d{3}\b", blob))
    if not entries:
        out.append(f"{key['session']} r{rn}: observer note has no ```jsonl log block; weaknesses not tagged")
    tags = tag_table()
    log = [e for e in read_jsonl(LOG) if not (e["session"] == key["session"] and e["round"] == rn)]
    drops, verified = set(), set()
    for e in entries:
        if e.get("kind") in ("drop", "verify"):
            (drops if e["kind"] == "drop" else verified).add(int(e.get("candidate", 0)))
            continue
        if e.get("tag") and tags and e["tag"] not in tags:
            out.append(f"  unknown tag {e['tag']!r} (add it to observer/TAGS.md)")
        log.append({**key, "ts_code": ts_code, "date": day, **{k: e.get(k) for k in ("kind", "severity", "expert", "tag", "ref", "note")}})
    log.sort(key=lambda e: (e["session"], e["round"]))
    write_jsonl(LOG, log)
    metrics = [m for m in metrics if not (m["session"] == key["session"] and m["round"] == rn)]
    metrics.append({**key, "ts_code": ts_code, "date": day, "check_errors": summary["errors"], "check_warnings": summary["warnings"],
                    "weak_high": sev["high"], "weak_medium": sev["medium"], "weak_low": sev["low"],
                    "kb_cited": kb_cited, "thinkers": len(r.get("thinkers_consulted") or []),
                    "candidates": len(r.get("knowledge_candidates") or [])})
    metrics.sort(key=lambda m: (m["session"], m["round"]))
    write_jsonl(METRICS, metrics)
    out.append(f"{key['session']} r{rn}: check {summary['errors']}E/{summary['warnings']}W · weaknesses {sev['high']}/{sev['medium']}/{sev['low']} · log +{len(entries) - len(drops)} · KB cited {kb_cited}")
    write_candidates(r, summary, drops, verified, name, out)
    promote_playbook(log, out)


def all_rounds() -> list[Path]:
    return sorted((ROOT / "sessions").glob("*/*/rounds/round-*.json"))


# ---------- proposals ----------

def existing_proposal_tags() -> set[str]:
    have = set()
    for p in PROPOSALS.glob("*.md"):
        m = re.search(r"^\*\*Tag:\*\*\s*([a-z0-9-]+/[a-z0-9-]+)", p.read_text(encoding="utf-8"), re.M)
        if m:
            have.add(m.group(1))
    return have


def draft_proposals(out: list[str]):
    log = read_jsonl(LOG)
    tags = tag_table()
    have = existing_proposal_tags()
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for e in log:
        if e.get("kind") == "weakness" and e.get("expert") and e.get("tag"):
            groups[(e["expert"], e["tag"])].append(e)
    experts_per_tag = Counter()
    for (expert, tag), es in groups.items():
        if len({(e["session"], e["round"]) for e in es}) >= THRESHOLD:
            experts_per_tag[tag] += 1
    for (expert, tag), es in sorted(groups.items()):
        rounds = {(e["session"], e["round"]) for e in es}
        if len(rounds) < THRESHOLD or f"{expert}/{tag}" in have:
            continue
        if experts_per_tag[tag] >= 2:
            out.append(f"  {expert}/{tag}: tag recurs on {experts_per_tag[tag]} experts — a shared problem; routed to the playbook/checklist, no card proposal")
            continue
        target = tags.get(tag, {}).get("target", "") or "§3 Method"
        if target.startswith("—"):
            out.append(f"  {expert}/{tag}: workflow-level tag, no card proposal (playbook/check rule instead)")
            continue
        fn = PROPOSALS / f"{TODAY}-{expert}-{tag}.md"
        ev_lines = "\n".join(
            f"- {e['session']} r{e['round']} · {expert} · {e.get('ref') or '?'} — \"{clean(e.get('note', ''))[:160]}\" — [{e.get('severity')}]"
            for e in sorted(es, key=lambda e: (e["session"], e["round"])))
        fn.write_text(f"""# Proposal: {expert} — {tags.get(tag, {}).get('meaning', tag)}

**Status:** drafting
**Kind:** improvement
**Tag:** {expert}/{tag}
**Filed:** {TODAY} by scripts/improve.py (threshold: `{tag}` on {expert} in {len(rounds)} rounds)
**Target:** experts/{expert}.md → {target}
**Evidence:**
{ev_lines}

## Change

TODO (orchestrator): read the cited turns and the target section, then write the exact text to add,
replace or remove. Mark additions `[observer-added, from <session> r<N>]` unless they carry a new
§8 anchor. Set **Status:** proposed when done.

## Risk

TODO (orchestrator).

## Validation

(filled by the independent reviewer; required before status → validated)

1. Cited statements or source evidence show the claim: —
2. No contradiction with §8 anchors or §1 scope: —
3. Not already covered by another expert: —
4. `scripts/validate.py` passes on a scratch copy: —
**Verdict:** —

## Applied

—
""", encoding="utf-8")
        out.append(f"  drafted {fn.relative_to(ROOT)} ({len(rounds)} rounds)")
        have.add(f"{expert}/{tag}")


# ---------- report ----------

def report() -> str:
    metrics = read_jsonl(METRICS)
    log = read_jsonl(LOG)
    lines = ["# Improvement report", ""]
    if metrics:
        lines += ["| session | r | check E/W | weaknesses H/M/L | KB cited | thinkers |", "|---|---|---|---|---|---|"]
        for m in metrics:
            lines.append(f"| {m['session']} | {m['round']} | {m['check_errors']}/{m['check_warnings']} | "
                         f"{m['weak_high']}/{m['weak_medium']}/{m['weak_low']} | {m['kb_cited']} | {m.get('thinkers', 0)} |")
        last = metrics[-3:]
        lines += ["", f"Last {len(last)} rounds: errors {sum(m['check_errors'] for m in last)}, high/medium weaknesses "
                      f"{sum(m['weak_high'] + m['weak_medium'] for m in last)}, KB cited {sum(m['kb_cited'] for m in last)}."]
    else:
        lines.append("No rounds ingested yet.")
    weak = Counter((e.get("expert") or "workflow", e["tag"]) for e in log if e.get("kind") == "weakness" and e.get("tag"))
    if weak:
        lines += ["", "## Recurring weaknesses (expert, tag, rounds)", ""]
        for (who, tag), n in weak.most_common(12):
            lines.append(f"- {who} · `{tag}` · {n}")
    pats = Counter(e["tag"] for e in log if e.get("kind") == "pattern" and e.get("tag"))
    if pats:
        lines += ["", "## Patterns seen", ""] + [f"- `{t}` · {n}" for t, n in pats.most_common(8)]
    st = Counter()
    for p in PROPOSALS.glob("*.md"):
        if p.name.startswith("_"):
            continue
        m = re.search(r"^\*\*Status:\*\*\s*(\w+)", p.read_text(encoding="utf-8"), re.M)
        st[m.group(1) if m else "?"] += 1
    if st:
        lines += ["", "## Proposals", "", ", ".join(f"{k}: {v}" for k, v in sorted(st.items()))]
        if st.get("drafting") or st.get("proposed") or st.get("validated"):
            lines.append("Pending work: fill `drafting`, review `proposed`, apply `validated` (skills/observe/SKILL.md).")
    if PLAYBOOK.exists():
        n = PLAYBOOK.read_text(encoding="utf-8").count("\n- [P-")
        lines += ["", f"Playbook entries: {n}. Knowledge files: " + ", ".join(
            str(p.relative_to(ROOT)) for p in sorted((ROOT / "knowledge").rglob("*.md")) if p.name not in ("README.md", "playbook.md"))]
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    out: list[str] = []
    cmd, rest = argv[0], argv[1:]
    force = "--force" in rest
    if cmd == "ingest":
        if "--all" in rest:
            paths = all_rounds()
        else:
            args = [a for a in rest if not a.startswith("--")]
            if not args:
                print("ingest needs a round.json, a session dir, or --all")
                return 2
            p = Path(args[0]).resolve()
            paths = sorted(p.glob("rounds/round-*.json")) if p.is_dir() else [p]
        for p in paths:
            ingest_round(p, force, out)
    elif cmd == "proposals":
        draft_proposals(out)
        if not out:
            out.append("no expert/tag pair has reached the threshold")
    elif cmd == "report":
        print(report(), end="")
        return 0
    else:
        print(f"unknown command {cmd}")
        return 2
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
