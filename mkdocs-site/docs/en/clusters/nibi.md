---
title: "Nibi/en"
tags:
  []

keywords:
  []
---

{| class="wikitable"
|-
| Availability: since 31 July 2025
|-
| SSH login node: nibi.alliancecan.ca
|-
| Automation node: <i>robot.nibi.alliancecan.ca</i>
|-
| Web interface: [ondemand.sharcnet.ca](https://ondemand.sharcnet.ca)
|-
| Globus collection: [alliancecan#nibi](https://app.globus.org/file-manager?origin_id=07baf15f-d7fd-4b6a-bf8a-5b5ef2e229d3) 
|-
| Data transfer node (rsync, scp, sftp,...): use login nodes 
|-
| Portal: [portal.nibi.sharcnet.ca](https://portal.nibi.sharcnet.ca)
|}

Nibi, the Anishinaabemowin word for water, is a general purpose cluster of 134,400 CPU cores and 288 H100 NVIDIA GPUs. Built by [Hypertec](https://www.hypertec.com/), the cluster is hosted and operated by [SHARCNET](https://www.sharcnet.ca/) at University of Waterloo.

<!--
Note that Nibi, like Fir, does provide internet access from compute nodes; no special firewall permission or proxying is necessary.
-->

=Storage=
Parallel storage: 25 petabytes, all [SSD](https://en.wikipedia.org/wiki/Solid-state_drive) from [VAST Data](https://www.vastdata.com/) for `/home`, `/project` and `/scratch`.

Note that Vast implements space accounting for quotas differently: you are "charged" for the apparent size of your files.  This is in contrast to some Lustre configurations, which transparently compress files, and charge for the space used after compression.

Note also that Nibi is using a new, experimental mechanism for handling /scratch.  As on all systems, you have a soft and hard limit, but on Nibi, the soft limit is low (1TB), and you have a 60d grace period.  After the grace period expires, the soft limit is enforced (no further file creation/expansion).  To fix this, your usage must drop below the soft limit.

=Interconnect fabric=
* Nokia 200/400G ethernet
** 200 Gbit/s network bandwidth for CPU nodes.
** 200 Gbit/s non-blocking network bandwidth between all Nvidia GPU nodes.
** 200 Gbit/s network bandwidth between all AMD GPU nodes.
** 24x100 Gbit/s connection to the VAST storage nodes.
** 2:1 blocking at 400 Gbit/s uplinks for all compute nodes.

The topology of the network is described in the file:

 /etc/slurm/topology.conf

For better performance of tightly coupled multi-node jobs, you may constrain them to use only one network switch, by adding this option to your job submission script:

 #SBATCH --switches=1

=Node characteristics=
{| class="wikitable sortable"
! nodes !! cores !! available memory !! node-local storage || CPU !! GPU
|-
| 700 || 192 || 748G or 766000M || 3T || 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3 ||
|-
|  10 || 192 || 6000G or 6144000M || 3T || 2 x Intel 6972P @ 2.4 GHz, 384MB cache L3 ||
|-
|  36 || 112 || 2000G or 2048000M || 11T || 2 x Intel 8570 @ 2.1 GHz, 300MB cache L3 || 8 x Nvidia H100 SXM (80 GB), connected via NVLink
|-
|   6 ||  96 || 495G or 507000M || 3T || 4 x AMD MI300A @ 2.1GHz (Zen4+CDNA3) || The CPU cores and CDNA3-based GPUs are in the same socket and share a unified memory.
|}
## GPU instances 
Available GPU instance names are:
{| class="wikitable"
! colspan="2" | Model or instance !! Short name !! Without unit !! By memory !! Full name
|-
| <b>GPU</b>
|| <b>H100-80gb</b>
|| `h100`
|| `h100`
|| `h100_80gb`
|| `nvidia_h100_80gb_hbm3`
|-
| rowspan="3" | <b>MIG</b>
|| <b>H100-1g.10gb</b>
|| `h100_1g.10gb`
|| `h100_1.10`
|| `h100_10gb`
|| `nvidia_h100_80gb_hbm3_1g.10gb`
|-
| <b>H100-2g.20gb</b>
|| `h100_2g.20gb`
|| `h100_2.20`
|| `h100_20gb`
|| `nvidia_h100_80gb_hbm3_2g.20gb`
|-
| <b>H100-3g.40gb</b>
|| `h100_3g.40gb`
|| `h100_3.40`
|| `h100_40gb`
|| `nvidia_h100_80gb_hbm3_3g.40gb`
|}

To request one or more full H100 GPUs, you need to use one of the following Slurm options:

* <b>One H100-80gb</b> : `--gpus=h100:1` or `--gpus=h100_80gb:1`
* <b>Multiple H100-80gb</b> per node :
** `--gpus-per-node=h100:2`
** `--gpus-per-node=h100:3`
** `--gpus-per-node=h100:4`
* <b>For multiple full H100 GPUs</b> spread anywhere: `--gpus=h100:n` (replace n with the number of GPUs you want)

Approximately half of the GPU nodes are configured with [MIG technology](multi-instance_gpu.md), and only 3 GPU instance sizes are available:

* <b>H100-1g.10gb</b>: 1/8th of the computing power with 10GB GPU memory
* <b>H100-2g.20gb</b>: 2/8th of the computing power with 20GB GPU memory
* <b>H100-3g.40gb</b>: 3/8th of the computing power with 40GB GPU memory
To request <b>one and only one GPU instance</b> for your compute job, use the corresponding option:

* <b>H100-1g.10gb</b> : `--gpus=h100_1g.10gb:1`
* <b>H100-2g.20gb</b> : `--gpus=h100_2g.20gb:1`
* <b>H100-3g.40gb</b> : `--gpus=h100_3g.40gb:1`
The maximum recommended number of CPU cores and system memory per GPU instance is listed [in this table](allocations_and_compute_scheduling#ratios_in_bundles.md).

=Site specifics=
## Internet access
All nodes on Nibi have Internet access, no special firewall permission or proxying is necessary.

## Project space
User directories are no longer created by default on `/project`. Users can always create their own directories in the group's `/project` using `mkdir`. This allows groups to decide how their `/project` is organised for sharing data amongst group members. 

## Scratch quota
An 1 TB soft quota on scratch applies to each user. This soft quota can be exceeded for up to 60 days after which no additional files may be written to scratch. Files may be written again once the user has removed or deleted enough files to bring their total scratch use under 1 TB. See the [Storage and file management](storage-and-file-management.md) for more information.

## Access through Open OnDemand (OOD)
One can now access the Nibi cluster simply through a web browser. Nibi uses Open OnDemand (OOD), a web based platform that simplifies cluster access by providing a web interface to the login nodes and a remote desktop environment. To login to Nibi, go to https://ondemand.sharcnet.ca/, sign in with MFA, you will see a user friendly interface offering options to open a Bash shell terminal or launch a remote desktop session.

## Use of JupyterLab via OOD
[thumb](file:nibi-jupyterlab.png.md)
You can run JupyterLab interactively via the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca).

**Option 1**: working with a pre-configured environment, same as from   [JupyterHub](jupyterhub.md)

After logging in to the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca), click “Compute Node” from the top menu and select “Nibi JupyterLab.” This will open a page with a form where you can request a new Nibi JupyterLab session.

After completing the form with your requirement details, click “Launch” to submit your request. Once the status of the requested Nibi JupyterLab changes to Running, click “Connect to Jupyter” to open JupyterLab in your web browser. 

More details about the pre-configured JupyterLab are described [here](jupyterlab#the_jupyterlab_interface.md). 

**Option 2**: working with a self-built 
[Python virtual environment](python#creating_and_using_a_virtual_environment.md) 

After logging in to the Nibi Open OnDemand [portal](https://ondemand.sharcnet.ca), click “Compute Node” from the top menu and select “Compute Desktop.” This will open a page with a form where you can request a new Compute Desktop session.
[thumb](file:nibi-desktop.png.md)

After completing the form with your requirement details, click “Launch” to submit your request. Once the status of the requested Compute desktop changes to Running, click “Launch Compute Desktop” to connect to the desktop. A Linux desktop will appear.

On the Compute desktop, right-click the mouse in any blank area, a shortcut menu appears; select "Open in Terminal" to open a terminal window, where you can create or activate your Python virtual environment that has JupyterLab installed. 
  
If you do not have JupyterLab installed in the Python virtual environment, which you would like to work with, you can have it installed with the command:

```bash
pip install --no-index jupyterlab
```
 

Then, you can launch JupyterLab from your Python virtual environment with the command:

```bash
jupyter-lab --notebook-dir $HOME
```

 
You will see JupyterLab is opened in the web browser on the Desktop with your $HOME contents listed in the file browser panel on JupyterLab.

## Support for VDI via OOD
Nibi no longer offers Virtual Desktop Infrastructure (VDI). Instead, it provides a remote desktop environment through the [portal](https://ondemand.sharcnet.ca/) of Open OnDemand (OOD), offering improved hardware performance and software support.

## Oops, I accidentally deleted my files, what should I do?
A backup mechanism on Nibi takes a snapshot of your files on `/home` and `/project` every 30 minutes and saves the snapshots for two weeks.  If you accidentally delete a file, you may be able to retrieve it from these snapshots, providing the file was deleted less than two weeks ago.  However, if one makes changes to a file after the most recent snapshot then deletes it, the changes cannot be recovered.

To find a deleted file, use the `oops` command to check the current directory, or give an optional directory name to check there instead. To recover a file, copy it from the path returned by `oops` using standard tools like `cp`. Snapshots are read-only; you cannot delete or change files in snapshots, you must copy them first. Do not refer to files in snapshots in your job scripts.

```bash
ls
dont_delete_me.txt
```