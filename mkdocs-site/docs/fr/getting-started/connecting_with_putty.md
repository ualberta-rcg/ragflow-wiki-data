---
title: "Connecting with PuTTY/fr"
slug: "connecting_with_putty"
lang: "fr"

source_wiki_title: "Connecting with PuTTY/fr"
source_hash: "24f3a984c5a57b97b82e1cf620f702cd"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:35:16.059779+00:00"

tags:
  - se-connecter

keywords:
  - "redirection X11"
  - "PuTTY"
  - "connexion SSH"
  - "clés SSH"
  - "serveur"

questions:
  - "Comment peut-on configurer et sauvegarder les paramètres d'une session, y compris le nom d'utilisateur, pour un usage futur dans PuTTY ?"
  - "Quels sont les prérequis et la procédure pour activer et tester la redirection X11 permettant d'utiliser des applications graphiques ?"
  - "Comment doit-on configurer PuTTY pour utiliser une clé privée SSH (.ppk) lors de l'authentification, en particulier dans les versions récentes du logiciel ?"
  - "Comment peut-on configurer et sauvegarder les paramètres d'une session, y compris le nom d'utilisateur, pour un usage futur dans PuTTY ?"
  - "Quels sont les prérequis et la procédure pour activer et tester la redirection X11 permettant d'utiliser des applications graphiques ?"
  - "Comment doit-on configurer PuTTY pour utiliser une clé privée SSH (.ppk) lors de l'authentification, en particulier dans les versions récentes du logiciel ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Démarrez [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) et entrez le nom ou l'adresse du serveur auquel vous voulez vous connecter.
Les paramètres peuvent être sauvegardés pour usage futur : entrez le nom dans le champ *Sauvegarder la session* et cliquez sur le bouton *Sauvegarder* à droite de la liste des noms.
Vous pouvez aussi sauvegarder le nom d'utilisateur pour une connexion à un serveur en particulier : sous *Catégorie > Connexion > Données*, entrez le nom d'utilisateur dans le champ *Nom d'utilisateur pour la connexion automatique*. Il ne sera plus nécessaire d'entrer le nom d'utilisateur pour vous connecter.

## Redirection X11
Pour utiliser des applications graphiques, activez la redirection X11 : sous *Connexion > SSH > X11*, cochez *Activer le transfert X11*.
La fonction de redirection X11 nécessite un serveur *X window* tel que [Xming](http://www.straightrunning.com/xmingnotes/) ou, pour les versions récentes de Windows, [VcXsrv](https://sourceforge.net/projects/vcxsrv/). Le serveur X window devrait être en marche avant d'établir la connexion SSH. Pour tester la redirection, ouvrez une session PuTTY et lancez une commande simple, par exemple `xclock`.

!!! tip
    L'affichage d'une fenêtre contextuelle montrant une horloge indique que la redirection X11 est probablement fonctionnelle.

## Paire de clés SSH
Pour localiser la clé privée : sous *Catégorie > Connexion > SSH > Authentification*, cliquez sur le bouton *Parcourir*.
PuTTY utilise les fichiers avec le suffixe .ppk; ces suffixes sont générés via PuTTYGen (voir [Generating SSH keys in Windows](generating-ssh-keys-in-windows.md) pour savoir comment créer ces clés).
Dans les versions plus récentes de PuTTY, vous devez cliquer sur le signe + près de *Authentification*, puis sélectionner *Identifiants* pour pouvoir chercher le *Fichier de clé privée pour l'authentification*. Dans cette plus récente interface, les champs *Certificat à utiliser* et *Plug-in pour fournir la réponse d'authentification* doivent être vides.