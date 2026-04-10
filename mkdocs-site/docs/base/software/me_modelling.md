---
title: "ME modelling"
slug: "me_modelling"
lang: "base"

source_wiki_title: "ME modelling"
source_hash: "ffcb46c6b5781a65b6baef30b51a1ffd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:11:26.377474+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Introduction
Models of metabolism and expression (ME-models) are mathematical knowledge bases that integrate information on both the expression machinery and metabolism of a cell and are capable of generating predictions of phenotype. They are formulated as optimization problems where a bisection method finds the optimum growth rate and proteome allocation. Solving these complex methods hence requires an efficient computing approach that is best obtained in low-level programming languages. The solveME[^solveME] Python wrapper allows the utilization of Fortran efficiency and the qMinos solver[^qMinos]. The CobraME[^CobraME] package provides useful functions to build and solve ME-models with the ease of Python. The EcoliME package provides the ability to construct the *i*JL1678b[^iJL1678b] ME-model of *Escherichia coli*.

## Installation
The ME-modelling environment contains many dependencies that are more easily managed by the use of a Python virtual environment.
We provide the steps to set up a virtual environment in Python 2 using the virtualenv software; using conda or venv would also work. More detailed information on how to create a virtual environment can be found [here](https://help.dreamhost.com/hc/en-us/articles/215489338-Installing-and-using-virtualenv-with-Python-2).

### Setup the Virtual Environment
We suggest creating a folder containing all ME-modelling related packages.
Set up a virtual environment for ME-modelling using virtualenv in Python 2.7, on mp2:

```bash
ml python/2.7.14
pip install virtualenv --user
mkdir ME_modelling
cd ME_modelling
virtualenv -p /home/username/opt/python-2.7.15/bin/python ME_env
```

Activate the virtual environment. The virtual environment remains active in all following steps:

```bash
source ME_env/bin/activate
```

Install required dependencies. Note that more-itertools==5.0.0 is the last Python 2.7 supported version:

```bash
pip install pandas
pip install sympy
pip install more-itertools==5.0.0
```

!!! important "Important"
    The Python compiler should be GCC > 5.4.0. Compiling numpy with this version is also necessary:

```bash
pip install git+https://github.com/numpy/numpy@v1.14.0
```

Install cobrapy==0.5.11 within the virtual environment. The required cobrapy==0.5.11 is not available for installation via `pip install`. This version can be obtained from GitHub:

```bash
git clone https://github.com/opencobra/cobrapy.git
cd cobrapy-0.5.11
python setup.py develop
```

### Install ME-Modelling Software
Get solvemepy from GitHub (https://github.com/SBRG/solvemepy):

```bash
git clone https://github.com/SBRG/solvemepy.git
```

Obtain quadMinos. This quad precision solver can be obtained for academic use from Professor Michael Saunders at Stanford University. Once downloaded, compile the solver; these installation steps can be found [here](https://github.com/SBRG/solvemepy):

```bash
cd solvemepy
cp Makefile.defs quadLP_root/minos56/
cp Makefile.defs quadLP_root/qminos56/
cd [solveme_root]
cp [qminos_root]/qminos56/lib/libquadminos.a ./
cp [qminos_root]/minos56/lib/libminos.a ./
```

Install solvemepy:

```bash
cd solvemepy
python setup.py develop
```

Get CobraME from GitHub (https://github.com/SBRG/cobrame) and install:

```bash
git clone https://github.com/SBRG/cobrame.git
cd cobrame
python setup.py develop
```

Get EcoliME from GitHub (https://github.com/SBRG/ecolime/tree/master/ecolime) and install:

```bash
git clone https://github.com/SBRG/ecolime.git
cd ecolime
python setup.py develop
```

## Building and Solving a ME-Model
CobraME[^CobraME] conveniently contains all scripts and files required to build a complete ME-model for *Escherichia coli* from scratch.

The ME-model can be built from:

1.  A Jupyter Notebook
2.  A Python script

### Virtual Environment in Jupyter Notebook
A Jupyter Notebook can be run on an interactive node. The information for installation can be found [here](https://docs.computecanada.ca/wiki/Jupyter).

To build, solve, and modify a ME-model in Jupyter, set up the virtual environment previously created to run in Jupyter Lab or Jupyter Notebook. [Click for more information on virtual environment in IPython.](https://anbasile.github.io/programming/2017/06/25/jupyter-venv/) In the **activated** virtual environment:

```bash
pip install ipykernel
ipython kernel install --user --name=ME_env_name
```

The [ecoliME](https://github.com/SBRG/ecolime) package contains a Jupyter Notebook to build the *i*JL1768b *E. coli* ME-model:
<https://github.com/SBRG/ecolime/blob/master/ecolime/build_me_model.ipynb>
and to solve the ME-model:
<https://github.com/SBRG/ecolime/blob/master/ecolime/solve_demo.ipynb>

## Using the ME Model
This section has yet to be completed.

[^solveME]: Yang, L., Ma, D., Ebrahim, A., Lloyd, C. J., Saunders, M. A., & Palsson, B. O. (2016). [solveME: fast and reliable solution of nonlinear ME models](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1240-1). BMC Bioinformatics, 17(1), 391. doi:10.1186/s12859-016-1240-1
[^qMinos]: Ma, D., Yang, L., Fleming, R.M.T., Thiele, I., Palsson, B.O., Saunders, M.A. (2017). [Reliable and efficient solution of genome-scale models of Metabolism and macromolecular Expression](https://www.nature.com/articles/srep40863). Scientific Reports, 7, 40863. doi:10.1038/srep40863
[^CobraME]: Lloyd CJ, Ebrahim A, Yang L, King ZA, Catoiu E, O’Brien EJ, et al. (2018) [COBRAme: A computational framework for genome-scale models of metabolism and gene expression](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006302). PLoS Comput Biol. 2018;14: e1006302.
[^iJL1678b]: Liu JK, O’Brien EJ, Lerman JA, Zengler K, Palsson BO, Feist AM. [Reconstruction and modeling protein translocation and compartmentalization in Escherichia coli at the genome-scale.](https://www.ncbi.nlm.nih.gov/pubmed/25227965)(2014) BMC Syst Biol. 8: 110.