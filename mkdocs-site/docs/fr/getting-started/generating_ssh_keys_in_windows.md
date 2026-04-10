---
title: "Generating SSH keys in Windows/fr"
slug: "generating_ssh_keys_in_windows"
lang: "fr"

source_wiki_title: "Generating SSH keys in Windows/fr"
source_hash: "f96c9c96c9ef4fa28221cc8f2d986e1f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:58:07.865828+00:00"

tags:
  - connecting

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

*Page enfant de [SSH](ssh.md)*

# Générer une paire de clés

La génération de clés avec PuTTY et MobaXTerm ne comporte que de légères différences.
*   Avec MobaXTerm, allez à l'option « Outils » -> « MobaKeyGen (Générateur de clé SSH) » (''Tools->MobaKeyGen (SSH key generator)'');
*   Avec PuTTY, lancez l'exécutable PuTTYGen.

La fenêtre affichée est semblable dans les deux cas. Elle peut servir à générer une nouvelle clé ou à charger une clé existante.

1.  Pour « Type de clé à générer » (''Type of key to generate''), sélectionnez « Ed25519 »; le type RSA est aussi acceptable, mais « Nombre de bits » (''Number of bits'') doit être configuré à 2048 ou plus.
2.  Cliquez sur le bouton « Générer » (''Generate''). On vous demandera alors de déplacer au hasard la souris pour générer des données qui serviront à créer la clé.
3.  Entrez une phrase de passe pour votre clé. Il est important de vous souvenir de cette phrase de passe parce que vous en aurez besoin chaque fois que vous chargerez PuTTY ou MobaXTerm pour utiliser cette paire de clés.
4.  Cliquez sur « Enregistrer la clé privée » (''Save private key'') et entrez un nom pour le fichier; l'extension `.ppk` est ajoutée au nom du fichier.
5.  Dans « Enregistrer la clé publique » (''Save public key''), le nom de la clé publique est par convention le même que celui pour la clé privée, mais dans ce cas, l'extension `.pub` est ajoutée au nom du fichier.

# Installer la partie publique de la paire de clés

## Via la CCDB

Nous vous encourageons à enregistrer votre clé publique SSH dans la CCDB, ce qui vous permettra de l'utiliser pour vous connecter à toutes nos grappes. Copiez le contenu de la zone de texte « Clé publique à coller dans OpenSSH... » (''Public key for pasting into OpenSSH ...'') et collez-la dans la zone de texte [dans la CCDB, option « Mon compte -> Gérer vos clés SSH »](https://ccdb.computecanada.ca/ssh_authorized_keys). Pour plus d'information, voyez le paragraphe [*Par la base de données CCDB*](ssh-keys.md#par-la-base-de-donnees-ccdb).

## Installation locale

Si pour quelque raison que ce soit vous ne voulez pas utiliser la fonctionnalité de la CCDB, vous pouvez téléverser votre clé publique sur *chacune* des grappes comme suit :

1.  Copiez le contenu de la zone de texte « Clé publique à coller dans OpenSSH... » (''Public key for pasting into OpenSSH ...'') et collez-le sur une seule ligne à la fin de `/home/USERNAME/.ssh/authorized_keys` sur la grappe à laquelle vous voulez vous connecter.
2.  Vérifiez que les permissions pour les répertoires et les fichiers sont correctes et que le propriétaire est correct, comme décrit dans [ces directives](using-ssh-keys-in-linux.md#installation-locale).

Vous pouvez aussi utiliser l'outil `ssh-copy-id` s'il est disponible sur votre ordinateur personnel.

# Se connecter avec une paire de clés

Testez la nouvelle clé en vous connectant au serveur avec SSH; voyez [avec PuTTY](connecting-with-putty.md#paire-de-cles-ssh); [avec MobaXTerm](connecting-with-mobaxterm.md#paire-de-cles-ssh); ou [avec WinSCP](https://winscp.net/eng/docs/ui_login_authentication).

Pour une démonstration avec PuTTY, voyez la vidéo YouTube [Easily setup PuTTY SSH keys for passwordless logins using Pageant](https://www.youtube.com/watch?v=2nkAQ9M6ZF8).

# Convertir une clé OpenStack

Une clé [OpenStack](managing-your-cloud-resources-with-openstack.md) possède l'extension `.pem`; elle peut être convertie en cliquant sur le bouton « Charger » (''Load'') dans PuTTYGen. Avec le filtre « Tous les fichiers (*.*) » (''All Files (*.*)''), sélectionnez le fichier `.pem` téléchargé de OpenStack, puis cliquez sur « Ouvrir » (''Open''). Vous pouvez au choix entrer une phrase de passe dans le champ « Phrase de passe de la clé » (''Key passphrase'') pour accéder à votre clé privée. Cliquez sur « Enregistrer la clé privée » (''Save private key'').

Cette clé privée peut être utilisée avec PuTTY pour se connecter à une instance créée avec OpenStack. Pour plus d'information, consultez « Lancer une instance » dans la page [Cloud : Guide de démarrage](cloud-quick-start.md).