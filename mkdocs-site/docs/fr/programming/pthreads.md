---
title: "Pthreads/fr"
slug: "pthreads"
lang: "fr"

source_wiki_title: "Pthreads/fr"
source_hash: "d2f9242e054e7d17e7bd28d70b76b3b8"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T10:03:01.397919+00:00"

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

## Introduction

Le terme *pthreads* provient de [POSIX threads](https://fr.wikipedia.org/wiki/Threads_POSIX), l'une des premières techniques de parallélisation. Tout comme les autres outils faisant usage de fils d'exécution, Pthreads s'emploie dans un contexte de mémoire partagée et donc habituellement sur un seul nœud où le nombre de fils actifs est limité aux cœurs CPU disponibles sur ce nœud. On utilise Pthreads dans plusieurs langages de programmation, mais surtout en C. En Fortran, la parallélisation de fils d'exécution se fait préférablement avec [OpenMP](openmp.md). En C++, les outils de la bibliothèque [Boost](http://www.boost.org) issus de la [norme C11](https://fr.wikipedia.org/wiki/C%2B%2B11) sont mieux adaptés à la programmation orientée-objet.

La bibliothèque Pthreads a servi de base aux approches de parallélisation qui ont suivi, dont OpenMP. On peut voir Pthreads comme étant un ensemble d'outils primitifs offrant des fonctionnalités élémentaires de parallélisation, contrairement aux API conviviales et de haut niveau comme OpenMP. Dans le modèle Pthreads, les fils sont générés dynamiquement pour exécuter des sous-procédures dites légères qui effectuent les opérations de façon asynchrone; ces fils sont ensuite détruits après avoir réintégré le processus principal.

!!! warning "Partage de données et situations de compétition"
    Étant donné que tous les fils d'un même programme résident dans le même espace mémoire, il est aisé de partager les données en utilisant des variables globales, contrairement à une approche distribuée comme [MPI](mpi.md). Cependant, toute modification des données partagées risque de créer des [situations de compétition](https://en.wikipedia.org/wiki/Race_condition) (*race conditions*).

!!! tip "Analyse de la scalabilité"
    Pour paralléliser un programme avec Pthreads ou toute autre technique, il est crucial de considérer la capacité du programme à s'exécuter en parallèle, ce que nous appelons sa [scalabilité](scalability.md). Une fois votre logiciel parallélisé et que sa qualité vous satisfait, nous vous recommandons d'effectuer une analyse de sa scalabilité afin d'en comprendre la performance.

## Compilation

Pour utiliser les fonctions et structures de données associées à Pthreads dans votre programme C, il faut y inclure le fichier d'en-tête `pthread.h` et compiler le programme avec un indicateur pour faire le lien avec la bibliothèque Pthreads.

```bash
gcc -pthread -o test threads.c
```

Le nombre de fils pour le programme est défini par une des méthodes suivantes :
*   utilisé comme argument dans une ligne de commande;
*   entré via une variable d'environnement;
*   encodé dans le fichier source (ceci ne permet toutefois pas d'ajuster le nombre de fils à l'exécution).

## Création et destruction des Pthreads

Pour paralléliser avec Pthreads un programme séquentiel existant, nous utilisons un modèle de programmation où les fils sont créés par un parent, exécutent une partie du travail, puis sont réintégrés au parent. Le parent est soit le *fil maître* séquentiel ou un des autres *fils esclaves*.

La fonction [pthread_create](http://pubs.opengroup.org/onlinepubs/009695399/functions/pthread_create.html) crée de nouveaux fils avec ces quatre arguments :
*   l'identifiant unique pour le nouveau fil;
*   l'ensemble des attributs du fil;
*   la fonction C que le fil exécute lorsqu'il est amorcé (la routine de lancement);
*   l'argument de la routine de lancement.

```c title="thread.c"
#include <stdio.h>
#include <pthread.h>

const long NT = 12;

void* task(void* thread_id)
{
  long tnumber = (long) thread_id;
  printf("Hello World from thread %ld\n",1+tnumber);
}

int main(int argc,char** argv)
{
  int success;
  long i;
  pthread_t threads[NT];

  for(i=0; i<NT; ++i) {
    success = pthread_create(&threads[i],NULL,task,(void*)i);
    if (success != 0) {
      printf("ERROR: Unable to create worker thread %ld successfully\n",i);
      return 1;
    }
  }
  for(i=0; i<NT; ++i) {
    pthread_join(threads[i],NULL);
  }
  return 0;
}
```

Dans cet exemple, l'index du fil (de 0 à 11) est passé en argument; la fonction `task` est donc exécutée par chacun des 12 fils. Remarquez que la fonction `pthread_create` ne bloque pas le fil maître, qui continue à exécuter la fonction `main` après la création de chacun des fils. Une fois les 12 fils créés, le fil maître entre dans la deuxième boucle `for` et appelle la fonction bloquante [pthread_join](http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_join.html) : le fil maître attend alors que les 12 fils esclaves terminent l'exécution de la fonction `task` et qu'ils réintègrent ensuite le fil maître. Cet exemple simple illustre bien le fonctionnement de base d'un fil POSIX : le fil maître crée un fil en lui assignant une fonction à exécuter et attend ensuite que le fil créé termine cette fonction, puis réintègre le fil maître.

En exécutant ce code plusieurs fois de suite, vous noterez probablement une variation dans l'ordre dans lequel les fils esclaves disent *hello*, ce qui est prévisible puisqu'ils s'exécutent en mode asynchrone. Chaque fois que le programme est exécuté, les 12 fils répondent en même temps à la fonction `printf` et ce n'est jamais le même fil qui remporte la course.

## Synchronisation de l'accès aux données

Dans un programme réel, les fils esclaves doivent lire et dans certains cas modifier les données afin d'accomplir leurs tâches. Ces données sont habituellement un ensemble de variables globales de divers types et dimensions; l'accès concurrent en lecture et en écriture par plusieurs fils doit donc être synchronisé afin d'éviter les [situations de compétition](https://en.wikipedia.org/wiki/Race_condition), c'est-à-dire les cas où le résultat du programme dépend de l'ordre dans lequel les fils esclaves accèdent aux données. Si un programme en parallèle doit donner le même résultat que sa version en série, les situations de compétition ne doivent pas se produire.

Le moyen le plus simple et le plus utilisé pour contrôler l'accès concurrent est le [verrou](https://fr.wikipedia.org/wiki/Verrou_(informatique)); dans le contexte de Pthreads, le mécanisme de verrouillage est le *mutex* (pour *mutual exclusion*). Les variables de ce type sont assignées à un seul fil à la fois. Après la lecture ou la modification, le fil désactive le verrou. Le code entre l'appel de la variable et le moment où elle est désactivée est exécuté exclusivement par ce fil. Pour créer un mutex, il faut déclarer une variable globale de type `pthread_mutex_t`. Cette variable est initialisée par la fonction [pthread_mutex_init](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_init.html). À la fin du programme, les ressources sont *déverrouillées* par la fonction [pthread_mutex_destroy](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_destroy.html).

```c title="thread_mutex.c"
#include <stdio.h>
#include <pthread.h>

const long NT = 12;

pthread_mutex_t mutex;

void* task(void* thread_id)
{
  long tnumber = (long) thread_id;
  pthread_mutex_lock(&mutex);
  printf("Hello World from thread %ld\n",1+tnumber);
  pthread_mutex_unlock(&mutex);
}

int main(int argc,char** argv)
{
  int success;
  long i;
  pthread_t threads[NT];

  pthread_mutex_init(&mutex,NULL);

  for(i=0; i<NT; ++i) {
    success = pthread_create(&threads[i],NULL,task,(void*)i);
    if (success != 0) {
      printf("ERROR: Unable to create worker thread %ld successfully\n",i);
      pthread_mutex_destroy(&mutex);
      return 1;
    }
  }
  for(i=0; i<NT; ++i) {
    pthread_join(threads[i],NULL);
  }

  pthread_mutex_destroy(&mutex);

  return 0;
}
```

Dans cet exemple basé sur le contenu du fichier `thread.c` plus haut, l'accès au canal de sortie standard est sérialisé comme il se doit avec un mutex. L'appel de [pthread_mutex_lock](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_lock.html) effectue le blocage, c'est-à-dire que le fil attendra indéfiniment que le mutex devienne disponible.

!!! warning "Prévention des interblocages (deadlocks)"
    Il faut s'assurer que le code ne provoque pas d'autre blocage, car le mutex doit éventuellement devenir disponible. Cela pose surtout problème dans un programme réel qui comporte plusieurs variables mutex contrôlant l'accès à différentes structures de données globales.

Dans le cas de l'alternative non bloquante [pthread_mutex_trylock](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_lock.html), la valeur non nulle est immédiatement produite si le mutex n'est pas accompli, indiquant ainsi que le mutex est occupé.

!!! tip "Optimisation des blocs sérialisés"
    Il faut également s'assurer qu'il n'y a pas de code superflu à l'intérieur du bloc sérialisé. Puisque ce code est exécuté en série, il doit être le plus concis possible afin de ne pas entraver le parallélisme de l'exécution du programme.

Une synchronisation plus subtile est possible avec le verrou lecture/écriture `pthread_rwlock_t`. Cet outil permet la lecture simultanée d'une variable par plusieurs fils, mais se comporte comme un mutex standard pour l'écriture, c'est-à-dire qu'aucun autre fil n'a accès à cette variable (en lecture ou en écriture) pendant qu'un fil y écrit. Comme pour le mutex, le verrou `pthread_rwlock_t` doit être initialisé avant son utilisation et détruit quand il n'est plus nécessaire. Un fil obtient un verrou en lecture avec [pthread_rwlock_rdlock](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_rwlock_rdlock.html) et un verrou en écriture avec [pthread_rwlock_wrlock](http://pubs.opengroup.org/onlinepubs/007908775/xsh/pthread_rwlock_wrlock.html). Dans les deux cas, le verrou est détruit avec [pthread_rwlock_unlock](http://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_rwlock_unlock.html).

Un autre outil permet à plusieurs fils d'agir sur la même condition, par exemple d'attendre que les fils esclaves soient appelés à une tâche. Il s'agit d'une variable-condition, de type `pthread_cond_t`. Comme le mutex ou le verrou lecture/écriture, la variable-condition doit être initialisée avant son utilisation et détruite lorsqu'elle n'est plus nécessaire. Pour utiliser cette variable-condition, un mutex doit contrôler l'accès aux variables qui ont une incidence sur la condition. Un fil en attente d'une condition verrouille le mutex et fait appel à la fonction [pthread_cond_wait](http://pubs.opengroup.org/onlinepubs/007908775/xsh/pthread_cond_wait.html) avec la variable-condition et le mutex en arguments. Le mutex est alors relâché de manière atomique pendant que le fil attend la condition; les autres fils peuvent alors verrouiller le mutex, soit pour attendre la condition ou pour modifier une ou plusieurs variables, ce qui modifiera la condition.

```c title="thread_condition.c"
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h> // For atoi

const long NT = 2;

pthread_mutex_t mutex;
pthread_cond_t ticker;

int workload;

void* task(void* thread_id)
{
  long tnumber = (long) thread_id;

  if (tnumber == 0) {
    pthread_mutex_lock(&mutex);
    while(workload <= 25) {
      pthread_cond_wait(&ticker,&mutex);
    }
    printf("Thread %ld: incrementing workload by 15\n",1+tnumber);
    workload += 15;
    pthread_mutex_unlock(&mutex);
  }
  else {
    int done = 0;
    do {
      pthread_mutex_lock(&mutex);
      workload += 3;
      printf("Thread %ld: current workload is %d\n",1+tnumber,workload);
      if (workload > 25) {
        done = 1;
        pthread_cond_signal(&ticker);
      }
      pthread_mutex_unlock(&mutex);
    } while(!done);
  }
}

int main(int argc,char** argv)
{
  int success;
  long i;
  pthread_t threads[NT];

  if (argc < 2) {
      printf("Usage: %s <initial_workload>\n", argv[0]);
      return 1;
  }
  workload = atoi(argv[1]);
  if (workload > 25) {
    printf("Initial workload must be <= 25, exiting...\n");
    return 0;
  }

  pthread_mutex_init(&mutex,NULL);
  pthread_cond_init(&ticker,NULL);

  for(i=0; i<NT; ++i) {
    success = pthread_create(&threads[i],NULL,task,(void*)i);
    if (success != 0) {
      printf("ERROR: Unable to create worker thread %ld successfully\n",i);
      pthread_mutex_destroy(&mutex);
      return 1;
    }
  }

  for(i=0; i<NT; ++i) {
    pthread_join(threads[i],NULL);
  }

  printf("Final workload is %d\n",workload);

  pthread_cond_destroy(&ticker);
  pthread_mutex_destroy(&mutex);

  return 0;
}
```

Dans cet exemple, deux fils esclaves modifient la valeur de l'entier `workload` dont la valeur initiale doit être plus petite ou égale à 25. Le premier fil verrouille le mutex et attend parce que `workload <= 25`; la variable-condition `ticker` est créée et le mutex est relâché. Le deuxième fil peut alors exécuter la boucle, qui elle incrémente de trois la valeur de `workload` à chaque itération. À chaque incrémentation, le deuxième fil vérifie si la valeur de `workload` est plus grande que 25; si c'est le cas, le fil appelle [pthread_cond_signal](http://pubs.opengroup.org/onlinepubs/007908799/xsh/pthread_cond_signal.html) pour signaler au fil en attente que la condition est satisfaite. Une fois que le signal est reçu par le premier fil (qui est alors réveillé), le deuxième fil fixe la condition de sortie de la boucle, libère le mutex et se termine, étant ensuite réuni au fil maître avec `pthread_join`. Entretemps, le premier fil, étant réveillé, incrémente de 15 la valeur de `workload` et quitte la fonction `task`. Quand tous les fils esclaves sont réintégrés, le fil maître imprime la valeur finale de `workload` et le programme se termine.

!!! note "Différence entre `pthread_cond_signal` et `pthread_cond_broadcast`"
    De façon générale, dans un programme réel où plusieurs fils sont en attente d'une variable-condition, la fonction `pthread_cond_broadcast` signale à tous les fils en attente que la condition est satisfaite. Dans ce contexte, `pthread_cond_signal` avertirait un seul fil au hasard et les autres fils demeureraient en attente.

## Pour en savoir plus

Pour plus d'information sur Pthreads, sur les arguments optionnels pour les diverses fonctions (les paramètres utilisés dans cette page utilisent l'argument par défaut NULL) et sur les sujets de niveau avancé, nous recommandons l'ouvrage de David Butenhof, [Programming with POSIX Threads](https://ptgmedia.pearsoncmg.com/images/9780201633924/samplepages/0201633922.pdf) ou l'excellent [tutoriel du Lawrence Livermore National Laboratory](https://computing.llnl.gov/tutorials/pthreads).