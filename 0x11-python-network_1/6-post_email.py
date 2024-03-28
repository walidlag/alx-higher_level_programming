#!/usr/bin/python3
"""
Initiates a POST request to the provided URL, including the email as a parameter, and then showcases the response body"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
