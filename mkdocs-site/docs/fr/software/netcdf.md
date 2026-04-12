---
title: "NetCDF/fr"
slug: "netcdf"
lang: "fr"

source_wiki_title: "NetCDF/fr"
source_hash: "fb8e693dd24da59a032147b5cfe99d45"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:44:19.524991+00:00"

tags:
  - software

keywords:
  - "modules d'environnement"
  - "C"
  - "format de données"
  - "Fortran"
  - "PnetCDF"
  - "parallèle"
  - "ncdump"
  - "parallélisation"
  - "ncgen"
  - "NetCDF"
  - "MPI"
  - "Utilitaires"
  - "HDF5"

questions:
  - "Qu'est-ce que NetCDF et quels sont ses principaux avantages et inconvénients pour la gestion de données scientifiques ?"
  - "Comment sélectionner et charger les modules d'environnement NetCDF appropriés en fonction du langage de programmation (C, C++, Fortran) et des besoins en parallélisation (MPI) ?"
  - "Quelles sont les commandes et les étapes requises pour compiler et lier correctement des programmes en C ou en Fortran aux bibliothèques NetCDF ?"
  - "Comment doit-on procéder pour compiler un programme utilisant la bibliothèque NetCDF selon l'exemple fourni ?"
  - "Quels sont les rôles spécifiques des utilitaires ncdump, ncgen et nccopy dans la gestion et la conversion des fichiers NetCDF ?"
  - "Qu'est-ce que la bibliothèque PnetCDF et quelles sont ses particularités par rapport à la bibliothèque NetCDF standard ?"
  - "Comment compiler un programme en C utilisant la bibliothèque NetCDF en mode série ?"
  - "Quelles bibliothèques et options de compilation doivent être spécifiées pour un programme en Fortran utilisant NetCDF ?"
  - "Quel module doit être chargé pour préparer la compilation d'un programme en C faisant appel à NetCDF en parallèle avec MPI ?"
  - "Comment doit-on procéder pour compiler un programme utilisant la bibliothèque NetCDF selon l'exemple fourni ?"
  - "Quels sont les rôles spécifiques des utilitaires ncdump, ncgen et nccopy dans la gestion et la conversion des fichiers NetCDF ?"
  - "Qu'est-ce que la bibliothèque PnetCDF et quelles sont ses particularités par rapport à la bibliothèque NetCDF standard ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Généralités

NetCDF (pour *Network Common Data Form*) est :
*   une interface pour un accès aux données orienté tableaux et
*   une bibliothèque qui fournit une implémentation de cette interface.

Son format de données autodocumenté et indépendant de l'architecture matérielle permet la création, l'accès et le partage de données scientifiques.

Plusieurs modifications ont été apportées à la bibliothèque avec la version 4 mise en production en 2008; il ne sera pas question ici des versions précédentes. NetCDF 4.x est rétrocompatible, mais les versions antérieures ne peuvent utiliser les nouveaux fichiers.

*   Site web du projet : [https://www.unidata.ucar.edu/software/netcdf](https://www.unidata.ucar.edu/software/netcdf)
*   Documentation : [https://www.unidata.ucar.edu/software/netcdf/docs](https://www.unidata.ucar.edu/software/netcdf/docs)
*   Fichiers à télécharger : [https://www.unidata.ucar.edu/downloads/netcdf/index.jsp](https://www.unidata.ucar.edu/downloads/netcdf/index.jsp)
*   FAQ : [https://www.unidata.ucar.edu/software/netcdf/docs/faq.html](https://www.unidata.ucar.edu/software/netcdf/docs/faq.html)

### Points forts
*   Les données sont indépendantes de l'architecture matérielle ([boutisme ou *endianness*](https://fr.wikipedia.org/wiki/Endianness)).
*   Les données structurées en unités physiques permettent le suivi de l'information pertinente.
*   NetCDF4 écrit et lit en parallèle si construit avec une version parallèle de [HDF5](hdf5.md).
*   Les données peuvent être compressées à l'écriture.
*   Interface plus simple que HDF5.
*   Gratuit pour la plupart des plateformes.

### Points faibles
*   L'interface Python ne permet pas la parallélisation (version 1.0.5).
*   Certains fichiers produits avec [HDF5](hdf5.md) ne peuvent être lus par NetCDF.

## Guide de démarrage
Nous abordons ici les détails de configuration.

### Modules d'environnement

Les [modules](../programming/utiliser_des_modules.md) suivants sont disponibles via CVMFS :
*   **netcdf**
    *   pour lier avec les programmes contenant uniquement des instructions en C
*   **netcdf-c++**
    *   pour lier avec les programmes contenant des instructions en C et en C++
*   **netcdf-fortran**
    *   pour lier avec les programmes contenant des instructions en Fortran

D'autres modules utilisent [MPI](mpi.md) pour permettre des entrées/sorties en parallèle :
*   **netcdf-mpi**
    *   pour lier avec les programmes contenant des instructions en C et faisant appel à des bibliothèques MPI
*   **netcdf-c++-mpi**
    *   pour lier avec les programmes contenant des instructions en C et C++ et faisant appel à des bibliothèques MPI
*   **netcdf-fortran-mpi**
    *   pour lier avec les programmes contenant des instructions en Fortran et faisant appel à des bibliothèques MPI

Exécutez `module avail netcdf` pour connaître les versions disponibles pour le compilateur et les modules MPI que vous avez chargés. Pour la liste complète des modules NetCDF, exécutez `module -r spider '.*netcdf.*'`.

Utilisez `module load netcdf/version` pour configurer l'environnement selon la version sélectionnée. Par exemple, pour charger la bibliothèque NetCDF version 4.1.3 pour C, lancez

```bash
module load netcdf/4.1.3
```

### Soumettre un script
Consultez [Exécuter des tâches](../running-jobs/running_jobs.md) pour des exemples de scripts soumis à l'ordonnanceur Slurm. Nous vous recommandons d'inclure la commande `module load ...` dans votre script.

### Lier des programmes à des bibliothèques NetCDF
Les exemples qui suivent montrent comment lier des bibliothèques NetCDF à des programmes en C et en Fortran.

#### NetCDF en série
Programme en C :
```bash
module load netcdf/4.4.1
gcc example.c -lnetcdf
```

Programme en Fortran : il faut spécifier deux bibliothèques dans l'ordre approprié.
```bash
module load gcc netcdf-fortran
gfortran example.f90 -I$EBROOTNETCDFMINFORTRAN/include -lnetcdf -lnetcdff
```

#### NetCDF en parallèle
Programme en C faisant appel à MPI :
```bash
module load netcdf-mpi
gcc example.c -lnetcdf
```

#### Exemple
Dans [cet exemple](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf-tutorial/simple_005fxy_005fwr_002ec.html#simple_005fxy_005fwr_002ec), un fichier NetCDF est créé et contient une seule variable bidimensionnelle nommée *data* dont les dimensions sont *x* et *y*.

Pour compiler l'exemple,
```bash
module load netcdf
gcc ex_netcdf4.c -lnetcdf
```

### Utilitaires
Plusieurs utilitaires peuvent lire et écrire des fichiers selon différents formats.
*   ncdump : Cet outil génère la représentation texte CDL d'un ensemble de données netCDF avec l'option d'exclure certaines ou toutes les données variables. Le résultat peut en principe être utilisé en entrée avec ncgen. ncdump et ncgen peuvent donc être employés pour convertir une représentation binaire en représentation texte et vice versa. Consultez [la section ncdump](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf/ncdump.html) du site web UCAR.
*   ncgen : À l'inverse de ncdump, cet outil génère un fichier binaire NetCDF. Consultez [la section ncgen](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf/ncgen.html#ncgen).
*   nccopy : Copie un fichier netCDF en pouvant modifier le format binaire, la taille des blocs, la compression et d'autres paramètres de stockage. Consultez [la section nccopy](https://www.unidata.ucar.edu/software/netcdf/workshops/2011/utilities/Nccopy.html).

Pour vous aider à trouver les commandes pour lier et compiler, utilisez les utilitaires `nf-config` et `nc-config`; consultez la [documentation](https://www.unidata.ucar.edu/software/netcdf/workshops/2012/utilities/Nc-config.html).

## PnetCDF
PnetCDF est une autre bibliothèque pour la lecture et l'écriture de fichiers au format NetCDF. Les noms de ses procédures sont différents de ceux de NetCDF. La bibliothèque offre aussi des procédures non-blocantes. Consultez [le site web PnetCDF](https://trac.mcs.anl.gov/projects/parallel-netcdf) pour plus d'information.