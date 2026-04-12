---
title: "Debugging and profiling/fr"
slug: "debugging_and_profiling"
lang: "fr"

source_wiki_title: "Debugging and profiling/fr"
source_hash: "eb73223b39c8bddc53dcf07aef6a0f73"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:50:45.373154+00:00"

tags:
  []

keywords:
  - "erreurs d'exécution"
  - "outils"
  - "développement logiciel"
  - "débogage"
  - "profilage"

questions:
  - "Quelle est la différence principale entre le rôle d'un logiciel de débogage et celui d'un logiciel de profilage selon le texte ?"
  - "Dans quel type d'environnement sur les grappes de calcul est-il strictement recommandé d'effectuer ses sessions de débogage ?"
  - "Quels sont les modules et les architectures spécifiques requis pour pouvoir utiliser l'ensemble d'outils de profilage Scalasca ?"
  - "Quelle est la différence principale entre le rôle d'un logiciel de débogage et celui d'un logiciel de profilage selon le texte ?"
  - "Dans quel type d'environnement sur les grappes de calcul est-il strictement recommandé d'effectuer ses sessions de débogage ?"
  - "Quels sont les modules et les architectures spécifiques requis pour pouvoir utiliser l'ensemble d'outils de profilage Scalasca ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Une étape importante en développement logiciel, particulièrement en Fortran et C/C++, est l'utilisation d'un logiciel de débogage pour détecter et identifier l'origine des erreurs d'exécution (par exemple, les fuites de mémoire, les exceptions de virgule flottante, etc.). Après avoir éliminé les erreurs, la prochaine étape est de profiler le programme avec un logiciel de profilage pour déterminer le pourcentage du temps d'exécution pour chacune des sections du code source avec un scénario de test représentatif. Un profileur peut fournir de l'information sur le nombre de fois qu'une fonction est appelée, quelles sont les fonctions qui l'appellent ou encore combien de millisecondes en moyenne coûte chaque appel.

## Outils

Nos grappes offrent un choix de débogueurs et de profileurs pour effectuer le travail en mode graphique par connexion X11 ou en mode ligne de commande.

!!! attention "Environnement de débogage recommandé"
    Le débogage devrait être effectué dans une [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives) et non sur un nœud de connexion. Il est strictement recommandé d'utiliser une tâche interactive pour vos sessions de débogage sur les grappes de calcul.

### Débogueur GNU (gdb)

Voir [GDB](gdb.md).

### Débogueur PGI (pgdb)

Voir [PGDBG](pgdbg.md).

### Débogueur ARM (ddt)

Voir [ARM](../software/arm_software.md).

### Profileur GNU (gprof)

Voir [Gprof](gprof.md).

### Profileur Scalasca (scalasca, scorep, cube)

Scalasca est un ensemble d'outils *open source* avec une interface graphique pour le profilage parallèle avec GPU. Ces outils sont disponibles pour **gcc 9.3.0** et **OpenMPI 4.0.3**, dans des architectures AVX2 et AVX512. Chargez l'environnement avec :

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scalasca
```

La version courante est **2.5**. Vous trouverez plus d'information et des exemples de flux de travail dans le [Scalasca User Guide](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.5/docs/manual/).

### Profileur PGI (pgprof)

Voir [Pgprof](../software/pgprof.md).

### Profileur Nvidia en ligne de commande (nvprof)

Voir [nvprof](nvprof.md).

### Valgrind

Voir [Valgrind](../software/valgrind.md).

## Autres références

*   [Introduction to (Parallel) Performance](https://docs.scinet.utoronto.ca/index.php/Introduction_To_Performance), SciNet
*   [Code profiling on Graham](https://www.youtube.com/watch?v=YsF5KMr9uEQ) (vidéo de 54 minutes), SHARCNET