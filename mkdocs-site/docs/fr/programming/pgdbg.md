---
title: "Pgdbg/fr"
slug: "pgdbg"
lang: "fr"

source_wiki_title: "Pgdbg/fr"
source_hash: "0c87a561b42529ef1fe031c352567ad2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:24:54.696062+00:00"

tags:
  []

keywords:
  - "barre d'outils"
  - "SIGTRAP"
  - "compilateur PGI"
  - "mode ligne de commande"
  - "commande thread"
  - "pgdbg"
  - "omp.c"
  - "interface graphique"
  - "code source"
  - "débogage"
  - "fil courant"
  - "OpenMP"
  - "PGDBG"

questions:
  - "Qu'est-ce que l'outil PGDBG et pour quels types d'applications ou de langages est-il particulièrement recommandé par rapport à GDB ?"
  - "Quelles sont les étapes de préparation requises, notamment concernant les modules d'environnement et les options de compilation, avant de pouvoir déboguer un code ?"
  - "Comment lancer une session de débogage en mode ligne de commande et quelles commandes permettent d'inspecter et de sélectionner les différents fils d'exécution (threads) ?"
  - "Quels sont les principaux éléments qui composent l'interface graphique par défaut du débogueur PGDBG ?"
  - "Quel est le rôle spécifique des quatre listes déroulantes présentes dans la barre d'outils principale ?"
  - "Quelles sont les fonctionnalités offertes par les volets du code source, des entrées/sorties et de débogage au sein de l'interface ?"
  - "Quelle commande permet de sélectionner un fil d'exécution spécifique comme fil courant dans le débogueur ?"
  - "Quel est l'état actuel et le signal reçu par le thread numéro 3 selon la sortie affichée ?"
  - "Dans quel fichier source et à quelle ligne le thread sélectionné s'est-il arrêté ?"
  - "Quels sont les principaux éléments qui composent l'interface graphique par défaut du débogueur PGDBG ?"
  - "Quel est le rôle spécifique des quatre listes déroulantes présentes dans la barre d'outils principale ?"
  - "Quelles sont les fonctionnalités offertes par les volets du code source, des entrées/sorties et de débogage au sein de l'interface ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

PGDBG est un outil simple mais puissant pour le débogage d’applications parallèles MPI et OpenMP sous Linux. L’outil fait partie du paquet du compilateur PGI et est configuré pour OpenMP avec fils parallèles. Il peut être utilisé en mode graphique avec redirection X11 ou en mode ligne de commande.

Un débogueur GNU comme GDB conviendra pour la plupart des programmes C, C++ ou Fortran77. Cependant, GDB ne fonctionne pas très bien avec les programmes Fortran 90/95; c’est pourquoi le Portland Group a développé [PGDBG](https://www.pgroup.com/products/tools.htm/pgdbg.htm).

## Guide de démarrage

Le travail avec PGDBG s’effectue généralement en deux étapes :
1.  **compilation** : le code est compilé (avec l’option `-g` pour obtenir les symboles de débogage);
2.  **exécution et débogage** : le code est exécuté et les résultats sont analysés.
Le débogage peut se faire en mode ligne de commande ou en mode graphique.

## Modules d'environnement

Il faut d’abord charger le [module](utiliser-des-modules.md) pour le paquet PGI. Pour connaître les versions disponibles pour les modules du compilateur, de MPI et de CUDA que vous avez chargés, lancez `module avail pgi`. Pour connaître la liste complète des modules PGI disponibles, lancez `module -r spider '.*pgi.*'`. En date de décembre 2018, les versions disponibles sont
*   pgi/13.10
*   pgi/17.3
Pour charger un module, lancez `module load pgi/version`; par exemple, pour la version 17.3, la commande est

```bash
module load pgi/17.3
```

## Compilation

Avant d’être débogué, le code doit d’abord être compilé en ajoutant l’indicateur `-g` pour obtenir les renseignements utiles au débogage.

```bash
pgcc -g program.c -o program
```

## Exécution et débogage en mode ligne de commande

Une fois le code compilé avec les options appropriées, lancez PGDBG pour effectuer l’analyse. Par défaut, l’affichage se fait par l’interface graphique. Si toutefois vous ne voulez pas utiliser cette interface ou que vous n’avez pas la redirection X11, vous pouvez travailler en mode ligne de commande en ajoutant l’option `text` au lancement de PGDBG.

En mode ligne de commande, une invite est affichée.

```bash
pgdbg -text program
```

```text
PGDBG 17.3-0 x86-64 (Cluster, 256 Process)
PGI Compilers and Tools
Copyright (c) 2017, NVIDIA CORPORATION.  All rights reserved.
Loaded: /home/user/program
pgdbg>
```

À l’invite, lancez la commande `run`.

```bash
pgdbg> run
```

En cours d’exécution du programme, PGDBG s’attache automatiquement aux fils et décrit chacun d’eux au fur et à mesure qu’ils sont créés. En cours de débogage, PGDBG travaille sur un seul fil à la fois, le fil courant.
La commande `thread` sert à sélectionner le fil courant,
la commande `threads` liste les fils utilisés à ce moment par un programme actif.

```bash
pgdbg > threads
```

```text
0  ID PID    STATE      SIGNAL      LOCATION
   3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
=> 2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

Par exemple, pour sélectionner ID 2 comme fil courant, la commande `thread` serait

```bash
pgdbg > thread 3
pgdbg > threads
```

```text
0  ID PID    STATE      SIGNAL      LOCATION
=> 3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

## Exécution et débogage en mode graphique

L’interface graphique est utilisée par défaut. Si vous avez configuré la redirection X11, PGDBG démarre en mode graphique dans une nouvelle fenêtre.

Les éléments de l'interface graphique sont :
*   barre de menus
*   barre d'outils
*   volet du code source
*   volet des entrées-sorties (E/S)
*   volet de débogage.

### Barre de menus

La barre de menus principale affiche ''Fichier'', ''Édition'', ''Affichage'', ''Connexions'', ''Débogage'' et ''Aide''. Il est possible de naviguer avec la souris ou avec les raccourcis-clavier.

### Barre d'outils principale

La barre d'outils principale contient plusieurs boutons et quatre listes déroulantes. La première liste ''Processus actuel'', montre le processus en cours, autrement dit, le fil courant. Le libellé change selon que le processus ou le fil est décrit. Quand plusieurs fils sont disponibles, cette liste sert à sélectionner le processus ou le fil qui devrait être courant.

La deuxième liste ''Appliquer'' détermine le groupe de processus et de fils auxquels les commandes d'action s'appliquent.
La troisième liste ''Afficher'' détermine le groupe de processus et de fils auxquels les commandes d'affichage de données s'appliquent.

La quatrième liste ''Fichier'' affiche le fichier source qui contient la cible courante.

### Volets du code source et des outils de débogage

Le volet du code source montre le code pour la session en cours. Ce volet et les onglets du volet de débogage sont des éléments ancrables; en double-cliquant dessus, vous pouvez les détacher de la fenêtre principale.

### Volet des entrées-sorties du programme

Les résultats produits par le programme sont affichés dans ce volet. Utilisez le champ ''Entrée'' pour faire des entrées au programme.

### Volet de débogage

Situé au bas de la fenêtre, ce volet comporte des onglets qui servent différentes fonctions de débogage et de visualisation de l'information.

## Références

*   [Guide de l'utilisateur du débogueur PGI (en anglais)](https://www.pgroup.com/resources/docs/17.7/x86/pgdbg-user-guide/index.htm)
*   [Site web de PGI](https://www.pgroup.com/index.htm)