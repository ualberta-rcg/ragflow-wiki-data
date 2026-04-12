---
title: "Using SSH keys in Linux/fr"
slug: "using_ssh_keys_in_linux"
lang: "fr"

source_wiki_title: "Using SSH keys in Linux/fr"
source_hash: "0328743118681ade616e7f5528bd731d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:20:05.853985+00:00"

tags:
  - connecting

keywords:
  - "clé publique SSH"
  - "agent ssh"
  - "clé privée"
  - "CCDB"
  - "invite"
  - "ssh-add"
  - "ECDSA-SK 256"
  - "phrase de passe"
  - "paire de clés"
  - "ssh-copy-id"
  - "clé de sécurité matérielle"
  - "SHA256"
  - "grappe"
  - "SSH"
  - "ordinateur local"
  - "transfert d'agent"
  - "configuration SSH"
  - "ssh-agent"
  - "clé matérielle"
  - "ssh-keygen"

questions:
  - "Où se trouvent habituellement les paires de clés SSH existantes et comment sont-elles nommées par défaut ?"
  - "Quelles commandes permettent de générer une nouvelle paire de clés SSH standard de type ed25519 ou RSA ?"
  - "Comment procéder pour créer une paire de clés SSH soutenue par une clé de sécurité matérielle comme une YubiKey ?"
  - "Quelles sont les différentes méthodes recommandées pour installer une clé publique sur un système distant et quelles permissions de fichiers doivent être respectées ?"
  - "Comment doit-on procéder pour tester la connexion à une grappe distante à l'aide de sa nouvelle clé privée ?"
  - "Quel est le rôle du programme ssh-agent et comment permet-il de se connecter sans avoir à saisir sa phrase de passe à chaque fois ?"
  - "Quelles actions l'utilisateur doit-il effectuer suite à l'apparition de l'invite ?"
  - "Quel algorithme de chiffrement est utilisé pour générer cette clé selon l'image affichée ?"
  - "Quel composant physique spécifique est mentionné comme devant être activé ?"
  - "Quelle commande permet d'ajouter une paire de clés à l'agent SSH sur un ordinateur local ?"
  - "Comment procéder pour ajouter une clé privée si elle ne se trouve pas dans un emplacement par défaut ?"
  - "Quelle option de la commande ssh-add permet d'afficher la liste des clés privées actuellement ajoutées à l'agent ?"
  - "Comment configurer le transfert d'agent SSH pour utiliser une clé privée sur une grappe distante ?"
  - "Quelle précaution de sécurité importante doit-on respecter dans le fichier de configuration SSH concernant le transfert d'agent ?"
  - "Quel est l'avantage d'utiliser un gestionnaire de trousseau de clés (keychain manager) sur son ordinateur local pour les connexions SSH ?"
  - "Comment configurer le transfert d'agent SSH pour utiliser une clé privée sur une grappe distante ?"
  - "Quelle précaution de sécurité importante doit-on respecter dans le fichier de configuration SSH concernant le transfert d'agent ?"
  - "Quel est l'avantage d'utiliser un gestionnaire de trousseau de clés (keychain manager) sur son ordinateur local pour les connexions SSH ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Sous-page de [SSH](ssh.md)*

## Créer une paire de clés
Vérifiez si vous avez déjà une paire de clés avant d'en créer une nouvelle. Si vous avez déjà une paire de clés, mais que vous ne vous souvenez plus où vous l'avez utilisée, il est préférable d'en créer une nouvelle, car vous ne devriez pas utiliser une clé sans connaître son degré de sécurité.

Les paires de clés se trouvent habituellement dans le répertoire `.ssh/` de votre espace `/home`. Par défaut, le nom de la clé est composé du préfixe **id_** suivi de son type (**rsa, dsa, ed25519**); la clé publique possède le suffixe **.pub**. Un exemple commun serait `id_rsa` et `id_rsa.pub`. Il est de bonne pratique de nommer une clé de façon à suggérer où elle est utilisée.

Si vous avez besoin d'une nouvelle paire de clés, vous pouvez la générer avec la commande `ssh-keygen`.

```bash
ssh-keygen -t ed25519
```
ou
```bash
ssh-keygen -b 4096 -t rsa
```
(Cet exemple crée explicitement une clé `4-kbit RSA`, un choix raisonnable).

Le résultat sera semblable à ceci :

```console
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
The key fingerprint is:
ef:87:b5:b1:4d:7e:69:95:3f:62:f5:0d:c0:7b:f1:5e username@hostname
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|           .     |
|            o .  |
|        S    o o.|
|         .  + +oE|
|          .o O.oB|
|         .. +oo+*|
|          ... o..|
+-----------------+
```

!!! tip
    À l'invite, entrez une phrase de passe. Si vous avez déjà sauvegardé une paire de clés avec leurs noms par défaut, vous devriez donner un nom différent au fichier pour éviter d'écraser les clés existantes. Voyez plus d'information sur les [meilleures pratiques](ssh_keys.md#meilleures-pratiques).

## Créer une paire de clés soutenue par une clé de sécurité matérielle
Certains sites prennent désormais en charge l'utilisation de clés SSH soutenues par une clé de sécurité matérielle (par exemple, YubiKey). Si vous avez besoin d'une de ces clés, vous pouvez la générer avec la commande `ssh-keygen`.

```bash
ssh-keygen -t ecdsa-sk
```

Le résultat sera semblable à ceci :

```console
Generating public/private ecdsa-sk key pair.
You may need to touch your authenticator to authorize key generation.
Enter file in which to save the key (/home/username/.ssh/id_ecdsa_sk):
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/username/.ssh/id_ecdsa_sk
Your public key has been saved in /home/username/.ssh/id_ecdsa_sk.pub
The key fingerprint is:
SHA256:P051NAesYSxF7NruGLfnyAFMUBmGLwCaSRiXDwUY6Ts username@hostname
The key's randomart image is:
+-[ECDSA-SK 256]--+
|o*++o.  .o+Bo..  |
|+oo+  . .oo = .. |
|. +o   . ..+ oo .|
| .  .   .o. o. o |
|  .     S.oo. .  |
| E       ..o..   |
|  .       =.o    |
|         o *.+.  |
|          o.=o.  |
+----[SHA256]-----+
```

Une invite vous demande d'entrer une phrase de passe et d'activer la clé matérielle.

## Installer la clé publique

### Installation via la CCDB
Nous vous encourageons à enregistrer votre clé publique SSH dans la CCDB, ce qui vous permettra de l'utiliser pour vous connecter à toutes nos grappes. Copiez le contenu de la clé publique (dans notre exemple, **id_rsa.pub**) et téléversez-la dans la CCDB tel que décrit à l'étape 3 de [cette procédure](ssh_keys.md).

Le moyen le plus simple et le plus sécuritaire d'installer une clé sur un système distant est d'utiliser la commande
```bash
ssh-copy-id -i ~/.ssh/mynewkey.pub graham.computecanada.ca
```
Ici, **mynewkey** et **mynewkey.pub** sont les noms de la nouvelle paire de clés. Nous supposons que votre nom d'utilisateur sur le système distant est le même que celui que vous utilisez localement.

La commande `ssh-copy-id` ne fait rien d'exceptionnel; elle se connecte au système distant et place la clé publique dans `.ssh/authorized_keys` dans votre répertoire `/home`. Le principal avantage est que `ssh-copy-id` crée les fichiers et les répertoires nécessaires et ajuste les permissions automatiquement. À la place, vous pouvez installer votre clé manuellement. Pour ce faire, copiez le fichier de la clé publique sur le serveur distant, puis faites :
```bash
mkdir ~/.ssh
cat id_rsa.pub >> ~/.ssh/authorized_keys
chmod --recursive go-rwx ~/.ssh
chmod go-w ~
```
SSH est pointilleux quant aux permissions, à la fois pour le client et pour le serveur. SSH échouera si les conditions suivantes ne sont pas remplies :
*   Le fichier de clé privée ne doit pas être accessible aux autres. `chmod go-rwx id_rsa`
*   Votre répertoire `/home` distant ne doit pas être accessible en écriture par d'autres. `chmod go-w ~`
*   Il en est de même pour vos `~/.ssh` et `~/.ssh/authorized_keys` `chmod --recursive go-rwx ~/.ssh`.

!!! warning
    Notez que le débogage de ces conditions sur le système distant peut être difficile et même nécessiter l'intervention d’un administrateur système.

## Se connecter avec une paire de clés
Enfin, testez la nouvelle clé en vous connectant au serveur à partir de votre poste local avec la commande :
```bash
ssh -i /path/to/your/privatekey USERNAME@ADDRESS
```
où :
*   `/path/to/your/privatekey` indique le nom du fichier de la clé privée, par exemple `/home/ubuntu/.ssh/id_rsa`;
*   `USERNAME` est le nom de l'utilisateur sur la grappe;
*   `ADDRESS` est l'adresse du serveur distant.

Si vous avez les privilèges admin sur le serveur et que vous avez créé un compte pour un autre utilisateur, ce dernier devrait lui-même tester la connexion pour ne pas avoir à divulguer sa clé privée.

## Agent d'authentification
Une fois que votre paire de clés est créée et que la clé publique est installée sur la grappe, vous pouvez vous servir de la paire de clés pour vous connecter. Ceci est préférable à l’utilisation d’un mot de passe, mais chaque fois que vous voulez vous connecter à une grappe, vous devez entrer une phrase de passe pour déverrouiller la clé privée. Pour éviter ceci, le programme `ssh-agent` met en mémoire votre clé privée sur votre ordinateur local et la fournit aux programmes qui en ont besoin. Vous n'avez donc qu'à déverrouiller la clé privée une seule fois et vous pouvez toujours vous connecter à une grappe distante sans avoir besoin d'une phrase de passe.

Vous pouvez démarrer `ssh-agent` avec la commande :
```bash
eval `ssh-agent`
```
Après avoir démarré `ssh-agent`, qui s'exécutera en arrière-plan dans votre session sur votre ordinateur local, vous pouvez ajouter votre paire de clés à l'agent avec la commande :
```bash
ssh-add
```
En supposant que vous ayez installé votre paire de clés dans l'un des emplacements habituels, la commande `ssh-add` devrait la trouver, mais si nécessaire, vous pouvez explicitement ajouter le chemin complet de la clé privée en tant qu'argument à `ssh-add`. L'option `ssh-add -l` affiche les clés privées qui ont été ajoutées à l'agent ssh.

Le programme `ssh-agent` permet de négocier automatiquement l'échange de clés entre votre ordinateur personnel et la grappe, mais si vous devez utiliser votre clé privée sur la grappe elle-même, par exemple lors de l'interaction avec un référentiel GitHub distant, vous devrez activer le transfert d’agent. Pour activer cette fonction sur une grappe ([Béluga](../clusters/béluga.md) dans l'exemple), ajoutez les lignes suivantes à votre fichier `$HOME/.ssh/config` sur votre ordinateur local.
```text title="config"
Host beluga.computecanada.ca
    ForwardAgent yes
```

!!! warning
    Notez que le fichier de configuration SSH ne doit jamais contenir la ligne `Host *` pour le transfert de l'agent.

### Installation locale
macOS et plusieurs distributions récentes de Linux offrent des **gestionnaires de trousseaux de clés** graphiques faciles à configurer pour gérer votre paire de clés. En vous connectant à votre ordinateur local, la clé privée est enregistrée en mémoire et le système d'exploitation peut automatiquement fournir cette clé au client SSH quand vous vous connectez à distance sur une grappe. Vous n'aurez plus besoin d'entrer une phrase de passe pour vous connecter par la suite.