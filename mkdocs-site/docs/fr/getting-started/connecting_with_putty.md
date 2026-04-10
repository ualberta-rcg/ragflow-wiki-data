---
title: "Connecting with PuTTY/fr"
tags:
  - se-connecter

keywords:
  []
---

[400px|thumb|  Entrez le nom ou l'adresse du serveur (cliquez pour agrandir)](file:putty_basic.png.md)
[400px|thumb| Entrez le nom d'utilisateur; ce champ n'est pas obligatoire puisque le nom peut être entré à la connexion (cliquez pour agrandir)](file:putty_username.png.md)
[400px|thumb| Activez la redirection X11 (cliquez pour agrandir)](file:putty_x11_forwarding.png.md)
[400px|thumb| Créez la clé SSH (cliquez pour agrandir)](file:putty_ssh_key.png.md)

Démarrez [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) et entrez  le nom ou l'adresse du serveur auquel vous voulez vous connecter. 

Les paramètres peuvent être sauvegardés pour usage futur&nbsp;: entrez le nom dans le champ <i>Save Session</i> et cliquez sur le bouton <i>Save</i> à droite de la liste des noms.

Vous pouvez aussi sauvegarder le nom d'utilisateur pour une connexion à un serveur en particulier&nbsp;: sous <i>Category->Connection->Data</i>, entrez le nom d'utilisateur dans le champ <i>Auto-login username</i>.  Il ne sera plus nécessaire d'entrer le nom d'utilisateur pour vous connecter.

=Redirection X11=
Pour utiliser des applications graphiques, activez la redirection X11 : sous <i>Connection->SSH->X11</i>, cochez <i>Enable X11 forwarding</i>. 

La fonction de redirection X11 nécessite un serveur <i>X window</i> tel que  [Xming](http://www.straightrunning.com/xmingnotes/) ou, pour les versions récentes de Windows, [VcXsrv](https://sourceforge.net/projects/vcxsrv/). Le serveur X window devrait être en marche avant d'établir la connexion SSH. Pour tester la redirection, ouvrez une session PuTTY et lancez une commande simple, par exemple `xclock`. L'affichage d'une fenêtre contextuelle montrant une horloge indique que la redirection X11 est probablement fonctionnelle.

=Paire de clés SSH=
Pour localiser la clé privée&nbsp;:  sous <i>Category->Connection->SSH->Auth</i>, cliquez sur le bouton <i>Browse</i>.

PuTTY utilise les fichiers avec le suffixe .ppk; ces suffixes sont générés via PuTTYGen (voir [Generating SSH keys in Windows](generating-ssh-keys-in-windows.md) pour savoir comment créer ces clés).
Dans les versions plus récentes de Putty, vous devez cliquer sur le signe + près de <i>Auth</i>, puis sélectionner <i>Credentials</i> pour pouvoir chercher le <i>Private key file for authentication</i>. Dans cette plus récente interface, les champs <i>Certificate to use</i> et <i>Plugin to provide authentication response</i> doivent être vides.