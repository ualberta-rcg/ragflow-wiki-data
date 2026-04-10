---
title: "Fortran"
tags:
  []

keywords:
  []
---

Fortran is a compiled programming language with a long history available on Compute Canada's servers thanks to the compilers that are installed (<tt>gfortran</tt> and <tt>ifort</tt>). In general you will get much better performance using a compiled language and we encourage you to write your programs in these languages, which could be Fortran, C or C++.

==Useful compiler options== 

Most contemporary Fortran compilers have a variety of options that can be very helpful during the debugging phase of code development.
* <tt>-fcheck=all</tt> for the gfortran compiler and <tt>-check</tt> for the ifort compiler check array bounds and alert for disassociated pointers and uninitialized variables;
* <tt>-fpe0</tt> (ifort) causes the application to halt for floating point exceptions such as division by zero or the square root of a negative, instead of simply generating a NaN and letting the application run; 
* during testing, you should use <tt>-O0</tt> to disable optimizations and <tt>-g</tt> to add debugging symbols.    

==Numerical linear algebra== 

Note that modern versions of Fortran, i.e. from Fortran 90 on, include built-in functions to handle basic linear algebra operations like multiplication involving matrices and vectors (<tt>matmul</tt> and <tt>dot_product</tt>) and tranposition of matrices (<tt>transpose</tt>). You should use these or the system-provided BLAS/LAPACK libraries and never attempt to write your own methods for such operations, except as an educational exercise. The BLAS matrix-matrix multiplication routine can be up to 100 times faster than a naive implementation involving three nested loops.    

==Segmentation faults== 

An error that is frequently seen with a Fortran program comes from interface problems. These problems surface if a pointer, a dynamically allocated array or even a function pointer is passed as an argument to a subroutine. There are no compile-time problems, but when the program is ran you see for example the following message:
; **forrtl: severe (174): SIGSEGV, segmentation fault occurred**
To correct this problem, you should ensure that the interface of the subroutine is explicitly defined. This can be done in Fortran using the INTERFACE command. Then the compiler can construct the interface and the segmentation faults are fixed.

When the argument is an allocatable array, you should replace the following code:

by this code:

The same principle applies when the argument is a function pointer. Consider, for example, the following code: 

To avoid segmentation faults you should replace the above code by the following: