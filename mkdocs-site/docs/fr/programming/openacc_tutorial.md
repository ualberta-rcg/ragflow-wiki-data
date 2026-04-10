---
title: "OpenACC Tutorial/fr"
slug: "openacc_tutorial"
lang: "fr"

source_wiki_title: "OpenACC Tutorial/fr"
source_hash: "69eb83ee6f6928e167f086a89b0ae46e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:21:01.300231+00:00"

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

Le contenu de ce tutoriel provient en grande partie de la session de formation intensive sur OpenACC qui s'est déroulée à la [GPU Technology Conference 2016](http://www.gputechconf.com/).

OpenACC (pour *Open Accelerators*) est une interface de programmation (API) qui sert à porter du code sur des accélérateurs comme les processeurs graphiques (GPU, de l'anglais *graphic processing unit*) et les coprocesseurs. Ce standard de programmation pour le calcul parallèle a été développé par Cray, CAPS, NVIDIA et PGI. À l'instar d'[OpenMP](openmp.md), le code C, C++ ou Fortran est annoté par le programmeur pour identifier les parties que le compilateur doit paralléliser.

SHARCNET offre un tutoriel de formation autonome; cliquez sur le lien [Introduction to GPU Programming](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

!!! note "Prérequis"
    Ce tutoriel démontre comment utiliser OpenACC pour accélérer des programmes en C, C++ ou Fortran; une bonne connaissance d'un de ces langages vous permettra de tirer meilleur profit des exercices.

!!! tip "Avant de commencer"
    Téléchargez les exemples à partir du [répertoire GitHub](https://github.com/calculquebec/cq-formation-openacc).

## Plan des leçons

*   [Introduction](openacc-tutorial-introduction.md)
*   [Profileurs](openacc-tutorial-profiling.md)
*   [Ajouter des directives](openacc-tutorial-adding-directives.md)
*   [Mouvement des données](openacc-tutorial-data-movement.md)
*   [Optimiser les boucles](openacc-tutorial-optimizing-loops.md)

## Références

*   [OpenACC Programming and Best Practices Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/openacc-guide.pdf)
*   [OpenACC API 2.7 OpenACC 2.15 Reference Guide (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
*   [Getting Started with OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
*   [PGI Compiler](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
*   [PG Profiler](http://www.pgroup.com/resources/pgprof-quickstart.htm)
*   [NVIDIA Visual Profiler](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)