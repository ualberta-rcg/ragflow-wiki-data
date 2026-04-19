---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:45:32.127953+00:00"

tags:
  []

keywords:
  - "compilateurs"
  - "Langage C"
  - "normes ISO"
  - "concurrence"
  - "mot-clé volatile"

questions:
  - "Quelles sont les principales évolutions apportées par la norme C11 concernant la gestion de la mémoire et de la concurrence ?"
  - "Pourquoi l'utilisation du mot-clé volatile en C est-elle souvent source d'erreurs par rapport à son équivalent en Java ?"
  - "Quels sont les risques potentiels liés aux options d'optimisation des compilateurs GCC et Intel, et quelles solutions sont recommandées pour les éviter ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

Le C est un langage de programmation impératif et généraliste de haut niveau, créé entre 1969 et 1973 aux Bell Labs par Dennis Ritchie. Des normes ISO ont été établies en 1989-1990 (C89 ou C90), en 1999 (C99) et en 2011 (C11). Pour en apprendre davantage sur le langage et l'impact de ces normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), son historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), qui inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), une mise à jour majeure, qui a ajouté le modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'y avait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs.

!!! tip "Recommandation"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! warning "Attention à l'utilisation de `volatile`"
    Le mot-clé `volatile` est souvent employé incorrectement en C parce qu'il est confondu avec le `volatile` de Java qui n'a pas du tout le même sens. Le mot-clé `volatile` en Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

### GCC

!!! warning "Risques liés à l'option d'optimisation -O3"
    L'option `-O3` de GCC comprend des améliorations qui peuvent être dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! tip "Conseils pour l'optimisation GCC"
    En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, consultez la page de manuel (par exemple, `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sûrs.

### Intel

!!! warning "Difficultés potentielles avec les compilateurs Intel"
    Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante.

!!! tip "Respect des normes avec les compilateurs Intel"
    Prenez connaissance des pages de manuel Intel (par exemple, `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).