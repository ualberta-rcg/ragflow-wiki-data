---
title: "BLAS and LAPACK/fr"
slug: "blas_and_lapack"
lang: "fr"

source_wiki_title: "BLAS and LAPACK/fr"
source_hash: "b260d1cda8bec2cf2ccb5009606c7b50"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:44:35.823713+00:00"

tags:
  []

keywords:
  - "implémentations"
  - "BLAS"
  - "implémentation"
  - "BLAS/LAPACK"
  - "FLEXIBLAS"
  - "compilateur"
  - "MKL Link Advisor"
  - "Intel MKL"
  - "LAPACK"
  - "BLIS"
  - "FlexiBLAS"
  - "Narval"

questions:
  - "Pourquoi existe-t-il différentes implémentations des bibliothèques BLAS et LAPACK et comment le choix du matériel influence-t-il leur performance ?"
  - "Quel problème majeur l'outil FlexiBLAS permet-il de résoudre par rapport à la compilation traditionnelle des logiciels ?"
  - "Comment peut-on compiler un code avec FlexiBLAS et changer l'implémentation utilisée au moment de l'exécution ?"
  - "Quelle est la différence de configuration par défaut entre le système Nibi et les autres systèmes concernant FLEXIBLAS et Intel MKL ?"
  - "Comment doit-on modifier les options du compilateur et de l'éditeur de liens pour utiliser directement Intel MKL avec un compilateur Intel ?"
  - "Quel outil est recommandé pour déterminer les bibliothèques requises avec des compilateurs non-Intel comme GCC ou pour résoudre les erreurs de référence indéfinie ?"
  - "Quelles sont les implémentations de FLEXIBLAS disponibles en janvier 2022 et quelle commande permet d'en obtenir la liste complète ?"
  - "Quelle est l'implémentation configurée par défaut pour FLEXIBLAS sur la grappe Narval ?"
  - "Quelle bibliothèque est utilisée par défaut sur les autres grappes lorsque la variable d'environnement FLEXIBLAS n'est pas définie ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[BLAS (Basic Linear Algebra Subprogram)](http://www.netlib.org/blas/) et [LAPACK (Linear Algebra PACK)](http://www.netlib.org/lapack/) sont deux des bibliothèques les plus courantes en calcul de pointe pour la recherche. Elles servent aux opérations sur les vecteurs et les matrices, qui sont fréquentes dans plusieurs algorithmes. Elles sont même plus que des bibliothèques, car elles définissent une interface de programmation standard, soit un ensemble de définitions de fonctions qu'on peut appeler pour faire certains calculs, comme le produit scalaire de deux vecteurs de nombres à double précision ou le produit de deux matrices hermitiennes de nombres complexes.

En plus de l'implémentation de référence de Netlib, il existe plusieurs autres implémentations de ces deux standards. La performance de ces implémentations peut varier grandement selon le logiciel utilisé. Par exemple, il est clairement établi que l'implémentation fournie par [la bibliothèque Intel Math Kernel Library (Intel MKL)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) donne une meilleure performance avec les processeurs Intel dans la majorité des situations. Intel est cependant propriétaire de cette implémentation, et dans certains cas, il est préférable d'utiliser [l'implémentation libre OpenBLAS](https://github.com/xianyi/OpenBLAS) ou encore [BLIS](https://github.com/flame/blis), dont la performance est meilleure avec les processeurs AMD. Deux projets qui ne sont plus maintenus sont [gotoblas](https://www.tacc.utexas.edu/research-development/tacc-software/gotoblas2) et [ATLAS BLAS](https://github.com/math-atlas/math-atlas).

Malheureusement, il faut habituellement recompiler un logiciel pour savoir quelle implémentation est la plus performante pour un code particulier et une configuration matérielle précise. Ceci est problématique quand on cherche à créer un environnement logiciel portable pouvant fonctionner sur plusieurs grappes. Pour y remédier, vous pouvez utiliser [FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas), une couche d'abstraction qui permet de changer l'implémentation de BLAS et de LAPACK au moment de l'exécution plutôt que durant la compilation.

## Choisir une implémentation
Depuis quelques années, nous recommandions d'utiliser Intel MKL comme implémentation de référence, étant donné que nos grappes n'avaient que des processeurs Intel. Depuis la mise en service de [Narval](../clusters/narval.md), qui possède des processeurs AMD, nous recommandons maintenant de compiler le code avec FlexiBLAS. La configuration de notre module FlexiBLAS fait en sorte qu'à BLIS est utilisé en présence de processeurs AMD et Intel MKL en présence d'autres types de processeurs, ce qui donne habituellement la performance optimale.

## Compiler avec FlexiBLAS
Puisque FlexiBLAS est relativement récent, ce ne sont pas tous les systèmes qui vont le reconnaître par défaut. Il est généralement possible d'y pallier en configurant les options de l'éditeur de liens pour utiliser `-lflexiblas` pour BLAS et pour LAPACK. Ces options sont habituellement dans votre `Makefile`, autrement vous pouvez les passer comme paramètres à `configure` ou `cmake`. Les versions de CMake à partir de la 3.19 peuvent trouver FlexiBLAS automatiquement; pour utiliser une de ces versions, chargez le module `cmake/3.20.1` ou `cmake/3.21.4`.

## Changer l'implémentation de BLAS/LAPACK pour l'exécution
L'avantage principal de FlexiBLAS est de pouvoir changer l'implémentation en arrière-plan au moment de l'exécution en configurant la variable d'environnement `FLEXIBLAS`. En date de janvier 2022, les implémentations disponibles sont `netlib`, `blis`, `imkl` et `openblas`, mais vous pouvez obtenir la liste complète avec la commande suivante :

```bash
flexiblas list
```

*   Sur [Narval](../clusters/narval.md), nous avons configuré `FLEXIBLAS=blis` pour utiliser BLIS par défaut. Sur les autres grappes, `FLEXIBLAS` n'est pas défini et Intel MKL est utilisé par défaut.
*   Sur [Nibi](../clusters/nibi.md), `FLEXIBLAS` n'est pas défini et Intel MKL est utilisé par défaut.
*   Sur les autres systèmes, nous avons configuré `FLEXIBLAS=aocl`.

## Utiliser directement Intel MKL

!!! note
    Même si nous recommandons d'utiliser FlexiBLAS, il est toujours possible d'utiliser directement Intel MKL.

Avec un compilateur Intel (par exemple `ifort`, `icc`, `icpc`), la solution consiste à remplacer `-lblas` et `-llapack` dans les options du compilateur et de l'éditeur de liens avec :

*   `-mkl=sequential` pour ne pas utiliser de fils internes, ou
*   `-mkl` pour utiliser des fils internes.

Ceci fait en sorte que l'implémentation MKL de BLAS/LAPACK est utilisée. Consultez [la documentation sur les options](https://software.intel.com/en-us/mkl-linux-developer-guide-using-the-mkl-compiler-option).

Avec les compilateurs autres que ceux d'Intel, par exemple la GCC (GNU Compiler Collection), vous devez lister explicitement les bibliothèques MKL requises au cours de l'étape de l'édition de liens.

!!! tip
    Intel fournit l'outil [MKL Link Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) pour vous aider à déterminer les options de compilation et d'édition de liens. Cet outil est aussi utile si vous obtenez des erreurs `undefined reference` avec les compilateurs Intel et `-mkl`.