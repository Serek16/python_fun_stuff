import requests

url = 'https://reqres.in/api/login'

payload = {
    "email": "",
    "password": ""
}

with requests.Session() as s:
    r = s.post(url, json=payload)
    print(r)
    print(r.text)
