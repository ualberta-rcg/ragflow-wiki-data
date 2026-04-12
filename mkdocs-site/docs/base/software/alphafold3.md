---
title: "AlphaFold3"
slug: "alphafold3"
lang: "base"

source_wiki_title: "AlphaFold3"
source_hash: "2537238e2b88ba38f1ba5f3150829a7a"
last_synced: "2026-04-12T15:59:52.668416+00:00"
last_processed: "2026-04-12T16:17:18.118177+00:00"

tags:
  - software

keywords:
  - "Python virtual environment"
  - "AlphaFold3"
  - "SLURM_TMPDIR"
  - "caching MSA/template search"
  - "model inference"
  - "Model inference"
  - "input data"
  - "A100 GPU"
  - "Data pipeline"
  - "virtual environment"
  - "pip install"
  - "unified memory"
  - "GPU memory"
  - "pipeline stages"
  - "inference stage"
  - "AlphaFold"
  - "Alphafold3"
  - "model parameters"
  - "databases"
  - "CPU-only data pipeline"
  - "data pipeline"
  - "job submission"
  - "AlphaFold 3"
  - "SLURM submission script"

questions:
  - "What are the step-by-step instructions for creating a Python virtual environment and installing AlphaFold3 on the cluster?"
  - "How do users obtain the AlphaFold3 model parameters and where must the required databases be stored?"
  - "Why is it necessary to run AlphaFold3 in stages, and how does this separation of tasks optimize resource usage?"
  - "What are the recommended CPU and memory resource allocations for running the AlphaFold3 data pipeline script?"
  - "What specific GPU hardware constraints must be met to successfully execute the AlphaFold3 model inference stage?"
  - "How do the provided SLURM scripts manage the setup of virtual environments and the installation of AlphaFold3 dependencies during job execution?"
  - "Why is the CPU-only data pipeline separated from the GPU-dependent model inference?"
  - "How does caching the results of the MSA and template search benefit the overall pipeline?"
  - "What types of variations can be tested across multiple inferences using the reused augmented JSON?"
  - "How are the input and output directory paths configured for the AlphaFold data?"
  - "What commands are used to generate and activate the virtual environment in the SLURM temporary directory?"
  - "How are AlphaFold and its dependencies installed within the newly created virtual environment?"
  - "What are the necessary environment variables and command-line arguments needed to configure and run the AlphaFold3 inference script?"
  - "How can a user submit the data processing and inference stages as either independent or dependent jobs using the job scheduler?"
  - "What specific environment variable adjustments and memory allocations are required to troubleshoot GPU out-of-memory issues when processing large inputs?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

This page discusses how to use AlphaFold v3.0.

Source code and documentation for AlphaFold3 can be found at their [GitHub page](https://github.com/google-deepmind/alphafold3).
Any publication that discloses findings arising from use of this source code or the model parameters should [cite](https://github.com/google-deepmind/alphafold3#citing-this-work) the [AlphaFold3 paper](https://doi.org/10.1038/s41586-024-07487-w).

## Available versions
AlphaFold3 is available on our clusters as prebuilt Python packages (wheels). You can list available versions with `avail_wheels`.
```bash
avail_wheels alphafold3
```

AlphaFold2 is still available. Documentation is [here](alphafold2.md).

## Creating a requirements file for AlphaFold3

1. Load AlphaFold3 dependencies.
```bash
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12
```

2. Download run script.

### Version 3.0.1
```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/tags/v3.0.1/run_alphafold.py
```

### Version 3.0.0
```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/23e3d46d4ca126e8731e8c0cbb5673e9a848ceb5/run_alphafold.py
```

3. Create and activate a Python virtual environment.
```bash
virtualenv --no-download ~/alphafold3_env
source ~/alphafold3_env/bin/activate
```

4. Install a specific version of AlphaFold3 and its Python dependencies.
```bash
pip install --no-index --upgrade pip
pip install --no-index alphafold3==X.Y.Z
```
where `X.Y.Z` is the exact desired version, for instance `3.0.0`.
You can omit to specify the version in order to install the latest one available from the wheelhouse.

5. Build data.
```bash
build_data
```
This will create data files inside your virtual environment.

6. Validate it.
```bash
python run_alphafold.py --help
```

7. Freeze the environment and requirements set.
```bash
pip freeze > ~/alphafold3-requirements.txt
```

8. Deactivate the environment.
```bash
deactivate
```

9. Clean up and remove the virtual environment.
```bash
rm -r ~/alphafold3_env
```

The virtual environment will be created in your job instead.

## Model
You can obtain the model by requesting it from Google. They aim to respond to requests within 2-3 business days.
Please see [Obtaining Model Parameters](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file).

## Databases
Note that AlphaFold3 requires a set of databases.

**Important:** The databases must live in the `$SCRATCH` directory.

1. Download the fetch script
```bash
wget https://raw.githubusercontent.com/google-deepmind/alphafold3/refs/heads/main/fetch_databases.sh
```

2. Download the databases
```bash
mkdir -p $SCRATCH/alphafold/dbs
bash fetch_databases.sh $SCRATCH/alphafold/dbs
```

## Running AlphaFold3 in stages
Alphafold3 must be run in [stages](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#running-the-pipeline-in-stages), that is:
1. Splitting the CPU-only data pipeline from model inference (which requires a GPU), to optimise cost and resource usage.
2. Caching the results of MSA/template search, then reusing the augmented JSON for multiple different inferences across seeds or across variations of other features (e.g. a ligand).

For reference on Alphafold3:
*   see [inputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)
*   see [outputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md)
*   see [performance](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md)

### 1. Data pipeline (CPU)
Edit the following submission script according to your needs.
```bash title="alphafold3-data.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-data
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # a MAXIMUM of 8 core, AlphaFold has no benefit to use more
#SBATCH --mem=64G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data
OUTPUT_DIR=$SLURM_TMPDIR/alphafold/output   # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# build data in $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --nhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --jackhmmer_n_cpu=$SLURM_CPUS_PER_TASK \
    --norun_inference  # Run data stage

# copy back
mkdir $SCRATCH/alphafold/output
cp -vr $OUTPUT_DIR $SCRATCH/alphafold/output
```

### 2. Model inference
Edit the following submission script according to your needs.

!!! warning "Compatibility"
    Alphafold3 **only** support compute capability 8.0 or greater, that is **A100s or greater**.

```bash title="alphafold3-inference.sh"
#!/bin/bash

#SBATCH --job-name=alphafold3-inference
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=08:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=1         # AlphaFold has no benefit to use more for the inference stage
#SBATCH --gpus=a100:1             # Alphafold3 inference only runs on ONE A100 or greater.
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 hmmer-alphafold3/3.4 rdkit/2024.03.5 python/3.12 cuda/12.2 cudnn/9.2

DOWNLOAD_DIR=$SCRATCH/alphafold/dbs    # set the appropriate path to your downloaded data
INPUT_DIR=$SCRATCH/alphafold/input     # set the appropriate path to your input data, following the data stage.
OUTPUT_DIR=$SCRATCH/alphafold/output   # set the appropriate path to your output data

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Install AlphaFold and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/alphafold3-requirements.txt

# build data in $VIRTUAL_ENV
build_data

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#compilation-time-workaround-with-xla-flags
export XLA_FLAGS="--xla_gpu_enable_triton_gemm=false"

# https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#gpu-memory
export XLA_PYTHON_CLIENT_PREALLOCATE=true
export XLA_CLIENT_MEM_FRACTION=0.95

# Edit with the proper arguments and run your commands.
# run_alphafold.py --help
python run_alphafold.py \
    --db_dir=$DOWNLOAD_DIR \
    --input_dir=$INPUT_DIR \
    --output_dir=$OUTPUT_DIR \
    --jax_compilation_cache_dir=$HOME/.cache \
    --norun_data_pipeline  # Run inference stage
```

### 3. Job submission

Then, submit the jobs to the scheduler.

#### Independent jobs
```bash
sbatch alphafold3-data.sh
```

Wait until it complete, then submit the second stage:
```bash
sbatch alphafold3-inference.sh
```

#### Dependent jobs
```bash
jid1=$(sbatch alphafold3-data.sh)
jid2=$(sbatch --dependency=afterok:$jid1 alphafold3-inference.sh)
sq
```
If the first stage fails, you will have to manually cancel the second stage:
```bash
scancel -u $USER -n alphafold3-inference
```

## Troubleshooting
### Out of memory (GPU)
If you would like to run AlphaFold3 on inputs larger than 5,120 tokens, or on a GPU with less memory (an A100 with 40 GB of memory, for instance), you can enable [unified memory](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#unified-memory)

In your submission script for the inference stage, add these environment variables:
```bash
export XLA_PYTHON_CLIENT_PREALLOCATE=false
export TF_FORCE_UNIFIED_MEMORY=true
export XLA_CLIENT_MEM_FRACTION=2.0  # 2 x 40GB = 80 GB
```
and adjust the amount of memory allocated to your job accordingly, for instance: `#SBATCH --mem=80G`