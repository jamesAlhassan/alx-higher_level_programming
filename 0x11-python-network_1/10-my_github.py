#!/usr/bin/python3
'''
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

import requests as r
from requests.auth import HTTPBasicAuth as r_auth
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.agrv[2]
    auth = r_auth(username, password)
    res = r.get(url, auth=auth)
    print(res.json().get('id'))
