---
title: "Graham/fr"
slug: "graham"
lang: "fr"

source_wiki_title: "Graham/fr"
source_hash: "05ceb584c66e63061cb3ec8484e6c37e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:06:35.587271+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

!!! warning "Attention"
    Graham a été remplacée par une nouvelle grappe nommée [Nibi](nibi.md). Pendant la période de transition, les informations sur la capacité de chacun des systèmes ainsi que les arrêts ou les réductions de service seront disponibles sur la page [Renouvellement de l'infrastructure](infrastructure_renewal.md).

| Clé                      | Valeur                                                                  |
| :----------------------- | :---------------------------------------------------------------------- |
| Disponibilité            | depuis 2017                                                             |
| Nœud de connexion        | **graham.alliancecan.ca**                                               |
| Collection Globus        | **computecanada#graham-globus**                                         |
| Nœud de copie (rsync, scp, sftp, etc.) | utilisez un nœud de connexion ou le nœud robot                      |

Graham est un système hétérogène adapté pour une grande variété de types de tâches; il est situé à l'Université de Waterloo. Son nom rappelle [Wes Graham](https://en.wikipedia.org/wiki/Wes_Graham), premier directeur du *Computing Centre* de l'Université de Waterloo.

Les systèmes de fichiers parallèles et le stockage persistant (souvent nommé NDC-Waterloo) sont semblables à ceux de [Cedar](cedar.md). L'interconnexion n'est pas la même et il y a des proportions différentes du nombre de chaque type de nœuds de calcul.

Un système de refroidissement liquide utilise des échangeurs de chaleur à même les portes arrière.

[Introduction à Graham](getting_started.md)

[Exécuter des tâches](running_jobs.md)

[Transférer des données](transferring_data.md)

## Particularités

*   Selon notre politique, les nœuds de calcul de Graham n'ont pas accès à l'internet. Pour y faire exception, contactez le [soutien technique](technical_support.md) avec les renseignements suivants:

    ```text
    Adresse IP :
    Port(s) :
    Protocole :  TCP ou UDP
    Contact :
    Date de fin :
    ```

    Avant de mettre fin au lien internet, nous communiquerons avec la personne-ressource pour vérifier si la règle est toujours nécessaire.

*   Crontab n'est pas offert sur Graham.
*   Une tâche devrait avoir une durée minimum d'une heure et un maximum de 168 heures (sept jours). Pour une tâche de test, le minimum est de cinq minutes.
*   Le total des tâches en exécution et en attente au même moment ne peut dépasser 1000. Dans le cas d'un lot de tâches (*array job*), chacune est comptée individuellement.

## Stockage

| Type d'espace                      | Détails                                                                                                                                                                                                                                                                                                                                       |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **espace /home**                   | * localisation des répertoires /home<br/>* chaque répertoire /home a un petit [quota](storage_and_file_management.md#quotas-et-politiques) fixe<br/>* non alloué via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours d'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources); le stockage de grande envergure se fait sur l'espace /project<br/>* est sauvegardé chaque jour |
| Volume total de 133To              |                                                                                                                                                                                                                                                                                                                                               |
| **espace /scratch**                | * stockage /scratch actif ou temporaire<br/>* non alloué<br/>* grand [quota](storage_and_file_management.md#quotas-et-politiques) fixe, par utilisateur<br/>* les données inactives sont purgées                                                                                                                                                 |
| Volume total de 3.2Po              |                                                                                                                                                                                                                                                                                                                                               |
| Système de fichiers parallèle de haute performance |                                                                                                                                                                                                                                                                                                                                               |
| **espace /project**                | * allocations via le [service d'accès rapide](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/service-dacces-rapide) ou le [concours d'allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources)<br/>* ne convient pas aux tâches d'écriture et de lecture en parallèle; utiliser l'espace /scratch<br/>* grand [quota](storage_and_file_management.md#quotas-et-politiques) ajustable par projet<br/>* est sauvegardé chaque jour |
| Volume total de 16Po               |                                                                                                                                                                                                                                                                                                                                               |
| Stockage persistant externe        |                                                                                                                                                                                                                                                                                                                                               |

## Interconnexion haute performance

Interconnexion InfiniBand Mellanox FDR (56Go/s.) et EDR (100Go/s.). FDR sert aux nœuds GPU et aux nœuds infonuagiques; tous les autres types de nœuds utilisent EDR. Un répartiteur (*director switch*) central de 324 ports rassemble les connexions des ilots CPU et GPU de 1024 cœurs. Les 56 nœuds infonuagiques se situent sur les nœuds CPU; ils sont regroupés sur un plus grand ilot et partagent 8 liens FDR vers le répartiteur.

Une interconnexion non bloquante (*InfiniBand fabric*) à haute bande passante et faible latence connecte tous les nœuds et le stockage /scratch.

Les nœuds configurés pour le service infonuagique possèdent aussi un réseau Ethernet 10Go/s. et des liens de 40Go/s. vers le stockage /scratch.

L'architecture de Graham a été planifiée pour supporter de multiples tâches parallèles jusqu'à 1024 cœurs grâce à une réseautique non bloquante.

Pour les tâches plus imposantes, le facteur de blocage est de 8:1; même pour les tâches exécutées sur plusieurs ilots, l'interconnexion est de haute performance.

[Diagramme des interconnexions pour Graham](https://docs.computecanada.ca/mediawiki/images/b/b3/Gp3-network-topo.png)

## Visualisation

Graham offre des nœuds dédiés pour la visualisation qui permettent uniquement les connexions VNC (**gra-vdi.alliancecan.ca**). Pour l'information sur comment les utiliser, voyez la page [VNC](vnc.md).

## Caractéristiques des nœuds

Au début de 2025, la capacité de Graham a été réduite pour que nous puissions installer le nouveau système Nibi. Le tableau suivant montre les nœuds qui sont disponibles à compter de février 2025.

Tous les nœuds de Graham sont dotés de la fonctionnalité [Turbo Boost](https://en.wikipedia.org/wiki/Intel_Turbo_Boost).

| nœuds | cœurs | mémoire disponible | CPU                                       | stockage      | GPU                                       |
| :---- | :---- | :----------------- | :---------------------------------------- | :------------ | :---------------------------------------- |
| 2     | 40    | 377G ou 386048M    | 2 x Intel Xeon Gold 6248 Cascade Lake @ 2.5GHz | 5.0TB NVMe SSD | 8 x NVIDIA V100 Volta (mémoire 32GB HBM2), NVLINK |
| 6     | 16    | 187G ou 191840M    | 2 x Intel Xeon Silver 4110 Skylake @ 2.10GHz | 11.0TB SATA SSD | 4 x NVIDIA T4 Turing (mémoire 16Go GDDR6) |
| 30    | 44    | 187G ou 191840M    | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10GHz | 5.8TB NVMe SSD | 4 x NVIDIA T4 Turing (mémoire 16Go GDDR6) |
| 136   | 44    | 187G ou 191840M    | 2 x Intel Xeon Gold 6238 Cascade Lake @ 2.10GHz | 879GB SATA SSD | -                                         |
| 1     | 128   | 2000G ou 2048000M  | 2 x AMD EPYC 7742                         | 3.5TB SATA SSD | 8 x NVIDIA A100 Ampere                    |
| 2     | 32    | 256G ou 262144M    | 2 x Intel Xeon Gold 6326 Cascade Lake @ 2.90GHz | 3.5TB SATA SSD | 4 x NVIDIA A100 Ampere                    |
| 11    | 64    | 128G ou 131072M    | 1 x AMD EPYC 7713                         | 1.8TB SATA SSD | 4 x NVIDIA RTX A5000 Ampere               |
| 6     | 32    | 1024G ou 1048576M  | 1 x AMD EPYC 7543                         | 8x2TB NVMe     | -                                         |

La plupart des applications fonctionneront soit avec des nœuds Broadwell, Skylake ou Cascade Lake et les différences en termes de performance devraient être minimes à comparer avec les temps d'attente. Nous recommandons donc de ne pas sélectionner un type de nœud particulier pour vos tâches. Si nécessaire, pour les tâches qui doivent être exécutées avec un CPU Cascade Lake, utilisez `--constraint=cascade` (voir [comment spécifier l'architecture CPU](running_jobs.md#particularites-de-certaines-grappes)).

Pour le stockage local sur nœud, il est recommandé d'utiliser le répertoire temporaire `$SLURM_TMPDIR` généré par [Slurm](running_jobs.md). Ce répertoire avec son contenu est supprimé à la fin de l'exécution de la tâche.

Remarquez que la quantité de mémoire disponible est moindre que la valeur arrondie suggérée par la configuration matérielle. Par exemple, les nœuds de type base 128G ont effectivement 128Gio de mémoire vive, mais une certaine quantité est utilisée en permanence par le noyau (*kernel*) et le système d'exploitation. Pour éviter la perte de temps encourue par le *swapping* ou le *paging*, l'ordonnanceur n'allouera jamais une tâche dont les exigences dépassent la quantité de mémoire disponible indiquée dans le tableau ci-dessus.
Notez aussi que la mémoire allouée pour la tâche doit être suffisante pour les lectures et écritures dans la mémoire tampon qui sont effectuées par le noyau et le système de fichiers; lorsque ces opérations sont nombreuses, il est préférable de demander plus de mémoire que la quantité totale requise par les processus.

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

**Les nœuds sont disponibles à tous les utilisateurs pour des durées d'exécution maximales de 7 jours**.

Dans l'exemple suivant, le script soumet une tâche pour un des nœuds de 8 GPU. La commande `module load` fait en sorte que les modules compilés pour l'architecture Skylake soient utilisés. Remplacez *nvidia-smi* par la commande que vous voulez lancer.

!!! attention "Important"
    Déterminez le nombre de CPU à demander en appliquant un ratio CPU/GPU de 3.5 ou moins sur des nœuds de 28 cœurs. Par exemple, si votre tâche doit utiliser 4 GPU, vous devriez demander **au plus 14 cœurs CPU** et pour utiliser 1 GPU, demander **au plus 3 cœurs CPU**. Les utilisateurs peuvent faire exécuter quelques tâches de test de moins d'une heure pour connaître le niveau de performance du code.

Les deux plus récents nœuds Volta ont 40 cœurs et le nombre de cœurs par GPU demandé doit être ajusté à la hausse selon le cas; une tâche peut par exemple utiliser 5 cœurs CPU par GPU. Ces nœuds sont aussi interconnectés. Si vous voulez utiliser un de ces nœuds, il faut ajouter au script de soumission de la tâche le paramètre `constraint=cascade,v100`.

Exemple avec un seul GPU

```bash title="gpu_single_GPU_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=3
#SBATCH --mem=12G
#SBATCH --time=1-00:00
module load arch/avx512 StdEnv/2018.3
nvidia-smi
```

Exemple avec un nœud entier

```bash title="gpu_single_node_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:8
#SBATCH --exclusive
#SBATCH --cpus-per-task=28
#SBATCH --mem=150G
#SBATCH --time=1-00:00
module load StdEnv/2023
nvidia-smi
```

Les nœuds Volta de Graham ont un disque local rapide qui devrait être utilisé si la tâche exige beaucoup d'opérations I/O. Dans la tâche, la variable d'environnement `$SLURM_TMPDIR` donne la localisation du répertoire temporaire sur le disque. Vous pouvez y copier vos fichiers de données au début du script avant d'exécuter le programme, et y copier vos fichiers de sortie à la fin du script. Comme tous les fichiers contenus dans `$SLURM_TMPDIR` sont supprimés quand la tâche est terminée, vous n'avez pas à le faire. Vous pouvez même [créer des environnements virtuels Python](python.md#creer-un-environnement-virtuel-dans-vos-taches) dans cet espace temporaire pour améliorer l'efficacité.

### Nœuds GPU Turing

Ces nœuds s'utilisent comme les nœuds Volta, sauf que vous devriez les demander en indiquant

`--gres=gpu:t4:2`

Dans cet exemple, on demande deux cartes T4 par nœud.

### Nœuds GPU Ampere

L'utilisation de ces nœuds est semblable à celle des nœuds Volta, sauf que pour les obtenir, il faut spécifier

`--gres=gpu:a100:2`

ou

`--gres=gpu:a5000:2`

Dans cet exemple, on demande deux cartes Ampere par nœud.

## Réduction de la capacité

À compter du 13 janvier 2025, la capacité de Graham sera limitée à environ 25% jusqu'à ce que [Nibi](nibi.md) soit disponible.