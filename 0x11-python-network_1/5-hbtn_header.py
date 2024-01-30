#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable"""

import requests
import sys

url = sys.argv[1]

response = requests.get(url=url)
header = response.headers["X-Request-Id"]
print(header)