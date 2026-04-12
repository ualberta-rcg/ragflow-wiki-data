---
title: "Open Babel/fr"
slug: "open_babel"
lang: "fr"

source_wiki_title: "Open Babel/fr"
source_hash: "23c23914c5618833c509ca403154eb71"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:07:02.987239+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "Open Babel"
  - "parallélisation OpenMP"
  - "conversion de formats"
  - "interface Python"
  - "données chimiques"

questions:
  - "À quoi sert principalement la boîte à outils Open Babel selon le texte ?"
  - "Quelle est la différence d'utilisation entre les modules openbabel et openbabel-omp, et pourquoi ce dernier est-il déconseillé sur les nœuds de connexion ?"
  - "Comment un utilisateur peut-il accéder aux fonctionnalités d'Open Babel via le langage Python ?"
  - "À quoi sert principalement la boîte à outils Open Babel selon le texte ?"
  - "Quelle est la différence d'utilisation entre les modules openbabel et openbabel-omp, et pourquoi ce dernier est-il déconseillé sur les nœuds de connexion ?"
  - "Comment un utilisateur peut-il accéder aux fonctionnalités d'Open Babel via le langage Python ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

[Open Babel](https://openbabel.org/) est une boîte à outils conçue pour traiter les nombreux formats de données chimiques. Il s'agit d'un projet ouvert et collaboratif permettant à quiconque de rechercher, convertir, analyser ou stocker les données provenant de la modélisation moléculaire, de la chimie, des matériaux solides, de la biochimie ou de domaines connexes.

Consultez le [guide d'utilisateur d'Open Babel](https://openbabel.org/docs/).

Deux types de modules sont installés sur nos grappes :

## `openbabel`

Cette version séquentielle peut être utilisée en toute sécurité, même sur les nœuds de connexion, pour convertir les formats des fichiers de structure chimique. Dans la plupart des cas, c'est le bon module.

### Exemple

````bash
[user@login1]$ module load openbabel
[user@login1]$ wget "https://www.chemspider.com/FilesHandler.ashx?type=str&3d=yes&id=171" -O acetic_acid.mol
[user@login1]$ obabel -i mol acetic_acid.mol -o pdb -O acetic_acid.pdb
````

Remarques :

*   La commande `wget` télécharge le fichier `acetic_acid.mol`.
*   La commande `obabel` convertit la molécule décrite dans `acetic_acid.mol` du format `.mol` au format `.pdb`.

## `openbabel-omp`

Cette version offre la parallélisation avec OpenMP.

!!! warning
    **N'utilisez pas ce module sur les nœuds de connexion**, car même pour des tâches simples, il créera autant de fils (threads) qu'il détectera de CPU sur la machine, provoquant ainsi des pics de charge qui perturberont les autres utilisateurs.

La version parallèle est utile pour convertir un très grand nombre de structures moléculaires ou calculer un grand nombre de descripteurs chimio-informatiques pour plusieurs molécules.

Assurez-vous de définir la variable d'environnement `OMP_NUM_THREADS` afin d'indiquer à Open Babel combien de CPU il peut utiliser.

### Exemple

La tâche suivante utilise le [fichier SDF](https://en.wikipedia.org/wiki/Chemical_table_file#SDF) `many_molecules.sdf` qui devrait contenir une base de données de plusieurs molécules et génère des représentations canoniques [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) pour chacune d'elles, en utilisant deux cœurs CPU.

````sh title="parallel_openbabel_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1000M
module load openbabel-omp
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-1}"

obabel -i sdf many_molecules.sdf -o can -O many_canonical_smiles.txt
````

## Python

Les fonctionnalités d'Open Babel peuvent être utilisées à partir d'autres langages tels que Python. [L'interface Python pour Open Babel](https://openbabel.org/docs/UseTheLibrary/Python.html) est ajoutée aux modules `openbabel` et `openbabel-omp` en tant qu'extensions. Par conséquent, les paquets `openbabel` et `pybel` peuvent être utilisés après avoir chargé `openbabel` et un module Python compatible.

### Exemple

```bash
$ module load python/3.11 openbabel/3.1.1
$ python
Python 3.11.5 (main, Sep 19 2023, 19:49:15) [GCC 11.3.0] on linux
>>> import openbabel
>>> print(openbabel.__version__)
3.1.1.1
>>> from openbabel import pybel
>>>