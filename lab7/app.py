from wsgiref.simple_server import make_server
from server import wsgi_app

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print("SOAP server listening on http://127.0.0.1:8000...")
    server.serve_forever()
