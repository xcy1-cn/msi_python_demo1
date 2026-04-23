import requests

url = "https://jsonplaceholder.typicode.com/users"

def getJsonFormUrl(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    raise Exception(f"Failed to fetch JSON from {url}: {res.status_code}")

print(getJsonFormUrl(url))