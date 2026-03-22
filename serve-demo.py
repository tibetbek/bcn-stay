#!/usr/bin/env python3
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class DemoHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/hotel-mirall-demo.html'
        return super().do_GET()

    def log_message(self, format, *args):
        pass  # suppress logs

server = http.server.HTTPServer(('', 3001), DemoHandler)
server.serve_forever()
