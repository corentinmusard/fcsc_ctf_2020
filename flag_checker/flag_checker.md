# Flag checker

Après analyse du code source, on voit que la vérification du flag appelle la fonction `_check` du fichier `index.js`.
```js
var _check = Module["_check"] = function ()
{
    return (_check = Module["_check"] = Module["asm"]["b"]).apply(null, arguments)
};
```
Dans la console (F12) :
```js
>> Module['asm']['b']
function 4()

>> Module['asm']['b'].toString()
function() {
    [native code]
}
```

Le code de la fonction n'est pas disponible.
On voit dans `index.js` que le fichier `index.wasm` est utilisé.
On le télécharge est on le désassemble avec `wasm2wat` de `https://github.com/WebAssembly/wabt`.

```sh
# raccourci pour le wu

(func (;4;) (type 0) (param i32) (result i32)
    (local i32 i32)
    local.get 0
    i32.load8_u
    local.tee 2
    if  ;; label = @1
      local.get 0
      local.set 1
      loop  ;; label = @2
        local.get 1
        local.get 2
        i32.const 3
        i32.xor
        i32.store8
        local.get 1
        i32.load8_u offset=1
        local.set 2
        local.get 1
        i32.const 1
        i32.add
        local.set 1
        local.get 2
        br_if 0 (;@2;)
      end
    end
    local.get 0
    call 3
    i32.eqz)

# raccourci pour le wu

(data (;0;) (i32.const 1024) "E@P@x4f1g7f6ab:42`1g:f:7763133;e0e;03`6661`bee0:33fg732;b6fea44be34g0~"))
```

La fonction `4` effectue un xor entre le nombre `3` et la chaine en dessous, puis appelle la fonction `3` que je n'ai pas mis ici.
Si on effectue ce xor, on récupère le flag.
La fonction `3` doit être une fonction de comparaison de chaine.
