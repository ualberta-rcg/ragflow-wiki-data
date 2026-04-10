---
title: "OpenACC Tutorial - Introduction/fr"
slug: "openacc_tutorial_-_introduction"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Introduction/fr"
source_hash: "377b52f74bae7e7662237db400c11d8a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:25:36.999399+00:00"

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
    * connaître la différence entre CPU et accélérateur
    * connaître la différence entre vitesse et débit
    * connaître les étapes pour porter du code existant sur un accélérateur

## Différence entre CPU et accélérateur
Historiquement, le développement de l'informatique s'est fait autour du CPU (le processeur central), mais celui-ci ne terminait qu'une opération de calcul par cycle d'horloge. La fréquence des horloges des CPU était en hausse constante jusqu'à environ 2005, où elle atteignait un plateau autour de 4GHz. Elle a très peu augmenté depuis et plusieurs horloges sont encore aujourd'hui sous les 4GHz; [un article de Pär Persson Mattsson](https://www.comsol.com/blogs/havent-cpu-clock-speeds-increased-last-years/) explique bien pourquoi. Les manufacturiers ont choisi d'additionner les cœurs de calcul dans un même circuit, ouvrant ainsi la voie au calcul en parallèle.

En 2022, les tâches séquentielles sont toujours exécutées plus rapidement avec des CPU :
* ils ont un accès direct à la mémoire qui est souvent d'une grande capacité et
* ils peuvent exécuter un petit nombre de tâches très rapidement en raison de la vitesse de l'horloge.

On leur connaît cependant certains inconvénients :
* faiblesse de la bande passante mémoire,
* des mécanismes de cache compensent pour la faiblesse de la bande passante, mais [les défauts de cache sont coûteux](https://en.wikipedia.org/wiki/CPU_cache#Cache_miss),
* ils sont aussi plus énergivores que les accélérateurs.

Un accélérateur type comme un GPU ou un coprocesseur est un jeu de puces hautement parallèle, composé de centaines ou de milliers de cœurs de calcul de basse fréquence, relativement simples : ils sont optimisés pour le calcul en parallèle. Les GPU au haut de la gamme possèdent habituellement quelques centaines de cœurs de calcul et une large bande passante leur permettant d'accéder leur mémoire (*device memory*). Ils disposent de beaucoup plus de ressources de calcul que les CPU les plus performants en plus d'offrir un **meilleur débit** et une **meilleure performance par watt**. Par contre, ils possèdent relativement peu de mémoire et la performance par fil est faible.

!!! info "Privilégier la vitesse ou le débit?"
    Selon la tâche à effectuer, un CPU offrira l'avantage de la vitesse alors qu'un accélérateur sera privilégié pour son débit.

    Une composante à **haute vitesse** peut accomplir une tâche en très peu de temps, ce qui est souhaitable pour effectuer un seul calcul séquentiel, par exemple une équation différentielle du premier ordre. Une telle composante de haute vitesse se compare à une moto de compétition ou à une voiture de course : le passager est déplacé très rapidement du point A au point B.

    Une composante à **haut débit** accomplit beaucoup plus de travail, mais nécessite plus de temps, ce qui est souhaitable pour résoudre un problème hautement parallèle. Les exemples de ce genre de tâches sont nombreux : pensons par exemple aux opérations matricielles, aux transformées de Fourier et aux équations différentielles multidimensionnelles. Ce type de composante se compare à un train ou à un autobus : plusieurs passagers sont déplacés du point A au point B, mais certainement plus lentement que dans le cas de la moto ou l'automobile.

## Porter du code sur un accélérateur
On peut considérer ceci comme étant une phase du processus d'optimisation. Un cas type est constitué des étapes suivantes :
1. profiler le code
2. identifier les goulots d'étranglement (*bottlenecks*)
3. remplacer le plus important goulot d'étranglement par du code optimisé
4. valider le code sortant
5. reprendre à partir de l'étape 1

Porter du code sur un accélérateur aurait ainsi les étapes suivantes :
1. profiler le code
2. localiser le parallélisme dans les goulots
3. porter le code
    1. décrire le parallélisme au compilateur
    2. décrire le flux des données au compilateur
    3. optimiser les boucles
4. valider le résultat
5. reprendre à partir de l'étape 1

OpenACC peut être un langage plutôt *descriptif*. Le programmeur peut donc indiquer au compilateur quelles sont les portions de code à paralléliser et laisser le compilateur effectuer le travail. Pour ce faire, il suffit d'ajouter quelques directives dans le code (voir le point 3.1 ci-dessus, *décrire le parallélisme au compilateur*). La qualité du compilateur a toutefois un effet important sur la performance; même avec les meilleurs compilateurs, il est possible que certains mouvements de données doivent être éliminés, ce que le programmeur peut faire au point 3.2, *décrire le flux des données au compilateur*. Enfin, si le programmeur possède de l'information sur comment obtenir une meilleure performance en ajustant les boucles, il en informera le compilateur au point 3.3, *optimiser les boucles*.

[^- Retour au début du tutoriel](openacc-tutorial.md) | [Page suivante, *Profileurs* ->](openacc-tutorial-profiling.md)