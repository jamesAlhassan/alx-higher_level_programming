#!/usr/bin/python3
'''sends a request to the URL and displays
the body of the response (decoded in utf-8)
'''
import urllib.error as er
import urllib.request as ur
import sys


if __name == '__main__':
    url = sys.argv[1]

    req = ur.Request(url)

    try:
        with ur.urlopen(req) as res:
            print(res.read().decode('ascii'))
    except er.HTTPError as e:
        print(f'Error code: {e.code}')
