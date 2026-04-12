---
title: "Managing your Linux VM/fr"
slug: "managing_your_linux_vm"
lang: "fr"

source_wiki_title: "Managing your Linux VM/fr"
source_hash: "24e49ac1609b79aa5fa0b86e601cd5a6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:58:32.483194+00:00"

tags:
  - cloud

keywords:
  - "machines virtuelles"
  - "Linux"
  - "privilèges admin"
  - "gestion des utilisateurs"
  - "clés SSH"

questions:
  - "Comment créer un nouveau compte d'utilisateur et configurer ses clés SSH pour l'accès à la machine virtuelle ?"
  - "Quelle commande et quelle méthode faut-il utiliser pour accorder des privilèges d'administrateur (root) à un utilisateur ?"
  - "Quelles sont les solutions proposées pour récupérer les données ou l'accès à une machine virtuelle compromise ?"
  - "Comment créer un nouveau compte d'utilisateur et configurer ses clés SSH pour l'accès à la machine virtuelle ?"
  - "Quelle commande et quelle méthode faut-il utiliser pour accorder des privilèges d'administrateur (root) à un utilisateur ?"
  - "Quelles sont les solutions proposées pour récupérer les données ou l'accès à une machine virtuelle compromise ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Linux est très utilisé pour les machines virtuelles. Les distributions souvent employées sont AlmaLinux, CentOS, Debian, Fedora et Ubuntu. Vous trouverez ici de l'assistance pour les tâches communes. Il est aussi possible d'utiliser [le système d'exploitation Windows](cloud-quick-start.md#windows).

# Gestion des utilisateurs sous Linux

Il existe quelques méthodes pour permettre à plusieurs personnes d'avoir accès à une machine virtuelle. Notre recommandation est de créer de nouveaux comptes d'utilisateur et de leur associer des [clés SSH](ssh-keys.md).

## Créer un compte d'utilisateur et ses clés

Pour créer un compte d'utilisateur sur Ubuntu, utilisez la commande suivante :

```bash
sudo adduser --disabled-password USERNAME
```

Pour pouvoir se connecter, le nouvel utilisateur devra avoir une paire de clés. Selon le système d'exploitation, voyez [Générer des clés SSH sous Windows](generating-ssh-keys-in-windows.md) ou [Créer une paire de clés](using-ssh-keys-in-linux.md#créer-une-paire-de-clés) sous Linux et Mac. Ajoutez ensuite la clé publique à `/home/USERNAME/.ssh/authorized_keys` pour la machine virtuelle et vérifiez que les permissions et le propriétaire sont corrects, comme indiqué aux étapes 2 et 3 de [Se connecter avec une paire de clés](using-ssh-keys-in-linux.md#se-connecter-avec-une-paire-de-clés).

## Privilèges admin

Pour accorder les privilèges d'administrateur (*root*) à un utilisateur, utilisez la commande suivante :

```bash
sudo visudo -f /etc/sudoers.d/90-cloud-init-users
```

Ceci démarre un éditeur où vous pouvez ajouter une ligne comme :

```
USERNAME ALL=(ALL) NOPASSWD:ALL
```

Pour plus d'information sur la commande `visudo` et sur comment modifier le fichier, consultez le [tutoriel de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos#what-is-visudo).

## Problèmes de système et de sécurité

Référez-vous aux pages suivantes :

*   [Récupération des données d'une machine virtuelle compromise](recovering-data-from-a-compromised-vm.md)
*   [Récupération d'une machine virtuelle via la console](vm-recovery-via-cloud-console.md)