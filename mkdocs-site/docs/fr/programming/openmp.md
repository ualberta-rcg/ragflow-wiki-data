---
title: "OpenMP/fr"
slug: "openmp"
lang: "fr"

source_wiki_title: "OpenMP/fr"
source_hash: "43c40573cb89b8df73e677c1d4b067e3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:04:31.558008+00:00"

tags:
  []

keywords:
  - "Fortran"
  - "Variables d'environnement"
  - "OMP_SCHEDULE"
  - "exécution"
  - "sentinelles"
  - "threads"
  - "fil d'exécution"
  - "code C"
  - "directives OpenMP"
  - "sections parallèles"
  - "directives"
  - "Fortran 90"
  - "gfortran"
  - "Tâche multifil"
  - "fils d'exécution"
  - "OMP_NUM_THREADS"
  - "compilation"
  - "planification"
  - "Directives"
  - "architecture NUMA"
  - "itérations"
  - "compilateurs"
  - "variables d'environnement"
  - "pragma"
  - "calcul parallèle"
  - "application hybride OpenMP/MPI"
  - "OpenMP"
  - "Clauses"

questions:
  - "Qu'est-ce qu'OpenMP et comment ses directives permettent-elles de paralléliser un programme tout en conservant la possibilité de l'exécuter de manière séquentielle ?"
  - "Quelle est la relation entre les fils d'exécution (threads) et les processeurs physiques, et pourquoi la synchronisation est-elle cruciale lors du calcul en parallèle ?"
  - "Comment les directives OpenMP sont-elles concrètement insérées dans le code source (Fortran et C) et quelles options de compilation faut-il utiliser pour les activer ?"
  - "Que doit-on consulter pour connaître l'option de compilation OpenMP appropriée pour son compilateur ?"
  - "Comment les directives OpenMP sont-elles intégrées dans un programme Fortran et qu'est-ce qu'une sentinelle ?"
  - "Quel mécanisme est utilisé pour insérer des directives OpenMP dans un code en langage C ?"
  - "Comment la syntaxe des directives et clauses OpenMP diffère-t-elle entre le Fortran et le C/C++ selon le tableau fourni ?"
  - "Quelles sont les principales variables d'environnement affectant l'exécution d'un programme OpenMP et comment peut-on les définir sous Unix ?"
  - "Quels sont les rôles respectifs et les valeurs possibles des variables OMP_NUM_THREADS et OMP_SCHEDULE dans la configuration d'une application OpenMP ?"
  - "Quels sont les avantages et les inconvénients des modes de planification dynamiques (dynamic, guided, auto) par rapport à l'affinité mémoire dans une architecture NUMA ?"
  - "Quel est le rôle de la variable d'environnement OMP_STACKSIZE et quelles sont les conséquences si sa valeur est insuffisante pour le code exécuté ?"
  - "Comment les variables d'affinité spécifiques aux compilateurs (comme KMP_AFFINITY ou GOMP_CPU_AFFINITY) permettent-elles d'optimiser les performances d'accès mémoire ?"
  - "Quel est le rôle principal de la variable OMP_SCHEDULE dans l'exécution du code ?"
  - "De quoi dépend la valeur par défaut de cette variable et comment peut-elle être définie ?"
  - "Quelles sont les valeurs possibles pour configurer OMP_SCHEDULE et que représente la lettre \"n\" dans ces configurations ?"
  - "Quelles sont les commandes utilisées pour compiler et exécuter le code Fortran 90 avec OpenMP ?"
  - "Où doit-on se renseigner pour savoir comment soumettre une tâche multifil ou OpenMP ?"
  - "Quelles références externes sont fournies pour consulter les spécifications et obtenir des exemples sur OpenMP ?"
  - "Quelle commande est utilisée pour compiler le code avec la prise en charge d'OpenMP ?"
  - "Comment le nombre de threads d'exécution est-il défini dans l'environnement avant le lancement du programme ?"
  - "Quelles informations spécifiques sont affichées par chaque thread lors de l'exécution du programme ?"
  - "Quelles sont les commandes utilisées pour compiler et exécuter le code Fortran 90 avec OpenMP ?"
  - "Où doit-on se renseigner pour savoir comment soumettre une tâche multifil ou OpenMP ?"
  - "Quelles références externes sont fournies pour consulter les spécifications et obtenir des exemples sur OpenMP ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description
[OpenMP](http://openmp.org/wp/) (pour *Open Multi-Processing*) est une interface de programmation (API) pour le calcul parallèle sur architecture à mémoire partagée. L'interface OpenMP est supportée sur de nombreuses plateformes dont Unix et Windows, pour les langages de programmation C/C++ et Fortran. Elle est composée d'un ensemble de directives, d'une bibliothèque logicielle et de variables d'environnement.

OpenMP permet de développer rapidement des applications parallèles à fine granularité en restant proche du code séquentiel. Avec une seule instance du programme, plusieurs sous-tâches peuvent être exécutées en parallèle. Les directives insérées dans le programme déterminent si une section du programme s'exécute en parallèle; dans ce cas, les directives prennent aussi en charge la distribution du travail sur plusieurs fils. Ainsi, un compilateur qui ne comprend pas les directives peut tout de même compiler le programme, qui peut ensuite être exécuté en série.

L'interface OpenMP est basée sur le concept de [fils d'exécution](https://fr.wikipedia.org/wiki/Thread_(informatique)), bien connu en programmation orientée objet. Un fil d'exécution est un peu comme un *processeur virtuel opérant en séquentiel*; il s'agit de la plus petite unité de travail/calcul que peut programmer un système d'exploitation. Du point de vue du programmeur, cinq fils équivalent virtuellement à cinq processeurs qui peuvent effectuer du calcul en parallèle. Il est important de comprendre que le nombre de fils n'est pas associé au nombre de processeurs physiques disponibles : par exemple, deux processeurs peuvent exécuter un programme possédant 10 fils. C'est le système d'exploitation qui se charge de partager le temps des processeurs disponibles entre les fils.

Il n'est cependant pas possible d'exécuter *le même fil sur plusieurs processeurs*; si vous disposez par exemple de quatre processeurs, vous devrez utiliser au minimum quatre fils pour profiter de toute la puissance de calcul. Dans certains cas, il pourrait être avantageux d'utiliser plus de fils que de processeurs; cependant, le nombre de fils est habituellement égal au nombre de processeurs.

Un autre point important concernant les fils est la synchronisation. Lorsque plusieurs fils d'un même programme effectuent des calculs en même temps, on ne peut absolument pas présumer de l'ordre dans lequel ils vont s'effectuer. Si un ordre déterminé est nécessaire pour assurer l'intégrité du code, le programmeur utilisera les directives de synchronisation d'OpenMP. La méthode exacte de distribution sur les fils demeure inconnue du programmeur, mais il existe toutefois des fonctionnalités de contrôle (voir [affinité processeur](https://en.wikipedia.org/wiki/Processor_affinity)).

!!! tip "Conseil"
    Pour paralléliser un programme avec OpenMP ou toute autre technique, il importe de considérer la capacité du programme à s'exécuter en parallèle, ce que nous appellerons sa [scalabilité](scalabilite.md). Après avoir parallélisé votre logiciel et que sa qualité vous satisfait, nous vous recommandons d'effectuer une analyse de sa scalabilité pour en comprendre la performance.

Pour des renseignements sur l'utilisation d'OpenMP sous Linux, consultez ce [tutoriel](http://www.admin-magazine.com/HPC/Articles/Programming-with-OpenMP).

## Compilation
Pour la plupart des compilateurs, la compilation d'un code OpenMP s'effectue simplement en ajoutant une option de compilation. Pour les compilateurs GNU (GCC), il s'agit de l'option `-fopenmp`; pour ceux d'Intel, [dépendant de la version](https://github.com/OpenMathLib/OpenBLAS/issues/1546), ce peut être `-qopenmp`, `-fopenmp` ou `-openmp`. Pour les autres compilateurs, vérifiez leur documentation respective.

## Directives

Les directives OpenMP sont insérées dans les programmes Fortran en utilisant des sentinelles. Une sentinelle est un mot clé placé immédiatement après le symbole indiquant un commentaire. Par exemple :

```fortran
!$OMP directive
c$OMP directive
C$OMP directive
*$OMP directive
```

En C, les directives sont insérées en utilisant un pragma :

```c
#pragma omp directive
```

### Directives OpenMP

| Fortran | C, C++ |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `!$OMP PARALLEL [clause, clause,…]` <br /> `block` <br /> `!$OMP END PARALLEL` | `#pragma omp parallel [clause, clause,…]` <br /> `structured-block` |
| `!$OMP DO [ clause, clause,… ]` <br /> `do_loop` <br /> `!$OMP END DO` | `#pragma omp for [ clause, clause,… ]` <br /> `for-loop` |
| `!$OMP SECTIONS [clause, clause,…]` <br /> `!$OMP SECTION` <br /> `block` <br /> `!$OMP SECTION` <br /> `block` <br /> `!$OMP END SECTIONS [NOWAIT]` | `#pragma omp sections [clause, clause,…] {` <br /> `[ #pragma omp section ]` <br /> `structured-block` <br /> `[ #pragma omp section ]` <br /> `structured-block` <br /> `}` |
| `!$OMP SINGLE [clause, clause,…]` <br /> `block` <br /> `!$OMP END SINGLE [NOWAIT]` | `#pragma omp single [clause, clause,…]` <br /> `structured-block` |
| `!$OMP PARALLEL DO [clause, clause,…]` <br /> `DO_LOOP` <br /> `[ !$OMP END PARALLEL DO ]` | `#pragma omp parallel for [clause, clause,…]` <br /> `for-loop` |
| `!$OMP PARALLEL SECTIONS [clause, clause,…]` <br /> `!$OMP SECTION` <br /> `block` <br /> `!$OMP SECTION` <br /> `block` <br /> `!$OMP END PARALLEL SECTIONS` | `#pragma omp parallel sections [clause, clause,…] {` <br /> `[ #pragma omp section ]` <br /> `structured-block` <br /> `[ #pragma omp section ]` <br /> `structured-block` <br /> `}` |
| `!$OMP MASTER` <br /> `block` <br /> `!$OMP END MASTER` | `#pragma omp master` <br /> `structured-block` |
| `!$OMP CRITICAL [(name)]` <br /> `block` <br /> `!$OMP END CRITICAL [(name)]` | `#pragma omp critical [(name)]` <br /> `structured-block` |
| `!$OMP BARRIER` | `#pragma omp barrier` |
| `!$OMP ATOMIC` <br /> `expresion_statement` | `#pragma omp atomic` <br /> `expression-statement` |
| `!$OMP FLUSH [(list)]` | `#pragma omp flush [(list)]` |
| `!$OMP ORDERED` <br /> `block` <br /> `!$OMP END ORDERED` | `#pragma omp ordered` <br /> `structured-block` |
| `!$OMP THREADPRIVATE( /cb/[, /cb/]…)` | `#pragma omp threadprivate ( list )` |
| **Clauses** | |
| `PRIVATE ( list )` | `private ( list )` |
| `SHARED ( list )` | `shared ( list )` |
| `DEFAULT ( PRIVATE | SHARED | NONE )` | `default ( shared | none )` |
| `FIRSTPRIVATE ( list )` | `firstprivate ( list )` |
| `LASTPRIVATE ( list )` | `lastprivate ( list )` |
| `REDUCTION ( { operator | intrinsic } : list )` | `reduction ( op : list )` |
| `IF ( scalar_logical_expression )` | `if ( scalar-expression )` |
| `COPYIN ( list )` | `copyin ( list )` |
| `NOWAIT` | `nowait` |

## Environnement
Certaines variables d'environnement ont un effet sur l'exécution d'un programme OpenMP :

```bash
OMP_NUM_THREADS
OMP_SCHEDULE
OMP_DYNAMIC
OMP_STACKSIZE
OMP_NESTED
```

Les variables sont définies ou modifiées avec une commande Unix telle que :

```bash
export OMP_NUM_THREADS=12
```

Dans la plupart des cas, vous voudrez spécifier avec `OMP_NUM_THREADS` le nombre de cœurs réservés par machine. Ceci pourrait cependant être différent pour une application hybride OpenMP/MPI.

Une autre variable importante est `OMP_SCHEDULE`. Celle-ci contrôle comment sont distribuées les boucles (et plus généralement les sections parallèles). La valeur par défaut dépend du compilateur et peut être définie dans le code source. Les valeurs possibles sont *static,n*, *dynamic,n*, *guided,n* et *auto* où *n* indique le nombre d'itérations gérées par chaque fil d'exécution.
*   Dans le cas de *static*, le nombre d'itérations est fixe et les itérations sont distribuées au début de la section parallèle.
*   Dans le cas de *dynamic*, le nombre d'itérations est fixe, mais les itérations sont distribuées pendant l'exécution en fonction du temps requis par chaque fil pour exécuter ses itérations.
*   Dans le cas de *guided*, *n* indique le nombre minimal d'itérations. Le nombre d'itérations est d'abord choisi « grand », puis diminue dynamiquement au fur et à mesure que le nombre restant d'itérations diminue.
*   Pour le mode *auto*, le compilateur et la bibliothèque sont libres de faire des choix.

L'avantage des cas *dynamic*, *guided* et *auto* est qu'ils permettent en théorie de mieux balancer les fils d'exécution, puisqu'ils s'ajustent dynamiquement selon le temps requis par chaque fil. Par contre, l'inconvénient est que vous ne savez pas à l'avance quel processeur exécutera quel fil, et à quelle mémoire il doit accéder. Il est ainsi impossible avec ces types de planification de prévoir l'affinité entre la mémoire et le processeur exécutant le calcul. Ceci peut être particulièrement problématique dans une architecture [NUMA](http://en.wikipedia.org/wiki/Non_Uniform_Memory_Access).

!!! warning "Mise en garde"
    La variable d'environnement `OMP_STACKSIZE` définit la taille de la pile pour chacun des fils créés à l'exécution de OpenMP. Remarquez que le fil principal OpenMP (celui qui exécute la partie séquentielle du programme) obtient la taille de sa pile de l'interpréteur (*shell*) alors que `OMP_STACKSIZE` affecte chacun des fils additionnels créés à l'exécution. Si cette variable n'est pas définie, la valeur sera de 4Mo. Si votre code ne possède pas assez de mémoire pour la pile, il pourrait se terminer de façon anormale en raison d'une erreur de segmentation.

D'autres variables d'environnement sont aussi disponibles : certaines sont spécifiques à un compilateur alors que d'autres sont plus génériques. Consultez la liste des variables pour les [compilateurs Intel](http://software.intel.com/sites/products/documentation/doclib/stdxe/2013/composerxe/compiler/cpp-lin/GUID-E1EC94AE-A13D-463E-B3C3-6D7A7205F5A1.htm) et pour les [compilateurs GNU](http://gcc.gnu.org/onlinedocs/libgomp/Environment-Variables.html).

Les variables d'environnement spécifiques au compilateur Intel débutent par `KMP_` alors que celles spécifiques à GNU débutent par `GOMP_`. Pour des performances optimales en accès mémoire, fixez les variables `OMP_PROC_BIND` et les variables d'affinité `KMP_AFFINITY` pour Intel et `GOMP_CPU_AFFINITY` pour GNU. Ceci empêche les fils d'exécution OpenMP de se déplacer d'un processeur à l'autre, ce qui est particulièrement important dans une architecture [NUMA](http://en.wikipedia.org/wiki/Non_Uniform_Memory_Access).

## Exemple
Voici un exemple "hello world" qui montre l'usage d'OpenMP.

=== "C"

    ```c title="hello.c"
    #include <stdio.h>
    #include <omp.h>

    int main() {
      #pragma omp parallel
       {
          printf("Hello world from thread %d out of %d\n",
                   omp_get_thread_num(),omp_get_num_threads());
       }
      return 0;
    }
    ```

=== "Fortran"

    ```fortran title="hello.f90"
    program hello
     implicit none
     integer omp_get_thread_num,omp_get_num_threads
     !$omp parallel
      print *, 'Hello world from thread',omp_get_thread_num(), &
               'out of',omp_get_num_threads()
     !$omp end parallel

    end program hello
    ```

Le code C est compilé et exécuté comme suit :

```bash
litai10:~$ gcc -O3 -fopenmp ompHello.c -o ompHello
litai10:~$ export OMP_NUM_THREADS=4
litai10:~$ ./ompHello
Hello world from thread 0 out of 4
Hello world from thread 2 out of 4
Hello world from thread 1 out of 4
Hello world from thread 3 out of 4
```

Le code Fortran 90 est compilé et exécuté comme suit :

```bash
litai10:~$ gfortran -O3 -fopenmp ompHello.f90 -o fomphello
litai10:~$ export OMP_NUM_THREADS=4
litai10:~$ ./fomphello
 Hello world from thread           0 out of           4
 Hello world from thread           2 out of           4
 Hello world from thread           1 out of           4
 Hello world from thread           3 out of           4
```

Pour savoir comment soumettre une tâche OpenMP, consultez la section Tâche multifil ou tâche OpenMP de la page [Exécuter des tâches](../running-jobs/running_jobs.md).

## Références
*   Lawrence Livermore National Laboratory : [documentation OpenMP](https://computing.llnl.gov/tutorials/openMP).
*   [OpenMP.org](http://www.openmp.org/) :
    *   [spécifications](http://www.openmp.org/specifications/)
    *   aide-mémoire pour les interfaces [C/C++](http://www.openmp.org/wp-content/uploads/OpenMP-4.0-C.pdf) et [Fortran](http://www.openmp.org/wp-content/uploads/OpenMP-4.0-Fortran.pdf)
    *   [exemples](http://www.openmp.org/wp-content/uploads/openmp-examples-4.0.2.pdf)