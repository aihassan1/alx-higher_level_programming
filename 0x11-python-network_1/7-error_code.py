#!/usr/bin/python3
"""
Displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":
    # Retrieve the URL from the command-line arguments
    url = sys.argv[1]

    try:
        r = requests.get(url=url)
        r.raise_for_status()
        print(r.text)

    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
