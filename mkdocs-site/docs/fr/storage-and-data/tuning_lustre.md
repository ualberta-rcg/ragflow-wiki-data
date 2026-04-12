---
title: "Tuning Lustre/fr"
slug: "tuning_lustre"
lang: "fr"

source_wiki_title: "Tuning Lustre/fr"
source_hash: "4886be679143067d5589fa12d78b5ded"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:12:13.231366+00:00"

tags:
  []

keywords:
  - "resegmenter"
  - "stripe_count"
  - "objets alloués"
  - "lfs getstripe"
  - "lfs setstripe"
  - "processus MPI"
  - "ouvertures et fermetures de fichiers"
  - "lmm_stripe_offset"
  - "lfs migrate"
  - "Système de fichiers Lustre"
  - "fichiers de données"
  - "programme parallèle"
  - "lmm_stripe_count"
  - "stripe_size"

questions:
  - "Quels sont les rôles respectifs des paramètres stripe_count et stripe_size dans le système de fichiers Lustre ?"
  - "Quelles commandes permettent de consulter et de configurer la segmentation d'un répertoire ou d'un nouveau fichier ?"
  - "Comment doit-on procéder pour appliquer de nouveaux paramètres de répartition à un fichier déjà existant ?"
  - "Comment le fait d'augmenter le nombre de disques alloués à un fichier influence-t-il à la fois ses performances et sa vulnérabilité matérielle ?"
  - "Quelle est la stratégie de lecture et de répartition recommandée pour les petits fichiers par rapport aux gros fichiers de données dans un environnement MPI ?"
  - "Quelles sont les bonnes pratiques générales à adopter concernant l'ouverture, la fermeture et l'agglomération des fichiers pour optimiser les opérations d'entrée/sortie ?"
  - "Quel est le nombre d'objets alloués par défaut pour le fichier \"new_file\" et quelle variable définit cette valeur ?"
  - "Quelle commande spécifique permet de resegmenter un ancien fichier existant ?"
  - "Quelles informations de configuration technique sont révélées par les colonnes telles que `obdidx` et `objid` au début du texte ?"
  - "Comment le fait d'augmenter le nombre de disques alloués à un fichier influence-t-il à la fois ses performances et sa vulnérabilité matérielle ?"
  - "Quelle est la stratégie de lecture et de répartition recommandée pour les petits fichiers par rapport aux gros fichiers de données dans un environnement MPI ?"
  - "Quelles sont les bonnes pratiques générales à adopter concernant l'ouverture, la fermeture et l'agglomération des fichiers pour optimiser les opérations d'entrée/sortie ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Système de fichiers Lustre

[Lustre](http://lustre.org/) est un système de fichiers distribué de haute performance qui vous permet de réaliser des opérations d'entrée-sortie en parallèle avec un fort débit. Il y a cependant quelques précautions à prendre si l'on veut obtenir un rendement maximal. Les conseils présentés ici s'adressent aux utilisateurs et utilisatrices expérimenté.e.s et doivent être suivis avec prudence. Assurez-vous d'effectuer des tests pour vérifier la validité scientifique des résultats obtenus et pour faire en sorte que les modifications entraînent une réelle amélioration de la performance.

## Paramètres `stripe_count` et `stripe_size`

Pour chaque fichier ou répertoire, il est possible de modifier ces paramètres.
*   `stripe_count` est le nombre de disques sur lesquels les données sont réparties;
*   `stripe_size` est la taille du plus petit bloc de données alloué dans le système de fichiers.

Il est possible de connaître la valeur de ces paramètres pour un fichier ou un répertoire donné avec la commande :
```bash
lfs getstripe /chemin/vers/fichier
```

De même, il est possible de modifier ces paramètres pour un répertoire donné avec la commande :
```bash
lfs setstripe -c nombre /chemin/vers/repertoire
```

Par exemple, si `nombre`=8, le fichier sera réparti sur huit disques RAID et chaque Mo sera écrit séquentiellement sur jusqu'à 8 serveurs.

```bash
lfs setstripe -c 8 /home/utilisateur/nouveaurepertoire
```

Le fait de changer ces paramètres ne modifiera pas un fichier existant; pour les changer, il faut migrer le fichier ou le copier (et non le déplacer) vers un répertoire ayant des paramètres différents. Pour créer un fichier vide avec des valeurs particulières pour `stripe_count` et `stripe_size` sans modifier les paramètres du répertoire, vous pouvez exécuter `lfs setstripe` sur le nom du fichier que vous voulez créer : le fichier sera créé vide et aura les paramètres spécifiés.

Exemple d'un répertoire non segmenté avec le fichier `example_file` (`lmm_stripe_count` est égal à 1 et il n'y a qu'un seul objet) :

```bash
$ lfs getstripe striping_example/
striping_example/
stripe_count:  1 stripe_size:   1048576 pattern:       raid0 stripe_offset: -1
striping_example//example_file
lmm_stripe_count:  1
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 2
 	obdidx		 objid		 objid		 group
 	     2	       3714477	     0x38adad	   0x300000400
```

Nous pouvons modifier la segmentation de ce répertoire pour utiliser 2 disques et créer un nouveau fichier.

```bash
$ lfs setstripe -c 2 striping_example
$ dd if=/dev/urandom of=striping_example/new_file bs=1M count=10
$ lfs getstripe striping_example/
striping_example/
stripe_count:  2 stripe_size:   1048576 pattern:       raid0 stripe_offset: -1
striping_example//example_file
lmm_stripe_count:  1
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 2
 	obdidx		 objid		 objid		 group
 	     2	       3714477	     0x38adad	   0x300000400
striping_example//new_file
lmm_stripe_count:  2
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 3
 	obdidx		 objid		 objid		 group
 	     3	       3714601	     0x38ae29	   0x400000400
 	     0	       3714618	     0x38ae3a	   0x2c0000400
```

Seulement le fichier `new_file` utilise par défaut `count=2` (`lmm_stripe_count`) et 2 objets sont alloués.

Pour resegmenter l'ancien fichier, on utilise `lfs migrate` :

```bash
$ lfs migrate -c 2 striping_example/example_file
$ lfs getstripe striping_example/example_file
striping_example/example_file
lmm_stripe_count:  2
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    2
lmm_stripe_offset: 10
 	obdidx		 objid		 objid		 group
 	    10	       3685344	     0x383be0	   0x500000400
 	    11	       3685328	     0x383bd0	   0x540000400
```

`lmm_stripe_count` est maintenant de 2 et deux objets sont alloués.

!!! note "Considération importante"
    Augmenter le nombre de disques peut améliorer les performances, mais rend aussi le fichier plus vulnérable aux défaillances matérielles.

!!! tip "Gestion des petits fichiers pour les programmes parallèles"
    Lorsqu'un programme parallèle a besoin de lire un petit fichier (< 1 Mo), par exemple un fichier de configuration, il est plus efficace de placer ce fichier sur un seul disque (`stripe_count=1`), de le lire avec le processus maître (`master rank`), et ensuite de l'envoyer aux autres processus à l'aide de `MPI_Broadcast` ou `MPI_Scatter`.

!!! tip "Optimisation pour les gros fichiers de données avec MPI"
    Lorsque l'on manipule de gros fichiers de données, il est préférable d'utiliser autant de disques que le nombre de processus MPI. La taille sera habituellement la même que celle du tampon de données qui est lu ou écrit par chaque processus; par exemple, si chaque processus lit 1 Mo de données à la fois, alors 1 Mo sera probablement l'idéal. Si vous n'avez pas de bonne raison de modifier cette taille, nous vous recommandons de la laisser à sa valeur par défaut, qui a été optimisée pour des fichiers de grande taille.

    !!! warning "Important : Taille du bloc"
        La taille du bloc doit toujours être un multiple entier de 1 Mo.

!!! tip "Réduction des opérations d'ouverture et de fermeture de fichiers"
    De manière générale, il faut réduire au maximum les ouvertures et fermetures de fichiers. Il sera donc préférable d’agglomérer toutes les données dans un seul fichier plutôt que d'écrire une multitude de petits fichiers. Il sera aussi grandement préférable d'ouvrir le fichier une seule fois au début de l'exécution et de le fermer à la fin, plutôt que de l'ouvrir et de le fermer à l'intérieur d'une même exécution chaque fois que l'on veut y ajouter de nouvelles données.

## Pour plus d'information

*   [Archivage et compression de fichiers](archiving-and-compressing-files.md)