---
title: "Debugging and profiling/fr"
tags:
  []

keywords:
  []
---

Une étape importante en développement logiciel, particulièrement en Fortran et C/C++, est l'utilisation d'un logiciel de débogage pour détecter et identifier l'origine des erreurs d'exécution (par exemple les fuites de mémoire, les exceptions de virgule flottante, etc.). Après avoir éliminé les erreurs, la prochaine étape est de profiler le programme avec un logiciel de profilage pour déterminer le pourcentage du temps d'exécution pour chacune des sections du code source avec un scénario de test représentatif. Un profileur peut fournir de l'information sur le nombre de fois qu'une fonction est appelée, quelles sont les fonctions qui l'appellent ou encore combien de millisecondes en moyenne coûte chaque appel.   

=Outils=

Nos grappes offrent un choix de débogueurs et de profileurs pour effectuer le travail en mode graphique par connexion X11 ou en mode ligne de commande. Le débogage devrait être effectué dans une [tâche interactive](running-jobs-fr#tâches_interactives.md) et non dans un nœud de connexion. 

## Débogueur GNU (gdb) 

Voir [GDB](gdb-fr.md).

## Débogueur PGI (pgdb) 
Voir [PGDBG](pgdbg-fr.md).

## Débogueur ARM (ddt) 

Voir [ARM](arm-software-fr.md).

## Profileur GNU (gprof) 

Voir [Gprof](gprof.md).

## Profileur Scalasca (scalasca, scorep, cube) 

Scalasca est un ensemble d'outils <i>open source</i> avec une interface graphique pour le profilage parallèle avec GPU. Ces outils sont disponibles pour <b>gcc 9.3.0</b> et <b>OpenMPI 4.0.3</b>, dans des architectures AVX2 et AVX512. Chargez l'environnement avec

`module load StdEnv/2020 gcc/9.3.0 openmpi/4.0.3 scalasca`

La version courante est <b>2.5</b>. Vous trouverez plus d'information et des exemples de flux de travail dans [Scalasca User Guide](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.5/docs/manual/).

## Profileur PGI (pgprof) 
Voir [Pgprof](pgprof-fr.md).

## Profileur Nvidia en ligne de commande (nvprof) 
Voir [nvprof](nvprof.md).

## Valgrind

Voir [Valgrind](valgrind-fr.md).

= Autres références =

* [Introduction to (Parallel) Performance](https://docs.scinet.utoronto.ca/index.php/Introduction_To_Performance), SciNet
* [Code profiling on Graham](https://www.youtube.com/watch?v=YsF5KMr9uEQ) (vidéo de 54 minutes), SHARCNET