---
title: "VNC/fr"
tags:
  []

keywords:
  []
---

[400px|thumb|MATLAB exécuté dans VNC](file:matlab-vnc.png.md)

Pour démarrer à distance l'interface graphique d'un programme, on utilise généralement le protocole X11 via SSH. Cependant, les performances de cette méthode sont souvent insuffisantes pour effectuer des rotations graphiques complexes et fluides. Une meilleure option est d'utiliser [VNC](https://fr.wikipedia.org/wiki/Virtual_Network_Computing) pour se connecter à un ordinateur à distance.

<span id="Setup"></span>
= Configuration =

Pour vous connecter au serveur VNC, vous devez d'abord installer un client VNC sur votre ordinateur. Nous recommandons le paquet [TigerVNC](http://tigervnc.org/) disponible pour Windows, macOS et pour la plupart des distributions Linux. Nous abordons ici le téléchargement, l'installation et la configuration de TigerVNC de manière sécuritaire pour chaque système d'exploitation.

## Windows 

Téléchargez et exécutez la plus récente version stable de l'installateur <tt>vncviewer64-x.y.z.exe</tt> à partir de [la page officielle](https://sourceforge.net/projects/tigervnc/files/stable/), par exemple `vncviewer64-1.15.0.exe` (depuis avril 2025). Vérifiez que vous avez bien téléchargé VNC Viewer et non le serveur. Pour créer des tunnels sécuritaires entre votre ordinateur et vncserver comme décrit ci-dessous, vous devez ouvrir une fenêtre de terminal et exécuter la commande SSH, ce qui peut être fait avec le standard PowerShell de Windows 10, à partir de la mise à jour 1809.

<span id="MacOS"></span>
## macOS 

Installez le plus récent paquet DMG stable à partir de [la page officielle de téléchargement](https://sourceforge.net/projects/tigervnc/files/stable/) et cliquez sur le bouton vert <i>Download Latest Version</i> pour TigerVNC-1.15.0.dmg (depuis avril 2025). Quand le fichier DMG est téléchargé, faites un double-clic dessus pour l'ouvrir.  Une fenêtre contextuelle est affichée avec l'icône de TigerVNC Viewer ainsi que les fichiers LICENSE.TXT et README.rst. Glissez l'icône  tigervnc dans le dossier Applications et/ou dans le [Dock](https://support.apple.com/en-ca/guide/mac-help/mh35859/mac). Pour supprimer la fenêtre contextuelle, vous devez démonter le fichier  DMG. Pour ce faire, ouvrez une fenêtre de New Finder; assurez-vous que `View->ShowSidebar` est sélectionné. Dans le menu de gauche, cliquez sur la petite flèche vers le haut près de `TigerVNC-1.15.0`; et fermez la fenêtre de Finder. Avec macOS Monterey 12.2, [si TigerVNC plante](https://github.com/TigerVNC/tigervnc/issues/1423), utilisez plutôt la dernière version.

## Linux 

Installez TigerVNC Viewer pour votre version de Linux :

{| class="wikitable"
! Version
! Commande
|-
| Debian, Ubuntu
| `sudo apt-get install tigervnc-viewer`
|-
| Fedora, CentOS, or RHEL
| `sudo yum install tigervnc`
|-
| Gentoo
| `emerge -av net-misc/tigervnc`
|}

Lancez TigerVNC par le menu des applications ou en entrant `vncviewer` sur la ligne de commande de votre ordinateur.  

<span id="Connect"></span>
= Connexion =

Vous avez maintenant besoin d'un serveur VNC auquel vous connecter. Il peut s'agir d'un vncserver temporaire que vous avez lancé sur un nœud de connexion ou un nœud de calcul, comme expliqué dans les sections ci-dessous.

<span id="Login_nodes"></span>
## Nœuds de connexion 

Avec votre ordinateur, vous pouvez utiliser des applications peu exigeantes (qui ne requièrent pas de GPU) sur un bureau VNC distant, sous condition de certaines limites de mémoire et de temps CPU. Pour ce faire, connectez-vous d'abord à un nœud de connexion. Par exemple, sur Nibi,

 [<b>laptop</b>:~] ssh nibi.alliancecan.ca

Lancez ensuite `vncserver -list` pour savoir si d'autres vncservers dont vous n'avez plus besoin sont toujours actifs sur le nœud Nibi auquel vous êtes connecté; si c'est le cas, tuez-les avec la commande `pkill`.

 [<b>l4</b>(login node):~] `pkill Xvnc -u $USER`

Étape 1 : Vous pouvez maintenant lancer vncserver sur le nœud de connexion, comme ci-dessous.

 [<b>l4</b>(login node):~] vncserver -idletimeout 86400

 Desktop 'TurboVNC: l4.nibi.sharcnet:1 (yourusername)' started on display <b>l4</b>.nibi.sharcnet:1

 Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
 Log file is <span style="Color:green">/home/yourusername/.vnc/<b>l4</b>.nibi.sharcnet:1.log</span>

Notez que la commande vncserver fournie par StdEnv/2023 est basée sur [turbovnc](https://turbovnc.org). Lors du démarrage d'un nouveau vncserver sur un nœud de connexion, ajoutez `-idletimeout seconds` comme indiqué ci-dessus. Cela causera la fermeture définitive de votre `vncserver` (après S secondes sans connexion à VNC Viewer) si vous oubliez de fermer votre session vncviewer en cliquant sur `System -> Log out` sur le bureau VNC. Au premier démarrage de vncserver, vous devrez définir un mot de passe qui [pourra être modifié ultérieurement](vnc-fr#mot_de_passe.md). Ce mot de passe sera requis pour vous connecter à  votre bureau avec un vncclient (tel que vncviewer). Le même mot de passe sera requis lors de l'établissement de [connexions multiples](vnc-fr#connexions_multiples.md) en supposant que vous ayez démarré vncserver en ajoutant l'option `-alwaysshared`.

Étape 2 : Déterminez maintenant quel est le port qui écoute le nouveau vncserver (dans cet exemple, il s'agit de 5901) avec la commande `grep` sur le fichier de journalisation.

 [<b>l4</b>(login node):~] grep -iE "\sport|kill" <span style="Color:green">/home/yourusername/.vnc/<b>l4</b>.nibi.sharcnet:1.log</span>
 25/08/2025 15:16:20 Listening for VNC connections on TCP port <span style="Color:blue">5901</span>

Vous pouvez maintenant quitter le nœud de connexion. Le vcnserver que vous avez lancé restera actif jusqu'à ce que la limite de temps définie avec l'option `-idletimeout` soit atteinte.

 [<b><span style="Color:green">l4</span></b>(login node):~]  exit
 [<b>laptop</b>:~]

Étape 3 : Sur votre bureau, démarrez un tunnel SSH. Ainsi, un port arbitraire (5905 dans cet exemple) sera transféré au port que votre serveur VNC écoute (5901 selon ce qui précède).

 [<b>laptop</b>:~] ssh nibi.computecanada.ca -L <span style="Color:red">5905</span>:<b><span style="Color:green">l4</span></b>:<span style="Color:blue">5901</span>

4) Ensuite, sur votre bureau, cliquez sur l'icône de l'application <i>TigerVNC Viewer</i> et entrez `localhost:5905` dans la boîte de dialogue <i>VNC Viewer: Connexion détails</i> qui s'affiche. ** OU ** ouvrez une autre fenêtre de terminal et entrez la commande suivante, puis appuyez sur la touche Retour (*Enter*). Dans les deux cas, une fenêtre contextuelle vous demandera le mot de passe d'authentification VNC que vous avez configuré précédemment. Une fois le mot de passe saisi, votre bureau distant devrait immédiatement s'afficher.

 [<b>laptop</b>:~] vncviewer localhost:<span style="Color:red">5905</span>

Bien qu'il n'y ait pas de limite de temps pour les processus sur les nœuds de connexion, les applications exécutées sur votre bureau distant sont soumises à des limites de mémoire et de temps CPU. Si vous avez besoin de plus de mémoire, de ressources CPU ou d'accès GPU pour vos applications ou pour l'accélération graphique, suivez la procédure ci-dessous pour démarrer votre serveur VNC sur un nœud de calcul et demandez les ressources nécessaires à l'aide de la commande `salloc`.

<span id="Compute_nodes"></span>
## Nœuds de calcul 

Si votre programme requiert des limites de mémoire et/ou de temps processeur supérieures à celles offertes par un ou plusieurs nœuds de connexion, connectez-vous à un nœud de calcul à l'aide de la commande `salloc`, démarrez un serveur VNC, puis établissez un tunnel sécurisé vers ce serveur (avec la redirection de port appropriée) et connectez-vous depuis votre ordinateur avec un client VNC. Cette méthode vous permettra d'accéder à votre serveur VNC sur un nœud de calcul avec un environnement graphique complet; toutefois, par défaut, l'accélération matérielle OpenGL ne sera pas possible.

<b>1) Démarrez un serveur VNC</b>

Avant de démarrer votre serveur VNC, connectez-vous à une grappe (par exemple Nibi) et créez une allocation sur un nœud de connexion avec la commande `salloc` (limite de 24 heures). Par exemple, pour demander une [tâche interactive](running_jobs-fr#tâches_interactives.md) qui utilise 4 CPU et 16Go de mémoire, vous pourriez utiliser

 [<b>l4</b>(login node):~] salloc --time=1:00:00 --cpus-per-task=4 --mem=16000 --account=def-piusername
 salloc: Pending job allocation 1149016
 salloc: job 1149016 queued and waiting for resources
 salloc: job 1149016 has been allocated resources
 salloc: Granted job allocation 1149016
 salloc: Waiting for resource configuration
 salloc: Nodes <b>c48</b> are ready for job
 [<b>c48</b>(compute node):~]

Une fois la tâche interactive démarrée, définissez une variable d'environnement pour éviter les erreurs répétitives.

 [<b>c48</b>(compute node):~] export XDG_RUNTIME_DIR=${SLURM_TMPDIR}

Ensuite, démarrez un serveur VNC avec `vncserver` et portez attention au nœud de calcul dans lequel la tâche est exécutée (<b>c48</b> dans notre exemple). En cas de doute, utilisez la commande `hostname` pour vérifier de quel nœud il s'agit. Si vous faites ceci pour la première fois, une invite demandera un mot de passe pour votre serveur VNC. <b>VOUS DEVEZ ENTRER UN MOT DE PASSE</b>, autrement n'importe qui pourra se connecter et obtenir l'accès aux fichiers dans votre compte. Vous pourrez changer le mot de passe par la suite avec la commande `vncpasswd`. Revenons à l'exemple&nbsp;:

 [<b>c48</b>(compute node):~] vncserver

 Desktop 'TurboVNC: c48.nibi.sharcnet:1 (yourusername)' started on display <b>c48</b>.nibi.sharcnet:1

 Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
 Log file is <span style="Color:green">/home/yourusername/.vnc/<b>c48</b>.nibi.sharcnet:1.log</span>

Lancez la commande `grep` dans le fichier de journalisation pour identifier le port sur lequel votre serveur VCN écoute.

 [<b>c48</b>(compute node):~] grep -iE "\sport|kill" <span style="Color:green">/home/yourusername/.vnc/<b>c48</b>.nibi.sharcnet:1.log</span>
 26/08/2025 10:43:36 Listening for VNC connections on TCP port <span style="Color:blue">5901</span>

<b>2) Établissez un tunnel SSH vers le serveur VNC</b>

Une fois le serveur VNC démarré, il faut créer un tunnel sécurisé entre votre ordinateur et le nœud de calcul sur lequel vncserver est exécuté (voir l'étape précédente). Deux types de commandes peuvent être utilisées selon la grappe utilisée.

Pour toutes les grappes (<b>sauf Nibi</b>), vous pouvez utiliser la forme <code>ssh username@clustername -L localforwardedport:<span style="Color:orange">computenode</span>:remotelisteningport</code> recommandée précédemment. Par exemple, si un vncserver est démarré sur le nœud de calcul  b><span style="Color:orange">rc12509</span></b> de `rorqual` et que le port local de votre ordinateur portable à transférer est <span style="Color:red">5905</span>, la commande appropriée est&nbsp;:

 [<b>laptop</b>:~] ssh username@rorqual.alliancecan.ca -L <span style="Color:red">5905</span>:<b><span style="Color:orange">rc12509</span></b>:<span style="Color:blue">5901</span>
 Duo two-factor login for username
 Enter a passcode or select one of the following options:
 [rc12509(compute node):~] 

Pour Nibi, une nouvelle forme de la commande doit être utilisée, soit <code>ssh -J username@clustername -L localforwardedport:<span style="Color:orange">localhost</span>:remotelisteningport computenode</code>. De plus, une paire de clés SSH doit être créée sur votre ordinateur avec le contenu de la clé publique saisie dans votre fichier `~/.ssh/authorized_keys` sur `nibi`. Cette approche fonctionne également sur toute autre grappe et pourrait donc être privilégiée. En reprenant l'exemple précédent, où <b>c48</b> est le nœud de calcul sur lequel vous avez démarré vncserver et <span style="Color:red">5905</span> est le port local de votre ordinateur transféré, la commande pour Nibi est&nbsp;:

 [<b>laptop</b>:~] ssh -J username@nibi.alliancecan.ca -L <span style="Color:red">5905</span>:<span style="Color:orange">localhost</span>:<span style="Color:blue">5901</span> <b><span style="Color:green">c48<span></b>
 Duo two-factor login for username
 Enter a passcode or select one of the following options:
 [c48(compute node):~]

Si vous quittez le nœud auquel votre tunnel est connecté, vous ne pourrez plus vous connecter au serveur VNC avec vncviewer. Cependant, comme vncserver continuera de fonctionner, vous pourrez encore y accéder avec un nouveau tunnel. Pour plus d'information, voir [Tunnels SSH](ssh-tunnelling-fr.md).

<b>3) Connectez-vous au serveur VNC</b>

Sous Linux, ouvrez une nouvelle fenêtre de terminal et connectez votre client VNC à <b>localhost:port</b>. Dans le prochain exemple, la commande `vncviewer` de TigerVNC établit la connexion au serveur VNC actif sur cdr768. Vous devrez entrer le mot de passe que vous avez défini précédemment.

 [<b>laptop</b>:~]$ vncviewer localhost:<span style="Color:red">5905</span>

 TigerVNC viewer v1.15.0
 Built on: 2025-02-16 03:59
 Copyright (C) 1999-2025 TigerVNC team and many others (see README.rst)
 See https://www.tigervnc.org for information on TigerVNC.

 Tue Aug 26 10:59:59 2025
 DecodeManager: Detected 12 CPU core(s)
 DecodeManager: Creating 4 decoder thread(s)
 CConn:       Connected to host localhost port 5905
 CConnection: Server supports RFB protocol version 3.8
 CConnection: Using RFB protocol version 3.8
 CConnection: Choosing security type VeNCrypt(19)
 CVeNCrypt:   Choosing security type TLSVnc (258)

 Tue Aug 26 11:00:03 2025
 CConn:       Using pixel format depth 24 (32bpp) little-endian rgb888
 CConnection: Enabling continuous updates

Sous macOS ou Windows (mais pas de distribution Linux), plutôt que de lancer `vncviewer` par la ligne de commande, vous pouvez cliquer sur l'icône de l'application <i>TigerVNC Viewer</i> et entrez l'information sur le <b>localhost:port</b>. [400px|thumb**Mac Tiger VNC Viewer Connection Details Dialogue Box**](file:vncviewerconnect3.png.md)
Notez aussi que le port VNC par défaut utilisé par TigerVNC Viewer est 5900; par conséquent, si vous avez spécifié 5900 comme port local à transférer au démarrage de votre tunnel SSH, vous pourriez simplement spécifier **localhost**. Cependant, sous Windows, vous pourriez ne pas pouvoir configurer un tunnel SSH sur le port local 5900.

Une fois `vncviewer` connecté, un [bureau Linux MATE](https://mate-desktop.org/) s'affichera. Pour lancer un terminal, cliquez sur *Applications -> System Tools -> MATE Terminal* dans le menu du haut. Vous pouvez également ajouter un raccourci au menu supérieur en faisant un clic droit sur *MATE Terminal* et en cliquant sur *Add this launcher to panel*. Enfin, pour lancer un programme, utilisez la commande comme vous le feriez normalement dans une session `bash`, par exemple `xclock`. Pour démarrer un programme plus complexe comme MATLAB, chargez le module, puis exécutez la commande `matlab`.

<span id="More_information"></span>
= Autres points importants =

<span id="Vncserver_password"></span>
## Mot de passe 

Pour réinitialiser votre mot de passe, utilisez la commande

<source lang="bash">
[gra-login1:~] vncpasswd
Password:
Verify:
Would you like to enter a view-only password (y/n)? n
</source>

Vous pouvez choisir de supprimer définitivement votre configuration VNC incluant votre mot de passe en supprimant votre répertoire `~/.vnc`. La prochaine fois que vous lancerez `vncserver`, une invite vous demandera de définir un nouveau mot de passe.

<span id="Killing_vncserver"></span>
## Tuer le vncserver 

Si un vncserver actif n'est plus nécessaire, tuez-le avec `vncserver -kill :DISPLAY#` comme démontré ci-dessous.

 [gra-login1:~] vncserver -list | grep -v ^$
 TurboVNC sessions:
 X DISPLAY #	PROCESS ID	NOVNC PROCESS ID
 :<span style="color:red">44</span>	        27644

 [gra-login1:~] vncserver -kill :<span style="color:red">44</span>
 Killing Xvnc process ID 27644

Si vous avez plusieurs vncservers actifs sur un nœud, vous pouvez les tuer TOUS du même coup avec
 [gra-login1:~] pkill Xvnc -u $USER

<span id="Multiple_connections"></span>
## Connexions multiples 

Tous les vncservers exécutés sous votre nom d'utilisateur (sur un nœud de connexion ou de calcul) peuvent être listés avec `vncserver -list`. Si un vncserver a été démarré avec l'option supplémentaire `-AlwaysShared`, plusieurs connexions peuvent être établies en créant un nouveau tunnel et un nouveau vncviewer à partir de n'importe quel emplacement distant, par exemple

 [<b>l4</b>(login node):~] vncserver -idletimeout 86400 -alwaysshared | grep -v ^$
 Desktop 'TurboVNC: l4.nibi.sharcnet:1 (yourusername)' started on display <b>l4</b>.nibi.sharcnet:1
 Starting applications specified in /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/xstartup.turbovnc
 Log file is /home/yourusername/.vnc/<b>l4</b>.nibi.sharcnet:1.log

Ainsi, on peut laisser vncviewer actif sur un ordinateur au bureau, puis se reconnecter à nouveau depuis chez soi pour accéder au même ordinateur et ensuite, par exemple, continuer à travailler de manière transparente avec les mêmes applications sans avoir à les fermer. Si toutefois un vncserver n'a pas été démarré avec `vncserver -AlwaysShared`, une seule connexion vncviewer sera possible et avant de quitter pour la maison, vous devrez fermer toutes les applications sur le bureau et fermer vncserver. Une fois à la maison, il faudra créer un nouveau bureau et ouvrir les applications pour poursuivre votre travail.

<span id="Failures_to_connect"></span>
## Échecs de connexion 

Des échecs répétés à établir une nouvelle connexion vncserver/vncviewer pourraient être causés par un tunnel SSH existant sur votre ordinateur qui bloquerait les ports. Pour déterminer la présence de tels tunnels et les tuer, ouvrez une fenêtre de terminal sur votre ordinateur et lancez la commande `ps ux | grep ssh` suivie de `kill PID`.

<span id="Unlock_screensaver"></span>
## Déverrouiller l'écran de veille 

Si votre écran de veille VNC s'éteint en raison du délai d'affichage et qu'un mot de passe vous est demandé, entrez le mot de passe de votre compte sur la grappe et non le mot de passe vncserver. 
Si le bureau MATE est en cours d'exécution et que l'écran de veille ne se déverrouille pas, essayez avec la commande `killall -9 .mate-screensaver`. Ceci ne devrait plus se produire car l'écran de veille VNC a été désactivé sur nos grappes.

<span id="Cannot_log_in"></span>
== Problème de connexion == 

La connexion à gra-vdi.alliancecan.ca se fait en deux étapes&nbsp;:

1)
 username
 Entrez votre  mot de passe pour CCDB.
2)
 username
 Entrez votre code de passe pour l'authentification multifacteur.

Si vous entrez un nom d'utilisateur/mot de passe erroné pour l'étape 1, vous aurez quand même à passer l'étape 2. Si vous saisissez ensuite votre nom d'utilisateur/mot de passe, vous recevrez un message indiquant que la connexion est établie et vous reviendrez vers l'écran de connexion de l'étape 1. La solution est de réessayer en vous assurant d'avoir saisi la bonne combinaison nom d'utilisateur/mot de passe. Si vous ne vous souvenez plus de votre mot de passe CCDB, allez sur [here](https://ccdb.alliancecan.ca/security/forgot) pour le réinitialiser, à condition que votre compte ne soit pas en attente de renouvellement par la chercheuse principale ou le chercheur principal.

<span id="OpenGL_graphics"></span>
## OpenGL 

Pour exécuter un programme graphique utilisant OpenGL accéléré par le matériel, quelques modifications seront nécessaires dans la section <i>Nœuds de calcul</i> ci-dessus.

Tout d'abord, la commande `salloc` doit être modifiée pour demander un nœud GPU. À défaut, le programme utilisera le rendu logiciel sur les CPU, ce qui est beaucoup plus lent. Pour demander le premier nœud GPU disponible (et ainsi minimiser le temps d'attente au cas où la grappe comporte plusieurs types de nœuds GPU), il suffit de spécifier

 [<b>l4</b>(login node):~] salloc --time=1:00:00 --cpus-per-task=4 --gpus-per-node=1 --mem=16000 --account=def-piname

Toutefois, si la grappe que vous utilisez comporte plusieurs types de nœuds, dont l'un est reconnu pour offrir une bonne accélération graphique, par exemple un nœud équipé d'un GPU <b>t4</b>, alors utilisez

 [<b>l4</b>(login node):~] salloc --time=1:00:00 --cpus-per-task=4 --gpus-per-node=t4:1 --mem=16000 --account=def-piname

Deuxièmement, il faudra probablement ajouter `vglrun` juste avant le nom du `PROGRAM`` sur la ligne de commande de votre terminal VNC. Par exemple

  [<b>c48</b>(compute node):~] vglrun -d egl PROGRAM

Ensuite, la fonction `vglrun` configure des variables d'environnement supplémentaires pour garantir que votre programme utilise les bibliothèques VirtualGL appropriées. Toutefois, si votre programme a déjà été modifié pour utiliser l'environnement standard cvmfs actuel, cette étape est inutile. 

<span id="Portal_alternatives"></span>
## Autres options 

Si vous rencontrez des problèmes graphiques à l'utilisation de VNC comme décrit ci-dessus, essayez d'utiliser [OpenOnDemand](https://ondemand.sharcnet.ca/) sur <b>nibi</b> ou [JupyterHub](https://jupyterhub.rorqual.alliancecan.ca) sur <b>rorqual</b>. Les deux grappes offrent une interface web VDI automatisée avec un bureau moderne qui est conçue pour une utilisation simplifiée, ainsi que des performances matérielles améliorées et une meilleure prise en charge logicielle.