#!/usr/bin/python3
"""
The script will send a request to the given URL, showing the response body if there are no issues and indicating the HTTP error code otherwise
"""
    from sys import argv
    from requests import get


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
