from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "healthy",
                "project": "AWS DevOps Automation"
            }).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<h1>AWS DevOps Automation</h1>"
                b"<p>My first CI/CD project is running!</p>"
            )

server = HTTPServer(("127.0.0.1", 8000), AppHandler)
print("Application running at http://127.0.0.1:8000")
server.serve_forever()