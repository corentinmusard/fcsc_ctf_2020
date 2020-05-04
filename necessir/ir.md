# NECessIR

Il faut diminuer la vitesse du fichier audio pour obtenir quelque chose de comprehensible (voir fichier `ir-.mp3`). J'ai utiliser `audacity` pour ça.
On entends maintenant des "bips" régulier.

Un tour sur google avec les mots clef "infrared NEC" nous indique qu'il s'agit du protocole NEC.

Lien utile : https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol

Le texte et le schéma du site suffit à comprendre comment décoder le signal.

J'ai récupérer le binaire à la main, puis je l'ai convertis en ascii avec `ir.py`.
