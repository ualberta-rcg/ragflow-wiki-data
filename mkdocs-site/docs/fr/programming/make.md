---
title: "Make/fr"
tags:
  []

keywords:
  []
---

## Description 
[make](https://fr.wikipedia.org/wiki/Make) est un logiciel qui construit automatiquement des bibliothèques ou des fichiers souvent exécutables, à partir d'éléments de base tels que du code source.

La commande <tt>make</tt> interprète et exécute les instructions du fichier <tt>makefile</tt>.  À la différence d'un simple script, <tt>make</tt> exécute les commandes seulement si elles sont nécessaires.  Le but est d'arriver à un résultat (logiciel compilé ou installé, documentation créée, etc.) sans nécessairement refaire toutes les étapes. 

Dans le fichier <tt>makefile</tt> se trouvent, entre autres, des informations sur les dépendances. 
Par exemple, puisque l'exécutable du programme dépend des fichiers source, si certains de ces fichiers ont changé, un réassemblage du programme est nécessaire. 
De la même manière, les fichiers objets dépendant de leurs fichiers sources associés, si un fichier source a été modifié, ce dernier doit être recompilé pour recréer le nouveau fichier objet.  
Toutes ces dépendances doivent être incluses dans le fichier <tt>makefile</tt>.  Ainsi, il n'est plus nécessaire de recompiler tous les fichiers sources à chaque modification; la commande <tt>make</tt>  s'occupe de recompiler et réassembler uniquement ce qui est nécessaire.

== Exemples d'utilisation == 
Le principal argument de la commande <tt>make</tt> est généralement la cible.  Il s'agit de la composante que <tt>make</tt> doit construire.  
Les cibles disponibles dépendent du contenu du <tt>makefile</tt>, mais certaines cibles sont très communes, par exemple *all*, *test*, *check*, *clean* et *install*,
qui sont souvent employées. Dans l'exemple suivant de <tt>make</tt>, aucune cible n'est spécifiée.

```bash
make
```

Le comportement typique est de tout construire, soit l'équivalent de

```bash
make all
```

Les cibles *test* ou *check* sont généralement utilisées pour exécuter des tests afin de valider que l'application ou la bibliothèque compilée fonctionne correctement.  De façon générale, ces cibles sont dépendantes de la cible *all*.  Vous pouvez ainsi vérifier la compilation via la commande

```bash
make all && make check
```

ou

```bash
make all && make test
```

La cible *clean* efface tous les fichiers binaires compilés précédemment afin de reprendre la compilation de zéro.  Il existe parfois aussi la cible *distclean* qui efface non seulement les fichiers créés par <tt>make</tt>, mais aussi les fichiers créés lors de l'opération de configuration par [configure](autotools.md) ou [cmake](cmake.md).  Ainsi, pour nettoyer le répertoire de compilation, vous pouvez généralement exécuter

```bash
make clean
```

et parfois

```bash
make distclean
```

La cible *install* procède normalement à l'installation de l'application ou de la bibliothèque compilée.  L'emplacement de l'installation dépend du <tt>makefile</tt>, mais peut souvent se modifier via un paramètre additionnel *prefix* ainsi&nbsp; :

```bash

```
$HOME/PROGRAM}}

Ces cibles  <tt>all, test, check, clean, distclean</tt> et <tt>install</tt> ne sont cependant que des conventions et l'auteur d'un <tt>makefile</tt> pourrait très bien choisir une autre convention.  Pour davantage d'information sur les cibles typiques, notamment supportées par toutes les applications GNU, consultez [cette page](http://www.gnu.org/software/make/manual/make.html#Standard-Targets).  Les options pour configurer les répertoires d'installation et autres sont quant à elles listées [ici](http://www.gnu.org/software/make/manual/make.html#Directory-Variables).

== Exemple de <tt>Makefile</tt> == 
L'exemple suivant, d'utilisation générale, inclut beaucoup d'explications et de commentaires.  Pour un guide approfondi sur la création de fichiers <tt>makefile</tt>, visitez le [site Web GNU Make](http://www.gnu.org/software/make/manual/make.html#Introduction).