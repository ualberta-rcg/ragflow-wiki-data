---
title: "OpenACC Tutorial - Introduction/fr"
tags:
  []

keywords:
  []
---

## Différence entre CPU et accélérateur 
Historiquement, le développement de l'informatique s'est fait autour du CPU (le processeur central), mais celui-ci ne terminait qu'une opération de calcul par cycle d'horloge. La fréquence des horloges des CPU était en hausse constante jusqu'à environ 2005, où elle atteignait un plateau autour de 4GHz. Elle a très peu augmenté depuis et plusieurs horloges sont encore aujourd'hui sous les 4GHz; [un article de Pär Persson Mattsson](https://www.comsol.com/blogs/havent-cpu-clock-speeds-increased-last-years/) explique bien pourquoi. Les manufacturiers ont choisi d'additionner les cœurs de calcul dans un même circuit, ouvrant ainsi la voie au calcul en parallèle.

En 2022, les tâches séquencielles sont toujours exécutées plus rapidement avec des CPU&nbsp;:
* ils ont un accès direct à la mémoire qui est souvent d'une grande capacité et
* ils peuvent exécuter un petit nombre de tâches très rapidement en raison de la vitesse de l'horloge.

On leur connaît cependant certains inconvénients&nbsp;:
* faiblesse de la bande passante mémoire,
* des mécanismes de cache compensent pour la faiblesse de la bande passante, mais [les défauts de cache sont coûteux](https://en.wikipedia.org/wiki/CPU_cache#Cache_miss),
* ils sont aussi plus énergivores que les accélérateurs. 

Un accélérateur type comme un GPU ou un coprocesseur est un jeu de puces hautement parallèle, composé de centaines ou de milliers de cœurs de calcul de basse fréquence, relativement simples&nbsp;: ils sont optimisés pour le calcul en parallèle. Les GPU au haut de la gamme possèdent habituellement quelques centaines de cœurs de calcul et une large bande passante leur permettant d'accéder leur mémoire (*device memory*). Ils disposent de beaucoup plus de ressources de calcul que les CPU les plus performants en plus d'offrir un **meilleur débit** et une **meilleure performance par watt**. Par contre, ils possèdent relativement peu de mémoire et la performance par fil est faible. 

## Porter du code sur un accélérateur 
On peut considérer ceci comme étant une phase du processus d'optimisation. Un cas type est constitué des étapes suivantes&nbsp;: 
# profiler le code
# identifier les goulots d'étranglement (*bottlenecks*)
# remplacer le plus important goulot d'étranglement par du code optimisé
# valider le code sortant
# reprendre à partir de l'étape 1

Porter du code sur un accélérateur aurait ainsi les étapes suivantes&nbsp;:
# profiler le code
# localiser le parallélisme dans les goulots
# porter le code
## décrire le parallélisme au compilateur
## décrire le flux des données au compilateur
## optimiser les boucles
# valider le résultat
# reprendre à partir de l'étape 1

OpenACC peut être  un langage plutôt *descriptif*. Le programmeur peut donc indiquer au compilateur quelles sont les portions de code à paralléliser et laisser le compilateur effectuer le travail. Pour ce faire, il suffit d'ajouter quelques directives dans le code (voir le point 3.1 ci-dessus, *décrire le parallélisme au compilateur*). La qualité du compilateur a toutefois un effet important sur la performance; même avec les meilleurs compilateurs, il est possible que certains mouvements de données doivent être éliminés, ce que le programmeur peut faire au point 3.2, *décrire le flux des données au compilateur*. Enfin, si le programmeur possède de l'information sur comment obtenir une meilleure performance en ajustant les boucles, il en informera le compilateur au point 3.3, *optimiser les boucles*. 

[^- Retour au début du tutoriel](openacc-tutorial-fr.md) | [Page suivante, *Profileurs* ->](openacc-tutorial---profiling-fr.md)