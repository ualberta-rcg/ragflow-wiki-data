---
title: "Standard software environments/fr"
slug: "standard_software_environments"
lang: "fr"

source_wiki_title: "Standard software environments/fr"
source_hash: "07ecfc84e552818ea7f28c0f552796f6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:34:42.741209+00:00"

tags:
  []

keywords:
  - "Open MPI"
  - "extensions de modules"
  - "compilateurs"
  - "Environnement logiciel"
  - "architectures CPU"
  - "Compilateurs"
  - "noyau Linux"
  - "Modules"
  - "bio-informatique"
  - "optimisations spécifiques"
  - "StdEnv"
  - "environnement logiciel"
  - "module"
  - "couche de compatibilité"
  - "compilateur"

questions:
  - "Qu'est-ce qu'un environnement logiciel standard (StdEnv) et comment ses modules sont-ils structurés ?"
  - "Quelles sont les principales mises à jour et modifications apportées aux modules par défaut dans la version StdEnv/2023 ?"
  - "Comment la version StdEnv/2020 optimise-t-elle les performances des binaires sur des grappes possédant plusieurs générations de processeurs ?"
  - "Quelles sont les exigences minimales du noyau Linux pour les différentes versions de l'environnement standard ?"
  - "Quel changement majeur a été apporté à l'outil de la couche de compatibilité lors du passage à la version 2020 ?"
  - "Quelles sont les principales différences techniques, telles que les compilateurs et le support AVX512, entre les environnements obsolètes StdEnv/2016.4 et StdEnv/2018.3 ?"
  - "Quel est l'impact du déplacement d'Intel à un niveau plus bas de la hiérarchie sur la visibilité des modules ?"
  - "Quels sont les exemples spécifiques de modules qui ne nécessitent plus le chargement préalable du module gcc ?"
  - "Quelles optimisations techniques ont permis de rendre ces modules visibles indépendamment du compilateur chargé ?"
  - "Quelles sont les exigences minimales du noyau Linux pour les différentes versions de l'environnement standard ?"
  - "Quel changement majeur a été apporté à l'outil de la couche de compatibilité lors du passage à la version 2020 ?"
  - "Quelles sont les principales différences techniques, telles que les compilateurs et le support AVX512, entre les environnements obsolètes StdEnv/2016.4 et StdEnv/2018.3 ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour plus d'information sur la migration vers les environnements standards, voyez la page [Migration vers le nouvel environnement standard](../clusters/migration_to_the_new_standard_environment.md).

## Description
Nos environnements logiciels sont rendus disponibles par un ensemble de [modules](utiliser_des_modules.md) qui vous permettent d'alterner entre différentes versions d'un paquet logiciel. Ces modules sont organisés selon une structure en arbre dont le tronc est composé des mêmes utilitaires que ceux offerts dans les environnements Linux. Les branches principales de ce tronc sont les versions des compilateurs auxquelles sont rattachées des sous-branches pour chaque version de MPI ou CUDA.

Un environnement logiciel standard est composé d’une combinaison particulière de modules de compilation et de modules MPI groupés dans un module appelé `StdEnv`. Ces environnements sont communément utilisés par notre équipe technique pour construire d’autres logiciels.

En date de février 2023, les quatre versions des environnements standards étaient 2023, 2020, 2018.3 et 2016.4, chacune comportant des améliorations importantes. Nous supportons seulement les versions 2023 et 2020.

Nous décrivons ici les différences entre les versions et expliquons pourquoi il est préférable d’installer la plus récente.

Les plus récentes versions des paquets logiciels sont habituellement installées dans le plus récent environnement logiciel.

### `StdEnv/2023`
Cette dernière itération de notre environnement logiciel utilise par défaut GCC 12.3.0, Intel 2023.1, et Open MPI 4.1.5.

Pour activer cet environnement, lancez la commande :
```bash
module load StdEnv/2023
```

#### Amélioration de la performance
L'ensemble minimal des instructions CPU supporté est AVX2, de façon générale `x86-64-v3`. Même la couche de compatibilité qui offre les commandes Linux de base est compilé avec des optimisations pour ces commandes.

#### Changements aux modules par défaut
Le compilateur par défaut GCC plutôt que Intel. Nous compilons avec Intel uniquement les applications qui démontrent une meilleure performance avec Intel. CUDA devient une extension de OpenMPI plutôt que le contraire, c'est-à-dire que MPI pour CUDA est chargé au lancement si CUDA est chargé. Ceci permet de partager plusieurs bibliothèques MPI sur toutes les branches (CUDA ou non).

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

Activez cet environnement avec la commande :
```bash
module load StdEnv/2020
```

#### Amélioration de la performance
Les binaires générés avec le compilateur Intel supportent automatiquement les jeux d’instructions AVX2 et AVX512. Techniquement, ce sont des binaires multiarchitecture, aussi appelés [fat binaries](https://en.wikipedia.org/wiki/Fat_binary). Ceci signifie que quand vous utilisez une grappe comme Cedar ou Graham qui ont connu plusieurs générations de processeurs, vous n’avez plus besoin de charger manuellement un des modules `arch` si vous utilisez des paquets logiciels générés avec le compilateur Intel.

Certains paquets logiciels installés auparavant avec GCC ou Intel se trouvent maintenant à un niveau plus bas de la hiérarchie, ce qui fait que le même module est visible peu importe le compilateur qui est chargé; c’est le cas par exemple pour les modules [R](../software/r.md) et pour plusieurs paquets en bio-informatique pour lesquels le module `gcc` devait auparavant être chargé. Ceci a été rendu possible par des optimisations spécifiques aux architectures CPU que nous avons effectuées sous le niveau du compilateur.

Nous avons aussi installé une version plus récente de [GNU C Library](https://en.wikipedia.org/wiki/GNU_C_Library) qui offre des fonctions mathématiques optimisées. Ceci a nécessité une plus récente version du noyau Linux (voir ci-dessous).

#### Couche de compatibilité
La couche de compatibilité est un niveau de la hiérarchie en dessous de celui des compilateurs et des paquets logiciels pour que ces derniers soient indépendants du système d’exploitation sous-jacent et qu’ils fonctionnent autant sous CentOS que sous Ubuntu ou Fedora. Un changement majeur dans la version 2020 a été de changer d'outil pour la couche de compatibilité en passant de [Nix package manager](https://en.wikipedia.org/wiki/Nix_package_manager) à [Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix).

#### Noyau Linux
Les versions 2016.4 et 2018.3 nécessitent une version du noyau Linux 2.6.32 ou plus, ce qui est supporté à partir de CentOS 6. La version 2020 demande un noyau Linux 3.10 ou plus, ce qui est supporté à partir de CentOS 7. Les autres distributions Linux ont habituellement un noyau beaucoup plus récent et vous n’aurez donc pas à changer votre distribution Linux si vous utilisez cet environnement standard sous une autre que CentOS.

#### Extensions de modules
Avec l'environnement 2020, nous avons commencé à installer plusieurs extensions Python dans les modules principaux correspondants. Par exemple, `PyQt5` a été installé dans le module `qt/5.12.8` pour supporter plusieurs versions de Python. Le système des modules a été modifié pour vous permettre de trouver facilement ce type d'extensions. Par exemple, avec :
```bash
module spider pyqt5
```
vous saurez que vous pouvez obtenir le module `qt/5.12.8`.

### `StdEnv/2018.3`
!!! warning "Obsolète"
    Cet environnement n'est plus pris en charge.

Cette deuxième version de notre environnement logiciel a été installée en 2018, avec la mise en service de la grappe [Béluga](../clusters/béluga.md), peu après le déploiement de [Niagara](niagara.md). Les compilateurs par défaut sont passés à GCC 7.3.0 et Intel 2018.3. L’implémentation MPI par défaut est passée à Open MPI 3.1.2. Il s’agit de la première version à offrir le support des instructions AVX512.

Activez cet environnement avec la commande :
```bash
module load StdEnv/2018.3
```

### `StdEnv/2016.4`
!!! warning "Obsolète"
    Cet environnement n'est plus supporté.

Cette première version de notre environnement logiciel a été installée en 2016 avec la mise en service des grappes [Cedar](../clusters/cedar.md) et [Graham](../clusters/graham.md). Les compilateurs par défaut sont GCC 5.4.0 et Intel 2016.4. L’implémentation MPI par défaut est Open MPI 2.1.1. La plupart des logiciels compilés dans cet environnement ne supportent pas les instructions AVX512, contrairement aux processeurs Skylake de [Béluga](../clusters/béluga.md), [Niagara](niagara.md) et aux récents ajouts à Cedar et Graham.

Activez cet environnement avec la commande :
```bash
module load StdEnv/2016.4