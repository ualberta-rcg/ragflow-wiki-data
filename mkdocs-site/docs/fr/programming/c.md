---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-10-11T01:39:35.690021+00:00"
last_processed: "2026-10-11T02:25:51.566620+00:00"

tags:
  []

keywords:
  - "mot‑clé volatile"
  - "modèle de mémoire et concurrence"
  - "compilateurs GCC et Intel"
  - "normes ISO C89 C99 C11"
  - "langage C"

questions:
  - "Quelles sont les principales normes ISO du langage C et quelles évolutions majeures chacune a introduites ?"
  - "Pourquoi le mot‑clé <tt>volatile</tt> en C ne doit pas être confondu avec le même mot‑clé en Java, et quelle est l’alternative C pour obtenir un comportement similaire ?"
  - "Quels conseils le texte donne‑t‑il concernant le choix des options de compilation avec GCC et les compilateurs Intel pour éviter des comportements indésirables, notamment en matière d’optimisation et de calcul en virgule flottante ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, consultez les liens suivants :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent conduire à des pages qui pourraient contenir des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Évolution des modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011; il n'y avait auparavant aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont ou non été documentés par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou plus.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! warning "Attention : confusion avec Java"
    Le mot-clé `volatile` est souvent mal utilisé en C, car il est confondu avec le mot-clé `volatile` de Java, qui n'a pas du tout la même signification. Le mot-clé `volatile` de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

L'option `-O3` comprend des améliorations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! tip "Recommandation pour l'optimisation"
    En cas de doute, utilisez plutôt l'option `-O2`.

Si vous avez le temps, consultez la page man (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sûrs.

#### Intel

!!! warning "Opérations en virgule flottante avec Intel"
    Les compilateurs C et C++ d'Intel peuvent entraîner des difficultés lors d'opérations avec virgule flottante. Pour respecter les normes ANSI, ISO et IEEE, consultez les pages man d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source`. Pour plus de détails, référez-vous à [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).