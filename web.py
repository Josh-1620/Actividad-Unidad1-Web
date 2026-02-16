from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
    parsed_url = urlparse(self.path)
    path_parts = parsed_url.path.strip("/").split("/")
    query = dict(parse_qsl(parsed_url.query))

    if len(path_parts) == 2 and path_parts[0] == "proyecto":
        proyecto = path_parts[1]
        autor = query.get("autor", "")
        response = f"<h1>Proyecto: {proyecto} Autor: {autor}</h1>"
    else:
        response = "<h1>Ruta no encontrada</h1>"

    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(response.encode("utf-8"))


    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(("localhost", PORT), WebRequestHandler)
    print(f"Starting server on port {PORT}")
    server.serve_forever()
