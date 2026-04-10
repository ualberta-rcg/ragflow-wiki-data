---
title: "SpaCy/fr"
slug: "spacy"
lang: "fr"

source_wiki_title: "SpaCy/fr"
source_hash: "4789de82c592d3e38e002c6b903c967f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:22:59.921474+00:00"

tags:
  - software
  - ai-and-machine-learning

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

[spaCy](https://spacy.io/) est un paquet Python pour le traitement avancé du langage naturel.

## Installation

### Roues disponibles

La commande suivante affiche la version la plus récente de `spaCy`.

```bash
avail_wheels spacy thinc thinc_gpu_ops
```

Voyez [Lister les roues disponibles](python/lister-les-wheels-disponibles.md).

### Roues précompilées

L'option privilégiée est de l'installer avec une [roue Python](https://pythonwheels.com/) précompilée.

1.  Chargez le module `python/3.6`.
2.  Créez et activez un [environnement virtuel](python/creer-et-utiliser-un-environnement-virtuel.md).
3.  Installez `spaCy` dans l'environnement virtuel à l'aide de `pip install`.
    *   Pour les unités centrales de traitement (UC) et les unités de traitement graphique (UG) :
        ```bash
        (venv) [name@server ~]$ pip install spacy[cuda] --no-index
        ```
    *   Pour les unités centrales de traitement (UC) seulement :
        ```bash
        (venv) [name@server ~]$ pip install spacy --no-index
        ```

**Version pour UG :** Pour utiliser la version pour UG, vous devez actuellement ajouter les bibliothèques CUDA à la variable `LD_LIBRARY_PATH` :

```bash
(venv) [name@server ~]$ module load gcc/5.4.0 cuda/9
(venv) [name@server ~]$ export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```

Pour utiliser le script d'emballage (`wrapper`) Pytorch avec `thinc`, vous devez aussi installer la roue `torch_cpu` ou `torch_gpu`.