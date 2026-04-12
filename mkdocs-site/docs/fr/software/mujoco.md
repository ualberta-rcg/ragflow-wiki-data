---
title: "MuJoCo/fr"
slug: "mujoco"
lang: "fr"

source_wiki_title: "MuJoCo/fr"
source_hash: "93ded354a4821a1119275f416b74c40b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:33:45.114677+00:00"

tags:
  - software

keywords:
  - "MuJoCo"
  - "apprentissage par renforcement"
  - "moteur physique"
  - "interfaces Python"
  - "robotique"

questions:
  - "Qu'est-ce que le moteur logiciel MuJoCo et pour quels domaines de recherche a-t-il été conçu ?"
  - "Comment MuJoCo est-il utilisé dans le contexte de l'apprentissage par renforcement ?"
  - "Quelles sont les commandes à exécuter pour charger les modules MuJoCo et vérifier que l'importation en Python fonctionne correctement ?"
  - "Qu'est-ce que le moteur logiciel MuJoCo et pour quels domaines de recherche a-t-il été conçu ?"
  - "Comment MuJoCo est-il utilisé dans le contexte de l'apprentissage par renforcement ?"
  - "Quelles sont les commandes à exécuter pour charger les modules MuJoCo et vérifier que l'importation en Python fonctionne correctement ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[MuJoCo](https://docs.computecanada.ca/wiki/MuJoCo) (pour **Mu**lti-**Jo**int dynamics with **Co**ntact) est un moteur logiciel spécialisé en physique dont le but est de faciliter la recherche et le développement en robotique, biomécanique, graphisme et animation ainsi que d'autres domaines nécessitant des simulations rapides et précises.

On l'utilise souvent avec les interfaces Python `mujoco_py` comme environnement pour la recherche en apprentissage par renforcement (*RL* pour *reinforced learning*).

Le module `MuJoCo` contient la bibliothèque C/C++ et les interfaces Python.

## Bibliothèque
Pour avoir accès aux fichiers d'en-tête et aux binaires, chargez le module avec

```bash
module load mujoco
```

## Interfaces Python
Pour connaître les versions de Python compatibles, lancez

```bash
module spider mujoco/2.2.2
```

1.  Chargez les modules avec
    ```bash
    module load mujoco python
    ```
2.  Importez MuJoCo avec
    ```bash
    python -c "import mujoco"
    ```

!!! note "Vérification de l'importation"
    L'importation est réussie si rien n'est affiché.