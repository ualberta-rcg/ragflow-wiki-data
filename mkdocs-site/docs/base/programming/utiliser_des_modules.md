---
title: "Utiliser des modules"
slug: "utiliser_des_modules"
lang: "base"

source_wiki_title: "Utiliser des modules"
source_hash: "93d75e3c15d2530eb28f39c0b6989631"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:28:51.588001+00:00"

tags:
  []

keywords:
  - "module spider"
  - "environnement"
  - "bibliothèque FFTW"
  - "système de modules"
  - "serveurs Linux"
  - "module"
  - "module load"
  - "hiérarchie de modules"
  - "versions de modules"
  - "environnement logiciel"
  - "load"
  - "compilateur gcc"
  - "commandes module"
  - "collection de modules"
  - "sous-commande"
  - "list"
  - "Lmod"
  - "modules"
  - "openmpi"
  - "remplacement automatique"

questions:
  - "Qu'est-ce qu'un fichier module et comment modifie-t-il l'environnement logiciel de l'utilisateur ?"
  - "Quel est l'avantage principal de l'architecture modulaire gérée par l'outil Lmod sur les serveurs ?"
  - "À quoi servent les différentes sous-commandes telles que spider, avail, list et load pour la gestion des modules ?"
  - "Comment peut-on ajouter, retirer ou effacer complètement des modules de son environnement à l'aide des sous-commandes Lmod ?"
  - "Quelle est la méthode recommandée pour sauvegarder et restaurer un ensemble de modules sans utiliser le chargement automatique dans le fichier .bashrc ?"
  - "Pourquoi le système utilise-t-il une hiérarchie de modules plutôt qu'une structure plate pour gérer les différentes versions et dépendances ?"
  - "Comment peut-on consulter la liste des modules qui nous sont disponibles ?"
  - "Quelle sous-commande permet d'afficher les modules actuellement chargés dans l'environnement ?"
  - "Quelle est la procédure pour charger un module spécifique tel que gcc/9.3 ?"
  - "Quel problème de gestion des versions est illustré par l'exemple de la bibliothèque FFTW ?"
  - "Pourquoi la méthode consistant à inclure toutes les dépendances dans le nom du module est-elle critiquée ?"
  - "Quelle solution le texte propose-t-il pour remplacer cette nomenclature jugée peu pratique ?"
  - "Quelle est la différence entre les commandes « module avail » et « module spider » dans le contexte d'une hiérarchie de modules ?"
  - "Comment le système gère-t-il le remplacement automatique et ses dépendances lorsqu'on charge un module de la même famille ou une nouvelle version ?"
  - "Quelles commandes spécifiques faut-il exécuter pour pouvoir utiliser le système de modules avec les interpréteurs de commandes ZSH ou KSH ?"
  - "Quelle est la différence entre les commandes « module avail » et « module spider » dans le contexte d'une hiérarchie de modules ?"
  - "Comment le système gère-t-il le remplacement automatique et ses dépendances lorsqu'on charge un module de la même famille ou une nouvelle version ?"
  - "Quelles commandes spécifiques faut-il exécuter pour pouvoir utiliser le système de modules avec les interpréteurs de commandes ZSH ou KSH ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Our servers can run all software that operates on Linux. In the simplest case, the software you need will already be installed on one of the compute servers. It will then be accessible as a **module**. If this is not the case, you can either ask our team to install it for you, or you can do it yourself.

Modules are configuration files that contain instructions to modify your software environment. This modular architecture allows multiple versions of the same application to be installed without conflict. For new servers, modules are managed by the [Lmod](https://www.tacc.utexas.edu/research-development/tacc-projects/lmod) tool, developed at [TACC](https://www.tacc.utexas.edu/). This tool replaces [*Environment Modules*](http://modules.sourceforge.net/), which is used on most older servers. If you are familiar with it, you should not be too unfamiliar, as *Lmod* was designed to be very similar to *Environment Modules*. Refer to the section [Lmod vs Environment Modules](#lmod-vs-environment-modules) below for the main differences.

A modulefile contains the necessary information to make an application or library available in the user's session. Typically, a modulefile contains instructions that modify or initialize environment variables like `PATH` and `LD_LIBRARY_PATH` to use the different installed software. Note that simply loading a module does not execute the software in question. To find out the name of the binary file and its usage syntax, you must read the software's documentation; with the `module` command, you normally do not need to know the path to the software or library. You can see details for the module by typing the command `module show <module name>`.

## Main `module` Commands
The `module` command has several sub-commands. The normal syntax is
```bash
module command [other options]
```

To see the list of available sub-commands, use
```bash
module help
```

### `spider` Sub-command
The `spider` sub-command displays all modules located in the [current standard software environment](standard_software_environments.md).
```bash
module spider
```

If you specify the name of an application, for example with
```bash
module spider openmpi
```
this will display the list of all available versions.

If you specify the name of the application with its version number, for example with
```bash
module spider openmpi/4.0.3
```
this will display the list of module options to load to access that version.

### `avail` Sub-command
To list the modules you can load, use
```bash
module avail
```

You can obtain a list of modules available for a particular library or tool with
```bash
module avail openmpi
```

Note that the `module avail` command may not list certain modules that are incompatible with the modules you have loaded. To see the list of modules other than those loaded and available to you, use the `spider` sub-command documented above.

### `list` Sub-command
The `list` sub-command displays the modules currently loaded in your environment.
```bash
module list
```

### `load` Sub-command
The `load` sub-command allows you to load a given module. For example
```bash
module load gcc/9.3
```
would load the GCC compiler module version 9.3.

You can load more than one module with a single command. For example
```bash
module load gcc/9.3 openmpi/4.0
```
would load both the GCC 9.3 compiler and the OpenMPI 4.0 library compiled for GCC.

If you load a module that is incompatible with an already loaded module, Lmod will indicate that it has replaced the old module with the new one. This can happen particularly for compilers and MPI implementations.

### `unload` Sub-command
Contrary to the `load` sub-command, `unload` removes a module from your environment. For example
```bash
module unload gcc/9.3
```
would remove the GCC 9.3 compiler from your environment.

If certain modules depended on this compiler, Lmod will indicate that they have been deactivated.

### `purge` Sub-command
The `purge` sub-command allows you to remove all loaded modules at once.
```bash
module purge
```

Some modules may be marked as *sticky* (permanent) by system administrators and will not be removed.

### `show`, `help`, and `whatis` Sub-commands
The `show`, `help`, and `whatis` sub-commands provide additional information about a given module. The `show` sub-command displays the entire module, the `help` command displays a help message, and the `whatis` command shows a description of the module.
```bash
module help gcc/9.3
```

### `apropos` or `keyword` Sub-command
The `apropos` or `keyword` sub-commands allow searching for a keyword across all modules. If you don't know which module is appropriate for your computation, you can search the descriptions.

## Automatic Module Loading
!!! warning "Automatic Module Loading"
    We advise against automatically loading modules in your `.bashrc`. We recommend instead loading the necessary modules as needed, for example in your job scripts. To facilitate loading a large number of modules, it is preferable to use a module collection.

## Module Collections
Lmod allows you to create a module collection. To do this, first load the required modules with, for example
```bash
module load gcc/9.3 openmpi/4.0.3 mkl
```

Then use the `save` command to save this collection.
```bash
module save my_modules
```
The argument `my_modules` is a name you give to the collection.

You can then, in a subsequent session or in a job, restore this collection with the command
```bash
module restore my_modules
```

## Hidden Modules
!!! tip "Hidden Modules"
    Some modules are hidden. You can ignore them. These are generally modules you do not need to load manually. They are loaded automatically as needed.

## Module Hierarchy
Many high-performance computing systems worldwide use a flat module structure with all modules at the same level. This becomes problematic when a large number of version combinations of different modules are available. For example, if you need to use the FFTW library, and the `fftw` module is available in several versions, including one compiled with the `gcc` compiler version 4.8 and `openmpi` 1.6, you may have already seen modules named `openmpi/4.0_gcc9.3` and `fftw/3.8_gcc9.3_openmpi4.0`. This is neither elegant nor practical. To solve this problem, we use a module hierarchy. Instead of using the command
```bash
module load gcc/9.3 openmpi/4.0_gcc9.3 fftw/3.8_gcc9.3_openmpi4.0
```
you will use the command
```bash
module load gcc/9.3 openmpi/4.0 fftw/3.8
```
This is made possible with a module hierarchy. The `fftw/3.8` module that is loaded will not be the same if you have previously loaded the Intel compiler or the GCC compiler.

The disadvantage of using a module hierarchy is that, since modules can have the same name, only modules compatible with *parent* modules are displayed by the `module avail` command. Loading a parent is therefore a prerequisite to accessing certain modules. To get complete information, the module system makes the `module spider` command available. This command traverses the entire hierarchy and displays all modules. By specifying a particular module and version, it is then possible to know which paths in the hierarchy allow loading the desired module.

## Automatic Module Replacement
When the module system detects two modules of the same family, or two versions of the same module, the `module load` command will automatically replace the original module with the one to be loaded. If the replaced module is a node in the module hierarchy, dependent modules will be reloaded if a compatible version exists, or deactivated otherwise.

## Creating Modules
For instructions on how to create modules, please refer to the [official documentation](http://lmod.readthedocs.io/en/latest/015_writing_modules.html).

## Using Modules with ZSH and KSH
If you want to use modules with ZSH or KSH shells, execute the following commands:
```bash
zsh -l
ksh -l