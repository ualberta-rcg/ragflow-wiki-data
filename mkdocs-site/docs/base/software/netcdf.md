---
title: "NetCDF"
slug: "netcdf"
lang: "base"

source_wiki_title: "NetCDF"
source_hash: "a31f1e663a7cc5b46da870f42b6093db"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:43:28.845013+00:00"

tags:
  - software

keywords:
  - "two-dimensional variable"
  - "gcc"
  - "environment modules"
  - "PnetCDF"
  - "netcdf-mpi"
  - "ncdump"
  - "utilities"
  - "parallel I/O"
  - "ncgen"
  - "NetCDF"
  - "example program"
  - "Network Common Data Form"
  - "scientific data"

questions:
  - "What is NetCDF and what are its primary functions in handling scientific data?"
  - "What are the main strengths and weaknesses of using NetCDF compared to other formats like HDF5?"
  - "How do you load and link the appropriate NetCDF environment modules for different programming languages like C and Fortran?"
  - "How do the ncdump and ncgen utilities work together to transform NetCDF data representations?"
  - "What modifications can be made to a NetCDF file's storage settings using the nccopy utility?"
  - "What are the key features that distinguish the PnetCDF library from the standard NetCDF library?"
  - "What commands are required to load the NetCDF module and compile the example C program?"
  - "Where can users find the tutorial link demonstrating the use of NetCDF?"
  - "What are the specific contents and dimensions of the NetCDF file created by the example program?"
  - "How do the ncdump and ncgen utilities work together to transform NetCDF data representations?"
  - "What modifications can be made to a NetCDF file's storage settings using the nccopy utility?"
  - "What are the key features that distinguish the PnetCDF library from the standard NetCDF library?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## General

NetCDF (Network Common Data Form) is:
* an interface for array-oriented data access, and
* a library that provides an implementation of the interface.
The NetCDF library also defines a machine-independent format for representing scientific data. Together, the interface, library, and format support the creation, access, and sharing of scientific data.

!!! info "NetCDF Version Compatibility"
There were significant changes to the library with the release of version 4.0. NetCDF 4.x is backwards compatible - it can read files produced by an earlier version but the opposite isn't true. Since 4.0 was released in 2008, we will not discuss earlier versions here.

* Project web site : [https://www.unidata.ucar.edu/software/netcdf](https://www.unidata.ucar.edu/software/netcdf)
* Manual: [https://www.unidata.ucar.edu/software/netcdf/docs](https://www.unidata.ucar.edu/software/netcdf/docs)
* Downloads: [https://www.unidata.ucar.edu/downloads/netcdf/index.jsp](https://www.unidata.ucar.edu/downloads/netcdf/index.jsp)
* FAQ: [https://www.unidata.ucar.edu/software/netcdf/docs/faq.html](https://www.unidata.ucar.edu/software/netcdf/docs/faq.html)

## Strengths
* The data are independent of the processor architecture ([endianness](https://en.wikipedia.org/wiki/Endianness)).
* The data are structured in a way that keeps track of all the pertinent information, e.g. physical units.
* NetCDF4 can read and write in parallel, if it is built using a parallel version of [HDF5](hdf5.md).
* Data can be compressed as it is written.
* A simpler interface than HDF5.
* It's free software for most platforms.

## Weak points
* The Python interface doesn't support parallelism (version 1.0.5)
* Certain files produced with [HDF5](hdf5.md) cannot be read using NetCDF

## Quickstart guide
This section summarizes configuration details.

### Environment modules

The following [modules](../programming/utiliser_des_modules.md) providing NetCDF are available on our clusters via CVMFS:
* **netcdf**
    * for linking with programs containing C instructions only
* **netcdf-c++**
    * for linking with programs containing both C and C++ instructions
* **netcdf-fortran**
    * for linking with programs containing Fortran instructions

There is also a set of NetCDF modules compiled with [MPI](mpi.md) support for parallel I/O:
* **netcdf-mpi**
    * for linking with programs containing C instructions and calling MPI libraries
* **netcdf-c++-mpi**
    * for linking with programs containing both C and C++ instructions and calling MPI
* **netcdf-fortran-mpi**
    * for linking with programs containing Fortran instructions and calling MPI

Run `module avail netcdf` to see what versions are currently available with the compiler and MPI modules you have loaded. For a comprehensive list of NetCDF modules, run `module -r spider '.*netcdf.*'`.

Use `module load netcdf/version` to set your environment to use your chosen version. For example, to load the NetCDF version 4.1.3 C-based library, do:

```bash
module load netcdf/4.1.3
```

### Submission scripts
Please refer to the page "[Running jobs](../running-jobs/running_jobs.md)" for examples of job scripts for the Slurm workload manager. We recommend you include the `module load ...` command in your job script.

### Linking code to NetCDF libraries
Below are a few examples showing how to link NetCDF libraries to C and Fortran code:

#### Serial NetCDF
For C code,
```bash
module load netcdf/4.4.1
gcc example.c -lnetcdf
```

For Fortran code, notice that two libraries are required and their order matters:
```bash
module load gcc netcdf-fortran
gfortran example.f90 -I$EBROOTNETCDFMINFORTRAN/include -lnetcdf -lnetcdff
```

#### Parallel NetCDF
For C code which calls MPI,
```bash
module load netcdf-mpi
gcc example.c -lnetcdf
```

#### Example
An example demonstrating the use of the NetCDF can be found at the following [link](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf-tutorial/simple_005fxy_005fwr_002ec.html#simple_005fxy_005fwr_002ec). The example program creates a NetCDF file containing a single two-dimensional variable called "data", and labels the two dimensions "x" and "y".

To compile the example:
```bash
module load netcdf
gcc ex_netcdf4.c -lnetcdf
```

### NetCDF utilities
There are several utilities that read or write files in different formats.
* ncdump
    * "The ncdump tool generates the CDL text representation of a netCDF dataset on standard output, optionally excluding some or all of the variable data in the output. The output from ncdump is intended to be acceptable as input to ncgen. Thus ncdump and ncgen can be used as inverses to transform data representation between binary and text representation." See [ncdump](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf/ncdump.html) on the UCAR site for more.
* ncgen
    * This utility takes an input file in CDL format and creates a binary netCDF file. It is the reverse of ncdump. See [ncgen](https://www.unidata.ucar.edu/software/netcdf/netcdf-4/newdocs/netcdf/ncgen.html#ncgen) for more.
* nccopy
    * Copies a netCDF file and can change binary format, chunk sizes, compression, and other storage settings. See [nccopy](https://www.unidata.ucar.edu/software/netcdf/workshops/2011/utilities/Nccopy.html) for more.

There are also utilities `nc-config` and `nf-config` to help you find the correct compilation and linking commands. More on them can be found [here](https://www.unidata.ucar.edu/software/netcdf/workshops/2012/utilities/Nc-config.html).

## PnetCDF

PnetCDF is another library for reading and writing NetCDF-format files. It uses different procedure names than NetCDF and provides non-blocking procedures. See the [PnetCDF web site](https://trac.mcs.anl.gov/projects/parallel-netcdf) for a detailed discussion.