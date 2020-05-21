import requests
from pyquery import PyQuery
from bs4 import BeautifulSoup

payload = {
    'j_username': '',
    'j_password': '',
    '_login_redirect_url': 'https%3A%2F%2Fwww.filmweb.pl%2Fuser%2Fserek16_00',
    '_prm': 'true'
}

sex_data = {}

login_url = 'https://www.filmweb.pl/j_login'
settings_url = 'https://www.filmweb.pl/settings'
sex_url = 'https://www.filmweb.pl/settings/sex'

with requests.Session() as s:
    p = s.post(login_url, data=payload)

    r = s.get(settings_url)
    soup = BeautifulSoup(r.content, 'html5lib')

    sex_data['token'] = soup.find('input', attrs={'name': 'token'})['value']
    sex_data['sex'] = 'F'

    sex_change = s.post(sex_url, data=sex_data)
