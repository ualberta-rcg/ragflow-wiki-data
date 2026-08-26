---
title: "VirSorter2"
slug: "virsorter2"
lang: "base"

source_wiki_title: "VirSorter2"
source_hash: "461990dbfc21ac46a43c1c93e36c8735"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:22:20.616035+00:00"

tags:
  - software

keywords:
  - "SLURM submission script"
  - "Python virtual environment"
  - "pip install"
  - "sbatch"
  - "database directory"
  - "non-interactive job"
  - "salloc"
  - "own dataset"
  - "submit job"
  - "--mem-per-cpu"
  - "interactive job"
  - "--cpus-per-task"
  - "test-virsorter.sh"
  - "successful test run"
  - "VirSorter2"

questions:
  - "What is VirSorter2 and where can its source code and documentation be accessed?"
  - "How can VirSorter2 v2.2.4 be installed and configured in a Python virtual environment using Alliance’s prebuilt Python wheels?"
  - "What are the required steps to test a VirSorter2 installation with the provided test dataset on a SLURM‑based system?"
  - "What steps must be completed before you can submit a non‑interactive job with your own dataset?"
  - "How does the `sbatch` command facilitate submitting jobs on the Alliance CAN platform?"
  - "Where can you find the documentation for using `sbatch` to submit jobs?"
  - "What command is used to request an interactive job allocation with 2 GB memory per CPU and 2 CPUs per task?"
  - "Which script should be executed after the allocation is granted to run the analysis?"
  - "How should you properly terminate the interactive job allocation once the script has finished?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

VirSorter2 is a tool to identify new viral sequences.

This page discusses how to install and use VirSorter2 v2.2.4.

Source code and documentation for VirSorter2 can be found on their [GitHub page](https://github.com/jiarong/VirSorter2).

Remember to [cite](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y#citeas) VirSorter2 if you use it for your analyses.

## Installing VirSorter2 in a Python virtual environment
These instructions install VirSorter2 in your `$HOME` directory using Alliance's prebuilt [Python wheels](http://pythonwheels.com/). Custom Python wheels are stored in `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. To install a VirSorter2 wheel, we will use the `pip` command and install it into a [Python virtual environment](python.md#creating-and-using-a-virtual-environment).

1.  Load the necessary modules.
    ```bash
    module load StdEnv/2020 python/3.8 hmmer/3.3.2 prodigal/2.6.3
    ```
2.  Create and activate a Python virtual environment.
    ```bash
    virtualenv --no-download ~/ENV_virsorter
    source ~/ENV_virsorter/bin/activate
    ```
3.  Install VirSorter2 v2.2.4 in the virtual environment.
    ```bash
    pip install --no-index --upgrade 'pip<25'
    pip install --no-index virsorter==2.2.4
    ```
4.  Validate the installation.
    ```bash
    virsorter -h
    ```
5.  Freeze the environment and requirements set.
    ```bash
    pip freeze > ~/virsorter-2.2.4-requirements.txt
    ```
6.  Download the database in `$SCRATCH` with the `--skip-deps-install` option to bypass conda installation and also because dependencies are already installed.
    ```bash
    virsorter setup --db-dir $SCRATCH/db -j 4 --skip-deps-install
    ```

## Testing VirSorter2
1.  Deactivate your virtual environment
    ```bash
    deactivate
    ```

2.  Download the test dataset in `$SCRATCH`.
    ```bash
    wget -O $SCRATCH/test.fa https://raw.githubusercontent.com/jiarong/VirSorter2/master/test/8seq.fa
    ```
3.  Create a submission script
    ```bash title="test-virsorter.sh"
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
3.  Start an interactive job.
    ```bash
    salloc --mem-per-cpu=2G --cpus-per-task=2 --account=<your-account>
    ```
    ```console
    salloc: Granted job allocation 1234567
    $ bash test-virsorter.sh             # Run the submission script
    $ exit                               # Terminate the allocation
    salloc: Relinquishing job allocation 1234567
    ```

Upon a successful test run, you can submit a non-interactive job with your own dataset using [`sbatch`](https://docs.alliancecan.ca/wiki/Running_jobs#Use_sbatch_to_submit_jobs).