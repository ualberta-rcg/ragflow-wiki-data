---
title: "Multi-Instance GPU/fr"
slug: "multi-instance_gpu"
lang: "fr"

source_wiki_title: "Multi-Instance GPU/fr"
source_hash: "0d88a5c5d2c3eb3d070495a70ad9cb8f"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:57:40.753440+00:00"

tags:
  []

keywords:
  - "configuration MIG"
  - "puissance de calcul"
  - "mémoire GPU"
  - "instance de GPU"
  - "configurations"
  - "Instances GPU"
  - "GPU NVIDIA"
  - "GPU"
  - "profils MIG"
  - "utilisation de la mémoire"
  - "consommation d'énergie"
  - "streaming multiprocessors"
  - "technologie MIG"
  - "utilisation"
  - "GPU virtuel"
  - "NVIDIA A100 et H100"
  - "nvidia-smi"
  - "instance MIG"
  - "système"
  - "GPU A100"
  - "cœurs CPU"
  - "GPU H100"
  - "tâche"

questions:
  - "Qu'est-ce que la technologie Multi-Instance GPU (MIG) et quels sont ses avantages pour l'allocation des ressources ?"
  - "Dans quels cas est-il recommandé d'utiliser une instance de GPU plutôt qu'un GPU entier pour exécuter une tâche ?"
  - "Quelles sont les principales limites techniques et restrictions associées à l'utilisation de la technologie MIG ?"
  - "Comment la nomenclature des profils d'instances (comme H100-1g.10gb) définit-elle la puissance de calcul et la mémoire allouées ?"
  - "Quelles sont les commandes et les paramètres requis pour soumettre une tâche interactive ou en lot utilisant une instance GPU spécifique ?"
  - "Quels indicateurs de performance (consommation d'énergie, utilisation du GPU, mémoire) permettent de déterminer si une tâche doit être migrée vers une instance moins puissante ?"
  - "De quoi dépendent les profils et configurations MIG selon le texte ?"
  - "Quels sont les différents systèmes et modèles de GPU NVIDIA spécifiques qui sont listés ?"
  - "Où peut-on consulter la documentation officielle concernant les profils MIG supportés ?"
  - "Quels sont les paramètres de ressources matérielles (mémoire GPU et cœurs CPU) qu'il faut évaluer pour exécuter une tâche ?"
  - "Quelle est la capacité totale de mémoire disponible sur le modèle de GPU A100 présenté ?"
  - "Quelle quantité maximale de mémoire GPU est réellement utilisée par la tâche dans l'exemple mentionné ?"
  - "Comment peut-on surveiller l'utilisation des ressources d'un GPU en temps réel pendant l'exécution d'une tâche ?"
  - "Comment les 132 processeurs (SM) d'un GPU H100 SXM5 sont-ils concrètement répartis entre les différentes instances MIG ?"
  - "Pourquoi la division en huitièmes présentée dans la documentation de NVidia ne reflète-t-elle pas la réalité mathématique de l'architecture du GPU H100 ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Plusieurs logiciels sont incapables d'exploiter pleinement les GPU modernes tels que les [A100](https://www.nvidia.com/en-us/data-center/a100/) et [H100](https://www.nvidia.com/en-us/data-center/h100/) de NVIDIA. La technologie multi-instances ([MIG](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) pour *Multi-Instance GPU*) permet de partitionner un seul GPU en plusieurs instances, faisant ainsi de chacune un GPU virtuel complètement indépendant. Chacune des instances de GPU dispose alors d'une portion des ressources de calcul et de la mémoire du GPU d'origine, le tout détaché des autres instances par des protections sur puce.

Les instances d'un GPU sont moins gourmandes, ce qui se reflète par une utilisation moins rapide de votre priorité de calcul. Les tâches soumises sur une instance plutôt que sur un GPU entier utilisent moins de la priorité qui vous est allouée et vous pourrez exécuter plus de tâches avec un temps d'attente plus court.

## Pourquoi choisir un GPU entier ou une instance de GPU

Les tâches qui utilisent moins de la moitié de la puissance de calcul d'un GPU entier et moins de la moitié de la mémoire GPU disponible doivent être évaluées et testées sur une instance. Dans la plupart des cas, ces tâches s'exécutent tout aussi rapidement sur une instance et consomment moins de la moitié des ressources de calcul.

Voir [Quand migrer une tâche sur une instance](#quand-migrer-une-tâche-sur-une-instance) ci-dessous.

## Limites de la technologie

[La technologie MIG ne prend pas en charge](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) la [communication interprocessus CUDA](https://developer.nvidia.com/docs/drive/drive-os/6.0.8.1/public/drive-os-linux-sdk/common/topics/nvsci_nvsciipc/Inter-ProcessCommunication1.html) qui optimise le transfert de données via NVLink et NVSwitch. Cette limite diminue aussi l'efficacité de la communication entre les instances. Par conséquent, **il n'est pas permis d'utiliser plusieurs instances MIG à la fois dans une même tâche**; toute soumission d'une telle tâche est donc rejetée.
Si vous pensez avoir besoin de plusieurs instances MIG, vous pouvez :
* Demander une instance plus puissante, par exemple, une instance de taille 3g au lieu de trois instances de taille 1g.
* Demander un GPU entier ou plusieurs GPU.
* Utiliser [MPS](../software/hyper-q___mps.md) plutôt que MIG.
* [Écrivez au soutien technique](../support/technical_support.md) en expliquant pourquoi vous voulez exécuter votre application sur plusieurs instances MIG; nous vous assisterons pour trouver une solution.

Veuillez noter que les API graphiques ne sont pas prises en charge (par exemple OpenGL, Vulkan, etc.); voir [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations).

Les tâches avec GPU qui nécessitent de nombreux cœurs CPU par GPU peuvent également nécessiter un GPU entier au lieu d'une instance. Le nombre maximum de cœurs CPU par instance dépend du [nombre maximum de cœurs CPU par GPU entier](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles) et des [profils MIG qui sont configurés](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#a100-profiles). Ces deux caractéristiques varient d'une grappe à l'autre et d'un nœud GPU à l'autre.

## Configurations disponibles

Plusieurs [configurations et profils MIG sont possibles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles), mais les profils suivants dépendent du système :
* [Narval, GPU NVIDIA A100-40gb](../clusters/narval.md#instances-gpu)
* [Rorqual, GPU NVIDIA H100-80gb](../clusters/rorqual.md#instances-gpu)
* [Nibi, GPU NVIDIA H100-80gb](../clusters/nibi.md#instances-gpu)
* [Fir, GPU NVIDIA H100-80gb](../software/fir.md)

Le nom du profil indique la taille de l'instance.
* **H100-1g.10gb** : 1/8^e^ de la puissance de calcul et 10Go de mémoire
* **H100-2g.20gb** : 2/8^e^ de la puissance de calcul et 20Go de mémoire
* **H100-3g.40gb** : 3/8^e^ de la puissance de calcul et 40Go de mémoire

Le fait d'utiliser des profils moins puissants diminue l'impact sur votre allocation et votre priorité.

Pour la liste de toutes les instances MIG disponibles (et le nom complet des GPU) sur une grappe en particulier, lancez

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

Pour connaître le maximum recommandé de cœurs CPU et de mémoire système par instance, voir [le tableau des ratios](../running-jobs/allocations_and_compute_scheduling.md#ratios-dans-les-bundles).

## Exemples

Pour demander une instance de 20Go à 3/8^e^ de la puissance pour une tâche interactive d’une durée d’une (1) heure :

```bash
salloc --account=def-someuser --gpus=a100_3g.20gb:1 --cpus-per-task=2 --mem=40gb --time=1:0:0
```

Pour demander une instance de 20Go à 4/8^e^ de la puissance pour un script de tâches en lot d’une durée de 24 heures qui utilise le maximum recommandé de cœurs et de mémoire système :

```sh title="a100_4g.20gb_mig_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100_4g.20gb:1 
#SBATCH --cpus-per-task=6    # Il y a 6 cœurs CPU par 3g.20gb et 4g.20gb sur Narval.
#SBATCH --mem=62gb           # Il y a 62Go de mémoire GPU par 3g.20gb et 4g.20gb sur Narval.
#SBATCH --time=24:00:00

hostname
nvidia-smi
```

## Quand migrer une tâche sur une instance

L'historique de vos tâches est disponible sur le portail d'utilisation de Narval (préparation en cours).

La consommation d’énergie est un bon indicateur de la puissance de calcul totale demandée au GPU. Par exemple, une tâche nécessitait un GPU A100 entier avec une enveloppe thermique (TDP) maximale de 400 W, mais n'utilisait que 100 W en moyenne, soit seulement 50 W de plus que la consommation au repos.

Les fonctionnalités du GPU peuvent également fournir des informations sur son utilisation dans les cas où la consommation d'énergie n'est pas suffisante. Dans un autre exemple, l'analyse de l'utilisation du GPU a confirmé que la tâche utilisait moins de 25 % de la puissance de calcul disponible d'un GPU A100 entier.

Il faut aussi tenir compte de la quantité maximale de mémoire GPU et de la quantité moyenne de cœurs CPU nécessaires pour exécuter la tâche. Par exemple, une tâche a utilisé un maximum de 3Go de mémoire GPU sur les 40Go d'un GPU A100.

La tâche a aussi été lancée en utilisant un seul cœur de processeur. En tenant compte de ces trois métriques, nous voyons que la tâche pourrait facilement s'exécuter sur une instance de 3g.20gb avec de la puissance et de la mémoire à revendre.

Un autre moyen de [surveiller l'utilisation d'une tâche en cours d'exécution](../running-jobs/running_jobs.md) consiste à se connecter au nœud sur lequel la tâche se trouve et utiliser `nvidia-smi` pour lire les métriques du GPU en temps réel. Cela ne fournira pas de valeurs maximales et moyennes pour la mémoire et la puissance de toute la tâche, mais pourrait être utile pour identifier une sous-utilisation du GPU.

## Détails sur la configuration

Dans [la documentation de NVIDIA](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-mig-profiles.html#h100-mig-profiles), il est question de septièmes et de huitièmes de GPU, mais la réalité est plus complexe. Un GPU H100 SXM5 a un total de 132 processeurs (SM pour *streaming multiprocessors*). Le nombre 132 est le produit de 11*3*2*2, et ne se divise ni par sept, ni par huit.

Les 132 SM d'un MIG de configuration H100 SXM5 sont partitionnés ainsi :

* **une** instance de **60** SM (`nvidia_h100_80gb_hbm3_3g.40gb`)
* **une** instance de **32** SM (`nvidia_h100_80gb_hbm3_2g.20gb`)
* **deux** instances de **16** SM (`nvidia_h100_80gb_hbm3_1g.10gb`)

ce qui laisse huit SM qui ne sont pas assignés et donc perdus.
(60+32+16+16+(8) = 124 *assignés* + 8 *non assignés* = 132).
Il serait préférable, mais pas très commode, de considérer un MIG H100 comme étant divisé en trente-troisièmes. Ce que NVIDIA considère comme étant un huitième représente donc 4/33^e^ du GPU H100, deux huitièmes étant 8/33^e^ et trois huitièmes étant 15/33^e^, laissant 2/33^e^ du GPU non assignés à une instance.