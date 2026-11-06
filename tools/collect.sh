#!/usr/bin/env bash
# Six7 public manuals: copy each built manual from its repo at a named commit, close it with the
# collaboration credits (tools/credits.py), and record where it came from.
# Usage: tools/collect.sh <folder holding the Six7 repo checkouts>   (each checkout is fetched, never changed)
# MANIFEST.json gives each page's source commit, the SHA-256 of the page as built there ("source_sha256"),
# and the SHA-256 of the page as published here, with the credits ("sha256").
set -euo pipefail
SRC="${1:?folder with the Six7 checkouts}"; OUT="$(cd "$(dirname "$0")/.." && pwd)"
# repo  ref  pages (the Core Operator manual is Six7's own and stays out)
ROWS=(
  "Six7 origin/main six7-suite.html"
  "SIX7-Kanban origin/main six7-kanban-configuration.html six7-kanban-user.html"
  "SIX7-CRM origin/main six7-crm-configuration.html six7-crm-user.html"
  "SIX7-Service-Desk origin/main six7-service-desk-configuration.html six7-service-desk-user.html"
  "SIX7-Contracts-Providers origin/main six7-contracts-providers-configuration.html six7-contracts-providers-user.html"
  "Six7-Core origin/core-build six7-hub-user.html"
)
sha() { sha256sum "$1" | cut -d' ' -f1; }
echo '{ "collected": "'"$(date -u +%FT%TZ)"'", "credits": "tools/credits.py", "pages": [' > "$OUT/MANIFEST.json.tmp"; first=1
for row in "${ROWS[@]}"; do
  read -r repo ref pages <<<"$row"; git -C "$SRC/$repo" fetch -q origin
  commit=$(git -C "$SRC/$repo" rev-parse "$ref")
  for p in $pages; do
    git -C "$SRC/$repo" show "$commit:docs/manual/$p" > "$OUT/$p"
    source_sha=$(sha "$OUT/$p")
    python3 -I "$OUT/tools/credits.py" "$OUT/$p" >/dev/null
    [ $first = 1 ] || echo ',' >> "$OUT/MANIFEST.json.tmp"; first=0
    printf '  { "page": "%s", "repo": "dreamsgarage/%s", "ref": "%s", "commit": "%s", "source_sha256": "%s", "sha256": "%s" }' \
      "$p" "$repo" "$ref" "$commit" "$source_sha" "$(sha "$OUT/$p")" >> "$OUT/MANIFEST.json.tmp"
  done
done
printf '\n] }\n' >> "$OUT/MANIFEST.json.tmp"; mv "$OUT/MANIFEST.json.tmp" "$OUT/MANIFEST.json"
echo "Collected $(grep -c '"page"' "$OUT/MANIFEST.json") pages into $OUT, each closed with the credits"
