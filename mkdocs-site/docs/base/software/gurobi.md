---
title: "Gurobi"
slug: "gurobi"
lang: "base"

source_wiki_title: "Gurobi"
source_hash: "d27d2cb901e6fc80938d2fecfab903de"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:49:09.294056+00:00"

tags:
  - software

keywords:
  - "--url argument"
  - "Resources"
  - "license checkouts"
  - "job submission"
  - "Python virtual environments"
  - "download script"
  - "installation"
  - "EBROOTGUROBI/lib"
  - "Gurobi"
  - "Slurm"
  - "license checkout rate"
  - "https link"
  - "gurobi_cl"
  - "academic publication"
  - "Performance and Parameters"
  - "cluster"
  - "virtual environment"
  - "Gurobi version"
  - "Slurm job script"
  - "wheel file"
  - "python"
  - "Modeling Examples"
  - "Slurm script"
  - "gurobi"
  - "StdEnv/2023"
  - "module load"
  - "gurobipy"
  - "Jupyter notebooks"
  - "Python virtual environment"
  - "video recording"
  - "license server"
  - "Batch job submission"
  - "optimization problems"
  - "Interactive allocations"
  - "Algorithms and Search"
  - "Gurobi license server"
  - "cite Gurobi"
  - "Gurobi for Python"
  - "Java"
  - "slurm dependency"
  - "Optimization with Python"
  - "Gurobi documentation"
  - "Jupyter Notebooks"
  - "Gurobi Knowledge Base"
  - "Threads parameter"
  - "academic usage agreement"
  - "bash script"

questions:
  - "What steps must a user take to agree to the academic usage terms and gain access to the Gurobi license?"
  - "How can a user test their account to verify that the Gurobi license has been successfully configured?"
  - "Why is it critical to minimize license checkouts, and what methods are recommended to reduce the load on the license server?"
  - "How can a user request an interactive allocation to run Gurobi using either the command-line tool or the interactive shell?"
  - "What is the command used to replay previously recorded Gurobi API calls?"
  - "How do you submit a prepared Slurm script for a Gurobi problem to the cluster's batch job queue?"
  - "What specific Slurm feature does the script utilize to help minimize the load on the Gurobi license server?"
  - "What is the maximum number of Gurobi license checkouts permitted on a cluster within a 24-hour period?"
  - "How does the daily job submission limit change if a Gurobi program requires two licenses per job?"
  - "What topics are covered in the referenced sections of the Gurobi Knowledge Base?"
  - "Where can users access the extensive online documentation for Gurobi?"
  - "What job scheduling parameters are defined in the provided bash script snippet?"
  - "Why is it necessary to dynamically generate a `gurobi.env` file to set the thread parameter when submitting a Gurobi Python job through Slurm?"
  - "Why do users need to create a Python virtual environment to use Gurobi alongside packages like NumPy or Pandas?"
  - "How can a user check which specific Python versions are supported by different Gurobi modules across various standard environments?"
  - "Why is the recommended installation method for Gurobi for Python different for versions 11 and newer compared to versions 10 and older?"
  - "What workaround must be used when installing Gurobi 10.0.3 or older to bypass the read-only file system error associated with the setup.py command?"
  - "Why do standard pip installation commands fail for Gurobi 11 on this system, and how can users successfully download and convert the required wheel file?"
  - "Which versions of the Gurobi module are being loaded in the provided terminal commands?"
  - "What specific Python versions and encodings are listed within the Gurobi library directories?"
  - "What environment variable is used to navigate to the Gurobi library path after loading the standard environment?"
  - "What is the primary purpose of the prepared script regarding the existing wheel?"
  - "What specific manual steps must a user perform on the PyPI website for each new Gurobi version?"
  - "How is the copied wheel file link passed to the script during execution?"
  - "How do you configure a Slurm job script to run a Python script within an activated Gurobi virtual environment?"
  - "What specific command-line option is required to allow a Java virtual environment to locate Gurobi libraries?"
  - "Where can users find official resources and modeling examples for using Gurobi with Jupyter Notebooks?"
  - "What is the step-by-step navigation path on the Gurobi website to find the Jupyter Notebook modeling examples?"
  - "What alternative search method can be used on the Gurobi support site to locate these resources?"
  - "What specific programming language and tool are featured in the optimization modeling examples mentioned in the text?"
  - "Where can users find a video demonstration of using Gurobi with Jupyter notebooks?"
  - "At what specific timestamp does the Gurobi demonstration begin in the provided video recording?"
  - "What resource should be consulted to learn how to properly cite Gurobi software in an academic publication?"
  - "Where can users find a video demonstration of using Gurobi with Jupyter notebooks?"
  - "At what specific timestamp does the Gurobi demonstration begin in the provided video recording?"
  - "What resource should be consulted to learn how to properly cite Gurobi software in an academic publication?"

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

We support and provide a free license to use Gurobi on the [Nibi](nibi.md), [Narval](narval.md), [Fir](fir.md), [Rorqual](rorqual.md) and [Trillium](trillium.md) clusters. The license provides a total number of 4096 simultaneous uses (tokens in use) and permits distributed optimization with up to 100 nodes. A single user can run multiple simultaneous jobs. In order to use Gurobi, you must agree to certain conditions. Please [contact support](technical-support.md) and include a copy of the following completed agreement. You will then be added into our license file as a user within a few days.

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

If it returns "Success" you can begin using Gurobi immediately. If the test returns "Fail" then check whether a file named *~/.license/gurobi* exists. If it does then remove it, reload the gurobi module and run the test again. If it still returns "Fail" check whether there are any environment variables containing GUROBI being defined in either of your *~/.bashrc* or *~/.bash_profile* files. If you find any, comment or remove the lines then logout and login again, reload the Gurobi module and run the test again. If you still get "Fail", [contact support](technical-support.md) for help.

### Minimizing license checkouts

Note that all Gurobi license checkouts are handled by a single license server located in Ontario; it is therefore important to limit license checkout attempts as much as possible. Rather than checking out a license for each invocation of Gurobi in a job---which may occur dozens or even hundreds of times---you should ensure that your program, whatever the language or computing environment used, only makes a single license checkout and then reuses this license token throughout the lifetime of the job. This will improve your job's performance because contacting a remote license server is very costly in time; moreover, responsiveness of our license server for everyone using Gurobi will also improve.

!!! warning
    Failure to use Gurobi carefully in this regard may ultimately result in random intermittent license checkout failures for all users. If this happens, you will be contacted and asked to kill all your jobs until your program is fixed and tested to ensure the problem is resolved.

Some documentation on this subject for C++ programs may be found [here](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license), explaining how to create a single Gurobi environment which can then be used for all your models. Python users can consult this [page](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license), which discusses how to implement this same idea of using a single environment and thus a single license token with multiple models. Other programs that call Gurobi, such as R, can also easily trigger the problem when run in parallel, especially when many simultaneous parallel jobs are submitted and/or run.

If you will be submitting many Gurobi jobs to the scheduler in a loop, use the following sample script (or equivalent) to ensure the jobs start gradually. Doing so will help minimize the license checkout rate and hence the load imposed on our Gurobi license server. The script uses the [Slurm](https://slurm.schedmd.com/sbatch.html) dependency `--after` option introduced in [Advanced Job Submission](advanced-job-submission.md). Currently, we request no more than 10,000 Gurobi license checkouts/jobs be performed on a cluster over a 24-hour period. If your Gurobi program uses an algorithm that requires checking out two licenses per job, this would translate into submitting no more than 5,000 jobs per day.

```bash
[l2(nibi):~] cat submit.sh
i=1; jobid=$(sbatch --parsable --output=slurm-%j-$i.out script.sh)
for i in {2..1000}; do
 jobid=$(sbatch --parsable --dependency=after:$jobid --output=slurm-%j-$i.out script.sh)
 [ "$?" -ne 0 ] && exit 1
done
```

## Interactive allocations

### Gurobi command-line tools

```bash
[gra-login2:~] salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
[gra800:~] module load gurobi
[gra800:~] gurobi_cl Record=1 Threads=8 Method=2 ResultFile=p0033.sol LogFile=p0033.log $GUROBI_HOME/examples/data/p0033.mps
[gra800:~] gurobi_cl --help
```

### Gurobi interactive shell

```bash
[gra-login2:~] salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
[gra800:~] module load gurobi
[gra800:~] echo "Record 1" > gurobi.env    # see *
[gra800:~] gurobi.sh
gurobi> m = read('/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/gurobi/8.1.1/examples/data/glass4.mps')
gurobi> m.Params.Threads = 8               # see **
gurobi> m.Params.Method = 2
gurobi> m.Params.ResultFile = "glass4.sol"
gurobi> m.Params.LogFile = "glass4.log"
gurobi> m.optimize()
gurobi> m.write('glass4.lp')
gurobi> m.status                           # see ***
gurobi> m.runtime                          # see ****
gurobi> help()
```

where:

*   **`Record 1`**: [Gurobi Documentation - Recording API Calls](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)
*   **`m.Params.Threads`**: [Gurobi Documentation - Parameter Descriptions](https://www.gurobi.com/documentation/8.1/refman/parameter_descriptions.html)
*   **`m.status`**: [Gurobi Documentation - Optimization Status Codes](https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html)
*   **`m.runtime`**: [Gurobi Documentation - Attributes](https://www.gurobi.com/documentation/8.1/refman/attributes.html)

### Replaying API calls

You can record API calls and repeat them with

```bash
[gra800:~] gurobi_cl recording000.grbr
```

Reference: [https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)

## Cluster batch job submission

Once a Slurm script has been prepared for a Gurobi problem, it can be submitted to the queue by running the `sbatch script-name.sh` command. The job's status in the queue can then be checked by running the `sq` command. The following Slurm scripts demonstrate solving 2 problems provided in the `examples` directory of each Gurobi module.

### Data example

The following Slurm script utilizes the [Gurobi command-line interface](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_the_model_using_th.html) to solve a [simple coin production model](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_a_simple_model_the.html) written in [LP format](https://www.gurobi.com/documentation/9.5/refman/lp_format.html). The last line demonstrates how [parameters](https://www.gurobi.com/documentation/9.5/refman/parameters.html) can be passed directly to the Gurobi command-line tool `gurobi_cl` using simple command-line arguments. For help selecting which [parameters](https://www.gurobi.com/documentation/9.5/refman/parameters.html) are best used for a particular problem and for choosing optimal values, refer to both the *Performance and Parameters* and *Algorithms and Search* sections found in the [Gurobi Knowledge Base](https://support.gurobi.com/hc/en-us/categories/360000840331-Knowledge-Base) as well as the extensive online [Gurobi documentation](https://www.gurobi.com/documentation/).

=== "script-lp_coins.sh"
    ```bash
    #!/bin/bash
    #SBATCH --account=def-group   # some account
    #SBATCH --time=0-00:30        # specify time limit (D-HH:MM)
    #SBATCH --cpus-per-task=8     # specify number threads
    #SBATCH --mem=4G              # specify total memory
    #SBATCH --nodes=1             # do not change

    #module load StdEnv/2016      # for versions < 9.0.3
    module load StdEnv/2020       # for versions > 9.0.2

    module load gurobi/9.5.0

    rm -f coins.sol
    gurobi_cl Threads=$SLURM_CPUS_ON_NODE Method=2 ResultFile=coins.sol ${GUROBI_HOME}/examples/data/coins.lp
    ```

### Python example

This is an example Slurm script for solving a [simple facility location model](https://www.gurobi.com/documentation/9.5/examples/a_list_of_the_grb_examples.html) with [Gurobi Python](https://www.gurobi.com/documentation/9.5/examples/facility_py.html). The example shows how to set the threads [parameter](https://www.gurobi.com/documentation/9.5/refman/parameters.html#sec:Parameters) equal to the number of cores allocated to a job by dynamically generating a [`gurobi.env`](https://www.gurobi.com/documentation/9.5/quickstart_linux/using_a_grb_env_file.html) file into the working directory when using the [Gurobi Python interface](https://www.gurobi.com/documentation/9.5/refman/python_parameter_examples.html). This must be done for each submitted job, otherwise Gurobi will (by default) start as many execute [threads](https://www.gurobi.com/documentation/9.5/refman/threads.html#parameter:Threads) as there are physical cores on the compute node, potentially slowing down the job and negatively impacting other user jobs running on the same node.

=== "script-facility.sh"
    ```bash
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
    ```

## Using Gurobi in Python virtual environments

Gurobi brings its own version of Python which does not contain any 3rd-party Python packages except Gurobi. In order to use Gurobi together with popular Python packages like NumPy, Matplotlib, Pandas and others, we need to create a [virtual Python environment](python.md#creating-and-using-a-virtual-environment) in which we can install both `gurobipy` and for example `pandas`. Before we start, we need to decide which combination of versions for Gurobi and Python to use. Following is a list of the Python versions supported by the major Gurobi versions installed in the previous through current standard environments (StdEnv):

```bash
[name@server ~] module load StdEnv/2016; module load gurobi/8.1.1; cd $EBROOTGUROBI/lib; ls -d python*
python2.7  python2.7_utf16  python2.7_utf32  python3.5_utf32  python3.6_utf32  python3.7_utf32

[name@server ~] module load StdEnv/2020; module load gurobi/9.5.2; cd $EBROOTGUROBI/lib; ls -d python*
python2.7_utf16  python2.7_utf32  python3.10_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32

[name@server ~] module load StdEnv/2023; module load gurobi/10.0.3; cd $EBROOTGUROBI/lib; ls -d python*
python3.10_utf32  python3.11_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32

[name@server ~] module load StdEnv/2023; module load gurobi/11.0.1; cd $EBROOTGUROBI/lib; ls -d python*
python3.11
```

### Installing Gurobi for Python

As mentioned near the end of this official document [How do I install Gurobi for Python?](http://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), the previously recommended method for installing Gurobi for Python with `setup.py` has been deprecated to only be usable with Gurobi 10 versions (and older). Section *Gurobi 11 versions (and newer)* below shows how to simultaneously download a compatible binary wheel from [pypi.org](https://pypi.org/project/gurobipy/) and convert it into a format usable with the newly recommended command to install Gurobi for Python.

### Gurobi versions 10.0.3 (and older)

The following steps need to be done once per system and are usable with StdEnv/2023 and older. First, load the modules to [create the virtual environment](python.md#creating-and-using-a-virtual-environment) and activate it:

```bash
[name@server ~] $ module load gurobi/10.0.3 python
[name@server ~] $ virtualenv --no-download  ~/env_gurobi
[name@server ~] $ source ~/env_gurobi/bin/activate
```

Now install any Python packages you want to use, in this case `pandas`:

```bash
(env_gurobi) [name@server ~] $ pip install --no-index  pandas
```

Next, install `gurobipy` in the environment. Note that as of StdEnv/2023 the installation can no longer be done under `$EBROOTGUROBI` using the command `python setup.py build --build-base /tmp/${USER} install` since a fatal error (`error: could not create 'gurobipy.egg-info': Read-only file system`) will occur. Instead, the required files need to be copied elsewhere (such as `/tmp/$USER`) and the installation made from there, for example:

```bash
(env_gurobi) [name@server ~] $ mkdir /tmp/$USER
(env_gurobi) [name@server ~] $ cp -r $EBROOTGUROBI/{lib,setup.py} /tmp/$USER
(env_gurobi) [name@server ~] $ cd /tmp/$USER
(env_gurobi) [name@server ~] $ python setup.py install
# Output from the previous command
(env_gurobi) [name@gra-login1:/tmp/name] python setup.py install
/home/name/env_gurobi/lib/python3.11/site-packages/setuptools/_core_metadata.py:158: SetuptoolsDeprecationWarning: Invalid config.
!!

        ********************************************************************************
        newlines are not allowed in `summary` and will break in the future
        ********************************************************************************

!!
  write_field('Summary', single_line(summary))
removing /tmp/name/build
(env_gurobi) [name@gra-login1:/tmp/name]
(env_gurobi) [name@server ~] $ deactivate
[name@server ~]
```

### Gurobi versions 11.0.0 (and newer)

Once again, the following steps need to be done once per system and are usable with StdEnv/2023 and older. First load the modules to [create the virtual environment](python.md#creating-and-using-a-virtual-environment) and activate it. Version 11.0.0 is skipped since it has been observed to seg fault in at least one example versus Version 11.0.1 which runs smoothly.

```bash
[name@server ~] $ module load gurobi/11.0.1 python
[name@server ~] $ virtualenv --no-download  ~/env_gurobi
[name@server ~] $ source ~/env_gurobi/bin/activate
```

As before, install any needed Python packages. Since the following matrix example requires `numpy`, we install the pandas package:

```bash
(env_gurobi) [name@server ~] $ pip install --no-index  pandas
```

Next install `gurobipy` into the environment. As mentioned above and in [this article](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python) the use of `setup.py` to install Gurobi for Python is deprecated starting with Gurobi 11. Both `pip` and `conda` are given as alternatives; however, since `conda` should not be used on our systems, the `pip` approach will be demonstrated here. The installation of `gurobipy` is slightly complicated since our Linux systems are set up with gentoo prefix. As a result neither A) the recommended command to download and install the `gurobipy` extension from the public PyPI server `pip install gurobipy==11.0.1` mentioned in the article line or B) the offline command to install the wheel with `python -m pip install --find-links <wheel-dir> --no-index gurobipy`, will work. Instead, we have prepared a script to download and simultaneously convert the existing wheel into a usable format with a new name. There is one caveat; for each new Gurobi version, you must go into [https://pypi.org/project/gurobipy/11.0.1/#history](https://pypi.org/project/gurobipy/11.0.1/#history) and click on the desired version followed by the `Download files` button located in the menu on the left. Finally, click to copy the HTTPS link for the wheel file (named `gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl` in the case of Gurobi 11.0.1) and paste it as the `--url` argument as shown below:

```bash
(env_gurobi) [name@server ~] $ wget https://raw.githubusercontent.com/ComputeCanada/wheels_builder/main/unmanylinuxize.sh
(env_gurobi) [name@server ~] $ chmod u+rx unmanylinuxize.sh
(env_gurobi) [name@server ~] $ ./unmanylinuxize.sh --package gurobipy --version 11.0.1 --url \
> https://files.pythonhosted.org/packages/1c/96/4c800e7cda4a1688d101a279087646912cf432b0f61ff5c816f0bc8503e0/gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
(env_gurobi) [name@server ~] $ ls
gurobipy-11.0.1-cp311-cp311-linux_x86_64.whl  unmanylinuxize.sh
(env_gurobi) [name@server ~] $ python -m pip install --find-links $PWD --no-index gurobipy
(env_gurobi) [name@server ~] $ deactivate
[name@server ~]
```

### Running Gurobi in the environment

Once created, our Gurobi environment can be activated and used at any time. To demonstrate this, we also load gurobi (so `$EBROOTGUROBI` is defined) and `scipy-stack` (so `scipy` is available). Both are required to run the matrix example (along with `numpy` that was already installed into our environment with pip in a previous step above via pandas).

```bash
[name@server ~] $ module load gurobi/11.0.1 scipy-stack
[name@server ~] $ source ~/env_gurobi/bin/activate
(env_gurobi) [name@server ~]
```

Python scripts, such as the examples provided with the gurobi module, can now be run (within the virtual environment) using python:

```bash
(env_gurobi) [name@server ~] $ python $EBROOTGUROBI/examples/python/matrix1.py
```

Likewise, custom Python scripts such as the following can be run as jobs in the queue by writing Slurm scripts that load your virtual environment.

```bash
[name@server ~] $ cat my_gurobi_script.py
```
```python
import pandas as pd
import numpy as np
import gurobipy as gurobi
from gurobipy import *
# etc
```

Submit your script to the queue by running `sbatch my_slurm_script.sh` as per usual:

=== "my_slurm_script.sh"
    ```bash
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
    ```

Further information regarding how to create and use Python virtual environments within job scripts can be found [here](python.md#creating-virtual-environments-inside-of-your-jobs).

## Using Gurobi with Java

To use Gurobi with Java, you will also need to load a Java module and add an option to your Java command in order to allow the Java virtual environment to find the Gurobi libraries. A sample job script is below:

=== "gurobi-java.sh"
    ```bash
    #!/bin/bash
    #SBATCH --time=0-00:30        # time limit (D-HH:MM)
    #SBATCH --cpus-per-task=1     # number of CPUs (threads) to use
    #SBATCH --mem=4096M           # memory per CPU (in MB)

    module load java/14.0.2
    module load gurobi/9.1.2

    java -Djava.library.path=$EBROOTGUROBI/lib -Xmx4g -jar my_java_file.jar
    ```

## Using Gurobi with Jupyter notebooks

Various topics can be found by visiting [Resources](https://www.gurobi.com/resources/), then clicking [Code and Modeling Examples](https://www.gurobi.com/resources/?category-filter=code-example) and finally [Optimization with Python – Jupyter Notebook Modeling Examples](https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/). Alternatively, visit [support.gurobi.com](https://support.gurobi.com/) and search on *Jupyter Notebooks*.

A demo case of using Gurobi with Jupyter notebooks on our systems can be found in this [video recording, i.e., at time 38:28](https://youtu.be/Qk3Le5HBxeg?t=2310).

## Cite Gurobi

Please see [How do I cite Gurobi software for an academic publication?](https://support.gurobi.com/hc/en-us/articles/360013195592-How-do-I-cite-Gurobi-software-for-an-academic-publication?).