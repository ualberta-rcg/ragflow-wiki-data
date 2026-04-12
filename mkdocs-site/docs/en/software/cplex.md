---
title: "CPLEX/en"
slug: "cplex"
lang: "en"

source_wiki_title: "CPLEX/en"
source_hash: "dfc7d459ace2f4f3d07721d301af838e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:03:32.062771+00:00"

tags:
  - software

keywords:
  - "personal module"
  - "CLASSPATH"
  - "CPLEX"
  - "prepend-path"
  - "cplexroot"
  - "IBM"
  - "optimization software"
  - "virtual environment"
  - "oplroot"
  - "Java"
  - "Python"
  - "installation"
  - "LIBRARY_PATH_EXPANDED"
  - "LD_LIBRARY_PATH"

questions:
  - "What is IBM CPLEX and how can academic users obtain the correct version for Compute Canada clusters?"
  - "What command is used to execute the downloaded CPLEX installation archive?"
  - "How do you create and configure a personal module file to properly access the installed CPLEX software?"
  - "What variables must be adjusted to ensure the CPLEX configuration matches the user's specific version and installation path?"
  - "What are the necessary steps and potential memory workarounds required to configure and compile CPLEX for Java?"
  - "How should a user proceed to install CPLEX Python modules such as docplex using a virtual environment?"
  - "What specific optimization software components and tools are being configured in this script?"
  - "Which environment variables are being modified to include the new library and binary paths?"
  - "What operating system and system architecture are explicitly targeted by the directory paths mentioned in the text?"
  - "What variables must be adjusted to ensure the CPLEX configuration matches the user's specific version and installation path?"
  - "What are the necessary steps and potential memory workarounds required to configure and compile CPLEX for Java?"
  - "How should a user proceed to install CPLEX Python modules such as docplex using a virtual environment?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) is software for optimization, developed by IBM and available for academic users through [IBM's Academic Initiative](https://www.ibm.com/academic/home).

## Download
To use CPLEX on Digital Research Alliance of Canada (the Alliance) clusters, you must first [register with IBM](https://www.ibm.com/academic/home) and then download a personal version of the software. If you are presented with a choice of architectures, choose *Linux x86-64*.

## Installation
The file is an executable archive which will perform the installation after you have answered a few questions. To execute the archive, you need to type the command `bash ./cplex_studioXYZ.linux-x86.bin`.

To access the software, you can create a personal module. Modules are normally created and placed in a directory hierarchy. In order for your modules to be found, you need to modify the configuration file `$HOME/.bashrc` so that it points to the root of this hierarchy, by adding the following line:

```bash
export MODULEPATH=$HOME/modulefiles:$MODULEPATH
```

Next, you need to create a directory structure in which to put your new CPLEX module:

```bash
mkdir -p $HOME/modulefiles/mycplex
```

In this directory, you should create a file (e.g., `$HOME/modulefiles/mycplex/12.8.0`) with the version number corresponding to the version you downloaded (e.g., 12.8.0) and with the following content:

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
Adjust the lines which correspond to the variables `cplexversion` and `studio_root` so that they have the correct values for your situation, i.e., the version you downloaded and the path you specified when extracting the archive.

## Java
If you use Java, you will have some further steps to carry out. Firstly, in your `.bashrc` file, you can add the line:

```bash
export CLASSPATH=.
```
which will allow your code to be found during execution.

Next, you should modify the dynamic library of CPLEX. Look for this library in the directory hierarchy of the installation directory, make a copy of it, and then execute the command:

```bash
setrpaths.sh --path libcplex1280.so
```

!!! note
    It's possible that during your compilation, you receive an error message because of a lack of memory. In this case, you should request a compute node using an interactive job to do the compilation. For example:

    ```bash
    salloc --time=1:0:0 --ntasks=1 --mem-per-cpu=8G
    ```

## Python
After you have installed [CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) as documented above, you must first install the module that you created:

```bash
module load mycplex/<version>
```

To install the CPLEX Python modules like `docplex`, we suggest that you use a [virtual environment](python.md#creating-and-using-a-virtual-environment).

Once the virtual environment has been activated, you should navigate to the directory `$STUDIO_ROOT/python`, after which you can install the module using the command:

```bash
python setup.py install
```

!!! warning
    The installation of these Python modules must be done on the login node because they are not available in our [software stack](../programming/available_python_wheels.md).