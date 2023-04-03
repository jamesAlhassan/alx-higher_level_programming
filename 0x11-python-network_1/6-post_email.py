#!/usr/bin/python3
'''takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''
import requests as r
import sys


if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    request = r.post(sys.argv[1], data=data)
    body = request.content.decode('utf-8')
    print(body)
