---
title: "Including a command within the wiki/fr"
slug: "including_a_command_within_the_wiki"
lang: "fr"

source_wiki_title: "Including a command within the wiki/fr"
source_hash: "0089c05ff38b5402eb52367c71ded2fc"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:20:29.865520+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Pour inclure une commande dans le wiki, il faut utiliser le gabarit `{{Commande}}`. Ce gabarit détecte la syntaxe **bash**. Par exemple, le code :
```text
{{Commande|cd src; make && make install; cd ..}}
```
produit le résultat :
```bash
cd src; make && make install; cd ..
```

## Caractères spéciaux "=" et "|"

Puisque `{{Commande}}` est un gabarit, les signes "=" et "|" sont interprétés par le wiki.

Pour inclure le signe "égal", utilisez `{{=}}`.
Par exemple, le code :
```text
{{Commande|./configure --prefix{{=}}$HOME && make && make install}}
```
produit le résultat :
```bash
./configure --prefix=$HOME && make && make install
```
Pour le trait vertical, utilisez `{{!}}`.

## Inclure un ensemble de commandes

Vous pouvez utiliser le gabarit `{{Commands}}` pour inclure un ensemble de commandes. Inscrivez alors chaque commande sur une seule ligne, précédée du caractère **|**. Par exemple :
```text
{{Commands
|cd src
|make
|make install
|cd ..
}}
```
produit le résultat :
```bash
cd src
make
make install
cd ..
```

## Modifier l'invite de commande

Si vous voulez modifier l'invite de commande (*invite de commande*), vous pouvez le faire en ajoutant un paramètre `prompt`. Par exemple :
```text
{{Command|prompt=[nom@briaree $]|cd src; make && make install; cd ..}}
```
produit le résultat :
```bash
[name@briaree $] cd src; make && make install; cd ..
```

De même,
```text
{{Commands
|prompt=[name@briaree $]
|cd src
|make
|make install
|cd ..
}}
```
produit le résultat :
```bash
[name@briaree $] cd src
[name@briaree $] make
[name@briaree $] make install
[name@briaree $] cd ..
```

## Afficher le résultat d'une commande

Vous pouvez afficher le résultat d'une commande (et d'une seule) en ajoutant l'option `resultat`. Par exemple :
```text
{{Command
|df -h .
|resultat=
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home
}}
```
produit le résultat :
```bash
df -h .
Sys. de fich.         Tail. Occ. Disp. %Occ. Monté sur
/lustre2/home         516T  340T  150T  70% /home