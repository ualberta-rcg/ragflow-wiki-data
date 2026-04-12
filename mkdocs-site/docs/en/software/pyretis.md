---
title: "PyRETIS/en"
slug: "pyretis"
lang: "en"

source_wiki_title: "PyRETIS/en"
source_hash: "503277bd0b37b5aef2ecb8e121fb06dd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:32:15.956543+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "PyRETIS"
  - "rare event molecular simulations"
  - "virtual environment"
  - "transition interface sampling"
  - "Python library"

questions:
  - "What is the primary purpose of the PyRETIS library and what specific molecular simulation methods does it emphasize?"
  - "What are the specific installation steps and dependency requirements for setting up PyRETIS and its analysis tool, PyVisA, in a virtual environment?"
  - "Where can users find the official documentation and academic papers detailing the usage of PyRETIS?"
  - "What is the primary purpose of the PyRETIS library and what specific molecular simulation methods does it emphasize?"
  - "What are the specific installation steps and dependency requirements for setting up PyRETIS and its analysis tool, PyVisA, in a virtual environment?"
  - "Where can users find the official documentation and academic papers detailing the usage of PyRETIS?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[PyRETIS](http://www.pyretis.org/) is a Python library for rare event molecular simulations with emphasis on methods based on *transition interface sampling* (TIS) and *replica exchange transition interface sampling* (RETIS).

## Installing PyRETIS

We provide pre-compiled Python Wheels for PyRETIS in our [Wheelhouse](../programming/available_python_wheels.md) that are compatible with different versions of Python and can be installed within a [virtual Python environment](python.md#creating-and-using-a-virtual-environment).

As of July 2020, PyRETIS 2.5.0 is compatible with Python versions 3.6 and 3.7. According to the [PyRETIS installation instructions](http://www.pyretis.org/v2.5.0/user/install.html) the dependency [MDTraj](http://mdtraj.org/) has to be installed **after** PyRETIS.

A Python virtualenv with PyRETIS can be created by running the following series of commands (lines beginning with `#` are comments, `$` is a prompt and `(env_PyRETIS) $` is a prompt with an activated virtualenv):

```bash
# load the Python module we want to use, e.g. python/3.7:
module load python/3.7
 
# create a virtualenv
virtualenv --no-download ~/env_PyRETIS
 
# activate the virtualenv
source ~/env_PyRETIS/bin/activate
 
# install PyRETIS and then mdtraj
pip install --no-index pyretis
pip install --no-index mdtraj
 
# run PyRETIS
pyretisrun --help
```

In order to use `pyretisrun` (e.g. in our job scripts) we only need to activate the module again:

```bash
source ~/env_PyRETIS/bin/activate
pyretisrun --input INPUT.rst  --log_file LOG_FILE.log
```

PyRETIS also offers an analysis tool, named PyVisA. Its GUI requires PyQt5 to be executed. PyQt5 is installed part of the Qt modules.

!!! note
    In order to allow the Python version from the virtualenv to find PyQt5, it is important to first load the modules for Python and Qt before activating the PyRETIS virtualenv:

    ```bash
    module load python/3.7 qt/5.11.3
    source ~/env_PyRETIS/bin/activate
    pyretisanalyse  -pyvisa  ...
    ```

## Using PyRETIS

The usage of PyRETIS is documented on the PyRETIS website at [http://www.pyretis.org/](http://www.pyretis.org/) and in the group's papers:

1.  Lervik A, Riccardi E, van Erp TS. PyRETIS: A well-done, medium-sized python library for rare events. J Comput Chem. 2017;38: 2439–2451. [doi:10.1002/jcc.24900](https://doi.org/10.1002/jcc.24900)
2.  Riccardi E, Lervik A, Roet S, Aarøen O, Erp TS. PyRETIS 2: An improbability drive for rare events. J Comput Chem. 2020;41: 370–377. [doi:10.1002/jcc.26112](http://doi.org/10.1002/jcc.26112)