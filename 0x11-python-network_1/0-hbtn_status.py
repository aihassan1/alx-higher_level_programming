#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode("utf-8"))
