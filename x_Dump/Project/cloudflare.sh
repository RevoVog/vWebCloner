#!/usr/bin/env bash
set -euo pipefail

LOG=/tmp/cloudflared.log
cloudflared tunnel --url http://localhost:80 --no-autoupdate >"$LOG" 2>&1 &
PID=$!
echo $PID >/var/run/cloudflared.pid

# Wait until Cloudflare prints the link
URL=""
for i in {1..20}; do
  sleep 1
  URL=$(grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" "$LOG" | head -n1 || true)
  if [ -n "$URL" ]; then break; fi
done

if [ -n "$URL" ]; then
  echo "CLOUDFLARE_URL=$URL"
else
  echo "Could not fetch Cloudflare URL. Check $LOG"
fi
