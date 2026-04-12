---
title: "Transition from Niagara to Trillium/en"
slug: "transition_from_niagara_to_trillium"
lang: "en"

source_wiki_title: "Transition from Niagara to Trillium/en"
source_hash: "71651b93732d1188ab89cc650f14624a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:03:48.495135+00:00"

tags:
  []

keywords:
  - "Hardware changes"
  - "CVMFS software stack"
  - "SSH login"
  - "GPU nodes"
  - "Trillium cluster"
  - "directory locations"
  - "GPU compute nodes"
  - "CPU and GPU subclusters"
  - "NVIDIA H100"
  - "Recompilation"
  - "StdEnv/2023"
  - "data migration"
  - "module load"
  - "Trillium"
  - "CUDA"
  - "gcc compiler"
  - "software stack"
  - "CCDB opt-in"
  - "Niagara"
  - "AMD Zen 4"
  - "resource management"
  - "Virtual python environments"

questions:
  - "How do users opt-in to gain access to the Trillium cluster and its HPSS storage system?"
  - "What are the required login methods and initial setup commands for new users accessing the CPU and GPU subclusters?"
  - "What are the specific hardware configurations and upgrades of the Trillium CPU and GPU compute nodes compared to the previous systems?"
  - "How do users manually transfer data that was modified after the automatic migration cutoff date, and what are the new directory paths for home, scratch, and project on Trillium?"
  - "What changes have been made to file and directory permissions on Trillium, and how does the read-only nature of home and project directories affect where compute jobs must write data?"
  - "How does the software stack on Trillium differ from Niagara, and what specific commands are required to load the standard environment and CUDA modules?"
  - "What are the specific hardware specifications, including CPU and GPU models, for an individual compute node in the Trillium GPU subcluster?"
  - "How many total compute nodes and individual GPUs make up the entire Trillium GPU subcluster?"
  - "What are the required resource utilization guidelines for running jobs efficiently on the system?"
  - "How do you load the default set of modules, such as the gcc compiler, to match the environment of other national clusters?"
  - "What specific module needs to be loaded in addition to the standard environment to compile GPU code?"
  - "Which specific nodes on the Trillium cluster support the use of the cuda module, and which do not?"
  - "Why is it recommended to recompile all code, and which specific types of code absolutely require it?"
  - "Why must users recreate their Python virtual environments, and what is the recommended alternative to using Anaconda?"
  - "What resources are available for users seeking training, documentation, or technical support for the Trillium system?"
  - "Why is it recommended to recompile all code, and which specific types of code absolutely require it?"
  - "Why must users recreate their Python virtual environments, and what is the recommended alternative to using Anaconda?"
  - "What resources are available for users seeking training, documentation, or technical support for the Trillium system?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Getting Access

### Opt-in

For Niagara and Mist, users had to opt-in on CCDB to use the system. The same is true for the Trillium cluster, but the webpage on which you can do this has changed to [https://ccdb.alliancecan.ca/me/access_systems](https://ccdb.alliancecan.ca/me/access_systems) (on which you can also opt in to other national services).

Users that had opted into Niagara/Mist on August 5, 2025 will have automatically been opted-in to Trillium.

Opting into Trillium gives you access to both the CPU and GPU subclusters of Trillium.

To get access to HPSS, the nearline system for Trillium, there is a separate opt-in on [https://ccdb.alliancecan.ca/me/access_systems](https://ccdb.alliancecan.ca/me/access_systems); here too, if you had access to HPSS through Niagara before August 5th, you will be opted-in automatically. For the moment, HPSS has not been integrated into Trillium yet. Once it has, the files on HPSS will not have changed as it is still the same storage system.

### Logging in

#### Terminal access

You can log in to the CPU subcluster of Trillium by SSHing to `trillium.alliancecan.ca`:

```bash
$ ssh USERNAME@trillium.alliancecan.ca
```

The first time you log in, please make sure you are actually accessing Trillium by checking if the [login node SSH host key fingerprint](../getting-started/ssh_security_improvements.md) matches. As was the case on Niagara and Mist, you will need to use [SSH Keys](../getting-started/ssh_keys.md) and have MFA enabled on your CCDB account. This will get you onto one of six CPU login nodes called tri-login01-6. These login nodes do not have GPUs and **can only submit jobs to CPU compute nodes**.

To access the GPU subcluster of Trillium, you should log into `trillium-gpu.alliancecan.ca` (also with SSH keys and MFA):

```bash
$ ssh USERNAME@trillium-gpu.alliancecan.ca
```

This will land you on the GPU login node trig-login01, which has 4 NVIDIA H100 GPUs, and from which you can only **submit to the compute nodes of the GPU subcluster**.

#### First time actions

After logging in for the first time, you will see the files that were on Niagara. Your initialization files likely won't work, or not exactly as they should. We **highly recommend** that you run the following command:

```bash
$ trisetup
```

This will populate the following files in your home directory: `.bashrc`, `.bash_profile`, `.chsrc`, and `.Xauthority`. It will also create the directories `.licenses`, `.local`, `.ssh`, and `links`. The latter contains symbolic links to your scratch and project directories. Your original versions of these files will be saved under a different name with a date stamp.

After this, you can recompile your code, reinstall virtual environments, etc. (see below).

#### Web access

The [SciNet OnDemand website](https://ondemand.scinet.utoronto.ca) will remain connected to Niagara for now, but will eventually also offer a way to log into Trillium and run web-based apps like Jupyter with access to the Trillium file system.

## Hardware changes

Trillium consists of two homogeneous subclusters, a CPU subcluster and a GPU subcluster.

### CPUs

Each compute node of the CPU subcluster has 192 cores (Niagara had 40) and 755 GB of available memory (Niagara had 188 GB). The CPUs are AMD Zen 5 chips - a.k.a. Turin (Niagara had Intel Skylake and Cascaselake chips). There are 1224 compute nodes in the Trillium CPU subcluster, for a total of 235,008 cores.

If you were compiling code that used math and linear algebra routines from the Intel MKL, we suggest you switch to [Flexiblas](../programming/blas_and_lapack.md), or use the AMD AOCL libraries directly; these are available in the `aocl-blas` and `aocl-lapack` modules.

### GPUs

Each compute node in the GPU subcluster has 96 cores and 755 GB of available memory, and 4 GPUs. The CPUs are AMD Zen 4 (a.k.a. Genoa) chips, while the GPUs are NVIDIA H100 (Mist's GPUs were V100). There are 61 GPU compute nodes, so in total Trillium has 244 GPUs.

!!! note
    It is important to make sure that your jobs are not wasting resources. They should either use all of the cores, or exhaust most of the memory, or efficiently use GPUs.

## Storage

### Automatic data migration

Any data that was present on your home, scratch, and project directories on Niagara on July 31st 2025 and that you did not change after that, will have been copied over to the corresponding directory on Trillium. Any data that was added or modified afterwards on Niagara may need to be copied over by the user. For example, a user might SSH to Niagara `nia-datamover1`:

```bash
$ ssh USERNAME@nia-datamover1.scinet.utoronto.ca
```

and take advantage that both Niagara and Trillium file systems are mounted there to copy locally from one to the other:

```bash
USERNAME@nia-dm1:~$ cp /home/G/GROUP/USERNAME/file.txt /trillium_home/USERNAME/file.txt
```

As of November 4, 2025, the quotas of home and scratch remain the same default values as they were on Niagara, i.e., 100 GB and 25 TB, respectively.

### Directory locations

The directory layout of home, scratch, and project has changed compared to that on Niagara. Your home and scratch directories will not be nested under a group, but will be at **/home/USERNAME** and **/scratch/USERNAME**.

The scratch quota and purging settings will be reviewed in the coming months.

If your group had a project directory on Niagara, you will now find that at **/project/RRG-NAME**, where RRG-NAME is the name of your RRG allocation. In addition all groups now have a project directory **/project/def-PINAME** with a quota of 1 TB.

As before, home and project will be backed up, but scratch will not.

To make it easier to find these locations, a directory called `links` can be created inside your `$HOME` containing links to your scratch and project directories. To get this set of links, please run the following command, once, after logging in:

```bash
$ trisetup
```

This will also update your `.bashrc` and other startup files; the command will show exactly what it did and where it saves any earlier version.

Once setup, the links in `$HOME/links/project` will be automatically updated if you join, leave, or move groups.

### File and directory permissions

Your home directory on Niagara had you as the owner but your PI's group as the group-ownership. In contrast, on Trillium, your files and directories in home have the group-ownership of your own, private group. This means that sharing files on home with other group members will require you to set the permissions using ACLs or change the group ownership of files.

The situation is similar for scratch, in that new users will see their scratch directory to be private, i.e., it has the group-ownership set to their private group; if you want to share files with someone else, you will need to use ACL or change group ownerships. It should be noted, however, that users whose files were transferred from Niagara, will see those having the group-ownership of the research group under which their scratch was originally nested.

The project directories are setup for sharing and as such have group-membership corresponding to their def or RRG allocation.

!!! note "Read-only file systems"
    The home and project file systems are read-only on compute nodes on Trillium. Your compute jobs, therefore, have to write to the scratch directory. Copying data from scratch to project or home should be restricted to data that really needs to be conserved and backed up. For this, you can either use the `scp` or `rsync` commands to a datamover or login node at the end of your job, or log into the datamover node and perform the transfer there.

## Software

### Software stack

The default NiaEnv software stack that was available on Niagara will be retired and will not be available on Trillium. Likewise, the MistEnv software stack on Mist will not be available on Trillium-gpu. The CVMFS software stack that is available on the other national clusters will be used on Trillium as well. However, only the **gentoo/2023** and **CCconfig** modules will be loaded by default; all other modules (for compilers, libraries, Python, etc.) will have to be explicitly loaded.

To get the same set of default modules as on the other national clusters, you should load the `StdEnv/2023` module:

```bash
$ module load StdEnv/2023
```

This will load the GCC compiler as the default compiler, as well as many other modules.

To compile GPU code with CUDA, you also need to load the `cuda` module:

```bash
trig-login01$ module load StdEnv/2023 cuda/12.6
```

The `cuda` module is not available on the Trillium CPU nodes, it only works with its GPU login node and GPU compute nodes.

### Recompilation required

!!! warning
    Even though all your files, including binaries, were copied over, codes that weren’t using the CVMFS software stack, or that used absolute paths, will have to be recompiled. In fact, it is recommended to recompile all your code, even if they did use the CVMFS stack on Niagara.

### Recreate virtual Python environments required

!!! warning
    Even though all your files were copied over, your virtual environments will not work. You must recreate them because of the users’ directory change.

If you had Anaconda virtual environments, you will find that there is no Anaconda module. You should switch to using virtual environments instead.

## Training, documentation, and support

*   New quickstart: [Trillium Quickstart](trillium_quickstart.md)
*   Support email: [trillium@tech.alliancecan.ca](mailto:trillium@tech.alliancecan.ca)
*   Self-guided "[Intro to SciNet and Trillium](https://education.scinet.utoronto.ca/course/view.php?id=1389)"