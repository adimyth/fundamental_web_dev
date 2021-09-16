# Web Server

## What is Web Server
Web server can refer to hardwar or software or a combination of both -
1. On the *hardware* side, a web server is a computer that stores web server software and a webiste's component files (example - HTML files, images, CSS stylesheets and Javascript files). It connects to the internet and supports data interchange with other devices connected on the web.
2. On the *software* side, a web server includes several parts that controls how users access hosted files. At a **minimum**, it is an *HTTP server*. An HTTP server is one that understands URLs(web addresses) and HTTP protocol.

At the most basic level, whenever a browser needs a file that is hosted on a web server, the browser requests the file via HTTP. When the request reaches the correct (hardware) web server, the (software) HTTP server accepts the request, finds the requested document, and sends it back to the browser, also through HTTP.

> WEB SERVER's fundamental job is to accept and fulfill requests from clients for static content from a website

## Types
A **static web server** consists of a computer (hardware) with an HTTP server (software) that returns the hosted files as is to the browser.

A **dynamic web server** consists of a static web server (hardware+http server) along with some extra software like application server & database. We call it "dynamic" because the application server updates the hosted files before sending content to your browser via the HTTP server.

For example, to produce the final webpages you see in the browser, the application server might fill an HTML template with content from a database. Sites like MDN or Wikipedia have thousands of webpages. Typically, these kinds of sites are composed of only a few HTML templates and a giant database, rather than thousands of static HTML documents. This setup makes it easier to maintain and deliver the content.

## Hosting Files
First, a web server has to store all the files name HTML files, CSS stylesheets, images, etc & other resources. For this typically we go with a hosting provider like Hostinger, HostGator, GoDaddy, etc. Example - `Web Hosting` [service by GoDaddy](https://in.godaddy.com/hosting/web-hosting)

## Communicating through HTTP
Second, a web server provides support for (HyperText Transfer Protocol) HTTP. As the name suggests it specifies how to transfer hypertext (web documents) between two computers. A protocol is a set of rule for communication between two computers.

***HTTP is Textual, STATELESS*** protocol.

**Textual** - All commands are plain-text and human-readable
**Stateless** - Neither the server nor the client remembers the previous communications. For example, relying on HTTP server alone it cannot remember passwords or transcations so far (ex - cart contents). You need an application server for these.

## Common & Top Web Servers
1. **Apache HTTP Server** - Developed by Apache Software Foundation, it is a free and open source web server for Windows, Mac OS X, Unix, Linux, Solaris and other operating systems; it needs the Apache license.
2. **Nginx** - A popular open source web server for administrators because of its light resource utilization and scalability. It can handle many concurrent sessions 
3. **Microsoft Internet Information Services (IIS)** - Developed by Microsoft for Microsoft platforms; it is not open sourced, but widely used.
due to its event-driven architecture. Nginx also can be used as a proxy server and load balancer.
4. **Lighttpd** - A free web server that comes with the FreeBSD operating system. It is seen as fast and secure, while consuming less CPU power.
5. **Apache TomCat**

## Web server security practices
There are plenty of security practices individuals can set around web server use that can make for a safer experience. A few example security practices can include processes like:

* **Reverse proxy** which is designed to hide an internal server and act as an intermediary for traffic originating on an internal server
* **Access restriction** through processes such as limiting the web host's access to infrastructure machines or using Secure Socket Shell (SSH)
* Keeping web servers patched and up to date to help ensure the web server isn't susceptible to vulnerabilities
network monitoring to make sure there isn't any or unauthorized activity
* Using a firewall and SSL as firewalls can monitor HTTP traffic while having a Secure Sockets Layer (SSL) can help keep data secure



![TCP Socket Flow](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

`socket()` - creates a new socket
`bind(URL, PORT)` - binds the socket to the address
`listen()` - listens for new connections 
`accept()` - accepts a connection and returns `(conn, addr)` where `conn` is a new socket object used to send and receive data and `address` is the address bound to the socket on the other end of the connection
`recv()` - receive data in bytes
`sendall()` - sends the entire data at once in bytes

