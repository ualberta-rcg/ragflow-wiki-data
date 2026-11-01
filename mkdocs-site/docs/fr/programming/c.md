---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:29:48.056519+00:00"

tags:
  []

keywords:
  - "normes ISO C89 C99 C11"
  - "mot‑clé volatile"
  - "langage C"
  - "modèle de mémoire et de concurrence"
  - "compilateurs GCC et Intel"

questions:
  - "Quelles sont les principales nouveautés apportées par les normes ISO C99 et C11 par rapport à C90, notamment en matière de modèle de mémoire et de fonctionnalités de concurrence ?"
  - "Pourquoi le mot‑clé <tt>volatile</tt> en C ne doit‑il pas être confondu avec le <tt>volatile</tt> de Java, et quelle est l’alternative C appropriée pour garantir la visibilité et l’ordre des accès concurrents ?"
  - "Quels sont les pièges liés aux options d’optimisation « ‑O3 » de GCC et aux réglages de précision flottante des compilateurs Intel, et quelles recommandations suivre pour compiler du code C contenant de la concurrence ou des opérations en virgule flottante ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multithread, *atomics*, *compare-and-swap*).

!!! warning "Liens externes"
    Ces liens pourraient contenir des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait au préalable aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple concernant les comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs.

!!! tip "Recommandation"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous pourrez le constater en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'utilisation de ce modificateur est cependant rare et se limite à certains types de code de bas niveau.

!!! warning "Confusion avec Java"
    `volatile` est employé incorrectement en C, car on le confond avec le `volatile` Java qui n'a pas du tout le même sens. Le mot-clé Java `volatile` correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

L'option `-O3` comprend des améliorations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! warning "Optimisations GCC"
    En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, consultez la page de manuel (par exemple `man gcc`) et recherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sécuritaires.

#### Intel

Les compilateurs C et C++ d'Intel peuvent occasionner des difficultés dans le cas d'opérations avec virgule flottante.

!!! warning "Compilateurs Intel et virgule flottante"
    Consultez les pages de manuel Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour des détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).