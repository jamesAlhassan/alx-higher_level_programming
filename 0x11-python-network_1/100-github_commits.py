#!/usr/bin/python3
'''
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API
'''
import requests as r
import sys as s


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    repo = s.argv[1]
    user = s.argv[2]

    res = r.get(url)
    commits = res.json()

    try:
        for (i in range(10)):
            print(f'{commits[1].get("sha")}:
                    {commits[i].get("commit").get("author").get("name")}')
    except IndexError:
        pass
