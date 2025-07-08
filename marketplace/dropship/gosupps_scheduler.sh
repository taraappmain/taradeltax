#!/bin/bash
# Scheduler: run auto-sync every 6 hours

cd "$(dirname "$0")"
echo "🕒 Starting GoSupps sync job at $(date)"
/usr/bin/python3.11 gosupps_auto_sync.py

