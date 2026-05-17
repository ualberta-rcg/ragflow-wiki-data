---
title: "Delft3D"
slug: "delft3d"
lang: "base"

source_wiki_title: "Delft3D"
source_hash: "7c9edc5963a2c22412cb747c655e7169"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:21:39.448755+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: true
---

[Delft3D](https://oss.deltares.nl/web/delft3d/home) is a 3D modeling suite to investigate hydrodynamics, sediment transport and morphology and water quality for fluvial, estuarine and coastal environments.

# Examples
Delft3D comes with a number of `run_*` scripts that are expected to be used with the Sun Grid Engine job scheduler and the MPICH library. The Alliance uses SLURM for a [job scheduler](../running-jobs/running_jobs.md) and Open MPI for a default MPI implementation. To illustrate how one can run Delft3D under SLURM, we have provided submission scripts to run the examples supplied with the software.

To copy examples into a scratch directory follow these steps:

```bash
module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 delft3d
cp -a $EBROOTDELFT3D/examples $SCRATCH/delft3d-examples
```

A test case within each sub-directory contains a `start-slurm.sh` script that you can run like this:

```bash
sbatch start-slurm.sh
```

The `readme.examples` file provides a summary of the results.