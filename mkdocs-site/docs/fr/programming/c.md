---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-08-30T01:09:18.871111+00:00"
last_processed: "2026-08-30T01:33:38.860610+00:00"

tags:
  []

keywords:
  - "langage C"
  - "options de compilation GCC -O2 -O3"
  - "mot‑clé volatile"
  - "modèle de mémoire et de concurrence"
  - "normes ISO C89 C99 C11"

questions:
  - "Quelles sont les principales révisions du standard ISO du langage C et quelles nouveautés introduisent‑elles, notamment en matière de gestion de la mémoire et de la concurrence ?"
  - "Pourquoi l’utilisation du mot‑clé <tt>volatile</tt> en C diffère‑t‑elle de son équivalent en Java, et quelles alternatives C offrent des garanties similaires de visibilité entre threads ?"
  - "Quels sont les risques associés aux options d’optimisation -O3 de GCC et aux paramètres de modèle de virgule flottante d’Intel, et quelles alternatives sont recommandées pour garantir la conformité aux normes ?"

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

!!! warning "Mise en garde"
    Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Modèles de mémoire et de concurrence optimisés

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'y avait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs.

!!! note "Recommandation"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++ comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

`volatile` est souvent employé incorrectement en C, car on le confond avec le `volatile` Java qui n'a pas du tout le même sens. Le mot-clé Java `volatile` correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

!!! warning "Mise en garde : options d'optimisation GCC"
    L'option `-O3` comprend des améliorations possiblement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, lisez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pouvez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

!!! warning "Mise en garde : compilateurs Intel et virgule flottante"
    Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante. Prenez connaissance des pages man Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour des détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).