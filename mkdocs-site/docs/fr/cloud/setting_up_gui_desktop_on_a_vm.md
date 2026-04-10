---
title: "Setting up GUI Desktop on a VM/fr"
tags:
  - cloud

keywords:
  []
---

Certains logiciels que vous pouvez installer sur votre machine virtuelle (VM ou instance) sont accessibles uniquement, ou préférablement, via leur interface utilisateur graphique (GUI). Vous pouvez utiliser une interface graphique avec la redirection X11, mais vous pourriez obtenir une meilleure performance en utilisant VNC pour vous connecter à une session graphique qui se trouve sur votre instance.

Nous décrivons ici les étapes pour configurer une interface de bureau   avec VNC sur une instance qui utilise le système d’exploitation Ubuntu.

<ol>
<li> Sur votre instance, installez un bureau ayant une interface graphique. Plusieurs paquets sont disponibles pour Ubuntu :

* [ubuntu-unity-desktop](https://ubuntuunity.org/|)
* [ubuntu-mate-desktop](https://ubuntu-mate.org/|)
* [lubuntu-desktop](https://lubuntu.net/|)
* [xubuntu-desktop](https://xubuntu.org/screenshots/|)
* [xfce4](https://www.xfce.org/|)
* ubuntu-desktop
* [kde-plasma-desktop](https://kde.org/plasma-desktop/|)
* ubuntu-desktop-minimal
* [cinnamon](https://en.wikipedia.org/wiki/Cinnamon_(desktop_environment)|)
* [icewm](https://ice-wm.org/|)

[Cet article montre quelques-uns de ces bureaux](https://cloudinfrastructureservices.co.uk/best-ubuntu-desktop-environments). Les commandes suivantes installent un bureau MATE.

```bash
sudo apt install ubuntu-mate-desktop
```

Au cours de l'installation du paquet  `ubuntu-mate-desktop` vous devez sélectionner le gestionnaire de session par défaut; le meilleur choix serait  [Cette installation peut souvent prendre de 15 à 30 minutes.
</li>
<li>Installez le serveur TigerVNC.

Ce logiciel installé sur votre instance permet d’utiliser l’interface de bureau que vous avez installée à l’étape 1.

```bash
sudo apt install -y tigervnc-common tigervnc-standalone-server
```

Cette commande installe le serveur TigerVNC et les logiciels nécessaires. Pour plus d’information sur les serveurs VNC, voyez [[VNC/fr|notre page wiki VNC](https://en.wikipedia.org/wiki/LightDM|`lightdm`].)].
</li>
<li>Démarrez le serveur VNC.

```bash
vncserver
```

```
-> enter a password
-> enter "n" for view-only password
```
 Au premier démarrage du serveur VNC, vous devez entrer un mot de passe qui vous servira à vous connecter au bureau VNC. Il n’est pas nécessaire que le mot de passe soit pour lecture seulement. Pour modifier votre mot de passe, utilisez la commande `vncpasswd`.
</li>
<li>Testez la connexion en ouvrant le port 5901 (pour savoir comment ouvrir un port vers votre instance OpenStack, voir [Groupes de sécurité](managing_your_cloud_resources_with_openstack-fr#groupes_de_sécurité.md)) et connectez-vous avec un client VNC, par exemple [TigerVNC](https://tigervnc.org/). Cette option n’est pas sécuritaire parce que les données entrant et sortant de l’instance ne seront pas chiffrées. Par contre, cette étape vous permet de tester la connexion client-serveur avant de vous connecter de façon sécuritaire via un tunnel SSH; vous pouvez ignorer cette étape si vous savez comment configurer un tunnel SSH correctement.
</li>
Connectez-vous via un [tunnel SSH](ssh_tunnelling-fr.md). [Vous pouvez consulter cet exemple qui utilise un noeud de calcul sur nos grappes.](vnc-fr#noeuds_de_calcul.md)  Pour vous connecter sous Linux ou Mac :<li>

*Ouvrez votre terminal.
*Dans votre terminal local, entrez `SSH -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM`
*Lancez votre client VNC.
*Dans le champ pour le serveur VNC, entrez `localhost:5901`.
*Le bureau graphique pour votre session à distance devrait s’ouvrir. 
</li>
<li> Fermez le port 5901; ce port ne sert plus après que la connexion avec le serveur VNC est établie via un tunnel SSH et il est recommandé de [supprimer cette règle dans vos groupes de sécurité](managing_your_cloud_resources_with_openstack-fr#groupes_de_sécurité.md).
</li>
<li> Quand vous n’avez plus besoin du bureau, arrêtez le serveur VNC avec

```bash
vncserver -kill :1
```

</ol>