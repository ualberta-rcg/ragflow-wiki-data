---
title: "Jupyter/fr"
tags:
  - software

keywords:
  []
---

= Vocabulaire Jupyter et pages wiki reliées =
* **Jupyter** : une implémentation d'applications Web et d’interfaces interactives de notebooks.
** *Google Colab* serait une autre implémentation du même type d'environnement.
* **Application Jupyter** : semblable à toute autre application, mais est affichée dans un onglet Web distinct. L'application peut accéder aux données stockées à distance sur le serveur; les calculs intensifs sont pris en charge par le serveur distant.
* [**JupyterHub** : un serveur Web hébergeant des portails et noyaux (*kernels*) Jupyter](jupyterhub-fr.md).

## JupyterLab 
Portail Web avec interface moderne pour la gestion et l'exécution d'applications et la création de fichiers Notebook avec des noyaux (*kernels*) variés. Pour plus d'information, voyez&nbsp;:
* [**JupyterLab via JupyterHub**, un environnement JupyterLab préinstallé](jupyterhub-fr#jupyterlab.md) avec un noyau Python par défaut et accès aux modules logiciels;
* ['''JupyterLab à partir d'un environnement virtuel''':  environnement personnalisé](advanced-jupyter-configuration-fr.md) qui est lancé par une tâche Slurm.

## Jupyter Notebook 
Portail Web moins récent pour la gestion et l'exécution d'applications et la création de fichiers Notebook avec des noyaux (*kernels*) variés. Pour plus d'information, voyez&nbsp;:
* [**Jupyter Notebook via JupyterHub**, un environnement Jupyter Notebook préinstallé](jupyterhub-fr#interface_utilisateur.md) avec un noyau Python par défaut et accès aux modules logiciels;
* ['''Jupyter Notebook à partir d'un environnement virtuel'*: un environnement personnalisé](jupyternotebook-fr.md) qui est lancé par une tâche Slurm.

## Noyau (*kernel'') 
Service actif derrière l'interface Web&nbsp;:
* Noyaux Notebook (par exemple Python, R, Julia)
* Noyaux d'application (par exemple RStudio, VSCode)

## Notebook 
Une page de cellules exécutables contenant du code et du texte formaté&nbsp;:
* **Notebook IPython **: un notebook exécuté par un noyau (*kernel*) Python et qui dispose de commandes interactives IPython particulières qui ne sont pas prises en charge par un interpréteur Python régulier.