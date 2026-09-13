---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:19:08.464263+00:00"

tags:
  []

keywords:
  - "norme ISO C11"
  - "option -O3"
  - "mot‑clé volatile"
  - "option -fp-model precise"
  - "modèle de mémoire et de concurrence"

questions:
  - "Quelles sont les principales nouveautés apportées par les normes ISO C99 et C11 comparées à C90 ?"
  - "En quoi le mot‑clé <tt>volatile</tt> en C diffère‑t‑il de son homologue en Java, et quelles sont les conséquences d’une mauvaise utilisation ?"
  - "Quels problèmes peuvent survenir avec l’option d’optimisation -O3 de GCC et les modèles de virgule flottante d’Intel, et quelles alternatives sont conseillées ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## C

C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, voyez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent conduire à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait au préalable aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs.

!!! tip "Compilation de code C concurrent"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version plus récente.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! warning "Confusion autour du mot-clé `volatile`"
    Le mot-clé `volatile` est souvent employé incorrectement en C, car il est confondu avec son homologue en Java, qui n'a pas du tout le même sens. Le mot-clé Java `volatile` correspond en C aux types `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

!!! warning "Optimisations `-O3` avec GCC"
    L'option `-O3` comprend des améliorations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, consultez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

!!! warning "Problèmes de virgule flottante avec les compilateurs Intel"
    Les compilateurs C et C++ d'Intel risquent de causer des difficultés lors d'opérations avec virgule flottante. Prenez connaissance des pages man Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` afin de respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).