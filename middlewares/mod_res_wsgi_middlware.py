from flask import Flask

"""
a dumb middleware that assumes response is a list of strings;
and reverses each of them
"""
def reverse_response(handler):
    print("Inside Middleware")
    def _inner(environ, start_response):
        response = handler(environ, start_response)
        mod_resp = [x[::-1] for x in response]
        return mod_resp
    return _inner

def application(environ, start_response):
    return "Hello world"

app = Flask(__name__)
# nesting middlewares
app.wsgi_app = reverse_response(app.wsgi_app)
 
@app.route("/", methods=["GET"])
def hello():
    return "Hello World!!"
  
if __name__ == "__main__":
    app.run("localhost", 5000)
 
