#!/usr/bin/python3
"""
The script will send a request to the given URL, showing the response body if there are no issues and indicating the HTTP error code otherwise
"""
    from sys import argv
    from requests import get


if __name__ == "__main__":
    url = argv[1]

    response = get(url)
    ERR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERR_TXT.format(status) if (status >= 400) else response.text)
