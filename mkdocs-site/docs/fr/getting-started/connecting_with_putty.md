---
title: "Connecting with PuTTY/fr"
slug: "connecting_with_putty"
lang: "fr"

source_wiki_title: "Connecting with PuTTY/fr"
source_hash: "24f3a984c5a57b97b82e1cf620f702cd"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:50:21.638461+00:00"

tags:
  - se-connecter

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Démarrez [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) et entrez le nom ou l'adresse du serveur auquel vous voulez vous connecter.

Les paramètres peuvent être sauvegardés pour usage futur : entrez le nom dans le champ *Session enregistrée* et cliquez sur le bouton *Enregistrer* à droite de la liste des noms.

Vous pouvez aussi sauvegarder le nom d'utilisateur pour une connexion à un serveur en particulier : sous *Catégorie->Connexion->Données*, entrez le nom d'utilisateur dans le champ *Nom d'utilisateur d'ouverture de session automatique*. Il ne sera plus nécessaire d'entrer le nom d'utilisateur pour vous connecter.

## Redirection X11

Pour utiliser des applications graphiques, activez la redirection X11 : sous *Connexion->SSH->X11*, cochez *Activer la redirection X11*.

La fonction de redirection X11 nécessite un serveur X tel que [Xming](http://www.straightrunning.com/xmingnotes/) ou, pour les versions récentes de Windows, [VcXsrv](https://sourceforge.net/projects/vcxsrv/). Le serveur X devrait être en marche avant d'établir la connexion SSH. Pour tester la redirection, ouvrez une session PuTTY et lancez une commande simple, par exemple `xclock`. L'affichage d'une fenêtre contextuelle montrant une horloge indique que la redirection X11 est probablement fonctionnelle.

## Paire de clés SSH

Pour localiser la clé privée : sous *Catégorie->Connexion->SSH->Authentification*, cliquez sur le bouton *Parcourir*.

PuTTY utilise les fichiers avec le suffixe .ppk; ces suffixes sont générés via PuTTYGen (voir [Générer des clés SSH sous Windows](generating-ssh-keys-in-windows.md) pour savoir comment créer ces clés).

Dans les versions plus récentes de PuTTY, vous devez cliquer sur le signe + près de *Authentification*, puis sélectionner *Informations d'identification* pour pouvoir chercher le *Fichier de clé privée pour l'authentification*. Dans cette plus récente interface, les champs *Certificat à utiliser* et *Module d'extension pour fournir la réponse d'authentification* doivent être vides.