from wsgiref.simple_server import make_server

def capitalize_response(handler):
    """dumb middleware that assumes response is a list of strings which can be capitlized"""
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

