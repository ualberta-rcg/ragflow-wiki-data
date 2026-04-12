---
title: "CPLEX"
slug: "cplex"
lang: "base"

source_wiki_title: "CPLEX"
source_hash: "a4019465ab84d2aced24414474ff77c4"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:03:03.585933+00:00"

tags:
  - software

keywords:
  - "CPLEX"
  - "prepend-path"
  - "IBM"
  - "environnement virtuel"
  - "oplroot"
  - "LIBRARY_PATH"
  - "concertroot"
  - "logiciel d'optimisation"
  - "Java"
  - "Python"
  - "compilation"
  - "modules personnels"
  - "installation"
  - "LIBRARY_PATH_EXPANDED"

questions:
  - "Comment les usagers universitaires peuvent-ils obtenir le logiciel CPLEX pour l'utiliser sur une grappe de Calcul Canada ?"
  - "Quelle est la commande exacte à exécuter pour lancer l'installation de l'archive téléchargée ?"
  - "Quelles étapes et modifications de fichiers sont nécessaires pour créer et configurer un module personnel permettant d'accéder au logiciel ?"
  - "Quelles variables doivent être ajustées pour correspondre à la version et au chemin d'accès de l'installation de CPLEX ?"
  - "Quelles sont les étapes supplémentaires nécessaires pour configurer et compiler un projet Java utilisant CPLEX, notamment en cas d'erreur de mémoire ?"
  - "Quelle est la procédure recommandée pour installer les paquets CPLEX dans un environnement virtuel Python sur le nœud de tête ?"
  - "What is the primary purpose of the `prepend-path` commands in this configuration snippet?"
  - "Which specific optimization software components are having their library paths configured in this text?"
  - "How does the formatting of the `LIBRARY_PATH_EXPANDED` variable differ from the standard `LIBRARY_PATH` variable?"
  - "Quelles variables doivent être ajustées pour correspondre à la version et au chemin d'accès de l'installation de CPLEX ?"
  - "Quelles sont les étapes supplémentaires nécessaires pour configurer et compiler un projet Java utilisant CPLEX, notamment en cas d'erreur de mémoire ?"
  - "Quelle est la procédure recommandée pour installer les paquets CPLEX dans un environnement virtuel Python sur le nœud de tête ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

CPLEX is an optimization software developed by IBM, available to academic users through the [Academic Initiative](https://www.ibm.com/academic/home) program.

## Downloading
To use CPLEX on a Digital Research Alliance of Canada cluster, [you must first register with IBM](https://www.ibm.com/academic/home) and then download your personal version of the software. If you have a choice between several architectures, choose *Linux x86-64*.

## Installation
The file is an executable archive that will perform the installation by asking a few questions. To run the archive, you need to execute `bash ./cplex_studioXYZ.linux-x86.bin`.

To access the software, you can create personal modules. Modules are usually created and placed in a directory tree. For your modules to be found, you must modify your `$HOME/.bashrc` configuration file to point to the root of this tree by adding the following line:

```bash
export MODULEPATH=$HOME/modulefiles:$MODULEPATH
```

Next, you need to create a directory structure to place your new CPLEX module:

```bash
mkdir -p $HOME/modulefiles/mycplex
```

In this directory, you will create a file (for example, `$HOME/modulefiles/mycplex/12.8.0`) named with the version number you downloaded previously (the XYZ), which contains the following:

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

Adjust the lines corresponding to the `cplexversion` and `studio_root` variables so they have the correct values: the downloaded version and the access path for this software (i.e., the path you specified when extracting the archive).

## Java
If you are using Java, you will have a few extra steps. First, in your `.bashrc` file, you can add the line:
```bash
export CLASSPATH=.
```
which will allow your code to be found during execution.

Next, you will need to modify the dynamic library for CPLEX. Look for this library in the installation directory tree, make a copy of it, and run the command:
```bash
setrpaths.sh --path libcplex1280.so
```

!!! warning "Memory Error during Compilation"
    It is possible that during compilation, you may receive an error message due to insufficient memory. If this is the case, you will need to request an interactive compute node to perform the compilation.
    For example:
    ```bash
    salloc --time=1:0:0 --ntasks=1 --mem-per-cpu=8G
    ```

## Python
After installing [CPLEX](https://www.ibm.com/analytics/data-science/prescriptive-analytics/cplex-optimizer) as indicated in the previous section, you must first load CPLEX:
```bash
module load mycplex/<version>
```

To install CPLEX packages such as `docplex`, we suggest doing so from a [virtual environment](../python/#create-and-use-a-virtual-environment).

Once the virtual environment is activated, you will need to navigate to the `$STUDIO_ROOT/python` directory, and then you can install the library with the command:
```bash
python setup.py install
```

!!! note
    The installation of CPLEX packages must be done on the head node, as they are not available on our [software stack](../programming/available_python_wheels.md).