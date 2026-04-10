---
title: "OpenACC Tutorial - Optimizing loops/fr"
slug: "openacc_tutorial_-_optimizing_loops"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Optimizing loops/fr"
source_hash: "5240c4154a2b14f15c397f6257662336"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:27:43.872513+00:00"

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

!!! info "Objectifs d'apprentissage"
    * Comprendre les différents niveaux de parallélisme dans un processeur graphique (GPU).
    * Comprendre les messages du compilateur au sujet de la parallélisation.
    * Savoir obtenir des suggestions d'optimisation par le profileur visuel.
    * Savoir indiquer au compilateur les paramètres de parallélisation.

## Se montrer plus habile que le compilateur
Jusqu'ici, le compilateur a fait du bon travail; dans les étapes précédentes, le gain en performance a triplé en comparaison de celle du processeur central (CPU). Étudions maintenant comment le compilateur a parallélisé le code et donnons-lui si possible un coup de main. Pour ce faire, il faut comprendre les différents niveaux de parallélisme possibles avec OpenACC, particulièrement avec un processeur graphique (GPU) NVIDIA. Examinons d'abord la rétroaction fournie par le compilateur pendant la compilation de la dernière version (dans steps2.kernels).

```bash
pgc++ -fast -ta=tesla,lineinfo -Minfo=all,intensity,ccff   -c -o main.o main.cpp
```

```text
...
initialize_vector(vector &, double):
...
          42, Intensity = 0.0
              Loop is parallelizable
              Accelerator kernel generated
              Generating Tesla code
              42, #pragma acc loop gang, vector(128) /* blockIdx.x threadIdx.x */
dot(const vector &, const vector &):
...
          29, Intensity = 1.00    
              Loop is parallelizable
              Accelerator kernel generated
              Generating Tesla code
              29, #pragma acc loop gang, vector(128) /* blockIdx.x threadIdx.x */
              30, Sum reduction generated for sum
waxpby(double, const vector &, double, const vector &, const vector &):
...
          44, Intensity = 1.00    
              Loop is parallelizable
              Accelerator kernel generated
              Generating Tesla code
              44, #pragma acc loop gang, vector(128) /* blockIdx.x threadIdx.x */
```
Remarquez que chaque boucle est parallélisée avec `vector(128)`; ceci signifie que le compilateur a généré des instructions pour un bloc de code de longueur 128. C'est ici que le programmeur possède un avantage. En fait, si vous examinez le contenu du fichier `matrix.h`, vous verrez que chaque rangée de la matrice possède 27 éléments; le compilateur a donc généré des instructions pour le calcul inutile de 101 éléments. Nous verrons plus loin comment traiter ce cas.

## Niveaux de parallélisme OpenACC
Les trois niveaux possibles de parallélisme avec OpenACC sont `vector`, `worker` et `gang`.

* Les fils `vector` exécutent une seule opération sur plusieurs données (SIMD), en une seule étape. S'il y a moins de données que la longueur du vecteur, l'opération est exécutée quand même sur des valeurs NULL et le résultat est rejeté.
* La clause `worker` calcule un `vector`.
* Le niveau `gang` comprend un `worker` ou plus, qui partagent des ressources telles que la mémoire cache ou le processeur.
Chaque `gang` travaille de manière complètement indépendante.

!!! note "Correspondance entre OpenACC et CUDA"
    OpenACC étant conçu pour des accélérateurs génériques, il n'y a pas de correspondance directe avec les fils, blocs et warps CUDA. Dans la version 2.0 d'OpenACC, les niveaux sont imbriqués allant de l'extérieur avec `gang` vers l'intérieur avec `vector`. La correspondance OpenACC-CUDA est établie par le compilateur. Nous savons qu'il pourrait y avoir des exceptions, mais la correspondance suivante est généralement valide.
    * `vector` OpenACC => fils CUDA
    * `worker` OpenACC => warps CUDA
    * `gang` OpenACC => blocs de fils CUDA

## Contrôle du parallélisme
On peut utiliser `loop` avec certaines clauses pour contrôler le niveau de parallélisme que le compilateur doit produire pour la boucle. Ces clauses sont :
* `gang`, qui produit le niveau de parallélisme `gang`
* `worker`, qui produit le niveau de parallélisme `worker`
* `vector`, qui produit le niveau de parallélisme `vector`
* `seq`, qui exécute la boucle séquentiellement sans parallélisme
Une boucle peut avoir plusieurs clauses de niveau, mais il faut les placer de l'extérieur vers l'intérieur (de `gang` à `vector`).

### Spécifier le type d'accélérateur
Dépendant de comment la parallélisation est appelée à se dérouler, les différents types d'accélérateurs n'auront pas la même performance. La clause OpenACC `device_type` permet de spécifier le type d'accélérateur auquel s'applique la clause qui la succède dans le libellé du code. Par exemple, `device_type(nvidia) vector` se réalise uniquement si le code est compilé pour un processeur graphique (GPU) NVIDIA.

### Spécifier la taille de chaque niveau de parallélisme
Un paramètre de taille peut être ajouté aux clauses `vector`, `worker` et `gang`. Par exemple, `worker(32) vector(32)` crée 32 workers pour effectuer des calculs sur des vecteurs de longueur 32.

!!! note "Valeurs maximales"
    Certains accélérateurs peuvent avoir des nombres limite de `vector`, `worker` et `gang` pour paralléliser une boucle. Dans le cas des processeurs graphiques (GPU) NVIDIA,
    * la longueur de `vector` est un multiple de 32 (1024 au plus);
    * la taille de `gang` est le produit du nombre de `worker` multiplié par la taille de `vector` (1204 au plus).

## Contrôler la longueur de `vector`
Revenons à notre exemple; nous avions remarqué que le compilateur avait fixé à 128 la longueur de `vector`. Comme nous savons que les rangées contiennent 27 éléments, nous pouvons diminuer à 32 la longueur de `vector`. Avec la directive `kernels`, voici comment se présente le code :

```cpp
#pragma acc kernels present(row_offsets,cols,Acoefs,xcoefs,ycoefs)
  {
    for(int i=0;i<num_rows;i++) {
      double sum=0;
      int row_start=row_offsets[i];
      int row_end=row_offsets[i+1];
#pragma acc loop device_type(nvidia) vector(32)
      for(int j=row_start;j<row_end;j++) {
        unsigned int Acol=cols[j];
        double Acoef=Acoefs[j];
        double xcoef=xcoefs[Acol];
        sum+=Acoef*xcoef;
      }
      ycoefs[i]=sum;
    }
  }
```
Si vous préférez la directive `parallel loop`, la longueur de `vector` est définie au niveau de la boucle la plus externe avec la clause `vector_length`. La clause vector est ensuite utilisée pour paralléliser une boucle interne via le niveau vector, ce qui donne :

```cpp
#pragma acc parallel loop present(row_offsets,cols,Acoefs,xcoefs,ycoefs) \
        device_type(nvidia) vector_length(32)
  for(int i=0;i<num_rows;i++) {
    double sum=0;
    int row_start=row_offsets[i];
    int row_end=row_offsets[i+1];
#pragma acc loop reduction(+:sum) \
        device_type(nvidia) vector
    for(int j=row_start;j<row_end;j++) {
      unsigned int Acol=cols[j];
      double Acoef=Acoefs[j];
      double xcoef=xcoefs[Acol];
      sum+=Acoef*xcoef;
    }
    ycoefs[i]=sum;
  }
```
Si vous faites ce changement, vous verrez que sur un K20, le temps d'exécution passe de 10 à environ 15 secondes. Le compilateur démontre ici son habileté.

## Analyse guidée du profileur visuel NVIDIA

Comme nous avons fait dans la section ''Performance du code porté'' de la leçon [Ajouter des directives](openacc-tutorial-ajouter-des-directives.md), ouvrez NVIDIA Visual Profiler et démarrez une nouvelle session avec le dernier exécutable que nous avons produit. Effectuez les étapes qui suivent :
1. Sous l'onglet **Analyse**, cliquez sur **Examiner l'utilisation du processeur graphique**. À la fin de l'analyse, le compilateur produit une série d'avertissements qui indiquent les améliorations possibles.
2. Cliquez sur **Examiner les noyaux individuels** pour faire afficher la liste des noyaux.
3. Sélectionnez le premier de la liste et cliquez sur **Effectuer l'analyse du noyau**. Le profileur présente une analyse détaillée du noyau et indique les goulots d'étranglement probables. Dans ce cas, la performance est limitée par la latence de la mémoire.
4. Cliquez sur **Effectuer l'analyse de latence**.

À la fin de la procédure, les renseignements suivants devraient être affichés :
Nous avons ici plusieurs renseignements importants :
* le texte indique clairement que la performance est limitée par la taille des blocs, ce qui correspond à la taille des gangs en OpenACC;
* la ligne ''Fils d'exécution actifs'' nous informe que le processeur graphique exécute 512 fils sur les 2048 possibles;
* la ligne ''Occupation'' montre que le processeur graphique est utilisé à 25% de sa capacité; il s'agit du ratio de l'utilisation réelle sur l'utilisation possible du processeur graphique. Remarquez qu'une occupation à 100% ne donne pas nécessairement la meilleure performance, mais 25% est plutôt bas;

* Les réponses les plus utiles se trouvent dans la table ''Warps''.
    * On y apprend que le processeur graphique exécute 32 fils par bloc (en OpenACC, des fils vector par gang) alors qu'il pourrait en exécuter 1024.
    * On voit aussi que le processeur graphique exécute 1 warp par bloc (en OpenACC, 1 worker par gang) alors qu'il pourrait en exécuter 32.
    * Sur la dernière ligne, on voit que pour que l'accélérateur fonctionne à son plein rendement, il faudrait exécuter 64 gangs, mais l'accélérateur peut seulement en traiter 16.
La conclusion est que nous avons besoin de gangs plus grands, ce que nous ferons en ajoutant des workers tout en gardant la taille du vecteur à 32.

## Ajouter des `worker`s
Puisque nous savons que pour un processeur graphique (GPU) NVIDIA la taille d'un `gang` ne peut pas dépasser 1024 et que cette taille est le produit de la longueur de `vector` multipliée par la quantité de `worker`s, nous voulons avoir 32 `worker`s par gang. Avec la directive `kernels`, le code se lit :

```cpp
#pragma acc kernels present(row_offsets,cols,Acoefs,xcoefs,ycoefs)
  {
#pragma acc loop device_type(nvidia) gang worker(32)
    for(int i=0;i<num_rows;i++) {
      double sum=0;
      int row_start=row_offsets[i];
      int row_end=row_offsets[i+1];
#pragma acc loop device_type(nvidia) vector(32)
      for(int j=row_start;j<row_end;j++) {
        unsigned int Acol=cols[j];
        double Acoef=Acoefs[j];
        double xcoef=xcoefs[Acol];
        sum+=Acoef*xcoef;
      }
      ycoefs[i]=sum;
    }
  }
```
Remarquez que nous parallélisons la boucle externe workers puisque la boucle interne est déjà au niveau de parallélisme `vector`.

Avec la directive `parallel loop`, le code se lit :

```cpp
#pragma acc parallel loop present(row_offsets,cols,Acoefs,xcoefs,ycoefs) \
        device_type(nvidia) vector_length(32) \
        gang worker num_workers(32)
  for(int i=0;i<num_rows;i++) {
    double sum=0;
    int row_start=row_offsets[i];
    int row_end=row_offsets[i+1];
#pragma acc loop reduction(+:sum) \
        device_type(nvidia) vector
    for(int j=row_start;j<row_end;j++) {
      unsigned int Acol=cols[j];
      double Acoef=Acoefs[j];
      double xcoef=xcoefs[Acol];
      sum+=Acoef*xcoef;
    }
    ycoefs[i]=sum;
  }
```
Cette étape supplémentaire résulte en une performance près du double de celle que compilateur peut faire de lui-même. Sur un K20, le code prenait 10 secondes à exécuter et la durée est maintenant de 6 secondes.

## Deux autres clauses d'optimisation
Jusqu'ici nous n'avons pas mentionné deux clauses qui sont très utiles dans l'optimisation des boucles.
* La clause **`collapse(N)`** est utilisée avec une directive de boucle pour replier les N prochaines boucles en une même boucle plate. Elle sert dans les cas de boucles imbriquées ou quand les boucles sont très courtes.
* La clause **`tile(N,[M,...])`** répartit les boucles suivantes dans une structure en mosaïque avant de paralléliser. Elle est utile dans le cas d'un algorithme à forte localité parce que l'accélérateur peut utiliser les données de carreaux environnants.

## Exercice
!!! question "Itérations de Jacobi"
    Mettez en pratique ce que vous avez appris sur OpenACC.
    Dans le répertoire `bonus` se trouve du code qui résout l'[équation de Laplace](https://fr.wikipedia.org/wiki/%C3%89quation_de_Laplace) avec la [méthode de Jacobi](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Jacobi). Portez ce code sur un processeur graphique (GPU) et observez le gain en performance que vous obtenez.
[Retour au début du tutoriel](openacc-tutorial.md)