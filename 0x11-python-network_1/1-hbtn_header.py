#!/usr/bin/python3
"""
The value of the X-Request-Id variable
located in the response header is shown
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
