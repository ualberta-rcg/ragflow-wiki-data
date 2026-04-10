---
title: "Using a new empty volume on a Linux VM/fr"
slug: "using_a_new_empty_volume_on_a_linux_vm"
lang: "fr"

source_wiki_title: "Using a new empty volume on a Linux VM/fr"
source_hash: "91dd39f9953b600d2e11ff4ec0c20b56"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:20:17.035709+00:00"

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

Dans la plupart des environnements Linux, les étapes suivantes serviront à partitionner, formater et monter un nouveau volume.

!!! attention
    S'il ne s'agit pas d'un nouveau volume, n'exécutez pas le partitionnement et le formatage, car une partie des données sera perdue. Procédez uniquement au montage.

1.  Partitionnez le volume avec :
    ```bash
    sudo fdisk /dev/vdb
    ```
    `fdisk` vous demande d'entrer une commande; utilisez les caractères suivants :
    *   `n` => nouvelle partition
    *   `p` => primaire, une seule partition sur le disque
    *   `1` => partition numéro 1
    *   `<return>` => premier secteur (utiliser la valeur par défaut)
    *   `<return>` => dernier secteur (utiliser la valeur par défaut)
    *   `w` => écrire la table de partition sur disque et quitter
2.  Formatez la nouvelle partition avec :
    ```bash
    sudo mkfs -t ext4 /dev/vdb1
    ```
3.  Créez l'endroit où monter le périphérique :
    ```bash
    sudo mkdir /media/data
    ```
4.  Montez le volume avec :
    ```bash
    sudo mount /dev/vdb1 /media/data
    ```

Si, pour une raison quelconque, l'instance est réinitialisée, le volume devra être monté à nouveau. Pour que l'instance remonte le volume automatiquement, modifiez le fichier `/etc/fstab` en y ajoutant une ligne comme ceci :

```text
/dev/vdb1 /media/data ext4 defaults 0 2
```

La page [fstab](https://fr.wikipedia.org/wiki/Fstab) présente plus de renseignements. Si l'instance n'est pas réinitialisée, le nouveau périphérique ajouté au fichier `/etc/fstab` peut être monté avec :

```bash
sudo mount -a
```

## Démonter un volume ou un autre périphérique

!!! attention "Prévenir la corruption des données"
    Si vous devez démonter un volume ou un autre périphérique, par exemple pour en créer une image ou pour l'attacher à une autre instance, il est préférable de le démonter d'abord afin d'éviter toute corruption des données.

Pour démonter le volume que nous avons monté dans l'exemple ci-dessus, utilisez la commande suivante :
```bash
sudo umount /media/data
```
Pour que cette commande fonctionne, aucun fichier ne doit être utilisé en lecture ou en écriture par le système d'exploitation ou par une autre application active dans l'instance. Autrement, un message sera affiché indiquant que le volume est occupé.