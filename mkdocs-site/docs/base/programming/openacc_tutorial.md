---
title: "OpenACC Tutorial"
tags:
  []

keywords:
  []
---

This tutorial is strongly inspired from the OpenACC Bootcamp session presented at [GPU Technology Conference 2016](http://www.gputechconf.com/). 

OpenACC is an application programming interface (API) for porting code onto accelerators such as GPU and coprocessors. It has been developed by Cray, CAPS, NVidia and PGI. Like in [OpenMP](openmp.md), the programmer annotates C, C++ or Fortran code to identify portions that should be parallelized by the compiler. 

A self-paced course on this topic is available from SHARCNET: [Introduction to GPU Programming](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

== Lesson plan == 
* [Introduction](openacc-tutorial---introduction.md)
* [Gathering a profile and getting compiler information](openacc-tutorial---profiling.md)
* [Expressing parallelism with OpenACC directives](openacc-tutorial---adding-directives.md)
* [Expressing data movement](openacc-tutorial---data-movement.md)
* [Optimizing loops](openacc-tutorial---optimizing-loops.md)

== External references == 
Here are some useful external references: 
* [OpenACC Programming and Best Practices Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
* [OpenACC API 2.7 Reference Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
* [Getting Started with OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
* [PGI Compiler](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
* [PG Profiler](http://www.pgroup.com/resources/pgprof-quickstart.htm)
* [NVIDIA Visual Profiler](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)