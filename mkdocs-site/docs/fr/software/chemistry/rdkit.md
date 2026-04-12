---
title: "RDKit/fr"
slug: "rdkit"
lang: "fr"

source_wiki_title: "RDKit/fr"
source_hash: "46628c417ebe3c00bc01fbf86531f9fd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:58:01.150582+00:00"

tags:
  []

keywords:
  - "RDKit"
  - "environnement virtuel"
  - "chimie computationnelle"
  - "module"
  - "Python"

questions:
  - "Qu'est-ce que RDKit et pour quels types d'applications est-il utilisé ?"
  - "Quelle est la procédure à suivre pour configurer et utiliser RDKit correctement avec un environnement virtuel Python ?"
  - "Quelles sont les solutions recommandées pour résoudre l'erreur \"ModuleNotFoundError: No module named 'rdkit'\" ?"
  - "Qu'est-ce que RDKit et pour quels types d'applications est-il utilisé ?"
  - "Quelle est la procédure à suivre pour configurer et utiliser RDKit correctement avec un environnement virtuel Python ?"
  - "Quelles sont les solutions recommandées pour résoudre l'erreur \"ModuleNotFoundError: No module named 'rdkit'\" ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[RDKit](https://www.rdkit.org/) est un ensemble d'applications pour la chimie computationnelle et l'apprentissage machine qui sont écrites en C++ et en Python.

## Versions disponibles
Les bibliothèques C++ et les interfaces Python sont disponibles via un module.

Pour connaître les versions disponibles, utilisez
```bash
module spider rdkit
```

Pour l'information sur une version particulière, utilisez
```bash
module spider rdkit/X.Y.Z
```
où `X.Y.Z` est la version recherchée, par exemple `2024.03.5`.

## Interfaces (*bindings*) Python
Le module contient des interfaces pour plusieurs versions de Python. Pour connaître les versions disponibles, utilisez
```bash
module spider rdkit/X.Y.Z
```
où `X.Y.Z` est la version que vous voulez.

### Dépendance
Quand un autre wheel dépend de `rdkit`, la dépendance doit être satisfaite.

1.  Désactivez tout environnement virtuel Python.
    ```bash
    test $VIRTUAL_ENV && deactivate
    ```

    !!! note "Remarque"
        Si un environnement virtuel est actif, il est important de le désactiver avant de charger le module. Une fois le module chargé, activez à nouveau votre environnement virtuel.

2.  Chargez le module.
    ```bash
    module load rdkit/2024.03.5 python/3.12
    ```

3.  Vérifiez qu'il est visible par `pip` avec
    ```bash
    pip list | grep rdkit
    ```
    ```text
    rdkit            2024.3.5
    ```
    et que le module Python que vous avez chargé lui a accès, avec
    ```bash
    python -c 'import rdkit'
    ```
    Si aucune erreur ne survient, le problème devrait être réglé.

4.  [Créez un environnement virtuel](../python.md) et installez les paquets.

## Dépannage

### Message *ModuleNotFoundError: No module named 'rdkit'*
Ce message peut survenir si `rdkit` n’est pas disponible.
```text
ModuleNotFoundError: No module named 'rdkit'
```

!!! tip "Solutions possibles"
    *   Vérifiez quelles versions de Python sont compatibles avec le module RDKit chargé avec `module spider rdkit/X.Y.Z`. Une fois qu'un module Python compatible est chargé, vérifiez que `python -c 'import rdkit'` fonctionne.
    *   Chargez le module avant d'activer votre environnement virtuel; voir [Dépendance ci-dessus](#dépendance).

Voir aussi [ModuleNotFoundError: No module named 'X'](../python.md).