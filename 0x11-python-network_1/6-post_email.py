#!/usr/bin/python3
""" Module of request """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = requests.post(url, data)
    print(req.text)
