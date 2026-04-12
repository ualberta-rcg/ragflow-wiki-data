---
title: "CUDA tutorial/fr"
slug: "cuda_tutorial"
lang: "fr"

source_wiki_title: "CUDA tutorial/fr"
source_hash: "a8a045b229f306c058c1fd25516973d9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:07:38.661347+00:00"

tags:
  - software

keywords:
  - "modèle SIMT"
  - "mémoire CPU"
  - "blocs CUDA"
  - "copies de mémoire"
  - "blocs de fils"
  - "mémoire GPU"
  - "kernel"
  - "exemple simple"
  - "accélération"
  - "mémoire constante"
  - "__global__"
  - "mémoire partagée"
  - "GPU"
  - "CPU"
  - "cudaMalloc"
  - "parallélisation"
  - "CUDA"
  - "Bande passante"
  - "programmation parallèle"
  - "mémoire globale"
  - "PCI-e"
  - "parallélisme intensif"
  - "carte graphique"
  - "fils parallèles"
  - "stratégies de programmation"
  - "ordonnancement des fils"

questions:
  - "Qu'est-ce qu'un GPU et comment son architecture matérielle est-elle structurée pour le calcul de haute performance ?"
  - "Quelles sont les cinq étapes fondamentales du modèle de programmation CUDA impliquant l'hôte (CPU) et la carte graphique (GPU) ?"
  - "Comment le modèle d'exécution SIMT gère-t-il les fonctions GPU (kernels) et l'organisation des fils d'exécution (threads) ?"
  - "Qu'est-ce que le modèle SIMT mentionné pour l'exécution simultanée du kernel ?"
  - "Quelles sont les trois étapes de la procédure recommandée pour transférer les données et exécuter le programme entre le CPU et le GPU ?"
  - "Comment les fils sont-ils organisés et structurés au sein des blocs et des grilles ?"
  - "Comment les fils d'exécution sont-ils organisés hiérarchiquement dans CUDA et comment partagent-ils l'information ?"
  - "Comment l'ordonnanceur gère-t-il l'exécution des blocs de fils sur les processeurs en continu (SM) pour optimiser le temps de calcul ?"
  - "Quels sont les différents types de mémoire GPU disponibles et quelles fonctions de base permettent de gérer l'allocation et le transfert des données ?"
  - "Quelle est la différence principale entre la parallélisation par blocs et la parallélisation par fils (threads) dans CUDA ?"
  - "Quel est l'avantage d'utiliser la mémoire partagée par rapport à la mémoire globale, et quelles sont ses limites de communication ?"
  - "Pourquoi est-il crucial de minimiser les transferts de données entre l'hôte (CPU) et la carte graphique (GPU) pour optimiser les performances ?"
  - "Pourquoi l'auteur précise-t-il qu'il ne faut pas s'attendre à une grande accélération avec cet exemple ?"
  - "Quel est le rôle spécifique de la fonction `__global__ void add` dans ce programme ?"
  - "À quoi sert la fonction `cudaMalloc` appelée dans la fonction principale ?"
  - "Comment peut-on évaluer et optimiser l'utilisation de la bande passante lors de l'analyse des temps d'exécution ?"
  - "Pourquoi la mémoire constante offre-t-elle un accès hautement efficace en lecture seule bien qu'elle réside dans la DRAM ?"
  - "Quelle est la stratégie recommandée pour répartir les données entre les mémoires globale, partagée, constante et les registres selon le mode d'accès ?"
  - "Pourquoi le bus PCI-e représente-t-il un goulot d'étranglement par rapport à la mémoire de l'hôte et de la carte graphique ?"
  - "Quelles sont les stratégies recommandées pour minimiser l'impact des transferts de mémoire entre le CPU et le GPU ?"
  - "Pourquoi peut-il être préférable d'exécuter une tâche non optimale sur le GPU plutôt que de la confier au CPU ?"
  - "Comment peut-on évaluer et optimiser l'utilisation de la bande passante lors de l'analyse des temps d'exécution ?"
  - "Pourquoi la mémoire constante offre-t-elle un accès hautement efficace en lecture seule bien qu'elle réside dans la DRAM ?"
  - "Quelle est la stratégie recommandée pour répartir les données entre les mémoires globale, partagée, constante et les registres selon le mode d'accès ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Dans ce tutoriel, nous présentons la composante de calcul hautement parallèle qu'est le processeur graphique (ou GPU pour *graphics processing unit*); le langage de programmation parallèle [CUDA](cuda.md); et quelques-unes des librairies numériques CUDA utilisées en calcul de haute performance.

!!! info "Prérequis"
    Ce tutoriel montre comment utiliser CUDA pour accélérer des programmes en C ou C++; une bonne connaissance d'un de ces langages vous permettra d'en tirer le meilleur profit. Si CUDA sert aussi aux programmes en Fortran, nous nous limiterons ici à CUDA pour C/C++ et utiliserons le terme **CUDA C**. Il s'agit essentiellement de produire des fonctions en C/C++ pouvant être exécutées par les CPUs et les GPUs.

!!! info "Objectifs d'apprentissage"
    * Comprendre l'architecture d'un GPU
    * Comprendre le déroulement d'un programme CUDA
    * Comprendre et gérer les différents types de mémoires GPU
    * Écrire et compiler un exemple de code CUDA

## Qu'est-ce qu'un GPU?

Un GPU (pour *graphics processing unit*) est un processeur monopuce capable d'effectuer des calculs mathématiques rapidement pour produire des rendus d'images.
Depuis quelques années, la puissance du GPU sert aussi à accélérer l'exécution de calculs intensifs dans plusieurs domaines de la recherche scientifique de pointe.

## Qu'est-ce que CUDA?

CUDA (*compute unified device architecture*) est un environnement logiciel et un modèle de programmation évolutif pour le traitement de calculs parallèles intensifs sur GPU.

## Architecture du GPU

Un GPU se compose :
* d'une mémoire globale
    * semblable à la mémoire CPU
    * accessible par CPU et GPU
* des multiprocesseurs en continu (SM pour *streaming multiprocessors*)
    * chaque SM est composé de plusieurs processeurs en continu (SP pour *streaming processors*)
    * ils effectuent les calculs
    * chaque SM est doté d'une unité de contrôle, de registres, de pipelines d'exécution, etc. qui lui sont propres

## Modèle de programmation

Voyons d'abord quelques termes importants :
* **Hôte** : désigne le CPU et sa mémoire (mémoire hôte).
* **Carte graphique** : désigne le GPU et sa mémoire (mémoire de la carte graphique).

Le modèle CUDA est un modèle hétérogène où à la fois le CPU et le GPU sont utilisés. Le code CUDA peut gérer les deux types de mémoires : la mémoire hôte et la mémoire de la carte graphique. Le code exécute aussi les fonctions du GPU appelées `kernels` (noyaux). Ces fonctions sont exécutées en parallèle par plusieurs fils GPU. Le processus comporte cinq étapes :
1. Déclaration et allocation de la mémoire hôte et de la mémoire de la carte graphique.
2. Initialisation de la mémoire hôte.
3. Transfert des données de la mémoire hôte à la mémoire de la carte graphique.
4. Exécution des fonctions GPU (*kernels*).
5. Retour des données à la mémoire hôte.

## Modèle d'exécution

Le code CUDA simple exécuté dans un GPU s'appelle `kernel`. Il faut se demander :
* comment faire pour exécuter un `kernel` sur un groupe de multiprocesseurs en continu?
* comment faire pour que ce `kernel` soit exécuté de façon parallèle intensive?

Voici la recette en réponse à ces questions :
* chaque cœur GPU (processeur en continu) exécute un fil (*thread*) séquentiel, ce qui est le plus petit ensemble discret d'instructions géré par l'ordonnanceur du système d'exploitation
* tous les cœurs GPU exécutent le `kernel` de manière simultanée selon le modèle SIMT (*single instruction, multiple threads*)

La procédure suivante est recommandée :
1. Copier les données en entrée de la mémoire CPU à la mémoire GPU.
2. Charger puis lancer le programme GPU (le `kernel`).
3. Copier les résultats de la mémoire GPU à la mémoire CPU.

## Blocs de fils

Pour obtenir un parallélisme intensif, on doit utiliser le plus de fils possible; puisqu'un `kernel` CUDA comprend un très grand nombre de fils, il faut bien les organiser. Avec CUDA, les fils sont groupés en blocs de fils, eux-mêmes formant une grille. Diviser les fils fait en sorte que :
* les fils groupés coopèrent via la mémoire partagée,
* les fils d'un bloc ne coopèrent pas avec les fils des autres blocs.

Selon ce modèle, les fils dans un bloc travaillent sur le même groupe d'instructions (mais peut-être avec des jeux de données différents) et s'échangent les données via la mémoire partagée. Les fils dans les autres blocs font de même.

Chaque fil utilise des identifiants (IDs) pour décider quelles données utiliser :
* IDs des blocs : 1D ou 2D (`blockIdx.x`, `blockIdx.y`)
* IDs des fils : 1D, 2D, ou 3D (`threadIdx.x`, `threadIdx.y`, `threadIdx.z`)

Ce modèle simplifie l'adressage de la mémoire lors du traitement de données multidimensionnelles.

## Ordonnancement des fils

Un processeur en continu (SM) exécute habituellement un bloc de fils à la fois. Le code est exécuté en groupes de 32 fils (appelés *warps*). Un ordonnanceur physique est libre d'assigner des blocs à tout SM en tout temps. De plus, quand un SM reçoit le bloc qui lui est assigné, ceci ne signifie pas que ce bloc en particulier sera exécuté sans arrêt. En fait, l'ordonnanceur peut retarder/suspendre l'exécution de tels blocs selon certaines conditions, par exemple si les données ne sont plus disponibles (en effet, la lecture de données à partir de la mémoire globale du GPU exige beaucoup de temps). Lorsque ceci se produit, l'ordonnanceur exécute un autre bloc de fils qui est prêt à être exécuté. Il s'agit en quelque sorte d'ordonnancement *zero-overhead* favorisant un flux d'exécution plus régulier afin que les SM ne demeurent pas inactifs.

## Types de mémoire GPU

Plusieurs types de mémoire sont disponibles aux opérations CUDA :
* mémoire globale
    * non sur la puce (*off-chip*), efficace pour opérations I/O, mais relativement lente
* mémoire partagée
    * sur la puce (*on-chip*), permet une bonne collaboration des fils, très rapide
* registres et mémoire locale
    * espace de travail des fils, très rapide
* mémoire constante

## Quelques opérations de base

### Allocation de la mémoire
* `cudaMalloc((void**)&array, size)`
    * Allocation d'objet dans la mémoire de la carte graphique. Nécessite l'adresse d'un pointeur vers les données allouées et la taille.
* `cudaFree(array)`
    * Désallocation de l'objet dans la mémoire. Nécessite uniquement le pointeur vers les données.

### Transfert de données
* `cudaMemcpy(array_dest, array_orig, size, direction)`
    * Copie les données de la carte graphique vers l'hôte ou de l'hôte vers la carte graphique. Nécessite les pointeurs vers les données, la taille et le type de direction (`cudaMemcpyHostToDevice`, `cudaMemcpyDeviceToHost`, `cudaMemcpyDeviceToDevice`, etc.)
* `cudaMemcpyAsync`
    * Identique à `cudaMemcpy`, mais transfère les données de manière asynchrone, ce qui signifie que l'exécution des autres processus n'est pas bloquée.

## Exemple d'un programme CUDA C simple

Dans cet exemple, nous additionnons deux nombres. Il s'agit d'un exemple très simple et il ne faut pas s'attendre à observer une grande accélération.

```cpp hl_lines="1 5"
__global__ void add (int *a, int *b, int *c){
  *c = *a + *b;
}

int main(void){
  int a, b, c;
  int *dev_a, *dev_b, *dev_c;
  int size = sizeof(int);

  // Alloue la mémoire pour a, b et c sur l'appareil
  cudaMalloc ( (void**) &dev_a, size);
  cudaMalloc ( (void**) &dev_b, size);
  cudaMalloc ( (void**) &dev_c, size);

  a=2; b=7;
  // Copie les données d'entrée vers l'appareil
  cudaMemcpy (dev_a, &a, size, cudaMemcpyHostToDevice);
  cudaMemcpy (dev_b, &b, size, cudaMemcpyHostToDevice);

  // Lance le noyau add() sur le GPU, en passant les paramètres
  add <<< 1, 1 >>> (dev_a, dev_b, dev_c);

  // Copie le résultat de l'appareil vers l'hôte
  cudaMemcpy (&c, dev_c, size, cudaMemcpyDeviceToHost);

  cudaFree ( dev_a ); cudaFree ( dev_b ); cudaFree ( dev_c );
}
```

Il manque certainement quelque chose; ce code n'a pas une allure parallèle… Comme solution, modifions le contenu du `kernel` entre les chevrons triples (`<<< >>>`).

```cpp hl_lines="1 5"
add <<< N, 1 >>> (dev_a, dev_b, dev_c);
```

Ici, nous avons remplacé 1 par N pour que N blocs CUDA différents soient exécutés en même temps. Pour paralléliser cependant, il faut aussi faire des modifications au `kernel` :

```cpp hl_lines="1 5"
__global__   void add (int *a, int *b, int *c){
  c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x];
```

où `blockIdx.x` est le numéro unique identifiant un bloc CUDA. De cette manière, chaque bloc CUDA ajoute une valeur de `a[ ]` à `b[ ]`.

Modifions à nouveau le contenu entre les chevrons triples.

```cpp hl_lines="1 5"
add <<< 1, **N** >>> (dev_a, dev_b, dev_c);
```

La tâche est maintenant distribuée sur des fils parallèles plutôt que sur des blocs. Quel est l'avantage des fils parallèles? Contrairement aux blocs, les fils peuvent communiquer entre eux; autrement dit, nous parallélisons sur plusieurs fils dans le bloc lorsque la communication est intense. Les portions de code qui peuvent être exécutées indépendamment, soit avec peu ou pas de communication, sont distribuées sur des blocs parallèles.

## Avantages de la mémoire partagée

Jusqu'ici, tous les transferts en mémoire dans le `kernel` ont été via la mémoire régulière (globale) du GPU, ce qui est relativement lent. Il y a souvent tellement de communication entre fils que la performance est significativement diminuée. Pour contrer ce problème, nous pouvons utiliser la mémoire partagée qui peut accélérer les transferts en mémoire entre les fils. Le secret par contre est que seuls les fils du même bloc peuvent communiquer. Pour illustrer l'utilisation de cette mémoire, voyons l'exemple du produit scalaire où deux vecteurs sont multipliés élément par élément et additionnés par la suite, ainsi :

```cpp hl_lines="1 5"
__global__   void dot(int *a, int *b, int *c){
  int temp = a[threadIdx.x]*b[threadIdx.x]; 
}
```

Après que chaque fil a exécuté sa portion, il faut tout additionner; chaque fil doit partager ses données. Toutefois, le problème est que chaque copie de la variable temporaire du fil est privée. La solution est d'utiliser la mémoire partagée avec les modifications suivantes au `kernel` :

```cpp hl_lines="1 4"
#define N 512
__global__   void dot(int *a, int *b, int *c){
  __shared__ int temp[N];
  temp[threadIdx.x] = a[threadIdx.x]*b[threadIdx.x];
  __syncthreads();
  if(threadIdx.x==0){
    int sum; for(int i=0;i<N;i++) sum+= temp[i];
    *c=sum;
  }
}
```

## Facteurs de performance de base

### Transferts entre mémoires
* PCI-e est extrêmement lent (4-6 Go/s) en comparaison à la mémoire hôte et à la mémoire de la carte graphique.
* Minimisez les copies de mémoire dans les deux sens.
* Gardez les données sur la carte graphique le plus longtemps possible.
* Il n'est parfois pas efficace d'utiliser l'hôte (le CPU) pour des tâches non optimales; il pourrait être plus rapide de les exécuter avec le GPU que de les copier vers le CPU, de les exécuter et d'en retourner le résultat.
* Utilisez les temps de mémoire pour analyser les temps d'exécution.

### Bande passante
* Tenez toujours compte des limites de la bande passante lorsque vous modifiez votre code.
* Connaissez la bande passante de pointe théorique des différents liens de données.
* Comptez les octets écrits/lus et comparez-les avec la pointe théorique.
* Utilisez les différents types de mémoire selon le cas : globale, partagée, constante.

### Stratégies usuelles de programmation
* La mémoire constante réside aussi dans la DRAM; l'accès est beaucoup plus lent que pour la mémoire partagée.

    !!! tip "À noter"
        mais, elle est **mise en cache** !

* Accès hautement efficace en lecture seule, transmission.
* Répartissez bien les données selon le mode d'accès :
    * Lecture seule : mémoire constante (très rapide si dans le cache)
    * Lecture/écriture dans le bloc : mémoire partagée (très rapide)
    * Lecture/écriture dans le fil : registres (très rapide)
    * Lecture/écriture en entrée/résultats : mémoire globale (très lent)