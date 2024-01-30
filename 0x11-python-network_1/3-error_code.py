#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.request
import urllib.error

url = sys.argv[1]
request = urllib.request.Request(url)

try:
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)

except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
