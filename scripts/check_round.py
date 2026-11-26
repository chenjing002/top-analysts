#!/usr/bin/env python3
"""Deterministic gate for one round: numbers, units, confidence caps, chat discipline, stall signals.

Usage:  python3 scripts/check_round.py sessions/<ts>/<sid>/rounds/round-NN.json [--json] [--quiet]
Exit 1 on errors. `scripts/validate.py` runs this for every round; rounds in sessions started on
or after GATE_FROM fail validation on errors, older rounds are reported only.

Checks (ids are referenced from skills/analyze/CHECKLIST.md):
  N1 direct S1/S2 evidence values must exist in the session's local data (1% tolerance)
  N2 `derived:` evidence with `formula` + `inputs` is recomputed (1% tolerance)
  N3 `derived:` evidence without formula/inputs is a warning
  N4 every 亿 / % / × / 元 figure in the spoken text appears in that turn's evidence
  U1 no "billion"/"million"/"trillion" in spoken text (house unit is 亿)
  C1 statement or conclusion at `high` confidence while resting on a model default
     (r = 8%, g = 3%, tax = 25%) or an unverified estimate is an error
  C2 fact-kind knowledge candidates need every figure verified by N1/N2, a 3-significant-figure
     match in local data, or an observer `verify` log line (else they enter as hypotheses)
  R1 the required return appears at a single rate; show two others (reverse curve)
  D1 turn longer than 110 words; D2 non-closing turn without exactly one question;
  D3 round one conclusion must carry the scorecard (great/good/gruesome + floor)
  D4 round one workpaper must carry the paired-line divergence scan (question menu)
  D5 round one must estimate what the main assets are worth (workpaper `calc.revalued_book` or an
     asset-worth section; conclusion says what they are worth against the price)
  T1 open disagreement, T2 unexplained S1/S2 cross-check mismatch on a cited series,
  T3 conclusion repeats the previous round, T4 single-quarter evidence under a high-confidence
     conclusion — each needs a Thinker consulted or an explicit decline in `thinkers_consulted`
"""
from __future__ import annotations

import ast
import json
import math
import operator
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE_FROM = "2026-11-24"  # sessions with session_id >= this date are hard-gated
TOL = 0.01
UNIT_WORDS = re.compile(r"\b(billion|million|trillion|bn|mn)\b", re.I)
DEFAULTS = re.compile(r"(r\s*=\s*8\s*%|8\s*%\s*(hurdle|required|discount)|required return of 8|hurdle of 8|g\s*=\s*3\s*%|tax\s*(rate)?\s*(of|=)?\s*25\s*%|25\s*%\s*tax|\bdefault\b|\bestimate[sd]?\b|\bassum(e|ed|es|ption)\b)", re.I)
DEFAULT_PARAMS = re.compile(r"(r\s*=\s*8\s*%|8\s*%\s*(hurdle|required|discount)|required return of 8|hurdle of 8|g\s*=\s*3\s*%|tax\s*(rate)?\s*(of|=)?\s*25\s*%|25\s*%\s*tax|model default|\bestimate[sd]?\b|\bscenario\b)", re.I)
RATE_WORDS = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%\s*(?:hurdle|required return|discount rate|cost of (?:equity|capital)|required)|(?:hurdle|required return|discount rate|r)\s*(?:=|of|at)\s*(\d{1,2}(?:\.\d)?)\s*%", re.I)
NUM_IN_TEXT = re.compile(r"(?<![\w.])(\d[\d,]*\.?\d*)\s*(亿|%|×|x\b|元|倍)")
DECIMAL_IN_TEXT = re.compile(r"(?<![\w.])(\d+\.\d+)(?![\d%亿×元倍])")
NUM_ANY = re.compile(r"-?\d[\d,]*\.?\d*")
LOCAL_SRC = re.compile(r"^\s*(S1|S2)\b", re.I)
QUARTERLY_SRC = re.compile(r"(raw_income|raw_balancesheet|raw_cashflow|raw_daily|duckdb|quarter|单季|Q[1-4]|\d{8}|TTM|9M|H1|H2)", re.I)
NONLOCAL_SRC = re.compile(r"^\s*(SRC|AR|KB|P-|user|panel|hypothesis|interpretation)", re.I)

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}


class Report:
    def __init__(self):
        self.errors, self.warnings, self.info = [], [], []
        self.candidates = []

    def err(self, cid, msg): self.errors.append(f"[{cid}] {msg}")
    def warn(self, cid, msg): self.warnings.append(f"[{cid}] {msg}")
    def note(self, cid, msg): self.info.append(f"[{cid}] {msg}")


# ---------- numeric pool ----------

def _walk(o, out):
    if isinstance(o, bool):
        return
    if isinstance(o, (int, float)):
        if math.isfinite(o):
            out.append(float(o))
    elif isinstance(o, dict):
        for v in o.values():
            _walk(v, out)
    elif isinstance(o, list):
        for v in o:
            _walk(v, out)
    elif isinstance(o, str):
        s = o.replace(",", "")
        if re.fullmatch(r"-?\d+(\.\d+)?", s):
            out.append(float(s))


def numeric_pool(data_dir: Path) -> list[float]:
    pool = []
    for name in ("factsheet.json", "avl_raw.json", "bme_raw.json"):
        p = data_dir / name
        if p.exists():
            try:
                _walk(json.loads(p.read_text(encoding="utf-8")), pool)
            except json.JSONDecodeError:
                pass
    return sorted(set(pool))


def close(a: float, b: float, tol: float = TOL) -> bool:
    if a == b:
        return True
    scale = max(abs(a), abs(b))
    if scale < 1:
        return abs(a - b) <= 0.005
    return abs(a - b) / scale <= tol


def in_pool(v: float, pool: list[float]) -> bool:
    # try the value, percent↔decimal, 亿↔yuan, and sign
    for cand in (v, v / 100, v * 100, v * 1e8, v / 1e8, -v):
        if cand == 0:
            continue
        for p in pool:
            if close(cand, p):
                return True
    return False


# ---------- derived evidence ----------

def safe_eval(expr: str, env: dict) -> float:
    node = ast.parse(expr.replace("×", "*").replace("−", "-").replace("÷", "/"), mode="eval")

    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        if isinstance(n, ast.Name):
            if n.id not in env:
                raise KeyError(n.id)
            return float(env[n.id])
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.operand))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("sum", "min", "max", "abs"):
            args = [ev(a) for a in n.args]
            if n.func.id == "sum":
                return float(sum(args if len(args) > 1 else args[0] if isinstance(args[0], list) else args))
            return float({"min": min, "max": max, "abs": abs}[n.func.id](*args))
        raise ValueError(f"unsupported expression: {ast.dump(n)}")

    return ev(node)


# ---------- text numbers ----------

def text_numbers(text: str) -> list[tuple[float, str, str]]:
    """(value, unit, as-written) for each unit-bearing or decimal figure in spoken text."""
    out = []
    for m in NUM_IN_TEXT.finditer(text):
        s = m.group(1).replace(",", "")
        try:
            out.append((float(s), m.group(2), m.group(1)))
        except ValueError:
            pass
    for m in DECIMAL_IN_TEXT.finditer(text):
        out.append((float(m.group(1)), "", m.group(1)))
    return out


def sig_figs(written: str) -> int:
    digits = written.replace(",", "").replace(".", "").lstrip("0")
    return len(digits.rstrip("0")) if "." not in written else len(digits)


def evidence_numbers(ev: dict) -> list[float]:
    nums = []
    vals = ev.get("values")
    if isinstance(vals, dict):
        _walk(vals, nums)
    elif isinstance(vals, list):
        _walk(vals, nums)
    for m in NUM_ANY.finditer(ev.get("claim", "") or ""):
        s = m.group(0).replace(",", "")
        try:
            nums.append(float(s))
        except ValueError:
            pass
    return nums


def matches_any(v: float, nums: list[float], text_repr: str = "") -> bool:
    # displayed precision: "182亿" vs 181.9 → |Δ| ≤ 0.5 ok; "28.6%" vs 0.286 ok
    decimals = len(text_repr.split(".")[1]) if "." in text_repr else 0
    half_unit = 0.5 * 10 ** (-decimals)
    for n in nums:
        for cand in (n, n * 100, n / 100):
            if abs(cand - v) <= half_unit + 1e-9 or close(cand, v, 0.02):
                return True
    return False


# ---------- main checks ----------

def check(round_path: Path, rep: Report) -> dict:
    r = json.loads(round_path.read_text(encoding="utf-8"))
    sess_dir = round_path.parent.parent
    data_dir = sess_dir / "data"
    pool = numeric_pool(data_dir)
    if not pool:
        rep.warn("N0", f"no local data under {data_dir}; numeric checks skipped")
    stmts = r.get("statements", [])
    verified_numbers: list[float] = []
    round_nums: list[float] = []
    thinkers = r.get("thinkers_consulted") or []
    has_thinker_or_decline = len(thinkers) > 0

    for i, s in enumerate(stmts):
        who = s.get("expert", "?")
        tag = f"t{i + 1} {who}"
        text = s.get("text", "") or ""
        turn_nums: list[float] = []

        for j, e in enumerate(s.get("evidence", []) or []):
            src = (e.get("source") or "").strip()
            nums = evidence_numbers(e)
            turn_nums.extend(nums)
            if e.get("unverifiable"):
                rep.note("N1", f"{tag} evidence {j + 1} marked unverifiable: {e.get('unverifiable')}")
                continue
            if src.lower().startswith("derived"):
                if e.get("formula") and isinstance(e.get("inputs"), dict):
                    try:
                        got = safe_eval(e["formula"], e["inputs"])
                        claimed = e.get("result")
                        if claimed is None and isinstance(e.get("values"), dict) and len(e["values"]) == 1:
                            claimed = list(e["values"].values())[0]
                        if claimed is None:
                            rep.warn("N2", f"{tag} evidence {j + 1}: formula given but no `result` (or single `values`) to compare")
                        elif not close(got, float(claimed)):
                            rep.err("N2", f"{tag} evidence {j + 1}: formula {e['formula']!r} = {got:.6g}, claimed {claimed}")
                        else:
                            verified_numbers.append(float(claimed))
                        for v in e["inputs"].values():
                            if pool and isinstance(v, (int, float)) and not in_pool(float(v), pool):
                                rep.warn("N2", f"{tag} evidence {j + 1}: input {v} not found in local data")
                    except Exception as ex:  # noqa: BLE001
                        rep.err("N2", f"{tag} evidence {j + 1}: cannot evaluate formula ({ex})")
                else:
                    rep.warn("N3", f"{tag} evidence {j + 1}: derived figure without `formula` + `inputs` — add them or mark `unverifiable`")
                continue
            if NONLOCAL_SRC.match(src):
                continue
            if LOCAL_SRC.match(src) and pool:
                missing = [n for n in nums if abs(n) >= 0.001 and not (1900 <= n <= 2100 and float(n).is_integer()) and not in_pool(n, pool)]
                if missing:
                    if QUARTERLY_SRC.search(src):
                        rep.warn("N1", f"{tag} evidence {j + 1}: {missing[:4]} not in fact sheet (quarterly/duckdb source {src!r}); workpaper must show the query")
                    else:
                        rep.err("N1", f"{tag} evidence {j + 1}: {missing[:4]} not found in local data for source {src!r}")
                else:
                    verified_numbers.extend(nums)

        # N4 spoken numbers need evidence (this turn, or an earlier turn of the round when quoting a colleague)
        for v, unit, written in text_numbers(text):
            if unit == "" and 1900 <= v <= 2100:
                continue
            if matches_any(v, turn_nums, written):
                continue
            if matches_any(v, round_nums, written):
                rep.note("N4", f"{tag}: {written}{unit} relies on an earlier turn's evidence")
                continue
            if pool and sig_figs(written) >= 3 and in_pool(v, pool):
                rep.warn("N4", f"{tag}: spoken figure {written}{unit} is in the local data but this turn cites no evidence item for it")
            else:
                rep.err("N4", f"{tag}: spoken figure {written}{unit} has no matching evidence item")
        round_nums.extend(turn_nums)

        # U1 units (dollar amounts quoted from a source are allowed)
        m = next((m for m in UNIT_WORDS.finditer(text)
                  if not re.search(r"(\$|usd|dollar)", text[max(0, m.start() - 40): m.end() + 12], re.I)), None)
        if m:
            rep.err("U1", f"{tag}: unit word {m.group(0)!r} in spoken text; write 亿")

        # C1 confidence vs defaults
        ev_blob = " ".join(json.dumps(e, ensure_ascii=False) for e in s.get("evidence", []) or [])
        if s.get("confidence") == "high" and DEFAULTS.search(text + " " + ev_blob):
            rep.err("C1", f"{tag}: confidence high while the turn rests on a default/estimate/assumption ({DEFAULTS.search(text + ' ' + ev_blob).group(0)!r})")

        # D1/D2 chat discipline
        words = len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)?|[一-鿿]", text))
        if words > 110:
            rep.warn("D1", f"{tag}: {words} words (cap 110)")
        q = text.count("?") + text.count("？")
        is_last = i == len(stmts) - 1
        if not is_last and q == 0:
            rep.warn("D2", f"{tag}: non-closing turn ends without a question")
        elif q > 1:
            rep.warn("D2", f"{tag}: {q} questions in one turn (ask one)")

    # conclusion
    concl = r.get("conclusion", {}) or {}
    answer = concl.get("answer", "") or ""
    all_blob = json.dumps(r, ensure_ascii=False)
    concl_blob = json.dumps(concl, ensure_ascii=False)
    hit = DEFAULT_PARAMS.search(all_blob) or DEFAULTS.search(concl_blob)
    if concl.get("confidence") == "high" and hit:
        rep.err("C1", f"conclusion confidence high while the round rests on a default or an estimate ({hit.group(0)!r}); cap at medium")
    # R1 required return shown at one rate only
    rates = {m.group(1) or m.group(2) for m in RATE_WORDS.finditer(all_blob)}
    if len(rates) == 1:
        rep.warn("R1", f"required return appears at one rate only ({rates.pop()}%); show the reverse curve at two other rates and argue the hurdle")
    if UNIT_WORDS.search(answer):
        rep.err("U1", "conclusion uses billion/million; write 亿")
    if r.get("round") == 1:
        low = answer.lower()
        if not any(k in low for k in ("great", "good", "gruesome")) or "floor" not in low:
            rep.warn("D3", "round one conclusion lacks the scorecard verdict (great/good/gruesome) and/or the downside floor")
        wp = data_dir / "workpaper-round-01.md"
        if wp.exists():
            wtxt = wp.read_text(encoding="utf-8").lower()
            if "divergence" not in wtxt or "growth_gap" not in wtxt:
                rep.warn("D4", "round one workpaper has no paired-line divergence scan (section naming the pairs and calc.growth_gap); see SKILL §3 step 1.7")
            if "revalued_book" not in wtxt and "asset worth" not in wtxt:
                rep.warn("D5", "round one workpaper does not estimate what the main assets are worth (calc.revalued_book or an asset-worth section with each basis); see SKILL §3 step 1.4")
        else:
            rep.warn("D4", f"no {wp.name} under {data_dir}; the divergence scan cannot be checked")
        if "worth" not in low:
            rep.warn("D5", "round one conclusion does not say what the main assets are worth against the price")

    # knowledge candidates
    for k, c in enumerate(r.get("knowledge_candidates", []) or []):
        text = c.get("text", "") or ""
        nums = [float(m.group(0).replace(",", "")) for m in NUM_ANY.finditer(text) if m.group(0).replace(",", "") not in ("", "-")]
        nums = [n for n in nums if not (1900 <= n <= 2100 and n.is_integer()) and abs(n) >= 0.01]
        unverified = [n for n in nums if not matches_any(n, verified_numbers, f"{n:g}")
                      and not (pool and sig_figs(f"{n:g}") >= 3 and in_pool(n, pool))]
        status = "verified" if not unverified else "unverified"
        rep.candidates.append({"index": k, "kind": c.get("kind"), "confidence": c.get("confidence"), "status": status, "unverified": unverified[:6]})
        if c.get("kind") == "fact" and c.get("confidence") == "high" and unverified:
            rep.warn("C2", f"knowledge candidate {k + 1} (fact, high) has figures not verifiable locally {unverified[:4]}; improve.py will demote it")

    # stall signals
    open_dis = [d for d in r.get("disagreements", []) or [] if d.get("status") == "open"]
    if open_dis and not has_thinker_or_decline:
        rep.warn("T1", f"{len(open_dis)} disagreement(s) left open and no Thinker consulted or declined (Hamming 2.3 invert / Tukey 2.5 bounding)")
    fs = data_dir / "factsheet.json"
    if fs.exists():
        try:
            checks = json.loads(fs.read_text(encoding="utf-8")).get("cross_check", [])
            bad = {c.get("concept") for c in checks if c.get("flag") not in ("ok", None) and abs(c.get("pct_diff") or 0) > 1}
            cited = {c for c in bad if c and c in all_blob}
            if cited and not has_thinker_or_decline:
                rep.warn("T2", f"S1/S2 cross-check differs >1% on cited series {sorted(cited)} and no Thinker consulted (Hamming 2.5 consistency first)")
        except json.JSONDecodeError:
            pass
    prev = round_path.parent / f"round-{int(r.get('round', 1)) - 1:02d}.json"
    if prev.exists():
        pa = (json.loads(prev.read_text(encoding="utf-8")).get("conclusion", {}) or {}).get("answer", "") or ""
        a, b = set(re.findall(r"\w+", answer.lower())), set(re.findall(r"\w+", pa.lower()))
        if a and b:
            jac = len(a & b) / len(a | b)
            if jac > 0.6 and not has_thinker_or_decline:
                rep.warn("T3", f"conclusion overlaps previous round {jac:.0%}; the same answer is returning (Hamming 2.2)")
    if concl.get("confidence") == "high" and re.search(r"single quarter|single-quarter|单季", all_blob, re.I) and not has_thinker_or_decline:
        rep.warn("T4", "high-confidence conclusion with single-quarter evidence in the round (Tukey 2.4 resistant estimate)")

    gated = str(r.get("session_id", "")) >= GATE_FROM
    try:
        shown = str(round_path.relative_to(ROOT))
    except ValueError:
        shown = str(round_path)
    return {"round": shown, "gated": gated, "errors": len(rep.errors),
            "warnings": len(rep.warnings), "candidates": rep.candidates}


def run(path: Path) -> tuple[Report, dict]:
    rep = Report()
    summary = check(path, rep)
    return rep, summary


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    path = Path(argv[0]).resolve()
    rep, summary = run(path)
    if "--json" in argv:
        out = dict(summary)
        out.update({"error_list": rep.errors, "warning_list": rep.warnings, "info": rep.info})
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        if "--quiet" not in argv:
            for n in rep.info:
                print("INFO ", n)
        for w in rep.warnings:
            print("WARN ", w)
        for e in rep.errors:
            print("ERROR", e)
        print(f"check_round {summary['round']}: {summary['errors']} errors, {summary['warnings']} warnings"
              f"{' (gated)' if summary['gated'] else ' (report only, pre-' + GATE_FROM + ')'}")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
