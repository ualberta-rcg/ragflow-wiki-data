---
title: "Open Babel/fr"
tags:
  - software
  - computationalchemistry

keywords:
  []
---

## Description 
[Open Babel](https://openbabel.org/) est une boîte à outils conçue pour parler les nombreux langages des données chimiques. Il s'agit d'un projet ouvert et collaboratif permettant à quiconque de rechercher, convertir, analyser ou stocker les données provenant de la modélisation moléculaire, de la chimie, des matériaux solides, de la biochimie ou de domaines connexes.

Consultez le [Open Babel User Guide](https://openbabel.org/docs/).

Deux types de modules sont installés sur nos grappes&nbsp;:

## `openbabel` 
Cette version séquentielle peut être utilisée en toute sécurité même sur les nœuds de connexion pour convertir les formats des fichiers de structure chimique. Dans la plupart des cas, c'est le bon module.

#### Exemple 

```bash

```
str&3dyes&id171" -O acetic_acid.mol
| obabel  -i mol  acetic_acid.mol  -o pdb  -O acetic_acid.pdb
}}
Remarques :
* La commande `wget` télécharge le fichier `acetic_acid.mol`.
* La commande `obabel` convertit la molécule décrite dans `acetic_acid.mol` du format `.mol` au format `.pdb`.

## `openbabel-omp` 
Cette version offre la parallélisation avec OpenMP.

La version parallèle est utile pour convertir un très grand nombre de structures moléculaires ou calculer un grand nombre de descripteurs chimio-informatiques pour plusieurs molécules.

Assurez-vous de définir la variable d'environnement `OMP_NUM_THREADS` afin d'indiquer à Open Babel combien de CPU il peut utiliser.

#### Exemple 
La prochaine tâche utilise le [fichier SDF](https://en.wikipedia.org/wiki/Chemical_table_file#SDF)   `many_molecules.sdf` qui devrait contenir une base de données de plusieurs  molécules et génère des représentations canoniques [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) pour chacune d'elles, en utilisant deux cœurs CPU.
{{File
  |name=parallel_openbabel_job.sh
  |lang="sh"
  |contents=
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1000M
module load openbabel-omp
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

obabel  -i sdf  many_molecules.sdf  -o can  -O many_canonical_smiles.txt
}}

## Python 
Les fonctionnalités d'Open Babel peuvent être utilisées à partir d'autres langages tels que Python. [L'interface Python pour Open Babel](https://openbabel.org/docs/UseTheLibrary/Python.html) est ajoutée aux modules `openbabel` eg `openbabel-omp`  en tant qu'extensions. Par conséquent, les paquets `openbabel` et `pybel` peuvent être utilisés après avoir chargé `openbabel` et un module Python compatible.

#### Exemple 

 $ module load python/3.11 openbabel/3.1.1
 $ python
 Python 3.11.5 (main, Sep 19 2023, 19:49:15) [GCC 11.3.0] on linux
 >>> import openbabel
 >>> print(openbabel.__version__)
 3.1.1.1
 >>> from openbabel import pybel
 >>>