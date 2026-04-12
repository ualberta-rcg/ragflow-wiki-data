---
title: "Gprof"
slug: "gprof"
lang: "base"

source_wiki_title: "Gprof"
source_hash: "5cc2a3593ccf36ad4f21d0c46f2c4ecb"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:45:13.216473+00:00"

tags:
  []

keywords:
  - "GNU Profiler (gprof)"
  - "profiling"
  - "-pg option"
  - "gmon.out"
  - "GNU compiler"

questions:
  - "What is the GNU Profiler (gprof) and how does it collect statistics on a program?"
  - "What specific compiler option must be used to ensure gprof can gather call-graph data without errors?"
  - "How do you generate the final profiling analysis text file after the program has successfully executed and created the gmon.out file?"
  - "What is the GNU Profiler (gprof) and how does it collect statistics on a program?"
  - "What specific compiler option must be used to ensure gprof can gather call-graph data without errors?"
  - "How do you generate the final profiling analysis text file after the program has successfully executed and created the gmon.out file?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# GNU Profiler (gprof)

## What is gprof?
[gprof](https://sourceware.org/binutils/docs/gprof/) is a profiling software which collects information and compiles statistics on your code. Generally, it searches for functions and subroutines in your program and inserts timing instructions for each one. Executing such a modified program creates a raw data file which can be interpreted by gprof and turned into profiling statistics.

[gprof](https://sourceware.org/binutils/docs/gprof/) comes with the GNU compiler suite and is available with the `gcc` module on our clusters.

## Preparing your application
### Loading the GNU compiler
Load the appropriate GNU compiler. For example, for GCC:

```bash
module load gcc/7.3.0
```

### Compiling your code
To get useful information from [gprof](https://sourceware.org/binutils/docs/gprof/), you first need to compile your code with debugging information enabled. With the GNU compilers, you do so by adding the `-pg` option to the compilation command. This option tells the compiler to generate extra code to write profile information suitable for the analysis. Without this option, no call-graph data will be gathered and you may get the following error:

```
gprof: gmon.out file is missing call-graph data
```

### Executing your code
Once your code has been compiled with the proper options, you then execute it:

```bash
/path/to/your/executable arg1 arg2
```

You should run your code the same way as you would without gprof profiling; the execution line does not change.
Once the binary has been executed and finished without any errors, a new file `gmon.out` is created in the current working directory.

!!! note
    If your code changes the current directory, `gmon.out` will be created in the new working directory, insofar as your program has sufficient permissions to do so.

### Getting the profiling data
In this step the gprof tool is executed with the binary name and the above mentioned `gmon.out` as argument; the analysis file is created with all the desired profiling information.

```bash
gprof /path/to/your/executable gmon.out > analysis.txt