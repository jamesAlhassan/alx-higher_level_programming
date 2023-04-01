#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''

import requests as re


if __name__ == '__main__':
    response = re.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
