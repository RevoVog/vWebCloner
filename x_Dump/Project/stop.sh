#!/usr/bin/env bash
set -euo pipefail

systemctl stop apache2 || true

if [ -f /var/run/cloudflared.pid ]; then
  PID=$(cat /var/run/cloudflared.pid)
  kill "$PID" 2>/dev/null || true
  rm -f /var/run/cloudflared.pid
fi
