---
title: "Anaconda"
slug: "anaconda"
lang: "base"

source_wiki_title: "Anaconda"
source_hash: "55e74e5650798fdea9f5f2f325ec3647"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:13:29.362508+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Anaconda is a Python distribution.

!!! warning "Before Using Anaconda"
    We are aware that Anaconda is widely used in several fields studied by our users (data science, AI, bioinformatics, etc.). Anaconda is an interesting solution to simplify the management of Python and libraries on a personal computer. However, on a cluster like those maintained by the Alliance, library management must be handled by our staff to ensure maximum compatibility and performance. Moreover, using Anaconda on a compute cluster can lead to several problems.

    Before using Anaconda, we ask you to contact our [technical support](technical-support.md) so our experts can explore alternatives with you. If you choose to use Anaconda, please note that our team will not be able to offer you support if you encounter issues.

## Why is Anaconda not recommended on a compute cluster?

Anaconda can be problematic on a compute cluster for several reasons:

*   Anaconda very often installs software (compilers, scientific libraries, etc.) that already exist on Alliance clusters as modules, with a configuration that is not optimal and can cause conflicts.
*   installs binaries that are not optimized for our cluster's processors. Your calculations could therefore be slower.
*   makes incorrect assumptions about library locations. You might encounter runtime errors.
*   installs into the `$HOME` directory by default, where it places a huge quantity of files. The Anaconda installation alone can take up nearly half of your file count quota in your home directory.
*   is slower for package installation.
*   modifies `$HOME/.bashrc`, which can cause conflicts.

## What are the alternatives?

The first step you should take is to contact our [technical support](technical-support.md) so our experts can explore the best alternative for your needs with you. If you prefer to try it yourself, two main options are listed below.

### Transitioning from Conda to virtualenv

[Virtualenv](python.md#creating-and-using-a-virtual-environment) offers all the features you need to use Python on our clusters. This should be the first choice you explore. Here's how to switch to virtualenv if you are using Anaconda on your personal computer:

1.  List the dependencies (requirements) of the application you want to use. To do this, you can:
    *   Run `pip show <package_name>` from your virtual environment (if the package exists on [PyPI](https://pypi.org/))
    *   Or, check if there is a `requirements.txt` file in the Git repository.
    *   Or, check the `install_requires` variable in the `setup.py` file, which lists the requirements.
2.  Find which dependencies are Python packages and which are libraries provided by Anaconda. For example, CUDA and CuDNN are libraries available on Anaconda Cloud, but which you should not install yourself on our clusters. They are already installed.
3.  Remove anything that is not a Python package from the dependency list (for example, remove `cudatoolkit` and `cudnn`).
4.  Use a [virtualenv](python.md#creating-and-using-a-virtual-environment), in which you will install these dependencies.

Your application should now work. If it doesn't, please do not hesitate to contact our [technical support](technical-support.md).

### Using Apptainer

In some situations, the complexity of a software's dependencies requires a solution where the environment can be fully controlled. For these situations, we recommend the [Apptainer](apptainer.md#working-with-conda) tool: note that a Docker image can be converted to an Apptainer image. The only drawback of Apptainer is that images consume a lot of disk space, so if your research group plans to use multiple images, it would be wise to group them together in a single directory within the group's project space to avoid duplicates.

[Using Conda in Apptainer](using-conda-in-apptainer.md)