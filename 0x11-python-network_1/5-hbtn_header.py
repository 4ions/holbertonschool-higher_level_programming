#!/usr/bin/python3
""" Module of request """
import requests
import sys

req = requests.get(sys.argv[1])
for key, value in req.headers.items():
    if key == 'X-Request-Id':
        print(value)
