---
title: "Multi-Instance GPU/fr"
tags:
  []

keywords:
  []
---

Plusieurs logiciels sont incapables d'exploiter pleinement les GPU modernes tels que les [A100](https://www.nvidia.com/en-us/data-center/a100/) et [H100](https://www.nvidia.com/en-us/data-center/h100/) de NVidia. La technologie multi-instances [(MIG pour <i>Multi-Instance GPU</i>)](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) permet de partitionner un seul GPU en plusieurs instances, faisant ainsi de chacune un GPU virtuel complètement indépendant. Chacune des instances de GPU dispose alors d'une portion des ressources de calcul et de la mémoire du GPU d'origine, le tout détaché des autres instances par des protections sur puce.

Les instances d'un GPU sont moins gourmandes, ce qui se reflète par une utilisation moins rapide de votre priorité de calcul. Les tâches soumises sur une instance plutôt que sur un GPU entier utilisent moins de la priorité qui vous est allouée et vous pourrez exécuter plus de tâches avec un temps d'attente plus court.

= Pourquoi choisir un GPU entier ou une instance de GPU=
Les tâches qui utilisent moins de la moitié de la puissance de calcul d'un GPU entier et moins de la moitié de la mémoire GPU disponible doivent être évaluées et testées sur une instance. Dans la plupart des cas, ces tâches s'exécutent tout aussi rapidement sur une instance et consomment moins de la moitié des ressources de calcul.

Voir [Quand migrer une tâche sur une instance](multi-instance-gpu-fr#quand_migrer_une_tâche_sur_une_instance.md) ci-dessous.

<div class="mw-translate-fuzzy">
= Limites de la technologie =
[La technologie MIG ne prend pas en charge](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations) la [communication interprocessus CUDA](https://developer.nvidia.com/docs/drive/drive-os/6.0.8.1/public/drive-os-linux-sdk/common/topics/nvsci_nvsciipc/Inter-ProcessCommunication1.html) qui optimise le transfert de données via NVLink et NVSwitch. Cette limite diminue aussi l'efficacité de la communication entre les instances. En conséquence, <b>le lancement d'un exécutable sur plusieurs MIG à la fois n'améliore pas la performance et doit être évité.</b>
</div>

<div class="mw-translate-fuzzy">
Veuillez noter que les API graphiques ne sont pas prises en charge (par exemple OpenGL, Vulkan, etc.); voir [Application Considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#application-considerations).
</div>

Les tâches avec GPU qui nécessitent de nombreux cœurs CPU par GPU peuvent également nécessiter un GPU entier au lieu d'une instance. Le nombre maximum de cœurs CPU par instance dépend du 
[nombre maximum de cœurs CPU par GPU entier](allocations_and_compute_scheduling-fr#ratios_dans_les_bundles.md) et des [profils MIG qui sont configurés](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#a100-profiles). Ces deux caractéristiques varient d'une grappe à l'autre et d'un nœud GPU à l'autre.

<div class="mw-translate-fuzzy">
= Configurations disponibles =
[Plusieurs configurations et profils MIG sont possibles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles), mais les profils suivants dépendent du système&nbsp;:
* [Narval|NVIDIA A100-40gb pour Narval](narval#instances-_gpu.md)
* [NVIDIA H100-80gb pour Rorqual](rorqual#instances-_gpu.md)
* Nibi:
** nvidia_h100_80gb_hbm3_1g.10gb
** nvidia_h100_80gb_hbm3_2g.20gb
** nvidia_h100_80gb_hbm3_3g.40gb
</div>

<div class="mw-translate-fuzzy">
Le nom du profil indique la taille de l'instance, par exemple `3g.20gb` est dotée de 20Go de mémoire GPU et sa performance est égale aux 3/8<sup>e</sup> de la performance de calcul d’un GPU entier. Le fait de nécessiter moins de puissance diminue l’impact sur votre allocation et sur la priorité assignée à vos tâches.
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
Using less powerful profiles will have a lower impact on your allocation and priority.
</div>

Pour la liste de tous les gabarits (et le nom complet des GPU) sur une grappe en particulier, lancez

```bash

```
grep gpused 's/gpu://g'sed 's/),/\n/g'cut -d: -f1sortuniq}}

Pour connaître le maximum recommandé de cœurs CPU et de mémoire système par instance, voir
[le tableau des ratios](allocations_and_compute_scheduling-fr#ratios_dans_les_bundles.md).

<span id="Job_examples"></span>
= Exemples =

Pour demander une instance de 20Go à 3/8 de la puissance pour une tâche interactive d’une durée d’une (1) heure&nbsp;:
 

```bash

```
def-someuser --gpusa100_3g.20gb:1 --cpus-per-task2 --mem40gb --time1:0:0
}}

Pour demander une instance de 20Go à 4/8 de la puissance pour un script de tâches en lot d’une durée de 24&nbsp;heures qui utilise le maximum recommandé de cœurs et de mémoire système&nbsp:

**`a100_4g.20gb_mig_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100_4g.20gb:1 
#SBATCH --cpus-per-task=6    # There are 6 CPU cores per 3g.20gb and 4g.20gb on Narval.
#SBATCH --mem=62gb           # There are 62GB GPU RAM per 3g.20gb and 4g.20gb on Narval.
#SBATCH --time=24:00:00

hostname
nvidia-smi
```

<span id="Finding_which_of_your_jobs_should_use_an_instance"></span>
= Quand migrer une tâche sur une instance =

L'historique de vos tâches est disponible sur  [le portail d'utilisation de Narval (préparation en cours)](portail.md). 

La consommation d’énergie est un bon indicateur de la puissance de calcul totale demandée au GPU. Par exemple, le travail suivant nécessitait un GPU&nbsp;A100 entier avec une enveloppe thermique (TDP) maximale de 400&nbsp;W, mais n'utilisait que 100&nbsp;W en moyenne, soit seulement 50&nbsp;W de plus que la consommation au repos&nbsp;:
 
[400px|frame|left|Consommation d'énergie sur un GPU A100](file:examplegpupower.png.md) 
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

Les fonctionnalités du GPU peuvent également fournir des informations sur son utilisation dans les cas où la consommation d'énergie n'est pas suffisante. Dans ce prochain exemple de tâche, le graphique d'utilisation du GPU confirme la conclusion du graphique de consommation d'énergie du GPU selon laquelle la tâche utilise moins de 25&nbsp;% de la puissance de calcul disponible d'un GPU&nbsp;A100 entier&nbsp;:
 
[400px|frame|left|Utilisation d'un GPU A100](file:examplegpuutilisation.png.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

Il faut aussi tenir compte de la quantité maximale de mémoire GPU et de la quantité moyenne de cœurs CPU nécessaires pour exécuter la tâche. Dans le prochain exemple, la tâche utilise un maximum de 3Go de mémoire GPU sur les 40Go d'un GPU&nbsp;A100.
 
[400px|frame|left|Utilisation de la mémoire du GPU A100](file:examplegpumemory.png.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

La tâche a aussi été lancée en utilisant un seul cœur de processeur. En tenant compte de ces trois métriques, nous voyons que la tâche pourrait facilement s'exécuter sur une instance de 3&nbsp;g.20&nbsp;Go ou de 4&nbsp;g.20&nbsp;Go avec de la puissance et de la mémoire à revendre. 

Un autre moyen de [surveiller l'utilisation d'une tâche en cours d'exécution](running-jobs-fr#surveillance_d'une_tâche_en_cours.md) consiste à se connecter au nœud sur lequel la tâche se trouve et utiliser `nvidia-smi` pour lire les métriques du GPU en temps réel. Cela ne fournira pas de valeurs maximales et moyennes pour la mémoire et la puissance de toute la tâche, mais pourrait être utile pour identifier une sous-utilisation du GPU.