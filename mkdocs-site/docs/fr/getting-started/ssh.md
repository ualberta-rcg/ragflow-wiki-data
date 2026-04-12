---
title: "SSH/fr"
slug: "ssh"
lang: "fr"

source_wiki_title: "SSH/fr"
source_hash: "dd39d58a9943398db31f8c2902c27cde"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:13:39.530674+00:00"

tags:
  - connecting

keywords:
  - "Windows"
  - "algorithme d'échange de clés"
  - "connexion SSH"
  - "X11"
  - "Linux"
  - "authentification multifacteur"
  - "protocole SSH"
  - "serveur X11"
  - "XQuartz"
  - "clés SSH"
  - "client SSH"
  - "erreurs de connexion"
  - "clés hôtes"
  - "macOS"
  - "mise à jour de sécurité"

questions:
  - "Quel est le rôle principal du protocole SSH et dans quels cas est-il utilisé pour interagir avec les grappes de calcul ?"
  - "Quelles sont les informations et les configurations préalables requises pour établir une connexion SSH depuis son ordinateur ?"
  - "Que faut-il installer sur son système d'exploitation local pour pouvoir utiliser des applications graphiques à distance via le protocole X11 ?"
  - "Que faut-il faire si le message d'erreur \"remote host identification has changed\" apparaît lors de la connexion ?"
  - "Quelles versions de clients SSH ou de systèmes d'exploitation doivent être mises à jour pour résoudre les erreurs de chiffrement ou de protocole ?"
  - "Comment doit-on réagir face à l'avertissement \"connection is not using a post-quantum key exchange algorithm\" et comment le masquer ?"
  - "Quel composant logiciel est indispensable pour pouvoir utiliser le système X11 sur un ordinateur ?"
  - "Quelle application externe doit généralement être installée pour faire fonctionner un serveur X11 sous macOS ?"
  - "Quels logiciels permettent de disposer d'un serveur X11 sous Windows selon le texte ?"
  - "Que faut-il faire si le message d'erreur \"remote host identification has changed\" apparaît lors de la connexion ?"
  - "Quelles versions de clients SSH ou de systèmes d'exploitation doivent être mises à jour pour résoudre les erreurs de chiffrement ou de protocole ?"
  - "Comment doit-on réagir face à l'avertissement \"connection is not using a post-quantum key exchange algorithm\" et comment le masquer ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Le protocole SSH (*Secure Shell*) est fréquemment utilisé pour obtenir une connexion sécurisée à une machine à distance. Une connexion SSH est entièrement chiffrée, ce qui comprend les informations d'identification entrées pour se connecter (nom d'utilisateur et mot de passe). Le protocole SSH est employé pour vous connecter à nos grappes afin d'exécuter des commandes, vérifier la progression des tâches ou, dans certains cas, transférer des fichiers.

## Pour vous connecter

Vous avez besoin d'un programme client SSH; il en existe pour la plupart des systèmes d'exploitation.
*   Sous macOS et Linux, le plus utilisé est OpenSSH, une application en ligne de commande installée par défaut.
*   Avec les récentes versions de Windows, SSH est disponible via le terminal PowerShell, dans l'invite `cmd` ou par WSL (Windows Subsystem for Linux). D'autres clients SSH sont aussi offerts par des tiers comme [PuTTY](connecting_with_putty.md), [MobaXTerm](connecting_with_mobaxterm.md), [WinSCP](https://winscp.net/eng/download.php) et [Bitvise](https://www.bitvise.com/ssh-client-download).

Pour utiliser correctement ces clients SSH, vous devez :
*   **Connaître le nom de la machine à laquelle vous voulez vous connecter**; le format ressemble à `fir.alliancecan.ca` ou `trillium.alliancecan.ca`.
*   **Connaître votre nom d'utilisateur (*username*)**; le format ressemble à `ansmith`. Votre nom d'utilisateur **n'est pas** votre adresse de courriel, ni votre CCI (par exemple `abc-123`), ni un CCRI (par exemple `abc-123-01`).
*   **Connaître votre mot de passe ou utiliser une [clé SSH](ssh_keys.md)**. Votre mot de passe est le même que celui que vous utilisez pour [vous connecter au portail CCDB](https://ccdb.alliancecan.ca/). Nous vous recommandons de créer et utiliser une clé SSH, ce qui est plus sécuritaire qu'un mot de passe.
*   **Vous enregistrer à [l'authentification multifacteur](multifactor_authentication.md) et vous souvenir de votre deuxième facteur.**
*   **Vous avez demandé l'[accès au système pour votre compte](https://ccdb.alliancecan.ca/me/access_systems).**

Dans un client ligne de commande (*par exemple* /Applications/Utilities/Terminal.app sous macOS; cmd ou PowerShell sous Windows), utilisez la commande `ssh` ainsi :

```bash
ssh username@machine_name
```

Pour plus d'information sur les clients graphiques comme MobaXterm ou PuTTY, consultez :
*   [Connexion à un serveur avec MobaXTerm](connecting_with_mobaxterm.md)
*   [Connexion à un serveur avec PuTTY](connecting_with_putty.md)

À votre première connexion à une machine, on vous demandera d'enregistrer une copie de sa clé hôte (*host key*); cette clé est un identifiant unique avec lequel le client SSH vérifie s'il s'agit de la même machine quand vous vous connectez par la suite.

Pour plus d'information sur comment générer des paires de clés, voir :
*   [Clés SSH](ssh_keys.md)
    *   [Générer des clés SSH sous Windows](generating_ssh_keys_in_windows.md)
    *   [Utiliser des clés SSH sous Linux](using_ssh_keys_in_linux.md)
Pour permettre la communication entre les nœuds de calcul et l'internet, voir :
*   [Tunnels SSH](ssh_tunnelling.md)
Pour simplifier la connexion avec un fichier de configuration, voir :
*   [Fichier de configuration SSH](ssh_configuration_file.md)

## X11 pour les applications graphiques

SSH prend en charge les applications graphiques via le protocole [X](https://fr.wikipedia.org/wiki/X_Window_System), connu sous le nom de X11. Pour utiliser X11, un serveur X11 doit être installé sur votre ordinateur. Sous Linux, un serveur X11 sera habituellement déjà installé, mais sous macOS vous devrez généralement installer un paquet externe tel que [XQuartz](https://www.xquartz.org). Sous Windows, MobaXterm est fourni avec un serveur X11; avec PuTTY, le serveur est [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

En ligne de commande SSH, ajoutez l'option `-Y` pour permettre les communications X11.

```bash
ssh -Y username@machine_name
```

## Erreurs de connexion

Il est possible que vous receviez un message d'erreur lors de votre connexion à une grappe :
*   *no matching cipher found*
*   *no matching MAC found*
*   *unable to negotiate a key exchange method*
*   *couldn't agree a key exchange algorithm*
*   *remote host identification has changed*

Ce dernier message peut indiquer une attaque de l'homme du milieu (*man-in-the-middle attack*) ou une mise à jour de la sécurité pour la grappe à laquelle vous voulez vous connecter. Si ce message est affiché, vérifiez si l'empreinte de la clé hôte mentionnée correspond à une des [clés hôtes valides](ssh_host_keys.md); si c'est le cas, vous pouvez poursuivre la connexion.
Si la clé hôte n'est pas dans la liste, fermez la connexion et contactez le [soutien technique](../support/technical_support.md).

Les utilisateurs de Niagara ont eu [des mesures à prendre](https://docs.scinet.utoronto.ca/index.php/SSH_Changes_in_May_2019) suite à la mise à jour de sécurité du 31 mai 2019. Des mises à jour semblables ont été effectuées sur les autres grappes vers la fin de septembre 2019; pour plus d'information, consultez la [page wiki sur l'amélioration de la sécurité](ssh_security_improvements.md).

Dans le cas des autres messages d'erreur, vous devrez effectuer la mise à jour de votre système d'exploitation et/ou de votre client SSH pour permettre un chiffrement plus robuste, des protocoles d'échange de clés et des algorithmes MAC (*message authentication code*).

Ces erreurs sont connues pour les versions suivantes qui devront être mises à jour :
*   OpenSSH sous CentOS/RHEL 5
*   [PuTTY](connecting_with_putty.md) v0.64 et moins, sous Windows

## Avertissements

### *connection is not using a post-quantum key exchange algorithm*

Nous vous recommandons de ne pas tenir compte de cet avertissement. Il indique que si du trafic chiffré est enregistré aujourd'hui, un ordinateur hypothétique du futur (par exemple, un ordinateur quantique) pourrait le déchiffrer. Il s'agit simplement d'une question de longueur de clé pouvant être devinée par force brute; ce n'est donc ni nouveau ni urgent. Nous ne prévoyons pas reconfigurer nos systèmes à court terme. Vous pouvez éviter cet avertissement en configurant votre client SSH avec l'option `WarnWeakCrypto no`, comme [indiqué dans le message d'avertissement](https://www.openssh.org/pq.html).