#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>

Arguments:
    URL: The URL to send the request to.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url=url)
    header = response.headers["X-Request-Id"]
    print(header)
