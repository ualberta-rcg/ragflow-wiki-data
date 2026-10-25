---
title: "GRRM/fr"
slug: "grrm"
lang: "fr"

source_wiki_title: "GRRM/fr"
source_hash: "b5fe7828a49356282a01b1ff45bc4f7c"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:53:54.956126+00:00"

tags:
  - software

keywords:
  - "g16"
  - "Global Reaction Route Mapping"
  - "installation script"
  - "formchk"
  - "Intel MPI"
  - "SLURM script"
  - "STLM_SERVER_ADDRESS"
  - "single node"
  - "floating license"
  - "Gaussian"
  - "GRRM23"
  - "unfchk"
  - "checkpoint"
  - "STLM_SERVER_PORT"

questions:
  - "What is the purpose of Global Reaction Route Mapping (GRRM23) and which quantum chemistry programs does it work with?"
  - "How can a user obtain a license for GRRM23, and what are the available options for setting up the floating license server?"
  - "What are the key steps required to install and configure GRRM23, including necessary environment variable settings?"
  - "How should the environment variables be configured and sourced to correctly initialize GRRM23?"
  - "What are the necessary Slurm script parameters and GRRM23 command‑line options for running a job on a single node?"
  - "Why does GRRM23 only support single‑node execution with Gaussian, and how can other programs like ORCA be used instead?"
  - "Which executables should be added to the <code>subgau</code>, <code>subchk</code> and <code>subunchk</code> lines, respectively?"
  - "What placeholders need to be replaced in <code>STLM_SERVER_ADDRESS</code> and <code>STLM_SERVER_PORT</code> for license validation?"
  - "Who provides the information required to replace the <code>XXX</code> values for the license?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le logiciel Global Reaction Route Mapping ([GRRM](https://global.hpc.co.jp/products/grrm23/)) est un logiciel commercial pour l'analyse des chemins de réaction chimique. Le programme est capable d'explorer de manière exhaustive la surface d'énergie potentielle d'un ensemble d'atomes, trouvant automatiquement les géométries moléculaires des réactifs, des états de transition et des produits. GRRM23 fonctionne de concert avec des logiciels de chimie quantique tels que [Gaussian 16](gaussian.md) et [ORCA](orca.md).

## Licence

Pour obtenir une licence et connaître les prix, soumettez une demande à [HPC SYSTEMS Inc.](https://global.hpc.co.jp/contact/) ou contactez [Kenshiro Kimura](mailto:ke-kimura@hpc.co.jp).

GRRM23 utilise une approche de licence flottante pour valider les utilisateurs; cela nécessite la mise en place d'un serveur de licences. À cette fin, HPC SYSTEMS Inc. permet aux utilisateurs de se connecter aux serveurs de licences de leur site au Japon sans frais supplémentaires. Alternativement, un serveur de licences peut être mis en place dans votre université au Canada. Pour plus d'informations sur l'une ou l'autre des options de serveur de licences, contactez le soutien technique de [HPC SYSTEMS Inc.](https://global.hpc.co.jp/contact/).

## Installation

Après avoir acheté une licence, les utilisateurs recevront un lien et des instructions pour télécharger un fichier compressé `tar.bz2`. Téléchargez le fichier et suivez les instructions ci-dessous.

Dans votre répertoire personnel, créez un répertoire pour l'installation et un autre pour les exécutables :

```bash
mkdir GRRM23_Installation
mkdir GRRM23_RUN
```

Déplacez le fichier GRRM23 compressé vers `$HOME/GRRM23_Installation` et extrayez-le à cet endroit :

```bash
cd GRRM23_Installation
tar xjf GRRM23.tar.bz2
```

Vérifiez que cela a créé un script d'installation (`install.sh`). Ensuite, depuis `$HOME/GRRM23_Installation`, exécutez le script comme suit :

```bash
./install.sh /home/user/GRRM23_RUN
```

L'installation vous affichera l'écran suivant :

```text
Installation configuration:
GRRMroot = /home/user/GRRM23_RUN
Intel MPI installation prefix = /home/user/GRRM23_RUN/mpi-rt
Are you sure to start installation? [Y/n]
```

Tapez « Y » et appuyez sur « Entrée » pour poursuivre l'installation. Une fois l'installation terminée, le message « GRRM INSTALLATION DONE » devrait apparaître :

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

Copiez les dernières lignes (de `source` jusqu'à la dernière ligne `export`) dans votre fichier `.bashrc` de votre répertoire personnel. Étant donné que G16 n'est pas chargé sur les nœuds de connexion de l'Alliance, vous devez ajouter manuellement `g16`, `formchk` et `unfchk` dans les lignes correspondantes ci-dessous (`subgau`, `subchk` et `subuchk`, respectivement). Pour valider votre licence, remplacez les valeurs `XXX` dans `STLM_SERVER_ADDRESS` et `STLM_SERVER_PORT` par les informations fournies par HPC SYSTEMS Inc. pour votre licence (HPC SYSTEMS Inc. enverra ces informations aux utilisateurs par courriel) :

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
source ~/.bashrc
```

Ensuite, tapez `GRRM23p` dans le terminal. Si l'installation a réussi, le texte suivant devrait apparaître :

```text
USAGE: GRRMp [input file name] (-p[Nproc]) (-h[Hour]) (-w/xxx/xxx) 
(-f[machine_file]) (-c[Ncore])
```

[Gaussian](gaussian.md) (G16) est déjà installé sur Fir et Nibi. Les nœuds de calcul sur les deux systèmes ont accès à Internet dans le but de contacter un serveur de licences.

## Utilisation

Pour des exemples d'entrée, veuillez consulter le [manuel de l'utilisateur de GRRM23](https://afir.sci.hokudai.ac.jp/manual/). Dans la plupart des cas, GRRM23 ne nécessite qu'un seul fichier d'entrée (`Job.com`) contenant les coordonnées cartésiennes d'une molécule et les options de méthodologie. Dans d'autres cas, GRRM23 nécessite la sortie d'une tâche GRRM23 précédente.

### Exemple de script Slurm pour un seul nœud

Pour un seul nœud (`--nodes=1`) et 12 cœurs (`--ntasks-per-node=12`), exécuté depuis votre répertoire `/scratch` :

```bash
#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
#SBATCH --mem-per-cpu=4000M

module load gaussian/g16.c01
export GAUSS_SCRDIR=/home/user/scratch/

GRRM23p Job -p1 -s80000
```

*   `-p1` : nombre de processus parallèles.
*   `-s80000` : indique quand (en secondes) créer un fichier de point de contrôle afin qu'une tâche interrompue puisse être redémarrée correctement. Notez que 80000 secondes équivalent à environ 22 heures. Ce temps doit être inférieur à la valeur `--time` que vous demandez à Slurm.

!!! warning "Nœuds multiples non supportés"
    En raison des licences Gaussian sur Fir et Nibi, GRRM23 ne peut être utilisé avec Gaussian que sur un seul nœud.

### Exemple d'utilisation avec ORCA

```bash
#!/bin/bash
#SBATCH --time=18:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem-per-cpu=4000M

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.0

GRRM23p glucose -p1 -h15
```

## Ressources externes

Manuels GRRM : [Manuels GRRM](https://afir.sci.hokudai.ac.jp/manual/)

## Remerciements

L'ébauche originale de cette page a été contribuée par Eduardo Romero Montalvo.