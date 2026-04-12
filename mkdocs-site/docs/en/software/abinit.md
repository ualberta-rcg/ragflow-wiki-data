---
title: "ABINIT/en"
slug: "abinit"
lang: "en"

source_wiki_title: "ABINIT/en"
source_hash: "aa8c939e599f7133f55450274833ebc6"
last_synced: "2026-04-12T19:03:20.394416+00:00"
last_processed: "2026-04-12T19:08:32.262150+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "ABINIT"
  - "computational chemistry"
  - "density functional theory"
  - "atomic data files"
  - "job script"

questions:
  - "What is the primary purpose of the ABINIT software suite and what theoretical frameworks does it utilize?"
  - "How should users obtain the necessary atomic data files for their calculations since they are not maintained centrally on the system?"
  - "What is the recommended procedure for submitting and running non-trivial ABINIT calculations using the job scheduler?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The [ABINIT](https://www.abinit.org) program is "a software suite to calculate the optical, mechanical, vibrational, and other observable properties of materials. Starting from the quantum equations of density functional theory, you can build up to advanced applications with perturbation theories based on DFT, and many-body Green's functions (GW and DMFT). ABINIT can calculate molecules, nanostructures and solids with any chemical composition, and comes with several complete and robust tables of atomic potential", according to its authors.

Run `module spider abinit` to see what versions of ABINIT are currently available. Run it again with a specific version number, e.g. `module spider abinit/8.4.4`, to see if there are other modules that must be loaded first. See [Using modules](../programming/modules.md) for more on the `module` command.

## Atomic data files

We do not maintain a collection of atomic data files for ABINIT. You should obtain the atomic data files you need for your calculation by following the links from the [Atomic data files](https://www.abinit.org/downloads/atomic-data-files) page.

These files rarely exceed 1 megabyte in size, so they may be downloaded directly to any login node using `wget` and the URL of the data file. For example,

```bash
wget http://www.pseudo-dojo.org/pseudos/nc-sr-04_pbe_standard/H.psp8.gz
```

## Example input

Data files for the tutorials and tests can be found at `$EBROOTABINIT/share/abinit-test/Psps_for_tests/`.
Input files mentioned in the [ABINIT tutorial](https://docs.abinit.org/tutorial/) can be found at `$EBROOTABINIT/share/abinit-test/tutorial`.

## Example job script

ABINIT calculations other than the most trivial tests or tutorial examples should be run via the job scheduler, [Slurm](../running-jobs/running_jobs.md). Below is an example job script for running ABINIT, which uses 64 CPU cores on two nodes for 48 hours, requiring 1024 MB of memory per core. You should be able to adapt this to your own needs and the particular cluster you are using.

```sh title="abinit_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=2                # number of nodes
#SBATCH --ntasks=64               # number of MPI processes
#SBATCH --mem-per-cpu=1024M      # memory use per MPI process; default unit is megabytes
#SBATCH --time=2-00:00           # time (DD-HH:MM)

module purge
module load abinit/8.2.2
srun abinit < parameters.txt >& output.log