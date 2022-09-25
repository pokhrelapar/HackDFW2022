import requests
import json

url = "http://127.0.0.1:5000/location"

r = requests.get(url)
print(r.status_code)
x = r.json()

print(x)

