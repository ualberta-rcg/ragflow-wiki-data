---
title: "Tutoriel Apprentissage machine/en"
slug: "tutoriel_apprentissage_machine"
lang: "en"

source_wiki_title: "Tutoriel Apprentissage machine/en"
source_hash: "d83b2ce127ca508e105ae4cf4d0e4776"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:11:31.411758+00:00"

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

This page is a beginner's manual concerning how to port a machine learning job to one of our clusters.

## Step 1: Remove All Graphical Display

Edit your program such that it doesn't use a graphical display. All graphical results will have to be written to disk, and visualized on your personal computer once the job is finished. For example, if you show plots using matplotlib, you need to [write the plots to image files instead of showing them on screen](https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab).

## Step 2: Archiving a Data Set

Shared storage on our clusters is not designed to handle lots of small files (they are optimized for very large files). Make sure that the data set you need for your training is in an archive format like `tar`, which you can then transfer to your job's compute node when the job starts.

!!! warning
    If you do not respect these rules, you risk causing an enormous number of I/O operations on the shared filesystem, leading to performance issues on the cluster for all its users.

If you want to learn more about how to handle collections of large numbers of files, we recommend that you spend some time reading [this page](handling-large-collections-of-files.md).

Assuming that the files you need are in the directory `mydataset`:

```bash
tar cf mydataset.tar mydataset/*
```

The above command does not compress the data. If you believe that this is appropriate, you can use `tar czf`.

## Step 3: Preparing Your Virtual Environment

[Create a virtual environment](python.md#creating-and-using-a-virtual-environment) in your home space.

For details on installation and usage of machine learning frameworks, refer to our documentation:

*   [PyTorch](pytorch.md)
*   [TensorFlow](tensorflow.md)

## Step 4: Interactive Job (salloc)

We recommend that you try running your job in an [interactive job](running-jobs.md#interactive-jobs) before submitting it using a script (discussed in the following section). You can diagnose problems more quickly using an interactive job. An example of the command for submitting such a job is:

```bash
salloc --account=def-someuser --gres=gpu:1 --cpus-per-task=3 --mem=32000M --time=1:00:00
```

Once the job has started:

*   Activate your virtual environment.
*   Try to run your program.
*   Install any missing modules if necessary. Since the compute nodes don't have internet access, you will have to install them from a login node. Please refer to our documentation on [virtual environments](python.md#creating-and-using-a-virtual-environment).
*   Note the steps that you took to make your program work.

!!! tip "Local Storage Usage"
    Now is a good time to verify that your job reads and writes as much as possible on the compute node's local storage (`$SLURM_TMPDIR`) and as little as possible on the [shared filesystems (home, scratch, and project)](storage-and-file-management.md).

## Step 5: Scripted Job (sbatch)

You must [submit your jobs](running-jobs.md#use-sbatch-to-submit-jobs) using a script in conjunction with the `sbatch` command, so that they can be entirely automated as a batch process. Interactive jobs are just for preparing and debugging your jobs, so that you can execute them fully and/or at scale using `sbatch`.

### Important Elements of an `sbatch` Script

1.  Account that will be "billed" for the resources used
2.  Resources required:
    *   Number of CPUs, suggestion: 6
    *   Number of GPUs, suggestion: 1
        !!! note "GPU Usage"
            Use one (1) single GPU, unless you are certain that your program can use several. By default, TensorFlow and PyTorch use just one GPU.
    *   Amount of memory, suggestion: `32000M`
    *   Duration (Maximum Béluga: 7 days, Graham and Cedar: 28 days)
3.  *Bash* commands:
    *   Preparing your environment (modules, virtualenv)
    *   Transferring data to the compute node
    *   Starting the executable

### Example Script

````bash title="ml-test.sh"
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
````

### Checkpointing a Long-Running Job

We recommend that you checkpoint your jobs in 24-hour units. Submitting jobs which have short durations ensures they are more likely to start sooner. By creating a daisy chain of jobs, it is possible to overcome the seven-day limit on Béluga.

1.  Modify your job submission script (or your program) so that your job can be interrupted and continued. Your program should be able to access the most recent checkpoint file. (See the example script below).
2.  Verify how many epochs (or iterations) can be carried out in a 24-hour unit.
3.  Calculate how many of these 24-hour units you will need: `n_units = n_epochs_total / n_epochs_per_24h`
4.  Use the argument `--array 1-<n_blocs>%1` to ask for a chain of `n_blocs` jobs.

The job submission script will look like this:

````bash title="ml-test-chain.sh"
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
`