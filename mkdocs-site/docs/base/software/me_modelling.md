---
title: "ME modelling"
slug: "me_modelling"
lang: "base"

source_wiki_title: "ME modelling"
source_hash: "ffcb46c6b5781a65b6baef30b51a1ffd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:44:13.515361+00:00"

tags:
  []

keywords:
  - "solvemepy"
  - "EcoliME"
  - "Python virtual environment"
  - "solveME"
  - "ME-model"
  - "quadMinos"
  - "ME-modelling softwares"
  - "ME-models"
  - "virtual environment"
  - "qMinos solver"
  - "quad precision solver"
  - "CobraME"
  - "Jupyter notebook"
  - "installation steps"

questions:
  - "What are Models of metabolism and expression (ME-models) and how do they generate phenotype predictions?"
  - "What specific roles do the solveME, CobraME, and EcoliME packages play in the ME-modeling framework?"
  - "What are the key dependencies and recommended steps for setting up the ME-modelling installation environment?"
  - "What are the necessary steps and repositories required to install the CobraME and EcoliME packages?"
  - "How do you configure a virtual environment to run the ME-model within a Jupyter notebook?"
  - "Which specific Jupyter notebooks are provided in the ecoliME package to build and solve the iJL1768b E. coli ME-model?"
  - "How can a user download the solvemepy software from GitHub?"
  - "What is quadMinos and from whom can it be obtained for academic use?"
  - "What steps must be taken to install the quadMinos solver after it has been downloaded?"
  - "What are the necessary steps and repositories required to install the CobraME and EcoliME packages?"
  - "How do you configure a virtual environment to run the ME-model within a Jupyter notebook?"
  - "Which specific Jupyter notebooks are provided in the ecoliME package to build and solve the iJL1768b E. coli ME-model?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
Models of metabolism and expression (ME-models) are mathematical knowledgebases that integrate information on both the expression machinery and metabolism of a cell and are capable of generating predictions of phenotype. They are formulated as optimization problems where a bisection method finds the optimum growth rate and proteome allocation. Solving these complex methods hence requires an efficient computing approach that is best obtained in low-level programming languages. The solveME [Yang, L., Ma, D., Ebrahim, A., Lloyd, C. J., Saunders, M. A., & Palsson, B. O. (2016). solveME: fast and reliable solution of nonlinear ME models. BMC Bioinformatics, 17(1), 391. doi:10.1186/s12859-016-1240-1](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1240-1) Python wrapper allows the utilization of fortran efficiency and the qMinos solver [Ma, D., Yang, L., Fleming, R.M.T., Thiele, I., Palsson, B.O., Saunders, M.A. (2017). Reliable and efficient solution of genome-scale models of Metabolism and macromolecular Expression. Scientific Reports, 7, 40863. doi:10.1038/srep40863](https://www.nature.com/articles/srep40863). The CobraME [Lloyd CJ, Ebrahim A, Yang L, King ZA, Catoiu E, O’Brien EJ, et al. (2018) COBRAme: A computational framework for genome-scale models of metabolism and gene expression. PLoS Comput Biol. 2018;14: e1006302.](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006302) package provides useful function to build and solve ME models with the ease of Python. The EcoliME package provides the ability to construct the *i*JL1678b [Liu JK, O’Brien EJ, Lerman JA, Zengler K, Palsson BO, Feist AM. Reconstruction and modeling protein translocation and compartmentalization in Escherichia coli at the genome-scale.(2014) BMC Syst Biol. 8: 110.](https://www.ncbi.nlm.nih.gov/pubmed/25227965) ME-model of *Escherichia coli*.

## Installation
The ME-modelling environment contains many dependencies that are more easily managed by the use of a Python Virtual environment.
We provide the steps to setup a virtual environment in Python2 using the virtualenv software, using conda or venv would also work. More detailed information on how to create a virtual environment can be found [here](https://help.dreamhost.com/hc/en-us/articles/215489338-Installing-and-using-virtualenv-with-Python-2).

### Setup the virtual environment
We suggest creating a folder containing all ME-modelling related packages.
Setup a virtual environment for ME-modelling using virtualenv in Python2.7, on mp2:
```bash
ml python/2.7.14
pip install virtualenv –user
mkdir ME_modelling
cd ME_modelling
virtualenv -p /home/username/opt/python-2.7.15/bin/python ME_env
```
Activate the virtual environment, the virtual environment remains active in all following steps:
```bash
source ME_env/bin/activate
```
Install required dependencies, note that more-itertools==5.0.0 is the last Python2.7 supported version:
```bash
pip install pandas
pip install sympy
pip install more-itertools==5.0.0
```
!!! warning "Important"
    The Python compiler should be GCC > 5.4.0.

Compiling numpy with this version is also necessary:
```bash
pip install git+https://github.com/numpy/numpy@v1.14.0
```
Install cobrapy==0.5.11 within the virtual environment. The required cobrapy==0.5.11 is not available for installation via pip install. This version can be obtained from GitHub:
```bash
git clone https://github.com/opencobra/cobrapy.git
cd cobrapy-0.5.11
python setup.py develop
```

### Install ME-modelling softwares
Get solvemepy from GitHub (https://github.com/SBRG/solvemepy):
```bash
git clone https://github.com/SBRG/solvemepy.git
```
Obtain quadMinos. This quad precision solver can be obtained for academic use from Pr. Michael Saunders at Stanford University. Once downloaded, compile the solver, these installation steps can be found [here](https://github.com/SBRG/solvemepy):
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

## Building and solving a ME-model
Cobrame conveniently contains all scripts and files required to build a complete ME-model for *Escherichia coli* from scratch.

The ME-model can be built from:
1.  A Jupyter notebook
2.  A Python script

### Virtual environment in Jupyter notebook
A Jupyter notebook can be run on an interactive node. The information for installation can be found [here](https://docs.computecanada.ca/wiki/Jupyter).

To build, solve and modify a ME-model in Jupyter, set up the virtual environment previously created to run in Jupyter Lab or Jupyter Notebook. [Click for more information on virtual environment in ipython.](https://anbasile.github.io/programming/2017/06/25/jupyter-venv/) In the **activated** virtual environment:
```bash
pip install ipykernel
ipython kernel install --user --name=ME_env_name
```
The [ecoliME](https://github.com/SBRG/ecolime) package contains a Jupyter notebook to build the *i*JL1768b *E. coli* ME-model:
https://github.com/SBRG/ecolime/blob/master/ecolime/build_me_model.ipynb
and to solve the ME-model:
https://github.com/SBRG/ecolime/blob/master/ecolime/solve_demo.ipynb

## Using the ME model
This section has yet to be completed