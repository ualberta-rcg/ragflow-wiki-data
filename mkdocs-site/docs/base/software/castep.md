---
title: "CASTEP"
slug: "castep"
lang: "base"

source_wiki_title: "CASTEP"
source_hash: "fa50b5bda91138d1be321afc0be6c6d3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:03:22.238698+00:00"

tags:
  - software
  - computationalchemistry

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

## Installing CASTEP
For example, with version `20.11`:
1. You must [**get the archive file that contains the installer**](http://www.castep.org/get_castep); this file should be named `CASTEP-20.11.tar.gz`.
2. Upload the `CASTEP-20.11.tar.gz` file to your `/home/$USER` folder on the cluster you intend to use.
3. On the cluster, run the command:

```bash
[name@server ~]$ eb CASTEP-20.11-iofbf-2020a.eb --sourcepath=$HOME --disable-enforce-checksums
```

Once this command has completed, log out from the cluster and log back in.

## Using CASTEP
You should be able to load the module with:

```bash
[name@server ~]$ module load castep
```

On a compute node, the CASTEP executable can be used like an [MPI application](running-jobs.md#mpi-job):

```bash
[name@server ~]$ srun castep.mpi seedname
```

Where input files would be `seedname.cell` and `seedname.param` (i.e. "seedname" could be a different name).

## Reference
* [CASTEP User Documentation](https://castep-docs.github.io/castep-docs/)