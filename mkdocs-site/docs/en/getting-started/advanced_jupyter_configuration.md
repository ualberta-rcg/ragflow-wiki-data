---
title: "Advanced Jupyter configuration/en"
tags:
  []

keywords:
  []
---

= Introduction =

* <b>Project Jupyter</b>: "a non-profit, open-source project, born out of the IPython Project in 2014 as it evolved to support interactive data science and scientific computing across all programming languages."<ref>https://jupyter.org/about.html</ref>
* <b>JupyterLab</b>: "a web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design allows for extensions that expand and enrich functionality."<ref>https://jupyter.org/</ref>

A JupyterLab server should only run on a compute node or on a cloud instance; cluster login nodes are not a good choice because they impose various limits which can stop applications if they consume too much CPU time or memory. In the case of using a compute node, users can reserve compute resources by [submitting a job](running_jobs.md) that requests a specific number of CPUs (and optionally GPUs), an amount of memory and the run time. <b>In this page, we give detailed instructions on how to configure and submit a JupyterLab job on any national cluster.</b>

If you are instead looking for a preconfigured Jupyter environment, please check the [Jupyter](jupyter.md) page.

= Installing JupyterLab =

These instructions install JupyterLab with the `pip` command in a
[Python virtual environment](python#creating_and_using_a_virtual_environment.md):

<ol>
<li>If you do not have an existing Python virtual environment, create one. Then, activate it:
<ol>
<li>Load a Python module, either the default one (as shown below) or
a specific version (see available versions with `module avail python`):
```bash
module load python
```

<b>If you intend to use RStudio Server</b>, make sure to load `rstudio-server` first:
```bash
module load rstudio-server python
```

</li><li>Create a new Python virtual environment:
```bash
virtualenv --no-download $HOME/jupyter_py3
```

</li><li>Activate your newly created Python virtual environment:
```bash
source $HOME/jupyter_py3/bin/activate
```

</li>
</ol>
</li><li>Install JupyterLab in your new virtual environment (note: it takes a few minutes):
```bash
pip install --no-index jupyterlab
```

</li><li>In the virtual environment, create a wrapper script that launches JupyterLab:
```bash
echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/jupyterlab.sh
```

</li><li>Finally, make the script executable:
```bash
chmod u+x $VIRTUAL_ENV/bin/jupyterlab.sh
```

</li>
</ol>
= Installing extensions =

Extensions allow you to add functionalities and modify the JupyterLab’s user interface. 

### Jupyter Lmod 

[Jupyter Lmod](https://github.com/cmd-ntrf/jupyter-lmod) is an extension that allows you to interact with environment modules before launching kernels. The extension uses the Lmod's Python interface to accomplish module-related tasks like loading, unloading, saving a collection, etc.

The following commands will install and enable the Jupyter Lmod extension in your environment (note: the third command takes a few minutes to complete):

```bash
jupyter labextension install jupyterlab-lmod
```

Instructions on how to manage loaded <i>software</i> modules in the JupyterLab interface are provided in the [JupyterHub page](jupyterhub#jupyterlab.md).

### RStudio Server 

The RStudio Server allows you to develop R codes in an RStudio environment that appears in your web browser in a separate tab. Based on the above [Installing JupyterLab](#installing_jupyterlab.md) procedure, there are a few differences:

<ol>
<li>Load the `rstudio-server` module <b>before</b> the `python` module <b>and before creating a new virtual environment</b>:
```bash
module load rstudio-server python
```

</li><li>Once [Jupyter Lab is installed in the new virtual environment](#installing_jupyterlab.md), install the Jupyter RSession proxy:
```bash
pip install --no-index jupyter-rsession-proxy
```

</li>
</ol>
All other configuration and usage steps are the same. In JupyterLab, you should see an RStudio application in the <i>Launcher</i> tab.

= Using your installation =

## Activating the environment 

Make sure the Python virtual environment in which you have installed JupyterLab is activated.
For example, when you log onto the cluster, you have to activate it again with:
```bash
source $HOME/jupyter_py3/bin/activate
```

To verify that your environment is ready, you can get a list of installed `jupyter*` packages with the following command:
```bash

```
 grep jupyter
|result=
jupyter-client==7.1.0+computecanada
jupyter-core==4.9.1+computecanada
jupyter-server==1.9.0+computecanada
jupyterlab==3.1.7+computecanada
jupyterlab-pygments==0.1.2+computecanada
jupyterlab-server==2.3.0+computecanada
}}
## Starting JupyterLab 

To start a JupyterLab server, submit an interactive job with `salloc`. Adjust the parameters based on your needs. See [Running jobs](running-jobs.md) for more information.

```bash

```
1:0:0 --ntasks1 --cpus-per-task2 --mem-per-cpu1024M --accountdef-yourpi srun $VIRTUAL_ENV/bin/jupyterlab.sh
|result=
...
[I 2021-12-06 10:37:14.262 ServerApp] jupyterlab  extension was successfully linked.
...
[I 2021-12-06 10:37:39.259 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2021-12-06 10:37:39.356 ServerApp]

    To access the server, open this file in a browser:
        file:///home/name/.local/share/jupyter/runtime/jpserver-198146-open.html
    Or copy and paste one of these URLs:
        http://node_name.int.cluster.computecanada.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
     or http://127.0.0.1:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
}}
## Connecting to JupyterLab 

To access JupyterLab running on a compute node from your web browser, you will need to create an [SSH tunnel](ssh-tunnelling.md) from your computer through the cluster since the compute nodes are not directly accessible from the internet.

### From Linux or macOS 

On a Linux or macOS system, we recommend using the [sshuttle](https://sshuttle.readthedocs.io) Python package.

On your computer, open a new terminal window and create the SSH tunnel with the following `sshuttle` command where <code><username></code> must be replaced with your Alliance account username, and <code><cluster></code> by the cluster on which you have launched JupyterLab:

```bash
sshuttle --dns -Nr <username>@<cluster>.alliancecan.ca
```

Then, copy and paste the first provided HTTP address into your web browser. In the above `salloc` example, this would be:
<pre>
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
</pre>
### From Windows 

An [SSH tunnel](ssh-tunnelling.md) can be created from Windows using [MobaXTerm](connecting_with_mobaxterm.md) as follows. Note: this procedure also works from any terminal that supports the `ssh` command.

<ol>
<li>Once JupyterLab is launched on a compute node (see [Starting JupyterLab](#starting_jupyterlab.md)), you can extract the `hostname:port` and the `token` from the first provided HTTP address. For example:<pre>
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c368829...2728fad4eb
       └────────────────────┬────────────────────┘           └──────────┬──────────┘
                      hostname:port                                   token
</pre>
</li><li>Open a new Terminal tab in MobaXTerm. In the following command, replace <code><hostname:port></code> with its corresponding value (refer to the above figure), replace <code><username></code> with your Alliance account username, and replace <code><cluster></code> with the cluster on which you have launched JupyterLab:
```bash
ssh -L 8888:<hostname:port> <username>@<cluster>.alliancecan.ca
```

</li><li>Open your web browser and go to the following address where <code><token></code> must be replaced with the alphanumerical value extracted from the above figure:<pre>
http://localhost:8888/?token=<token>
</pre>
</li>
</ol>
## Shutting down JupyterLab 

You can shut down the JupyterLab server before the walltime limit by pressing <b>Ctrl-C twice</b> in the terminal that launched the interactive job.

If you have used MobaXterm to create an SSH tunnel, press <b>Ctrl-D</b> to shut down the tunnel.

= Adding kernels =

It is possible to add kernels for other programming languages, for a different Python version or for a persistent virtual environment that has all required packages and libraries for your project. Refer to [Making kernels for Jupyter](http://jupyter-client.readthedocs.io/en/latest/kernels.html) to learn more.

The installation of a new kernel is done in two steps:
# Installation of the packages that will allow the language interpreter to communicate with the Jupyter interface. 
# Creation of a file that will indicate to JupyterLab how to initiate a communication channel with the language interpreter. This file is called a <i>kernel spec file</i>, and it will be saved in a subfolder of `~/.local/share/jupyter/kernels`.

In the following sections, we provide a few examples of the kernel installation procedure.

## Julia Kernel 

Prerequisites:
# The configuration of a Julia kernel depends on a Python virtual environment and a `kernels` folder. If you do not have these dependencies, make sure to follow the first few instructions listed in <b>[Python kernel](#python_kernel.md)</b> (note: no Python kernel required).
# Since the installation of Julia packages requires an access to the internet, the configuration of a Julia kernel must be done in a <b>[remote shell session on a login node](ssh.md)</b>.

Once you have a Python virtual environment available and activated, you may configure the Julia kernel:

<ol>
<li>Load the <b>[Julia](julia.md)</b> module:
```bash
module load julia
```

</li><li>Install IJulia:
```bash

```
 julia
}}
</li><li><b>Important</b>: start or restart a new JupyterLab session before using the Julia kernel.</li>
</ol>

For more information, see the [IJulia documentation](https://github.com/JuliaLang/IJulia.jl).

### Installing more Julia packages 

As in the above installation procedure, it is required to install Julia packages from a login node, but the Python virtual environment could be deactivated:

<ol>
<li>Make sure the same Julia module is loaded:
```bash
module load julia
```

</li><li>Install any required package. For example with `Glob`:
```bash

```
 julia
}}
</li><li>The newly installed Julia packages should already be usable in a notebook executed by the Julia kernel.</li>
</ol>

## Python kernel 

In a terminal with an active session on the remote server,
you may configure a [Python virtual environment](python#creating_and_using_a_virtual_environment.md) with all the required [Python modules](available_python_wheels.md)
and a custom Python kernel for JupyterLab.
Here are the initial steps for the simplest Jupyter configuration
in a new Python virtual environment:

<ol>
<li>If you do not have a Python virtual environment, create one. Then, activate it:</li>
<ol>
<li>Start from a clean Bash environment (this is only required if you are using the Jupyter <i>Terminal</i> via [JupyterHub](jupyterhub.md) for the creation and configuration of the Python kernel):
```bash

```
$HOME bash -l
}}
</li><li>Load a Python module:
```bash
module load python
```

</li><li>Create a new Python virtual environment:
```bash
virtualenv --no-download $HOME/jupyter_py3
```

</li><li>Activate your newly created Python virtual environment:
```bash
source $HOME/jupyter_py3/bin/activate
```

</ol>
</li><li>Create the common `kernels` folder, which is used by all kernels you want to install:
```bash
mkdir -p ~/.local/share/jupyter/kernels
```

</li><li>Finally, install the Python kernel:
<ol>
<li>Install the `ipykernel` library:
```bash
pip install --no-index ipykernel
```

</li><li>Generate the kernel spec file. Replace <code><unique_name></code> with a name that will uniquely identify your kernel:
```bash
python -m ipykernel install --user --name <unique_name> --display-name "Python 3.x Kernel"
```

</li>
</ol>
</li><li><b>Important</b>: start or restart a new JupyterLab session before using the Python kernel.</li>
</ol>

For more information, see the [ipykernel documentation](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).

### Installing more Python libraries 

Based on the Python virtual environment configured in the previous section:

<ol>
<li>If you are using the Jupyter <i>Terminal</i> via [JupyterHub](jupyterhub.md), make sure the activated Python virtual environment is running in a clean Bash environment. See the above section for details.</li>
<li>Install any required library. For example, `numpy`:
```bash
pip install --no-index numpy
```

</li><li>The newly installed Python libraries can now be imported in any notebook using the `Python 3.x Kernel`.</li>
</ol>

## R Kernel 

Prerequisites:
# The configuration of an R kernel depends on a Python virtual environment and a `kernels` folder. If you do not have these dependencies, make sure to follow the first few instructions listed in <b>[Python kernel](#python_kernel.md)</b> (note: no Python kernel required).
# Since the installation of R packages requires an access to <b>[CRAN](https://cran.r-project.org/)</b>, the configuration of an R kernel must be done in a <b>[remote shell session on a login node](ssh.md)</b>.

Once you have a Python virtual environment available and activated, you may configure the R kernel:

<ol>
<li>Load an R module:
```bash
module load r/4.1
```

</li><li>Install the R kernel dependencies (`crayon`, `pbdZMQ`, `devtools`) - this will take up to 10 minutes, and packages should be installed in a local directory like `~/R/x86_64-pc-linux-gnu-library/4.1`:
```bash
R --no-save
```

```
> install.packages(c('crayon', 'pbdZMQ', 'devtools'), repos
</li><li>Install the R kernel.
```bash
devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))
```

</li><li>Install the R kernel spec file.
```bash
IRkernel::installspec()
```

</li><li><b>Important</b>: Start or restart a new JupyterLab session before using the R kernel.</li>
</ol>

For more information, see the [IRkernel documentation](https://irkernel.github.io/docs/).

### Installing more R packages 

The installation of R packages cannot be done from notebooks because there is no access to CRAN.
As in the above installation procedure, it is required to install R packages from a login node, but the Python virtual environment could be deactivated:

<ol>
<li>Make sure the same R module is loaded:
```bash
module load r/4.1
```

</li><li>Start the R shell and install any required package. For example with `doParallel`:
```bash
R --no-save
```

```
> install.packages('doParallel', repos
</li><li>The newly installed R packages should already be usable in a notebook executed by the R kernel.</li>
</ol>

= Running notebooks as Python scripts =
For longer run or analysis, we need to submit a [non-interactive job](running_jobs#use_sbatch_to_submit_jobs.md). We then need to convert our notebook to a Python script, create a submission script and submit it.

1. From the login node, create and activate a [virtual environment](python#creating_and_using_a_virtual_environment.md), then install <tt>nbconvert</tt> if not already available.

```bash
pip install --no-index nbconvert
```

2. Convert the notebook (or all notebooks) to Python scripts.

```bash
jupyter nbconvert --to python mynotebook.ipynb
```

3. Create your submission script, and submit your job.

In your submission script, run your converted notebook with:
<syntaxhighlight lang="bash">python mynotebook.py</syntaxhighlight>

and submit your non-interactive job:

```bash
sbatch my-submit.sh
```

= References =