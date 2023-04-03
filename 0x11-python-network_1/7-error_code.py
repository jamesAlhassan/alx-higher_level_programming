#!/usr/bin/python3
'''hat takes in a URL, sends a request to the URL
and displays the body of the response.
'''
import requests as r
import sys


if __name__ == '__main__':
    re = r.get(sys.argv[1])
    if re.status_code >= 400:
        print(f'Error code: {re.status_code}')
    else:
        print(re.content.decode('utf-8'))
