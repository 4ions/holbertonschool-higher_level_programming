#!/usr/bin/python3
"""Module of urllib """
from urllib import parse, request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
