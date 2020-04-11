# Fundamental Web Development

Trying to understand the working of the following, by developing them from scratch.
1. Basic Client-Server Architecture
2. Communication between web server and web application using WSGI
3. Middlewares (developed from scratch)

# WSGI
![Link 1](https://www.youtube.com/watch?v=WqrCnVAkLIo)
![Link 2](https://rahmonov.me/posts/what-the-hell-is-wsgi-anyway-and-what-do-you-eat-it-with/)

## History
### Static Web Servers
![static](https://i.imgur.com/HRRxRPt.png)

Very boring! No sessions, no dynamic content, etc. All  the HTML pages were just stored on the web server & sent when a request came in. 

### Common Gateway Interface (CGI)
![cgi](https://i.imgur.com/6WS0bSr.png)

The idea is that the scripts would still reside on the web server and when a request came in for that script instead of serving the contents of it, you would actually invoke the script.

Every time a request came in a script was executed like in PHP, etc. Essentially, we would invoke a script for dynamic content.

The advantage being that simply printing stuff on **stdout** will be returned as HTTP response. For eg; if the script returns *`Hello World`*, then it will be passed as a HTTP response.

>The biggest limitation being that everytime a new request came in we were forced to restart the entire script which could include restarting the python interpreter (which happens whenever u run a script). Even though it adds few hundred milliseconds for each request, the accumulation makes the server very slow

## WSGI 
>Fast, dynamic and pythonic

![wsgi-1](https://imgur.com/9W7M7sr.png)

![wsgi-1](https://imgur.com/ScbGd2S.png)

What was really needed was a *seperate web server and seperate web application* to which we could send request when we receive them and get responses out to send them to user.

WSGI provides a standard interface between *web servers (eg. gunicorn)* and *web applications or frameworks (eg; DJANGO)*.  WSGI is a  SET OF RULES for a web server and a web application to communicate with each other. 

 According to PEP 333, the document which specifies the details of the WSGI, the application interface is implemented as a ```callable object such as a function, a method, a class or an instance with a *__call__*``` method. This object should accept two positional arguments and return the response body as strings in an iterable.

The two arguments are:-
* a dictionary with environment variables
* a callback function that will be used to send HTTP status and HTTP headers to the server

```python
def application(start_response, environ):
	response = 'Hello World'
	headers = [('Content-Length', len(response))]
	start_response('200 OK', headers)
	return [response]
```
```
# environ
{
	'REQUEST_METHOD': 'GET',
	'PATH_INFO': '/url/',
	'SERVER_PROTOCOL': 'HTTP/1.1',
	........
}
```


## MiddleWare
[Link 1](https://oz123.github.io/advanced-python/book/middlewares.html)

The name middleware stems from the fact that it is the software that sits between the client-side requests on the front end and the back-end resource being requested.

A middleware is an object that wrapps the original application. Middlewares and apps are agnostic to each other, so we can plug any *WSGI* app to a middleware a any middleware to any WSGI app. There can be chain of middlewares, allowing a request or resphttps://www.youtube.com/watch?v=WqrCnVAkLIoonse to go through many layers of processing. 

Essentially, the middleware performs some specific function on the HTTP request or response at a specific stage in the HTTP pipeline before or after the user defined controller. Middleware is a design pattern to eloquently add cross cutting concerns like logging, handling authentication, or gzip compression without having many code contact points. Since these cross-cutting concerns are handled in middleware, the controllers/user defined handlers can focus on the core business logic.

>Client - Web Server - Middleware - Web Application

```python
from wsgiref.simple_server import make_server
import json

def capitalize_response(handler):
    """dumb middleware the assumes response is a list of
       strings which can be capitlized"""
    print("Inside Capitalize Middleware")
    def _inner(environ, start_response):
        response = handler(environ, start_response)
        return [line.decode().upper().encode() for line in response]
    return _inner


def environment_logger(handler):
    """middleware that just simply prints the environment variable to STDOUT"""
    print("Inside Environment Logging Middleware")
    def _inner(environ, start_response):
        _ = handler(environ, start_response)
        response_body = [
                    '{key}: {value}'.format(key=key, value=value) for key, value in sorted(environ.items())
                ]
        response_body = '\n'.join(response_body)
        return [response_body.encode("utf-8")]
    return _inner


def handler(environ, start_function):
    print("Inside Web Application")
    start_function('200 OK', [('Content-Type', 'application/json')])
    return [b"Hello World!\n"]

# nesting middlewares
app = capitalize_response(environment_logger(handler))

if __name__ == "__main__":
    srv = make_server('localhost', 5000, app)
    srv.serve_forever()

```

