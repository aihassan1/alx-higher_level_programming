#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and 
displays the body of the response (decoded in utf-8)
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

except urllib.error.URLError as e:
    print("Error code: {}".format(e.code))
