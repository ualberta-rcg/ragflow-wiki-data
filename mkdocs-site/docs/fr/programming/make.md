---
title: "Make/fr"
slug: "make"
lang: "fr"

source_wiki_title: "Make/fr"
source_hash: "5a646e5ef71768da5f7854023e58983c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:23:30.075861+00:00"

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

## Description
[make](https://fr.wikipedia.org/wiki/Make) est un logiciel qui construit automatiquement des bibliothèques ou des fichiers, souvent exécutables, à partir d'éléments de base tels que du code source.

La commande `make` interprète et exécute les instructions du fichier `makefile`. À la différence d'un simple script, `make` exécute les commandes seulement si elles sont nécessaires. Le but est d'arriver à un résultat (logiciel compilé ou installé, documentation créée, etc.) sans nécessairement refaire toutes les étapes.

Dans le fichier `makefile` se trouvent, entre autres, des informations sur les dépendances.
Par exemple, puisque l'exécutable du programme dépend des fichiers sources, si certains de ces fichiers ont changé, un réassemblage du programme est nécessaire.
De la même manière, les fichiers objets dépendant de leurs fichiers sources associés, si un fichier source a été modifié, ce dernier doit être recompilé pour recréer le nouveau fichier objet.
Toutes ces dépendances doivent être incluses dans le fichier `makefile`. Ainsi, il n'est plus nécessaire de recompiler tous les fichiers sources à chaque modification; la commande `make` s'occupe de recompiler et réassembler uniquement ce qui est nécessaire.

## Exemples d'utilisation
Le principal argument de la commande `make` est généralement la cible. Il s'agit de la composante que `make` doit construire.
Les cibles disponibles dépendent du contenu du `makefile`, mais certaines cibles sont très communes, par exemple *all*, *test*, *check*, *clean* et *install*, qui sont souvent employées. Dans l'exemple suivant de `make`, aucune cible n'est spécifiée.

```bash
make
```

Le comportement typique est de tout construire, soit l'équivalent de

```bash
make all
```

Les cibles *test* ou *check* sont généralement utilisées pour exécuter des tests afin de valider que l'application ou la bibliothèque compilée fonctionne correctement. De façon générale, ces cibles sont dépendantes de la cible *all*. Vous pouvez ainsi vérifier la compilation via la commande

```bash
make all && make check
```

ou

```bash
make all && make test
```

La cible *clean* efface tous les fichiers binaires compilés précédemment afin de reprendre la compilation de zéro. Il existe parfois aussi la cible *distclean* qui efface non seulement les fichiers créés par `make`, mais aussi les fichiers créés lors de l'opération de configuration par [configure](autotools.md) ou [cmake](cmake.md). Ainsi, pour nettoyer le répertoire de compilation, vous pouvez généralement exécuter

```bash
make clean
```

et parfois

```bash
make distclean
```

La cible *install* procède normalement à l'installation de l'application ou de la bibliothèque compilée. L'emplacement de l'installation dépend du `makefile`, mais peut souvent se modifier via un paramètre additionnel `prefix` ainsi :

```bash
make install prefix=$HOME/PROGRAM
```

Ces cibles `all`, `test`, `check`, `clean`, `distclean` et `install` ne sont cependant que des conventions et l'auteur d'un `makefile` pourrait très bien choisir une autre convention. Pour davantage d'information sur les cibles typiques, notamment supportées par toutes les applications GNU, consultez [cette page](http://www.gnu.org/software/make/manual/make.html#Standard-Targets). Les options pour configurer les répertoires d'installation et autres sont quant à elles listées [ici](http://www.gnu.org/software/make/manual/make.html#Directory-Variables).

## Exemple de makefile
L'exemple suivant, d'utilisation générale, inclut beaucoup d'explications et de commentaires. Pour un guide approfondi sur la création de fichiers `makefile`, visitez le [site Web GNU Make](http://www.gnu.org/software/make/manual/make.html#Introduction).

```make title="Makefile"
# Makefile pour facilement mettre à jour la compilation d'un programme (.out)
# --------
#
# par Alain Veilleux, 4 août 1993
#     Dernière révision,  30 mars 1998
#
# BUT ET FONCTIONNEMENT DU PRÉSENT SCRIPT :
#    Script sous forme makefile permettant de mettre à jour un programme
#    comprenant plusieurs routines séparées sur le disque. Ce script n'est pas  #    exécuté par lui-même, mais est plutôt lu et interprété par la commande 
#    make. Lors de son appel, la commande make vérifie les dates des     
#    différents fichiers composant votre programme compilé. Seulement les 
#    routines ayant été modifiées depuis la compilation du programme final     
#    seront recompilées sous forme objet (fichiers terminés par .o). Les    
#    fichiers .o seront ensuite liés ensemble pour reformer une version mise à #    jour du programme final.
#
# POUR ADAPTER LE PRÉSENT SCRIPT À VOTRE PROGRAMME : 
#    Modifiez le contenu des variables de la section ci-dessous. Des   
#    commentaires vous guideront dans ce sens.
#
# UTILISATION DE make SUR LA LIGNE DE COMMANDE UNIX :
#    1- Tapez «make» pour mettre à jour l'ensemble du programme. 
#    2- Tapez «make NomRoutine» pour mettre à jour seulement la
#          routine NomRoutine.
#


#====================  Définition des variables  ====================
# Remarque : les variables sont parfois appelées des «macros» dans les fichiers Makefile

# Nom du compilateur à utiliser (FORTRAN, C ou autre)
NomCompilateur= xlf

# Options de compilation : ci-dessous, vous trouverez les options normalement 
#                          utilisées pour compiler en FORTRAN. Vous pouvez  
#                          assigner d'autres valeurs que celles suggerées à la 
#                          variable OptionsDeCompilation.
#OptionsDeCompilation= -O3 
# Enlever le caractère # ci-dessous pour activer la compilation en mode debug 
#OptionsDeCompilation= -g 
# Enlever le caractère #  ci-dessous pour utiliser gprof qui indique le temps de
#    calcul de chaque sous-routine
#OptionsDeCompilation= -O3 -pg

# Liste des routines à compiler : on nomme ici les versions objet 
# Placez un \ à la fin de chaque ligne si vous voulez poursuivre la liste 
#    des routines sur la ligne suivante. 
FichiersObjets= trnb3-1.part.o mac4251.o inith.o dsite.o initv.o main.o \
                entree.o gcals.o defvar1.o defvar2.o magst.o mesure.o

# Nom du programme exécutable finalement produit 
ProgrammeOut= trnb3-1.out 

#=====  Fin de la définition des variables  ===== 

#===============  Il n'y a rien à changer à partir d'ici  ===============


# Définit une règle : comment construire un fichier objet (terminé par .o) 
#                   à partir d'un fichier source (terminé par .f) 
# remarque : les symboles $< seront remplacés par le nom du programme à compiler 
# Compilation de programmes en langage Fortran
.f.o:     
	$(NomCompilateur) $(OptionsDeCompilation) -c $<

# Définit une règle : comment construire un fichier objet (terminé par .o) 
#                   à partir d'un fichier source (terminé par .c) 
# remarque : les symboles $< seront remplacés par le nom du programme à compiler 
# Compilation de programmes en langage C  
  
.c.o:
	$(NomCompilateur) $(OptionsDeCompilation) -c $<

 
# Définit une règle : comment construire un fichier objet (terminé par .o) 
#                   à partir d'un fichier source (termine par .C) 
# remarque : les symboles $< seront remplacés par le nom du programme à compiler 
# Compilation de programmes en langage C
    
 .C.o:
	$(NomCompilateur) $(OptionsDeCompilation) -c $<

# Dépendance du programme exécutable envers les fichiers objets (.o) le 
#    composant. 
# La dépendance des fichiers objets envers les fichiers sources (.f et .c) est 
#    sous-entendue par les règles définies plus haut.
$(ProgrammeOut): $(FichiersObjets)
	$(NomCompilateur) $(OptionsDeCompilation) -o $(ProgrammeOut) \
                                            $(FichiersObjets)