#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in
order to solve this challenge

CHALLENGE: Please list 10 commits (from the most recent to oldest)
of the repository rail by the userrails
"""

if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()
    try:

        for idx in range(10):
            sha = commits[idx]['sha']
            commit = commits[idx]['commit']
            author_name = commit['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
