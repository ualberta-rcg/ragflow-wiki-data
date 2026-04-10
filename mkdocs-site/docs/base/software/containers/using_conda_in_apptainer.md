---
title: "Using Conda in Apptainer"
slug: "using_conda_in_apptainer"
lang: "base"

source_wiki_title: "Using Conda in Apptainer"
source_hash: "e413f33bda79b81ff2b9b49decd0cdd8"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:13:55.850239+00:00"

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

# Using Conda in Apptainer

!!! important "Important Notes"
    We will preface this tutorial on how to use Conda inside a container with the following **important notes**:

    *   Even inside a container, Conda should not be your preferred solution. Priority should always be given to using [modules](modules.md) from our [software stack](available-software.md), and [wheels](python.md) from our [Python wheelhouse](available-python-wheels.md). These are optimized for our systems and we are better equipped to provide support if you use them. Please [contact us](technical-support.md) if you need a module or a Python package that is not currently available on our systems.
    *   This tutorial will use the [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) package manager instead of Conda. If you choose to use Conda instead, keep in mind that its use is subject to [Anaconda's Terms of Service](https://legal.anaconda.com/policies/en?name=terms-of-service#terms-of-service) and might require a [commercial licence](https://www.anaconda.com/pricing/terms-of-service-faqs).
    *   This tutorial shows how to create a read-only image, i.e., a one-off `.sif` file containing a Conda environment that has everything you need to run your application. We strongly discourage installing software interactively with Conda inside a container and will not show how to do this here.

Creating an Apptainer image and using Conda to install software inside it is a 3-step process. The first step is to create a `.yml` file describing the Conda environment we wish to create inside the container. In the example that follows, we create the file `environment.yml`. This file is where we give our environment a name, then give Conda a list of packages that must be installed and the channels where to look for them. For more information [see here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

```yaml title="environment.yml"
name: base
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python
  - pip
  - star
  - bwa
  - multiqc
```

Second, we create an Apptainer [image definition file](https://apptainer.org/docs/user/main/definition_files.html). This file, here called `image.def`, describes what are the steps Apptainer should take to create our image. These steps are:
1.  Pull a Docker image from DockerHub that has the micromamba package manager pre-installed.
2.  Create a copy of the Conda environment definition file `environment.yml` inside the container
3.  Call micromamba and have it configure the environment defined in `environment.yml`.

```yaml title="image.def"
Bootstrap: docker
From: mambaorg/micromamba:latest

%files
    environment.yml /environment.yml

%post
    micromamba install -n base --file environment.yml && \
        micromamba clean --all --yes
```

The last step is to build the Apptainer image using the definition file above:

```bash
module load apptainer
APPTAINER_BIND=' ' apptainer build image.sif image.def
```

You can test that your image provides `multiqc`, for example, like this:

```bash
apptainer run image.sif multiqc --help
```
```text
/// MultiQC 🎃 v1.25.1

Usage: multiqc [OPTIONS] [ANALYSIS DIRECTORY]
...