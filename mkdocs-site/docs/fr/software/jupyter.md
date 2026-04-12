---
title: "Jupyter/fr"
slug: "jupyter"
lang: "fr"

source_wiki_title: "Jupyter/fr"
source_hash: "74585a28f8cac50e3e405ce2692c7f02"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:15:26.760780+00:00"

tags:
  - software

keywords:
  - "JupyterLab"
  - "Noyau"
  - "JupyterHub"
  - "Jupyter"
  - "Jupyter Notebook"

questions:
  - "Quelle est la différence principale entre les portails Web JupyterLab et Jupyter Notebook ?"
  - "Quel est le rôle d'un noyau (kernel) dans l'environnement Jupyter et quels sont des exemples de noyaux pris en charge ?"
  - "Qu'est-ce que JupyterHub et comment permet-il de gérer les applications et les calculs intensifs sur un serveur distant ?"
  - "Quelle est la différence principale entre les portails Web JupyterLab et Jupyter Notebook ?"
  - "Quel est le rôle d'un noyau (kernel) dans l'environnement Jupyter et quels sont des exemples de noyaux pris en charge ?"
  - "Qu'est-ce que JupyterHub et comment permet-il de gérer les applications et les calculs intensifs sur un serveur distant ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Vocabulaire Jupyter et pages wiki reliées
*   **Jupyter** : une implémentation d'applications Web et d’interfaces interactives de notebooks.
    *   *Google Colab* serait une autre implémentation du même type d'environnement.
*   **Application Jupyter** : semblable à toute autre application, mais est affichée dans un onglet Web distinct. L'application peut accéder aux données stockées à distance sur le serveur; les calculs intensifs sont pris en charge par le serveur distant.
*   [**JupyterHub** : un serveur Web hébergeant des portails et noyaux (*kernels*) Jupyter](../interactive/jupyterhub.md).

## JupyterLab
Portail Web avec interface moderne pour la gestion et l'exécution d'applications et la création de fichiers Notebook avec des noyaux (*kernels*) variés. Pour plus d'information, voyez :
*   [**JupyterLab via JupyterHub**, un environnement JupyterLab préinstallé](../interactive/jupyterhub.md#jupyterlab) avec un noyau Python par défaut et accès aux modules logiciels;
*   [**JupyterLab à partir d'un environnement virtuel** : environnement personnalisé](../getting-started/advanced_jupyter_configuration.md) qui est lancé par une tâche Slurm.

## Jupyter Notebook
Portail Web moins récent pour la gestion et l'exécution d'applications et la création de fichiers Notebook avec des noyaux (*kernels*) variés. Pour plus d'information, voyez :
*   [**Jupyter Notebook via JupyterHub**, un environnement Jupyter Notebook préinstallé](../interactive/jupyterhub.md#interface-utilisateur) avec un noyau Python par défaut et accès aux modules logiciels;
*   [**Jupyter Notebook à partir d'un environnement virtuel** : un environnement personnalisé](../interactive/jupyternotebook.md) qui est lancé par une tâche Slurm.

## Noyau (*kernel*)
Service actif derrière l'interface Web :
*   Noyaux Notebook (par exemple Python, R, Julia)
*   Noyaux d'application (par exemple RStudio, VSCode)

## Notebook
Une page de cellules exécutables contenant du code et du texte formaté :
*   **Notebook IPython** : un notebook exécuté par un noyau (*kernel*) Python et qui dispose de commandes interactives IPython particulières qui ne sont pas prises en charge par un interpréteur Python régulier.