---
title: "EasyBuild/fr"
tags:
  []

keywords:
  []
---

[EasyBuild](https://easybuild.io/) est un outil pour la construction, l’installation et la maintenance de logiciels sur les systèmes de calcul de haute performance. Nous l’utilisons pour construire presque tout le contenu de notre [répertoire CVMFS](accessing_cvmfs-fr.md).

= Génération de modules =
Une des fonctionnalités principales d’EasyBuild est sa capacité de générer automatiquement des [modules](utiliser_des_modules.md) d’environnement qui peuvent être utilisés pour rendre un logiciel disponible dans une session. En plus de définir les variables d’environnement standards de Linux telles que  PATH, CPATH et LIBRARY_PATH, EasyBuild définit aussi quelques variables d’environnement qui lui sont spécifiques dont certaines sont d’intérêt pour les utilisateurs&nbsp:
* <code>EBROOT<name></code> qui contient le chemin complet du répertoire où se trouve le logiciel <code><name></code> 
* <code>EBVERSION<name></code> qui contient la version complète du logiciel <code><name></code> chargé par le module

Par exemple, le module `python/3.10.2` sur Narval définit
* `EBROOTPYTHON`: `/cvmfs/soft.computecanada.ca/easybuild/software/2020/avx2/Core/python/3.10.2`
* `EBVERSIONPYTHON`: `3.10.2`

Pour connaître les variables d’environnement définies par le module `python/3.10.2`, utilisez 

```bash

```
 grep EB}}

= Recettes d’installation et journalisation =
EasyBuild conserve une copie de la recette utilisée pour installer chaque paquet logiciel et un journal détaillé dans le répertoire d’installation  <code>$EBROOT<name>/easybuild</code>. Par exemple, pour le module `python/3.10.2`, le répertoire d’installation contient, entre autres
* `$EBROOTPYTHON/easybuild/Python-3.10.2.eb`
* `$EBROOTPYTHON/easybuild/easybuild-Python-3.10.2-*.log`

= Utilisation dans votre compte =
Vous pouvez utiliser EasyBuild pour installer des paquets logiciels dans votre propre compte. Par contre, dans la plupart des cas, il est préférable de demander au [soutien technique](technical-support-fr.md) d’installer ces logiciels pour un usage généralisé, ce qui fait en sorte que le paquet logiciel sera disponible sur toutes nos grappes. Cela évitera aussi d’affecter votre quota et ne causera pas une charge indue sur le système de fichiers parallèle. 

## Qu’est-ce qu’une recette? 

Une recette est un fichier EasyConfig au format texte qui contient l’information dont EasyBuild a besoin pour construire un logiciel donné dans un environnement donné. Les noms sont formés selon la convention  
* <code><name>-<version>-<toolchain name>-<toolchain version>.eb</code>
où <code><name></code> est le nom du paquet, <code><version></code> est la version du paquet, <code><toolchain name></code> est le nom de la chaîne de compilation et  <code><toolchain version></code> est la version de la chaîne de compilation.

## Trouver une recette 
EasyBuild contient plusieurs recettes qui peuvent fonctionner ou non avec nos chaînes de compilation. La meilleure façon d’avoir une recette qui fonctionne est de commencer avec une des recettes que nous avons installées. Vous pouvez les trouver dans le répertoire d'installation, tel que décrit ci-haut, ou encore dans le répertoire `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO` folder. 

## Installer un logiciel avec EasyBuild 
Une fois que vous avez trouvé une recette qui vous satisfait, copiez-la du répertoire `/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO` et modifiez-la au besoin. Lancez ensuite

```bash
eb <recipe.eb>
```

Ceci installe le logiciel dans votre répertoire /home dans `$HOME/.local/easybuild`. Quand l’installation est terminée, fermez votre session et reconnectez-vous à la grappe. Le logiciel devrait alors pouvoir être chargé avec un module.

### Réinstaller une version existante 
Si vous réinstallez une version que nous avons  installée pour usage généralisé, mais que vous voulez en modifier les paramètres, vous devrez utiliser 

```bash
eb <recipe.eb> --force
```

pour installer une version locale dans votre répertoire /home.

### Installer ailleurs que dans /home 
Pour installer un paquet logiciel dans votre espace /project par exemple, utilisez 

```bash
eb <recipe.eb> --installpath /path/to/your/project/easybuild
```

Pour que ces modules soient disponibles dans vos sessions, utilisez

```bash

```
/path/to/your/project/easybuild/modules}}
Pour que ces modules soient disponibles par défaut dans vos sessions, ajoutez cette commande au fichier `.bashrc`  de votre répertoire /home.

= Pour plus d'information =

* [<i>Building software on Compute Canada clusters using EasyBuild</i>](https://westgrid.github.io/trainingMaterials/getting-started/#building-software-with-easybuild), webinaire
* [Documentation pour notre équipe technique](https://github.com/ComputeCanada/software-stack/blob/main/doc/easybuild.md)
* [Tutoriels](https://easybuild.io/tutorial/)