import socket
from http_parsing import print_contents, parser
from views import view

URL = "localhost"
PORT = 8080

# response has similar format as request object
def process_response(response):
    return (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(response)}\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            f"{response}"
            "\r\n"
            )
        

with socket.socket() as s:
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
            response = view(path)
            response = process_response(response)
            conn.sendall(response.encode("utf-8"))

