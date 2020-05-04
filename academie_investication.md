# Académie de l'investigation

## C'est la rentrée

On trouve les infos nécessaire en utilisant `strings` puis `grep`.

```
_HOSTNAME=challenge.fcsc
LOGNAME=Lesage
BOOT_IMAGE=/boot/vmlinuz-5.4.0-4-amd64
```
Le flag est donc `FCSC{challenge.fcsc:Lesage:5.4.0-4-amd64}`.

## Premiers artéfacts

On avait déjà la version de linux, il manque juste la version de debian : `Debian GNU/Linux bullseye/sid`.
Maintenant il va falloir créer un profile pour volatility car les infos demandées sont assez complexe à trouver avec `grep`.

Maintenant on télécharge un iso de debian bullseye. On l'installe avec qemu, virtualbox ou autre.
```sh
# Pour l'installation
qemu-img create mydisk.img 10G
qemu-system-x86_64 -boot d -m 512 -hda mydisk.img -cdrom debian-bullseye-DI-alpha2-amd64-netinst.iso
# Après l'installation, pour lancer la VM
qemu-system-x86_64 -boot d -m 512 -hda mydisk.img -net nic -net user
```

Hop, direction google pour trouve le package `linux-headers-5.4.0-4-amd64`.
On le retrouve après quelques recherches sur un repo non officiel : `https://git.sdxlive.com/DR/plain/Debian/pool/stable/l/linux/`.
On télécharge le `.deb` voulu et également `linux-headers-5.4.0-4-common` et `linux-kbuild-5.4_5.4.19-1_amd64` car ce sont ces dépendances.

On installe les 3 `.deb`. `dpkg -i linux-headers-5.4.0-4-amd64.deb`

On suit le wiki de volatility (https://github.com/volatilityfoundation/volatility/wiki/Linux) pour créer le profile.
Enfin une bonne chose de faite, on va pouvoir travailler maintenant.

Mon profile s'appelle `LinuxDebian11x64` et est dans le dossier `profiles`.

On récupère la première information avec l'historique bash.
```sh
$ volatility --plugins=profiles --profile=LinuxDebian11x64 -f dmp.mem linux_bash
1523 bash                 2020-03-26 23:29:19 UTC+0000   nmap -sS -sV 10.42.42.0/24
```

Puis la 2eme avec `linux_psscan`.
```sh
$ volatility --plugins=profiles --profile=LinuxDebian11x64 -f dmp.mem linux_psscan | grep 1254
0x000000003fdccd80 pool-xfconfd         1254            -               -1              -1     0x0fd08ee88ee08ec0 -
```

Et enfin la 3eme avec `linux_netstat -U`. (`-U` pour ne pas afficher les sockets UNIX, qui sont inutiles pour nous).
```
TCP      10.42.42.131    :36970 116.203.52.118  :  443 ESTABLISHED                   tor/706  
TCP      10.42.42.131    :37252 163.172.182.147 :  443 ESTABLISHED                   tor/706  
TCP      10.42.42.131    :47106 216.58.206.226  :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :55224 151.101.121.140 :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :53190 104.124.192.89  :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :45652 35.190.72.21    :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :38186 216.58.213.142  :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :50612 104.93.255.199  :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :58772 185.199.111.154 :  443 ESTABLISHED              chromium/119187
TCP      10.42.42.131    :57000 10.42.42.134    :   22 ESTABLISHED                   ssh/119468
TCP      10.42.42.131    :51858 10.42.42.128    :  445 ESTABLISHED             smbclient/119577
TCP      fd:6663:7363:1000:c10b:6374:25f:dc37:36280 fd:6663:7363:1000:55cf:b9c6:f41d:cc24:58014 ESTABLISHED                  ncat/1515 
TCP      127.0.0.1       :38498 127.0.0.1       :34243 ESTABLISHED                   cli/119514
```

Le flag est donc `FCSC{pool-xfconfd:nmap -sS -sV 10.42.42.0/24:13}`.

## Porte dérobée

Les infos demandées sont trouvées grâce à `linux_netstat`, `linux_pslist`, `linux_psaux` et `linux_pstree`.

Quel est le numéro de port à l'écoute de cette connexion ?
`36280`

Quelle est l'adresse IP distante connectée au moment du dump ?
`fd:6663:7363:1000:55cf:b9c6:f41d:cc24`

Quel est l'horodatage de la création du processus en UTC de cette porte dérobée ?
`2020-03-26 23:24:20`

Le flag est donc `FCSC{36280:fd:6663:7363:1000:55cf:b9c6:f41d:cc24:2020-03-26 23:24:20}`.

## Rédaction

Créons un fichier `test.docx` avec libreoffice. Si on regarde le contenue du fichier, on voit que c'est juste un `.zip`.
Le contenu textuel du fichier se trouve dans `document.xml`. Et plus particulièrement après une balise `<w:body>`.
Il reste plus qu'à `grep` cette balise pour trouver le contenu du fichier recherché.

Le flag est donc `PQHJRTSFYH-3467024-LSHRFLDFGA`.

## Administration

On va utiliser ce programme : https://github.com/congwang/rsakeyfind.
Il nous trouve 2 clés privées identiques.
On récupère comme information : `n`, `e` et `d`.
C'est suffisant pour récupérer le message chiffré.
On crée un script python `academie_administration.py` pour décoder le message.

Le flag est donc `FCSC{ac5cad66114d4866a4b55e43cb8896cc4947855241b5af8d2f8a123c36083d98}`.

## Dans les nuages

Je n'ai pas réussi ce chall, je laisse juste ici quelques infos que j'avais.

518175248 mdp.kdbx - KeePass

837028696 Panel-o/
837028728 userCol
837028808 Admin3

ETag: "5e7ca98d-e"

/home/Lesage/.ssh/id_rsa
/home/Lesage/Documents/lu1196159e8v28.tmp
/home/Lesage/Documents/note.docx
/home/Lesage/Documents/rapport-f.docx
/home/Lesage/Documents/temp/rapport-prez.docx
/home/Lesage/Pictures/Screenshot_2020-03-26_23-59-01.png

/home/Lesage/Downloads/LinuxForensicsForNon-LinuxFolks.pdf
/home/Lesage/Downloads/event_log
/home/Lesage/Downloads/audio_debug
/home/Lesage/.mozilla/firefox/peyjyk3f.default-esr/key4.db
/home/Lesage/.mozilla/firefox/peyjyk3f.default-esr/cookies.sqlite
/home/Lesage/.mozilla/firefox/peyjyk3f.default-esr/cookies.sqlite-wal

sql:/home/Lesage/.pki/nssd

TCP      10.42.42.131    :60750 10.42.42.132    :   80 CLOSE_WAIT               chromium/119187

119577 1001   1001   smbclient //10.42.42.128/users -U Compta -W PAQUERETTE          

/var/log/samba/log.smbclient
/etc/samba/smbpasswd