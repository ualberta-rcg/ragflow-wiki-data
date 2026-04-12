---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:54:08.966980+00:00"

tags:
  []

keywords:
  - "compilateurs"
  - "mot-clé volatile"
  - "langage C"
  - "concurrence"
  - "normes ISO"

questions:
  - "Quelles sont les principales normes ISO qui ont fait évoluer le langage C depuis sa création par Dennis Ritchie ?"
  - "Pourquoi est-il fortement recommandé d'utiliser la norme C11 ou supérieure pour la gestion de la mémoire et de la concurrence ?"
  - "Quels sont les pièges à éviter concernant l'utilisation du mot-clé \"volatile\" et les options d'optimisation des compilateurs GCC et Intel ?"
  - "Quelles sont les principales normes ISO qui ont fait évoluer le langage C depuis sa création par Dennis Ritchie ?"
  - "Pourquoi est-il fortement recommandé d'utiliser la norme C11 ou supérieure pour la gestion de la mémoire et de la concurrence ?"
  - "Quels sont les pièges à éviter concernant l'utilisation du mot-clé \"volatile\" et les options d'optimisation des compilateurs GCC et Intel ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

!!! attention "Attention aux sources"
    Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

!!! tip "Recommandation"
    Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait au préalable aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version plus récente.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! warning "Mise en garde sur le mot-clé volatile"
    Le modificateur `volatile` est employé incorrectement en C car on le confond avec le `volatile` Java qui n'a pas du tout le même sens. Le mot-clé Java `volatile` correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

!!! warning "Attention aux options d'optimisation GCC"
    L'option `-O3` comprend des améliorations possiblement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, lisez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pouvez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

!!! warning "Attention aux options de compilation Intel"
    Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante. Prenez connaissance des pages man Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour des détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).