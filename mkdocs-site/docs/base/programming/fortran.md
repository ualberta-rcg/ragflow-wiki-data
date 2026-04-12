---
title: "Fortran"
slug: "fortran"
lang: "base"

source_wiki_title: "Fortran"
source_hash: "e55cc0774823b7bd38e54a7ca0f04d7c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:05:59.255384+00:00"

tags:
  []

keywords:
  - "interface"
  - "Fortran"
  - "boundInf"
  - "interface pointer"
  - "linear algebra"
  - "FunctionToIntegrate"
  - "explicit interface"
  - "boundSup"
  - "computeIntegral"
  - "segmentation faults"
  - "compiler options"

questions:
  - "What are the recommended compiler options for debugging Fortran code and handling floating-point exceptions?"
  - "Why should developers use built-in functions or BLAS/LAPACK libraries for linear algebra operations instead of writing custom methods?"
  - "How can the INTERFACE command be used to prevent segmentation faults when passing pointers or allocatable arrays to subroutines?"
  - "How does the provided Fortran code use an interface block to pass a function as an argument to another procedure?"
  - "What are the specific roles and return values of the `FunctionToIntegrate` and `computeIntegral` functions in this snippet?"
  - "How are the integration boundaries, `boundInf` and `boundSup`, declared and intended to be used within the integration function?"
  - "What is the cause of the segmentation fault in the initial Fortran code snippet?"
  - "How does the updated code in `interface_pointer.f90` resolve the segmentation fault issue?"
  - "What role does the `external` keyword play when defining the functions and variables in the provided examples?"
  - "How does the provided Fortran code use an interface block to pass a function as an argument to another procedure?"
  - "What are the specific roles and return values of the `FunctionToIntegrate` and `computeIntegral` functions in this snippet?"
  - "How are the integration boundaries, `boundInf` and `boundSup`, declared and intended to be used within the integration function?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Fortran is a compiled programming language with a long history available on Compute Canada's servers thanks to the compilers that are installed (`gfortran` and `ifort`). In general, you will get much better performance using a compiled language and we encourage you to write your programs in these languages, which could be Fortran, C or C++.

## Useful compiler options

!!! tip "Compiler Options for Debugging"
    Most contemporary Fortran compilers have a variety of options that can be very helpful during the debugging phase of code development.

    *   `-fcheck=all` for the gfortran compiler and `-check` for the ifort compiler check array bounds and alert for disassociated pointers and uninitialized variables;
    *   `-fpe0` (ifort) causes the application to halt for floating-point exceptions such as division by zero or the square root of a negative, instead of simply generating a NaN and letting the application run;
    *   during testing, you should use `-O0` to disable optimizations and `-g` to add debugging symbols.

## Numerical linear algebra

!!! note "Numerical Linear Algebra Best Practices"
    Modern versions of Fortran, i.e. from Fortran 90 on, include built-in functions to handle basic linear algebra operations like multiplication involving matrices and vectors (`matmul` and `dot_product`) and transposition of matrices (`transpose`). You should use these or the system-provided BLAS/LAPACK libraries and never attempt to write your own methods for such operations, except as an educational exercise. The BLAS matrix-matrix multiplication routine can be up to 100 times faster than a naive implementation involving three nested loops.

## Segmentation faults

An error that is frequently seen with a Fortran program comes from interface problems. These problems surface if a pointer, a dynamically allocated array or even a function pointer is passed as an argument to a subroutine. There are no compile-time problems, but when the program is run you see for example the following message:
**forrtl: severe (174): SIGSEGV, segmentation fault occurred**
To correct this problem, you should ensure that the interface of the subroutine is explicitly defined. This can be done in Fortran using the `INTERFACE` command. Then the compiler can construct the interface and the segmentation faults are fixed.

When the argument is an allocatable array, you should replace the following code:

```fortran linenums="1" title="error_allocate.f90"
Program Eigenvalue
implicit none

integer                       :: ierr
integer                       :: ntot
real, dimension(:,:), pointer :: matrix

read(5,*) ntot
ierr = genmat( ntot, matrix )

call Compute_Eigenvalue( ntot, matrix )

deallocate( matrix )
end
```

by this code:

```fortran linenums="1" title="interface_allocate.f90"
Program Eigenvalue
implicit none

integer                       :: ierr
integer                       :: ntot
real, dimension(:,:), pointer :: matrix

interface
    function genmat( ntot, matrix )
    implicit none
    integer                       :: genmat
    integer, intent(in)           :: ntot
    real, dimension(:,:), pointer :: matrix
    end function genmat
end interface

read(5,*) ntot
ierr = genmat( ntot, matrix )

call Compute_Eigenvalue( ntot, matrix )

deallocate( matrix )
end
```

The same principle applies when the argument is a function pointer. Consider, for example, the following code:

```fortran linenums="1" title="error_=pointer.f90"
Program AreaUnderTheCurve
implicit none

real,parameter :: boundInf = 0.
real,parameter :: boundSup = 1.
real           :: area
real, external :: computeIntegral
real, external :: FunctionToIntegrate

area = computeIntegral( FunctionToIntegrate, boundInf, boundSup )

end

function FunctionToIntegrate( x )
implicit none

real             :: FunctionToIntegrate
real, intent(in) :: x

FunctionToIntegrate = x

end function FunctionToIntegrate

function computeIntegral( func, boundInf, boundSup )
implicit none

real, external   :: func
real, intent(in) :: boundInf, boundSup

...
```

To avoid segmentation faults you should replace the above code by the following:

```fortran linenums="1" title="interface_pointer.f90"
Program Eigenvalue
implicit none

real,parameter :: boundInf = 0.
real,parameter :: boundSup = 1.
real           :: area
real, external :: computeIntegral

interface
    function FunctionToIntegrate( x )
    implicit none
    real             :: FunctionToIntegrate
    real, intent(in) :: x
    end function FunctionToIntegrate
end interface

area = computeIntegral( FunctionToIntegrate, boundInf, boundSup )

end


function FunctionToIntegrate( x )
implicit none

real             :: FunctionToIntegrate
real, intent(in) :: x

FunctionToIntegrate = x

end function FunctionToIntegrate


function computeIntegral( func, boundInf, boundSup )
implicit none

real, intent(in) :: boundInf, boundSup

interface
    function func( x )
    implicit none
    real             :: func
    real, intent(in) :: x
    end function func
end interface

...