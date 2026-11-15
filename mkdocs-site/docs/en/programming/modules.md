---
title: "Modules/en"
slug: "modules"
lang: "en"

source_wiki_title: "Modules/en"
source_hash: "3455bbff2e355ccb007de55e40be87fd"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:38:29.383200+00:00"

tags:
  []

keywords:
  - "environment modules"
  - "module"
  - "Lmod modules"
  - "Python modules"
  - "virtual environment"

questions:
  - "What are Lmod (environment) modules and how do they modify the shell environment to enable specific software packages?"
  - "How does a Python module differ from a Python package, and what import statements are used to load them?"
  - "What preparation steps, such as creating a virtual environment, are required before importing Python modules from the provided pre‑compiled wheels?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

In computing, a module is a unit of software that is designed to be independent, interchangeable, and contains everything necessary to provide the desired functionality. [^1]
The term "module" may sometimes have a more specific meaning depending on the context.
This page describes a few types of modules and suggests links to further documentation content.

## Disambiguation

### Lmod modules

Also called "environment modules", Lmod modules are used to alter your (shell) environment so as to enable you to use a particular software package,
or to use a non-default version of certain common software packages such as compilers. See [Using modules](modules.md).

### Python modules

In Python, a module is a file of code (usually Python code) which can be loaded with the `import ...` or `from ... import ...` statements to provide functionality. A Python package is a collection of Python modules; the terms "package" and "module" are frequently interchanged in casual use. [^2]

Certain frequently used Python modules such as Numpy can be imported if you first load the `scipy-stack` Lmod module at the shell level.
See [SciPy stack](../software/python.md#scipy-stack) for details.

We maintain a large collection of [Python "wheels."](../software/python.md#available-wheels)
These are modules which are pre-compiled to be compatible with the [Standard software environments](standard_software_environments.md).
Before importing modules from our wheels, you should create a [virtual environment](../software/python.md#creating-and-using-a-virtual-environment).

Python modules which are not in the `scipy-stack` Lmod module or in our wheels collection can be installed from the internet
as described in the [Installing packages](../software/python.md#installing-packages) section.

## Other related topics

The main [Available software](available_software.md) page is a good starting point. Other related pages are:
*   [Standard software environments](standard_software_environments.md): as of April 1, 2021, `StdEnv/2020` is the default collection of Lmod modules
*   Tables of Lmod modules optimized for AVX, **AVX2** and **AVX512** [CPU instructions](standard_software_environments.md#performance-improvements)
*   Category 'Software': a list of different software pages in this wiki, including commercial or licensed software

## Footnotes

[^1]: [Wikipedia, "Modular programming"](https://en.wikipedia.org/wiki/Modular_programming)
[^2]: [Tutorialspoint.com, "What is the difference between a python module and a python package?"](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package)