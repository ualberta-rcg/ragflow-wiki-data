---
title: "Faiss/fr"
slug: "faiss"
lang: "fr"

source_wiki_title: "Faiss/fr"
source_hash: "a7ad0f4be22ca0862b755ae38847f0f1"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:18:59.073312+00:00"

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

[Faiss](https://github.com/facebookresearch/faiss/wiki) est une bibliothèque efficace pour la recherche de similarités et le regroupement de vecteurs denses. Elle contient des algorithmes qui recherchent dans des ensembles de vecteurs de n'importe quelle taille, même ceux qui sont trop grands pour la mémoire vive. Elle contient également du code pour l'évaluation et le réglage des paramètres. Faiss est écrite en C++ avec des scripts enveloppants complets pour Python (versions 2 et 3). Certains des algorithmes les plus utiles sont implémentés sur GPU. Faiss est développée principalement par [Meta AI Research](https://research.facebook.com/) avec l'aide de contributeurs externes.

## Liaisons Python
Le module contient des liaisons pour plusieurs versions de Python.
Pour connaître les versions disponibles, lancez

```bash
module spider faiss/X.Y.Z
```

ou allez directement à *faiss-cpu* avec

```bash
module spider faiss-cpu/X.Y.Z
```

où `X.Y.Z` désigne la version voulue.

### Utilisation
1. Chargez les modules requis.

```bash
module load StdEnv/2023 gcc cuda faiss/X.Y.Z python/3.11
```

où `X.Y.Z` désigne la version choisie.

2. Importez Faiss.

```bash
python -c "import faiss"
```

Si la commande n'affiche rien, l'importation a réussi.

#### Paquets Python disponibles
Certains paquets Python dépendent des liaisons `faiss-cpu` ou `faiss-gpu` pour être installés.
Le module `faiss` fournit
* `faiss`
* `faiss-gpu`
* `faiss-cpu`

```bash
pip list | fgrep faiss
```
```text
faiss-gpu                          1.7.4
faiss-cpu                          1.7.4
faiss                              1.7.4
```

Avec le module `faiss` chargé, les dépendances des extensions ci-dessus seront satisfaites.