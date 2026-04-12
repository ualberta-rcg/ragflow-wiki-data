---
title: "VNC/fr"
slug: "vnc"
lang: "fr"

source_wiki_title: "VNC/fr"
source_hash: "d7fa1d0ef2752a6b01d2b79b60a786bc"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:37:59.187690+00:00"

tags:
  []

keywords:
  - "temps CPU"
  - "accélération graphique OpenGL"
  - "connexion"
  - "mot de passe d'authentification"
  - "VNC"
  - "TigerVNC"
  - "bureau distant"
  - "RFB protocol"
  - "bureau VNC distant"
  - "port TCP"
  - "VNC Viewer"
  - "commande grep"
  - "limites de mémoire"
  - "connexions multiples"
  - "nœud de calcul"
  - "applications"
  - "tunnel SSH"
  - "fichier de journalisation"
  - "mot de passe CCDB"
  - "bureau Linux MATE"
  - "vncserver"
  - "grappe"
  - "connexions"
  - "interface web VDI"
  - "pixel format"
  - "connexion VNC"
  - "salloc"
  - "bureau"
  - "nœuds de calcul"
  - "nœud de connexion"
  - "tâche interactive"
  - "serveur VNC"
  - "TLSVnc"
  - "connexion à distance"
  - "DecodeManager"
  - "fenêtre de terminal"
  - "écran de veille"
  - "VeNCrypt"
  - "interface graphique"
  - "vncviewer"

questions:
  - "Pourquoi est-il recommandé d'utiliser VNC plutôt que le protocole X11 via SSH pour exécuter des interfaces graphiques à distance ?"
  - "Quelles sont les étapes requises pour installer le client TigerVNC sur les différents systèmes d'exploitation (Windows, macOS et Linux) ?"
  - "Quelles sont les conditions et les limites à respecter lors de l'utilisation d'un bureau VNC distant sur un nœud de connexion ?"
  - "Comment démarrer un serveur VNC sur un nœud de connexion en configurant une fermeture automatique en cas d'inactivité ?"
  - "Comment identifier le port TCP utilisé par le serveur VNC nouvellement créé à l'aide du fichier de journalisation ?"
  - "Quelles sont les étapes pour établir un tunnel SSH et se connecter au bureau distant avec TigerVNC Viewer depuis son ordinateur local ?"
  - "Sur quels types de nœuds est-il possible de lancer une application selon le texte ?"
  - "Quel type d'applications peut-on exécuter sur un bureau VNC distant et sous quelles contraintes de ressources ?"
  - "Quelle est la première étape à accomplir pour accéder à ces applications, comme illustré avec l'exemple de Nibi ?"
  - "Quelles sont les deux méthodes proposées pour initier la connexion VNC ?"
  - "Quelle information de sécurité est requise par la fenêtre contextuelle dans les deux cas ?"
  - "Quel est le résultat final une fois que le mot de passe d'authentification a été saisi ?"
  - "Pourquoi est-il nécessaire d'utiliser un nœud de calcul plutôt qu'un nœud de connexion pour exécuter certaines applications via VNC ?"
  - "Comment la commande salloc est-elle utilisée pour allouer des ressources spécifiques (comme le CPU et la mémoire) lors d'une tâche interactive ?"
  - "Quelle est la procédure pour identifier le port TCP sur lequel le serveur VNC écoute une fois qu'il a été démarré ?"
  - "Quelle est la différence entre la commande de création d'un tunnel SSH pour la grappe Nibi et celle utilisée pour les autres grappes ?"
  - "Que se passe-t-il avec le serveur VNC si l'on quitte le nœud auquel le tunnel SSH est connecté ?"
  - "Comment doit-on procéder pour se connecter au serveur VNC à l'aide du client une fois le tunnel SSH établi ?"
  - "Quelle commande permet d'identifier le port d'écoute du serveur VNC dans le fichier de journalisation ?"
  - "Quel est le chemin du fichier de journalisation analysé dans l'exemple fourni ?"
  - "Sur quel port TCP le serveur VNC écoute-t-il selon le résultat affiché ?"
  - "How many CPU cores did the DecodeManager detect, and how many decoder threads were created?"
  - "What host, port, and RFB protocol version were established for the server connection?"
  - "Which security types and pixel format settings were selected during the session setup?"
  - "Comment configurer la connexion avec TigerVNC Viewer sous macOS ou Windows et lancer des applications sur le bureau Linux MATE ?"
  - "Quelles sont les méthodes permettant de réinitialiser ou de supprimer le mot de passe de votre configuration VNC ?"
  - "Comment gérer les sessions VNC actives, que ce soit pour les fermer ou pour permettre des connexions multiples depuis différents emplacements ?"
  - "Quel est l'avantage principal de démarrer un vncserver avec l'option `-AlwaysShared` ?"
  - "Combien de connexions vncviewer sont possibles si le serveur n'est pas démarré en mode partagé ?"
  - "Quelles manipulations l'utilisateur doit-il effectuer pour reprendre son travail à domicile si l'option de partage n'a pas été activée ?"
  - "Comment peut-on résoudre les échecs de connexion VNC liés aux tunnels SSH et les problèmes d'authentification à deux étapes ?"
  - "Quelles sont les étapes et commandes nécessaires pour exécuter un programme graphique utilisant l'accélération matérielle OpenGL sur un nœud de calcul ?"
  - "Quelles alternatives à VNC sont recommandées en cas de problèmes graphiques pour bénéficier d'une interface web simplifiée et de meilleures performances ?"
  - "Comment peut-on résoudre les échecs de connexion VNC liés aux tunnels SSH et les problèmes d'authentification à deux étapes ?"
  - "Quelles sont les étapes et commandes nécessaires pour exécuter un programme graphique utilisant l'accélération matérielle OpenGL sur un nœud de calcul ?"
  - "Quelles alternatives à VNC sont recommandées en cas de problèmes graphiques pour bénéficier d'une interface web simplifiée et de meilleures performances ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Essayez d'abord JupyterLab"
    Cette page présente des fonctions avancées de VNC. Dans plusieurs cas, il est plus simple d'utiliser VNC dans votre navigateur et [Desktop](jupyterlab.md). Employez cette méthode avant d'utiliser les instructions données ci-dessous.

Pour démarrer à distance l'interface graphique d'un programme, on utilise généralement le protocole X11 via SSH. Cependant, les performances de cette méthode sont souvent insuffisantes pour effectuer des rotations graphiques complexes et fluides. Une meilleure option est d'utiliser [VNC](https://fr.wikipedia.org/wiki/Virtual_Network_Computing) pour se connecter à un ordinateur à distance.

## Configuration

Pour vous connecter au serveur VNC, vous devez d'abord installer un client VNC sur votre ordinateur. Nous recommandons le paquet [TigerVNC](http://tigervnc.org/) disponible pour Windows, macOS et pour la plupart des distributions Linux. Nous abordons ici le téléchargement, l'installation et la configuration de TigerVNC de manière sécuritaire pour chaque système d'exploitation.

### Windows

Téléchargez et exécutez la plus récente version stable de l'installateur `vncviewer64-x.y.z.exe` à partir de [la page officielle](https://sourceforge.net/projects/tigervnc/files/stable/), par exemple `vncviewer64-1.15.0.exe` (depuis avril 2025). Vérifiez que vous avez bien téléchargé VNC Viewer et non le serveur. Pour créer des tunnels sécuritaires entre votre ordinateur et vncserver comme décrit ci-dessous, vous devez ouvrir une fenêtre de terminal et exécuter la commande SSH, ce qui peut être fait avec le standard PowerShell de Windows 10, à partir de la mise à jour 1809.

### macOS

Installez le plus récent paquet DMG stable à partir de [la page officielle de téléchargement](https://sourceforge.net/projects/tigervnc/files/stable/) et cliquez sur le bouton vert *Download Latest Version* pour TigerVNC-1.15.0.dmg (depuis avril 2025). Quand le fichier DMG est téléchargé, faites un double-clic dessus pour l'ouvrir. Une fenêtre contextuelle est affichée avec l'icône de TigerVNC Viewer ainsi que les fichiers LICENSE.TXT et README.rst. Glissez l'icône tigervnc dans le dossier Applications et/ou dans le [Dock](https://support.apple.com/en-ca/guide/mac-help/mh35859/mac). Pour supprimer la fenêtre contextuelle, vous devez démonter le fichier DMG. Pour ce faire, ouvrez une fenêtre de nouveau Finder; assurez-vous que `View->ShowSidebar` est sélectionné. Dans le menu de gauche, cliquez sur la petite flèche vers le haut près de `TigerVNC-1.15.0`; et fermez la fenêtre de Finder. Avec macOS Monterey 12.2, [si TigerVNC plante](https://github.com/TigerVNC/tigervnc/issues/1423), utilisez plutôt la dernière version.

### Linux

Installez TigerVNC Viewer pour votre version de Linux :

| Version               | Commande                               |
| :-------------------- | :------------------------------------- |
| Debian, Ubuntu        | `sudo apt-get install tigervnc-viewer` |
| Fedora, CentOS, RHEL  | `sudo yum install tigervnc`            |
| Gentoo                | `emerge -av net-misc/tigervnc`         |

Lancez TigerVNC par le menu des applications ou en entrant `vncviewer` sur la ligne de commande de votre ordinateur.

## Connexion

Vous avez maintenant besoin d'un serveur VNC auquel vous connecter. Il peut s'agir d'un vncserver temporaire que vous avez lancé sur un nœud de connexion ou un nœud de calcul, comme expliqué dans les sections ci-dessous.

### Nœuds de connexion

Avec votre ordinateur, vous pouvez utiliser des applications peu exigeantes (qui ne requièrent pas de GPU) sur un bureau VNC distant, sous condition de certaines limites de mémoire et de temps CPU. Pour ce faire, connectez-vous d'abord à un nœud de connexion. Par exemple, sur Nibi,

```bash
laptop:~ % ssh nibi.alliancecan.ca
```

Lancez ensuite `vncserver -list` pour savoir si d'autres vncservers dont vous n'avez plus besoin sont toujours actifs sur le nœud Nibi auquel vous êtes connecté; si c'est le cas, tuez-les avec la commande `pkill`.

```bash
l4(login node):~ % pkill Xvnc -u $USER
```

Étape 1 : Vous pouvez maintenant lancer vncserver sur le nœud de connexion, comme ci-dessous.

```bash
l4(login node):~ % vncserver -idletimeout 86400
```
```text
Desktop 'TurboVNC: l4.nibi.sharcnet:1 (yourusername)' started on display l4.nibi.sharcnet:1
Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
Log file is /home/yourusername/.vnc/l4.nibi.sharcnet:1.log
```

Notez que la commande vncserver fournie par StdEnv/2023 est basée sur [TurboVNC](https://turbovnc.org). Lors du démarrage d'un nouveau vncserver sur un nœud de connexion, ajoutez `-idletimeout seconds` comme indiqué ci-dessus. Cela causera la fermeture définitive de votre `vncserver` (après S secondes sans connexion à VNC Viewer) si vous oubliez de fermer votre session vncviewer en cliquant sur `System -> Log out` sur le bureau VNC. Au premier démarrage de vncserver, vous devrez définir un mot de passe qui [pourra être modifié ultérieurement](#mot-de-passe). Ce mot de passe sera requis pour vous connecter à votre bureau avec un vncclient (tel que vncviewer). Le même mot de passe sera requis lors de l'établissement de [connexions multiples](#connexions-multiples) en supposant que vous ayez démarré vncserver en ajoutant l'option `-alwaysshared`.

Étape 2 : Déterminez maintenant quel est le port qui écoute le nouveau vncserver (dans cet exemple, il s'agit de 5901) avec la commande `grep` sur le fichier de journalisation.

```bash
l4(login node):~ % grep -iE "\sport|kill" /home/yourusername/.vnc/l4.nibi.sharcnet:1.log
```
```text
25/08/2025 15:16:20 Listening for VNC connections on TCP port 5901
```

Vous pouvez maintenant quitter le nœud de connexion. Le vcnserver que vous avez lancé restera actif jusqu'à ce que la limite de temps définie avec l'option `-idletimeout` soit atteinte.

```bash
l4(login node):~ % exit
```
```bash
laptop:~ %
```

Étape 3 : Sur votre bureau, démarrez un tunnel SSH. Ainsi, un port arbitraire (5905 dans cet exemple) sera transféré au port que votre serveur VNC écoute (5901 selon ce qui précède).

```bash
laptop:~ % ssh nibi.computecanada.ca -L 5905:l4:5901
```

4) Ensuite, sur votre bureau, cliquez sur l'icône de l'application *TigerVNC Viewer* et entrez `localhost:5905` dans la boîte de dialogue *VNC Viewer: Connexion détails* qui s'affiche. **OU** ouvrez une autre fenêtre de terminal et entrez la commande suivante, puis appuyez sur la touche Retour (*Entrée*). Dans les deux cas, une fenêtre contextuelle vous demandera le mot de passe d'authentification VNC que vous avez configuré précédemment. Une fois le mot de passe saisi, votre bureau distant devrait immédiatement s'afficher.

```bash
laptop:~ % vncviewer localhost:5905
```

Bien qu'il n'y ait pas de limite de temps pour les processus sur les nœuds de connexion, les applications exécutées sur votre bureau distant sont soumises à des limites de mémoire et de temps CPU. Si vous avez besoin de plus de mémoire, de ressources CPU ou d'accès GPU pour vos applications ou pour l'accélération graphique, suivez la procédure ci-dessous pour démarrer votre serveur VNC sur un nœud de calcul et demandez les ressources nécessaires à l'aide de la commande `salloc`.

### Nœuds de calcul

Si votre programme requiert des limites de mémoire et/ou de temps processeur supérieures à celles offertes par un ou plusieurs nœuds de connexion, connectez-vous à un nœud de calcul à l'aide de la commande `salloc`, démarrez un serveur VNC, puis établissez un tunnel sécurisé vers ce serveur (avec la redirection de port appropriée) et connectez-vous depuis votre ordinateur avec un client VNC. Cette méthode vous permettra d'accéder à votre serveur VNC sur un nœud de calcul avec un environnement graphique complet; toutefois, par défaut, l'accélération matérielle OpenGL ne sera pas possible.

#### 1) Démarrez un serveur VNC

Avant de démarrer votre serveur VNC, connectez-vous à une grappe (par exemple Nibi) et créez une allocation sur un nœud de connexion avec la commande `salloc` (limite de 24 heures). Par exemple, pour demander une [tâche interactive](../running-jobs/running_jobs.md) qui utilise 4 CPU et 16Go de mémoire, vous pourriez utiliser

```bash
l4(login node):~ % salloc --time=1:00:00 --cpus-per-task=4 --mem=16000 --account=def-piusername
```
```text
salloc: Pending job allocation 1149016
salloc: job 1149016 queued and waiting for resources
salloc: job 1149016 has been allocated resources
salloc: Granted job allocation 1149016
salloc: Waiting for resource configuration
salloc: Nodes c48 are ready for job
```
```bash
c48(compute node):~ %
```

Une fois la tâche interactive démarrée, définissez une variable d'environnement pour éviter les erreurs répétitives.

```bash
c48(compute node):~ % export XDG_RUNTIME_DIR=${SLURM_TMPDIR}
```

Ensuite, démarrez un serveur VNC avec `vncserver` et portez attention au nœud de calcul dans lequel la tâche est exécutée (**c48** dans notre exemple). En cas de doute, utilisez la commande `hostname` pour vérifier de quel nœud il s'agit. Si vous faites ceci pour la première fois, une invite demandera un mot de passe pour votre serveur VNC. **VOUS DEVEZ ENTRER UN MOT DE PASSE**, autrement n'importe qui pourra se connecter et obtenir l'accès aux fichiers dans votre compte. Vous pourrez changer le mot de passe par la suite avec la commande `vncpasswd`. Revenons à l'exemple :

```bash
c48(compute node):~ % vncserver
```
```text
Desktop 'TurboVNC: c48.nibi.sharcnet:1 (yourusername)' started on display c48.nibi.sharcnet:1
Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
Log file is /home/yourusername/.vnc/c48.nibi.sharcnet:1.log
```

Lancez la commande `grep` dans le fichier de journalisation pour identifier le port sur lequel votre serveur VCN écoute.

```bash
c48(compute node):~ % grep -iE "\sport|kill" /home/yourusername/.vnc/c48.nibi.sharcnet:1.log
```
```text
26/08/2025 10:43:36 Listening for VNC connections on TCP port 5901
```

#### 2) Établissez un tunnel SSH vers le serveur VNC

Une fois le serveur VNC démarré, il faut créer un tunnel sécurisé entre votre ordinateur et le nœud de calcul sur lequel vncserver est exécuté (voir l'étape précédente). Deux types de commandes peuvent être utilisées selon la grappe utilisée.

Pour toutes les grappes (**sauf Nibi**), vous pouvez utiliser la forme `ssh username@clustername -L localforwardedport:computenode:remotelisteningport` recommandée précédemment. Par exemple, si un vncserver est démarré sur le nœud de calcul **rc12509** de `rorqual` et que le port local de votre ordinateur portable à transférer est 5905, la commande appropriée est :

```bash
laptop:~ % ssh username@rorqual.alliancecan.ca -L 5905:rc12509:5901
```
```text
Duo two-factor login for username
Enter a passcode or select one of the following options:
```
```bash
rc12509(compute node):~ %
```

Pour Nibi, une nouvelle forme de la commande doit être utilisée, soit `ssh -J username@clustername -L localforwardedport:localhost:remotelisteningport computenode`. De plus, une paire de clés SSH doit être créée sur votre ordinateur avec le contenu de la clé publique saisie dans votre fichier `~/.ssh/authorized_keys` sur `nibi`. Cette approche fonctionne également sur toute autre grappe et pourrait donc être privilégiée. En reprenant l'exemple précédent, où **c48** est le nœud de calcul sur lequel vous avez démarré vncserver et 5905 est le port local de votre ordinateur transféré, la commande pour Nibi est :

```bash
laptop:~ % ssh -J username@nibi.alliancecan.ca -L 5905:localhost:5901 c48
```
```text
Duo two-factor login for username
Enter a passcode or select one of the following options:
```
```bash
c48(compute node):~ %
```

Si vous quittez le nœud auquel votre tunnel est connecté, vous ne pourrez plus vous connecter au serveur VNC avec vncviewer. Cependant, comme vncserver continuera de fonctionner, vous pourrez encore y accéder avec un nouveau tunnel. Pour plus d'information, voir [Tunnels SSH](../getting-started/ssh_tunnelling.md).

#### 3) Connectez-vous au serveur VNC

Sous Linux, ouvrez une nouvelle fenêtre de terminal et connectez votre client VNC à **localhost:port**. Dans le prochain exemple, la commande `vncviewer` de TigerVNC établit la connexion au serveur VNC actif sur cdr768. Vous devrez entrer le mot de passe que vous avez défini précédemment.

```bash
laptop:~ % vncviewer localhost:5905
```
```text
TigerVNC viewer v1.15.0
Built on: 2025-02-16 03:59
Copyright (C) 1999-2025 TigerVNC team and many others (see README.rst)
See https://www.tigervnc.org for information on TigerVNC.
Tue Aug 26 10:59:59 2025
DecodeManager: Detected 12 CPU core(s)
DecodeManager: Creating 4 decoder thread(s)
CConn: Connected to host localhost port 5905
CConnection: Server supports RFB protocol version 3.8
CConnection: Using RFB protocol version 3.8
CConnection: Choosing security type VeNCrypt(19)
CVeNCrypt: Choosing security type TLSVnc (258)
Tue Aug 26 11:00:03 2025
CConn: Using pixel format depth 24 (32bpp) little-endian rgb888
CConnection: Enabling continuous updates
```

Sous macOS ou Windows (mais pas de distribution Linux), plutôt que de lancer `vncviewer` par la ligne de commande, vous pouvez cliquer sur l'icône de l'application *TigerVNC Viewer* et entrez l'information sur le **localhost:port**.

Notez aussi que le port VNC par défaut utilisé par TigerVNC Viewer est 5900; par conséquent, si vous avez spécifié 5900 comme port local à transférer au démarrage de votre tunnel SSH, vous pourriez simplement spécifier **localhost**. Cependant, sous Windows, vous pourriez ne pas pouvoir configurer un tunnel SSH sur le port local 5900.

Une fois `vncviewer` connecté, un [bureau Linux MATE](https://mate-desktop.org/) s'affichera. Pour lancer un terminal, cliquez sur *Applications -> Outils système -> Terminal MATE* dans le menu du haut. Vous pouvez également ajouter un raccourci au menu supérieur en faisant un clic droit sur *Terminal MATE* et en cliquant sur *Ajouter ce lanceur au tableau de bord*. Enfin, pour lancer un programme, utilisez la commande comme vous le feriez normalement dans une session `bash`, par exemple `xclock`. Pour démarrer un programme plus complexe comme MATLAB, chargez le module, puis exécutez la commande `matlab`.

## Autres points importants

### Mot de passe

Pour réinitialiser votre mot de passe, utilisez la commande

```bash
gra-login1:~ % vncpasswd
```
```text
Password:
Verify:
Would you like to enter a view-only password (y/n)? n
```

Vous pouvez choisir de supprimer définitivement votre configuration VNC incluant votre mot de passe en supprimant votre répertoire `~/.vnc`. La prochaine fois que vous lancerez `vncserver`, une invite vous demandera de définir un nouveau mot de passe.

### Tuer le vncserver

Si un vncserver actif n'est plus nécessaire, tuez-le avec `vncserver -kill :DISPLAY#` comme démontré ci-dessous.

```bash
gra-login1:~ % vncserver -list
```
```text
TurboVNC sessions:
X DISPLAY #     PROCESS ID      NOVNC PROCESS ID
:44             27644
```
```bash
gra-login1:~ % vncserver -kill :44
```
```text
Killing Xvnc process ID 27644
```

Si vous avez plusieurs vncservers actifs sur un nœud, vous pouvez les tuer TOUS du même coup avec

```bash
gra-login1:~ % pkill Xvnc -u $USER
```

### Connexions multiples

Tous les vncservers exécutés sous votre nom d'utilisateur (sur un nœud de connexion ou de calcul) peuvent être listés avec `vncserver -list`. Si un vncserver a été démarré avec l'option supplémentaire `-AlwaysShared`, plusieurs connexions peuvent être établies en créant un nouveau tunnel et un nouveau vncviewer à partir de n'importe quel emplacement distant, par exemple

```bash
l4(login node):~ % vncserver -idletimeout 86400 -alwaysshared
```
```text
Desktop 'TurboVNC: l4.nibi.sharcnet:1 (yourusername)' started on display l4.nibi.sharcnet:1
Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
Log file is /home/yourusername/.vnc/l4.nibi.sharcnet:1.log
```

Ainsi, on peut laisser vncviewer actif sur un ordinateur au bureau, puis se reconnecter à nouveau depuis chez soi pour accéder au même ordinateur et ensuite, par exemple, continuer à travailler de manière transparente avec les mêmes applications sans avoir à les fermer. Si toutefois un vncserver n'a pas été démarré avec `vncserver -AlwaysShared`, une seule connexion vncviewer sera possible et avant de quitter pour la maison, vous devrez fermer toutes les applications sur le bureau et fermer vncserver. Une fois à la maison, il faudra créer un nouveau bureau et ouvrir les applications pour poursuivre votre travail.

### Échecs de connexion

Des échecs répétés à établir une nouvelle connexion vncserver/vncviewer pourraient être causés par un tunnel SSH existant sur votre ordinateur qui bloquerait les ports. Pour déterminer la présence de tels tunnels et les tuer, ouvrez une fenêtre de terminal sur votre ordinateur et lancez la commande `ps ux | grep ssh` suivie de `kill PID`.

### Déverrouiller l'écran de veille

Si votre écran de veille VNC s'éteint en raison du délai d'affichage et qu'un mot de passe vous est demandé, entrez le mot de passe de votre compte sur la grappe et non le mot de passe vncserver. Si le bureau MATE est en cours d'exécution et que l'écran de veille ne se déverrouille pas, essayez avec la commande `killall -9 .mate-screensaver`. Ceci ne devrait plus se produire car l'écran de veille VNC a été désactivé sur nos grappes.

### Problème de connexion

La connexion à gra-vdi.alliancecan.ca se fait en deux étapes :

1.  username
    Entrez votre mot de passe pour CCDB.
2.  username
    Entrez votre code de passe pour l'authentification multifacteur.

Si vous entrez un nom d'utilisateur/mot de passe erroné pour l'étape 1, vous aurez quand même à passer l'étape 2. Si vous saisissez ensuite votre nom d'utilisateur/mot de passe, vous recevrez un message indiquant que la connexion est établie et vous reviendrez vers l'écran de connexion de l'étape 1. La solution est de réessayer en vous assurant d'avoir saisi la bonne combinaison nom d'utilisateur/mot de passe. Si vous ne vous souvenez plus de votre mot de passe CCDB, allez [ici](https://ccdb.alliancecan.ca/security/forgot) pour le réinitialiser, à condition que votre compte ne soit pas en attente de renouvellement par la chercheuse principale ou le chercheur principal.

### OpenGL

Pour exécuter un programme graphique utilisant OpenGL accéléré par le matériel, quelques modifications seront nécessaires dans la section *Nœuds de calcul* ci-dessus.

Tout d'abord, la commande `salloc` doit être modifiée pour demander un nœud GPU. À défaut, le programme utilisera le rendu logiciel sur les CPU, ce qui est beaucoup plus lent. Pour demander le premier nœud GPU disponible (et ainsi minimiser le temps d'attente au cas où la grappe comporte plusieurs types de nœuds GPU), il suffit de spécifier

```bash
l4(login node):~ % salloc --time=1:00:00 --cpus-per-task=4 --gpus-per-node=1 --mem=16000 --account=def-piname
```

Toutefois, si la grappe que vous utilisez comporte plusieurs types de nœuds, dont l'un est reconnu pour offrir une bonne accélération graphique, par exemple un nœud équipé d'un GPU **t4**, alors utilisez

```bash
l4(login node):~ % salloc --time=1:00:00 --cpus-per-task=4 --gpus-per-node=t4:1 --mem=16000 --account=def-piname
```

Deuxièmement, il faudra probablement ajouter `vglrun` juste avant le nom du `PROGRAM` sur la ligne de commande de votre terminal VNC. Par exemple

```bash
c48(compute node):~ % vglrun -d egl PROGRAM
```

Ensuite, la fonction `vglrun` configure des variables d'environnement supplémentaires pour garantir que votre programme utilise les bibliothèques VirtualGL appropriées. Toutefois, si votre programme a déjà été modifié pour utiliser l'environnement standard cvmfs actuel, cette étape est inutile.

### Autres options

Si vous rencontrez des problèmes graphiques à l'utilisation de VNC comme décrit ci-dessus, essayez d'utiliser [OpenOnDemand](https://ondemand.sharcnet.ca/) sur **nibi** ou [JupyterHub](https://jupyterhub.rorqual.alliancecan.ca) sur **rorqual**. Les deux grappes offrent une interface web VDI automatisée avec un bureau moderne qui est conçue pour une utilisation simplifiée, ainsi que des performances matérielles améliorées et une meilleure prise en charge logicielle.