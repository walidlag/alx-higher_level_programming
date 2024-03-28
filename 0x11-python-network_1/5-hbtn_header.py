#!/usr/bin/python3
"""Shows the X-Request-Id header variable from a request to a specified URL
"""
from sys import argv
from requests import get


if __name__ == '__main__':
    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
