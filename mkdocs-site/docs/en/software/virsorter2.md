---
title: "VirSorter2/en"
slug: "virsorter2"
lang: "en"

source_wiki_title: "VirSorter2/en"
source_hash: "e179f1f67d2af1cd7cd69e817031d093"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:22:42.765222+00:00"

tags:
  - software

keywords:
  - "Python virtual environment"
  - "pip install"
  - "sbatch submission"
  - "database setup"
  - "VirSorter2"

questions:
  - "How can VirSorter2 v2.2.4 be installed in a Python virtual environment on the Alliance system, including module loading and wheel installation?"
  - "What are the required steps to test the VirSorter2 installation, from deactivating the environment to running the provided test dataset with a submission script?"
  - "How should a SLURM job be configured and submitted to run VirSorter2 on your own dataset, including module loading, virtual environment creation, and database specification?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[VirSorter2](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-020-00990-y) is a tool to identify new viral sequences.

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
6.  Download the database in `$SCRATCH` with the `--skip-deps-install` option to bypass Conda installation and also because dependencies are already installed.
    ```bash
    virsorter setup --db-dir $SCRATCH/db -j 4 --skip-deps-install
    ```

## Testing VirSorter2
1.  Deactivate your virtual environment.
    ```bash
    deactivate
    ```
2.  Download the test dataset in `$SCRATCH`.
    ```bash
    wget -O $SCRATCH/test.fa https://raw.githubusercontent.com/jiarong/VirSorter2/master/test/8seq.fa
    ```
3.  Create a submission script.
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
4.  Start an interactive job.
    ```bash
    salloc --mem-per-cpu=2G --cpus-per-task=2 --account=<your-account>
    ```
    ```text
    salloc: Granted job allocation 1234567
    bash test-virsorter.sh             # Run the submission script
    exit                               # Terminate the allocation
    salloc: Relinquishing job allocation 1234567
    ```

Upon a successful test run, you can submit a non-interactive job with your own dataset using `[sbatch](https://docs.alliancecan.ca/wiki/Running_jobs#use-sbatch-to-submit-jobs)`.