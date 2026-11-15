---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:24:30.798307+00:00"

tags:
  []

keywords:
  - "mot‑clé volatile"
  - "norme ISO C11"
  - "modèle de mémoire et de concurrence"
  - "option de compilation -O2"
  - "option -fp-model precise d'Intel"

questions:
  - "Quelles sont les principales nouveautés apportées par les normes ISO C99 et C11 comparées à C90 ?"
  - "En quoi le mot‑clé <tt>volatile</tt> en C diffère‑t‑il du <tt>volatile</tt> de Java, et quelle construction C doit‑on utiliser pour obtenir un comportement équivalent ?"
  - "Quels problèmes peut‑on rencontrer avec l’option -O3 de GCC et quelles recommandations suivre pour compiler du code C concurrent de façon sûre ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en savoir plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

!!! caution "Avertissement"
    Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

# Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait auparavant aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple concernant les comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs.

!!! tip "Recommandation"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

# Pièges

## Mot-clé `volatile`

Le modificateur `volatile` a une signification très particulière en C et C++, comme vous pourrez le constater en consultant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! warning "Attention"
    `volatile` est souvent employé incorrectement en C, car il est confondu avec le `volatile` de Java, qui n'a pas du tout la même signification. Le mot-clé Java `volatile` correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

## Compilateurs

### GCC

L'option `-O3` inclut des optimisations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! warning "Attention"
    En cas de doute, privilégiez plutôt l'option `-O2`. Si le temps le permet, consultez la page `man` (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres potentiellement dangereux.

### Intel

Les compilateurs C et C++ d'Intel peuvent entraîner des difficultés dans le cas d'opérations avec virgule flottante.

!!! warning "Attention"
    Consultez les pages `man` d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).