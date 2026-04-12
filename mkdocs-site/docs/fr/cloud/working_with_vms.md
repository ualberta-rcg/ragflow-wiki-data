---
title: "Working with VMs/fr"
slug: "working_with_vms"
lang: "fr"

source_wiki_title: "Working with VMs/fr"
source_hash: "37fe32b1e78daa75490068d625d071a7"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T13:38:25.764102+00:00"

tags:
  - cloud

keywords:
  - "Modifier la taille"
  - "Gabarit"
  - "Machine virtuelle"
  - "Instance"
  - "Verrouiller une instance"

questions:
  - "Pourquoi et comment verrouiller une instance dans le tableau de bord ?"
  - "Quels sont les risques potentiels liés à la modification de la taille d'une instance ?"
  - "Comment la gestion des disques éphémères diffère-t-elle entre les gabarits de type \"c\" et \"p\" lors d'un redimensionnement ?"
  - "Pourquoi et comment verrouiller une instance dans le tableau de bord ?"
  - "Quels sont les risques potentiels liés à la modification de la taille d'une instance ?"
  - "Comment la gestion des disques éphémères diffère-t-elle entre les gabarits de type \"c\" et \"p\" lors d'un redimensionnement ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Service infonuagique](cloud.md)*

Une machine virtuelle (*VM*) est un serveur virtuel dans une infrastructure de nuage. OpenStack utilise le terme *instance* pour désigner une machine virtuelle active que vous pouvez gérer à partir du tableau de bord.

# Instances

## Verrouiller une instance

Il peut être utile de verrouiller une instance lorsque vous travaillez à un projet avec plusieurs autres personnes ou que vous voulez empêcher qu'une instance soit arrêtée ou supprimée accidentellement.

Pour verrouiller une instance, cliquez sur *Verrouiller l'instance* dans le menu déroulant de la colonne *Actions* du tableau de bord. Une icône indique que le verrou est mis.

!!! warning "Attention"
    La plupart des options du menu *Actions* ne pourront pas être exécutées tant que l'instance est verrouillée.

Pour déverrouiller une instance, cliquez sur *Déverrouiller l'instance* dans le menu déroulant de la colonne *Actions* du tableau de bord.

## Modifier la taille d'une instance

Il est possible de modifier la taille d'une instance en changeant son gabarit. Il y a toutefois certains points à considérer selon que le gabarit est "p" ou "c" (voir [Gabarits d'instances](virtual-machine-flavors.md)).

!!! warning "Important"
    Le fait de redimensionner une instance peut causer des problèmes, car l'instance est en quelque sorte supprimée puis recréée avec un nouveau gabarit. En cas de doute, demandez l'avis du [soutien technique](technical-support.md).

### Gabarits "c"

Les gabarits "c" ont des disques éphémères additionnels dont la taille peut être modifiée en sélectionnant un autre gabarit "c". La taille de ces disques éphémères ne peut pas être diminuée et donc les instances de gabarit "c" ne peuvent être modifiées que par des gabarits avec des disques de taille égale ou supérieure. Une fois la taille modifiée, vous ne verrez pas un disque éphémère plus grand dans votre instance, c'est-à-dire que la commande `df -h` ne montrera pas l'augmentation. Pour voir l'espace ajouté, il faut modifier la taille du système de fichiers (voir la commande `resize2fs`).

!!! warning "Prudence"
    La modification d'un système de fichiers peut prendre beaucoup de temps si les partitions sont larges. Faites une copie du système de fichiers avant de procéder (voir [Sauvegarder une instance](backing-up-your-vm.md)).

### Gabarits "p"

Les gabarits "p" n'ont typiquement pas de disques éphémères qui leur sont associés; leur taille peut donc être modifiée sans ces considérations.