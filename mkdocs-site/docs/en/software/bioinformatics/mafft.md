---
title: "MAFFT/en"
slug: "mafft"
lang: "en"

source_wiki_title: "MAFFT/en"
source_hash: "cbd2c843325925ba8238988fd8c46edc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:34:59.888755+00:00"

tags:
  []

keywords:
  - "multiple nodes"
  - "single node"
  - "MAFFT"
  - "MPI"
  - "multiple sequence alignment"

questions:
  - "What is MAFFT and how do its specific alignment methods, such as L-INS-i and FFT-NS-2, differ based on the number of sequences?"
  - "How can a user configure a SLURM script to utilize multithreading for running MAFFT on a single node?"
  - "What are the specific module, SLURM, and temporary directory requirements for executing MAFFT across multiple nodes using MPI?"
  - "What is MAFFT and how do its specific alignment methods, such as L-INS-i and FFT-NS-2, differ based on the number of sequences?"
  - "How can a user configure a SLURM script to utilize multithreading for running MAFFT on a single node?"
  - "What are the specific module, SLURM, and temporary directory requirements for executing MAFFT across multiple nodes using MPI?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MAFFT](https://mafft.cbrc.jp/alignment/software/) is a multiple sequence alignment program for unix-like operating systems. It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment of <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.

## Single node
MAFFT can benefit from multiple cores on a single node. For more information: [https://mafft.cbrc.jp/alignment/software/multithreading.html](https://mafft.cbrc.jp/alignment/software/multithreading.html)

!!! note
    The `MAFFT_TMPDIR` is set to `$SLURM_TMPDIR/maffttmp` when you load the module.

```bash title="mafft_submit.sh"
#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0

module load gcc/9.3.0 mafft

mafft --globalpair --thread $SLURM_CPUS_PER_TASK input > output
```

## Multiple nodes (MPI)
MAFFT can use MPI to align a large number of sequences: [https://mafft.cbrc.jp/alignment/software/mpi.html](https://mafft.cbrc.jp/alignment/software/mpi.html)

!!! note
    `MAFFT_TMPDIR` is set to `$SCRATCH/maffttmp` when you load the module. If you change this temporary directory, it must be shared by all hosts.

```bash title="mafft_mpi_submit.sh"
#!/bin/bash

#SBATCH --time=04:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=12G

module load gcc/9.3.0 mafft-mpi

srun mafft --mpi --large --globalpair --thread $SLURM_CPUS_PER_TASK input > output