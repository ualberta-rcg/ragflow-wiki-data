---
title: "Pgdbg"
slug: "pgdbg"
lang: "base"

source_wiki_title: "Pgdbg"
source_hash: "e9ac25ff1fcdaa2eea703b44e913ced7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:23:52.084925+00:00"

tags:
  []

keywords:
  - "Main toolbar"
  - "Source window"
  - "PGDBG debugger"
  - "Graphical mode"
  - "SIGTRAP"
  - "omp.c"
  - "thread context"
  - "command-line mode"
  - "pgdbg"
  - "thread ID"
  - "Debug information tabs"
  - "debugging"
  - "OpenMP"
  - "PGI compiler"
  - "PGDBG"

questions:
  - "What is PGDBG, and for which types of applications and programming languages is it particularly well-suited compared to standard debuggers like GDB?"
  - "What are the necessary steps to prepare the environment modules and compile code to enable debugging with PGDBG?"
  - "How do you initiate a text-mode debugging session and manage or switch between different threads during program execution?"
  - "What are the main areas that make up the graphical user interface of the PGDBG debugger?"
  - "What are the specific functions of the four drop-down lists located on the main toolbar?"
  - "How do the source window and debug information tabs function within the layout of the debugger?"
  - "What command is used to switch the context to a specific thread in the provided debugging session?"
  - "What is the current state and signal of the threads listed in the output?"
  - "In which source file and at what memory addresses are the stopped threads located?"
  - "What are the main areas that make up the graphical user interface of the PGDBG debugger?"
  - "What are the specific functions of the four drop-down lists located on the main toolbar?"
  - "How do the source window and debug information tabs function within the layout of the debugger?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description
PGDBG is a powerful and simple tool for debugging both MPI-parallel and OpenMP thread-parallel Linux applications. It is included in the PGI compiler package and configured for OpenMP thread-parallel debugging.

For most C, C++, or Fortran 77 codes, one can use a regular GNU debugger such as GDB. However, Fortran 90/95 programs are not handled very well by GDB. The Portland Group has developed a debugger called [pgdbg](https://www.pgroup.com/products/tools.htm/pgdbg.htm) which is more suited for such codes. Pgdbg is provided in two modes: a graphical mode with enabled X11 forwarding, or a text mode.

## Quickstart guide
Using PGDBG usually consists of two steps:
1.  **Compilation**: Compile the code with debugging enabled.
2.  **Execution and debugging**: Execute the code and analyse the results.

The actual debugging can be accomplished in either command-line mode or graphical mode.

### Environment modules
Before you start profiling with PGDBG, the appropriate [module](utiliser-des-modules.md) needs to be loaded.
PGDBG is part of the PGI compiler package, so run `module avail pgi` to see what versions are currently available with the compiler, MPI, and CUDA modules you have loaded. For a comprehensive list of PGI modules, run `module -r spider '.*pgi.*'`.

As of December 2018, these were:
*   pgi/13.10
*   pgi/17.3

Use `module load pgi/version` to select a version; for example, to load the PGI compiler version 17.3, use

```bash
module load pgi/17.3
```

### Compiling your code
To be able to debug with pgdbg, you first need to compile your code with debugging information enabled. With pgdbg, you do so by adding a debugging flag "-g":

```bash
pgcc -g program.c -o program
```

### Command-line mode
Once your code is compiled with the proper options, you can run PGDBG for the analysis. The debugger's default user interface is a graphical user interface (GUI). However, if for some reason you don't want to run in GUI or don't have X11 forwarding, you can run pgdbg in a text mode by adding an extra option "-text":

```bash
pgdbg -text program arg1 arg2
```

Once PGDBG is invoked in the command-line mode, you will have access to a prompt:

```
pgdbg -text program
PGDBG 17.3-0 x86-64 (Cluster, 256 Process)
PGI Compilers and Tools
Copyright (c) 2017, NVIDIA CORPORATION.  All rights reserved.
Loaded: /home/user/program
pgdbg>
```

Before you can debug, you need to execute `run` in the prompt:

```
pgdbg> run
```

PGDBG automatically attaches to new threads as they are created during program execution. PGDBG describes when a new thread is created.
During a debug session, at any one time, PGDBG operates in the context of a single thread, the *current thread*. The current thread is chosen by using the `thread` command. The `threads` command lists all threads currently employed by an active program:

```
pgdbg > threads
0  ID PID    STATE      SIGNAL      LOCATION
   3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
=> 2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

For example, now we switch the context to thread with ID 2. Use command `thread` to do so:

```
pgdbg > thread 3
pgdbg > threads
0  ID PID    STATE      SIGNAL      LOCATION
=> 3  18399  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   2  18398  Stopped    SIGTRAP     main line: 32 in "omp.c" address: 0x80490cf
   1  18397  Stopped    SIGTRAP     main line: 31 in "omp.c" address: 0x80490ab
   0  18395  Stopped    SIGTRAP     f line: 5 in "omp.c" address: 0x8048fa0
```

### Graphical mode
This is the default user interface of the PGDBG debugger. If you have set the X11 forwarding, then PGDBG will start in the graphical mode in a pop-up window.

As the illustration shows, the GUI is divided into several areas:
*   menu bar
*   main toolbar
*   source window
*   program I/O window
*   and debug information tabs.

#### Menu bar
The main menu bar contains these menus: File, Edit, View, Connections, Debug and Help. You can navigate the menus using the mouse or keyboard shortcuts.

#### Main toolbar
The debugger's main toolbar contains several buttons and four drop-down lists. The first drop-down list displays the current process or, in other words, the current thread. The list’s label changes depending on whether processes or threads are described. When multiple threads are available, use this drop-down list to specify which process or thread should be the current one.

The second drop-down list is labelled Apply. The selection in the Apply drop-down determines the set of processes and threads to which action commands are applied. The third drop-down list is labelled Display. The selection in the Display drop-down determines the set of processes and threads to which data display commands are applied.

The fourth drop-down list, labelled as File, displays the source file that contains the current target location.

#### Source window
The source window and all of the debug information tabs are dockable tabs, meaning that they can be taken apart from the main window. This can be done by double-clicking the tab. The source window shows the source code for the current session.

#### Program I/O Window
Program output is displayed in the Program IO tab’s central window. Program input is entered into this tab’s Input field.

#### Debug information tab
Debug information tabs take up the lower half of the debugger GUI. Each of these tabs provides a particular function or view of debug information. The following sections discuss the tabs as they appear from left-to-right in the GUI’s default configuration.

## References
*   [PGI Debugger User's Guide](https://www.pgroup.com/resources/docs/17.7/x86/pgdbg-user-guide/index.htm)
*   [PGI webpage](https://www.pgroup.com/index.htm)