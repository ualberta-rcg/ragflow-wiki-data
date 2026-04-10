---
title: "FastTree/fr"
slug: "fasttree"
lang: "fr"

source_wiki_title: "FastTree/fr"
source_hash: "a57d35d60006d4d59078e403d9968b55"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:19:28.759346+00:00"

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

[FastTree](https://morgannprice.github.io/fasttree/) déduit des arbres phylogénétiques de vraisemblance maximale à partir d'alignements de séquences de nucléotides ou de protéines. FastTree peut gérer des alignements comportant jusqu'à un million de séquences dans un laps de temps et avec une consommation de mémoire raisonnables.

## Modules d'environnement

Nous offrons des modules pour des calculs en simple précision et en double précision. Les calculs en simple précision sont plus rapides, mais ceux en double précision sont plus précis. La double précision est recommandée lorsque vous utilisez une matrice de transition fortement biaisée ou si vous souhaitez résoudre avec précision des branches très courtes.

Pour connaître la disponibilité des modules :

```bash
module spider fasttree
```

Pour charger un module simple précision :

```bash
module load fasttree/2.1.11
```

Pour charger un module double précision :

```bash
module load fasttree-double/2.1.11
```

## Dépannage

!!! warning "Message d'erreur :"
    Le message *WARNING! This alignment consists of closely-related and very long sequences* indique généralement des branches très courtes, parfois même de longueur négative.

## Références

*   [Page web de FastTree](https://morgannprice.github.io/fasttree/)