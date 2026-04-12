---
title: "Using Nix"
slug: "using_nix"
lang: "base"

source_wiki_title: "Using Nix"
source_hash: "a1f720abbd772386552c4bbe9be0dfb1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:18:40.775800+00:00"

tags:
  - software

keywords:
  - "nix"
  - "nix commands"
  - "Nixpkgs"
  - "buildEnv"
  - "emacs attributes"
  - "python compositions"
  - "software composition"
  - "R packages"
  - "Haskell packages"
  - ".nix file"
  - "nix-env"
  - "python packages"
  - "nixpkgs"
  - "symlink"
  - "Nix"
  - "nix environment"
  - "Nix expressions"
  - "emacsPackages"
  - "package compositions"
  - "emacs packages"
  - "emacsWithPackages"
  - "SHARCNET systems"
  - "Python packages"
  - "Emacs packages"
  - "per-user"
  - "PATH"
  - "haskell packages"
  - "Emacs"
  - "emacs"

questions:
  - "What is Nix, and why should module-loaded software be preferred over it for long-running simulations?"
  - "How can a user completely reset their Nix environment when standard rollback commands are insufficient?"
  - "What are the differences between using Nix for one-off, per-project, and per-user situations, and which commands are associated with each?"
  - "How can a user specify the output symlink name when executing the command?"
  - "What effect does loading the nix module have on a user's PATH environment variable?"
  - "Which command should be used to add or remove compositions from the per-user directory?"
  - "How does Nix manage environment versions, and what commands are used to navigate or delete these generations?"
  - "What is the process for creating a custom composition using a `.nix` file to bundle multiple binaries together?"
  - "How does Nixpkgs handle Python-specific environments, such as wrapping Python executables with a specific set of libraries?"
  - "How can users create customized R or RStudio wrappers that include a specific set of R packages?"
  - "What attributes does Nixpkgs provide to set up a Haskell environment with specific packages and Hoogle documentation?"
  - "What are the common aliases and naming conventions used in Nixpkgs for specifying versions of Python and Emacs?"
  - "How can users directly execute programs provided by Python packages using the Nix command line?"
  - "What is the purpose of creating a Python composition within a `.nix` file?"
  - "How does a custom Python composition enable access to a specific set of libraries?"
  - "How can you configure a `.nix` file to create an Emacs environment with specific packages enabled?"
  - "What command allows you to directly build and examine the contents of an individual Emacs package?"
  - "What are the available aliases and shortcuts for specifying Emacs versions and package compositions?"
  - "What resource is provided in the text for learning how to fix broken Haskell packages?"
  - "What does the `Ng` suffix indicate when applied to Emacs-related attributes in Nixpkgs?"
  - "What is the difference between the `emacs<major><minor>` and `emacs<major><minor>Packages` attributes?"
  - "How can you configure a `.nix` file to create an Emacs environment with specific packages enabled?"
  - "What command allows you to directly build and examine the contents of an individual Emacs package?"
  - "What are the available aliases and shortcuts for specifying Emacs versions and package compositions?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Overview

[Nix](https://nixos.org/nix/) is a software building and composition system that allows users to manage their own persistent software environments. It is only available on SHARCNET systems (i.e., graham and legacy).

*   Supports one-off, per-project, and per-user usage of compositions
*   Compositions can be built, installed, upgraded, downgraded, and removed as a user
*   Operations either succeed or fail leaving everything intact (operations are atomic).
*   Extremely easy to add and share compositions

Currently Nix is building software in a generic manner (e.g., without AVX2 or AVX512 vector instructions support), so module-loaded software should be preferred for longer running simulations when it exists.

!!! note
    The message `failed to lock thread to CPU XX` is a harmless warning that can be ignored.

## Enabling and disabling the Nix environment

The user’s current Nix environment is enabled by loading the Nix module. This creates some `*.nix*` files and sets some environment variables.

```bash
[name@cluster:~]$ module load nix
```

It is disabled by unloading the Nix module. This unsets the environment variables but leaves the `*.nix*` files alone.

```bash
[name@cluster:~]$ module unload nix
```

## Completely resetting the Nix environment

Most per-user operations can be undone with the `--rollback` option (i.e., `nix-env --rollback` or `nix-channel --rollback`). Sometimes it is useful to entirely reset Nix though. This is done by unloading the module, erasing all user-related Nix files, and then reloading the module file.

```bash
[name@cluster:~]$ module unload nix
[name@cluster:~]$ rm -fr ~/.nix-profile ~/.nix-defexpr ~/.nix-channels ~/.config/nixpkgs
[name@cluster:~]$ rm -fr /nix/var/nix/profiles/per-user/$USER /nix/var/nix/gcroots/per-user/$USER
[name@cluster:~]$ module load nix
```

# Existing compositions

The `nix search` command can be used to locate already available compositions:

```bash
[user@cluster:~]$ nix search git
...
* nixpkgs.git (git-minimal-2.19.3)
  Distributed version control system
...
```

!!! tip "Pro tips"
    *   You need to specify `-u` after upgrading your channel (this will take a while).
    *   The search string is actually a regular expression, and multiple ones are ANDed together.

Often our usage of a composition is either a one-off, a per-project, or an all-the-time situation. Nix supports all three of these cases.

## One-offs

If you just want to use a composition once, the easiest way is to use the `nix run` command. This command will start a shell in which `PATH` has been extended to include the specified composition:

```bash
[user@cluster:~]$ nix run nixpkg.git
[user@cluster:~]$ git
[user@cluster:~]$ exit
```

Note that this does not protect the composition from being garbage-collected overnight (e.g., the composition is only guaranteed to be around temporarily for your use until sometime in the wee morning hours).

!!! tip "Pro tips"
    *   You can specify more than one composition in the same `nix run` command.
    *   You can specify a command instead of a shell with `-c <cmd> <args> ...`.

## Per-project

If you want to use a program for a specific project, the easiest way is with the `nix build` command. This command will create a symbolic link (by default named `result`) from which you can access the program's *bin* directory to run it.

```bash
[user@cluster:~]$ nix build nixpkgs.git
[user@cluster:~]$ ./result/bin/git
```

Note that (currently) the composition will only be protected from overnight garbage collection if you output the symlink into your *home* directory and do not rename or move it.

!!! tip "Pro tips"
    *   You can specify the output symlink name with the `-o <name>` option.
    *   Add the *bin* directory to your `PATH` to not have to type it in every time.

## Per-user

Loading the `nix` module adds the per-user common *~/.nix-profile/bin* directory to your `PATH`. You can add and remove compositions from this directory with the `nix-env` command:

```bash
[user@cluster:~]$ nix-env --install --attr nixpkgs.git
[user@cluster:~]$ nix-env --query
```

git-minimal-2.19.3

```bash
[user@cluster:~]$ nix-env --uninstall git-minimal
uninstalling 'git-minimal-2.19.3'
[user@cluster:~]$ nix-env --query
```

Each command actually creates a new version, so all prior versions remain and can be used:

```bash
[user@cluster:~]$ nix-env --list-generations
   1   2020-07-29 13:10:03
   2   2020-07-29 13:11:52   (current)
[user@cluster:~]$ nix-env --switch-generation 1
[user@cluster:~]$ nix-env --query
git-minimal-2.19.3
[user@cluster:~]$ nix-env --switch-generation 2
[user@cluster:~]$ nix-env --query
```

!!! tip "Pro tips"
    *   `nix-env --rollback` moves up one generation.
    *   `nix-env --delete-generations <time>` deletes environments older than `<time>` (e.g., `30d`).
    *   See our [nix-env page](using-nix-nix-env.md) for a much more in-depth discussion of using `nix-env`.

# Creating compositions

Often we require our own unique composition. A basic example would be to bundle all the binaries from multiple existing compositions in a common *bin* directory (e.g., `make`, `gcc`, and `ld` to build a simple C program). A more complex example would be to bundle Python with a set of Python libraries by wrapping the Python executables with shell scripts to set `PYTHON_PATH` for the Python libraries before running the real Python binaries.

All of these have a common format. You write a Nix expression in a `.nix` file that composes together existing compositions, and then you tell the above commands to use that with the `-f <nix file>` option. For example, say the file `python.nix` has an expression for a Python environment in it; you can create a per-project *bin* directory with:

```bash
[user@cluster:~]$ nix build -f python.nix -o python
[user@cluster:~]$ ./python/bin/python
```

The Nix expression you put in the file generally:

*   Does `with import <nixpkgs> {}` to bring the set of Nixpkgs into scope.
*   Calls existing composition functions with a list of space-separated components to include.

The template for doing the second of these follows below as it differs slightly across the various ecosystems.

!!! tip "Pro tip"
    *   There are many [languages and frameworks supported](https://nixos.org/nixpkgs/manual/#chap-language-support), but only a few described here. Send us an email if you would like a missing supported one added here.

## Generic

Nixpkgs provides a `buildEnv` function that does a basic composition of compositions (by combining their *bin*, *lib*, etc. directories). The list of packages are the same as used before, minus the leading `nixpkgs` prefix as it was imported (e.g., `git` instead of `nixpkgs.git`).

```nix
with import <nixpkgs> {};
buildEnv {
  name = "my environment";
  paths = [
    ... list of compositions ...
  ];
}
```

## Python

Nixpkgs provides the following Python-related attributes:

*   `python<major><minor>` - a composition providing the given Python.
*   `python<major><minor>.pkgs` - the set of Python compositions using the given Python.
*   `python<major><minor>.withPackages` - wraps Python with `PYTHON_PATH` set to a given set of Python packages.

We can use the former directly to use the programs provided by Python compositions:

```bash
[user@cluster:~]$ nix run python36.pkgs.spambayes
[user@cluster:~]$ sb_filter.py --help
[user@cluster:~]$ exit
```

And the latter in a `.nix` file to create a Python composition that enables a given set of libraries (e.g., a `python` command we can run and access the given set of Python packages from):

```nix
with import <nixpkgs> { };
python.withPackages (packages:
  with packages; [
    ... list of python packages ...
  ]
)
```

!!! tip "Pro tips"
    *   The aliases `python` and `python<major>` give default `python<major><minor>` versions.
    *   The aliases `pythonPackages<major><minor>` are short for `python<major><minor>.pkgs` (including default version variants).
    *   The function `python<major><minor>.pkgs.buildPythonPackage` can be used to build your own Python packages.

## R

Nixpkgs provides the following R-related attributes:

*   `R` - a composition providing R.
*   `rstudio` - a composition providing RStudio.
*   `rPackages` - the set of R packages.
*   `rWrapper` - a composition that wraps R with `R_LIBS` set to a minimal set of R packages.
*   `rstudioWrapper` - a composition that wraps RStudio with `R_LIBS` set to a minimal set of R packages.

We can use `rPackages` directly to examine the content of R packages:

```bash
[user@cluster:~]$ nix build rPackages.exams -o exams
[user@cluster:~]$ cat exams/library/exams/NEWS
[user@cluster:~]$ exit
```

And the latter two can be overridden in a `.nix` file to create R and RStudio wrappers to create a composition enabling a given set of R libraries (e.g., an `R` or `rstudio` command we can run and access the given set of R packages from):

```nix
with import <nixpkgs> { };
rWrapper.override {
  packages = with rPackages; [
    ... list of R packages ...
  ];
}
```

!!! tip "Pro tip"
    *   The function `rPackages.buildRPackage` can be used to build your own R packages.

## Haskell

Nixpkgs provides the following Haskell-related attributes:

*   `haskell.compiler.ghc<major><minor><patch>` - composition providing the given GHC.
*   `haskell.packages.ghc<major><minor><patch>` - the set of Haskell packages compiled by the given GHC.
*   `haskell.packages.ghc<major><minor><patch>.ghc.withPackages` - composition wrapping GHC to enable the given packages.
*   `haskell.packages.ghc<major><minor><patch>.ghc.withHoogle` - composition wrapping GHC to enable the given packages with Hoogle and documentation indices.

We can use the first directly to use programs provided by Haskell packages:

```bash
[user@cluster:~]$ nix run haskell.packages.ghc864.pandoc
[user@cluster:~]$ pandoc --help
```

And the last two in a `.nix` file create a GHC environment to enable a given set of Haskell packages (e.g., a `ghci` we can run and access the given set of packages from):

```nix
with import <nixpkgs> { };
haskell.packages.ghc864.ghc.withPackages (packages:
  with packages; [
    ... list of Haskell packages ...
  ];
}
```

!!! tip "Pro tips"
    *   The alias `haskellPackages` gives a default `haskell.packages.ghc<major><minor><patch>`.
    *   The attributes in `haskell.lib` contain a variety of useful attributes for tweaking Haskell packages (e.g., enabling profiling, etc.).
    *   The upstream maintainer has a useful [YouTube video](https://www.youtube.com/watch?v=KLhkAEk8I20) on how to fix broken Haskell packages.

## Emacs

Nixpkgs provides the following Emacs-related attributes (append an `Ng` suffix for older versions of Nixpkgs, e.g., `emacs25Ng` and `emacs25PackagesNg`):

*   `emacs<major><minor>` - a composition providing the given Emacs editor.
*   `emacs<major><minor>Packages` - the set of Emacs packages for the given Emacs editor.
*   `emacs<major><minor>Packages.emacsWithPackages` - composition wrapping Emacs to enable the given packages.

We can use the second directly to examine the content of packages:

```bash
[user@cluster:~]$ nix build nixpkgs.emacs25Packages.magit -o magit
[user@cluster:~]$ cat magit/share/emacs/site-lisp/elpa/magit*/AUTHORS.md
[user@cluster:~]$ exit
```

And the last one in a `.nix` file creates a composition giving Emacs with the given set of packages enabled:

```nix
with import <nixpkgs> { };
emacs25Packages.emacsWithPackages (packages:
  with packages; [
    ... list of emacs packages ...
  ];
}
```

!!! tip "Pro tips"
    *   The aliases `emacs` and `emacsPackages` give a default `emacs<major><minor>` and `emacsPackages<major><minor>` version.
    *   The alias `emacs<major><minor>WithPackages` is short for `emacs<major><minor>Packages.emacsWithPackages` (including default version variants).