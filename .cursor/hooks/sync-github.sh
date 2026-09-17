#!/bin/bash
# If a book file changed (or this is end-of-turn), publish chapters 1-10.
cat >/dev/null
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
python3 "$ROOT/scripts/sync_github.py" >/dev/null 2>&1 || true
echo '{}'
exit 0
