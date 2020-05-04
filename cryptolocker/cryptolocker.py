#!/usr/bin/env python3.8

key =  "0ba883a22afb84506c8d8fd9e42a5ce4e8eb1cc87c315a28dd"
flag_enc = open("flag.txt.enc", "r").read()

flag = ""
i = 2

for c in flag_enc:
    flag += chr(ord(c) ^ ord(key[(i) % len(key)]))
    i += 1

print(flag)
