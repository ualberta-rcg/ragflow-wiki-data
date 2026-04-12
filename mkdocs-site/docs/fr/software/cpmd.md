---
title: "CPMD/fr"
slug: "cpmd"
lang: "fr"

source_wiki_title: "CPMD/fr"
source_hash: "ce1eb9d7cd34e70cc753bb13253a5856"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:05:00.501332+00:00"

tags:
  - software
  - computationalchemistry
  - biomolecularsimulation

keywords:
  - "dynamique moléculaire"
  - "hydrogen molecule"
  - "simulation ab initio"
  - "single point calculation"
  - "bash"
  - "pseudo-potentials"
  - "SBATCH"
  - "EasyBuild"
  - "pseudo-potentiels"
  - "optimize wavefunction"
  - "openmpi"
  - "CPMD"
  - "DFT functional LDA"

questions:
  - "Qu'est-ce que le programme CPMD et sur quelle théorie scientifique repose-t-il ?"
  - "Quelles sont les démarches à suivre pour obtenir les droits d'accès et charger le module CPMD sur les grappes de calcul ?"
  - "Comment doit-on configurer et lancer une tâche CPMD en parallèle avec les fichiers d'entrée et les pseudo-potentiels ?"
  - "Quelles sont les ressources de calcul (nœuds, tâches, mémoire, temps) demandées via les directives Slurm dans ces scripts ?"
  - "Quels modules d'environnement spécifiques doivent être chargés avant de lancer l'exécution de CPMD ?"
  - "Quelle est la différence principale entre le premier et le deuxième script concernant l'exécution de la commande cpmd.x ?"
  - "What type of molecule and specific calculation are being configured in this input file?"
  - "What are the defined dimensions and cutoff values for the simulation cell?"
  - "Which Density Functional Theory (DFT) functional and pseudopotential are specified for the atoms?"
  - "Quelles sont les ressources de calcul (nœuds, tâches, mémoire, temps) demandées via les directives Slurm dans ces scripts ?"
  - "Quels modules d'environnement spécifiques doivent être chargés avant de lancer l'exécution de CPMD ?"
  - "Quelle est la différence principale entre le premier et le deuxième script concernant l'exécution de la commande cpmd.x ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CPMD](https://www.cpmd.org/wordpress/) est un programme de simulation *ab initio* en dynamique moléculaire basé sur la théorie de la fonctionnelle de la densité (DFT) pour les ondes planes/pseudo-potentiels.

## Limites de la licence

Par le passé, vous deviez d'abord vous enregistrer et attendre la confirmation de l'équipe de développement, mais maintenant l'enregistrement n'est plus nécessaire. Cependant, les modules qui sont installés sur nos grappes sont protégés par un groupe POSIX.

Pour pouvoir utiliser [CPMD](http://cpmd.org) sur nos grappes, écrivez au [soutien technique](soutien-technique.md#fr) pour que nous vous ajoutions au groupe POSIX.

## Module

Pour [charger le module](../programming/utiliser_des_modules.md), lancez :

```bash
module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3
```

## Installer CPMD localement

La réponse des administrateurs de CPMD peut prendre quelques semaines et même quelques mois. Comme utilisateur enregistré, vous avez accès aux fichiers sources de CPMD; vous pouvez donc construire l'application dans votre répertoire /home avec notre environnement EasyBuild en utilisant la même recette que nous utilisons pour une installation centrale.

Pour CPMD 4.3 dans votre compte sur une de nos grappes, suivez les directives suivantes :

Créez d'abord un répertoire local.
```bash
$ mkdir -p ~/.local/easybuild/sources/c/CPMD
```

Placez les tarballs et les rustines (*patches*) dans ce répertoire.
```
$ ls -al ~/.local/easybuild/sources/c/CPMD
cpmd2cube.tar.gz
cpmd2xyz-scripts.tar.gz
cpmd-v4.3.tar.gz
fourier.tar.gz
patch.to.4612
patch.to.4615
patch.to.4616
patch.to.4621
patch.to.4624
patch.to.4627
```

Lancez ensuite la commande EasyBuild.
```bash
$ eb CPMD-4.3-iomkl-2020a.eb --rebuild
```

L'option `--rebuild` fait en sorte que EasyBuild utilise l'installation située dans votre répertoire /home plutôt que celle de l'endroit central.

Une fois l'application installée, déconnectez-vous de la grappe et reconnectez-vous à nouveau.

La commande `module load cpmd` trouvera l'application dans votre répertoire /home.
```bash
$ module load StdEnv/2020
$ module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3
$ which cpmd.x
~/.local/easybuild/software/2020/avx2/MPI/intel2020/openmpi4/cpmd/4.3/bin/cpmd.x
```

Vous pouvez maintenant l'utiliser dans un script de soumission de tâche.

## Exemples de script

Pour faire exécuter une tâche, vous devez configurer un fichier d'entrée et l'accès aux pseudo-potentiels.

Si le fichier d'entrée et les pseudo-potentiels sont dans le même répertoire, la commande suivante fait exécuter le programme en parallèle :

`srun cpmd.x <input files> > <output file>` (comme dans le script 1)

Si les pseudo-potentiels sont dans un répertoire différent, la commande est

`srun cpmd.x <input files> <path to pseudo potentials location> > <output file>` (comme dans le script 2)

```txt title="1-h2-wave.inp"
&INFO
isolated hydrogen molecule.
single point calculation.
&END

&CPMD
 OPTIMIZE WAVEFUNCTION
 CONVERGENCE ORBITALS
  1.0d-7
 CENTER MOLECULE ON
 PRINT FORCES ON
&END

&SYSTEM
 SYMMETRY
  1
 ANGSTROM
 CELL
  8.00 1.0 1.0  0.0  0.0  0.0
 CUTOFF
  70.0
&END

&DFT
 FUNCTIONAL LDA
&END

&ATOMS
*H_MT_LDA.psp
 LMAX=S
  2
 4.371   4.000   4.000
 3.629   4.000   4.000
&END
```

```bash title="run-cpmd.sh"
#!/bin/bash

#SBATCH --account=def-someacct
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=2500M
#SBATCH --time=0-1:00

# Load the modules:

module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3

echo "Starting run at: `date`"

CPMD_INPUT="1-h2-wave.inp"
CPMD_OUTPUT="1-h2-wave_output.txt"

srun cpmd.x ${CPMD_INPUT} > ${CPMD_OUTPUT}

echo "Program finished with exit code $? at: `date`"
```

```bash title="run-cpmd.sh"
#!/bin/bash

#SBATCH --account=def-someacct
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=2500M
#SBATCH --time=0-1:00

# Load the modules:

module load StdEnv/2020
module load intel/2020.1.217 openmpi/4.0.3 cpmd/4.3

echo "Starting run at: `date`"

CPMD_INPUT="1-h2-wave.inp"
CPMD_OUTPUT="1-h2-wave_output.txt"
PP_PATH=<path to the location of pseudo-potentials>

srun cpmd.x ${CPMD_INPUT} ${PP_PATH} > ${CPMD_OUTPUT}

echo "Program finished with exit code $? at: `date`"
```

## Référence

*   [site web](https://www.cpmd.org/wordpress/)