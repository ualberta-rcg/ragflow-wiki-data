---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:41:39.848078+00:00"

tags:
  []

keywords:
  - "modèle de mémoire et de concurrence"
  - "options de compilation -O2"
  - "modificateur volatile"
  - "normes ISO C11"
  - "langage C"

questions:
  - "Quelles sont les normes ISO du langage C (C89/C90, C99, C11) et quelles évolutions majeures chacune a‑t‑elle apportées ?"
  - "En quoi le mot‑clé <tt>volatile</tt> en C diffère‑t‑il du <tt>volatile</tt> Java, et quelle fonctionnalité C doit‑on utiliser pour obtenir un comportement similaire de visibilité et d’atomicité ?"
  - "Quels paramètres de compilation recommandez‑vous pour GCC et les compilateurs Intel afin d’éviter les optimisations dangereuses ou les imprécisions en virgule flottante lors du développement de code concurrent en C ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent conduire à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Meilleurs modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait au préalable aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous le constaterez en consultant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'utilisation de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

`volatile` est utilisé incorrectement en C car on le confond avec le `volatile` Java qui n'a pas du tout le même sens. Le mot-clé Java `volatile` correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

!!! warning "Options d'optimisation (GCC)"
    L'option `-O3` comprend des améliorations possiblement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, consultez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pouvez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

!!! caution "Opérations en virgule flottante (Intel)"
    Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante. Consultez les pages man d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour des détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).