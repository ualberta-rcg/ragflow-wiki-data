---
title: "Multi-Instance GPU/fr"
slug: "multi-instance_gpu"
lang: "fr"

source_wiki_title: "Multi-Instance GPU/fr"
source_hash: "9fbf693e5fa68e778aef15be0177d684"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:35:09.119594+00:00"

tags:
  []

keywords:
  - "ressources de calcul"
  - "nvidia-smi"
  - "temps réel"
  - "grappe Narval"
  - "taille de l'instance"
  - "cœur de processeur"
  - "consommation d'énergie"
  - "instance"
  - "surveiller une tâche"
  - "mémoire GPU"
  - "NVIDIA A100 et H100"
  - "performance de calcul"
  - "utilisation du GPU"
  - "profils MIG"
  - "instance GPU"
  - "instances de GPU"
  - "métriques"
  - "nom du profil"
  - "métriques du GPU"
  - "allocation"
  - "mémoire du GPU A100"
  - "Multi-Instance GPU (MIG)"
  - "puissance et mémoire"
  - "sous-utilisation du GPU"

questions:
  - "Qu'est-ce que la technologie Multi-Instance GPU (MIG) et quels avantages offre-t-elle en termes de ressources et de temps d'attente ?"
  - "Dans quelles conditions est-il recommandé de privilégier l'utilisation d'une instance de GPU plutôt que celle d'un GPU entier ?"
  - "Quelles sont les limites techniques de la technologie MIG, notamment concernant la communication interprocessus et la prise en charge des API graphiques ?"
  - "Comment peut-on obtenir la liste de tous les gabarits de GPU disponibles sur une grappe spécifique ?"
  - "Quels paramètres Slurm doivent être configurés pour demander une instance GPU partielle lors d'une tâche interactive ou en lot ?"
  - "Quels indicateurs de performance permettent de déterminer si une tâche devrait être migrée vers une instance GPU moins puissante ?"
  - "Comment le nom du profil d'une instance permet-il de connaître sa capacité en mémoire GPU ?"
  - "Quelle est la proportion de performance de calcul offerte par un profil comme \"3g.20gb\" par rapport à un GPU complet ?"
  - "Quel est l'impact de l'utilisation d'une instance nécessitant moins de puissance sur l'allocation et la priorité des tâches ?"
  - "Combien de cœurs de processeur ont été utilisés pour lancer la tâche ?"
  - "Quel modèle de GPU est analysé pour son utilisation de la mémoire ?"
  - "Quels types d'instances sont recommandés pour exécuter cette tâche avec de la puissance et de la mémoire en réserve ?"
  - "Quelle commande permet de lire les métriques du GPU en temps réel en se connectant au nœud de la tâche ?"
  - "Quelles informations spécifiques concernant la mémoire et la puissance ne peuvent pas être obtenues avec cette méthode ?"
  - "Pour quel objectif précis cette approche de surveillance en temps réel est-elle particulièrement utile ?"
  - "Quelle commande permet de lire les métriques du GPU en temps réel en se connectant au nœud de la tâche ?"
  - "Quelles informations spécifiques concernant la mémoire et la puissance ne peuvent pas être obtenues avec cette méthode ?"
  - "Pour quel objectif précis cette approche de surveillance en temps réel est-elle particulièrement utile ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Plusieurs logiciels sont incapables d'exploiter pleinement les GPU modernes tels que les [A100](https://www.nvidia.com/en-us/data-center/a100/) et [H100](https://www.nvidia.com/en-us/data-center/h100/) de NVIDIA. La technologie multi-instances [MIG (pour *Multi-Instance GPU*)](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) permet de partitionner un seul GPU en plusieurs instances, faisant ainsi de chacune un GPU virtuel complètement indépendant. Chacune des instances de GPU dispose alors d'une portion des ressources de calcul et de la mémoire du GPU d'origine, le tout détaché des autres instances par des protections sur puce.

Les instances d'un GPU sont moins gourmandes, ce qui se reflète par une utilisation moins rapide de votre priorité de calcul. Les tâches soumises sur une instance plutôt que sur un GPU entier utilisent moins de la priorité qui vous est allouée et vous pourrez exécuter plus de tâches avec un temps d'attente plus court.

## Pourquoi choisir un GPU entier ou une instance de GPU

Les tâches qui utilisent moins de la moitié de la puissance de calcul d'un GPU entier et moins de la moitié de la mémoire GPU disponible doivent être évaluées et testées sur une instance. Dans la plupart des cas, ces tâches s'exécutent tout aussi rapidement sur une instance et consomment moins de la moitié des ressources de calcul.

Voir [Quand migrer une tâche sur une instance](#quand-migrer-une-tache-sur-une-instance) ci-dessous.

## Limites de la technologie

[La technologie MIG ne prend pas en charge](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) la [communication interprocessus CUDA](https://developer.nvidia.com/docs/drive/drive-os/6.0.8.1/public/drive-os-linux-sdk/common/topics/nvsci_nvsciipc/Inter-ProcessCommunication1.html) qui optimise le transfert de données via NVLink et NVSwitch. Cette limite diminue aussi l'efficacité de la communication entre les instances. En conséquence, **le lancement d'un exécutable sur plusieurs MIG à la fois n'améliore pas la performance et doit être évité.**

!!! attention "Attention"
    Veuillez noter que les API graphiques ne sont pas prises en charge (par exemple OpenGL, Vulkan, etc.); voir [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations).

Les tâches avec GPU qui nécessitent de nombreux cœurs CPU par GPU peuvent également nécessiter un GPU entier au lieu d'une instance. Le nombre maximum de cœurs CPU par instance dépend du [nombre maximum de cœurs CPU par GPU entier](allocations-and-compute-scheduling.md#ratios-dans-les-bundles) et des [profils MIG qui sont configurés](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#a100-profiles). Ces deux caractéristiques varient d'une grappe à l'autre et d'un nœud GPU à l'autre.

## Configurations disponibles

[Plusieurs configurations et profils MIG sont possibles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles), mais les profils suivants dépendent du système :
*   [NVIDIA A100-40gb pour Narval](narval.md#instances-gpu)
*   [NVIDIA H100-80gb pour Rorqual](rorqual.md#instances-gpu)
*   Nibi:
    *   nvidia_h100_80gb_hbm3_1g.10gb
    *   nvidia_h100_80gb_hbm3_2g.20gb
    *   nvidia_h100_80gb_hbm3_3g.40gb

Le nom du profil indique la taille de l'instance, par exemple `3g.20gb` est dotée de 20Go de mémoire GPU et sa performance est égale aux 3/8<sup>e</sup> de la performance de calcul d’un GPU entier. Le fait de nécessiter moins de puissance diminue l’impact sur votre allocation et sur la priorité assignée à vos tâches.

Pour la liste de tous les gabarits (et le nom complet des GPU) sur une grappe en particulier, lancez

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

Pour connaître le maximum recommandé de cœurs CPU et de mémoire système par instance, voir [le tableau des ratios](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).

## Exemples

Pour demander une instance de 20Go à 3/8 de la puissance pour une tâche interactive d’une durée d’une (1) heure :

```bash
[name@narval ~]$ salloc --account=def-someuser --gpus=a100_3g.20gb:1 --cpus-per-task=2 --mem=40gb --time=1:0:0
```

Pour demander une instance de 20Go à 4/8 de la puissance pour un script de tâches en lot d’une durée de 24 heures qui utilise le maximum recommandé de cœurs et de mémoire système :

```sh title="a100_4g.20gb_mig_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100_4g.20gb:1 
#SBATCH --cpus-per-task=6    # There are 6 CPU cores per 3g.20gb and 4g.20gb on Narval.
#SBATCH --mem=62gb           # There are 62GB GPU RAM per 3g.20gb and 4g.20gb on Narval.
#SBATCH --time=24:00:00

hostname
nvidia-smi
```

## Quand migrer une tâche sur une instance

L'historique de vos tâches est disponible sur [le portail d'utilisation de Narval (préparation en cours)](portail.md).

La consommation d’énergie est un bon indicateur de la puissance de calcul totale demandée au GPU. Par exemple, le travail suivant nécessitait un GPU A100 entier avec une enveloppe thermique (TDP) maximale de 400 W, mais n'utilisait que 100 W en moyenne, soit seulement 50 W de plus que la consommation au repos.

Les fonctionnalités du GPU peuvent également fournir des informations sur son utilisation dans les cas où la consommation d'énergie n'est pas suffisante. Dans ce prochain exemple de tâche, le graphique d'utilisation du GPU confirme la conclusion du graphique de consommation d'énergie du GPU selon laquelle la tâche utilise moins de 25 % de la puissance de calcul disponible d'un GPU A100 entier.

Il faut aussi tenir compte de la quantité maximale de mémoire GPU et de la quantité moyenne de cœurs CPU nécessaires pour exécuter la tâche. Dans le prochain exemple, la tâche utilise un maximum de 3Go de mémoire GPU sur les 40Go d'un GPU A100.

La tâche a aussi été lancée en utilisant un seul cœur de processeur. En tenant compte de ces trois métriques, nous voyons que la tâche pourrait facilement s'exécuter sur une instance de 3 g.20 Go ou de 4 g.20 Go avec de la puissance et de la mémoire à revendre.

Un autre moyen de [surveiller l'utilisation d'une tâche en cours d'exécution](running-jobs.md#surveillance-dune-tache-en-cours) consiste à se connecter au nœud sur lequel la tâche se trouve et utiliser `nvidia-smi` pour lire les métriques du GPU en temps réel. Cela ne fournira pas de valeurs maximales et moyennes pour la mémoire et la puissance de toute la tâche, mais pourrait être utile pour identifier une sous-utilisation du GPU.