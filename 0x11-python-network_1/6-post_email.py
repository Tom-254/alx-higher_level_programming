#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys
    para = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=para)
    print(res.text)