---
title: "Jupyter/en"
slug: "jupyter"
lang: "en"

source_wiki_title: "Jupyter/en"
source_hash: "5ea1a5e38000d3b97bd772c004706cd8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:15:12.919011+00:00"

tags:
  - software

keywords:
  - "JupyterLab"
  - "JupyterHub"
  - "Kernel"
  - "Jupyter"
  - "Jupyter Notebook"

questions:
  - "What is the difference between the JupyterLab and Jupyter Notebook web portals?"
  - "What roles do JupyterHub and Kernels play in the overall Jupyter architecture?"
  - "How is a Notebook defined in this vocabulary, and what distinguishes an IPython notebook from a regular Python shell?"
  - "What is the difference between the JupyterLab and Jupyter Notebook web portals?"
  - "What roles do JupyterHub and Kernels play in the overall Jupyter architecture?"
  - "How is a Notebook defined in this vocabulary, and what distinguishes an IPython notebook from a regular Python shell?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# The Jupyter vocabulary and related wiki pages
* **Jupyter**: an implementation of Web applications and notebook rendering
  * *Google Colab* would be another implementation of the same kind of environment
* **Jupyter Application**: like a regular application, but is displayed in a separate Web browser tab. The application has access to the data stored remotely on the server, and the heavy computations are also handled by the remote server
* [**JupyterHub**: a Web server hosting Jupyter portals and kernels](jupyterhub.md)

## JupyterLab
A Web portal with a modern interface for managing and running applications, as well as rendering notebook files of various kernels. For more details:
* [**JupyterLab via JupyterHub**: a pre-installed JupyterLab environment](jupyterhub.md#jupyterlab), with a default Python kernel and the access to software modules
* [**JupyterLab from a virtual environment**: a self-made environment](advanced-jupyter-configuration.md) to be launched by a Slurm job

## Jupyter Notebook
An older Web portal for managing and running applications, as well as rendering notebook files of various kernels. For more details:
* [**Jupyter Notebook via JupyterHub**: a pre-installed Jupyter Notebook environment](jupyterhub.md#user-interface), with a default Python kernel and the access to software modules
* [**Jupyter Notebook from a virtual environment**: a self-made environment](jupyter-notebook.md) to be launched by a Slurm job

## Kernel
The active service behind the Web interface. There are:
* Notebook kernels (e.g. Python, R, Julia)
* Application kernels (e.g. RStudio, VSCode)

## Notebook
A page of executable cells of code and formatted text:
* **IPython notebooks**: a notebook executed by a Python kernel, and has some IPython interactive special commands that are not supported by a regular Python shell