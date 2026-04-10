---
title: "VirSorter2"
tags:
  - software

keywords:
  []
---

__TOC__ 

[VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y) is a tool to identify new viral sequences.

This page discusses how to install and use VirSorter2 v2.2.4.

Source code and documentation for VirSorter2 can be found on their [GitHub page](https://github.com/jiarong/VirSorter2).

Remember to [cite](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y#citeas) VirSorter2 if you use it for your analyses.

== Installing VirSorter2 in a Python virtual environment == 
These instructions install VirSorter2 in your $HOME directory using Alliance's prebuilt [Python wheels](http://pythonwheels.com/). Custom Python wheels are stored in `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. To install a VirSorter2 wheel, we will use the `pip` command and install it into a [Python virtual environment](python#creating_and_using_a_virtual_environment.md).

1. Load the necessary modules.

```bash
module load StdEnv/2020 python/3.8 hmmer/3.3.2 prodigal/2.6.3
```

2. Create and activate a Python virtual environment.

```bash
source ~/ENV_virsorter/bin/activate
```

3. Install VirSorter2 v2.2.4 in the virtual environment.

```bash

```
2.2.4
}}
4. Validate the installation.

```bash
virsorter -h
```

5. Freeze the environment and requirements set.

```bash
pip freeze > ~/virsorter-2.2.4-requirements.txt
```

6. Download the database in $SCRATCH with the `--skip-deps-install` option to bypass conda installation and also because dependencies are already installed.

```bash
virsorter setup --db-dir $SCRATCH/db -j 4 --skip-deps-install
```

== Testing VirSorter2 == 
1. Deactivate your virtual environment

```bash
deactivate
```

2. Download the test dataset in `$SCRATCH`.

```bash
wget -O $SCRATCH/test.fa https://raw.githubusercontent.com/jiarong/VirSorter2/master/test/8seq.fa
```

3. Create a submission script

**`test-virsorter.sh`**
```bash
#!/bin/bash

#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=2G
#SBATCH --cpus-per-task=2

# Load modules dependencies
module load StdEnv/2020 python/3.8 hmmer/3.3.2 prodigal/2.6.3

# Generate your virtual environment in $SLURM_TMPDIR
virtualenv --no-download $SLURM_TMPDIR/ENV
source $SLURM_TMPDIR/ENV/bin/activate
pip install --no-index --upgrade pip

# Install VirSorter2 and its dependencies
pip install --no-index -r ~/virsorter-2.2.4-requirements.txt

# Run VirSorter2 with the test dataset, using at most $SLURM_CPUS_PER_TASK and ignore conda.
# The database must already exist and you must specify its location.
virsorter run -w $SCRATCH/test.out -i $SCRATCH/test.fa --min-length 1500 -j $SLURM_CPUS_PER_TASK --verbose --use-conda-off --db-dir $SCRATCH/db all
```

3. Start an interactive job.

```bash

```
2G --cpus-per-task2 --account<your-account>
}}
 salloc: Granted job allocation 1234567
 $ bash test-virsorter.sh             # Run the submission script
 $ exit                               # Terminate the allocation
 salloc: Relinquishing job allocation 1234567

Upon a successful test run, you can submit a non-interactive job with your own dataset using [`sbatch`](https://docs.alliancecan.ca/wiki/Running_jobs#Use_sbatch_to_submit_jobs).