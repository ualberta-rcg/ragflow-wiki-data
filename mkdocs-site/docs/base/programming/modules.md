---
title: "Modules"
slug: "modules"
lang: "base"

source_wiki_title: "Modules"
source_hash: "83510c441d4cf38974066ce2e04632ea"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:36:07.902341+00:00"

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

In computing, a module is a unit of software that is designed to be independent, interchangeable, and contains everything necessary to provide the desired functionality.[^1] The term "module" may sometimes have a more specific meaning depending on the context. This page describes a few types of modules and suggests links to further documentation content.

## Disambiguation

### Lmod modules

Also called "environment modules", Lmod modules are used to alter your (shell) environment so as to enable you to use a particular software package, or to use a non-default version of certain common software packages such as compilers. See [Using modules](using-modules.md).

### Python modules

In Python, a module is a file of code (usually Python code) which can be loaded with the `import ...` or `from ... import ...` statements to provide functionality. A Python package is a collection of Python modules; the terms "package" and "module" are frequently interchanged in casual use.[^2]

Certain frequently used Python modules such as Numpy can be imported if you first load the `scipy-stack` Lmod module at the shell level. See [SciPy stack](python.md#scipy-stack) for details.

We maintain a large collection of [Python "wheels."](python.md#available-wheels) These are modules which are pre-compiled to be compatible with the [Standard software environments](standard-software-environments.md). Before importing modules from our wheels, you should create a [virtual environment](python.md#creating-and-using-a-virtual-environment).

Python modules which are not in the `scipy-stack` Lmod module or in our wheels collection can be installed from the internet as described in the [Installing packages](python.md#installing-packages) section.

## Other related topics

The main [Available software](available-software.md) page is a good starting point. Other related pages are:
* [Standard software environments](standard-software-environments.md): as of April 1, 2021, `StdEnv/2020` is the default collection of Lmod modules
* Lmod [modules specific to Niagara](modules-specific-to-niagara.md)
* Tables of Lmod modules optimized for [AVX](modules-avx.md), **[AVX2](modules-avx2.md)** and **[AVX512](modules-avx512.md)** [CPU instructions](standard-software-environments.md#performance-improvements)
* [Category *Software*](category-software.md): a list of different software pages in this wiki, including commercial or licensed software

## Footnotes

[^1]: [Wikipedia, "Modular programming"](https://en.wikipedia.org/wiki/Modular_programming)
[^2]: [Tutorialspoint.com, "What is the difference between a python module and a python package?"](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package)