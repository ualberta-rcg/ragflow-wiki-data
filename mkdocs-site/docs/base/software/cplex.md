---
title: "CPLEX"
slug: "cplex"
lang: "base"

source_wiki_title: "CPLEX"
source_hash: "a4019465ab84d2aced24414474ff77c4"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:12:27.069296+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) is optimization software developed by IBM that is available to academic users via the [Academic Initiative](https://www.ibm.com/academic/home) program.

## Download
To use CPLEX on a Digital Research Alliance of Canada (the Alliance) cluster, [you must first register with IBM](https://www.ibm.com/academic/home) and then download your personal version of the software. If you have a choice between several architectures, choose *Linux x86-64*.

## Installation
The file is an executable archive that will perform the installation by asking a few questions. To execute the archive, run `bash ./cplex_studioXYZ.linux-x86.bin`.

To access the software, you can create personal modules. Modules are usually created and placed in a directory tree. For your modules to be found, you must modify the `$HOME/.bashrc` configuration file to point to the root of this tree, by adding the following line:

```bash
export MODULEPATH=$HOME/modulefiles:$MODULEPATH
```

Next, you need to create a directory structure to place your new CPLEX module:

```bash
mkdir -p $HOME/modulefiles/mycplex
```

In this directory, you will create a file (for example, `$HOME/modulefiles/mycplex/12.8.0`) named with the version number you previously downloaded (the XYZ) and containing the following:

```sh title="cplex_module.sh"
#%Module1.0####
##
## cplex
##
proc ModulesHelp { } {
        global cplexversion

        puts stderr "\tIBM ILOG cplex "
        puts stderr "\tThis module provides configuration for cplex, concert, cpoptimizer and opl"
}

module-whatis   "IBM ILOG cplex (cplex, concert, cpoptimizer, opl). This version doesn't ask for a licence file."

# for Tcl script use only
set     cplexversion        XYZ
set     studio_root          <root path of cplex>
set     cplexroot             $studio_root/cplex
set     concertroot           $studio_root/concert
set     oplroot               $studio_root/opl
set     cpoptimizerroot       $studio_root/cpoptimizer


set cplexbin x86-64_linux
set cplexlib $cplexbin/static_pic
set concertbin x86-64_linux
set concertlib $concertbin/static_pic
set oplbin x86-64_linux
set opllib $oplbin/static_pic
set cpoptimizerbin x86-64_linux
set cpoptimizerlib $cpoptimizerbin/static_pic


prepend-path    PATH         $cplexroot/bin/$cplexbin
prepend-path    PATH         $oplroot/bin/$oplbin
prepend-path    PATH         $cpoptimizerroot/bin/$cpoptimizerbin

prepend-path    CPATH        $cplexroot/include
prepend-path    CPATH        $concertroot/include
prepend-path    CPATH        $oplroot/include
prepend-path    CPATH        $cpoptimizerroot/include

prepend-path -d " "   CPATH_EXPANDED        -I$cplexroot/include
prepend-path -d " "  CPATH_EXPANDED        -I$concertroot/include
prepend-path -d " "   CPATH_EXPANDED        -I$oplroot/include
prepend-path -d " "   CPATH_EXPANDED        -I$cpoptimizerroot/include

prepend-path    LIBRARY_PATH $cplexroot/lib/$cplexlib
prepend-path    LIBRARY_PATH $concertroot/lib/$concertlib
prepend-path    LIBRARY_PATH $oplroot/lib/$opllib
prepend-path    LIBRARY_PATH $oplroot/bin/x86-64_linux/
prepend-path    LIBRARY_PATH $cpoptimizerroot/lib/$cpoptimizerlib

prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$cplexroot/lib/$cplexlib
prepend-path -d " "  LIBRARY_PATH_EXPANDED -L$concertroot/lib/$concertlib
prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$oplroot/lib/$opllib
prepend-path -d " "   LIBRARY_PATH_EXPANDED -L$oplroot/bin/x86-64_linux/
prepend-path -d " "   LIBRARY_PATH_EXPANDED  -L$cpoptimizerroot/lib/$cpoptimizerlib

prepend-path    LD_LIBRARY_PATH      $cplexroot/bin/$cplexbin
prepend-path    LD_LIBRARY_PATH      $oplroot/bin/$oplbin

prepend-path     CLASSPATH $cplexroot/lib/cplex.jar
prepend-path     MATLABPATH $cplexroot/matlab
prepend-path     STUDIO_ROOT $studio_root
```

Adjust the lines corresponding to the `cplexversion` and `studio_root` variables so that they have the correct values: the downloaded version and the path to this software (i.e., the path you specified when extracting the archive).

## Java
If you are using Java, you will have a few additional steps. First, in your `.bashrc` file, you can add the line,

```bash
export CLASSPATH=.
```
which will allow your code to be found during execution.

Next, you will need to modify the CPLEX dynamic library. Find this library in the installation directory tree, make a copy of it, and execute the command:

```bash
setrpaths.sh --path libcplex1280.so
```

!!! note "Memory Requirements"
    It is possible that during your compilation, you may encounter an error message due to a lack of memory. If this is the case, you will need to request an interactive compute node to perform the compilation. For example:

```bash
salloc --time=1:0:0 --ntasks=1 --mem-per-cpu=8G
```

## Python
After installing [CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) as indicated in the previous section, you must first load CPLEX:

```bash
module load mycplex/<version>
```

To install CPLEX packages such as `docplex`, we suggest doing so from a [virtual environment](python.md#create-and-use-a-virtual-environment).

Once the virtual environment is activated, you will need to navigate to the `$STUDIO_ROOT/python` directory, and then you can install the library with the command:

```bash
python setup.py install
```
The installation of CPLEX packages must be done on the head node, as they are not available on our [software stack](available_python_wheels.md).