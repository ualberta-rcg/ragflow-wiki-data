---
title: "Using GPUs with Slurm/fr"
tags:
  - slurm

keywords:
  []
---

= Introduction =

Pour demander un ou plusieurs GPU pour une tâche [Slurm](running-jobs-fr.md), utilisez
  --gpus-per-node=<model_specifier>:<number>

Par exemple
  --gpus-per-node=a100:1

Ceci est pour un seul GPU A100, à moins que vous ajoutiez `--nodes` pour demander plusieurs nœuds.
Pour les modèles valides, voir la section <i>[GPU disponibles</i>](using-gpus-with-slurm-fr.md) ci-dessous.

Vous pouvez aussi utiliser
  --gres=gpu:<model_specifier>:<number>
Cependant, il est possible que ce format ne soit plus pris en charge. Nous vous recommandons de le remplacer par  `--gpus-per-node`.

Slurm prend en charge plusieurs autres directives que vous pouvez utiliser pour demander des GPU, par exemple `--gpus`, `--gpus-per-socket`, `--gpus-per-task`, `--mem-per-gpu` et `--ntasks-per-gpu`. Voyez la documentation de Slurm sur [sbatch](https://slurm.schedmd.com/sbatch.html).  Notre équipe ne teste pas toutes les combinaisons; si vous n'obtenez pas le résultat voulu, contactez le [soutien technique](technical-support-fr.md).

Pour l'information générale sur l'ordonnancement des tâches, consultez [Exécuter des tâches](running-jobs-fr.md).

= GPU disponibles =

{| class="wikitable"
|-
! Grappe !! Modèle 
!Multi-instances
(MIG)!! Identifiant pour Slurm 
!Synonyme pour Slurm
|- 
| rowspan=4|[Fir](fir-fr#caractéristiques_des_nœuds.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|
|-
| rowspan=5|[Narval](narval#caractéristiques_des_nœuds.md) || rowspan=5|A100-40gb 
| || a100 
|
|-
|1/8
|  a100_1g.5gb  
|
|-
|2/8
|  a100_2g.10gb 
|
|-
|2/8
|  a100_3g.20gb 
|
|-
|4/8
|  a100_4g.20gb 
|
|- 
| rowspan=5|[Nibi](nibi-fr#caractéristiques_des_nœuds.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|h100_1g.10gb h100_1.10 h100_10gb
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|h100_2g.20gb h100_2.20 h100_20gb
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|h100_3g.40gb h100_3.40 h100_40gb
|-
| MI300A-128gb  
| || mi300a  
|
|- 
| rowspan=4|[Rorqual](rorqual#caractéristiques_des_nœuds.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|h100_1g.10gb h100_1.10 h100_10gb
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|h100_2g.20gb h100_2.20 h100_20gb
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|h100_3g.40gb h100_3.40 h100_40gb
|-
| [Trillium](trillium#node_characteristics.md) || H100-80gb 
| || h100 
|
|-
| rowspan=2|[Rorqual](rorqual#caractéristiques_des_nœuds.md)  || H100-80gb 
| || h100 
|
|-
|  L40S-48gb 
| || l40s 
|
|-
| rowspan=2|[tamIA](tamia#caractéristiques_des_nœuds.md) || H100-80gb 
| || h100 
|
|-
|  H200 
| || h200 
|
|-
| rowspan=2|[Vulcan](vulcan-fr#matériel.md) || L40S-48gb 
| || l40s 
|
|}

La commande ci-dessous présente les identifiants de GPU (et MIG) disponibles sur chacune des grappes. Cette commande est utile si le tableau plus haut n'a pas été mis à jour récemment.

```bash

```
grep gpused 's/gpu://g'sed 's/),/\n/g'cut -d: -f1sortuniq}}

Sur certaines grappes, il existe des identifiants courts pour quelques modèles de MIG; cette commande ne les fournit pas.

De plus, la présence d'un modèle de GPU ne garantit pas que vous pouvez utiliser un identifiant de modèle correspondant; des restrictions supplémentaires peuvent s'appliquer, dépendant notamment de votre groupe de recherche.

Pour plus d'information, cliquez sur le nom de la grappe dans le tableau ci-dessus, ou contactez [le soutien technique](technical-support-fr.md).

Si vous ne spécifiez pas de modèle, votre tâche risque d'être rejetée ou acheminée vers une instance de GPU arbitraire.

Très peu de programmes sont capables d'utiliser efficacement un modèle arbitraire, c'est pourquoi nous recommandons vivement de toujours spécifier un identifiant de modèle dans vos scripts de tâches. 

Des GPU sont disponibles sur Arbutus, mais comme c'est le cas pour les autres ressources infonuagiques, il n'est pas possible de soumettre des tâches via Slurm.
Pour plus d'information, voir [Ressources infonuagiques](cloud-resources-fr.md).

## GPU multi-instances (MIG) 
La technologie MIG permet de partitionner un GPU en plusieurs instances. Vos tâches pourraient utiliser un MIG plutôt qu'un GPU entier. Pour plus d'information, voir [GPU multi-instances](multi-instance_gpu-fr.md).

<span id="Requesting_CPU_cores_and_system_memory"></span>
= Demander des cœurs CPU et la mémoire système =

Avec chaque instance GPU, une tâche doit avoir un nombre de cœurs CPU (`1` par défaut) et une certaine quantité de mémoire système. Pour le maximum de cœurs CPU et de mémoire système, voir [le tableau des ratios](allocations_and_compute_scheduling-fr#ratios_dans_les_bundles.md).

<span id="Examples"></span>
= Exemples =

## Tâches avec un seul cœur 
Pour une tâche qui nécessite un seul cœur CPU et un GPU,

**`gpu_serial_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1
#SBATCH --mem=4000M               # mémoire par nœud
#SBATCH --time=0-03:00
./program                         # pour tester, utilisez nvidia-smi
```

## Tâches multifils 
Pour une tâche GPU qui nécessite plusieurs CPU dans un seul nœud,

**`gpu_threaded_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1         # nombre de GPU par nœud
#SBATCH --cpus-per-task=6         # cœurs ou fils CPU
#SBATCH --mem=4000M               # mémoire par nœud
#SBATCH --time=0-03:00
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./program
```

Pour chaque GPU complet demandé, nous recommandons
* sur Fir, un maximum de 12 cœurs CPU
* sur Narval, un maximum de 12 cœurs CPU
* sur Nibi, un maximum de 14 cœurs CPU
* sur Rorqual, un maximum de 16 cœurs CPU

## Tâches MPI 

**`gpu_mpi_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100:8             # nombre total de GPU
#SBATCH --ntasks-per-gpu=1        # 8 processus MPI au total
#SBATCH --cpus-per-task=6         # cœurs CPU par processus MPI
#SBATCH --mem-per-cpu=5G          # mémoire hôte par cœur CPU
#SBATCH --time=0-03:00            # temps de calcul (JJ-HH:MM)
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$SLURM_CPUS_PER_TASK ./program
```

## Nœuds entiers  
Si votre application peut utiliser efficacement un nœud entier et ses GPU associés, vous pouvez probablement réduire le temps d'attente si vous demandez un nœud entier. Utilisez les scripts suivants comme modèle. 

<span id="Packing_single-GPU_jobs_within_one_SLURM_job"></span>
### Regroupement de tâches pour un seul GPU

Pour exécuter pendant plus de 24 heures quatre programmes qui utilisent un seul GPU ou deux programmes qui utilisent deux GPU, nous recommandons [GNU Parallel](gnu-parallel-fr.md). Voici un exemple simple&nbsp;:
<pre>
cat params.input | parallel -j4 'CUDA_VISIBLE_DEVICES=$(({%} - 1)) python {} &> {#}.out'
</pre>
L'identifiant du GPU est calculé en soustrayant 1 de l'identifiant de la fente (<i>slot</i>), représenté par {%}. L'identifiant de la tâche est représenté par {#}, avec des valeurs partant de 1.

Le fichier `params.input` devrait contenir les paramètres sur des lignes distinctes, comme suit&nbsp;:
<pre>
code1.py
code2.py
code3.py
code4.py
...
</pre>
Vous pouvez ainsi soumettre plusieurs tâches. Le paramètre `-j4` fait en sorte que GNU Parallel exécutera quatre tâches concurremment en lançant une tâche aussitôt que la précédente est terminée. Pour éviter que deux tâches se disputent le même GPU, utilisez CUDA_VISIBLE_DEVICES.

<span id="Profiling_GPU_tasks"></span>
## Profilage des tâches avec GPU 

Sur [Narval](narval.md) et [Rorqual](rorqual.md) le profilage est possible, mais 
[DCGM (NVIDIA Data Center GPU Manager)](https://developer.nvidia.com/dcgm)
doit être désactivé. Ceci doit se faire lorsque vous soumettez la tâche en configurant la variable d'environnement `DISABLE_DCGM`.

```bash

```
1 salloc --accountdef-someuser --gpus-per-nodea100:1 --mem4000M --time03:00}}

Ensuite, dans votre tâche interactive, attendez que DCGM soit désactivé sur le nœud. 

```bash

```
 grep 'Hostengine build info:')" ]; do  sleep 5; done}}

Enfin, lancez le profileur (voir [débogage et profilage](debugging-and-profiling-fr.md) pour les détails).

Sur Fir et Nibi, le profilage de GPU décrit ci-dessus n'est pas encore disponible.

= Voir aussi =
[CUDA](cuda-fr.md)

[GPU multi-instances](multi-instance-gpu-fr.md)

[Exécuter des tâches](running-jobs-fr.md)

[Portail Metrix sur l'utilisation des ressources](metrix.md)

[NVTOP pour le suivi de l'utilisation des GPU](nvtop-fr.md)

[Cuda Multi-Process Service (MPS)](hyper-q_-_mps-fr.md)