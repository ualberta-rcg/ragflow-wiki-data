---
title: "Using node-local storage/fr"
slug: "using_node-local_storage"
lang: "fr"

source_wiki_title: "Using node-local storage/fr"
source_hash: "13c70ea6c2ca8763daa8c092c7c72fe3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:28:18.999326+00:00"

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

Quand [l'ordonnanceur Slurm démarre une tâche](running-jobs.md), un répertoire temporaire est créé sur chacun des nœuds qui sont assignés à cette tâche.
Par la variable d'environnement `$SLURM_TMPDIR`, Slurm configure ensuite le chemin complet pour ce répertoire.

Parce que ce répertoire se trouve sur un disque local, les opérations en entrée et en sortie (I/O) sont presque toujours plus rapides qu'avec le [stockage sur le réseau](storage-and-file-management.md) (/project, /scratch et /home). En particulier, le stockage sur disque local est à privilégier pour les transactions fréquentes de petites quantités de données. Toutes les tâches qui font beaucoup de lecture et d'écriture (ce qui est le cas pour la plupart des tâches) seront probablement exécutées plus rapidement en utilisant `$SLURM_TMPDIR` plutôt que le stockage sur le réseau.

De par sa nature temporaire, `$SLURM_TMPDIR` est plus compliqué à utiliser que le stockage sur le réseau.
Les données en entrée doivent être copiées du réseau à `$SLURM_TMPDIR` avant qu'elles puissent être lues
et les données en sortie doivent être copiées de `$SLURM_TMPDIR` au réseau avant que la tâche soit terminée pour que ces données soient conservées.

# Données en entrée

Pour pouvoir *lire* les données contenues dans `$SLURM_TMPDIR`, vous devez d'abord y copier les données.
Dans les cas les plus simples, vous pouvez faire ceci avec `cp` ou `rsync`.

```bash
cp /project/def-someone/you/input.files.* $SLURM_TMPDIR/
```

Cependant, ceci pourrait ne pas fonctionner avec une grande quantité de données ou dans le cas où les données doivent être lues par des processus exécutés sur des nœuds différents.
Pour plus d'information, voir [Tâches utilisant plusieurs nœuds](#taches-utilisant-plusieurs-noeuds) et [Espace disponible](#espace-disponible) ci-dessous.

## Bibliothèques et fichiers exécutables

Un cas particulier se présente avec du code comme donnée en entrée. Pour exécuter une application, l'interpréteur (*shell*) démarré par Slurm doit ouvrir au moins un des fichiers de cette application dont la lecture s'effectue généralement sur l'espace de stockage du réseau. Il est rare qu'une application ne soit lancée qu'avec un seul fichier; en effet, la plupart des applications font aussi appel à plusieurs fichiers, par exemple des bibliothèques.

Nous remarquons en particulier que les applications exécutées dans un environnement virtuel [Python](python.md) génèrent un très grand nombre de transactions I/O, plus qu'il n'en faut d'ailleurs pour créer l'environnement virtuel lui-même. C'est pourquoi notre recommandation est de [créer un environnement virtuel dans vos tâches](python.md#creer-un-environnement-virtuel-dans-vos-taches) avec `$SLURM_TMPDIR`.

# Données en sortie

Les données en sortie doivent être copiées de `$SLURM_TMPDIR` vers un espace de stockage permanent avant que la tâche ne se termine. Si une tâche s'arrête par manque de temps, les dernières lignes du script ne seront peut-être pas exécutées.
Les solutions suivantes sont possibles :

*   demander plus de temps pour que l'application puisse être exécutée au complet, quoique ce n'est pas toujours possible;
*   placer des points de contrôle dans l'espace de stockage sur le réseau et pas dans `$SLURM_TMPDIR`;
*   écrire une fonction pour intercepter un signal.

## Intercepter un signal

Vous pouvez demander à Slurm d'envoyer un signal à la tâche peu avant qu'elle n'atteigne sa limite de temps pour que celle-ci copie le résultat de `$SLURM_TMPDIR` vers l'espace de stockage sur le réseau. Ceci est utile si votre estimé du temps d'exécution est incertain ou que vous enchaînez plusieurs tâches Slurm pour effectuer un long calcul.

Pour ce faire, écrivez une fonction pour l'interpréteur (*shell*) afin que la copie soit faite et utilisez la commande `trap` pour associer la fonction avec le signal. Pour plus d'information, voir [cette page du CRIANN](https://services.criann.fr/en/services/hpc/cluster-myria/guide/signals-sent-by-slurm/).

Avec cette méthode, le contenu de `$SLURM_TMPDIR` ne sera pas conservé si un nœud tombe en panne ou si le système de fichiers réseau connaît un problème.

# Tâches utilisant plusieurs nœuds

Si une tâche est répartie sur plusieurs nœuds et que chacun d'eux doit utiliser les données, `cp` ou `tar -x` ne sont pas suffisants.

## Copier des fichiers

Pour copier un ou plusieurs fichiers sur `$SLURM_TMPDIR` de chacun des nœuds alloués, utilisez

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 cp file [files...] $SLURM_TMPDIR
```

## Archives compressées

### ZIP

Pour extraire vers `$SLURM_TMPDIR` :

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 unzip archive.zip -d $SLURM_TMPDIR
```

### Tarball
Pour extraire vers `$SLURM_TMPDIR` :

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 tar -xvf archive.tar.gz -C $SLURM_TMPDIR
```

# Espace disponible

Dans le cas de [Trillium](trillium.md), `$SLURM_TMPDIR` est implémenté comme `RAMdisk`; l'espace disponible est donc limité par la mémoire du nœud, moins la capacité de RAM utilisée par votre application.

Pour les grappes d'usage général, la quantité d'espace disponible dépend de la grappe et du nœud auquel votre tâche est assignée.

| Grappe | Capacité `$SLURM_TMPDIR` | Capacité des disques |
| :----- | :----------------------- | :------------------- |
| [Fir](fir.md) | 7T | 7.84T |
| [Narval](narval.md) | 800G | 960G, 3.84T |
| [Nibi](nibi.md) | 3T | 3T, 11T |
| [Rorqual](rorqual.md) | 375G | 480G, 3.84T |

Si votre tâche réserve des [nœuds entiers](advanced-mpi-scheduling.md#noeuds-entiers), il est raisonnable de penser qu'autant d'espace `$SLURM_TMPDIR` sera disponible sur chaque nœud.
Par contre, si votre tâche demande moins qu'un nœud entier, les autres tâches pourront aussi écrire dans le même système de fichiers (mais non dans le même répertoire) et ainsi limiter l'espace disponible pour votre tâche.

À chacun des sites, certains nœuds ont plus d'espace disque local qu'indiqué dans le tableau; voyez la section *Caractéristiques des nœuds* pour chacune des grappes ([Fir](fir.md), [Narval](narval.md), [Nibi](nibi.md), [Rorqual](rorqual.md)).