import socket
from http.server import BaseHTTPRequestHandler, HTTPStatus

class EchoRequestHandler(BaseHTTPRequestHandler):
  server_version = 'Echo'
  sys_version = ''
  def handle_one_request(self):
      try:
        self.raw_requestline = self.rfile.readline(65537)
        if len(self.raw_requestline) > 65536:
          self.requestline = ''
          self.request_version = ''
          self.command = ''
          self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
          return
        if not self.raw_requestline:
          self.close_connection = True
          return
        if not self.parse_request():
          # An error code has been sent, just exit
          return
        self.do_any()
        self.wfile.flush() #actually send the response if not already done.
      except socket.timeout as e:
        #a read or a write timed out.  Discard this connection
        self.log_error("Request timed out: %r", e)
        self.close_connection = True
        return

  def do_any(self):
    """Process every request."""
    response = self.response.encode('utf-8')
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', str(len(response)))
    self.end_headers()
    self.wfile.write(response)

  @property
  def payload(self) -> str:
    result = b''
    length = int(self.headers.get('content-length', 0))
    result = self.rfile.read(length)
    return result

  @property
  def response(self) -> str:
      return f"""{self.command} {self.path} {self.protocol_version}
{str(self.headers).strip()}
{str(self.payload.decode('utf-8'))}""".strip()
