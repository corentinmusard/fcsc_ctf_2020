# CryptoLocker

## Partie forensic

```bash
$ file memory.dmp
memory.dmp: MS Windows 32bit crash dump, PAE, full dump, 262030 pages
```
On a affaire à un dump mémoire windows.


Volatility n'a pas l'air de trouver un profile adéquat, je vais forcer un profile de Windows 32bits au hasard.
```bash
volatility -f memory.dmp --profile Win7SP1x86 imageinfo`
```
Ça fonctionne, on récupère les infos habituelles.

D'un autre côté, `string memory.dmp | grep 'flag.txt' ` trouve des occurences interessantes.
On voit le fichier `C:\Users\IEUser\Desktop\flag.txt`.

Allons voir si volatility peut le récuperer.
`volatility -f memory.dmp --profile Win7SP0x86 filescan` permet de lister chaque fichier contenu dans l'image.

Par 'chance', le fichier `flag.txt` est présent. Dans le même dossier, on trouve également `key.txt` et `update_v0.5.exe`.
```
0x000000003ed13898      2      1 R--rw- \Device\HarddiskVolume1\Users\IEUser\Desktop\key.txt
0x000000003ed139f0      2      0 RW-rw- \Device\HarddiskVolume1\Users\IEUser\Desktop\flag.txt.enc
0x000000003ed66b60      6      0 R--r-d \Device\HarddiskVolume1\Users\IEUser\Desktop\update_v0.5.exe
```
On extrait ces 2 fichiers.
```bash
mkdir filedump
volatility -f memory.dmp --profile Win7SP0x86 dumpfiles -D filedump/ -Q 0x000000003ed13898
volatility -f memory.dmp --profile Win7SP0x86 dumpfiles -D filedump/ -Q 0x000000003ed139f0
volatility -f memory.dmp --profile Win7SP0x86 dumpfiles -D filedump/ -Q 0x000000003ed66b60
```

key.txt
```
0ba883a22afb84506c8d8fd9e42a5ce4e8eb1cc87c315a28dd
```

## Partie reverse
`update_v0.5.exe` est un PE32, il va falloir faire du reverse.

Très rapidement, on trouve une fonction `_encryptFile`.
La fonction lit `flag.txt`, effectue un xor avec la clé de `key.txt` et écrit le contenu chiffré dans `flag.txt.enc`.

Dans le programme, le flag est chiffré en partant d'un compteur `i=0`.
Pour une raison que je n'ai pas compris, pour avoir le flag en clair, il faut partir de `i=2`.

Et voilà.
