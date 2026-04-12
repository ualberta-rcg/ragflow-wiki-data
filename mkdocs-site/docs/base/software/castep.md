---
title: "CASTEP"
slug: "castep"
lang: "base"

source_wiki_title: "CASTEP"
source_hash: "fa50b5bda91138d1be321afc0be6c6d3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:54:19.475850+00:00"

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
  - "What are the necessary steps and commands required to install CASTEP on the cluster?"
  - "How do you load the CASTEP module into your environment after the installation is complete?"
  - "What command is used to execute a CASTEP job on a compute node, and what specific input files does it require?"
  - "What are the necessary steps and commands required to install CASTEP on the cluster?"
  - "How do you load the CASTEP module into your environment after the installation is complete?"
  - "What command is used to execute a CASTEP job on a compute node, and what specific input files does it require?"

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

!!! tip
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