---
title: "Dalton/fr"
slug: "dalton"
lang: "fr"

source_wiki_title: "Dalton/fr"
source_hash: "41d6b5dcaf1a9ea4693595b45bd1ba66"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:57:39.183731+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Introduction

Le cœur de la suite logicielle Dalton2016 est composé de deux applications puissantes pour l'étude des structures électroniques de molécules : Dalton et LSDalton. Ensemble, ces applications offrent des fonctionnalités étendues pour le calcul des propriétés moléculaires aux niveaux théoriques HF, DFT, MCSCF et CC. Plusieurs de ses propriétés sont uniques à la suite Dalton2016.

*   [site web du projet](http://daltonprogram.org/)
*   [documentation](http://daltonprogram.org/documentation/)
*   [forum](http://forum.daltonprogram.org/)

# Modules

```bash
$ module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha
```

Notez que `dalton/2017-alpha` dépend d’une version d'OpenMPI différente de celle par défaut. Pour plus d’information sur la commande `module`, consultez [Utiliser des modules](utiliser-des-modules.md).

# Utilisation

Voici un exemple :

*   Fichier d'entrée : `dft_rspexci_nosym.dal` (voir les exemples ci-dessous)
*   Spécification de la molécule : `H2O_cc-pVDZ_nosym.mol` (voir les exemples ci-dessous)
*   Pour utiliser les bases atomiques, ajoutez l'option `-b ${BASLIB}` sur la ligne de commande (voir les exemples ci-dessous).
*   Pour définir le nombre de processus avec une option sur la ligne de commande ou une variable d’environnement :
    *   Ajoutez l’option `-N ${SLURM_NTASKS}` sur la ligne de commande pour le lanceur (voir Script 1 dans les exemples ci-dessous).
    *   Ou `export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}` (voir Script 2 dans les exemples ci-dessous).

Pour exécuter Dalton, chargez le module et utilisez le lanceur `dalton`.

```bash
dalton -b ${BASLIB} -N ${SLURM_NTASKS}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol
```

ou

```bash
export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}
dalton -b ${BASLIB}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol
```

# Exemples : Scripts et fichiers d’entrée

## Exemple 1 : dft_rspexci_nosym

=== "INPUT"
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

=== "MOLECULE"
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

=== "Script 1"
    ```bash title="run_dalton_job.sh"
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

=== "Script 2"
    ```bash title="run_dalton_job.sh"
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

## Exemple 2 : dft_rspexci_sym.dal

=== "INPUT"
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

=== "MOLECULE"
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

=== "Script 1"
    ```bash title="run_dalton_job.sh"
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

=== "Script 2"
    ```bash title="run_dalton_job.sh"
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