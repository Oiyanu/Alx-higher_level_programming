#!/usr/bin/python3
"""sends request to the URL, displays value of the variable X-Request-Id"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
