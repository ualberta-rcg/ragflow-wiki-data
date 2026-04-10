---
title: "Using Conda in Apptainer"
tags:
  []

keywords:
  []
---

<noinclude>

</noinclude>

We will preface this tutorial on how to use Conda inside a container with the following **important notes**:

* Even inside a container, Conda should not be your preferred solution. Priority should always be given to using [modules](modules.md) from our [software stack](available_software.md), and [wheels](python.md) from our [Python wheelhouse](available_python_wheels.md). These are optimized for our systems and we are better equipped to provide support if you use them. Please [contact us](technical--support.md) if you need a module or a Python package that is not currently available on our systems.
* This tutorial will use the [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) package manager instead of Conda. If you choose to use Conda instead, keep in mind that its use is subject to [Anaconda's Terms of Service](https://legal.anaconda.com/policies/en?name=terms-of-service#terms-of-service) and might require a  [commercial license](https://www.anaconda.com/pricing/terms-of-service-faqs).
* This tutorial shows how to create a read-only image, i.e., a one-off <tt>.sif</tt> file containing a Conda environment that has everything you need to run your application. We strongly discourage installing software interactively with Conda inside a container and will not show how to do this here.

Creating an Apptainer image and using Conda to install software inside it is a 3-step process. The first step is to create a <tt>.yml</tt> file describing the Conda environment we wish to create inside the container. In the example that follows, we create the file <tt>environment.yml</tt> . This file is where we give our environment a name, then give Conda a list of packages that must be installed and the channels where to look for them. For more information [see here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

**`environment.yml`**
```yaml
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

Second, we create an Apptainer [image definition file](https://apptainer.org/docs/user/main/definition_files.html). This file, here called <tt>image.def</tt>, describes what are the steps Apptainer should take to create our image. These steps are:
#Pull a Docker image from DockerHub that has the micromamba package manager pre-installed.
#Create a copy of the Conda environment definition file <tt>environment.yml</tt> inside the container
#Call micromamba and have it configure the environment defined in <tt>environment.yml</tt>.

**`image.def`**
```yaml
Bootstrap: docker
From: mambaorg/micromamba:latest

%files
    environment.yml /environment.yml

%post
    micromamba install -n base --file environment.yml && \
        micromamba clean --all --yes
```

The last step is to build the Apptainer image using the definition file above:
   module load apptainer
   APPTAINER_BIND=' ' apptainer build image.sif image.def

You can test that your image provides `multiqc`, for example, like this:

```bash
apptainer run image.sif multiqc --help
```

```
/// MultiQC 🎃 v1.25.1
 
 Usage: multiqc [OPTIONS] [ANALYSIS DIRECTORY]
...
```