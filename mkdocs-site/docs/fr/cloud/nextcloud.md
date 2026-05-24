---
title: "Nextcloud/fr"
slug: "nextcloud"
lang: "fr"

source_wiki_title: "Nextcloud/fr"
source_hash: "e2eec68036d59f5bb7cd4e41283b2fe9"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:46:30.117933+00:00"

tags:
  []

keywords:
  - "fichiers"
  - "installation"
  - "service distant"
  - "Clients WebDAV"
  - "synchronisation"
  - "configuration"
  - "Nextcloud Alliance"
  - "partager des fichiers"
  - "CCDB"
  - "serveur"
  - "Outils ligne de commande"
  - "Client de synchronisation"
  - "partage de données"
  - "Nextcloud"
  - "client"
  - "rclone"
  - "répertoire local"
  - "Nextcloud SHARCNET"
  - "mot de passe crypté"
  - "stockage de données"

questions:
  - "Quelle est la limite de stockage par défaut du service Nextcloud et quelle solution est recommandée pour les données plus volumineuses ?"
  - "Quelles sont les différentes méthodes d'accès permettant de consulter et de synchroniser ses fichiers sur Nextcloud ?"
  - "Quelles sont les principales différences entre les serveurs Nextcloud de l'Alliance et de SHARCNET, notamment en matière de sauvegarde et d'intégration ?"
  - "Comment configurer un client WebDAV sur différents systèmes d'exploitation pour accéder à Nextcloud ?"
  - "Quelle est la différence principale entre l'utilisation d'un client WebDAV et celle d'un client de synchronisation Nextcloud ?"
  - "Quels outils en ligne de commande UNIX peuvent être utilisés pour transférer des fichiers avec Nextcloud et comment les utiliser ?"
  - "Quel est le rôle du client Nextcloud une fois qu'il est installé sur le poste de travail ?"
  - "Que faut-il prendre en compte concernant la durée de l'opération de synchronisation ?"
  - "Comment le système gère-t-il les modifications apportées localement aux fichiers ?"
  - "Où le fichier de configuration contenant le mot de passe crypté est-il sauvegardé ?"
  - "Quelle est la démarche à suivre pour installer rclone sur un ordinateur avec un environnement semblable à Unix ?"
  - "Dans quel cas spécifique l'installation de rclone n'est-elle pas nécessaire ?"
  - "Comment configurer un nouveau profil de service distant pour Nextcloud à l'aide de la commande rclone ?"
  - "Quelles commandes rclone doit-on utiliser pour vérifier l'espace disque, téléverser et télécharger des fichiers ?"
  - "Quelles sont les options disponibles dans Nextcloud pour partager des fichiers avec des utilisateurs possédant ou non un compte CCDB ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le service Nextcloud permet le stockage et le partage de données à la manière de Dropbox. Pour [vous connecter au serveur](https://nextcloud.computecanada.ca/), utilisez le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pouvez consulter le [manuel d'utilisation Nextcloud (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et la [documentation Nextcloud en ligne](https://docs.nextcloud.com/). Une fois la connexion établie, un autre document PDF est disponible via votre compte. Les données entre les ordinateurs locaux et notre service Nextcloud sont toutes chiffrées.

Le service Nextcloud est conçu pour les ensembles de données relativement modestes (jusqu'à 100 Go). Si vous avez besoin de plus d'options de stockage, voir [Nextcloud SHARCNET](#nextcloud-sharcnet) ci-dessous. Pour les grands ensembles de données, nous recommandons [Globus](../getting-started/globus.md).

Pour vous familiariser avec le service, voyez [la démo sur le site web de Nextcloud](https://try.nextcloud.com/).

Profitez de l'occasion pour mettre de l'ordre dans vos dossiers, éliminer les données dont vous n'avez plus besoin, vérifier les personnes avec qui vos données sont partagées, etc.

## Nextcloud Alliance

*   **URL du serveur :** https://nextcloud.computecanada.ca
*   **Localisation du serveur :** Université Simon-Fraser, Burnaby, C.-B.
*   **Quota fixe :** 100 Go par utilisateur
*   **Sauvegarde des données :** une fois par jour; aucune copie sur support externe
*   **Méthodes d'accès :** interface web, client de synchronisation de bureau Nextcloud, applications mobiles Nextcloud, tout client WebDAV
*   **Documentation :** [manuel d'utilisation Nextcloud (PDF)](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf) et [la documentation en ligne](https://docs.nextcloud.com/).

## Nextcloud SHARCNET
Le Nextcloud SHARCNET peut être monté directement sur la grappe Nibi, permettant ainsi l'accès à vos fichiers sans avoir à les transférer manuellement. Par défaut, vous disposez de 100 Go; pour obtenir un quota plus élevé, écrivez à [help@sharcnet.ca](mailto:help@sharcnet.ca). Pour plus d'information, consultez [le manuel d'utilisation Nextcloud de SHARCNET](https://helpwiki.sharcnet.ca/wiki/Nextcloud_User_Guide).
*   **URL du serveur** : https://nextcloud.sharcnet.ca/
*   **Localisation du serveur** : Université de Waterloo, Waterloo, Ont.
*   **Quota fixe** : 100 Go par utilisateur
*   **Sauvegarde des données** : une fois par jour, sur ruban
*   **Méthodes d'accès :** interface web, client de synchronisation de bureau Nextcloud, applications mobiles Nextcloud, tout client WebDAV
*   **Documentation** : [manuel d'utilisation Nextcloud de SHARCNET](https://helpwiki.sharcnet.ca/wiki/Nextcloud_User_Guide)

## Interface web Nextcloud

Pour utiliser l'interface web, connectez-vous à [Nextcloud](https://nextcloud.computecanada.ca/) via un navigateur avec le nom d'utilisateur et le mot de passe de votre compte avec l'Alliance. Vous pourrez télécharger et téléverser des fichiers entre Nextcloud et votre appareil mobile ou votre ordinateur, ou encore modifier et partager des fichiers avec d'autres utilisateurs. Pour plus d'information, consultez le [manuel d'utilisation](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

## Client de synchronisation de bureau et applications mobiles Nextcloud

Vous pouvez [télécharger le client de synchronisation de bureau Nextcloud ou les applications mobiles Nextcloud](https://nextcloud.com/install/) pour synchroniser les données en provenance respectivement de votre ordinateur ou de votre appareil mobile. Une fois installé sur votre poste de travail, le client synchronise le contenu de votre répertoire Nextcloud avec le contenu du répertoire local. Sachez cependant que cette opération peut prendre un certain temps. Vous pouvez modifier les fichiers localement et ils seront automatiquement mis à jour dans Nextcloud.

## Clients WebDAV

De façon générale, tous les clients WebDAV vous permettront de monter un répertoire Nextcloud sur votre ordinateur en passant par `https://nextcloud.computecanada.ca/remote.php/webdav/`.

Vous pourrez ensuite glisser-déplacer des fichiers entre le lecteur WebDAV et votre ordinateur local.

*   **macOS :** Sélectionnez *Aller -> Se connecter au serveur*, entrez `https://nextcloud.computecanada.ca/remote.php/webdav/` dans le champ *Adresse du serveur* et cliquez sur *Connecter*. Vous devez ensuite entrer votre nom d'utilisateur et votre mot de passe pour vous connecter. Après l'authentification, un lecteur WebDAV sera présent sur votre Mac.

*   **Windows :** Avec l'option *Connecter un lecteur réseau*, sélectionnez un lecteur et entrez `https://nextcloud.computecanada.ca/remote.php/webdav/` dans le champ *Dossier*.

Vous pouvez aussi utiliser tout autre client, par exemple [Cyberduck](https://cyberduck.io/) qui est disponible pour macOS et Windows.

*   **Linux :** Plusieurs applications WebDAV sont disponibles; voyez les recommandations dans le [manuel d'utilisation](https://docs.nextcloud.com/server/19/Nextcloud_User_Manual.pdf).

### Comparaison entre client WebDAV et client de synchronisation

Les clients WebDAV montent votre stockage Nextcloud sur votre ordinateur. Les fichiers ne sont pas copiés, c'est-à-dire que quand vous modifiez un fichier, ce qui est modifié en fait c'est le fichier original enregistré dans le système Nextcloud situé à l'Université Simon-Fraser.

Quand vous vous connectez avec le client de synchronisation Nextcloud, le client commence par synchroniser vos fichiers sur Nextcloud avec une copie des fichiers sur votre ordinateur. Les fichiers qui sont différents sont téléchargés sur votre propre client. Les fichiers modifiés sont recopiés sur tous les systèmes synchronisés pour qu'ils soient identiques partout. La copie peut prendre beaucoup de temps si vous et/ou vos collaborateurs modifiez fréquemment les fichiers. Ici, l'avantage est que vous pouvez travailler sans être connecté au serveur et que la prochaine fois que vous vous connectez, les fichiers seront synchronisés.

## Outils en ligne de commande Unix

Vous pouvez utiliser tous les clients en ligne de commande WebDAV qui vous sont disponibles, par exemple [curl](https://curl.haxx.se/) et [cadaver](http://www.webdav.org/cadaver/) pour copier les fichiers entre votre poste de travail et Nextcloud. Les outils en ligne de commande sont utiles pour copier des données entre Nextcloud et un serveur auquel vous vous connectez.

`curl` est habituellement installé sur macOS et les systèmes Linux; il peut être utilisé pour télécharger et téléverser des fichiers avec une adresse URL.

### Téléverser un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> -T <nom_fichier> https://nextcloud.computecanada.ca/remote.php/webdav/
```

### Télécharger un fichier avec `curl`

```bash
curl -k -u <nom_utilisateur> https://nextcloud.computecanada.ca/remote.php/webdav/<nom_fichier> -o <nom_fichier>
```

### Téléverser ou télécharger un fichier avec `rclone`

Contrairement à [curl](https://curl.haxx.se/), [rclone](https://rclone.org) permet de créer une configuration une seule fois pour chaque service de stockage et d'utiliser cette configuration à plusieurs reprises sans devoir entrer chaque fois les détails de l'hôte et votre mot de passe. Le mot de passe est crypté et enregistré sur l'ordinateur ou le serveur où la commande `~/.config/rclone/rclone.conf` est utilisée.

D'abord, [installez rclone sur votre ordinateur](https://rclone.org/install/) si l'environnement est semblable à Unix.

Si vous utilisez une de nos grappes, `rclone` est disponible et n'a pas besoin d'être installé.

```bash
$ [nom_utilisateur@serveur ~]$ which rclone
$ /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/rclone
```

Configurez ensuite un service distant avec la commande

```bash
$ rclone config
```

Vous avez ici l'option de modifier un service existant et de créer ou supprimer un service distant. Dans notre exemple, nous créons un profil de service nommé *nextcloud*.

```
# Choisissez "n" pour "New remote" (Nouveau service distant)
n
# Entrez le nom du nouveau service distant
nextcloud
# Type de stockage à configurer --> 52 / WebDAV
52
# URL de l'hôte http auquel se connecter
https://nextcloud.computecanada.ca/remote.php/dav/files/<votre_nom_utilisateur_CCDB>
# Nom du site/service/logiciel WebDAV que vous utilisez --> 2 / Nextcloud
2
# Nom d'utilisateur
<votre_nom_utilisateur_CCDB>
# Choisissez "y" pour l'option de mot de passe
y
# Mot de passe
<votre_mot_de_passe_CCDB>
# Laissez "Option bearer_token" vide
# Choisissez "no" pour "Edit advanced config" (Modifier la configuration avancée)
no
# Choisissez "yes" pour "Keep this 'nextcloud' remote" (Garder ce service distant 'nextcloud')
yes
# Choisissez "q" pour quitter la configuration
q
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
$ rclone copy /chemin/vers/fichier/local nextcloud:chemin/distant
```

Pour télécharger un fichier, utilisez

```bash
$ rclone copy nextcloud:chemin/distant/fichier .
```

## Partager des fichiers

Quand vous sélectionnez un fichier ou un répertoire que vous voulez partager avec un autre utilisateur enregistré dans CCDB, entrez le prénom, le nom ou le nom d’utilisateur de cette personne et la liste des utilisateurs correspondants sera affichée. Prenez soin d’entrer ces renseignements correctement car plusieurs noms sont semblables; en cas de doute, entrez le nom d’utilisateur qui est unique à chaque personne.

Vous pouvez aussi entrer le nom d’un groupe CCDB (par défaut, plateformes et portails de recherche, groupes de recherche et autres groupes où le partage est configuré) pour partager avec ses membres.

L’option *Partager le lien* permet aussi de partager avec des personnes qui n’ont pas de compte avec l'Alliance; Nextcloud leur fait parvenir une notification avec le lien pour accéder au fichier.