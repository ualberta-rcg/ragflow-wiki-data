---
title: "Connecting with MobaXTerm/fr"
slug: "connecting_with_mobaxterm"
lang: "fr"

source_wiki_title: "Connecting with MobaXTerm/fr"
source_hash: "3cae66585ce2fc857a40c26713127d58"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:34:28.480842+00:00"

tags:
  - se-connecter

keywords:
  - "MobaXterm"
  - "Clé privée"
  - "Serveur"
  - "Connexion SSH"
  - "Redirection X11"

questions:
  - "Quelles sont les fonctionnalités supplémentaires de MobaXterm par rapport à PuTTY et comment y configurer une nouvelle connexion SSH ?"
  - "Comment activer et tester la redirection X11 dans MobaXterm pour exécuter des applications graphiques à distance ?"
  - "Quelle est la procédure pour associer une clé privée SSH à une session existante dans les paramètres de MobaXterm ?"
  - "Quelles sont les fonctionnalités supplémentaires de MobaXterm par rapport à PuTTY et comment y configurer une nouvelle connexion SSH ?"
  - "Comment activer et tester la redirection X11 dans MobaXterm pour exécuter des applications graphiques à distance ?"
  - "Quelle est la procédure pour associer une clé privée SSH à une session existante dans les paramètres de MobaXterm ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! tip "Fonctionnalités avancées de MobaXterm"
MobaXterm, comparé à PuTTY ([Connexion à un serveur avec PuTTY](connexion-avec-putty.md)), offre des fonctionnalités supplémentaires notables. Il intègre un client SFTP et un serveur X11, vous permettant d'exécuter des programmes graphiques à distance sans nécessiter de serveurs additionnels. De plus, MobaXterm peut utiliser vos sessions PuTTY existantes, vous évitant de reconfigurer vos paramètres.

Pour vous connecter à un serveur auquel vous n'êtes pas encore connecté avec MobaXterm ou PuTTY : sous *Sessions* -> *Nouvelle session*, sélectionnez *SSH*. Entrez ensuite l'adresse du serveur et votre nom d'utilisateur (s'il y a lieu, cochez *Spécifier le nom d'utilisateur*). Cliquez sur *OK*.

MobaXterm enregistre ces renseignements pour les connexions futures au serveur et établit la connexion SSH. Après avoir entré votre mot de passe, la fenêtre affichée présente deux panneaux :

*   Le panneau de gauche est le terminal par lequel vous entrez des commandes.
*   Le panneau de droite affiche la liste des fichiers enregistrés sur le serveur; vous pouvez glisser-déplacer vos fichiers de votre ordinateur vers le serveur et inversement.

## Redirection X11

Pour activer la redirection X11 et permettre l'utilisation d'applications graphiques à partir du serveur :

1.  Vérifiez que la redirection X11 est activée pour la session en question. Pour ce faire, cliquez sur le nom de la session et sélectionnez *Modifier la session*. Dans la fenêtre *Paramètres de la session*, sélectionnez *Paramètres SSH avancés*; la case à cocher *Redirection X11* doit être sélectionnée.
2.  Vérifiez que l'icône du *Serveur X* est verte (coin supérieur droit de la fenêtre principale). Si l'icône n'est pas verte, le serveur n'est pas activé. Pour le démarrer, cliquez sur l'icône rouge du *Serveur X*.
3.  Testez la redirection X11. Pour ce faire, démarrez la session en double-cliquant dessus dans le panneau de gauche et entrez votre mot de passe. Lancez ensuite une commande simple, par exemple `xclock`; l'affichage d'une fenêtre contextuelle montrant une horloge indique que la redirection X11 est probablement fonctionnelle.

## Paire de clés SSH

Dans le panneau de gauche, cliquez sur le nom de la session avec le bouton droit de la souris, puis sélectionnez *Modifier la session*; ceci affiche la fenêtre *Paramètres de la session*. Sélectionnez *Paramètres SSH avancés* et cochez *Utiliser une clé privée*. Pour sélectionner la clé privée que vous souhaitez utiliser, cliquez sur l'icône de moniteur dans la partie droite de la fenêtre; ceci affiche la liste des clés parmi lesquelles faire votre choix. Pour créer une paire de clés, consultez [Générer des clés SSH sous Windows](generer-des-cles-ssh-sous-windows.md).