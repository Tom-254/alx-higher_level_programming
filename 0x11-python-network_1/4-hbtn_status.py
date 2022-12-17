#!/usr/bin/python3
"""
Using the requests module
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
