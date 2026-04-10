---
title: "Delft3D"
slug: "delft3d"
lang: "base"

source_wiki_title: "Delft3D"
source_hash: "3393775aeaa31c7e2d690d9fb06be25e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:09:24.988991+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[Delft3D](https://oss.deltares.nl/web/delft3d/home) is a 3D modelling suite to investigate hydrodynamics, sediment transport and morphology and water quality for fluvial, estuarine and coastal environments.

# Examples
Delft3D comes with a number of `run_*` scripts that are expected to be used with the Sun Grid Engine job scheduler and the MPICH library. The Alliance uses SLURM for a job scheduler and Open MPI for a default MPI implementation. To illustrate how one can run Delft3D under SLURM, we have provided submission scripts to run computational examples supplied with the software.

To copy examples into your home directory follow these steps:

```bash
$ module load StdEnv/2020 intel/2020.1.217 openmpi/4.0.3 delft3d
$ cp -a $EBROOTDELFT3D/examples ~/
```

Test cases within the `~/examples/` directory contain `start-slurm.sh` scripts that you can run with SLURM using a command such as this one:

```bash
sbatch start-slurm.sh
```

The `~/examples/readme.examples` file provides a summary of the results.