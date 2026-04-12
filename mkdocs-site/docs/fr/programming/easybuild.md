---
title: "EasyBuild/fr"
slug: "easybuild"
lang: "fr"

source_wiki_title: "EasyBuild/fr"
source_hash: "f1083ee3bf20904fce76266772fd1cdf"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:56:19.860576+00:00"

tags:
  []

keywords:
  - "recette"
  - "chaîne de compilation"
  - "easybuild"
  - "installation"
  - "logiciels"
  - "modules d'environnement"
  - "Compute Canada"
  - "construire un logiciel"
  - "module"
  - "commande eb"
  - "installation de logiciel"
  - "installation locale"
  - "répertoire /project"
  - "calcul de haute performance"
  - "réinstaller une version"
  - "EasyBuild"
  - "fichier EasyConfig"
  - "convention"
  - "modules"
  - "recettes d'installation"

questions:
  - "Quelles sont les variables d'environnement spécifiques générées par EasyBuild lors de la création d'un module et que contiennent-elles ?"
  - "Où EasyBuild conserve-t-il les recettes d'installation et les journaux détaillés pour chaque paquet logiciel installé ?"
  - "Dans quelles situations précises est-il justifié d'utiliser EasyBuild pour installer un logiciel dans son propre compte plutôt que de faire appel au soutien technique ?"
  - "Où peut-on trouver les recettes EasyBuild préinstallées pour s'assurer de leur compatibilité ?"
  - "Qu'est-ce qu'une chaîne de compilation et de quels composants logiciels est-elle formée ?"
  - "Quelles sont les commandes et les étapes requises pour installer ou réinstaller un logiciel avec EasyBuild dans son répertoire personnel ?"
  - "Qu'est-ce qu'une recette dans le contexte d'EasyBuild et quel type d'information contient-elle ?"
  - "Quelle est la méthode la plus simple et recommandée pour obtenir une recette fonctionnelle ?"
  - "Quelle est la convention de nommage spécifique utilisée pour les fichiers EasyConfig ?"
  - "Dans quel répertoire l'installation du logiciel s'effectue-t-elle ?"
  - "Quelles étapes doivent être suivies après l'installation pour pouvoir charger le logiciel avec un module ?"
  - "Quelle commande permet de réinstaller une version existante pour en modifier les paramètres ?"
  - "Quelle commande doit-on utiliser pour installer un paquet logiciel dans un répertoire spécifique autre que /home ?"
  - "Comment configurer la session courante pour rendre accessibles les modules installés dans un chemin personnalisé ?"
  - "Que faut-il ajouter au fichier .bashrc pour que ces modules soient disponibles par défaut à chaque nouvelle session ?"
  - "Quelle commande doit-on utiliser pour installer un paquet logiciel dans un répertoire spécifique autre que /home ?"
  - "Comment configurer la session courante pour rendre accessibles les modules installés dans un chemin personnalisé ?"
  - "Que faut-il ajouter au fichier .bashrc pour que ces modules soient disponibles par défaut à chaque nouvelle session ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[EasyBuild](https://easybuild.io/) est un outil pour la construction, l’installation et la maintenance de logiciels sur les systèmes de calcul de haute performance. Nous l’utilisons pour construire presque tout le contenu de notre [répertoire CVMFS](../software/cvmfs/accessing_cvmfs.md).

## Génération de modules
Une des fonctionnalités principales d’EasyBuild est sa capacité de générer automatiquement des [modules d’environnement](utiliser_des_modules.md) qui peuvent être utilisés pour rendre un logiciel disponible dans une session. En plus de définir les variables d’environnement standards de Linux telles que PATH, CPATH et LIBRARY_PATH, EasyBuild définit aussi quelques variables d’environnement qui lui sont spécifiques dont certaines sont d’intérêt pour les utilisateurs :

*   ``EBROOT<name>`` qui contient le chemin complet du répertoire où se trouve le logiciel ``<name>``
*   ``EBVERSION<name>`` qui contient la version complète du logiciel ``<name>`` chargé par le module

Par exemple, le module ``python/3.10.2`` sur Narval définit :

*   ``EBROOTPYTHON``: ``/cvmfs/soft.computecanada.ca/easybuild/software/2020/avx2/Core/python/3.10.2``
*   ``EBVERSIONPYTHON``: ``3.10.2``

Pour connaître les variables d’environnement définies par le module ``python/3.10.2``, utilisez :
```bash
module show python/3.10.2 | grep EB
```

## Recettes d’installation et journalisation
EasyBuild conserve une copie de la recette utilisée pour installer chaque paquet logiciel et un journal détaillé dans le répertoire d’installation ``$EBROOT<name>/easybuild``. Par exemple, pour le module ``python/3.10.2``, le répertoire d’installation contient, entre autres :

*   ``$EBROOTPYTHON/easybuild/Python-3.10.2.eb``
*   ``$EBROOTPYTHON/easybuild/easybuild-Python-3.10.2-*.log``

## Utilisation dans votre compte
Vous pouvez utiliser EasyBuild pour installer des paquets logiciels dans votre propre compte. Par contre, dans la plupart des cas, il est préférable de demander au [soutien technique](../support/technical_support.md) d’installer ces logiciels pour un usage généralisé, ce qui fait en sorte que le paquet logiciel sera disponible sur toutes nos grappes. Cela évitera aussi d’affecter votre quota et ne causera pas une charge indue sur le système de fichiers parallèle.

!!! warning "Quand utiliser EasyBuild pour installer un logiciel dans votre répertoire /home"
    Les cas suivants justifient l’utilisation d’EasyBuild :

    *   vous avez besoin d’un logiciel modifié ou personnalisé
    *   vous avez besoin d’installer un logiciel qui change chaque jour, ou qui n’a pas de numéro de version
    *   il ne nous est pas possible d’installer le paquet pour utilisation généralisée pour des raisons de licence, en particulier dans le cas des logiciels commerciaux [VASP](../software/vasp.md) et [Materials Studio](../software/materials_studio.md).

    Au contraire, **il ne faut pas** installer des paquets logiciels dans votre propre espace :

    *   si vous avez besoin d’une version différente
    *   si vous avez besoin d’un paquet logiciel construit avec un compilateur différent, avec MPI ou avec une implémentation CUDA

    Si vous hésitez, contactez le [soutien technique](../support/technical_support.md).

## Qu’est-ce qu’une recette?
!!! note
    Nous n’abordons pas ici la création d’une recette de toutes pièces; au besoin, consultez la [documentation d'EasyBuild](https://docs.easybuild.io/en/latest/Writing_easyconfig_files.html). Il est plus facile de modifier une recette existante ou encore de trouver une recette que vous pourrez utiliser telle quelle.

Une recette est un fichier EasyConfig au format texte qui contient l’information dont EasyBuild a besoin pour construire un logiciel donné dans un environnement donné. Les noms sont formés selon la convention :

*   ``<name>-<version>-<toolchain name>-<toolchain version>.eb``

où ``<name>`` est le nom du paquet, ``<version>`` est la version du paquet, ``<toolchain name>`` est le nom de la chaîne de compilation et ``<toolchain version>`` est la version de la chaîne de compilation.

## Trouver une recette
EasyBuild contient plusieurs recettes qui peuvent fonctionner ou non avec nos chaînes de compilation. La meilleure façon d’avoir une recette qui fonctionne est de commencer avec une des recettes que nous avons installées. Vous pouvez les trouver dans le répertoire d'installation, tel que décrit ci-haut, ou encore dans le répertoire ``/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO``.

!!! info "Chaîne de compilation (*toolchain*)"
    Une chaîne de compilation est un ensemble formé d’un compilateur, d’une implémentation MPI, d’une version de CUDA et de bibliothèques mathématiques; cet ensemble sert à compiler le paquet logiciel. Les noms des chaînes de compilation sont souvent étranges, par exemple ``gofbc`` qui est une combinaison de GCC, OpenMPI, FlexiBlas et CUDA. Il n’est pas nécessaire de se souvenir de la composition d’une chaîne parce qu'elles-mêmes ont des recettes qu’on trouve aussi dans le répertoire ``/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO``. Par exemple, la chaîne ``gofbc`` version ``2020.1.403.114`` contient, comme décrit dans ``/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO/gofbc/gofbc-2020.1.403.114.eb``:

    ```python
    local_gccver = '9.3.0'

    # specify subtoolchains as builddependencies
    # this way they will be considered as subtoolchains but
    # are not loaded in the modulefile or software compiled
    # with this toolchain
    builddependencies = [
        ('gccflexiblascuda', '2020.1.114'),
        ('gompic', version),
    ]

    dependencies = [
        ('GCC', local_gccver),  # part of gcccuda
        ('CUDA', '11.4', '', ('GCC', local_gccver)),  # part of gcccuda
        ('OpenMPI', '4.0.3', '', ('gcccuda', '2020.1.114')),
        ('FlexiBLAS', '3.0.4'),
    ]
    ```

    Ceci signifie que cette chaîne contient GCC 9.3.0, OpenMPI 4.0.3, CUDA 11.4 et FlexiBLAS 3.0.4. La section ``builddependencies`` indique que la chaîne ``gofbc`` est un surensemble des chaînes ``gompic`` et ``gccflexiblascuda``. Quand une chaîne de compilation est un surensemble d’autres chaînes de compilation, les paquets logiciels construits avec le surensemble peuvent dépendre de paquets logiciels construits avec les sous-chaînes. Dans cet exemple, les paquets logiciels construits avec ``gofbc`` peuvent dépendre de paquets logiciels construits avec ``gompic``, mais le contraire est impossible.

## Installer un logiciel avec EasyBuild
Une fois que vous avez trouvé une recette qui vous satisfait, copiez-la du répertoire ``/cvmfs/soft.computecanada.ca/easybuild/ebfiles_repo/$EBVERSIONGENTOO`` et modifiez-la au besoin. Lancez ensuite :
```bash
eb <recipe.eb>
```
Ceci installe le logiciel dans votre répertoire /home dans ``$HOME/.local/easybuild``. Quand l’installation est terminée, fermez votre session et reconnectez-vous à la grappe. Le logiciel devrait alors pouvoir être chargé avec un module.

### Réinstaller une version existante
Si vous réinstallez une version que nous avons installée pour usage généralisé, mais que vous voulez en modifier les paramètres, vous devrez utiliser :
```bash
eb <recipe.eb> --force
```
pour installer une version locale dans votre répertoire /home.

### Installer ailleurs que dans /home
Pour installer un paquet logiciel dans votre espace /project par exemple, utilisez :
```bash
eb <recipe.eb> --installpath /path/to/your/project/easybuild
```
Pour que ces modules soient disponibles dans vos sessions, utilisez :
```bash
export RSNT_LOCAL_MODULEPATHS=/path/to/your/project/easybuild/modules
```
Pour que ces modules soient disponibles par défaut dans vos sessions, ajoutez cette commande au fichier ``.bashrc`` de votre répertoire /home.

## Pour plus d'information

*   [*Building software on Compute Canada clusters using EasyBuild*](https://westgrid.github.io/trainingMaterials/getting-started/#building-software-with-easybuild), webinaire
*   [Documentation pour notre équipe technique](https://github.com/ComputeCanada/software-stack/blob/main/doc/easybuild.md)
*   [Tutoriels](https://easybuild.io/tutorial/)