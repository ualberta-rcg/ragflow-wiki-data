---
title: "Utiliser des modules/fr"
slug: "utiliser_des_modules"
lang: "fr"

source_wiki_title: "Utiliser des modules/fr"
source_hash: "a23e873ebce5b0acb79badc00a91e427"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:30:00.455136+00:00"

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

Nos serveurs peuvent exécuter la totalité des logiciels fonctionnant sous Linux. Dans le cas le plus simple, le logiciel dont vous avez besoin sera déjà installé sur l'un des serveurs de calcul. Il sera alors accessible sous la forme d'un **module**. Si ce n'est pas le cas, vous pouvez soit demander à notre équipe de l'installer pour vous, soit le faire vous-même.

Les modules sont des fichiers de configuration qui contiennent des instructions pour modifier votre environnement logiciel. Cette architecture modulaire permet d'avoir plusieurs versions d'une même application installées sans que celles-ci entrent en conflit. Pour les nouveaux serveurs, les modules sont gérés par l'outil [Lmod](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod) développé au [TACC](https://www.tacc.utexas.edu/). Cet outil remplace [*Environment Modules*](http://modules.sourceforge.net) qui est utilisé sur la plupart des anciens serveurs. Si vous le connaissez, vous ne devriez pas être trop dépaysé, car *Lmod* a été conçu pour être très similaire à *Environment Modules*. Référez-vous à la section [Lmod vs Environment Modules](#lmod-vs-environment-modules) ci-dessous pour connaître les différences principales.

Un fichier module (*modulefile*) contient les informations nécessaires pour rendre disponible une application ou une bibliothèque dans la session de l'usager. Typiquement, un fichier module contient des instructions qui modifient ou initialisent les variables d'environnement comme `PATH` et `LD_LIBRARY_PATH` pour utiliser les différents logiciels installés. Notez que le simple fait de charger un module n'exécute pas le logiciel dont il est question. Pour connaître le nom du fichier binaire et la syntaxe de son usage, il faut lire la documentation du logiciel et avec la commande `module`, vous n'avez normalement pas besoin de connaître le chemin du logiciel ou de la bibliothèque. Vous pouvez voir des détails pour le module en tapant la commande `module show <nom de module>`.

## Principales commandes de `module`
La commande `module` a plusieurs sous-commandes. La syntaxe normale est

```bash
module commande [autres options]
```

Pour connaître la liste des sous-commandes disponibles, utilisez

```bash
module help
```

### Sous-commande `spider`
La sous-commande `spider` fait afficher tous les modules qui se trouvent dans [l'environnement logiciel standard](standard-software-environments.md) courant.

```bash
module spider
```

Si vous spécifiez le nom d'une application, par exemple avec

```bash
module spider openmpi
```
cela affichera la liste de toutes les versions disponibles.

Si vous spécifiez le nom de l'application avec son numéro de version, par exemple avec

```bash
module spider openmpi/4.0.3
```
cela affichera la liste des options de module à charger afin d'accéder à cette version.

### Sous-commande `avail`
Pour lister les modules que vous pouvez charger, utilisez

```bash
module avail
```

Vous pouvez obtenir une liste de modules disponibles pour une bibliothèque ou un outil particulier avec

```bash
module avail openmpi
```

Notez que la commande `module avail` peut ne pas lister certains modules qui sont incompatibles avec les modules que vous avez chargés. Pour voir la liste des modules autres que ceux qui sont chargés et qui vous sont disponibles, utilisez la sous-commande `spider` documentée ci-dessus.

### Sous-commande `list`
La sous-commande `**list**` affiche les modules qui sont présentement chargés dans votre environnement.

```bash
module list
```

### Sous-commande `load`
La sous-commande `**load**` permet de charger un module donné. Par exemple

```bash
module load gcc/9.3
```
pourrait charger le module du compilateur GCC version 9.3.

Vous pouvez charger plus d'un module avec une même commande. Par exemple

```bash
module load gcc/9.3 openmpi/4.0
```
chargerait à la fois le compilateur GCC 9.3 et la bibliothèque OpenMPI 4.0 compilée pour GCC.

Si vous chargez un module qui est incompatible avec un module déjà chargé, *Lmod* vous indiquera qu'il a remplacé l'ancien module par le nouveau. Ceci peut se produire en particulier pour des compilateurs et des implémentations MPI.

### Sous-commande `unload`
Au contraire de la sous-commande `**load**`, `**unload**` enlève un module de votre environnement. Par exemple

```bash
module unload gcc/9.3
```
enlèverait le compilateur GCC 9.3 de votre environnement.

Si certains modules dépendaient de ce compilateur, *Lmod* vous indiquera qu'ils ont été désactivés.

### Sous-commande `purge`
La sous-commande `**purge**` permet d'enlever d'un seul coup tous les modules que vous avez chargés.

```bash
module purge
```

Certains modules peuvent être marqués comme *sticky* (permanents) par les administrateurs de système et ne seront pas enlevés.

### Sous-commandes `show`, `help` et `whatis`
Les sous-commandes `**show**`, `**help**` et `**whatis**` permettent d'avoir de l'information supplémentaire sur un module donné. La sous-commande `**show**` affiche l'intégralité du module, la commande `**help**` affiche un message d'aide, et la commande `**whatis**` montre une description du module.

```bash
module help gcc/9.3
```

### Sous-commande `apropos` ou `keyword`
Les sous-commandes `apropos` ou `keyword` permettent de chercher un mot-clé dans l'ensemble des modules. Si vous ne savez pas quel module est approprié pour réaliser votre calcul, vous pouvez ainsi chercher dans les descriptions.

## Chargement automatique des modules
!!! avertissement
    Nous **déconseillons de charger des modules automatiquement dans votre `.bashrc`**. Nous vous recommandons plutôt de charger les modules nécessaires au besoin, par exemple dans vos scripts de tâches. Afin de faciliter le chargement d'un grand nombre de modules, il est préférable d'utiliser une collection de modules.

## Collection de modules
*Lmod* vous permet de créer une collection de modules. Pour ce faire, chargez d'abord les modules requis avec, par exemple

```bash
module load gcc/9.3 openmpi/4.0.3 mkl
```

Utilisez ensuite la commande `save` pour sauvegarder cette collection.

```bash
module save mes_modules
```
L'argument `mes_modules` est un nom que vous donnez à la collection.

Vous pouvez ensuite, dans une session ultérieure ou dans une tâche, restaurer cette collection avec la commande

```bash
module restore mes_modules
```

## Modules cachés
Certains modules sont cachés. Vous pouvez les ignorer. Il s'agit généralement de modules que vous n'avez pas à charger manuellement. Ils sont chargés automatiquement selon les besoins.

## Hiérarchie de modules
Plusieurs des systèmes de calcul informatique de pointe à travers le monde utilisent une structure de modules plate avec tous les modules au même niveau. Ceci devient problématique lorsqu'un grand nombre de combinaisons de versions de différents modules sont disponibles. Par exemple, si vous avez à utiliser la bibliothèque [FFTW](fftw.md), et que le module `fftw` est disponible en plusieurs versions, dont une version compilée avec le compilateur `gcc` version 4.8 et `openmpi` 1.6, vous avez peut-être déjà vu des modules nommés `openmpi/4.0_gcc9.3` et `fftw/3.8_gcc9.3_openmpi4.0`. Ceci n'est ni élégant ni pratique. Pour résoudre ce problème, nous utilisons une hiérarchie de modules. Plutôt que d'utiliser la commande

```bash
module load gcc/9.3 openmpi/4.0_gcc9.3 fftw/3.8_gcc9.3_openmpi4.0
```
vous utiliserez la commande

```bash
module load gcc/9.3 openmpi/4.0 fftw/3.8
```
Ceci est rendu possible avec une hiérarchie de modules. Le module `fftw/3.8` qui est chargé ne sera pas le même si vous avez chargé au préalable le compilateur Intel ou le compilateur GCC.

L'inconvénient d'utiliser une hiérarchie de modules est que, puisque des modules peuvent avoir le même nom, seuls les modules compatibles avec les modules *parents* sont affichés par la commande `module avail`. Charger un parent est donc un prérequis afin d'avoir accès à certains modules. Pour avoir l'information complète, le système de module rend disponible la commande `module spider`. Celle-ci parcourt la hiérarchie complète et affiche tous les modules. En spécifiant un module et une version particulière, il est alors possible de savoir quels chemins de la hiérarchie permettent de charger le module désiré.

## Remplacement automatique de modules
Lorsque le système de modules détecte deux modules de la même famille, ou deux versions du même module, la commande `module load` remplacera automatiquement le module original par celui qui doit être chargé. Dans le cas où le module remplacé est un nœud de la hiérarchie de modules, les modules dépendants seront chargés de nouveau s'il existe une version compatible, ou désactivés dans le cas contraire.

## Créer des modules
Pour des instructions sur comment créer des modules, veuillez vous référer à la [documentation officielle](http://lmod.readthedocs.io/en/latest/015_writing_modules.html).

## Utiliser des modules avec ZSH et KSH
Si vous voulez utiliser des modules avec les *interpréteurs de commandes* ZSH ou KSH, exécutez les commandes suivantes :

```bash
zsh -l
```

```bash
ksh -l