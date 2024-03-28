#!/usr/bin/python3
"""
Sends a request to the specified URL and exhibits the decoded
(utf-8) response body
"""

from urllib import request, error
import sys

if __name__ == '__main__':
    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
