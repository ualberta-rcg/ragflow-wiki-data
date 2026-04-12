---
title: "Migration to the new standard environment"
slug: "migration_to_the_new_standard_environment"
lang: "base"

source_wiki_title: "Migration to the new standard environment"
source_hash: "cbce9d496f502849bbb90fdcb876e48d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:07:11.346348+00:00"

tags:
  []

keywords:
  - "StdEnv/2023"
  - "HPC clusters"
  - "module load"
  - "recompile code"
  - "standard environment"

questions:
  - "How does the transition to the new default StdEnv/2023 environment affect my existing compiled code and installed packages?"
  - "What steps must be taken to override the default settings and continue using an older standard environment for an existing workflow?"
  - "What are the rules and best practices regarding mixing modules from different environments or loading them in a .bashrc file?"
  - "How does the transition to the new default StdEnv/2023 environment affect my existing compiled code and installed packages?"
  - "What steps must be taken to override the default settings and continue using an older standard environment for an existing workflow?"
  - "What are the rules and best practices regarding mixing modules from different environments or loading them in a .bashrc file?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## What are the differences between StdEnv/2023 and the earlier environments?
The differences are discussed in [Standard software environments](../programming/standard_software_environments.md).

## Can I change my default standard environment?
After April 1, 2024, **`StdEnv/2023` will be the default environment for all clusters.** However, you can specify your own default environment at any time by modifying the `$HOME/.modulerc` file. For example, running the following command will set your default environment to `StdEnv/2020`:

```bash
echo "module-version StdEnv/2020 default" >> $HOME/.modulerc
```
You must log out and log in again for this change to take effect.

## Do I need to reinstall/recompile my code when the StdEnv changes?
Yes. If you compile your own code, or have installed R or Python packages, you should recompile your code or reinstall the packages you need with the newest version of the standard environment.

## How can I use an earlier environment?
If you have an existing workflow and want to continue to use the same software versions you are using now, simply add
```bash
module load StdEnv/2020
```
to your job scripts before loading any other modules.

## Will the earlier environments be removed?
The earlier environments and any software dependent on them will remain available, **but versions 2016.4 and 2018.3 are no longer supported**, and we recommend not using them. Our staff will only install software in the new environment 2023.

## Can I mix modules from different environments?
!!! warning "Mixing modules from different environments"
    You should use a single environment for a given job. Different jobs can use different standard environments by explicitly loading one or the other at the job's beginning, but within a single job, you should only use a single environment. The results of trying to mix different environments are unpredictable but in general will lead to errors of one kind or another.

## Which environment should I use?
If you are starting a new project, or if you want to use a newer version of an application, you should use `StdEnv/2023` by adding
```bash
module load StdEnv/2023
```
to your job scripts. This command does not need to be deleted to use `StdEnv/2023` after April 1.

## Can I keep using an older environment by loading modules in my .bashrc?
!!! warning "Loading modules in .bashrc"
    Loading modules in your `.bashrc` is **not recommended**. Instead, explicitly load modules in your job scripts.

## I don't use the HPC clusters but cloud resources only. Do I need to worry about this?
No, this change will only affect the [available software](../programming/available_software.md) accessed by [using environment modules](using-modules.md).

## I can no longer load a module that I previously used
More recent versions of most applications are installed in the new environment. To see the available versions, run the `module avail` command. For example,

```bash
module avail gcc
```
shows several versions of the GCC compilers, which may be different from those in earlier environments.