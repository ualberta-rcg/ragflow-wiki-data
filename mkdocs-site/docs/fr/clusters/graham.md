---
title: "Graham/fr"
slug: "graham"
lang: "fr"

source_wiki_title: "Graham/fr"
source_hash: "05ceb584c66e63061cb3ec8484e6c37e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:47:38.624630+00:00"

tags:
  []

keywords:
  - "Stockage persistant externe"
  - "Nœuds GPU"
  - "nœuds Volta"
  - "Slurm"
  - "allocations"
  - "interconnexion haute performance"
  - "cœurs CPU par GPU"
  - "architecture CPU"
  - "caractéristiques des nœuds"
  - "nœuds GPU"
  - "Volume total de 16Po"
  - "concours d'allocation de ressources"
  - "stockage"
  - "exécution de tâches"
  - "nœuds de calcul"
  - "mémoire disponible"
  - "SATA SSD"
  - "NVIDIA A100 Ampere"
  - "script de soumission"
  - "tâches de test"
  - "Ampere"
  - "Intel Xeon Gold"
  - "$SLURM_TMPDIR"
  - "AMD EPYC"
  - "Graham"
  - "InfiniBand"
  - "NVMe"
  - "Nibi"
  - "performance du code"
  - "V100 Volta"
  - "Volta"
  - "service d'accès rapide"

questions:
  - "Par quel nouveau système la grappe Graham a-t-elle été remplacée et où peut-on trouver les informations durant cette transition ?"
  - "Quelles sont les règles et restrictions spécifiques concernant l'exécution des tâches et l'accès à internet sur les nœuds de calcul de Graham ?"
  - "Quels sont les trois différents espaces de stockage offerts sur le système et quelles sont leurs caractéristiques principales ?"
  - "Quel est le volume total de stockage disponible pour ce projet ?"
  - "Quelle est la nature du stockage informatique mentionné dans le texte ?"
  - "Par quels moyens peut-on obtenir des allocations pour accéder à ces ressources ?"
  - "Comment l'architecture du réseau d'interconnexion de Graham est-elle structurée pour assurer de hautes performances lors de l'exécution de tâches parallèles ?"
  - "Quelle est la méthode spécifique requise pour accéder aux nœuds dédiés à la visualisation sur le système ?"
  - "Quelles sont les principales caractéristiques matérielles des nœuds disponibles sur Graham suite à la réduction de sa capacité en février 2025 ?"
  - "Quelles sont les recommandations concernant l'utilisation du stockage local et l'allocation de la mémoire vive pour optimiser l'exécution des tâches ?"
  - "Quelles sont les caractéristiques et les différences de performance entre les générations de GPU actuellement en service (V100, T4, A100) ?"
  - "Quelles sont les règles spécifiques à respecter concernant le ratio de cœurs CPU par GPU lors de la soumission d'une tâche sur les nœuds Volta ?"
  - "Quelles sont les différentes configurations de cartes graphiques (GPU) NVIDIA disponibles parmi ces serveurs ?"
  - "Quels modèles de processeurs (CPU) AMD et Intel équipent ces différentes machines ?"
  - "Quelles sont les capacités de mémoire vive (RAM) et les options de stockage (SATA ou NVMe) proposées dans cette liste ?"
  - "Comment doit-on configurer les paramètres d'un script Slurm pour demander différents types ou quantités de GPU (Volta, Turing, Ampere) ?"
  - "Comment la variable d'environnement $SLURM_TMPDIR permet-elle d'optimiser les tâches nécessitant beaucoup d'opérations d'entrée/sortie sur les nœuds Volta ?"
  - "Quel événement affectera la capacité de calcul de la grappe Graham à partir du 13 janvier 2025 ?"
  - "Quel est l'objectif principal des tâches de test de moins d'une heure ?"
  - "Comment le nombre de cœurs CPU par GPU doit-il être ajusté lors de l'utilisation des récents nœuds Volta à 40 cœurs ?"
  - "Quel paramètre exact doit être ajouté au script de soumission pour pouvoir utiliser ces nœuds spécifiques ?"
  - "Comment doit-on configurer les paramètres d'un script Slurm pour demander différents types ou quantités de GPU (Volta, Turing, Ampere) ?"
  - "Comment la variable d'environnement $SLURM_TMPDIR permet-elle d'optimiser les tâches nécessitant beaucoup d'opérations d'entrée/sortie sur les nœuds Volta ?"
  - "Quel événement affectera la capacité de calcul de la grappe Graham à partir du 13 janvier 2025 ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Attention"
    Graham a été remplacée par une nouvelle grappe nommée [Nibi](nibi.md). Pendant la période de transition, les informations sur la capacité de chacun des systèmes ainsi que les arrêts ou les réductions de service seront disponibles sur la page [Renouvellement de l'infrastructure](infrastructure-renewal.md).

| Caractéristique                   | Valeur                                                              |
| :-------------------------------- | :------------------------------------------------------------------ |
| Disponibilité                     | depuis 2017                                                         |
| Nœud de connexion                 | **graham.alliancecan.ca**                                           |
| Collection Globus                 | **computecanada#graham-globus**                                     |
| Nœud de copie (rsync, scp, sftp, etc.) | Utilisez un nœud de connexion ou le nœud robot                    |

Graham est un système hétérogène adapté pour une grande variété de types de tâches; il est situé à l'Université de Waterloo. Son nom rappelle [Wes Graham](https://en.wikipedia.org/wiki/Wes_Graham), premier directeur du *Computing Centre* de l'Université de Waterloo.

Les systèmes de fichiers parallèles et le stockage persistant (souvent nommé NDC-Waterloo) sont semblables à ceux de [Cedar](cedar.md). L'interconnexion n'est pas la même et il y a des proportions différentes du nombre de chaque type de nœuds de calcul.

Un système de refroidissement liquide utilise des échangeurs de chaleur à même les portes arrière.

*   [Introduction à Graham](getting-started.md)
*   [Exécuter des tâches](running-jobs.md)
*   [Transférer des données](transferring-data.md)

## Particularités

*   Selon notre politique, les nœuds de calcul de Graham n'ont pas accès à l'internet. Pour y faire exception, contactez le [soutien technique](technical-support.md) avec les renseignements suivants:

```
Adresse IP :
Port(s) :
Protocole : TCP ou UDP
Contact :
Date de fin :
```

Avant de mettre fin au lien internet, nous communiquerons avec la personne-ressource pour vérifier si la règle est toujours nécessaire.

*   Crontab n'est pas offert sur Graham.
*   Une tâche devrait avoir une durée minimale d'une heure et un maximum de 168 heures (sept jours). Pour une tâche de test, le minimum est de cinq minutes.
*   Le total des tâches en exécution et en attente au même moment ne peut dépasser 1000. Dans le cas d'un lot de tâches (*array job*), chacune est comptée individuellement.

## Stockage

| Espace de stockage    | Caractéristiques                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **espace /home**<br>Volume total de 133 To | * localisation des répertoires /home<br>* chaque répertoire /home a un petit [quota](storage-and-file-management.md#quotas-et-politiques) fixe<br>* non alloué via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours d'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources); le stockage de grande envergure se fait sur l'espace /project<br>* est sauvegardé chaque jour |
| **espace /scratch**<br>Volume total de 3.2 Po<br>Système de fichiers parallèle de haute performance | * stockage /scratch actif ou temporaire<br>* non alloué<br>* grand [quota](storage-and-file-management.md#quotas-et-politiques) fixe, par utilisateur<br>* les données inactives sont purgées                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **espace /project**<br>Volume total de 16 Po<br>Stockage persistant externe | * allocations via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours d'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources)<br>* ne convient pas aux tâches d'écriture et de lecture en parallèle; utiliser l'espace /scratch<br>* grand [quota](storage-and-file-management.md#quotas-et-politiques) ajustable par projet<br>* est sauvegardé chaque jour |

## Interconnexion haute performance

Interconnexion InfiniBand Mellanox FDR (56 Go/s) et EDR (100 Go/s). FDR sert aux nœuds GPU et aux nœuds infonuagiques; tous les autres types de nœuds utilisent EDR. Un répartiteur (*director switch*) central de 324 ports rassemble les connexions des îlots CPU et GPU de 1024 cœurs. Les 56 nœuds infonuagiques se situent sur les nœuds CPU; ils sont regroupés sur un plus grand îlot et partagent 8 liens FDR vers le répartiteur.

Une interconnexion non bloquante (*InfiniBand fabric*) à haute bande passante et faible latence connecte tous les nœuds et le stockage /scratch.

Les nœuds configurés pour le service infonuagique possèdent aussi un réseau Ethernet 10 Go/s et des liens de 40 Go/s vers le stockage /scratch.

L'architecture de Graham a été planifiée pour supporter de multiples tâches parallèles jusqu'à 1024 cœurs grâce à une réseautique non bloquante.

Pour les tâches plus imposantes, le facteur de blocage est de 8:1; même pour les tâches exécutées sur plusieurs îlots, l'interconnexion est de haute performance.

[Diagramme des interconnexions pour Graham](https://docs.computecanada.ca/mediawiki/images/b/b3/Gp3-network-topo.png)

## Visualisation

Graham offre des nœuds dédiés pour la visualisation qui permettent uniquement les connexions VNC (**gra-vdi.alliancecan.ca**). Pour l'information sur comment les utiliser, voyez la page [VNC](vnc.md).

## Caractéristiques des nœuds

Au début de 2025, la capacité de Graham a été réduite pour que nous puissions installer le nouveau système Nibi. Le tableau suivant montre les nœuds qui sont disponibles à compter de février 2025.

Tous les nœuds de Graham sont dotés de la fonctionnalité [Turbo Boost](https://en.wikipedia.org/wiki/Intel_Turbo_Boost).

| Nœuds | Cœurs | Mémoire disponible | CPU | Stockage | GPU |
| :---- | :---- | :----------------- | :-- | :------- | :-- |
| 2 | 40 | 377 Go ou 386048 Mo | 2 x Intel Xeon Gold 6248 Cascade Lake @ 2.5 GHz | 5.0 To NVMe SSD | 8 x NVIDIA V100 Volta (mémoire 32 Go HBM2), NVLINK |
| 6 | 16 | 187 Go ou 191840 Mo | 2 x Intel Xeon Silver 4110 Skylake @ 2.10 GHz | 11.0 To SATA SSD | 4 x NVIDIA T4 Turing (mémoire 16 Go GDDR6) |
| 30 | 44 | 187 Go ou 191840 Mo | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10 GHz | 5.8 To NVMe SSD | 4 x NVIDIA T4 Turing (mémoire 16 Go GDDR6) |
| 136 | 44 | 187 Go ou 191840 Mo | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10 GHz | 879 Go SATA SSD | - |
| 1 | 128 | 2000 Go ou 2048000 Mo | 2 x AMD EPYC 7742 | 3.5 To SATA SSD | 8 x NVIDIA A100 Ampere |
| 2 | 32 | 256 Go ou 262144 Mo | 2 x Intel Xeon Gold 6326 Cascade Lake @ 2.90 GHz | 3.5 To SATA SSD | 4 x NVIDIA A100 Ampere |
| 11 | 64 | 128 Go ou 131072 Mo | 1 x AMD EPYC 7713 | 1.8 To SATA SSD | 4 x NVIDIA RTX A5000 Ampere |
| 6 | 32 | 1024 Go ou 1048576 Mo | 1 x AMD EPYC 7543 | 8x2 To NVMe | - |

La plupart des applications fonctionneront soit avec des nœuds Broadwell, Skylake ou Cascade Lake et les différences en termes de performance devraient être minimes à comparer avec les temps d'attente. Nous recommandons donc de ne pas sélectionner un type de nœud particulier pour vos tâches. Si nécessaire, pour les tâches qui doivent être exécutées avec un CPU Cascade Lake, utilisez `--constraint=cascade` (voir [comment spécifier l'architecture CPU](running-jobs.md#particularites-de-certaines-grappes)).

Pour le stockage local sur nœud, il est recommandé d'utiliser le répertoire temporaire `$SLURM_TMPDIR` généré par [Slurm](running-jobs.md). Ce répertoire avec son contenu est supprimé à la fin de l'exécution de la tâche.

Remarquez que la quantité de mémoire disponible est moindre que la valeur arrondie suggérée par la configuration matérielle. Par exemple, les nœuds de type base 128 Go ont effectivement 128 Go de mémoire vive, mais une certaine quantité est utilisée en permanence par le noyau (*kernel*) et le système d'exploitation. Pour éviter la perte de temps encourue par le *swapping* ou le *paging*, l'ordonnanceur n'allouera jamais une tâche dont les exigences dépassent la quantité de mémoire disponible indiquée dans le tableau ci-dessus. Notez aussi que la mémoire allouée pour la tâche doit être suffisante pour les lectures et écritures dans la mémoire tampon qui sont effectuées par le noyau et le système de fichiers; lorsque ces opérations sont nombreuses, il est préférable de demander plus de mémoire que la quantité totale requise par les processus.

## GPU

Les trois générations de GPU Tesla, de la plus ancienne à la plus récente, sont :

*   V100 Volta (deux nœuds avec interconnexion NVLINK)
*   GPU Turing Ts4
*   A100 Ampere

Les GPU P100 ne sont plus en service. V100 leur succède et offrent deux fois plus de performance pour les calculs standards et huit fois plus de performance pour les calculs en apprentissage profond qui peuvent utiliser ses unités de calcul avec cœurs Tensor. La carte T4 plus récente est adaptée aux tâches d'apprentissage profond; elle n'est pas efficace pour les calculs double précision, mais sa performance en simple précision est bonne; elle possède aussi des cœurs Tensor et peut traiter les calculs à précision réduite avec les entiers.

### Nœuds GPU Pascal

Ne sont plus en service.

### Nœuds GPU Volta

Graham a deux nœuds GPU Volta au total qui ont une interconnexion NVLINK à large bande passante.

**Les nœuds sont disponibles à tous les utilisateurs pour des durées d'exécution maximales de 7 jours.**

Dans l'exemple suivant, le script soumet une tâche pour un des nœuds de 8 GPU. La commande `module load` fait en sorte que les modules compilés pour l'architecture Skylake soient utilisés. Remplacez *nvidia-smi* par la commande que vous voulez lancer.

!!! important "Important"
    Déterminez le nombre de CPU à demander en appliquant un ratio CPU/GPU de 3.5 ou moins sur des nœuds de 28 cœurs. Par exemple, si votre tâche doit utiliser 4 GPU, vous devriez demander **au plus 14 cœurs CPU** et pour utiliser 1 GPU, demander **au plus 3 cœurs CPU**. Les utilisateurs peuvent faire exécuter quelques tâches de test de moins d'une heure pour connaître le niveau de performance du code.

Les deux plus récents nœuds Volta ont 40 cœurs et le nombre de cœurs par GPU demandé doit être ajusté à la hausse selon le cas; une tâche peut par exemple utiliser 5 cœurs CPU par GPU. Ces nœuds sont aussi interconnectés. Si vous voulez utiliser un de ces nœuds, il faut ajouter au script de soumission de la tâche le paramètre `constraint=cascade,v100`.

Exemple avec un seul GPU
```sh: gpu_single_GPU_job.sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=3
#SBATCH --mem=12Go
#SBATCH --time=1-00:00
module load arch/avx512 StdEnv/2018.3
nvidia-smi
```

Exemple avec un nœud entier
```sh: gpu_single_node_job.sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:8
#SBATCH --exclusive
#SBATCH --cpus-per-task=28
#SBATCH --mem=150Go
#SBATCH --time=1-00:00
module load StdEnv/2023
nvidia-smi
```

Les nœuds Volta de Graham ont un disque local rapide qui devrait être utilisé si la tâche exige beaucoup d'opérations E/S (I/O). Dans la tâche, la variable d'environnement `$SLURM_TMPDIR` donne la localisation du répertoire temporaire sur le disque. Vous pouvez y copier vos fichiers de données au début du script avant d'exécuter le programme, et y copier vos fichiers de sortie à la fin du script. Comme tous les fichiers contenus dans `$SLURM_TMPDIR` sont supprimés quand la tâche est terminée, vous n'avez pas à le faire. Vous pouvez même [créer des environnements virtuels Python](python.md#creer-un-environnement-virtuel-dans-vos-taches) dans cet espace temporaire pour améliorer l'efficacité.

### Nœuds GPU Turing

Ces nœuds s'utilisent comme les nœuds Volta, sauf que vous devriez les demander en indiquant :
` --gres=gpu:t4:2`
Dans cet exemple, on demande deux cartes T4 par nœud.

### Nœuds GPU Ampere

L'utilisation de ces nœuds est semblable à celle des nœuds Volta, sauf que pour les obtenir, il faut spécifier :
` --gres=gpu:a100:2`
ou
` --gres=gpu:a5000:2`
Dans cet exemple, on demande deux cartes Ampere par nœud.

## Réduction de la capacité

À compter du 13 janvier 2025, la capacité de Graham sera limitée à environ 25% jusqu'à ce que [Nibi](nibi.md) soit disponible.