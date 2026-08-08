---
title: "Debugging and profiling/fr"
slug: "debugging_and_profiling"
lang: "fr"

source_wiki_title: "Debugging and profiling/fr"
source_hash: "54b4799f4a13fedd9fdf3d9a34fa2739"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:30:09.047477+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

Une étape importante en développement logiciel, particulièrement en Fortran et C/C++, est l'utilisation d'un logiciel de débogage pour détecter et identifier l'origine des erreurs d'exécution (par exemple les fuites de mémoire, les exceptions de virgule flottante, etc.). Après avoir éliminé les erreurs, la prochaine étape est d'utiliser un logiciel de profilage pour déterminer le pourcentage du temps d'exécution pour chacune des sections du code source avec un scénario de test représentatif. Un profileur peut fournir de l'information sur le nombre de fois qu'une fonction est appelée, quelles sont les fonctions qui l'appellent ou encore combien de millisecondes en moyenne coûte chaque appel.

## Déboguer sur une grappe

**Puisque les sessions de débogage sur les nœuds de connexion sont à éviter, il faut plutôt passer par une tâche interactive.** Les options sont :

*   utiliser la commande Slurm `salloc ...`; voir **[Tâches interactives](../running-jobs/running_jobs.md#tâches-interactives)**;
*   ouvrir une session JupyterLab; voir **[Lancer JupyterLab](../interactive/jupyterlab.md#lancer-jupyterlab)** pour les instructions de connexion et pour connaître les [applications préconstruites](../interactive/jupyterlab.md#applications-préconstruites);
*   démarrer une session de bureau distant pour faire du profilage visuel; voir **[cette partie de la page JupyterLab](../interactive/jupyterlab.md)** ou **[les références pour Trillium ou Nibi dans la page Open OnDemand](../interactive/open_ondemand.md#introduction)**.

## Outils

Nos grappes offrent un choix de débogueurs et de profileurs pour effectuer le travail en mode graphique par connexion X11 ou en mode ligne de commande.

### Débogueur GNU (gdb)

Voir [GDB](gdb.md).

### Débogueur PGI (pgdb)

Voir [PGDBG](pgdbg.md).

### Débogueur ARM (ddt)

Voir [ARM](../software/arm_software.md).

### Profileur GNU (gprof)

Voir [Gprof](gprof.md).

### Profileur Scalasca (scalasca, scorep, cube)

Scalasca est un ensemble d'outils *open source* avec une interface graphique pour le profilage parallèle avec GPU. Ces outils sont disponibles pour **gcc 9.3.0** et **OpenMPI 4.0.3**, dans des architectures AVX2 et AVX512. Chargez l'environnement avec

```bash
module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scalasca
```

La version courante est **2.5**. Vous trouverez plus d'information et des exemples de flux de travail dans [Scalasca User Guide](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.5/docs/manual/).

### Profileur PGI (pgprof)

Voir [Pgprof](../software/pgprof.md).

### Profileur Nvidia en ligne de commande (nvprof)

Voir nvprof.

### Valgrind

Voir [Valgrind](../software/valgrind.md).

## Autres références

*   [Introduction to (Parallel) Performance](https://docs.scinet.utoronto.ca/index.php/Introduction_To_Performance), SciNet
*   [Code profiling on Graham](https://www.youtube.com/watch?v=YsF5KMr9uEQ) (vidéo de 54 minutes), SHARCNET