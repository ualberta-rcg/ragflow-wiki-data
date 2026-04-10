---
title: "SSH/fr"
tags:
  - connecting

keywords:
  []
---

Le protocole SSH (<i>Secure Shell</i>) est fréquemment utilisé pour obtenir une connexion sécurisée à une machine à distance. Une connexion SSH est entièrement chiffrée, ce qui comprend les informations d'identification entrées pour se connecter (nom d'utilisateur et mot de passe). Le protocole SSH est employé pour vous connecter à nos grappes afin d'exécuter des commandes, vérifier la progression des tâches ou, dans certains cas, transférer des fichiers.

<span id="What_you_need"></span>
= Pour vous connecter =

Vous avez besoin d'un programme client SSH; il en existe pour la plupart des systèmes d'exploitation.
*Sous macOS et Linux, le plus utilisé est OpenSSH, une application en ligne de commande installée par défaut.
*Avec les récentes versions de Windows,  SSH est disponible via le terminal PowerShell, dans l'invite `cmd` ou par WSL (Windows Subsystem for Linux). D'autres clients SSH sont aussi offerts par des tiers comme [PuTTY](connecting-with-putty-fr.md), [MobaXTerm](connecting-with-mobaxterm-fr.md), [WinSCP](https://winscp.net/eng/download.php) et [Bitvise](https://www.bitvise.com/ssh-client-download). 

Pour utiliser correctement ces clients SSH, vous devez&nbsp;:
* <b>Connaître le nom de la machine à laquelle vous voulez vous connecter</b>; le format ressemble à `fir.alliancecan.ca` ou `trillium.alliancecan.ca`.
* <b>Connaître votre nom d'utilisateur (<i>username</i>)</b>; le format ressemble à `ansmith`. Votre nom d'utilisateur <b>n'est pas</b> votre adresse de courriel, ni votre CCI (par exemple code>abc-123</code>), ni un CCRI (par exemple `abc-123-01`).
* <b>Connaître votre mot de passe ou utiliser une [clé SSH](ssh-keys-fr.md)</b>. Votre mot de passe est le même que celui que vous utilisez pour [vous connecter au portail CCDB](https://ccdb.alliancecan.ca/). Nous vous recommandons de créer et utiliser une clé SSH, ce qui est plus sécuritaire qu'un mot de passe. 
* <b> Vous enregistrer à [l'authentification multifacteur](multifactor-authentication-fr.md) et vous souvenir de votre deuxième facteur.</b>
* <b>Vous avez demandé l'[accès au système pour votre compte](https://ccdb.alliancecan.ca/me/access_systems).</b>

Dans un client ligne de commande (<i>par exemple</i> /Applications/Utilities/Terminal.app sous macOS; cmd ou PowerShell sous Windows), utilisez la commande `ssh` ainsi

```bash
ssh username@machine_name
```

Pour plus d'information sur les clients graphiques comme MobaXterm ou PuTTY, consultez
*[Connexion à un serveur avec MobaXTerm](connecting_with_mobaxterm-fr.md)
*[Connexion à un serveur avec PuTTY](connecting-with-putty-fr.md)

À votre première connexion à une machine, on vous demandera d'enregistrer une copie de sa clé hôte (<i>host key</i>); cette clé est un identifiant unique avec lequel le client SSH vérifie s'il s'agit de la même machine quand vous vous connectez par la suite. 

Pour plus d'information sur comment générer des paires de clés, voir
*[Clés SSH](ssh-keys-fr.md)
**[Générer des clés SSH sous Windows](generating-ssh-keys-in-windows-fr.md)
**[Utiliser des clés SSH sous Linux](using-ssh-keys-in-linux-fr.md)
Pour permettre la communication entre les nœuds de calcul et l'internet, voir
*[Tunnels SSH](ssh-tunnelling-fr.md)
Pour simplifier la connexion avec un fichier de  configuration, voir
*[Fichier de configuration SSH](ssh-configuration-file-fr.md)

<span id="X11_for_graphical_applications"></span>
= X11 pour les applications graphiques =

SSH prend en charge les applications graphiques via le protocole [X](https://fr.wikipedia.org/wiki/X_Window_System), connu sous le nom de X11. Pour utiliser X11, un serveur X11 doit être installé sur votre ordinateur. Sous Linux, un serveur X11 sera habituellement déjà installé, mais sous macOS vous devrez généralement installer un paquet externe tel que [XQuartz](https://www.xquartz.org). Sous Windows, MobaXterm est fourni avec un serveur X11; avec PuTTY, le serveur est  [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

En ligne de commande SSH, ajoutez l'option `-Y` pour permettre les communications X11.

```bash
ssh -Y username@machine_name
```

= Erreurs de connexion =
Il est possible que vous receviez un message d'erreur lors de votre connexion à une grappe &nbsp;:
* <i>no matching cipher found</i>
* <i>no matching MAC found</i>
* <i>unable to negotiate a key exchange method</i>
* <i>couldn't agree a key exchange algorithm</i>
* <i>remote host identification has changed</i>

Ce dernier message peut indiquer une attaque de l'homme du milieu (<i>man-in-the-middle attack</i>) ou une mise à jour de la sécurité pour la grappe à laquelle vous voulez vous connecter. Si ce message est affiché, vérifiez si l'empreinte (<i>fingerprint</i>) de la clé hôte mentionnée correspond à une des [clés hôtes valides](ssh-host-keys.md); si c'est le cas, vous pouvez poursuivre la connexion.
Si la clé hôte n'est pas dans la liste, fermez la connexion et contactez le [soutien technique](technical-support-fr.md).

Les utilisateurs de Niagara ont eu  [des mesures à prendre](https://docs.scinet.utoronto.ca/index.php/SSH_Changes_in_May_2019) suite à la mise à jour de sécurité du 31 mai 2019. Des mises à jour semblables ont été effectuées sur les autres grappes vers la fin de septembre 2019; pour plus d'information, consultez la [page wiki sur l'amélioration de la sécurité](ssh-security-improvements-fr.md).

Dans le cas des autres messages d'erreur, vous devrez effectuer la mise à jour de votre système d'exploitation et/ou de votre client SSH pour permettre un chiffrement plus robuste, des protocoles d'échange de clés et des algorithmes MAC (<i>message authentication code</i>).

Ces erreurs sont connues pour les versions suivantes qui devront être mises à jour :
* OpenSSH sous CentOS/RHEL 5
* [PuTTY](connecting-with-putty-fr.md) v0.64 et moins, sous Windows

<span id="Warnings"></span>
= Avertissements =

## <i>connection is not using a post-quantum key exchange algorithm</i> 

Nous vous recommandons de ne pas tenir compte de cet avertissement. Il indique que si du trafic chiffré est enregistré aujourd'hui, un ordinateur hypothétique du futur (par exemple, un ordinateur quantique) pourrait le déchiffrer. Il s'agit simplement d'une question de longueur de clé pouvant être devinée par force brute; ce n'est donc ni nouveau ni urgent. Nous ne prévoyons pas  reconfigurer nos systèmes à court terme. Vous pouvez éviter cet avertissement en configurant votre client SSH avec l'option `WarnWeakCrypto no`, comme [indiqué dans le message d'avertissement](https://www.openssh.org/pq.html) .