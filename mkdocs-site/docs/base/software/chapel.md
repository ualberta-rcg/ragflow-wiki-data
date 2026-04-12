---
title: "Chapel"
slug: "chapel"
lang: "base"

source_wiki_title: "Chapel"
source_hash: "7f51c376deb5325e4b370585c1aed230"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:14:09.926521+00:00"

tags:
  - software

keywords:
  - "single-locale"
  - "NVIDIA GPU support"
  - "Slurm submission script"
  - "chapel-ucx-cuda"
  - "parallel programming"
  - "HPC"
  - "Interactive jobs"
  - "Compute node"
  - "InfiniBand clusters"
  - "Chapel"
  - "multi-locale"
  - "Multi-locale Chapel"
  - "GPU support"

questions:
  - "What are the two main styles of parallel programming available in Chapel?"
  - "What are the primary advantages and current limitations of using Chapel for high-performance computing?"
  - "How do the module requirements and execution commands differ when running Chapel in a single-locale versus a multi-locale environment?"
  - "What module is required to enable NVIDIA GPU support for multi-locale Chapel on InfiniBand clusters?"
  - "How do you compile and run Chapel GPU code interactively after starting a job on an allocated compute node?"
  - "What is the recommended approach for submitting production jobs instead of using an interactive session?"
  - "How do you compile and execute Chapel code from the prompt during an interactive job?"
  - "What is the recommended procedure for submitting production jobs to the cluster?"
  - "What specific hardware acceleration is supported for multi-locale Chapel according to the text?"
  - "What module is required to enable NVIDIA GPU support for multi-locale Chapel on InfiniBand clusters?"
  - "How do you compile and run Chapel GPU code interactively after starting a job on an allocated compute node?"
  - "What is the recommended approach for submitting production jobs instead of using an interactive session?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Chapel is a general-purpose, compiled, high-level parallel programming language with built-in abstractions for shared- and distributed-memory parallelism. There are two styles of parallel programming in Chapel: (1) **task parallelism**, where parallelism is driven by *programmer-specified tasks*, and (2) **data parallelism**, where parallelism is driven by applying the same computation on subsets of data elements, which may be in the shared memory of a single node, or distributed over multiple nodes.

These high-level abstractions make Chapel ideal for learning parallel programming for a novice HPC user. Chapel is incredibly intuitive, striving to merge the ease-of-use of [Python](python.md) and the performance of traditional compiled languages such as [C](../programming/c.md) and [Fortran](../programming/fortran.md). Parallel blocks that typically take tens of lines of [MPI](mpi.md) code can be expressed in only a few lines of Chapel code. Chapel is open source and can run on any Unix-like operating system, with hardware support from laptops to large HPC systems.

Chapel has a relatively small user base, so many libraries that exist for [C](../programming/c.md), [C++](cpp.md), [Fortran](../programming/fortran.md) have not yet been implemented in Chapel. Hopefully, that will change in coming years if Chapel adoption continues to gain momentum in the HPC community.

For more information, please watch our [Chapel webinars](https://westgrid.github.io/trainingMaterials/programming/#chapel).

## Single-locale Chapel

Single-locale (single node; shared-memory only) Chapel on our general-purpose clusters is provided by the module `chapel-multicore`. You can use `salloc` to test Chapel codes either in serial:

```bash
module load gcc/12.3 chapel-multicore/2.4.0
salloc --time=0:30:0 --ntasks=1 --mem-per-cpu=3600 --account=def-someprof
chpl test.chpl -o test
./test
```

or on multiple cores on the same node:

```bash
module load gcc/12.3 chapel-multicore/2.4.0
salloc --time=0:30:0 --ntasks=1 --cpus-per-task=3 --mem-per-cpu=3600 --account=def-someprof
chpl test.chpl -o test
./test
```

For production jobs, please write a [job submission script](../running-jobs/running_jobs.md) and submit it with `sbatch`.

## Multi-locale Chapel

Multi-locale (multiple nodes; hybrid shared- and distributed-memory) Chapel on our InfiniBand clusters is provided by the module `chapel-ucx`.

Consider the following Chapel code printing basic information about the nodes available inside your job:

!!! example "probeLocales.chpl"

    ```chapel
    use MemDiagnostics;
    for loc in Locales do
      on loc {
        writeln("locale #", here.id, "...");
        writeln("  ...is named: ", here.name);
        writeln("  ...has ", here.numPUs(), " processor cores");
        writeln("  ...has ", here.physicalMemory(unit=MemUnits.GB, retType=real), " GB of memory");
        writeln("  ...has ", here.maxTaskPar, " maximum parallelism");
      }
    ```

To run this code on an InfiniBand cluster, you need to load the `chapel-ucx` module:
```bash
module load gcc/12.3 chapel-ucx/2.4.0
salloc --time=0:30:0 --nodes=4 --cpus-per-task=3 --mem-per-cpu=3500 --account=def-someprof
```

Once the [interactive job](../running-jobs/running_jobs.md#interactive-jobs) starts, you can compile and run your code from the prompt on the first allocated compute node:
```bash
chpl --fast probeLocales.chpl
./probeLocales -nl 4
```

For production jobs, please write a [Slurm submission script](../running-jobs/running_jobs.md) and submit your job with `sbatch` instead.

## Multi-locale Chapel with NVIDIA GPU support

To enable GPU support, please use the module `chapel-ucx-cuda`. It adds NVIDIA GPU support to multi-locale Chapel on our InfiniBand clusters.

Consider the following basic Chapel GPU code:

!!! example "probeGPU.chpl"

    ```chapel
    use GpuDiagnostics;
    startGpuDiagnostics();
    writeln("Locales: ", Locales);
    writeln("Current locale: ", here, " named ", here.name, " with ", here.maxTaskPar, " CPU cores",
    	" and ", here.gpus.size, " GPUs");
    // same code can run on GPU or CPU
    var operateOn =
      if here.gpus.size > 0 then here.gpus[0]   // use the first GPU
      else here;                                // use the CPU
    writeln("operateOn: ", operateOn);
    on operateOn {
      var A : [1..10] int;
      @assertOnGpu foreach a in A do // thread parallelism on a CPU or a GPU
        a += 1;
      writeln(A);
    }
    stopGpuDiagnostics();
    writeln(getGpuDiagnostics());
    ```

To run this code on an InfiniBand cluster, you need to load the `chapel-ucx-cuda` module:
```bash
module load gcc/12.3 cuda/12.2 chapel-ucx-cuda/2.4.0
salloc --time=0:30:0 --mem-per-cpu=3500 --gpus-per-node=1 --account=def-someprof
```

Once the [interactive job](../running-jobs/running_jobs.md#interactive-jobs) starts, you can compile and run your code from the prompt on the allocated compute node:
```bash
chpl --fast probeGPU.chpl
./probeGPU -nl 1
```

For production jobs, please write a [Slurm submission script](../running-jobs/running_jobs.md) and submit your job with `sbatch` instead.