#!/usr/bin/python3
""" Module of urllib """
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(arv[1]) as response:
        print(response.getheader("X-Request-Id"))
