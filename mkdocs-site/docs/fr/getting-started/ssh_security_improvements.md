---
title: "SSH security improvements/fr"
slug: "ssh_security_improvements"
lang: "fr"

source_wiki_title: "SSH security improvements/fr"
source_hash: "56a1fa72ab2c95e52ee5b4b3e3ff168c"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:08:02.246040+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

SSH est le protocole de connexion à nos grappes. Pour protéger les communications, SSH vérifie l'identité du serveur et de l'utilisateur en les comparant aux identités connues, et effectue le chiffrement de la connexion. La sécurité étant périodiquement menacée par de nouveaux risques, nous n'offrons pas le soutien pour certaines options de SSH qui ne sont plus jugées sécuritaires; vous devrez donc effectuer les modifications expliquées ci-dessous.

## Modifications apportées en septembre et octobre 2019

Des courriels importants expliquant ces modifications ont été envoyés aux utilisateurs les 29 juillet et 16 septembre 2019.

La puissance de traitement de plus en plus forte fait en sorte que certains algorithmes et protocoles de chiffrement qui étaient suffisamment efficaces il y a 10 ou 15 ans présentent aujourd’hui un risque d’intrusion par des tierces parties. Nous avons donc modifié nos politiques et pratiques en rapport avec [SSH](ssh.md), l’outil principal utilisé pour offrir des connexions sécurisées à nos grappes. Vous devez mettre à jour la copie locale de la clé hôte qui identifie chacune des grappes. De plus, dans certains cas, il sera nécessaire de mettre à jour le logiciel du client SSH et/ou de générer une nouvelle paire de clés.

## Quelles sont les modifications?

Les modifications suivantes ont été apportées le 24 septembre 2019 pour Graham et une semaine plus tard pour Béluga et Cedar :

1.  Désactivation de certains algorithmes de chiffrement.
2.  Désactivation de certains types de clés publiques.
3.  Régénération des clés hôtes.

Même si certains de ces termes vous sont inconnus, les directives suivantes vous aideront à vous préparer adéquatement. Si les tests proposés ci-dessous indiquent que vous devez changer ou mettre à jour votre client SSH, [cette autre page](ssh.md) pourrait vous être utile.

Les utilisateurs d'Arbutus ne sont pas touchés puisque la connexion se fait par interface web et non via SSH.

Il est possible que quelques-uns de ces messages et erreurs aient été produits par suite de [mises à jour pour Niagara](https://docs.scinet.utoronto.ca/index.php/SSH_Changes_in_May_2019) effectuées le 31 mai 2019 et pour Graham au début d'août.

## Mise à jour de la liste des hôtes de votre client

Quand les modifications seront complétées, un avertissement semblable au suivant sera probablement affiché la première fois que vous vous connecterez à une grappe.

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:mf1jJ3ndpXhpo0k38xVxjH8Kjtq3o1+ZtTVbeM0xeCk.
Please contact your system administrator.
Add correct host key in /home/username/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/username/.ssh/known_hosts:109
ED25519 host key for graham.computecanada.ca has changed and you have requested strict checking.
Host key verification failed.
Killed by signal 1.
```

Cet avertissement indique que les clés hôtes de la grappe (ici la grappe Graham) ont été modifiées et que le logiciel de votre client SSH se souvient des clés antérieures. Ceci se produit pour contrer les [attaques de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu). L'avertissement sera affiché sur chaque ordinateur à partir duquel vous vous connectez.

Vous pourriez aussi recevoir un avertissement de mystification (*DNS spoofing*) dû également à une telle modification.

### MobaXterm, PuTTY, WinSCP

Sous Windows, avec un client [MobaXterm](connecting-with-mobaxterm.md), [PuTTY](connecting-with-putty.md) ou [WinSCP](https://winscp.net/eng/download.php), l'avertissement sera affiché dans une fenêtre et vous serez invité à accepter la nouvelle clé en cliquant sur **Oui**. Avant de cliquer, assurez-vous que l'empreinte se trouve dans la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-cles-hotes). Si elle ne s'y trouve pas, contactez le [soutien technique](technical-support.md).

### macOS, Linux, GitBash, Cygwin

Si vous utilisez `ssh` en ligne de commande, une de ces commandes fera en sorte que votre système *oublie* l'ancienne clé hôte :

**Graham**
```bash
for h in 2620:123:7002:4::{2..5} 199.241.166.{2..5} {gra-login{1..3},graham,gra-dtn,gra-dtn1,gra-platform,gra-platform1}.{sharcnet,computecanada}.ca; do ssh-keygen -R $h; done
```

**Cedar**
```bash
for h in 206.12.124.{2,6} cedar{1,5}.cedar.computecanada.ca cedar.computecanada.ca; do ssh-keygen -R $h; done
```

**Beluga**
```bash
for h in beluga{,{1..4}}.{computecanada,calculquebec}.ca 132.219.136.{1..4}; do ssh-keygen -R $h; done
```

**Mp2**
```bash
for h in ip{15..20}-mp2.{computecanada,calculquebec}.ca 204.19.23.2{15..20}; do ssh-keygen -R $h; done
```

La prochaine fois que vous vous connecterez par SSH, vous devrez confirmer les nouvelles clés, par exemple

```bash
$ ssh graham.computecanada.ca
The authenticity of host 'graham.computecanada.ca (142.150.188.70)' can't be established.
ED25519 key fingerprint is SHA256:mf1jJ3ndpXhpo0k38xVxjH8Kjtq3o1+ZtTVbeM0xeCk.
ED25519 key fingerprint is MD5:bc:93:0c:64:f7:e7:cf:d9:db:81:40:be:4d:cd:12:5c.
Are you sure you want to continue connecting (yes/no)? oui
```

Avant d'entrer **oui**, assurez-vous que l'empreinte se trouve dans la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-cles-hotes). Si elle ne s'y trouve pas, contactez le [soutien technique](technical-support.md).

## Dépannage

Voir la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-cles-hotes).

### Ma clé SSH ne fonctionne plus

Si on vous demande un mot de passe mais que vous utilisiez les clés SSH par le passé, il est probable que ce soit dû à la désactivation des clés DSA et RSA 1024 bits.

Il vous faudra générer une nouvelle clé plus forte. La méthode est différente selon que vous êtes sous [Windows](generating-ssh-keys-in-windows.md) ou [Linux/macOS](using-ssh-keys-in-linux.md). Dans ce dernier cas, la référence décrit aussi comment ajouter votre nouvelle clé publique au serveur hôte à distance pour que l'authentification se fasse par la clé plutôt par mot de passe.

### Impossibilité de se connecter

Les messages d'erreur suivants
```text
Unable to negotiate with 142.150.188.70 port 22: no matching cipher found.
Unable to negotiate with 142.150.188.70 port 22: no matching key exchange method found.
Unable to negotiate with 142.150.188.70 port 22: no matching mac found.
```
indiquent que vous devez effectuer la mise à jour de votre client SSH et utiliser une version compatible parmi celles listées ci-dessous.

### Clients compatibles

**La liste suivante n'est pas complète**, mais nous avons testé la configuration avec ces clients; il est possible que les versions antérieures de ces clients ne soient pas compatibles. Nous vous recommandons de mettre à jour votre système d'exploitation et votre client SSH.

#### Linux

*   OpenSSH_7.4p1, OpenSSL 1.0.2k-fips (CentOS 7.5, 7.6)
*   OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13, OpenSSL 1.0.1f (Ubuntu 14)

#### macOS

Pour connaître la version de votre client SSH, utilisez la commande `ssh -V`.

*   OpenSSH 7.4p1, OpenSSL 1.0.2k (Homebrew)
*   OpenSSH 7.9p1, LibreSSL 2.7.3 (macOS 10.14.5)

#### Windows

*   [MobaXterm Home Edition](connecting-with-mobaxterm.md) v11.1
*   [PuTTY](connecting-with-putty.md) 0.72
*   Windows Services for Linux (WSL) v1
    *   Ubuntu 18.04 (OpenSSH_7.6p1 Ubuntu-4ubuntu0.3, OpenSSL 1.0.2n)
    *   openSUSE Leap 15.1 (OpenSSH_7.9p1, OpenSSL 1.1.0i-fips)

#### iOS

*   Termius, 4.3.12

## Empreintes de clés hôtes

Les commandes suivantes servent à récupérer les empreintes de clés hôtes à distance :

```bash
ssh-keyscan <hostname> | ssh-keygen -E md5 -l -f -
ssh-keyscan <hostname> | ssh-keygen -E sha256 -l -f -
```

Les empreintes pour les grappes de Calcul Canada sont listées ci-dessous. Si l'empreinte que vous recevez ne correspond à aucune de cette liste, n'acceptez pas la connexion et contactez le [soutien technique](technical-support.md).