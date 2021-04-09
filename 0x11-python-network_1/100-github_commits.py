#!/usr/bin/python3
""" Module of requests """
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_repo_name = sys.argv[2]
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(owner_repo_name, repo_name))
    json = req.json()
    if json:
        for i in range(0, len(json)):
            print("{}: {}".format(json[i].get("sha"), json[i]
                  .get("commit").get("author").get("name")))
