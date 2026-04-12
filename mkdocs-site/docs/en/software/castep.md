---
title: "CASTEP/en"
slug: "castep"
lang: "en"

source_wiki_title: "CASTEP/en"
source_hash: "a2c5078c70213d407e036cc03b671dcb"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:54:29.929936+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "CASTEP"
  - "Installation"
  - "MPI application"
  - "Cluster"
  - "Computational Chemistry"

questions:
  - "What are the required steps and commands to successfully install CASTEP on a cluster?"
  - "How do you load the CASTEP module and execute it as an MPI application on a compute node?"
  - "What types of input files are necessary to run a CASTEP job using a specific seedname?"
  - "What are the required steps and commands to successfully install CASTEP on a cluster?"
  - "How do you load the CASTEP module and execute it as an MPI application on a compute node?"
  - "What types of input files are necessary to run a CASTEP job using a specific seedname?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Installing CASTEP

For example, with version `20.11`:

1.  You must [**get the archive file that contains the installer**](http://www.castep.org/get_castep); this file should be named `CASTEP-20.11.tar.gz`.
2.  Upload the `CASTEP-20.11.tar.gz` file to your `/home/$USER` folder on the cluster you intend to use.
3.  On the cluster, run the command:

    ```bash
    eb CASTEP-20.11-iofbf-2020a.eb --sourcepath=$HOME --disable-enforce-checksums
    ```

    !!! note
        Once this command has completed, log out from the cluster and log back in.

## Using CASTEP

You should be able to load the module with:

```bash
module load castep
```

On a compute node, the CASTEP executable can be used like an [MPI application](../running-jobs/running_jobs.md#mpi-job):

```bash
srun castep.mpi seedname
```

Where input files would be `seedname.cell` and `seedname.param` (i.e., "seedname" could be a different name).

## Reference

*   [CASTEP User Documentation](https://castep-docs.github.io/castep-docs/)