---
title: "Visualization"
slug: "visualization"
lang: "base"

source_wiki_title: "Visualization"
source_hash: "ff0bde737d84a04ad598a73eeb85a096"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:51:15.028057+00:00"

tags:
  - software

keywords:
  - "VisIt"
  - "VTK"
  - "YT series"
  - "VNC remote desktop"
  - "ssh"
  - "cluster login node"
  - "Using YT for analysis and visualization of volumetric data"
  - "VisIt scripting"
  - "ParaViewWeb"
  - "ParaView"
  - "module load vmd"
  - "visualization workshops"
  - "Western Canada visualization training materials"
  - "OSPRay rendering"
  - "Xvfb off-screen rendering"
  - "Scientific visualization with Plotly"
  - "graphical application"
  - "VNC"
  - "interactive job salloc"
  - "NetworkX graph visualization"
  - "VMD"
  - "YT"
  - "X11-forwarding"
  - "HPC visualization"
  - "Ontario HPC Summer School 2016"

questions:
  - "What are the key features, supported platforms, and scripting capabilities of the visualization packages listed (ParaView, VisIt, VMD, VTK, and YT)?"
  - "How does client‑server interactive visualization operate on Alliance systems, and which packages (e.g., ParaView, VisIt) support this mode?"
  - "What remote visualization methods are recommended for interactive versus non‑interactive rendering on Alliance clusters, and why are X11‑forwarding and VNC considered less efficient alternatives?"
  - "How can I request an interactive job on a compute node and run a visualization program like VMD using Slurm on Trillium?"
  - "What are the recommended approaches for running graphical applications off‑screen (e.g., with Xvfb) versus using a remote desktop via VNC, and when should each method be chosen?"
  - "Where can I access visualization training resources, such as workshop slides, webinars, and video recordings for tools like VisIt, ParaView, YT, and others?"
  - "Why is VNC generally faster than X11 forwarding for heavy graphics workloads on clusters?"
  - "How can you enable X11 forwarding when connecting to a cluster using SSH, and what prerequisites are required on your local machine?"
  - "What types of graphical applications are suitable to run on the login node, and what limitations should you be aware of?"
  - "What visualization tools and topics are covered in the webinars listed on the Western Canada visualization training materials page?"
  - "Where can the video recordings and slide decks for the YT series and the Plotly webinar be accessed?"
  - "What specific subjects are addressed in the “Using YT for analysis and visualization of volumetric data” (Part 1) and “Working with data objects in YT” (Part 2) webinars?"
  - "What visualization tools and techniques are highlighted in the presentations and tutorials listed?"
  - "How can users run ParaView on Compute Canada’s HPC clusters, including client‑server and batch modes on both CPU and GPU partitions?"
  - "Where can users access additional visualization resources, community pages, and obtain technical support?"

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

There are many options for remote visualization on our systems. In general, whenever possible, for interactive rendering we recommend **client-server visualization** on interactive or high-priority nodes, and for non-interactive visualization we recommend **off-screen batch jobs** on regular compute nodes.

Other, *less efficient* options are X11-forwarding and VNC. For some packages these are the only available remote GUI options.

### Client-server interactive visualization

In the client-server mode, supported by both ParaView and VisIt, all data will be processed remotely on the cluster, using either CPU or GPU rendering, while you interact with your visualization through a familiar GUI client on your local computer. You can find the details of setting up client-server visualization in [ParaView](paraview.md) and [VisIt](visit.md) pages.

### Remote windows with X11-forwarding

In general, X11-forwarding should be avoided for any heavy graphics, as it requires many round trips and is much slower than VNC (below). However, in some cases you can connect via ssh with X11. Below we show how you would do this on our clusters. We assume you have an X-server installed on your local computer.

=== "Rorqual, Fir, Nibi, Narval"

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

=== "Trillium"

    Since runtime is limited on the login nodes, you might want to request a testing job in order to have more time for exploring and visualizing your data. On the plus side, you will have access to 40 cores on each of the nodes requested. For performing an interactive visualization session in this way please follow these steps:

    1.  ssh into `trillium.alliancecan.ca` with the `-X/-Y` flag for X11-forwarding
    2.  Request an interactive job, i.e.,
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

*   YT series: “Using YT for analysis and visualization of volumetric data” (Part 1) and "Working with data objects in YT” (Part 2)
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
*   [Trillium Quickstart#Testing and debugging](../clusters/trillium_quickstart.md#testing-and-debugging) for X11 forwarding and interactive graphical sessions on Trillium
*   [VNC](../interactive/vnc.md) for remote desktop access

## How to get visualization help
Please contact [Technical support](../support/technical_support.md).