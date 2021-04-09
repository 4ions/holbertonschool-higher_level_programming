#!/usr/bin/python3
""" Module of request """
import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
