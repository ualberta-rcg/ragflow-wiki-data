---
title: "Modules/fr"
tags:
  []

keywords:
  []
---

En programmation, un module est un logiciel indépendant et interchangeable qui contient tout ce qu'il faut pour fournir une certaine fonctionnalité.

<ref> Voir [*Programmation modulaire* sur Wikipédia](https://fr.wikipedia.org/wiki/Programmation_modulaire).</ref>
Selon le contexte, le terme *module* peut avoir sens différent. Nous décrivons ici quelques types de modules et suggérons d'autres références de documentation. 

## Précision 

### Modules Lmod 

Aussi nommés ''modules d'environnement*, les modules Lmod sont employés pour modifier votre environnement (*shell'') pour permettre l'utilisation d'un paquet logiciel ou d'une version d'un logiciel autre que celle offerte par défaut, par exemple pour les compilateurs (voir [Utiliser des modules](utiliser-des-modules.md)).

### Modules Python 

Un module Python est un fichier constitué habituellement de code Python qui peut être chargé avec les énoncés `import ...` ou `from ... import ...`. Un paquet Python est une collection de modules Python; notez que les termes *paquet* et *module* sont souvent employés sans distinction. <ref>Voir [*What is the difference between a python module and a python package?*](https://www.tutorialspoint.com/What-is-the-difference-between-a-python-module-and-a-python-package,)</ref>

Certains modules Python tels que Numpy peuvent être importés si vous chargez d'abord le module Lmod `scipy-stack` au niveau du *shell* 
(voir [Pile logicielle SpiCy](python-fr#pile_logicielle_scipy.md)).

Nous offrons une importante collection de [*wheels* Python](python-fr#wheels_disponibles.md)
qui sont des des modules précompilés compatibles avec nos [environnements logiciels standards](standard-software-environments-fr.md).
Avant d'importer des modules d'un *wheel*, vous devez créer un [environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md).  

Les modules Python qui ne sont ni dans le module Lmod `scipy-stack` ni dans notre collection de *wheels* peuvent être installés à partir de l'internet tel que décrit dans [Installer des paquets](python#frinstaller_des_paquets.md).

## Information complémentaire 

*Page wiki [Logiciels disponibles](available-software-fr.md)
*[Environnements logiciels standards](standard-software-environments-fr.md); par défaut, la collection de modules est `StdEnv/2020` (depuis le 1er avril 2021)
*[Modules Lmod particuliers sur Niagara](modules-specific-to-niagara.md)
*Modules Lmod optimisés avec [instructions CPU](standard_software_environments-fr#amélioration-de_la_performance.md) pour [AVX](modules-avx.md), **[AVX2](modules-avx2.md)** and **[AVX512](modules-avx512.md)** 
* Page wiki [Category *Software*](:category:software.md) : liste des pages de notre site wiki relatives aux logiciels du commerce ou offerts avec licence

## Références