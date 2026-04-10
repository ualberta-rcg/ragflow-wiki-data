---
title: "Apptainer/fr"
tags:
  []

keywords:
  []
---

<span id="Forewords"></span>
=Introduction=

<span id="Official_Apptainer_documentation"></span>
## Documentation officielle pour Apptainer

Cette page ne décrit pas toutes les fonctionnalités et ne remplace pas la [documentation officielle d'Apptainer](http://apptainer.org/docs). Nous décrivons ici l'utilisation de base, abordons certains aspects de l'utilisation sur nos systèmes et présentons des exemples. Nous vous recommandons de lire la documentation officielle sur les fonctionnalités que vous utilisez.

Pour installer Apptainer sur votre ordinateur, [consultez cette page](http://apptainer.org/docs/user/main/quick_start.html#quick-installation). Si vous utilisez une récente version de Windows, [installez d'abord WSL](https://learn.microsoft.com/fr-ca/windows/wsl/install) puis installez Apptainer dans le sous-système. Si vous utilisez macOS, installez d'abord une distribution Linux dans une machine virtuelle sur votre ordinateur, puis installez Apptainer dans la machine virtuelle.

<span id="If_you_are_currently_using_Singularity"></span>
## Si vous utilisez Singularity

Nous vous recommandons d'utiliser Apptainer plutôt que Singularity. La Fondation Linux a adopté SingularityCE (jusqu'à v3.9.5) et renommé Apptainer, avec les modifications suivantes&nbsp;:

* ajout du support pour  [DMTCP (<i>Distributed MultiThreaded Checkpointing</i>)](https://dmtcp.sourceforge.io/);
* abandon du support pour l'option `--nvccli` en ligne de commande;
* abandon du support pour `apptainer build --remote`;
* remplacement du point de chute distant SylabsCloud par un point de chute DefaultRemote, sans définition du serveur pour `library://`;
** au besoin, vous pouvez  [restorer le point de chute distant SylabsCloud](https://apptainer.org/docs/user/1.0/endpoint.html#restoring-pre-apptainer-library-behavior);
* remplacement du terme `singularity` par `apptainer` dans tous les noms d'exécutables, de chemins, etc.;
** p.ex., la commande  `singularity` est changée pour `apptainer`,
** p.ex., le répertoire `~/.singularity` est changé pour `~/.apptainer`;
* remplacement du terme `SINGULARITY` par `APPTAINER` dans toutes les variables d'environnement.

Apptainer version 1 étant compatible avec Singularity, vous pouvez utiliser les mêmes scripts.

<span id="Other_Linux_container_technologies"></span>
## Autres technologies de conteneurs Linux

Les grappes de calcul haute performance utilisent habituellement Apptainer. En réponse à plusieurs qui demandent s'il existe d'autres technologies de conteneurs Linux, voici nos commentaires sur quelques-uns&nbsp;:
* [Podman](https://podman.io/) 
** comme Apptainer, supporte l'utilisation des conteneurs normaux (<i>rootless</i>);
** est disponible sous forme de paquet pour les distributions Linux qui supportent RPM, et pour quelques autres;
** même si c’est une technologie de conteneurs Linux, [Podman peut être installé sur des ordinateurs Windows et macOS](https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md);
** Podman version 4 supporte les fichiers Apptainer .SIF.
* [Docker](https://www.docker.com/)
** Docker ne peut être utilisé sécuritairement sur les systèmes multi-utilisateurs. Il n’est donc pas offert sur nos grappes;
** dans plusieurs cas, vous pouvez construire une image Apptainer à partir d'une image Docker (voir [Construire une_image SIF](apptainer-fr#construire_une_image_sif.md) ci-dessous);
** vous pouvez installer Docker sur votre ordinateur et créer une image Apptainer qui sera ensuite téléversée sur une grappe de calcul haute performance [comme décrit ci-dessous](https://docs.alliancecan.ca/wiki/Apptainer/fr#Créer_un_conteneur_Apptainer_à_partir_de_Dockerfile).
<b></b>.

## Autres sujets
### Généralités
* Vous devez d’abord avoir une <b>image</b> de votre conteneur, c'est-à-dire un fichier .sif  ou un répertoire servant de bac à sable (<i>sandbox</i>). Si ce n’est pas le cas, voir [Construire une image Apptainer ci-dessous](apptainer-fr#construire_une_image_apptainer.md).
*En plus d’avoir installé Apptainer, vous avez aussi besoin d’installer ou de construire tous les logiciels nécessaires pour travailler dans le conteneur. [Plusieurs logiciels sont déjà installés sur nos grappes](available-software-fr.md) et vous pouvez les utiliser sans créer de conteneur.

### `sudo`
Les sites web et la documentation font souvent référence à `sudo` pour l’obtention de permissions de superutilisateur (<i>root</i>), mais ceci n’est pas possible sur nos grappes. Si vous devez utiliser `sudo`, vos options sont&nbsp;:

* Installez Linux, Apptainer et `sudo` dans une machine virtuelle sur un ordinateur que vous contrôlez, ce qui vous donnera un accès `sudo`. Construisez votre ou vos images dans cette machine et téléversez-les sur une de nos grappes.
* Au besoin, demandez l’assistance du [soutien technique](technical-support.md) pour construire votre image. S’il n’est pas possible de le faire pour vous avec `sudo`, nous pourrons peut-être vous proposer d’autres solutions.
* À partir de la version 1.1.x, le support pour l’utilisation implicite ou explicite de  `--fakeroot` rend possible des choses qui n’étaient pas possibles avec les versions antérieures ou avec Singularity, par exemple la possibilité de construire des images à partir de fichiers de définition  .def ou de construire des images sans avoir recours à `sudo`. Ceci dit, il faut se rappeler que ce ne sont pas toutes les images qui peuvent être construites sans `sudo` ou sans les permissions <i>root</i>.

### Construire des images ou des overlays
Pour construire vos propres images ou overlays&nbsp;:
* ne construisez pas une image d’un bac à sable avec `--fakeroot` dans un système de fichiers réseau; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs);
* configurez `APPTAINER_CACHEDIR` pour indiquer un endroit dans un système de fichiers qui n‘est pas en réseau; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs);
* configurez `APPTAINER_TMPDIR` pour indiquer un endroit dans un système de fichiers qui n‘est pas de type Lustre/GPFS; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs);
* n’utilisez pas les systèmes de fichiers qui sont de type Lustre/GPFS parce qu’ils n’offrent pas les fonctionnalités nécessaires pour la construction de conteneurs (en particulier `--fakeroot`); voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

=Charger le module Apptainer=
Pour utiliser la version disponible par défaut, lancez
<source lang="console">$ module load apptainer</source>

Pour connaître toutes les versions disponibles, lancez
<source lang="console">$ module spider apptainer</source>

<span id="Running_programs_within_a_container"></span>
=Exécuter des programmes dans un conteneur=

<span id="Important_command_line_options"></span>
## Options de ligne de commande à retenir

Les logiciels exécutés dans un conteneur se trouvent dans un environnement qui utilise des bibliothèques et outils différents de ceux installés dans le système hôte. Il est donc important que les programmes exécutés dans un conteneur <b>n’utilisent pas de paramètres de configuration ou de logiciels définis hors du conteneur</b>. Cependant, Apptainer adopte par défaut l’environnement de l’interpréteur de l’hôte, ce qui peut causer des problèmes à l’exécution de certains programmes. Les options suivantes utilisées avec `apptainer run`, `apptainer shell`, `apptainer exec`, et/ou `apptainer instance` évitent ces problèmes.

{| class="wikitable"
|+Options en ligne de commande

|-
| style="width: 20pt;" |`-C` || Isole le conteneur actif de <b>tous les systèmes de fichiers</b>, du PID parent, des IPC et de l’environnement. Pour accéder aux systèmes de fichiers à l’extérieur du conteneur, vous devez utiliser des [bind mounts](https://docs.alliancecan.ca/wiki/Apptainer/fr#Bind_mounts).
|-
| `-c` ||Isole le conteneur actif de <b>la plupart des systèmes de fichiers</b> en n’utilisant qu’un répertoire `/dev` minimal, un répertoire `/tmp` vide et un répertoire `/home` vide.Pour accéder aux systèmes de fichiers à l’extérieur du conteneur, vous devez utiliser des [bind mounts](https://docs.alliancecan.ca/wiki/Apptainer/fr#Bind_mounts).
|-
| `-e` || Supprime certaines variables de l’environnement de l’interpréteur avant le lancement des commandes et configure les paramètres pour une meilleure compatibilité OCI/Docker. Cette option ajoute implicitement `--containall`, `--no-init`, `--no-umask` et `--writable-tmpfs`.
|}

Une autre importante option est  `-W` ou `--workdir`. Sur nos grappes et avec la plupart des systèmes Linux, les systèmes de fichiers semblables à `/tmp` utilisent la mémoire RAM et non l’espace sur disque. Les tâches exécutées sur nos grappes disposent habituellement de peu de mémoire RAM et elles sont annulées si elles consomment plus de mémoire que ce qui a été alloué. Pour contourner ce problème, Apptainer doit utiliser un disque physique pour son répertoire de travail  (`workdir`). Pour ce faire, on utilise l’option `-W` suivie du chemin vers un disque où Apptainer peut lire et écrire des fichiers temporaires. Dans l’exemple suivant, la commande myprogram dans l’image du conteneur  `myimage.sif` spécifie le répertoire de travail `/path/to/a/workdir.
apptainer run -C -B /project -W /path/to/a/workdir myimage.sif myprogram`.

<source lang="console">apptainer run -C -B /project -W /path/to/a/workdir myimage.sif myprogram</source>

où
* l'option `workdir` peut être supprimée si aucun conteneur actif ne l’utilise.
* quand Apptainer est utilisé dans une tâche lancée avec `salloc`, `sbatch`, ou [JupyterHub](jupyterhub-fr.md) sur nos grappes, le répertoire de travail doit être `${SLURM_TMPDIR}`, par exemple `-W ${SLURM_TMPDIR}`.
** Note : Aucun programme intensif (incluant Apptainer) ne doit être exécuté sur les nœuds de connexion. Utilisez plutôt `salloc`pour démarrer  une tâche interactive.
* les bind mounts ne fonctionnent pas de la même manière sur toutes nos grappes; consultez [Bind mounts et overlays persistants ci-dessous](https://docs.alliancecan.ca/wiki/Apptainer/fr#Bind_mounts_et_overlays_persistants) pour savoir comment accéder à `/home`, `/project`, et `/scratch`.

<span id="Using_GPUs"></span>
## Utiliser des GPU

Tenez compte des points suivants quand votre logiciel dans un conteneur requiert l’utilisation de GPU&nbsp;:
*Assurez-vous de passer `--nv` (pour le matériel NVIDIA) et `--rocm` (pour le matériel AMD) aux commandes Apptainer.
**Ces options font en sorte que les entrées appropriées dans `/dev` soient incluses dans le bind mount à l’intérieur du conteneur.
**Ces options localisent les bibliothèques pour les GPU et les attachent à l’hôte, en plus de configurer la variable d’environnement `LD_LIBRARY_PATH` pour que les bibliothèques fonctionnent dans le conteneur.
*Assurez-vous que l’application qui utilise le GPU dans le conteneur a été correctement compilée pour pouvoir utiliser le GPU et ses bibliothèques.
*Pour utiliser OpenCL dans le conteneur, utilisez les options précédentes et ajoutez le bind mount `-B /etc/OpenCL`.

Voyez l'exemple sous [Travailler avec des GPU NVIDIA ci-dessous](https://docs.alliancecan.ca/wiki/Apptainer/fr#Travailler_avec_des_GPU_NVIDIA).

<span id="Using_MPI_programs"></span>
## Lancer des programmes MPI

Pour lancer des programmes MPI dans un conteneur, il faut ajuster certaines choses dans l’environnement hôte. Voyez un exemple dans  [Travailler avec des programmes MPI ci-dessous](https://docs.alliancecan.ca/wiki/Apptainer/fr#Travailler_avec_des_programmes_MPI). Vous trouverez plus d’information dans [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

<span id="Container-specific_help:_apptainer_run-help"></span>
## Aide avec `apptainer run-help`

Les conteneurs Apptainer construits à partir de [fichiers de définition](http://apptainer.org/docs/user/main/definition_files.html)  ont souvent une fonctionnalité `%help` appelée comme suit

 apptainer run-help your-container-name.sif

où
* `your-container-name.sif` est le nom du conteneur.

Si votre conteneur a aussi des applications, lancez

 apptainer run-help --app appname your-container-name.sif

où
* `appname` est le nom de l'application
* `your-container-name.sif` est le nom du conteneur

Pour obtenir la liste des applications qui se trouvent dans le conteneur, lancez

 apptainer inspect --list-apps your-container-name.sif

où 
* `your-container-name.sif` est le nom du conteneur.

<span id="Running_software:_apptainer_run_or_apptainer_exec"></span>
## Lancer un logiciel avec `apptainer run` ou `apptainer exec`

La commande `apptainer run` lance le conteneur, exécute le script `%runscript` défini pour ce conteneur (s’il y en a un), puis lance la commande spécifiée.
Pour sa part, la commande `apptainer exec,` ne va pas exécuter le script, même s’il est défini dans le conteneur.

Nous recommandons de toujours utiliser `apptainer run`.

Supposons maintenant que vous voulez compiler avec `g++`  le programme C++ `myprog.cpp` qui se trouve dans un conteneur, pour ensuite lancer le programme.  Vous pouvez utiliser

 apptainer run your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
 apptainer run your-container-name.sif ./a.out

où
* `your-container-name.sif`  est le nom du fichier .SIF
* `g++ -O2 -march=broadwell ./myprog.cpp` est la commande à exécuter dans le conteneur.

Sur nos grappes, vous devrez ajouter des options après `run`, mais avant `your-container-name.sif`, dont - `-C`, `-c`, `-e` et `-W` en plus de certaines options bind mount pour que l’espace disque soit disponible pour les programmes dans le conteneur, par exemple

  apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
  apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch ./a.out

Pour plus d'information, consultez

* [Options de ligne de commande à retenir](https://docs.alliancecan.ca/wiki/Apptainer/fr#Options_de_ligne_de_commande_à_retenir)
* [Utiliser des GPU](https://docs.alliancecan.ca/wiki/Apptainer/fr#Utiliser_des_GPU)
* [Bind mounts et overlays persistants](https://docs.alliancecan.ca/wiki/Apptainer/fr#Bind_mounts_et_overlays_persistants)

Consultez aussi la [documentation officielle pour Apptainer](http://apptainer.org/docs/user/main/index.html).

<span id="Interactively_running_software:_apptainer_shell"></span>
## Interactivité  avec `apptainer shell`

Les commandes `apptainer run`, `apptainer exec` et `apptainer instance` exécutent immédiatement les programmes, ce qui est parfait dans les scripts de tâches pour BASH et Slurm. Il peut parfois être nécessaire de travailler interactivement dans un conteneur; pour ce faire, utilisez la commande `apptainer shell`.

Par exemple

 apptainer shell your-container-name.sif

où
* `your-container-name.sif` est le nom de votre fichier SIF

Quand le conteneur est prêt, l’invite  `Apptainer&gt;` s’affichera (ou `Singularity&gt;` dans le cas des versions antérieures). Entrez alors les commandes pour l’interpréteur, puis entrez `exit` et appuyez sur la touche Enter/Return pour sortir du conteneur.

Sur nos grappes, vous devrez ajouter des options après `run`, mais avant `your-container-name.sif`, dont - `-C`, `-c`, `-e` et `-W` en plus de certaines options bind mount pour que l’espace disque soit disponible pour les programmes dans le conteneur, par exemple

  apptainer shell -C -W $SLURM_TMPDIR -B /home:/cluster_home -B /project -B /scratch your-container-name.sif

Pour plus d'information, consultez

* [Options de ligne de commande à retenir](https://docs.alliancecan.ca/wiki/Apptainer/fr#Options_de_ligne_de_commande_à_retenir)
* [Utiliser des GPU](https://docs.alliancecan.ca/wiki/Apptainer/fr#Utiliser_des_GPU)
* [Bind mounts et overlays persistants](https://docs.alliancecan.ca/wiki/Apptainer/fr#Bind_mounts_et_overlays_persistants)

Consultez aussi la [documentation officielle d'Apptainer](http://apptainer.org/docs/user/main/index.html).

<b>IMPORTANT :</b> Si vous utilisez une image d’un overlay persistant (dans un fichier SIF ou un fichier distinct) et que vous voulez que cette image reflète les modifications, il faut, en plus des options nommées ci-dessus, passer au conteneur l’option `-w` ou `--writable`, autrement les modifications faites dans la session code>apptainer shell</code> ne seront pas sauvegardées.

<span id="Running_daemons:_apptainer_instance"></span>
## Utiliser des démons avec `apptainer instance`

Apptainer est conçu pour exécuter correctement des démons pour des tâches de calcul sur des grappes, en partie à l’aide de la commande `apptainer instance`. Voir les détails dans [Running Services](http://apptainer.org/docs/user/main/running_services.html) de la documentation officielle.

<b>Remarque 1 :</b> N’exécutez pas manuellement un démon sans utiliser `apptainer instance` et les autres commandes reliées. Apptainer fonctionne bien avec d’autres outils comme l’ordonnanceur Slurm employé sur nos grappes. Quand une tâche plante, est annulée ou se termine de toute autre façon, les démons lancés avec `apptainer instance` ne seront pas bloqués et ne laisseront pas de processus défunts. Aussi, la commande `apptainer instance` vous permet de contrôler les démons et les programmes qui sont exécutés dans un même conteneur.

<b>Remarque 2 :</b> Les démons ne sont exécutés que lorsque la tâche est en marche. Si l'ordonnanceur annule la tâche, tous les démons qui lui sont rattachés seront aussi annulés. Si vous avez besoin de démons qui restent actifs au-delà du temps d’exécution, vous pouvez à la place les exécuter  dans une machine virtuelle, dans un nuage; contactez alors le [soutien technique](technical-support-fr.md).

<span id="Running_MPI_programs"></span>
## Travailler avec des programmes MPI

L’exécution de programmes MPI sur des nœuds dans un conteneur Apptainer requiert une configuration particulière. La communication entre les nœuds est beaucoup plus efficace avec MPI en raison de sa bonne utilisation du matériel d’interconnexion. Ceci se fait habituellement de façon automatique et ne cause aucun souci, sauf quand le programme utilise plusieurs nœuds dans une grappe.

<b>Remarque :</b>  Quand tous les processus MPI sont exécutés dans un conteneur Apptainer sur un seul nœud à mémoire partagée, le matériel d'interconnexion n’est pas sollicité et aucun problème ne survient, par exemple avec l’option  `--nodes=1` dans un script `sbatch`. Par contre, si le nombre de nœuds n'est pas <b>explicitement défini</b> comme étant `1`, l’ordonnanceur peut choisir d’exécuter le programme MPI sur plusieurs nœuds et il est possible que la tâche ne puisse pas être exécutée.

(contenu en préparation)

<span id="Bind_mounts_and_persistent_overlays"></span>
=Bind mounts et overlays persistants=

Apptainer offre les fonctionnalités suivantes :
* <b>bind mounts</b>, pour avoir accès à l’espace disque à l’extérieur du conteneur;
* <b>persistent overlays</b>, pour superposer un système de fichiers en lecture/écriture à un conteneur immuable (lecture seulement).

## Bind mounts

L'utilisation des options  `-C` ou `-c`  avec un conteneur empêche l’accès à votre espace disque. Pour y pallier, il faut explicitement demander le  bind mount de cet espace. Supposons que l’option `-C` est utilisée dans une tâche

 apptainer run -C -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt

où `./my_data_file.txt` est un fichier dans le répertoire courant de l’hôte, c’est-à-dire que le fichier n’est pas situé dans le conteneur. L’option `-C` fait en sorte que le programme `wc` dans le conteneur n'aura pas accès au fichier et une erreur d’accès surviendra. Pour éviter ceci, il faut faire un bind mount du répertoire courant

 apptainer run -C -B . -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt

où `-B .` fait le bind mount du répertoire courant `.`.

Même s’il est possible de créer plusieurs bind mount, il est souvent plus simple de faire le bind mount du répertoire de niveau supérieur sous lequel les répertoires sont situés. Par exemple, sur nos grappes, vous pouvez utiliser

 apptainer run -C -B /project -B /scratch -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt

où 
* `-B /project` fait le bind mount du système de fichiers /project 
* `-B /scratch` fait le bind mount du système de fichiers /scratch

Ceci est particulièrement utile 
*pour avoir accès aux fichiers des autres membres de votre équipe,
*pour avoir accès aux fichiers et répertoires dont certains sont des `symlinks` vers différents endroits et qui pourraient être inaccessibles si le bind mount n’est pas fait pour le système de fichiers au complet.

Si les bind mount ne fonctionnent pas sur la grappe que vous utilisez, lancez le script suivant pour obtenir les options qui doivent être passées à Apptainer.

 /home/preney/public/apptainer-scripts/get-apptainer-options.sh

Le bind mount ne doit pas nécessairement être au même endroit dans le conteneur. Vous pouvez faire le bind mount d’un fichier ou d’un répertoire ailleurs, par exemple

 apptainer run -C -B ./my_data_file.txt:/special/input.dat -W $SLURM_TMPDIR a-container.sif wc -l /special/input.dat

où le bind mount `-B ./my_data_file.txt:/special/input.dat` associe le fichier `./my_data_file.txt` au fichier `/special/input.dat` dans le conteneur, pour être traité avec la commande `wc`. Ceci est utile quand des programmes ou des scripts dans un conteneur contiennent des chemins figés dans le code (<i>hard coded</i>) vers des fichiers ou des répertoires qui sont situés ailleurs.

Si vous avez besoin de faire le bind mount du système de fichiers /home dans votre conteneur, utilisez un autre répertoire de destination comme

* `-B /home:/cluster_home`

Ceci fait en sorte que les fichiers de configuration et les programmes qui sont dans votre répertoire /home n'interfèreront pas avec les logiciels dans votre conteneur. À l’inverse, si vous utilisez `-B /home`, les programmes dans `$HOME/bin` et les paquets Python dans `$HOME/.local/lib/python3.x` pourraient être utilisés plutôt que les fichiers correspondants du conteneur.

Enfin, <b>évitez de faire le bind mount de CVMFS dans vos conteneurs</b>.  Les programmes fournis par CVMFS peuvent être incompatibles avec vos conteneurs. L’objectif d’un conteneur est de fournir un environnement complet qui ne dépend pas de logiciels externes. Les programmes exécutés dans un conteneur devraient s’y trouver en entier et ceux qui ne sont pas nécessaires ne devraient pas y être ajoutés.

<span id="Persistent_overlays"></span>
## Overlays persistants

Voir les détails dans [Persistent Overlays](https://apptainer.org/docs/user/main/persistent_overlays.html) de la documentation officielle.

<span id="Building_an_Apptainer_image"></span>
=Construire une image Apptainer=

<b>ATTENTION :</b> Lisez d’abord les  recommandations ci-dessus dans [Construire des images ou des overlays](https://docs.alliancecan.ca/wiki/Apptainer/fr#Construire_des_images_ou_des_overlays) ci-dessus.

Une image Apptainer peut être

* un fichier `SIF` ou 
* un répertoire servant de bac à sable (<i>sandbox</i>).

Un fichier SIF peut contenir un ou plusieurs systèmes de fichiers `squashfs` compressés et en lecture seule. Il est aussi possible qu’un fichier `SIF`  contienne des fichiers en lecture-écriture et/ou des images overlay, mais nous n’abordons pas ces cas ici; consultez plutôt [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs). À moins d’employer des méthodes plus complexes pour créer une image, la commande Apptainer code>build</code> produit un fichier SIF composé d’un système de fichiers `squashfs` en lecture seule. Ceci est la meilleure option, car l’image en lecture seule restera telle quelle et elle sera plus compacte; il faut se rappeler que les opérations de lecture de cette image se font à très grande vitesse.

<b>Un répertoire bac à sable</b> est un répertoire ordinaire qui est vide au début et auquel Apptainer ajoute les fichiers et les répertoires au fur et à mesure que l’image est construite. L’accès au répertoire et sa mise à jour doivent se faire uniquement via Apptainer. Un bac à sable est utile quand il faut accéder à l’image en lecture-écriture  pour la modifier. Par contre, si les modifications sont peu fréquentes, il est préférable d’utiliser un fichier `SIF`. Il est possible de construire une image, faire des modifications puis construire un nouveau fichier `SIF` pour l’image modifiée, par exemple

<source lang="console">$ cd $HOME
$ mkdir mynewimage.dir
$ apptainer build mynewimage.dir myimage.sif
$ apptainer shell --writable mynewimage.dir
Apptainer> # Run commands to update mynewimage.dir here.
Apptainer> exit
$ apptainer build newimage.sif mynewimage.dir
$ rm -rf mynewimage.dir</source>

L’utilisation d’un fichier `SIF` est recommandée car la performance à partir de l’image du conteneur est plus rapide que lorsque chaque fichier  est stocké séparément dans les systèmes de fichiers de nos grappes, qui sont optimisés pour traiter des fichiers de grande taille et pour les opérations parallèles de lecture et d’écriture. Aussi, contrairement à une image SIF, un bac à sable aura un impact important sur le nombre de fichiers que vous stockez, alors que ce nombre est limité par un quota. (Certaines images peuvent contenir des milliers de fichiers et de répertoires.)

Les permissions <i>root</i> sont requises pour l’utilisation des gestionnaires de paquets des distributions Linux; un simple utilisateur ne peut donc pas construire des images sur nos grappes de calcul avec Apptainer 1.0.x et les versions Singularity précédentes. Au besoin, écrivez au [soutien technique](technical-support-fr.md) pour de l’assistance dans la création de votre image ou utilisez un ordinateur où Apptainer est installé et où vous avez les permissions <i>root</i>.

L’option `--fakeroot` d’Apptainer est utilisée pour créer et manipuler des images. Avec les versions antérieures à  1.1, il faut contacter le [soutien technique](technical-support-fr.md) et demander qu’un administrateur accorde la permission d’utiliser `--fakeroot` sur la grappe utilisée, ce qui n’est pas toujours possible. Avec Apptainer version 1.1, `--fakeroot` peut être utilisée sans permission supplémentaire.

Certains conteneurs ne peuvent être créés si vous n’avez pas les permissions <i>root</i>. De tels conteneurs ne peuvent pas être construits sur nos grappes.

Si tout ce dont vous avez besoin est une image Docker telle quelle, vous pourrez souvent la construire et l’exécuter facilement sans les permissions <i>root</i> et sans l’utilisation de `--fakeroot`.  Si par la suite vous devez modifier l’image, vous devrez peut-être avoir les permissions <i>root</i>, par exemple pour utiliser un gestionnaire de paquets. Pour cette raison, les exemples suivants supposent l’utilisation d'une image Docker telle quelle.

<span id="Building_an_SIF_image"></span>
## Construire une image SIF

<b>ATTENTION :</b> Veuillez tenir compte des recommandations faites dans [Construire des images ou des overlays](https://docs.alliancecan.ca/wiki/Apptainer/fr#Construire_des_images_ou_des_overlays) ci-dessus.

Pour construire l’image d’un fichier SIF avec la plus récente image busybox de Docker, lancez
<source lang="console">$ apptainer build bb.sif docker://busybox</source>

Pour des fonctions plus avancées, voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

<span id="Building_a_sandbox_image"></span>
## Construire un bac à sable

<b>ATTENTION :</b> Veuillez tenir compte des recommandations faites dans [Construire des images ou des overlays](https://docs.alliancecan.ca/wiki/Apptainer/fr#Construire_des_images_ou_des_overlays) ci-dessus.

Pour construire un bac à sable plutôt qu’un fichier SIF, remplacez le nom du fichier SIF par `--sandbox DIR_NAME` ou `-s DIR_NAME` où `DIR_NAME` est le nom du répertoire à créer pour le bac à sable.  Par exemple, pour créer un fichier SIF avec `apptainer build`, la commande est
<source lang="console">$ apptainer build bb.sif docker://busybox</source>
Remplacez `bb.sif` par un nom de répertoire, par exemple `bb.dir`, avec l’option  `--sandbox`.
<source lang="console">$ apptainer build --sandbox bb.dir docker://busybox</source>

Rappelons les  différences entre un fichier SIF et un bac à sable&nbsp;:

*l’image du conteneur est contenue dans un seul fichier SIF compressé, en lecture seule,
*les fichiers individuels formant l’image du conteneur sont placés dans un répertoire servant de bac à sable. Ces fichiers ne sont pas compressés, peuvent être nombreux (plusieurs milliers) et sont accessibles en lecture-écriture.

L’utilisation d’un bac à sable entame significativement vos quotas d’espace disque et de nombre de fichiers. Si vous n’avez pas besoin d’un accès en lecture et en écriture fréquent à l’image du conteneur, il est recommandé d’utiliser un fichier SIF. Ce dernier offre aussi un accès plus rapide.

<span id="Example_use_cases"></span>
=Cas d'usage=

<span id="Using_Conda_in_Apptainer"></span>
## Travailler avec Conda 

<span id="Using_Spack_in_Apptainer"></span>
## Travailler avec Spack 

(contenu en préparation)

<span id="Using_NVIDIA_GPUs_in_Apptainer"></span>
## Travailler avec des GPU NVIDIA 

(contenu en préparation)

<span id="Using_MPI_in_Apptainer"></span>
## Travailler avec MPI

(contenu en préparation)

<span id="Creating_an_Apptainer_container_from_a_Dockerfile"></span>
## Créer un conteneur Apptainer à partir de Dockerfile

<b>Remarque : Il faut d’abord installer Docker et Apptainer sur un ordinateur où vous disposez des permissions nécessaires. Les commandes présentées ici ne fonctionnent pas sur nos grappes.</b>

Malheureusement, certains projets logiciels offrent un fichier d’instructions Dockerfile mais pas d’image de conteneur. Il faut alors créer une image à partir du fichier Dockerfile. Cependant, Docker n’est pas installé sur nos grappes. Ceci dit, si vous pouvez travailler avec un ordinateur où Docker et Apptainer sont installés et où vous avez les permissions suffisantes (accès <i>root</i> ou `sudo`, ou appartenance au groupe `docker` et permission `--fakeroot`) , les commandes suivantes vous permettront d'utiliser Docker puis Apptainer pour construire une image Apptainer sur cet ordinateur.

Remarque : Docker pourrait planter si vous ne faites pas partie du groupe `docker`. Il pourrait aussi s’avérer impossible de créer certains conteneurs sans les permissions <i>root</i>,  `sudo` ou `--fakeroot`. Vérifiez que vous possédez les permissions nécessaires.

Si vous n'avez qu'un Dockerfile et que vous voulez créer une image Apptainer, lancez la commande suivante sur un ordinateur où Docker et Apptainer sont installés et où vous disposez des permissions nécessaires.

 docker build -f Dockerfile -t your-tag-name
 docker save your-tag-name -o your-tarball-name.tar
 docker image rm your-tag-name
 apptainer build --fakeroot your-sif-name.sif docker-archive://your-tarball-name.tar
 rm your-tarball-name.tar

où

*`your-tag-name` est le nom à donner au conteneur Docker,
*`your-tarball-name.tar` est le nom à donner au fichier dans lequel Docker sauvegardera le contenu généré pour le conteneur,
*`--fakeroot` peut être omis si c’est optionnel; pour utiliser plutôt `sudo`, omettez `--fakeroot` et ajoutez `sudo`en préfixe à la ligne,
*`your-sif-name.sif` est le nom du fichier SIF pour le conteneur Apptainer.

Le fichier SIF résultant est un conteneur Apptainer correspondant aux instructions Dockerfile. Copiez le fichier SIF sur la ou les grappes que vous voulez utiliser.

<b>Remarque :</b> Il est possible que le Dockerfile ajoute des couches additionnelles; vous n’avez qu’à les supprimer avec

 docker images

puis `docker image rm ID` (où ID est l’identifiant de l’image obtenue par la commande `docker images`). Ceci libère l’espace disque occupé par les couches additionnelles.

<span id="Miscellaneous_items"></span>
=Sujets divers=

<span id="Cleaning_Apptainer&#039;s_cache_directory"></span>
## Vider le répertoire cache

Pour trouver les fichiers du répertoire cache, lancez

 apptainer cache list

Supprimez les fichiers avec

 apptainer cache clean

<span id="Changing_Apptainer&#039;s_default_directories"></span>
## Modifier les répertoires par défaut

Avant de lancer Apptainer, configurez les variables d’environnement suivantes pour utiliser d’autres répertoires temporaires et cache que ceux désignés par défaut.

* `APPTAINER_CACHEDIR` : répertoire où les fichiers sont téléchargés et mis en cache par Apptainer
* `APPTAINER_TMPDIR` : répertoire où Apptainer enregistre les fichiers temporaires, incluant pour la création d’images `squashfs`

Par exemple, pour qu’Apptainer utilise votre espace /scratch pour la cache et les fichiers temporaires (ce qui est probablement le meilleur endroit), utilisez

 $ mkdir -p /scratch/$USER/apptainer/{cache,tmp}
 $ export APPTAINER_CACHEDIR="/scratch/$USER/apptainer/cache"
 $ export APPTAINER_TMPDIR="/scratch/$USER/apptainer/tmp"

avant de lancer Apptainer.