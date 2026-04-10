---
title: "BUSCO/en"
tags:
  - software

keywords:
  []
---

BUSCO (<i>Benchmarking sets of Universal Single-Copy Orthologs</i>) is an application for assessing genome assembly and annotation completeness.

For more information, see the [user manual](https://busco.ezlab.org/busco_userguide.html).

## Available versions 
Recent versions are available as wheels. Older versions are available as a module; please see the [Modules](#modules.md) section below.

To see the latest available version, run

```bash
avail_wheels busco
```

## Python wheel 
### Installation 
<b>1.</b> Load the necessary modules.

```bash
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06
```

<b>2.</b> Create the virtual environment.

```bash
source ~/busco_env/bin/activate
```

<b>3.</b> Install the wheel and its dependencies.

```bash

```
6.0.0
}}

<b>4.</b> Validate the installation.

```bash
busco --help
```

<b>5.</b>  Freeze the environment and requirements set. To use the requirements text file, see the <i>bash</i> submission script shown at point 8.

```bash
pip freeze > ~/busco-requirements.txt
```

### Usage 
#### Datasets 
<b>6.</b> You must pre-download any datasets from [BUSCO data](https://busco-data.ezlab.org/v5/data/) before submitting your job.

You can access the available datasets in your terminal by typing `busco --list-datasets`.

You have <b>two</b> options to download datasets:

*use the `busco` command,
*use the `wget` command.

===== <b>6.1</b>  Using the `busco` command =====
This is the preferred option. Type this command in your working directory to download a particular dataset, for example

```bash
busco --download bacteria_odb10
```

It is also possible to do a bulk download by replacing the dataset name by the following arguments: `all`, `prokaryota`, `eukaryota`, or `virus`, for example

```bash
busco --download virus
```

This will
::1. create a BUSCO directory hierarchy for the datasets,
::2. download the appropriate datasets,
::3. decompress the file(s),
::4. if you download multiple files, they will all be automatically added to the lineages directory. 

The hierarchy will look like this:
<blockquote>
* busco_downloads/

::* information/

::::lineages_list.2021-12-14.txt

::* lineages/

::::bacteria_odb10

::::actinobacteria_class_odb10

::::actinobacteria_phylum_odb10

::* placement_files/

::::list_of_reference_markers.archaea_odb10.2019-12-16.txt
</blockquote>

Doing so, all your lineage files should be in <b>busco_downloads/lineages/</b>. When referring to `--download_path busco_downloads/` in the BUSCO command line, it will know where to find the lineage dataset argument `--lineage_dataset bacteria_odb10`. If the <i>busco_download </i> directory is not in your working directory, you will need to provide the full path.

=====<b>6.2</b> Using the `wget` command =====

All files must be decompressed with `tar -xvf file.tar.gz`.

```bash
tar -xvf bacteria_odb10.2020-03-06.tar.gz
```

#### Test 
<b>7.</b> Download a genome file.

```bash
wget https://gitlab.com/ezlab/busco/-/raw/master/test_data/bacteria/genome.fna
```

<b>8.</b> Run.

Command to run a single genome:

{{Command|busco --offline --in genome.fna --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/}}

Command to run multiple genomes that would be saved in the genome directory (in this example, the <i>genome/</i> folder would need to be in the current directory; otherwise, you need to provide the full path):

{{Command|busco --offline --in genome/ --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/}}

The single genome command should take less than 60 seconds to complete. Production runs which take longer must be submitted to the [scheduler](running-jobs.md).

===== BUSCO tips =====

Specify `--in genome.fna` for single file analysis. 

Specify `--in genome/` for multiple files analysis.

===== Slurm tips =====
Specify `--offline` to avoid using the internet.

Specify `--cpu` to `$SLURM_CPUS_PER_TASK` in your job submission script to use the number of CPUs allocated.

Specify `--restart` to restart from a partial run.

#### Job submission

Here you have an example of a submission script. You can submit as so: `sbatch run_busco.sh`.

{{File
  |name=run_busco.sh
  |lang="bash"
  |contents=

#!/bin/bash

#SBATCH --job-name=busco9_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=01:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # adjust depending on the size of the genome(s)/protein(s)/transcriptome(s)
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install busco and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/busco-requirements.txt

# Edit with the proper arguments, run your commands.
busco --offline --in genome.fna --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/

}}

#### Augustus parameters
<b>9.</b> Advanced users may want to use Augustus parameters: `--augustus_parameters="--yourAugustusParameter"`.

*Copy the Augustus <i>config</i> directory to a writable location.

```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

*Make sure to define the `AUGUSTUS_CONFIG_PATH` environment variable.

```bash

```
$HOME/augustus_config}}

#### SEPP parameters
<b>10.</b> To use SEPP parameters, you need to install SEPP locally in your virtual environment. This should be done from the login node.

<b>10.1.</b> Activate your BUSCO virtual environment.

```bash
source busco_env/bin/activate
```

<b>10.2.</b> Install DendroPy.

```bash
pip install 'dendropy<4.6'
```

<b>10.3.</b> Install SEPP.

```bash
python setup.py install
```

<b>10.4.</b> Validate the installation.

```bash
run_sepp.py -h
```

<b>10.5.</b> Because SEPP is installed locally, you cannot create the virtual environment as described in the previous submission script. To activate your local virtual environment, simply add the following command immediately under the line to load the module:

```bash
source ~/busco_env/bin/activate
```

== Modules == 

<b>1.</b> Load the necessary modules.

```bash
module load StdEnv/2018.3 gcc/7.3.0 openmpi/3.1.4 busco/3.0.2 r/4.0.2
```

This will also load modules for Augustus, BLAST+, HMMER and some other
software packages that BUSCO relies upon.

<b>2.</b> Copy the configuration file.

```bash
cp -v $EBROOTBUSCO/config/config.ini.default $HOME/busco_config.ini
```

or

```bash
wget -O $HOME/busco_config.ini https://gitlab.com/ezlab/busco/raw/master/config/config.ini.default
```

<b>3.</b> Edit the configuration file. The locations of external tools are all specified in the last section, which is shown below:

**`partial_busco_config.ini`**
```text
[tblastn]
# path to tblastn
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/blast+/2.7.1/bin/

[makeblastdb]
# path to makeblastdb
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/blast+/2.7.1/bin/

[augustus]
# path to augustus
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/bin/

[etraining]
# path to augustus etraining
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/bin/

# path to augustus perl scripts, redeclare it for each new script
[gff2gbSmallDNA.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/
[new_species.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/
[optimize_augustus.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/

[hmmsearch]
# path to HMMsearch executable
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/hmmer/3.1b2/bin/

[Rscript]
# path to Rscript, if you wish to use the plot tool
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/r/4.0.2/bin/
```

<b>4.</b> Copy the Augustus `config` directory to a writable location.

```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

<b>5.</b> Check that it runs.

```bash

```
$HOME/busco_config.ini
|export AUGUSTUS_CONFIG_PATH$HOME/augustus_config
|run_BUSCO.py --in $EBROOTBUSCO/sample_data/target.fa --out TEST --lineage_path $EBROOTBUSCO/sample_data/example --mode genome
}}

The `run_BUSCO.py` command should take less than 60 seconds to complete.
Production runs which take longer should be submitted to the [scheduler](running-jobs.md).

= Troubleshooting =
## Cannot write to Augustus config path 
Make sure you have copied the <i>config</i> directory to a writable location and exported the `AUGUSTUS_CONFIG_PATH` variable.