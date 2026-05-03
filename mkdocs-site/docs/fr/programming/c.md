---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:40:22.383434+00:00"

tags:
  []

keywords:
  - "Compilateurs"
  - "Langage C"
  - "Concurrence"
  - "Mot-clé volatile"
  - "Normes ISO"

questions:
  - "Quelles sont les principales normes ISO du langage C et quelles fonctionnalités majeures ont été introduites par la norme C11 ?"
  - "Pourquoi l'utilisation du mot-clé volatile est-elle souvent source de confusion en C par rapport à son équivalent en Java ?"
  - "Quelles précautions spécifiques doivent être prises concernant les options d'optimisation lors de l'utilisation des compilateurs GCC et Intel ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

Le langage C est un langage de programmation impératif et généraliste de haut niveau, créé entre 1969 et 1973 par Dennis Ritchie aux Bell Labs. Aujourd'hui, des normes ISO ont été établies en 1989-1990 (C89 ou C90), en 1999 (C99) et en 2011 (C11). Pour en apprendre plus sur le langage et l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens pourraient mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Améliorations des modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'existait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui avaient ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

`volatile` est souvent employé incorrectement en C, car on le confond avec le `volatile` de Java qui n'a pas du tout le même sens. Le mot-clé `volatile` de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

L'option `-O3` comprend des améliorations possiblement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous avez le temps, lisez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

Les compilateurs C et C++ d'Intel risquent de causer des difficultés dans le cas d'opérations avec virgule flottante. Prenez connaissance des pages man d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).