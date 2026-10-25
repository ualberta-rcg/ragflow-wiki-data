---
title: "Apptainer"
slug: "apptainer"
lang: "base"

source_wiki_title: "Apptainer"
source_hash: "68c037150c0056187e19711d480fddbf"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:28:58.560203+00:00"

tags:
  []

keywords:
  - "translate"
  - "-B option"
  - "sandbox image"
  - "Docker image"
  - "sudo"
  - "apptainer instance"
  - "disk access speeds"
  - "apptainer exec"
  - "-w/--writable option"
  - "container image"
  - "running daemons"
  - "Conda in Apptainer"
  - "Dockerfile"
  - "Apptainer -W workdir"
  - "available software on clusters"
  - "bind mount options"
  - "-c"
  - "force test to run on more than one node"
  - "bind mounts"
  - "apptainer run"
  - "Apptainer"
  - "apptainer cache clean"
  - "install software"
  - "IPC"
  - "quota file count"
  - "/home /project /scratch"
  - "your-container-name.sif"
  - "module load cuda/13.3"
  - "cache directory"
  - "apptainer inspect --list-apps"
  - "building an image"
  - "environment"
  - "before running"
  - "container image (.sif)"
  - "bind mount"
  - "SIF image"
  - "container"
  - "mpirun inside container"
  - "APPTAINER_TMPDIR"
  - "scratch space"
  - "HPC clusters"
  - "SIF file"
  - "comment"
  - "isolate container"
  - "GPUs"
  - "SLURM_TMPDIR"
  - "Apptainer --fakeroot"
  - "GPUs in Apptainer"
  - "apptainer"
  - "--app appname"
  - "run-help"
  - "--fakeroot"
  - "command line options"
  - "cluster"
  - "hybrid model"
  - "-e"
  - "code"
  - "%runscript"
  - "root permissions"
  - "clean environment options"
  - "APPTAINER_CACHEDIR"
  - "Singularity"
  - "parent PID"
  - "sandbox directory"
  - "disk performance"
  - "container software"
  - "apptainer exec --nv"
  - "multiple nodes"
  - "temporary files"
  - "persistent overlays"
  - "symlinks"
  - "module load openmpi"
  - "Podman"
  - "GPU support --nv --rocm"

questions:
  - "What are the main changes introduced when transitioning from Singularity to Apptainer, and how can existing scripts be ported?"
  - "How should Apptainer be installed on various platforms such as native Linux, Windows (via WSL), and macOS (via a virtual machine)?"
  - "Which other Linux container technologies are discussed, and what are the security or compatibility considerations for using them on HPC clusters?"
  - "Why is sudo unavailable on the Alliance clusters, and what alternatives are recommended for obtaining root privileges?"
  - "What specific steps should be taken to safely build Apptainer container images or overlays, especially regarding networked and Lustre/GPFS filesystems?"
  - "Which Apptainer command‑line options provide environment isolation (e.g., ‑C and ‑c), and how do their isolation levels differ?"
  - "What steps are involved in building an Apptainer image according to the referenced “building an image” section?"
  - "Why might it be unnecessary to install certain software inside an Apptainer container when that software is already available on the cluster?"
  - "How does the presence of pre‑installed software on clusters influence the decision to create a new Apptainer container?"
  - "What does the `-c` option isolate in a running container, and which directories does it provide by default?"
  - "Why is it necessary to use bind mounts when the container needs access to filesystems outside of its isolated environment?"
  - "How does the isolation provided by `-c` differ from other container isolation options that include full filesystem access?"
  - "What does the `-e` option do in Apptainer and which other options does it automatically enable?"
  - "How should the `-W`/`--workdir` option be configured to prevent RAM‑related job failures, and what variable is recommended for its path in SLURM environments?"
  - "What flags and bind‑mount settings are required to run GPU‑accelerated applications (NVIDIA, AMD, or OpenCL) inside an Apptainer container?"
  - "What does the command `apptainer run-help --app appname your-container-name.sif` do, and what should replace `appname` and `your-container-name.sif`?"
  - "How can you list all apps installed in a given Apptainer container?"
  - "Which commands are used to run software inside an Apptainer container, and what are the differences between them?"
  - "What is the difference between `apptainer run` and `apptainer exec` in terms of executing a container’s `%runscript`?"
  - "Which additional command‑line options (e.g., `-C`, `-c`, `-e`, `-W`, bind mounts) are recommended for use on the clusters, and what do they accomplish?"
  - "How can you start an interactive session inside a container with Apptainer, and what is the proper way to exit that session?"
  - "Why is it essential to include the -w or --writable option when modifying a persistent overlay image inside an apptainer shell session?"
  - "What are the recommended methods and limitations for running daemons within Apptainer containers on a compute cluster?"
  - "How can bind mounts be employed to access host directories (e.g., current directory, /project, /scratch) when using Apptainer with the -C option?"
  - "What is the purpose of using the `-C -W $SLURM_TMPDIR -B` options together in the `apptainer shell` command?"
  - "Which documentation sections should be consulted for details on important command‑line options, GPU usage, and bind mounts/persistent overlays?"
  - "Where can users access the official Apptainer documentation for additional information?"
  - "Why are bind mounts especially useful for accessing other team members' files located in different places?"
  - "How do symlinks influence the necessity of mounting the entire filesystem when using bind mounts?"
  - "What should you do if bind mounts don’t work on your cluster, specifically regarding obtaining Apptainer bind mount options for /home, /project, and /scratch?"
  - "How can you bind‑mount a file or directory to a different location inside an Apptainer container, and why is this useful?"
  - "What are the key differences between creating an Apptainer image as a SIF file versus a sandbox directory, and in which scenarios should each format be preferred?"
  - "Why is it recommended to avoid bind‑mounting the /home filesystem or CVMFS paths directly into an Apptainer container?"
  - "Why is using a SIF file recommended instead of a sandbox image on the cluster?"
  - "How does storing an image as a single SIF file improve disk performance and reduce quota file count compared to keeping the files separately?"
  - "Which Apptainer commands are demonstrated for building a new SIF image and removing the original directory?"
  - "Why can't normal users build Apptainer images on clusters without root permissions, and what alternatives are recommended?"
  - "How does the --fakeroot feature behave in Apptainer versions prior to 1.1 compared to version 1.1 and later?"
  - "What are the key differences between building a SIF image and a sandbox directory, and when should each format be chosen?"
  - "Why is using an SIF file recommended over other formats, and how does it improve disk access speed?"
  - "How can Conda be integrated and used inside an Apptainer container?"
  - "What must be done to ensure GPU support works correctly within an Apptainer container?"
  - "How do you enable NVIDIA or AMD GPU support when running a container with Apptainer, and what module loading steps are required?"
  - "What are the recommended approaches for running MPI applications across multiple nodes with Apptainer, and why is the hybrid model preferred over the bind model?"
  - "Which environment and compatibility considerations must be addressed to ensure that the MPI version inside the container works correctly with the host’s MPI installation?"
  - "What prerequisites and system permissions are needed to build an Apptainer image from a Dockerfile using Docker and Apptainer?"
  - "What is the step‑by‑step command sequence to convert a Dockerfile into an Apptainer SIF file, and what does each command accomplish?"
  - "How can you clean Apptainer’s cache and customize its default cache and temporary directories?"
  - "What is the purpose of the `-c` and `-e` clean‑environment options, and when should each be tried?"
  - "Why can a job script that works on a single node fail when executed on multiple nodes?"
  - "How can you force a test with 4 tasks to run on two or more nodes during the testing phase?"
  - "What does the APPTAINER_CACHEDIR environment variable control in Apptainer?"
  - "Which directory is defined by APPTAINER_TMPDIR and when is it used?"
  - "How can you set up Apptainer to use a custom scratch space for its cache and temporary files?"
  - "What steps should be taken before running <code>apptainer</code>?"
  - "Why does the snippet include the comment “<!--T:139-->” and the closing “</translate>” tag?"
  - "What is the purpose of using the <code>apptainer</code> command in this context?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Forewords

## Official Apptainer documentation

This page does not describe all features of Apptainer and does not replace [Apptainer's official documentation](http://apptainer.org/docs). It summarizes basic use, documents some aspects of using Apptainer on Alliance systems, and provides some relevant examples. We recommend you read the official Apptainer documentation concerning the features of Apptainer you are using.

Should you wish to install Apptainer on your own system, [instructions appear here](http://apptainer.org/docs/user/main/quick_start.html#quick-installation). If you are using a recent Windows system, [install WSL](https://learn.microsoft.com/en-ca/windows/wsl/install) first, then within such, install Apptainer. If you are using a Mac, install a Linux distribution in a virtual machine on your computer first, then install Apptainer within such.

## If you are currently using Singularity

We strongly recommend that you use Apptainer instead of Singularity. The Linux Foundation has adopted SingularityCE (up to v3.9.5) and renamed it Apptainer with these changes:

*   Added support for [DMTCP checkpointing](https://dmtcp.sourceforge.io/).
*   Removed support for the `--nvccli` command line option.
*   Removed support for `apptainer build --remote`.
*   Removed support for the SylabsCloud remote endpoint, replacing it with a DefaultRemote endpoint with no defined server for `library://`.
    *   If you need the SylabsCloud remote, the [previous default can be restored](https://apptainer.org/docs/user/1.0/endpoint.html#restoring-pre-apptainer-library-behavior).
*   Renamed all executable names, paths, etc. having `singularity` in their names to have `apptainer` in them.
    *   *E.g.*, instead of using the `singularity` command one uses the `apptainer` command.
    *   *E.g.*, the `~/.singularity` directory is now `~/.apptainer`.
*   Renamed all environment variables having `SINGULARITY` in their names to have `APPTAINER` in them.

Should you need to port scripts to Apptainer, know Apptainer version 1 is backwards compatible with Singularity so switching to Apptainer can be done incrementally.

## Other Linux container technologies

HPC clusters typically use Apptainer. Many users ask about other Linux container technologies so here are some with some comments:
*   [Podman](https://podman.io/)
    *   Supports rootless (*i.e.*, normal) container use, etc. similar to Apptainer.
    *   Is available as a package in rpm-supporting (and some other) Linux distributions.
    *   While Podman is a Linux container technology, there are [instructions for installing Podman on Windows/Mac machines](https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md).
    *   Podman version 4 supports Apptainer .SIF files.
*   [Docker](https://www.docker.com/)
    *   Using Docker on a multiuser cluster creates security risks, therefore we do not make Docker available on our HPC clusters.
    *   In many cases you can build an Apptainer image from a Docker image; see [Building an SIF image](#building-an-sif-image) below.
    *   You can install Docker on your own computer and use it to create an Apptainer image, which can then be uploaded to an HPC cluster as outlined in [Creating an Apptainer container from a Dockerfile](#creating-an-apptainer-container-from-a-dockerfile) below.

## Other items

### General

*   In order to use Apptainer you must have a container **image**, *e.g.*, a `.sif` file or a "sandbox" directory created previously. If you don't already have an image or a sandbox, see the section on **[building an image](#building-an-apptainer-image)** below.
*   While Apptainer is installed and available for use, using Apptainer will require you to install and/or build all software you will need to make use of in your container. In many instances, [we already have such software installed on our clusters](../../programming/available_software.md) so there is often no need to create a container with the same installed in it.

### `sudo`

Many users ask about `sudo` since documentation and websites often discuss using `sudo`. Know the ability to use `sudo` to obtain superuser/root permissions is not available on our clusters. Should you require using `sudo`, consider the following options:

*   Install Linux, Apptainer, and `sudo` in a virtual machine on a system you control so you will be able to have `sudo` access within such. Build your image(s) on that machine and upload them in order to use them on Alliance systems.
*   If appropriate, [submit a ticket](../../support/technical_support.md) asking if Alliance staff would be able to help build the image(s) required needing `sudo`. This may or may not be possible, but feel free to ask in a ticket if what you wish to achieve is beyond your means. Additionally, we may respond with other ways to achieve such which may or may not involve Apptainer.
*   Apptainer version 1.1.x and newer has improved support for users using `--fakeroot` implicitly and explicitly so some things may be possible that were not with Apptainer version 1.0 and Singularity. This includes being able to build some images from `.def` definition files and building some images without needing to use `sudo`. That said, not all images will be able to be built without needing to use `sudo` or superuser/root.

### Building images or overlays

Should you need to build your own container image(s) or overlay(s), be aware of the following:
*   Avoid building a sandbox image using `--fakeroot` on networked filesystem(s): [link to Apptainer documentation](https://apptainer.org/docs/admin/main/installation.html#fakeroot-with-uid-gid-mapping-on-network-filesystems).
*   Explicitly set `APPTAINER_CACHEDIR` to a non-networked filesystem location before using Apptainer: [link to Apptainer documentation](https://apptainer.org/docs/admin/main/installation.html#apptainer-cache-atomic-rename).
*   Explicitly set `APPTAINER_TMPDIR` to a non-Lustre/GPFS filesystem location before using Apptainer: [link to Apptainer documentation](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).
*   Avoid using Lustre/GPFS filesystems as they don't have the feature set required to properly support building Apptainer containers (including `--fakeroot`): [link to Apptainer documentation](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

# Loading an Apptainer module

In order to use the default version of Apptainer available run:
```bash
module load apptainer
```

To see the available versions of Apptainer that can be loaded run:
```bash
module spider apptainer
```

# Running programs within a container

## Important command line options

Software that is run inside a container is in an environment that uses different libraries and tools than what is installed on the host system. It is, therefore, important to run programs within containers by **not** using any environment settings or software defined outside of the container. Unfortunately, by default, Apptainer will run adopting the shell environment of the host and this can result in issues when running programs. To avoid such issues when using `apptainer run`, `apptainer shell`, `apptainer exec`, and/or `apptainer instance`, use one of these options:

| Apptainer environment command line options |
|---|---|
| `-C` | Isolates the running container from **all filesystems** as well as the parent PID, IPC, and environment. Using this option will require [using bind mounts](#bind-mounts) if access to filesystems outside of the container is needed. |
| `-c` | Isolates the running container from **most filesystems** only using a minimal `/dev`, an empty `/tmp` directory, and an empty `/home` directory. Using this option will require [using bind mounts](#bind-mounts) if access to filesystems outside of the container is needed. |
| `-e` | Cleans (some) shell environment variables before running container commands and applies settings for increased OCI/Docker compatibility. Using this option also implies the use of options `--containall`, `--no-init`, `--no-umask`, and `--writable-tmpfs`. |

Another important option is the `-W` or `--workdir` option. On our clusters and on most Linux systems, `/tmp` and similar filesystems use RAM, not disk space. Since jobs typically run on our clusters with limited RAM amounts, this can result in jobs getting killed because they consume too much RAM relative to what was requested for the job. A suitable workaround for this is to tell Apptainer to use a real disk location for its working directory (`workdir`). This is done by passing the `-W` option followed by a path to a disk location where Apptainer can read/write temporary files For example, to run a command called `myprogram` in an Apptainer container image called `myimage.sif` with its working directory set to `/path/to/a/workdir` in the filesystem, you would use

```bash
apptainer run -C -B /project -W /path/to/a/workdir myimage.sif myprogram
```

where:
*   `workdir` can be removed if there are no live containers using it.
*   When using Apptainer in an `salloc`, in an `sbatch` job, or when using [JupyterHub](../../interactive/jupyterhub.md) on our clusters, use `${SLURM_TMPDIR}` for the working directory's location, *e.g.*, `-W ${SLURM_TMPDIR}`.
    *   ASIDE: One should **not** be running programs (including Apptainer) on a login node. Use an interactive `salloc` job.
*   When using bind mounts, see the [section on bind mounts](#bind-mounts) below since not all of our clusters are the same concerning the exact bind mounts needed to access `/home`, `/project`, and `/scratch`.

## Using GPUs

When running software inside a container that requires the use of GPUs it is important to do the following:
*   Ensure that you pass the `--nv` (for NVIDIA hardware) and `--rocm` (for AMD hardware) to Apptainer commands.
    *   These options will ensure the appropriate `/dev` entries are bind mounted inside the container.
    *   These options will locate and bind GPU-related libraries on the host, as well as set the `LD_LIBRARY_PATH` environment variable to enable the aforementioned libraries to work inside the container.
*   Ensure the application using the GPU inside the container was properly compiled to use the GPU and its libraries.
*   When needing to use OpenCL inside the container, besides using the aforementioned options, use the following bind mount: `-B /etc/OpenCL`.

An example of [using NVIDIA GPUs within an Apptainer container](#using-gpus-in-apptainer) appears later on this page.

## Container-specific help: `apptainer run-help`

Apptainer containers built from [Definition files](http://apptainer.org/docs/user/main/definition_files.html) often will have a `%help` section. To see this section run:

```bash
apptainer run-help your-container-name.sif
```

where:
*   `your-container-name.sif` is the name of your container

It is possible your container also has "apps" defined in it, you can get help for those apps by running:

```bash
apptainer run-help --app appname your-container-name.sif
```

where:
*   `appname` is the name of the app
*   `your-container-name.sif` is the name of your container

To see a list of apps installed in your container (if there are any), run:

```bash
apptainer inspect --list-apps your-container-name.sif
```

where:
*   `your-container-name.sif` is the name of your container

## Running software: `apptainer run` or `apptainer exec`

When the `apptainer run` command launches the container, it first runs the `%runscript` defined for that container (if there is one), and then runs the specific command you specified.
The `apptainer exec` command will not run the `%runscript`, even if one is defined in the container.

We suggest that you aways use `apptainer run`.

For example, suppose you want to run the `g++` compiler inside your container to compile a C++ program called `myprog.cpp` and then run that program. To do this, you might use this command:

```bash
apptainer run your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
apptainer run your-container-name.sif ./a.out
```

where:
*   `your-container-name.sif` is the name of your SIF file
*   `g++ -O2 -march=broadwell ./myprog.cpp` is the command you want to run inside the container

On our clusters, you will want to use a number of additional options (that appear after `run`, but before `your-container-name.sif`). These options include `-C`, `-c`, `-e`, `-W` as well as various bind mount options to make your disk space available to the programs that run in your container. For example:

```bash
apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch ./a.out
```

For more information on these options see the following sections on this page:

*   [Important command line options](#important-command-line-options)
*   [Using GPUs](#using-gpus)
*   [Bind mounts and persistent overlays](#bind-mounts-and-persistent-overlays)

as well as the [official Apptainer documentation](http://apptainer.org/docs/user/main/index.html).

## Interactively running software: `apptainer shell`

The `apptainer run`, `apptainer exec`, and `apptainer instance` commands run the programs provided immediately which makes them excellent for use in BASH and SLURM job scripts. There are times when one needs to interactively do work inside a container. To run commands interactively while remaining inside a container, use the `apptainer shell` command instead.

For example, to run commands interactively in a container one first invokes the `apptainer shell` command, *e.g.*,

```bash
apptainer shell your-container-name.sif
```

where:
*   `your-container-name.sif` is the name of your SIF file

Once the container starts, you will see an `Apptainer>` prompt (or `Singularity>` prompt if using Singularity). At this prompt you can run desired shell commands in the container. When done, type `exit` and hit the Enter/Return key to exit the container.

On our clusters, you will want to use a number of additional options (that appear after `run` and before `your-container-name.sif`). These options will include `-C`, `-c`, `-e`, `-W` as well as various bind mount options to make your disk space available to the programs that run in your container. For example:

```bash
apptainer shell -C -W $SLURM_TMPDIR -B /home:/cluster_home -B /project -B /scratch your-container-name.sif
```

For more information on these options see the following sections on this page:

*   [Important Command Line Options](#important-command-line-options)
*   [Using GPUs](#using-gpus)
*   [Bind Mounts and Persistent Overlays](#bind-mounts-and-persistent-overlays)

as well as the [official Apptainer documentation](http://apptainer.org/docs/user/main/index.html).

!!! important
    In addition to choose to use the above options, if you are making use of a persistent overlay image (as a separate file or contained within the SIF file) and want changes to be written to that image, it is extremely important to pass the `-w` or `--writable` option to your container. If this option is not passed to it, any changes you make to the image in the `apptainer shell` session will not be saved!

## Running daemons: `apptainer instance`

Apptainer has been designed to be able to properly run daemons within compute jobs on clusters. Running daemons is achieved, in part, by using `apptainer instance`. See the [official Apptainer documentation on Running Services](http://apptainer.org/docs/user/main/running_services.html) for the details.

!!! note "Note 1"
    Don't run daemons manually without using `apptainer instance` and related commands. Apptainer works properly with other tools such as the Slurm scheduler that run on our clusters. When a job is cancelled, killed, crashes, or is otherwise finished, daemons run using `apptainer instance` will not hang or result in defunct processes. Additionally by using the `apptainer instance` command you will be able to control the daemons and programs running in the same container.

!!! note "Note 2"
    Daemons can only run in your job while your job is running. Should the scheduler kill your job, all daemons running in that job will also be killed. Should you need to run daemons longer than the job they were started in, you may need to also have a virtual machine running in the cloud. If so please contact [technical support](../../support/technical_support.md).

# Bind mounts and persistent overlays

Often, one will want to use either or both of these features in Apptainer:
*   **bind mounts**, to access disk space originating outside of the container, and,
*   **persistent overlays**, to overlay a writable filesystem on an otherwise immutable (*i.e.*, read-only) container image.

## Bind mounts

When Apptainer is used with the `-C` or `-c` options, one will notice that they cannot access their disk space when inside the container. The remedy for this is to explicitly bind mount the disk space they wish to access. For example, suppose a user was using `-C` like this in an `sbatch` job to use Apptainer:

```bash
apptainer run -C -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

where `./my_data_file.txt` is a file in the current directory on the host, *i.e.*, the file is not stored in the container at all. Because of the `-C` option, this file will not be accessible to the `wc` program inside the container and an access error will result. The fix is to bind mount the current directory, *e.g.*,

```bash
apptainer run -C -B . -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

where `-B .` will bind mount the current directory, `.`.

While one can have multiple bind mounts specified, it is often easier to specify the top directories of the filesystems one wishes to access. For example, on our clusters one might want to use

```bash
apptainer run -C -B /project -B /scratch -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

where:
*   `-B /project` mounts the project filesystem
*   `-B /scratch` mounts the scratch filesystem

Doing this is especially useful when:
*   you need to access others' files on your research team in other locations, and/or,
*   you need to access files/directories some of which are `symlinks` to different locations that would/might otherwise be broken if you did not mount the entire filesystem.

If using these bind mounts does not work on the cluster you are using, run this next script to obtain the bind mount options you need to pass to Apptainer for /home, /project, and /scratch on that cluster

```bash
/home/preney/public/apptainer-scripts/get-apptainer-options.sh
```

It should be mentioned that a bind mount does not need to be in the same location inside the container: one can bind mount any file or directory to be at a different location, *e.g.*,

```bash
apptainer run -C -B ./my_data_file.txt:/special/input.dat -W $SLURM_TMPDIR a-container.sif wc -l /special/input.dat
```

*i.e.*, `-B ./my_data_file.txt:/special/input.dat` bind mount maps the file `./my_data_file.txt` to be the file `/special/input.dat` inside the container and the `wc` command now processes that file. This feature can be useful when programs/scripts inside the container have hard-coded paths to files and directories that must be located in certain locations.

If you need to bind-mount the `/home` filesystem in your container, use an alternate destination directory:

*   `-B /home:/cluster_home`

This ensures that configuration files and programs in your home directory do not interfere with the software in your container. For example, programs in `$HOME/bin` and Python packages in `$HOME/.local/lib/python3.x` could be used instead of the corresponding files in your container if you used `-B /home`.

Finally, **don't mount our CVMFS paths** inside your containers as this is fraught with perils and defeats many reasons to use a container. The programs that have to run inside a container need to be completely inside the container. Don't introduce even more programs inside the container if they don't need to be there.

## Persistent overlays

Please refer to Apptainer documentation page about [persistent overlays](https://apptainer.org/docs/user/main/persistent_overlays.html).

# Building an Apptainer image

!!! note
    Please note and heed the advice given in section **[Building images and overlays](#building-images-or-overlays)**.

Apptainer images can be created in the following formats:

*   as an `SIF` file, or
*   as a sandbox directory.

**`SIF` files** can contain multiple parts where each part is typically a `squashfs` filesystem (which are read-only and compressed). It is possible for `SIF` files to contain read-write filesystems and overlay images as well, but such is beyond the scope of this page; see [Apptainer's official documentation](http://apptainer.org/docs) on how to do such. Unless more advanced methods of building an image were used, the Apptainer `build` command produces a `SIF` file with a read-only `squashfs` filesystem when building images. This is the preferred option since the resulting image remains as-is since it is read-only, and the image is much smaller because it is compressed. Know that disk reads from that image are done very quickly.

**A sandbox directory** is a normal directory in the filesystem that starts out as empty. As Apptainer builds the image, it adds to it the files and directories needed in the image. The contents of a sandbox directory should only be accessed or updated through the use of Apptainer. One might need to use a sandbox directory in situations where one needs to have read-write access to the image itself in order to be able to update the container image. That said, if updates are infrequent, it is typically easier and better to use a `SIF` file and when updates need to be done, build a sandbox image from the `SIF` file, make the required changes, and then build a new `SIF` file, *e.g.*,

```bash
cd $HOME
mkdir mynewimage.dir
apptainer build mynewimage.dir myimage.sif
apptainer shell --writable mynewimage.dir
# Run commands to update mynewimage.dir here.
exit
apptainer build newimage.sif mynewimage.dir
rm -rf mynewimage.dir
```

Using an `SIF` file is recommended as disk performance (from the container image) will be faster than storing each file separately on our cluster filesystems, which are set up to handle large files and parallel I/O. Using an `SIF` file instead of a sandbox image will also only use a quota file count amount of 1 instead of thousands (some images will typically contain thousands of files and directories).

Many Linux distribution package managers require root permissions in order to use them. This implies that Apptainer version 1.0.x and the older Singularity cannot be used on compute clusters to build images as a normal user. Should such occur, [submit a ticket](../../support/technical_support.md) asking for help to create that image or use a computer with Apptainer installed where you have root permissions.

Apptainer has a `--fakeroot` feature used to build and manipulate images. With versions prior to Apptainer 1.1, one wanting to use this feature on a cluster requires [submitting a ticket](../../support/technical_support.md) for a system administrator to consider adding that person so Apptainer's `--fakeroot` on a specific cluster, which may or not be possible. With Apptainer version 1.1, `--fakeroot` can be used without being formally added.

Know that some containers will not build successfully without using a `root` account to build them. These images cannot be built on our clusters.

If all you need is to use a Docker image as-is with Apptainer, often those images can be built and run without issues, *e.g.*, without any need to have additional permissions or explicitly use `--fakeroot`. Should you need to modify the image after creating it, you may need elevated permissions to successfully do this, *e.g.*, if the image's Linux distribution package manager requires such and you need to install a package using it. For this reason, the examples shown below assume one only needs to use a Docker image as-is.

## Building an SIF image

!!! note
    Please note and heed the advice concerning building images/overlays in section **[Building images and overlays](#building-images-or-overlays)** above.

To build an Apptainer SIF file image from Docker's latest available busybox image, use the `apptainer build` command:
```bash
apptainer build bb.sif docker://busybox
```

See the [Apptainer documentation](http://apptainer.org/docs) for more advanced aspects of building images.

## Building a sandbox image

!!! note
    Please note and heed the advice concerning building images/overlays in section **[Building images and overlays](#building-images-or-overlays)** above.

In order to build a "sandbox" directory instead of an `SIF` file instead of providing an `SIF` file name, instead provide `--sandbox DIR_NAME` or `-s DIR_NAME` where `DIR_NAME` is the name of the to-be-created-directory where you want your "sandbox" image. For example, if the `apptainer build` command to create an `SIF` file was:
```bash
apptainer build bb.sif docker://busybox
```
then change `bb.sif` to a directory name, *e.g.*, `bb.dir`, and prefix such with `--sandbox`:
```bash
apptainer build --sandbox bb.dir docker://busybox
```

Differences between building a "sandbox" image and a (normal) `SIF` file are:

*   the `SIF` file's image will be contained in a single file, compressed, and read-only,
*   the "sandbox" image will be placed in a directory, uncompressed, may contain thousands of files (depending on what exactly is in the image), and will be able to be read-write.

Within an account, using a "sandbox" directory will consume significant amounts of both disk space and file count quotas, thus, if read-write access to the underlying image is not normally required, you are advised to use an `SIF` instead. Additionally, using an `SIF` file will have higher disk access speeds to content contained within the `SIF` file.

# Example use cases

## Using Conda in Apptainer

!!! warning "Content from 'Using Conda in Apptainer' is missing"
    The content for this section, which would normally be transcluded from the MediaWiki page "Using Conda in Apptainer", is not available in the provided source. Please insert the relevant documentation here when available.

## Using GPUs in Apptainer

To use GPUs from within Apptainer ensure the software for the type(s) of GPUs being used in the container is installed inside the container.
If it such software is not installed then it is unlikely that your container's software will be able to use any GPUs.

To use NVIDIA GPUs from within Apptainer ensure that:
*   the command line option `--nv` appears after the `apptainer exec` or `apptainer run` command (before the .sif file)
*   the appropriate module(s) are loaded for the GPU, *e.g.*, `module load cuda/13.3`

To use AMD GPUs from within Apptainer ensure that:
*   the command line option `--rocm` appears after the `apptainer exec` or `apptainer run` command (before the .sif file)
*   the appropriate module(s) are loaded for the GPU.

## Using MPI in Apptainer

The easiest way to run an MPI application in Apptainer is to constrain it to a single node.
In that case, your job script will resemble one for a multithreaded job running on a single node, *e.g.*:

```bash
#!/bin/bash
#SBATCH --mem-per-cpu=1024M
#SBATCH --time=0-00:05
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
apptainer exec -c mpirun ./your-mpi-program args
```

Observe that `mpirun` is executed *inside* the container.

If you need to run an MPI application across nodes and you can do so without Apptainer, then we recommend not using Apptainer.
Running an MPI application within any container across nodes is error-prone.

Two methods are described the [Apptainer documentation](http://apptainer.org/docs/user/main/mpi.html) to run an MPI application with Apptainer across nodes:
1.  [The hybrid model](https://apptainer.org/docs/user/latest/mpi.html#hybrid-model).
2.  [The bind model](https://apptainer.org/docs/user/latest/mpi.html#bind-model).
Of these two, we recommend the hybrid model.

Beware of these issues:
*   The MPI version installed inside the container **must** be compatible with the MPI used on the host. This includes all needed fabrics, *etc.*
*   You must `module load` the version of MPI needed on the host *before* running the `apptainer` command that runs the MPI job.

Assuming your MPI job uses one thread per MPI rank (that is, it is not a "hybrid" MPI/shared-memory job), then you can specify the number of ranks as the number of tasks in your job script.
For example, if there are 4 ranks:

```bash
#!/bin/bash
#SBATCH --mem-per-cpu=3G
#SBATCH --time=0-00:05
#SBATCH --ntasks=4
module load openmpi apptainer
# This for loop ensures all special OMPI (OpenMPI) variables that are set in the host environment
# are properly exported for use inside the container:
for v in "${!OMPI_@}" ; do
    export APPTAINERENV_${v}=${!v}
done
mpirun -np ${SLURM_NTASKS} -- apptainer exec -e YOUR_CONTAINER.sif ./your-mpi-program args
```

The above example depends on the `OMPI` prefix used by Open MPI.
If you want to see which variables are set in the host environment by a given module,
run `module show` for that module, *e.g.*, `module show openmpi`.

If you encounter problems and you are using one of the Apptainer clean environment options,
*e.g.*, `-e`, `-c`, or `-C`, then try relaxing that option.
That is, if `-C` doesn't work, try `-c`, and if `-c` doesn't work, try `-e`.
Our tests indicate that you will probably need at least one of these clean environment options.

Bear in mind that a job script which works on a single node can easily fail when run on multiple nodes.
Consider forcing your job to run on more than one node while still in the testing phase.
For example, if your test has 4 tasks, then you can force the test to run on 2 or more nodes by specifying
`#SBATCH --nodes 2-4` in the job script.

## Creating an Apptainer container from a Dockerfile

!!! note
    **This section requires you to install and use Docker and Apptainer on a system where you have appropriate privileges. These instructions will *not* work on our compute clusters.**

Unfortunately, some instructions for packages only provide a `Dockerfile` without a container image. A `Dockerfile` contains the instructions necessary for the Docker software to build that container. Our clusters do not have the Docker software installed. That said, if you've access to a system with both Docker and Apptainer installed, and, sufficient access to Docker (*e.g.*, `sudo` or root access, or, you are in that system's `docker` group) and if needed Apptainer (*e.g.*, `sudo` or root access, or, you have `--fakeroot` access), then you can follow the instructions below to use Docker and then Apptainer to build an Apptainer image on that system.

!!! note
    Using Docker may fail if you are not in the `docker` group. Similarly, building some containers may fail with Apptainer without appropriate `sudo`, root, or `--fakeroot` permissions. It is your responsibility to ensure you've such access on the system you are running the commands below.

If one only has a Dockerfile and wishes to create an Apptainer image, run the following on a computer with Docker and Apptainer installed (where you've sufficient permissions):

```bash
docker build -f Dockerfile -t your-tag-name
docker save your-tag-name -o your-tarball-name.tar
docker image rm your-tag-name
apptainer build --fakeroot your-sif-name.sif docker-archive://your-tarball-name.tar
rm your-tarball-name.tar
```

where:

*   `your-tag-name` is a name you make up that will identify the container created in Docker
*   `your-tarball-name.tar` is a filename you create that Docker will save the generated content of the container to
*   `--fakeroot` is possibly optional (if so omit such); if `sudo` is needed instead then omit `--fakeroot` and prefix the line with `sudo`
*   `your-sif-name.sif` is the name of the Apptainer SIF file for the Apptainer container

After this is done, the SIF file is an Apptainer container for the `Dockerfile`. Transfer the SIF to the appropriate cluster(s) in order to use such.

!!! note
    It is possible that the Dockerfile pulled in more layers which means you will have to manually delete those additional layers by running:

```bash
docker images
```

followed by running `docker image rm ID` (where ID is the image ID output from the `docker images` command) in order to free up the disk space associated with those other image layers on the system you are using.

# Miscellaneous items

## Cleaning Apptainer's cache directory

Over time Apptainer's file cache will grow. To see where these files are run:

```bash
apptainer cache list
```

and to remove those files, run:

```bash
apptainer cache clean
```

## Changing Apptainer's default directories

You can override Apptainer's default temporary and cache directories by setting these environment variables before running `apptainer`:

*   `APPTAINER_CACHEDIR`: the directory where Apptainer will download and cache files
*   `APPTAINER_TMPDIR`: the directory where Apptainer will write temporary files including when building (squashfs) images

For example, to tell Apptainer to use your scratch space for its cache and temporary files (which is might be a better location), one might run:

```bash
mkdir -p /scratch/$USER/apptainer/{cache,tmp}
export APPTAINER_CACHEDIR="/scratch/$USER/apptainer/cache"
export APPTAINER_TMPDIR="/scratch/$USER/apptainer/tmp"
```

before running `apptainer`.