---
title: "Fir/fr"
slug: "fir"
lang: "fr"

source_wiki_title: "Fir/fr"
source_hash: "893e0c21377515e6121b334f96ead34a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:21:25.355842+00:00"

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

| Disponibilité | 11 août 2025 |
| :------------ | :--------------------------------------------------------------------------------------------------------------------- |
| Nœud de connexion | `fir.alliancecan.ca` |
| Nœud d'automatisation | `robot.fir.alliancecan.ca` |
| Collection Globus | [*alliancecan#fir-globus*](https://globus.alliancecan.ca/file-manager?origin_id=8dec4129-9ab4-451d-a45f-5b4b8471f7a3&two_pane=false) |
| JupyterHub | [jupyterhub.fir.alliancecan.ca](https://jupyterhub.fir.alliancecan.ca/) |
| Nœud de copie (rsync, scp, sftp ...) | *à déterminer* |
| Portail | *à déterminer* |

Fir est une grappe de calcul polyvalente et hétérogène, développée en partenariat avec Lenovo Canada et Data Direct Networks (DDN). Elle est conçue pour prendre en charge un large éventail de calculs scientifiques. Hébergée à l'Université Simon-Fraser à Burnaby en Colombie-Britannique, elle doit son nom au sapin de Douglas le plus volumineux au Canada qui se trouve près de Red Creek, sur l'île de Vancouver.

## À propos de Fir

L'Université Simon-Fraser maintient son engagement en faveur d'un calcul haute performance respectueux de l'environnement. Avec Fir, l'Université passe du refroidissement par air traditionnel au refroidissement liquide direct sur puce, améliorant ainsi considérablement l'efficacité énergétique et réduisant la consommation d'énergie associée au refroidissement.

Le nouveau réseau InfiniBand haut débit offre des performances plus de deux fois supérieures à celles de la grappe Cedar de la génération précédente.

Fir est actuellement classée 78<sup>e</sup> au [TOP500](https://top500.org/lists/top500/list/2025/06/) des supercalculateurs les plus puissants au monde.

## Permission d'accès

Connectez-vous au portail CCDB et cliquez sur *Ressources --> Accès aux systèmes*.

Dans la liste de gauche, sélectionnez Fir.

Sélectionnez *Je demande d'accès*.

L'activation de votre accès pourrait prendre environ une heure.

## Politiques particulières

Les nœuds de calcul ont plein accès à l'internet.

L'outil `crontab` n'est pas supporté.

Une tâche doit être d'une durée d'au moins une heure et d'au moins cinq minutes pour une tâche de test. La durée maximale est de sept jours (168 heures).

Pour transférer des données via Globus, utilisez une des adresses indiquées au haut de la page. Pour les outils comme rsync et scp, utilisez le nœud de connexion.

## Stockage

51PB de stockage DDN Lustre haute performance (2PB NVME / 49 SAS).

!!! note
    Tous les éléments montés partagent l’espace de stockage disponible.

| Storage Area | Access Path | Quotas | Backup | Notes |
| :----------- | :---------- | :----- | :----- | :---- |
| **HOME** | (par défaut) `$HOME` | petit quota par utilisateur | sauvegarde automatique une fois par jour | Cet espace ne peut pas être agrandi. Utilisez votre espace `project` pour les grands besoins en stockage. |
| **SCRATCH** | `$HOME/scratch` | grand quota par utilisateur | pas de sauvegarde | Cet espace est conçu pour les fichiers temporaires. Les anciens fichiers sont automatiquement purgés. |
| **PROJECT** | `$HOME/project/${def-project-id}` | grand quota ajustable par projet | sauvegarde une fois par jour | Cet espace est conçu pour le partage de données entre membres d'un groupe et pour le stockage de beaucoup de données. |

## Réseautique haute performance

*   réseau InfiniBand NDR
*   taille des îlots de nœuds CPU : 216 nœuds de 192 cœurs, facteur de blocage 27:5
*   nœuds GPU : facteur de blocage 2:1
*   accès au stockage non bloquant

## Caractéristiques des nœuds

| nœuds | cœurs | mémoire disponible | CPU | Stockage | GPU |
| :---- | :---- | :----------------- | :-- | :------- | :-- |
| 864 | 192 | 750G ou 768000M | 2 x AMD EPYC 9655 (Zen 5) @ 2.7 GHz, cache L3 de 384MB | NVMe,7.84TB | |
| 8 | 192 | 6000G ou 6144000M | 2 x AMD EPYC 9654 (Zen 4) @ 2.4 GHz, cache L3 de 384MB | NVMe,7.84TB | |
| 160 | 48 | 1125G ou 1152000M | 1 x AMD EPYC 9454 (Zen 4) @ 2.75 GHz, cache L3 de 256MB | NVMe,7.84TB | 4 x NVidia H100 SXM5 (mémoire de 80GB), connexion via NVLink |

## Nœuds CPU

### Architecture

Chaque nœud est composé de 2 processeurs AMD EPYC 9655 (Zen 5) @ 2.7GHz avec un total de 192 cœurs physiques. L’architecture NUMA est basée sur des puces fragmentées (*chiplets*), chacune fonctionnant comme un nœud NUMA distinct. La hiérarchie de la mémoire et de la cache est non uniforme et la performance dépend de la localité des données.

### Configuration

*   2 sockets avec chacun
    *   **96 cœurs**
    *   **4 nœuds NUMA** avec chacun
        *   **3 CCDs** (*chiplets*) avec chacun
            *   **8 cœurs**
            *   **cache L3 partagée de 32 MiB**
        *   **3 canaux de mémoire**

Où chaque cœur a
*   1 MiB de cache L2
*   32+32 KiB de cache L1 pour instructions
*   12 canaux de mémoire DDR5 (partagés via la puce I/O)

Total
*   8 nœuds NUMA par nœud (4 par socket × 2)
*   24 CCD (*chiplets*) par nœud (12 par socket × 2)
*   192 cœurs au total
*   768 MiB de cache L3 au total

### Réglage de la performance

Pour profiter au mieux de l’architecture EPYC 9655 :

1.  Alignez les tâches sur des CCD. Chaque CCD contient 8 cœurs intimement liés et une cache L3 partagée. Garder les fils d’exécution dans un CCD élimine la latence entre les puces fragmentées.

    Utiliser :
    ```bash
    #SBATCH --cpus-per-task=8
    ```
    Ceci fait en sorte que les fils pour chaque tâche restent dans un seul CCD.

2.  Distribuez les tâches sur les CCD.

    Avec 24 CCD par nœud, lancez 24 tâches par nœud pour utiliser pleinement tous les CCD sans les surcharger.

    Utilisez :
    ```bash
    #SBATCH --ntasks-per-node=24
    ```
    avec `--cpus-per-task=8`, pour bien utiliser pleinement le nœud de 192 cœurs.

## Nœuds GPU

### Architecture

Chaque nœud est composé de 1 processeur AMD EPYC 9454 (Zen 4) @ 2.75 GHz avec 48 cœurs physiques. Le processeur utilise l’architecture NUMA basée sur des puces fragmentées et le temps d’accès à la mémoire dépend de la localité des cœurs et de la mémoire. Les nœuds GPU utilisent le mode NPS=4 (NUMA par socket), ce qui divise le socket en 4 nœuds NUMA pour obtenir la meilleure localité pour la mémoire.

### Configuration

*   1 socket, configuré NPS=4
    *   **4 NUMA nodes**, each with
        *   **2 CCD** (Core Complex Dies), chacun avec
            *   **6 cœurs**
            *   **32MiB de cache L3 partagée**
        *   **3 canaux de mémoire**

Où chaque cœur a
*   1 MiB de cache L2
*   32 KiB de cache L1 pour les instructions
*   32 KiB de cache L1 pour les données
*   12 canaux de mémoire DDR5 (partagés par la puce d'entrée-sortie)

*   2 accélérateurs NVidia H100 80GB
    *   Les 4 accélérateurs de nœud sont connectés via SXM5.

### Réglage de la performance

Pour profiter au mieux de l’architecture EPYC 9454 CPU et obtenir la localité optimale pour les CPU et GPU :

1.  Liez les fils à des CCD.

    Chaque CCD contient 6 cœurs intimement liés et une cache L3 de 32 MiB. Pour garder les fils dans un CCD utilisez :
    ```bash
    #SBATCH --cpus-per-task=6
    ```
    Les fils restent dans le même CCD, ce qui diminue la latence entre les CCD et améliore l’utilisation de la cache.

2.  Associez les tâches aux nœuds NUMA. Avec 4 nœuds NUMA par socket (NPS=4), lancez 4 tâches par nœud (ou un multiple de 4) pour obtenir la meilleure performance.
    ```bash
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=12
    ```
    Ceci garde chaque tâche dans un domaine NUMA et permet un accès local à la mémoire et au GPU.

### Instances GPU

Utilisez une des options Slurm suivantes :

**Une instance H100-80gb** : `--gpus=h100:1`

**Plusieurs H100-80gb par nœud** :
*   `--gpus-per-node=h100:2`
*   `--gpus-per-node=h100:3`
*   `--gpus-per-node=h100:4`

**Plusieurs instances H100 réparties :** `--gpus=h100:n` (où n est le nombre de GPU demandé)

Environ la moitié des nœuds GPU utilisent la technologie MIG. Trois tailles d'instances sont disponibles :

*   **1g.10gb** : 1/8<sup>e</sup> de la puissance de calcul avec 10GB de mémoire GPU
*   **2g.20gb** : 2/8<sup>e</sup> de la puissance de calcul avec 20GB de mémoire GPU
*   **3g.40gb** : 3/8<sup>e</sup> de la puissance de calcul avec 40GB de mémoire GPU

Pour demander une et une seule instance GPU pour votre tâche de calcul, utilisez l'option correspondante :

*   **1g.10gb** : `--gpus=nvidia_h100_80gb_hbm3_1g.10gb:1`
*   **2g.20gb** : `--gpus=nvidia_h100_80gb_hbm3_2g.20gb:1`
*   **3g.40gb** : `--gpus=nvidia_h100_80gb_hbm3_3g.40gb:1`