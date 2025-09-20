#!/usr/bin/env bash
# send_mail.sh
# Usage: ./send_mail.sh recipient@example.com
# Requires subject.txt and body.txt in the same folder (or set MAIL_FROM / SMTP_* env vars for SMTP fallback)

set -euo pipefail

RECIPIENT="${1:-}"
SUBJECT_FILE="subject.txt"
BODY_FILE="body.txt"

if [[ -z "$RECIPIENT" ]]; then
  echo "Usage: $0 recipient@example.com"
  exit 1
fi

if [[ ! -f "$SUBJECT_FILE" ]]; then
  echo "Error: $SUBJECT_FILE not found."
  exit 1
fi

if [[ ! -f "$BODY_FILE" ]]; then
  echo "Error: $BODY_FILE not found."
  exit 1
fi

# Read subject and body (subject may be multi-line; we collapse newlines to single space in header)
SUBJECT="$(tr '\n' ' ' <"$SUBJECT_FILE" | sed -e 's/[[:space:]]\+/ /g' -e 's/^ //; s/ $//')"

# 1) Try sendmail
if command -v sendmail >/dev/null 2>&1; then
  {
    printf "From: %s\nTo: %s\nSubject: %s\n\n" "${MAIL_FROM:-noreply@localhost}" "$RECIPIENT" "$SUBJECT"
    cat "$BODY_FILE"
  } | sendmail -t
  echo "Email sent using sendmail."
  exit 0
fi

# 2) Try mailx (or mail)
if command -v mailx >/dev/null 2>&1 || command -v mail >/dev/null 2>&1; then
  if command -v mailx >/dev/null 2>&1; then
    mailx -s "$SUBJECT" "$RECIPIENT" < "$BODY_FILE"
  else
    # fallback to mail
    mail -s "$SUBJECT" "$RECIPIENT" < "$BODY_FILE"
  fi
  echo "Email sent using mailx/mail."
  exit 0
fi

# 3) Try msmtp (expects ~/.msmtprc or env config)
if command -v msmtp >/dev/null 2>&1; then
  {
    printf "From: %s\nTo: %s\nSubject: %s\n\n" "${MAIL_FROM:-noreply@localhost}" "$RECIPIENT" "$SUBJECT"
    cat "$BODY_FILE"
  } | msmtp "$RECIPIENT"
  echo "Email sent using msmtp."
  exit 0
fi

# 4) Python fallback using SMTP server environment variables:
#    Requires: SMTP_SERVER, SMTP_USER, SMTP_PASS (SMTP_PORT optional, default 587)
#    Optional: MAIL_FROM (default noreply@localhost)
if command -v python3 >/dev/null 2>&1; then
  python3 - "$RECIPIENT" "$SUBJECT_FILE" "$BODY_FILE" <<'PY'
import sys, os, smtplib
from email.message import EmailMessage

to=sys.argv[1]
subject=open(sys.argv[2],"r",encoding="utf-8").read().strip().replace("\n"," ")
body=open(sys.argv[3],"r",encoding="utf-8").read()

msg=EmailMessage()
msg["From"]=os.environ.get("MAIL_FROM","noreply@localhost")
msg["To"]=to
msg["Subject"]=subject
msg.set_content(body)

smtp_server=os.environ.get("SMTP_SERVER")
smtp_port=int(os.environ.get("SMTP_PORT","587"))
smtp_user=os.environ.get("SMTP_USER")
smtp_pass=os.environ.get("SMTP_PASS")

if not smtp_server or not smtp_user or not smtp_pass:
    print("SMTP_SERVER, SMTP_USER and SMTP_PASS environment variables are required for the Python SMTP fallback.", file=sys.stderr)
    sys.exit(2)

with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as s:
    s.starttls()
    s.login(smtp_user, smtp_pass)
    s.send_message(msg)

print("Email sent using Python SMTP.")
PY

  exit $?
fi

echo "No supported mail delivery utility found (sendmail, mailx/mail, msmtp, or python3)."
echo "Install one of them or configure SMTP env vars for the Python fallback."
exit 2
