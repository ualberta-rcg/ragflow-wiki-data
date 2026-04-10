---
title: "Fortran"
slug: "fortran"
lang: "base"

source_wiki_title: "Fortran"
source_hash: "e55cc0774823b7bd38e54a7ca0f04d7c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:22:51.841122+00:00"

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

Fortran is a compiled programming language with a long history available on Compute Canada's servers thanks to the compilers that are installed (`gfortran` and `ifort`). In general you will get much better performance using a compiled language and we encourage you to write your programs in these languages, which could be Fortran, C or C++.

## Useful compiler options

!!! tip
    Most contemporary Fortran compilers have a variety of options that can be very helpful during the debugging phase of code development.
    *   `-fcheck=all` for the gfortran compiler and `-check` for the ifort compiler check array bounds and alert for disassociated pointers and uninitialized variables;
    *   `-fpe0` (ifort) causes the application to halt for floating point exceptions such as division by zero or the square root of a negative, instead of simply generating a NaN and letting the application run;
    *   during testing, you should use `-O0` to disable optimizations and `-g` to add debugging symbols.

## Numerical linear algebra

!!! note
    Modern versions of Fortran, i.e. from Fortran 90 on, include built-in functions to handle basic linear algebra operations like multiplication involving matrices and vectors (`matmul` and `dot_product`) and transposition of matrices (`transpose`). You should use these or the system-provided BLAS/LAPACK libraries and never attempt to write your own methods for such operations, except as an educational exercise. The BLAS matrix-matrix multiplication routine can be up to 100 times faster than a naive implementation involving three nested loops.

## Segmentation faults

!!! warning
    An error that is frequently seen with a Fortran program comes from interface problems. These problems surface if a pointer, a dynamically allocated array or even a function pointer is passed as an argument to a subroutine. There are no compile-time problems, but when the program is run you see for example the following message:

    ```
    forrtl: severe (174): SIGSEGV, segmentation fault occurred
    ```

    To correct this problem, you should ensure that the interface of the subroutine is explicitly defined. This can be done in Fortran using the `INTERFACE` command. Then the compiler can construct the interface and the segmentation faults are fixed.

When the argument is an allocatable array, you should replace the following code:

```fortran title="error_allocate.f90"
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

```fortran title="interface_allocate.f90"
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

```fortran title="error_=pointer.f90"
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

```fortran title="interface_pointer.f90"
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