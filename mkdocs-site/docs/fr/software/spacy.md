---
title: "SpaCy/fr"
slug: "spacy"
lang: "fr"

source_wiki_title: "SpaCy/fr"
source_hash: "4789de82c592d3e38e002c6b903c967f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:33:22.768690+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "traitement du langage naturel"
  - "environnement virtuel"
  - "spaCy"
  - "Python"
  - "installation"

questions:
  - "Qu'est-ce que le paquet Python spaCy et quelle est sa fonction principale ?"
  - "Quelles sont les étapes à suivre pour installer spaCy à l'aide de \"wheels\" précompilés dans un environnement virtuel ?"
  - "Quelles configurations supplémentaires sont requises pour utiliser la version GPU de spaCy et son script enveloppant Pytorch ?"
  - "Qu'est-ce que le paquet Python spaCy et quelle est sa fonction principale ?"
  - "Quelles sont les étapes à suivre pour installer spaCy à l'aide de \"wheels\" précompilés dans un environnement virtuel ?"
  - "Quelles configurations supplémentaires sont requises pour utiliser la version GPU de spaCy et son script enveloppant Pytorch ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[spaCy](https://spacy.io/) est un paquet Python pour le traitement avancé du langage naturel.

## Installation

### *Wheels* disponibles

La commande suivante montre le plus récent build de `spaCy`.

```bash
avail_wheels spacy thinc thinc_gpu_ops
```

Voyez [Lister les *wheels* disponibles](python/lister-les-wheels-disponibles.md).

### *Wheels* précompilés

L’option privilégiée est de l’installer avec un [wheel](https://pythonwheels.com/) Python précompilé.

1.  Chargez le module `python/3.6`.
2.  Créez et activez un [environnement virtuel](python/creer-et-utiliser-un-environnement-virtuel.md).
3.  Installez `spaCy` dans l’environnement virtuel avec `pip install`.
    *   Pour les CPU et les GPU :
        ```bash
        pip install spacy[cuda] --no-index
        ```
    *   Pour les CPU seulement :
        ```bash
        pip install spacy --no-index
        ```

!!! tip "Version GPU"
    Pour utiliser la version GPU, vous devez présentement ajouter les bibliothèques CUDA à la variable `LD_LIBRARY_PATH` :

    ```bash
    module load gcc/5.4.0 cuda/9
    export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
    ```

Pour utiliser le script enveloppant (*wrapper*) Pytorch avec `thinc`, vous devez aussi installer le *wheel* `torch_cpu` ou `torch_gpu`.