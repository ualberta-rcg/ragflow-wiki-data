---
title: "AMS/fr"
slug: "ams"
lang: "fr"

source_wiki_title: "AMS/fr"
source_hash: "bfecfaebac727dbfc03d137b450c2816"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:07:05.279504+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

## Introduction
AMS (Amsterdam Modeling Suite) est la nouvelle appellation d'ADF (Amsterdam Density Functional) et fait partie de la suite [SCM Software for Chemistry and Materials](https://www.scm.com/). AMS offre des outils très performants pour la recherche en chimie computationnelle, notamment dans les domaines de la catalyse (homogène et hétérogène), la chimie inorganique, la chimie des éléments lourds, la biochimie et différents types de spectroscopie.

Tous les produits du module SCM sont disponibles :
*   ADF
*   ADF-GUI
*   BAND
*   BAND-GUI
*   DFTB
*   ReaxFF
*   COSMO-RS
*   QE-GUI
*   NBO6

## Utiliser AMS sur Nibi
Le module `ams` est installé sur [Nibi](../clusters/nibi.md). SHARCNET est propriétaire de cette licence qui est réservée aux centres de calcul universitaires; cette licence ne peut être utilisée pour des services de consultation ou pour tout autre usage de nature commerciale. Pour connaître les versions disponibles, lancez la commande :

```bash
module spider ams
```

Pour les commandes en rapport avec les modules, voyez [Utiliser des modules](../programming/utiliser_des_modules.md).

### Soumettre une tâche

Les tâches soumises sur nos grappes sont ordonnancées par Slurm; pour les détails, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

#### Exemples de scripts pour une tâche AMS

!!! info "Utilisation des ressources"
    Le script suivant demande 32 CPU sur un nœud. Veuillez utiliser un nombre raisonnable de CPU au lieu de simplement exécuter une tâche sur un nœud complet de Nibi, à moins que vous n'ayez démontré que votre tâche peut utiliser efficacement 192 CPU.

```bash linenums="1" title="H2O_adf.sh"
#!/bin/bash
#SBATCH --account=def-pi
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32          # 32 cpus on 1 node, MPI job
#SBATCH --mem-per-cpu=3G              # memory per cpu
#SBATCH --time=00-01:00               # time (DD-HH:MM)
#SBATCH --output=H2O_adf-%j.log       # output .log file

module unload openmpi
module load ams/2025.102
export SCM_TMPDIR=$SLURM_TMPDIR      # use the local disk
bash H2O_adf.run                    # run the input script
```

Le fichier en entrée ci-dessous est utilisé dans le script.

```text linenums="1" title="H2O_adf.run"
#!/bin/sh
# This is a shell script for AMS
# You should use '$AMSBIN/ams' instead of '$ADFBIN/adf'

AMS_JOBNAME=H2O_adf $AMSBIN/ams <<eor
   # Input options for the AMS driver:
   System
      Atoms
         O             0.000000     0.000000     0.000000
         H             0.000000    -0.689440    -0.578509
         H             0.000000     0.689440    -0.578509
      End
   End
   Task GeometryOptimization
   GeometryOptimization
      Convergence gradients=1e-4
   End

   # The input options for ADF, which are described in this manual,
   # should be specified in the 'Engine ADF' block:

   Engine ADF
      Basis
         Type TZP
      End
      XC
         GGA PBE
      End
   EndEngine
eor
```

#### Exemples de scripts pour une tâche BAND

```bash linenums="1" title="SnO_EFG_band.run"
#!/bin/sh
# The calculation of the electric field gradient is invoked by the EFG key block
# Since Sn is quite an heavy atom we use the scalar relativistic option.

$AMSBIN/ams <<eor

Task SinglePoint
System
   FractionalCoords True

   Lattice
      3.8029  0.0  0.0
      0.0  3.8029  0.0
      0.0  0.0  4.8382
   End

   Atoms
      O   0.0  0.0  0.0
      O   0.5  0.5  0.0
      Sn  0.0  0.5  0.2369
      Sn  0.5  0.0 -0.2369
   End
End

Engine Band
   Title SnO EFG
   NumericalQuality Basic      ! Only for speed
   Tails bas=1e-8              ! Only for reproducibility with nr. of cores
   ! useful for Moessbauer spectroscopy: density and coulomb pot. at nuclei
   PropertiesAtNuclei
   End

   EFG
      Enabled True
   End

   Basis
      Type DZ
      Core none
   End
EndEngine
eor
```

### Remarques

1.  !!! warning "Compatibilité des fichiers d'entrée"
    Le fichier en entrée pour AMS est différent de celui pour ADF; le fichier en entrée précédent pour ADF ne fonctionnera pas avec le nouveau AMS. Vous trouverez des exemples dans `/opt/software/ams/2025.102/examples/`.
2.  À l'exception du fichier en sortie `.log`, les fichiers sont tous sauvegardés dans le sous-répertoire `AMS_JOBNAME.results`. Si `AMS_JOBNAME` n'est pas défini dans le fichier en entrée `.run`, le nom par défaut sera `ams.results`.
3.  Le nom du fichier de point de sauvegarde est `ams.rkf` plutôt que `TAPE13` dans les versions ADF précédentes.

Pour plus d'information, consultez [SCM Support](https://www.scm.com/support/).

## AMS-GUI sur Nibi

Pour utiliser AMS en mode graphique sur le bureau de nœud de calcul (OnDemand Compute Node Desktop), suivez ces étapes :

1.  Connectez-vous à [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca).
2.  Dans le menu déroulant du haut, sélectionnez *Nœud de calcul > Bureau de calcul*.
3.  Pour la visualisation, entrez les valeurs *Ordinateurs=1*, *Cœurs=1*, *UCG=Aucun* et cliquez sur *Lancer*.
4.  Quand l'état du bureau passe de *En attente* à *En cours d'exécution*, appuyez sur *Lancer le bureau Nibi*.
5.  Quand le bureau est affiché, sélectionnez *Applications > Outils système > Terminal MATE*.
6.  `module unload openmpi`
7.  `module load ams` (pour changer la version courante)
8.  `export SCM_OPENGL_SOFTWARE=1` (pour activer le rendu logiciel)
9.  `amsinput` ou `amsview`

Par contre, si vous avez spécifié UCG=t4 (15GB) au lancement du bureau, utilisez plutôt :

`LD_PRELOAD= amsinput` ou `LD_PRELOAD= amsview`

!!! tip "Astuce de sélection"
    Pour sélectionner un ou plusieurs atomes, gardez MAJ enfoncée puis cliquez.