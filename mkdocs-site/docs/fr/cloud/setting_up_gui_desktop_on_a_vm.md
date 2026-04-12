---
title: "Setting up GUI Desktop on a VM/fr"
slug: "setting_up_gui_desktop_on_a_vm"
lang: "fr"

source_wiki_title: "Setting up GUI Desktop on a VM/fr"
source_hash: "96de8b2cc02dea39a8d8f3797083755b"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:29:02.878950+00:00"

tags:
  - cloud

keywords:
  - "machine virtuelle"
  - "Cloud"
  - "bureau graphique"
  - "tunnel SSH"
  - "interface graphique"
  - "serveur VNC"
  - "port 5901"
  - "groupes de sécurité"
  - "Ubuntu"
  - "vncserver"
  - "arrêter"
  - "client VNC"
  - "bureau"

questions:
  - "Comment installer un environnement de bureau graphique sur une machine virtuelle Ubuntu ?"
  - "Quelles sont les étapes nécessaires pour installer, configurer et démarrer le serveur TigerVNC ?"
  - "Comment sécuriser la connexion à la session graphique VNC à l'aide d'un tunnel SSH ?"
  - "Quelle adresse doit-on saisir dans le client VNC pour se connecter au serveur ?"
  - "Quel est le résultat attendu une fois la configuration du client VNC correctement effectuée ?"
  - "Pourquoi est-il recommandé de fermer le port 5901 et de modifier les groupes de sécurité après l'établissement de la connexion ?"
  - "Quelle commande permet d'arrêter le serveur VNC ?"
  - "Dans quelle situation doit-on procéder à l'arrêt du serveur ?"
  - "À quelle catégorie informatique cette instruction est-elle associée ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Certains logiciels que vous pouvez installer sur votre machine virtuelle (VM ou instance) sont accessibles uniquement, ou préférablement, via leur interface utilisateur graphique (GUI). Vous pouvez utiliser une interface graphique avec la redirection X11, mais vous pourriez obtenir une meilleure performance en utilisant VNC pour vous connecter à une session graphique qui se trouve sur votre instance.

Nous décrivons ici les étapes pour configurer une interface de bureau avec VNC sur une instance qui utilise le système d’exploitation Ubuntu.

1.  Sur votre instance, installez un bureau ayant une interface graphique. Plusieurs paquets sont disponibles pour Ubuntu :
    *   [ubuntu-unity-desktop](https://ubuntuunity.org/)
    *   [ubuntu-mate-desktop](https://ubuntu-mate.org/)
    *   [lubuntu-desktop](https://lubuntu.net/)
    *   [xubuntu-desktop](https://xubuntu.org/screenshots/)
    *   [xfce4](https://www.xfce.org/)
    *   ubuntu-desktop
    *   [kde-plasma-desktop](https://kde.org/plasma-desktop/)
    *   ubuntu-desktop-minimal
    *   [cinnamon](https://en.wikipedia.org/wiki/Cinnamon_(desktop_environment))
    *   [icewm](https://ice-wm.org/)

    [Cet article montre quelques-uns de ces bureaux](https://cloudinfrastructureservices.co.uk/best-ubuntu-desktop-environments). Les commandes suivantes installent un bureau MATE.
    ```bash
    sudo apt update
    sudo apt upgrade -y
    sudo apt install ubuntu-mate-desktop
    ```
    Au cours de l'installation du paquet `ubuntu-mate-desktop`, vous devez sélectionner le gestionnaire de session par défaut; le meilleur choix serait [`lightdm`](https://en.wikipedia.org/wiki/LightDM). Cette installation peut souvent prendre de 15 à 30 minutes.

2.  Installez le serveur TigerVNC.
    Ce logiciel installé sur votre instance permet d’utiliser l’interface de bureau que vous avez installée à l’étape 1.
    ```bash
    sudo apt install -y tigervnc-common tigervnc-standalone-server
    ```
    Cette commande installe le serveur TigerVNC et les logiciels nécessaires. Pour plus d’information sur les serveurs VNC, voyez [notre page wiki VNC](../interactive/vnc.md).

3.  Démarrez le serveur VNC.
    ```bash
    vncserver
    ```
    Lorsque vous démarrez le serveur VNC pour la première fois, vous serez invité à entrer un mot de passe qui vous servira à vous connecter au bureau VNC, puis à confirmer si vous souhaitez un mot de passe en lecture seule (entrez "n"). Il n’est pas nécessaire que le mot de passe soit pour lecture seulement. Pour modifier votre mot de passe, utilisez la commande `vncpasswd`.

4.  Testez la connexion en ouvrant le port 5901 (pour savoir comment ouvrir un port vers votre instance OpenStack, voir [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md)) et connectez-vous avec un client VNC, par exemple [TigerVNC](https://tigervnc.org/).

    !!! warning "Connexion non sécuritaire"
        Cette option n’est pas sécuritaire parce que les données entrant et sortant de l’instance ne seront pas chiffrées. Par contre, cette étape vous permet de tester la connexion client-serveur avant de vous connecter de façon sécuritaire via un tunnel SSH; vous pouvez ignorer cette étape si vous savez comment configurer un tunnel SSH correctement.

5.  Connectez-vous via un [tunnel SSH](../getting-started/ssh_tunnelling.md). [Vous pouvez consulter cet exemple qui utilise un nœud de calcul sur nos grappes](../interactive/vnc.md#nœuds-de-calcul).
    Pour vous connecter sous Linux ou Mac :
    *   Ouvrez votre terminal.
    ```bash
    SSH -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM
    ```
    *   Lancez votre client VNC.
    *   Dans le champ pour le serveur VNC, entrez `localhost:5901`.
    *   Le bureau graphique pour votre session à distance devrait s’ouvrir.

6.  Fermez le port 5901.
    !!! tip "Sécurité des ports"
        Ce port ne sert plus après que la connexion avec le serveur VNC est établie via un tunnel SSH et il est recommandé de [supprimer cette règle dans vos groupes de sécurité](managing_your_cloud_resources_with_openstack.md).

7.  Quand vous n’avez plus besoin du bureau, arrêtez le serveur VNC avec
    ```bash
    vncserver -kill :1