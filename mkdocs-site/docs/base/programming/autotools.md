---
title: "Autotools"
slug: "autotools"
lang: "base"

source_wiki_title: "Autotools"
source_hash: "47b2d3837383d99d5d512a94dede150a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:36:43.788927+00:00"

tags:
  []

keywords:
  - "Makefiles"
  - "autoconf"
  - "configure script"
  - "GNU build system"
  - "compiler options"

questions:
  - "What is the primary purpose of the autoconf tool and its configure script in the software build process?"
  - "How can a user specify a custom installation directory for their software instead of installing it system-wide?"
  - "In what ways can a user customize the compilation process, such as enabling specific features or defining compiler variables, when running the configure script?"
  - "What is the primary purpose of the autoconf tool and its configure script in the software build process?"
  - "How can a user specify a custom installation directory for their software instead of installing it system-wide?"
  - "In what ways can a user customize the compilation process, such as enabling specific features or defining compiler variables, when running the configure script?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

[autoconf](https://en.wikipedia.org/wiki/Autoconf) is a tool that belongs to the [autotools](http://en.wikipedia.org/wiki/GNU_build_system) suite, also known as the *GNU build system*. The tool automates the process of generating the custom [Makefiles](make.md) necessary to build a program on different systems, with (perhaps) different compilers. When a program is built with the help of `autoconf`, the first step is to call the `configure` script:

```bash
./configure
```

This verifies that compilers and other relevant software are installed on the computer and that appropriate versions are available, and generates a Makefile customised for your system.

After that, you call [make](make.md) as usual:
```bash
make
```

Finally, `make install` installs the files at the right places. If you do not want to install the software for all users of the server, but only for yourself, you normally need to specify where to install your software. You can (usually) do this in the following manner:

```bash
mkdir $HOME/SOFTWARE
make install --prefix=$HOME/SOFTWARE
```
In other cases you must supply the `--prefix` option to `./configure` instead of to `make`; see the documentation for the particular software you are trying to install. You may also wish to [create a module](creer-un-module.md) to show the system the paths to your newly installed software.

A basic compilation of a program using `autoconf` can thus be as simple as
```bash
./configure && make && make install --prefix=$HOME/SOFTWARE
```

## Frequently used options for *configure* scripts

`configure` scripts generally accept a large number of options. They vary from project to project. Nevertheless, certain options are very common and deserve mentioning. In all cases you can run
```bash
./configure --help
```
to get a detailed list of all supported options.

### Installation directory

An option that is always available is `--prefix`. This option allows you to define the directory where the command `make install` installs the application or the library. For example, to install an application into the subdirectory `programs` within your home directory, you could use
```bash
./configure --prefix=$HOME/programs/
```

### Feature options

Most configuration scripts allow you to enable or to disable certain features of the program or library that you compile. Those options are generally of the type `--enable-feature` or `--disable-feature`. Within advanced computing, those options often include, for example, parallelisation using threads or using MPI. You could thus have
```bash
./configure --enable-mpi
```
or also
```bash
./configure --enable-threads
```

Often there are also options like `--with-...` to configure some features specifically.

!!! tip "Recommendation"
    It is generally recommended not to use such options and to let `autoconf` find the parameters automatically. Nevertheless, it is sometimes necessary to specify some parameters using `--with-...` options.

For example, you could specify
```bash
./configure --enable-mpi --with-mpi-dir=$MPIDIR
```

### Options defined by variables

You can generally specify the compiler that is used and the options that should be passed to it by declaring variables after the `./configure` command. For example, to define the C compiler and the options to give it, you could run
```bash
./configure CC=icc CFLAGS="-O3 -xHost"
```
The most commonly used variables include

| Option     | Description                                                                              |
| :--------- | :--------------------------------------------------------------------------------------- |
| `CFLAGS`   | Options to pass to the C compiler                                                        |
| `CPPFLAGS` | Options to pass to the preprocessor and to C, C++, Objective C, and Objective C++ compilers |
| `CXXFLAGS` | Options to pass to the C++ compiler                                                      |
| `DEFS`     | Allows the definition of a preprocessor macro                                            |
| `FCFLAGS`  | Options to pass to the Fortran compiler                                                  |
| `FFLAGS`   | Options to pass to the Fortran 77 compiler                                               |
| `LDFLAGS`  | Options to pass to the linker                                                            |
| `LIBS`     | Libraries to link                                                                        |

A more exhaustive list of variables and typical options is available [in the autoconf documentation](http://www.gnu.org/software/autoconf/manual/autoconf.html).