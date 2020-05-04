#!/usr/bin/env python3.8
"""
Programme pour tester facilement les payload
"""
from base64 import b64encode
import sys
import urllib.request

def request(arg: str) -> int:
    url_base = 'http://challenges2.france-cybersecurity-challenge.fr:5007/?search='
    url = url_base + b64encode(arg.encode()).decode()
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    print(html)

if len(sys.argv) == 2:
    request(sys.argv[1])
else:
    print(f"usage: {sys.argv[0]} 'payload'")
