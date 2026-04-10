---
title: "ADF/fr"
slug: "adf"
lang: "fr"

source_wiki_title: "ADF/fr"
source_hash: "f3d2d5299c2ad6d173c24e6984ac61bd"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:20:21.829631+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "SCM"
  - "WATER"
  - "nœud de calcul"
  - "ADF"
  - "SCM-GUI"
  - "Basis Type TZP"
  - "Z-Matrix"
  - "Graham"
  - "TigerVNC"
  - "Internal Coordinates"
  - "Geometry Optimization"
  - "chimie computationnelle"
  - "AMS"

questions:
  - "Quelles sont les principales applications de la suite logicielle SCM (anciennement ADF) en chimie computationnelle ?"
  - "Pourquoi le module adf est-il exclusivement installé sur la grappe Graham et comment peut-on vérifier les versions disponibles ?"
  - "Comment configurer un script pour soumettre une tâche unique ou grouper plusieurs calculs dans une même tâche avec Slurm ?"
  - "Comment doit-on configurer le script SLURM pour exécuter une tâche d'optimisation avec ADF sur une grappe de calcul ?"
  - "Quelle est la méthode recommandée pour utiliser l'interface graphique ADF-GUI à distance (sur Graham ou gra-vdi) afin d'éviter les lenteurs de la redirection X11 ?"
  - "Quelle est la procédure pour obtenir une licence permettant d'utiliser ADF-GUI localement sur un ordinateur de bureau ?"
  - "What specific computational task and convergence criteria are defined in the first section of the input?"
  - "Which basis set and core size are specified for the calculation?"
  - "How are the internal coordinates of the water molecule structured in the Z-Matrix section?"
  - "Comment doit-on configurer le script SLURM pour exécuter une tâche d'optimisation avec ADF sur une grappe de calcul ?"
  - "Quelle est la méthode recommandée pour utiliser l'interface graphique ADF-GUI à distance (sur Graham ou gra-vdi) afin d'éviter les lenteurs de la redirection X11 ?"
  - "Quelle est la procédure pour obtenir une licence permettant d'utiliser ADF-GUI localement sur un ordinateur de bureau ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

!!! warning "Attention"
    La suite ADF a été renommée AMS depuis la version de 2020. Cette nouvelle version comporte des changements importants, notamment dans les formats d'entrée et de sortie. Pour plus d'information, voir [AMS](ams.md).

La suite logicielle [SCM (Software for Chemistry and Materials)](https://www.scm.com/), à l'origine la suite ADF pour *Amsterdam Density Functional*, offre des applications très performantes pour la recherche en chimie computationnelle, notamment dans les domaines de la catalyse (homogène et hétérogène), la chimie inorganique, la chimie des éléments lourds, la biochimie et différents types de spectroscopie.

Les produits suivants sont disponibles :
*   ADF
*   ADF-GUI
*   BAND
*   BAND-GUI
*   DFTB
*   ReaxFF
*   COSMO-RS
*   QE-GUI
*   NBO6

## Utiliser SCM sur Graham

Le module `adf` est seulement installé sur [Graham](graham.md) en raison de restrictions liées à l'octroi des licences. Pour connaître les versions disponibles, lancez la commande

```bash
module spider adf
```

Pour les commandes en rapport avec les modules, voyez [Utiliser des modules](utiliser-des-modules.md).

### Soumettre une tâche

Les tâches soumises sur Graham sont ordonnancées par Slurm; pour les détails, consultez [Exécuter des tâches](running-jobs.md).

#### Tâche unique

Le script suivant utilise un nœud entier; l'avant-dernière ligne charge la version 2019.305 et la dernière ligne appelle ADF directement.

```bash title="mysub.sh"
#!/bin/bash
#SBATCH --nodes=1 --ntasks-per-node=32  # 1 node with 32 cpus, you can modify it
#SBATCH --mem=0                         # request all memory on node
#SBATCH --time=00-03:00                 # time (DD-HH:MM)
#SBATCH --output=adf_test-%j.log        # output file

module unload openmpi
module load adf/2019.305
ADF adf_test.inp  
```

Le fichier en entrée ci-dessous est utilisé dans le script.

```text title="adf_test.inp"
 Title WATER Geometry Optimization with Delocalized Coordinates

 Atoms
    O             0.000000     0.000000     0.000000
    H             0.000000    -0.689440    -0.578509
    H             0.000000     0.689440    -0.578509
 End

 Basis
 Type TZP
 Core Small
 End

 Geometry
  Optim Deloc
  Converge 0.0000001
 End

 End Input
```

#### Tâches multiples avec ADF ou BAND

Plusieurs calculs peuvent être groupés dans une même tâche avec un script semblable à celui-ci :

```bash title="GO_H2O.run"
#!/bin/bash
if test -z "$SCM_TESTOUTPUT" ; then SCM_TESTOUTPUT=GO_H2O.out; fi

$ADFBIN/adf << eor > $SCM_TESTOUTPUT
Title WATER Geometry Optimization with Delocalized Coordinates

Atoms
   O             0.000000     0.000000     0.000000
   H             0.000000    -0.689440    -0.578509
   H             0.000000     0.689440    -0.578509
End

Basis
Type TZP
Core Small
End

Geometry
 Optim Deloc
 Converge 0.0000001
End

End Input
eor

rm TAPE21 logfile
$ADFBIN/adf << eor >> $SCM_TESTOUTPUT
Title WATER Geometry Optimization in Cartesians with new optimizer

Atoms
    O             0.000000     0.000000     0.000000
    H             0.000000    -0.689440    -0.578509
    H             0.000000     0.689440    -0.578509
End

Basis
 Type TZP
 Core Small
End

Geometry
  Optim Cartesian
  Branch New
  Converge 0.0000001
End

End Input
eor

rm TAPE21 logfile
$ADFBIN/adf << eor >> $SCM_TESTOUTPUT
Title WATER Geometry Optimization with Internal Coordinates

Atoms    Z-Matrix
 1. O   0 0 0
 2. H   1 0 0   rOH
 3. H   1 2 0   rOH  theta
End

Basis
 Type TZP
 Core Small
End

GeoVar
 rOH=0.9
 theta=100
End
Geometry
  Converge 0.0000001
End

End Input
eor

rm TAPE21 logfile
$ADFBIN/adf << eor >> $SCM_TESTOUTPUT
Title WATER   optimization with (partial) specification of Hessian

Atoms    Z-Matrix
 1. O   0 0 0
 2. H   1 0 0   rOH
 3. H   1 2 0   rOH  theta
End

GeoVar
 rOH=0.9
 theta=100
End
HessDiag  rad=1.0  ang=0.1

Fragments
 H   t21.H
 O   t21.O
End

Geometry
  Converge 0.0000001
End

End Input
eor

rm TAPE21 logfile
$ADFBIN/adf << eor >> $SCM_TESTOUTPUT
Title WATER Geometry Optimization in Cartesians

Geometry
  Optim Cartesian
  Converge 0.0000001
End

Define
 rOH=0.9
 theta=100
End

Atoms    Z-Matrix
 1. O   0 0 0
 2. H   1 0 0   rOH
 3. H   1 2 0   rOH theta
End

Fragments
 H   t21.H
 O   t21.O
End

End Input
eor

mv TAPE21 H2O.t21
```

Le script suivant est identique à celui utilisé pour une tâche unique (mysub.sh), à l’exception de la dernière ligne qui appelle le script `GO_H2O.run` plutôt que d’appeler ADF directement.

```bash title="GO_H2O.sh"
#!/bin/bash
#SBATCH --nodes=1 --ntasks-per-node=32  # 1 node with 32 cpus, you can modify it
#SBATCH --mem=0                         # request all memory on node
#SBATCH --time=00-03:00                 # time (DD-HH:MM)
#SBATCH --output=GO_H2O_%j.log          # output file

module unload openmpi
module load adf/2019.305
bash GO_H2O.run                         # run the shell script
```

### Exemples

Pour des exemples d’entrée/sortie pour ADF, voyez sur Graham :
` /home/jemmyhu/tests/test_ADF/2019.305/test_adf/`

Pour des exemples de fichiers `.inp` et `.sh` avec BAND, voyez sur Graham :
` /home/jemmyhu/tests/test_ADF/2019.305/test_band`

## Utiliser SCM-GUI

Avec des applications comme ADF-GUI, la redirection X11 via une connexion SSH exige beaucoup de temps pour produire les rendus. Nous recommandons de vous connecter avec [VNC](vnc.md).

### Graham

Sur un nœud de calcul de Graham, ADF peut être utilisé interactivement en mode graphique avec TigerVNC pour une durée maximale de 3 heures.

1.  [Installez un client TigerVNC](vnc.md#configuration) sur votre ordinateur.
2.  [Connectez-vous à un nœud de calcul](vnc.md#noeuds-de-calcul) avec `vncviewer`.
3.  `module load adf`
4.  `adfinput`

### Gra-vdi

Sur gra-vdi, ADF peut être utilisé interactivement en mode graphique, sans limite de durée.

1.  [Installez un client TigerVNC](vnc.md#configuration) sur votre ordinateur.
2.  [Connectez-vous à gra-vdi.computecanada.ca](vnc.md#noeuds-vdi) avec `vncviewer`.
3.  `module load clumod`
4.  `module load adf`
5.  `adfinput`

Voyez [ce tutoriel sur comment utiliser ADF-GUI avec TigerVNC sur gra-vdi](https://www.sharcnet.ca/~jemmyhu/TigerVNC-for-ADF-GUI.pdf) (en anglais).

### Utiliser ADF-GUI localement

SCM offre une licence distincte pour utiliser ADF-GUI sur un ordinateur de bureau local; pour acquérir votre propre licence, contactez [license@scm.com](mailto:license@scm.com).