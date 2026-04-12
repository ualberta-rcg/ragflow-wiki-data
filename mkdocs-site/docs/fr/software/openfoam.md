---
title: "OpenFOAM/fr"
slug: "openfoam"
lang: "fr"

source_wiki_title: "OpenFOAM/fr"
source_hash: "60bbc69659015cadeabe03f0d3c9bde1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:01:50.254131+00:00"

tags:
  - software

keywords:
  - "solveur petscFoam"
  - "petsc/3.21.6"
  - "dynamique des fluides"
  - "espace scratch local"
  - "performance"
  - "corrections de bogues"
  - "modélisation numérique"
  - "PETSc"
  - "OpenFOAM"
  - "module"
  - "PETSc 3.21.2"
  - "openfoam/v2412"
  - "compilation"
  - "solveur"

questions:
  - "Qu'est-ce qu'OpenFOAM et quels sont ses principaux domaines d'application ?"
  - "Comment le système de nommage des modules permet-il de distinguer les versions issues de la branche .com de celles de la branche .org ?"
  - "Comment doit-on préparer son environnement et configurer ses scripts pour exécuter des tâches séquentielles ou parallèles avec OpenFOAM ?"
  - "Quelles sont les étapes requises pour télécharger, extraire et compiler le solveur petscFoam ?"
  - "Comment peut-on confirmer que le solveur petscFoam est fonctionnel et que ses dépendances sont bien trouvées ?"
  - "Quelles stratégies d'optimisation permettent de réduire l'impact des opérations d'écriture sur les performances du système de fichiers ?"
  - "Avec quelle version de PETSc la version openfoam/v2412 a-t-elle été testée lors de sa sortie ?"
  - "Quelle commande a été utilisée pour déterminer la version de PETSc configurée avec OpenFOAM ?"
  - "Quelles sont les différences attendues entre la version PETSc 3.21.2 et le module petsc/3.21.6 mentionné ?"
  - "Quelles sont les étapes requises pour télécharger, extraire et compiler le solveur petscFoam ?"
  - "Comment peut-on confirmer que le solveur petscFoam est fonctionnel et que ses dépendances sont bien trouvées ?"
  - "Quelles stratégies d'optimisation permettent de réduire l'impact des opérations d'écriture sur les performances du système de fichiers ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[OpenFOAM](https://fr.wikipedia.org/wiki/OpenFOAM) (pour *Open Field Operation and Manipulation*) est un paquet logiciel **open source** gratuit pour la modélisation numérique de la dynamique des fluides. Ses nombreuses fonctions touchent autant l'électromagnétisme et la dynamique des solides que les flux liquides complexes avec réaction chimique, turbulence et transfert thermique.

## Modules

```bash
module load openfoam
```

La communauté OpenFOAM comprend :
* La OpenFOAM Foundation avec ses sites web [openfoam.org](https://openfoam.org/) et [cfd.direct](https://cfd.direct/),
* OpenCFD avec son site web [openfoam.com](https://www.openfoam.com/).

Les versions semblent identiques jusqu'à 2.3.1 (décembre 2014). Pour les versions après 2.3.1 :
* Les modules dont le nom commence par la lettre v sont dérivés de la branche .com (par exemple, `` `openfoam/v1706` ``) ;
* Les modules dont le nom commence par un chiffre sont dérivés de la branche .org (par exemple, `` `openfoam/4.1` ``).

Pour plus d'information sur les commandes, consultez [Utiliser des modules](../programming/utiliser_des_modules.md).

## Documentation

* [documentation OpenFOAM.com](https://www.openfoam.com/documentation/)
* [CFD Direct, Guide de l'utilisateur](https://cfd.direct/openfoam/user-guide/).

## Utilisation

Votre environnement nécessite beaucoup de préparation. Pour pouvoir exécuter les commandes OpenFOAM (`` `paraFoam` ``, `` `blockMesh` ``, etc.), vous devez charger un [module](../programming/utiliser_des_modules.md).

Le script suivant est pour une tâche séquentielle avec OpenFOAM 5.0 :
````bash title="submit.sh"
#!/bin/bash
#SBATCH --time=00:01:00
#SBATCH --account=def-someuser

module purge
module load openfoam/12

blockMesh
icoFoam
````

Le script suivant est pour une tâche parallèle :
````bash title="submit.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --ntasks=4               # number of MPI processes
#SBATCH --mem-per-cpu=1024M      # memory; default unit is megabytes
#SBATCH --time=0-00:10           # time (DD-HH:MM)

module purge
module load openfoam/12

blockMesh
setFields
decomposePar
srun interFoam -parallel
````

La préparation du maillage (`` `blockMesh` ``) peut être assez rapide pour se faire en ligne de commande (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). L'étape la plus exigeante est habituellement celle du solveur (entre autres `` `icoFoam` ``) ; ces tâches devraient toujours être soumises à l'ordonnanceur, sauf pour de très petits cas ou des tutoriels.

## Solveur petscFoam

OpenFOAM peut être compilé avec le solveur externe petscFoam. Nos modules OpenFOAM n'incluent pas ce solveur, mais la compilation peut se faire sur toutes nos grappes.

Les versions d'OpenFOAM et de PETSc doivent être compatibles. Par exemple, les combinaisons suivantes sont valides :

* `` `openfoam/v2412` `` et `` `petsc/3.21.6` ``
* `` `openfoam/v2312` `` et `` `petsc/3.20.0` ``

### Compatibilité des versions d'OpenFOAM et de PETSc

Pour vérifier quelle version mineure de PETSc est compatible avec une version particulière d'OpenFOAM, chargez le module OpenFOAM souhaité et exécutez la commande `` `grep` ``.

```bash
module load openfoam/v2412 && grep "^petsc_version" $EBROOTOPENFOAM/OpenFOAM*/etc/config.sh/petsc
```

```text
petsc_version=petsc-3.21.2
```

Nous savons ainsi que quand `` `openfoam/v2412` `` est sortie, les tests ont été faits avec PETSc 3.21.2.

Nous avons un module pour `` `petsc/3.21.6` `` issu de la même branche 3.21 et qui ne devrait contenir que des corrections de bogues par rapport à la version 3.21.2.

### Compiler le solveur petscFoam

Il faut maintenant télécharger et extraire le paquet `` `external-solver-main.tar.gz` ``.
```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 openfoam/v2412 petsc/3.21.6
wget https://develop.openfoam.com/modules/external-solver/-/archive/main/external-solver-main.tar.gz
tar xvfz external-solver-main.tar.gz
cd tar xvfz external-solver-main
```

L'exécution de `` `./Allmake` `` compilera le solveur petscFoam.
```bash
./Allwmake
```

```text
========================================
2025-08-14 15:00:00 -0400
Starting compile of external-solver (petsc) with OpenFOAM-v2412
[...]
========================================
  Finished compile of external-solver (petsc) with OpenFOAM-v2412
  Gcc system compiler
  linux64GccDPInt32Opt, with EASYBUILDMPI eb-mpi
```

### Confirmer que le solveur petscFoam est fonctionnel

Quelques tests rapides peuvent confirmer ceci.

Vérifiez si OpenFOAM peut charger petscFoam.
```bash
foamHasLibrary -verbose petscFoam
```

```text
Can load "petscFoam"
```

Vérifiez si la bibliothèque dynamique se trouve dans `` `$FOAM_USER_LIBBIN` ``.
```bash
ls $FOAM_USER_LIBBIN
```

```text
libpetscFoam.so
```

Vérifiez si `` `libpetscFoam.so` `` peut trouver ses dépendances.
```bash
ldd $FOAM_USER_LIBBIN/libpetscFoam.so | grep petsc
```

```text
 libpetsc.so.3.21 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libpetsc.so.3.21 (0x00007f96fa800000)
 libstrumpack.so.7.2 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libstrumpack.so.7.2 (0x00007f96f8200000)
 libml.so.13 => /cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/gcc12/openmpi4/petsc/3.21.6/lib/libml.so.13 (0x00007f96fa281000)
```

## Performance

La fonction de débogage produit fréquemment des centaines d'opérations d'écriture par seconde, ce qui peut causer une baisse de performance des systèmes de fichiers partagés. Si vous êtes en production et que vous n'avez pas besoin de cette information, diminuez ou désactivez la fonction de débogage avec :
```bash
mkdir -p $HOME/.OpenFOAM/$WM_PROJECT_VERSION
cp $WM_PROJECT_DIR/etc/controlDict $HOME/.OpenFOAM/$WM_PROJECT_VERSION/
```

Plusieurs autres paramètres peuvent diminuer la quantité et la fréquence des écritures sur disque ; voir la documentation pour la [version 6](https://cfd.direct/openfoam/user-guide/v6-controldict/) et la [version 7](https://cfd.direct/openfoam/user-guide/v7-controldict/).

Par exemple, le dictionnaire `` `debugSwitches` `` dans `` `$HOME/.OpenFOAM/$WM_PROJECT_VERSION/controlDict` `` peut être modifié pour que les valeurs des indicateurs qui sont plus grandes que zéro soient égales à zéro. Une autre solution serait d'utiliser l'espace scratch local (`` `$SLURM_TMPDIR` ``) qui est un disque attaché directement au nœud de calcul ; voir la [section Disque local dans la page Travailler avec un grand nombre de fichiers](../storage-and-data/handling_large_collections_of_files.md#disque-local).

### Espace /scratch local sur un nœud de calcul

Si votre flux de travail crée plusieurs petits fichiers, il serait préférable d'utiliser `` `$SLURM_TMPDIR` `` comme répertoire de travail. Pour plus d'information, voir [Stockage local sur les nœuds de calcul](../storage-and-data/using_node-local_storage.md).