---
title: "Nibi/en"
slug: "nibi"
lang: "en"

source_wiki_title: "Nibi/en"
source_hash: "609d45599ea16db1125fc88ff416b722"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:01:12.769260+00:00"

tags:
  []

keywords:
  - "H100 GPUs"
  - "JupyterLab"
  - "NVIDIA GPUs"
  - "CPU cores"
  - "VAST Data storage"
  - "Nibi Open OnDemand"
  - "nvidia_h100_80gb_hbm3"
  - "Nibi cluster"
  - "MIG"
  - "Nibi"
  - "GPU instance names"
  - "file recovery"
  - "Compute Node"
  - "Short name"
  - "Compute nodes"
  - "pre-configured environment"
  - "JupyterHub"
  - "Nibi JupyterLab"
  - "Slurm options"
  - "Python virtual environment"
  - "H100-80gb"
  - "Open OnDemand"

questions:
  - "What is the Nibi cluster, and what are the primary methods provided for users to access and transfer data to it?"
  - "How does Nibi's storage system handle space accounting and the experimental quota limits for the /scratch directory?"
  - "What are the specific hardware characteristics of Nibi's compute nodes and its interconnect network fabric?"
  - "How do users specify requests for full H100 GPUs versus fractional Multi-Instance GPU (MIG) instances using Slurm commands?"
  - "What are the specific policies regarding user directory creation in the project space and the scratch storage quotas on the Nibi cluster?"
  - "How can users access the Nibi cluster and run interactive applications like JupyterLab through a web browser using Open OnDemand?"
  - "What are the different naming categories used to classify the GPU instances in the table?"
  - "What is the designated full name for the H100-80gb GPU instance?"
  - "What is the short name provided for the MIG H100-1g.10gb instance?"
  - "What is the URL for the Nibi Open OnDemand portal mentioned in the text?"
  - "What kind of working environment does \"Option 1\" provide for users?"
  - "What specific steps must a user take to request a new Nibi JupyterLab session after logging into the portal?"
  - "How can a user launch and access JupyterLab using a custom Python virtual environment through the Nibi Open OnDemand portal?"
  - "What are the scheduling requirements and user responsibilities when running jobs on the AMD MI300A nodes?"
  - "How does the snapshot backup mechanism work on Nibi, and what steps are required to recover an accidentally deleted file using the oops command?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Key                                         | Value                                                                                                        |
| :------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| Availability                                | since 31 July 2025                                                                                           |
| SSH login node                              | `nibi.alliancecan.ca`                                                                                        |
| Automation node                             | *robot.nibi.alliancecan.ca*                                                                                  |
| Web interface                               | [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)                                                         |
| Globus collection                           | [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3)       |
| Data transfer node (rsync, scp, sftp,...) | use login nodes                                                                                              |
| Portal                                      | [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)                                                    |

Nibi, the Anishinaabemowin word for water, is a general-purpose cluster of 134,400 CPU cores and 288 H100 NVIDIA GPUs. Built by [Hypertec](https://www.hypertec.com/), the cluster is hosted and operated by [SHARCNET](https://www.sharcnet.ca/) at the University of Waterloo.

## Storage
Parallel storage: 25 petabytes, all [SSD](https://en.wikipedia.org/wiki/Solid-state_drive) from [VAST Data](https://www.vastdata.com/) for `/home`, `/project` and `/scratch`.

!!! note
    Vast implements space accounting for quotas differently: you are "charged" for the apparent size of your files. This is in contrast to some Lustre configurations, which transparently compress files, and charge for the space used after compression.

!!! warning
    Nibi is using a new, experimental mechanism for handling `/scratch`. As on all systems, you have a soft and hard limit, but on Nibi, the soft limit is low (1TB), and you have a 60-day grace period. After the grace period expires, the soft limit is enforced (no further file creation/expansion). To fix this, your usage must drop below the soft limit.

## Interconnect fabric
* Nokia 200/400G ethernet
    * 200 Gbit/s network bandwidth for CPU nodes.
    * 200 Gbit/s non-blocking network bandwidth between all Nvidia GPU nodes.
    * 200 Gbit/s network bandwidth between all AMD GPU nodes.
    * 24x100 Gbit/s connection to the VAST storage nodes.
    * 2:1 blocking at 400 Gbit/s uplinks for all compute nodes.

The topology of the network is described in the file:

`/etc/slurm/topology.conf`

For better performance of tightly coupled multi-node jobs, you may constrain them to use only one network switch, by adding this option to your job submission script:

```bash
# Request a single network switch for the job
#SBATCH --switches=1
```

## Node characteristics
| nodes | cores | available memory | node-local storage | CPU                                       | GPU                                             |
| :---- | :---- | :--------------- | :----------------- | :---------------------------------------- | :---------------------------------------------- |
| 700   | 192   | 748G or 766000M  | 3T                 | 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3 |                                                 |
| 10    | 192   | 6000G or 6144000M| 3T                 | 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3 |                                                 |
| 36    | 112   | 2000G or 2048000M| 11T                | 2 x Intel 8570 @ 2.1 GHz, 300MB cache L3  | 8 x Nvidia H100 SXM (80 GB), connected via NVLink |
| 6     | 96    | 495G or 507000M  | 3T                 | 4 x AMD MI300A @ 2.1GHz (Zen4+CDNA3)      | The CPU cores and CDNA3-based GPUs are in the same socket and share a unified memory. [See section below for use instructions.](#amd-mi300a-nodes) |

### GPU instances
Available GPU instance names are:

| Model or instance     | Short name      | Without unit    | By memory    | Full name                         |
| :-------------------- | :-------------- | :-------------- | :----------- | :-------------------------------- |
| **GPU**               |                 |                 |              |                                   |
| **H100-80gb**         | `h100`          | `h100`          | `h100_80gb`  | `nvidia_h100_80gb_hbm3`           |
| **MIG**               |                 |                 |              |                                   |
| **H100-1g.10gb**      | `h100_1g.10gb`  | `h100_1.10`     | `h100_10gb`  | `nvidia_h100_80gb_hbm3_1g.10gb`   |
| **H100-2g.20gb**      | `h100_2g.20gb`  | `h100_2.20`     | `h100_20gb`  | `nvidia_h100_80gb_hbm3_2g.20gb`   |
| **H100-3g.40gb**      | `h100_3g.40gb`  | `h100_3.40`     | `h100_40gb`  | `nvidia_h100_80gb_hbm3_3g.40gb`   |

To request one or more full H100 GPUs, you need to use one of the following Slurm options:

*   **One H100-80gb**: `--gpus=h100:1` or `--gpus=h100_80gb:1`
*   **Multiple H100-80gb** per node:
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **For multiple full H100 GPUs** spread anywhere: `--gpus=h100:n` (replace n with the number of GPUs you want)

Approximately half of the GPU nodes are configured with [MIG technology](../programming/multi-instance_gpu.md), and only 3 GPU instance sizes are available:

*   **H100-1g.10gb**: 1/8th of the computing power with 10GB GPU memory
*   **H100-2g.20gb**: 2/8th of the computing power with 20GB GPU memory
*   **H100-3g.40gb**: 3/8th of the computing power with 40GB GPU memory

To request **one and only one GPU instance** for your compute job, use the corresponding option:

*   **H100-1g.10gb**: `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb**: `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb**: `--gpus=h100_3g.40gb:1`

The maximum recommended number of CPU cores and system memory per GPU instance is listed [in this table](../running-jobs/allocations_and_compute_scheduling.md#ratios-in-bundles).

## Site specifics
### Internet access
All nodes on Nibi have Internet access; no special firewall permission or proxying is necessary.

### Project space
User directories are no longer created by default on `/project`. Users can always create their own directories in the group's `/project` using `mkdir`. This allows groups to decide how their `/project` is organised for sharing data amongst group members.

### Scratch quota
A 1 TB soft quota on scratch applies to each user. This soft quota can be exceeded for up to 60 days, after which no additional files may be written to scratch. Files may be written again once the user has removed or deleted enough files to bring their total scratch use under 1 TB. See the [Storage and file management](../storage-and-data/storage_and_file_management.md) for more information.

### Access through Open OnDemand (OOD)
One can now access the Nibi cluster simply through a web browser. Nibi uses Open OnDemand (OOD), a web-based platform that simplifies cluster access by providing a web interface to the login nodes and a remote desktop environment. To log in to Nibi, go to [https://ondemand.sharcnet.ca/](https://ondemand.sharcnet.ca/), sign in with MFA; you will see a user-friendly interface offering options to open a Bash shell terminal or launch a remote desktop session.

### Use of JupyterLab via OOD
You can run JupyterLab interactively via the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca).

**Option 1**: working with a pre-configured environment, same as from [JupyterHub](../interactive/jupyterhub.md)

After logging in to the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca), click “Compute Node” from the top menu and select “Nibi JupyterLab.” This will open a page with a form where you can request a new Nibi JupyterLab session.

After completing the form with your requirement details, click “Launch” to submit your request. Once the status of the requested Nibi JupyterLab changes to Running, click “Connect to Jupyter” to open JupyterLab in your web browser.

More details about the pre-configured JupyterLab are described [here](../interactive/jupyterlab.md#the-jupyterlab-interface).

**Option 2**: working with a self-built [Python virtual environment](../software/python.md#creating-and-using-a-virtual-environment)

After logging in to the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca), click “Compute Node” from the top menu and select “Compute Desktop.” This will open a page with a form where you can request a new Compute Desktop session.

After completing the form with your requirement details, click “Launch” to submit your request. Once the status of the requested Compute desktop changes to Running, click “Launch Compute Desktop” to connect to the desktop. A Linux desktop will appear.

On the Compute desktop, right-click the mouse in any blank area; a shortcut menu appears. Select "Open in Terminal" to open a terminal window, where you can create or activate your Python virtual environment that has JupyterLab installed.

If you do not have JupyterLab installed in the Python virtual environment, which you would like to work with, you can have it installed with the command:

```bash
# (your_python_ENV) [username@<node>.nibi]$
pip install --no-index jupyterlab
```

Then, you can launch JupyterLab from your Python virtual environment with the command:

```bash
# (your_python_ENV) [username@<node>.nibi]$
jupyter-lab --notebook-dir $HOME
```

You will see JupyterLab is opened in the web browser on the Desktop with your `$HOME` contents listed in the file browser panel on JupyterLab.

### Support for VDI via OOD
Nibi no longer offers Virtual Desktop Infrastructure (VDI). Instead, it provides a remote desktop environment through the [portal](https://ondemand.sharcnet.ca/) of Open OnDemand (OOD), offering improved hardware performance and software support.

### AMD MI300A nodes
These should be currently scheduled as full nodes. It is the user's responsibility to make sure the processes inside the job run with correct core and memory binding. Here is a representative job script that uses 4 processes.

```sh linenums="1" title="simple_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --gpus=mi300a:4
#SBATCH --mem=100g
#SBATCH --time=00:02:00

# verify GPUS are available (optional)

rocm-smi

# run program compiled with ROCm support for MI300A
```

### Oops, I accidentally deleted my files, what should I do?
A backup mechanism on Nibi takes a snapshot of your files on `/home` and `/project` every 30 minutes and saves the snapshots for two weeks. If you accidentally delete a file, you may be able to retrieve it from these snapshots, providing the file was deleted less than two weeks ago. However, if one makes changes to a file after the most recent snapshot then deletes it, the changes cannot be recovered.

To find a deleted file, use the `oops` command to check the current directory, or give an optional directory name to check there instead. To recover a file, copy it from the path returned by `oops` using standard tools like `cp`. Snapshots are read-only; you cannot delete or change files in snapshots, you must copy them first. Do not refer to files in snapshots in your job scripts.

```bash
# [username@<node>.nibi]$
ls
dont_delete_me.txt
rm dont_delete_me.txt
ls
# Output:
# [username@<node>.nibi]$
oops
# Output:
# Deleted files found in snapshots:
# ./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt
# Files created less than 9 min ago (2026-04-01 14:00:00-04:00) are not yet backed up
# Files deleted more than 0 days ago (2026-04-01 13:30:00-04:00) please submit a help ticket
cp ./.snapshot/backup_2026-04-01_18_00_00_UTC/dont_delete_me.txt .
ls
# Output:
# dont_delete_me.txt