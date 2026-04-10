---
title: "Dar/fr"
slug: "dar"
lang: "fr"

source_wiki_title: "Dar/fr"
source_hash: "1e096fae0ff905b261db0f9b14aea0ad"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:58:37.908032+00:00"

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

*Page enfant de : [Stockage et gestion de fichiers](storage-and-file-management.md)*

L’utilitaire logiciel libre `dar` (pour *Disk ARchive*) a été conçu pour remplacer l’outil Unix `tar` et peut être compilé par tout système de type Unix. Il est activement maintenu depuis son lancement en 2002.

Comme `tar`, il permet les types de sauvegarde complète, différentielle et incrémentale. Cependant, l’accès aux fichiers et la restauration des données se font plus rapidement qu’avec `tar` puisque chacune des archives contient un index des fichiers; ceci est un grand avantage pour les archives volumineuses. L’utilitaire `dar` compresse chacun des fichiers séparément, ce qui offre plus de résilience dans les cas de corruption de données; il est en outre possible d’éviter la compression de fichiers fortement compressés comme les `mp4` ou `gz`. Parmi ses nombreuses fonctionnalités utiles, on trouve le chiffrement robuste; le découpage d’une archive en tranches pouvant aller jusqu’à un octet; la gestion d’attributs étendus, de fichiers épars, de liens physiques et symboliques; la détection de corruption de données dans les deux fichiers d’en-tête et leur récupération avec un minimum de perte. Pour plus d’information, consultez la [page web](http://dar.linux.free.fr) et la [comparaison avec `tar`](http://dar.linux.free.fr/doc/FAQ.html#tar).

## Où trouver l’utilitaire

Sur nos grappes, `dar` est disponible sur `/cvmfs`.
Avec [StdEnv/2020](standard-software-environments.md) :

```bash
[user_name@localhost]$ which dar
/cvmfs/soft.computecanada.ca/gentoo/2020/usr/bin/dar
[user_name@localhost]$ dar --version
dar version 2.5.11, Copyright (C) 2002-2052 Denis Corbin
...
```

## Utilisation manuelle

### Archivage de base et extraction

Supposons le sous-répertoire `test` dans le répertoire courant. Pour en faire une archive, vous pouvez entrer la commande suivante dans le répertoire courant.

```bash
[user_name@localhost]$ dar -w -c all -g test
```

Le fichier archive `all.1.dar` est créé, où `all` est le nom de base et `1` est le numéro de la tranche. Une archive peut être divisée en plusieurs tranches. Plusieurs répertoires et fichiers peuvent être inclus dans une archive, par exemple

```bash
[user_name@localhost]$ dar -w -c all -g testDir1 -g testDir2 -g file1 -g file2
```

Notez que tous les chemins doivent être relatifs au répertoire courant.

Pour lister le contenu d’une archive, utilisez uniquement le nom de base.

```bash
[user_name@localhost]$ dar -l all
```

Pour extraire un fichier dans un sous-répertoire `restore`, utilisez le nom de base et le chemin du fichier.

```bash
[user_name@localhost]$ dar -R restore/ -O -w -x all -v -g test/filename
```

L’indicateur `-O` permet de faire abstraction de la propriété des fichiers. Si vous restaurez les fichiers d’une autre personne sans être administrateur (*root*), une mauvaise attribution de propriété pourrait causer un problème. Si vous restaurez vos propres fichiers, un message sera émis si vous n’êtes pas administrateur et vous demandera de confirmer l’opération. Pour ne pas recevoir ce message, utilisez l’indicateur `-O`. Si `restore/test` existe, l’indicateur `-w` désactive l’avertissement.

Pour extraire un répertoire entier, utilisez

```bash
[user_name@localhost]$ dar -R restore/ -O -w -x all -v -g test
```

De la même manière qu’une archive est créée, vous pouvez passer plusieurs répertoires et fichiers avec plusieurs indicateurs `-g`. Remarquez que `dar` n’accepte pas les masques génériques (*wildcard masks*) Unix après `-g`.

#### Travailler avec le système de fichiers Lustre

Certains attributs étendus sont automatiquement sauvegardés quand les fichiers archivés proviennent d'un [système de fichiers Lustre](https://www.lustre.org/) (habituellement dans `/home`, `/project` ou `/scratch` sur [une de nos grappes de calcul d'usage général](national-systems.md)).
Pour connaître les attributs étendus assignés à chaque fichier archivé, utilisez l'indicateur `-alist-ea`.

```bash
dar -l all -alist-ea
```

Nous voyons des énoncés comme `Extended Attribute: [lustre.lov]`.
Avec cet attribut, les extractions de fichiers vers un endroit au format Lustre fonctionneront comme à l'habitude.
Par contre, si vous tentez d'extraire un fichier pour le stocker localement sur un [nœud de calcul](using-node-local-storage.md) (soit dans `$SLURM_TMPDIR`), vous obtiendrez des messages d'erreur comme `Error while adding EA lustre.lov : Operation not supported`.

Pour éviter ces erreurs, l'indicateur `-u` peut exclure un type particulier d'attribut et quand même extraire les fichiers touchés, par exemple

```bash
dar -R restore/ -O -w -x all -v -g test -u 'lustre*'
```

Une autre solution est de supprimer l'attribut `lustre.lov` à la création de l'archive avec le même indicateur `-u`.

```bash
dar -w -c all -g test -u 'lustre*'
```

En conclusion, ceci est nécessaire uniquement si vous avez l'intention d'extraire des fichiers vers un endroit qui n'a pas le format Lustre.

### Sauvegarde incrémentale

Pour créer une sauvegarde différentielle et incrémentale, joignez à `-A` le nom de base de l’archive référencée. Prenons l’exemple d’une sauvegarde complète nommée `monday` que vous créez le lundi.

```bash
[user_name@localhost]$ dar -w -c monday -g test
```

Le mardi, certains des fichiers sont modifiés et seuls ceux-ci sont inclus dans une nouvelle sauvegarde incrémentale nommée `tuesday`, en utilisant l'archive `monday` en référence.

```bash
[user_name@localhost]$ dar -w -A monday -c tuesday -g test
```

Le mercredi, d’autres fichiers sont modifiés et une nouvelle sauvegarde est créée nommée `wednesday`, avec l'archive `tuesday` en référence.

```bash
[user_name@localhost]$ dar -w -A tuesday -c wednesday -g test
```

Il y a maintenant trois fichiers :

```bash
[user_name@localhost]$ ls *.dar
monday.1.dar     tuesday.1.dar    wednesday.1.dar
```

Le fichier `wednesday.1.dar` contient uniquement les fichiers modifiés le mercredi, mais pas les fichiers de lundi ou mardi. La commande

```bash
[user_name@localhost]$ dar -R restore -O -x wednesday
```

ne restaurera que les fichiers modifiés le mercredi. Pour restaurer tous les fichiers, vous devrez passer par toutes les sauvegardes en ordre chronologique.

```bash
[user_name@localhost]$ dar -R restore -O -w -x monday      # restore the full backup
[user_name@localhost]$ dar -R restore -O -w -x tuesday     # restore the first incremental backup
[user_name@localhost]$ dar -R restore -O -w -x wednesday   # restore the second incremental backup
```

### Limiter la taille des tranches

Pour fixer la taille maximale en octets de chaque tranche, utilisez l’indicateur `-s` suivi d’un nombre et d’une unité de mesure (k, M, G ou T). Par exemple, pour une archive de 1340Mo, la commande

```bash
[user_name@localhost]$ dar -s 100M -w -c monday -g test
```

crée 14 tranches nommées `monday.{1..14}.dar`. Pour extraire de toutes ces tranches, utilisez le nom de base.

```bash
[user_name@localhost]$ dar -O -x monday
```

## Scripts externes

Un membre de notre équipe a créé des fonctions Bash pour rendre l'utilisation de `dar` plus facile. Nous vous invitons à vous en inspirer pour la préparation de vos propres scripts. Pour les détails, voyez [ici](https://github.com/razoumov/sharedSnippets).