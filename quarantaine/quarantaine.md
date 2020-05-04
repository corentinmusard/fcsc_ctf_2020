# Quarantaine

Outil utilisé pour simplifier les circuits : https://github.com/hneemann/Digital

On voit que des blocs sont similaires. Simplifions-les.

Le bloc en entrée de x_{0} vaut toujours 0.
```
a_{0} = 0
```
![first](https://github.com/corentinmusard/<todo>/blob/master/img/first.png "first")

Le bloc en entrée de x_{39} vaut toujours 1.
```
a_{39} = 1
```
![last](https://github.com/corentinmusard/<todo>/blob/master/img/last.png "last")

Les autres blocs en entrée permettent d'échanger les bits.
```
x_{n} = a_{n+1}
x_{n+1} = a_{n}
```
![swap](https://github.com/corentinmusard/<todo>/blob/master/img/swap.png "swap")

Les blocs en sortie sont en faites des `xor`.
```
y = c ^ d
```
![xor](https://github.com/corentinmusard/<todo>/blob/master/img/xor.png "xor")

Il reste plus qu'à faire le reste du circuit.
![quarantaine](https://github.com/corentinmusard/<todo>/blob/master/img/quarantaine.png "quarantaine")

On récupère l'équation simplifié.
Il reste plus qu'à le programmer dans `quarantaine.c`.
Bon, seulement la fonction réciproque était necessaire, mais j'y avais pas pensé.
