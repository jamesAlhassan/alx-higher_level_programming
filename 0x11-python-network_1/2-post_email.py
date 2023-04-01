#!/usr/bin/python3
"""sends POST request with the email as a parameter
and displays the body of the response
"""
import urllib.request as ur
import urllib.parse as up
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    rec = {'email': sys.argv[2]}
    data = up.urlencode(rec).encode('ascii')

    req = ur.Request(url, data)

    with ur.urlopen(req) as res:
        print(res.read().decode('utf-8'))
