#!/usr/bin/env bash
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root (sudo)."
  exit 1
fi

# Stop Apache
systemctl stop apache2 || true

# Kill cloudflared if pid file exists
if [ -f /var/run/cloudflared.pid ]; then
  PID=$(cat /var/run/cloudflared.pid)
  if ps -p "$PID" > /dev/null 2>&1; then
    kill "$PID" || true
  fi
  rm -f /var/run/cloudflared.pid
fi

echo "Stopped apache2 and cloudflared (if running)."
