sample_request = """
POST / HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.68.0
Accept: */*
Content-Length: 17
Content-Type: application/x-www-form-urlencoded

some random stuff
"""

def parser(http_request):
    request, *headers, _, body = http_request.split("\r")
    method, path, protocol = request.split(" ")
    headers = dict(line.split(":", maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def print_contents(method, path, protocol, headers, body):
    print("Request Content")
    print("="*30)
    print(f"Method: {method}")
    print(f"Path: {path}")
    print(f"Protocol: {protocol}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")
    print("\n\n")

