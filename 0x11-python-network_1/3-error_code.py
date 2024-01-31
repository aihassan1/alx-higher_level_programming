#!/usr/bin/python3
"""
Displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    # Retrieve the URL from the command-line arguments
    url = sys.argv[1]

    # Create a urllib.request.Request object with the provided URL
    request = urllib.request.Request(url)

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(request) as response:
            # Decode the response body as UTF-8
            body = response.read().decode("utf-8")
            # Print the body of the response
            print(body)

    # Handle HTTP errors
    except urllib.error.HTTPError as e:
        # Print the error code
        print("Error code: {}".format(e.code))
