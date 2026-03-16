#!/usr/bin/env bash
set -euo pipefail

# Very simple deploy stub to exercise scripting references.
# Pretend to run migrations then start the backend demo app.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR%/scripts}"

python "$ROOT_DIR/backend/migrate_db.py" || echo "migrations failed (expected in tests)"
python "$ROOT_DIR/backend/main.py"
