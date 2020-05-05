# Rustique

Pour ce challenge, on doit lire le contenu d'un fichier `flag.txt`. On peut seulement compiler du code Rust, et savoir si la compilation a échouée ou non.

## Récupérer la taille

### Payload

```rust
let my_string : &[u8; 4] = include_bytes!("/flag.txt");
```

### Explication

La chose importante utilisée ici est la macro `include_bytes!("fichier")`.
La macro va être remplacer par le contenu du fichier en argument.

Le type renvoyé est `&[u8; n]` avec `n` la longueur de la chaine.
On peut donc tester en modifiant `n` à chaque fois.
Si ça compile, c'est que c'est le bon `n`.

On trouve une longueur de 71.

## Récuperer le contenu

### Payload

```rust
const VALUE: i8 = 1 / (include_bytes!("/flag.txt")[4] as i8 - b'F' as i8);
```

### Explication

Pour le contenu du fichier, on essaie de faire une division du type `1 / (flag[i] - c)`.
Si `flag[i] == c` alors il y a une division par 0 et donc la compilation échoue.
Sinon ça compile.

`FCSC{a35036487430b24da38b43e1369f56e69a25bd39e594cd1e7ff3e97b62b3c638}`
