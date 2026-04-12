---
title: "FastTree/fr"
slug: "fasttree"
lang: "fr"

source_wiki_title: "FastTree/fr"
source_hash: "a57d35d60006d4d59078e403d9968b55"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:02:59.005672+00:00"

tags:
  []

keywords:
  - "modules d'environnement"
  - "vraisemblance maximale"
  - "FastTree"
  - "arbres phylogénétiques"
  - "alignements de séquences"

questions:
  - "À quoi sert le logiciel FastTree et quelle est sa capacité maximale de traitement de séquences ?"
  - "Dans quels cas est-il recommandé d'utiliser le module en double précision plutôt que celui en simple précision ?"
  - "Quelle est la conséquence habituelle du message d'avertissement concernant des séquences très longues et étroitement liées ?"
  - "À quoi sert le logiciel FastTree et quelle est sa capacité maximale de traitement de séquences ?"
  - "Dans quels cas est-il recommandé d'utiliser le module en double précision plutôt que celui en simple précision ?"
  - "Quelle est la conséquence habituelle du message d'avertissement concernant des séquences très longues et étroitement liées ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[FastTree](https://morgannprice.github.io/fasttree/) déduit des arbres phylogénétiques de vraisemblance maximale à partir d'alignements de séquences de nucléotides ou de protéines. FastTree peut gérer des alignements comportant jusqu'à un million de séquences dans un laps de temps et avec une consommation de mémoire raisonnables.

## Modules d'environnement

Nous offrons des modules pour des calculs en simple précision et en double précision. Les calculs en simple précision sont plus rapides, mais ceux en double précision sont plus précis.

!!! tip "Quand utiliser la double précision"
    La double précision est recommandée lorsque vous utilisez une matrice de transition fortement biaisée ou si vous souhaitez résoudre avec précision des branches très courtes.

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

!!! warning "Message d'avertissement : *WARNING! This alignment consists of closely-related and very long sequences*"
    Ce message indique que l'alignement est composé de séquences très longues et étroitement liées. Cela conduit généralement à des branches très courtes, parfois même de longueur négative.

## Références

*   [Page web pour FastTree](https://morgannprice.github.io/fasttree/)