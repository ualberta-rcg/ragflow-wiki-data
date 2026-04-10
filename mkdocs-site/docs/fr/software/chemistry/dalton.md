---
title: "Dalton/fr"
tags:
  []

keywords:
  []
---

= Introduction =

Le noyau de la suite logicielle Dalton2016 est constitué de deux puissantes applications pour l'étude des structures électroniques de molécules : Dalton et LSDalton. Ensemble, ces applications offrent des fonctionnalités étendues pour le calcul des propriétés moléculaires aux niveaux théoriques HF, DFT, MCSCF et CC. Plusieurs de ses propriétés sont uniques à la suite Dalton2016. 

* site web du projet : http://daltonprogram.org/
* documentation : http://daltonprogram.org/documentation/
* forum : http://forum.daltonprogram.org/

= Modules =

<source lang="bash">
$ module load nixpkgs/16.09 intel/2016.4 openmpi/2.0.2 dalton/2017-alpha
</source>

Remarquez que `dalton/2017-alpha` dépend d’une version OpenMPI autre que la version par défaut. Pour de l’information sur la commande module voyez [Utiliser des modules](utiliser-des-modules.md).

= Utilisation =

Voici un exemple ː

* fichier d'entrée : `dft_rspexci_nosym.dal` (voir les exemples ci-dessous)
* spécification de la molécule : `H2O_cc-pVDZ_nosym.mol` (voir les exemples ci-dessous)
* pour utiliser les bases atomiques, ajouter l'option `-b ${BASLIB}` en ligne de commande (voir les exemples ci-dessous)
* pour définir le nombre de processus avec une option en ligne de commande ou une variable d’environnement :
** ajoutez l’option `-N ${SLURM_NTASKS}` en ligne de commande pour le lanceur (voir Script 1 dans les exemples ci-dessous)
** ou  `export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}` (voir Script 2 dans les exemples ci-dessous).

Pour exécuter Dalton, chargez le module et utilisez le lanceur `dalton`.

<source lang="bash">
dalton -b ${BASLIB} -N ${SLURM_NTASKS}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol 
</source>

ou

<source lang="bash">
export DALTON_NUM_MPI_PROCS=${SLURM_NTASKS}
dalton -b ${BASLIB}  -dal dft_rspexci_nosym.dal  -mol H2O_cc-pVDZ_nosym.mol 
</source>

= Exemples ː scripts et fichiers d’entrée =

## Exemple 1 : dft_rspexci_nosym 
<tabs>

<tab name="INPUT">

**`dft_rspexci_nosym.dal`**
```txt
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

</tab>

<tab name="MOLECULE">

**`H2O_cc-pVDZ_nosym.mol`**
```txt
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

</tab>

<tab name="Script 1">
{{File
  |name=run_dalton_job.sh
  |lang="bash"
  |contents=
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
}}
</tab>

<tab name="Script 2">
{{File
  |name=run_dalton_job.sh
  |lang="bash"
  |contents=
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
}}
</tab>

</tabs>
## Exemple 2 : dft_rspexci_sym.dal 
<tabs>

<tab name="INPUT">

**`dft_rspexci_sym.dal`**
```txt
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

</tab>

<tab name="MOLECULE">

**`H2O_cc-pVDZ_sym.mol`**
```txt
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

</tab>

<tab name="Script 1">
{{File
  |name=run_dalton_job.sh
  |lang="bash"
  |contents=
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
}}
</tab>

<tab name="Script 2">
{{File
  |name=run_dalton_job.sh
  |lang="bash"
  |contents=
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
}}
</tab>

</tabs>