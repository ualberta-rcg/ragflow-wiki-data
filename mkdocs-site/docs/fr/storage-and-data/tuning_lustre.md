---
title: "Tuning Lustre/fr"
slug: "tuning_lustre"
lang: "fr"

source_wiki_title: "Tuning Lustre/fr"
source_hash: "4886be679143067d5589fa12d78b5ded"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:10:34.922145+00:00"

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

# Système de fichiers Lustre

[Lustre](http://lustre.org/) est un système de fichiers distribué de haute performance qui vous permet de réaliser des opérations d'entrée-sortie en parallèle avec un fort débit. Il y a cependant quelques mises en garde à observer si l'on veut obtenir une performance maximale. Les conseils présentés ici sont destinés aux usagers expérimentés et doivent être suivis avec prudence. Assurez-vous d'effectuer des essais afin de valider la rigueur scientifique des résultats obtenus et pour vous assurer que les modifications mènent à une véritable amélioration de la performance.

## Paramètres `stripe_count` et `stripe_size`

Pour chaque fichier ou répertoire, il est possible de modifier ces paramètres.
*   `stripe_count` est le nombre de disques sur lesquels les données sont fragmentées;
*   `stripe_size` est la taille de la plus petite unité d'allocation de données dans le système de fichiers.

Il est possible de connaître la valeur de ces paramètres pour un fichier ou un répertoire donné avec la commande :

```bash
lfs getstripe /path/to/file
```

De même, il est possible de modifier ces paramètres pour un répertoire donné avec la commande :

```bash
lfs setstripe -c count /path/to/dir
```

Par exemple, si *count*=8, le fichier sera réparti sur huit disques RAID et chaque Mo sera écrit séquentiellement sur jusqu'à 8 serveurs.

```bash
lfs setstripe -c 8 /home/user/newdir
```

Le fait de changer ces paramètres ne modifiera pas un fichier existant; pour les changer, il faut migrer le fichier ou le copier (et non le déplacer) vers un répertoire ayant des paramètres différents. Pour créer un fichier vide avec des valeurs particulières pour `stripe_count` et `stripe_size` sans modifier les paramètres du répertoire, vous pouvez lancer `lfs setstripe` sur le nom du fichier que vous voulez créer : le fichier sera créé vide et aura les paramètres spécifiés.

Exemple d'un répertoire non fragmenté avec le fichier *example_file* (`lmm_stripe_count` est égal à 1 et il n'y a qu'un seul objet) :

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

Nous pouvons modifier la fragmentation de ce répertoire pour utiliser 2 disques et créer un nouveau fichier.

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

Seulement le fichier *new_file* utilise par défaut count=2 (`lmm_stripe_count`) et 2 objets sont alloués.

Pour refragmenter l'ancien fichier, on utilise `lfs migrate` :

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

Augmenter le nombre de disques peut augmenter les performances, mais rend aussi le fichier plus vulnérable aux pannes matérielles.

Lorsqu'un programme parallèle a besoin de lire un petit fichier (< 1Mo), par exemple un fichier de configuration, il est plus efficace de placer ce fichier sur un seul disque (*stripe count=1*), de le lire avec le processus principal (*master rank*), et ensuite de l'envoyer aux autres processus à l'aide de `MPI_Broadcast` ou `MPI_Scatter`.

Lorsque l'on manipule de gros fichiers de données, il est préférable d'utiliser autant de disques que le nombre de processus MPI. La taille sera habituellement la même que celle du tampon de données qui est lu ou écrit par chaque processus; par exemple, si chaque processus lit 1Mo de données à la fois, alors 1Mo sera probablement l'idéal. Si vous n'avez pas de raison valable de modifier cette taille, nous vous recommandons de la laisser à sa valeur par défaut, qui a été optimisée pour des fichiers de grande taille.

!!! note "Note"
    La taille doit toujours être un multiple entier de 1Mo.

De manière générale, il faut réduire au maximum les ouvertures et fermetures de fichiers. Il sera donc préférable de regrouper toutes les données dans un seul fichier plutôt que d'écrire une pléthore de petits fichiers. Il sera aussi nettement préférable d'ouvrir le fichier une seule fois au début de l'exécution et de le fermer à la fin, plutôt que de l'ouvrir et de le refermer au cours de la même exécution chaque fois que l'on veut y ajouter de nouvelles données.

## Pour plus d'information

*   [Archivage et compression de fichiers](archiving-and-compressing-files.md)