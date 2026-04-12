---
title: "Generating SSH keys in Windows/fr"
slug: "generating_ssh_keys_in_windows"
lang: "fr"

source_wiki_title: "Generating SSH keys in Windows/fr"
source_hash: "f96c9c96c9ef4fa28221cc8f2d986e1f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:39:08.419527+00:00"

tags:
  - connecting

keywords:
  - "OpenStack"
  - "Cloud"
  - "PuTTY"
  - "phrase de passe"
  - "paire de clés"
  - "MobaXTerm"
  - "PuTTYgen"
  - "clé privée"
  - "fichier .pem"
  - "CCDB"
  - "clé publique"
  - "PuTTYGen"
  - "instance"

questions:
  - "Quelles sont les étapes et les paramètres recommandés pour générer une nouvelle paire de clés SSH avec PuTTYgen ou MobaXTerm ?"
  - "Comment installer la clé publique générée, que ce soit de manière globale via la CCDB ou localement sur une grappe spécifique ?"
  - "Comment peut-on convertir une clé OpenStack au format .pem pour l'utiliser avec les outils PuTTY ?"
  - "Quel logiciel permet d'utiliser cette clé privée pour se connecter à une instance ?"
  - "Avec quelle plateforme l'instance mentionnée dans le texte a-t-elle été créée ?"
  - "Où peut-on trouver des informations supplémentaires concernant le lancement d'une instance ?"
  - "Quel logiciel doit être utilisé pour convertir le fichier d'extension \".pem\" provenant d'OpenStack ?"
  - "Comment configurer le filtre de recherche dans l'application pour pouvoir sélectionner et ouvrir le fichier téléchargé ?"
  - "Quelle étape facultative permet de sécuriser l'accès à la clé privée avant de la sauvegarder définitivement ?"
  - "Quel logiciel permet d'utiliser cette clé privée pour se connecter à une instance ?"
  - "Avec quelle plateforme l'instance mentionnée dans le texte a-t-elle été créée ?"
  - "Où peut-on trouver des informations supplémentaires concernant le lancement d'une instance ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [SSH](ssh.md)*

## Générer une paire de clés

La génération de clés avec PuTTY et MobaXTerm ne comporte que de légères différences.

*   Avec MobaXTerm, allez à l'option *Outils->MobaKeyGen (générateur de clés SSH)*;
*   Avec PuTTY, lancez l'exécutable PuTTYGen.

La fenêtre affichée est semblable dans les deux cas. Elle peut servir à générer une nouvelle clé ou à charger une clé existante.

1.  Pour *Type de clé à générer*, sélectionnez *Ed25519*; le type RSA est aussi acceptable, mais *Nombre de bits* doit être configuré à 2048 ou plus.
2.  Cliquez sur le bouton *Générer*. On vous demandera alors de déplacer au hasard la souris pour générer des données qui serviront à créer la clé.
3.  Entrez une phrase de passe pour votre clé.

    !!! warning "Important"
        Il est important de vous souvenir de cette phrase de passe parce que vous en aurez besoin chaque fois que vous chargerez PuTTY ou MobaXTerm pour utiliser cette paire de clés.

4.  Cliquez sur *Sauvegarder la clé privée* et entrez un nom pour le fichier; l'extension `.ppk` est ajoutée au nom du fichier.
5.  Dans *Sauvegarder la clé publique*, le nom de la clé publique est par convention le même que celui pour la clé privée, mais dans ce cas, l'extension `.pub` est ajoutée au nom du fichier.

## Installer la partie publique de la paire de clés

### Via la CCDB

!!! note "Recommandation"
    Nous vous encourageons à enregistrer votre clé publique SSH dans la CCDB, ce qui vous permettra de l'utiliser pour vous connecter à toutes nos grappes.

Copiez le contenu de la zone de texte *Clé publique à coller dans OpenSSH ...* et collez-la dans la zone de texte [dans la CCDB, option Mon compte -> Gérer vos clés SSH](https://ccdb.computecanada.ca/ssh_authorized_keys). Pour plus d'information, voyez le paragraphe [*Par la base de données CCDB*](ssh_keys.md#par-la-base-de-donnees-ccdb).

### Installation locale

Si pour quelque raison que ce soit vous ne voulez pas utiliser la fonctionnalité de la CCDB, vous pouvez téléverser votre clé publique sur *chacune* des grappes comme suit :

1.  Copiez le contenu de la zone de texte *Clé publique à coller dans OpenSSH ...* et collez-le sur une seule ligne à la fin de `/home/USERNAME/.ssh/authorized_keys` sur la grappe à laquelle vous voulez vous connecter.
2.  Vérifiez que les permissions pour les répertoires et les fichiers sont correctes et que le propriétaire est correct, comme décrit dans [ces directives](using_ssh_keys_in_linux.md#installation-locale).

Vous pouvez aussi utiliser l'outil `ssh-copy-id` s'il est disponible sur votre ordinateur personnel.

## Se connecter avec une paire de clés

Testez la nouvelle clé en vous connectant au serveur avec SSH; voyez comment [avec PuTTY](connecting_with_putty.md#paire-de-cles-ssh); [avec MobaXTerm](connecting_with_mobaxterm.md#paire-de-cles-ssh); ou [avec WinSCP](https://winscp.net/eng/docs/ui_login_authentication).

Pour une démonstration avec PuTTY, voyez la vidéo YouTube [Easily setup PuTTY SSH keys for passwordless logins using Pageant](https://www.youtube.com/watch?v=2nkAQ9M6ZF8).

## Convertir une clé OpenStack

Une clé [OpenStack](../cloud/managing_your_cloud_resources_with_openstack.md) possède l'extension `.pem`; elle peut être convertie en cliquant sur le bouton *Charger* dans PuTTYGen. Avec le filtre *Tous les fichiers (*.*)*, sélectionnez le fichier `.pem` téléchargé de OpenStack, puis cliquez sur *Ouvrir*. Vous pouvez au choix entrer une phrase de passe dans le champ *Phrase de passe de la clé* pour accéder à votre clé privée. Cliquez sur *Sauvegarder la clé privée*.

Cette clé privée peut être utilisée avec PuTTY pour se connecter à une instance créée avec OpenStack. Pour plus d'information, consultez *Lancer une instance* dans la page [Cloud : Guide de démarrage](../cloud/cloud_quick_start.md).