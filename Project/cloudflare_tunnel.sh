#!/usr/bin/env bash
set -euo pipefail

# This script runs cloudflared in the background and writes its PID to /var/run/cloudflared.pid
# Assumes cloudflared is installed. If not, install first (see cloudflared docs).

if ! command -v cloudflared >/dev/null 2>&1; then
  echo "cloudflared not found. Please install cloudflared first and authenticate if required."
  exit 2
fi

# Run ephemeral tunnel; output redirected
LOG=/tmp/cloudflared.out
cloudflared tunnel --url http://localhost:80 > "$LOG" 2>&1 &
echo $! > /var/run/cloudflared.pid
sleep 1
echo "cloudflared started (PID $(cat /var/run/cloudflared.pid)). Logs: $LOG"
