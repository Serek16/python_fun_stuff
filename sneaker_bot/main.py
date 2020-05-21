import requests
import json
from pyquery import PyQuery

payload = {
    'email': '',
    'password': ''
}

headers = {
    'accept': "*/*",
    'content-type': "application/json",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

login_url = 'https://www.zalando-lounge.pl/onboarding-api/login'
login_url2 = 'https://www.zalando-lounge.pl/#/login'
logged_url = 'https://www.zalando-lounge.pl/myaccount'


with requests.Session() as s:
    g = s.get("https://www.zalando-lounge.pl/#/login")
    p = s.post(login_url, json=payload, headers=headers)

    r = s.get(logged_url)

    print(p)
    print(p.status_code)

    title = PyQuery(r.content)("title").text()
    print(title)
    print('res: {}'.format(p.text))
