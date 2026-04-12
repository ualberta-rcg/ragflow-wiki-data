---
title: "Mii/fr"
slug: "mii"
lang: "fr"

source_wiki_title: "Mii/fr"
source_hash: "7db0e57a29fb5675577889567d701a51"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:08:50.226659+00:00"

tags:
  []

keywords:
  - "Recherche"
  - "chargement automatique"
  - "MODULEPATH"
  - "Commande"
  - "openmpi/4.0.3"
  - "commandes"
  - "Modules"
  - "moteur de recherche"
  - "Mii"
  - "Binaires"
  - "blast 2.12.0"
  - "Lmod"
  - "modules"
  - "gcc/9.3.0"

questions:
  - "Quelles sont les principales caractéristiques et fonctionnalités offertes par le moteur de recherche Mii ?"
  - "Comment l'environnement de l'interpréteur est-il affecté après l'exécution d'un module chargé automatiquement par Mii ?"
  - "De quelle manière Mii réagit-il face à une commande connue par rapport à une commande qu'il ne reconnaît pas ?"
  - "Comment utiliser la commande de recherche pour trouver la liste des modules offrant des binaires spécifiques ?"
  - "Quelle commande doit-on exécuter pour désactiver l'outil Mii ?"
  - "Comment peut-on réactiver Mii après sa désactivation ?"
  - "What software modules were loaded into the environment after the user selected option 1?"
  - "Which module did Lmod automatically replace with \"gcc/9.3.0\" during the loading process?"
  - "What module was reloaded as a result of changes to the MODULEPATH?"
  - "Comment utiliser la commande de recherche pour trouver la liste des modules offrant des binaires spécifiques ?"
  - "Quelle commande doit-on exécuter pour désactiver l'outil Mii ?"
  - "Comment peut-on réactiver Mii après sa désactivation ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un moteur de recherche intelligent pour les modules.

Mii cherche et charge des modules sur demande dans une installation existante.

Une fois Mii chargé, les modules se chargent automatiquement quand les commandes sont connues.
Pour les commandes inconnues, Mii demande de façon interactive quels modules doivent être chargés.

Caractéristiques :
*   supporte les installations de Lmod et Environment Modules
*   intégration pour les interpréteurs bash et zsh
*   liste des modules / renseignements particuliers (via `mii list`, `mii show`)
*   recherche de commandes exactes (via `mii exact`)
*   recherche de commandes similaires (via `mii search`)
*   format d'exportation JSON optionnel

!!! warning "Important"
    Un module chargé automatiquement ne persiste pas après la commande. L'environnement de l'interpréteur demeure tel qu'il était avant que Mii ait téléchargé le module.

## Activation
Chargez et activez avec la commande

```bash
module load mii
```

Une fois chargé, Mii propose des suggestions. Par exemple, quand une commande n'est pas trouvée, Mii suggère

```bash
cmd
```
```text
[mii] cmd not found! Similar commands: "xcmd", "vmd", "c2d"
```

## Commandes connues
Une commande ou un binaire connu sera chargé automatiquement.

```bash
python3.9 --version
```
```text
[mii] loading StdEnv/2020 python/3.9.6 ...
Python 3.9.6
```

## Commandes inconnues
Quand une commande ou un binaire n'est pas connu, Mii suggère des candidats potentiels selon leur pertinence.

```bash
blastn -version
```
```text
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
Vous pouvez chercher des binaires pour obtenir la liste des modules qui les offrent. Les résultats sont présentés par ordre de pertinence.

```bash
mii search pgc+
```
```text
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

## Désactivation de Mii
Lancez la commande

```bash
mii disable
```

## Réactivation de Mii
Lancez la commande

```bash
mii enable