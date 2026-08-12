"""Minimal HTTP app for the Docker + ECR demo."""

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
MESSAGE = b"Hello from Jenkins Docker demo!\n"


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(MESSAGE)

    def log_message(self, format, *args):
        # Keep container logs quiet during smoke tests
        return


def create_server(port=PORT):
    return HTTPServer(("0.0.0.0", port), HelloHandler)


def main():
    server = create_server()
    print(f"Listening on port {PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
