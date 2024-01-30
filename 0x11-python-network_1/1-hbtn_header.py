#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
    display the value of the X-Request-Id variable
    found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    arg1 = sys.argv[1]
    req = urllib.request.Request(arg1)

    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
