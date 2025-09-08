#!/bin/bash

# 1. Run your Python server in background
echo "[*] Starting Python server..."
python3 server.py &

SERVER_PID=$!

# Wait a bit to make sure it's running
sleep 2

# 2. Start Cloudflare Tunnel (temporary link)
echo "[*] Starting Cloudflare Tunnel..."
cloudflared tunnel --url http://localhost:8080
kill $SERVER_PID
