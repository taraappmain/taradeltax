#!/bin/bash
# Scheduler: run GoSupps auto-sync every 6 hours (cron or manual)

cd "$(dirname "$0")" || exit 1
echo "🕒 Starting GoSupps sync job at $(date)"

# Run Python with full path and check for errors
PYTHON_BIN="/usr/bin/python3.11"
SCRIPT="gosupps_auto_sync.py"

if [ ! -f "$SCRIPT" ]; then
  echo "❌ Script $SCRIPT not found!"
  exit 1
fi

$PYTHON_BIN "$SCRIPT"
if [ $? -ne 0 ]; then
  echo "❌ gosupps_auto_sync.py exited with errors at $(date)"
else
  echo "✅ gosupps_auto_sync.py completed successfully at $(date)"
fi

