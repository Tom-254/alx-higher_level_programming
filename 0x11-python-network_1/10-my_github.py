#!/usr/bin/python3

"""
takes GitHub credentials (username and password)
"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    info = (username, token)
    res = requests.get(url, auth=info)
    try:
        print(res.json()['id'])
    except Exception:
        print('None')
