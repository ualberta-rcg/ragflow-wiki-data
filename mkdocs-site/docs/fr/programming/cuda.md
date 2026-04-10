---
title: "CUDA/fr"
slug: "cuda"
lang: "fr"

source_wiki_title: "CUDA/fr"
source_hash: "2cc5bbfafd71bc6c6738cc46172b8f21"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:15:53.119646+00:00"

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

[CUDA](https://developer.nvidia.com/cuda-toolkit) est une plateforme de calcul parallèle et un modèle de programmation développé par NVIDIA pour des calculs généraux utilisant le GPU.

On peut voir CUDA comme étant un ensemble de bibliothèques et de compilateurs C, C++ et Fortran qui permettent de créer des programmes pour les GPU. Pour d'autres outils de programmation pour GPU, consultez le [Tutoriel OpenACC](openacc-tutorial.md).

## Un exemple simple

### Compilation
Nous exécutons ici du code créé avec le compilateur CUDA C/C++ `nvcc`. Ce même exemple plus détaillé se trouve à la page [Tutoriel CUDA](cuda-tutorial.md).

Chargez d'abord le [module](utiliser-des-modules.md) CUDA.
```bash
module purge
module load cuda
```

Dans cet exemple, nous additionnons deux nombres. Enregistrez le fichier sous `add.cu`; *le suffixe `cu` est important*.

```c++ title="add.cu"
#include <iostream>

__global__ void add (int *a, int *b, int *c){
  *c = *a + *b;
}

int main(void){
  int a, b, c;
  int *dev_a, *dev_b, *dev_c;
  int size = sizeof(int);
  
  //  allocate device copies of a,b, c
  cudaMalloc ( (void**) &dev_a, size);
  cudaMalloc ( (void**) &dev_b, size);
  cudaMalloc ( (void**) &dev_c, size);
  
  a=2; b=7;
  //  copy inputs to device
  cudaMemcpy (dev_a, &a, size, cudaMemcpyHostToDevice);
  cudaMemcpy (dev_b, &b, size, cudaMemcpyHostToDevice);
  
  // launch add() kernel on GPU, passing parameters
  add <<< 1, 1 >>> (dev_a, dev_b, dev_c);
  
  // copy device result back to host
  cudaMemcpy (&c, dev_c, size, cudaMemcpyDeviceToHost);
  std::cout<<a<<"+"<<b<<"="<<c<<std::endl;
  
  cudaFree ( dev_a ); cudaFree ( dev_b ); cudaFree ( dev_c );
}
```

Compilez le programme avec `nvcc` pour créer l'exécutable `add`.
```bash
nvcc add.cu -o add
```

### Soumission de tâches
Pour exécuter le programme, créez le script Slurm ci-dessous. Assurez-vous de remplacer `def-someuser` par votre nom de compte (voir [Comptes et projets](running-jobs.md#comptes-et-projets)). Pour les détails sur l'ordonnancement, consultez [Ordonnancement Slurm des tâches avec GPU](using-gpus-with-slurm.md).

```bash title="gpu_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:1              # Number of GPUs (per node)
#SBATCH --mem=400M                # memory (per node)
#SBATCH --time=0-00:10            # time (DD-HH:MM)
./add #name of your program
```

Soumettez la tâche à l'ordonnanceur.
```bash
sbatch gpu_job.sh
Submitted batch job 3127733
```
Pour plus d'information sur la commande `sbatch`, l'exécution et le suivi des tâches, consultez [Exécuter des tâches](running-jobs.md).

Le fichier en sortie sera semblable à ceci :
```text
cat slurm-3127733.out
2+7=9
```
Sans GPU, le résultat serait semblable à `2+7=0`.

### Lier des bibliothèques
Si votre programme doit établir des liens avec des bibliothèques incluses avec CUDA, par exemple [cuBLAS](https://developer.nvidia.com/cublas), compilez avec ces indicateurs :
```bash
nvcc -lcublas -Xlinker=-rpath,$CUDA_PATH/lib64
```

Voyez le [Tutoriel CUDA](cuda-tutorial.md) pour plus de détails sur cet exemple et pour savoir comment utiliser le parallélisme avec les GPU.

## Dépannage

### Attribut *compute capability*

NVIDIA utilise le terme *compute capability* pour désigner un des attributs des dispositifs GPU.

NVIDIA a créé ce terme technique qui indique les fonctionnalités prises en charge par ce GPU et spécifie certains paramètres matériels de ce dernier.

Pour plus de détails, consultez [Compute Capability and Streaming Multiprocessor Versions](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/cuda-platform.html#cuda-platform-compute-capability-sm-version).

Les messages d’erreur suivants sont causés par un problème en rapport avec cet attribut.

```text
nvcc fatal : Unsupported gpu architecture 'compute_XX'
```

```text
no kernel image is available for execution on the device (209)
```

L'ajout d'un indicateur dans l'appel `nvcc` pourrait résoudre ces problèmes.

```text
-gencode arch=compute_XX,code=[sm_XX,compute_XX]
```

Si vous utilisez `cmake`, l'indicateur serait

```bash
cmake .. -DCMAKE_CUDA_ARCHITECTURES=XX
```

où XX est la valeur de *compute capability* pour le GPU NVIDIA qui sera utilisé pour exécuter votre application. Pour connaître ces valeurs, voir [CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus) et omettez le point décimal.

**Par exemple**, si votre code sera exécuté sur un nœud A100 de Narval, le tableau de NVIDIA mentionne que sa *compute capability* a la valeur de *8.0*.
L'indicateur à utiliser lors de la compilation avec `nvcc` est

```text
-gencode arch=compute_80,code=[sm_80,compute_80]
```

L'indicateur pour `cmake` est

```bash
cmake .. -DCMAKE_CUDA_ARCHITECTURES=80