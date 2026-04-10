---
title: "Chapel/fr"
tags:
  - software

keywords:
  []
---

Chapel est un langage de programmation parallèle compilé de haut niveau à usage général avec des abstractions intégrées pour le parallélisme à mémoire partagée et distribuée. Chapel offre deux styles de programmation parallèle&nbsp;: (1) le <b>parallélisme de tâches</b>, où le parallélisme se fait par des tâches spécifiées par programmation, et (2) le <b>parallélisme de données</b>, où le parallélisme se fait en effectuant les mêmes calculs sur des sous-ensembles de données qui peuvent se trouver dans la mémoire partagée d'un nœud unique ou être distribués sur plusieurs nœuds.

Ces abstractions de haut niveau font de Chapel l'outil idéal pour apprendre la programmation parallèle pour le calcul de haute performance. Ce langage est incroyablement intuitif et s'efforce de fusionner la facilité d'utilisation de [Python](python-fr.md) avec les performances des langages compilés traditionnels tels que [C](c-fr.md) et [Fortran](fortran-fr.md). Les blocs parallèles qui prennent généralement des dizaines de lignes de code [MPI](mpi-fr.md) peuvent être exprimés en seulement quelques lignes de code Chapel. Chapel est <i>open source</i> et peut fonctionner sur n'importe quel système d'exploitation de type Unix, avec une prise en charge matérielle des ordinateurs portables aux grands systèmes de CHP.

Chapel a une base d'utilisateurs relativement petite, donc de nombreuses bibliothèques qui existent pour [C](c-fr.md), [C++](c++-fr.md) et [Fortran](fortran-fr.md) n'ont pas encore été implémentées dans Chapel. Espérons que cela changera dans les années à venir, si l'adoption de Chapel continue de prendre de l'ampleur dans la communauté de CHP.

Pour plus d'information, voyez [nos webinaires Chapel](https://westgrid.github.io/trainingMaterials/programming/#chapel).

<span id="Single-locale_Chapel"></span>
## Calculs simples 

Le module `chapel-multicore` est utilisé sur nos grappes d'usage général avec un nœud unique et une mémoire partagée seulement. Vous pouvez utiliser `salloc` pour tester si votre code fonctionne en séquentiel.

```bash

```
0:30:0 --ntasks1 --mem-per-cpu3600 --accountdef-someprof
|chpl test.chpl -o test
|./test
}}
ou avec plusieurs cœurs sur un même nœud&nbsp;:

```bash

```
0:30:0 --ntasks1 --cpus-per-task3 --mem-per-cpu3600 --accountdef-someprof
|chpl test.chpl -o test
|./test
}}
Pour les tâches de production, veuillez préparer un [script de soumission de tâche](running-jobs-fr.md) et le soumettre avec `sbatch`.

<span id="Multi-locale_Chapel"></span>
## Calculs distribués 

Pour des tâches avec plusieurs nœuds et une mémoire hybride (partagée et distribuée) sur nos grappes InfiniBand, chargez le module `chapel-ofi`.

Le code suivant imprime l'information de base au sujet des nœuds disponibles dans votre tâche.
{{
File
  |name=probeLocales.chpl
  |lang="chapel"
  |contents=
use MemDiagnostics;
for loc in Locales do
  on loc {
    writeln("locale #", here.id, "...");
    writeln("  ...is named: ", here.name);
    writeln("  ...has ", here.numPUs(), " processor cores");
    writeln("  ...has ", here.physicalMemory(unit=MemUnits.GB, retType=real), " GB of memory");
    writeln("  ...has ", here.maxTaskPar, " maximum parallelism");
  }
}}

Pour exécuter ce code sur june grappe InfiniBand, vous devez charger le module`chapel-ucx`.

```bash

```
0:30:0 --nodes4 --cpus-per-task3 --mem-per-cpu3500 --accountdef-someprof
}}

Une fois que la [[Running_jobs/fr#Tâches_interactives|] tâche interactive] est lancée, vous pouvez compiler et exécuter votre code à partir de l'invite sur le premier nœud de calcul alloué.

```bash
./probeLocales -nl 4
```

Pour les tâches de production, veuillez préparer un [script de soumission de tâche](running-jobs-fr.md) et soumettre la tâche avec `sbatch`.

<span id="Multi-locale_Chapel_with_NVIDIA_GPU_support"></span>
## Calcul distribué avec les GPU NVIDIA 

Pour utiliser un GPU, chargez le module `chapel-ucx-cuda` qui supporte les GPU NVIDIA sur nos grappes InfiniBand.

Ceci est du code de base pour utiliser un GPU avec Chapel.
{{
File
  |name=probeGPU.chpl
  |lang="chapel"
  |contents=
use GpuDiagnostics;
startGpuDiagnostics();
writeln("Locales: ", Locales);
writeln("Current locale: ", here, " named ", here.name, " with ", here.maxTaskPar, " CPU cores",
	" and ", here.gpus.size, " GPUs");
// same code can run on GPU or CPU
var operateOn =
  if here.gpus.size > 0 then here.gpus[0]   // use the first GPU
  else here;                                // use the CPU
writeln("operateOn: ", operateOn);
on operateOn {
  var A : [1..10] int;
  @assertOnGpu foreach a in A do // thread parallelism on a CPU or a GPU
    a += 1;
  writeln(A);
}
stopGpuDiagnostics();
writeln(getGpuDiagnostics());
}}

Pour exécuter ce code sur une grappe InfiniBand, chargez le module `chapel-ucx-cuda`.

```bash

```
0:30:0 --mem-per-cpu3500 --gpus-per-node1 --accountdef-someprof
}}

Une fois que la [[Running_jobs/fr#Tâches_interactives|] tâche interactive] est lancée, vous pouvez compiler et exécuter votre code à partir de l'invite sur le nœud de calcul alloué.

```bash
./probeGPU -nl 1
```

Pour les tâches de production, veuillez préparer un [script de soumission de tâche](running-jobs-fr.md) et soumettre la tâche avec `sbatch`.