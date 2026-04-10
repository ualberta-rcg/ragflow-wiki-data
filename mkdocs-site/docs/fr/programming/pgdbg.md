---
title: "Pgdbg/fr"
slug: "pgdbg"
lang: "fr"

source_wiki_title: "Pgdbg/fr"
source_hash: "0c87a561b42529ef1fe031c352567ad2"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:56:26.242824+00:00"

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

PGDBG est un outil simple, mais puissant pour le débogage d'applications parallèles MPI et OpenMP sous Linux. L'outil fait partie du paquet du compilateur PGI et est configuré pour OpenMP avec des fils parallèles. Il peut être utilisé en mode graphique avec redirection X11 ou en mode ligne de commande.

Un débogueur GNU comme GDB conviendra pour la plupart des programmes C, C++ ou Fortran77. Cependant, GDB ne fonctionne pas très bien avec les programmes Fortran 90/95; c'est pourquoi le Portland Group a développé [pgdbg](https://www.pgroup.com/products/tools.htm/pgdbg.htm).

## Guide de démarrage

Le travail avec PGDBG s'effectue généralement en deux étapes :
1.  **Compilation** : le code est compilé (avec l'option `-g` pour obtenir les symboles de débogage);
2.  **Exécution et débogage** : le code est exécuté et les résultats sont analysés.

Le débogage peut se faire en mode ligne de commande ou en mode graphique.

### Modules d'environnement

Il faut d'abord charger le [module](utiliser-des-modules.md) pour le paquet PGI. Pour connaître les versions disponibles pour les modules du compilateur, de MPI et de CUDA que vous avez chargés, lancez `module avail pgi`. Pour connaître la liste complète des modules PGI disponibles, lancez `module -r spider '.*pgi.*'`. En date de décembre 2018, les versions disponibles sont :
*   `pgi/13.10`
*   `pgi/17.3`

Pour charger un module, lancez `module load pgi/version`; par exemple, pour la version 17.3, la commande est :
```bash
module load pgi/17.3
```

### Compilation

Avant d'être débogué, le code doit d'abord être compilé en ajoutant l'indicateur `-g` pour obtenir les renseignements utiles au débogage.
```bash
pgcc -g program.c -o program
```

### Exécution et débogage en mode ligne de commande

Une fois le code compilé avec les options appropriées, lancez PGDBG pour effectuer l'analyse. Par défaut, l'affichage se fait par l'interface graphique. Si toutefois vous ne voulez pas utiliser cette interface ou que vous n'avez pas la redirection X11, vous pouvez travailler en mode ligne de commande en ajoutant l'option `text` au lancement de PGDBG.

En mode ligne de commande, une invite est affichée.
```bash
pgdbg -text program
```
```text
PGDBG 17.3-0 x86-64 (Cluster, 256 Process)
PGI Compilers and Tools
Copyright (c) 2017, NVIDIA CORPORATION. All rights reserved.
Loaded: /home/user/program
pgdbg>
```

À l'invite, lancez la commande `run`.
```text
pgdbg> run
```

En cours d'exécution du programme, PGDBG s'attache automatiquement aux fils et décrit chacun d'eux au fur et à mesure qu'ils sont créés. En cours de débogage, PGDBG travaille sur un seul fil à la fois, le fil courant.
La commande `thread` sert à sélectionner le fil courant,
la commande `threads` liste les fils utilisés à ce moment par un programme actif.
```text
pgdbg > threads
0  ID PID    STATE      SIGNAL      LOCATION
   3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
=> 2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

Par exemple, pour sélectionner ID 2 comme fil courant, la commande `thread` serait :
```text
pgdbg > thread 3
```
```text
pgdbg > threads
0  ID PID    STATE      SIGNAL      LOCATION
=> 3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

### Exécution et débogage en mode graphique

L'interface graphique est utilisée par défaut. Si vous avez configuré la redirection X11, PGDBG démarre en mode graphique dans une nouvelle fenêtre.

Les éléments de l'interface graphique sont :
*   la barre de menus
*   la barre d'outils
*   le panneau du code source
*   le panneau des entrées/sorties (E/S)
*   le panneau de débogage.

#### Barre de menus

La barre de menus principale affiche *Fichier*, *Modifier*, *Affichage*, *Connexions*, *Débogage* et *Aide*. Il est possible de naviguer avec la souris ou avec les raccourcis-clavier.

#### Barre d'outils principale

La barre d'outils principale contient plusieurs boutons et quatre listes déroulantes. La première liste, *Processus courant*, montre le processus en cours, autrement dit, le fil courant. Le libellé change selon que le processus ou le fil est décrit. Quand plusieurs fils sont disponibles, cette liste sert à sélectionner le processus ou le fil qui devrait être courant.

La deuxième liste, *Appliquer*, détermine le groupe de processus et de fils auxquels les commandes d'action s'appliquent.
La troisième liste, *Affichage*, détermine le groupe de processus et de fils auxquels les commandes d'affichage de données s'appliquent.

La quatrième liste, *Fichier*, affiche le fichier source qui contient la cible courante.

#### Panneaux du code source et des outils de débogage

Le panneau du code source montre le code pour la session en cours. Ce panneau et les onglets du panneau de débogage sont des éléments ancrables; en double-cliquant dessus, vous pouvez les détacher de la fenêtre principale.

#### Panneau des entrées/sorties du programme

Les résultats produits par le programme sont affichés dans ce panneau. Utilisez le champ *Entrée* pour faire des entrées au programme.

#### Panneau de débogage

Situé au bas de la fenêtre, ce panneau comporte des onglets qui servent différentes fonctions de débogage et de visualisation de l'information.

## Références

*   [PGI Debugger User's Guide](https://www.pgroup.com/resources/docs/17.7/x86/pgdbg-user-guide/index.htm)
*   [site web de PGI](https://www.pgroup.com/index.htm)