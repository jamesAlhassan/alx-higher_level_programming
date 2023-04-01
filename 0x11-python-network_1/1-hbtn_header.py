#!/usr/bin/python3
"""sends request & displays the value of the X-Request-Id variable """
import urllib.request as ur
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    request = ur.Request(url)

    with ur.urlopen(request) as res:
        print(dict(res.headers).get('X-Request-Id'))
