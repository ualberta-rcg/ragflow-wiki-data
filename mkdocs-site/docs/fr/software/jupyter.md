---
title: "Jupyter/fr"
slug: "jupyter"
lang: "fr"

source_wiki_title: "Jupyter/fr"
source_hash: "74585a28f8cac50e3e405ce2692c7f02"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:37:14.307966+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Vocabulaire Jupyter et pages wiki reliées
*   **Jupyter** : une implémentation d'applications Web et d’interfaces interactives de *notebooks*.
    *   *Google Colab* serait une autre implémentation du même type d'environnement.
*   **Application Jupyter** : semblable à toute autre application, mais est affichée dans un onglet Web distinct. L'application peut accéder aux données stockées à distance sur le serveur; les calculs intensifs sont pris en charge par le serveur distant.
*   [**JupyterHub** : un serveur Web hébergeant des portails et *noyaux* (kernels) Jupyter](jupyterhub.md).

## JupyterLab
Portail Web avec interface moderne pour la gestion et l'exécution d'applications et la création de fichiers *Notebook* avec des *noyaux* (kernels) variés. Pour plus d'information, voyez :
*   [**JupyterLab via JupyterHub**, un environnement JupyterLab préinstallé](jupyterhub.md#jupyterlab) avec un *noyau* Python par défaut et accès aux modules logiciels;
*   [**JupyterLab à partir d'un environnement virtuel** : environnement personnalisé](advanced-jupyter-configuration.md) qui est lancé par une tâche Slurm.

## Jupyter Notebook
Portail Web moins récent pour la gestion et l'exécution d'applications et la création de fichiers *Notebook* avec des *noyaux* (kernels) variés. Pour plus d'information, voyez :
*   [**Jupyter Notebook via JupyterHub**, un environnement Jupyter Notebook préinstallé](jupyterhub.md#interface-utilisateur) avec un *noyau* Python par défaut et accès aux modules logiciels;
*   [**Jupyter Notebook à partir d'un environnement virtuel** : un environnement personnalisé](jupyter-notebook.md) qui est lancé par une tâche Slurm.

## Noyau (kernel)
Service actif derrière l'interface Web :
*   Noyaux *Notebook* (par exemple Python, R, Julia)
*   Noyaux d'application (par exemple RStudio, VSCode)

## Notebook
Une page de cellules exécutables contenant du code et du texte formaté :
*   **Notebook IPython** : un *notebook* exécuté par un *noyau* (kernel) Python et qui dispose de commandes interactives IPython particulières qui ne sont pas prises en charge par un interpréteur Python régulier.