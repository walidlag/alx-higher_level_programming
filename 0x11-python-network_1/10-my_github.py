#!/usr/bin/python3
"""
Utilizes your GitHub credentials (username and password) to access the GitHub API and showcase your user ID
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
