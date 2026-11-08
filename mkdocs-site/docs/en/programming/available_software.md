---
title: "Available software/en"
slug: "available_software"
lang: "en"

source_wiki_title: "Available software/en"
source_hash: "0f2bdf907d3ac8f1f43dc867005e4054"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:50:15.883439+00:00"

tags:
  []

keywords:
  - "computational chemistry"
  - "distributed file system"
  - "Galaxy workflow platform"
  - "Apptainer"
  - "standard software environments"
  - "license restrictions"
  - "software installed locally"
  - "software modules"
  - "AVX512"
  - "Gaussian software"
  - "site-specific software"
  - "AVX2"
  - "CVMFS"

questions:
  - "How do users load and access software packages on the national systems using modules and the Lmod system?"
  - "What steps must be taken to obtain access to software that requires a license or is only available at specific sites?"
  - "Where are Python, R, and Perl packages stored, and how should users install or manage these packages on the clusters?"
  - "Which software modules are listed as installed locally and what categories (chem, phys, bio) do they belong to?"
  - "On which clusters (Nibi or Fir) are the listed software packages deployed?"
  - "According to the introductory note, what is the primary reason some packages might not be available for installation?"
  - "What is the role of CVMFS in managing most application software across sites?"
  - "Which processor instruction set modules are listed under the AVX512 and AVX2 tabs?"
  - "Why are certain packages installed only at specific sites rather than through CVMFS?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Availability"
    **Some software listed below may not be available in the specific StdEnv you have loaded.**

    `StdEnv/2020` is now deprecated/hidden on the newer systems. See [StdEnv/2020](standard_software_environments.md)

## Notes
Except for basic system programs, you access most software by loading a **module**. See [Using modules](modules.md) for more on how to use the Lmod module system. Note that some prerequisite modules are loaded by default.

Here are a few things to know about the available software:
* Most [Python](../software/python.md) modules are not installed as (Lmod) modules. They are instead provided as binary [wheels](available_python_wheels.md), stored on our systems under `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`. One such package is [TensorFlow](../software/tensorflow.md). For instructions on how to install or list Python packages, see the [Python](../software/python.md) page.
* Similarly, most [R](../software/r.md) or [Perl](../software/perl.md) packages are not installed either. We recommend installing them in your personal or group file space. See the [R](../software/r.md) and [Perl](../software/perl.md) pages for instructions on how to do so.
* A page discusses [symbolic algebra software](../software/symbolic_algebra_software.md) like Mathematica and Sage.
* Note that [Docker](https://www.docker.com/) is not available on our clusters but [Apptainer](../software/containers/apptainer.md) is available by loading the module `apptainer`. Docker containers can be converted to Apptainer as discussed [here](https://apptainer.org/docs/).
* Some of the software packages listed below are not immediately usable because they require you to have a license. You may need to be granted access to them by us. Attempting to load the module for one of these will give you instructions on what to do to obtain access.
* While the vast majority of the software packages below are accessible on all our servers, a few are only available at one site or another due to licensing restrictions. See [Site-specific software](#site-specific-software) below.
* The packages listed below are available in one or more [standard software environments](standard_software_environments.md). In rare circumstances it may be necessary to load a different standard environment (StdEnv) to access a particular version of a particular package. For more on this please read [Standard software environments](standard_software_environments.md).
* Many packages related to the operating system, such as [Autotools](autotools.md), [Make](make.md), [Git](../software/git.md), and others, are not installed as modules but are part of the default environment. These are not listed below.

## List of globally-installed modules
The table below lists software for which an environment module has been installed on our systems. In simple cases, the module name listed in the *Module* column can be used with the `module load` command to configure your environment. In more complicated cases, some prerequisite modules may also need to be loaded. Click on the corresponding *[Expand]* link in the *Description* column for a list of prerequisites and brief notes about the software. If more extensive documentation about a package is available, there will be a link in the *Documentation* column. Click the double arrows in the column heading to sort in ascending or descending order for a given column. In particular, sorting by software type might be of interest. The *Type* column shows the software tagged as: ai (artificial intelligence), bio (biology, bioinformatics), chem (chemistry), geo (earth sciences), io (input/output), math (mathematics), mpi ([MPI](../software/mpi.md)), phys (physics and engineering), tools (languages and libraries), vis ([visualization](../software/visualization.md)).

Software for legacy architectures can be found on their respective pages: AVX and SSE3.

### AVX512 (Fir, Nibi, Rorqual, Trillium, Killarney, tamIA, Vulcan)
<!-- The table content for AVX512 modules (originally from Modules_avx512) would appear here. As the content was transcluded from an external MediaWiki page, it is not available for direct conversion in this document. -->

### AVX2 (Narval)
<!-- The table content for AVX2 modules (originally from Modules_avx2) would appear here. As the content was transcluded from an external MediaWiki page, it is not available for direct conversion in this document. -->

## Site-specific software
Most application software is installed in CVMFS, a distributed file system which makes central management of the many packages easier.
Certain packages, however, are not installed in CVMFS but are installed only at some sites, or are installed separately at each site.
This is usually due to license restrictions on the package in question.
Such packages are listed in the following table.

List of software installed locally

| Module           | Type  | Documentation                 | Cluster | Description                                                                                                                                                                                                                                 |
| :--------------- | :---- | :---------------------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| adf/2016.106     | chem  | [ADF](../software/adf.md)                 | Nibi    | Amsterdam Density Functional Modeling Suite, computational chemistry software                                                                                                                                                               |
| adf/2017.207     | chem  | [ADF](../software/adf.md)                 | Nibi    | Amsterdam Density Functional Modeling Suite, computational chemistry software                                                                                                                                                               |
| adf/2018.104     | chem  | [ADF](../software/adf.md)                 | Nibi    | Amsterdam Density Functional Modeling Suite, computational chemistry software                                                                                                                                                               |
| adf/2019.305     | chem  | [ADF](../software/adf.md)                 | Nibi    | Amsterdam Density Functional Modeling Suite, computational chemistry software                                                                                                                                                               |
| ams/2020.102     | chem  | [AMS](../software/ams.md)                 | Nibi    | Amsterdam Modeling Suite products                                                                                                                                                                                                           |
| amber/16         | chem  | [AMBER](../software/amber.md)             | Nibi    | The Amber Molecular Dynamics Package                                                                                                                                                                                                        |
| dirac/16.0       | phys  |                               | Fir     | The DIRAC program computes molecular properties using relativistic quantum chemical methods. Homepage: http://diracprogram.org                                                                                                                  |
| dirac/17.0       | phys  |                               | Fir     | The DIRAC program computes molecular properties using relativistic quantum chemical methods. Homepage: http://diracprogram.org                                                                                                                  |
| galaxy/20.01     | bio   |                               | Fir     | Galaxy is a scientific workflow, data integration, and data and analysis persistence and publishing platform that aims to make computational biology accessible to research scientists that do not have computer programming or systems administration experience. Any group on Fir can have one Galaxy instance. The Galaxy instance will be run under a shared account which will be created by admins. Please contact [technical support](../support/technical_support.md) to set up Galaxy for you. Homepage: https://usegalaxy.org/ |
| gaussian/g03.d01 | chem  | [Gaussian](../software/gaussian.md)       | Nibi    | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g09.e01 | chem  | [Gaussian](../software/gaussian.md)       | Nibi    | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g16.b01 | chem  | [Gaussian](../software/gaussian.md)       | Nibi    | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g16.c01 | chem  | [Gaussian](../software/gaussian.md)       | Nibi    | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g03.d01 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g09.b01 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g09.e01 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g16.a03 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g16.b01 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gaussian/g16.c01 | chem  | [Gaussian](../software/gaussian.md)       | Fir     | Gaussian is a general-purpose computational chemistry software package. Homepage: http://gaussian.com/                                                                                                                                      |
| gbrowse/2.56     | bio   | [GBrowse](../software/bioinformatics/gbrowse.md)         | Fir     | GBrowse is a combination of database and interactive web pages for manipulating and displaying annotations on genomes. Homepage: http://gmod.org/wiki/GBrowse                                                                                        |
| TPP/5.1.0        | bio   |                               | Fir     | The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics, developed at the SPC. On Fir we can also provide TPP web interface (tpp_gui) per group upon user request                                                  |