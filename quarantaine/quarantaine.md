# Quarantaine

Outil utilisé pour simplifier les circuits : https://github.com/hneemann/Digital

On voit que des blocs sont similaires. Simplifions-les.

Le bloc en entrée de x_{0} vaut toujours 0.
```
a_{0} = 0
```
![first](first.png "first")

Le bloc en entrée de x_{39} vaut toujours 1.
```
a_{39} = 1
```
![last](last.png "last")

Les autres blocs en entrée permettent d'échanger les bits.
```
x_{n} = a_{n+1}
x_{n+1} = a_{n}
```
![swap](swap.png "swap")

Les blocs en sortie sont en faites des `xor`.
```
y = c ^ d
```
![xor](xor.png "xor")

Il reste plus qu'à faire le reste du circuit.
![quarantaine](quarantaine.png "quarantaine")

On récupère l'équation simplifié.
Il reste plus qu'à le programmer dans [quarantaine.c](quarantaine.c).
Bon, seulement la fonction réciproque était necessaire, mais j'y avais pas pensé.
