# Find_me

Lorsque l'on monte le fs `find_me`, on voit qu'il y a 2 fichier.
Un fichier chiffré avec luks et un fichier `pass.b64` qui dit que le pass n'est plus là.
On va utiliser `sleuthkit` pour récuperer les fichiers effacés.

```sh
$ fls find_me 
d/d 11: lost+found
r/r 12: unlock_me
r/r 13: pass.b64
r/r * 14:   part00
r/r * 15:   part01
r/r * 16:   part02
r/r * 17:   part03
r/r * 18:   part04
r/r * 19:   part05
r/r * 20:   part06
r/r * 21:   part07
r/r * 22:   part08
r/r * 23:   part09
r/r * 24:   part0a
r/r * 25:   part0b
r/r * 26:   part0c
r/r * 27:   part0d
r/r * 28:   part0e
r/r * 29:   part0f
r/r * 30:   part10
r/r * 31:   part11
r/r * 32:   part12
r/r * 33:   part13
r/r * 34:   part14
V/V 7681:   $OrphanFiles

$ istat find_me 14
#9730

$ istat find_me 34
#9750

$ blkls find_me 9730-9750
TWYtOVkyb01OWm5IWEtzak04cThuUlRUOHgzVWRZ

$ echo 'TWYtOVkyb01OWm5IWEtzak04cThuUlRUOHgzVWRZ' | base64 -d
Mf-9Y2oMNZnHXKsjM8q8nRTT8x3UdY
$ cryptsetup luksOpen unlock_me test
<enter password>

# /dev/mapper/test est créé

$ mount /dev/mapper/test /mnt/find2/
$ cd /mnt/find2
$ cat .you_found_me
FCSC{750322d61518672328c856ff72fac0a80220835b9864f60451c771ce6f9aeca1}
```
