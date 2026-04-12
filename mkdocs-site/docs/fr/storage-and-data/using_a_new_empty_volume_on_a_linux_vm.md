---
title: "Using a new empty volume on a Linux VM/fr"
slug: "using_a_new_empty_volume_on_a_linux_vm"
lang: "fr"

source_wiki_title: "Using a new empty volume on a Linux VM/fr"
source_hash: "91dd39f9953b600d2e11ff4ec0c20b56"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:20:50.911591+00:00"

tags:
  []

keywords:
  - "fstab"
  - "monter un volume"
  - "formater"
  - "démonter un volume"
  - "partitionner"

questions:
  - "Quelles sont les étapes de commandes nécessaires pour partitionner, formater et monter un nouveau volume sous Linux ?"
  - "Comment doit-on configurer le système pour que le volume soit monté automatiquement en cas de réinitialisation de l'instance ?"
  - "Pourquoi est-il recommandé de démonter un volume avant de l'attacher à une autre instance et quelle condition est requise pour y parvenir sans erreur ?"
  - "Quelles sont les étapes de commandes nécessaires pour partitionner, formater et monter un nouveau volume sous Linux ?"
  - "Comment doit-on configurer le système pour que le volume soit monté automatiquement en cas de réinitialisation de l'instance ?"
  - "Pourquoi est-il recommandé de démonter un volume avant de l'attacher à une autre instance et quelle condition est requise pour y parvenir sans erreur ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Dans la plupart des environnements Linux, les étapes suivantes serviront à partitionner, formater et monter un nouveau volume.

!!! warning "Attention"
    Si ce n'est pas un nouveau volume, n'effectuez pas les étapes de partitionnement et de formatage, car cela entraînera la perte de données. Procédez uniquement au montage.

1.  Partitionnez le volume avec
    ```bash
    sudo fdisk /dev/vdb
    ```
    `fdisk` vous demande de saisir une commande; utilisez les caractères suivants :

    *   `n` => nouvelle partition
    *   `p` => primaire, une seule partition sur le disque
    *   `1` => partition numéro 1
    *   `[Entrée]` => premier secteur (utiliser la valeur par défaut)
    *   `[Entrée]` => dernier secteur (utiliser la valeur par défaut)
    *   `w` => écrire la table de partition sur disque et quitter

2.  Formatez la nouvelle partition avec
    ```bash
    sudo mkfs -t ext4 /dev/vdb1
    ```

3.  Créez l'emplacement où monter le périphérique
    ```bash
    sudo mkdir /media/data
    ```

4.  Montez le volume avec
    ```bash
    sudo mount /dev/vdb1 /media/data
    ```

Si pour une raison quelconque l'instance est redémarrée, le volume devra être monté à nouveau. Pour que l'instance monte le volume automatiquement, modifiez `/etc/fstab` en ajoutant une ligne comme ceci :

```
/dev/vdb1 /media/data ext4 defaults 0 2
```

La page [fstab](https://fr.wikipedia.org/wiki/Fstab) présente plus de détails. Si l'instance n'est pas redémarrée, le nouveau périphérique ajouté à `/etc/fstab` peut être monté avec :

```bash
sudo mount -a
```

## Démonter un volume ou un autre périphérique

Si vous devez démonter un volume ou un autre périphérique, par exemple pour en créer une image ou pour le joindre à une autre instance, il est préférable de le démonter d'abord afin d'éviter la corruption des données.

Pour démonter le volume que nous avons monté dans l'exemple ci-dessus, utilisez la commande :

```bash
sudo umount /media/data
```

!!! warning "Attention"
    Pour que cette commande fonctionne, aucun fichier ne doit être utilisé en lecture ou en écriture par le système d'exploitation ou par une autre application active dans l'instance. Sinon, un message s'affichera indiquant que le volume est occupé.