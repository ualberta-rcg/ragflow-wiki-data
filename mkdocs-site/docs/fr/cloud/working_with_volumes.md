---
title: "Working with volumes/fr"
slug: "working_with_volumes"
lang: "fr"

source_wiki_title: "Working with volumes/fr"
source_hash: "89e944f68bbe7852a05b9553a52edb07"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:53:58.953804+00:00"

tags:
  - cloud

keywords:
  - "point de montage"
  - "grandes images"
  - "utilisation générale"
  - "type de volume"
  - "remontage après redémarrage"
  - "stockage MVE"
  - "sauvegarder les données importantes"
  - "/dev/vdb1"
  - "/etc/fstab"
  - "instance"
  - "OpenStack Horizon"
  - "qcow2"
  - "démarrer depuis un volume"
  - "type high_performance"
  - "codes d'effacement"
  - "tableau de bord"
  - "Charger dans l'image"
  - "UUID"
  - "changer le type de volume"
  - "stockage sur disque HDD"
  - "créer une image depuis un volume"
  - "volume"
  - "vérifier le quota disponible"
  - "triple réplication"
  - "tâches intensives en entrée/sortie"
  - "format du disque"
  - "répertoire /mnt"
  - "sudo mount"
  - "volume éphémère"
  - "attacher un volume"
  - "séparer les données"
  - "vmdk"
  - "high_performance"
  - "cloner un volume"

questions:
  - "Quel type de stockage et de mécanisme de protection des données est utilisé pour les volumes « rbd1 » et comment cela affecte le coût et la performance ?"
  - "Quelles sont les étapes à suivre dans le tableau de bord pour créer, attacher et formater correctement un nouveau volume avant de le monter sur une instance ?"
  - "Comment monter un volume sur une instance Linux et quelles précautions faut‑il prendre pour garantir que le montage persiste après le redémarrage de l’instance ?"
  - "Quelle commande permet de monter un volume sur le répertoire /mnt et quels paramètres doit‑on adapter selon le dispositif ?"
  - "Où se trouve la structure de fichiers du volume une fois la commande de montage exécutée ?"
  - "Que faut‑il faire pour que le volume reste accessible après le redémarrage de l’instance ?"
  - "Comment configurer le montage automatique d’un volume au démarrage d’une instance en utilisant le fichier /etc/fstab et l’UUID du dispositif ?"
  - "Pourquoi le démarrage d’une instance depuis un volume est‑il préférable à celui depuis une image, et quels risques sont associés aux volumes éphémères ?"
  - "Quelles sont les étapes à suivre dans le tableau de bord pour créer une image à partir d’un volume existant ?"
  - "Quel format de disque doit‑on choisir pour créer une image destinée à OpenStack et pourquoi le format QCOW2 est‑il recommandé ?"
  - "Quelle est la procédure recommandée pour cloner un volume dans OpenStack et quelles précautions faut‑il prendre avant de lancer le clonage ?"
  - "Comment détacher correctement un volume attaché à une instance, notamment lorsqu’il s’agit d’un volume de démarrage (/dev/vda) ?"
  - "Pourquoi l'option « l'instance » n'est‑elle pas cochée lors de la création d’une instance ?"
  - "Quels problèmes peuvent survenir avec des images de plus de 10‑20 Go et quelle stratégie de sauvegarde est recommandée ?"
  - "Quelles sont les étapes à suivre dans le tableau de bord pour charger un volume dans une image ?"
  - "Quelles précautions doit‑on prendre avant de changer le type d’un volume dans OpenStack ?"
  - "Comment changer le type d’un volume de rbd1 vers high_performance en utilisant le tableau de bord Horizon ?"
  - "Quelle commande CLI permet de re‑typer un volume en high_performance et comment suivre l’avancement de l’opération ?"
  - "Quels sont les deux types de volumes présentés ainsi que leurs modes de stockage respectifs ?"
  - "Pour quels types d’applications ou de charges de travail le volume « high_performance » est‑il recommandé ?"
  - "Quelle contrainte de quota est spécifiquement associée au volume « high_performance » ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un volume est un espace de stockage qui n'est pas détruit à l'arrêt d'une machine virtuelle. Sur nos nuages, les volumes utilisent le stockage [Ceph](https://fr.wikipedia.org/wiki/Ceph) avec triple réplication, ou encore des [codes d'effacement](https://fr.wikipedia.org/wiki/Code_d%27effacement) pour garantir l’intégrité des données en cas de panne matérielle. Sur [Arbutus](cloud_resources.md), les volumes de type **rbd1** sont stockés sur des disques durs mécaniques et utilisent des codes d'effacement pour assurer l'intégrité des données, réduisant ainsi les coûts de stockage supplémentaires encourus par la triple réplication. Les volumes de type **high_performance** sont stockés sur des disques NVMe SSD et utilisent la triple réplication, moins efficace en termes de stockage, mais offrant de meilleures performances. Voir [l’information sur les volumes OpenStack](https://docs.openstack.org/cinder/latest/cli/cli-manage-volumes.html).

## Créer un volume

Pour créer un volume, cliquez sur le bouton *+ Créer un volume* et remplissez les champs comme suit :

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
Après quelques secondes, la page des volumes est rafraîchie et montre le nouveau volume lié à l'instance sélectionnée avec `/dev/vdb` ou un autre emplacement semblable.

### Formater un nouveau volume

*   **NE FORMATEZ PAS** si vous attachez un volume qui a déjà été utilisé pour stocker des données.
*   **Le formatage efface toute l'information qui se trouve dans le volume**, ce qui peut avoir d'importantes répercussions; la prudence est de mise.
*   Formater un volume signifie le préparer pour y enregistrer des fichiers et des répertoires.
*   Avant de pouvoir utiliser un nouveau volume, il faut le formater.
*   Voyez les directives sur [Linux](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md) ou Windows.

### Monter un volume

*   **Monter** un volume signifie créer une association logique entre le système de fichiers du volume d'une part et les répertoires et la structure des fichiers de l'instance d'autre part.
*   Montez le volume avec une commande semblable à
    ```bash
    sudo mount /dev/vdb1 /mnt
    ```
    selon le nom du périphérique, l'organisation du disque et le point de montage.
Le répertoire et la structure de fichiers du volume seront ainsi disponibles dans le répertoire `/mnt` de l'instance. Cependant, au redémarrage de l'instance, le volume devra être monté de nouveau avec la même commande `mount`.

Il est possible de monter automatiquement des volumes au démarrage d'une instance en ajoutant au fichier `/etc/fstab` une ligne qui contient les détails sur comment les monter.

Pour voir l'information, lancez la commande
```bash
blkid
```

Selon l'UUID, ajoutez à `/etc/fstab` la ligne
```
/dev/disk/by-uuid/anananan-anan-anana-anan-ananananana /mnt auto defaults,nofail 0 3
```

Remplacez *anananan-anan-anana-anan-ananananana* par l'UUID du périphérique que vous voulez monter automatiquement.

Pour plus d'information sur comment modifier ce fichier, voyez [cette page](https://help.ubuntu.com/community/Fstab).

## Démarrer depuis un volume
!!! warning "Attention"
    Le démarrage à partir d'une image crée un volume éphémère local et rapide sur l'hyperviseur. Cependant, les volumes éphémères ne sont pas sauvegardés. Un volume éphémère est perdu si l'instance est supprimée; si le sous-système de disques haute disponibilité de l'hyperviseur fait défaut; ou si l'instance doit être évacuée.

Pour créer un service persistant, il est recommandé de démarrer l'instance depuis un volume. Une instance démarrée depuis une image plutôt que d'un volume est stockée sur le disque local de la machine qui opère cette même instance. L'instance pourrait être perdue si un problème survient sur la machine ou sur son disque. Le stockage du volume procure une redondance qui protège l'instance de défaillance du matériel. De façon générale, les gabarits pour démarrer depuis un volume commencent par la lettre p (voir la page [Gabarits d'instances](virtual_machine_flavors.md)).

Pour plus d'information sur les options de stockage, voir [Options de stockage infonuagique](cloud_storage_options.md).

Démarrer une instance depuis un volume peut se faire
*   à partir d'une image en créant un nouveau volume;
*   à partir d'un volume existant;
*   à partir d'un instantané (*snapshot*), en créant un nouveau volume.

Si vous faites ceci pour la première fois, utilisez la première option; les deux autres options ne sont possibles que si vous avez déjà créé un volume ou un instantané de volume.

Un volume peut être créé au lancement d'une instance. Sélectionnez *Démarrer depuis une image (crée un volume)*. Remplissez ensuite les champs *Nom de l'image* et *Taille du périphérique*. Pour que le volume persiste après l'utilisation de l'instance, ne cochez pas la case *Supprimer le volume lors de la suppression de l'instance*, au bas de la fenêtre. Il est préférable de ne jamais cocher cette case puisque le volume peut être supprimé manuellement plus tard.

## Créer une image depuis un volume

Créer une image à partir d'un volume permet de télécharger l'image pour servir de copie de sécurité ou pour créer une instance sur un autre nuage, par exemple avec [VirtualBox](https://www.virtualbox.org/). Pour copier un volume vers un autre volume dans le même nuage, procédez plutôt par [clonage](#cloner-un-volume).

Pour créer l'image d'un volume, celle-ci doit d'abord être détachée de l'instance. Dans le cas d'un *volume de démarrage*, l'image ne peut être détachée que si l'instance est supprimée. Assurez-vous que la case *Supprimer le volume lors de la suppression de l'instance* n'a pas été cochée à la création de l'instance.

Les grandes images (plus de 10-20Gio) peuvent prendre beaucoup de temps à créer, téléverser ou lors d'autres opérations. Une solution serait de [séparer les données](backing_up_your_vm.md) si possible.

### Utiliser le tableau de bord
1.  Sous *Projet → Volumes*, sélectionnez le volume.
2.  Dans la colonne *Actions*, sélectionnez *Charger dans l'image* du menu déroulant.
3.  Entrez un nom pour la nouvelle image.
4.  Sélectionnez le *Format du disque*. QCOW2 est recommandé pour le nuage OpenStack parce que ce format est relativement plus compact que *Raw* et plus efficace avec OpenStack. Si vous voulez utiliser l'image avec Virtualbox sélectionnez de préférence *vmdk* ou *vdi*.
5.  Cliquez sur le bouton *Charger*.

### Utiliser le client de ligne de commande
Un [client de ligne de commande OpenStack](openstack_command_line_clients.md) peut faire ceci :
```bash
openstack image create --disk-format <format> --volume <volume_name> <image_name>
```
où
*   `<format>` est le format du disque; les deux options sont [qcow2](https://en.wikipedia.org/wiki/Qcow) et [vmdk](https://en.wikipedia.org/wiki/VMDK),
*   `<volume_name>` peut se trouver en cliquant sur le nom du volume à partir du tableau de bord OpenStack,
*   `<image_name>` est le nom que vous donnez à l'image.
Vous pouvez ensuite [télécharger l'image](working_with_images.md).

## Cloner un volume
Le clonage est le moyen recommandé pour la copie de volumes. Il est toujours possible de créer un nouveau volume depuis l'image d'un volume existant, mais le clonage est plus rapide et demande moins d'échange de données. C'est un moyen très utile si vous avez une instance persistante et que vous voulez faire des tests avant de passer en production. Nous recommandons fortement de terminer l’instance avant de cloner un volume pour éviter que l’état du volume cloné soit incohérent par rapport au volume source dans le cas où ce dernier aurait été modifié pendant la création du clone. Pour cloner un volume, utilisez [un client de ligne de commande OpenStack](openstack_command_line_clients.md) et entrez
```bash
openstack volume create --source <source-volume-id> --size <size-of-new-volume> <name-of-new-volume>
```

## Détacher un volume
Avant de détacher un volume, il est important de vérifier si des fichiers de ce volume sont utilisés par le système d'exploitation ou des applications actives dans votre instance; si c'est le cas, le volume détaché pourrait être corrompu ou les applications pourraient avoir des comportements inattendus. Il est donc recommandé de fermer l'instance ou de [démonter le volume](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md).

Pour détacher un volume, connectez-vous à OpenStack (voir la [liste des liens à nos ressources infonuagiques](cloud.md#ressources-infonuagiques)) et sélectionnez le projet qui contient le volume à détacher. Sélectionnez *Volumes → Volumes* pour faire afficher les volumes. La colonne *Attaché à* indique ce à quoi chaque volume est attaché.

*   Si la colonne indique `/dev/vda`, il s'agit d'un volume de démarrage; vous devez détacher l'instance avant de détacher le volume, autrement le message d'erreur *Impossible de déconnecter le volume* sera affiché.

*   Si la colonne indique `/dev/vdb`, `/dev/vdc`, etc., il n'est pas nécessaire de détacher l'instance. Dans la liste déroulante sous *Actions*, sélectionnez *Gérer les attachements*, cliquez sur le bouton *Détacher le volume* puis sur l'autre bouton *Détacher le volume* pour confirmer.

## Changer le type d'un volume existant

Les nuages OpenStack offrent plusieurs types de stockage pour les volumes. Sur Arbutus, les principaux types sont

| Type de volume         | Stockage                                  | Utilisation recommandée                                                                                                                               |
| :--------------------- | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **rbd1**               | Stockage sur disque HDD                   | Utilisation générale et tâches non intensives ou qui ne demandent pas de stockage de haute performance                                                  |
| **high_performance**   | Stockage MVE (M-Profile Vector Extension) | Systèmes d'exploitation, bases de données et autres tâches intensives en entrée/sortie, ou sensibles à la latence.<br>Remarque : le quota est très limité pour ce type de volume. |

Avant de changer le type d'un volume, il est recommandé de :
*   Sauvegarder les données importantes; comme pour toute opération de stockage, assurez-vous que les données importantes sont sauvegardées avant de faire des modifications.
*   Vérifier le quota disponible; le stockage de destination peut avoir des quotas ou des contraintes de disponibilité différents de ceux de la source.
*   Prévoir que l'opération prenne un certain temps; la migration peut nécessiter la migration des données d'autres systèmes de stockage.
*   Éviter les activités inutiles pendant la migration. Pour les applications importantes ou à forte intensité d'écriture, pensez à planifier le changement pendant une période de maintenance.

Il est possible de passer de **rbd1** à **high_performance** sans avoir à créer un nouveau volume, soit dans l'interface web ou dans la ligne de commande du client.

### Changer via le tableau de bord

Avant de commencer, nous recommandons de sauvegarder toutes les données importantes. L'exemple suivant décrit le processus de migration de **rbd1** vers **high_performance**.

1.  Connectez-vous au tableau de bord OpenStack Horizon.
2.  Sélectionnez le projet approprié.
3.  Dans le menu de navigation, sélectionnez *Projet → Volumes → Volumes*.
4.  Localisez le volume que vous voulez modifier.
5.  Dans la colonne *Actions*, ouvrez le menu déroulant du volume et sélectionnez *Changer le type de volume*.
6.  Dans la boîte de dialogue *Changer le type de volume* :
    *   Pour *Type*, sélectionnez **high_performance**.
    *   Pour *Politique de migration*, sélectionnez *Sur demande*.
7.  Cliquez sur le bouton *Changer le type de volume* pour commencer l'opération.
8.  Retournez à la page *Volumes* et surveillez l'état du volume. Pendant l'opération, le volume peut afficher le statut *Retyping*.
9.  Quand l'opération est terminée, vérifiez que le *Type* du volume est maintenant **high_performance**.

!!! warning "Important"
    Passer de **rbd1** à **high_performance** pourrait nécessiter que les données du volume soient migrées vers d'autres espaces de stockage; l'opération peut donc prendre un certain temps, surtout pour les volumes plus gros. Ne supposez pas qu'un tel changement se fait instantanément.

### Changer via la ligne de commande

Identifiez d'abord le volume sur la ligne de commande du client avec
```bash
openstack volume list
```

Vérifiez le type actuel avec
```bash
openstack volume show <volume>
```

Changez pour le type **high_performance**.
```bash
openstack volume set --type high_performance --retype-policy on-demand <volume>
```

Pour suivre le processus de changement du volume, utilisez
```bash
openstack volume show <volume>
```

Quand l'opération est terminée, vérifiez que le changement s'est bien fait.