from datetime import datetime

# returns dynamic response
def application(start_response, environ):
    response = view(environ["PATH_INFO"])
    status = "200 OK"
    headers = [("Content-Type", "text/html"),
                ("Content-Length", len(response)),
                ("Date", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))]
    start_response(status, headers)
    return [response]


def view(path):
    if path == "/":
        return f"You are at Homepage: ({path})"
    else:
        return f"You are at some other page: ({path})"
