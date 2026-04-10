---
title: "Connecting with MobaXTerm/fr"
slug: "connecting_with_mobaxterm"
lang: "fr"

source_wiki_title: "Connecting with MobaXTerm/fr"
source_hash: "3cae66585ce2fc857a40c26713127d58"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:49:29.796502+00:00"

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

Si les outils de connexion [MobaXterm](http://mobaxterm.mobatek.net/) et PuTTY (voir [Connexion à un serveur avec PuTTY](connecting-with-putty.md)) se ressemblent, MobaXterm offre toutefois plus de fonctionnalités. Ce dernier comprend un client SFTP et un serveur X11 intégrés qui permettent d'opérer des programmes graphiques à distance, sans requérir un autre serveur. MobaXterm peut utiliser les sessions PuTTY déjà enregistrées sans que vous deviez en définir à nouveau les paramètres.

Pour vous connecter à un serveur auquel vous ne vous êtes pas au préalable connecté avec MobaXterm ou PuTTY : sous *Sessions* -> *Nouvelle session*, sélectionnez *SSH* puis entrez l'adresse du serveur et votre nom d'utilisateur (s'il y a lieu, cochez *Spécifier le nom d'utilisateur*). Cliquez sur *OK*. MobaXterm enregistre ces renseignements pour les connexions ultérieures au serveur et établit la connexion SSH. Après avoir entré votre mot de passe, la fenêtre affichée présente deux panneaux :
* le panneau de gauche est le terminal par lequel vous entrez des commandes
* le panneau de droite montre la liste des fichiers enregistrés sur le serveur; vous pouvez glisser-déplacer vos fichiers de votre ordinateur vers le serveur et inversement.

## Redirection X11

Pour activer la redirection X11 et permettre l'utilisation d'applications graphiques à partir du serveur :
1. Vérifiez que la redirection X11 est en fonction pour la session particulière. Pour ce faire, cliquez sur le nom de la session et sélectionnez *Modifier la session*. Dans la fenêtre *Paramètres de la session*, sélectionnez *Paramètres SSH avancés*; la case *Redirection X11* doit être cochée.
2. Vérifiez que l'icône du *serveur X* est verte (coin supérieur droit de la fenêtre principale). Si l'icône n'est pas verte, le serveur n'est pas activé. Pour le démarrer, cliquez sur l'icône du X en rouge.
3. Testez la redirection X11. Pour ce faire, démarrez la session en faisant un double-clic sur la session, dans le panneau de gauche et entrez votre mot de passe. Lancez ensuite une commande simple, par exemple `xclock`; l'affichage d'une fenêtre contextuelle montrant une horloge indique que la redirection X11 est probablement fonctionnelle.

## Paire de clés SSH

Dans le panneau de gauche, cliquez sur le nom de la session avec le bouton droit de la souris, puis sélectionnez *Modifier la session*; ceci fait afficher la fenêtre *Paramètres de la session*. Sélectionnez *Paramètres SSH avancés* et cochez *Utiliser une clé privée*. Pour sélectionner la clé privée que vous voulez utiliser, cliquez sur l'icône de moniteur dans la partie droite de la fenêtre; ceci fait afficher la liste des clés parmi lesquelles faire votre choix. Pour créer une paire de clés, voyez [Generating SSH keys in Windows](generating-ssh-keys-in-windows.md).