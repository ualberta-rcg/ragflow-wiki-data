---
title: "Valgrind"
slug: "valgrind"
lang: "base"

source_wiki_title: "Valgrind"
source_hash: "305b97a7f833f93633b06ba69d121939"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:38:44.985840+00:00"

tags:
  - software

keywords:
  - "bounds of an array"
  - "Invalid pointer access"
  - "AVX-512 limitations"
  - "Memory leak"
  - "Out of bound errors"
  - "segmentation fault"
  - "memory leaks"
  - "memory access problem"
  - "Error message"
  - "debugging tool"
  - "memcheck"
  - "Uninitialized variables"
  - "Valgrind"
  - "error messages"

questions:
  - "What is Valgrind primarily used for, and what specific types of memory errors can it detect?"
  - "How must an application be prepared and compiled before it can be effectively analyzed by Valgrind?"
  - "What is the AVX-512 limitation in current versions of Valgrind, and how can users circumvent this issue?"
  - "What does the error message for a memory leak look like and when is it displayed during program execution?"
  - "How does the system report an invalid pointer access or an out-of-bounds memory error?"
  - "What specific error message indicates that a program's conditional jump or move depends on an uninitialized variable?"
  - "Why do memory access problems, such as reading outside array bounds, often go undetected in smaller size problems?"
  - "How does Valgrind assist developers in identifying memory access violations?"
  - "What specific types of error messages does Valgrind produce when detecting code problems?"
  - "What does the error message for a memory leak look like and when is it displayed during program execution?"
  - "How does the system report an invalid pointer access or an out-of-bounds memory error?"
  - "What specific error message indicates that a program's conditional jump or move depends on an uninitialized variable?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Valgrind

[Valgrind](http://valgrind.org/) is a powerful debugging tool to detect bad memory usage. It can detect memory leaks, but also access to unallocated or deallocated memory, multiple deallocation or other bad memory usage. If your program ends with a *segmentation fault*, *broken pipe* or *bus error*, you most likely have such a problem in your code. Valgrind is installed on Alliance clusters as part of the base software distribution, so there is no need to load a module to use it.

## AVX-512 Limitations
Note that current versions of Valgrind are unable to handle the [AVX-512](https://en.wikipedia.org/wiki/AVX-512) instructions used on the latest Intel and AMD processors, producing an error message like the following:

```text
vex amd64->IR: unhandled instruction bytes: 0x62 0xF1 0xFE 0x8 0x6F 0x8B 0xE8 0xFF 0xFF 0xFF
vex amd64->IR:   REX=0 REX.W=0 REX.R=0 REX.X=0 REX.B=0
vex amd64->IR:   VEX=0 VEX.L=0 VEX.nVVVV=0x0 ESC=NONE
vex amd64->IR:   PFX.66=0 PFX.F2=0 PFX.F3=0
==35839== valgrind: Unrecognised instruction at address 0x4e68448.
==35839==    at 0x4E68448: if_posix_open (in /cvmfs/soft.computecanada.ca/easybuild/software/2020/avx512/Compiler/gcc9/openmpi/4.0.3/lib/libopen-pal.so.40.20.3)
==35839==    by 0x4E2C44A: mca_base_framework_components_open (in /cvmfs/soft.computecanada.ca/easybuild/software/2020/avx512/Compiler/gcc9/openmpi/4.0.3/lib/libopen-pal.so.40.20.3)
...
```

!!! warning "AVX-512 Workaround"
    On all of our current clusters except Narval, the default environment uses these AVX-512 instructions. You can circumvent this problem by first loading the AVX-2 environment:

    ```bash
    module load arch/avx2
    ```

    and then recompiling your application from scratch to ensure the binary doesn't contain any such instructions.

## Preparing your application
To get useful information from [Valgrind](http://valgrind.org/), you first need to compile your code with debugging information enabled. With most compilers, you do so by adding a `-g` option during compilation.

!!! note "Optimizations and False Positives"
    Some aggressive optimizations may yield false errors in Valgrind if they result in unsupported operations, which may occur in certain mathematical libraries. Since you don't want to diagnose errors in those libraries, but rather errors in your own code, you should compile and link your code against non-optimized versions of the libraries (such as the Netlib implementation of BLAS/LAPACK) that do not use those operations. This is of course only to diagnose issues; when the time comes to run real simulations, you should link against optimized libraries.

## Using Valgrind
Once your code is compiled with the proper options, you execute it within Valgrind with the following command:

```bash
valgrind --tool=memcheck --leak-check=yes --show-reachable=yes ./your_program
```

For more information about Valgrind, we recommend [this page](http://www.cprogramming.com/debugging/valgrind.html).

### Words of wisdom
!!! tip "Important Considerations"
    * When you run your code in Valgrind, your application is executed within a virtual machine that validates every memory access. It will therefore run **much slower** than usual. Choose the size of the problem to test with caution, much smaller than what you would usually run.
    * You do not need to run the exact same problem that results in a segmentation fault to detect memory issues in your code. Very frequently, memory access problems, such as reading data outside of the bounds of an array, will go undetected for small size problems, but will cause a segmentation fault for large ones. Valgrind will detect even the slightest access outside of the bounds of an array.

### Some typical error messages
Here are some problems that Valgrind will help you detect, and the error messages that it will produce.

#### Memory leak
The error message for a memory leak will be given at the end of the program execution, and will look like this:

```text
==2116== 100 bytes in 1 blocks are definitely lost in loss record 1 of 1
==2116==    at 0x1B900DD0: malloc (vg_replace_malloc.c:131)
==2116==    by 0x804840F: main (in /home/cprogram/example1)
```

#### Invalid pointer access/out of bound errors
If you attempt to read or write to an unallocated pointer or outside of the allocated memory, the error message will look like this:

```text
==9814==  Invalid write of size 1
==9814==    at 0x804841E: main (example2.c:6)
==9814==  Address 0x1BA3607A is 0 bytes after a block of size 10 alloc'd
==9814==    at 0x1B900DD0: malloc (vg_replace_malloc.c:131)
==9814==    by 0x804840F: main (example2.c:5)
```

#### Usage of uninitialized variables
If you use an uninitialized variable, you will get an error message such as:

```text
==17943== Conditional jump or move depends on uninitialised value(s)
==17943==    at 0x804840A: main (example3.c:6)