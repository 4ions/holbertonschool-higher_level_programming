#!/usr/bin/python3
""" Module of requests """
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""
    req = requests.post(url, data=data)
    try:
        d = req.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
