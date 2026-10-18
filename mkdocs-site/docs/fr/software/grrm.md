---
title: "GRRM/fr"
slug: "grrm"
lang: "fr"

source_wiki_title: "GRRM/fr"
source_hash: "e6ed71052d376fc973c0a15ddcc16ec8"
last_synced: "2026-10-18T00:43:06.821597+00:00"
last_processed: "2026-10-18T01:36:08.349738+00:00"

tags:
  - software

keywords:
  - "G16"
  - "subgau"
  - "Intel MPI"
  - ".bashrc"
  - "Slurm script"
  - "GRRM23 installation"
  - "environment variables"
  - "single node limitation"
  - "HPC SYSTEMS Inc."
  - "GRRM23"
  - "global reaction route mapping"
  - "installation script"
  - "Gaussian license"
  - "floating license"
  - "STLM_SERVER_ADDRESS"

questions:
  - "What is Global Reaction Route Mapping (GRRM23) and which quantum chemistry software does it integrate with?"
  - "How can a user obtain a license for GRRM23, and what are the options for setting up a license server?"
  - "What are the main steps and required environment variable configurations for installing and running GRRM23 on a Linux system?"
  - "What environment variables must be set for GRRM23, and how should they be exported in the user’s environment?"
  - "How should a GRRM23 job be submitted on a Slurm cluster, including the required script directives and command‑line options?"
  - "Why is GRRM23 restricted to a single node when using Gaussian, and what alternative quantum‑chemistry program is demonstrated for multi‑core use?"
  - "Which commands should be added to your `.bashrc` and under which alias names (subgau, subchk, subunchk) should they be placed?"
  - "Why is it necessary to manually add `g16`, `formchk`, and `unfchk` on the Alliance login nodes?"
  - "What specific values need to replace the `XXX` placeholders in `STLM_SERVER_ADDRESS` and `STLM_SERVER_PORT` to validate your license?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le logiciel Global Reaction Route Mapping ([GRRM](https://global.hpc.co.jp/products/grrm23/)) est un logiciel commercial pour l'analyse des chemins de réactions chimiques. Le programme est capable d'explorer de manière exhaustive la surface d'énergie potentielle d'un ensemble d'atomes, trouvant automatiquement les géométries moléculaires des réactifs, des états de transition et des produits. GRRM23 fonctionne de concert avec des logiciels de chimie quantique tels que [Gaussian 16](gaussian.md) et [ORCA](orca.md).

## Licence

Pour obtenir une licence et des informations sur les prix, soumettez une demande à [HPC SYSTEMS Inc.](https://global.hpc.co.jp/contact/) ou contactez [Kenshiro Kimura](mailto:ke-kimura@hpc.co.jp).

GRRM23 utilise une approche de licence flottante pour valider les utilisateurs; cela nécessite la mise en place d'un serveur de licences. Pour cela, HPC SYSTEMS Inc. permet aux utilisateurs de se connecter à des serveurs de licences situés dans leur entreprise au Japon, sans frais supplémentaires. Alternativement, un serveur de licences peut être mis en place à l'université de l'utilisateur au Canada. Pour plus d'informations sur l'une ou l'autre des options de serveur de licences, contactez le soutien technique de [HPC SYSTEMS Inc.](https://global.hpc.co.jp/contact/).

## Installation

Après l'achat d'une licence, les utilisateurs recevront un lien et des instructions pour télécharger un fichier compressé tar.bz2. Téléchargez le fichier et suivez les instructions ci-dessous. Remplacez le chemin de votre répertoire personnel là où `/home/user` est mentionné.

Dans votre répertoire personnel, créez un répertoire pour l'installation et un autre pour les exécutables :

```bash
mkdir GRRM23_Installation
mkdir GRRM23_RUN
```

Déplacez le fichier compressé GRRM23 vers `$HOME/GRRM23_Installation` et extrayez-le là :

```bash
cd GRRM23_Installation
tar xjf GRRM23.tar.bz2
```

Vérifiez que cela a créé un script d'installation (`install.sh`). Ensuite, depuis `/home/user/GRRM23_Installation`, exécutez le script comme suit :

```bash
./install.sh /home/user/GRRM23_RUN
```

L'installation vous demandera de confirmer la configuration suivante :

```text
Installation configuration:
GRRMroot = /home/user/GRRM23_RUN
Intel MPI installation prefix = /home/user/GRRM23_RUN/mpi-rt
Are you sure to start installation? [Y/n]
```

Tapez « Y » et appuyez sur « Enter » pour poursuivre l'installation. Une fois l'installation terminée, un message « GRRM INSTALLATION DONE » devrait apparaître :

```text
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

Copiez les dernières lignes (de « source » jusqu'à la dernière ligne « export ») dans votre fichier `.bashrc` de votre répertoire personnel. Puisque G16 n'est pas chargé sur les nœuds de connexion de l'Alliance, vous devez ajouter manuellement `g16`, `formchk` et `unfchk` dans les lignes correspondantes ci-dessous (`subgau`, `subchk` et `subuchk`, respectivement). Pour valider votre licence, remplacez les valeurs `XXX` de `STLM_SERVER_ADDRESS` et `STLM_SERVER_PORT` par les informations fournies par HPC SYSTEMS Inc. pour votre licence (HPC SYSTEMS Inc. enverra ces informations aux utilisateurs par courriel) :

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

Déconnectez-vous et reconnectez-vous, ou sourcez votre fichier `.bashrc` :

```bash
source /home/user/.bashrc
```

Ensuite, tapez `GRRM23p` dans le terminal. Si l'installation a réussi, le texte suivant devrait apparaître :

```text
USAGE: GRRMp [input file name] (-p[Nproc]) (-h[Hour]) (-w/xxx/xxx)
(-f[machine_file]) (-c[Ncore])
```

[Gaussian](gaussian.md) (G16) est déjà installé sur Fir et Nibi. Les nœuds de calcul sur les deux systèmes ont accès à Internet afin de contacter un serveur de licences.

## Utilisation

Pour des exemples de fichiers d'entrée, veuillez vous référer au [manuel de l'utilisateur de GRRM23](https://afir.sci.hokudai.ac.jp/manual/). Dans la plupart des cas, GRRM23 ne nécessite qu'un seul fichier d'entrée (`Job.com`) contenant les coordonnées cartésiennes d'une molécule et les options de méthodologie. Dans certains autres cas, GRRM23 nécessite la sortie d'une tâche GRRM23 précédente.

### Exemple de script Slurm pour un nœud unique

Pour un nœud unique (`--nodes=1`) et 12 cœurs (`--ntasks-per-node=12`), s'exécutant à partir du répertoire `/scratch` de l'utilisateur :

```bash
#!/bin/bash
#SBATCH --time=1-00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=Job

cd /home/user/scratch/

module load gaussian/g16.c01
export GAUSS_SCRDIR=/home/user/scratch/

GRRM23p ${input} -p1 -s80000
```

*   `-p1` : nombre de processus parallèles.
*   `-s80000` : indique quand (en secondes) créer un fichier de point de contrôle afin qu'une tâche interrompue puisse être redémarrée correctement. Notez que 80000 secondes équivalent à environ 22 heures. Ce temps doit être inférieur au `--time` que vous demandez à Slurm.

!!! warning "Nœuds multiples non pris en charge"
    En raison des licences Gaussian sur Fir et Nibi, GRRM23 ne peut être utilisé avec Gaussian que sur un seul nœud.

### Exemple avec ORCA

```bash
#!/bin/bash
#SBATCH --time=0-18:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=glucose

cd /home/user/scratch/Pyrolysis_of_Models/glucose

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.0

GRRM23p ${input} -p1 -h15
```

## Ressources externes

Manuels GRRM : [https://afir.sci.hokudai.ac.jp/manual/](https://afir.sci.hokudai.ac.jp/manual/)

## Remerciements

L'ébauche originale de cette page a été rédigée par Eduardo Romero Montalvo.