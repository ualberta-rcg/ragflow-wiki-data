---
title: "Vtune/fr"
slug: "vtune"
lang: "fr"

source_wiki_title: "Vtune/fr"
source_hash: "ea12c7036cf121a8b471afa892cc538a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:51:05.557484+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Introduction

[VTune](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html) est un produit d'Intel pour analyser la performance des systèmes et des applications [OpenMP et MPI](https://software.intel.com/content/www/us/en/develop/documentation/itac-vtune-mpi-openmp-tutorial-lin/top.html).

## Module logiciel

Pour charger le module sur une de nos grappes, lancez :

```bash
module load vtune
```

## Changement de noms

Il sera question ici de Intel® VTune™ Amplifier, dont le nom a été changé pour Intel® VTune™ Profiler dans la documentation des plus récentes versions. Aussi, les commandes `amplxe-cl` et `amplxe-gui` ont été renommées `vtune` et `vtune-gui` respectivement pour la ligne de commande et les outils graphiques. Les versions des modules VTune offertes pour nos grappes sont antérieures au changement de ces noms. Pour plus d'information, voyez [cette page du guide de l'utilisateur](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top/launch.html).

## Types d'analyses

Pour collecter de l'information pour analyse, lancez :

```bash
vtune -collect <analysis-type> <target_exe> <exe_arguments>
```

où `<analysis-type>` est le nom d'un type d'analyse disponible (par ex. `hotspots`), et `<target_exe>` est le chemin vers l'exécutable que vous voulez analyser. Nous vous recommandons de compiler votre exécutable avec l'option `-g` et d'utiliser le niveau d'optimisation normal afin d'obtenir des résultats exacts. Il est possible de faire lister sur la ligne de commande des options d'arguments spécifiques à une version ainsi que plusieurs exemples d'utilisation avec `vtune -help`, après avoir chargé le module VTune.
Téléchargez [la documentation de Parallel Studio XE (incluant VTune)](https://software.intel.com/content/www/us/en/develop/articles/download-documentation-intel-parallel-studio-xe-current-previous.html) et le [guide de l'utilisateur Intel VTune Profiler User Guide](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html).

## Créer un rapport

Pour créer un rapport, lancez :

```bash
vtune -report <report-type>
```

où `<report-type>` est le type de rapport à générer (`hotspots`). Voyez aussi la page [Generate Command Line Reports](https://software.intel.com/en-us/vtune-amplifier-help-generating-command-line-reports).

## Exemple de matrice

Pour analyser et générer le projet Intel *Matrix Sample Project* en ligne de commande avec 4 cœurs :

```bash
salloc --time=1:00:00 --cpus-per-task=4 --ntasks=1 --mem=16G --account=def-yours
module load StdEnv/2020 vtune
cp -a $EBROOTVTUNE/vtune/$EBVERSIONVTUNE*/samples/en/C++/matrix .
cd matrix/linux
make icc
vtune -collect hotspots ../matrix
vtune -report summary
```

La plus récente version de `matrix_multiply` (qui construit avec `cmake`) [se trouve ici](https://github.com/oneapi-src/oneAPI-samples/tree/master/Tools/VTuneProfiler).

## Mode graphique

*Intel Matrix Sample Project* peut être exécuté en mode graphique, comme décrit [ici](https://software.intel.com/content/www/us/en/develop/documentation/vtune-hotspots-tutorial-linux-c/top/run-hotspots-analysis.html). Pour utiliser VTune dans VNC voyez les directives ci-dessous. Le mode graphique peut être utile pour générer des configurations en commande de ligne, comme décrit [ici](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top/analyze-performance/control-data-collection/generating-command-line-configuration-from-gui.html).

### Nœuds des grappes

1.  Connectez-vous à un nœud de calcul ou à un nœud de connexion avec [TigerVNC](https://docs.alliancecan.ca/wiki/VNC/fr#Connexion) ;
2.  `module load StdEnv/2020 vtune`
3.  `vtune-gui`

### Nœuds VDI

1.  Connectez-vous à un nœud de calcul ou à un nœud de connexion avec [TigerVNC](https://docs.alliancecan.ca/wiki/VNC/fr#Connexion) ;
2.  `module load CcEnv StdEnv/2020 vtune`
3.  `vtune-gui`

## Exemple MPI

D'abord, chargez le dernier module VTune.

```bash
module load StdEnv/2020
module load vtune
```

Ensuite, compilez votre programme MPI comme vous le feriez habituellement et exécutez-le dans une tâche ou une session interactive lancée par une commande `salloc` en utilisant :

```bash
srun aps your_mpi_program.x
```

Une fois le programme terminé, les données de profilage seront stockées dans un répertoire appelé `aps_result_AAAAMMJJ` où `AAAAMMJJ` correspond à la date actuelle.

Il y a beaucoup d'informations que vous pouvez extraire de ces données. Pour obtenir le rapport sommaire de base de la performance de votre programme, exécutez :

```bash
aps-report -D aps_result_AAAAMMJJ
```

où vous remplacerez `AAAAMMJJ` pour correspondre au répertoire réel qui a été créé. Cette commande crée un fichier HTML, qui peut être copié sur votre ordinateur personnel et visualisé dans un navigateur. Le rapport identifiera clairement les problèmes de performance qui affectent votre code.