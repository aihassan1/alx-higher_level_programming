#!/usr/bin/python3
"""
    # script that takes in a URL, sends a request to the URL and
    # display the value of the X-Request-Id variable
    # found in the header of the response.
"""

import sys
import urllib.request

arg1 = sys.argv[1]
req = urllib.request.Request(arg1)

with urllib.request.urlopen(req) as response:
    content = response.headers["X-Request-Id"]
    print(content)
