#!/usr/bin/python3
""" Write a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as
    a parameter, and displays the body of the response
    (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
