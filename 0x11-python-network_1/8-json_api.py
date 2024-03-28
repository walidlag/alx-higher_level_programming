#!/usr/bin/python3
"""Executes a request to the provided URL and presents the response body"""

import requests
import sys

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if isinstance(response, dict) and response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
