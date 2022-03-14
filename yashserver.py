#!/usr/bin/env python3

import http.server
import json
import urllib.request


def getData():
    response = urllib.request.urlopen("http://yash-practice-backend-service:8089/someJson")
    text = response.read()
    jsonObj = json.loads(text)
    jsonObj['serverAddedKey'] = 'serverAddedValue'
    return jsonObj


class HelloHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/someJson":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(bytes('{ "key": "valueBlerg" }', "utf-8"))

        elif self.path == "/getData":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(getData()), "utf-8"))

        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html><head><title>Yash says Hello</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Hello.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


def main():
    server = http.server.HTTPServer(("0.0.0.0", 8088), HelloHandler)

    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Interrupted.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

