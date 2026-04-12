---
title: "Working with volumes/fr"
slug: "working_with_volumes"
lang: "fr"

source_wiki_title: "Working with volumes/fr"
source_hash: "277e4c7eebbfe8f40bb11019dc80b1e7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:42:05.604798+00:00"

tags:
  - cloud

keywords:
  - "Attacher un volume"
  - "openstack image create"
  - "cloner un volume"
  - "instance"
  - "Image"
  - "/etc/fstab"
  - "image"
  - "OpenStack"
  - "volume"
  - "Virtualbox"
  - "Volume"
  - "format"
  - "Démarrer depuis un volume"
  - "détacher un volume"
  - "Monter un volume"
  - "Formater un volume"
  - "commande mount"
  - "redémarrage"
  - "client ligne de commande"
  - "Instance"

questions:
  - "Qu'est-ce qu'un volume dans cet environnement infonuagique et comment le stockage de ses données est-il protégé contre les défaillances matérielles ?"
  - "Quelles sont les étapes requises dans le tableau de bord pour créer un nouveau volume et l'attacher à une instance ?"
  - "Pourquoi faut-il être prudent lors du formatage d'un volume et comment procède-t-on pour le monter de façon permanente dans le système d'exploitation ?"
  - "Comment configurer le montage automatique d'un périphérique de stockage à l'aide de son UUID dans le fichier fstab ?"
  - "Pourquoi est-il fortement recommandé de démarrer une instance depuis un volume plutôt que depuis une image ?"
  - "Quelles sont les étapes et les conditions préalables pour créer une image à partir d'un volume via le tableau de bord ou la ligne de commande ?"
  - "Dans quel répertoire de l'instance la structure de fichiers du volume est-elle rendue disponible ?"
  - "Quelle commande est nécessaire pour monter manuellement le volume après un redémarrage ?"
  - "Quel fichier doit être modifié pour automatiser le montage du volume au démarrage de l'instance ?"
  - "Pourquoi certains formats d'image sont-ils privilégiés pour OpenStack ou Virtualbox par rapport au format Raw ?"
  - "Sur quel bouton l'utilisateur doit-il cliquer dans l'interface pour charger l'image ?"
  - "Quelle est la commande à exécuter dans le client en ligne de commande pour créer une image ?"
  - "Pourquoi le clonage est-il la méthode recommandée pour copier un volume et quelle précaution majeure faut-il prendre avant de l'exécuter ?"
  - "Quelles sont les vérifications préalables nécessaires pour détacher un volume en toute sécurité afin d'éviter la corruption des données ou des comportements inattendus ?"
  - "Comment identifier si un volume est un volume de démarrage à partir de son point d'attachement, et comment cela affecte-t-il la procédure de détachement dans OpenStack ?"
  - "Pourquoi le clonage est-il la méthode recommandée pour copier un volume et quelle précaution majeure faut-il prendre avant de l'exécuter ?"
  - "Quelles sont les vérifications préalables nécessaires pour détacher un volume en toute sécurité afin d'éviter la corruption des données ou des comportements inattendus ?"
  - "Comment identifier si un volume est un volume de démarrage à partir de son point d'attachement, et comment cela affecte-t-il la procédure de détachement dans OpenStack ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un volume fournit un espace de stockage qui n'est pas détruit lorsqu'on termine l'instance à laquelle il est attaché. Dans nos environnements infonuagiques, le stockage est assuré par [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)), soit avec triple réplication, soit avec [des codes d'effacement](https://en.wikipedia.org/wiki/Erasure_code) comme protection contre les défaillances matérielles. Dans [Arbutus](cloud-resources.md), le type de volume *Default* utilise des codes d'effacement et réduit les coûts de stockage additionnels de la triple réplication; le type de volume *OS or Database* utilise la triple réplication. Consultez [la documentation OpenStack sur les volumes](https://docs.openstack.org/cinder/latest/cli/cli-manage-volumes.html).

## Créer un volume

Cliquez sur le bouton **+ Créer un volume** et remplissez les champs comme suit :

*   **Nom du volume** : par exemple, `data`
*   **Description** : (optionnel)
*   **Source du volume** : `Aucune source, volume vide`
*   **Type** : `Pas de type de volume`
*   **Taille (Gio)** : `40` ou toute autre valeur appropriée pour vos données ou votre système d'exploitation
*   **Zone de disponibilité** : `nova` est la seule option disponible

Cliquez sur le bouton **Créer un volume**.

## Monter un volume sur une instance

### Attacher un volume

*   **Attacher** un volume signifie l'associer à une instance. C'est comme insérer une clé USB ou ajouter un disque externe à votre ordinateur.
*   Vous pouvez attacher un volume à partir de la page **Volume** du tableau de bord.
*   Dans la colonne **Actions**, sélectionnez **Gérer les attachements** du menu déroulant.
*   Dans le champ **Attacher à l'instance**, sélectionnez l'instance appropriée.
*   Cliquez sur le bouton **Attacher le volume**.

Après quelques secondes, la page des volumes est rafraîchie et montre le nouveau volume lié à l'instance sélectionnée avec `/dev/vdb` ou autre endroit semblable.

### Formater un nouveau volume

!!! warning "Attention : Formatage d'un volume"
    **NE FORMATEZ PAS** si vous attachez un nouveau volume. Le volume a dû être formaté si vous l'avez déjà utilisé pour stocker des données.
    **Le formatage efface toute l'information qui se trouve dans le volume**, ce qui peut avoir d'importantes répercussions; la prudence est de mise.

*   Formater un volume signifie le préparer pour y enregistrer des fichiers et des répertoires.
*   Avant de pouvoir utiliser un nouveau volume, il faut le formater.
*   Voyez les directives sur [Linux](using-a-new-empty-volume-on-a-linux-vm.md) ou [Windows](using-a-new-empty-volume-on-a-windows-vm.md).

### Monter un volume

*   **Monter** un volume signifie créer une association logique entre le système de fichiers du volume d'une part et les répertoires et la structure des fichiers de l'instance d'autre part.
*   Montez le volume avec une commande semblable à :
    ```bash
    [name@server ~]$ sudo mount /dev/vdb1 /mnt
    ```
    selon le nom du dispositif, l'organisation du disque et le point de montage.
    Le répertoire et la structure de fichiers du volume seront ainsi disponibles dans le répertoire `/mnt` de l'instance. Cependant, au redémarrage de l'instance, le volume devra être monté de nouveau avec la même commande `mount`.

Il est possible de monter automatiquement des volumes au démarrage d'une instance en ajoutant au fichier `/etc/fstab` une ligne qui contient les détails sur comment les monter.

Pour voir l'information, lancez la commande :
```bash
blkid
```

Selon le UUID, ajoutez à `/etc/fstab` la ligne :

```bash
/dev/disk/by-uuid/anananan-anan-anana-anan-ananananana /mnt auto defaults,nofail 0 3
```

Remplacez *anananan-anan-anana-anan-ananananana* par l'UUID du dispositif que vous voulez monter automatiquement.

Pour plus d'information, voyez [cette page de la documentation Ubuntu](https://help.ubuntu.com/community/Fstab).

## Démarrer depuis un volume

Pour créer un service persistant, il est recommandé de démarrer l'instance depuis un volume. Une instance démarrée depuis une image plutôt que d'un volume est stockée sur le disque local de la machine qui opère cette même instance. L'instance pourrait être perdue si un problème survient sur la machine ou sur son disque. Le stockage du volume procure une redondance qui protège l'instance des défaillances matérielles. De façon générale, les gabarits pour démarrer depuis un volume commencent par la lettre p (voir la page [Gabarits d'instances](virtual-machine-flavors.md)).

Démarrer une instance depuis un volume peut se faire :
*   à partir d'une image en créant un nouveau volume;
*   à partir d'un volume existant;
*   à partir d'un instantané (*snapshot*), en créant un nouveau volume.

Si vous faites ceci pour la première fois, utilisez la première option; les deux autres options ne sont possibles que si vous avez déjà créé un volume ou un instantané de volume.

Un volume peut être créé au lancement d'une instance. Sélectionnez **Démarrer depuis une image (crée un volume)**. Remplissez ensuite les champs **Nom de l'image** et **Taille du périphérique**.

!!! tip "Conseil pour la persistance du volume"
    Il est préférable de ne jamais cocher la case **Supprimer le volume lors de la suppression de l'instance** puisque le volume peut être supprimé manuellement plus tard.

## Créer une image depuis un volume

Créer une image depuis un volume permet de télécharger l'image pour servir de copie de sécurité ou pour créer une instance sur un autre nuage, par exemple avec [VirtualBox](https://www.virtualbox.org/). Pour copier un volume vers un autre volume dans le même nuage, procédez plutôt par [clonage](#cloner-un-volume).

Pour créer l'image d'un volume, elle doit d'abord être détachée de l'instance. Dans le cas d'un volume de démarrage (*boot volume*), l'image ne peut être détachée que si l'instance est supprimée. Assurez-vous que la case **Supprimer le volume lors de la suppression de l'instance** n'a pas été cochée à la création de l'instance.

!!! note "Gestion des grandes images"
    Les grandes images (plus de 10-20 Gio) peuvent prendre beaucoup de temps à créer, téléverser ou d'autres opérations. Une solution serait de [séparer les données](backing-up-your-vm.md#exemple-dune-strategie-de-sauvegarde) si possible.

### Utiliser le tableau de bord

1.  Sous **Projet** > **Volumes**, sélectionnez le volume.
2.  Dans la colonne **Actions**, sélectionnez **Charger dans l'image** du menu déroulant.
3.  Entrez un nom pour la nouvelle image.
4.  Sélectionnez le **Format du disque**. QCOW2 est recommandé pour le nuage OpenStack parce que ce format est relativement plus compact que *Raw* et plus efficace avec OpenStack. Si vous voulez utiliser l'image avec Virtualbox, sélectionnez de préférence *vmdk* ou *vdi*.
5.  Cliquez sur le bouton **Charger**.

### Utiliser le client en ligne de commande

Un [client en ligne de commande](openstack-command-line-clients.md) peut faire ceci :
```bash
openstack image create --disk-format <format> --volume <volume_name> <image_name>
```
où :
*   `<format>` est le format du disque; les deux options sont [qcow2](https://en.wikipedia.org/wiki/Qcow) et [vmdk](https://en.wikipedia.org/wiki/VMDK).
*   `<volume_name>` peut se trouver en cliquant sur le nom du volume à partir du tableau de bord OpenStack.
*   `<image_name>` est le nom que vous donnez à l'image.

Vous pouvez ensuite [télécharger l'image](working-with-images.md#telecharger-une-image).

## Cloner un volume

Le clonage est le moyen recommandé pour la copie de volumes. Il est toujours possible de créer un nouveau volume depuis l'image d'un volume existant, mais le clonage est plus rapide et demande moins d'échange de données. C'est un moyen très utile si vous avez une instance persistante et que vous voulez faire des tests avant de passer en production.

!!! warning "Recommandation pour le clonage"
    Nous recommandons fortement de terminer l'instance avant de cloner un volume pour éviter que l'état du volume cloné soit incohérent par rapport au volume source dans le cas où ce dernier aurait été modifié pendant la création du clone.

Pour cloner un volume, utilisez [un client en ligne de commande](openstack-command-line-clients.md) et entrez :
```bash
openstack volume create --source <source-volume-id> --size <size-of-new-volume> <name-of-new-volume>
```

## Détacher un volume

!!! warning "Précautions avant de détacher un volume"
    Avant de détacher un volume, il est important de vérifier si des fichiers de ce volume sont utilisés par le système d'exploitation ou des applications actives dans votre instance. Si c'est le cas, le volume détaché pourrait être corrompu ou les applications pourraient avoir des comportements inattendus. Il est donc recommandé de fermer l'instance ou de [démonter le volume](using-a-new-empty-volume-on-a-linux-vm.md#demonter-un-volume-ou-autre-peripherique).

Pour détacher un volume, connectez-vous à OpenStack (voir la [liste des liens à nos ressources infonuagiques](cloud.md#ressources-infonuagiques)) et sélectionnez le projet qui contient le volume à détacher. Sélectionnez **Volumes** > **Volumes** pour faire afficher les volumes. La colonne **Attaché à** indique ce à quoi chaque volume est attaché.

*   !!! note "Volume de démarrage"
    Si la colonne indique `/dev/vda`, il s'agit d'un volume de démarrage; vous devez détacher l'instance avant de détacher le volume, autrement le message d'erreur *Impossible de déconnecter le volume* sera affiché.

*   Si la colonne indique `/dev/vdb`, `/dev/vdc`, etc., il n'est pas nécessaire de détacher l'instance. Dans la liste déroulante sous **Actions**, sélectionnez **Gérer les attachements**, cliquez sur le bouton **Détacher le volume** puis sur l'autre bouton **Détacher le volume** pour confirmer.