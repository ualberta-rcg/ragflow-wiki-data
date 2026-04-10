---
title: "OpenACC Tutorial - Adding directives/fr"
slug: "openacc_tutorial_-_adding_directives"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Adding directives/fr"
source_hash: "d41cb399a73cde93207fcf33b3a79630"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:23:21.722516+00:00"

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

*   comprendre le processus de transfert (*offloading*)
*   comprendre ce qu'est une directive OpenACC
*   connaître la différence entre les directives `loop` et `kernels`
*   savoir programmer avec OpenACC
*   comprendre le concept d'alias en C/C++
*   savoir utiliser la rétroaction du compilateur et éviter les faux alias

## Transfert vers un processeur graphique (GPU)

Avant de porter du code sur un GPU, il faut savoir que ceux-ci ne partagent pas la même mémoire que le CPU de l'hôte.

*   la mémoire de l'hôte est en général plus grande, mais plus lente que la mémoire du GPU;
*   un GPU n'a pas d'accès direct à la mémoire de l'hôte;
*   pour pouvoir utiliser un GPU, les données doivent passer par le bus PCI, dont la bande passante est moins grande que celles du CPU et du GPU;
*   il est donc de la plus haute importance de bien gérer les transferts entre la mémoire de départ et le GPU. En anglais, ce processus s'appelle *offloading*.

## Directives OpenACC

Les directives OpenAcc sont semblables aux directives [OpenMP](openmp.md). En C/C++, ce sont des énoncés `pragmas` et en Fortran, des commentaires. L'emploi de directives comporte plusieurs avantages :

*   Premièrement, puisque le code est peu affecté, les modifications peuvent se faire de manière incrémentale, un `pragma` à la fois; ceci est particulièrement utile pour le débogage puisqu'il est ainsi facile d'identifier le changement précis qui crée le bogue.
*   Deuxièmement, OpenACC peut être désactivé au moment de la compilation; les `pragmas` sont alors vus comme étant des commentaires et ne sont pas considérés par le compilateur, ce qui permet de compiler une version accélérée et une version normale à partir du même code source.
*   Troisièmement, comme le compilateur fait tout le travail de transfert, le même code peut être compilé pour différents types d'accélérateurs, que ce soit un GPU ou des instructions SIMD sur un CPU; ainsi, un changement du matériel exigera simplement la mise à jour du compilateur, sans modification au code.

Le code de notre exemple contient deux boucles : la première initialise deux vecteurs et la seconde effectue une opération de [niveau 1](https://fr.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) d'addition des vecteurs.

| C/C++                       | FORTRAN                      |
| :-------------------------- | :--------------------------- |
| ```cpp hl_lines="1 2 13"    | ```fortran hl_lines="1 7"    |
| #pragma acc kernels         | !$acc kernels                |
| {                           |   do i=1,N                   |
|   for (int i=0; i<N; i++)   |     x(i) = 1.0               |
|   {                         |     y(i) = 2.0               |
|     x[i] = 1.0;             |   end do                     |
|     y[i] = 2.0;             |                              |
|   }                         |   y(:) = a*x(:) + y(:)       |
|                             | !$acc end kernels            |
|   for (int i=0; i<N; i++)   | ```                          |
|   {                         |                              |
|     y[i] = a * x[i] + y[i]; |                              |
|   }                         |                              |
| }                           |                              |
| ```                         |                              |

Dans les deux cas, le compilateur identifie deux noyaux (*kernels*) :

*   en C/C++, les deux noyaux sont à l'intérieur de chaque boucle;
*   en Fortran, les noyaux sont à l'intérieur de la première boucle et à l'intérieur de la boucle implicite effectuée lors d'une opération sur des tableaux.

Remarquez que le bloc OpenACC est délimité en C/C++ par des accolades; en Fortran, le commentaire est placé une fois au début et une dernière fois à la fin, avec l'ajout cette fois de `end`.

### Boucles et noyaux

Quand le compilateur lit la directive OpenACC `kernels`, il analyse le code pour identifier les sections pouvant être parallélisées. Ceci correspond souvent au corps d'une boucle qui a des itérations indépendantes. Dans ce cas, le compilateur délimite le début et la fin du corps du code avec la fonction [*kernel*](https://en.wikipedia.org/wiki/Compute_kernel). Les appels à cette fonction ne seront pas affectés par les autres appels. La fonction est compilée et peut ensuite être exécutée sur un accélérateur. Comme chaque appel est indépendant, chacun des centaines de cœurs de l'accélérateur peut exécuter la fonction en parallèle pour un index spécifique.

| BOUCLE                           | KERNEL                         |
| :------------------------------- | :----------------------------- |
| ```cpp                          | ```cpp                        |
| for (int i=0; i<N; i++)          | void kernelName(A, B, C, i)    |
| {                                | {                              |
|   C[i] = A[i] + B[i];            |   C[i] = A[i] + B[i];          |
| }                                | }                              |
| ```                              | ```                            |
| Calcule séquentiellement de `i=0` à `i=N-1`, inclusivement. | Chaque unité de calcul exécute la fonction pour une seule valeur de `i`. |

## La directive `kernels`

Cette directive est dite *descriptive*. Le programmeur l'utilise pour signifier au compilateur les portions qui selon lui peuvent être parallélisées. Le compilateur fait ce qu'il veut de cette information et adopte la stratégie qui lui semble la meilleure pour exécuter le code, **incluant** son exécution séquentielle. De façon générale, le compilateur

1.  analyse le code pour détecter le parallélisme,
2.  s'il détecte du parallélisme, identifie les données à transférer et décide quand faire le transfert,
3.  crée un *kernel*,
4.  transfère le *kernel* au GPU.

Voici un exemple de cette directive :

```cpp hl_lines="1 2 7"
#pragma acc kernels
{
  for (int i=0; i<N; i++)
  {
    C[i] = A[i] + B[i];
  }
}
```

Il est rare que le code soit aussi simple et il faut se baser sur la [rétroaction du compilateur](../profiling/#renseignements-sur-le-compilateur) pour trouver les portions qu'il a négligé de paralléliser.

!!! note "Description ou prescription"

    Si vous avez déjà utilisé [OpenMP](openmp.md), vous retrouverez dans OpenACC le principe de *directives*. Il existe cependant d'importantes différences entre les directives OpenMP et OpenACC :

    *   Les directives OpenMP sont à la base *prescriptives*. Ceci signifie que le compilateur est forcé d'accomplir la parallélisation, peu importe que l'effet détériore ou améliore la performance. Le résultat est prévisible pour tous les compilateurs. De plus, la parallélisation se fera de la même manière, peu importe le matériel utilisé pour exécuter le code. Par contre, le même code peut connaître une moins bonne performance, dépendant de l'architecture. Il peut donc être préférable par exemple de changer l'ordre des boucles. Pour paralléliser du code avec OpenMP et obtenir une performance optimale dans différentes architectures, il faudrait avoir un ensemble différent de directives pour chaque architecture.

    *   Pour leur part, plusieurs directives OpenACC sont de nature *descriptive*. Ici, le compilateur est libre de compiler le code de la façon qu'il juge la meilleure, selon l'architecture visée. Dans certains cas, le code ne sera pas parallélisé du tout. Le **même code** exécuté sur un GPU ou sur un CPU peut donner du code binaire différent. Ceci signifie que la performance pourrait varier selon le compilateur et que les compilateurs d'une nouvelle génération seront plus efficaces, surtout en présence de nouveau matériel.

### Exemple : porter un produit matrice-vecteur

Pour notre exemple, nous utilisons du code provenant du [répertoire Github](https://github.com/calculquebec/cq-formation-openacc), particulièrement une portion de code [fichier `cpp/matrix_functions.h`](https://github.com/calculquebec/cq-formation-openacc/blob/main/cpp/matrix_functions.h#L20). Le code Fortran équivalent se trouve dans la sous-routine [`matvec` contenue dans le fichier `matrix.F90`](https://github.com/calculquebec/cq-formation-openacc/blob/main/f90/matrix.F90#L101). Le code C++ est comme suit :

```cpp
  for(int i=0;i<num_rows;i++) {
    double sum=0;
    int row_start=row_offsets[i];
    int row_end=row_offsets[i+1];
    for(int j=row_start;j<row_end;j++) {
      unsigned int Acol=cols[j];
      double Acoef=Acoefs[j];
      double xcoef=xcoefs[Acol];
      sum+=Acoef*xcoef;
    }
    ycoefs[i]=sum;
  }
```

Le [premier changement](https://github.com/calculquebec/cq-formation-openacc/blob/main/cpp/step1.kernels/matrix_functions.h#L29) à faire au code est d'ajouter la directive `kernels` pour essayer de le faire exécuter sur le GPU. Pour l'instant, nous n'avons pas à nous préoccuper du transfert des données ou à fournir des renseignements au compilateur.

```cpp hl_lines="1 2 15"
#pragma acc kernels
  {
    for(int i=0;i<num_rows;i++) {
      double sum=0;
      int row_start=row_offsets[i];
      int row_end=row_offsets[i+1];
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

#### Construire avec OpenACC

Les compilateurs NVidia utilisent l'option `-acc` pour permettre la compilation pour un accélérateur. Nous utilisons la sous-option `-gpu=managed` pour indiquer au compilateur que nous voulons utiliser la [mémoire gérée](https://developer.nvidia.com/blog/unified-memory-cuda-beginners/) pour simplifier le transfert de données en provenance et à destination du périphérique; nous n'utiliserons pas cette option dans un prochain exemple. Nous utilisons aussi l'option `-fast` pour l'optimisation.

```bash
nvc++ -fast -Minfo=accel -acc -gpu=managed main.cpp -o challenge
```

```text
...
matvec(const matrix &, const vector &, const vector &):
     23, include "matrix_functions.h"
          30, Generating implicit copyin(cols[:],row_offsets[:num_rows+1],Acoefs[:]) [if not already present]
              Generating implicit copyout(ycoefs[:num_rows]) [if not already present]
              Generating implicit copyin(xcoefs[:]) [if not already present]
          31, Loop carried dependence of ycoefs-> prevents parallelization
              Loop carried backward dependence of ycoefs-> prevents vectorization
              Complex loop carried dependence of Acoefs->,xcoefs-> prevents parallelization
              Generating NVIDIA GPU code
              31, #pragma acc loop seq
              35, #pragma acc loop vector(128) /* threadIdx.x */
                  Generating implicit reduction(+:sum)
          35, Loop is parallelizable
```

Le résultat montre que la boucle externe sur la ligne 31 n'a pas pu être parallélisée par le compilateur. Dans la prochaine section, nous expliquons comment traiter ces dépendances.

## Réparer les fausses dépendances de boucles

Même lorsque le programmeur sait qu'une boucle peut être parallélisée, il arrive que le compilateur ne le remarque pas. Un cas commun en C/C++ est connu sous le nom de [*pointer aliasing*](https://en.wikipedia.org/wiki/Pointer_aliasing). Contrairement au Fortran, C/C++ ne possèdent pas comme tel de tableaux (*arrays*), mais plutôt des pointeurs. Le concept d'alias s'applique à deux pointeurs dirigés vers la même mémoire. Si le compilateur ne sait pas que des pointeurs ne sont pas des alias, il doit cependant le supposer. Dans l'exemple précédent, on voit clairement pourquoi le compilateur ne pouvait pas paralléliser la boucle. En supposant que les pointeurs sont identiques, il y a forcément dépendance des itérations de la boucle.

### Mot-clé `restrict`

Une des manières de dire au compilateur que les pointeurs **ne sont pas** des alias est d'utiliser le mot-clé `restrict`, introduit à cette fin dans C99. Il n'y a toujours pas de manière standard pour ce faire en C++, mais chaque compilateur possède un mot-clé qui lui est propre. Dépendant du compilateur, on peut utiliser `__restrict` ou `__restrict__`. Les compilateurs du Portland Group et de NVidia utilisent `__restrict`. Pour savoir pourquoi il n'existe pas de standard en C++, consultez [ce document](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2014/n3988.pdf). Ce concept est important pour OpenACC comme pour toute programmation C/C++, car les compilateurs peuvent effectuer plusieurs autres optimisations si les pointeurs ne sont pas des alias. Remarquez que le mot-clé se place **après** le pointeur puisque c'est à ce dernier qu'il se réfère, et non au type; autrement dit, la déclaration doit se lire `float * __restrict A;` plutôt que `float __restrict * A;`.

!!! note "Utilisation du mot-clé `restrict`"

    En déclarant un pointeur comme étant *restreint*, on s'assure qu'uniquement ce pointeur ou une valeur dérivée (comme `ptr +1`) pourra accéder à l'objet auquel il réfère, et ce pour la durée de vie du pointeur. Ceci est une garantie que le programmeur donne au compilateur; si le programmeur manque à son obligation, le comportement n'est pas défini. Pour plus d'information, consultez l'article Wikipédia [restrict](https://en.wikipedia.org/wiki/Restrict).

### Boucle avec clause `independent`

Une autre façon de s'assurer que le compilateur traite les boucles de manière indépendante est de le spécifier explicitement avec la clause `independent`. Comme toute autre directive *prescriptive*, le compilateur y est obligé et l'analyse qu'il pourrait faire ne sera pas considérée. En reprenant l'exemple de la section *La directive `kernels`* ci-dessus, nous avons :

```cpp hl_lines="3"
#pragma acc kernels
{
#pragma acc loop independent
for (int i=0; i<N; i++)
{
  C[i] = A[i] + B[i];
}
}
```

### Produit matrice-vecteur

Revenons au cas du produit matrice-vecteur présenté plus haut. Notre recommandation pour éviter les faux alias est de définir les pointeurs comme étant restreints en remplaçant le code de `matrix_functions.h`.

```cpp
  double *Acoefs=A.coefs;
  double *xcoefs=x.coefs;
  double *ycoefs=y.coefs;
```

par le code

```cpp
  double *__restrict Acoefs=A.coefs;
  double *__restrict xcoefs=x.coefs;
  double *__restrict ycoefs=y.coefs;
```

Remarquez que les autres pointeurs n'ont pas besoin d'être restreints puisque le compilateur ne les rapporte pas comme causant des problèmes. En recompilant avec les changements que nous venons de faire, le compilateur émet le message suivant :

```bash
nvc++ -fast -Minfo=accel -acc -gpu=managed main.cpp -o challenge
```

```text
matvec(const matrix &, const vector &, const vector &):
     23, include "matrix_functions.h"
          27, Generating implicit copyout(ycoefs[:num_rows]) [if not already present]
              Generating implicit copyin(xcoefs[:],row_offsets[:num_rows+1],Acoefs[:],cols[:]) [if not already present]
          30, Loop is parallelizable
              Generating Tesla code
              30, #pragma acc loop gang /* blockIdx.x */
              34, #pragma acc loop vector(128) /* threadIdx.x */
                  Generating implicit reduction(+:sum)
          34, Loop is parallelizable
```

## Performance du code porté

Maintenant que le code est porté sur le GPU, nous pouvons analyser sa performance et vérifier si les résultats sont corrects. L'exécution du code original sur un nœud GPU produit ceci :

```bash
./cg.x
```

```text
Rows: 8120601, nnz: 218535025
Iteration: 0, Tolerance: 4.0067e+08
Iteration: 10, Tolerance: 1.8772e+07
Iteration: 20, Tolerance: 6.4359e+05
Iteration: 30, Tolerance: 2.3202e+04
Iteration: 40, Tolerance: 8.3565e+02
Iteration: 50, Tolerance: 3.0039e+01
Iteration: 60, Tolerance: 1.0764e+00
Iteration: 70, Tolerance: 3.8360e-02
Iteration: 80, Tolerance: 1.3515e-03
Iteration: 90, Tolerance: 4.6209e-05
Total Iterations: 100 Total Time: 29.894881s
```

Voici le résultat pour la version OpenACC :

```bash
./challenge
```

```text
Rows: 8120601, nnz: 218535025
Iteration: 0, Tolerance: 4.0067e+08
Iteration: 10, Tolerance: 1.8772e+07
Iteration: 20, Tolerance: 6.4359e+05
Iteration: 30, Tolerance: 2.3202e+04
Iteration: 40, Tolerance: 8.3565e+02
Iteration: 50, Tolerance: 3.0039e+01
Iteration: 60, Tolerance: 1.0764e+00
Iteration: 70, Tolerance: 3.8360e-02
Iteration: 80, Tolerance: 1.3515e-03
Iteration: 90, Tolerance: 4.6209e-05
Total Iterations: 100 Total Time: 115.068931s
```

Les résultats sont corrects, toutefois, loin de gagner en vitesse, l'opération a pris près de quatre fois plus de temps! Utilisons le NVidia Visual Profiler (`nvvp`) pour voir ce qui se passe.

### NVIDIA Visual Profiler

[NVIDIA Visual Profiler (NVVP)](https://developer.nvidia.com/nvidia-visual-profiler) est un profileur graphique pour les applications OpenACC. C'est un outil d'analyse pour les **codes écrits avec les directives OpenACC et CUDA C/C++**. En conséquence, si l'exécutable n'utilise pas le GPU, ce profileur ne fournira aucun résultat.

Quand [X11 est redirigé vers un serveur X-Server](../visualization/#fenetres-a-distance-avec-redirection-x11) ou quand vous utilisez un [environnement bureau Linux](../vnc/) (aussi via [JupyterHub](../jupyterhub/#bureau) avec 2 cœurs CPU, 5000M de mémoire et 1 GPU), vous pouvez lancer NVVP à partir d'un terminal :

```bash
module load cuda/11.7 java/1.8
```

```bash
nvvp
```

1.  Après l'affichage de la fenêtre de lancement de NVVP, vous devez entrer le répertoire *Workspace* qui sera employé pour les fichiers temporaires. Dans le chemin suggéré, remplacez `home` par `scratch` et cliquez sur *OK*.
2.  Sélectionnez *File > New Session* ou cliquez sur le bouton correspondant dans la barre d'outils.
3.  Cliquez sur le bouton *Browse* à la droite du champ *File* pour le chemin.
    *   Changez le répertoire s'il y a lieu.
    *   Sélectionnez un exécutable construit avec des codes écrits avec des directives OpenACC et CUDA C/C++.
4.  Sous le champ *Arguments*, sélectionnez l'option *Profile current process only*.
5.  Cliquez sur *Next >* pour voir les autres options de profilage.
6.  Cliquez sur *Finish* pour lancer le profilage de l'exécutable.

Pour faire ceci, suivez ces étapes :

1.  Lancez `nvvp` avec la commande `nvvp &` (le symbole `&` commande le lancement en arrière-plan).
2.  Sélectionnez *File -> New Session*.
3.  Dans le champ *File:*, cherchez l'exécutable (nommé dans notre exemple `challenge`).
4.  Cliquez sur *Next* jusqu'à ce que vous puissiez cliquer sur *Finish*.

Le programme est exécuté et on obtient un tableau chronologique du déroulement. On remarque que le transfert de données entre le départ et l'arrivée occupe la plus grande partie du temps d'exécution, ce qui est fréquent quand du code est porté d'un CPU vers un GPU. Nous verrons comment ceci peut être amélioré dans la prochaine partie, [Mouvement des données](openacc-tutorial-data-movement.md).

## La directive `parallel loop`

Avec la directive `kernels`, c'est le compilateur qui fait toute l'analyse; ceci est une approche *descriptive* pour porter du code. OpenACC offre aussi une approche *prescriptive* avec la directive `parallel` qui peut être combinée à la directive `loop` ainsi :

```cpp hl_lines="1"
#pragma acc parallel loop
for (int i=0; i<N; i++)
{
  C[i] = A[i] + B[i];
}
```

Comme `parallel loop` est une directive *prescriptive*, le compilateur est forcé d'exécuter la boucle en parallèle. Ceci signifie que la clause `independent` mentionnée plus haut est implicite à l'intérieur d'une zone parallèle.

Pour utiliser cette directive dans notre exemple du produit matrice-vecteur, nous avons besoin des clauses `private` et `reduction` pour gérer le flux des données dans la zone parallèle.

*   Avec la clause `private`, une copie de la variable est faite pour chaque itération de la boucle; la valeur de la variable est ainsi indépendante des autres itérations.
*   Avec la clause `reduction`, les valeurs de la variable dans chaque itération sont *réduites* à une valeur unique. La clause s'utilise entre autres avec les opérations addition (+), multiplication (*), maximum (max) et minimum (min).

Ces clauses ne sont pas nécessaires avec la directive `kernels` puisque celle-ci fait le travail pour vous.

Reprenons l'exemple de produit matrice-vecteur avec la directive `parallel loop` :

```cpp hl_lines="6"
#pragma acc parallel loop
  for(int i=0;i<num_rows;i++) {
    double sum=0;
    int row_start=row_offsets[i];
    int row_end=row_offsets[i+1];
#pragma acc loop reduction(+:sum)
    for(int j=row_start;j<row_end;j++) {
      unsigned int Acol=cols[j];
      double Acoef=Acoefs[j];
      double xcoef=xcoefs[Acol];
      sum+=Acoef*xcoef;
    }
    ycoefs[i]=sum;
  }
```

La compilation produit le message suivant :

```bash
nvc++ -fast -Minfo=accel -acc -gpu=managed main.cpp -o challenge
```

```text
matvec(const matrix &, const vector &, const vector &):
     23, include "matrix_functions.h"
          27, Accelerator kernel generated
              Generating Tesla code
              29, #pragma acc loop gang /* blockIdx.x */
              34, #pragma acc loop vector(128) /* threadIdx.x */
                  Sum reduction generated for sum
          27, Generating copyout(ycoefs[:num_rows])
              Generating copyin(xcoefs[:],Acoefs[:],cols[:],row_offsets[:num_rows+1])
          34, Loop is parallelizable
```

## Différences entre `parallel loop` et `kernels`

| PARALLEL LOOP                                      | KERNELS                                                                  |
| :------------------------------------------------- | :----------------------------------------------------------------------- |
| *   l'intégrité du code parallélisé revient au programmeur | *   la responsabilité d'analyser le code et de garantir son intégrité revient au compilateur |
| *   le programmeur voit la parallélisation que le compilateur pourrait manquer | *   une seule directive peut s'appliquer à une grande portion de code    |
| *   le fonctionnement est identique en OpenMP      | *   le compilateur est libre d'optimiser le code                         |

Les deux approches sont valides et leur performance est comparable.

!!! question "Exercice : utiliser `kernels` ou `parallel loop`"

1.  Modifiez les fonctions `matvec`, `waxpby` et `dot`. Vous pouvez utiliser soit `kernels`, soit `parallel loop`. La solution se trouve dans les répertoires `step1.*` de [Github](https://github.com/calculquebec/cq-formation-openacc).
2.  Modifiez le Makefile en ajoutant `-acc -gpu=managed` et `-Minfo=accel` aux indicateurs pour le compilateur.

[<- Page précédente, Profileurs](openacc-tutorial-profiling.md) | [^- Retour au début du tutoriel](openacc-tutorial.md) | [Page suivante, Mouvement des données ->](openacc-tutorial-data-movement.md)