---
title: "Debugging and profiling/en"
slug: "debugging_and_profiling"
lang: "en"

source_wiki_title: "Debugging and profiling/en"
source_hash: "2a3b1d52ad7f02dfd4d570881351d93a"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:29:54.175683+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

An important step in the software development process, particularly for compiled languages like Fortran and C/C++, concerns the use of a program called a debugger to detect and identify the origin of runtime errors (e.g., memory leaks, floating point exceptions and so forth) so that they can be eliminated. Once the program's correctness is assured, a further step is profiling the software. This involves the use of another software tool, a profiler, to determine what percentage of the total execution time each section of the source code is responsible for when run with a representative test case. A profiler can give information like how many times a particular function is called, which other functions are calling it, and how many milliseconds of time each invocation of this function costs on average.

## Debugging on a cluster

!!! warning
    Debugging sessions should be conducted using an interactive job **and not run on a login node**. You have multiple options:

*   With the Slurm command `salloc ...`. See **[Interactive jobs](../running-jobs/running_jobs.md#interactive-jobs)** for all the details.
*   With a [JupyterLab](../interactive/jupyterlab.md) session. See the [JupyterLab](../interactive/jupyterlab.md) page for the **[connection details](../interactive/jupyterlab.md#launching-jupyterlab)** and the **[prebuilt applications](../interactive/jupyterlab.md#prebuilt-applications)**.
*   With a remote desktop session for visual profiling tools. See **[this section of JupyterLab](../interactive/jupyterlab.md#desktop)** or one of the two **[Quickstart guides for Open OnDemand](../interactive/open_ondemand.md#introduction)** for the instructions.

## Debugging and profiling tools

Our national clusters offer a variety of debugging and profiling tools, both command line and those with a graphical user interface, whose use requires an X11 connection.

### GNU debugger (gdb)

Please see the [GDB page](gdb.md).

### PGI debugger (pgdb)

Please see the [Pgdbg page](https://docs.alliancecan.ca/wiki/Pgdbg).

### ARM debugger (ddt)

Please see the [ARM software page](../software/arm_software.md).

### GNU profiler (gprof)

Please see the [Gprof page](gprof.md).

### Scalasca profiler (scalasca, scorep, cube)

Scalasca is an open source, GUI-driven parallel profiling tool set. It is currently available for **gcc 9.3.0** and **OpenMPI 4.0.3**, with AVX2 or AVX512 architecture. Its environment can be loaded with:

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scalasca
```

The current version is **2.5**. More information can be found in the 2.x user guide, which contains workflow examples [here](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.5/docs/manual/).

### PGI profiler (pgprof)

Please see the [Pgprof page](../software/pgprof.md).

### Nvidia command-line profiler (nvprof)

Please see the nvprof page.

### Valgrind

Please see the [Valgrind page](../software/valgrind.md).

## External references

*   [Introduction to (Parallel) Performance](https://docs.scinet.utoronto.ca/index.php/Introduction_To_Performance) from SciNet
*   [Code profiling on Graham](https://www.youtube.com/watch?v=YsF5KMr9uEQ), video, 54 minutes.