---
title: "Gprof/en"
slug: "gprof"
lang: "en"

source_wiki_title: "Gprof/en"
source_hash: "e2d74474609162aa4267a789bb8a4fa2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:45:21.853302+00:00"

tags:
  []

keywords:
  - "GNU Profiler"
  - "gprof"
  - "gmon.out"
  - "GNU compiler"
  - "profiling data"

questions:
  - "What is the GNU Profiler (gprof) and how does it function to create profiling statistics?"
  - "Why must the `-pg` option be included during the compilation step when preparing an application for gprof?"
  - "What is the process for executing the compiled code and extracting the final profiling data from the generated `gmon.out` file?"
  - "What is the GNU Profiler (gprof) and how does it function to create profiling statistics?"
  - "Why must the `-pg` option be included during the compilation step when preparing an application for gprof?"
  - "What is the process for executing the compiled code and extracting the final profiling data from the generated `gmon.out` file?"

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

To get useful information from [gprof](https://sourceware.org/binutils/docs/gprof/), you first need to compile your code with debugging information enabled.

!!! warning "Compiling with `-pg`"
    With the GNU compilers, you do so by adding the `-pg` option to the compilation command. This option tells the compiler to generate extra code to write profile information suitable for the analysis. Without this option, no call-graph data will be gathered and you may get the following error:

    ```text
    gprof: gmon.out file is missing call-graph data
    ```

### Executing your code

Once your code has been compiled with the proper options, you then execute it:

```bash
/path/to/your/executable arg1 arg2
```

You should run your code the same way as you would without gprof profiling; the execution line does not change.
Once the binary has been executed and finished without any errors, a new file `gmon.out` is created in the current working directory. Note that if your code changes the current directory, `gmon.out` will be created in the new working directory, insofar as your program has sufficient permissions to do so.

### Getting the profiling data

In this step the gprof tool is executed with the binary name and the above mentioned `gmon.out` as argument; the analysis file is created with all the desired profiling information.

```bash
gprof /path/to/your/executable gmon.out > analysis.txt