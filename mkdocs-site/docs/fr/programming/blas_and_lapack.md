---
title: "BLAS and LAPACK/fr"
slug: "blas_and_lapack"
lang: "fr"

source_wiki_title: "BLAS and LAPACK/fr"
source_hash: "9a163a19948a6f32c5991967b5dcf97a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:43:27.338555+00:00"

tags:
  []

keywords:
  - "compilateur Intel"
  - "implémentation"
  - "Narval"
  - "FLEXIBLAS"
  - "Intel MKL"
  - "BLAS/LAPACK"
  - "options de compilation"
  - "FlexiBLAS"
  - "LAPACK"
  - "MKL Link Advisor"
  - "BLIS"
  - "BLAS"
  - "implémentations"

questions:
  - "Que sont les bibliothèques BLAS et LAPACK, et pourquoi est-il important de choisir la bonne implémentation selon le matériel utilisé ?"
  - "Quel est le rôle principal de FlexiBLAS et quel problème majeur permet-il de résoudre lors du déploiement de logiciels sur plusieurs grappes de calcul ?"
  - "Comment doit-on configurer la compilation d'un programme avec FlexiBLAS et comment changer l'implémentation en arrière-plan lors de l'exécution ?"
  - "Comment doit-on modifier les options d'un compilateur Intel pour utiliser directement la bibliothèque MKL à la place de FlexiBLAS ?"
  - "Quelle est la démarche à suivre pour intégrer Intel MKL avec des compilateurs tiers tels que GCC ?"
  - "Dans quelles situations l'outil Intel MKL Link Advisor s'avère-t-il utile pour les développeurs ?"
  - "Quelles sont les implémentations de FLEXIBLAS disponibles en janvier 2022 et quelle commande permet d'en afficher la liste complète ?"
  - "Quelle est la configuration par défaut de la variable FLEXIBLAS sur la grappe Narval ?"
  - "Quelle bibliothèque est utilisée par défaut sur les grappes autres que Narval lorsque la variable FLEXIBLAS n'est pas définie ?"
  - "Comment doit-on modifier les options d'un compilateur Intel pour utiliser directement la bibliothèque MKL à la place de FlexiBLAS ?"
  - "Quelle est la démarche à suivre pour intégrer Intel MKL avec des compilateurs tiers tels que GCC ?"
  - "Dans quelles situations l'outil Intel MKL Link Advisor s'avère-t-il utile pour les développeurs ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[BLAS (Basic Linear Algebra Subprogram)](http://www.netlib.org/blas/) et [LAPACK (Linear Algebra PACK)](http://www.netlib.org/lapack/) sont deux des bibliothèques les plus utilisées en calcul de pointe pour la recherche. Elles servent aux opérations sur les vecteurs et les matrices qui sont fréquentes dans plusieurs algorithmes. Elles sont encore plus que des bibliothèques, car elles définissent une interface de programmation standard, soit un ensemble de définitions de fonctions qui peuvent être appelées pour faire certains calculs comme le produit scalaire de deux vecteurs de nombres double précision ou le produit de deux matrices hermitiennes de nombres complexes.

En plus de l'implémentation de référence de Netlib, il existe plusieurs autres implémentations de ces deux standards. La performance de ces implémentations peut varier de beaucoup selon le logiciel utilisé; par exemple, il est clairement établi que l'implémentation fournie par [la bibliothèque Intel Math Kernel Library (Intel MKL)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) offre une meilleure performance avec les processeurs Intel dans la plupart des situations. Intel est cependant propriétaire de cette implémentation et dans certains cas il est préférable d'utiliser [l'implémentation libre OpenBLAS](https://github.com/xianyi/OpenBLAS) ou encore [BLIS](https://github.com/flame/blis), dont la performance est meilleure avec les processeurs AMD. Deux projets qui ne sont plus maintenus sont [gotoblas](https://www.tacc.utexas.edu/research-development/tacc-software/gotoblas2) et [ATLAS BLAS](https://github.com/math-atlas/math-atlas).

!!! info "À propos de FlexiBLAS"
    Malheureusement, il faut habituellement recompiler un logiciel pour savoir quelle implémentation est la plus performante pour un code particulier et une configuration matérielle précise. Ceci est problématique quand on veut créer un environnement logiciel portable pouvant fonctionner sur plusieurs grappes. Pour y remédier, vous pouvez utiliser [FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas), une couche d'abstraction qui permet de changer l'implémentation de BLAS et de LAPACK au moment de l'exécution plutôt que pendant la compilation.

## Choisir une implémentation
Depuis quelques années, nous recommandions d'utiliser Intel MKL comme implémentation de référence étant donné que nos grappes n'avaient que des processeurs Intel. Depuis la mise en service de [Narval](../clusters/narval.md) qui possède des processeurs AMD, nous recommandons maintenant de compiler le code avec FlexiBLAS. La configuration de notre module FlexiBLAS fait en sorte que BLIS est utilisé en présence de processeurs AMD et Intel MKL en présence d'autres types de processeurs, ce qui offre habituellement la performance optimale.

## Compiler avec FlexiBLAS
Puisque FlexiBLAS est relativement récent, ce ne sont pas tous les systèmes qui vont le reconnaître par défaut. Il est généralement possible de pallier à ceci en configurant les options d'édition pour utiliser `-lflexiblas` pour BLAS et pour LAPACK. Ces options sont habituellement dans votre Makefile, autrement vous pouvez les passer comme paramètres à `configure` ou `cmake`. Les versions de CMake à partir de 3.19 peuvent trouver FlexiBLAS automatiquement; pour utiliser une de ces versions, chargez le module `cmake/3.20.1` ou `cmake/3.21.4`.

## Changer l'implémentation de BLAS/LAPACK pour l'exécution
L'avantage principal de FlexiBLAS est de pouvoir changer l'implémentation en arrière-plan pour l'exécution en configurant la variable d'environnement `FLEXIBLAS`. En date de janvier 2022, les implémentations disponibles sont `netlib`, `blis`, `imkl` et `openblas`, mais vous pouvez obtenir la liste complète avec la commande :

```bash
flexiblas list
```

Sur [Narval](../clusters/narval.md), nous avons configuré `FLEXIBLAS=blis` pour utiliser BLIS par défaut. Sur les autres grappes, `FLEXIBLAS` n'est pas défini et Intel MKL est utilisé par défaut.

## Utiliser directement Intel MKL
Même si nous recommandons d'utiliser FlexiBLAS, il est toujours possible d'utiliser directement Intel MKL. Avec un compilateur Intel (par exemple `ifort`, `icc`, `icpc`), la solution est de remplacer `-lblas` et `-llapack` dans les options du compilateur et de l'éditeur (*linker*) avec :
*   `-mkl=sequential` pour ne pas utiliser de fils internes, ou
*   `-mkl` pour utiliser des fils internes.

Ceci fait en sorte que l'implémentation MKL de BLAS/LAPACK est utilisée. Voyez [la documentation sur les options](https://software.intel.com/en-us/mkl-linux-developer-guide-using-the-mkl-compiler-option).

Avec les compilateurs autres que ceux d'Intel, par exemple la GCC (GNU Compiler Collection), vous devez lister explicitement les bibliothèques MKL requises au cours de l'étape d'édition. Intel fournit l'outil [MKL Link Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) pour vous aider à déterminer les options de compilation et d'édition.

!!! tip "Problèmes de référence indéfinie"
    [MKL Link Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) est aussi utile si vous obtenez des erreurs *undefined reference* avec les compilateurs Intel et `-mkl`.