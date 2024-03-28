#!/usr/bin/python3
"""
Posts a request to the provided URL with the email included as a parameter,
then showcases the decoded (utf-8) response body
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
