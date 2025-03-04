from http.server import HTTPServer, BaseHTTPRequestHandler

port = 80

httpd = HTTPServer(('', port), BaseHTTPRequestHandler)
print('Starting simple httpd on port: ', str(httpd.server_port))
httpd.serve_forever()