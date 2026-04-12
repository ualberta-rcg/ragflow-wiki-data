---
title: "OpenACC Tutorial - Optimizing loops/fr"
slug: "openacc_tutorial_-_optimizing_loops"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Optimizing loops/fr"
source_hash: "5240c4154a2b14f15c397f6257662336"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:57:09.155451+00:00"

tags:
  []

keywords:
  - "OpenACC"
  - "device_type"
  - "reduction"
  - "device_type(nvidia)"
  - "xcoefs"
  - "parallélisation de boucle"
  - "K20"
  - "pragma acc loop"
  - "clauses d'optimisation"
  - "Analyse guidée"
  - "GPU NVIDIA"
  - "GPU"
  - "niveau de parallélisme"
  - "NVIDIA Visual Profiler"
  - "row_offsets"
  - "CUDA"
  - "Acoefs"
  - "Optimisation des gangs"
  - "méthode de Jacobi"
  - "niveaux de parallélisme"
  - "Contrôle du parallélisme"
  - "loop"
  - "temps d'exécution"
  - "vector"
  - "compilateur"

questions:
  - "Pourquoi la parallélisation par défaut du compilateur avec `vector(128)` génère-t-elle des calculs inutiles pour la matrice présentée dans le texte ?"
  - "Quels sont les trois niveaux de parallélisme offerts par OpenACC (vector, worker, gang) et comment interagissent-ils entre eux ?"
  - "Quelle est la correspondance générale établie par le compilateur entre les niveaux de parallélisme d'OpenACC et l'architecture CUDA ?"
  - "Quelle est la correspondance générale entre les éléments OpenACC (vector, worker, gang) et l'architecture CUDA ?"
  - "Quelle directive peut-on utiliser pour contrôler le niveau de parallélisme d'une boucle ?"
  - "Quel est le rôle des clauses associées à la directive « loop » lors de la compilation ?"
  - "Quels sont les différents niveaux de parallélisme disponibles dans OpenACC et dans quel ordre hiérarchique doivent-ils être imbriqués ?"
  - "Comment la clause `device_type` permet-elle de spécifier et d'optimiser l'exécution du code pour un type d'accélérateur particulier, tel qu'un GPU NVIDIA ?"
  - "De quelle manière peut-on contrôler la taille des niveaux de parallélisme (comme la longueur de `vector`) et quelles sont les contraintes matérielles associées ?"
  - "Quelles sont les étapes à suivre dans le NVIDIA Visual Profiler pour identifier les goulots d'étranglement d'un noyau spécifique ?"
  - "Quelles informations clés le profileur révèle-t-il concernant l'occupation du GPU et la taille des blocs (gangs) lors de l'analyse de latence ?"
  - "Comment doit-on ajuster les directives OpenACC en ajoutant des « workers » pour maximiser l'utilisation des capacités d'un GPU NVIDIA ?"
  - "Quel changement spécifique dans le code OpenACC est testé dans cet extrait ?"
  - "Comment le temps d'exécution sur l'architecture K20 est-il affecté par cette modification ?"
  - "Pourquoi l'augmentation du temps d'exécution démontre-t-elle l'habileté initiale du compilateur ?"
  - "Quel est l'impact sur les performances de la parallélisation explicite des boucles avec les niveaux `worker` et `vector` par rapport à l'optimisation automatique du compilateur ?"
  - "Dans quels cas spécifiques est-il recommandé d'utiliser les clauses d'optimisation `collapse` et `tile` lors de la parallélisation des boucles ?"
  - "Quel est l'objectif de l'exercice pratique proposé concernant l'équation de Laplace et comment permet-il de mettre en application les concepts d'OpenACC ?"
  - "What mathematical operation is being implemented by the nested loops and array accesses in this code snippet?"
  - "How do the OpenACC pragmas in the code optimize parallel execution for specific hardware architectures?"
  - "What sparse matrix representation format is implied by the use of the `row_offsets`, `cols`, and `Acoefs` arrays?"
  - "Quel est l'impact sur les performances de la parallélisation explicite des boucles avec les niveaux `worker` et `vector` par rapport à l'optimisation automatique du compilateur ?"
  - "Dans quels cas spécifiques est-il recommandé d'utiliser les clauses d'optimisation `collapse` et `tile` lors de la parallélisation des boucles ?"
  - "Quel est l'objectif de l'exercice pratique proposé concernant l'équation de Laplace et comment permet-il de mettre en application les concepts d'OpenACC ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "Objectifs d'apprentissage"
*   comprendre les différents niveaux de parallélisme dans un GPU
*   comprendre les messages du compilateur au sujet de la parallélisation
*   savoir obtenir des suggestions d'optimisation par le profileur visuel
*   savoir indiquer au compilateur les paramètres de parallélisation

## Se montrer plus habile que le compilateur
Jusqu'ici, le compilateur a fait du bon travail; dans les étapes précédentes, le gain en performance a triplé en comparaison de celle du CPU. Étudions maintenant comment le compilateur a parallélisé le code et donnons-lui si possible un coup de main. Pour ce faire, il faut comprendre les différents niveaux de parallélisme possibles avec OpenACC, particulièrement avec un GPU NVIDIA. Examinons d'abord la rétroaction fournie par le compilateur pendant la compilation de la dernière version (dans `steps2.kernels`).

```bash
pgc++ -fast -ta=tesla,lineinfo -Minfo=all,intensity,ccff -c -o main.o main.cpp
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

*   Les fils `vector` exécutent une seule opération sur plusieurs données (SIMD), en une seule étape. S'il y a moins de données que la longueur du vecteur, l'opération est exécutée quand même sur des valeurs NULL et le résultat est rejeté.
*   La clause `worker` calcule un `vector`.
*   Le niveau `gang` comprend un `worker` ou plus, qui partagent des ressources telles que la mémoire cache ou le processeur. Chaque `gang` travaille de manière complètement indépendante.

!!! info "Correspondance entre OpenACC et CUDA"
    OpenACC étant conçu pour des accélérateurs génériques, il n'y a pas de correspondance directe avec les fils, blocs et warps CUDA. Dans la version 2.0 d'OpenACC, les niveaux sont imbriqués allant de l'extérieur avec `gang` vers l'intérieur avec `vector`. La correspondance OpenACC-CUDA est établie par le compilateur. Nous savons qu'il pourrait y avoir des exceptions, mais la correspondance suivante est généralement valide.
    *   `vector` OpenACC => fils CUDA
    *   `worker` OpenACC => warps CUDA
    *   `gang` OpenACC => blocs de fils CUDA

## Contrôle du parallélisme
On peut utiliser `loop` avec certaines clauses pour contrôler le niveau de parallélisme que le compilateur doit produire pour la boucle. Ces clauses sont :
*   `gang`, qui produit le niveau de parallélisme `gang`
*   `worker`, qui produit le niveau de parallélisme `worker`
*   `vector`, qui produit le niveau de parallélisme `vector`
*   `seq`, qui exécute la boucle séquentiellement sans parallélisme

Une boucle peut avoir plusieurs clauses de niveau, mais il faut les placer de l'extérieur vers l'intérieur (de `gang` à `vector`).

### Spécifier le type d'accélérateur
Dépendant de comment la parallélisation est appelée à se dérouler, les différents types d'accélérateurs n'auront pas la même performance. La clause OpenACC `device_type` permet de spécifier le type d'accélérateur auquel s'applique la clause qui la succède dans le libellé du code. Par exemple, `device_type(nvidia) vector` se réalise uniquement si le code est compilé pour un GPU NVIDIA.

### Spécifier la taille de chaque niveau de parallélisme
Un paramètre de taille peut être ajouté aux clauses `vector`, `worker` et `gang`. Par exemple, `worker(32) vector(32)` crée 32 workers pour effectuer des calculs sur des vecteurs de longueur 32.

!!! warning "Valeurs maximales"
    Certains accélérateurs peuvent avoir des nombres limite de `vector`, `worker` et `gang` pour paralléliser une boucle. Dans le cas des GPUs NVIDIA,
    *   la longueur de `vector` est un multiple de 32 (1024 au plus);
    *   la taille de `gang` est le produit du nombre de `worker` multiplié par la taille de `vector` (1204 au plus).

## Contrôler la longueur de `vector`
Revenons à notre exemple; nous avions remarqué que le compilateur avait fixé à 128 la longueur de `vector`. Comme nous savons que les rangées contiennent 27 éléments, nous pouvons diminuer à 32 la longueur de `vector`. Avec la directive `kernels`, voici comment se présente le code :

```cpp hl_lines="7"
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

```cpp hl_lines="2 8"
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

## Analyse guidée du NVIDIA Visual Profiler

Comme nous avons fait dans la section *Performance du code porté* de la leçon [Ajouter des directives](https://docs.computecanada.ca/wiki/OpenACC_Tutorial_-_Adding_directives/fr), ouvrez NVIDIA Visual Profiler et démarrez une nouvelle session avec le dernier exécutable que nous avons produit. Effectuez les étapes qui suivent :
1.  Sous l'onglet *Analyse*, cliquez sur *Examiner l'utilisation du GPU*. À la fin de l'analyse, le compilateur produit une série d'avertissements qui indiquent les améliorations possibles.
2.  Cliquez sur *Examiner les noyaux individuels* pour faire afficher la liste des noyaux.
3.  Sélectionnez le premier de la liste et cliquez sur *Analyser le noyau*. Le profileur présente une analyse détaillée du noyau et indique les goulots d'étranglement probables. Dans ce cas, la performance est limitée par la latence de la mémoire.
4.  Cliquez sur *Analyser la latence*.

À la fin de la procédure, les renseignements suivants devraient être affichés :

Nous avons ici plusieurs renseignements importants :
*   le texte indique clairement que la performance est limitée par la taille des blocs, ce qui correspond à la taille des gangs en OpenACC;
*   la ligne *Fils actifs* nous informe que le GPU exécute 512 fils sur les 2048 possibles;
*   la ligne *Taux d'occupation* montre que le GPU est utilisé à 25% de sa capacité; il s'agit du ratio de l'utilisation réelle sur l'utilisation possible du GPU. Remarquez qu'une occupation à 100% ne donne pas nécessairement la meilleure performance, mais 25% est plutôt bas;

*   Les réponses les plus utiles se trouvent dans le tableau *Warps*.
    *   On y apprend que le GPU exécute 32 fils par bloc (en OpenACC, des fils vector par gang) alors qu'il pourrait en exécuter 1024.
    *   On voit aussi que le GPU exécute 1 warp par bloc (en OpenACC, 1 worker par gang) alors qu'il pourrait en exécuter 32.
    *   Sur la dernière ligne, on voit que pour que l'accélérateur fonctionne à son plein rendement, il faudrait exécuter 64 gangs, mais l'accélérateur peut seulement en traiter 16.

La conclusion est que nous avons besoin de gangs plus grands, ce que nous ferons en ajoutant des workers tout en gardant la taille du vecteur à 32.

## Ajouter des `worker`s
Puisque nous savons que pour un GPU NVIDIA la taille d'un `gang` ne peut pas dépasser 1024 et que cette taille est le produit de la longueur de `vector` multipliée par la quantité de `worker`s, nous voulons avoir 32 `worker`s par gang. Avec la directive `kernels`, le code se lit :

```cpp hl_lines="3"
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

```cpp hl_lines="3"
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
*   La clause `collapse(N)` est utilisée avec une directive de boucle pour replier les N prochaines boucles en une même boucle plate. Elle sert dans les cas de boucles imbriquées ou quand les boucles sont très courtes.
*   La clause `tile(N,[M,...])` répartit les boucles suivantes dans une structure en mosaïque avant de paralléliser. Elle est utile dans le cas d'un algorithme à forte localité parce que l'accélérateur peut utiliser les données de carreaux environnants.

## Exercice
!!! challenge "Itérations de Jacobi"
    Mettez en pratique ce que vous avez appris sur OpenACC.
    Dans le répertoire `bonus` se trouve du code qui résout l'[équation de Laplace](https://fr.wikipedia.org/wiki/%C3%89quation_de_Laplace) avec la [méthode de Jacobi](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Jacobi). Portez ce code sur un GPU et observez le gain en performance que vous obtenez.

[Retour au début du tutoriel](https://docs.computecanada.ca/wiki/OpenACC_Tutorial/fr)