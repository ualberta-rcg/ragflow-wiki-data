---
title: "Automation in the context of multifactor authentication/fr"
slug: "automation_in_the_context_of_multifactor_authentication"
lang: "fr"

source_wiki_title: "Automation in the context of multifactor authentication/fr"
source_hash: "3733092de8d35a2eadeef8f63a374159"
last_synced: "2026-08-30T01:09:18.871111+00:00"
last_processed: "2026-08-30T01:32:41.090460+00:00"

tags:
  []

keywords:
  - "masque d'adresse IP"
  - "accepter ou refuser les commandes"
  - "client SSH"
  - "accès sur demande"
  - "identityfile"
  - "définir toutes les commandes"
  - "ssh.exec_command"
  - "nœuds d'automatisation"
  - "paramiko.SSHClient"
  - "authentification multifacteur"
  - "set_missing_host_key_policy"
  - "rsync -a"
  - "Rorqual"
  - "host robot"
  - "adressage IPv4"
  - "ssh.connect"
  - "clé SSH avec contrainte restrict"
  - "clé SSH restreinte"
  - "Paramiko"
  - "fichier ~/.ssh/config"
  - "utilisation de -i pour spécifier la clé privée"
  - "allowed_commands/transfer_commands.sh"
  - "adressage IPv6"
  - "installer Paramiko"
  - "type de clés Ed25519"
  - "connexion au nœud d'automatisation"
  - "script enveloppant"
  - "commandes Slurm"
  - "ls -l"
  - "command=\"COMMAND\""
  - "dépôt git"
  - "clé inscrite dans le portail CCDB"
  - "scripts préparés"

questions:
  - "Comment demander l'accès aux nœuds spéciaux d'automatisation et quelles informations doivent être fournies au soutien technique ?"
  - "Quelles contraintes spécifiques (restrict, from, command) les clés SSH doivent respecter pour se connecter à ces nœuds d'automatisation ?"
  - "Quelles sont les limitations fonctionnelles des nœuds spéciaux d'automatisation comparées aux nœuds de connexion réguliers (type d'authentification et types d'actions autorisées) ?"
  - "Quel rôle joue le script enveloppant dans la gestion des commandes autorisées ?"
  - "Comment peut‑on créer ou personnaliser ses propres scripts d’acceptation/rejet de commandes ?"
  - "Où peut‑on accéder aux scripts pré‑préparés pour les cas d’usage fréquents mentionnés dans le texte ?"
  - "Quels scripts d'allowed_commands sont fournis et quelles types de commandes chaque script autorise‑t‑il ?"
  - "Comment doit‑on formater une clé SSH afin de la restreindre à des commandes spécifiques (par ex. transfert de fichiers avec scp/sftp/rsync ou seules les commandes Slurm) ?"
  - "Quels sont les noms d’hôtes des nœuds d’automatisation par grappe et comment les configurer dans le fichier ~/.ssh/config pour les utiliser correctement ?"
  - "Comment identifier, via les messages de débogage, si le client SSH utilise une adresse IPv4 ou IPv6 pour se connecter au nœud d’automatisation ?"
  - "Quelle est la conséquence d’utiliser un masque IPv4 dans le champ <code>restrict,from=</code> d’une clé SSH lorsque le client se connecte au nœud avec une adresse IPv6 ?"
  - "Quelles solutions sont proposées pour forcer l’utilisation d’IPv4 (ou d’IPv6) avec le client SSH ou avec un script Python utilisant Paramiko ?"
  - "Quels paramètres devez‑vous ajouter dans le fichier ~/.ssh/config pour que le client SSH utilise la clé et les options souhaitées ?"
  - "Comment la configuration présentée permet‑elle d’exécuter la commande distante `ssh robot /usr/bin/ls` ?"
  - "En quoi cette même configuration rend‑elle possible l’utilisation de `rsync -a datadir/a robot:scratch/testdata` ?"
  - "Quelle commande doit‑on exécuter pour installer Paramiko avec le support des clés Ed25519 ?"
  - "Quelle commande est utilisée pour lister les fichiers du nœud d’automatisation Rorqual après la connexion ?"
  - "Pourquoi est‑il important d’utiliser une clé inscrite dans le portail CCDB lors de la connexion au nœud d’automatisation ?"
  - "What is the purpose of the Python script that uses Paramiko to connect to `robot.rorqual.alliancecan.ca` and execute `ls -l`?"
  - "Which security implications arise from using `AutoAddPolicy()` and a private key located at `/home/username/.ssh/cc_allowed` in this SSH connection?"
  - "How does the script capture and display the output of the remote command, and what would happen if an error occurs during execution?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Les flux de travail automatisés se connectant à nos grappes ne peuvent pas recourir à un deuxième facteur d'authentification. Étant donné que l'authentification multifacteur est maintenant exigée, vous devez demander l'accès à l'un des nœuds d'automatisation dédiés. Un deuxième facteur ne sera alors pas requis, mais sachez que les fonctionnalités de ces nœuds sont limitées par rapport à celles des nœuds de connexion réguliers, tant en ce qui concerne le type d'authentification requise que les types d'actions autorisées.

## Mesures de sécurité accrues

### Accès sur demande seulement
Pour avoir accès aux nœuds d'automatisation dédiés, écrivez au [soutien technique](../support/technical_support.md). Décrivez le type d'automatisation, listez les commandes qui seront exécutées ainsi que les outils ou les bibliothèques pour gérer l'automatisation.

!!! note "Note"
    Les nœuds d'automatisation sont conçus pour des charges de travail prévisibles. Ils ne conviennent pas à l'utilisation d'agents d'IA. Si vous avez des questions, écrivez au [soutien technique](../support/technical_support.md).

### Accès via certaines clés SSH avec contraintes
L'accès aux nœuds d'automatisation se fait uniquement via les [clés SSH téléversées dans CCDB](ssh_keys.md). Les clés inscrites dans un fichier `*~/.ssh/authorized_keys*` ne sont pas acceptées. Veuillez respecter la règle **une clé SSH par utilisation**. Ne réutilisez pas la clé pour vous connecter interactivement; générez plutôt une clé expressément pour votre flux de travail automatisé. De plus, les clés SSH **doivent respecter** les contraintes suivantes :

#### `restrict`
Cette contrainte désactive la redirection de port (*port forwarding*), la redirection d'agent (*agent forwarding*) et la redirection X11. Le pseudotélétype (PTY) est aussi désactivé, puisqu'il bloquerait la plupart des flux interactifs. Nous posons ces conditions parce que les nœuds d'automatisation dédiés ne doivent pas être utilisés pour les processus interactifs ou de longue durée; dans ces cas, il faut utiliser les nœuds réguliers.

#### `from="pattern-list"`
Cette contrainte fait en sorte que la clé ne peut être utilisée qu'à partir d'adresses IP qui respectent le *pattern* et non par d'autres ordinateurs. La liste des *patterns* doit être uniquement composée d'adresses IP qui spécifient la classe du réseau, le réseau et le sous-réseau, soit les trois premiers éléments de l'adresse. Par exemple, `` `x.y.*.*` `` ne serait pas acceptée, mais `` `x.y.z.*` `` le serait. Aussi, l'adresse IP doit être une adresse **publique**; ainsi, `` `10.0.0.0 – 10.255.255.255` ``, `` `172.16.0.0 – 172.31.255.255` `` et `` `192.168.0.0 – 192.168.255.255` `` seraient incorrectes. Pour connaître votre adresse IP publique, allez sur le site [What Is My IP Address?](https://whatismyipaddress.com/) ou lancez la commande `` `curl ifconfig.me` `` de l'interpréteur (*shell*).

#### `command="COMMAND"`
Cette contrainte exécute la commande `` `COMMAND` `` lors de la connexion. Ceci vous permet de définir les seules commandes qui peuvent être utilisées avec la clé.

Les chemins spécifiés dans `` `COMMAND` `` peuvent être absolus (soit de `` `/` ``) ou relatifs au répertoire personnel dans `` `/home` ``.

### Scripts enveloppants pour la commande `command=`
Cette commande permet de définir toutes les commandes, mais elle est le plus utile quand vous avez un script enveloppant qui accepte ou refuse les commandes qui sont appelées. Vous pouvez écrire vos propres scripts, mais nous en avons préparé certains pour des cas qui se présentent fréquemment. Ces scripts se trouvent dans [ce dépôt Git](https://github.com/ComputeCanada/software-stack-custom/tree/main/bin/computecanada/allowed_commands).

*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/transfer_commands.sh` `` permet uniquement les commandes de transfert de fichiers, comme `` `scp` ``, `` `sftp` `` ou `` `rsync` ``
*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/archiving_commands.sh` `` permet les commandes d'archivage de fichiers, comme `` `gzip` ``, `` `tar` `` ou `` `dar` ``
*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/file_commands.sh` `` permet les commandes de manipulation de fichiers, comme `` `mv` ``, `` `cp` `` ou `` `rm` ``
*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/git_commands.sh` `` permet la commande `` `git` ``
*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/slurm_commands.sh` `` permet certaines commandes Slurm, comme `` `squeue` ``, `` `sbatch` ``, `` `scancel` ``, `` `scontrol` ``, `` `sq` ``
*   `` `/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/allowed_commands.sh` `` permet toutes les commandes ci-dessus

### Exemples de clés SSH acceptées
Les clés doivent respecter les trois conditions décrites ci-dessus. En voici quelques exemples qui seraient valides pour le transfert de fichiers avec `` `scp` ``, `` `sftp` `` ou `` `rsync` `` :

```text
restrict,from="216.18.209.*",command="/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/transfer_commands.sh" ssh-ed25519 AAAAC3NzaC1lZDI1NTE6AACAIExK9iTTDGsyqKKzduA46DvIJ9oFKZ/WN5memqG9Invw
```

Le prochain exemple permettrait uniquement des commandes Slurm (squeue, scancel, sbatch, scontrol, sq).

```text
restrict,from="216.18.209.*",command="/cvmfs/soft.computecanada.ca/custom/bin/computecanada/allowed_commands/slurm_commands.sh" ssh-ed25519 AAAAC3NzaC1lZDI1NTE6AACAIExK9iTTDGsyqKKzduA46DvIJ9oFKZ/WN5memqG9Invw
```

!!! warning "Attention"
    Avant d'ajouter la clé SSH dans [votre compte CCDB](https://ccdb.alliancecan.ca/ssh_authorized_keys), assurez-vous que les contraintes soient indiquées comme dans les exemples précédents.

## Nœuds d'automatisation, par grappe
Pour vous connecter à un nœud d'automatisation, utilisez les adresses suivantes :
*   Fir : robot.fir.alliancecan.ca
*   Narval : robot.narval.alliancecan.ca
*   Nibi : robot.nibi.alliancecan.ca
*   Rorqual : robot.rorqual.alliancecan.ca
*   tamIA: robot.tamia.ecpia.ca
*   Trillium : robot2.scinet.utoronto.ca

## Ne pas se tromper de clé
Si vous avez plusieurs clés, assurez-vous d'utiliser la bonne. Ceci peut se faire avec des paramètres passés à la commande, comme dans les exemples ci-dessous.

Avec `` `ssh` `` ou `` `scp` ``,

```bash
ssh -i .ssh/private_key_to_use ...
scp -i .ssh/private_key_to_use ...
```

Avec `` `rsync` ``,

```bash
rsync -e "ssh -i .ssh/private_key_to_use" ...
```

Il est souvent beaucoup plus pratique d'inclure ces paramètres dans votre fichier `~/.ssh/config` pour qu'ils soient pris en compte quand le client SSH est invoqué. Par exemple :

```ini
host robot
  hostname robot.cluster.alliancecan.ca
  user myrobot
  identityfile ~/.ssh/my-robot-key
  identitiesonly yes
  requesttty no
```

Ceci signifie que les deux types de commandes suivantes feront ce que vous voulez.

```bash
ssh robot /usr/bin/ls
rsync -a datadir/a robot:scratch/testdata
```

## Problème d'adressage avec IPv4 et IPv6 {#ipv4-vs-ipv6-issue}

En voulant se connecter à un nœud d'automatisation, le client SSH de votre ordinateur pourrait choisir l'adressage IPv6 plutôt que l'adressage IPv4 moins récent. Ceci semble plus probable dans un environnement Windows. Si c'est le cas, assurez-vous que le masque de l'adresse IP que vous entrez dans le champ `` `restrict,from=` `` de la clé corresponde au type d'adresse que votre ordinateur utilisera pour se connecter au nœud.

Vérifiez vos adresses sur le site [https://test-ipv6.com/](https://test-ipv6.com/).

*   Une adresse IPv4 ressemble à **199.241.166.5**.
*   Une adresse IPv6 ressemble à **2620:123:7002:4::5**.

Si vous entrez le masque IPv4 **199.241.166.\*** pour la clé SSH dans CCDB et que votre client SSH veut se connecter au nœud avec une adresse IPv6, il se pourrait que la clé ne soit pas acceptée parce que l'adresse source n'est pas comme le masque.

### Comment identifier le problème {#how-to-identify-the-problem}

Si la connexion SSH à un nœud d'automatisation ne se fait pas, faites un test avec la commande

```bash
ssh -i ~/.ssh/automation_key -vvv username@robot.rorqual.alliancecan.ca "ls -l"
```

Ceci essaie d'établir la connexion avec le nœud d'automatisation sur Rorqual et d'exécuter la commande `` `ls -l` `` avec la clé SSH `` `~/.ssh/automation_key` ``. La liste des fichiers contenus dans votre répertoire `/home` sur Rorqual est ensuite affichée.

Cette commande produit beaucoup d'information de débogage à cause de l'option `` `-vvv` `` (*Very Very Verbose*). Si le message dans *Connecting to...* ressemble à

```text
debug1: Connecting to robot.rorqual.alliancecan.ca [199.241.166.5] port 22.
```

l'adressage se fait avec IPv4. Si le message ressemble plutôt à

```text
debug1: Connecting to robot.rorqual.alliancecan.ca [2620:123:7002:4::5] port 22.
```

l'adressage se fait avec IPv6.

### Solutions {#possible-solutions}

*   **Forcer le client SSH à utiliser IPv4 ou IPv6** avec les options `` `-4` `` et `` `-6` `` selon le format utilisé dans CCDB pour la clé.

*   **Pointer au nœud d'automatisation avec l'adresse IP du nœud** plutôt qu'avec son nom; par exemple, sur Rorqual
    ```bash
    ssh -i ~/.ssh/automation_key -vvv username@132.219.138.79 "ls -l"
    ```
    pour forcer SSH à utiliser les adresses IPv4.

*   **Désactiver l'adressage IPv6 sur votre ordinateur** pour faire en sorte que IPv4 soit utilisé.
    Il ne devrait y avoir aucun impact négatif pour votre ordinateur, mais Microsoft ne le recommande pas et vous ne devriez l'utiliser qu'en dernier recours. La méthode de désactivation de l'adressage IPv6 dépend de l'ordinateur et du système d'exploitation.

## Automatisation avec Python et Paramiko {#automation-using-python-and-paramiko}

Si votre flux de travail est automatisé avec le [module Paramiko de Python](https://www.paramiko.org/index.html), voici comment le faire fonctionner avec un nœud d'automatisation :

```python
# ====================================================================================================
#! /usr/bin/env python3
# ====================================================================================================
import os
import paramiko
# ====================================================================================================

key = paramiko.Ed25519Key.from_private_key_file("/home/username/.ssh/cc_allowed")

user = "username"
host = "robot.rorqual.alliancecan.ca"

ssh = paramiko.SSHClient()

# If the host is not known, it is OK.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host, username=user, pkey=key)

cmd = "ls -l"
stdin, stdout, stderr = ssh.exec_command(cmd)

print("".join(stdout.readlines()))

ssh.close()
# ====================================================================================================
```

Ceci établit la connexion au nœud d'automatisation de **Rorqual** avec une clé inscrite dans le portail CCDB et exécute la commande `` `ls -l` `` pour obtenir la liste des fichiers. La liste est ensuite affichée à l'écran.

Remarquez qu'il est important **d'installer Paramiko** avec la commande

```bash
pip install paramiko[all]
```

Ceci fait en sorte que le support pour le type de clés **Ed25519** est aussi installé.