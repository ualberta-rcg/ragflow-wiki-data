---
title: "BLAS and LAPACK"
slug: "blas_and_lapack"
lang: "base"

source_wiki_title: "BLAS and LAPACK"
source_hash: "a4fa3d3ed42fb32a0853fe840891d233"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:42:51.592948+00:00"

tags:
  []

keywords:
  - "GNU Compiler Collection"
  - "Intel compilers"
  - "-mkl=sequential"
  - "Intel MKL"
  - "BLAS/LAPACK"
  - "BLIS"
  - "FlexiBLAS"
  - "LAPACK"
  - "MKL Link Advisor"
  - "BLAS"
  - "compiler and linker options"
  - "-mkl compiler option"

questions:
  - "Why are there multiple implementations of the BLAS and LAPACK standards, and how does hardware affect their performance?"
  - "What is FlexiBLAS, and how does it solve the problem of testing different BLAS and LAPACK implementations across various hardware clusters?"
  - "How can a user compile their software against FlexiBLAS and subsequently change the active BLAS/LAPACK implementation at runtime?"
  - "What is the primary function of the `-mkl` compiler option?"
  - "How must the linking phase be handled differently when using a non-Intel compiler such as GCC?"
  - "What specific issues can the Intel MKL Link Advisor tool help developers resolve?"
  - "What is the default library used when FLEXIBLAS is left undefined on the clusters?"
  - "How should compiler and linker options be modified to use Intel MKL directly with Intel compilers?"
  - "What is the specific effect of using the `-mkl=sequential` flag during compilation?"
  - "What is the primary function of the `-mkl` compiler option?"
  - "How must the linking phase be handled differently when using a non-Intel compiler such as GCC?"
  - "What specific issues can the Intel MKL Link Advisor tool help developers resolve?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

BLAS (Basic Linear Algebra Subprograms) and LAPACK (Linear Algebra PACK) are two of the most commonly used libraries in advanced research computing. They are used for vector and matrix operations that are commonly found in a plethora of algorithms. **More importantly**, they are more than libraries, as they define a standard programming interface. A programming interface is a set of function definitions that can be called to accomplish specific computation, for example the dot product of two vectors of double precision numbers, or the matrix product of two hermitian matrices of complex numbers.

Beside the reference implementation done by Netlib, there exist a large number of implementations of these two standards. The performance of these implementations can vary widely depending on the hardware that is running them. For example, it is well established that the implementation provided by the [Intel Math Kernel Library (Intel MKL)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) performs best in most situations on Intel processors. That implementation is however proprietary, and in some situations, it is preferred to use the open-source implementation [OpenBLAS](https://github.com/xianyi/OpenBLAS). Another open-source implementation, named [BLIS](https://github.com/flame/blis), performs better on AMD processors. Previously, you may have known [gotoblas](https://www.tacc.utexas.edu/research-development/tacc-software/gotoblas2) and [ATLAS BLAS](https://github.com/math-atlas/math-atlas), but those projects are no longer maintained.

Unfortunately, testing which implementation performs best for a given code and given hardware usually requires recompiling software. This is a problem when trying to create a portable software environment that works on multiple clusters. This can be fixed by using [FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas). This is an abstraction layer that allows one to swap which implementation of BLAS and LAPACK is used at runtime, rather than at compile time.

## Which implementation should I use?
For the past few years, we have been recommending to use Intel MKL as a reference implementation. This recommendation was driven by the fact that we only had Intel processors in our clusters. This changed with the arrival of [Narval](../clusters/narval.md), which is built with AMD processors. We now recommend using FlexiBLAS when compiling code. Our FlexiBLAS module is configured such that Intel MKL will be used except when using AMD processors, in which case BLIS will be used. This arrangement will usually offer optimal performance.

## How do I compile against FlexiBLAS?
Unfortunately, FlexiBLAS is relatively new, and not all build systems will recognize it by default. This can generally be fixed by setting the linking options to use `-lflexiblas` for BLAS and for LAPACK. You will typically find these options in your Makefile, or be able to pass them as parameters to `configure` or `cmake`. Versions 3.19 and higher of CMake can find FlexiBLAS automatically; you must load one of the `cmake/3.20.1` or `cmake/3.21.4` modules to use such a version.

## How do I change which BLAS/LAPACK implementation is used at runtime?
The main benefit of using FlexiBLAS is the ability to change the implementation backend at runtime by setting the environment variable `FLEXIBLAS`. At the time of this writing, four implementations are available: `netlib`, `blis`, `imkl`, and `openblas`, but the full list can be obtained by running the command:

```bash
flexiblas list
```

!!! note
    On [Narval](../clusters/narval.md), we have set `FLEXIBLAS=blis` to use BLIS by default, while on other clusters, `FLEXIBLAS` is left undefined, which defaults to using Intel MKL.

## Using Intel MKL directly
Although we recommend using FlexiBLAS, it is still possible to use Intel MKL directly. If you are using one of the Intel compilers (e.g. `ifort`, `icc`, `icpc`) then the solution is to replace `-lblas` and `-llapack` in your compiler and linker options with either:

*   `-mkl=sequential`, which will not use internal threading, or
*   `-mkl` which will use internal threading.

This will ensure that the MKL implementation of BLAS/LAPACK is used. See [here](https://software.intel.com/en-us/mkl-linux-developer-guide-using-the-mkl-compiler-option) for more on the significance of `sequential` and other options.

If you are using a non-Intel compiler, for example the GNU Compiler Collection, then you will need to explicitly list the necessary MKL libraries during the link phase. Intel provides a tool called the [MKL Link Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) to help you find the correct compiler and linker options.

The same [MKL Link Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) tool is also useful if you receive "undefined reference" errors while using Intel compilers and `-mkl`.