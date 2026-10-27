#!/usr/bin/env python3
"""Local preview server that understands the site's clean URLs (/about -> about.html).

Usage (from the repository root):  python3 tools/serve.py [port]
"""
import http.server, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public_html")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        fs_path = super().translate_path(path)
        if not os.path.exists(fs_path) and os.path.isfile(fs_path.rstrip("/") + ".html"):
            return fs_path.rstrip("/") + ".html"
        return fs_path

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Preview: http://localhost:{port}/  (Arabic: http://localhost:{port}/ar/)")
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
