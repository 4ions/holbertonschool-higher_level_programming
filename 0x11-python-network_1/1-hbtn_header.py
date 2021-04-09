#!/usr/bin/python3
""" Module of urllib """
from urllib import request
from sys import argv

url = argv[1]
if __name__ == "__main__":
    with request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(html)
