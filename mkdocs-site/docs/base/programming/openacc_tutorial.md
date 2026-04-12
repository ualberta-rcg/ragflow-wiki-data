---
title: "OpenACC Tutorial"
slug: "openacc_tutorial"
lang: "base"

source_wiki_title: "OpenACC Tutorial"
source_hash: "0b8447d55582af9bb1418fe7321b549c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:51:29.287530+00:00"

tags:
  []

keywords:
  - "GPU programming"
  - "OpenACC"
  - "parallelization"
  - "directives"
  - "profiling"

questions:
  - "What is OpenACC and how does it enable programmers to parallelize their code on accelerators?"
  - "What programming languages are required as prerequisites, and where can the example files for the tutorial be downloaded?"
  - "What are the specific topics and skills covered in the tutorial's lesson plan?"
  - "What is OpenACC and how does it enable programmers to parallelize their code on accelerators?"
  - "What programming languages are required as prerequisites, and where can the example files for the tutorial be downloaded?"
  - "What are the specific topics and skills covered in the tutorial's lesson plan?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

This tutorial is strongly inspired by the OpenACC Bootcamp session presented at [GPU Technology Conference 2016](http://www.gputechconf.com/).

OpenACC is an application programming interface (API) for porting code onto accelerators such as GPU and coprocessors. It has been developed by Cray, CAPS, NVidia and PGI. Like in [OpenMP](openmp.md), the programmer annotates C, C++ or Fortran code to identify portions that should be parallelized by the compiler.

A self-paced course on this topic is available from SHARCNET: [Introduction to GPU Programming](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

!!! note "Prerequisites for this tutorial"
    This tutorial uses OpenACC to accelerate C, C++ or Fortran code. A working knowledge of one of these languages is therefore required to gain the most benefit out of it.

!!! info "Getting ready"
    This tutorial is based on examples. You can download all of the examples in this [Github repository](https://github.com/calculquebec/cq-formation-openacc).

## Lesson plan
* [Introduction](openacc_tutorial_-_introduction.md)
* [Gathering a profile and getting compiler information](openacc_tutorial_-_profiling.md)
* [Expressing parallelism with OpenACC directives](openacc_tutorial_-_adding_directives.md)
* [Expressing data movement](openacc_tutorial_-_data_movement.md)
* [Optimizing loops](openacc_tutorial_-_optimizing_loops.md)

## External references
Here are some useful external references:
* [OpenACC Programming and Best Practices Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
* [OpenACC API 2.7 Reference Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
* [Getting Started with OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
* [PGI Compiler](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
* [PG Profiler](http://www.pgroup.com/resources/pgprof-quickstart.htm)
* [NVIDIA Visual Profiler](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)