#!/usr/bin/python3
"""
The script will send a request to the given URL, showing the response body if there are no issues and indicating the HTTP error code otherwise
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
