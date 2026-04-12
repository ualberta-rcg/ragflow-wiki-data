---
title: "ParaView"
slug: "paraview"
lang: "base"

source_wiki_title: "ParaView"
source_hash: "f45a67d6a4759a8439cb25baa3e96f83"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:12:24.273551+00:00"

tags:
  - software

keywords:
  - "HPC clusters"
  - "Connection URL"
  - "large data processing"
  - "Alliance account"
  - "rendering"
  - "SSH port forwarding"
  - "OSMesa"
  - "cmake"
  - "render in parallel"
  - "interactive prompt"
  - "cluster resources"
  - "JupyterLab session"
  - "ParaView"
  - "Open OnDemand"
  - "remote parallel server"
  - "CPU-based rendering"
  - "Remote visualization"
  - "ParaView client"
  - "SWR drivers"
  - "interactivity"
  - "Virtual desktop"
  - "client-server visualization"
  - "LLVM"
  - "local port 11111"
  - "Add Server"
  - "GPU"
  - "cloud VM"
  - "multi-core visualization"
  - "parallel rendering"
  - "ParaView server"
  - "Single-core visualization"
  - "Client/Server"
  - "client-server setup"
  - "Parallel rendering"
  - "JupyterHub"
  - "cluster nodes"
  - "batch production"
  - "GPU rendering"
  - "pvserver"
  - "Multi-core visualization"
  - "Client-server mode"
  - "Offscreen rendering"
  - "JupyterLab"

questions:
  - "What are the three main workflows for remote visualization with ParaView on the HPC clusters?"
  - "Why does the documentation strongly advise against using the clusters' H100 GPUs for graphics rendering?"
  - "How do users initiate a small-scale interactive visualization session on clusters such as Fir, Rorqual, or Narval?"
  - "What are the initial configuration steps required to start a single-core JupyterLab session for ParaView?"
  - "Why is a client-server architecture necessary for true parallel rendering in ParaView?"
  - "How do you launch and connect the ParaView client and parallel server within a multi-core JupyterLab session?"
  - "What section should users on the Nibi or Trillium clusters navigate to for visualization options?"
  - "Which clusters allow users to launch a JupyterLab instance for single-core visualization?"
  - "What type of account is required to sign in to JupyterHub and access the Server Options?"
  - "What specific values must be configured for the Host, Port, and Startup Type settings?"
  - "How do you initiate the connection between the remote ParaView client and the remote parallel server within the JupyterLab session?"
  - "What is the final outcome or capability achieved after successfully connecting the client and server?"
  - "How do you configure and connect a single-core ParaView client to a parallel ParaView server within an Open OnDemand desktop session?"
  - "How can a user verify that their dataset is being rendered in parallel rather than in serial?"
  - "What are the critical version compatibility requirements and rendering threshold settings when setting up a remote client-server connection for large-scale interactive visualization?"
  - "How can a user estimate the appropriate number of CPU cores to allocate for rendering a dataset in ParaView?"
  - "What are the steps and specific commands required to launch the ParaView server on a cluster's compute node?"
  - "How do you configure SSH port forwarding to successfully connect a local ParaView client to the remote cluster server?"
  - "How does the file size threshold determine whether rendering is performed locally on the GPU or remotely?"
  - "What are the specific effects on interactivity and cluster resource usage when the rendering threshold is set to 0MB?"
  - "Why is it necessary to experiment with the threshold value to balance visualization speed and large data processing?"
  - "Why is it normal to see no output in the shell after executing the command?"
  - "How do you navigate the ParaView interface to begin adding a new server?"
  - "What specific configuration details need to be entered to connect ParaView to the local port 11111?"
  - "How do you configure and submit serial or parallel batch production jobs for off-screen visualization in ParaView?"
  - "What are the prerequisite steps and packages needed to set up a custom ParaView server on a cloud virtual machine?"
  - "Why must ParaView be compiled with OSMesa support on a cloud VM, and how does it handle rendering without a GPU?"
  - "What type of rendering setup is achieved for the ParaView server according to the text?"
  - "What are the differences between the llvmpipe and SWR drivers, and which one is recommended?"
  - "What specific software and version must be downloaded and compiled on the virtual machine?"
  - "What specific software components and dependencies must be compiled from source to build the ParaView server?"
  - "How is the ParaView server executed to ensure it uses offscreen rendering with the OSMesa backend?"
  - "What steps are required to establish a secure connection between a local ParaView client and the remote server?"
  - "What specific software components and dependencies must be compiled from source to build the ParaView server?"
  - "How is the ParaView server executed to ensure it uses offscreen rendering with the OSMesa backend?"
  - "What steps are required to establish a secure connection between a local ParaView client and the remote server?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Remote visualization with ParaView on the clusters

## Introduction

This page describes remote visualization of your dataset residing on one of the Alliance's HPC clusters. Your workflow will fall into one of these scenarios:

1.  If your dataset is only a few GBs (either the entire dataset, if no time dependency, or each timestep in a time-dependent simulation), you can visualize it interactively using a small number of CPU cores. In this workflow, you start a remote desktop session – through **[JupyterHub or Open OnDemand](../interactive/jupyterlab.md#launching-jupyterlab)**, depending on the cluster – and run ParaView interactively inside it. For more details, see the **["Small-scale interactive" tab](#workflows)**.
2.  If you want to interactively visualize a larger dataset, we recommend using a client-server setup, where the ParaView client runs on your computer, and the server runs in parallel inside a [Slurm job on the HPC cluster](../running-jobs/running_jobs.md). What counts as "large" depends on the cluster: on [Trillium](../clusters/trillium.md#node-characteristics), only whole-node jobs in multiples of 192 cores are allowed, so your dataset should be 50–100 GB to utilize all 192 cores efficiently. On other clusters ([Fir](fir.md#node-characteristics), [Narval](../clusters/narval.md), [Nibi](../clusters/nibi.md#node-characteristics), [Rorqual](../clusters/rorqual.md)), you can schedule by core, making it possible to visualize much smaller datasets – even on a single core – though using more cores in parallel speeds up rendering. This setup is more complex, so [JupyterHub or Open OnDemand](../interactive/jupyterlab.md#launching-jupyterlab) is generally recommended for smaller datasets before attempting a client-server configuration. For more details, see the **["Large-scale interactive" tab](#workflows)**.
3.  Ideally, all production visualizations – such as generating 1,000 frames for a movie – should be scripted and run as batch, off-screen jobs on the clusters, without opening interactive windows and rendering directly to files. The GUI workflows described in [the first or second tab](#workflows) should be considered as interactive steps to set up your visualization and save it as a ParaView Python script, which can then be executed as a [batch job on the cluster](../running-jobs/running_jobs.md), either in serial or, more commonly, in parallel. For more details, see the **["Batch production" tab](#workflows)**.

## Note on GPU rendering

!!! warning
    In all cases, please **do not use the clusters' H100 GPUs for visualization**, as they are not optimized for graphics rendering. While H100 cards can run OpenGL and Vulkan applications, they utilize only 2 of the 66 on-board thread controllers (this number may vary), resulting in roughly 3% GPU utilization. This not only leads to poor cluster utilization but also renders at speeds comparable to a mid-range laptop GPU. Note that [MIG instances](../programming/multi-instance_gpu.md#limitations) (static GPU partitions) cannot run graphics APIs such as OpenGL or Vulkan.

    If GPU rendering is absolutely necessary – although this should only be done in very specific corner cases – use [Nibi's AMD MI300A nodes](../clusters/nibi.md#node-characteristics) or older NVIDIA GPUs (e.g., T4) where available. We plan to benchmark and document all non-H100 rendering options on this page.

## Workflows

Please use the tabs below to select your visualization workflow type.

=== "Small-scale interactive"

This tab describes interactive visualization through remote desktop via JupyterHub and Open OnDemand. If you are on [Fir](fir.md), [Rorqual](../clusters/rorqual.md) or [Narval](../clusters/narval.md), please see one of the JupyterLab sections below. If you are on [Nibi](../clusters/nibi.md) or [Trillium](../clusters/trillium.md), please scroll down to one of the Open OnDemand sections below.

### Single-core visualization via JupyterLab

On [Fir](fir.md), [Rorqual](../clusters/rorqual.md), or [Narval](../clusters/narval.md), you can launch a JupyterLab instance through a portal:

1.  Sign in **[JupyterHub on one cluster](../interactive/jupyterhub.md#jupyterhub-on-clusters)** with your Alliance account.
2.  In the *[Server Options](../interactive/jupyterhub.md#server-options)* form:
    *   under *Account* select one of the CPU accounts (do not use GPUs!);
    *   under *GPU configuration* select **None**;
    *   under *Number of Cores*, select **1**;
    *   set the *Time* required for your JupyterLab session;
    *   set the *Memory* based on the maximum amount of data to be processed at a time;
    *   under *User interface* select **JupyterLab**;
    *   press the *Start* button. In the background, this will submit a Slurm job to the cluster.
3.  Wait about one minute for the job to start and for the JupyterLab dashboard to appear in your browser.

After this, you have two options. One is:

4.  On the left-hand side, under *[Software Modules](../interactive/jupyterlab.md#software-modules)*, load **paraview/6.0.0** module.
5.  A *[ParaView (VNC) button](../interactive/jupyterlab.md#paraview)* should appear, click on it -- this starts ParaView in a virtual desktop.
    *   If ParaView does not start automatically, a shortcut button should be on the virtual desktop. Click on the button and wait for ParaView to start.

Alternatively, in the JupyterLab dashboard you can:

4.  Click on your *[preferred Desktop button](../interactive/jupyterlab.md#desktop)* -- this opens a session in a virtual desktop.
5.  Inside this virtual desktop open a terminal (usually via *Applications > System ...*) and type the following:

    ```bash
    module load paraview/6.0.0
    paraview
    ```

    A ParaView window should come up, ready to be used.

### Multi-core visualization via JupyterLab

The ParaView GUI application itself is single-threaded and cannot directly use multiple cores. Some filters -- such as contouring, clipping, or resampling -- do support multithreading via VTK backends like TBB or OpenMP. For true parallel rendering, however, you need to connect the single-core ParaView client to a parallel ParaView server. Both can be launched within JupyterLab, as documented below.

Compared to the above procedure for *[Single-core visualization via JupyterLab](#single-core-visualization-via-jupyterlab)*, here are the key differences:

*   In JupyterHub *Server Options* settings, under *Number of Cores*, select your desired number of cores, let's say 4.
*   Under *Memory*, scale your request accordingly, e.g. for 4 cores select 14400 MB memory (which is 3600 MB per core).
*   When your JupyterLab session starts, inside it you will have access to 1 MPI task with 4 CPU cores.
*   Open your preferred virtual desktop, then a terminal inside it, and type:

    ```bash
    module load paraview/6.0.0
    ```

    and then

    ```bash
    mpirun --oversubscribe -np 4 pvserver
    ```

    ```text
    Waiting for client...
    Connection URL: cs://fc30669:11111
    Accepting connection(s): fc30669:11111
    ```

*   Next, inside the virtual desktop, open another terminal and type:

    ```bash
    module load paraview/6.0.0
    paraview
    ```

*   In ParaView GUI, click *Connect* button, then:
    1.  click *Add Server*;
    2.  select *Server Type* = **Client/Server**;
    3.  set *Host* = **localhost** (instead of the specific compute node name);
    4.  set *Port* = **11111** (as seen in the `Connection URL` of the above example);
    5.  select *Startup Type* = **Manual**.
*   Next, click *Connect* again to connect the remote ParaView client to the remote parallel server (both running inside the JupyterLab session).
*   Now you can load a dataset and render it in parallel on 4 cores.

To check that you are doing parallel rendering, you can colour your dataset by the `Process Id` variable (this variable is unavailable when running in serial).

### Single-core visualization via Open OnDemand

On [Nibi](../clusters/nibi.md) or [Trillium](../clusters/trillium.md), you can launch an Open OnDemand instance through a portal. Sign in to [https://ondemand.sharcnet.ca](https://ondemand.sharcnet.ca) (Nibi) or [https://ondemand.scinet.utoronto.ca](https://ondemand.scinet.utoronto.ca) (Trillium) with your Alliance account.

Once logged in, find "Desktop" in the menu. On Nibi you will find it under *Compute Nodes | Compute Desktop*. Specify a CPU-only Slurm account and other resources (1 CPU core) and click *Launch*. Wait for the job to start ("Starting" should change to "Running") and then click *Launch Compute Desktop*. Inside the desktop, open a terminal and type:

```bash
module load paraview/6.0.0
paraview
```

Load your dataset and start working on your visualization.

### Multi-core visualization via Open OnDemand

The ParaView GUI application itself is single-threaded and cannot directly use multiple cores. Some filters -- such as contouring, clipping, or resampling -- do support multithreading via VTK backends like TBB or OpenMP. For true parallel rendering, however, you need to connect the single-core ParaView client to a parallel ParaView server. Both can be launched within Open OnDemand, as documented below.

Follow the same steps as for Serial Open OnDemand above. When you specify resources, on Nibi's Open OnDemand you can ask up to 128GB memory and up to 8 cores.

Let's say, you specified 4 cores. Inside your Open OnDemand desktop session, you will have access to 1 MPI task with 4 CPU cores. Open a terminal inside your remote desktop and type:

```bash
module load paraview/6.0.0
```

and then

```bash
mpirun --oversubscribe -np 4 pvserver
```

```text
Waiting for client...
Connection URL: cs://g4.nibi.sharcnet:11111
Accepting connection(s): g4.nibi.sharcnet:11111
```

Next, still inside the remote desktop, start another terminal and type:

```bash
module load paraview/6.0.0
paraview
```

In ParaView GUI:
*   Click *Connect* button, then:
    1.  click *Add Server*;
    2.  select *Server Type* = **Client/Server**;
    3.  set *Host* = **localhost** (instead of the specific compute node name);
    4.  set *Port* = **11111** (as seen in the `Connection URL` of the above example);
    5.  select *Startup Type* = **Manual**.
*   Next, click *Connect* again to connect the remote ParaView client to the remote parallel server (both running inside the Compute Desktop session).
*   Now you can load a dataset and render it in parallel on 4 cores.

To check that you are doing parallel rendering, you can colour your dataset by the Process Id variable (this variable is unavailable when running in serial).

=== "Large-scale interactive"

This tab describes interactive client-server setup on all our HPC clusters ([Rorqual](../clusters/rorqual.md), [Nibi](../clusters/nibi.md), [Fir](fir.md), [Trillium](../clusters/trillium.md), and [Narval](../clusters/narval.md)), where a client runs on your computer, and the server runs on the remote cluster.

!!! note "Note 1"
    ParaView requires the same major version on the local client and the remote host; this prevents incompatibility that typically shows as a failed handshake when establishing the client-server connection. For example, to use ParaView server version 6.0.0 on the cluster, you need client version 6.0.x on your computer.

!!! note "Note 2"
    An important setting in ParaView's preferences is *Render View -> Remote/Parallel Rendering Options -> Remote Render Threshold.* If you set it to default (20MB) or similar, small rendering will be done on your computer's GPU, the rotation with a mouse will be fast, but anything modestly intensive (under 20MB) will be shipped to your computer and (depending on your connection) visualization might be slow. If you set it to 0MB, all rendering will be remote including rotation, so you will really be using the cluster resources for everything, which is good for large data processing but not so good for interactivity. Experiment with the threshold to find a suitable value.

You can do both rasterization and ray tracing on cluster CPUs, allocating as many cores as necessary to your rendering. Modern CPU-based libraries such as OSPRay and OpenSWR offer performance quite similar to GPU-based rendering. Also, since the ParaView server uses MPI for distributed-memory processing, for very large datasets one can do parallel rendering on a large number of CPU cores, either on a single node, or scattered across multiple nodes.

The easiest way to estimate the number of necessary cores is to look at the amount of memory that you think you will need for your rendering and divide it by ~3.5 GB/core. For example, a 40GB dataset (that you load into memory at once, e.g. a single timestep) would require at least 12 cores just to hold the data. Since software rendering is CPU-intensive, we do not recommend allocating more than 4GB/core. In addition, it is important to allocate some memory for filters and data processing (e.g. a structured to unstructured dataset conversion will increase your memory footprint by ~3X); depending on your workflow, you may want to start this rendering with 32 cores or 64 cores. If your ParaView server gets killed when processing these data, you will need to increase the number of cores.

!!! note "Note 3"
    On Trillium, you must schedule on whole nodes, i.e. in multiples of 192 cores. Therefore, the minimum example on Trillium will require 192 cores.

1.  First, install on your computer the same ParaView version as the one available on the cluster you will be using. Next, log into the cluster and start a parallel CPU interactive job.

    ```bash
    salloc --time=1:00:0 --ntasks=... --mem-per-cpu=3600 --account=def-someprof
    ```

    On Trillium -- assuming you are using one node for visualization -- this command will be:

    ```bash
    salloc --time=1:00:0 --ntasks=192 --account=def-someprof
    ```

    The job should automatically start on one of the CPU interactive nodes.

2.  At the prompt that is now running inside your job, load the ParaView module and start the server. Note that on Trillium you must load `StdEnv/2023` before attempting to load `paraview/6.0.0`.

    ```bash
    module load paraview/6.0.0
    ```

    and then

    ```bash
    srun pvserver --force-offscreen-rendering --opengl-window-backend OSMesa
    ```

    ```text
    Waiting for client...
    Connection URL: cs://fc30669:11111
    Accepting connection(s): fc30669:11111
    ```

    Wait for the server to be ready to accept client connection.

3.  Make a note of the node (in this case fc30669) and the port (usually 11111) and in another terminal on your computer (on Mac/Linux; in Windows use a terminal emulator) link the port 11111 on your computer and the same port on the compute node (make sure to use the correct compute node). Note that "fir" must be replaced by the actual cluster name: Rorqual, Fir, Trillium, or Narval. For Nibi, see the note below.

    ```bash
    ssh <username>@fir.alliancecan.ca -L 11111:fc30669:11111
    ```

    !!! note "Note 4"
        Nibi limits inter-node traffic to ssh (not using port 11111), and it has some additional network traffic blocking the initial client-server handshake. For Nibi, please use this command on your computer instead

        ```bash
        ssh -T -J <username>@nibi.alliancecan.ca -L 11111:localhost:11111 <username>@<nibi_compute_node>
        ```

        to route ssh port forwarding in two steps through the login node. The flag `-T` disables pseudo-terminal allocation and is important to facilitate the initial handshake, but it will also disable any interactive prompt in the shell so you will see no output after this command, and this is normal.

4.  Start ParaView on your computer, go to *File -> Connect* (or click on the green *Connect* button in the toolbar) and click on *Add Server.* You will need to point ParaView to your local port 11111, so you can do something like name = fir, server type = Client/Server, host = localhost, port = 11111; click *Configure*, select *Manual* and click *Save.*
    Once the remote is added to the configuration, simply select the server from the list and click on *Connect.* The first terminal window that read *Accepting connection* will now read *Client connected.*

5.  Open a file in ParaView (it will point you to the remote filesystem) and visualize it as usual.

To check that you are doing parallel rendering, you can colour your dataset by the Process Id variable (this variable is unavailable when running in serial).

=== "Batch production"

For large-scale and automated visualization, we strongly recommend switching from interactive client-server to off-screen batch visualization. ParaView supports Python scripting, so you can script your workflow and submit it as a regular, possibly parallel production job on a cluster. If you need any help with this, please contact [Technical support](../support/technical_support.md).

With serial rendering, your workflow should look like this:

```bash
module load paraview/6.0.0
sbatch serial.sh
```

: where a Slurm job submission script "serial.sh" might look like this:

```sh title="serial.sh"
#!/bin/bash
#SBATCH --time=3:0:0
#SBATCH --mem-per-cpu=3600
#SBATCH --account=def-someuser
pvbatch --force-offscreen-rendering --opengl-window-backend OSMesa script.py
```

With parallel rendering, your workflow should look like this:

```bash
module load paraview/6.0.0
sbatch distributed.sh
```

: where a Slurm job submission script "distributed.sh" might look like this:

```sh title="distributed.sh"
#!/bin/bash
#SBATCH --time=3:0:0
#SBATCH --mem-per-cpu=3600
#SBATCH --ntasks=4
#SBATCH --account=def-someuser
srun pvbatch --force-offscreen-rendering --opengl-window-backend OSMesa script.py
```

# Client-server visualization in a cloud VM

In this section, we describe the setup and workflow for running a ParaView server on a cloud VM. This is a less common approach and should be used only if you require a custom setup that is not supported by the cluster-installed ParaView.

## Prerequisites

The [Cloud Quick Start Guide](../cloud/cloud_quick_start.md) explains how to launch a new virtual machine (VM). Once you log into the VM, you will need to install some additional packages to be able to compile ParaView or VisIt. For example, on a CentOS VM you can type:

```bash
sudo yum install xauth wget gcc gcc-c++ ncurses-devel python-devel libxcb-devel
sudo yum install patch imake libxml2-python mesa-libGL mesa-libGL-devel
sudo yum install mesa-libGLU mesa-libGLU-devel bzip2 bzip2-libs libXt-devel zlib-devel flex byacc
sudo ln -s /usr/include/GL/glx.h /usr/local/include/GL/glx.h
```

If you have your own private-public SSH key pair (as opposed to the cloud key), you may want to copy the public key to the VM to simplify logins, by issuing the following command on your computer

```bash
cat ~/.ssh/id_rsa.pub | ssh -i ~/.ssh/cloudwestkey.pem centos@vm.ip.address 'cat >>.ssh/authorized_keys'
```

## Compiling with OSMesa

Since the VM does not have access to a GPU (most Arbutus VMs don't), we need to compile ParaView with OSMesa support so that it can do offscreen (software) rendering. The default configuration of OSMesa will enable OpenSWR (Intel's software rasterization library to run OpenGL). What you will end up with is a ParaView server that uses OSMesa for offscreen CPU-based rendering without X but with both `llvmpipe` (older and slower) and `SWR` (newer and faster) drivers built. We recommend using SWR.

Back on the VM, compile `cmake`:

```bash
wget https://cmake.org/files/v4.1/cmake-4.1.1.tar.gz
tar -xf cmake-4.1.1.tar.gz && cd cmake-4.1.1
./bootstrap
make
sudo make install
```

Next, compile `llvm`:

```bash
cd
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-21.1.0/LLVM-21.1.0-Linux-X64.tar.xz
# unpack and cd there
mkdir -p build && cd build
cmake \
 -DCMAKE_BUILD_TYPE=Release \
 -DLLVM_BUILD_LLVM_DYLIB=ON \
 -DLLVM_ENABLE_RTTI=ON \
 -DLLVM_INSTALL_UTILS=ON \
 -DLLVM_TARGETS_TO_BUILD:STRING=X86 \
 ..
make
sudo make install
```

Next, compile Mesa with OSMesa:

```bash
cd
wget https://archive.mesa3d.org/mesa-25.2.3.tar.xz
# unpack and cd there
./configure \
 --enable-opengl --disable-gles1 --disable-gles2 \
 --disable-va --disable-xvmc --disable-vdpau \
 --enable-shared-glapi \
 --disable-texture-float \
 --enable-gallium-llvm --enable-llvm-shared-libs \
 --with-gallium-drivers=swrast,swr \
 --disable-dri \
 --disable-egl --disable-gbm \
 --disable-glx \
 --disable-osmesa --enable-gallium-osmesa
make
sudo make install
```

Next, compile the ParaView server:

```bash
cd
wget https://www.paraview.org/files/v6.0/ParaView-v6.0.0.tar.gz
# unpack and cd there
mkdir -p build && cd build
cmake \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_INSTALL_PREFIX=/home/centos/paraview \
 -DPARAVIEW_USE_MPI=OFF \
 -DPARAVIEW_ENABLE_PYTHON=ON \
 -DPARAVIEW_BUILD_QT_GUI=OFF \
 -DVTK_OPENGL_HAS_OSMESA=ON \
 -DVTK_USE_OFFSCREEN=ON \
 -DVTK_USE_X=OFF \
 ..
make
make install
```

## Client-server mode

You are now ready to start ParaView server on the VM with SWR rendering:

```bash
./paraview/bin/pvserver --force-offscreen-rendering --opengl-window-backend OSMesa
```

Back on your computer, organize an SSH tunnel from the local port 11111 to the VM's port 11111:

```bash
ssh centos@vm.ip.address -L 11111:localhost:11111
```

Finally, start the ParaView client on your computer and connect to `localhost:11111`. If successful, you should be able to open files on the remote VM. During rendering in the console you should see the message *SWR detected AVX2.*