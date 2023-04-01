#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import urllib.request as ur
import urllib.parse as up
import sys


if __name__ == '__main__':
    url = sys.agrv[1]
    rec = {'email': sys.argv[2]}
    data = up.urlencode(rec).encode('ascii')

    req = ur.Request(url, data)

    with ur.urlopen(req) as res:
        print(res.read().decode('utf-8'))
