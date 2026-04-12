---
title: "Anaconda/en"
slug: "anaconda"
lang: "en"

source_wiki_title: "Anaconda/en"
source_hash: "9b4e9f2c8f0207d7b401d92609f9db39"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:07:23.201980+00:00"

tags:
  - software

keywords:
  - "cluster"
  - "virtual environment"
  - "Anaconda"
  - "Python"
  - "Apptainer"

questions:
  - "Why is the use of Anaconda discouraged on the computing clusters?"
  - "How can a user transition their workflow from Conda to a Python virtual environment?"
  - "When is Apptainer recommended as an alternative to Anaconda, and what is its primary disadvantage?"
  - "Why is the use of Anaconda discouraged on the computing clusters?"
  - "How can a user transition their workflow from Conda to a Python virtual environment?"
  - "When is Apptainer recommended as an alternative to Anaconda, and what is its primary disadvantage?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Anaconda is a Python distribution.

!!! warning "Before using Anaconda"
    We are aware of the fact that Anaconda is widely used in several domains, such as data science, AI, bioinformatics, etc. Anaconda is a useful solution for simplifying the management of Python and scientific libraries on a personal computer. However, on a cluster like those supported by the Alliance, the management of these libraries and dependencies should be done by our staff, in order to ensure compatibility and optimal performance. Moreover, using Anaconda on a cluster may lead to multiple problems.
    Before using Anaconda, we ask that you contact our [Technical support](../support/technical_support.md), so that our experts can investigate alternatives with you. If you choose to use Anaconda regardless, note that our team may not be able to support you if you encounter issues.

## Why is Anaconda not recommended on a cluster?

Anaconda may cause issues on a cluster for multiple reasons:

*   Anaconda very often installs software (compilers, scientific libraries, etc.) which already exist on our clusters as modules, with a configuration that is not optimal, and which may cause conflicts.
*   It installs binaries which are not optimized for the processor architecture on our clusters. Your jobs may be slower because of it.
*   It makes incorrect assumptions about the location of various system libraries. Your jobs may encounter errors when running.
*   Anaconda uses the `$HOME` directory for its installation, where it writes an enormous number of files. A single Anaconda installation can easily absorb almost half of your quota for the number of files in your home directory.
*   Anaconda is slower than the installation of packages via Python wheels.
*   Anaconda modifies the `$HOME/.bashrc` file, which can easily cause conflicts.

## What are alternatives?
The first step you should take is to contact our [Technical support](../support/technical_support.md), so that our experts investigate with your what is the best alternative for your needs. If you prefer to attempt it yourself, two main options are listed below.

### Transition from Conda to virtualenv

A [virtual environment](python.md#creating-and-using-a-virtual-environment) offers you all the functionality which you need to use Python on our clusters. This should be the first option that you explore. Here is how to convert to the use of virtual environments if you use Anaconda on your personal computer:

1.  List the dependencies (requirements) of the application you want to use. To do so, you can:
    1.  Run `pip show <package_name>` from your virtual environment (if the package exists on [PyPI](https://pypi.org/))
    2.  Or, check if there is a `requirements.txt` file in the Git repository.
    3.  Or, check the variable `install_requires` of the file `setup.py`, which lists the requirements.
2.  Find which dependencies are Python modules and which are libraries provided by Anaconda. For example, CUDA and CuDNN are libraries which are available on Anaconda Cloud but which you should not install yourself on our clusters - they are already installed.
3.  Remove from the list of dependencies everything which is not a Python module (e.g. `cudatoolkit` and `cudnn`).
4.  Use a [virtual environment](python.md#creating-and-using-a-virtual-environment) in which you will install your dependencies.

Your software should run - if it doesn't, don't hesitate to [contact us](../support/technical_support.md).

### Using Apptainer

In some situations, the complexity of the dependencies of a program requires the use of a solution where you can control the entire software environment. In these situations, we recommend the tool [Apptainer](containers/apptainer.md#using-conda-in-apptainer); note that a Docker image can be converted into an Apptainer image. The only disadvantage of Apptainer is its consumption of disk space. If your research group plans on using several images, it would be wise to collect all of them together in a single directory of the group's project space to avoid duplication.