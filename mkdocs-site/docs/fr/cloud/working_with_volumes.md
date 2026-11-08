---
title: "Working with volumes/fr"
slug: "working_with_volumes"
lang: "fr"

source_wiki_title: "Working with volumes/fr"
source_hash: "fd71efb03c453153e5b48bfd42c6d558"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T03:04:07.942543+00:00"

tags:
  - cloud
  - cloud

keywords:
  - "/dev/vdb1"
  - "openstack image create"
  - "I/O-intensive workloads"
  - "démarrer depuis un volume"
  - "HDD-based storage"
  - "instance"
  - "cloner un volume"
  - "type high_performance"
  - "détacher un volume"
  - "high storage performance"
  - "UUID"
  - "high_performance"
  - "backup important data"
  - "/mnt"
  - "grandes images"
  - "type de volume high_performance"
  - "migration policy"
  - "attacher un volume"
  - "volume persistant"
  - "tableau de bord"
  - "volume retype"
  - "OpenStack Horizon"
  - "sudo mount"
  - "point de montage"
  - "volume"
  - "Charger dans l'image"
  - "triple réplication"
  - "créer une image depuis un volume"
  - "NVMe-based storage"
  - "sauvegarde"
  - "Change Volume Type"
  - "fstab"
  - "redémarrage de l'instance"
  - "format du disque"
  - "codes d'effacement"

questions:
  - "Quelle différence de stockage et de réplication existe‑t‑il entre les volumes de type « rbd1 » et « high_performance » sur Arbutus ?"
  - "Quelles sont les étapes à suivre pour créer un volume, l’attacher à une instance, puis le formater correctement ?"
  - "Comment monter un volume sur une VM (Linux ou Windows) et pourquoi le montage doit‑il être répété après chaque redémarrage de l’instance ?"
  - "Quelle commande doit‑on utiliser pour monter le volume en précisant le dispositif et le point de montage ?"
  - "Dans quel répertoire de l’instance les fichiers du volume seront‑ils accessibles après le montage ?"
  - "Quelle action est nécessaire pour remonter le volume après le redémarrage de l’instance ?"
  - "Comment configurer le montage automatique d’un volume au démarrage d’une instance en utilisant son UUID dans le fichier /etc/fstab ?"
  - "Quels sont les avantages de démarrer une instance depuis un volume plutôt que depuis une image, et quelles précautions prendre lors de la création du volume ?"
  - "Quelles étapes suivre dans le tableau de bord pour créer une image à partir d’un volume existant, notamment pour les volumes de démarrage ?"
  - "Quel format de disque doit‑on choisir pour créer une image destinée à OpenStack et pourquoi le qcow2 est‑il recommandé ?"
  - "Quelles sont les étapes et les précautions à observer pour cloner ou détacher un volume dans OpenStack ?"
  - "Quels types de volumes sont proposés sur le cloud Arbutus et quelles sont leurs utilisations recommandées ?"
  - "Pourquoi l'option « instance » n'a‑t‑elle pas été cochée lors de la création de l'instance ?"
  - "Quels sont les inconvénients des images de plus de 10‑20 Go et comment la séparation des données peut‑elle aider ?"
  - "Comment charger un volume dans une image en utilisant le tableau de bord (Projet → Volumes → Actions → « Charger dans l'image ») ?"
  - "What steps are required in the OpenStack Horizon dashboard to change a volume from the rbd1 type to high_performance?"
  - "How can the same volume‑type change be executed via the OpenStack command‑line client, and which commands are used?"
  - "What precautions and potential impacts (e.g., quota, migration time, disk activity) should be considered before initiating the volume type migration?"
  - "What are the main differences between HDD‑based storage and NVMe‑based storage in terms of performance and typical use cases?"
  - "Which types of workloads are recommended for each volume type (general‑purpose vs. I/O‑intensive or latency‑sensitive)?"
  - "What precaution is advised before changing the volume type of a storage volume?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un volume est un espace de stockage qui n'est pas détruit à l'arrêt d'une machine virtuelle. Sur nos nuages, les volumes utilisent le stockage [Ceph](https://fr.wikipedia.org/wiki/Ceph) avec triple réplication, ou encore des [codes d'effacement](https://fr.wikipedia.org/wiki/Code_d%27effacement) pour garantir l’intégrité des données en cas de panne matérielle. Sur [Arbutus](https://docs.alliancecan.ca/wiki/Cloud_resources/fr), les volumes de type *rbd1* sont stockés sur des disques durs mécaniques et utilisent des codes d'effacement pour assurer l'intégrité des données, réduisant ainsi les coûts de stockage supplémentaires encourus par la triple réplication. Les volumes de type *high_performance* sont stockés sur des disques NVMe SSD et utilisent la triple réplication, moins efficace en termes de stockage, mais offrant de meilleures performances. Voir [l’information sur les volumes OpenStack](https://docs.openstack.org/cinder/latest/cli/cli-manage-volumes.html).

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

Dans le tableau de bord, à partir de la page *Volumes* :
*   **Attacher** un volume signifie l'associer à une instance. C'est comme insérer une clé USB ou ajouter un disque externe à votre ordinateur.
*   Vous pouvez attacher un volume à partir de la page *Volumes* du tableau de bord.
*   Dans la colonne *Actions*, sélectionnez *Gérer les attachements* du menu déroulant.
*   Dans le champ *Attacher à l'instance*, sélectionnez l'instance appropriée.
*   Cliquez sur le bouton *Attacher le volume*.

Après quelques secondes, la page des volumes est rafraîchie et montre le nouveau volume lié à l'instance sélectionnée avec `/dev/vdb` ou autre endroit semblable.

### Formater un nouveau volume

*   **NE FORMATEZ PAS** si vous attachez un nouveau volume. Le volume a dû être formaté si vous l'avez déjà utilisé pour stocker des données.
*   **Le formatage efface toute l'information qui se trouve dans le volume**, ce qui peut avoir d'importantes répercussions; la prudence est de mise.
*   Formater un volume signifie le préparer pour y enregistrer des fichiers et des répertoires.
*   Avant de pouvoir utiliser un nouveau volume, il faut le formater.
*   Voyez les directives sur [Linux](../storage-and-data/using_a_new_empty_volume_on_a_linux_vm.md) ou Windows.

### Monter un volume

*   **Monter** un volume signifie créer une association logique entre le système de fichiers du volume d'une part et les répertoires et la structure des fichiers de l'instance d'autre part.
*   Montez le volume avec une commande semblable à `[name@server ~]$ sudo mount /dev/vdb1 /mnt` selon le nom du dispositif, l'organisation du disque et le point de montage.

Le répertoire et la structure de fichiers du volume seront ainsi disponibles dans le répertoire `/mnt` de l'instance. Cependant, au redémarrage de l'instance, le volume devra être monté de nouveau avec la même commande `mount`.

Il est possible de monter automatiquement des volumes au démarrage d'une instance en ajoutant au fichier `/etc/fstab` une ligne qui contient les détails sur comment les monter.

Pour voir l'information, lancez la commande
```bash
blkid
```

Selon le `UUID`, ajoutez à `/etc/fstab` la ligne

```
/dev/disk/by-uuid/anananan-anan-anana-anan-ananananana /mnt auto defaults,nofail 0 3
```

Remplacez *anananan-anan-anana-anan-ananananana* par l'UUID du dispositif que vous voulez monter automatiquement.

Pour plus d'information sur comment modifier ce fichier, voyez [cette page](https://help.ubuntu.com/community/Fstab).

## Démarrer depuis un volume

!!! warning "Attention"
    Le démarrage à partir d'une image crée un volume éphémère local et rapide sur l'hyperviseur. Cependant, les volumes éphémères ne sont pas sauvegardés. Un volume éphémère est perdu si l'instance est supprimée; si le sous-système de disques haute disponibilité de l'hyperviseur fait défaut; ou si l'instance doit être évacuée.

Pour créer un service persistant, il est recommandé de démarrer l'instance depuis un volume. Une instance démarrée depuis une image plutôt que d'un volume est stockée sur le disque local de la machine qui opère cette même instance. L'instance pourrait être perdue si un problème survient sur la machine ou sur son disque. Le stockage du volume procure une redondance qui protège l'instance de défaillance du matériel. De façon générale, les gabarits pour démarrer depuis un volume commencent par la lettre p (voir la page [Gabarits d'instances](virtual_machine_flavors.md)).

Pour plus d'information sur les options de stockage, voir [Options de stockage infonuagique](cloud_storage_options.md).

Démarrer une instance depuis un volume peut se faire :
*   à partir d'une image en créant un nouveau volume;
*   à partir d'un volume existant;
*   à partir d'un instantané (*snapshot*), en créant un nouveau volume.

Si vous faites ceci pour la première fois, utilisez la première option; les deux autres options ne sont possibles que si vous avez déjà créé un volume ou un instantané de volume.

Un volume peut être créé au lancement d'une instance. Sélectionnez *Démarrer depuis une image (crée un volume)*. Remplissez ensuite les champs *Nom de l'image* et *Taille du périphérique*. Pour que le volume persiste après l'utilisation de l'instance, ne cochez pas la case *Supprimer le volume lors de la suppression de l'instance*, au bas de la fenêtre. Il est préférable de ne jamais cocher cette case puisque le volume peut être supprimé manuellement plus tard.

## Créer une image depuis un volume

Pour créer une image depuis un volume, vous pouvez la télécharger pour servir de copie de sécurité ou pour créer une instance sur un autre nuage, par exemple avec [VirtualBox](https://www.virtualbox.org/). Pour copier un volume vers un autre volume dans le même nuage, procédez plutôt par [clonage](#cloner-un-volume).

Pour créer l'image d'un volume, elle doit d'abord être détachée de l'instance. Dans le cas d'un *boot volume*, l'image ne peut être détachée que si l'instance est supprimée. Assurez-vous que la case *Supprimer le volume lors de la suppression de l'instance* n'a pas été cochée à la création de l'instance.

Les grandes images (plus de 10-20 Go) peuvent prendre beaucoup de temps à créer, téléverser ou autres opérations. Une solution serait de [séparer les données](backing_up_your_vm.md) si possible.

### Utiliser le tableau de bord

1.  Sous *Projet* -> *Volumes*, sélectionnez le volume.
2.  Dans la colonne *Actions*, sélectionnez *Charger dans l'image* du menu déroulant.
3.  Entrez un nom pour la nouvelle image.
4.  Sélectionnez le *Format du disque*. QCOW2 est recommandé pour le nuage OpenStack parce que ce format est relativement plus compact que *Raw* et plus efficace avec OpenStack. Si vous voulez utiliser l'image avec Virtualbox sélectionnez de préférence *vmdk* ou *vdi*.
5.  Cliquez sur le bouton *Charger*.

### Utiliser le client ligne de commande

Un [client ligne de commande](openstack_command_line_clients.md) peut faire ceci :
```bash
openstack image create --disk-format <format> --volume <volume_name> <image_name>
```
où
*   `<format>` est le format du disque; les deux options sont [qcow2](https://en.wikipedia.org/wiki/Qcow) et [vmdk](https://en.wikipedia.org/wiki/VMDK),
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

Pour détacher un volume, connectez-vous à OpenStack (voir la [liste des liens à nos ressources infonuagiques](cloud.md#ressources-infonuagiques)) et sélectionnez le projet qui contient le volume à détacher. Sélectionnez *Volumes* -> *Volumes* pour faire afficher les volumes. La colonne *Attaché à* indique ce à quoi chaque volume est attaché.

*Si la colonne indique `/dev/vda`, il s'agit d'un volume de démarrage; vous devez détacher l'instance avant de détacher le volume, autrement le message d'erreur *Impossible de déconnecter le volume* sera affiché.

*Si la colonne indique `/dev/vdb`, `/dev/vdc`, etc., il n'est pas nécessaire de détacher l'instance. Dans la liste déroulante sous *Actions*, sélectionnez *Gérer les attachements*, cliquez sur le bouton *Détacher le volume* puis sur l'autre bouton *Détacher le volume* pour confirmer.

## Changer le type d'un volume existant

Les nuages OpenStack (comme Arbutus) peuvent offrir plusieurs types de volumes avec différentes caractéristiques de performance de stockage. Les deux principaux types de volumes disponibles sur Arbutus sont :

| Type de volume     | Stockage                                | Usage recommandé                                                                                                                                                                                            |
| :----------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *rbd1*             | Stockage basé sur disque dur (HDD)      | Stockage général et charges de travail ne nécessitant pas de hautes performances de stockage ou lorsque la grande taille est souhaitée                                                                          |
| *high_performance* | Stockage basé sur NVMe                  | Systèmes d'exploitation, bases de données et autres charges de travail à forte intensité d'E/S ou sensibles à la latence. **Note :** Le quota est très limité pour ce type de volume.                          |

Avant de changer un type de volume
Nous vous recommandons de :
1.  Sauvegarder les données importantes. Comme pour toute opération de stockage, assurez-vous que les données importantes sont sauvegardées avant d'effectuer des changements.
2.  Vérifier le quota disponible. Le niveau de stockage de destination peut avoir des quotas ou des contraintes de disponibilité différents.
3.  Prévoir que l'opération prendra du temps. Changer le stockage sous-jacent d'un grand volume peut nécessiter la migration des données entre les systèmes de stockage.
4.  Éviter toute activité de disque inutile pendant la migration. Pour les applications importantes ou à forte intensité d'écriture, envisagez de planifier le changement pendant une période de maintenance.

Les volumes existants peuvent être changés de *rbd1* à *high_performance* sans créer un nouveau volume. Cela peut être fait à la fois dans l'interface web ou via l'interface en ligne de commande (CLI) :

### Changer un volume existant à l'aide du tableau de bord

Avant de commencer, nous vous recommandons de sauvegarder toutes les données importantes sur le volume. Cet exemple expliquera le processus de migration d'un volume de type *rbd1* vers un volume de type *high_performance*.

1.  Connectez-vous au tableau de bord OpenStack Horizon.
2.  Sélectionnez le projet approprié.
3.  Dans le menu de navigation, sélectionnez *Projet* → *Volumes* -> *Volumes*.
4.  Repérez le volume que vous souhaitez modifier.
5.  Dans la colonne *Actions*, ouvrez le menu déroulant pour le volume et sélectionnez *Changer le type de volume*.
6.  Dans la boîte de dialogue *Changer le type de volume* :
    a.  Pour *Type*, sélectionnez *high_performance*.
    b.  Pour *Politique de migration*, sélectionnez *À la demande*.
7.  Cliquez sur *Changer le type de volume* pour démarrer l'opération.
8.  Retournez à la page *Volumes* et surveillez l'état du volume. Pendant l'opération, le volume peut afficher un état de *Retypage*.
9.  Une fois l'opération terminée, vérifiez que le *Type* du volume est maintenant *high_performance*.

**Important :** Le changement entre *rbd1* et *high_performance* peut nécessiter la migration des données du volume entre différents systèmes de stockage. L'opération peut donc prendre un certain temps, en particulier pour les volumes plus importants. Ne supposez pas qu'un changement de type de volume est instantané.

### Changer un volume existant à l'aide de l'interface en ligne de commande (CLI)

À l'aide du client de ligne de commande OpenStack, identifiez d'abord le volume :
```bash
openstack volume list
```

Vérifiez son type de volume actuel :
```bash
openstack volume show <volume>
```

Demandez ensuite que le volume soit modifié pour le type *high_performance* :
```bash
openstack volume set --type high_performance --retype-policy on-demand <volume>
```

Vous pouvez surveiller le volume pendant que le changement a lieu :
```bash
openstack volume show <volume>
```

Une fois l'opération terminée, vérifiez que le type de volume est affiché comme *high_performance*.