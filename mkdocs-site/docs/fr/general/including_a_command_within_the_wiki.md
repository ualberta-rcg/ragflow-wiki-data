---
title: "Including a command within the wiki/fr"
tags:
  []

keywords:
  []
---

Pour inclure une commande dans le wiki, il faut utiliser le gabarit <nowiki>
```bash

```
</nowiki>. Ce gabarit détecte la syntaxe **bash**. Par exemple, le code
<syntaxhighlight lang=text>

```bash
cd src; make && make install; cd ..
```

</syntaxhighlight>
produit le résultat :

```bash
cd src; make && make install; cd ..
```

== Caractères spéciaux "" et "" ==
Puisque <nowiki>
```bash

```
</nowiki> est un gabarit, les signes "=" et "|" sont interprétés par le wiki.

Pour inclure le signe "égal" utilisez <nowiki></nowiki>. 
Par exemple, le code
<syntaxhighlight lang=text>

```bash

```
$HOME && make && make install}}
</syntaxhighlight>
produit le résultat :

```bash

```
$HOME && make && make install}}
Pour le trait vertical, utilisez <nowiki></nowiki>.

## Inclure un ensemble de commandes 
Vous pouvez utiliser le gabarit <nowiki>
```bash

```
</nowiki> pour inclure un ensemble de commandes. Inscrivez alors chaque commande sur une seule ligne, précédée du caractère **|**. Par exemple,
<syntaxhighlight lang=text>

```bash
cd ..
```

</syntaxhighlight>
produit le résultat :

```bash
cd ..
```

## Modifier l'invite de commande 
Si vous voulez modifier l'invite de commande (*prompt*), vous pouvez le faire en ajoutant un paramètre **prompt**. Par exemple :
<syntaxhighlight lang=text>
```bash
cd src; make && make install; cd ..
```
</syntaxhighlight>
produit le résultat :

```bash
cd src; make && make install; cd ..
```

De même, 
<syntaxhighlight lang=text>

```bash
cd ..
```

</syntaxhighlight>
produit le résultat :

```bash
cd ..
```

## Afficher le résultat d'une commande 
Vous pouvez afficher le résultat d'une commande (et d'une seule) en ajoutant l'option <tt>resultat</tt>. Par exemple, 
<syntaxhighlight>

```bash
resultat=
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
```

</syntaxhighlight>
produit le résultat : 

```bash
resultat=
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
```