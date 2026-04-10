---
title: "Comet.ml/fr"
slug: "comet_ml"
lang: "fr"

source_wiki_title: "Comet.ml/fr"
source_hash: "6894193ca5851ef545b97a1b6b66205b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:44:09.742501+00:00"

tags:
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

[Comet](https://comet.ml) est une plateforme de méta-apprentissage machine qui permet de construire des modèles pour des applications concrètes et d’en faciliter le développement et la maintenance. La plateforme permet de suivre, comparer, décrire et reproduire les expériences, et accélère grandement la recherche d’hyperparamètres grâce à son [module d’exploration bayésienne](https://www.comet.ml/parameter-optimization).

## Utilisation sur nos grappes

### Disponibilité

Puisqu’une connexion internet est requise, l’utilisation de Comet est restreinte à certaines grappes.

| Grappe | Wandb disponible | Commentaire |
|:---|:---|:---|
| Narval | oui ✅ | `module load httpproxy` requis |
| Rorqual | oui ✅ | `module load httpproxy` requis |
| TamIA | oui ✅ | `module load httpproxy` requis |
| Fir | oui ✅ | `httpproxy` non requis |
| Nibi | oui ✅ | `httpproxy` non requis |
| Trillium | non ❌ | accès internet désactivé sur les nœuds de calcul |
| Vulcan | oui ✅ | `httpproxy` non requis |
| Killarney | oui ✅ | `httpproxy` non requis |

### Meilleures pratiques

!!! attention "Bonne pratique"
    Évitez de faire des requêtes au serveur de Comet à trop haute fréquence, car Comet pourrait limiter le débit et rendre imprévisible la durée de la tâche. Interagissez avec Comet à des intervalles d'au moins 1 minute.