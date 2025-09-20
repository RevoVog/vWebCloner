#!/usr/bin/env python3
import os
import sys
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Validate args
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} recipient@example.com")
    sys.exit(1)

recipient = sys.argv[1]

# Config from .env
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_FROM  = os.getenv("MAIL_FROM", SMTP_USER)

if not (SMTP_SERVER and SMTP_USER and SMTP_PASS):
    print("Missing SMTP_SERVER, SMTP_USER or SMTP_PASS in .env")
    sys.exit(2)

# Load subject and body
with open("subject.txt", "r", encoding="utf-8") as f:
    subject = f.read().strip().replace("\n", " ")

with open("body.txt", "r", encoding="utf-8") as f:
    body = f.read()

# Create email
msg = EmailMessage()
msg["From"] = MAIL_FROM
msg["To"] = recipient
msg["Subject"] = subject
msg.set_content(body)

# Send mail
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print(f"Mail sent to {recipient}")
except Exception as e:
    print("Failed to send mail:", e)
    sys.exit(3)
