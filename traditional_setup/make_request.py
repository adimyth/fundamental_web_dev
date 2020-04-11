import requests

URL = "http://localhost:8080/"

if __name__ == "__main__":
    response1 = requests.get(URL)
    print(response1.headers)
    print(response1.text)
    
    print("\n\n")
    
    response2 = requests.get(URL+"about")
    print(response2.headers)
    print(response2.text)

