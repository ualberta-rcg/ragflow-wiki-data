---
title: "AMS/fr"
slug: "ams"
lang: "fr"

source_wiki_title: "AMS/fr"
source_hash: "1ed4c9281aaedab74583f4e3c88b03c2"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:24:55.227795+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "soumission de tâches"
  - "AMS-GUI"
  - "electric field gradient"
  - "Nibi"
  - "ADF"
  - "AMS (Amsterdam Modeling Suite)"
  - "SinglePoint"
  - "FractionalCoords"
  - "OnDemand"
  - "EFG key block"
  - "scalar relativistic option"
  - "fichier en entrée"
  - "chimie computationnelle"
  - "AMS"

questions:
  - "Qu'est-ce que la suite logicielle AMS et quels sont les principaux modules et domaines de recherche qu'elle prend en charge ?"
  - "Quelles sont les restrictions de licence et les conditions d'utilisation du module AMS sur la grappe Nibi ?"
  - "Comment configurer correctement un script de soumission de tâche Slurm pour exécuter une simulation AMS ou BAND ?"
  - "Quelles sont les principales différences entre AMS et ADF concernant les fichiers d'entrée et la sauvegarde des résultats ?"
  - "Quelles sont les étapes spécifiques pour lancer l'interface graphique AMS-GUI interactivement via OnDemand sur le cluster Nibi ?"
  - "Quelles sont les recommandations et restrictions à respecter lors de l'utilisation de Nibi Desktop pour les applications AMS ?"
  - "How is the calculation of the electric field gradient invoked in the script?"
  - "Why is the scalar relativistic option used for this specific system?"
  - "What are the lattice parameters and atomic coordinates defined for the single point calculation?"
  - "Quelles sont les principales différences entre AMS et ADF concernant les fichiers d'entrée et la sauvegarde des résultats ?"
  - "Quelles sont les étapes spécifiques pour lancer l'interface graphique AMS-GUI interactivement via OnDemand sur le cluster Nibi ?"
  - "Quelles sont les recommandations et restrictions à respecter lors de l'utilisation de Nibi Desktop pour les applications AMS ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
AMS (Amsterdam Modeling Suite) est la nouvelle appellation d'[ADF](adf.md) (Amsterdam Density Functional) et fait partie de la suite [SCM Software for Chemistry and Materials](https://www.scm.com/). AMS offre des outils très performants pour la recherche en chimie computationnelle, notamment dans les domaines de la catalyse (homogène et hétérogène), la chimie inorganique, la chimie des éléments lourds, la biochimie et différents types de spectroscopie.

Tous les produits du module SCM sont disponibles :
* ADF
* ADF-GUI
* BAND
* BAND-GUI
* DFTB
* ReaxFF
* COSMO-RS
* QE-GUI
* NBO6

## Utiliser AMS sur Nibi
Le module `ams` est installé sur [Nibi](../clusters/nibi.md). SHARCNET est propriétaire de cette licence qui est réservée aux centres de calcul universitaires; cette licence ne peut être utilisée pour des services de consultation ou pour tout autre usage de nature commerciale. Pour connaître les versions disponibles, lancez la commande :

```bash
module spider ams
```

Pour les commandes en rapport avec les modules, voyez [Utiliser des modules](../programming/utiliser_des_modules.md).

### Soumettre une tâche
Les tâches soumises sur nos grappes sont ordonnancées par Slurm; pour les détails, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

#### Exemples de scripts pour une tâche AMS
Le script suivant demande 32 CPU sur un nœud. Veuillez utiliser un nombre raisonnable de CPU au lieu de simplement exécuter une tâche sur un nœud complet de Nibi, à moins que vous n'ayez démontré que votre tâche peut utiliser efficacement 192 CPU.

```bash title="H2O_adf.sh"
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

```text title="H2O_adf.run"
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

```bash title="SnO_EFG_band.run"
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
1. Le fichier en entrée pour AMS est différent de celui pour ADF; le fichier en entrée précédent pour ADF ne fonctionnera pas avec le nouveau AMS. Vous trouverez des exemples dans `/opt/software/ams/2025.102/examples/`.
2. À l'exception du fichier en sortie `.log`, les fichiers sont tous sauvegardés dans le sous-répertoire `AMS_JOBNAME.results`. Si `AMS_JOBNAME` n'est pas défini dans le fichier en entrée `.run`, le nom par défaut sera `ams.results`.
3. Le nom du fichier de point de sauvegarde est `ams.rkf` plutôt que `TAPE13` dans les versions ADF précédentes.

Pour plus d'information, consultez [SCM Support](https://www.scm.com/support/).

## AMS-GUI
### Nibi
Sur un nœud de calcul de Nibi (durée limite de 8 heures), AMS peut être utilisée interactivement en mode graphique via OnDemand en suivant ces étapes :

1. Connectez-vous à [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca).
2. Sélectionnez *Bureau Nibi* dans *Calcul* (dans le haut).
3. Sélectionnez vos options (sélectionnez 1 cœur pour une visualisation; ne sélectionnez pas *Activer VirtualGL*) et cliquez sur *Lanceur*.
4. Sélectionnez *Lanceur Bureau Nibi* une fois que la tâche est lancée.
5. Faites un clic droit sur le bureau et sélectionnez *Ouvrir un terminal*.
6. Sélectionnez *Terminal MATE* dans le menu *Outils Système* sous *Applications*.
7. `module unload openmpi`
8. `module load ams`
9. `amsinput &` (créer des fichiers d'entrée)
10. `amsview &` (visualiser les résultats)

Si vous devez sélectionner *Activer VirtualGL* pour un autre programme que vous utilisez, vous devez d'abord le désactiver pour AMS en le lançant avec `LD_PRELOAD= amsinput`.

!!! warning "Exécution de tâches sur le Bureau Nibi"
    Sur OnDemand, le Bureau Nibi est utilisé pour exécuter des applications AMS-GUI, par exemple pour créer les fichiers d'entrée et visualiser les résultats. Veuillez ne pas y exécuter de tâches régulières ou des tâches interactives de longue durée. Sélectionnez un seul cœur ainsi qu'une quantité de mémoire et un temps d'exécution raisonnables.