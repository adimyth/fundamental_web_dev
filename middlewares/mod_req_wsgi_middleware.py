from flask import Flask, request
from werkzeug.wrappers import Request, Response
from wsgiref.simple_server import make_server

"""
middleware that authenticates a user,
then modifies the environ object to pass to the application
"""
def check_credentials(handler):
    def _inner(environ, start_response):
        userName = request.authorization['username']
        password = request.authorization['password']
        if userName == "adimyth" and password == "expelliarmus":
            environ['user'] = { 'name': 'Aditya' }
            return handler(environ, start_response)
        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)
    return _inner


"""
application that returns "Hello world" if auth fails;
returns "Hello Aditya" otherwise
"""
app = Flask(__name__)
# nesting middlewares
app.wsgi_app = check_credentials(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    user = request.environ['user']
    return f"Hi {user['name']}"

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)

