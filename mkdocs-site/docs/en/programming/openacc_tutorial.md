---
title: "OpenACC Tutorial/en"
slug: "openacc_tutorial"
lang: "en"

source_wiki_title: "OpenACC Tutorial/en"
source_hash: "eafdb1f4ea8530bdf9ffcd704306c059"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:20:45.961128+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

This tutorial is strongly inspired by the OpenACC Bootcamp session presented at [GPU Technology Conference 2016](http://www.gputechconf.com/).

OpenACC is an application programming interface (API) for porting code onto accelerators such as GPUs and coprocessors. It has been developed by Cray, CAPS, NVidia, and PGI. Like in [OpenMP](openmp.md), the programmer annotates C, C++, or Fortran code to identify portions that should be parallelized by the compiler.

A self-paced course on this topic is available from SHARCNET: [Introduction to GPU Programming](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

!!! info "Prerequisites for this tutorial"
    This tutorial uses OpenACC to accelerate C, C++, or Fortran code. A working knowledge of one of these languages is therefore required to gain the most benefit out of it.

!!! info "Getting ready"
    This tutorial is based on examples. You can download all of the examples in this [Github repository](https://github.com/calculquebec/cq-formation-openacc).

## Lesson plan
* [Introduction](openacc-tutorial-introduction.md)
* [Gathering a profile and getting compiler information](openacc-tutorial-profiling.md)
* [Expressing parallelism with OpenACC directives](openacc-tutorial-adding-directives.md)
* [Expressing data movement](openacc-tutorial-data-movement.md)
* [Optimizing loops](openacc-tutorial-optimizing-loops.md)

## External references
Here are some useful external references:
* [OpenACC Programming and Best Practices Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
* [OpenACC API 2.7 Reference Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
* [Getting Started with OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
* [PGI Compiler](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
* [PG Profiler](http://www.pgroup.com/resources/pgprof-quickstart.htm)
* [NVIDIA Visual Profiler](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)