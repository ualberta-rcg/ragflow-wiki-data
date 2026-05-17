---
title: "Nextcloud/fr"
slug: "nextcloud"
lang: "fr"

source_wiki_title: "Nextcloud/fr"
source_hash: "02403773713aeb12f0fa5b7729c825c5"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:27:54.151282+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: true
---

Le service Nextcloud permet le stockage et le partage de données à la manière de Dropbox. Pour vous [connecter au serveur](https://nextcloud.computecanada.ca/), utilisez le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pouvez consulter le [Manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et la [documentation Nextcloud en ligne](https://docs.nextcloud.com/). Une fois la connexion établie, un autre document PDF est aussi disponible via votre compte. Les données entre les ordinateurs locaux et notre service Nextcloud sont toutes chiffrées.

!!! note "Ensembles de données"
    Le service Nextcloud est conçu pour les ensembles de données relativement modestes (jusqu'à 100 Go). Pour les grands ensembles de données, nous recommandons [Globus](../getting-started/globus.md).

Pour vous familiariser avec le service, voyez [la démo sur le site web de Nextcloud](https://try.nextcloud.com/).

Profitez donc de l'occasion pour mettre de l'ordre dans vos dossiers, éliminer les données dont vous n'avez plus besoin ou vérifier les personnes avec qui vos données sont partagées.

## Description

*   **URL du serveur :** https://nextcloud.computecanada.ca
*   **Localisation :** Université Simon-Fraser, Burnaby, CB
*   **Quota fixe :** 100 Go par utilisateur
*   **Sauvegarde des données :** une fois par jour; aucune copie sur support externe
*   **Méthodes d'accès :** interface web, client de synchronisation de bureau Nextcloud, applications mobiles Nextcloud, tout client WebDAV
*   **Documentation :** [manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et [documentation en ligne](https://docs.nextcloud.com/).

## Description du service Nextcloud de SHARCNET

Nextcloud est un service de stockage et de partage de fichiers basé sur le web, similaire à OneDrive, Google Drive ou Dropbox, mais hébergé de manière sécurisée sur l'infrastructure de l'Alliance. Il vous permet de stocker, d'accéder et de partager vos fichiers de recherche depuis n'importe quel appareil via un navigateur ou un client de bureau. Il peut également être monté directement sur la grappe Nibi, vous permettant d'accéder à vos fichiers sans avoir à les transférer manuellement. Les utilisateurs se voient allouer 100 Go par défaut; les chercheurs nécessitant un stockage supplémentaire peuvent soumettre une demande d'augmentation de quota.

*   **URL :** https://nextcloud.sharcnet.ca/
*   **Stockage :** 100 Go par utilisateur
*   **Emplacement :** Université de Waterloo, Waterloo, ON
*   **Sauvegardes :** Quotidiennes sur bibliothèque de bandes
*   **Accès :** Web, poste de travail, mobile, grappe Nibi (Rclone-WebDAV)
*   **Documentation :** https://helpwiki.sharcnet.ca/wiki/Nextcloud_User_Guide

## Interface web Nextcloud

Pour utiliser l'interface web, connectez-vous à [Nextcloud](https://nextcloud.computecanada.ca) via un navigateur avec le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pourrez télécharger et téléverser des fichiers entre Nextcloud et votre appareil mobile ou votre ordinateur, ou encore modifier et partager des fichiers avec d'autres utilisateurs. Pour plus d'information, consultez le [Manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

## Client de synchronisation de bureau et applications mobiles Nextcloud

Vous pouvez [télécharger le client de synchronisation de bureau Nextcloud ou les applications mobiles Nextcloud](https://nextcloud.com/install/) pour synchroniser les données en provenance respectivement de votre ordinateur ou de votre appareil mobile. Une fois installé sur votre poste de travail, le client synchronise le contenu de votre répertoire Nextcloud avec le contenu du répertoire sur votre local. Sachez cependant que cette opération peut prendre un certain temps. Vous pouvez modifier les fichiers localement et ils seront automatiquement mis à jour dans Nextcloud.

## Clients WebDAV

De façon générale, tous les clients WebDAV vous permettront de monter un répertoire Nextcloud sur votre ordinateur en passant par https://nextcloud.computecanada.ca/remote.php/webdav/.

Vous pourrez ensuite glisser-déplacer des fichiers entre le lecteur WebDAV et votre ordinateur local.

**Mac OSX :** Sélectionnez *Aller -> Se connecter au serveur*, entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Adresse du serveur* et cliquez sur *Connecter*. Vous devez ensuite entrer votre nom d'utilisateur et votre mot de passe pour vous connecter. Après l'authentification, un lecteur WebDAV sera présent sur votre Mac.

**Windows :** Avec l'option *Connecter un lecteur réseau*, sélectionnez un lecteur et entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Dossier*.

Vous pouvez aussi utiliser tout autre client, par exemple [Cyberduck](https://cyberduck.io/) qui est disponible pour OSX et Windows.

**Linux :** Plusieurs applications WebDAV sont disponibles; voyez les recommandations dans le [Manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

### Comparaison entre WebDAV et le client de synchronisation

Les clients WebDAV montent votre stockage Nextcloud sur votre ordinateur. Les fichiers ne sont pas copiés, c'est-à-dire que quand vous modifiez un fichier, ce qui est modifié en fait c'est le fichier original enregistré dans le système Nextcloud situé à l'Université Simon-Fraser.

Quand vous vous connectez avec le client de synchronisation Nextcloud, le client commence par synchroniser vos fichiers sur Nextcloud avec une copie des fichiers sur votre ordinateur. Les fichiers qui sont différents sont téléchargés sur votre propre client. Les fichiers modifiés sont recopiés sur tous les systèmes synchronisés pour qu'ils soient identiques partout. La copie peut prendre beaucoup de temps si vous et/ou vos collaborateurs modifiez fréquemment les fichiers. Ici, l'avantage est que vous pouvez travailler sans être connecté au serveur et que la prochaine fois que vous vous connectez, les fichiers seront synchronisés.

## Outils en ligne de commande UNIX

Vous pouvez utiliser tous les clients en ligne de commande WebDAV qui vous sont disponibles, par exemple [curl](https://curl.haxx.se/) et [cadaver](http://www.webdav.org/cadaver/) pour copier les fichiers entre votre poste de travail et Nextcloud. Les outils en ligne de commande sont utiles pour copier des données entre Nextcloud et un serveur auquel vous vous connectez.

`curl` est habituellement installé sur Mac OSX et les systèmes Linux; il peut être utilisé pour télécharger et téléverser des fichiers avec une adresse URL.

### Téléverser un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> -T <nom_fichier> https://nextcloud.computecanada.ca/remote.php/webdav/
```

### Télécharger un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> https://nextcloud.computecanada.ca/remote.php/webdav/<nom_fichier> -o <nom_fichier>
```

### Téléverser ou télécharger un fichier avec `rclone`

Contrairement à [curl](https://curl.haxx.se/), [rclone](https://rclone.org) permet de créer une configuration une seule fois pour chaque service de stockage et d'utiliser cette configuration à plusieurs reprises sans devoir entrer chaque fois les détails de l'hôte et votre mot de passe. Le mot de passe est crypté et enregistré sur l'ordinateur ou le serveur où la commande `` `~/.config/rclone/rclone.conf` `` est utilisée.

D'abord, [installez rclone sur votre ordinateur](https://rclone.org/install/) si l'environnement est semblable à Unix.

Si vous utilisez une de nos grappes, rclone est disponible et n'a pas besoin d'être installé.

```text
$ [nom@serveur ~] $ which rclone
/cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/rclone
```

Configurez ensuite un service distant avec la commande

```bash
rclone config
```

Vous avez ici l'option de modifier un service existant et de créer ou supprimer un service distant. Dans notre exemple, nous créons un profil de service nommé *nextcloud*.

```text
choose "n"  for "New remote"
Enter name for new remote --> nextcloud
Type of storage to configure --> 52 / WebDAV
URL of http host to connect to --> https://nextcloud.computecanada.ca/remote.php/dav/files/<votre nom d'utilisateur CCDB>
Name of the WebDAV site/service/software you are using --> 2 / Nextcloud
User name --> <votre nom d'utilisateur CCDB>
choose "y" for "Option pass"
Password --> <votre mot de passe CCDB>
Leave "Option bearer_token" empty
choose "no" for "Edit advanced config"
choose "yes" for "Keep this 'nextcloud' remote"
choose "q" to quit config
```

Votre nouveau profil de service distant devrait maintenant se trouver dans la liste des profils configurés; pour vérifier, lancez

```bash
rclone listremotes
```

Pour connaître l'espace disque disponible, utilisez

```bash
rclone about nextcloud:
```

Pour téléverser un fichier, utilisez

```bash
rclone copy /chemin/vers/fichier/local nextcloud:chemin/distant
```

Pour télécharger un fichier, utilisez

```bash
rclone copy nextcloud:chemin/distant/fichier .
```

## Partager des fichiers

Quand vous sélectionnez un fichier ou un répertoire que vous voulez partager avec un autre utilisateur enregistré dans CCDB, entrez le prénom, le nom ou le nom d’utilisateur de cette personne et la liste des utilisateurs correspondants sera affichée. Prenez soin d’entrer ces renseignements correctement car plusieurs noms sont semblables; en cas de doute, entrez le nom d’utilisateur qui est unique à chaque personne.
 
Vous pouvez aussi entrer le nom d’un groupe CCDB (par défaut, plateformes et portails de recherche, groupes de recherche et autres groupes où le partage est configuré) pour partager avec ses membres.
 
L’option *Lien de partage* permet aussi de partager avec des personnes qui n’ont pas de compte avec l'Alliance; Nextcloud leur fait parvenir une notification avec le lien pour accéder au fichier.