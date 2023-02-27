from http.server import HTTPServer
from echo.handler import EchoRequestHandler

def run():
  import os

  host = os.getenv('ECHO_HOST', 'localhost')
  port = int(os.getenv('ECHO_PORT', 8018))

  server = HTTPServer((host, port), EchoRequestHandler)
  print(f'Listening on {host}:{port}')
  try:
      server.serve_forever()
  except KeyboardInterrupt:
      pass
  server.server_close()

if __name__ == '__main__':
  run()
