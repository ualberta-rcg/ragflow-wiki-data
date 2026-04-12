---
title: "Modules/fr"
slug: "modules"
lang: "fr"

source_wiki_title: "Modules/fr"
source_hash: "0ede0f4299d39e073ff792db173d6c54"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:10:12.749730+00:00"

tags:
  []

keywords:
  - "programmation"
  - "modules Lmod"
  - "environnement logiciel"
  - "module"
  - "modules Python"

questions:
  - "Quelle est la définition générale d'un module en programmation selon le texte ?"
  - "À quoi servent spécifiquement les modules Lmod (ou modules d'environnement) ?"
  - "Quelles sont les différentes méthodes et prérequis pour utiliser ou installer des modules Python (tels que la pile SciPy, les \"wheels\" et les environnements virtuels) ?"
  - "Quelle est la définition générale d'un module en programmation selon le texte ?"
  - "À quoi servent spécifiquement les modules Lmod (ou modules d'environnement) ?"
  - "Quelles sont les différentes méthodes et prérequis pour utiliser ou installer des modules Python (tels que la pile SciPy, les \"wheels\" et les environnements virtuels) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

En programmation, un module est un logiciel indépendant et interchangeable qui contient tout ce qu'il faut pour fournir une certaine fonctionnalité.

Voir la page [Programmation modulaire sur Wikipédia](https://fr.wikipedia.org/wiki/Programmation_modulaire).
Selon le contexte, le terme *module* peut avoir sens différent. Nous décrivons ici quelques types de modules et suggérons d'autres références de documentation.

## Précision

### Modules Lmod

Aussi nommés *modules d'environnement*, les modules Lmod sont employés pour modifier votre environnement (*shell*) pour permettre l'utilisation d'un paquet logiciel ou d'une version d'un logiciel autre que celle offerte par défaut, par exemple pour les compilateurs (voir [Utiliser des modules](utiliser_des_modules.md)).

### Modules Python

Un module Python est un fichier constitué habituellement de code Python qui peut être chargé avec les énoncés `import ...` ou `from ... import ...`. Un paquet Python est une collection de modules Python; notez que les termes *paquet* et *module* sont souvent employés sans distinction. Voir [What is the difference between a python module and a python package?](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package).

Certains modules Python tels que Numpy peuvent être importés si vous chargez d'abord le module Lmod `scipy-stack` au niveau du *shell* (voir Pile logicielle SciPy).

Nous offrons une importante collection de *wheels* Python qui sont des modules précompilés compatibles avec nos environnements logiciels standards. Avant d'importer des modules d'un *wheel*, vous devez créer un environnement virtuel.

Les modules Python qui ne sont ni dans le module Lmod `scipy-stack` ni dans notre collection de *wheels* peuvent être installés à partir de l'internet tel que décrit dans Installer des paquets.

## Information complémentaire

*   Page wiki Logiciels disponibles
*   Environnements logiciels standards; par défaut, la collection de modules est `StdEnv/2020` (depuis le 1er avril 2021)
*   Modules Lmod particuliers sur Niagara
*   Modules Lmod optimisés avec instructions CPU pour AVX, **AVX2** et **AVX512**
*   Page wiki la catégorie *Logiciels* : liste des pages de notre site wiki relatives aux logiciels du commerce ou offerts avec licence

## Références