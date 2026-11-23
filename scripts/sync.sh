#!/usr/bin/env bash
# Sync the repository to GitHub after each round. Refuses to push if validation fails.
# Usage: scripts/sync.sh "600519.SH 2026-11-23-01 round 2: <question>"
set -euo pipefail
cd "$(dirname "$0")/.."

MSG="${1:-update}"

python3 scripts/render_round.py --all >/dev/null
python3 scripts/build_index.py
python3 scripts/validate.py --quiet

git add -A
if git diff --cached --quiet; then
  echo "sync: nothing to commit"
  exit 0
fi
git commit -q -m "$MSG" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push -q origin main
echo "sync: pushed '$MSG' → https://chenjing002.github.io/top-analysts/"
