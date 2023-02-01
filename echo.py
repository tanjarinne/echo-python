# -*- coding: utf-8 -*-
"""
Echo
"""

from http.server import HTTPServer
from echo.handler import EchoHandler


class Echo(EchoHandler):
    """Echo"""

    @property
    def payload(self) -> str:
        """Read body entirely and return its content."""
        result = b''
        length = int(self.headers.get('content-length', 0))
        if length:
            result = self.rfile.read(length)
        return result

    @property
    def response(self) -> str:
        """Generate the response Echo responds with."""
        return f"""{self.command} {self.path} {self.protocol_version}
{str(self.headers).strip()}

{str(self.payload.decode('utf-8'))}""".strip()

    def do_any(self):
        """Process every request."""
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(self.response.encode('utf-8'))


if __name__ == '__main__':
    import os

    host = os.getenv('ECHO_HOST', '0.0.0.0')
    port = int(os.getenv('ECHO_PORT', 8018))

    server = HTTPServer((host, port), Echo)
    print(f'Listening on {host}:{port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
