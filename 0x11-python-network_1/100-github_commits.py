#!/usr/bin/python3
"""The Python script retrieves a specific variable's value from the response header after sending a request to the given URL
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    URL = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = get(URL)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        print("Less than 10 commits available.")
