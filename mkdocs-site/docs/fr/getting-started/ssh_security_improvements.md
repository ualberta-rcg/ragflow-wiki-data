---
title: "SSH security improvements/fr"
slug: "ssh_security_improvements"
lang: "fr"

source_wiki_title: "SSH security improvements/fr"
source_hash: "56a1fa72ab2c95e52ee5b4b3e3ff168c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:18:50.474317+00:00"

tags:
  []

keywords:
  - "attaques de l'homme du milieu"
  - "grappe Graham"
  - "sécurité"
  - "clé publique"
  - "serveur hôte"
  - "avertissement"
  - "algorithmes de chiffrement"
  - "dépannage"
  - "clés hôtes"
  - "impossibilité de se connecter"
  - "mise à jour"
  - "messages d'erreur"
  - "SSH"
  - "connexion SSH"
  - "empreintes de clés hôtes"
  - "authentification"
  - "clients compatibles"
  - "clés SSH"
  - "client SSH"
  - "OpenSSH"

questions:
  - "Pourquoi les administrateurs ont-ils décidé de modifier les politiques et pratiques de sécurité SSH en 2019 ?"
  - "Quelles sont les trois modifications techniques spécifiques apportées aux grappes Graham, Béluga et Cedar ?"
  - "Que signifie l'avertissement de sécurité concernant l'identification de l'hôte distant lors de la connexion et comment l'utilisateur doit-il y réagir ?"
  - "Comment peut-on supprimer une ancienne clé hôte de son système sous macOS ou Linux pour résoudre un avertissement de sécurité ?"
  - "Que doit-on impérativement vérifier avant d'accepter une nouvelle clé hôte lors d'une connexion SSH ?"
  - "Pour quelle raison une clé SSH précédemment fonctionnelle peut-elle cesser de fonctionner et exiger un mot de passe, et comment y remédier ?"
  - "Que signifie l'avertissement d'échec de vérification de la clé hôte lors d'une connexion SSH ?"
  - "Quel type de cyberattaque ce mécanisme de vérification des clés vise-t-il à prévenir ?"
  - "Sur quels appareils cet avertissement de sécurité s'affichera-t-il après la modification des clés hôtes ?"
  - "Comment configurer l'authentification par clé publique sur un serveur distant pour remplacer l'utilisation d'un mot de passe ?"
  - "Que signifie le message d'erreur \"no matching cipher found\" lors d'une tentative de connexion au serveur ?"
  - "Comment résoudre le problème de connexion lié à l'erreur \"no matching key exchange method found\" sur le port 22 ?"
  - "Que signifie l'erreur de connexion SSH « no matching mac found » et quelle est la solution recommandée pour la résoudre ?"
  - "Quels sont les clients SSH et les systèmes d'exploitation spécifiques listés comme étant compatibles avec cette configuration ?"
  - "Comment récupérer et vérifier les empreintes de clés hôtes, et quelle procédure suivre en cas de non-correspondance ?"
  - "Que signifie l'erreur de connexion SSH « no matching mac found » et quelle est la solution recommandée pour la résoudre ?"
  - "Quels sont les clients SSH et les systèmes d'exploitation spécifiques listés comme étant compatibles avec cette configuration ?"
  - "Comment récupérer et vérifier les empreintes de clés hôtes, et quelle procédure suivre en cas de non-correspondance ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! info "Amélioration de la sécurité SSH"
    SSH est le protocole de connexion à nos grappes. Pour protéger les communications, SSH vérifie l'identité du serveur et de l'utilisateur en les comparant aux identités connues, et assure le chiffrement de la connexion. Comme la sécurité est périodiquement menacée par de nouveaux risques, nous n'offrons plus de soutien pour certaines options de SSH qui ne sont plus jugées sécuritaires; vous devrez donc effectuer les modifications expliquées ci-dessous.

## Modifications apportées en septembre et octobre 2019

Des courriels importants expliquant ces modifications ont été envoyés aux utilisateurs les 29 juillet et 16 septembre 2019.

La puissance de traitement de plus en plus forte fait en sorte que certains algorithmes et protocoles de chiffrement, qui étaient suffisamment efficaces il y a 10 ou 15 ans, présentent aujourd’hui un risque d’intrusion par des tiers. Nous avons donc modifié nos politiques et pratiques concernant [SSH](ssh.md), l’outil principal utilisé pour offrir des connexions sécurisées à nos grappes. Il vous faut mettre à jour la copie locale de la clé hôte qui identifie chaque grappe. De plus, dans certains cas, il sera nécessaire de mettre à jour le logiciel du client SSH et/ou de générer une nouvelle paire de clés.

### Quelles sont les modifications?

Les modifications suivantes ont été apportées le 24 septembre 2019 pour Graham et une semaine plus tard pour Béluga et Cedar :

1.  Désactivation de certains algorithmes de chiffrement.
2.  Désactivation de certains types de clés publiques.
3.  Régénération des clés hôtes.

Même si certains de ces termes vous sont inconnus, les directives suivantes vous aideront à vous préparer adéquatement. Si les tests proposés ci-dessous indiquent que vous devez changer ou mettre à jour votre client SSH, [cette autre page](ssh.md) pourrait vous être utile.

Les utilisateurs d'Arbutus ne sont pas touchés puisque la connexion se fait par interface web et non via SSH.

Il est possible que quelques-uns de ces messages et erreurs aient été produits par suite de [mises à jour pour Niagara](https://docs.scinet.utoronto.ca/index.php/SSH_Changes_in_May_2019) effectuées le 31 mai 2019 et pour Graham au début d'août.

### Mise à jour de la liste des hôtes de votre client

Quand les modifications seront complétées, un avertissement semblable au suivant sera probablement affiché la première fois que vous vous connecterez à une grappe.

```console
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

!!! warning "Avertissement : l'identification de l'hôte distant a changé!"
    Cet avertissement indique que les clés hôtes de la grappe (ici la grappe Graham) ont été modifiées et que le logiciel de votre client SSH se souvient des clés antérieures. Ceci se produit pour contrer les [attaques de l'homme du milieu](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu). L'avertissement sera affiché sur chaque ordinateur à partir duquel vous vous connectez.

    Vous pourriez aussi recevoir un avertissement de mystification (*DNS spoofing*) dû également à une telle modification.

#### MobaXterm, PuTTY, WinSCP

Sous Windows, avec un client [MobaXterm](connecting_with_mobaxterm.md), [PuTTY](connecting_with_putty.md) ou [WinSCP](https://winscp.net/eng/download.php), l'avertissement sera affiché dans une fenêtre et vous serez invité à accepter la nouvelle clé en cliquant sur **Oui**. Avant de cliquer, assurez-vous que l'empreinte se trouve dans la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-clés-hôtes). Si elle ne s'y trouve pas, contactez le [soutien technique](../support/technical_support.md).

#### macOS, Linux, GitBash, Cygwin

Si vous utilisez `ssh` en ligne de commande, une de ces commandes fera en sorte que votre système *oublie* l'ancienne clé hôte :

*   Graham
    ```bash
    for h in 2620:123:7002:4::{2..5} 199.241.166.{2..5} {gra-login{1..3},graham,gra-dtn,gra-dtn1,gra-platform,gra-platform1}.{sharcnet,computecanada}.ca; do ssh-keygen -R $h; done
    ```
*   Cedar
    ```bash
    for h in 206.12.124.{2,6} cedar{1,5}.cedar.computecanada.ca cedar.computecanada.ca; do ssh-keygen -R $h; done
    ```
*   Beluga
    ```bash
    for h in beluga{,{1..4}}.{computecanada,calculquebec}.ca 132.219.136.{1..4}; do ssh-keygen -R $h; done
    ```
*   Mp2
    ```bash
    for h in ip{15..20}-mp2.{computecanada,calculquebec}.ca 204.19.23.2{15..20}; do ssh-keygen -R $h; done
    ```

La prochaine fois que vous vous connecterez par SSH, vous devrez confirmer les nouvelles clés, par exemple :

```console
$ ssh graham.computecanada.ca
The authenticity of host 'graham.computecanada.ca (142.150.188.70)' can't be established.
ED25519 key fingerprint is SHA256:mf1jJ3ndpXhpo0k38xVxjH8Kjtq3o1+ZtTVbeM0xeCk.
ED25519 key fingerprint is MD5:bc:93:0c:64:f7:e7:cf:d9:db:81:40:be:4d:cd:12:5c.
Are you sure you want to continue connecting (yes/no)?
```

Avant d'entrer **oui**, assurez-vous que l'empreinte se trouve dans la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-clés-hôtes). Si elle ne s'y trouve pas, contactez le [soutien technique](../support/technical_support.md).

### Dépannage

Voir la liste des [empreintes de clés hôtes ci-dessous](#empreintes-de-clés-hôtes).

#### Ma clé SSH ne fonctionne plus

Si on vous demande un mot de passe, mais que vous avez utilisé des clés SSH par le passé, il est probable que ce soit dû à la désactivation des clés DSA et RSA 1024 bits.

Il vous faudra générer une nouvelle clé plus forte. La méthode est différente selon que vous êtes sous [Windows](generating_ssh_keys_in_windows.md) ou [Linux/macOS](using_ssh_keys_in_linux.md). Dans ce dernier cas, la référence décrit aussi comment ajouter votre nouvelle clé publique au serveur hôte à distance pour que l'authentification se fasse par la clé plutôt que par mot de passe.

#### Impossibilité de se connecter

Les messages d'erreur suivants :
```console
Unable to negotiate with 142.150.188.70 port 22: no matching cipher found.
Unable to negotiate with 142.150.188.70 port 22: no matching key exchange method found.
Unable to negotiate with 142.150.188.70 port 22: no matching mac found.
```
indiquent que vous devez effectuer la mise à jour de votre client SSH et utiliser une version compatible parmi celles listées ci-dessous.

#### Clients compatibles

**La liste suivante n'est pas complète**, mais nous avons testé la configuration avec ces clients; il est possible que les versions antérieures de ces clients ne soient pas compatibles. Nous vous recommandons de mettre à jour votre système d'exploitation et votre client SSH.

##### Linux

*   OpenSSH_7.4p1, OpenSSL 1.0.2k-fips (CentOS 7.5, 7.6)
*   OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13, OpenSSL 1.0.1f (Ubuntu 14)

##### OS X

Pour connaître la version de votre client SSH, utilisez la commande `ssh -V`.

*   OpenSSH 7.4p1, OpenSSL 1.0.2k (Homebrew)
*   OpenSSH 7.9p1, LibreSSL 2.7.3 (OS X 10.14.5)

##### Windows

*   [MobaXterm Home Edition](connecting_with_mobaxterm.md) v11.1
*   [PuTTY](connecting_with_putty.md) 0.72
*   Windows Subsystem for Linux (WSL) v1
    *   Ubuntu 18.04 (OpenSSH_7.6p1 Ubuntu-4ubuntu0.3, OpenSSL 1.0.2n)
    *   openSUSE Leap 15.1 (OpenSSH_7.9p1, OpenSSL 1.1.0i-fips)

##### iOS

*   Termius, 4.3.12

## Empreintes de clés hôtes

Les commandes suivantes servent à récupérer les empreintes de clés hôtes à distance :

```bash
ssh-keyscan <hostname> | ssh-keygen -E md5 -l -f -
```

```bash
ssh-keyscan <hostname> | ssh-keygen -E sha256 -l -f -
```

Les empreintes pour les grappes de Calcul Canada sont listées ci-dessous.

!!! warning "Vérification des empreintes de clés hôtes"
    Si l'empreinte que vous recevez ne correspond à aucune de cette liste, n'acceptez pas la connexion et contactez le [soutien technique](../support/technical_support.md).