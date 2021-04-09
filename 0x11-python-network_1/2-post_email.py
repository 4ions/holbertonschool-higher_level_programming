#!/usr/bin/python3
""" Module of urllib """
from urllib import parse, request
import sys

if __name__ == '__main__':
    data = {}
    data['email'] = sys.argv[2]
    url_values = parse.urlencode(data).encode()
    url = sys.argv[1]
    all_info = request.Request(url, url_values)
    with request.urlopen(all_info) as response:
        page = response.read()
        print(page.decode('utf-8'))