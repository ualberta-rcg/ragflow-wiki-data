---
title: "Tensorboard/fr"
slug: "tensorboard"
lang: "fr"

source_wiki_title: "Tensorboard/fr"
source_hash: "cf6619ac10a3627e4cee8ec995281f28"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:46:39.018407+00:00"

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

TensorBoard est une suite d'applications web pour inspecter et comprendre vos tâches d'IA et d'apprentissage machine. Elle comprend des outils visuels pour suivre les indicateurs de performance et d'évaluation; profiler le code; explorer les couches intermédiaires des modèles; visualiser les plongements sémantiques; et bien plus encore. Conçue initialement pour TensorFlow (https://www.tensorflow.org/tensorboard/get_started), elle prend également en charge d'autres environnements tels que PyTorch (https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html) et JAX (https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html).

## Avec JupyterHub

Sur les grappes où [JupyterHub](jupyterhub.md) est disponible, vous pouvez lancer TensorBoard en cliquant sur l'icône suivante dans un onglet actif du lanceur.

L'application s'ouvrira alors dans un nouvel onglet de votre navigateur. Allez sur cet onglet pour commencer à utiliser TensorBoard.

Lorsque vous lancez TensorBoard sur JupyterHub, un répertoire *$HOME/tensorboard_logs* est créé. C'est à cet emplacement que TensorBoard recherche les données à afficher dans votre navigateur. Vous devez donc vous assurer que tous les appels à TensorBoard dans votre code écrivent des données dans ce répertoire, autrement aucune donnée ne s'affichera dans l'onglet TensorBoard de votre navigateur. Vous pouvez modifier l'emplacement de ce répertoire en ajoutant *export TENSORBOARD_LOGDIR=/some/other/path* dans votre fichier `.bashrc`.

Pour des exemples d'utilisation de TensorBoard, voir la documentation pour votre outil IA :

* [PyTorch](https://docs.pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
* [TensorFlow](https://www.tensorflow.org/tensorboard/get_started)
* [Jax](https://docs.jaxstack.ai/en/latest/JAX_visualizing_models_metrics.html)