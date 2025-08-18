#!/usr/bin/env python3
# cgi-bin/login.py
# Simple CGI script: logs username/password to /tmp/login_submissions.log and returns an HTML acknowledgement.

import cgi
import cgitb
import time
import os
cgitb.enable()

form = cgi.FieldStorage()
username = form.getfirst('username', '')
password = form.getfirst('password', '')

remote = os.environ.get('REMOTE_ADDR', '-')
ts = time.strftime('%Y-%m-%d %H:%M:%S')

logline = f"{ts}\t{remote}\t{username}\t{password}\n"
try:
    with open('/tmp/login_submissions.log', 'a') as f:
        f.write(logline)
except Exception as e:
    # if logging fails, write to Apache error log by raising an error (cgitb will handle)
    pass

print("Content-Type: text/html")
print()
print(f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Thanks</title></head>
<body>
  <h2>Thanks, {cgi.escape(username)}</h2>
  <p>Your submission was received at {ts} from {remote}.</p>
  <p><a href="/">Back to login</a></p>
</body></html>""")
