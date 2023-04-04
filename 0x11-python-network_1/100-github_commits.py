#!/usr/bin/python3
'''
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API
'''
import requests as r
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    res = r.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print(f"{commits[1].get('sha')}:\
                    {commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
