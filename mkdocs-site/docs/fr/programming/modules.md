---
title: "Modules/fr"
slug: "modules"
lang: "fr"

source_wiki_title: "Modules/fr"
source_hash: "d671b8cb421087a08c6c93781e4612ee"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:38:47.039199+00:00"

tags:
  []

keywords:
  - "Standard software environments"
  - "module Lmod"
  - "module Python"
  - "environnement virtuel"
  - "wheels Python"

questions:
  - "Quel est le rôle des modules Lmod et comment permettent‑ils de modifier l’environnement shell pour utiliser des versions spécifiques de logiciels ?"
  - "En quoi consiste un module Python, quelle est la différence avec un paquet Python, et comment les « wheels » facilitent‑ils leur utilisation dans les environnements virtuels ?"
  - "Où peut‑on trouver la collection de modules standard (StdEnv/2020) et quelles ressources complémentaires sont proposées pour installer ou optimiser des logiciels sur le système ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

En programmation, un module est un logiciel indépendant et interchangeable qui contient tout ce qu'il faut pour fournir une certaine fonctionnalité.

Selon le contexte, le terme *module* peut avoir un sens différent. Nous décrivons ici quelques types de modules et suggérons d'autres références de documentation.

## Précision

### Modules Lmod

Aussi nommés *modules d'environnement*, les modules Lmod sont employés pour modifier votre environnement (*shell*) pour permettre l'utilisation d'un paquet logiciel ou d'une version d'un logiciel autre que celle offerte par défaut, par exemple pour les compilateurs (voir [Utiliser des modules](utiliser_des_modules.md)).

### Modules Python

Un module Python est un fichier constitué habituellement de code Python qui peut être chargé avec les énoncés `import ...` ou `from ... import ...`. Un paquet Python est une collection de modules Python; notez que les termes *paquet* et *module* sont souvent employés sans distinction.

Certains modules Python tels que Numpy peuvent être importés si vous chargez d'abord le module Lmod `scipy-stack` au niveau du *shell* (voir [Pile logicielle SciPy](../software/python.md)).

Nous offrons une importante collection de [*wheels* Python](../software/python.md) qui sont des modules précompilés compatibles avec nos [environnements logiciels standards](standard_software_environments.md).
Avant d'importer des modules d'un *wheel*, vous devez créer un [environnement virtuel](../software/python.md).

Les modules Python qui ne sont ni dans le module Lmod `scipy-stack` ni dans notre collection de *wheels* peuvent être installés à partir d'internet tel que décrit dans [Installer des paquets](../software/python.md).

## Information complémentaire

*   Page wiki [Logiciels disponibles](available_software.md)
*   [Environnements logiciels standards](standard_software_environments.md); par défaut, la collection de modules est `StdEnv/2020` (depuis le 1er avril 2021)
*   Modules Lmod particuliers sur Niagara
*   Modules Lmod optimisés avec [instructions CPU](standard_software_environments.md) pour AVX, **AVX2** et **AVX512**
*   Page wiki Catégorie *Software* : liste des pages de notre site wiki relatives aux logiciels du commerce ou offerts avec licence

## Références

*   [Voir "Programmation modulaire" sur Wikipédia](https://fr.wikipedia.org/wiki/Programmation_modulaire)
*   ["What is the difference between a python module and a python package?"](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package)