#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil

APACHE_DIR = "/var/www/html"

if len(sys.argv) != 2:
    print("Usage: python3 host_with_cloudflare.py <file.html>")
    sys.exit(1)

html_file = sys.argv[1]

# Check if file exists
if not os.path.isfile(html_file):
    print(f"[✘] File '{html_file}' not found!")
    sys.exit(1)

# Step 1: Copy HTML to Apache directory
try:
    shutil.copy(html_file, APACHE_DIR)
    print(f"[✔] {html_file} copied to Apache web root.")
except PermissionError:
    print("[✘] Permission denied. Run with sudo.")
    sys.exit(1)

# Step 2: Start Apache2 service
subprocess.run(["sudo", "systemctl", "enable", "apache2"])
subprocess.run(["sudo", "systemctl", "start", "apache2"])
print("[✔] Apache2 is running.")

# Step 3: Start Cloudflare Tunnel
print("[…] Starting Cloudflare tunnel (Ctrl+C to stop)...")
try:
    subprocess.run(["cloudflared", "tunnel", "--url", "http://localhost"], check=True)
except KeyboardInterrupt:
    print("\n[✔] Tunnel stopped by user.")
