---
title: "Dalton/fr"
slug: "dalton"
lang: "fr"

source_wiki_title: "Dalton/fr"
source_hash: "41d6b5dcaf1a9ea4693595b45bd1ba66"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:42:49.507666+00:00"

tags:
  []

keywords:
  - "daltoninput"
  - "variables"
  - "run_dalton_job.sh"
  - "DALTON_NUM_MPI_PROCS"
  - "Dalton"
  - "structures électroniques"
  - "SLURM"
  - "daltonmol"
  - "SLURM_NTASKS"
  - "LSDalton"
  - "propriétés moléculaires"
  - "dalton"
  - "suite logicielle"
  - "bash script"

questions:
  - "Quelles sont les principales applications et fonctionnalités offertes par la suite logicielle Dalton2016 ?"
  - "Quelle commande doit-on utiliser pour charger correctement le module Dalton et ses dépendances dans l'environnement ?"
  - "Comment spécifie-t-on les fichiers d'entrée, les bases atomiques et le nombre de processus MPI lors de l'exécution du lanceur Dalton ?"
  - "Quels modules spécifiques doivent être chargés dans les scripts bash pour exécuter le programme Dalton sur la grappe de calcul ?"
  - "Quelles sont les deux méthodes distinctes présentées dans les scripts pour définir le nombre de processus MPI alloués à l'exécution de Dalton ?"
  - "Quelles informations et paramètres sont configurés dans les fichiers d'entrée (.dal) et de molécule (.mol) fournis dans l'Exemple 2 ?"
  - "What are the names of the input and molecule files defined in the script's variables?"
  - "How does the script utilize the SLURM workload manager to determine the number of tasks for the job?"
  - "What specific command-line flags and arguments are passed to the Dalton launcher during execution?"
  - "Quels modules spécifiques doivent être chargés dans les scripts bash pour exécuter le programme Dalton sur la grappe de calcul ?"
  - "Quelles sont les deux méthodes distinctes présentées dans les scripts pour définir le nombre de processus MPI alloués à l'exécution de Dalton ?"
  - "Quelles informations et paramètres sont configurés dans les fichiers d'entrée (.dal) et de molécule (.mol) fournis dans l'Exemple 2 ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Le noyau de la suite logicielle Dalton2016 est constitué de deux puissantes applications pour l'étude des structures électroniques de molécules : Dalton et LSDalton. Ensemble, ces applications offrent des fonctionnalités étendues pour le calcul des propriétés moléculaires aux niveaux théoriques HF, DFT, MCSCF et CC. Plusieurs de ses propriétés sont uniques à la suite Dalton2016.

*   [site web du projet](http://daltonprogram.org/)
*   [documentation](http://daltonprogram.org/documentation/)
*   [forum](http://forum.daltonprogram.org/)

## Modules

```bash
$ module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha
```

!!! note
    Remarquez que `dalton/2017-alpha` dépend d’une version OpenMPI autre que la version par défaut. Pour de l’information sur la commande `module`, voyez [Utiliser des modules](../../programming/utiliser_des_modules.md).

## Utilisation

Voici un exemple :

*   fichier d'entrée : `dft_rspexci_nosym.dal` (voir les exemples ci-dessous)
*   spécification de la molécule : `H2O_cc-pVDZ_nosym.mol` (voir les exemples ci-dessous)
*   pour utiliser les bases atomiques, ajouter l'option `-b ${BASLIB}` en ligne de commande (voir les exemples ci-dessous)
*   pour définir le nombre de processus avec une option en ligne de commande ou une variable d’environnement :
    *   ajoutez l’option `-N ${SLURM_NTASKS}` en ligne de commande pour le lanceur (voir Script 1 dans les exemples ci-dessous)
    *   ou `export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}` (voir Script 2 dans les exemples ci-dessous).

Pour exécuter Dalton, chargez le module et utilisez le lanceur `dalton`.

```bash
dalton -b ${BASLIB} -N ${SLURM_NTASKS}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol
```

ou

```bash
export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}
dalton -b ${BASLIB}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol
```

## Exemples : scripts et fichiers d’entrée

### Exemple 1 : dft_rspexci_nosym

```txt title="dft_rspexci_nosym.dal"
**DALTON INPUT
.RUN RESPONSE
**INTEGRALS
.PROPRINT
**WAVE FUNCTIONS
.DFT
 B3LYP
**RESPONSE
*LINEAR
.SINGLE RESIDUE
.ROOTS
 3
**END OF DALTON INPUT
```

```txt title="H2O_cc-pVDZ_nosym.mol"
BASIS
cc-pVDZ
H2O

    2    0
        8.    1
O     0.0  0.0000000000 0.0
        1.    2
H1    1.430    0.0  1.1
H2   -1.430    0.0  1.1
```

```bash title="run_dalton_job.sh (Script 1)"
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=3500M
#SBATCH --time=00-30:00

# Load the module: 

module load nixpkgs/16.09  intel/2016.4  openmpi/2.0.2 dalton/2017-alpha

# Setting the variables:

dltonlaun=dalton
dltonexec=dalton.x
daltoninput=dft_rspexci_nosym.dal
daltonmol=H2O_cc-pVDZ_nosym.mol

echo "Starting run at: `date`"

echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

${dltonlaun} -b ${BASLIB} -N ${SLURM_NTASKS}  -dal ${daltoninput}  -mol ${daltonmol}

echo "Program finished with exit code $? at: `date`"
```

```bash title="run_dalton_job.sh (Script 2)"
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --mem-per-cpu=3500M
#SBATCH --time=00-30:00

# Load the module: 

module load nixpkgs/16.09  intel/2016.4  openmpi/2.0.2 dalton/2017-alpha

# Setting the variables:

dltonlaun=dalton
dltonexec=dalton.x
daltoninput=dft_rspexci_nosym.dal
daltonmol=H2O_cc-pVDZ_nosym.mol

# Set the number of cores DALTON_NUM_MPI_PROCS to ${SLURM_NTASKS}

export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}

echo "Starting run at: `date`"

echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

${dltonlaun} -b ${BASLIB}  -dal ${daltoninput}  -mol ${daltonmol}

echo "Program finished with exit code $? at: `date`"
```

### Exemple 2 : dft_rspexci_sym.dal

```txt title="dft_rspexci_sym.dal"
**DALTON INPUT
.RUN RESPONSE
**INTEGRALS
.PROPRINT
**WAVE FUNCTIONS
.DFT
 B3LYP
**RESPONSE
*LINEAR
.SINGLE RESIDUE
**END OF DALTON INPUT
```

```txt title="H2O_cc-pVDZ_sym.mol"
BASIS
cc-pVDZ
H2O

    2
        8.    1
O     0.0  0.0000000000 0.0
        1.    2
H1    1.430    0.0  1.1
H2   -1.430    0.0  1.1
```

```bash title="run_dalton_job.sh (Script 1)"
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=3500M
#SBATCH --time=00-30:00

# Load the module: 

module load nixpkgs/16.09  intel/2016.4  openmpi/2.0.2 dalton/2017-alpha

# Setting the variables:

dltonlaun=dalton
dltonexec=dalton.x
daltoninput=dft_rspexci_sym.dal
daltonmol=H2O_cc-pVDZ_sym.mol

echo "Starting run at: `date`"

echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

${dltonlaun} -b ${BASLIB} -N ${SLURM_NTASKS}  -dal ${daltoninput}  -mol ${daltonmol}

echo "Program finished with exit code $? at: `date`"
```

```bash title="run_dalton_job.sh (Script 2)"
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=3500M
#SBATCH --time=00-30:00

# Load the module:

module load nixpkgs/16.09  intel/2016.4  openmpi/2.0.2 dalton/2017-alpha

# Setting the variables:

dltonlaun=dalton
dltonexec=dalton.x
daltoninput=dft_rspexci_sym.dal
daltonmol=H2O_cc-pVDZ_sym.mol

# Set the number of cores DALTON_NUM_MPI_PROCS to ${SLURM_NTASKS}

export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}

echo "Starting run at: `date`"

echo "Running the example: INPUT=${daltoninput} - Molecule=${daltonmol}"

${dltonlaun} -b ${BASLIB}  -dal ${daltoninput}  -mol ${daltonmol}

echo "Program finished with exit code $? at: `date`"