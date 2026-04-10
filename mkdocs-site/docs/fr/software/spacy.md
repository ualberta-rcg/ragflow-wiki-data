---
title: "SpaCy/fr"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

[spaCy](https://spacy.io/) est un paquet Python pour le traitement avancé du langage naturel.

= Installation =

## *Wheels* disponibles

La commande suivante montre le plus récent build de <tt>spaCy</tt>.

```bash
avail_wheels spacy thinc thinc_gpu_ops
```

Voyez [Lister les *wheels* disponibles](python-fr#lister_les_wheels_disponibles.md).

## *Wheels* précompilés

L’option privilégiée est de l’installer avec un [wheel](https://pythonwheels.com/) Python précompilé. 
:1. Chargez le module <tt>python/3.6</tt>
:2. Créez et activez un  [environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md).
:3. Installez <tt>spaCy</tt> dans l’environnement virtuel avec `pip install`. 
:*Pour les CPU et les GPU :
:
```bash
pip install spacy[cuda] --no-index
```

:*Pour les CPU seulement :
:
```bash
pip install spacy --no-index
```

**Version GPU**: Pour utiliser la version GPU, vous devez présentement ajouter les bibliothèques CUDA à la variable <tt>LD_LIBRARY_PATH</tt>:

```bash

```
$CUDA_HOME/lib64:$LD_LIBRARY_PATH
}}

Pour utiliser le script enveloppant (*wrapper*) Pytorch  avec <tt>thinc</tt>, vous devez aussi installer le *wheel* <tt>torch_cpu</tt> ou <tt>torch_gpu</tt>.