---
title: "Tutoriel Apprentissage machine"
slug: "tutoriel_apprentissage_machine"
lang: "base"

source_wiki_title: "Tutoriel Apprentissage machine"
source_hash: "17be65b92d63dcf1bec53c340238f717"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:11:05.448739+00:00"

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

This page is a getting started guide for porting a Machine Learning task to one of our clusters.

## Step 1: Remove all graphical display

Modify your program so that it does not use graphical display. Any graphical results should be written to disk in a file, and viewed on your personal computer once the task is complete. For example, if you are displaying graphics with matplotlib, you must [save the graphics as files instead of displaying them on screen](https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab).

## Step 2: Archiving a dataset

Shared storage on our clusters is not optimized for handling a large number of small files (it is rather optimized for very large files). Make sure that the dataset you need for your training is in an archive file (such as "tar"), which you will transfer to your compute node at the start of your job. **If you do not do this, you risk causing high-frequency file reads from the storage node to your compute node, thereby harming overall system performance**. If you want to learn more about managing large file collections, we recommend reading [this page](https://docs.alliancecan.ca/wiki/handling-large-collections-of-files/fr).

Assuming the files you need are in the `mydataset` folder:

```bash
$ tar cf mydataset.tar mydataset/*
```

The above command does not compress the data. If you think it would be appropriate, you can use `tar czf`.

## Step 3: Preparing the virtual environment

[Create a virtual environment](python.md#create-and-use-a-virtual-environment) in your home space.

For details on installing and using different machine learning frameworks, refer to our documentation:

*   [PyTorch](pytorch.md)
*   [TensorFlow](tensorflow.md)

## Step 4: Interactive job (salloc)

We recommend trying your job in an [interactive job](running-jobs.md#interactive-jobs) before submitting it with a script (next section). This will allow you to diagnose problems more quickly. Here is an example command for submitting an interactive job:

```bash
$ salloc --account=def-someuser --gres=gpu:1 --cpus-per-task=3 --mem=32000M --time=1:00:00
```

Once in the job:

*   Activate your Python virtual environment
*   Try running your program
*   Install any missing packages if necessary. Since compute nodes do not have internet access, you will need to perform the installation from a login node. Refer to our [documentation on Python virtual environments](python.md#create-and-use-a-virtual-environment) for more details.
*   Note the steps that were necessary to get your program working

**Now is a good time to check that your job reads and writes as much as possible to the compute node's local storage (`$SLURM_TMPDIR`), and as little as possible to the [shared file systems (home, scratch, project)](storage-and-file-management.md).**

## Step 5: Scripted job (sbatch)

You must [submit your jobs](running-jobs.md#submit-jobs-with-sbatch) using `sbatch` scripts, so that they can be fully automated. Interactive jobs are only used to prepare and debug jobs that will then be run entirely and/or at large scale using `sbatch`.

### Important elements of an `sbatch` script

1.  Account to which resources will be "billed"
2.  Requested resources:
    *   Number of CPUs, suggestion: 6
    *   Number of GPUs, suggestion: 1 (**Use only one (1) GPU, unless you are certain your program uses several. By default, TensorFlow and PyTorch use a single GPU.**)
    *   Amount of memory, suggestion: `32000M`
    *   Duration (Maximum Beluga: 7 days, Graham and Cedar: 28 days)
3.  Bash commands:
    *   Environment preparation (modules, virtualenv)
    *   Data transfer to the compute node
    *   Launching the executable

### Example script

```bash title="ml-test.sh"
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

### Breaking a long job into chunks

We recommend breaking your jobs into 24-hour chunks. Requesting shorter jobs improves your priority. By creating a job chain, it is possible to exceed the 7-day limit on Beluga.

1.  Modify your submission script (or program) so that your job can be interrupted and continued. Your program must be able to access the most recent *checkpoint*. (See the example script below.)
2.  Check how many epochs (or iterations) can be completed within 24 hours.
3.  Calculate how many 24-hour chunks you will need: `n_blocks = n_epochs_total / n_epochs_per_24h`
4.  Use the argument `--array 1-<n_blocks>%1` to request a chain of `n_blocks` jobs.

The submission script will look like this:

```bash title="ml-test-chain.sh"
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