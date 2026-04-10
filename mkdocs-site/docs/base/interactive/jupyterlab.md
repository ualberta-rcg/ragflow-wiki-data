---
title: "JupyterLab"
tags:
  []

keywords:
  []
---

= JupyterLab = 
JupyterLab is the recommended general-purpose user interface to use on a JupyterHub.
From a JupyterLab server, you can manage your remote files and folders,
and you can launch Jupyter applications like a terminal, (Python 3) notebooks, RStudio and a Linux desktop.

You can add your own "kernels", which appear as application tiles described below.  To configure such kernels, please see [Adding kernels](jupyternotebook#adding_kernels.md).

## Launching JupyterLab 
There are a few ways to launch JupyterLab. 

The traditional way would be to use [JupyterHub](jupyterhub#jupyterhub-on-clusters.md), but more recently, sites have deployed Open OnDemand which sometimes can launch the interface below. In the table below, the column "Fully-featured" indicates whether the JupyterLab interface available has all of the features described below. If there is a link, it is to that cluster's JupyterHub or Open OnDemand server.

{| class="wikitable" style="text-align: center;"
|+
!Cluster
! colspan="2" |JupyterHub
! colspan="3" |Open OnDemand
|-
|
|Available
|Fully-featured
|Available
|JupyterLab
|Fully-featured
|-
|Fir
| colspan="2" |[Yes](https://jupyterhub.fir.alliancecan.ca/)
| colspan="3" |No
|-
|Killarney
| colspan="2" |No
| colspan="3" |No
|-
|Narval
| colspan="2" | [Yes](https://jupyterhub.narval.alliancecan.ca/)
| colspan="3" |No
|-
|Nibi
| colspan="2" |No
| colspan="3" |[Yes](https://ondemand.sharcnet.ca/)
|-
|Rorqual
| colspan="2" |[Yes](https://jupyterhub.rorqual.alliancecan.ca/) 
| colspan="3" |No
|-
|tamIA
| colspan="2" |No
| colspan="3" |No
|-
|Trillium
| colspan="2" |No
| colspan="3" |[Yes](http://ondemand.scinet.utoronto.ca/), request "Jupyter Lab + Alliance software extensions"
|-
|Vulcan
| colspan="2" |No
| colspan="3" |[Yes](https://vulcan.alliancecan.ca/)
|}

It is also possible to launch JupyterLab by [installing it yourself in a virtual environment](advanced-jupyter-configuration.md), but this is not recommended. You will also not benefit from any of the pre-configured applications described below.

== The JupyterLab interface == 

When you open JupyterLab in one of our most recent clusters, you will be presented with a dashboard pre-populated with a few launchers. Default launchers include Python 3.11, LibreQDA, Mate Desktop (VNC), OpenRefine, RStudio, VS Code and XFCE4 Desktop (VNC). In addition, you may find links to the cluster's [Globus](globus.md) collection, to the cluster's job portal, as well as links to relevant documentation pages. By loading modules, you will see new launchers appear in the dashboard (see below). 

In the menu bar on the top, please note that in order to close your session, you may do so through the *File* menu: 
* <i>Hub Control Panel</i>: if you want to manually stop the JupyterLab server and the corresponding job on the cluster. This is useful when you want to start a new JupyterLab server with more or less resources.
* <i>Log Out</i>: the session will end, which will also stop the JupyterLab server and the corresponding job on the cluster.
Most other menu items are related to notebooks and Jupyter applications.
[none|thumb|750x750px|Default home tab when JupyterLab is loaded](file:jupyterlab-launcher-with-modules.png.md)

### Tool selector on left 
On the left side of the interface, you will find the tool selector. This changes the content of the frame on the right. The most relevant ones are:

#### <i>File Browser</i> (folder icon) 
This is where you can browse in your home, project and scratch spaces. It is also possible to use it to upload files.
[alt=File browser|none|frame|File browser](file:file-browser.png.md)

#### <i>Running Terminals and Kernels</i> (stop icon)  
This is to stop kernel sessions and terminal sessions

#### <i>GPU Dashboards</i> (GPU card icon)  
If your job uses GPUs, this will give you access to some resource monitoring options.

#### <i>Software Modules</i> 
[alt=Software module selector|none|thumb|Software module selector](file:software-module-selector.png.md)
This is where you can load or unload [software modules](available-software.md) available in our environment. Depending on the modules loaded, icons directing to the corresponding [Jupyter applications](#prebuilt_applications.md) will appear in the <i>Launcher</i> tab. By default, we load a number of modules to provide you access to basic tools. 

The search box can search for any [available module](available-software.md) and show the result in the <i>Available Modules</i> subpanel. Note: Some modules are hidden until their dependency is loaded: we recommend that you first look for a specific module with `module spider module_name` from a terminal.

The next subpanel is the list of <i>Loaded Modules</i> in the whole JupyterLab session. 

The last subpanel is the list of <i>Available modules</i>, similar to the output of `module avail`. By clicking on a module's name, detailed information about the module is displayed. By clicking on the <i>Load</i> link, the module will be loaded and added to the <i>Loaded Modules</i> list.

=== Status bar at the bottom === 

* By clicking on the icons, this brings you to the <i>Running Terminals and Kernels</i> tool.

== Prebuilt applications == 

JupyterLab offers access to a terminal, an IDE (Desktop), a Python console and different options to create text and markdown files. This section presents only the main supported Jupyter applications that work with our software stack.

### Applications that are available by default 
A number of software modules are loaded by default, to give you access to those applications without any further actions. 

#### Python 
[alt=Python launcher icon|left|thumb|Python launcher icon](file:python-launcher-icon.png.md)
A Python kernel, with the default version, is automatically loaded. This allows you to start python notebooks automatically using the icon. 

We load a default version of the Python software, but you may use a different one by loading another version of the `ipython-kernel` modules.

This python environment does not come with most pre-installed packages. However, you can load some modules, such as `scipy-stack` in order to get additional features. 

You can also install python packages directly in the notebook's environment, by running 

`pip install --no-index package-name` 

in a cell of your notebook and then restarting your kernel.

#### VS Code 
[alt=VS Code launcher icon|left|thumb|VS Code launcher icon](file:vs-code-launcher-icon.png.md)
VS Code (Visual Studio Code) is a code editor originally developed by Microsoft, but which is an open standard on which [code-server](https://github.com/coder/code-server) is based to make the application available through any browser. 

The version which we have installed comes with a large number of [extensions](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/blob/main/2023/code-server/code-server-4.101.2.eb#L27) pre-installed. For more details, see our page on [Visual Studio Code](visual-studio-code.md).

For a new session, the <i>VS Code</i> session can take up to 3 minutes to complete its startup.

It is possible to reopen an active VS Code session after the web browser tab was closed.

The VS Code session will end when the JupyterLab session ends.

#### LibreQDA 
[alt=LibreQDA launcher icon|left|thumb|LibreQDA launcher icon](file:libreqda-launcher-icon.png.md)
<i>[LibreQDA](https://aide.libreqda.org/)</i> is an application for qualitative analysis, forked from [Taguette](https://www.taguette.org/). 
 
This icon will launch a single-user version of the software, which can be used for text analysis. 

For a new session, the <i>LibreQDA</i> session can take up to 3 minutes to complete its startup.

It is possible to reopen an active LibreQDA session after the web browser tab was closed.

The LibreQDA session will end when the JupyterLab session ends.

#### RStudio 
[alt=RStudio launcher icon|left|thumb|RStudio launcher icon](file:rstudio-launcher-icon.png.md)
[RStudio](https://posit.co/download/rstudio-desktop/) is an integrated development environment primarily use for the [R](r.md) language. 

We load a default version of the R software, but you may use a different one by loading another version of the `rstudio-server` modules. Please do so **before** launching RStudio, otherwise you may have to restart your JupyterLab session.

This <i>RStudio</i> launcher will open or reopen an RStudio interface in a new web browser tab.

It is possible to reopen an active RStudio session after the web browser tab was closed.

The RStudio session will end when the JupyterLab session ends.

Note that simply quitting RStudio or closing the RStudio and JupyterHub tabs in your browser will not release the resources (CPU, memory, GPU) nor end the underlying Slurm job.  <b>Please end your session with the menu item `File > Log Out` on the JupyterLab browser tab</b>.

#### MLflow 
[MLflow](https://mlflow.org/) is an open-source platform, purpose-built to assist machine learning practitioners and teams in handling the complexities of the machine learning process. MLflow focuses on the full lifecycle for machine learning projects, ensuring that each phase is manageable, traceable, and reproducible. We load a default version of MLflow by default, but you may use a different version of it by loading a `mlflow` module. Please see our [MLflow](mlflow.md) page for more information on how to use MLflow to track your AI experiments. 
[thumb|alt=MLflow launcher icon|none|MLflow launcher icon|105x105px](file:mlflow-launcher-icon.png.md)

#### OpenRefine 
[alt=OpenRefine launcher icon|left|thumb|OpenRefine launcher icon](file:openrefine-launcher-icon.png.md)
[OpenRefine](https://openrefine.org/) is a powerful, free and open-source tool to clean up messy data, to transform it, and to extend it in order to add value to it. 

It is commonly used to correct typos in manually collected survey data.

For a new session, the <i>OpenRefine</i> session can take up to 3 minutes to complete its startup.

It is possible to reopen an active OpenRefine session after the web browser tab was closed.

The OpenRefine session will end when the JupyterLab session ends.

==== Tensorboard ==== 
[Tensorboard](https://www.tensorflow.org/tensorboard) provides the visualization and tooling needed for machine learning experimentation. TensorBoard is a tool for providing the measurements and visualizations needed during the machine learning workflow. It enables tracking experiment metrics like loss and accuracy, visualizing the model graph, projecting embeddings to a lower dimensional space, and much more. We load a default version of `tensorboard`, but if a different module is available, you can change the version. See our page on [Tensorboard](tensorboard.md) for more details on using this software package. 
[110px|thumb|alt=Tensorboard launcher|Tensorboard launcher|none](file:tensorboard-launcher.png.md)

#### Desktop 
[alt=Desktop launchers|left|thumb|Desktop launchers](file:desktop-launchers.png.md)
Two different Desktop environments are available by default. [Mate Desktop](https://mate-desktop.org/), and [XFCE Desktop](https://www.xfce.org/). You may choose whichever you prefer. XFCE yields a more modern UI, while Mate is lighter to use.
These launchers will open or reopen a remote Linux desktop interface in a new web browser tab. 

This is equivalent to running a [VNC server on a compute node](vnc#compute_nodes.md), then creating an [SSH tunnel](ssh_tunnelling.md) and finally using a [VNC client](vnc#setup.md), but you need nothing of all this with JupyterLab!

For a new session, the <i>Desktop</i> session can take up to 3 minutes to complete its startup.

It is possible to reopen an active desktop session after the web browser tab was closed.

The desktop session will end when the JupyterLab session ends.

#### Terminal 
[alt=Terminal launcher|left|thumb|Terminal launcher](file:terminal-launcher.png.md)
JupyterLab also natively allows you to open a terminal session. This may be useful to run bash commands, submit jobs, or edit files. 

The terminal runs a (Bash) shell on the remote compute node without the need of an SSH connection.

Gives access to the remote filesystems (`/home`, `/project`, `/scratch`).

Allows running compute tasks.

The terminal allows copy-and-paste operations of text:

Copy operation: select the text, then press Ctrl+C.

Note: Usually, Ctrl+C is used to send a SIGINT signal to a running process, or to cancel the current command. To get this behaviour in JupyterLab's terminal, click on the terminal to deselect any text before pressing Ctrl+C.

Paste operation: press Ctrl+V.

#### Globus 
[alt=Globus launcher|none|thumb|Globus launcher](file:globus-launcher.png.md)
If [Globus](globus.md) is availalbe on the cluster you are using, you may see this icon. This will open your browser to the corresponding Globus collection.

#### Metrix 
[alt=Metrix launcher|none|thumb|Metrix launcher](file:metrix-launcher.png.md)
If the [Metrix job portal](metrix-fr.md) is available on the cluster you are using, this icon will open a page with the statistics of your job. 

### Applications available after loading a module 
Multiple of the modules we provide will also make a launcher available when they are loaded, even though they are not loaded by default. 

#### Julia 
[alt=Julia launcher|none|thumb|Julia launcher](file:julia-launcher.png.md)
Loading a module `ijulia-kernel` will allow you to open a notebook with the Julia language. 

#### Ansys suite 
The [Ansys](ansys.md) suite has multiple tools which provide a graphical user interface. If you load one of the `ansys` modules, you will get a series of launcher, most of which work through a VNC connection in the browser. 
{| class="wikitable"
|+
![alt=Ansys CFX launcher|none|thumb|Ansys CFX launcher](file:ansys-cfx-launcher.png.md)
![alt=Ansys Fluent launcher|none|thumb|Ansys Fluent launcher](file:ansys-fluent-launcher.png.md)
![alt=Ansys Mapdl launcher|none|thumb|Ansys Mapdl launcher](file:ansys-mapdl-launcher.png.md)
![alt=Ansys Workbench launcher|none|thumb|Ansys Workbench launcher](file:ansys-workbench-launcher.png.md)
|}
In addition, Ansys Fluent has a web-based interface, which can be launched with the icon below. 
[alt=Ansys Fluent web launcher|none|thumb|Ansys Fluent web launcher](file:ansys-fluent-web-launcher.png.md)
Note that for Ansys Fluent, a password is required to connect to it. That password is generated when you launch it, and written in your personal folder, in the file `$HOME/fluent_webserver_token`.

Note that for Ansys, you will need to provide your own license, as explained in our [Ansys](ansys.md) page.

#### Ansys EDT 
[Ansys EDT](https://www.ansys.com/products/electronics) is in its own separate module. Loading the module `ansysedt` will make the corresponding launcher appear.

Note that for Ansys EDT, you will need to provide your own license, as explained in our [Ansys EDT](ansysedt.md) page.
[alt=Ansys EDT launcher|none|thumb|Ansys EDT launcher](file:ansys-edt-launcher.png.md)

#### COMSOL 
[alt=COMSOL launcher|none|thumb|COMSOL launcher](file:comsol-launcher.png.md)
[COMSOL](http://www.comsol.com) is a general-purpose software for modelling engineering applications.

Note that you will need to provide your own license file to use this software. 

Loading a `comsol` module will add a launcher to start the graphical user interface for COMSOL through a VNC session. See our page on [COMSOL](comsol.md) for more details on using this software package. 

#### Matlab 
[MATLAB](https://www.mathworks.com/?s_tid=gn_logo)  is available by loading a `matlab` module, which will add a launcher to start the software in a VNC session. Note that you will need to provide your own license file, as explained in our [MATLAB](matlab.md) page.
[alt=MATLAB launcher|none|thumb|MATLAB launcher](file:matlab-launcher.png.md)

#### NVidia Nsight Systems 
[NVidia Nsight Systems](https://developer.nvidia.com/nsight-systems) is a performance analysis tool developed primarily for profiling GPUs, but which can profile CPU code as well. 
[alt=NVidia Nsight Systems launcher|none|thumb|NVidia Nsight Systems launcher](file:nvidia-nsight-systems-launcher.png.md)
Loading a `cuda` or a `nvhpc` module will add a launcher to start the graphical user interface in a VNC session. 

#### Octave 
[GNU Octave](https://octave.org/) is an open-source scientific programming language largely compatible with MATLAB. Loading an `octave` module will add a launcher to start the graphical user interface for Octave through a VNC session. See our page on  [Octave](octave.md) for more details on using this software package.
[alt=Octave launcher|none|thumb|Octave launcher](file:octave-launcher.png.md)

#### ParaView 
[ParaView](https://www.paraview.org/) is a powerful open-source visualisation software. Loading a `paraview` module will add a launcher to start the Paraview graphical user interface through a VNC session. See our page on [ParaView](paraview.md) for more details on using this software package.
[alt=ParaView launcher|none|thumb|ParaView launcher](file:paraview-launcher.png.md)

#### QGIS 
[QGIS](https://qgis.org/) is a powerful open-source software for visualizing and processing geographic information systems (GIS) data.  Loading a `qgis` module will add a launcher to start the QGIS graphical user interface through a VNC session. See our page on [QGIS](qgis.md) for more details on this software package.
[alt=QGIS launcher|none|thumb|QGIS launcher](file:qgis-launcher.png.md)

#### StarCCM+ 
Siemens's [Star-CCM+](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/) is a commercial computational fluid dynamic simulation software. It is available by loading one of the `starccm` or the `starccm-mixed` modules, which will add a launcher to start the StarCCM+ graphical user interface through a VNC session. As for all commercial packages, you will need to provide your own license. See our page on [Star-CCM+](star-ccm+.md) for more details on using this software.
[alt=StarCCM+ launcher|none|thumb|StarCCM+ launcher](file:starccm+-launcher.png.md)

== Additional information on running Python notebooks == 

==== Python notebook ====  

[thumb|Searching for scipy-stack modules](file:jupyterlab_softwares_scipystack.png.md)
If any of the following scientific Python packages is required by your notebook, before you open this notebook, you must load the `scipy-stack` module from the JupyterLab <i>Softwares</i> tool:
* `ipython`, `ipython_genutils`, `ipykernel`, `ipyparallel`
* `matplotlib`
* `numpy`
* `pandas`
* `scipy`
* See [SciPy stack](python#scipy_stack.md) for more on this

Note: You may also install needed packages by running for example the following command inside a cell: `pip install --no-index numpy`.
* For some packages (like `plotly`, for example), you may need to restart the notebook's kernel before importing the package.
* The installation of packages in the default Python kernel environment is temporary to the lifetime of the JupyterLab session; you will have to reinstall these packages the next time you start a new JupyterLab session. For a persistent Python environment, you must configure a <b>[custom Python kernel](advanced_jupyter_configuration#python_kernel.md)</b>.

To open an existing Python notebook:
* Go back to the <i>File Browser</i>.
* Browse to the location of the `*.ipynb` file.
* Double-click on the `*.ipynb` file.
** This will open the Python notebook in a new JupyterLab tab.
** An IPython kernel will start running in the background for this notebook.

To open a new Python notebook in the current <i>File Browser</i> directory:
* Click on the <i>Python 3.x</i> launcher under the <i>Notebook</i> section.
** This will open a new Python 3 notebook in a new JupyterLab tab.
** A new IPython kernel will start running in the background for this notebook.

### Running notebooks as Python scripts 
1. From the console, or in a new notebook cell, install <tt>nbconvert</tt> :
<syntaxhighlight lang="bash">!pip install --no-index nbconvert</syntaxhighlight>

2. Convert your notebooks to Python scripts
<syntaxhighlight lang="bash">!jupyter nbconvert --to python my-current-notebook.ipynb</syntaxhighlight>

3. Create your [non-interactive submission script](running_jobs#use_sbatch_to_submit_jobs.md), and submit it.

In your submission script, run your converted notebook with:
<syntaxhighlight lang="bash">python my-current-notebook.py</syntaxhighlight>

And submit your non-interactive job:

```bash
sbatch my-submit.sh
```

= Troubleshooting = 
## ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system 
When installing packages in your notebook, you may run into an error where pip tries to uninstall a package in a read-only location.

For many cases, in your notebook cell, you can use:

```bash
pip install --no-index --ignore-installed <package>
```

to install the package that caused the error but note it ***may not*** work for all packages for instance <tt>pyarrow</tt>, <tt>opencv</tt>, <tt>mpi4py</tt>.

In case of questions, please contact us: [Technical support](technical-support.md)