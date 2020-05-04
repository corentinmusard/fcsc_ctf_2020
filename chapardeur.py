#!/usr/bin/env python3.8
"""

https://www.proofpoint.com/us/threat-insight/post/new-kpot-v20-stealer-brings-zero-persistence-and-memory-features-silently-steal

On a juste à lire le lien et faire les mêmes étapes
La clé a été changé, on procède par clair connu pour la retrouver

"""
from base64 import b64decode

def decode(enc: str) -> None:
    key = "tDlsdL5dv25c1Rhv"

    output = ""
    i = 0
    for c in enc:
        output += chr(ord(c) ^ ord(key[i % len(key)]))
        i += 1

    parse = output.split('__DELIMM__')
    print(parse)


# Chaine trouvé dans le GET
enc_b64 = "RHVdQ1V8BFVHAgRSAGNZRisbKDYoBXgpKW0HUgl8WUZMal1HXWIGU0Vtaid0HiE7ORszEhQ8UQUCU2o8dgApNDYBPiw7ZhsIGVUZSR8mEAJYGzM0Ng13JjNgajwUMxgGECUYEkETaiMkc3chdAA3KUQbMzQ2DXcmM2BqPABiWkIrGyg2KAV4KSltUQZCORwZBBsYCxATaiMkc3chdAA3KV5qGAsQYGo7MWB0IXMXOikrYRkAAT5FFhlUXA9UdzQyETcHBws8ajsxYHQhcxc6KSt0MywjHnQmNHdnPG5iNykwASA6KQFqOyltcSZ9GyU7KxszLCAJeS07f2o8"
enc = b64decode(enc_b64).decode()
decode(enc)

# Chaine trouvé dans le POST
enc = "\x2b\x00\x3e\x32\x34\x09\x74\x31\x29\x62\x49\x16\x42\x60" \
"\x18\x13\x01\x36\x3d\x06\x01\x7e\x78\x50\x1a\x13\x15\x43\x63\x66" \
"\x1b\x05\x01\x36\x5f\x09\x49\x1a\x5a\x10\x04\x57\x18\x22\x5c\x63" \
"\x45\x33\x00\x69\x1a\x1c\x55\x2f\x04\x32\x19\x46\x47\x06\x55\x20" \
"\x5c\x06\x11\x25\x19\x2c\x22\x0f\x66\x27\x7c\x49\x01\x55\x08\x37" \
"\x50\x47\x42\x7c\x5b\x42\x5c\x75\x0c\x52\x13\x51\x0d\x50\x50\x6b" \
"\x5a\x17\x17\x20\x5a\x15\x01\x7a\x57\x5d\x15\x02\x06\x00\x07\x31" \
"\x0d\x12\x46\x25\x5f\x12\x53\x29\x02\x05\x44\x02\x0d\x5a\x53\x67" \
"\x5b\x42\x16\x25\x0d\x16\x5d\x7b\x54\x53\x0b\x38\x6a\x27\x63\x13" \
"\x38\x33\x35\x11\x33"

decode(enc)
