---
title: "OpenACC Tutorial - Introduction/fr"
slug: "openacc_tutorial_-_introduction"
lang: "fr"

source_wiki_title: "OpenACC Tutorial - Introduction/fr"
source_hash: "377b52f74bae7e7662237db400c11d8a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:55:57.464429+00:00"

tags:
  []

keywords:
  - "optimiser les boucles"
  - "OpenACC"
  - "débit"
  - "processus d'optimisation"
  - "parallélisme"
  - "compilateur"
  - "CPU"
  - "goulots d'étranglement"
  - "porter du code"
  - "accélérateur"
  - "profiler le code"
  - "vitesse"
  - "composante"
  - "calcul en parallèle"

questions:
  - "Quelles sont les principales différences de conception et d'avantages entre un CPU et un accélérateur comme un GPU ?"
  - "Comment les concepts de vitesse et de débit déterminent-ils s'il faut utiliser un CPU ou un accélérateur pour une tâche donnée ?"
  - "Quelle est la première étape du processus d'optimisation pour porter un code existant vers un accélérateur ?"
  - "Quelles sont les principales étapes à suivre pour porter du code sur un accélérateur ?"
  - "Comment le langage OpenACC permet-il au programmeur d'indiquer au compilateur les portions de code à paralléliser ?"
  - "Pourquoi le programmeur doit-il parfois intervenir manuellement pour décrire le flux de données ou optimiser les boucles malgré le travail du compilateur ?"
  - "Comment la composante multidimensionnelle est-elle comparée à des moyens de transport en termes de capacité et de vitesse ?"
  - "Comment le texte définit-il l'action de porter du code sur un accélérateur ?"
  - "Quelle est la première étape mentionnée dans le processus type pour optimiser et porter du code ?"
  - "Quelles sont les principales étapes à suivre pour porter du code sur un accélérateur ?"
  - "Comment le langage OpenACC permet-il au programmeur d'indiquer au compilateur les portions de code à paralléliser ?"
  - "Pourquoi le programmeur doit-il parfois intervenir manuellement pour décrire le flux de données ou optimiser les boucles malgré le travail du compilateur ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "Objectifs d'apprentissage"
* Connaître la différence entre CPU et accélérateur
* Connaître la différence entre vitesse et débit
* Connaître les étapes pour porter du code existant sur un accélérateur

## Différence entre CPU et accélérateur
Historiquement, le développement de l'informatique s'est fait autour du CPU (le processeur central), mais celui-ci ne terminait qu'une opération de calcul par cycle d'horloge. La fréquence des horloges des CPU était en hausse constante jusqu'à environ 2005, où elle atteignait un plateau autour de 4 GHz. Elle a très peu augmenté depuis et plusieurs horloges sont encore aujourd'hui sous les 4 GHz; [un article de Pär Persson Mattsson](https://www.comsol.com/blogs/havent-cpu-clock-speeds-increased-last-years/) explique bien pourquoi. Les manufacturiers ont choisi d'additionner les cœurs de calcul dans un même circuit, ouvrant ainsi la voie au calcul en parallèle.

En 2022, les tâches séquentielles sont toujours exécutées plus rapidement avec des CPU :
* Ils ont un accès direct à la mémoire qui est souvent d'une grande capacité, et
* Ils peuvent exécuter un petit nombre de tâches très rapidement en raison de la vitesse de l'horloge.

On leur connaît cependant certains inconvénients :
* Faiblesse de la bande passante mémoire,
* Des mécanismes de cache compensent pour la faiblesse de la bande passante, mais [les défauts de cache sont coûteux](https://en.wikipedia.org/wiki/CPU_cache#Cache_miss),
* Ils sont aussi plus énergivores que les accélérateurs.

Un accélérateur type comme un GPU ou un coprocesseur est un jeu de puces hautement parallèle, composé de centaines ou de milliers de cœurs de calcul de basse fréquence, relativement simples : ils sont optimisés pour le calcul en parallèle. Les GPU au haut de la gamme possèdent habituellement quelques centaines de cœurs de calcul et une large bande passante leur permettant d'accéder leur mémoire (*device memory*). Ils disposent de beaucoup plus de ressources de calcul que les CPU les plus performants en plus d'offrir un **meilleur débit** et une **meilleure performance par watt**. Par contre, ils possèdent relativement peu de mémoire et la performance par fil est faible.

!!! tip "Privilégier la vitesse ou le débit?"
Selon la tâche à effectuer, un CPU offrira l'avantage de la vitesse alors qu'un accélérateur sera privilégié pour son débit.

Une composante à **haute vitesse** peut accomplir une tâche en très peu de temps, ce qui est souhaitable pour effectuer un seul calcul séquentiel, par exemple une équation différentielle du premier ordre. Une telle composante de haute vitesse se compare à une moto de compétition ou à une voiture de course : le passager est déplacé très rapidement du point A au point B.

Une composante à **haut débit** accomplit beaucoup plus de travail, mais nécessite plus de temps, ce qui est souhaitable pour résoudre un problème hautement parallèle. Les exemples de ce genre de tâches sont nombreux : pensons par exemple aux opérations matricielles, aux transformées de Fourier et aux équations différentielles multidimensionnelles. Ce type de composante se compare à un train ou à un autobus : plusieurs passagers sont déplacés du point A au point B, mais certainement plus lentement que dans le cas de la moto ou l'automobile.

## Porter du code sur un accélérateur
On peut considérer ceci comme étant une phase du processus d'optimisation. Un cas type est constitué des étapes suivantes :
1. Profiler le code
2. Identifier les goulots d'étranglement (*bottlenecks*)
3. Remplacer le plus important goulot d'étranglement par du code optimisé
4. Valider le code sortant
5. Reprendre à partir de l'étape 1

Porter du code sur un accélérateur aurait ainsi les étapes suivantes :
1. Profiler le code
2. Localiser le parallélisme dans les goulots
3. Porter le code
    1. Décrire le parallélisme au compilateur
    2. Décrire le flux des données au compilateur
    3. Optimiser les boucles
4. Valider le résultat
5. Reprendre à partir de l'étape 1

OpenACC peut être un langage plutôt *descriptif*. Le programmeur peut donc indiquer au compilateur quelles sont les portions de code à paralléliser et laisser le compilateur effectuer le travail. Pour ce faire, il suffit d'ajouter quelques directives dans le code (voir le point 3.1 ci-dessus, *décrire le parallélisme au compilateur*). La qualité du compilateur a toutefois un effet important sur la performance; même avec les meilleurs compilateurs, il est possible que certains mouvements de données doivent être éliminés, ce que le programmeur peut faire au point 3.2, *décrire le flux des données au compilateur*. Enfin, si le programmeur possède de l'information sur comment obtenir une meilleure performance en ajustant les boucles, il en informera le compilateur au point 3.3, *optimiser les boucles*.

[^- Retour au début du tutoriel](openacc_tutorial.md) | [Page suivante, *Profileurs* ->](openacc_tutorial_-_profiling.md)