---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:52:00.225098+00:00"

tags:
  []

keywords:
  - "langage C"
  - "normes ISO C89 C99 C11"
  - "modèle de mémoire et concurrence"
  - "compilateurs GCC et Intel"
  - "mot‑clé volatile"

questions:
  - "Quelles sont les principales différences entre les normes ISO C90, C99 et C11, notamment en ce qui concerne la gestion de la concurrence et le modèle de mémoire ?"
  - "Pourquoi le mot‑clé <tt>volatile</tt> est‑il souvent mal interprété en C, et quel est son équivalent fonctionnel dans le langage Java ?"
  - "Quels problèmes peuvent survenir avec l’option d’optimisation -O3 de GCC et les modèles de virgule flottante d’Intel, et quelles alternatives sont conseillées pour garantir la conformité aux normes ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre davantage sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

# Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait au préalable aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version plus récente.

# Pièges

## Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

`volatile` est employé incorrectement en C, car on le confond avec le `volatile` de Java qui n'a pas du tout le même sens. Le mot-clé `volatile` de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

## Compilateurs

### GCC

!!! warning "Option -O3 de GCC"
    L'option `-O3` de GCC comprend des améliorations qui peuvent s'avérer dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! tip "Utilisation sécuritaire de GCC"
    En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, lisez la page de manuel (`man`) (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sécuritaires.

### Intel

Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante.

!!! tip "Options recommandées pour les compilateurs Intel"
    Consultez les pages de manuel (`man`) d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).