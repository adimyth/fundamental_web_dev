import requests

URL = "http://localhost:8080/"
data = "some random data"
headers = {}
headers["Content-Type"] = "text/html"

if __name__ == "__main__":
    response1 = requests.post(URL, data=data, headers=headers)
    print(response1.headers)
    print(response1.text)
    
    print("\n\n")
    
    response2 = requests.post(URL+"about", data=data, headers=headers)
    print(response2.headers)
    print(response2.text)

