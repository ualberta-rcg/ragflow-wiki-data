---
title: "HDF5/fr"
slug: "hdf5"
lang: "fr"

source_wiki_title: "HDF5/fr"
source_hash: "33dd8e74ff4595319cdb6ae410d8c1b6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:53:09.766433+00:00"

tags:
  - software

keywords:
  - "hdf5-mpi"
  - "modules d'environnement"
  - "HDFView"
  - "stockage de données"
  - "outils en ligne de commande"
  - "data space"
  - "lecture et écriture"
  - "HDF5 ODBC Connector"
  - "Mode parallèle"
  - "format de fichier"
  - "ensemble de données"
  - "données scientifiques"
  - "Utilitaires"
  - "HDF5"

questions:
  - "Qu'est-ce que la bibliothèque HDF5 et à quels types de besoins en gestion de données scientifiques répond-elle ?"
  - "Quels sont les principaux points forts et points faibles de HDF5, notamment en termes de compatibilité et d'interface ?"
  - "Comment doit-on configurer son environnement et lier les bibliothèques pour compiler un programme utilisant HDF5 en mode séquentiel ou parallèle ?"
  - "Quelles sont les commandes requises pour compiler et exécuter un programme utilisant HDF5 avec MPI ?"
  - "Quelle est l'utilité des interfaces HDF5 ODBC Connector et HDFView présentées dans le document ?"
  - "Quels outils en ligne de commande permettent de vérifier la validité ou d'éditer un fichier HDF5 ?"
  - "Quelles sont les commandes nécessaires pour charger le module et compiler un programme HDF5 en mode parallèle ?"
  - "Quel type d'opération l'exemple de code fourni en lien permet-il d'illustrer ?"
  - "Quelles sont les étapes successives de traitement des données décrites dans l'exemple ?"
  - "Quelles sont les commandes requises pour compiler et exécuter un programme utilisant HDF5 avec MPI ?"
  - "Quelle est l'utilité des interfaces HDF5 ODBC Connector et HDFView présentées dans le document ?"
  - "Quels outils en ligne de commande permettent de vérifier la validité ou d'éditer un fichier HDF5 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Généralités

HDF5 (pour *Hierarchical Data Format*) est une bibliothèque de formatage des données scientifiques et qui en facilite le stockage, la lecture, la visualisation, la manipulation et l'analyse. Elle traite tous les types de données et sa conception permet autant des entrées-sorties flexibles et efficaces que la prise en charge de forts volumes de données. Elle est portable et extensible et peut accompagner les applications dans leur évolution.
La suite HDF5 Technology comprend des outils et des applications pour la gestion, la manipulation, la visualisation et l'analyse de données en format HDF5.
HDF (appelée aussi HDF4) est une bibliothèque et un format de fichier multiformat pour le stockage et la gestion sur plusieurs ordinateurs. HDF4 est le format original et même si elle est toujours supportée, la version HDF5 est recommandée.

## Description
HDF a été conçue pour
*   de forts volumes de données et des données complexes, mais peut être utilisée pour de bas volumes et des données simples
*   toutes les tailles et tous les types de systèmes (portable)
*   stockage et entrée-sortie flexibles et efficients
*   applications peuvent évoluer et traiter de nouveaux modèles

HDF comprend :
*   un format de fichier pour le stockage de données HDF4/HDF5
*   un modèle pour organiser et accéder des données HDF4/HDF5 avec diverses applications
*   plusieurs logiciels dont des bibliothèques, des modules linguistiques et plusieurs outils spécifiques au format

Références :
*   Site web du projet : [https://www.hdfgroup.org/solutions/hdf5/](https://www.hdfgroup.org/solutions/hdf5/)
*   Documentation : [https://support.hdfgroup.org/documentation/](https://support.hdfgroup.org/documentation/)
*   Téléchargement : [https://www.hdfgroup.org/downloads/hdf5](https://www.hdfgroup.org/downloads/hdf5)

## Points forts
*   Les données sont indépendantes de l'architecture matérielle ([boutisme](https://fr.wikipedia.org/wiki/Boutisme)).
*   Les données structurées en unités physiques permettent le suivi de l'information pertinente.
*   Utilisable en parallèle (MPI-IO)
*   Les données peuvent être compressées à l'écriture (zlib ou szip).
*   Interfaces pour C, C++, Fortran 90, Java et Python
*   Gère tous les types de données (plus que [NetCDF](netcdf.md)).
*   Lecture et écriture en format .mat de Matlab.
*   Gratuit pour la plupart des plateformes

## Points faibles
*   Interface plus compliquée que celle de [NetCDF](netcdf.md).
*   HDF5 n'exige pas UTF-8; ASCII est habituellement employé.
*   Les ensembles de données ne peuvent être libérés sans qu'une copie du fichier soit créée avec un autre outil.

# Guide de démarrage
Nous abordons ici les détails de configuration.

## Modules d'environnement
Les [modules](../programming/utiliser_des_modules.md) suivants sont disponibles sur nos grappes :
*   **hdf**
    *   version 4.1 et précédentes
*   **hdf5**
    *   plus récente version de HDF5
*   **hdf5-mpi**
    *   pour utiliser MPI

Exécutez `module avail hdf` pour connaître les versions disponibles pour le compilateur et les modules MPI que vous avez chargés. Pour la liste complète des modules HDF4/HDF5, exécutez `module -r spider '.*hdf.*'`.

Utilisez `module load hdf/version` ou `module load hdf5/version` pour configurer l'environnement selon la version sélectionnée. Par exemple, pour charger HDF5 version 1.14.2, lancez

```bash
module load hdf5/1.14.2
```

## Scripts de soumission de tâche

Pour des exemples de scripts pour l'ordonnanceur Slurm, consultez [Exécuter des tâches](../running-jobs/running_jobs.md). Nous vous recommandons d'utiliser la commande `module load ...` dans votre script.

## Lier à des bibliothèques HDF
Voici des exemples en mode séquentiel et en mode parallèle :

### Mode séquentiel

```bash
module load hdf5/1.14.2
gcc example.c -lhdf5
```

### Mode parallèle

```bash
module load hdf5-mpi/1.14.2
mpicc example.c -lhdf5
```

### Exemple
Consultez [un exemple](https://support.hdfgroup.org/ftp/HDF5/examples/examples-by-api/hdf5-examples/1_10/C/H5D/h5ex_d_rdwr.c) de lecture et écriture dans un ensemble de données. Des nombres entiers sont d'abord écrits avec des dimensions d'espace de données de DIM0xDIM1, puis le fichier est refermé. Le fichier est ensuite rouvert, les données sont lues et affichées.

Compilez et exécutez avec

```bash
module load hdf5-mpi
mpicc h5ex_d_rdwr.c -o h5ex_d_rdwr -lhdf5
mpirun -n 2 ./h5ex_d_rdwr
```

## Utilitaires
Vous trouverez [la liste complète](https://support.hdfgroup.org/products/hdf5_tools) sur le site web du Hdfgroup. Soulignons les utilitaires suivants :
*   HDF5 ODBC Connector
    *   interface SQL pour le format de données HDF5 en Excel, Tableau et autres
*   HDFView
    *   fureteur Java et paquet objets pour HDF5-1.10 (identification d'objets 64-bits) et HDF 4.2.12 (et suivantes)
*   quelques outils en ligne de commande
    *   gif2h5/h52gif
    *   h5cc, h5fc, h5c++
    *   h5debug
    *   h5diff
    *   h5dump
    *   h5import
*   h5check
    *   vérification de la validité d'un fichier HDF5
*   h5edit
    *   outils d'édition