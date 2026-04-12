---
title: "Chapel/fr"
slug: "chapel"
lang: "fr"

source_wiki_title: "Chapel/fr"
source_hash: "de4c4e75a8cef5ea6a88dad284ed2fec"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:14:47.891652+00:00"

tags:
  - software

keywords:
  - "mémoire partagée"
  - "calculs distribués"
  - "calcul de haute performance"
  - "GPU NVIDIA"
  - "calcul distribué"
  - "chapel-ucx"
  - "tâche interactive"
  - "maximum parallelism"
  - "grappe InfiniBand"
  - "processor cores"
  - "physicalMemory"
  - "soumission de tâche"
  - "Chapel"
  - "programmation parallèle"

questions:
  - "Quels sont les deux styles de programmation parallèle offerts par le langage Chapel et en quoi consistent-ils ?"
  - "Quels sont les avantages de Chapel en termes de performances et de facilité d'utilisation par rapport à des langages comme Python, C ou MPI, et quelle est sa principale limitation actuelle ?"
  - "Quels modules et commandes doivent être utilisés pour compiler et exécuter un code Chapel sur un seul nœud (mémoire partagée) par rapport à une exécution sur plusieurs nœuds (mémoire distribuée) ?"
  - "Quelle commande est recommandée pour soumettre des tâches de production au lieu d'utiliser une tâche interactive ?"
  - "Quel module spécifique doit être chargé pour activer le support des GPU NVIDIA sur les grappes InfiniBand avec Chapel ?"
  - "Quelles sont les commandes de base fournies pour compiler et exécuter un programme Chapel une fois l'allocation des ressources obtenue ?"
  - "Quelles caractéristiques matérielles du système le code Chapel permet-il d'afficher ?"
  - "Quel module spécifique doit être chargé pour permettre l'exécution de ce code sur une grappe InfiniBand ?"
  - "Quelle est la commande exacte fournie pour charger l'environnement nécessaire à l'exécution ?"
  - "Quelle commande est recommandée pour soumettre des tâches de production au lieu d'utiliser une tâche interactive ?"
  - "Quel module spécifique doit être chargé pour activer le support des GPU NVIDIA sur les grappes InfiniBand avec Chapel ?"
  - "Quelles sont les commandes de base fournies pour compiler et exécuter un programme Chapel une fois l'allocation des ressources obtenue ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Chapel est un langage de programmation parallèle compilé de haut niveau à usage général, doté d'abstractions intégrées pour le parallélisme à mémoire partagée et distribuée. Chapel offre deux styles de programmation parallèle : (1) le **parallélisme de tâches**, où le parallélisme est spécifié par programme, et (2) le **parallélisme de données**, où le parallélisme s'effectue en réalisant les mêmes calculs sur des sous-ensembles de données qui peuvent se trouver dans la mémoire partagée d'un seul nœud ou être distribués sur plusieurs nœuds.

Ces abstractions de haut niveau font de Chapel l'outil idéal pour apprendre la programmation parallèle en calcul de haute performance. Ce langage est incroyablement intuitif et vise à fusionner la facilité d'utilisation de [Python](python.md) avec les performances des langages compilés traditionnels tels que [C](../programming/c.md) et [Fortran](../programming/fortran.md). Les blocs parallèles qui nécessitent généralement des dizaines de lignes de code [MPI](mpi.md) peuvent être exprimés en seulement quelques lignes de code Chapel. Chapel est *open source* et peut fonctionner sur n'importe quel système d'exploitation de type Unix, avec une prise en charge matérielle allant des ordinateurs portables aux grands systèmes de CHP.

Chapel a une base d'utilisateurs relativement petite, de sorte que de nombreuses bibliothèques existantes pour [C](../programming/c.md), [C++](cpp.md) et [Fortran](../programming/fortran.md) n'ont pas encore été implémentées en Chapel. Espérons que cela changera dans les années à venir si l'adoption de Chapel continue de prendre de l'ampleur au sein de la communauté de CHP.

Pour plus d'information, consultez [nos webinaires Chapel](https://westgrid.github.io/trainingMaterials/programming/#chapel).

## Calculs simples

Le module `chapel-multicore` est utilisé sur nos grappes d'usage général avec un nœud unique et une mémoire partagée seulement. Vous pouvez utiliser `salloc` pour vérifier si votre code fonctionne en séquentiel.

```bash
module load gcc/12.3 chapel-multicore/2.4.0
salloc --time=0:30:0 --ntasks=1 --mem-per-cpu=3600 --account=def-someprof
chpl test.chpl -o test
./test
```

ou avec plusieurs cœurs sur un même nœud :

```bash
module load gcc/12.3 chapel-multicore/2.4.0
salloc --time=0:30:0 --ntasks=1 --cpus-per-task=3 --mem-per-cpu=3600 --account=def-someprof
chpl test.chpl -o test
./test
```

Pour les tâches de production, veuillez préparer un [script de soumission de tâche](../running-jobs/running_jobs.md) et le soumettre avec `sbatch`.

## Calculs distribués

Pour des tâches avec plusieurs nœuds et une mémoire hybride (partagée et distribuée) sur nos grappes InfiniBand, chargez le module `chapel-ofi`.

Le code suivant affiche l'information de base concernant les nœuds disponibles dans votre tâche.

::: chapel probeLocales.chpl
```chapel
use MemDiagnostics;
for loc in Locales do
  on loc {
    writeln("locale #", here.id, "...");
    writeln("  ...is named: ", here.name);
    writeln("  ...has ", here.numPUs(), " processor cores");
    writeln("  ...has ", here.physicalMemory(unit=MemUnits.GB, retType=real), " GB of memory");
    writeln("  ...has ", here.maxTaskPar, " maximum parallelism");
  }
```

Pour exécuter ce code sur une grappe InfiniBand, vous devez charger le module `chapel-ucx`.

```bash
module load gcc/12.3 chapel-ucx/2.4.0
salloc --time=0:30:0 --nodes=4 --cpus-per-task=3 --mem-per-cpu=3500 --account=def-someprof
```

Une fois que la [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives) est lancée, vous pouvez compiler et exécuter votre code à partir de l'invite sur le premier nœud de calcul alloué.

```bash
chpl --fast probeLocales.chpl -o probeLocales
./probeLocales -nl 4
```

Pour les tâches de production, veuillez préparer un [script de soumission de tâche](../running-jobs/running_jobs.md) et soumettre la tâche avec `sbatch`.

## Calcul distribué avec les GPU NVIDIA

Pour utiliser un GPU, chargez le module `chapel-ucx-cuda` qui prend en charge les GPU NVIDIA sur nos grappes InfiniBand.

Ceci est du code de base pour utiliser un GPU avec Chapel.

::: chapel probeGPU.chpl
```chapel
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
```

Pour exécuter ce code sur une grappe InfiniBand, chargez le module `chapel-ucx-cuda`.

```bash
module load gcc/12.3 cuda/12.2 chapel-ucx-cuda/2.4.0
salloc --time=0:30:0 --mem-per-cpu=3500 --gpus-per-node=1 --account=def-someprof
```

Une fois que la [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives) est lancée, vous pouvez compiler et exécuter votre code à partir de l'invite sur le nœud de calcul alloué.

```bash
chpl --fast probeGPU.chpl
./probeGPU -nl 1
```

Pour les tâches de production, veuillez préparer un [script de soumission de tâche](../running-jobs/running_jobs.md) et soumettre la tâche avec `sbatch`.