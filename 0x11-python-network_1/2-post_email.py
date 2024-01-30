#!/usr/bin/python3
"""
    takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # URL and data to be sent in the POST request
    url = sys.argv[1]
    email_arg = sys.argv[2]

    value = {"email": email_arg}
    email = urllib.parse.urlencode(value)
    email = email.encode("utf-8")

    # Create a POST request object
    request = urllib.request.Request(url=url, data=email)

    # send the request and get the response
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
