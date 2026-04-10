---
title: "Chapel/en"
tags:
  - software

keywords:
  []
---

Chapel is a general-purpose, compiled, high-level parallel programming language with built-in abstractions for shared- and distributed-memory parallelism. There are two styles of parallel programming in Chapel: (1) <b>task parallelism</b>, where parallelism is driven by <i>programmer-specified tasks</i>, and (2) <b>data parallelism</b>, where parallelism is driven by applying the same computation on subsets of data elements, which may be in the shared memory of a single node, or distributed over multiple nodes.

These high-level abstractions make Chapel ideal for learning parallel programming for a novice HPC user. Chapel is incredibly intuitive, striving to merge the ease-of-use of [Python](python.md) and the performance of traditional compiled languages such as [C](c.md) and [Fortran](fortran.md). Parallel blocks that typically take tens of lines of [MPI](mpi.md) code can be expressed in only a few lines of Chapel code. Chapel is open source and can run on any Unix-like operating system, with hardware support from laptops to large HPC systems.

Chapel has a relatively small user base, so many libraries that exist for [C](c.md), [C++](c++.md), [Fortran](fortran.md) have not yet been implemented in Chapel. Hopefully, that will change in coming years if Chapel adoption continues to gain momentum in the HPC community.

For more information, please watch our [Chapel webinars](https://westgrid.github.io/trainingMaterials/programming/#chapel).

## Single-locale Chapel 

Single-locale (single node; shared-memory only) Chapel on our general-purpose clusters is provided by the module `chapel-multicore`. You can use `salloc` to test Chapel codes either in serial:

```bash

```
0:30:0 --ntasks1 --mem-per-cpu3600 --accountdef-someprof
|chpl test.chpl -o test
|./test
}}
or on multiple cores on the same node:

```bash

```
0:30:0 --ntasks1 --cpus-per-task3 --mem-per-cpu3600 --accountdef-someprof
|chpl test.chpl -o test
|./test
}}
For production jobs, please write a [job submission script](running_jobs.md) and submit it with `sbatch`.

## Multi-locale Chapel 

Multi-locale (multiple nodes; hybrid shared- and distributed-memory) Chapel on our InfiniBand clusters is provided by the module `chapel-ucx`.

Consider the following Chapel code printing basic information about the nodes available inside your job:
{{
File
  |name=probeLocales.chpl
  |lang="chapel"
  |contents=
use MemDiagnostics;
for loc in Locales do
  on loc {
    writeln("locale #", here.id, "...");
    writeln("  ...is named: ", here.name);
    writeln("  ...has ", here.numPUs(), " processor cores");
    writeln("  ...has ", here.physicalMemory(unit=MemUnits.GB, retType=real), " GB of memory");
    writeln("  ...has ", here.maxTaskPar, " maximum parallelism");
  }
}}

To run this code on an InfiniBand cluster, you need to load the `chapel-ucx` module:

```bash

```
0:30:0 --nodes4 --cpus-per-task3 --mem-per-cpu3500 --accountdef-someprof
}}

Once the [interactive job](running_jobs#interactive_jobs.md) starts, you can compile and run your code from the prompt on the first allocated compute node:

```bash
./probeLocales -nl 4
```

For production jobs, please write a [Slurm submission script](running_jobs.md) and submit your job with `sbatch` instead.

## Multi-locale Chapel with NVIDIA GPU support 

To enable GPU support, please use the module `chapel-ucx-cuda`. It adds NVIDIA GPU support to multi-locale Chapel on our InfiniBand clusters.

Consider the following basic Chapel GPU code:
{{
File
  |name=probeGPU.chpl
  |lang="chapel"
  |contents=
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
}}

To run this code on an InfiniBand cluster, you need to load the `chapel-ucx-cuda` module:

```bash

```
0:30:0 --mem-per-cpu3500 --gpus-per-node1 --accountdef-someprof
}}

Once the [interactive job](running_jobs#interactive_jobs.md) starts, you can compile and run your code from the prompt on the allocated compute node:

```bash
./probeGPU -nl 1
```

For production jobs, please write a [Slurm submission script](running_jobs.md) and submit your job with `sbatch` instead.