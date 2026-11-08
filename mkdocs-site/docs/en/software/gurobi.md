---
title: "Gurobi/en"
slug: "gurobi"
lang: "en"

source_wiki_title: "Gurobi/en"
source_hash: "dca7144f2166ee8170bcb6f9403cdb32"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:56:16.893255+00:00"

tags:
  - software

keywords:
  - "threads parameter"
  - "StdEnv modules"
  - "StdEnv/2023"
  - "pip install"
  - "single license checkout per job"
  - "physical cores"
  - "Gurobi license"
  - "/tmp/$USER"
  - "Gurobi python interface"
  - "slurm after dependency"
  - "offline wheel installation"
  - "Python version compatibility"
  - "Gurobi command-line"
  - "Gurobi license checkout"
  - "gurobipy"
  - "Gurobi environment"
  - "virtual environment"
  - "Slurm job submission"
  - "virtualenv"
  - "Gurobi"
  - "gurobipy installation"
  - "Python API"
  - "virtual Python environment"
  - "4096 simultaneous uses"
  - "distributed optimization up to 100 nodes"
  - "gurobi.env"
  - "Gurobi 11.0.1"
  - "$EBROOTGUROBI"
  - "Threads parameter"
  - "pip install gurobipy"
  - "gurobi module"
  - "recording API calls"
  - "license server load"
  - "24‑hour period"
  - "scipy-stack"
  - "SLURM after dependency"
  - "numpy"
  - "SLURM job script"
  - "job submission limit"
  - "Read-only file system"
  - "working directory"
  - "Java library path"
  - "unmanylinuxize.sh"

questions:
  - "What are the license limitations for using Gurobi on the Digital Research Alliance of Canada clusters?"
  - "How can a user verify that their Gurobi license is correctly configured and troubleshoot a failed license test?"
  - "What best practices are recommended to minimize Gurobi license checkouts and prevent intermittent checkout failures?"
  - "What mechanism does the script employ to minimize the Gurobi license checkout rate?"
  - "What is the maximum number of Gurobi license checkouts or jobs allowed on the cluster within a 24‑hour period?"
  - "How does requiring two licenses per job change the daily job submission limit?"
  - "How can you submit a chain of dependent Gurobi jobs to Slurm using a bash loop and the `--dependency=after:` option?"
  - "What are the required steps to run Gurobi interactively on a compute node, including module loading, parameter setting, and model optimization?"
  - "In the example Slurm scripts, how are Gurobi parameters such as `Threads` and `Method` configured, and why is generating a `gurobi.env` file important for Python‑based Gurobi jobs?"
  - "Why must the `gurobi.env` file be copied into the working directory for every job when using the Gurobi Python interface?"
  - "What default behavior does Gurobi exhibit regarding thread allocation if the `gurobi.env` file is missing?"
  - "How can the lack of a proper `gurobi.env` file negatively impact other users’ jobs on the same compute node?"
  - "Which combinations of Gurobi and Python versions are available in the different StdEnv modules?"
  - "How can you install Gurobi for Python within a virtual environment for Gurobi 10.0.3 (and older) versions?"
  - "What is the recommended procedure for installing Gurobi for Python when using Gurobi 11 (or newer) versions?"
  - "What are the required commands to create, activate, and prepare a virtual environment for installing Gurobi 11.0.1?"
  - "How should the gurobipy wheel be obtained and converted for installation on the system’s Gentoo‑prefix environment?"
  - "Why is Gurobi 11.0.0 omitted in the instructions, and which additional modules must be loaded to run the provided matrix example?"
  - "What error occurs when trying to install gurobipy under $EBROOTGUROBI in StdEnv/2023?"
  - "Where should the gurobipy source files be copied to avoid the read‑only file system error?"
  - "Which installation command should be run from the new location to successfully install gurobipy?"
  - "What is the purpose of using `pip install --find-links $PWD --no-index gurobipy` in this setup?"
  - "How is the Gurobi environment activated, and how does loading `gurobi` and the `scipy-stack` ensure that `$EBROOTGUROBI` and SciPy are available?"
  - "Which Python packages are needed to run the matrix example, and how were they installed in the environment?"
  - "How can I run Python scripts that use Gurobi within a virtual environment on the cluster, and what does a typical Slurm job script look like for this setup?"
  - "What additional steps are required in a Slurm job script to use Gurobi with Java, including module loading and library path configuration?"
  - "Where can I find tutorials, example notebooks, and other resources for using Gurobi with Jupyter notebooks?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Gurobi](http://www.gurobi.com/) is a commercial software suite for solving complex optimization problems. This wiki page describes the non-commercial use of Gurobi software on our clusters.

## License limitations

We support and provide a free license to use Gurobi on the [Nibi](../clusters/nibi.md), [Narval](../clusters/narval.md), [Fir](fir.md), [Rorqual](../clusters/rorqual.md) and [Trillium](../clusters/trillium.md) clusters. The license provides a total number of 4096 simultaneous uses (tokens in use) and permits distributed optimization with up to 100 nodes. A single user can run multiple simultaneous jobs. In order to use Gurobi, you must agree to certain conditions. Please [contact support](../support/technical_support.md) and include a copy of the following completed agreement. You will then be added into our license file as a user within a few days.

### Academic usage agreement

My Alliance username is "_______" and I am a member of the academic institution "_____________________." This message confirms that I will only use the Gurobi license provided on Digital Research Alliance of Canada systems for the purpose of non-commercial research project(s) to be published in publicly available article(s).

### Configuring your account
You do NOT need to create a `~/.licenses/gurobi.lic` file. The required settings to use our Gurobi license are configured by default when you load a Gurobi module on any cluster.

### Testing your license
To verify your username has successfully been added to the Alliance Gurobi license, log into any cluster and run the following command:

```bash
module load gurobi
gurobi_cl 1> /dev/null && echo Success || echo Fail
```

If it returns "Success" you can begin using Gurobi immediately. If the test returns "Fail" then check whether a file named *~/.license/gurobi* exists. If it does then remove it, reload the Gurobi module and run the test again. If it still returns "Fail" check whether there are any environment variables containing GUROBI being defined in either of your *~/.bashrc* or *~/.bash_profile* files. If you find any, comment or remove the lines then logout and login again, reload the Gurobi module and run the test again. If you still get "Fail", [contact support](../support/technical_support.md) for help.

### Minimizing license checkouts

Note that all Gurobi license checkouts are handled by a single license server located in Ontario; it is therefore important to limit license checkout attempts as much as possible. Rather than checking out a license for each invocation of Gurobi in a job—which may occur dozens or even hundreds of times—you should ensure that your program, whatever the language or computing environment used, only makes a single license checkout and then reuses this license token throughout the lifetime of the job. This will improve your job's performance because contacting a remote license server is very costly in time; moreover, responsiveness of our license server for everyone using Gurobi will also improve.

!!! warning
    Failure to use Gurobi carefully in this regard may ultimately result in random intermittent license checkout failures for all users. If this happens, you will be contacted and asked to kill all your jobs until your program is fixed and tested to ensure the problem is resolved.

Some documentation on this subject for C++ programs may be found [here](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license), explaining how to create a single Gurobi environment which can then be used for all your models. Python users can consult this [page](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license), which discusses how to implement this same idea of using a single environment and thus a single license token with multiple models. Other programs that call Gurobi, such as R, can also easily trigger the problem when run in parallel, especially when many simultaneous parallel jobs are submitted and/or run.

If you will be submitting many Gurobi jobs to the scheduler in a loop, use the following sample script (or equivalent) to ensure the jobs start gradually. Doing so will help minimize the license checkout rate and hence the load imposed on our Gurobi license server. The script uses the [Slurm](https://slurm.schedmd.com/sbatch.html) dependency `after` option introduced in [Advanced Job Submission](../running-jobs/advanced_job_submission.md). Currently, we request no more than 10000 Gurobi license checkouts/jobs be performed on a cluster over a 24-hour period. If your Gurobi program uses an algorithm that requires checking out two licenses per job, this would translate into submitting no more than 5000 jobs per day.

```bash
cat submit.sh
i=1; jobid=$(sbatch --parsable --output=slurm-%j-$i.out script.sh)
for i in {2..1000}; do
 jobid=$(sbatch --parsable --dependency=after:$jobid --output=slurm-%j-$i.out script.sh)
 [ "$?" -ne 0 ] && exit 1
done
```

## Interactive allocations

### Gurobi command-line tools

```bash
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
gurobi_cl Record=1 Threads=8 Method=2 ResultFile=p0033.sol LogFile=p0033.log $GUROBI_HOME/examples/data/p0033.mps
gurobi_cl --help
```

### Gurobi interactive shell

```bash
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
echo "Record 1" > gurobi.env
gurobi.sh
```
```
gurobi> m = read('/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/gurobi/8.1.1/examples/data/glass4.mps')
gurobi> m.Params.Threads = 8
gurobi> m.Params.Method = 2
gurobi> m.Params.ResultFile = "glass4.sol"
gurobi> m.Params.LogFile = "glass4.log"
gurobi> m.optimize()
gurobi> m.write('glass4.lp')
gurobi> m.status
gurobi> m.runtime
gurobi> help()
```
where
*   [https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)
*   [https://www.gurobi.com/documentation/8.1/refman/parameter_descriptions.html](https://www.gurobi.com/documentation/8.1/refman/parameter_descriptions.html)
*   [https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html](https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html)
*   [https://www.gurobi.com/documentation/8.1/refman/attributes.html](https://www.gurobi.com/documentation/8.1/refman/attributes.html)

### Replaying API calls
You can record API calls and repeat them with

```bash
gurobi_cl recording000.grbr
```

Reference: [https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)

## Cluster batch job submission

Once a Slurm script has been prepared for a Gurobi problem, it can be submitted to the queue by running the `sbatch script-name.sh` command. The job's status in the queue can then be checked by running the `sq` command. The following Slurm scripts demonstrate solving 2 problems provided in the `examples` directory of each Gurobi module.

### Data example

The following Slurm script utilizes the Gurobi command-line interface to solve a simple coin production model written in LP format. The last line demonstrates how [parameters](https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters.html) can be passed directly to the Gurobi command-line tool "gurobi_cl" using simple command line arguments. For help choosing values see the *Performance and Parameters* and *Algorithms and Search* sections found in the [Gurobi Knowledge Base](https://support.gurobi.com/hc/en-us/categories/360000840331-Knowledge-Base) and the online [Gurobi documentation](https://docs.gurobi.com/current/).
````sh title="script-lp_coins.sh"
#!/bin/bash
#SBATCH --account=def-group   # some account
#SBATCH --time=0-00:30        # specify time limit (D-HH:MM)
#SBATCH --cpus-per-task=8     # specify number threads
#SBATCH --mem=4G              # specify total memory
#SBATCH --nodes=1             # do not change

module load StdEnv/2023       # versions >= 10.0.1

module load gurobi/13.0.0

rm -f coins.sol
gurobi_cl Threads=$SLURM_CPUS_ON_NODE Method=2 ResultFile=coins.sol ${GUROBI_HOME}/examples/data/coins.lp
````

### Python example

This is an example Slurm script for solving a [simple facility location model](https://www.gurobi.com/documentation/9.5/examples/a_list_of_the_grb_examples.html) with [Gurobi Python](https://www.gurobi.com/documentation/9.5/examples/facility_py.html). The example shows how to set the [threads parameter](https://www.gurobi.com/documentation/9.5/refman/parameters.html#sec:Parameters) equal to the number of cores allocated to a job by dynamically generating a [gurobi.env](https://www.gurobi.com/documentation/9.5/quickstart_linux/using_a_grb_env_file.html) file into the working directory when using the [Gurobi Python interface](https://www.gurobi.com/documentation/9.5/refman/python_parameter_examples.html). This must be done for each submitted job, otherwise Gurobi will (by default) start as many execute [threads](https://www.gurobi.com/documentation/9.5/refman/threads.html#parameter:Threads) as there are physical cores on the compute node, potentially slowing down the job and negatively impacting other user jobs running on the same node.
````sh title="script-facility.sh"
#!/bin/bash
#SBATCH --account=def-group   # some account
#SBATCH --time=0-00:30        # specify time limit (D-HH:MM)
#SBATCH --cpus-per-task=4     # specify number threads
#SBATCH --mem=4G              # specify total memory
#SBATCH --nodes=1             # do not change

#module load StdEnv/2020      # for versions < 10.0.3
module load StdEnv/2023       # for versions > 10.0.3

module load gurobi/11.0.1

echo "Threads ${SLURM_CPUS_ON_NODE:-1}" > gurobi.env

gurobi.sh ${GUROBI_HOME}/examples/python/facility.py
````

## Using Gurobi in Python virtual environments

Gurobi brings its own version of Python which does not contain any 3rd-party Python packages except Gurobi. In order to use Gurobi together with popular Python packages like NumPy, Matplotlib, Pandas and others, we need to create a [virtual Python environment](python.md#creating-and-using-a-virtual-environment) in which we can install both `gurobipy` and for example `pandas`. Before we start, we need to decide which combination of versions for Gurobi and Python to use. Following is a list of the Python versions supported by the major Gurobi versions installed in the previous through current standard environments (StdEnv):

```bash
module load StdEnv/2016; module load gurobi/8.1.1; cd $EBROOTGUROBI/lib; ls -d python*
python2.7  python2.7_utf16  python2.7_utf32  python3.5_utf32  python3.6_utf32  python3.7_utf32

module load StdEnv/2020; module load gurobi/9.5.2; cd $EBROOTGUROBI/lib; ls -d python*
python2.7_utf16  python2.7_utf32  python3.10_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32

module load StdEnv/2023; module load gurobi/10.0.3; cd $EBROOTGUROBI/lib; ls -d python*
python3.10_utf32  python3.11_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32

module load StdEnv/2023; module load gurobi/11.0.1; cd $EBROOTGUROBI/lib; ls -d python*
python3.11
```

### Installing Gurobi for Python

As mentioned near the end of this official document [How do I install Gurobi for Python?](http://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), the previously recommended method for installing Gurobi for Python with `setup.py` has been deprecated to only be usable with Gurobi 10 versions (and older). Section *Gurobi 11 versions (and newer)* below shows how to simultaneously download a compatible binary wheel from [pypi.org](https://pypi.org/project/gurobipy/) and convert it into a format usable with the newly recommended command to install Gurobi for Python.

### Gurobi versions 10.0.3 (and older)

The following steps need to be done once per system and are usable with StdEnv/2023 and older. First, load the modules to [create the virtual environment](python.md#creating-and-using-a-virtual-environment) and activate it:

```bash
module load gurobi/10.0.3 python
virtualenv --no-download  ~/env_gurobi
source ~/env_gurobi/bin/activate
```
Now install any Python packages you want to use, in this case `pandas`:

```bash
pip install --no-index  pandas
```
Next, install gurobipy in the environment. Note that as of StdEnv/2023 the installation can no longer be done under $EBROOTGUROBI using the command `python setup.py build --build-base /tmp/${USER} install` since a fatal error (`error: could not create 'gurobipy.egg-info': Read-only file system`) will occur. Instead, the required files need to be copied elsewhere (such as /tmp/$USER) and the installation made from there, for example:

```bash
mkdir /tmp/$USER
cp -r $EBROOTGUROBI/{lib,setup.py} /tmp/$USER
cd /tmp/$USER
python setup.py install
/home/roberpj/env_gurobi/lib/python3.11/site-packages/setuptools/_core_metadata.py:158: SetuptoolsDeprecationWarning: Invalid config.
!!

        ********************************************************************************
        newlines are not allowed in `summary` and will break in the future
        ********************************************************************************

!!
  write_field('Summary', single_line(summary))
removing /tmp/roberpj/build
deactivate
```

### Gurobi versions 11.0.0 (and newer)

Once again, the following steps need to be done once per system and are usable with StdEnv/2023 and older. First load the modules to [create the virtual environment](python.md#creating-and-using-a-virtual-environment) and activate it. Version 11.0.0 is skipped since it has been observed to seg fault in at least one example versus Version 11.0.1 which runs smoothly.

```bash
module load gurobi/11.0.1 python
virtualenv --no-download  ~/env_gurobi
source ~/env_gurobi/bin/activate
```
As before, install any needed Python packages. Since the following matrix example requires `numpy`, we install the pandas package:

```bash
pip install --no-index  pandas
```
Next install gurobipy into the environment. As mentioned above and in [this article](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python) the use of setup.py to install Gurobi for python is deprecated starting with Gurobi 11. Both pip and conda are given as alternatives; however, since conda should not be used on our systems, the pip approach will be demonstrated here. The installation of gurobipy is slightly complicated since our Linux systems are set up with gentoo prefix. As a result neither A) the recommended command to download and install the gurobipy extension from the public PyPI server `pip install gurobipy==11.0.1` mentioned in the article line or B) the offline command to install the wheel with `python -m pip install --find-links <wheel-dir> --no-index gurobipy`, will work. Instead, we have prepared a script to download and simultaneously convert the existing wheel into a usable format with a new name. There is one caveat; for each new Gurobi version, you must go into [https://pypi.org/project/gurobipy/11.0.1/#history](https://pypi.org/project/gurobipy/11.0.1/#history) and click on the desired version followed by the `Download files` button located in the menu on the left. Finally, click to copy the `https` link for the wheel file (named `gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl` in the case of Gurobi 11.0.1) and paste it as the `--url` argument as shown below :

```bash
wget https://raw.githubusercontent.com/ComputeCanada/wheels_builder/main/unmanylinuxize.sh
chmod u+rx unmanylinuxize.sh
./unmanylinuxize.sh --package gurobipy --version 11.0.1 --url \
https://files.pythonhosted.org/packages/1c/96/4c800e7cda4a1688d101a279087646912cf432b0f61ff5c816f0bc8503e0/gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
ls
gurobipy-11.0.1-cp311-cp311-linux_x86_64.whl  unmanylinuxize.sh
python -m pip install --find-links $PWD --no-index gurobipy
deactivate
```

### Running Gurobi in the environment

Once created our Gurobi environment can be activated and used at any time. To demonstrate this we also load gurobi (so $EBROOTGUROBI is defined) and `scipy-stack` (so scipy is available). Both are required to run the matrix example (along with numpy that was already installed into our environment with pip in a previous step above via pandas).

```bash
module load gurobi/11.0.1 scipy-stack
source ~/env_gurobi/bin/activate
```

Python scripts, such as the examples provided with the gurobi module can now be run (within the virtual environment) using python :

```python
python $EBROOTGUROBI/examples/python/matrix1.py
```

Likewise custom python scripts such as the following can be run as jobs in the queue by writing slurm scripts that load your virtual environment.

```python
import pandas as pd
import numpy as np
import gurobipy as gurobi
from gurobipy import *
etc
```

Submit your script to the queue by running `sbatch my_slurm_script.sh` as per usual :

````sh title="my_slurm_script.sh"
#!/bin/bash
#SBATCH --account=def-somegrp  # specify an account
#SBATCH --time=0-00:30         # time limit (D-HH:MM)
#SBATCH --nodes=1              # run job on one node
#SBATCH --cpus-per-task=4      # specify number of CPUS
#SBATCH --mem=4000M            # specify total MB memory

module load StdEnv/2023
module load gurobi/11.0.1
# module load scipy-stack      # uncomment if needed

echo "Threads ${SLURM_CPUS_ON_NODE:-1}" > gurobi.env

source ~/env_gurobi/bin/activate
python my_gurobi_script.py
````

Further information regarding how to create and use python virtual environments within job scripts can be found [here](python.md#creating-virtual-environments-inside-of-your-jobs).

## Using Gurobi with Java

To use Gurobi with Java, you will also need to load a Java module and add an option to your Java command in order to allow the Java virtual environment to find the Gurobi libraries. A sample job script is below:
````sh title="gurobi-java.sh"
#!/bin/bash
#SBATCH --time=0-00:30        # time limit (D-HH:MM)
#SBATCH --cpus-per-task=1     # number of CPUs (threads) to use
#SBATCH --mem=4096M           # memory per CPU (in MB)

module load java/14.0.2
module load gurobi/9.1.2

java -Djava.library.path=$EBROOTGUROBI/lib -Xmx4g -jar my_java_file.jar
````

## Using Gurobi with Jupyter notebooks

Various topics can be found by visiting [Resources](https://www.gurobi.com/resources/), then clicking [Code and Modeling Examples](https://www.gurobi.com/resources/?category-filter=code-example) and finally [Optimization with Python – Jupyter Notebook Modeling Examples](https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/). Alternatively visit [support.gurobi.com](https://support.gurobi.com/) and search on *Jupyter Notebooks*.

A demo case of using Gurobi with Jupyter notebooks on our systems can be found in this [video recording, i.e. at time 38:28](https://youtu.be/Qk3Le5HBxeg?t=2310).

## Cite Gurobi

[How do I cite Gurobi software for an academic publication?](https://support.gurobi.com/hc/en-us/articles/360013195592-How-do-I-cite-Gurobi-software-for-an-academic-publication-)

## Getting Help

The Gurobi general Help Center is located [here](https://support.gurobi.com/hc/en-us).
Gurobot a new Gurobi AI Agent is available [here](https://portal.gurobi.com/iam/chat).
The official online Gurobi documentation is [here](https://docs.gurobi.com/13.0/).
For help using Gurobi on the Alliance [submit a ticket](../support/technical_support.md).