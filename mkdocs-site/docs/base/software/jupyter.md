---
title: "Jupyter"
slug: "jupyter"
lang: "base"

source_wiki_title: "Jupyter"
source_hash: "6f1ad68c4ac7fba5b3c12ab813f97e16"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:15:02.641752+00:00"

tags:
  - software

keywords:
  - "JupyterLab"
  - "JupyterHub"
  - "Kernel"
  - "Jupyter"
  - "Jupyter Notebook"

questions:
  - "What is the difference between JupyterLab and Jupyter Notebook in terms of their interfaces?"
  - "How does a Jupyter Application handle data access and heavy computations?"
  - "What is the role of a Kernel in the Jupyter ecosystem, and what are the two main types mentioned?"
  - "What is the difference between JupyterLab and Jupyter Notebook in terms of their interfaces?"
  - "How does a Jupyter Application handle data access and heavy computations?"
  - "What is the role of a Kernel in the Jupyter ecosystem, and what are the two main types mentioned?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# The Jupyter vocabulary and related wiki pages
*   **Jupyter**: an implementation of Web applications and notebook rendering
    *   *Google Colab* would be another implementation of the same kind of environment
*   **Jupyter Application**: like a regular application, but is displayed in a separate Web browser tab. The application has access to the data stored remotely on the server, and the heavy computations are also handled by the remote server
*   [**JupyterHub**: a Web server hosting Jupyter portals and kernels](../interactive/jupyterhub.md)

## JupyterLab
A Web portal with a modern interface for managing and running applications, as well as rendering notebook files of various kernels. For more details:
*   [**JupyterLab via JupyterHub**: a pre-installed JupyterLab environment](../interactive/jupyterhub.md#jupyterlab), with a default Python kernel and the access to software modules
*   [**JupyterLab from a virtual environment**: a self-made environment](../getting-started/advanced_jupyter_configuration.md) to be launched by a Slurm job

## Jupyter Notebook
An older Web portal for managing and running applications, as well as rendering notebook files of various kernels. For more details:
*   [**Jupyter Notebook via JupyterHub**: a pre-installed Jupyter Notebook environment](../interactive/jupyterhub.md#user-interface), with a default Python kernel and the access to software modules
*   [**Jupyter Notebook from a virtual environment**: a self-made environment](../interactive/jupyternotebook.md) to be launched by a Slurm job

## Kernel
The active service behind the Web interface. There are:
*   Notebook kernels (e.g. Python, R, Julia)
*   Application kernels (e.g. RStudio, VSCode)

## Notebook
A page of executable cells of code and formatted text:
*   **IPython notebooks**: a notebook executed by a Python kernel, and has some IPython interactive special commands that are not supported by a regular Python shell