---
title: "Mii/fr"
slug: "mii"
lang: "fr"

source_wiki_title: "Mii/fr"
source_hash: "7db0e57a29fb5675577889567d701a51"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:35:23.852206+00:00"

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

Un moteur de recherche intelligent pour les modules.

Mii recherche et charge des modules sur demande dans une installation existante.

Une fois Mii chargé, les modules sont chargés automatiquement dans le cas de commandes connues. Pour les commandes inconnues, Mii demande interactivement quels modules doivent être chargés.

Caractéristiques :
*   prend en charge les installations de Lmod et Environment Modules
*   intégration des interpréteurs bash et zsh
*   liste des modules / renseignements particuliers (via `mii list`, `mii show`)
*   recherche de commandes exactes (via `mii exact`)
*   recherche de commandes similaires (via `mii search`)
*   format d'exportation JSON optionnel

!!! important "Important"
    Un module chargé automatiquement ne persiste pas après la commande. L'environnement de l'interpréteur reste tel qu'il était avant que Mii ait téléchargé le module.

## Activation
Chargez et activez avec la commande

```bash
module load mii
```

Une fois chargé, Mii émet des suggestions. Par exemple, lorsqu'une commande est introuvable, Mii suggère

```text
cmd
[mii] cmd not found! Similar commands: "xcmd", "vmd", "c2d"
```

## Commandes connues
Une commande ou un binaire qui est connu sera chargé automatiquement.

```text
python3.9 --version
[mii] loading StdEnv/2020 python/3.9.6 ...
Python 3.9.6
```

## Commandes non connues
Lorsqu'une commande ou un binaire n'est pas connu, Mii suggère des candidats potentiels en se basant sur leur pertinence.

```text
blastn -version
[mii] Please select a module to run blastn:
       MODULE         PARENT(S)
    1  blast+/2.12.0  StdEnv/2020 gcc/9.3.0
    2  blast+/2.11.0  StdEnv/2020 gcc/9.3.0
    3  blast+/2.10.1  StdEnv/2020 gcc/9.3.0
    4  rmblast/2.10.0 StdEnv/2020 gcc/9.3.0
    5  blast+/2.10.1  nixpkgs/16.09 gcc/7.3.0
    6  blast+/2.10.0  nixpkgs/16.09 gcc/7.3.0
    7  blast+/2.9.0   nixpkgs/16.09 gcc/7.3.0
    8  blast+/2.8.1   nixpkgs/16.09 gcc/7.3.0
    9  blast+/2.7.1   nixpkgs/16.09 gcc/7.3.0
    10 blast+/2.4.0   nixpkgs/16.09 gcc/7.3.0
    11 igblast/1.9.0  nixpkgs/16.09 gcc/7.3.0
    12 rmblast/2.9.0  nixpkgs/16.09 gcc/7.3.0
    13 blast+/2.6.0   nixpkgs/16.09 gcc/5.4.0
    14 igblast/1.9.0  nixpkgs/16.09 gcc/5.4.0
    15 igblast/1.8.0  nixpkgs/16.09 gcc/5.4.0
    16 igblast/1.7.0  nixpkgs/16.09 gcc/5.4.0
    17 rmblast/2.6.0  nixpkgs/16.09 gcc/5.4.0
    18 igblast/1.8.0  nixpkgs/16.09 gcc/4.8.5
Make a selection (1-18, q aborts) [1]: 1
[mii] loading StdEnv/2020 gcc/9.3.0 blast+/2.12.0 ...

Lmod is automatically replacing "intel/2020.1.217" with "gcc/9.3.0".


Due to MODULEPATH changes, the following have been reloaded:
  1) openmpi/4.0.3

blastn: 2.12.0+
 Package: blast 2.12.0, build Sep 27 2021 15:23:34
```
Dans cet exemple, nous avons entré le chiffre 1 à l'invite *Make a selection* et la commande s'est exécutée.

## Recherche
Vous pouvez chercher des binaires pour obtenir la liste des modules qui les offrent. Les résultats sont présentés dans l'ordre de leur pertinence.

```text
mii search pgc+
Results for "pgc+": (total 16)
    MODULE            COMMAND      PARENT(S)        RELEVANCE
    nvhpc/20.7        pgcc         StdEnv/2020      high
    nvhpc/20.7        pgc++        StdEnv/2020      high
    pgi/19.4          pgcc         nixpkgs/16.09    high
    pgi/19.4          pgc++        nixpkgs/16.09    high
    pgi/17.3          pgc          nixpkgs/16.09    high
    pgi/17.3          pgcc         nixpkgs/16.09    high
    pgi/17.3          pgc++        nixpkgs/16.09    high
    pgi/16.9          pgc          nixpkgs/16.09    high
    pgi/16.9          pgcc         nixpkgs/16.09    high
    pgi/16.9          pgc++        nixpkgs/16.09    high
    pgi/13.10         pgc          nixpkgs/16.09    high
    pgi/13.10         pgcc         nixpkgs/16.09    high
    pgi/13.10         pgc++        nixpkgs/16.09    high
    pgi/13.10         pgCC         nixpkgs/16.09    high
    gcccore/.9.3.0    gcc          StdEnv/2020      medium
    gcccore/.9.3.0    g++          StdEnv/2020      medium
```

## Désactiver Mii
Lancez la commande

```bash
mii disable
```

## Réactiver Mii
Lancez la commande

```bash
mii enable