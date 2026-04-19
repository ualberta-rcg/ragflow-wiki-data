---
title: "Narval/fr"
slug: "narval"
lang: "fr"

source_wiki_title: "Narval/fr"
source_hash: "88d1bcfa29d4a6e72e41f236b75a325c"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:00:01.022669+00:00"

tags:
  []

keywords:
  - "Ressources de calcul"
  - "réseau InfiniBand central"
  - "Technologie MIG"
  - "soutien technique"
  - "commutateurs HDR"
  - "réseau InfiniBand"
  - "Instances GPU"
  - "Nœuds CPU et GPU"
  - "processeurs AMD"
  - "Environnement logiciel"
  - "Narval"
  - "facteur de blocage"
  - "Suivi des tâches"
  - "îlots de nœuds"
  - "FlexiBLAS"
  - "Compilateurs Intel"
  - "calcul scientifique"
  - "Grappe Narval"
  - "Bibliothèques BLAS et LAPACK"
  - "Processeurs AMD EPYC"
  - "GPU A100"
  - "Intel MKL"
  - "stockage"
  - "serveurs de stockage"
  - "grappe de calcul"

questions:
  - "Quelles sont les principales restrictions d'utilisation de la grappe Narval, notamment concernant l'accès à internet et la gestion des tâches ?"
  - "Quelles sont les différences de capacité, de sauvegarde et de fonction entre les espaces de stockage HOME, SCRATCH et PROJECT ?"
  - "Comment l'architecture du réseau haute performance InfiniBand est-elle structurée pour connecter les nœuds de calcul et les serveurs de stockage ?"
  - "Quelles sont les caractéristiques matérielles et les capacités de calcul parallèle des différents nœuds de la grappe Narval ?"
  - "Quelles options de compilation faut-il utiliser ou éviter avec les compilateurs Intel pour assurer la compatibilité avec les processeurs AMD de Narval ?"
  - "Quel est l'environnement logiciel par défaut de Narval et quelles sont les recommandations concernant l'utilisation des bibliothèques mathématiques comme BLAS et LAPACK ?"
  - "À quoi servent les sept liens HDR restants dans l'architecture du réseau ?"
  - "Quel est le facteur de blocage maximum appliqué à la connexion des îlots de nœuds ?"
  - "Pourquoi les serveurs de stockage sont-ils configurés avec un facteur de blocage significativement plus bas ?"
  - "Que faut-il faire si une fonctionnalité n'est disponible que sur une ancienne version de l'environnement standard ?"
  - "Quelle est la limitation de la bibliothèque Intel MKL lorsqu'elle est utilisée sur des processeurs AMD ?"
  - "Quelle bibliothèque est désormais recommandée par défaut pour BLAS et LAPACK, et où peut-on trouver plus d'informations à ce sujet ?"
  - "Quelles sont les commandes Slurm requises pour allouer un ou plusieurs GPU A100 complets selon la répartition souhaitée ?"
  - "Quelles sont les caractéristiques des différentes instances GPU fractionnées (MIG) disponibles et comment en demander une spécifiquement ?"
  - "Comment le portail permet-il de faire le suivi des tâches de calcul et pourquoi est-il crucial d'ajuster ses demandes de ressources en conséquence ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Caractéristique | Valeur |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Disponibilité                       | depuis octobre 2021                                                                                                          |
| Nœud de connexion                   | **narval.alliancecan.ca**                                                                                                    |
| Collection Globus                   | **[Compute Canada - Narval](https://app.globus.org/file-manager?origin_id=a1713da6-098f-40e6-b3aa-034efe8b6e5b)**             |
| Nœud de copie (rsync, scp, sftp,...) | **narval.alliancecan.ca**                                                                                                    |
| Portail                             | [https://portail.narval.calculquebec.ca/](https://portail.narval.calculquebec.ca/)                                            |

Narval est une grappe hétérogène et polyvalente conçue pour une grande variété de calculs scientifiques de petite et moyenne taille. Construite par Dell Canada et CDW Canada, Narval est située à l' [École de technologie supérieure](http://www.etsmtl.ca/). Son nom rappelle le [narval](https://fr.wikipedia.org/wiki/Narval), un mammifère marin qui a parfois été observé dans les eaux du fleuve Saint-Laurent.

## Particularités
Notre politique veut que les nœuds de calcul de Narval n'aient pas accès à l'internet. Pour y faire exception, veuillez joindre le [soutien technique](../support/technical_support.md) en expliquant ce dont vous avez besoin et pourquoi. Notez que l'outil `crontab` n'est pas offert.

Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et vous ne pouvez pas avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est de 7 jours (168 heures).

## Stockage
| Type de stockage | Description et particularités                                                                                                                                                                                                                                                                                                                                                                                      |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME             | Système de fichiers Lustre, 64 To d’espace au total                                                                                                                                                                                                                                                                                                                                                              <ul><li>Cet espace est petit et ne peut pas être agrandi : vous devrez utiliser votre espace `project` pour les grands besoins en stockage.</li><li>Petits [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur.</li><li>Il y a une sauvegarde automatique une fois par jour.</li></ul> |
| SCRATCH          | Système de fichiers Lustre, 5.7 Po d’espace au total                                                                                                                                                                                                                                                                                                                                                             <ul><li>Grand espace pour stocker les fichiers temporaires pendant les calculs.</li><li>Pas de système de sauvegarde automatique.</li><li>Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur.</li><li>Il y a une [purge automatique](../storage-and-data/scratch_purging_policy.md) des vieux fichiers dans cet espace.</li></ul> |
| PROJECT          | Système de fichiers Lustre, 35 Po d’espace au total                                                                                                                                                                                                                                                                                                                                                              <ul><li>Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données.</li><li>Grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) ajustables par projet.</li><li>Il y a une sauvegarde automatique une fois par jour.</li></ul> |

Au tout début de la présente page, un tableau indique plusieurs adresses de connexion. Pour les transferts de données par [Globus](../getting-started/globus.md), il faut utiliser le **Point de chute Globus**. Par contre, pour les outils comme [rsync](../getting-started/transferring_data.md#rsync) et [scp](../getting-started/transferring_data.md#scp), il faut utiliser l'adresse du **Nœud de copie**.

## Réseautique haute performance

Le réseau [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [HDR de Mellanox](https://www.nvidia.com/en-us/networking/infiniband/qm8700/) relie tous les nœuds de la grappe. Chaque commutateur de 40 ports HDR (200 Gb/s) permet de connecter ensemble jusqu'à 66 nœuds en HDR100 (100 Gb/s) avec 33 liens HDR divisés en deux (2) par des câbles spéciaux. Les sept (7) liens HDR restants servent à connecter le commutateur d'un cabinet à chacun des sept (7) commutateurs HDR du réseau InfiniBand central. Les îlots de nœuds sont donc connectés avec un facteur de blocage maximum de 33:7 (4.7:1). Par contre, les serveurs de stockage sont branchés avec un facteur de blocage significativement plus bas pour une performance maximale.

En pratique, les cabinets de Narval contiennent des îlots de 48 ou 56 nœuds CPU réguliers. Il est donc possible d'exécuter des tâches parallèles utilisant jusqu’à 3584 cœurs et une réseautique non bloquante. Pour des tâches plus imposantes ou plus fragmentées sur le réseau, le facteur de blocage est de 4.7:1. L’interconnexion reste malgré tout de haute performance.

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | CPU                                                                                                                                                              | Stockage      | GPU                                                     |
| :---- | :---- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :------------------------------------------------------ |
| 1145  | 64    | 250G ou 256000M    | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M cache L3 | 1 x SSD de 960G |                                                         |
| 33    | 64    | 2009G ou 2057500M  | 2 x [AMD EPYC 7532 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7532.html) @ 2.40 GHz, 256M cache L3 | 1 x SSD de 960G |                                                         |
| 3     | 64    | 4000G ou 4096000M  | 2 x [AMD EPYC 7502 (Zen 2)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7002-series/amd-epyc-7502.html) @ 2.50 GHz, 128M cache L3 | 1 x SSD de 960G |                                                         |
| 159   | 48    | 498G ou 510000M    | 2 x [AMD EPYC 7413 (Zen 3)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-7003-series/amd-epyc-7413.html) @ 2.65 GHz, 128M cache L3 | 1 x SSD de 3.84T | 4 x NVidia A100SXM4 (mémoire 40G), connectés via NVLink |

### Particularités liées aux processeurs AMD
#### Ensemble d'instructions pris en charge
La grappe Narval est équipée de processeurs AMD EPYC de 2e et 3e génération qui prennent en charge les instructions [AVX2](https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2).

Narval ne prend toutefois pas en charge les instructions [AVX512](https://en.wikipedia.org/wiki/AVX-512), contrairement aux nœuds de grappes plus récentes.

#### Compilateurs Intel
Les compilateurs Intel peuvent très bien compiler des applications pour les processeurs AMD de Narval, et ce, en se limitant aux ensembles d'instructions AVX2 et les plus anciens. Pour ce faire, il faut utiliser l'option `-march=core-avx2` du compilateur Intel, ce qui permet d'obtenir des exécutables qui sont compatibles à la fois avec les processeurs Intel et AMD.

Par contre, si vous avez compilé un code sur un système utilisant des processeurs Intel et que vous avez utilisé une ou des options `-xXXXX`, telle que `-xCORE-AVX2`, les applications compilées ne fonctionneront pas sur Narval, car les compilateurs Intel ajoutent des instructions supplémentaires pour vérifier que le processeur utilisé est un produit Intel. Sur Narval, les options `-xHOST` et `-march=native` sont équivalentes à `-march=pentium` (l'ancien Pentium de 1993) et ne devraient **pas** être utilisés.

#### Environnements logiciels disponibles
[L'environnement logiciel standard `StdEnv/2023`](../programming/standard_software_environments.md) est l'environnement par défaut sur Narval. Les anciennes versions (2016 et 2018) ont été volontairement bloquées. Si vous avez besoin d'un logiciel qui n'est disponible que sur une ancienne version de l'environnement standard, nous vous invitons à envoyer une demande à [notre soutien technique](../support/technical_support.md).

#### Bibliothèques BLAS et LAPACK
La bibliothèque Intel MKL fonctionne sur les processeurs AMD, mais elle n'est pas optimale. Nous favorisons dorénavant l'utilisation de FlexiBLAS. Pour plus de détails, consulter la page [BLAS et LAPACK](../programming/blas_and_lapack.md).

### Instances GPU

Pour demander un ou plusieurs GPU A100 complets, il faut utiliser une des options Slurm suivantes :
*   **Un A100-40gb** :
    ```bash
    --gpus=a100:1
    ```
*   **Plusieurs A100-40gb** par nœud :
    ```bash
    --gpus-per-node=a100:2
    ```
    ```bash
    --gpus-per-node=a100:3
    ```
    ```bash
    --gpus-per-node=a100:4
    ```
*   **Plusieurs A100-40gb** éparpillés n'importe où :
    ```bash
    --gpus=a100:n
    ```
    (remplacer `n` par le nombre voulu)

Plusieurs nœuds GPU de Narval sont configurés avec la [technologie MIG](../programming/multi-instance_gpu.md) et quatre tailles d'instances GPU sont disponibles :

*   **1g.5gb** : 1/8 de la puissance de calcul avec 5 Go de mémoire GPU.
*   **2g.10gb** : 2/8 de la puissance de calcul avec 10 Go de mémoire GPU.
*   **3g.20gb** : 3/8 de la puissance de calcul avec 20 Go de mémoire GPU.

Pour demander **une et une seule** instance GPU pour votre tâche de calcul, voici les options correspondantes :

*   **1g.5gb** :
    ```bash
    --gpus=a100_1g.5gb:1
    ```
*   **2g.10gb** :
    ```bash
    --gpus=a100_2g.10gb:1
    ```
*   **3g.20gb** :
    ```bash
    --gpus=a100_3g.20gb:1
    ```

Les quantités maximales recommandées de **cœurs CPU et de mémoire système** par instance GPU sont listées dans la [table des caractéristiques des *bundles*](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Suivi de vos tâches

Depuis le [portail](https://portail.narval.calculquebec.ca/), vous pouvez suivre vos tâches de calcul CPU comme GPU **en temps réel** ou celles passées afin de maximiser l'utilisation des ressources et diminuer vos temps d'attente dans la file.

Vous pourrez notamment visualiser pour une tâche :
*   l'utilisation des cœurs de calcul;
*   la mémoire utilisée;
*   l'utilisation de GPUs.

Il est important d'utiliser les ressources allouées et de rectifier vos demandes lorsque les ressources de calcul sont peu ou pas utilisées. Par exemple, si vous demandez quatre cœurs (CPU) mais n'en utilisez qu'un seul, vous devez ajuster votre fichier de soumission en conséquence.