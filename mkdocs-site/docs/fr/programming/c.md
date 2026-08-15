---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:33:15.238612+00:00"

tags:
  []

keywords:
  - "modificateur volatile"
  - "langage C"
  - "modèle de mémoire et concurrence"
  - "options de compilation GCC -O2"
  - "normes ISO C11"

questions:
  - "Quelles sont les principales normes ISO du langage C et quelles évolutions majeures chacune a‑t‑elle introduites ?"
  - "Pourquoi le mot‑clé <tt>volatile</tt> est‑il souvent mal utilisé en C et quelle est l’alternative appropriée pour la concurrence ?"
  - "Quels conseils le texte donne‑t‑il concernant les options de compilation à privilégier avec GCC et les compilateurs Intel pour éviter des comportements indésirables ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

## C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en savoir plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (*multithread*, *atomiques*, *compare-and-swap*).

!!! attention "Note importante"
    Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'y avait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version ultérieure.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

`volatile` est souvent employé incorrectement en C, car on le confond avec le mot-clé *volatile* de Java qui n'a pas du tout le même sens. Le mot-clé *volatile* de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

L'option `-O3` comprend des optimisations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, privilégiez plutôt l'option `-O2`. Si vous avez le temps, consultez la page de manuel (par exemple `man gcc`) et cherchez `-O3`; vous pouvez ainsi désactiver les options qui ne sont pas sécuritaires.

#### Intel

Les compilateurs C et C++ d'Intel peuvent occasionner des difficultés lors d'opérations en virgule flottante. Consultez les pages de manuel d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` afin de respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).