from http.server import HTTPServer, BaseHTTPRequestHandler, \
    SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="SSL/server.key",
                               certfile='SSL/server.crt', server_side=True)

httpd.serve_forever()
