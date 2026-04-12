---
title: "C/fr"
slug: "c"
lang: "fr"

source_wiki_title: "C/fr"
source_hash: "370b4e50fae6f77d4cff7eb03c134b26"
last_synced: "2026-04-12T21:18:48.865179+00:00"
last_processed: "2026-04-12T21:23:14.177085+00:00"

tags:
  []

keywords:
  - "Mot-clé volatile"
  - "Compilateurs"
  - "Normes ISO"
  - "Langage C"
  - "Concurrence"

questions:
  - "Quelles sont les principales évolutions apportées par les différentes normes ISO du langage C, en particulier la norme C11 ?"
  - "Quelle est la différence de signification et d'usage du mot-clé volatile entre les langages C et Java ?"
  - "Quelles précautions spécifiques doivent être prises lors de l'utilisation des options de compilation avec GCC et Intel pour éviter des comportements dangereux ou inattendus ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Le langage C

Le langage C est un langage de programmation impératif et généraliste de haut niveau, créé entre 1969 et 1973 aux Bell Labs par Dennis Ritchie. Aujourd'hui, il existe des normes ISO qui ont été établies en 1989-1990 (C89 ou C90), 1999 (C99) et 2011 (C11). Pour en apprendre plus sur le langage et sur l'impact des normes ISO, voici quelques liens utiles :

*   [C](https://fr.wikipedia.org/wiki/C_(langage)), historique, C90.
*   [C99](https://en.wikipedia.org/wiki/C99), inclut les fonctions du langage et de la bibliothèque standard; `int` n'est plus le type par défaut.
*   [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)), mise à jour majeure, ajout du modèle de mémoire et des fonctionnalités de concurrence (multifil, *atomics*, *compare-and-swap*).

!!! warning "Fiabilité des sources"
    Ces liens peuvent mener à des pages qui contiennent des erreurs. Le document officiel peut être commandé auprès du [Conseil canadien des normes](http://www.scc.ca/fr).

## Modèles améliorés de mémoire et de concurrence

Ces modèles sont apparus dans la norme ISO de 2011. Auparavant, il n'y avait aucune gestion des accès concurrents à la mémoire en lecture et en écriture, par exemple en ce qui a trait aux comportements ambigus qui ont été documentés ou non par les fournisseurs de compilateurs. Nous recommandons de compiler le code C comportant de la concurrence en C11 ou une version plus récente.

## Pièges

### Mot-clé `volatile`

Le modificateur `volatile` a un sens très particulier en C et C++, comme vous le constaterez en lisant [cette page](http://en.cppreference.com/w/cpp/language/cv). L'emploi de ce modificateur est toutefois rare et se limite à certains types de code de bas niveau.

!!! tip "Confusion avec Java"
    Le mot-clé `volatile` est souvent employé incorrectement en C, car il est confondu avec le `volatile` de Java qui n'a pas du tout le même sens. Le mot-clé `volatile` de Java correspond en C à `atomic_*`, où l'astérisque représente un nom de type fondamental tel que `int`.

### Compilateurs

#### GCC

!!! warning "Options d'optimisation GCC"
    L'option `-O3` de GCC inclut des optimisations potentiellement dangereuses, par exemple pour les fonctions de crénelage (*aliasing*). En cas de doute, utilisez plutôt l'option `-O2`. Si vous en avez le temps, consultez la page de manuel (par exemple, en tapant `man gcc`) et recherchez `-O3`; vous pourrez ainsi désactiver les paramètres qui ne sont pas sécuritaires.

#### Intel

!!! warning "Opérations à virgule flottante avec les compilateurs Intel"
    Les compilateurs C et C++ d'Intel peuvent causer des problèmes avec les opérations à virgule flottante. Prenez connaissance des pages de manuel d'Intel (par exemple, en tapant `man icc`) et utilisez les options `-fp-model precise` ou `-fp-model source` pour respecter les normes ANSI, ISO et IEEE. Pour plus de détails, consultez [ce document](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).