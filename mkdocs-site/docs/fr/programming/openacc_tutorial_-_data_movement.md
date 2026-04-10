---
title: "OpenACC Tutorial - Data movement/fr"
slug: "openacc_tutorial_-_data_movement"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Data movement/fr"
source_hash: "401f3baa45a66c695adbe1848a868d5b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:24:46.765112+00:00"

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

!!! note "Objectifs d'apprentissage"
    * Comprendre les principes de localité et de mouvement des données.
    * Connaître la différence entre données structurées et données non structurées.
    * Savoir comment faire un transfert explicite.
    * Savoir compiler et exécuter du code OpenACC avec des directives de mouvement.

## Gestion explicite des données

Nous avons utilisé CUDA Unified Memory pour simplifier les premières étapes d'accélération de notre code. Si le processus est plus simple, le code n'est cependant pas portable :
* pour PGI seulement, l'indicateur `-ta=tesla:managed`
* pour NVIDIA seulement, CUDA Unified Memory

La gestion explicite des données rend le code portable et peut améliorer la performance.

## Zones de données structurées
La directive `data` délimite la zone du code où les tableaux GPU restent sur le GPU et sont partagés par tous les noyaux de la zone.
Voici un exemple de comment se définit la zone de données structurées :

```cpp
#pragma acc data
{
#pragma acc parallel loop ...
#pragma acc parallel loop
...
}
```
Un autre exemple :
```fortran
!$acc data
!$acc parallel loop
...
!$acc parallel loop
...
!$acc end data
```
!!! tip "Localité des données"
    Les tableaux à l'intérieur de la zone de données restent sur le GPU jusqu'à la fin de la zone.

## Données non structurées
Dans certains cas, la délimitation d'une zone ne permet pas l'utilisation de zones de données normales, par exemple quand on utilise des constructeurs ou des destructeurs.
### Directives
Dans ces cas, on utilise des directives de données non structurées.
*   **enter data**, définit le début de la durée de vie des données non structurées
    *   clauses : **copyin(list)**, **create(list)**
*   **exit data**, définit la fin de la durée de vie des données non structurées
    *   clauses : **copyout(list)**, **delete(list)**
Voici un exemple :

```cpp
#pragma acc enter data copyin(a)
...
#pragma acc exit data delete(a)
```

### Classes C++
Quel est l'avantage des clauses de données non structurées? Elles permettent l'utilisation d'OpenACC dans les classes C++.
De plus, ces clauses peuvent être utilisées quand les données sont allouées et initialisées dans une portion du code différente de celle où les données sont libérées, par exemple dans les modules Fortran.
```cpp
class Matrix { Matrix(int n) {
len = n;
v = new double[len];
#pragma acc enter data
                     create(v[0:len])
}
~Matrix() {
#pragma acc exit data
                     delete(v[0:len])
};
```

### Clauses de la directive `data`

*   **copyin(list )**, pour allouer de la mémoire du GPU et copier des données de la mémoire hôte vers le GPU, à l'entrée de la zone
*   **copyout(list)**, pour allouer de la mémoire du GPU et copier des données vers la mémoire hôte, à la sortie de la zone
*   **copy(list)**, pour allouer de la mémoire du GPU et copier des données de la mémoire hôte vers le GPU à l'entrée de la zone et copier des données vers la mémoire hôte, à la sortie de la zone (données structurées seulement)
*   **create(list)**, pour allouer de la mémoire du GPU, sans copier
*   **delete(list)**, pour désallouer de la mémoire du GPU, sans copier (données non structurées seulement)
*   **present(list)**, le GPU contient déjà des données en provenance d'une autre région

### Format des tableaux
Le compilateur ne peut pas toujours déterminer la taille d'un tableau; il faut donc en spécifier la taille et le format.
Voici un exemple en C
```cpp
#pragma acc data copyin(a[0:nelem]) copyout(b[s/4:3*s/4])
```

et un exemple en Fortran.
```fortran
!$acc data copyin(a(1:end)) copyout(b(s/4:3*s/4))
```

## Mouvement explicite des données
### Copier dans la matrice
Dans cet exemple, nous commençons par allouer et initialiser la matrice. La matrice est ensuite copiée dans la mémoire. La copie se fait en deux étapes :
1.  Copier la structure de la matrice.
2.  Copier les membres de la matrice.

```cpp
void allocate_3d_poisson_matrix(matrix &A, int N) {
   int num_rows=(N+1)*(N+1)*(N+1);
   int nnz=27*num_rows;
   A.num_rows=num_rows;
   A.row_offsets = (unsigned int*) \ malloc((num_rows+1)*sizeof(unsigned int));
   A.cols = (unsigned int*)malloc(nnz*sizeof(unsigned int));
   A.coefs = (double*)malloc(nnz*sizeof(double)); // Initialize Matrix
   A.row_offsets[num_rows]=nnz;
   A.nnz=nnz;
   #pragma acc enter data copyin(A)
   #pragma acc enter data copyin(A.row_offsets[:num_rows+1],A.cols[:nnz],A.coefs[:nnz])
}
```

### Supprimer la matrice
Pour libérer la mémoire, il faut d'abord sortir la matrice puis énoncer la commande `free`. Ceci se fait en deux étapes, mais en sens inverse :
1.  Supprimer les membres.
2.  Supprimer la structure.

```cpp
void free_matrix(matrix &A) {
   unsigned int *row_offsets=A.row_offsets;
   unsigned int * cols=A.cols;
   double * coefs=A.coefs;
   #pragma acc exit data delete(A.row_offsets,A.cols,A.coefs)
   #pragma acc exit data delete(A)
   free(row_offsets);
   free(cols);
   free(coefs);
}
```

### La clause `present`
Pour une gestion de haut niveau, il faut dire au compilateur que les données se trouvent déjà en mémoire.
La déclaration des variables locales devraient cependant se faire à l'intérieur de la fonction dans laquelle elles sont utilisées.
```cpp
function main(int argc, char **argv) {
#pragma acc data copy(A) {
    laplace2D(A,n,m);
}
}
...
function laplace2D(double[N][M] A,n,m){
   #pragma acc data present(A[n][m]) create(Anew)
   while ( err > tol && iter < iter_max ) {
      err=0.0;
      ...
   }
}
```

!!! tip "Utilisez `present` lorsque c'est possible"
    Les éléments critiques pour assurer une bonne performance sont une gestion de haut niveau et l'utilisation de la clause `present`.

Dans le prochain exemple, la zone de calcul dans le code contient l'information qui indique au compilateur que les données sont déjà présentes.
```cpp
#pragma acc kernels \
present(row_offsets,cols,Acoefs,xcoefs,ycoefs)
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

### Compiler et exécuter avec une gestion explicite de la mémoire
Pour faire une nouvelle compilation sans mémoire autogérée, remplacez `-ta=tesla:managed` par `-ta-tesla` dans le Makefile.

### La directive `update`
Cette directive permet d'actualiser un tableau ou une partie d'un tableau.
```fortran
do_something_on_device()
!$acc update self(a)   //  Copier « a » du GPU vers le CPU hôte
do_something_on_host()
!$acc update device(a)  // Copier « a » du CPU hôte vers le GPU
```

Dans cet autre exemple, nous modifions d'abord un vecteur dans la mémoire du CPU hôte, puis nous le copions dans la mémoire du GPU.

```cpp
void initialize_vector(vector &v,double val) {
   for(int i=0;i<v.n;i++)
      v.coefs[i]=val;   // Mise à jour du vecteur sur le CPU hôte
   #pragma acc update
      device(v.coefs[:v.n])    // Mise à jour du vecteur sur le GPU
}
```

### Développer et exécuter sans mémoire autogérée
Nous voyons ici la performance du code avec et sans mémoire autogérée.

Dans cet exemple, des essais ont été faits avec et sans l'option `-ta=tesla:managed`.

Les résultats démontrent que certains tests avec mémoire autogérée améliorent la vitesse; ceci est probablement dû à la mémoire épinglée. De façon générale, il semble que la localité fonctionne : quand la plupart des opérations sont effectuées sur le GPU et que les données y demeurent longtemps, le mouvement des données n'a pas d'incidence majeure sur la performance.

!!! example "Exercice : Ajouter des directives"
    1.  Utiliser les directives `kernels` ou `parallel loop` pour obtenir la gestion explicite des données. Les répertoires [step2.* de Github](https://github.com/calculquebec/cq-formation-openacc) contiennent la solution.
    2.  Modifiez les indicateurs du compilateur en `-ta=tesla` (non géré).
    3.  Vérifiez si les résultats et la performance sont les mêmes qu'avant.

[Page suivante, Optimisation des boucles](openacc-tutorial-optimizing-loops.md)
[Retour au début du tutoriel](openacc-tutorial.md)