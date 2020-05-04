#!/usr/bin/env python3.8
"""
La génération du serial est un simple xor avec 0x1f
On voit la comparaison en faisant un `ltrace ./SerialKeyler`
"""
from pwn import *

def serial_gen(username: str) -> None:
    key = chr(0x1f)
    output = ""
    i = 0
    for c in username:
        output = chr(ord(c) ^ ord(key[i % len(key)])) + output
        i += 1

    return output

r = remote("challenges2.france-cybersecurity-challenge.fr", 3001)

for i in range(55):
    msg = r.recvuntil(">>> ")
    username = msg.decode().split(': ')[-1].split('\n')[0]
    serial = serial_gen(username)
    print(f"{i} username='{username}', serial='{serial}'")
    r.send(serial+"\n")

r.interactive()
