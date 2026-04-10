---
title: "Modules/fr"
slug: "modules"
lang: "fr"

source_wiki_title: "Modules/fr"
source_hash: "0ede0f4299d39e073ff792db173d6c54"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:36:57.956730+00:00"

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

En programmation, un module est un logiciel indépendant et interchangeable qui contient tout ce qu'il faut pour fournir une certaine fonctionnalité.

Selon le contexte, le terme *module* peut avoir des sens différents. Nous décrivons ici quelques types de modules et suggérons d'autres références de documentation.

!!! note
    Consulter [*Programmation modulaire* sur Wikipédia](https://fr.wikipedia.org/wiki/Programmation_modulaire).

## Précision

### Modules Lmod

Aussi nommés *modules d'environnement*, les modules Lmod sont utilisés pour modifier votre environnement (*shell*) afin de permettre l'utilisation d'un paquet logiciel ou d'une version d'un logiciel autre que celle offerte par défaut, par exemple pour les compilateurs (voir [Utiliser des modules](utiliser-des-modules.md)).

### Modules Python

Un module Python est un fichier constitué habituellement de code Python qui peut être chargé avec les instructions `import ...` ou `from ... import ...`. Un paquet Python est une collection de modules Python; notez que les termes *paquet* et *module* sont souvent utilisés sans distinction.

!!! note
    Consulter [*What is the difference between a python module and a python package?*](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package).

Certains modules Python tels que Numpy peuvent être importés si vous chargez d'abord le module Lmod `scipy-stack` au niveau du *shell* (voir [Pile logicielle SciPy](python/fr.md#pile-logicielle-scipy)).

Nous offrons une importante collection de [*wheels* Python](python/fr.md#wheels-disponibles) qui sont des modules précompilés compatibles avec nos [environnements logiciels standards](standard-software-environments/fr.md). Avant d'importer des modules d'un *wheel*, vous devez créer un [environnement virtuel](python/fr.md#creer-et-utiliser-un-environnement-virtuel).

Les modules Python qui ne sont ni dans le module Lmod `scipy-stack` ni dans notre collection de *wheels* peuvent être installés à partir de l'internet tel que décrit dans [Installer des paquets](python/fr.md#installer-des-paquets).

## Informations complémentaires

*   Page wiki [Logiciels disponibles](available-software/fr.md)
*   [Environnements logiciels standards](standard-software-environments/fr.md); par défaut, la collection de modules est `StdEnv/2020` (depuis le 1er avril 2021)
*   [Modules Lmod particuliers sur Niagara](modules-specific-to-niagara.md)
*   Modules Lmod optimisés avec [instructions CPU](standard-software-environments/fr.md#amelioration-de-la-performance) pour [AVX](modules-avx.md), **[AVX2](modules-avx2.md)** et **[AVX512](modules-avx512.md)**
*   Page wiki [Catégorie *Software*](category-software.md) : liste des pages de notre site wiki relatives aux logiciels du commerce ou offerts sous licence