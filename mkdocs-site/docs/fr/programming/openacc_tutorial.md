---
title: "OpenACC Tutorial/fr"
slug: "openacc_tutorial"
lang: "fr"

source_wiki_title: "OpenACC Tutorial/fr"
source_hash: "69eb83ee6f6928e167f086a89b0ae46e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:51:58.863386+00:00"

tags:
  []

keywords:
  - "OpenACC"
  - "processeurs graphiques"
  - "directives"
  - "tutoriel"
  - "calcul parallèle"

questions:
  - "Qu'est-ce qu'OpenACC et quel est son rôle principal dans la programmation parallèle ?"
  - "Quels sont les langages de programmation requis et pris en charge pour utiliser les directives OpenACC dans ce tutoriel ?"
  - "Quelles sont les différentes leçons abordées dans le plan de formation de ce tutoriel ?"
  - "Qu'est-ce qu'OpenACC et quel est son rôle principal dans la programmation parallèle ?"
  - "Quels sont les langages de programmation requis et pris en charge pour utiliser les directives OpenACC dans ce tutoriel ?"
  - "Quelles sont les différentes leçons abordées dans le plan de formation de ce tutoriel ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le contenu du présent tutoriel est tiré en grande partie de la session de formation intensive sur OpenACC tenue à la [GPU Technology Conference 2016](http://www.gputechconf.com/).

OpenACC (pour *Open Accelerators*) est une interface de programmation API servant à porter du code sur des accélérateurs tels que des processeurs graphiques (GPU, pour *Graphics Processing Unit*) et des coprocesseurs. Ce standard de programmation pour le calcul parallèle a été développé par Cray, CAPS, NVIDIA et PGI. À l'instar d'[OpenMP](openmp.md), le code C, C++ ou Fortran est annoté par le programmeur pour identifier les parties que le compilateur doit paralléliser.

SHARCNET offre un tutoriel de formation autonome; cliquez sur [Introduction à la programmation GPU](https://training.sharcnet.ca/courses/enrol/index.php?id=173).

!!! info "Prérequis"
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
*   [Guide de référence OpenACC API 2.7 et 2.15 (PDF)](https://www.openacc.org/sites/default/files/inline-files/API%20Guide%202.7.pdf)
*   [Pour commencer avec OpenACC](https://developer.nvidia.com/blog/getting-started-openacc/)
*   [Compilateur PGI](https://docs.nvidia.com/hpc-sdk/pgi-compilers/legacy.html)
*   [Profileur PG](http://www.pgroup.com/resources/pgprof-quickstart.htm)
*   [Profileur visuel NVIDIA](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#visual-profiler)