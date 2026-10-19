#!/usr/bin/env bash
# Preview the theme locally with sample content.
#   scripts/dev.sh build   build to ./public
#   scripts/dev.sh serve   serve at http://localhost:1313 (default)
# Needs Hugo 0.91.x (the version micro.blog builds with) and Python 3.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 dev/make_config.py
case "${1:-serve}" in
  build) hugo --source dev --destination ../public ;;
  serve) hugo server --source dev --disableFastRender ;;
  *) echo "usage: scripts/dev.sh [build|serve]" >&2; exit 1 ;;
esac
