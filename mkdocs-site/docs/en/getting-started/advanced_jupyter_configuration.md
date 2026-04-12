---
title: "Advanced Jupyter configuration/en"
slug: "advanced_jupyter_configuration"
lang: "en"

source_wiki_title: "Advanced Jupyter configuration/en"
source_hash: "313eedbd32186855d6dc1a0cd610d445"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T04:53:32.630373+00:00"

tags:
  []

keywords:
  - "notebooks"
  - "software modules"
  - "Installing R packages"
  - "CRAN"
  - "sbatch"
  - "compute node"
  - "login node"
  - "Windows"
  - "SSH tunnel"
  - "MobaXTerm"
  - "R codes"
  - "nbconvert"
  - "Python scripts"
  - "virtual environment"
  - "Python modules"
  - "Python kernel"
  - "R module"
  - "RStudio Server"
  - "Jupyter notebooks"
  - "Python virtual environment"
  - "Jupyter kernel"
  - "Jupyter Lmod"
  - "rstudio-server"
  - "R kernel"
  - "JupyterHub"
  - "installing packages"
  - "Julia kernel"
  - "non-interactive job"
  - "JupyterLab"

questions:
  - "Why should a JupyterLab server be run on a compute node instead of a cluster login node?"
  - "What are the necessary steps to install JupyterLab using a Python virtual environment?"
  - "How do extensions like Jupyter Lmod enhance the JupyterLab interface, and how are they installed?"
  - "Where can users find instructions for managing loaded software modules in the JupyterLab interface?"
  - "What is the primary purpose of the RStudio Server as described in the text?"
  - "Which existing installation procedure serves as the baseline for setting up the RStudio Server?"
  - "How do you activate the Python virtual environment and verify that the necessary Jupyter packages are installed?"
  - "What command is used to start a JupyterLab server as an interactive job on the cluster?"
  - "How can users securely connect to the JupyterLab instance running on a compute node from their local Linux, macOS, or Windows machines?"
  - "What software or tools can be used to create an SSH tunnel from a Windows operating system?"
  - "What action must be completed on the compute node before you can extract the connection details?"
  - "Which specific pieces of information need to be extracted from the provided HTTP address?"
  - "How do you establish an SSH tunnel using MobaXTerm to access a running JupyterLab session in your web browser?"
  - "What are the specific keyboard commands used to shut down the JupyterLab server and close the SSH tunnel?"
  - "What are the two primary steps required to install and configure a new language kernel, such as Julia, in JupyterLab?"
  - "What are the necessary steps to create a Python virtual environment and install a custom Python kernel for JupyterLab?"
  - "Why must the installation of the R kernel and additional R packages be performed on a remote login node rather than directly within a notebook?"
  - "How do you install additional libraries and packages for both the Python and R kernels after their initial configuration?"
  - "What are the initial steps for creating and activating a new Python virtual environment for JupyterLab?"
  - "What specific components and modules need to be included in the virtual environment for a custom Jupyter configuration?"
  - "Under what circumstances is it required to start from a clean Bash environment when configuring the Python kernel?"
  - "Why is it not possible to install R packages directly from notebooks in this environment?"
  - "From which specific type of node must users perform the installation of R packages?"
  - "What are the necessary steps and commands required to prepare the environment and install a new R package?"
  - "How can newly installed R packages be utilized within a notebook environment?"
  - "Why would a user need to convert a Jupyter notebook into a Python script?"
  - "What are the necessary steps and commands to convert a notebook to a Python script and submit it as a non-interactive job?"
  - "How can newly installed R packages be utilized within a notebook environment?"
  - "Why would a user need to convert a Jupyter notebook into a Python script?"
  - "What are the necessary steps and commands to convert a notebook to a Python script and submit it as a non-interactive job?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Not recommended"
    The content of this page is for advanced users only. It is seldom tested, and is not recommended. Consider using our preconfigured [JupyterLab](jupyterlab.md) instead.

## Introduction

!!! warning "Running notebooks"
    Jupyter Lab and notebooks are meant for **short** interactive tasks such as testing, debugging or quickly visualize data (few minutes). Running longer analysis must be done in a [non-interactive job (sbatch)](running-jobs.md#use-sbatch-to-submit-jobs).
    See also [how to run notebooks as python scripts below](#running-notebooks-as-python-scripts).

*   **Project Jupyter**: "a non-profit, open-source project, born out of the IPython Project in 2014 as it evolved to support interactive data science and scientific computing across all programming languages." [https://jupyter.org/about.html](https://jupyter.org/about.html)
*   **JupyterLab**: "a web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design allows for extensions that expand and enrich functionality." [https://jupyter.org/](https://jupyter.org/)

A JupyterLab server should only run on a compute node or on a cloud instance; cluster login nodes are not a good choice because they impose various limits which can stop applications if they consume too much CPU time or memory. In the case of using a compute node, users can reserve compute resources by [submitting a job](running-jobs.md) that requests a specific number of CPUs (and optionally GPUs), an amount of memory and the run time. **In this page, we give detailed instructions on how to configure and submit a JupyterLab job on any national cluster.**

If you are instead looking for a preconfigured Jupyter environment, please check the [Jupyter](jupyter.md) page.

## Installing JupyterLab

These instructions install JupyterLab with the `pip` command in a [Python virtual environment](python.md#creating-and-using-a-virtual-environment):

1.  If you do not have an existing Python virtual environment, create one. Then, activate it:
    1.  Load a Python module, either the default one (as shown below) or a specific version (see available versions with `module avail python`):
        ```bash
        module load python
        ```
        **If you intend to use RStudio Server**, make sure to load `rstudio-server` first:
        ```bash
        module load rstudio-server python
        ```
    2.  Create a new Python virtual environment:
        ```bash
        virtualenv --no-download $HOME/jupyter_py3
        ```
    3.  Activate your newly created Python virtual environment:
        ```bash
        source $HOME/jupyter_py3/bin/activate
        ```
2.  Install JupyterLab in your new virtual environment (note: it takes a few minutes):
    ```bash
    pip install --no-index --upgrade pip
    pip install --no-index jupyterlab
    ```
3.  In the virtual environment, create a wrapper script that launches JupyterLab:
    ```bash
    echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/jupyterlab.sh
    ```
4.  Finally, make the script executable:
    ```bash
    chmod u+x $VIRTUAL_ENV/bin/jupyterlab.sh
    ```

## Installing extensions

Extensions allow you to add functionalities and modify the JupyterLab’s user interface.

### Jupyter Lmod

[Jupyter Lmod](https://github.com/cmd-ntrf/jupyter-lmod) is an extension that allows you to interact with environment modules before launching kernels. The extension uses the Lmod's Python interface to accomplish module-related tasks like loading, unloading, saving a collection, etc.

The following commands will install and enable the Jupyter Lmod extension in your environment (note: the third command takes a few minutes to complete):
```bash
module load nodejs
pip install jupyterlmod
jupyter labextension install jupyterlab-lmod
```
Instructions on how to manage loaded *software* modules in the JupyterLab interface are provided in the [JupyterHub page](jupyterhub.md#jupyterlab).

### RStudio Server

The RStudio Server allows you to develop R codes in an RStudio environment that appears in your web browser in a separate tab. Based on the above [Installing JupyterLab](#installing-jupyterlab) procedure, there are a few differences:

1.  Load the `rstudio-server` module **before** the `python` module **and before creating a new virtual environment**:
    ```bash
    module load rstudio-server python
    ```
2.  Once [Jupyter Lab is installed in the new virtual environment](#installing-jupyterlab), install the Jupyter RSession proxy:
    ```bash
    pip install --no-index jupyter-rsession-proxy
    ```
All other configuration and usage steps are the same. In JupyterLab, you should see an RStudio application in the *Launcher* tab.

## Using your installation

### Activating the environment

Make sure the Python virtual environment in which you have installed JupyterLab is activated.
For example, when you log onto the cluster, you have to activate it again with:
```bash
source $HOME/jupyter_py3/bin/activate
```
To verify that your environment is ready, you can get a list of installed `jupyter*` packages with the following command:
```bash
pip freeze | grep jupyter
```
```text
jupyter-client==7.1.0+computecanada
jupyter-core==4.9.1+computecanada
jupyter-server==1.9.0+computecanada
jupyterlab==3.1.7+computecanada
jupyterlab-pygments==0.1.2+computecanada
jupyterlab-server==2.3.0+computecanada
```

### Starting JupyterLab

To start a JupyterLab server, submit an interactive job with `salloc`. Adjust the parameters based on your needs. See [Running jobs](running-jobs.md) for more information.
```bash
salloc --time=1:0:0 --ntasks=1 --cpus-per-task=2 --mem-per-cpu=1024M --account=def-yourpi srun $VIRTUAL_ENV/bin/jupyterlab.sh
```
```text
...
[I 2021-12-06 10:37:14.262 ServerApp] jupyterlab | extension was successfully linked.
...
[I 2021-12-06 10:37:39.259 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2021-12-06 10:37:39.356 ServerApp]

    To access the server, open this file in a browser:
        file:///home/name/.local/share/jupyter/runtime/jpserver-198146-open.html
    Or copy and paste one of these URLs:
        http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
     or http://127.0.0.1:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
```

### Connecting to JupyterLab

To access JupyterLab running on a compute node from your web browser, you will need to create an [SSH tunnel](ssh-tunnelling.md) from your computer through the cluster since the compute nodes are not directly accessible from the internet.

#### From Linux or macOS

On a Linux or macOS system, we recommend using the [sshuttle](https://sshuttle.readthedocs.io) Python package.

On your computer, open a new terminal window and create the SSH tunnel with the following `sshuttle` command where `<username>` must be replaced with your Alliance account username, and `<cluster>` by the cluster on which you have launched JupyterLab:
```bash
sshuttle --dns -Nr <username>@<cluster>.alliancecan.ca
```
Then, copy and paste the first provided HTTP address into your web browser. In the above `salloc` example, this would be:
```text
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
```

#### From Windows

An [SSH tunnel](ssh-tunnelling.md) can be created from Windows using [MobaXTerm](connecting-with-mobaxterm.md) as follows. Note: this procedure also works from any terminal that supports the `ssh` command.

1.  Once JupyterLab is launched on a compute node (see [Starting JupyterLab](#starting-jupyterlab)), you can extract the `hostname:port` and the `token` from the first provided HTTP address. For example:
    ```text
    http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c368829...2728fad4eb
           └────────────────────┬────────────────────┘           └──────────┬──────────┘
                              hostname:port                               token
    ```
2.  Open a new Terminal tab in MobaXTerm. In the following command, replace `<hostname:port>` with its corresponding value (refer to the above figure), replace `<username>` with your Alliance account username, and replace `<cluster>` with the cluster on which you have launched JupyterLab:
    ```bash
    ssh -L 8888:<hostname:port> <username>@<cluster>.alliancecan.ca
    ```
3.  Open your web browser and go to the following address where `<token>` must be replaced with the alphanumerical value extracted from the above figure:
    ```text
    http://localhost:8888/?token=<token>
    ```

### Shutting down JupyterLab

You can shut down the JupyterLab server before the walltime limit by pressing **Ctrl-C twice** in the terminal that launched the interactive job.

If you have used MobaXterm to create an SSH tunnel, press **Ctrl-D** to shut down the tunnel.

## Adding kernels

It is possible to add kernels for other programming languages, for a different Python version or for a persistent virtual environment that has all required packages and libraries for your project. Refer to [Making kernels for Jupyter](http://jupyter-client.readthedocs.io/en/latest/kernels.html) to learn more.

The installation of a new kernel is done in two steps:
1.  Installation of the packages that will allow the language interpreter to communicate with the Jupyter interface.
2.  Creation of a file that will indicate to JupyterLab how to initiate a communication channel with the language interpreter. This file is called a *kernel spec file*, and it will be saved in a subfolder of `~/.local/share/jupyter/kernels`.

In the following sections, we provide a few examples of the kernel installation procedure.

### Julia Kernel

Prerequisites:
*   The configuration of a Julia kernel depends on a Python virtual environment and a `kernels` folder. If you do not have these dependencies, make sure to follow the first few instructions listed in **[Python kernel](#python-kernel)** (note: no Python kernel required).
*   Since the installation of Julia packages requires an access to the internet, the configuration of a Julia kernel must be done in a **[remote shell session on a login node](ssh.md)**.

Once you have a Python virtual environment available and activated, you may configure the Julia kernel:

1.  Load the **[Julia](julia.md)** module:
    ```bash
    module load julia
    ```
2.  Install IJulia:
    ```bash
    echo -e 'using Pkg\nPkg.add("IJulia")' | julia
    ```
3.  **Important**: start or restart a new JupyterLab session before using the Julia kernel.

For more information, see the [IJulia documentation](https://github.com/JuliaLang/IJulia.jl).

#### Installing more Julia packages

As in the above installation procedure, it is required to install Julia packages from a login node, but the Python virtual environment could be deactivated:

1.  Make sure the same Julia module is loaded:
    ```bash
    module load julia
    ```
2.  Install any required package. For example with `Glob`:
    ```bash
    echo -e 'using Pkg\nPkg.add("Glob")' | julia
    ```
3.  The newly installed Julia packages should already be usable in a notebook executed by the Julia kernel.

### Python kernel

In a terminal with an active session on the remote server, you may configure a [Python virtual environment](python.md#creating-and-using-a-virtual-environment) with all the required [Python modules](available-python-wheels.md) and a custom Python kernel for JupyterLab. Here are the initial steps for the simplest Jupyter configuration in a new Python virtual environment:

1.  If you do not have a Python virtual environment, create one. Then, activate it:
    1.  Start from a clean Bash environment (this is only required if you are using the Jupyter *Terminal* via [JupyterHub](jupyterhub.md) for the creation and configuration of the Python kernel):
        ```bash
        env -i HOME=$HOME bash -l
        ```
    2.  Load a Python module:
        ```bash
        module load python
        ```
    3.  Create a new Python virtual environment:
        ```bash
        virtualenv --no-download $HOME/jupyter_py3
        ```
    4.  Activate your newly created Python virtual environment:
        ```bash
        source $HOME/jupyter_py3/bin/activate
        ```
2.  Create the common `kernels` folder, which is used by all kernels you want to install:
    ```bash
    mkdir -p ~/.local/share/jupyter/kernels
    ```
3.  Finally, install the Python kernel:
    1.  Install the `ipykernel` library:
        ```bash
        pip install --no-index ipykernel
        ```
    2.  Generate the kernel spec file. Replace `<unique_name>` with a name that will uniquely identify your kernel:
        ```bash
        python -m ipykernel install --user --name <unique_name> --display-name "Python 3.x Kernel"
        ```
4.  **Important**: start or restart a new JupyterLab session before using the Python kernel.

For more information, see the [ipykernel documentation](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).

#### Installing more Python libraries

Based on the Python virtual environment configured in the previous section:

1.  If you are using the Jupyter *Terminal* via [JupyterHub](jupyterhub.md), make sure the activated Python virtual environment is running in a clean Bash environment. See the above section for details.
2.  Install any required library. For example, `numpy`:
    ```bash
    pip install --no-index numpy
    ```
3.  The newly installed Python libraries can now be imported in any notebook using the `Python 3.x Kernel`.

### R Kernel

Prerequisites:
*   The configuration of an R kernel depends on a Python virtual environment and a `kernels` folder. If you do not have these dependencies, make sure to follow the first few instructions listed in **[Python kernel](#python-kernel)** (note: no Python kernel required).
*   Since the installation of R packages requires an access to [CRAN](https://cran.r-project.org/), the configuration of an R kernel must be done in a **[remote shell session on a login node](ssh.md)**.

Once you have a Python virtual environment available and activated, you may configure the R kernel:

1.  Load an R module:
    ```bash
    module load r/4.1
    ```
2.  Install the R kernel dependencies (`crayon`, `pbdZMQ`, `devtools`) - this will take up to 10 minutes, and packages should be installed in a local directory like `~/R/x86_64-pc-linux-gnu-library/4.1`:
    ```bash
    R --no-save
    ```
    ```r
    install.packages(c('crayon', 'pbdZMQ', 'devtools'), repos='http://cran.us.r-project.org')
    ```
3.  Install the R kernel.
    ```r
    devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))
    ```
4.  Install the R kernel spec file.
    ```r
    IRkernel::installspec()
    ```
5.  **Important**: Start or restart a new JupyterLab session before using the R kernel.

For more information, see the [IRkernel documentation](https://irkernel.github.io/docs/).

#### Installing more R packages

The installation of R packages cannot be done from notebooks because there is no access to CRAN.
As in the above installation procedure, it is required to install R packages from a login node, but the Python virtual environment could be deactivated:

1.  Make sure the same R module is loaded:
    ```bash
    module load r/4.1
    ```
2.  Start the R shell and install any required package. For example with `doParallel`:
    ```bash
    R --no-save
    ```
    ```r
    install.packages('doParallel', repos='http://cran.us.r-project.org')
    ```
3.  The newly installed R packages should already be usable in a notebook executed by the R kernel.

## Running notebooks as Python scripts

For longer run or analysis, we need to submit a [non-interactive job](running-jobs.md#use-sbatch-to-submit-jobs). We then need to convert our notebook to a Python script, create a submission script and submit it.

1.  From the login node, create and activate a [virtual environment](python.md#creating-and-using-a-virtual-environment), then install `nbconvert` if not already available.
    ```bash
    pip install --no-index nbconvert
    ```
2.  Convert the notebook (or all notebooks) to Python scripts.
    ```bash
    jupyter nbconvert --to python mynotebook.ipynb
    ```
3.  Create your submission script, and submit your job.

In your submission script, run your converted notebook with:
```bash
python mynotebook.py
```

and submit your non-interactive job:
```bash
sbatch my-submit.sh
```

## References