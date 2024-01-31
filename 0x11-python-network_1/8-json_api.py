#!/usr/bin/python3
"""sends a POST request to url with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    parameter = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", params=parameter)
    try:
        json_data = response.json()

        if json_data == {}:
            print("No result")
        else:
            id = json_data.get("id")
            name = json_data.get("name")
            print("[{}] {}".format(id, name))

    except ValueError:
        print("Not a valid JSON")
