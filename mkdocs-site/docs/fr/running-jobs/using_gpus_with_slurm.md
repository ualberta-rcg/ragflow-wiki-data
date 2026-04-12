---
title: "Using GPUs with Slurm/fr"
slug: "using_gpus_with_slurm"
lang: "fr"

source_wiki_title: "Using GPUs with Slurm/fr"
source_hash: "8c8fadcdc08cb89fe5479c1003a75396"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:17:49.092209+00:00"

tags:
  - slurm

keywords:
  - "Profilage de GPU"
  - "modèles de GPU"
  - "SBATCH"
  - "MIG"
  - "Slurm"
  - "Rorqual"
  - "Regroupement de tâches"
  - "Tâches MPI"
  - "GNU Parallel"
  - "nvidia_h100_80gb_hbm3"
  - "scripts de tâches"
  - "GPU"
  - "Caractéristiques des nœuds"
  - "ordonnancement des tâches"
  - "Trillium"
  - "cœurs CPU"
  - "mémoire système"
  - "--gpus-per-node"
  - "processus MPI"
  - "SLURM"
  - "H100-80gb"

questions:
  - "Quelle est la directive recommandée pour demander un ou plusieurs GPU lors de l'exécution d'une tâche Slurm ?"
  - "Quels sont les différents modèles de GPU et les grappes (comme Fir, Narval ou Nibi) disponibles selon le tableau fourni ?"
  - "Que doit faire un utilisateur si l'utilisation de directives Slurm alternatives pour l'allocation de GPU ne produit pas le résultat escompté ?"
  - "Comment peut-on obtenir la liste des identifiants de GPU disponibles sur les différentes grappes de calcul ?"
  - "Pourquoi est-il fortement recommandé de spécifier un identifiant de modèle de GPU précis dans ses scripts de tâches ?"
  - "Quelles sont les recommandations et les configurations requises concernant l'allocation des cœurs CPU et de la mémoire système pour les différents types de tâches GPU (séquentielles, multifils, MPI) ?"
  - "Quels sont les différents profils de partitionnement et de mémoire (ex. 2g.20gb, 3g.40gb) disponibles pour les cartes NVIDIA H100 ?"
  - "Quels sont les noms des systèmes ou grappes de calcul (comme Trillium et Rorqual) qui intègrent ces nœuds GPU ?"
  - "Quelle est la capacité totale et le type de mémoire (VRAM) des processeurs graphiques principaux mentionnés dans le texte ?"
  - "Quel est le nombre maximum de cœurs CPU alloués pour les différentes grappes de calcul comme Narval, Nibi et Rorqual ?"
  - "Quel est l'objectif principal du script `gpu_mpi_job.sh` présenté dans le texte ?"
  - "Quelles sont les ressources spécifiques (GPU, processus MPI et cœurs CPU) configurées par les directives SBATCH dans l'exemple de tâche MPI ?"
  - "Pourquoi est-il recommandé de demander un nœud entier pour une application capable d'utiliser efficacement tous ses GPU ?"
  - "Comment l'outil GNU Parallel permet-il de regrouper et d'exécuter simultanément plusieurs tâches sur un seul GPU sans conflit ?"
  - "Quelle variable d'environnement doit être configurée pour désactiver DCGM et permettre le profilage des tâches GPU sur Narval et Rorqual ?"
  - "Pourquoi est-il recommandé de demander un nœud entier pour une application capable d'utiliser efficacement tous ses GPU ?"
  - "Comment l'outil GNU Parallel permet-il de regrouper et d'exécuter simultanément plusieurs tâches sur un seul GPU sans conflit ?"
  - "Quelle variable d'environnement doit être configurée pour désactiver DCGM et permettre le profilage des tâches GPU sur Narval et Rorqual ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

Pour demander un ou plusieurs GPU pour une tâche [Slurm](running-jobs.md), utilisez :
`--gpus-per-node=<spécificateur_modèle>:<nombre>`

Par exemple :
`--gpus-per-node=a100:1`

Ceci est pour un seul GPU A100, à moins que vous n'ajoutiez `--nodes` pour demander plusieurs nœuds.
Pour les modèles valides, consultez la section [GPU disponibles](#gpu-disponibles) ci-dessous.

Vous pouvez aussi utiliser :
`--gres=gpu:<spécificateur_modèle>:<nombre>`
Cependant, il est possible que ce format ne soit plus pris en charge. Nous vous recommandons de le remplacer par `--gpus-per-node`.

Slurm prend en charge plusieurs autres directives que vous pouvez utiliser pour demander des GPU, par exemple `--gpus`, `--gpus-per-socket`, `--gpus-per-task`, `--mem-per-gpu` et `--ntasks-per-gpu`. Voyez la documentation de Slurm sur [sbatch](https://slurm.schedmd.com/sbatch.html). Notre équipe ne teste pas toutes les combinaisons; si vous n'obtenez pas le résultat voulu, contactez le [soutien technique](technical-support.md).

Pour l'information générale sur l'ordonnancement des tâches, consultez [Exécuter des tâches](running-jobs.md).

## GPU disponibles

| Grappe | Modèle | Multi-instances (MIG) | Identifiant pour Slurm | Synonyme pour Slurm |
| :----- | :----- | :-------------------- | :--------------------- | :------------------ |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-80gb | | h100 | |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-80gb | 1/8 | nvidia_h100_80gb_hbm3_1g.10gb | |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-80gb | 2/8 | nvidia_h100_80gb_hbm3_2g.20gb | |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-80gb | 3/8 | nvidia_h100_80gb_hbm3_3g.40gb | |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-40gb | | a100 | |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-40gb | 1/8 | a100_1g.5gb | |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-40gb | 2/8 | a100_2g.10gb | |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-40gb | 2/8 | a100_3g.20gb | |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-40gb | 4/8 | a100_4g.20gb | |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-80gb | | h100 | |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-80gb | 1/8 | nvidia_h100_80gb_hbm3_1g.10gb | h100_1g.10gb h100_1.10 h100_10gb |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-80gb | 2/8 | nvidia_h100_80gb_hbm3_2g.20gb | h100_2g.20gb h100_2.20 h100_20gb |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-80gb | 3/8 | nvidia_h100_80gb_hbm3_3g.40gb | h100_3g.40gb h100_3.40 h100_40gb |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | MI300A-128gb | | mi300a | |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-80gb | | h100 | |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-80gb | 1/8 | nvidia_h100_80gb_hbm3_1g.10gb | h100_1g.10gb h100_1.10 h100_10gb |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-80gb | 2/8 | nvidia_h100_80gb_hbm3_2g.20gb | h100_2g.20gb h100_2.20 h100_20gb |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-80gb | 3/8 | nvidia_h100_80gb_hbm3_3g.40gb | h100_3g.40gb h100_3.40 h100_40gb |
| [Trillium](trillium.md#node-characteristics) | H100-80gb | | h100 | |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-80gb | | h100 | |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | L40S-48gb | | l40s | |
| [tamIA](tamia.md#caracteristiques-des-noeuds) | H100-80gb | | h100 | |
| [tamIA](tamia.md#caracteristiques-des-noeuds) | H200 | | h200 | |
| [Vulcan](vulcan.md#materiel) | L40S-48gb | | l40s | |

La commande ci-dessous présente les identifiants de GPU (et MIG) disponibles sur chacune des grappes. Cette commande est utile si le tableau plus haut n'a pas été mis à jour récemment.

```bash
sinfo -o "%G"|grep gpu|sed 's/gpu://g'|sed 's/),/\n/g'|cut -d: -f1|sort|uniq
```

Sur certaines grappes, il existe des identifiants courts pour quelques modèles de MIG; cette commande ne les fournit pas.

De plus, la présence d'un modèle de GPU ne garantit pas que vous pouvez utiliser un identifiant de modèle correspondant; des restrictions supplémentaires peuvent s'appliquer, dépendant notamment de votre groupe de recherche.

Pour plus d'information, cliquez sur le nom de la grappe dans le tableau ci-dessus, ou contactez [le soutien technique](technical-support.md).

!!! warning
    Si vous ne spécifiez pas de modèle, votre tâche risque d'être rejetée ou acheminée vers une instance de GPU arbitraire.
    Très peu de programmes sont capables d'utiliser efficacement un modèle arbitraire, c'est pourquoi nous recommandons vivement de toujours spécifier un identifiant de modèle précis dans vos scripts de tâches.

Des GPU sont disponibles sur Arbutus, mais comme c'est le cas pour les autres ressources infonuagiques, il n'est pas possible de soumettre des tâches via Slurm.
Pour plus d'information, voir [Ressources infonuagiques](cloud-resources.md).

### GPU multi-instances (MIG)
La technologie MIG permet de partitionner un GPU en plusieurs instances. Vos tâches pourraient utiliser un MIG plutôt qu'un GPU entier. Pour plus d'information, voir [GPU multi-instances](multi-instance-gpu.md).

## Demander des cœurs CPU et la mémoire système

Avec chaque instance GPU, une tâche doit avoir un nombre de cœurs CPU (`1` par défaut) et une certaine quantité de mémoire système. Pour le maximum de cœurs CPU et de mémoire système, voir [le tableau des ratios](allocations-and-compute-scheduling.md#ratios-dans-les-bundles).

## Exemples

### Tâches avec un seul cœur
Pour une tâche qui nécessite un seul cœur CPU et un GPU :

````bash tab="gpu_serial_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1
#SBATCH --mem=4000M               # mémoire par nœud
#SBATCH --time=0-03:00
./program                         # pour tester, utilisez nvidia-smi
````

### Tâches multifils
Pour une tâche GPU qui nécessite plusieurs CPU dans un seul nœud :

````bash tab="gpu_threaded_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1         # nombre de GPU par nœud
#SBATCH --cpus-per-task=6         # cœurs ou fils CPU
#SBATCH --mem=4000M               # mémoire par nœud
#SBATCH --time=0-03:00
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./program
````

Pour chaque GPU complet demandé, nous recommandons :
*   sur Fir, un maximum de 12 cœurs CPU
*   sur Narval, un maximum de 12 cœurs CPU
*   sur Nibi, un maximum de 14 cœurs CPU
*   sur Rorqual, un maximum de 16 cœurs CPU

### Tâches MPI
````bash tab="gpu_mpi_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100:8             # nombre total de GPU
#SBATCH --ntasks-per-gpu=1        # 8 processus MPI au total
#SBATCH --cpus-per-task=6         # cœurs CPU par processus MPI
#SBATCH --mem-per-cpu=5G          # mémoire hôte par cœur CPU
#SBATCH --time=0-03:00            # temps de calcul (JJ-HH:MM)
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$SLURM_CPUS_PER_TASK ./program
````

### Nœuds entiers
Si votre application peut utiliser efficacement un nœud entier et ses GPU associés, vous pouvez probablement réduire le temps d'attente si vous demandez un nœud entier. Utilisez les scripts suivants comme modèle.

#### Regroupement de tâches pour un seul GPU

Pour exécuter pendant plus de 24 heures quatre programmes qui utilisent un seul GPU ou deux programmes qui utilisent deux GPU, nous recommandons [GNU Parallel](gnu-parallel.md). Voici un exemple simple :

```bash
cat params.input | parallel -j4 'CUDA_VISIBLE_DEVICES=$(({%} - 1)) python {} &> {#}.out'
```

L'identifiant du GPU est calculé en soustrayant 1 de l'identifiant de la fente (*slot*), représenté par {%}. L'identifiant de la tâche est représenté par {#}, avec des valeurs partant de 1.

Le fichier `params.input` devrait contenir les paramètres sur des lignes distinctes, comme suit :

```text
code1.py
code2.py
code3.py
code4.py
...
```

Vous pouvez ainsi soumettre plusieurs tâches. Le paramètre `-j4` fait en sorte que GNU Parallel exécutera quatre tâches concurremment en lançant une tâche aussitôt que la précédente est terminée. Pour éviter que deux tâches se disputent le même GPU, utilisez CUDA_VISIBLE_DEVICES.

### Profilage des tâches avec GPU

Sur [Narval](narval.md) et [Rorqual](rorqual.md), le profilage est possible, mais [DCGM (NVIDIA Data Center GPU Manager)](https://developer.nvidia.com/dcgm) doit être désactivé. Ceci doit se faire lorsque vous soumettez la tâche en configurant la variable d'environnement `DISABLE_DCGM`.

```bash
DISABLE_DCGM=1 salloc --account=def-someuser --gpus-per-node=a100:1 --mem=4000M --time=03:00
```

Ensuite, dans votre tâche interactive, attendez que DCGM soit désactivé sur le nœud.

```bash
while [ ! -z "$(dcgmi -v | grep 'Hostengine build info:')" ]; do  sleep 5; done
```

Enfin, lancez le profileur (voir [débogage et profilage](debugging-and-profiling.md) pour les détails).

!!! note
    Sur Fir et Nibi, le profilage de GPU décrit ci-dessus n'est pas encore disponible.

## Voir aussi
*   [CUDA](cuda.md)
*   [GPU multi-instances](multi-instance-gpu.md)
*   [Exécuter des tâches](running-jobs.md)
*   [Portail Metrix sur l'utilisation des ressources](metrix.md)
*   [NVTOP pour le suivi de l'utilisation des GPU](nvtop.md)
*   [Cuda Multi-Process Service (MPS)](hyper-q-mps.md)