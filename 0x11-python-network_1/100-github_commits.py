#!/usr/bin/python3

"""
Script takes 2 arguments.
    First argument is the repository name
    Second argument is the owner name
    using the packages requests and sys
"""

if __name__ == '__main__':
    import sys
    import requests
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo_info = owner_name + "/" + repo_name
    url = "https://api.github.com/repos/" + repo_info + "/commits"
    res = requests.get(url)
    top = res.json()[:10]
    for info in top:
        sha = info['sha']
        author = info['commit']['author']['name']
        print('{}: {}'.format(sha, author))
