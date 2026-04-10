---
title: "Setting up GUI Desktop on a VM/fr"
slug: "setting_up_gui_desktop_on_a_vm"
lang: "fr"

source_wiki_title: "Setting up GUI Desktop on a VM/fr"
source_hash: "96de8b2cc02dea39a8d8f3797083755b"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:18:04.337792+00:00"

tags:
  - cloud

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

Certains logiciels que vous pouvez installer sur votre machine virtuelle (MV ou instance) sont accessibles uniquement, ou préférablement, via leur interface graphique utilisateur (GUI). Vous pouvez utiliser une interface graphique avec la redirection X11, mais vous pourriez obtenir une meilleure performance en utilisant VNC pour vous connecter à une session graphique qui se trouve sur votre instance.

Nous décrivons ici les étapes pour configurer une interface de bureau avec VNC sur une instance qui utilise le système d’exploitation Ubuntu.

## Étapes pour configurer un bureau graphique VNC

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

    Cette commande installe le serveur TigerVNC et les logiciels nécessaires. Pour plus d’information sur les serveurs VNC, voyez [notre page wiki VNC](vnc.md).

3.  Démarrez le serveur VNC.

    ```bash
    vncserver
    ```

    !!! info "Interaction"
        Lors de l'exécution de cette commande, vous serez invité(e) à :
        *   Saisir un mot de passe.
        *   Saisir "n" pour un mot de passe en lecture seule.

    Au premier démarrage du serveur VNC, vous devez entrer un mot de passe qui vous servira à vous connecter au bureau VNC. Il n’est pas nécessaire que le mot de passe soit en lecture seule. Pour modifier votre mot de passe, utilisez la commande `vncpasswd`.

4.  Testez la connexion en ouvrant le port 5901 (pour savoir comment ouvrir un port vers votre instance OpenStack, voir [Groupes de sécurité](managing_your_cloud_resources_with_openstack.md#groupes-de-securite)) et connectez-vous avec un client VNC, par exemple [TigerVNC](https://tigervnc.org/).

    !!! warning "Attention"
        Cette option n’est pas sécuritaire parce que les données entrant et sortant de l’instance ne seront pas chiffrées. Par contre, cette étape vous permet de tester la connexion client-serveur avant de vous connecter de façon sécuritaire via un tunnel SSH; vous pouvez ignorer cette étape si vous savez comment configurer un tunnel SSH correctement.

5.  Connectez-vous via un [tunnel SSH](ssh_tunnelling.md). [Vous pouvez consulter cet exemple qui utilise un nœud de calcul sur nos grappes](vnc.md#nœuds-de-calcul). Pour vous connecter sous Linux ou Mac :
    *   Ouvrez votre terminal.
    *   Dans votre terminal local, entrez la commande suivante :
        ```bash
        ssh -i filepathtoyoursshkey/sshprivatekeyfile.key -L5901:localhost:5901 ubuntu@ipaddressofyourVM
        ```
    *   Lancez votre client VNC.
    *   Dans le champ pour le serveur VNC, entrez `localhost:5901`.
    *   Le bureau graphique pour votre session à distance devrait s’ouvrir.

6.  Fermez le port 5901; ce port ne sert plus après que la connexion avec le serveur VNC est établie via un tunnel SSH et il est recommandé de [supprimer cette règle dans vos groupes de sécurité](managing_your_cloud_resources_with_openstack.md#groupes-de-securite).

7.  Quand vous n’avez plus besoin du bureau, arrêtez le serveur VNC avec la commande suivante :

    ```bash
    vncserver -kill :1