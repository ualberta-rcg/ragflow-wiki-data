---
title: "Nextcloud/fr"
slug: "nextcloud"
lang: "fr"

source_wiki_title: "Nextcloud/fr"
source_hash: "6c861915213d492e202c954979da2b5f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:13:40.487296+00:00"

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

Le service Nextcloud permet le stockage et le partage de données à la manière de Dropbox. Pour vous [connecter au serveur Nextcloud](https://nextcloud.computecanada.ca/), utilisez le nom d'utilisateur et le mot de passe de votre compte de l'Alliance. Vous pouvez consulter le [manuel de l'utilisateur Nextcloud (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et la [documentation Nextcloud en ligne](https://docs.nextcloud.com/). Une fois la connexion établie, un autre document PDF est aussi disponible via votre compte. Les données entre les ordinateurs locaux et notre service Nextcloud sont toutes chiffrées.

Le service Nextcloud est conçu pour les ensembles de données relativement modestes (jusqu'à 100 Go). Pour les grands ensembles de données, nous recommandons [Globus](globus.md).

Pour vous familiariser avec le service, voyez la [démo sur le site web de Nextcloud](https://try.nextcloud.com/).

!!! tip "Conseil"
    Profitez donc de l'occasion pour mettre de l'ordre dans vos dossiers, éliminer les données dont vous n'avez plus besoin ou vérifier les personnes avec qui vos données sont partagées.

## Description

*   **URL du serveur :** https://nextcloud.computecanada.ca
*   **Localisation :** Université Simon-Fraser, Burnaby, CB
*   **Quota fixe :** 100 Go par utilisateur
*   **Sauvegarde des données :** une fois par jour; aucune copie sur support externe
*   **Méthodes d'accès :** interface web, client de synchronisation Nextcloud Desktop, applications mobiles Nextcloud, tout client WebDAV
*   **Documentation :** [manuel de l'utilisateur (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et [documentation en ligne](https://docs.nextcloud.com/).

## Interface web Nextcloud

Pour utiliser l'interface web, connectez-vous à [Nextcloud](https://nextcloud.computecanada.ca) via un navigateur avec le nom d'utilisateur et le mot de passe de votre compte de l'Alliance. Vous pourrez télécharger et téléverser des fichiers entre Nextcloud et votre appareil mobile ou votre ordinateur, ou encore modifier et partager des fichiers avec d'autres utilisateurs. Pour plus d'information, consultez le [manuel de l'utilisateur](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

## Client de synchronisation Desktop et applications mobiles Nextcloud

Vous pouvez [télécharger le client de synchronisation Nextcloud Desktop ou les applications mobiles Nextcloud](https://nextcloud.com/install/) pour synchroniser les données de votre ordinateur ou de votre appareil mobile. Une fois installé sur votre poste de travail, le client synchronise le contenu de votre répertoire Nextcloud avec le contenu du répertoire sur votre machine locale. Sachez cependant que cette opération peut prendre un certain temps. Vous pouvez modifier les fichiers localement et ils seront automatiquement mis à jour dans Nextcloud.

## Clients WebDAV

De façon générale, tous les clients WebDAV vous permettront de monter un répertoire Nextcloud sur votre ordinateur en passant par https://nextcloud.computecanada.ca/remote.php/webdav/.

Vous pourrez ensuite glisser-déplacer des fichiers entre le lecteur WebDAV et votre ordinateur local.

**Mac OSX :** Sélectionnez *Aller -> Se connecter au serveur*, entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Adresse du serveur* et cliquez sur *Se connecter*. Vous devez ensuite entrer votre nom d'utilisateur et votre mot de passe pour vous connecter. Après l'authentification, un lecteur WebDAV sera présent sur votre Mac.

**Windows :** Avec l'option *Connecter un lecteur réseau*, sélectionnez un lecteur et entrez https://nextcloud.computecanada.ca/remote.php/webdav/ dans le champ *Dossier*.

Vous pouvez aussi utiliser tout autre client, par exemple [Cyberduck](https://cyberduck.io/), qui est disponible pour OSX et Windows.

**Linux :** Plusieurs applications WebDAV sont disponibles; voyez les recommandations dans le [manuel de l'utilisateur](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

### Comparaison entre WebDAV et le client de synchronisation

Les clients WebDAV montent votre stockage Nextcloud sur votre ordinateur. Les fichiers ne sont pas copiés, c'est-à-dire que quand vous modifiez un fichier, ce qui est modifié en fait c'est le fichier original enregistré dans le système Nextcloud situé à l'Université Simon-Fraser.

Quand vous vous connectez avec le client de synchronisation Nextcloud, le client commence par synchroniser vos fichiers sur Nextcloud avec une copie des fichiers sur votre ordinateur. Les fichiers qui sont différents sont téléchargés sur votre propre client. Les fichiers modifiés sont recopiés sur tous les systèmes synchronisés pour qu'ils soient identiques partout. La copie peut prendre beaucoup de temps si vous et/ou vos collaborateurs modifiez fréquemment les fichiers. Ici, l'avantage est que vous pouvez travailler sans être connecté au serveur et que la prochaine fois que vous vous connectez, les fichiers seront synchronisés.

## Outils en ligne de commande UNIX

Vous pouvez utiliser tous les clients WebDAV en ligne de commande qui vous sont disponibles, par exemple [curl](https://curl.haxx.se/) et [cadaver](http://www.webdav.org/cadaver/) pour copier les fichiers entre votre poste de travail et Nextcloud. Les outils en ligne de commande sont utiles pour copier des données entre Nextcloud et un serveur auquel vous vous connectez.

`curl` est habituellement installé sur Mac OSX et les systèmes Linux; il peut être utilisé pour télécharger et téléverser des fichiers avec une adresse URL.

### Téléverser un fichier avec `curl`

```bash
curl -k -u <username> -T <filename> https://nextcloud.computecanada.ca/remote.php/webdav/
```

### Télécharger un fichier avec `curl`

```bash
curl -k -u <username> https://nextcloud.computecanada.ca/remote.php/webdav/<filename> -o <filename>
```

### Téléverser ou télécharger un fichier avec `rclone`

Contrairement à [curl](https://curl.haxx.se/), [rclone](https://rclone.org) permet de créer une configuration une seule fois pour chaque service de stockage et d'utiliser cette configuration à plusieurs reprises sans devoir entrer chaque fois les détails de l'hôte et votre mot de passe. Le mot de passe est crypté et enregistré sur l'ordinateur ou le serveur où la commande `~/.config/rclone/rclone.conf` est utilisée.

D'abord, [installez rclone sur votre ordinateur](https://rclone.org/install/) si l'environnement est semblable à Unix.

Si vous utilisez une de nos grappes, rclone est disponible et n'a pas besoin d'être installé.

```bash
$ [name@server ~] $ which rclone
$ /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/rclone
```

Configurez ensuite un service distant avec la commande :

```bash
$ rclone config
```

Vous avez ici l'option de modifier un service existant et de créer ou supprimer un service distant. Dans notre exemple, nous créons un profil de service nommé *nextcloud*.

```bash
choose "n" for "Nouveau dépôt distant"
Entrez un nom pour le nouveau dépôt distant --> nextcloud
Type de stockage à configurer --> 52 / WebDAV
URL de l'hôte http auquel se connecter --> https://nextcloud.computecanada.ca/remote.php/dav/files/<votre nom d'utilisateur CCDB>
Nom du site/service/logiciel WebDAV que vous utilisez --> 2 / Nextcloud
Nom d'utilisateur --> <votre nom d'utilisateur CCDB>
choose "y" for "Option mot de passe"
Mot de passe --> <votre mot de passe CCDB>
Laisser "Option jeton de support" vide
choose "no" for "Modifier la configuration avancée"
choose "yes" for "Garder ce dépôt distant 'nextcloud'"
choose "q" pour quitter la configuration
```

Votre nouveau profil de service distant devrait maintenant se trouver dans la liste des profils configurés; pour vérifier, lancez la commande :

```bash
$ rclone listremotes
```

Pour connaître l'espace disque disponible, utilisez :

```bash
$ rclone about nextcloud:
```

Pour téléverser un fichier, utilisez :

```bash
$ rclone copy /chemin/vers/fichier/local nextcloud:chemin/distant
```

Pour télécharger un fichier, utilisez :

```bash
$ rclone copy nextcloud:chemin/distant/fichier .
```

## Partager des fichiers

Quand vous sélectionnez un fichier ou un répertoire que vous voulez partager avec un autre utilisateur enregistré dans CCDB, entrez le prénom, le nom ou le nom d’utilisateur de cette personne et la liste des utilisateurs correspondants sera affichée. Prenez soin d’entrer ces renseignements correctement car plusieurs noms sont semblables; en cas de doute, entrez le nom d’utilisateur qui est unique à chaque personne.

Vous pouvez aussi entrer le nom d’un groupe CCDB (par défaut, plateformes et portails de recherche, groupes de recherche et autres groupes où le partage est configuré) pour partager avec ses membres.

L’option *Partager le lien* permet aussi de partager avec des personnes qui n’ont pas de compte avec l'Alliance; Nextcloud leur fait parvenir une notification avec le lien pour accéder au fichier.