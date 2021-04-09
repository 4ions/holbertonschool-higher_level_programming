#!/usr/bin/python3
""" Module of requests """
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    token = sys.argv[2]
    req = requests.get("https://api.github.com/user", auth=(user, token))
    dict_git = req.json()
    print(dict_git.get('id'))
