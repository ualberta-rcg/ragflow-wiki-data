---
title: "Utiliser des modules"
slug: "utiliser_des_modules"
lang: "base"

source_wiki_title: "Utiliser des modules"
source_hash: "93d75e3c15d2530eb28f39c0b6989631"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:29:04.483483+00:00"

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

Our servers can run all Linux-compatible software. In the simplest case, the software you need will already be installed on one of the compute servers and accessible as a **module**. If not, you can either ask our team to install it for you, or you can do it yourself.

Modules are configuration files that contain instructions to modify your software environment. This modular architecture allows multiple versions of the same application to be installed without conflict. For new servers, modules are managed by the [Lmod](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod) tool developed at [TACC](https://www.tacc.utexas.edu/). This tool replaces [*Environment Modules*](http://modules.sourceforge.net), which is used on most older servers. If you are familiar with it, you should not feel too disoriented, as *Lmod* was designed to be very similar to *Environment Modules*. Refer to the section [Lmod vs Environment Modules](#lmod-vs-environment-modules) below for the main differences.

A modulefile (*modulefile*) contains the information required to make an application or library available in the user's session. Typically, a modulefile contains instructions that modify or initialize environment variables such as `PATH` and `LD_LIBRARY_PATH` to use the installed software. Note that simply loading a module does not execute the software in question. To find out the name of the binary file and its usage syntax, you must read the software's documentation. With the `module` command, you normally do not need to know the path to the software or library. You can see details for the module by typing the command `module show <module name>`.

## Main `module` Commands
The `module` command has several subcommands. The normal syntax is

```bash
module command [other options]
```

To see a list of available subcommands, use

```bash
module help
```

### `spider` Subcommand
The `spider` subcommand displays all modules in the current [standard software environment](standard-software-environments.md).

```bash
module spider
```

If you specify an application name, for example with

```bash
module spider openmpi
```

this will display a list of all available versions.

If you specify the application name with its version number, for example with

```bash
module spider openmpi/4.0.3
```

this will display a list of module options to load to access that version.

### `avail` Subcommand
To list the modules you can load, use

```bash
module avail
```

You can get a list of available modules for a particular library or tool with

```bash
module avail openmpi
```

Note that the `module avail` command may not list some modules that are incompatible with the modules you have loaded. To see a list of modules other than those currently loaded and available to you, use the `spider` subcommand documented above.

### `list` Subcommand
The `list` subcommand displays the modules currently loaded in your environment.

```bash
module list
```

### `load` Subcommand
The `load` subcommand allows you to load a given module. For example,

```bash
module load gcc/9.3
```

would load the GCC compiler module version 9.3.

You can load more than one module with a single command. For example,

```bash
module load gcc/9.3 openmpi/4.0
```

would load both the GCC 9.3 compiler and the OpenMPI 4.0 library compiled for GCC.

If you load a module that is incompatible with an already loaded module, Lmod will indicate that it has replaced the old module with the new one. This can occur particularly for compilers and MPI implementations.

### `unload` Subcommand
Unlike the `load` subcommand, `unload` removes a module from your environment. For example,

```bash
module unload gcc/9.3
```

would remove the GCC 9.3 compiler from your environment.

If certain modules depended on this compiler, Lmod will indicate that they have been deactivated.

### `purge` Subcommand
The `purge` subcommand allows you to remove all loaded modules at once.

```bash
module purge
```

Some modules may be marked as *sticky* by system administrators and will not be removed.

### `show`, `help`, and `whatis` Subcommands
The `show`, `help`, and `whatis` subcommands provide additional information about a given module. The `show` subcommand displays the entire module, the `help` command displays a help message, and the `whatis` command shows a description of the module.

```bash
module help gcc/9.3
```

### `apropos` or `keyword` Subcommands
The `apropos` or `keyword` subcommands allow you to search for a keyword across all modules. If you do not know which module is appropriate for your calculation, you can search within the descriptions.

## Automatic Module Loading

!!! warning
    Do NOT automatically load modules in your `.bashrc`.
    We recommend loading necessary modules as needed, for example, in your job scripts. To facilitate loading a large number of modules, it is preferable to use a module collection.

## Module Collections
Lmod allows you to create a module collection. To do this, first load the required modules with, for example,

```bash
module load gcc/9.3 openmpi/4.0.3 mkl
```

Then, use the `save` command to save this collection.

```bash
module save my_modules
```

The `my_modules` argument is a name you give to the collection.

You can then, in a later session or job, restore this collection with the command

```bash
module restore my_modules
```

## Hidden Modules
Some modules are hidden. You can ignore them. These are generally modules that you do not need to load manually; they are loaded automatically as needed.

## Module Hierarchy
Many high-performance computing systems worldwide use a flat module structure with all modules at the same level. This becomes problematic when a large number of version combinations of different modules are available. For example, if you need to use the [FFTW](fftw.md) library, and the `fftw` module is available in several versions, including a version compiled with `gcc` compiler version 4.8 and `openmpi` 1.6, you may have seen modules named `openmpi/4.0_gcc9.3` and `fftw/3.8_gcc9.3_openmpi4.0`. This is neither elegant nor practical. To solve this problem, we use a module hierarchy. Instead of using the command

```bash
module load gcc/9.3 openmpi/4.0_gcc9.3 fftw/3.8_gcc9.3_openmpi4.0
```

you will use the command

```bash
module load gcc/9.3 openmpi/4.0 fftw/3.8
```

This is made possible with a module hierarchy. The `fftw/3.8` module that is loaded will not be the same if you have previously loaded the Intel compiler or the GCC compiler.

The disadvantage of using a module hierarchy is that since modules can have the same name, only modules compatible with the *parent* modules are displayed by the `module avail` command. Loading a parent is therefore a prerequisite to access certain modules. To get complete information, the module system makes the `module spider` command available. This command traverses the entire hierarchy and displays all modules. By specifying a module and a particular version, it is then possible to know which paths in the hierarchy allow the desired module to be loaded.

## Automatic Module Replacement
When the module system detects two modules from the same family, or two versions of the same module, the `module load` command will automatically replace the original module with the one to be loaded. If the replaced module is a node in the module hierarchy, dependent modules will be reloaded if a compatible version exists, or deactivated otherwise.

## Creating Modules
For instructions on how to create modules, please refer to the [official documentation](http://lmod.readthedocs.io/en/latest/015_writing_modules.html).

## Using Modules with ZSH and KSH
If you want to use modules with ZSH or KSH *shells*, execute the following commands:

```bash
zsh -l
```

```bash
ksh -l