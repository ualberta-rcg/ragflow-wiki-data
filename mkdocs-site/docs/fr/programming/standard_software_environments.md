---
title: "Standard software environments/fr"
slug: "standard_software_environments"
lang: "fr"

source_wiki_title: "Standard software environments/fr"
source_hash: "de2b24e03a0b0bc08c92cfb11780d0b1"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T03:01:10.143639+00:00"

tags:
  []

keywords:
  - "Gentoo Prefix"
  - "StdEnv/2020"
  - "couche de compatibilité"
  - "AVX512"
  - "extensions Python PyQt5"
  - "binaire multiarchitecture"
  - "StdEnv/2026"
  - "modules de compilation"
  - "compilateur Intel"
  - "fat binaries"
  - "AVX2"
  - "GCC 12.3.0"
  - "noyau Linux 3.10"
  - "Open MPI 4.1.5"

questions:
  - "Quelles versions d’environnements standards sont actuellement prises en charge par l’équipe ?"
  - "Quels sont les principaux changements de modules et d’optimisations entre StdEnv/2026 et StdEnv/2023 ?"
  - "Quelle commande faut‑il utiliser pour activer un environnement StdEnv donné sur le système ?"
  - "Quels sont les principaux changements introduits dans la version 2020 de l’environnement logiciel par rapport aux versions 2016.4 et 2018.3 ?"
  - "Quelle version minimale du noyau Linux est requise pour chaque version de l’environnement (2016.4, 2018.3, 2020) et quelles distributions Linux sont concernées ?"
  - "Comment la couche de compatibilité a‑t‑elle évolué, notamment le passage de Nix package manager à Gentoo Prefix dans la version 2020 ?"
  - "Qu’est‑ce qu’un binaire multi‑architecture (fat binary) et comment il gère les jeux d’instructions AVX2 et AVX512 ?"
  - "Pourquoi, sur des grappes comme Cedar ou Graham, n’est‑plus nécessaire de charger manuellement un module <tt>arch</tt> ?"
  - "Quels bénéfices apporte l’utilisation de paquets logiciels compilés avec le compilateur Intel sur des systèmes contenant plusieurs générations de processeurs ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour plus d'information sur la migration vers les environnements standards, consultez la page Migration vers le nouvel environnement standard.

## Description
Nos environnements logiciels sont rendus disponibles par un ensemble de [modules](utiliser_des_modules.md) qui vous permettent d'alterner entre différentes versions d'un paquet logiciel. Ces modules sont organisés selon une structure en arbre dont le tronc est composé des mêmes utilitaires que ceux offerts dans les environnements Linux. Les branches principales de ce tronc sont les versions des compilateurs auxquelles sont rattachées des sous-branches pour chaque version de MPI ou CUDA.

Un environnement logiciel standard est composé d’une combinaison particulière de modules de compilation et de modules MPI groupés dans un module appelé `StdEnv`. Ces environnements sont communément utilisés par notre équipe technique pour construire d’autres logiciels.

En date de novembre 2026, les cinq versions des environnements standards étaient 2023, 2020, 2018.3 et 2016.4, chacune comportant des améliorations importantes. **Nous supportons seulement les versions 2026 et 2023.**

Nous décrivons ici les différences entre les versions et expliquons pourquoi il est préférable d’installer la plus récente.

Les plus récentes versions des paquets logiciels sont habituellement installées dans le plus récent environnement logiciel.

### `StdEnv/2026`
Cette version est la plus récente de notre environnement logiciel. Elle utilise par défaut GCC 15.3.0, Intel 2026.1, CUDA 13.3 et Open MPI 5.0.10.

Pour activer cet environnement, lancez la commande
```bash
module load StdEnv/2026
```

### `StdEnv/2023`
Cette dernière itération de notre environnement logiciel utilise par défaut GCC 12.3.0, Intel 2023.1 et Open MPI 4.1.5.

Pour activer cet environnement, lancez la commande
```bash
module load StdEnv/2023
```

#### Amélioration de la performance
L'ensemble minimal des instructions CPU supporté est AVX2, généralement `x86-64-v3`. Même la couche de compatibilité qui offre les commandes Linux de base est compilée avec des optimisations pour celles-ci.

#### Changements aux modules par défaut
Le compilateur par défaut est GCC plutôt qu'Intel. Nous compilons avec Intel uniquement les applications qui démontrent une meilleure performance avec Intel. CUDA devient une extension de OpenMPI plutôt que le contraire, c'est-à-dire que MPI pour CUDA est chargé au lancement si CUDA est chargé. Ceci permet de partager plusieurs bibliothèques MPI sur toutes les branches (CUDA ou non).

Les versions par défaut des modules suivants ont été mises à jour :
*   GCC 9.3 => GCC 12.3
*   OpenMPI 4.0.3 => OpenMPI 4.1.5
*   Compilateurs Intel 2020 => 2023
*   Intel MKL 2020 => Flexiblas 3.3.1 (avec MKL 2023 ou BLIS 0.9.0)
*   CUDA 11 => CUDA 12

### `StdEnv/2020`
!!! warning "Obsolète"
    Cet environnement n'est plus pris en charge sur les nouveaux systèmes; cependant, les logiciels pour CPU seulement fonctionneront sans problème.

Cette troisième version de notre environnement logiciel est devenue la version par défaut en avril 2021. Les compilateurs par défaut sont passés à GCC 9.3.0 et Intel 2020.1. MPI par défaut est passée à Open MPI 4.0.3.

Pour activer cet environnement, lancez la commande
```bash
module load StdEnv/2020
```

#### Amélioration de la performance
Les binaires générés avec le compilateur Intel supportent automatiquement les jeux d’instructions AVX2 et AVX512. Techniquement, ce sont des binaires multiarchitecture, aussi appelés [fat binaries](https://en.wikipedia.org/wiki/Fat_binary). Ceci signifie que lorsque vous utilisez une grappe comme Cedar ou Graham qui ont connu plusieurs générations de processeurs, vous n’avez plus besoin de charger manuellement l'un des modules `arch` si vous utilisez des paquets logiciels générés avec le compilateur Intel.

Certains paquets logiciels installés auparavant avec GCC ou Intel se trouvent maintenant à un niveau plus bas de la hiérarchie, ce qui fait que le même module est visible peu importe le compilateur qui est chargé. C’est le cas, par exemple, pour les modules R et pour plusieurs paquets en bio-informatique pour lesquels le module `gcc` devait auparavant être chargé. Ceci a été rendu possible par des optimisations spécifiques aux architectures CPU que nous avons effectuées sous le niveau du compilateur.

Nous avons aussi installé une version plus récente de [GNU C Library](https://en.wikipedia.org/wiki/GNU_C_Library) qui offre des fonctions mathématiques optimisées. Ceci a nécessité une plus récente version du noyau Linux (voir ci-dessous).

#### Couche de compatibilité
La couche de compatibilité est un niveau de la hiérarchie en dessous de celui des compilateurs et des paquets logiciels pour que ces derniers soient indépendants du système d’exploitation sous-jacent et qu’ils fonctionnent autant sous CentOS que sous Ubuntu ou Fedora. Un changement majeur dans la version 2020 a été de changer d'outil pour la couche de compatibilité en passant de [Nix package manager](https://en.wikipedia.org/wiki/Nix_package_manager) à [Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix).

#### Noyau Linux
Les versions 2016.4 et 2018.3 nécessitent une version du noyau Linux 2.6.32 ou plus, ce qui est supporté à partir de CentOS 6. La version 2020 demande un noyau Linux 3.10 ou plus, ce qui est supporté à partir de CentOS 7. Les autres distributions Linux ont habituellement un noyau beaucoup plus récent et vous n’aurez donc pas à changer votre distribution Linux si vous utilisez cet environnement standard sous une autre que CentOS.

#### Extensions de modules
Avec l'environnement 2020, nous avons commencé à installer plusieurs extensions Python dans les modules principaux correspondants. Par exemple, `PyQt5` a été installé dans le module `qt/5.12.8` pour supporter plusieurs versions de Python. Le système des modules a été modifié pour vous permettre de trouver facilement ce type d'extensions. Par exemple, avec
```bash
module spider pyqt5
```
vous saurez que vous pouvez obtenir le module `qt/5.12.8`.

### `StdEnv/2018.3`
!!! warning "Obsolète"
    Cet environnement n'est plus pris en charge.

Cette deuxième version de notre environnement logiciel a été installée en 2018, avec la mise en service de la grappe [Béluga](../clusters/béluga.md), peu après le déploiement de Niagara. Les compilateurs par défaut sont passés à GCC 7.3.0 et Intel 2018.3. L’implémentation MPI par défaut est passée à Open MPI 3.1.2. Il s’agit de la première version à offrir le support des instructions AVX512.

Pour activer cet environnement, lancez la commande
```bash
module load StdEnv/2018.3
```

### `StdEnv/2016.4`
!!! warning "Obsolète"
    Cet environnement n'est plus supporté.

Cette première version de notre environnement logiciel a été installée en 2016 avec la mise en service des grappes Cedar et Graham. Les compilateurs par défaut sont GCC 5.4.0 et Intel 2016.4. L’implémentation MPI par défaut est Open MPI 2.1.1. La plupart des logiciels compilés dans cet environnement ne supportent pas les instructions AVX512, contrairement aux processeurs Skylake de [Béluga](../clusters/béluga.md), Niagara et aux récents ajouts à Cedar et Graham.

Pour activer cet environnement, lancez la commande
```bash
module load StdEnv/2016.4