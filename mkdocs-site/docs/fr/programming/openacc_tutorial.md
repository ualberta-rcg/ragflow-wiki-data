---
title: "OpenACC Tutorial/fr"
tags:
  []

keywords:
  []
---

Le contenu du présent tutoriel est tiré en grande partie de la session de formation intensive sur OpenACC tenue à la [GPU Technology Conference 2016](http://www.gputechconf.com/). 

OpenACC (pour *Open Accelerators*) est une interface de programmation API servant à porter du code sur des accélérateurs tels que des processeurs graphiques (GPUs pour *grapical programming units*) et des coprocesseurs. Ce standard de programmation pour le calcul parallèle a été développé par Cray, CAPS, NVIDIA et PGI. À l'instar d'[OpenMP](openmp-fr.md), le code C, C++ ou Fortran est annoté par le programmeur pour identifier les parties que le compilateur doit paralléliser. 

SHARCNET offre un tutoriel de formation autonome; cliquez sur [Introduction to GPU Programming](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

## Plan des leçons
* [Introduction](openacc-tutorial---introduction-fr.md) 
* [Profileurs](openacc_tutorial_-_profiling-fr.md)
* [Ajouter des directives](openacc_tutorial_-_adding_directives-fr.md)
* [Mouvement des données](openacc-tutorial---data-movement-fr.md)
* [Optimiser les boucles](openacc-tutorial---optimizing-loops-fr.md)

## Références 

* [OpenACC Programming and Best Practices Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
* [OpenACC API 2.7 OpenACC 2.15 Reference Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
* [Getting Started with OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
* [PGI Compiler](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
* [PG Profiler](http://www.pgroup.com/resources/pgprof-quickstart.htm)
* [NVIDIA Visual Profiler](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)