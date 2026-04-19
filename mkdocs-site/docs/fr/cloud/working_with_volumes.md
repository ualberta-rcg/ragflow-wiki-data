---
title: "Working with volumes/fr"
slug: "working_with_volumes"
lang: "fr"

source_wiki_title: "Working with volumes/fr"
source_hash: "92fbf7683cb70aab58a676b558ddc750"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:15:46.110404+00:00"

tags:
  - cloud

keywords:
  - "volume"
  - "Charger dans l'image"
  - "répertoire"
  - "OpenStack"
  - "Format du disque"
  - "commande mount"
  - "démarrage depuis un volume"
  - "détacher un volume"
  - "instance"
  - "redémarrage de l'instance"
  - "QCOW2"
  - "cloner un volume"
  - "monter un volume"
  - "créer une image"
  - "point de montage"
  - "attacher un volume"
  - "image"
  - "client ligne de commande"
  - "stockage"

questions:
  - "Quelles sont les différences technologiques et de performance entre les types de volumes de stockage proposés, tels que rbd1 et high_performance ?"
  - "Quelles sont les étapes et les paramètres requis pour créer un nouveau volume à partir du tableau de bord ?"
  - "Quelle est la procédure complète (attacher, formater, monter) pour utiliser un volume sur une instance et quelle précaution cruciale faut-il prendre avant de le formater ?"
  - "Comment configurer le montage automatique d'un volume au démarrage d'une instance à l'aide du fichier /etc/fstab ?"
  - "Pourquoi est-il recommandé de démarrer une instance depuis un volume et quelles sont les différentes méthodes pour y parvenir ?"
  - "Quelles sont les étapes et les conditions requises pour créer une image à partir d'un volume en utilisant le tableau de bord ?"
  - "Quelle commande doit être utilisée pour monter le volume sur l'instance ?"
  - "Où les fichiers et le répertoire du volume seront-ils disponibles une fois le montage effectué ?"
  - "Quelle action est nécessaire concernant ce volume après le redémarrage de l'instance ?"
  - "Quelles sont les étapes à suivre dans l'interface pour configurer et charger une nouvelle image ?"
  - "Pourquoi le format de disque QCOW2 est-il spécifiquement recommandé pour le nuage OpenStack ?"
  - "Quels formats de disque doit-on privilégier si l'on souhaite utiliser l'image avec Virtualbox ?"
  - "Comment créer une image à partir d'un volume en utilisant le client en ligne de commande OpenStack ?"
  - "Pourquoi le clonage est-il la méthode recommandée pour copier un volume et quelle précaution majeure faut-il prendre avant de l'exécuter ?"
  - "Quelles précautions faut-il prendre avant de détacher un volume et comment la procédure diffère-t-elle s'il s'agit d'un volume de démarrage ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un volume est un espace de stockage qui n'est pas détruit à l'arrêt d'une machine virtuelle. Sur nos nuages, les volumes utilisent le stockage [Ceph](https://fr.wikipedia.org/wiki/Ceph) avec triple réplication, ou encore des [codes d'effacement](https://fr.wikipedia.org/wiki/Code_d%27effacement) pour garantir l’intégrité des données en cas de panne matérielle. Sur [Arbutus](cloud_resources.md), les volumes de type *rbd1* sont stockés sur des disques durs mécaniques et utilisent des codes d'effacement pour assurer l'intégrité des données, réduisant ainsi les coûts de stockage supplémentaires encourus par la triple réplication. Les volumes de type *high_performance* sont stockés sur des disques NVMe SSD et utilisent la triple réplication, moins efficace en termes de stockage, mais offrant de meilleures performances. Voir [l’information sur les volumes OpenStack](https://docs.openstack.org/cinder/latest/cli/cli-manage-volumes.html).

## Créer un volume

Cliquez sur le bouton *+ Créer un volume* et remplissez les champs comme suit :

*   *Nom du volume* : par exemple, `data`
*   *Description* : (optionnel)
*   *Source du volume* : `Aucune source, volume vide`
*   *Type* : `Pas de type de volume`
*   *Taille (Gio)* : `40` ou toute autre valeur appropriée pour vos données ou votre système d'exploitation
*   *Zone de disponibilité* : `nova` est la seule option disponible

Cliquez sur le bouton *Créer un volume*.

## Monter un volume sur une instance
### Attacher un volume

*   **Attacher** un volume signifie l'associer à une instance. Ceci est comme insérer une clé USB ou ajouter un disque externe à votre ordinateur.
*   Vous pouvez attacher un volume à partir de la page *Volume* du tableau de bord.
*   Dans la colonne *Actions*, sélectionnez *Gérer les attachements* du menu déroulant.
*   Dans le champ *Attacher à l'instance*, sélectionnez l'instance appropriée.
*   Cliquez sur le bouton *Attacher le volume*.
Après quelques secondes, la page des volumes est rafraîchie et montre le nouveau volume lié à l'instance sélectionnée avec `/dev/vdb` ou autre endroit semblable.

### Formater un nouveau volume

!!! warning "Attention lors du formatage"
    *   **NE FORMATEZ PAS** si vous attachez un nouveau volume qui a déjà été utilisé pour stocker des données.
    *   **Le formatage efface toute l'information qui se trouve dans le volume**, ce qui peut avoir d'importantes répercussions; la prudence est de mise.

*   Formater un volume signifie le préparer pour y enregistrer des fichiers et des répertoires.
*   Avant de pouvoir utiliser un nouveau volume, il faut le formater.
*   Voyez les directives sur [Linux](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md) ou Windows.

### Monter un volume
*   **Monter** un volume signifie créer une association logique entre le système de fichiers du volume d'une part et les répertoires et la structure des fichiers de l'instance d'autre part.
*   Montez le volume avec une commande semblable à :

    ```bash
    sudo mount /dev/vdb1 /mnt
    ```
    selon le nom du dispositif, l'organisation du disque et le point de montage.

Le répertoire et la structure de fichiers du volume seront ainsi disponibles dans le répertoire `/mnt` de l'instance. Cependant, au redémarrage de l'instance, le volume devra être monté de nouveau avec la même commande `mount`.

Il est possible de monter automatiquement des volumes au démarrage d'une instance en ajoutant au fichier `/etc/fstab` une ligne qui contient les détails sur comment les monter.

Pour voir l'information, lancez la commande :

```bash
blkid
```

Selon l'UUID, ajoutez à `/etc/fstab` la ligne :

```text
/dev/disk/by-uuid/anananan-anan-anana-anan-ananananana /mnt auto defaults,nofail 0 3
```

Remplacez *anananan-anan-anana-anan-ananananana* par l'UUID du dispositif que vous voulez monter automatiquement.

Pour plus d'information, voyez [cette page de la documentation Ubuntu](https://help.ubuntu.com/community/Fstab).

## Démarrer depuis un volume
Pour créer un service persistant, il est recommandé de démarrer l'instance depuis un volume. Une instance démarrée depuis une image plutôt que d'un volume est stockée sur le disque local de la machine qui opère cette même instance. L'instance pourrait être perdue si un problème survient sur la machine ou sur son disque. Le stockage du volume procure une redondance qui protège l'instance de défaillance du matériel. De façon générale, les gabarits pour démarrer depuis un volume commencent par la lettre p (voir la page [Gabarits d'instances](virtual_machine_flavors.md)).

Démarrer une instance depuis un volume peut se faire :
*   à partir d'une image en créant un nouveau volume;
*   à partir d'un volume existant;
*   à partir d'un instantané (*snapshot*), en créant un nouveau volume.

Si vous faites ceci pour la première fois, utilisez la première option; les deux autres options ne sont possibles que si vous avez déjà créé un volume ou un instantané de volume.

Un volume peut être créé au lancement d'une instance. Sélectionnez *Démarrer depuis une image (crée un volume)*. Remplissez ensuite les champs *Nom de l'image* et *Taille du périphérique*. Pour que le volume persiste après l'utilisation de l'instance, ne cochez pas la case *Supprimer le volume lors de la suppression de l'instance*, au bas de la fenêtre. Il est préférable de ne jamais cocher cette case puisque le volume peut être supprimé manuellement plus tard.

## Créer une image depuis un volume

Créer une image depuis un volume permet de télécharger l'image pour servir de copie de sécurité ou pour créer une instance sur un autre nuage, par exemple avec [VirtualBox](https://www.virtualbox.org/). Pour copier un volume vers un autre volume dans le même nuage, procédez plutôt par [clonage](#cloner-un-volume).

Pour créer l'image d'un volume, elle doit d'abord être détachée de l'instance. Dans le cas d'un *volume de démarrage*, l'image ne peut être détachée que si l'instance est supprimée. Assurez-vous que la case *Supprimer le volume lors de la suppression de l'instance* n'a pas été cochée à la création de l'instance.

Les grandes images (plus de 10-20 Go) peuvent prendre beaucoup de temps à créer, téléverser ou autres opérations. Une solution serait de [séparer les données](backing_up_your_vm.md) si possible.

### Utiliser le tableau de bord
1.  Sous *Projet* > *Volumes*, sélectionnez le volume.
2.  Dans la colonne *Actions*, sélectionnez *Charger dans l'image* du menu déroulant.
3.  Entrez un nom pour la nouvelle image.
4.  Sélectionnez le *Format du disque*. QCOW2 est recommandé pour le nuage OpenStack parce que ce format est relativement plus compact que *Raw* et plus efficace avec OpenStack. Si vous voulez utiliser l'image avec VirtualBox, sélectionnez de préférence *vmdk* ou *vdi*.
5.  Cliquez sur le bouton *Charger*.

### Utiliser le client ligne de commande
Un [client ligne de commande](openstack_command_line_clients.md) peut faire ceci :
```bash
openstack image create --disk-format <format> --volume <volume_name> <image_name>
```
où :
*   `<format>` est le format du disque; les deux options sont [qcow2](https://fr.wikipedia.org/wiki/Qcow) et [vmdk](https://fr.wikipedia.org/wiki/VMDK),
*   `<volume_name>` peut se trouver en cliquant sur le nom du volume à partir du tableau de bord OpenStack,
*   `<image_name>` est le nom que vous donnez à l'image.

Vous pouvez ensuite [télécharger l'image](working_with_images.md).

## Cloner un volume
Le clonage est le moyen recommandé pour la copie de volumes. Il est toujours possible de créer un nouveau volume depuis l'image d'un volume existant, mais le clonage est plus rapide et demande moins d'échange de données. C'est un moyen très utile si vous avez une instance persistante et que vous voulez faire des tests avant de passer en production. Nous recommandons fortement de terminer l’instance avant de cloner un volume pour éviter que l’état du volume cloné soit incohérent par rapport au volume source dans le cas où ce dernier aurait été modifié pendant la création du clone. Pour cloner un volume, utilisez [un client ligne de commande](openstack_command_line_clients.md) et entrez :

```bash
openstack volume create --source <source-volume-id> --size <size-of-new-volume> <name-of-new-volume>
```

## Détacher un volume
Avant de détacher un volume, il est important de vérifier si des fichiers de ce volume sont utilisés par le système d'exploitation ou des applications actives dans votre instance; si c'est le cas, le volume détaché pourrait être corrompu ou les applications pourraient avoir des comportements inattendus. Il est donc recommandé de fermer l'instance ou de [démonter le volume](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md).

Pour détacher un volume, connectez-vous à OpenStack (voir la [liste des liens à nos ressources infonuagiques](cloud.md#ressources-infonuagiques)) et sélectionnez le projet qui contient le volume à détacher. Sélectionnez *Volumes* > *Volumes* pour faire afficher les volumes. La colonne *Attaché à* indique ce à quoi chaque volume est attaché.

*   Si la colonne indique `/dev/vda`, il s'agit d'un volume de démarrage; vous devez détacher l'instance avant de détacher le volume, autrement le message d'erreur *Impossible de déconnecter le volume* sera affiché.

*   Si la colonne indique `/dev/vdb`, `/dev/vdc`, etc., il n'est pas nécessaire de détacher l'instance. Dans la liste déroulante sous *Actions*, sélectionnez *Gérer les attachements*, cliquez sur le bouton *Détacher le volume* puis sur l'autre bouton *Détacher le volume* pour confirmer.