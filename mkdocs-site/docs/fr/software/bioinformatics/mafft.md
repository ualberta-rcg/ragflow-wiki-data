---
title: "MAFFT/fr"
slug: "mafft"
lang: "fr"

source_wiki_title: "MAFFT/fr"
source_hash: "5d10c9fa7d02fb0a497617c5c4659c90"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:59:10.737725+00:00"

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

[MAFFT](https://mafft.cbrc.jp/alignment/software/) est un programme d'alignement de séquences multiples pour des systèmes d'exploitation comme Unix. Il offre plusieurs méthodes d'alignement dont G-INS-i (précis, pour l'alignement de <∼200 séquences), FFT-NS-2 (rapide, pour l'alignement de <∼30,000 séquences), etc.

## Nœud unique
MAFFT tire profit des cœurs multiples sur des nœuds uniques; consultez [https://mafft.cbrc.jp/alignment/software/multithreading.html](https://mafft.cbrc.jp/alignment/software/multithreading.html) pour plus de détails.

!!! note "Note"
    Au chargement du module, la variable d'environnement `MAFFT_TMPDIR` est fixée à `$SLURM_TMPDIR/maffttmp`.

```bash title="mafft_submit.sh"
#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0

module load gcc/9.3.0 mafft

mafft --globalpair --thread $SLURM_CPUS_PER_TASK input > output
```

## Nœuds multiples (MPI)
MAFFT peut utiliser MPI pour aligner un grand nombre de séquences; consultez [https://mafft.cbrc.jp/alignment/software/mpi.html](https://mafft.cbrc.jp/alignment/software/mpi.html) pour plus de détails.

!!! note "Note"
    Au chargement du module, la variable d'environnement `MAFFT_TMPDIR` est fixée à `$SLURM_TMPDIR/maffttmp`. Si vous changez de répertoire temporaire, il devra être partagé par tous les hôtes.

```bash title="mafft_mpi_submit.sh"
#!/bin/bash

#SBATCH --time=04:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=12G

module load gcc/9.3.0 mafft-mpi

srun mafft --mpi --large --globalpair --thread $SLURM_CPUS_PER_TASK input > output