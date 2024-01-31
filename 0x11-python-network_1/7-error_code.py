#!/usr/bin/python3
"""
Displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":
    # Retrieve the URL from the command-line arguments
    url = sys.argv[1]

    r = requests.get(url=url)
    if r.status_code < 400:
        print(r.text)

    else:
        print("Error code: {}".format(r.status_code))
