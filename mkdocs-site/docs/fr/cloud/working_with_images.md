---
title: "Working with images/fr"
slug: "working_with_images"
lang: "fr"

source_wiki_title: "Working with images/fr"
source_hash: "4aebe30c71a2e4e32beec5e1a18d06eb"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:40:22.110545+00:00"

tags:
  - cloud

keywords:
  - "Disque éphémère"
  - "deuxième projet"
  - "openstack image create"
  - "VirtualBox"
  - "télécharger une image"
  - "Téléverser une image"
  - "instance"
  - "client OpenStack"
  - "téléverser une image"
  - "fichier OpenStack RC"
  - "Image"
  - "qemu-img"
  - "état de propriété"
  - "OpenStack"
  - "Client ligne de commande"
  - "mettre à jour"
  - "liste des images"
  - "Volume"
  - "identifiant de l'image"
  - "image QCOW2"
  - "état de l'image"
  - "client ligne de commande"
  - "Instance"

questions:
  - "Qu'est-ce qu'une image dans le contexte de l'infonuagique et en quoi diffère-t-elle d'un disque éphémère ou d'un volume ?"
  - "Quelle est la procédure recommandée pour créer une image à partir d'une instance démarrant sur un disque éphémère ?"
  - "Quelles sont les deux étapes nécessaires pour partager une image avec un autre projet à l'aide des commandes OpenStack ?"
  - "Quelle commande doit-on utiliser pour vérifier l'état de propriété d'une image ?"
  - "Quelles sont les étapes et la commande nécessaires pour lister et télécharger une image OpenStack spécifique ?"
  - "Comment peut-on téléverser une nouvelle image locale vers OpenStack via la ligne de commande ?"
  - "Que représentent les variables <IMAGE_ID>, <MEMBER_ID> et <MEMBER_STATUS> dans la syntaxe expliquée ?"
  - "Quelles sont les différentes valeurs possibles pour définir le nouvel état d'une image ?"
  - "Que se passe-t-il concrètement une fois que le processus de mise à jour est complété ?"
  - "Quelles sont les étapes préalables requises avant de pouvoir téléverser une image sur OpenStack ?"
  - "Quelle commande exacte doit-on lancer pour créer une nouvelle image à partir d'un fichier local ?"
  - "À quoi correspondent les valeurs spécifiques telles que le format de disque et l'ID mentionnées dans les instructions ?"
  - "Quels sont les paramètres requis pour définir et téléverser une image sur le tableau de bord OpenStack ?"
  - "Qu'est-ce que VirtualBox et sur quels systèmes d'exploitation ce logiciel peut-il fonctionner ?"
  - "Quelle est la commande et l'outil nécessaires pour convertir une image QCOW2 au format compatible avec VirtualBox ?"
  - "Quels sont les paramètres requis pour définir et téléverser une image sur le tableau de bord OpenStack ?"
  - "Qu'est-ce que VirtualBox et sur quels systèmes d'exploitation ce logiciel peut-il fonctionner ?"
  - "Quelle est la commande et l'outil nécessaires pour convertir une image QCOW2 au format compatible avec VirtualBox ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

Une image est un fichier dont le contenu est le même que celui d'un disque virtuel. Une image contient souvent un système d'exploitation de base utilisé pour créer un volume ou un disque éphémère à partir duquel une instance est lancée. Un disque éphémère est un disque virtuel qui réside sur l'hôte (hyperviseur) où l'instance est exécutée. Contrairement aux fichiers d'un volume, les fichiers d'un disque éphémère sont supprimés lorsque l'instance est supprimée. La portabilité d'une image fait qu'elle peut être téléchargée d'un nuage; être utilisée pour créer une instance sur votre ordinateur avec VirtualBox ou un autre outil semblable ou; téléversée sur un autre nuage pour créer une nouvelle instance. Un volume et un disque éphémère n'offrent pas ces possibilités. Il existe plusieurs formats d'images dont raw, qcow2, vmdk et vdi.

Lorsque vous partagez vos images, assurez-vous d'y retirer l'information sensible comme les clés publiques et privées, les fichiers de configuration qui contiennent des mots de passe, etc. Lorsqu'une image créée d'une instance VirtualBox est téléchargée sur un de nos nuages, `cloud-init` doit avoir été installé et configuré correctement; voyez [la documentation d'OpenStack](https://docs.openstack.org/image-guide/create-images-manually.html).

Voyez la [liste des images](cloud_resources.md#images) fournies par l'équipe de soutien technique.

## Créer une image depuis une instance

La procédure est différente selon que l'instance démarre depuis un disque éphémère (généralement les gabarits de type c) ou un volume (généralement les gabarits de type p).

### Démarrer depuis un disque éphémère

Vous pouvez utiliser un [client ligne de commande OpenStack](openstack_command_line_clients.md) avec la commande
```bash
openstack server image create <server-name>
```
où `<server-name>` est remplacé par le nom de votre serveur. Ceci inclura uniquement le disque racine (par exemple /dev/vda) dans l'image. Puisque les disques éphémères et les volumes attachés non amorçables ne seront pas inclus dans l'image, des mesures supplémentaires doivent être prises pour préserver ces données. De plus, si l'instance écrit sur le disque pendant la création de l'image, le système de fichiers peut être sauvegardé dans un état incohérent. Nous vous recommandons d'éteindre l'instance (et non de la supprimer) avant de créer une image à partir de celle-ci.

### Démarrer depuis un volume

Voir [Créer une image depuis un volume](working_with_volumes.md#créer-une-image-depuis-un-volume).

## Partager une image avec un autre projet

C'est un processus en deux étapes :

1.  Un membre du projet auquel l'image appartient doit partager l'image avec l'autre projet.
2.  Un membre de l'autre projet doit accepter la nouvelle image qui est partagée.

Le membre du projet propriétaire utilise la commande [OpenStack](openstack_command_line_clients.md)
```console
[name@server]$  glance member-create <IMAGE_ID> <MEMBER_ID>
+------------+-------------+---------+
| Image ID   | Member ID   | Status  |
+------------+-------------+---------+
| <IMAGE_ID> | <MEMBER_ID> | pending |
+------------+-------------+---------+
```
où `<IMAGE_ID>` est l'identifiant de l'image à partager et `<MEMBER_ID>` est l'identifiant du projet avec lequel partager l'image.

Pour accepter l'image partagée, le membre du deuxième projet utilise la commande [OpenStack](openstack_command_line_clients.md#autres-interfaces) suivante
```console
[name@server]$  glance member-update <IMAGE_ID> <MEMBER_ID> <MEMBER_STATUS>
+------------+-------------+----------+
| Image ID   | Member ID   | Status   |
+------------+-------------+----------+
| <IMAGE_ID> | <MEMBER_ID> | accepted |
+------------+-------------+----------+
```
où `<IMAGE_ID>` est l'identifiant de l'image à mettre à jour, `<MEMBER_ID>` est l'identifiant du deuxième projet, et `<MEMBER_STATUS>` est le nouvel état de l'image. Les valeurs pour l'état sont `accepted`, `rejected` et `pending`. Une fois le processus complété, l'image paraît dans la liste des images du second projet.

Pour vérifier l'état de propriété de l'image, utilisez la commande
```console
[name@server]$ glance member-list --image-id <IMAGE_ID>
+------------+-------------+----------+
| Image ID   | Member ID   | Status   |
+------------+-------------+----------+
| <IMAGE_ID> | <MEMBER_ID> | accepted |
+------------+-------------+----------+
```

## Télécharger une image

Il faut d'abord installer le client OpenStack, puis télécharger le fichier RC OpenStack et le définir comme source (voir [OpenStack : Clients ligne de commande](openstack_command_line_clients.md)).
Le client OpenStack produit la liste des images disponibles de votre projet avec
```bash
openstack image list
```
Le résultat est un tableau semblable à ceci :

| ID                                     | Name                                  | Disk Format | Container Format | Size        | Status |
|:---------------------------------------|:--------------------------------------|:------------|:-----------------|:------------|:-------|
| 982761b2-c77b-4852-8ae3-bf98b32b8894   | Hadoop-2.2.4                          | qcow2       | bare             | 10253107200 | active |
| b7bd3033-9836-406d-a8f2-2e91978026b4   | hadoopmaster                          | qcow2       | bare             | 3493527552  | active |
| 2c751755-854d-49c3-af82-d501e51e7159   | hadoopmaster-active                   | qcow2       | bare             | 13134004224 | active |
| c41012f4-ed82-4478-a81f-5efb96a31b1a   | hadoopmaster-old                      | qcow2       | bare             | 3493527552  | active |
| 78e61a3f-b546-441a-b476-a7077b04ca36   | hadoopslave                           | qcow2       | bare             | 3490971648  | active |
| 516845c3-b256-4c6d-a2cb-e31e822c7e34   | hadoopslave1-active                   | qcow2       | bare             | 8345026560  | active |
| 1546bd86-5314-4fce-9576-e2f6930dad30   | hadoopslave1-old                      | qcow2       | bare             | 3490971648  | active |
| baf78e8d-8288-4854-a66b-812cdf3ccbca   | TestVM                                | qcow2       | bare             | 13167616    | active |
| 2faf97d7-5b0b-44ce-8024-3bef5a634570   | test_ubuntu_initial                   | qcow2       | bare             | 1799487488  | active |
| 308b6614-396a-4360-9c33-4e86f41ea0ec   | trusty                                | qcow2       | bare             | 256180736   | active |
| 9b3c3fda-2aca-43b5-a3e7-662a94f5e7fb   | Ubuntu_14.04_Trusty-amd64-20150708    | qcow2       | bare             | 257884672   | active |
| f93e66cf-fec1-4460-8fc7-506e716fbf30   | ucernvm-prod.1.18-10                  | raw         | bare             | 20971520    | active |

Dépendant de la version de votre client, il est possible que vous ayez besoin d'une option additionnelle comme `--long` pour voir toutes ces colonnes.

Pour télécharger une image en particulier, utilisez la commande
```bash
openstack image save --file ./<file-name-for-image>.<format> 2c751755-854d-49c3-af82-d501e51e7159
```
où `<format>` correspond à la valeur dans la colonne *Disk Format* et `<ID>` correspond à la valeur dans la colonne *ID*.

## Téléverser une image

Installez d'abord le client OpenStack, puis téléchargez et exécutez le fichier OpenStack RC (voir la section « Connecter le client ligne de commande à OpenStack » dans [Client ligne de commande](openstack_command_line_clients.md#connecter-le-client-ligne-de-commande-à-openstack)).
Lancez la commande
```bash
openstack image create --file <path-to-local-file-image> --disk-format <format> <new-image-name>
```
où
*   `<path-to-local-file-image>` est le chemin vers le fichier qui contient l'image à téléverser;
*   `<format>` est le format du disque; si aucun format n'est spécifié, le format *raw* s'applique; un format différent créera des problèmes et vous devez choisir un format qui correspond à celui de votre image;
*   `<new-image-name>` est le nom de l'image sur le tableau de bord OpenStack.

## Créer une instance VirtualBox depuis une image dans un nuage

[VirtualBox](https://www.virtualbox.org/) est un logiciel qui permet de créer des instances et de les exécuter sur votre ordinateur personnel. Il fonctionne sous divers systèmes d'exploitation (Windows, Linux, Mac) et les instances créées peuvent utiliser des systèmes d'exploitation différents.

Pour utiliser une image QCOW2 téléchargée d'un nuage OpenStack (comme ci-dessus), elle doit être convertie au format vmdk; pour ce faire, vous pouvez utiliser l'outil `qemu-img`. Il peut être installé par exemple avec
```bash
sudo apt-get install qemu-utils
```
(le paquet s'appelait auparavant `qemu-img`) puis la conversion peut se faire avec
```bash
qemu-img convert -f qcow2 vdisk.qcow2 -O vmdk vdisk.vmdk
```
Vous pouvez ensuite créer une nouvelle instance et lui attacher l'image vmdk. Pour plus de détails, voyez [how to run a vmdk file in VirtualBox](http://techathlon.com/how-to-run-a-vmdk-file-in-oracle-virtualbox/).