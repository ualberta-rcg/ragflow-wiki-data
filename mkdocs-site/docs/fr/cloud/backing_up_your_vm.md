---
title: "Backing up your VM/fr"
slug: "backing_up_your_vm"
lang: "fr"

source_wiki_title: "Backing up your VM/fr"
source_hash: "e6bbe234b6be93baf545bee34cb239ee"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:46:19.657783+00:00"

tags:
  - cloud

keywords:
  - "Cloud"
  - "instantané du volume"
  - "Copie de sauvegarde"
  - "base de données"
  - "instantané"
  - "Instantané de volume"
  - "création d'image"
  - "instance"
  - "Instance virtuelle"
  - "Configuration automatique"
  - "Image"
  - "OpenStack"
  - "volume"
  - "application d’approvisionnement"
  - "restauration"
  - "Synchroniser les données"
  - "quota de stockage"
  - "suppression de l'instance"
  - "sauvegarde"
  - "Clients ligne de commande"
  - "jeux de données"

questions:
  - "Quelles sont les méthodes et les outils recommandés pour sauvegarder les fichiers d'une instance à l'extérieur du nuage ?"
  - "Comment peut-on utiliser les outils d'approvisionnement et d'orchestration pour automatiser la recréation et la configuration d'une instance ?"
  - "Quelle est la procédure spécifique dans OpenStack pour créer une copie de sauvegarde d'une instance persistante à partir de ses volumes ?"
  - "Quelle est la procédure pour créer une image à partir d'un volume et pourquoi le format QCOW2 est-il particulièrement recommandé ?"
  - "Comment le processus de création d'instantanés et d'images diffère-t-il entre les instances persistantes et les instances de calcul ?"
  - "Quelle stratégie de sauvegarde est conseillée pour gérer efficacement les systèmes d'exploitation, les logiciels et les grands jeux de données ?"
  - "Quel est le risque lié à l'option de suppression du volume lors de la création d'une instance sous OpenStack ?"
  - "Quelle méthode permet d'empêcher la suppression d'un volume lors de la destruction de son instance associée ?"
  - "Quelle précaution concernant les quotas de stockage faut-il prendre avant de créer un instantané pour protéger son volume ?"
  - "Comment les jeux de données peuvent-ils être transférés vers un emplacement distant ?"
  - "Quelle étape supplémentaire est nécessaire lors de la sauvegarde de logiciels de base de données comme MySQL ou PostgreSQL ?"
  - "Pourquoi est-il indispensable de tester les copies de sauvegarde effectuées ?"
  - "Quels sont les clients en ligne de commande OpenStack disponibles pour gérer l'environnement cloud ?"
  - "Quelles sont les différentes méthodes pour gérer les images, telles que la création depuis une instance, le téléchargement ou le téléversement ?"
  - "Comment peut-on transférer et synchroniser des données au sein de cette infrastructure cloud ?"
  - "Quels sont les clients en ligne de commande OpenStack disponibles pour gérer l'environnement cloud ?"
  - "Quelles sont les différentes méthodes pour gérer les images, telles que la création depuis une instance, le téléchargement ou le téléversement ?"
  - "Comment peut-on transférer et synchroniser des données au sein de cette infrastructure cloud ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Fait partie de [Service infonuagique de Calcul Canada](cloud.md)*

Il existe plusieurs stratégies pour faire une copie de sauvegarde d'une instance et pour rétablir la situation en cas de problème; le choix de la stratégie à adopter dépend de vos exigences et de votre cas particulier.

!!! tip "Conseil important"
    Il est fortement recommandé de créer des copies de sauvegarde à l’extérieur du nuage. Une des règles fréquemment appliquées en matière de sauvegarde est celle du 3-2-1 qui veut que trois copies de vos données soient enregistrées sur au moins deux types de médias et qu’une de ces copies se trouve hors du site.

Nous discutons ici de quelques méthodes usuelles pour sauvegarder votre instance et en préserver l’état et nous présentons l’exemple d’une combinaison de certaines ces méthodes qui représente une stratégie de sauvegarde complète.

## Sauvegarde de fichiers

Plusieurs stratégies employées avec les ordinateurs physiques s’appliquent aussi aux instances virtuelles; par exemple, [rsync](https://rsync.samba.org/), [Duplicity](https://nongnu.org/duplicity/), [Borg](https://borgbackup.readthedocs.io/) et [Restic](https://restic.readthedocs.io/) sont des outils qui peuvent sauvegarder à distance les données de votre instance.

## Configuration automatique

Des outils d’approvisionnement comme [Ansible](https://www.ansible.com/), [Puppet](https://puppet.com/), [Chef](https://www.chef.io/) et [SaltStack](https://saltstack.com/) peuvent être utilisés pour automatiser la configuration des logiciels et du système d’exploitation. Avec les fichiers de spécification appropriés pour chacun de ces outils, il est très facile de recréer une instance. Les fichiers de spécification peuvent être gérés par une application de gestion de versions comme [Git](https://git-scm.com/). Les outils d’approvisionnement et d’orchestration (par exemple Heat et Terraform) peuvent être utilisés ensemble pour automatiser le processus complet de la création d’une instance et de la configuration des logiciels; voyez [Automatisation de la création d'instances](automating_vm_creation.md); les données qui ne seraient pas alors générées ou créées devront être sauvegardées en utilisant une méthode mentionnée à la section [Sauvegarde de fichiers](#sauvegarde-de-fichiers).

## Méthodes de sauvegarde OpenStack

OpenStack offre deux options pour le stockage :

*   stockage dans un volume, avec triple réplication; cette option protège les données en cas de problème de matériel, mais non en cas de suppression involontaire ou malicieuse;
*   stockage éphémère sur un nœud local; cette option protège aussi en cas de problème de matériel, mais ne devrait pas être utilisée avec des données critiques; on l’utilise surtout de façon temporaire.

OpenStack offre aussi des outils pour créer des images de disques et des instantanés d’instances. Les gabarits d’instance principaux p (*persistent*) et c (*compute*) ont des comportements différents; nous recommandons des procédures différentes de sauvegarde pour chaque gabarit.

### Instances persistantes

Les instances persistantes sont conçues pour être [démarrées depuis un volume](working_with_volumes.md). Une copie de sauvegarde est créée lorsqu’une copie du ou des volumes associés à l’instance est créée. Cependant, ceci ne comprend pas le gabarit de l’instance, son IP publique et ses règles de sécurité. La meilleure manière de créer une copie de sauvegarde d’un volume est donc de créer une image de ce volume. Cette image peut alors être [téléchargée](working_with_images.md) et réutilisée pour créer plusieurs nouvelles instances; vous pouvez y [accéder par VirtualBox](working_with_images.md) à partir de votre ordinateur personnel; ou la [téléverser](working_with_images.md) vers un autre nuage.

Pour créer une image depuis un volume, ce volume doit être détaché de l’instance. De plus, si le volume est le volume racine (*root*) de l’instance, il ne peut pas être détaché sans que l’instance ne soit supprimée. Vous pouvez supprimer votre instance sans perdre de données pourvu que vous n’ayez pas coché « Supprimer le volume lors de la suppression de l'instance » lors de la création de l’instance.

!!! warning "Attention"
    Sachez qu’OpenStack ne vous signalera pas que cette case a été cochée.

Une façon de contourner ceci est de créer un instantané du volume.

!!! warning "Note sur le quota"
    Assurez-vous toutefois que votre quota de stockage le permet puisque les instantanés sont comptabilisés.

Comme un volume ne peut pas être supprimé si un instantané de ce volume a été créé, le volume ne sera pas supprimé si vous supprimez l’instance, peu importe si vous avez ou non coché la case en question.

L’état de tous les volumes dont vous voulez créer une image devrait alors être « Disponible(s) ». Pour créer une image depuis un volume, sélectionnez « Charger vers l'image » dans le menu déroulant pour le volume. Sélectionnez le format QCOW2 et entrez un nom pour l’image. Il existe plusieurs formats pour les images de disques, mais QCOW2 fonctionne bien avec OpenStack et prend typiquement moins d’espace que les images de format brut. Les autres formats `vmdk` et `vdi` sont utiles quand vous travaillez avec d’autres outils de virtualisation comme VirtualBox.

Une fois que vous avez créé les images de tous les volumes que vous voulez sauvegarder, vous pouvez alors créer à nouveau l’instance à partir du volume racine original de l’instance et s’il y a lieu, y attacher les volumes supplémentaires que vous auriez rattachés à l’instance originale.

#### Instantané d'un volume

Vous pouvez aussi créer un instantané du volume pour conserver son état actuel; ceci n’est toutefois pas une solution de sauvegarde idéale puisque le volume original ne devrait pas être modifié. De plus, il n’est pas possible de télécharger un instantané puisqu’il dépend du volume original. Il est cependant possible de créer un nouveau volume à partir d’un de ses instantanés si par exemple certains fichiers ont été modifiés depuis que l’instantané a été créé et que les modifications n’ont pas besoin d’être sauvegardées, ou que des modifications de l’instance originale ne doivent pas être propagées à d’autres instances.

#### Instantané d'une instance

Le comportement d’un instantané d’instance dépend du gabarit de cette dernière. Dans le cas d’une instance persistante, OpenStack crée une image quasi vide qui contient des pointeurs aux instantanés du volume. Ces pointeurs sont dirigés vers les instantanés du volume de démarrage de l’instance persistante et des autres volumes qui ont été créés à la création de l’instantané de l’instance. Vous pouvez alors créer une nouvelle instance (« Démarrer depuis une image (crée un volume) »), ce qui crée de nouveaux volumes à partir des instantanés créés au préalable, démarre une nouvelle instance à partir du volume racine et attache tout autre volume dupliqué.

### Instances de calcul

Comme pour la création d’une instance persistante, l’objectif principal est de créer une image du disque racine tout au moins, mais aussi au besoin des volumes qui y sont rattachés. Toutefois, le processus pour créer une image est différent dans le cas des gabarits de type c (*compute*). Contrairement aux instances persistantes, ceux-ci ne sont pas conçus pour démarrer depuis un volume auquel l’accès s’est fait par réseau, mais plutôt depuis des images d’un disque qui résident sur l’ordinateur où l’instance est exécutée. Ceci signifie qu’il n’y a aucun volume dans le tableau de bord OpenStack sur lequel vous pouvez cliquer pour créer l’image de votre disque racine. Pour ce faire, vous devez cliquer sur « Créer un instantané » dans l'onglet « Aperçu » de l'instance. Comme cela se produit à la création d’une image avec une instance persistante, ceci crée une image; dans ce cas par contre, l’image n’est pas aussi vide (c’est-à-dire qu’elle ne contient pas que des pointeurs aux instantanés du volume), mais contient une copie du disque racine de l’instance.

Les instances de calcul possèdent un disque de données supplémentaire monté sur `/mnt` dont les données ne font pas partie de l’image de l’instance. Il faut donc procéder autrement pour sauvegarder ces données, par exemple les copier du disque avant que l’instance ne soit terminée.

## Exemple d’une stratégie de sauvegarde

Il peut être difficile de gérer des images de plus de 10-20Go qui exigent beaucoup de temps à télécharger et à créer des instances. Une bonne stratégie est d’isoler les grands jeux de données du système d’exploitation et des logiciels. Une copie de sauvegarde du système d’exploitation et des logiciels peut se faire avec une image du disque ou ils peuvent être recréés avec une application d’approvisionnement (voir [Configuration automatique](#configuration-automatique)). Les jeux de données peuvent ensuite être copiés vers un endroit distant avec une méthode usuelle de [sauvegarde](#sauvegarde-de-fichiers). Si vous utilisez un logiciel de base de données comme MySQL ou PostgreSQL, vous voudrez vider vos bases de données en y incluant la sauvegarde. Enfin et surtout, effectuez des tests pour savoir si vos copies de sauvegarde ont bien restauré ce qui était requis.

## Voir aussi

*   [Clients ligne de commande](openstack_command_line_clients.md)
*   [Créer une image depuis une instance](working_with_images.md)
*   [Télécharger une image](working_with_images.md)
*   [Téléverser une image](working_with_images.md)
*   [Synchroniser les données](../getting-started/transferring_data.md)