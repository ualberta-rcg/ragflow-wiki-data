---
title: "Tutoriel Apprentissage machine"
slug: "tutoriel_apprentissage_machine"
lang: "base"

source_wiki_title: "Tutoriel Apprentissage machine"
source_hash: "17be65b92d63dcf1bec53c340238f717"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:12:47.107485+00:00"

tags:
  []

keywords:
  - "soumettre vos tâches"
  - "Ensemble de données"
  - "script sbatch"
  - "tâches interactives"
  - "automatisées"
  - "Tâche interactive"
  - "environnement virtuel"
  - "Environnement virtuel"
  - "Apprentissage automatique"
  - "ressources demandées"
  - "sbatch"
  - "checkpoint"
  - "Tâche scriptée"
  - "morcellement de tâche"

questions:
  - "Comment doit-on adapter son code concernant les sorties graphiques pour qu'il fonctionne correctement sur la grappe ?"
  - "Pourquoi est-il essentiel de regrouper son ensemble de données dans un fichier archive avant de lancer l'entraînement ?"
  - "Quelle est la différence d'utilisation entre une tâche interactive (salloc) et une tâche scriptée (sbatch) lors de la préparation et de l'exécution du projet ?"
  - "Quels sont les éléments et les ressources essentiels à définir lors de la création d'un script de soumission sbatch ?"
  - "Quels sont les avantages de morceler une longue tâche de calcul en blocs de 24 heures ?"
  - "Comment utiliser les tableaux de tâches (--array) et les points de sauvegarde (checkpoints) pour enchaîner et reprendre l'exécution d'un programme ?"
  - "Pourquoi est-il nécessaire d'utiliser des scripts sbatch pour soumettre des tâches ?"
  - "À quoi servent principalement les tâches interactives dans ce processus ?"
  - "Quelle méthode doit être privilégiée pour exécuter des tâches de manière entièrement automatisée et à grande échelle ?"
  - "Quels sont les éléments et les ressources essentiels à définir lors de la création d'un script de soumission sbatch ?"
  - "Quels sont les avantages de morceler une longue tâche de calcul en blocs de 24 heures ?"
  - "Comment utiliser les tableaux de tâches (--array) et les points de sauvegarde (checkpoints) pour enchaîner et reprendre l'exécution d'un programme ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This page is a getting started guide for porting a Machine Learning task to one of our clusters.

## Step 1: Remove All Graphical Output

Modify your program so that it does not use graphical display. All graphical results must be written to disk in a file and viewed on your personal computer once the job is complete. For example, if you are displaying graphics with matplotlib, you must [save the graphics as files instead of displaying them on screen](https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab).

## Step 2: Archiving a Dataset

Shared storage on our clusters is not optimized for managing a large number of small files (they are optimized for very large files). Make sure that the dataset you need for your training is in an archive file (such as `tar`), which you will transfer to your compute node at the beginning of your job.

!!! warning
    If you do not do this, you risk causing high-frequency file reads from the storage node to your compute node, thus harming overall system performance.

If you want to learn more about managing large collections of files, we recommend reading [this page](https://docs.alliancecan.ca/wiki/Handling_large_collections_of_files).

Assuming the files you need are in the `mydataset` folder:

```bash
tar cf mydataset.tar mydataset/*
```

The command above does not compress the data. If you believe it would be appropriate, you can use `tar czf`.

## Step 3: Preparing the Virtual Environment

[Create a virtual environment](../python.md) in your home directory.

For details on installing and using different machine learning frameworks, refer to our documentation:

*   [PyTorch](../pytorch.md)
*   [TensorFlow](../tensorflow.md)

## Step 4: Interactive Job (salloc)

We recommend trying your job in an [interactive job](../../running-jobs/running_jobs.md#interactive-jobs) before submitting it with a script (next section). This will allow you to diagnose problems more quickly. Here is an example command to submit an interactive job:

```bash
salloc --account=def-someuser --gres=gpu:1 --cpus-per-task=3 --mem=32000M --time=1:00:00
```

Once in the job:

*   Activate your Python virtual environment
*   Attempt to run your program
*   Install missing packages if necessary. Since compute nodes do not have Internet access, you will need to perform the installation from a login node. Refer to our [Python virtual environments documentation](../python.md) for more details.
*   Note the steps that were necessary to get your program working

!!! tip
    Now is a good time to ensure your job reads from and writes to the compute node's local storage (`$SLURM_TMPDIR`) as much as possible, and as little as possible to the [shared file systems (home, scratch, project)](../../storage-and-data/storage_and_file_management.md).

## Step 5: Scripted Job (sbatch)

You must [submit your jobs](../../running-jobs/running_jobs.md) using `sbatch` scripts so that they can be fully automated. Interactive jobs are only used to prepare and debug jobs that will then be executed entirely and/or at scale using `sbatch`.

### Important Elements of an `sbatch` Script

1.  Account to which resources will be "billed"
2.  Requested resources:
    *   Number of CPUs, suggestion: 6
    *   Number of GPUs, suggestion: 1
        !!! note
            Use only one (1) GPU unless you are certain your program uses multiple. By default, TensorFlow and PyTorch use a single GPU.
    *   Amount of memory, suggestion: `32000M`
    *   Duration (Béluga maximum: 7 days, Graham and Cedar: 28 days)
3.  Bash commands:
    *   Environment preparation (modules, virtualenv)
    *   Data transfer to the compute node
    *   Executable launch

### Script Example

ml-test.sh
```bash
#!/bin/bash
#SBATCH --gres=gpu:1       # Request GPU "generic resources"
#SBATCH --cpus-per-task=3  # Refer to cluster's documentation for the right CPU/GPU ratio
#SBATCH --mem=32000M       # Memory proportional to GPUs: 32000 Cedar, 47000 Béluga, 64000 Graham.
#SBATCH --time=0-03:00     # DD-HH:MM:SS

module load python/3.6 cuda cudnn

SOURCEDIR=~/ml-test

# Prepare virtualenv
source ~/my_env/bin/activate
# You could also create your environment here, on the local storage ($SLURM_TMPDIR), for better performance. See our docs on virtual environments.

# Prepare data
mkdir $SLURM_TMPDIR/data
tar xf ~/projects/def-xxxx/data.tar -C $SLURM_TMPDIR/data

# Start training
python $SOURCEDIR/train.py $SLURM_TMPDIR/data
```

### Breaking Up a Long Job

!!! tip
    We recommend breaking up your jobs into 24-hour blocks. Requesting shorter jobs improves your priority. By creating a job chain, it is possible to exceed the 7-day limit on Béluga.

1.  Modify your submission script (or your program) so that your job can be interrupted and resumed. Your program must be able to access the most recent *checkpoint*. (See the script example below.)
2.  Check how many epochs (or iterations) can be completed within 24 hours.
3.  Calculate how many 24-hour blocks you will need: `n_blocks = n_epochs_total / n_epochs_per_24h`
4.  Use the argument `--array 1-<n_blocks>%1` to request a chain of `n_blocks` jobs.

The submission script will look like this:

ml-test-chain.sh
```bash
#!/bin/bash
#SBATCH --array=1-10%1   # 10 is the number of jobs in the chain
#SBATCH ...

module load python/3.6 cuda cudnn

# Prepare virtualenv
...

# Prepare data
...

# Get most recent checkpoint
CHECKPOINT_EXT='*.h5'  # Replace by *.pt for PyTorch checkpoints
CHECKPOINTS=~/scratch/checkpoints/ml-test
LAST_CHECKPOINT=$(find $CHECKPOINTS -maxdepth 1 -name "$CHECKPOINT_EXT" -print0 | xargs -r -0 ls -1 -t | head -1)

# Start training
if [ -z "$LAST_CHECKPOINT" ]; then
    # $LAST_CHECKPOINT is null; start from scratch
    python $SOURCEDIR/train.py --write-checkpoints-to $CHECKPOINTS ...
else
    python $SOURCEDIR/train.py --load-checkpoint $LAST_CHECKPOINT --write-checkpoints-to $CHECKPOINTS ...
fi