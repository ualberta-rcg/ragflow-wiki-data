---
title: "GRRM/fr"
slug: "grrm"
lang: "fr"

source_wiki_title: "GRRM/fr"
source_hash: "04378790e7838ca8d0d0844ec827079d"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:33:38.295711+00:00"

tags:
  - software

keywords:
  - ".bashrc"
  - "GRRM23"
  - "SLURM script"
  - "environment variables"
  - "checkpoint file"
  - "STLM_SERVER_ADDRESS"
  - "HPC SYSTEMS Inc."
  - "global reaction route mapping"
  - "floating license"
  - "install.sh"
  - "Gaussian/G16"
  - "formchk"
  - "Intel MPI"
  - "G16"

questions:
  - "What is the global reaction route mapping (GRRM23) program used for and which quantum chemistry packages can it work with?"
  - "How can a user obtain a GRRM23 license, and what are the options for setting up the required floating license server?"
  - "What are the essential steps and environment variable configurations needed to install and run GRRM23 on a Linux system?"
  - "What environment variables must be exported and sourced before running GRRM23, and what are their purposes?"
  - "How should a Slurm script be written to run a GRRM23 job on a single node, and what do the options “-p” and “-s” control?"
  - "Why is GRRM23 limited to a single node when using Gaussian 16, and where can users find the official GRRM documentation?"
  - "What specific lines must be added or edited in your .bashrc to include the g16, formchk, and unfchk executables (referred to as subgau, subchk, and subunchk)?"
  - "How should the placeholder values “XXX” be replaced in the STLM_SERVER_ADDRESS and STLM_SERVER_PORT variables, and where can you obtain the correct information?"
  - "Why is it necessary to manually add these commands to the .bashrc on the Alliance login nodes, and what role does the license validation play in this process?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le programme de cartographie globale des routes de réaction ([GRRM®](https://global.hpc.co.jp/products/grrm23/)) est un logiciel commercial développé pour l'analyse des chemins de réaction chimique; ce programme est capable d'explorer de manière exhaustive la surface d'énergie potentielle d'un ensemble d'atomes, trouvant automatiquement les géométries moléculaires des réactifs, des états de transition et des produits. GRRM23 fonctionne en conjonction avec des logiciels de chimie quantique tels que, mais sans s'y limiter, Gaussian 16.

## Entente de licence

Pour obtenir une licence (et les prix), veuillez soumettre une demande à l'adresse suivante : [https://global.hpc.co.jp/contact/](https://global.hpc.co.jp/contact/). Vous pouvez également contacter [Kenshiro Kimura](mailto:ke-kimura@hpc.co.jp) pour obtenir des instructions sur la demande de GRRM23. GRRM23 utilise une approche de licence flottante pour valider les utilisateurs; cela nécessite la mise en place d'un serveur de licences. À cette fin, HPC SYSTEMS Inc., la société qui vend GRRM23, permet aux utilisateurs de se connecter aux serveurs de licences situés sur leur site au Japon, sans frais supplémentaires. Alternativement, un serveur de licences peut être mis en place à l'université de l'utilisateur au Canada; pour cette option, veuillez contacter le support technique de HPC SYSTEMS Inc.

## Instructions d'installation

Après avoir acheté une licence, les utilisateurs recevront un lien et des instructions pour télécharger un fichier compressé `tar.bz2`. Téléchargez le fichier et suivez les instructions ci-dessous (substituez le chemin vers votre répertoire personnel réel là où `/home/user` est mentionné).

Dans votre répertoire personnel, créez un répertoire pour l'installation et un autre pour les exécutables :

```bash
mkdir GRRM23_Installation
mkdir GRRM23_RUN
```

Déplacez le fichier compressé GRRM23 vers `$HOME/GRRM23_Installation` et extrayez-le à cet endroit :

```bash
cd GRRM23_Installation
tar xjf GRRM23.tar.bz2
```

L'extraction du `tar.bz2` devrait générer un script d'installation (`install.sh`); depuis `/home/user/GRRM23_Installation`, exécutez le script comme suit :

```bash
./install.sh /home/user/GRRM23_RUN
```

L'installation vous présentera l'écran suivant :

```
Installation configuration:
GRRMroot = /home/user/GRRM23_RUN
Intel MPI installation prefix = /home/user/GRRM23_RUN/mpi-rt
Are you sure to start installation? [Y/n]
```

Tapez « Y » et appuyez sur « Entrée » pour poursuivre l'installation. Une fois l'installation terminée, un message « GRRM INSTALLATION DONE » devrait apparaître :

```
Installing Intel MPI ... done successfully.
Installing GRRM binary ...done successfully.
Installing STLib ...done successfully.

GRRM INSTALLATION DONE.
IMPORTANT[1]: Before using GRRM, please insert lines below to your shell (/bin/bash) configuration file.
IMPORTANT[2]: Please consult your system administrator about the STLM server IP address and port number.

source /home/user/GRRM23_RUN/mpi-rt/mpi/2021.6.0/env/vars.sh
export PATH="/home/user/GRRM23_RUN:${PATH}"
export LD_LIBRARY_PATH="/home/user/GRRM23_RUN:${LD_LIBRARY_PATH}"
export GRRMroot="/home/user/GRRM23_RUN"
export subgrr="GRRM23.out"
export subgau=""
export subchk=""
export subuchk=""
export submol=""
export subsiesta=""
export submpi="mpirun"
export I_MPI_FABRICS="shm:tcp"
export I_MPI_FALLBACK=0
export I_MPI_HYDRA_BOOTSTRAP="ssh"
export STLM_SERVER_ADDRESS="XXX.XXX.XXX.XXX"
export STLM_SERVER_PORT=XXXXX
```

Copiez les dernières lignes (de « `source` » à la dernière ligne « `export` ») dans votre fichier `.bashrc` situé dans votre répertoire personnel. Étant donné que `G16` n'est pas chargé sur les nœuds de connexion de l'Alliance, vous devez ajouter manuellement `g16`, `formchk` et `unfchk` aux lignes correspondantes ci-dessous (`subgau`, `subchk` et `subunchk`, respectivement). Pour valider votre licence, veuillez remplacer les valeurs `XXX` pour `STLM_SERVER_ADDRESS` et `STLM_SERVER_PORT` par les informations fournies par HPC SYSTEMS Inc. pour votre licence (HPC SYSTEMS Inc. enverra ces informations aux utilisateurs par courriel) :

```bash
source /home/user/GRRM23_RUN/mpi-rt/mpi/2021.6.0/env/vars.sh
export PATH="/home/user/GRRM23_RUN:${PATH}"
export LD_LIBRARY_PATH="/home/user/GRRM23_RUN:${LD_LIBRARY_PATH}"
export GRRMroot="/home/user/GRRM23_RUN"
export subgrr="GRRM23.out"
export subgau="g16"
export subchk="formchk"
export subuchk="unfchk"
export submol=""
export subsiesta=""
export submpi="mpirun"
export I_MPI_FABRICS="shm:tcp"
export I_MPI_FALLBACK=0
export I_MPI_HYDRA_BOOTSTRAP="ssh"
export STLM_SERVER_ADDRESS="XXX.XXX.XXX.XXX"
export STLM_SERVER_PORT=XXXXX
```

Sourcez votre fichier `.bashrc` et déconnectez-vous :

```bash
source /home/user/.bashrc
exit
```

Après vous être connecté, tapez `GRRM23p` dans le terminal. Si l'installation a réussi, le texte suivant devrait apparaître :

```
USAGE: GRRMp [input file name] (-p[Nproc]) (-h[Hour]) (-w/xxx/xxx) 
(-f[machine_file]) (-c[Ncore])
```

Les systèmes Fir et Nibi ont `G16` installé pour leurs utilisateurs. Les nœuds de calcul sur les deux systèmes peuvent se connecter à Internet pour se connecter à tout serveur de licences requis.

## Exécution de GRRM

Pour des exemples de fichiers d'entrée, veuillez vous référer au manuel de l'utilisateur de GRRM23. Généralement, GRRM23 ne nécessite qu'un seul fichier d'entrée (`Job.com`) contenant les coordonnées cartésiennes d'une molécule ainsi que les options de méthodologie; dans certains cas, GRRM23 nécessitera le fichier de sortie d'une tâche GRRM23 précédente.

### Exemple de script Slurm pour un nœud unique

Pour un nœud unique (`-N 1`) et 12 cœurs (`-n 12`), exécuté depuis le répertoire `/scratch` de l'utilisateur :

```bash
#!/bin/bash
#SBATCH -t 1-00:00
#SBATCH -J Job_SLURM
#SBATCH -o Job.SLURMout
#SBATCH -e Job.SLURMerr
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=Job

cd /home/user/scratch/

module load gaussian/g16.c01
export GAUSS_SCRDIR=/home/user/scratch/

GRRM23p ${input} -p1 -s80000
```

- `-p1` : nombre de processus parallèles;
- `-s80000` : indique quand créer un fichier de *checkpoint* (en secondes); vous devez spécifier à GRRM23 quand créer ces fichiers de *checkpoint* afin qu'une tâche interrompue ou tuée puisse être redémarrée correctement.

### Exemple avec ORCA

```bash
#!/bin/bash
#SBATCH -t 0-18:00
#SBATCH -J glucose_SLURM
#SBATCH -o glucose.SLURMout
#SBATCH -e glucose.SLURMerr
#SBATCH -N 1
#SBATCH -n 16
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=glucose

cd /home/user/scratch/Pyrolysis_of_Models/glucose

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.0

GRRM23p ${input} -p1 -h15
```

### Exemple de script Slurm pour plusieurs nœuds

Actuellement, étant donné que nous utilisons principalement GRRM23 avec G16, nous ne pouvons utiliser qu'un seul nœud, conformément aux politiques de licence de Gaussian16.

## Ressources externes

Manuels d'utilisateur de GRRM : [https://afir.sci.hokudai.ac.jp/manual/](https://afir.sci.hokudai.ac.jp/manual/)

## Remerciements

Cette documentation a été contribuée par Eduardo Romero Montalvo.