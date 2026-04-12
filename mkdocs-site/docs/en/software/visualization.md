---
title: "Visualization/en"
slug: "visualization"
lang: "en"

source_wiki_title: "Visualization/en"
source_hash: "6113c9c0a49e56bcfd4356e4aa1e9f62"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:46:41.015570+00:00"

tags:
  - software

keywords:
  - "testing job"
  - "VNC"
  - "Client-Server and VNC"
  - "visualization packages"
  - "graphical application"
  - "ParaView"
  - "Visualization"
  - "Remote visualization"
  - "login nodes"
  - "3D scientific visualization"
  - "Complex Networks Visualization"
  - "remote visualization"
  - "salloc"
  - "SciNet User Group Meeting"
  - "VisIt Basics"
  - "SciNet HPC"
  - "Python"
  - "Tkinter"
  - "University of Toronto"
  - "VisIt"
  - "interactive visualization session"
  - "Xvfb"
  - "Alliance systems"

questions:
  - "What are the primary features and specific use cases of the different visualization packages, such as ParaView, VMD, and YT, described in the text?"
  - "What are the recommended approaches for conducting interactive versus non-interactive remote visualization on Alliance systems?"
  - "Why is X11-forwarding generally discouraged for heavy graphics, and how can a user configure it for interactive sessions on compute nodes?"
  - "How can a user set up an interactive session with X11-forwarding to run visualization programs like VMD?"
  - "What is the process for running off-screen rendering jobs using the X virtual frame buffer (Xvfb) on either a CPU or GPU?"
  - "Why is VNC recommended over X11-forwarding for remote desktops, and what visualization training resources are available to users?"
  - "How do you use the `salloc` command to properly allocate resources and launch a graphical application like VMD?"
  - "Why is it recommended to request a testing job for data visualization instead of using the login nodes?"
  - "What computational advantages, such as core count, do you gain by requesting a testing job on the Trillium system?"
  - "What topics were covered in the October 2015 presentation by Ramses van Zon at the SciNet User Group Meeting?"
  - "Who presented the slides on \"VisIt Basics\" and during which meeting did this presentation take place?"
  - "Which programming language is featured in Marcelo Ponce's presentation on visualizing complex networks?"
  - "How can users contribute their own visualization scripts and workflows to the page?"
  - "What specific visualization resources and software are provided through the SciNet HPC links?"
  - "Who should users contact if they need help with visualization?"
  - "How can users contribute their own visualization scripts and workflows to the page?"
  - "What specific visualization resources and software are provided through the SciNet HPC links?"
  - "Who should users contact if they need help with visualization?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Popular visualization packages

### ParaView
[ParaView](http://www.paraview.org) is a general-purpose 3D scientific visualization tool. It is open-source and compiles on all popular platforms (Linux, Windows, Mac), understands a large number of input file formats, provides multiple rendering modes, supports Python scripting, and can scale up to tens of thousands of processors for rendering of very large datasets.

*   [Using ParaView on Alliance systems](paraview.md)
*   [ParaView official documentation](http://www.paraview.org/documentation)
*   [ParaView gallery](http://www.paraview.org/gallery)
*   [ParaView wiki](http://www.paraview.org/Wiki/ParaView)
*   [ParaView Python scripting](http://www.paraview.org/Wiki/ParaView/Python_Scripting)

### VisIt
Similar to ParaView, [VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/) is an open-source, general-purpose 3D scientific data analysis and visualization tool that scales from interactive analysis on laptops to very large HPC projects on tens of thousands of processors.

*   [Using VisIt on Alliance systems](visit.md)
*   [VisIt website](https://visit-dav.github.io/visit-website)
*   [VisIt gallery](https://visit-dav.github.io/visit-website/examples)
*   [VisIt user community wiki](http://www.visitusers.org)
*   [VisIt tutorials](http://www.visitusers.org/index.php?title=VisIt_Tutorial) along with [sample datasets](http://www.visitusers.org/index.php?title=Tutorial_Data)

### VMD
[VMD](http://www.ks.uiuc.edu/Research/vmd) is an open-source molecular visualization program for displaying, animating, and analyzing large biomolecular systems in 3D. It supports scripting in Tcl and Python and runs on a variety of platforms (MacOS X, Linux, Windows). It reads many molecular data formats using an extensible plugin system and supports a number of different molecular representations.

*   [Using VMD on Alliance systems](vmd.md)
*   [VMD User's Guide](http://www.ks.uiuc.edu/Research/vmd/current/ug)

### VTK
The Visualization Toolkit (VTK) is an open-source package for 3D computer graphics, image processing, and visualization. The toolkit includes a C++ class library as well as several interfaces for interpreted languages such as Tcl/Tk, Java, and Python. VTK was the basis for many excellent visualization packages including ParaView and VisIt.

*   [Using VTK on Alliance systems](vtk.md)
*   [VTK tutorials](https://itk.org/Wiki/VTK/Tutorials)

### YT
YT is a Python library for analyzing and visualizing volumetric, multi-resolution data. Initially developed for astrophysical simulation data, it can handle any uniform and multiple-resolution data on Cartesian, curvilinear, unstructured meshes and on particles.

*   [Using YT on Alliance systems](yt.md)

## Visualization on Alliance systems

!!! note "Recommendation for Visualization on Alliance Systems"
    There are many options for remote visualization on our systems. In general, whenever possible:
    *   For interactive rendering, we recommend **client-server visualization** on interactive or high-priority nodes.
    *   For non-interactive visualization, we recommend **off-screen batch jobs** on regular compute nodes.

!!! warning "Less Efficient Options"
    Other, *less efficient* options are X11-forwarding and VNC. For some packages these are the only available remote GUI options.

### Client-server interactive visualization

In the client-server mode, supported by both [ParaView](paraview.md) and [VisIt](visit.md), all data will be processed remotely on the cluster, using either CPU or GPU rendering, while you interact with your visualization through a familiar GUI client on your local computer. You can find the details of setting up client-server visualization in the [ParaView](paraview.md) and [VisIt](visit.md) pages.

### Remote windows with X11-forwarding

In general, X11-forwarding should be avoided for any heavy graphics, as it requires many round trips and is much slower than VNC (below). However, in some cases you can connect via ssh with X11. Below we show how you would do this on our clusters. We assume you have an X-server installed on your local computer.

#### Rorqual, Fir, Nibi, Narval

Connect to the cluster with the `-X/-Y` flag for X11-forwarding. You can start your graphical application on the login node (small visualizations)

```bash
module load vmd
vmd
```

or you can request interactive resources on a compute node (large visualizations)

```bash
salloc --time=1:00:0 --ntasks=1 --mem=3500 --account=def-someprof --x11
```

and, once the job is running, start your graphical application inside the job

```bash
module load vmd
vmd
```

#### Trillium

Since runtime is limited on the login nodes, you might want to request a testing job in order to have more time for exploring and visualizing your data. On the plus side, you will have access to 40 cores on each of the nodes requested. For performing an interactive visualization session in this way please follow these steps:

1.  ssh into trillium.alliancecan.ca with the `-X/-Y` flag for X11-forwarding
2.  Request an interactive job, ie.

    ```bash
    debugjob
    ```

    This will connect you to a node, let's say for the argument "niaXYZW".
3.  Run your visualization program, e.g., VMD

    ```bash
    module load vmd
    vmd
    ```

4.  Exit the debug session.

### Remote off-screen windows via Xvfb

Some applications insist on displaying graphical output, but you don't actually need to see them since the results are saved in a file. To work with offscreen rendering, the job can run as a regular batch job, using either the CPU or the GPU for 3D rendering. To enable this you can run the application you are calling with the X virtual frame buffer (Xvfb) in a job script as follows:

```bash
xvfb-run <name-of-application>
```

if using the CPU for rendering or

```bash
xvfb-run vglrun -d egl <name-of-application>
```

if using the GPU for rendering, in which case you need to reserve one GPU with Slurm, see [Using GPUs with Slurm](../running-jobs/using_gpus_with_slurm.md). Note that, depending on the workload the GPU may not necessarily be faster than the CPU, so it's important to benchmark before committing to using the more expensive GPU.

### Start a remote desktop via VNC

Frequently, it may be useful to start up graphical user interfaces for various software packages like Matlab. Doing so over X11-forwarding can result in a very slow connection to the server. Instead, we recommend using VNC to start and connect to a remote desktop. For more information, please see [the article on VNC](../interactive/vnc.md).

## Visualization training

Please [let us know](mailto:support@tech.alliancecan.ca) if you would like to see a visualization workshop at your institution.

### Full- or half-day workshops

*   [VisIt workshop slides](https://docs.alliancecan.ca/mediawiki/images/5/5d/Visit201606.pdf) from HPCS'2016 in Edmonton by *Marcelo Ponce* and *Alex Razoumov*
*   [ParaView workshop slides](https://docs.alliancecan.ca/mediawiki/images/6/6c/Paraview201707.pdf) from July 2017 by *Alex Razoumov*
*   [Gnuplot, xmgrace, remote visualization tools (X-forwarding and VNC), python's matplotlib](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-I.pdf) slides by *Marcelo Ponce* (SciNet/UofT) from Ontario HPC Summer School 2016
*   [Brief overview of ParaView & VisIt](https://support.scinet.utoronto.ca/~mponce/courses/ss2016/ss2016_visualization-II.pdf) slides by *Marcelo Ponce* (SciNet/UofT) from Ontario HPC Summer School 2016

### Webinars and other short presentations

[Western Canada visualization training materials page](https://training.westdri.ca/tools/visualization) has video recordings and slides from many visualization webinars including:

*   YT series: "Using YT for analysis and visualization of volumetric data" (Part 1) and "Working with data objects in YT” (Part 2)
*   “Scientific visualization with Plotly”
*   “Novel Visualization Techniques from the 2017 Visualize This Challenge”
*   “Data Visualization on Compute Canada’s Supercomputers” contains recipes and demos of running client-server ParaView and batch ParaView scripts on both CPU and GPU partitions of our HPC clusters
*   “Using ParaViewWeb for 3D Visualization and Data Analysis in a Web Browser”
*   “Scripting and other advanced topics in VisIt visualization”
*   “CPU-based rendering with OSPRay”
*   “3D graphs with NetworkX, VTK, and ParaView”
*   “Graph visualization with Gephi”

Other visualization presentations:

*   [Remote Graphics on SciNet's GPC system (Client-Server and VNC)](https://oldwiki.scinet.utoronto.ca/wiki/images/5/51/Remoteviz.pdf) slides by *Ramses van Zon* (SciNet/UofT) from October 2015 SciNet User Group Meeting
*   [VisIt Basics](https://support.scinet.utoronto.ca/education/go.php/242/file_storage/index.php/download/1/files%5B%5D/6399/), slides by *Marcelo Ponce* (SciNet/UofT) from February 2016 SciNet User Group Meeting
*   [Intro to Complex Networks Visualization, with Python](https://oldwiki.scinet.utoronto.ca/wiki/images/e/ea/8_ComplexNetworks.pdf), slides by *Marcelo Ponce* (SciNet/UofT)
*   [Introduction to GUI Programming with Tkinter](https://oldwiki.scinet.utoronto.ca/wiki/images/9/9c/Tkinter.pdf), from Sept.2014 by *Erik Spence* (SciNet/UofT)

## Tips and tricks

This section will describe visualization workflows not included into the workshop/webinar slides above. It is meant to be user-editable, so please feel free to add your cool visualization scripts and workflows here so that everyone can benefit from them.

## Regional and other visualization pages

*   [**National Visualization Team's page**](https://ccvis.netlify.app) with many sci-vis examples
*   [SFU's visualization webinars archive](https://training.westdri.ca/tools/visualization)

### [SciNet HPC at the University of Toronto](http://www.scinet.utoronto.ca)

*   [Visualization in Niagara](https://docs.scinet.utoronto.ca/index.php/Visualization)
*   [Visualization software](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Software_and_Libraries#anchor_viz)
*   [VNC](https://oldwiki.scinet.utoronto.ca/wiki/index.php/VNC)
*   [Visualization nodes](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Visualization_Nodes)
*   [Further resources and viz-tech talks](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Knowledge_Base:_Tutorials_and_Manuals#Visualization)
*   [Using ParaView](https://oldwiki.scinet.utoronto.ca/wiki/index.php/Using_Paraview)

## How to get visualization help

Please contact [Technical support](../support/technical_support.md).