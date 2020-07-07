import http.server
import socketserver
import os

PORT = os.getenv('PORT', '8080')

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        """handle webhook request here"""

with socketserver.TCPServer(('', int(PORT)), WebhookHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
