#!/usr/bin/python3
"""
Initiates a POST request to the provided URL, including the email as a parameter, 
and then showcases the response body"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)

