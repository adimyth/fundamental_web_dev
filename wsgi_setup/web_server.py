from app import application
import io
from http_parsing import print_contents, parser
import socket
import sys

URL = "localhost"
PORT = 8080

# clousure pattern; assumes this method has access to the connection object that we want to send data back on
# this function should return HTTP Status and HTTP headers to the server
def start_response(status, headers):
    conn.sendall(f"HTTP/1.1 {status}\r\n".encode("utf-8"))
    for key, value in headers:
        conn.sendall(f"{key}: {value}\r\n".encode("utf-8"))
    conn.sendall("\r\n".encode("utf-8"))


def get_environ(method, path, protocol, headers, body):
    print(method, path, protocol, body)
    environ = {}
    # standard environ keys
    environ["REQUEST_METHOD"] = method
    environ["PATH_INFO"] = path
    environ["CONTENT_TYPE"] = headers["Content-Type"]
    environ["CONTENT_LENGTH"] = headers["Content-Length"]
    environ["SERVER_NAME"] = headers["Host"].split(":")[0]
    environ["SERVER_PORT"] = headers["Host"].split(":")[1]
    environ["SERVER_PROTOCOL"] = protocol 
    # wsgi environ keys
    environ["wsgi.version"] = (1,0)
    environ["wsgi.url_scheme"] = protocol.lower()
    environ["wsgi.input"] = io.StringIO(body)
    environ["wsgi.errors"] = sys.stderr
    environ["wsgi.multhread"] = False
    environ["wsgi.multiprocess"] = False
    environ["wsgi.run_once"] = False
    return environ

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((URL, PORT))
    s.listen()
    
    while True:
        # conn - new socket object usable to send & receive data on the connection
        # address - address bound to the socket on the other side of the connection
        conn, addr = s.accept()
        print(f"Remote Address: {addr}")
        with conn:
            request = conn.recv(4096).decode("utf-8")
            method, path, protocol, headers, body = parser(request)
            environ = get_environ(method, path, protocol, headers, body)
            response = application(start_response, environ)
            # application returns an iterable of data
            for data in response:
                conn.sendall(data.encode("utf-8"))

