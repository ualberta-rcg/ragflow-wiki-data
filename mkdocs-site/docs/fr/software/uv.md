---
title: "Uv/fr"
slug: "uv"
lang: "fr"

source_wiki_title: "Uv/fr"
source_hash: "f029d12bf49735febb24e52444e6b0c2"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:30:06.804867+00:00"

tags:
  []

keywords:
  - "uv"
  - "grappes"
  - "pip"
  - "gestionnaire de paquets Python"
  - "cache"

questions:
  - "Quels sont les principaux problèmes que l'on risque de rencontrer en utilisant le gestionnaire uv sur les grappes ?"
  - "Quelle est la méthode recommandée pour installer des paquets Python sur les grappes ?"
  - "Comment peut-on vider la cache de uv et empêcher son utilisation future ?"
  - "Quels sont les principaux problèmes que l'on risque de rencontrer en utilisant le gestionnaire uv sur les grappes ?"
  - "Quelle est la méthode recommandée pour installer des paquets Python sur les grappes ?"
  - "Comment peut-on vider la cache de uv et empêcher son utilisation future ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! attention "Aucun soutien technique"
    Il n'y a présentement aucun soutien technique pour `uv` sur nos grappes.

`uv` est un gestionnaire de paquets et de projets Python extrêmement rapide, écrit en Rust. Son utilisation pourrait fonctionner, mais vous risquez de rencontrer des problèmes.

Voici quelques difficultés que vous pourriez rencontrer :
*   certains paquets sont distribués dans un format incompatible avec nos grappes, mais `uv` tente quand même de les installer;
*   `uv` est incapable de trouver les paquets Python fournis par les modules chargés;
*   `uv` peut rapidement saturer le quota de votre répertoire `/home`, car il stocke un très grand nombre de fichiers dans la cache.

## Installation de paquets Python
Pour installer des paquets sur nos grappes, utilisez `pip`; voir [Python](python.md).

Assurez-vous d'avoir au moins la version `pip>=25.0`.
```bash
pip install --no-index --upgrade pip
```

## Dépannage

### Vider la cache
Pour vider la cache, la commande est
```bash
uv cache clean
```
Par la suite, pour ne pas utiliser la cache, la commande est `uv --no-cache`.