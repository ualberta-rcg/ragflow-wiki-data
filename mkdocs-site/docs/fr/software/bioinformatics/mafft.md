---
title: "MAFFT/fr"
slug: "mafft"
lang: "fr"

source_wiki_title: "MAFFT/fr"
source_hash: "5d10c9fa7d02fb0a497617c5c4659c90"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:35:12.619218+00:00"

tags:
  []

keywords:
  - "nœuds multiples (MPI)"
  - "alignement de séquences multiples"
  - "SLURM"
  - "MAFFT"
  - "nœud unique"

questions:
  - "Quel est le but principal du programme MAFFT et comment ses méthodes d'alignement s'adaptent-elles au nombre de séquences à traiter ?"
  - "Comment configurer et soumettre une tâche MAFFT sur un nœud unique en exploitant plusieurs cœurs via SLURM ?"
  - "Quelle contrainte particulière s'applique au répertoire temporaire lors de l'exécution de MAFFT sur des nœuds multiples avec MPI ?"
  - "Quel est le but principal du programme MAFFT et comment ses méthodes d'alignement s'adaptent-elles au nombre de séquences à traiter ?"
  - "Comment configurer et soumettre une tâche MAFFT sur un nœud unique en exploitant plusieurs cœurs via SLURM ?"
  - "Quelle contrainte particulière s'applique au répertoire temporaire lors de l'exécution de MAFFT sur des nœuds multiples avec MPI ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MAFFT](https://mafft.cbrc.jp/alignment/software/) est un programme d'alignement de séquences multiples pour des systèmes d'exploitation comme Unix. Il offre plusieurs méthodes d'alignement, incluant L-INS-i (précis, pour l'alignement de <∼200 séquences), FFT-NS-2 (rapide, pour l'alignement de <∼30,000 séquences), etc.

## Nœud unique
MAFFT profite de cœurs multiples sur des nœuds uniques; voir https://mafft.cbrc.jp/alignment/software/multithreading.html.

!!! note
    Au chargement du module, la variable d'environnement `MAFFT_TMPDIR` est fixée à `$SLURM_TMPDIR/maffttmp`.

```bash
# mafft_submit.sh
#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0

module load gcc/9.3.0 mafft

mafft --globalpair --thread $SLURM_CPUS_PER_TASK input > output
```

## Nœuds multiples (MPI)
MAFFT peut utiliser MPI pour aligner un grand nombre de séquences; voir https://mafft.cbrc.jp/alignment/software/mpi.html.

!!! note
    Au chargement du module, la variable d'environnement `MAFFT_TMPDIR` est fixée à `$SLURM_TMPDIR/maffttmp`. Si vous changez de répertoire temporaire, il devra être partagé par tous les hôtes.

```bash
# mafft_mpi_submit.sh
#!/bin/bash

#SBATCH --time=04:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=12G

module load gcc/9.3.0 mafft-mpi

srun mafft --mpi --large --globalpair --thread $SLURM_CPUS_PER_TASK input > output