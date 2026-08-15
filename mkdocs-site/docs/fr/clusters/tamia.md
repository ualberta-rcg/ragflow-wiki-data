---
title: "TamIA/fr"
slug: "tamia"
lang: "fr"

source_wiki_title: "TamIA/fr"
source_hash: "262138f54d7e583f4e46e7f3dcb78450"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:35:41.119419+00:00"

tags:
  []

keywords:
  - "nœuds de calcul"
  - "environnement logiciel standard StdEnv/2023"
  - "--gpus-per-nodes"
  - "options Slurm"
  - "GPU H100"
  - "grappe de calcul"
  - "Système de fichiers Lustre"
  - "portail tamia"
  - "ajustement des ressources"
  - "réseau InfiniBand"
  - "suivi des tâches"
  - "tâches GPU"
  - "système de fichiers Lustre"
  - "sauvegarde automatique"
  - "GPU H100/H200"
  - "tamIA"
  - "intelligence artificielle"
  - "CCRI"
  - "utilisation des GPU"
  - "Canada"
  - "Ajouter des membres"
  - "quotas fixes par utilisateur"
  - "projet RAP"
  - "stockage Lustre"

questions:
  - "Quelles sont les étapes et les conditions nécessaires pour obtenir un accès à la grappe tamIA et pouvoir soumettre des tâches de calcul ?"
  - "Quelles sont les restrictions d’utilisation des nœuds de calcul de tamIA (accès Internet, crontab, VSCode, durée et nombre de tâches, exigences GPU) ?"
  - "Quels espaces de stockage sont proposés sur tamIA et quelles sont leurs limites respectives (HOME, project, etc.) ?"
  - "Quels sont les quotas attribués et les politiques de sauvegarde (ou de purge) pour les systèmes de fichiers SCRATCH et PROJECT ?"
  - "Quelle adresse de connexion doit‑on utiliser selon l’outil de transfert de données (Globus versus rsync ou scp) ?"
  - "Quelles sont les caractéristiques matérielles des nœuds (CPU, mémoire, stockage, GPU) et comment lancer une tâche GPU avec Slurm sur ces nœuds ?"
  - "Comment ajouter un membre à un projet en renseignant son CCRI dans la section « Ajouter des membres » ?"
  - "Pourquoi la grappe de calcul est‑elle accessible uniquement depuis le Canada ?"
  - "Quelle contrainte présente l’espace de stockage Lustre et quelle solution est suggérée pour les besoins de stockage importants ?"
  - "Quel est l'environnement logiciel standard (StdEnv/2023) utilisé par défaut sur tamIA ?"
  - "De quelle manière les tâches GPU sont‑elles assignées sur le cluster ?"
  - "Quelles options Slurm permettent de réserver un nœud avec des GPU H100 ou H200, et combien de GPU sont alloués pour chaque type ?"
  - "Comment spécifier le nombre et le type de GPU à allouer pour une tâche multi‑nœuds ?"
  - "Quels indicateurs peut‑on visualiser en temps réel sur le portail Tamia pour suivre l’utilisation d’une tâche de calcul ?"
  - "Pourquoi et comment doit‑on ajuster les demandes de ressources (CPU/GPU) lors d’une exécution de tâche ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

Voici le document MediaWiki converti en Markdown propre pour MkDocs Material, en français québécois :

| Disponibilité : | **31 mars 2025** |
|---|---|
| Nœud de connexion : | **tamia.alliancecan.ca** |
| [Nœud d'automatisation](../getting-started/automation_in_the_context_of_multifactor_authentication.md) : | robot.tamia.ecpia.ca |
| Collection Globus : | [Serveur Globus v5 de TamIA](https://app.globus.org/file-manager?origin_id=72c3bca0-9281-4742-b066-333ba0fdef72) |
| Nœud de copie (rsync, scp, sftp,...) : | **tamia.alliancecan.ca** |
| Portail : | <https://portail.tamia.ecpia.ca/> |

tamIA est une grappe dédiée aux besoins de la communauté scientifique canadienne en matière d'intelligence artificielle. tamIA est située à [l'Université Laval](http://www.ulaval.ca/) et est co-gérée avec [Mila](https://mila.quebec/) et [Calcul Québec](https://calculquebec.ca/). Son nom rappelle le [tamia](https://fr.wikipedia.org/wiki/Tamia), un mammifère rongeur présent en Amérique du Nord.

Cette grappe fait partie de [l'environnement de calcul pancanadien de l’IA (ECPIA)](https://www.alliancecan.ca/fr/nos-services/calcul-informatique-de-pointe/environnement-de-calcul-pan-canadien-pour-lintelligence-artificielle-ecpia).

## Particularités

!!! warning "Accès Internet restreint"
    Notre politique veut que les nœuds de calcul de tamIA n'aient pas accès à Internet. Pour y faire exception, veuillez joindre le [soutien technique](../support/technical_support.md) en expliquant ce dont vous avez besoin et pourquoi.

!!! warning "crontab interdit"
    Notez que l'outil `crontab` n'est pas offert.

!!! warning "VSCode interdit sur les nœuds de connexion"
    Notez que l'environnement de développement intégré [VSCode](https://code.visualstudio.com/) est **interdit** sur les nœuds **frontaux** (nœuds de connexion) en raison de sa lourde charge. Il est encore autorisé sur les nœuds de calcul.

!!! important "Durée et nombre de tâches"
    Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et vous ne pouvez pas avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est d'une journée (24 heures).

!!! important "Utilisation des GPU"
    Chaque tâche doit utiliser tous les GPU des serveurs alloués, soit 4 pour les H100 et 8 pour les H200.

## Accès

1.  Pour accéder à la grappe de calcul, chaque chercheuse ou chercheur doit [compléter une demande d'accès dans la CCDB](https://ccdb.alliancecan.ca/me/access_services) **(onglet *Intelligence artificielle*, puis sélectionner *tamIA*)**. L'accès à la grappe peut prendre jusqu'à une heure après avoir complété la demande d'accès.

2.  Pour pouvoir soumettre des tâches de calcul, vous devez être membre d'un projet RAP (*Projet d'allocation de ressources*) préfixé `aip-`. Si vous êtes une **chercheuse principale ou un chercheur principal** et que vous n'avez pas encore de tel RAP, vous devez soumettre une [déclaration de l'utilisation envisagée de l'intelligence artificielle](https://ccdb.alliancecan.ca/paice/general_access_to_paice_systems).

La procédure pour parrainer d'autres chercheuses et chercheurs est la suivante :
*   Sur la **[page d'accueil de la CCDB](https://ccdb.alliancecan.ca/)**, consulter la table *Projet avec allocation de ressources* ;
*   Chercher le RAPI du projet `aip-` et cliquer dessus pour être redirigé vers la page de gestion du RAP ;
*   En bas de la page de gestion du RAP, cliquer sur **Gérer l'appartenance aux projets** ;
*   Dans la section *Ajouter des membres*, entrer le CCRI du membre à ajouter.

La grappe de calcul est accessible uniquement à partir du Canada.

## Stockage

| | |
|:---|:---|
| HOME <br> Système de fichiers Lustre | !!! warning "Espace limité et pas de sauvegarde"Cet espace est petit et ne peut pas être agrandi : vous devrez utiliser votre espace `project` pour les grands besoins en stockage. Il y a de petits [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur. Il n'y a actuellement aucune sauvegarde automatique. (Planifié pour le printemps 2026) |
| SCRATCH <br> Système de fichiers Lustre | !!! warning "Purge automatique"C'est un grand espace pour stocker les fichiers temporaires pendant les calculs. Il n'y a pas de système de sauvegarde automatique. Il y a de grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) fixes par utilisateur. Il y a une [purge automatique](../storage-and-data/scratch_purging_policy.md) des vieux fichiers dans cet espace. |
| PROJECT <br> Système de fichiers Lustre | !!! note "Sauvegarde quotidienne"Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données. Il y a de grands [quotas](../storage-and-data/storage_and_file_management.md#quotas-et-politiques) ajustables par projet. Il y a une sauvegarde automatique une fois par jour. |

Le tableau au début de cette page indique plusieurs adresses de connexion. Pour les transferts de données par [Globus](../getting-started/globus.md), il faut utiliser le **Point de chute Globus**. Par contre, pour les outils comme [rsync](../getting-started/transferring_data.md#rsync) et [scp](../getting-started/transferring_data.md#scp), il faut utiliser l'adresse du **Nœud de copie**.

## Réseautique haute performance

Le réseau [InfiniBand](https://fr.wikipedia.org/wiki/Bus_InfiniBand) [NDR de Nvidia](https://www.nvidia.com/en-us/networking/quantum2/) relie tous les nœuds de la grappe. Chaque GPU est connecté à un port NDR200 via une carte Nvidia ConnectX-7. Chaque serveur a donc 4 ou 8 ports NDR200 de connectés sur la fabrique Infiniband.

Le réseau Infiniband est non bloquant pour les serveurs de calculs et est composé de 2 étages de commutateurs disposés dans une topologie "fat-tree". Le stockage et les nœuds de calcul sont reliés via 4 ou 8 connexions à 400 Gb/s au cœur du réseau.

## Caractéristiques des nœuds

| Nœuds | Cœurs | Mémoire disponible | CPU | Stockage | GPU |
|:-----|:-----|:-------------------|:----|:---------|:----|
| 12 | 64 | 1024 GB | 2 x [Intel Xeon Gold 6448Y 2,1 GHz, 32C](https://www.intel.com/content/www/us/en/products/sku/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz/specifications.html) | 1 x SSD de 7.68TB | 8 x [NVIDIA HGX H200](https://www.nvidia.com/en-us/data-center/h200/) SXM 141GB HBM3 700W, connectés via NVLink |
| 53 | 48 | 512 GB | 2 x [Intel Xeon Gold 6442Y 2,6 GHz, 24C](https://www.intel.com/content/www/us/en/products/sku/232380/intel-xeon-gold-6442y-processor-60m-cache-2-60-ghz/specifications.html) | 1 x SSD de 7.68TB | 4 x [NVIDIA HGX H100](https://www.nvidia.com/en-us/data-center/h100/) SXM 80GB HBM3 700W, connectés via NVLink |
| 8 | 64 | 512 GB | 2 x [Intel Xeon Gold 6438M 2.2G, 32C/64T](https://www.intel.com/content/www/us/en/products/sku/232398/intel-xeon-gold-6438m-processor-60m-cache-2-20-ghz/specifications.html) | 1 x SSD de 7.68TB | Aucun |

### Environnements logiciels disponibles

[L'environnement logiciel standard `StdEnv/2023`](../programming/standard_software_environments.md) est l'environnement par défaut sur tamIA.

### Tâches GPU

Les tâches sont assignées sur les nœuds complets. Utilisez une des options Slurm suivantes :

Pour une tâche sur un nœud avec GPU H100 :
```bash
--gpus=h100:4
```

Pour une tâche sur un nœud avec GPU H200 :
```bash
--gpus=h200:8
```

Pour les tâches avec plusieurs nœuds, utiliser `--gpus-per-nodes=h100:4` ou `--gpus-per-nodes=h200:8`.

## Suivi de vos tâches

Depuis le [portail](https://portail.tamia.ecpia.ca/), vous pourrez suivre vos tâches de calcul GPU comme CPU **en temps réel** ou celles passées afin de maximiser l'utilisation des ressources et diminuer vos temps d'attente dans la file.

Vous pourrez notamment visualiser pour une tâche :
*   l'utilisation des cœurs de calcul ;
*   la mémoire utilisée ;
*   l'utilisation des GPU.

Il est important d'utiliser les ressources allouées et de rectifier vos demandes lorsque les ressources de calcul sont peu ou pas utilisées. Par exemple, si vous demandez quatre cœurs (CPU) mais n'en utilisez qu'un seul, vous devez ajuster votre fichier de soumission en conséquence.