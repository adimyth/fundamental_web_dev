# Basic Web Server
![TCP Socket Flow](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

`socket()` - creates a new socket
`bind(URL, PORT)` - binds the socket to the address
`listen()` - listens for new connections 
`accept()` - accepts a connection and returns `(conn, addr)` where `conn` is a new socket object used to send and receive data and `address` is the address bound to the socket on the other end of the connection
`recv()` - receive data in bytes
`sendall()` - sends the entire data at once in bytes

