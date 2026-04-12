---
title: "Rorqual/fr"
slug: "rorqual"
lang: "fr"

source_wiki_title: "Rorqual/fr"
source_hash: "e60bf7befd16d550cc4fbc103837141a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:06:34.746750+00:00"

tags:
  []

keywords:
  - "calcul scientifique"
  - "instances GPU"
  - "Transferts de données"
  - "Topologie des nœuds CPU"
  - "mémoire cache"
  - "nœuds NUMA"
  - "mémoire GPU"
  - "Quotas"
  - "Rorqual"
  - "cœurs"
  - "Réseautique haute performance"
  - "chiplet"
  - "H100"
  - "nœuds GPU"
  - "Système de fichiers Lustre"
  - "instance GPU"
  - "stockage"
  - "SCRATCH"
  - "bundles"
  - "puissance de calcul"
  - "Caractéristiques des nœuds"
  - "grappe de calcul"
  - "Fichiers temporaires"
  - "cœurs CPU"
  - "mémoire système"
  - "Sauvegarde automatique"
  - "technologie MIG"
  - "programmes parallèles multifils"
  - "NVidia H100"
  - "accès aux systèmes"
  - "tâche de calcul"
  - "OpenMP"

questions:
  - "Quelle est la fonction principale de la grappe Rorqual et où est-elle située physiquement ?"
  - "Quelles sont les étapes à suivre et les ententes spécifiques à accepter pour obtenir l'accès à ce système de calcul ?"
  - "Quelles sont les restrictions techniques imposées aux utilisateurs concernant l'exécution des tâches et la gestion des espaces de stockage (HOME et SCRATCH) ?"
  - "Quelle est la fréquence des sauvegardes automatiques pour l'espace de stockage soumis à des quotas par utilisateur ?"
  - "Comment les utilisateurs peuvent-ils accéder au système de fichiers SCRATCH et quelle est sa capacité totale ?"
  - "Quelle est l'utilité principale de l'espace SCRATCH et bénéficie-t-il d'un système de sauvegarde automatique ?"
  - "Quelles sont les différences d'utilisation et les adresses de connexion requises pour transférer des données selon que l'on utilise Globus ou des outils comme rsync et scp ?"
  - "Quelles sont les caractéristiques matérielles (CPU, GPU, mémoire, stockage) des différents types de nœuds disponibles sur cette grappe de calcul ?"
  - "Comment la topologie interne des nœuds CPU (architecture NUMA, chiplets, mémoire cache) influence-t-elle l'optimisation des programmes parallèles multifils ?"
  - "Comment faut-il configurer les paramètres de tâche pour optimiser l'utilisation de la topologie des nœuds NUMA ?"
  - "Quelle est l'architecture matérielle détaillée (processeurs, mémoire, accélérateurs) qui compose les nœuds GPU ?"
  - "Quelles sont les différentes instances GPU (complètes et MIG) disponibles sur Rorqual et quelles options Slurm permettent de les réserver ?"
  - "Quelle est la capacité des mémoires caches L1 et L2 allouée à chaque cœur individuel ?"
  - "Combien de cœurs composent un \"chiplet\" et se partagent la même mémoire cache L3 ?"
  - "Pour quel type de programme cette architecture de cœurs groupés est-elle idéale et quelle option de commande l'illustre ?"
  - "Quelles sont les commandes spécifiques pour allouer les différentes partitions de GPU H100 ?"
  - "Où peut-on trouver les quantités maximales recommandées de cœurs CPU et de mémoire système par instance GPU ?"
  - "À quoi sert la table des caractéristiques des bundles mentionnée dans le texte ?"
  - "Quelle est la capacité de mémoire et la fraction de puissance de calcul allouées à l'instance H100-2g.20gb ?"
  - "Dans quel contexte spécifique ces différentes options de partitionnement GPU sont-elles proposées à l'utilisateur ?"
  - "Comment la puissance de calcul et la mémoire évoluent-elles entre les trois modèles d'instances présentés ?"
  - "Quelles sont les commandes spécifiques pour allouer les différentes partitions de GPU H100 ?"
  - "Où peut-on trouver les quantités maximales recommandées de cœurs CPU et de mémoire système par instance GPU ?"
  - "À quoi sert la table des caractéristiques des bundles mentionnée dans le texte ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Disponibilité | 19 juin 2025 |
| Nœud de connexion | `rorqual.alliancecan.ca` |
| Nœud de copie (rsync, scp, sftp ...) | `rorqual.alliancecan.ca` |
| [Nœud d'automatisation](automation-in-the-context-of-multifactor-authentication.md) | `robot.rorqual.alliancecan.ca` |
| Collection Globus | [alliancecan#rorqual](https://app.globus.org/file-manager?origin_id=f19f13f5-5553-40e3-ba30-6c151b9d35d4) |
| JupyterHub | [jupyterhub.rorqual.alliancecan.ca](https://jupyterhub.rorqual.alliancecan.ca/) |
| Portail | [metrix.rorqual.alliancecan.ca](https://metrix.rorqual.alliancecan.ca/) |
| Webinaire | [diapositives](https://docs.google.com/presentation/d/1SxqzNI9dtxnVCe8I2otJg6PJpLQwDjeDakNI7yMsuvU), [vidéo](https://www.youtube.com/watch?v=hTM6XOvYjxw) |

Rorqual est une grappe hétérogène et polyvalente conçue pour une grande variété de calculs scientifiques. Construite par Dell Canada et CDW Canada, Rorqual est située à l'[École de technologie supérieure](http://www.etsmtl.ca/). Son nom rappelle le [rorqual](https://fr.wikipedia.org/wiki/Rorqual), un mammifère marin dont plusieurs espèces, par exemple le [petit rorqual](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/petit-rorqual/) et le [rorqual bleu](https://baleinesendirect.org/decouvrir/especes-baleines-saint-laurent/13-especes/rorqual-bleu/) ont été observées dans les eaux du fleuve Saint-Laurent.

## Accès

Pour accéder à la grappe de calcul, chaque chercheuse ou chercheur doit [compléter une demande d'accès](https://ccdb.alliancecan.ca/me/access_systems) dans le formulaire que l'on trouve via *Ressources > Accès aux systèmes* de la barre de menus de CCDB. Dans ce formulaire :

1.  Sélectionnez *Rorqual* dans la liste de gauche.
2.  Dans le premier encadré à droite, sélectionnez la demande d'accès.
3.  Acceptez ensuite toutes les ententes particulières avec Calcul Québec :
    *   Consentement pour la collecte et l'utilisation de renseignements personnels,
    *   Accord de niveau de service de Rorqual,
    *   Conditions d’utilisation.

L'accès effectif à la grappe peut prendre **jusqu'à une heure** après avoir complété la demande d'accès.

## Particularités

!!! note
    Notre politique veut que les nœuds de calcul de Rorqual n'aient pas accès à l'internet. Pour y faire exception, veuillez joindre le [soutien technique](technical-support.md) en expliquant ce dont vous avez besoin et pourquoi. Notez que l'outil `crontab` n'est pas offert.

Chaque tâche devrait être d'une durée d’au moins une heure (au moins cinq minutes pour les tâches de test) et vous ne pouvez pas avoir plus de 1000 tâches (en exécution et en attente) à la fois. La durée maximale d'une tâche est de 7 jours (168 heures).

## Stockage

| | |
| :------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HOME <br> Système de fichiers Lustre, 116 To d’espace au total | *   Cet espace est petit et ne peut pas être agrandi : vous devrez utiliser votre espace `project` pour les grands besoins en stockage. <br> *   Petits [quotas](storage-and-file-management.md#quotas-et-politiques) fixes par utilisateur <br> *   Il y a une sauvegarde automatique une fois par jour. |
| SCRATCH <br> Système de fichiers Lustre, 6.5 Po d’espace au total | *   Accessible via le lien symbolique `$HOME/links/scratch` <br> *   Grand espace pour stocker les fichiers temporaires pendant les calculs. <br> *   Pas de système de sauvegarde automatique <br> *   Grands [quotas](storage-and-file-management.md#quotas-et-politiques) fixes par utilisateur <br> *   Il y a une [purge automatique](scratch-purging-policy.md) des vieux fichiers dans cet espace. |
| PROJECT <br> Système de fichiers Lustre, 62 Po d’espace au total | *   Accessible via le lien symbolique `$HOME/links/projects/nom-du-projet` <br> *   Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données. <br> *   Grands [quotas](storage-and-file-management.md#quotas-et-politiques) ajustables par projet <br> *   Il y a une sauvegarde automatique une fois par jour. |

Au tout début de la présente page, un tableau indique plusieurs adresses de connexion. Pour les transferts de données par [Globus](globus.md), il faut utiliser le **Point de chute Globus**. Par contre, pour les outils comme [rsync](transferring-data.md#rsync) et [scp](transferring-data.md#scp), il faut utiliser l'adresse du **Nœud de copie**.

## Réseautique haute performance

*   Réseautique InfiniBand
    *   HDR 200 Gbit/s
    *   Facteur de blocage maximum : 34:6 ou 5.667:1
    *   Taille des îlots de nœuds CPU : jusqu'à 31 nœuds de 192 cœurs pouvant communiquer sans blocage.

## Caractéristiques des nœuds

| nœuds | cœurs | mémoire disponible | stockage | CPU | GPU |
| :---- | :---- | :----------------- | :------- | :-- | :-- |
| 670   | 192   | 750G ou 768000M    | 1 x SSD SATA de 480Go (6Gbit/s) | 2 x [AMD EPYC 9654 (Zen 4)](https://www.amd.com/en/support/downloads/drivers.html/processors/epyc/epyc-9004-series/amd-epyc-9654.html) @ 2.40 GHz, cache L3 de 384Mo | |
| 8     |       | 1 x SSD NVMe de 3.84To | | | |
| 8     |       | 3013G ou 3086250M  | 1 x SSD SATA de 480Go (6Gbit/s) | | |
| 93    | 64    | 498G ou 510000M    | 1 x SSD NVMe de 3.84To | 2 x [Intel Xeon Gold 6448Y](https://ark.intel.com/content/www/us/en/ark/products/232384/intel-xeon-gold-6448y-processor-60m-cache-2-10-ghz.html) @ 2.10 GHz, cache L3 de 60Mo | 4 x NVidia H100 SXM5 (mémoire 80Go), connectés via NVLink |

*   Pour obtenir un plus grand espace `$SLURM_TMPDIR`, il faut demander `--tmp=xG`, où `x` est une valeur entre 370 et 3360.

### Topologie des nœuds CPU

Dans un nœud CPU, les 192 cœurs et les différents espaces mémoire ne sont pas équidistants, ce qui cause des délais variables (de l'ordre du nanoseconde) pour accéder aux données. Dans chaque nœud, on a :

*   Deux (2) prises CPU (*sockets*) ayant chacune 12 canaux de mémoire système.
    *   Quatre (4) *nœuds* [NUMA](https://fr.wikipedia.org/wiki/Non_uniform_memory_access) par prise CPU, chacun étant connecté à trois (3) canaux de mémoire système.
        *   Trois (3) *chiplets* par *nœud NUMA*, chacun ayant sa propre [mémoire cache L3](https://fr.wikipedia.org/wiki/Cache_de_processeur) de 32 Mio.
            *   Huit (8) cœurs par *chiplet*, chacun ayant sa propre mémoire cache L2 de 1 Mio et L1 de 32+32 Kio.

Autrement dit, on a :
*   Des groupes de 8 cœurs rapprochés qui se partagent une même mémoire cache L3, ce qui est idéal pour des [programmes parallèles multifils](running-jobs.md#tache-multifil-ou-tache-openmp) (par exemple, avec l'option `--cpus-per-task=8`)
*   Des *nœuds NUMA* de 3×8 = 24 cœurs qui se partagent un trio de canaux de mémoire système.
*   Un total de 2×4×3×8 = 192 cœurs par nœud.

Pour profiter pleinement des avantages de cette topologie, il faut réserver des nœuds complets (par exemple, avec `--ntasks-per-node=24 --cpus-per-task=8`) et contrôler explicitement l'emplacement des processus et des fils d'exécution. Selon le programme parallèle et le nombre de cœurs utilisés, les gains peuvent être marginaux ou significatifs.

### Topologie des nœuds GPU

Dans les nœuds GPU, l'architecture est moins hiérarchique. On a :

*   Deux (2) prises CPU (*sockets*). Pour chacune, on a :
    *   Huit (8) canaux de mémoire système
    *   60 Mio de mémoire cache L3
    *   32 cœurs équidistants ayant chacun sa propre mémoire cache L2 de 2 Mio et L1 de 32+48 Kio.
    *   Deux (2) accélérateurs NVidia H100

Au total, les quatre (4) accélérateurs du nœud sont interconnectés par [SXM5](https://en.wikipedia.org/wiki/SXM_(socket)).

### Instances GPU

Les différents noms d'instances GPU disponibles sur Rorqual sont :

| **Modèle ou instance** | Nom court | Sans unité | Par sa mémoire | Nom complet |
| :--------------------- | :-------- | :--------- | :------------- | :---------- |
| **GPU** | **H100-80gb** | `h100` | `h100` | `h100_80gb` | `nvidia_h100_80gb_hbm3` |
| **MIG** | **H100-1g.10gb** | `h100_1g.10gb` | `h100_1.10` | `h100_10gb` | `nvidia_h100_80gb_hbm3_1g.10gb` |
| | **H100-2g.20gb** | `h100_2g.20gb` | `h100_2.20` | `h100_20gb` | `nvidia_h100_80gb_hbm3_2g.20gb` |
| | **H100-3g.40gb** | `h100_3g.40gb` | `h100_3.40` | `h100_40gb` | `nvidia_h100_80gb_hbm3_3g.40gb` |

Pour demander un ou plusieurs GPU H100 complets, il faut utiliser une des options Slurm suivantes :
*   **Un H100-80gb** : `--gpus=h100:1` ou `--gpus=h100_80gb:1`
*   **Plusieurs H100-80gb** par nœud :
    *   `--gpus-per-node=h100:2`
    *   `--gpus-per-node=h100:3`
    *   `--gpus-per-node=h100:4`
*   **Plusieurs H100-80gb** éparpillés n'importe où : `--gpus=h100:n` (remplacer `n` par le nombre voulu)

Environ la moitié des nœuds GPU de Rorqual sont configurés avec la [technologie MIG](multi-instance-gpu.md) et seulement trois tailles d'instances GPU sont disponibles :

*   **H100-1g.10gb** : 1/8 de la puissance de calcul avec 10 Go de mémoire GPU.
*   **H100-2g.20gb** : 2/8 de la puissance de calcul avec 20 Go de mémoire GPU.
*   **H100-3g.40gb** : 3/8 de la puissance de calcul avec 40 Go de mémoire GPU.

Pour demander **une et une seule** instance GPU pour votre tâche de calcul, voici les options correspondantes :

*   **H100-1g.10gb** : `--gpus=h100_1g.10gb:1`
*   **H100-2g.20gb** : `--gpus=h100_2g.20gb:1`
*   **H100-3g.40gb** : `--gpus=h100_3g.40gb:1`

Les quantités maximales recommandées de **cœurs CPU et de mémoire système** par instance GPU sont listées dans la [table des caractéristiques des *bundles*](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).