---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:29:41.263414+00:00"

tags:
  []

keywords:
  - "normes ISO C11"
  - "options de compilation GCC -O2"
  - "modificateur volatile"
  - "langage C"
  - "modèle de mémoire et de concurrence"

questions:
  - "Quelles sont les principales différences entre les normes ISO C99 et C11, notamment en ce qui concerne la gestion de la concurrence et le modèle de mémoire ?"
  - "Pourquoi l’utilisation du mot‑clé <tt>volatile</tt> en C est‑elle souvent mal comprise, et quel équivalent C correspond au <tt>volatile</tt> de Java ?"
  - "Quels conseils donne le texte concernant le choix des options de compilation avec GCC et les compilateurs Intel pour éviter des comportements dangereux ou des imprécisions en virgule flottante ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

Le C est un langage de programmation impératif et généraliste de haut niveau créé entre 1969 et 1973 chez Bell Labs par Dennis Ritchie. Il existe aujourd'hui des normes ISO établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et l'impact des normes ISO, consultez les liens suivants :

* [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
* [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
* [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Modèles de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'y avait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple concernant les comportements ambigus qui avaient ou non été documentés par les fournisseurs de compilateurs.

!!! tip "Recommandation"
    Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version ultérieure.

## Pièges
### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous pouvez le constater en consultant [cette page](http://en.cppreference.com/w/cpp/language/cv). Cependant, l'emploi de ce modificateur est rare et se limite à certains types de code de bas niveau.

Le mot-clé `volatile` est souvent employé incorrectement en C, car on le confond avec le `volatile` de Java qui n'a pas du tout le même sens. Le mot-clé `volatile` de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs
#### GCC

L'option `-O3` inclut des optimisations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*).

!!! warning "Attention"
    En cas de doute, utilisez plutôt l'option `-O2`. Si vous en avez le temps, consultez la page de manuel (par exemple `man gcc`) et cherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sécuritaires.

#### Intel

Les compilateurs C et C++ d'Intel peuvent occasionner des difficultés dans le cas d'opérations avec virgule flottante.

!!! tip "Conseil"
    Consultez les pages de manuel d'Intel (par exemple `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).