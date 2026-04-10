---
title: "Generating SSH keys in Windows/fr"
tags:
  - connecting

keywords:
  []
---

*Page enfant de [SSH/fr](ssh/fr.md)*

[400px|thumb| Avant de générer la clé avec PuTTYgen (cliquez pour agrandir)](file:puttygen1.png.md)
[400px|thumb| Après avoir généré la clé avec PuTTYgen (cliquez pour agrandir)](file:puttygen1.png.md)

=Générer une paire de clés= 

La génération de clés avec PuTTY et MobaXTerm ne comporte que de légères différences.
* avec MobaXTerm, allez à l'option *Tools->MobaKeyGen (SSH key generator)*;
* avec PuTTY, lancez l'exécutable PuTTYGen.

La fenêtre affichée est semblable dans les deux cas. Elle peut servir à générer une nouvelle clé ou à charger une clé existante.

# Pour *Type of key to generate*, sélectionnez *Ed25519*; le type RSA est aussi acceptable, mais *Number of bits* doit être configuré à 2048 ou plus.
# Cliquez sur le bouton *Generate*. On vous demandera alors de déplacer au hasard la souris pour générer des données qui serviront à créer la clé.
# Entrez une phrase de passe pour votre clé. Il est important de vous souvenir de cette phrase de passe parce que vous en aurez besoin chaque fois que vous chargerez PuTTY ou MobaXTerm pour utiliser cette paire de clés.
# Cliquez sur *Save private key*  et entrez un nom pour le fichier; l'extension `.ppk` est ajoutée au nom du fichier.
# Dans *Save public key*, le nom de la clé publique est par convention le même que celui pour la clé privée, mais dans ce cas, l'extension `.pub` est ajoutée au nom du fichier.

=Installer la partie publique de la paire de clés=

## Via la CCDB

Nous vous encourageons à enregistrer votre clé publique SSH dans la CCDB, ce qui vous permettra de l'utiliser pour vous connecter à toutes nos grappes. Copiez le contenu de la zone de texte *Public key for pasting into OpenSSH ...* et collez-la dans la zone de texte [dans la CCDB, option *Mon compte -> Gérer vos clés SSH*](https://ccdb.computecanada.ca/ssh_authorized_keys). Pour plus d'information, voyez le paragraphe [*Par la base de données CCDB*](ssh_keys-fr#par_la_base_de_données_ccdb.md).

==Installation locale== 

Si pour quelque raison que ce soit vous ne voulez pas utiliser la fonctionnalité de la CCDB, vous pouvez téléverser votre clé publique sur <em>chacune</em> des grappes comme suit :

# Copiez le contenu de la zone de texte *Public key for pasting into OpenSSH ...* et collez-le sur une seule ligne à la fin de `/home/USERNAME/.ssh/authorized_keys` sur la grappe à laquelle vous voulez vous connecter.
# Vérifiez que les permissions pour les répertoires et les fichiers sont correctes et que le propriétaire est correct, comme décrit dans [ces directives](using-ssh-keys-in-linux-fr#installation_locale.md).

Vous pouvez aussi utiliser l'outil `ssh-copy-id` s'il est disponible sur votre ordinateur personnel.

=Se connecter avec une paire de clés= 

Testez la nouvelle clé en vous connectant au serveur avec SSH; voyez comment [avec PuTTY](connecting-with-putty-fr#paire_de_clés_ssh.md); [avec MobaXTerm](connecting-with-mobaxterm-fr#paire_de_clés_ssh.md); ou [avec WinSCP](https://winscp.net/eng/docs/ui_login_authentication).

Pour une démonstration avec PuTTY, voyez la vidéo YouTube [Easily setup PuTTY SSH keys for passwordless logins using Pageant](https://www.youtube.com/watch?v=2nkAQ9M6ZF8).

=Convertir une clé OpenStack= 

Une clé [OpenStack](managing_your_cloud_resources_with_openstack-fr.md) possède l'extension *.pem*; elle peut être convertie en cliquant sur le bouton *Load* dans PuTTYGen. Avec le filtre *All Files (*.*)*, sélectionnez le fichier *.pem* téléchargé de OpenStack, puis cliquez sur *Open*. Vous pouvez au choix entrer une phrase de passe dans le champ *Key passphrase* pour accéder à votre clé privée. Cliquez sur *Save private key*.

Cette clé privée peut être utilisée avec PuTTY pour se connecter à une instance créée avec OpenStack. Pour plus d'information, consultez *Lancer une instance* dans la page [Cloud : Guide de démarrage](cloud-quick-start-fr.md).