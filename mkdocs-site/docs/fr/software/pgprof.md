---
title: "PGPROF/fr"
slug: "pgprof"
lang: "fr"

source_wiki_title: "PGPROF/fr"
source_hash: "5679e344170f8bfa02e596c986188e4a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:42:27.304653+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

PGPROF est un outil simple, mais puissant pour l'analyse de programmes parallèles écrits avec OpenMP, MPI, OpenACC ou CUDA. Le profilage peut s’effectuer en mode ligne de commande ou en mode graphique.

## Utilisation
Avec les deux modes, le travail se fait généralement en deux étapes :
1.  **collecte des données**, par l’exécution de l’application avec le profilage activé;
2.  **analyse**, par la visualisation des données obtenues à la première étape.

### Modules d'environnement
Pour utiliser PGPROF, vous devez charger le [module](utiliser-des-modules.md) approprié.

Comme PGPROF fait partie du paquet pour le compilateur PGI, lancez la commande `module avail pgi` pour connaître les versions disponibles pour les modules de compilation, MPI et CUDA que vous avez déjà chargés. Pour la liste des modules PGI disponibles, lancez `module -r spider '.*pgi.*'`.
En date de décembre 2018, les modules disponibles sont :
*   pgi/13.10
*   pgi/17.3

Sélectionnez une version avec `module load pgi/version`; pour charger la version 17.3 du compilateur PGI, la commande est

```bash
module load pgi/17.3
```

### Compilation du code
Pour obtenir de PGPROF une information utile, vous devez d’abord compiler le code avec un des compilateurs PGI, soit `pgcc` pour C, `pgc++` pour C++ , `pgfortran` pour Fortran. Il est possible que du code source Fortran doive être compilé avec l’indicateur `-g`.

### Mode ligne de commande

**Collecte des données** : La première étape est d’utiliser PGPROF pour exécuter l’application, puis d’enregistrer les données sur la performance. Dans l’exemple suivant, `a.out` est l’application et `a.prof` est le fichier où les données sont enregistrées.

```bash
pgprof -o a.prof ./a.out
```

Le fichier de données peut être sauvegardé et ensuite analysé en mode graphique avec la commande *Fichier > Importer* (voir [Mode graphique](#mode-graphique)) ci-dessous ou en mode ligne de commande comme suit :

**Analyse** : Pour l’étape de visualisation, utilisez :

```bash
pgprof -i a.prof
```

Les résultats sont généralement présentés en plusieurs catégories, par exemple :
*   profil de la performance du noyau (*kernel*) GPU
*   profil de l’exécution de l’API de CUDA
*   profil de l’exécution d’OpenACC
*   profil de la performance des fonctions du CPU

```text
====== Profiling result:
Time(%)      Time     Calls       Avg       Min       Max  Name
 38.14%  1.41393s        20  70.696ms  70.666ms  70.731ms  calc2_198_gpu
 31.11%  1.15312s        18  64.062ms  64.039ms  64.083ms  calc3_273_gpu
 23.35%  865.68ms        20  43.284ms  43.244ms  43.325ms  calc1_142_gpu
  5.17%  191.78ms       141  1.3602ms  1.3120us  1.6409ms  [CUDA memcpy HtoD]
...
======== API calls:
Time(%)      Time     Calls       Avg       Min       Max  Name
 92.65%  3.49314s        62  56.341ms  1.8850us  70.771ms  cuStreamSynchronize
  3.78%  142.36ms         1  142.36ms  142.36ms  142.36ms  cuDevicePrimaryCtxRetain
...
======== OpenACC (excl):
Time(%)      Time     Calls       Avg       Min       Max  Name
 36.27%  1.41470s        20  70.735ms  70.704ms  70.773ms  acc_wait@swim-acc-data.f:223
 63.3%  1.15449s        18  64.138ms  64.114ms  64.159ms  acc_wait@swim-acc-data.f:302

======== CPU profiling result (bottom up):
Time(%)      Time  Name
 59.09%  8.55785s  cudbgGetAPIVersion
 59.09%  8.55785s   start_thread
 59.09%  8.55785s     clone
 25.75%  3.73007s  cuStreamSynchronize
 25.75%  3.73007s   __pgi_uacc_cuda_wait
 25.75%  3.73007s     __pgi_uacc_computedone
 10.38%  1.50269s       swim_mod_calc2_
```

#### Options
*   Pour faire afficher les résultats d’une seule catégorie, par exemple les résultats en rapport avec le CPU : `--cpu-profiling`.

*   Pour faire afficher d’abord les résultats pour la fonction principale, suivis de ceux pour les fonctions subordonnées : `--cpu-profiling-mode top-down`.

```bash
pgprof --cpu-profiling-mode top-down -i a.prof
```
```text
======== CPU profiling result (top down):
Time(%)      Time  Name
 97.36%  35.2596s  main
 97.36%  35.2596s   MAIN_
 32.02%  11.5976s     swim_mod_calc3_
 29.98%  10.8578s     swim_mod_calc2_
 25.93%  9.38965s     swim_mod_calc1_
  6.82%  2.46976s     swim_mod_inital_
  1.76%  637.36ms   __fvd_sin_vex_256
```

*   Pour savoir quelle partie de l’application requiert le plus de temps d’exécution : `--cpu-profiling-mode bottom-up` où les résultats pour chacune des fonctions sont suivis par ceux de la fonction qui l’appelle, remontant jusqu’à la fonction principale.

```bash
pgprof --cpu-profiling-mode bottom-up -i a.prof
```
```text
======== CPU profiling result (bottom up):
Time(%)      Time  Name
 32.02%  11.5976s  swim_mod_calc3_
 32.02%  11.5976s   MAIN_
 32.02%  11.5976s     main
 29.98%  10.8578s  swim_mod_calc2_
 29.98%  10.8578s   MAIN_
 29.98%  10.8578s     main
 25.93%  9.38965s  swim_mod_calc1_
 25.93%  9.38965s   MAIN_
 25.93%  9.38965s     main
  3.43%  1.24057s  swim_mod_inital_
```

### Mode graphique

En mode graphique, la collecte et l’analyse des données peuvent souvent se faire dans la même session. Il est toutefois possible d'analyser les données d'un fichier produit en ligne de commande.

**Collecte de données**
*   Lancez le profileur PGI.
    *   Comme l’interface utilisateur de PGPROF est basée sur Java, elle devrait être exécutée sur le nœud de calcul dans la session interactive plutôt que sur le nœud de connexion puisque ce dernier n’a pas suffisamment de mémoire (voir [Java](java.md#pieges) pour plus d’information). Pour activer la redirection X11, la session interactive peut être démarrée avec `salloc --x11 ...` (voir [Tâches interactives](running-jobs.md#taches-interactives) pour plus d'information).
*   Démarrez une nouvelle session, avec *Fichier > Nouvelle session*.
*   Sélectionnez le fichier exécutable à profiler et ajoutez les arguments de profilage, s’il y a lieu.
*   Cliquez sur *Suivant*, puis *Terminer*.

**Analyse**
*   Dans le volet *Détails du CPU*, cliquez sur le bouton *Afficher l'arborescence d'appels (appelants d'abord)*.

La fenêtre de visualisation des données comporte quatre volets.
*   Dans le volet supérieur, la partie de droite montre tous les événements selon le temps de leur exécution.
*   **Détails du GPU** : montre la performance des noyaux (*kernels*) GPU.
*   **Détails du CPU** : montre la performance des fonctions du CPU.
*   **Propriétés** : information détaillée pour la fonction sélectionnée dans le volet supérieur.

## Références
PGPROF est produit par [PGI](https://www.pgroup.com/), une filiale de [NVIDIA Corporation](https://www.nvidia.com/).
*   [Guide de démarrage](https://www.pgroup.com/resources/pgprof-quickstart.htm)
*   [Guide de l'utilisateur](https://www.pgroup.com/doc/pgi17profug.pdf)