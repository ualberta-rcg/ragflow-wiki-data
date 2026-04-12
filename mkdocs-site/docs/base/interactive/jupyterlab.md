---
title: "JupyterLab"
slug: "jupyterlab"
lang: "base"

source_wiki_title: "JupyterLab"
source_hash: "a3c789fc48f7f01af62824aabfe453cd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:18:10.041378+00:00"

tags:
  []

keywords:
  - "modelling engineering applications"
  - "package installation"
  - "remote Linux desktop"
  - "VNC session"
  - "VNC server"
  - "software modules"
  - "persistent environment"
  - "VS Code"
  - "LibreQDA"
  - "custom Python kernel"
  - "JupyterLab session"
  - "OpenRefine"
  - "Open OnDemand"
  - "SSH tunnel"
  - "nbconvert"
  - "Tensorboard"
  - "File Browser"
  - "upload files"
  - "Python kernel"
  - "non-interactive submission script"
  - "MLflow"
  - "terminal sessions"
  - "COMSOL"
  - "desktop session"
  - "Troubleshooting"
  - "Prebuilt applications"
  - "Terminal"
  - "Python notebook"
  - "Python"
  - "Kernels"
  - "license file"
  - "Taguette"
  - "Launchers"
  - "Running Terminals"
  - "qualitative analysis"
  - "JupyterHub"
  - "single-user version"
  - "graphical user interface"
  - "text analysis"
  - "Ansys suite"
  - "RStudio"
  - "Software Modules"
  - "JupyterLab"

questions:
  - "What applications and tasks can users manage and launch using the JupyterLab interface?"
  - "What are the recommended methods and platforms for launching JupyterLab on the various available clusters?"
  - "How do users navigate the JupyterLab interface to manage their files, running sessions, and server resources?"
  - "How can users search for, load, and manage software modules within the JupyterLab interface?"
  - "What steps are required to customize the default Python environment, such as changing the Python version or installing new packages?"
  - "What prebuilt applications are available by default, and what should users expect regarding their startup times and session lifespans?"
  - "What spaces can users browse and what actions can they perform using the File Browser?"
  - "What is the purpose of the \"Running Terminals and Kernels\" feature?"
  - "Which specific icons are used to represent the File Browser and the Running Terminals and Kernels in the interface?"
  - "What is LibreQDA and from which software was it originally forked?"
  - "What specific type of analysis is the single-user version of LibreQDA used for?"
  - "How long might it take for a new LibreQDA session to fully complete its startup process?"
  - "How must a user properly terminate their session to ensure that underlying compute resources like CPU and memory are released?"
  - "What is the required procedure for loading and using a non-default version of software applications such as RStudio or MLflow?"
  - "What are the two available remote Linux desktop environments, and how do they differ in terms of user interface and resource usage?"
  - "How does the native terminal session in JupyterLab handle copy-and-paste operations, specifically regarding the Ctrl+C command?"
  - "Which software applications require users to load specific modules and provide their own licenses before they can be launched?"
  - "How do users access the web-based interface for Ansys Fluent, and where can they find the required connection password?"
  - "How does JupyterLab simplify the process of accessing a remote Linux desktop compared to traditional VNC and SSH methods?"
  - "What is the maximum expected startup time for a new Desktop session?"
  - "Can an active desktop session be recovered if the web browser tab is closed?"
  - "What is the primary purpose of the COMSOL software?"
  - "What specific requirement must users fulfill regarding licensing to use COMSOL?"
  - "How can users access the graphical user interface for COMSOL?"
  - "How do users launch the graphical user interfaces for the various software packages mentioned in the text?"
  - "Which specific software packages require users to provide their own commercial license files?"
  - "What steps must be taken to create a persistent Python environment for JupyterLab sessions instead of a temporary one?"
  - "What action might be required before importing certain newly installed packages like plotly?"
  - "How long do packages installed in the default Python kernel environment remain available?"
  - "How can you configure a persistent Python environment to avoid reinstalling packages in future JupyterLab sessions?"
  - "How do you open an existing or new Python notebook using the JupyterLab File Browser?"
  - "What are the steps required to convert a Jupyter notebook into a Python script and run it as a non-interactive job?"
  - "How can you troubleshoot and resolve the \"Read-only file system\" OSError when installing packages in a notebook?"
  - "How do you open an existing or new Python notebook using the JupyterLab File Browser?"
  - "What are the steps required to convert a Jupyter notebook into a Python script and run it as a non-interactive job?"
  - "How can you troubleshoot and resolve the \"Read-only file system\" OSError when installing packages in a notebook?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# JupyterLab
JupyterLab is the recommended general-purpose user interface to use on a JupyterHub. From a JupyterLab server, you can manage your remote files and folders, and you can launch Jupyter applications like a terminal, (Python 3) notebooks, RStudio and a Linux desktop.

You can add your own "kernels", which appear as application tiles described below. To configure such kernels, please see [Adding kernels](jupyternotebook.md#adding-kernels).

## Launching JupyterLab
There are a few ways to launch JupyterLab.

The traditional way would be to use [JupyterHub](jupyterhub.md#jupyterhub-on-clusters), but more recently, sites have deployed Open OnDemand which sometimes can launch the interface below. In the table below, the column "Fully-featured" indicates whether the JupyterLab interface available has all of the features described below. If there is a link, it is to that cluster's JupyterHub or Open OnDemand server.

| Cluster   | JupyterHub Available | JupyterHub Fully-featured | Open OnDemand Available | Open OnDemand JupyterLab | Open OnDemand Fully-featured |
| :-------- | :------------------- | :------------------------ | :---------------------- | :----------------------- | :--------------------------- |
| Fir       | [Yes](https://jupyterhub.fir.alliancecan.ca/) | Yes                     | No                      | No                       | No                           |
| Killarney | No                   | No                        | No                      | No                       | No                           |
| Narval    | [Yes](https://jupyterhub.narval.alliancecan.ca/) | Yes                     | No                      | No                       | No                           |
| Nibi      | No                   | No                        | [Yes](https://ondemand.sharcnet.ca/) | Yes                      | Yes                          |
| Rorqual   | [Yes](https://jupyterhub.rorqual.alliancecan.ca/) | Yes                     | No                      | No                       | No                           |
| tamIA     | No                   | No                        | No                      | No                       | No                           |
| Trillium  | No                   | No                        | [Yes](http://ondemand.scinet.utoronto.ca/) | Yes (request "Jupyter Lab + Alliance software extensions") | Yes                          |
| Vulcan    | No                   | No                        | [Yes](https://vulcan.alliancecan.ca/) | Yes                      | Yes                          |

!!! warning
    It is also possible to launch JupyterLab by [installing it yourself in a virtual environment](../getting-started/advanced_jupyter_configuration.md), but this is not recommended. You will also not benefit from any of the pre-configured applications described below.

## The JupyterLab interface

When you open JupyterLab in one of our most recent clusters, you will be presented with a dashboard pre-populated with a few launchers. Default launchers include Python 3.11, LibreQDA, Mate Desktop (VNC), OpenRefine, RStudio, VS Code and XFCE4 Desktop (VNC). In addition, you may find links to the cluster's [Globus](../getting-started/globus.md) collection, to the cluster's job portal, as well as links to relevant documentation pages. By loading modules, you will see new launchers appear in the dashboard (see below).

In the menu bar on the top, please note that in order to close your session, you may do so through the *File* menu:
*   *Hub Control Panel*: if you want to manually stop the JupyterLab server and the corresponding job on the cluster. This is useful when you want to start a new JupyterLab server with more or less resources.
*   *Log Out*: the session will end, which will also stop the JupyterLab server and the corresponding job on the cluster.

Most other menu items are related to notebooks and Jupyter applications.

### Tool selector on left
On the left side of the interface, you will find the tool selector. This changes the content of the frame on the right. The most relevant ones are:

#### *File Browser* (folder icon)
This is where you can browse in your home, project and scratch spaces. It is also possible to use it to upload files.

#### *Running Terminals and Kernels* (stop icon)
This is to stop kernel sessions and terminal sessions

#### *GPU Dashboards* (GPU card icon)
If your job uses GPUs, this will give you access to some resource monitoring options.

#### *Software Modules*
This is where you can load or unload [software modules](../programming/available_software.md) available in our environment. Depending on the modules loaded, icons directing to the corresponding [Jupyter applications](#prebuilt-applications) will appear in the *Launcher* tab. By default, we load a number of modules to provide you access to basic tools.

!!! note
    The search box can search for any [available module](../programming/available_software.md) and show the result in the *Available Modules* subpanel. Some modules are hidden until their dependency is loaded: we recommend that you first look for a specific module with `module spider module_name` from a terminal.

The next subpanel is the list of *Loaded Modules* in the whole JupyterLab session.

The last subpanel is the list of *Available modules*, similar to the output of `module avail`. By clicking on a module's name, detailed information about the module is displayed. By clicking on the *Load* link, the module will be loaded and added to the *Loaded Modules* list.

### Status bar at the bottom
*   By clicking on the icons, this brings you to the *Running Terminals and Kernels* tool.

## Prebuilt applications

JupyterLab offers access to a terminal, an IDE (Desktop), a Python console and different options to create text and markdown files. This section presents only the main supported Jupyter applications that work with our software stack.

### Applications that are available by default
A number of software modules are loaded by default, to give you access to those applications without any further actions.

#### Python
A Python kernel, with the default version, is automatically loaded. This allows you to start python notebooks automatically using the icon.

We load a default version of the Python software, but you may use a different one by loading another version of the `ipython-kernel` modules.

This python environment does not come with most pre-installed packages. However, you can load some modules, such as `scipy-stack` in order to get additional features.

You can also install python packages directly in the notebook's environment, by running

```bash
pip install --no-index package-name
```

in a cell of your notebook and then restarting your kernel.

#### VS Code
VS Code (Visual Studio Code) is a code editor originally developed by Microsoft, but which is an open standard on which [code-server](https://github.com/coder/code-server) is based to make the application available through any browser.

The version which we have installed comes with a large number of [extensions](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/blob/main/2023/code-server/code-server-4.101.2.eb#L27) pre-installed. For more details, see our page on [Visual Studio Code](visual_studio_code.md).

!!! note
    For a new session, the *VS Code* session can take up to 3 minutes to complete its startup.

It is possible to reopen an active VS Code session after the web browser tab was closed.

The VS Code session will end when the JupyterLab session ends.

#### LibreQDA
[LibreQDA](https://aide.libreqda.org/) is an application for qualitative analysis, forked from [Taguette](https://www.taguette.org/).

This icon will launch a single-user version of the software, which can be used for text analysis.

!!! note
    For a new session, the *LibreQDA* session can take up to 3 minutes to complete its startup.

It is possible to reopen an active LibreQDA session after the web browser tab was closed.

The LibreQDA session will end when the JupyterLab session ends.

#### RStudio
[RStudio](https://posit.co/download/rstudio-desktop/) is an integrated development environment primarily use for the [R](../software/r.md) language.

!!! warning
    We load a default version of the R software, but you may use a different one by loading another version of the `rstudio-server` modules. Please do so **before** launching RStudio, otherwise you may have to restart your JupyterLab session.

This *RStudio* launcher will open or reopen an RStudio interface in a new web browser tab.

It is possible to reopen an active RStudio session after the web browser tab was closed.

The RStudio session will end when the JupyterLab session ends.

!!! warning
    Note that simply quitting RStudio or closing the RStudio and JupyterHub tabs in your browser will not release the resources (CPU, memory, GPU) nor end the underlying Slurm job. **Please end your session with the menu item `File > Log Out` on the JupyterLab browser tab**.

#### MLflow
[MLflow](https://mlflow.org/) is an open-source platform, purpose-built to assist machine learning practitioners and teams in handling the complexities of the machine learning process. MLflow focuses on the full lifecycle for machine learning projects, ensuring that each phase is manageable, traceable, and reproducible. We load a default version of MLflow by default, but you may use a different version of it by loading a `mlflow` module. Please see our [MLflow](../software/ai-ml/mlflow.md) page for more information on how to use MLflow to track your AI experiments.

#### OpenRefine
[OpenRefine](https://openrefine.org/) is a powerful, free and open-source tool to clean up messy data, to transform it, and to extend it in order to add value to it.

It is commonly used to correct typos in manually collected survey data.

!!! note
    For a new session, the *OpenRefine* session can take up to 3 minutes to complete its startup.

It is possible to reopen an active OpenRefine session after the web browser tab was closed.

The OpenRefine session will end when the JupyterLab session ends.

#### Tensorboard
[Tensorboard](https://www.tensorflow.org/tensorboard) provides the visualization and tooling needed for machine learning experimentation. TensorBoard is a tool for providing the measurements and visualizations needed during the machine learning workflow. It enables tracking experiment metrics like loss and accuracy, visualizing the model graph, projecting embeddings to a lower dimensional space, and much more. We load a default version of `tensorboard`, but if a different module is available, you can change the version. See our page on [Tensorboard](../software/ai-ml/tensorboard.md) for more details on using this software package.

#### Desktop
Two different Desktop environments are available by default. [Mate Desktop](https://mate-desktop.org/), and [XFCE Desktop](https://www.xfce.org/). You may choose whichever you prefer. XFCE yields a more modern UI, while Mate is lighter to use. These launchers will open or reopen a remote Linux desktop interface in a new web browser tab.

This is equivalent to running a [VNC server on a compute node](vnc.md#compute-nodes), then creating an [SSH tunnel](../getting-started/ssh_tunnelling.md) and finally using a [VNC client](vnc.md#setup), but you need nothing of all this with JupyterLab!

!!! note
    For a new session, the *Desktop* session can take up to 3 minutes to complete its startup.

It is possible to reopen an active desktop session after the web browser tab was closed.

The desktop session will end when the JupyterLab session ends.

#### Terminal
JupyterLab also natively allows you to open a terminal session. This may be useful to run bash commands, submit jobs, or edit files.

The terminal runs a (Bash) shell on the remote compute node without the need of an SSH connection.

Gives access to the remote filesystems (`/home`, `/project`, `/scratch`).

Allows running compute tasks.

The terminal allows copy-and-paste operations of text:

*   Copy operation: select the text, then press Ctrl+C.
*   !!! note
    Usually, Ctrl+C is used to send a SIGINT signal to a running process, or to cancel the current command. To get this behaviour in JupyterLab's terminal, click on the terminal to deselect any text before pressing Ctrl+C.
*   Paste operation: press Ctrl+V.

#### Globus
If [Globus](../getting-started/globus.md) is available on the cluster you are using, you may see this icon. This will open your browser to the corresponding Globus collection.

#### Metrix
If the [Metrix job portal](../software/metrix.md) is available on the cluster you are using, this icon will open a page with the statistics of your job.

### Applications available after loading a module
Multiple of the modules we provide will also make a launcher available when they are loaded, even though they are not loaded by default.

#### Julia
Loading a module `ijulia-kernel` will allow you to open a notebook with the Julia language.

#### Ansys suite
The [Ansys](../software/ansys.md) suite has multiple tools which provide a graphical user interface. If you load one of the `ansys` modules, you will get a series of launcher, most of which work through a VNC connection in the browser.

In addition, Ansys Fluent has a web-based interface, which can be launched with the icon below.

Note that for Ansys Fluent, a password is required to connect to it. That password is generated when you launch it, and written in your personal folder, in the file `$HOME/fluent_webserver_token`.

Note that for Ansys, you will need to provide your own license, as explained in our [Ansys](../software/ansys.md) page.

#### Ansys EDT
[Ansys EDT](https://www.ansys.com/products/electronics) is in its own separate module. Loading the module `ansysedt` will make the corresponding launcher appear.

Note that for Ansys EDT, you will need to provide your own license, as explained in our [Ansys EDT](../software/ansysedt.md) page.

#### COMSOL
[COMSOL](http://www.comsol.com) is a general-purpose software for modelling engineering applications.

Note that you will need to provide your own license file to use this software.

Loading a `comsol` module will add a launcher to start the graphical user interface for COMSOL through a VNC session. See our page on [COMSOL](../software/comsol.md) for more details on using this software package.

#### Matlab
[MATLAB](https://www.mathworks.com/?s_tid=gn_logo) is available by loading a `matlab` module, which will add a launcher to start the software in a VNC session. Note that you will need to provide your own license file, as explained in our [MATLAB](../software/matlab.md) page.

#### NVidia Nsight Systems
[NVidia Nsight Systems](https://developer.nvidia.com/nsight-systems) is a performance analysis tool developed primarily for profiling GPUs, but which can profile CPU code as well.

Loading a `cuda` or a `nvhpc` module will add a launcher to start the graphical user interface in a VNC session.

#### Octave
[GNU Octave](https://octave.org/) is an open-source scientific programming language largely compatible with MATLAB. Loading an `octave` module will add a launcher to start the graphical user interface for Octave through a VNC session. See our page on [Octave](../software/octave.md) for more details on using this software package.

#### ParaView
[ParaView](https://www.paraview.org/) is a powerful open-source visualisation software. Loading a `paraview` module will add a launcher to start the Paraview graphical user interface through a VNC session. See our page on [ParaView](../software/paraview.md) for more details on using this software package.

#### QGIS
[QGIS](https://qgis.org/) is a powerful open-source software for visualizing and processing geographic information systems (GIS) data. Loading a `qgis` module will add a launcher to start the QGIS graphical user interface through a VNC session. See our page on [QGIS](../software/qgis.md) for more details on this software package.

#### StarCCM+
Siemens's [Star-CCM+](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/) is a commercial computational fluid dynamic simulation software. It is available by loading one of the `starccm` or the `starccm-mixed` modules, which will add a launcher to start the StarCCM+ graphical user interface through a VNC session. As for all commercial packages, you will need to provide your own license. See our page on [Star-CCM+](../software/star-ccm.md) for more details on using this software.

## Additional information on running Python notebooks

### Python notebook

If any of the following scientific Python packages is required by your notebook, before you open this notebook, you must load the `scipy-stack` module from the JupyterLab *Softwares* tool:
*   `ipython`, `ipython_genutils`, `ipykernel`, `ipyparallel`
*   `matplotlib`
*   `numpy`
*   `pandas`
*   `scipy`
*   See [SciPy stack](../software/python.md#scipy-stack) for more on this

!!! note
    You may also install needed packages by running for example the following command inside a cell: `pip install --no-index numpy`.
    *   For some packages (like `plotly`, for example), you may need to restart the notebook's kernel before importing the package.

!!! important
    The installation of packages in the default Python kernel environment is temporary to the lifetime of the JupyterLab session; you will have to reinstall these packages the next time you start a new JupyterLab session. For a persistent Python environment, you must configure a **[custom Python kernel](../getting-started/advanced_jupyter_configuration.md#python-kernel)**.

To open an existing Python notebook:
*   Go back to the *File Browser*.
*   Browse to the location of the `*.ipynb` file.
*   Double-click on the `*.ipynb` file.
    *   This will open the Python notebook in a new JupyterLab tab.
    *   An IPython kernel will start running in the background for this notebook.

To open a new Python notebook in the current *File Browser* directory:
*   Click on the *Python 3.x* launcher under the *Notebook* section.
    *   This will open a new Python 3 notebook in a new JupyterLab tab.
    *   A new IPython kernel will start running in the background for this notebook.

### Running notebooks as Python scripts
1.  From the console, or in a new notebook cell, install `nbconvert`:
    ```bash
    !pip install --no-index nbconvert
    ```

2.  Convert your notebooks to Python scripts
    ```bash
    !jupyter nbconvert --to python my-current-notebook.ipynb
    ```

3.  Create your [non-interactive submission script](../running-jobs/running_jobs.md#use-sbatch-to-submit-jobs), and submit it.

In your submission script, run your converted notebook with:
```bash
python my-current-notebook.py
```

And submit your non-interactive job:
```bash
sbatch my-submit.sh
```

# Troubleshooting

!!! error "ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system"
    When installing packages in your notebook, you may run into an error where pip tries to uninstall a package in a read-only location.

    For many cases, in your notebook cell, you can use:
    ```bash
    pip install --no-index --ignore-installed <package>
    ```
    to install the package that caused the error but note it **may not** work for all packages for instance `pyarrow`, `opencv`, `mpi4py`.

In case of questions, please contact us: [Technical support](../support/technical_support.md)