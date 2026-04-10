---
title: "ARM software"
slug: "arm_software"
lang: "base"

source_wiki_title: "ARM software"
source_hash: "5fb2a58e9523499965bd7db3f3a64e25"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T01:35:30.320097+00:00"

tags:
  - software

keywords:
  - "MAP"
  - "CUDA"
  - "parallel debugger"
  - "manual launch"
  - "X11 forwarding"
  - "Linaro DDT"
  - "VNC"
  - "ddt command"
  - "directory permissions"
  - "CUDA driver"
  - "terminate allocation"
  - "DDT"
  - "ALLINEA_FORCE_CUDA_VERSION"
  - "MPI"

questions:
  - "What are Linaro DDT and MAP, and what are the current license limitations for using these tools on the cluster?"
  - "What is the step-by-step process for debugging CPU-only code interactively, including the necessary workaround for the OpenMPI message queue compatibility issue?"
  - "How should a user allocate resources and troubleshoot potential OpenMPI or CUDA version mismatches when debugging GPU code?"
  - "Why is it recommended to run the DDT interface under VNC instead of using X11 forwarding?"
  - "What are the specific steps to manually launch a job in DDT when your VNC session is located on a login node or VDI node?"
  - "How can you resolve X11 connection issues by modifying the permissions of your home directory?"
  - "How do you execute the DDT command for a specific code path?"
  - "What steps should be taken if DDT indicates a mismatch between the CUDA driver and toolkit versions?"
  - "How do you properly terminate the allocation after finishing your tasks?"
  - "Why is it recommended to run the DDT interface under VNC instead of using X11 forwarding?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: true
---

# Introduction

[Linaro DDT](https://www.linaroforge.com/linaro-ddt) (formerly known as ARM DDT) is a powerful commercial parallel debugger with a graphical user interface. It can be used to debug serial, MPI, multi-threaded, and CUDA programs, or any combination of the above, written in C, C++, and FORTRAN. [MAP](https://www.linaroforge.com/linaro-map)—an efficient parallel profiler—is another very useful tool from Linaro (formerly ARM).

The following modules are available on Nibi and Trillium (requires StdEnv module loaded):
*   ddt-cpu, for CPU debugging and profiling;
*   ddt-gpu, for GPU or mixed CPU/GPU debugging.

As this is a GUI application, log in using `ssh -Y`, and use an [SSH client](ssh.md) like [MobaXTerm](connecting-with-mobaxterm.md) (Windows) or [XQuartz](https://www.xquartz.org/) (Mac) to ensure proper X11 tunnelling.

Both DDT and MAP are normally used interactively through their GUI, which is normally accomplished using the `salloc` command (see below for details). MAP can also be used non-interactively, in which case it can be submitted to the scheduler with the `sbatch` command.

The current license limits the use of DDT/MAP to a maximum of 64 CPU cores across all users at any given time, while DDT-GPU is limited to 8 GPUs.

# Usage
## CPU-only code, no GPUs

1.  Allocate the node or nodes on which to do the debugging or profiling. This will open a shell session on the allocated node.

    ```bash
    salloc --x11 --time=0-1:00 --mem-per-cpu=4G --ntasks=4
    ```

2.  Load the appropriate module, for example

    ```bash
    module load ddt-cpu
    ```

3.  Run the ddt or map command.

    ```bash
    ddt path/to/code
    map path/to/code
    ```

    !!! note
        Make sure the MPI implementation is the default OpenMPI in the DDT/MAP application window, before pressing the **Run** button. If this is not the case, press the **Change** button next to the **Implementation:** string, and select the correct option from the drop-down menu. Also, specify the desired number of CPU cores in this window.

4.  When done, exit the shell to terminate the allocation.

!!! warning "OpenMPI Message Queue Compatibility Issue"
    The current versions of DDT and OpenMPI have a compatibility issue which breaks the important feature of DDT - displaying message queues (available from the "Tools" drop down menu). There is a workaround: before running DDT, you have to execute the following command:

    ```bash
    export OMPI_MCA_pml=ob1
    ```

    Be aware that the above workaround can make your MPI code run slower, so only use this trick when debugging.

## CUDA code

1.  Allocate the node or nodes on which to do the debugging or profiling with `salloc`. This will open a shell session on the allocated node.

    ```bash
    salloc --x11 --time=0-1:00 --mem-per-cpu=4G --ntasks=1 --gres=gpu:1
    ```

2.  Load the appropriate module, for example

    ```bash
    module load ddt-gpu
    ```

    !!! tip "OpenMPI/DDT-GPU Version Mismatch"
        This may fail with a suggestion to load an older version of OpenMPI first. In this case, reload the OpenMPI module with the suggested command, and then reload the ddt-gpu module.

    ```bash
    module load openmpi/2.0.2
    module load ddt-gpu
    ```

3.  Ensure a cuda module is loaded.

    ```bash
    module load cuda
    ```

4.  Run the ddt command.

    ```bash
    ddt path/to/code
    ```

    !!! warning "CUDA Driver/Toolkit Version Mismatch"
        If DDT complains about the mismatch between the CUDA driver and toolkit version, execute the following command and then run DDT again (use the version in this command), e.g.

    ```bash
    export ALLINEA_FORCE_CUDA_VERSION=10.1
    ```

5.  When done, exit the shell to terminate the allocation.

## Using VNC to fix the lag

The instructions above use X11 forwarding. X11 is very sensitive to packet latency. As a result, unless you happen to be on the same campus as the computer cluster, the ddt interface will likely be laggy and frustrating to use. This can be fixed by running ddt under VNC.

To do this, follow the directions on our [VNC page](vnc.md) to set up a VNC session. If your VNC session is on the compute node, then you can directly start your program under ddt as above. If your VNC session is on the login node or you are using the graham vdi node, then you need to manually launch the job as follows. From the ddt startup screen:

*   pick the **manually launch backend yourself** job start option,
*   enter the appropriate information for your job and press the **listen** button, and
*   press the **help** button to the right of **waiting for you to start the job...**.

This will then give you the command you need to run to start your job. Allocate a job on the cluster and start your program as directed. An example of doing this would be (where `$USER` is your username and `$PROGRAM ...` is the command to start your program):

```bash
[name@cluster-login:~]$ salloc ...
[name@cluster-node:~]$ /cvmfs/restricted.computecanada.ca/easybuild/software/2020/Core/allinea/20.2/bin/forge-client --ddtsessionfile /home/$USER/.allinea/session/gra-vdi3-1 $PROGRAM ...
```

# Known issues

!!! warning "X11 Forwarding Issues and Directory Permissions"
    If you are experiencing issues with getting X11 to work, change permissions on your home directory so that only you have access.

First, check (and record if needed) current permissions with

```bash
ls -ld /home/$USER
```

The output should begin with:

```
drwx------
```

If some of the dashes are replaced by letters, that means your group and other users have read, write (unlikely), or execute permissions on your directory.

This command will work to remove read and execute permissions for group and other users:

```bash
chmod go-rx /home/$USER
```

After you are done using DDT, you can if you like restore permissions to what they were (assuming you recorded them). More information on how to do this can be found on page [Sharing data](sharing-data.md).

# See also
*   ["Debugging your code with DDT"](https://youtu.be/Q8HwLg22BpY), video, 55 minutes.
*   [A short DDT tutorial.](parallel-debugging-with-ddt.md)