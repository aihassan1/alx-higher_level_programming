#!/usr/bin/python3
""" takes GitHub credentials and uses the GitHub API to display your id"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url=url, auth=(username, token))

    if response.status_code == 200:
        user_info = response.json()
        print("{}".format(user_info.get("id")))
    else:
        print("None")
