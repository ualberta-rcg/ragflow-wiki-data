---
title: "Managing your Linux VM/fr"
tags:
  - cloud

keywords:
  []
---

Linux est très utilisé pour les machines virtuelles. Les distributions souvent employées sont AlmaLunix, CentOS, Debian, Fedora et Ubuntu. Vous trouverez ici de l'assistance pour les tâches communes. Il est aussi possible d'utiliser [le système d'exploitation Windows](cloud_quick_start-fr#windows.md).

=Gestion des utilisateurs sous Linux= 

Il existe quelques méthodes pour permettre à plusieurs personnes d'avoir accès à une machine virtuelle. Notre recommandation est de créer de nouveaux comptes d'utilisateur et de leur associer des [clés SSH](ssh-keys-fr.md).

## Créer un compte d'utilisateur et ses clés
Pour créer un compte d'utilisateur sur Ubuntu, utilisez la commande 

```bash
sudo adduser --disabled-password USERNAME
```

Pour pouvoir se connecter, le nouvel utilisateur devra avoir une paire de clés; selon le système d'exploitation, voyez [Générer des clés SSH sous Windows](generating_ssh_keys_in_windows-fr.md)  ou [Créer une paire de clés](using_ssh_keys_in_linux-fr#créer_une_paire_de_clés.md) sous Linux et Mac. Ajoutez ensuite la clé publique à <tt>/home/USERNAME/.ssh/authorized_keys</tt> pour la machine virtuelle et vérifiez que les permissions et le propriétaire sont corrects, comme indiqué aux étapes 2 et 3 de [Se connecter avec une paire de clés](using_ssh_keys_in_linux-fr#se_connecter_avec_une_paire_de_clés.md).

## Privilèges admin
Pour accorder les privilèges admin (<i>root</i>) à un utilisateur, utilisez la commande 

```bash
sudo visudo -f /etc/sudoers.d/90-cloud-init-users
```

Ceci démarre un éditeur où vous pouvez ajouter une ligne comme
 USERNAME ALL=(ALL) NOPASSWD:ALL
Pour plus d'information sur la commande `visudo` et sur comment éditer le fichier, consultez le [tutoriel de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos#what-is-visudo).

## Problèmes de système et de sécurité
Référez-vous à 
* [Récupération des données d'une machine virtuelle compromise](recovering_data_from_a_compromised_vm-fr.md)
* [Récupération d'une machine virtuelle via la console](vm_recovery_via_cloud_console-fr.md)