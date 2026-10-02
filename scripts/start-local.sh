#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ ! -x .venv/bin/python ]]; then
  echo "Bitte zuerst: python3 -m venv .venv && .venv/bin/python -m pip install -e ." >&2
  exit 1
fi
exec .venv/bin/python -m activi_agent.browser_demo.server
