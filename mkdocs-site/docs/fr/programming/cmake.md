---
title: "CMake/fr"
tags:
  []

keywords:
  []
---

## Description 
[CMake](http://www.cmake.org/) (pour <i>cross-platform make</i>) est un outil de compilation libre multiplateforme et multilangage. Alors que [Autotools](autotools-fr.md) est l'outil traditionnel sous Linux (utilisé entre autres pour tous les projets GNU), plusieurs projets sont passés à CMake au cours des dernières années, et ce pour différentes raisons, entre autres KDE et MySQL. Ceux qui ont éprouvé certaines difficultés à construire leur propre projet avec Autotools trouveront probablement CMake beaucoup plus facile d'utilisation. Selon KDE, les principales raisons pour lesquelles ils sont passés de Autotools à CMake sont que la compilation est beaucoup plus rapide et que les fichiers de construction sont beaucoup plus faciles à écrire.

## Principe de base 
CMake fonctionne de la même manière que Autotools et requiert l'exécution d'un script `configure`, suivi d'un <i>build</i> avec `make`. Cependant, plutôt qu'appeler `./configure`, on appelle <code>cmake <i>directory</i></code>. Par exemple, si on est dans le répertoire où l'on veut construire l'application, on exécute

```bash
cmake .
```

Ainsi, pour configurer, construire et installer une application ou une bibliothèque, la façon la plus simple est avec

```bash
cmake . && make && make install
```

## Options utiles pour travailler avec les grappes 
Nos grappes sont configurées de telle sorte qu'à la compilation d'un nouveau paquet logiciel, l'information est automatiquement ajoutée au binaire résultant afin qu'il puisse trouver les bibliothèques desquelles il dépend; le mécanisme utilisé est `RUNPATH` (ou `RPATH`). Certains paquets qui utilisent CMake font de même avec une fonctionnalité offerte par CMake. Des conflits sont parfois créés quand les deux sont utilisés en même temps; pour éviter ceci, ajouter l'option 

* `-DCMAKE_SKIP_INSTALL_RPATH=ON`

en ligne de commande. Aussi, les bibliothèques de nos grappes sont installées dans des endroits non standards et il est difficile pour CMake de les trouver; il peut être utile d'ajouter sur la ligne de commande l'option 

* `-DCMAKE_SYSTEM_PREFIX_PATH=$EBROOTGENTOO`

Parfois, même cela n'est pas suffisant et vous pourriez devoir ajouter des options plus spécifiques aux bibliothèques utilisées par votre paquet logiciel, par exemple : 
* `-DCURL_LIBRARY=$EBROOTGENTOO/lib/libcurl.so -DCURL_INCLUDE_DIR=$EBROOTGENTOO/include`
* `-DPYTHON_EXECUTABLE=$EBROOTPYTHON/bin/python`
* `-DPNG_PNG_INCLUDE_DIR=$EBROOTGENTOO/include -DPNG_LIBRARY=$EBROOTGENTOO/lib/libpng.so`
* `-DJPEG_INCLUDE_DIR=$EBROOTGENTOO/include -DJPEG_LIBRARY=$EBROOTGENTOO/lib/libjpeg.so`
* `-DOPENGL_INCLUDE_DIR=$EBROOTGENTOO/include -DOPENGL_gl_LIBRARY=$EBROOTGENTOO/lib/libGL.so -DOPENGL_glu_LIBRARY=$EBROOTGENTOO/lib/libGLU.so`
* `-DZLIB_ROOT=$EBROOTGENTOO`

## Personnalisation de la configuration 
Tout comme avec Autotools, il est possible de personnaliser la configuration de l'application ou de la bibliothèque. Cela peut se faire par différentes options de la ligne de commande, mais aussi via une interface texte avec la commande `ccmake`.

### Commande `ccmake` 
La commande `ccmake` est appelée de la même façon que la commande `cmake`, en indiquant le répertoire à construire. S'il s'agit du répertoire courant, la commande est

```bash
ccmake .
```

Il faut appeler `ccmake` <i>après</i> avoir appelé `cmake`&nbsp;: en général, la commande est

```bash
cmake . && ccmake .
```

`ccmake` affiche d'abord la liste des options définies par le projet. Le résultat est une liste relativement courte semblable à ceci :

```bash
cmake . && ccmake .
```

```
Page 1 of 1
 ARPACK_LIBRARIES                 ARPACK_LIBRARIES-NOTFOUND
 CMAKE_BUILD_TYPE
 CMAKE_INSTALL_PREFIX             /usr/local
 CMAKE_OSX_ARCHITECTURES
 CMAKE_OSX_DEPLOYMENT_TARGET
 CMAKE_OSX_SYSROOT                /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk
 GSL_CONFIG                       /opt/local/bin/gsl-config
 GSL_CONFIG_PREFER_PATH           /bin;;/bin;
 GSL_EXE_LINKER_FLAGS             -Wl,-rpath,/opt/local/lib
 NON_TEMPLATES_DISABLED           ON
 NO_SQUACK_WARNINGS               ON
 PRECOMPILED_TEMPLATES            ON
 USE_GSL_OMP                      OFF
 USE_OMP                          OFF
Press [enter] to edit option                                                                                                                                                         CMake Version 2.8.8
Press [c] to configure
Press [h] for help           Press [q] to quit without generating
Press [t] to toggle advanced mode (Currently Off)
```

Comme indiqué au bas de cette liste, vous pouvez éditer une valeur en appuyant sur la touche `Enter`. Si vous modifiez une valeur, appuyez sur la touche `c` pour tester la configuration avec cette nouvelle valeur. Si la configuration réussit, vous aurez alors l'option `g`, pour générer le `Makefile` avec la nouvelle configuration, ou vous pouvez quitter avec la touche `q`. Le mode avancé est activé avec la touche `t`, ce qui produit une liste beaucoup plus longue de variables qui permettra de configurer l'application avec précision. Voici un exemple de liste d'options&nbsp;:

Remarquez que `ccmake` en mode avancé affiche aussi bien les bibliothèques trouvées que celles qui n'ont pas été trouvées. Si vous voulez utiliser une certaine version de [BLAS](blas-and-lapack-fr.md) par exemple, vous saurez immédiatement si c'est celle que CMake a trouvée et, le cas échéant, pourrez la modifier. `ccmake` affiche aussi la liste des options passées aux compilateurs et à l’éditeur de liens, et ce, en fonction du type de construction. 

### Options en ligne de commande
Les options affichées par `ccmake` peuvent toutes être modifiées en ligne de commande, avec la syntaxe

```bash

```
VALEUR}}

Par exemple, pour spécifier l'emplacement d'installation :

```bash

```
/home/user/mon_repertoire}}

Pour configurer la compilation, vous voudrez possiblement changer les valeurs suivantes :
{| class="wikitable" style="font-size: 95%; text-align: center;"
!Option
!Description
|-
!`CMAKE_C_COMPILER`
|change le compilateur C
|-
!`CMAKE_CXX_COMPILER`
|change le compilateur C++
|- 
!`CMAKE_LINKER`
|change l'éditeur de liens
|-
!`CMAKE_C_FLAGS`
|change les options passées au compilateur C
|-
!`CMAKE_CXX_FLAGS`
|change les options passées au compilateur C++
|-
!`CMAKE_SHARED_LINKER_FLAGS`
|change les options passées à l'éditeur de liens
|-
|}
La liste complète des options est disponible sur la [page officielle de CMake](http://www.cmake.org/Wiki/CMake_Useful_Variables). 

Si vous ne voulez pas vous aventurer dans ces options spécifiques, CMake propose une option plus simple avec `CMAKE_BUILD_TYPE`, qui définit le type de compilation à utiliser. Les valeurs possibles sont
{| class="wikitable" style="font-size: 95%; text-align: center;"
!Option
!Description
|-
! -
| aucune valeur
|-
! Debug
| active les options de débogage, désactive les options d'optimisation
|- 
! Release
| désactive les options de débogage, active les optimisations typiques
|-
! MinSizeRel
| désactive les options de débogage, active les options d'optimisation en minimisant la taille du binaire
|-
! RelWithDebInfo
| active les options de débogage et les optimisations typiques
|-
|}
Ces différents types de compilation définissent des options de compilateurs qui varient selon le compilateur utilisé; vous n'avez donc pas à vérifier quelles options doivent être utilisées.

## Références 

* [Guide d'initiation en français](http://florian-goujeon.developpez.com/cours/cmake/initiation/) qui couvre aussi bien la création de fichiers CMake que la compilation d'un projet déjà fait.
* [Exemple simple (en anglais)](http://www.cmake.org/cmake/help/examples.html) sur le site officiel.
* [Tutoriel (en anglais)](http://www.cmake.org/cmake/help/cmake_tutorial.html) plutôt complet sur le site officiel.
* [Tutoriel assez complet en français](http://rachid.koucha.free.fr/tech_corner/cmake_manual_fr.html).