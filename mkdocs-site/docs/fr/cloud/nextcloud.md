---
title: "Nextcloud/fr"
slug: "nextcloud"
lang: "fr"

source_wiki_title: "Nextcloud/fr"
source_hash: "6c861915213d492e202c954979da2b5f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:45:25.585547+00:00"

tags:
  []

keywords:
  - "synchronisation de fichiers"
  - "compte Alliance"
  - "WebDAV"
  - "synchronisation"
  - "CCDB"
  - "Université Simon-Fraser"
  - "groupe CCDB"
  - "rclone"
  - "nom d'utilisateur"
  - "fichier ou répertoire"
  - "partage de fichiers"
  - "partage de données"
  - "stockage"
  - "stockage de données"
  - "Share link"
  - "partage"
  - "Partager des fichiers"
  - "outils ligne de commande"
  - "utilisateur"
  - "Synchronization Client"
  - "Nextcloud"

questions:
  - "Quelles sont les caractéristiques principales et la limite de stockage du service Nextcloud proposé par l'Alliance ?"
  - "Quelles sont les différentes méthodes d'accès permettant de gérer et de synchroniser ses fichiers sur Nextcloud ?"
  - "Quelle est la différence fondamentale de fonctionnement entre un client WebDAV et le client de synchronisation (Desktop Synchronization Client) ?"
  - "Comment le client de synchronisation Nextcloud gère-t-il les modifications de fichiers et le travail hors ligne ?"
  - "Quels sont les avantages d'utiliser l'outil en ligne de commande rclone par rapport à curl pour transférer des fichiers ?"
  - "Quelle est la procédure à suivre pour partager des fichiers avec d'autres utilisateurs et comment éviter les erreurs d'identification ?"
  - "Où peut-on consulter les recommandations officielles concernant l'utilisation de WebDAV ?"
  - "Quelle est la principale différence de fonctionnement entre un client WebDAV et un client de synchronisation ?"
  - "Que se passe-t-il concrètement pour le fichier original stocké à l'Université Simon-Fraser lorsqu'il est modifié via WebDAV ?"
  - "Comment procéder pour partager un fichier ou un répertoire avec un autre utilisateur dans CCDB ?"
  - "Quelles informations spécifiques peut-on utiliser pour rechercher le destinataire du partage ?"
  - "Pourquoi est-il conseillé de privilégier le nom d'utilisateur lors de la recherche d'une personne ?"
  - "Quels types de groupes CCDB sont configurés par défaut pour permettre le partage avec leurs membres ?"
  - "Quelle option permet de partager des fichiers avec des personnes ne possédant pas de compte avec l'Alliance ?"
  - "Comment le système Nextcloud informe-t-il les utilisateurs externes qu'un lien d'accès leur a été partagé ?"
  - "Quels types de groupes CCDB sont configurés par défaut pour permettre le partage avec leurs membres ?"
  - "Quelle option permet de partager des fichiers avec des personnes ne possédant pas de compte avec l'Alliance ?"
  - "Comment le système Nextcloud informe-t-il les utilisateurs externes qu'un lien d'accès leur a été partagé ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le service Nextcloud permet le stockage et le partage de données à la manière de Dropbox. Pour [se connecter au serveur](https://nextcloud.computecanada.ca/), utilisez le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pouvez consulter le [manuel de l'utilisateur](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et la [documentation Nextcloud en ligne](https://docs.nextcloud.com/). Une fois la connexion établie, un autre document PDF est aussi disponible via votre compte. Les données entre les ordinateurs locaux et notre service Nextcloud sont toutes chiffrées.

!!! note "Limite de stockage"
    Le service Nextcloud est conçu pour les ensembles de données relativement modestes (jusqu'à 100 Go). Pour les grands ensembles de données, nous recommandons [Globus](../getting-started/globus.md).

Pour vous familiariser avec le service, voyez [la démo sur le site web de Nextcloud](https://try.nextcloud.com/).

!!! tip "Gestion de vos données"
    Profitez de l'occasion pour mettre de l'ordre dans vos dossiers, éliminer les données dont vous n'avez plus besoin ou vérifier les personnes avec qui vos données sont partagées.

## Description

*   **URL du serveur :** https://nextcloud.computecanada.ca
*   **Localisation :** Université Simon-Fraser, Burnaby, CB
*   **Quota fixe :** 100 Go par utilisateur
*   **Sauvegarde des données :** une fois par jour; aucune copie sur support externe
*   **Méthodes d'accès :** interface web, client Nextcloud de synchronisation pour poste de travail, applications mobiles Nextcloud, tout client WebDAV
*   **Documentation :** [manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et [documentation en ligne](https://docs.nextcloud.com/).

## Interface web Nextcloud

Pour utiliser l'interface web, connectez-vous à [Nextcloud](https://nextcloud.computecanada.ca) via un navigateur avec le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pourrez télécharger et téléverser des fichiers entre Nextcloud et votre appareil mobile ou votre ordinateur, ou encore modifier et partager des fichiers avec d'autres utilisateurs. Pour plus d'information, consultez le [manuel de l'utilisateur](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

## Client de synchronisation pour poste de travail et applications mobiles Nextcloud

Vous pouvez [télécharger le client de synchronisation Nextcloud pour poste de travail ou les applications mobiles Nextcloud](https://nextcloud.com/install/) pour synchroniser les données en provenance respectivement de votre ordinateur ou de votre appareil mobile. Une fois installé sur votre poste de travail, le client synchronise le contenu de votre répertoire Nextcloud avec le contenu du répertoire sur votre local. Sachez cependant que cette opération peut prendre un certain temps. Vous pouvez modifier les fichiers localement et ils seront automatiquement mis à jour dans Nextcloud.

## Clients WebDAV

De façon générale, tous les clients WebDAV vous permettront de monter un répertoire Nextcloud sur votre ordinateur en passant par https://nextcloud.computecanada.ca/remote.php/webdav/.

Vous pourrez ensuite glisser-déplacer des fichiers entre le lecteur WebDAV et votre ordinateur local.

**macOS :** Sélectionnez *Aller -> Se connecter au serveur*, entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Adresse du serveur* et cliquez sur *Connecter*. Vous devez ensuite entrer votre nom d'utilisateur et votre mot de passe pour vous connecter. Après l'authentification, un lecteur WebDAV sera présent sur votre Mac.

**Windows :** Avec l'option *Connecter un lecteur réseau*, sélectionnez un lecteur et entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Dossier*.

Vous pouvez aussi utiliser tout autre client, par exemple [Cyberduck](https://cyberduck.io/) qui est disponible pour macOS et Windows.

**Linux :** Plusieurs applications WebDAV sont disponibles; voyez les recommandations dans le [manuel de l'utilisateur](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

### Comparaison entre WebDAV et le client de synchronisation

Les clients WebDAV montent votre stockage Nextcloud sur votre ordinateur. Les fichiers ne sont pas copiés, c'est-à-dire que quand vous modifiez un fichier, ce qui est modifié en fait c'est le fichier original enregistré dans le système Nextcloud situé à l'Université Simon-Fraser.

Quand vous vous connectez avec le client de synchronisation Nextcloud, le client commence par synchroniser vos fichiers sur Nextcloud avec une copie des fichiers sur votre ordinateur. Les fichiers qui sont différents sont téléchargés sur votre propre client. Les fichiers modifiés sont recopiés sur tous les systèmes synchronisés pour qu'ils soient identiques partout. La copie peut prendre beaucoup de temps si vous et/ou vos collaborateurs modifiez fréquemment les fichiers. Ici, l'avantage est que vous pouvez travailler sans être connecté au serveur et que la prochaine fois que vous vous connectez, les fichiers seront synchronisés.

## Outils en ligne de commande UNIX

Vous pouvez utiliser tous les clients en ligne de commande WebDAV qui vous sont disponibles, par exemple [curl](https://curl.haxx.se/) et [cadaver](http://www.webdav.org/cadaver/) pour copier les fichiers entre votre poste de travail et Nextcloud. Les outils en ligne de commande sont utiles pour copier des données entre Nextcloud et un serveur auquel vous vous connectez.

`curl` est habituellement installé sur macOS et les systèmes Linux; il peut être utilisé pour télécharger et téléverser des fichiers avec une adresse URL.

### Téléverser un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> -T <nom_de_fichier> https://nextcloud.computecanada.ca/remote.php/webdav/
```

### Télécharger un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> https://nextcloud.computecanada.ca/remote.php/webdav/<nom_de_fichier> -o <nom_de_fichier>
```

### Téléverser ou télécharger un fichier avec `rclone`

Contrairement à [curl](https://curl.haxx.se/), [rclone](https://rclone.org) permet de créer une configuration une seule fois pour chaque service de stockage et d'utiliser cette configuration à plusieurs reprises sans devoir entrer chaque fois les détails de l'hôte et votre mot de passe. Le mot de passe est crypté et enregistré sur l'ordinateur ou le serveur où la commande `~/.config/rclone/rclone.conf` est utilisée.

D'abord, [installez rclone sur votre ordinateur](https://rclone.org/install/) si l'environnement est semblable à Unix.

Si vous utilisez une de nos grappes, rclone est disponible et n'a pas besoin d'être installé.

```bash
$ [nom@serveur ~] $ which rclone
$ /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/rclone
```

Configurez ensuite un service distant avec la commande

```bash
$ rclone config
```

Vous avez ici l'option de modifier un service existant et de créer ou supprimer un service distant. Dans notre exemple, nous créons un profil de service nommé *nextcloud*.

```bash
choose "n"  for "New remote"
Enter name for new remote --> nextcloud
Type of storage to configure --> 52 / WebDAV
URL of http host to connect to --> https://nextcloud.computecanada.ca/remote.php/dav/files/<votre_nom_utilisateur_CCDB>
Name of the WebDAV site/service/software you are using --> 2 / Nextcloud
User name --> <votre_nom_utilisateur_CCDB>
choose "y" for "Option pass"
Password --> <votre_mot_de_passe_CCDB>
Leave "Option bearer_token" empty
choose "no" for "Edit advanced config"
choose "yes" for "Keep this 'nextcloud' remote"
choose "q" to quit config
```

Votre nouveau profil de service distant devrait maintenant se trouver dans la liste des profils configurés; pour vérifier, lancez

```bash
$ rclone listremotes
```

Pour connaître l'espace disque disponible, utilisez

```bash
$ rclone about nextcloud:
```

Pour téléverser un fichier, utilisez

```bash
$ rclone copy /chemin/local/vers/le/fichier nextcloud:chemin/distant
```

Pour télécharger un fichier, utilisez

```bash
$ rclone copy nextcloud:chemin/distant/fichier .
```

## Partager des fichiers

Quand vous sélectionnez un fichier ou un répertoire que vous voulez partager avec un autre utilisateur enregistré dans CCDB, entrez le prénom, le nom ou le nom d’utilisateur de cette personne et la liste des utilisateurs correspondants sera affichée. Prenez soin d’entrer ces renseignements correctement car plusieurs noms sont semblables; en cas de doute, entrez le nom d’utilisateur qui est unique à chaque personne.

Vous pouvez aussi entrer le nom d’un groupe CCDB (par défaut, plateformes et portails de recherche, groupes de recherche et autres groupes où le partage est configuré) pour partager avec ses membres.

L’option *Lien de partage* permet aussi de partager avec des personnes qui n’ont pas de compte avec l'Alliance; Nextcloud leur fait parvenir une notification avec le lien pour accéder au fichier.