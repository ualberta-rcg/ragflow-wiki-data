---
title: "Hyper-Q / MPS/fr"
slug: "hyper-q___mps"
lang: "fr"

source_wiki_title: "Hyper-Q / MPS/fr"
source_hash: "59aca4d8819a83e9e7918c52c91568e6"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:18:24.796378+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Aperçu

Hyper-Q (ou MPS pour *Multi-Process Service*) est une fonctionnalité des GPU de NVIDIA qui sont compatibles avec les versions 3.5 et plus récentes de CUDA. Voir le tableau des modèles, architectures et capacités de calcul CUDA dans [NVIDIA Tesla](https://en.wikipedia.org/wiki/Nvidia_Tesla).

Selon [la documentation de NVIDIA](https://docs.nvidia.com/deploy/mps/index.html),
> *[traduction libre]* L'architecture d'exécution MPS est conçue pour permettre de façon transparente l'utilisation d'applications CUDA parallèles et coopératives (comme le sont typiquement les tâches MPI) en tirant avantage des fonctionnalités Hyper-Q des derniers GPU de NVIDIA (Kepler et suivants). Hyper-Q permet aux noyaux CUDA d’être traités en simultané sur un même GPU, ce qui améliore la performance quand la capacité de calcul du GPU est sous-utilisée par un seul processus.

Nos tests ont démontré que MPS peut augmenter le nombre d'opérations en virgule flottante effectuées par seconde (flops) même quand le GPU est partagé entre des processus CPU qui ne sont pas reliés. Ceci signifie que MPS est la fonctionnalité idéale pour des applications CUDA qui traitent des problèmes dont leur taille relativement petite les rend incapables de bien occuper les GPU modernes dotés de milliers de cœurs.

MPS n'est pas activée par défaut, mais il suffit de lancer les commandes suivantes avant de démarrer votre application CUDA.

```bash
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log
nvidia-cuda-mps-control -d
```

Vous pouvez alors utiliser MPS si vous avez plus d'un fil CPU qui a accès au GPU. Ceci se produit quand vous exécutez une application hybride MPI/CUDA, une application hybride OpenMP/CUDA ou plusieurs applications séquentielles CUDA (ferme de GPU).

Pour plus d'information sur MPS, voir [la documentation de NVIDIA](https://docs.nvidia.com/deploy/mps/index.html).

## Ferme de GPU

La fonctionnalité MPS est très utile pour exécuter plusieurs instances d’une même application CUDA quand celle-ci est trop petite pour occuper entièrement un GPU moderne. MPS vous permet d’exécuter toutes ces instances, pourvu que la mémoire du GPU soit suffisante. Dans plusieurs cas, la production de résultats pourrait être grandement augmentée.

Le script suivant est un exemple pour configurer la ferme avec un GPU.

```bash title="script.sh"
#!/bin/bash
#SBATCH --gpus-per-node=v100:1
#SBATCH --time=0-10:00
#SBATCH --mem-per-cpu=8G
#SBATCH --cpus-per-task=8

mkdir -p $SLURM_TMPDIR/tmp
export CUDA_MPS_LOG_DIRECTORY=$SLURM_TMPDIR/tmp
nvidia-cuda-mps-control -d

for ((i=0; i<SLURM_CPUS_PER_TASK; i++))
 do
 echo $i
 ./my_code $i  &
 done

wait
```

Dans cet exemple, un GPU de type V100 est partagé par 8 instances de `my_code` qui n’a comme argument que l’indice de boucle `$i`. Comme nous demandons 8 cœurs CPU (#SBATCH --cpus-per-task=8), il y a un cœur CPU pour chacune des instances de l’application. Les deux éléments importants sont
*   `&` sur la ligne d’exécution du code qui déplace les processus à l’arrière-plan et
*   la commande `wait` à la fin du script qui fait en sorte que la ferme de GPU se poursuive jusqu’à ce que tous les processus en arrière-plan soient terminés.