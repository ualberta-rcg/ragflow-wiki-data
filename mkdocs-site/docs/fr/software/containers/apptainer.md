---
title: "Apptainer/fr"
slug: "apptainer"
lang: "fr"

source_wiki_title: "Apptainer/fr"
source_hash: "93c1f864f7c06e94a1094f4322a8f43a"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:48:28.981341+00:00"

tags:
  []

keywords:
  - "conteneur .sif"
  - "sandbox"
  - "bibliothèques GPU"
  - "compatibilité version MPI"
  - "sudo"
  - "GPU"
  - "gestionnaire de paquets"
  - "construction d'images"
  - "MPI"
  - "Docker"
  - "apptainer instance"
  - "module load avant apptainer"
  - "persistent overlays"
  - "mpirun"
  - "Podman"
  - "espace disque"
  - "Apptainer"
  - "Singularity"
  - "environnement de l’interpréteur de l’hôte"
  - "Persistent Overlays"
  - "squashfs en lecture seule"
  - "création d'image Apptainer depuis Dockerfile"
  - "paramètres de configuration"
  - "option writable"
  - "docker build -f Dockerfile -t"
  - "Dockerfile"
  - "apptainer run"
  - "permissions root"
  - "option --fakeroot"
  - "bind mounts"
  - "modèle hybride"
  - "APPTAINER_CACHEDIR"
  - "Construire une image Apptainer"
  - "recommandations"
  - "conteneur immuable"
  - "sbatch"
  - "permissions root ou sudo"
  - "GPU avec OpenCL"
  - "overlays persistants"
  - "un seul nœud"
  - "bind mount"
  - "variable d’environnement LD_LIBRARY_PATH"
  - "option -B"
  - "apptainer exec"
  - "fichier SIF"
  - "interactivité"
  - "répertoire bac à sable"
  - "construction d'image"
  - "apptainer build"
  - "apptainer cache clean"
  - "apptainer build --fakeroot"
  - "options bind mount"
  - "image .sif"
  - "options --rocm"
  - "apptainer run vs exec"
  - "groupe docker"
  - "bac à sable"
  - "--fakeroot"
  - "permissions docker"
  - "options --nv"
  - "Apptainer run-help"
  - "apptainer shell"
  - "conteneur interactif"
  - "image Docker"
  - "option -C"
  - "mpirun dans le conteneur"
  - "option --nv"
  - "répertoire de travail"
  - "option -W"
  - "options de ligne de commande"

questions:
  - "Quelles sont les principales différences et changements entre Singularity et Apptainer mentionnés dans le texte ?"
  - "Comment installer Apptainer sur les différents systèmes d’exploitation (Windows, macOS, Linux) selon les recommandations fournies ?"
  - "Quelles alternatives de conteneurs Linux sont présentées et quelles sont leurs limites ou compatibilités avec les environnements HPC ?"
  - "Pourquoi l’utilisation de <code>sudo</code> n’est‑elle pas possible sur les grappes et quelles alternatives sont proposées ?"
  - "Quelles précautions doit‑on prendre lors de la construction d’images ou d’overlays avec <code>--fakeroot</code> sur des systèmes de fichiers réseau comme Lustre/GPFS ?"
  - "Quelles options de ligne de commande d’Apptainer sont recommandées pour éviter les conflits entre l’environnement de l’hôte et celui du conteneur ?"
  - "Quelle est la première étape nécessaire avant de créer un conteneur Apptainer à partir d’un Dockerfile ?"
  - "Où peut‑on trouver les instructions détaillées pour créer une image Apptainer à partir d’un Dockerfile ?"
  - "Que doit‑on faire si l’on ne possède pas encore de fichier .sif ou de répertoire sandbox pour le conteneur ?"
  - "Quelles sont les conséquences de l’adoption par défaut de l’environnement de l’interpréteur de l’hôte par Apptainer lors de l’exécution de programmes ?"
  - "Quelles options de ligne de commande peuvent être utilisées avec les commandes <code>apptainer run</code>, <code>apptainer shell</code>, <code>apptainer exec</code> et <code>apptainer instance</code> pour prévenir les problèmes liés à cet environnement ?"
  - "Pourquoi Apptainer ne nécessite‑t‑il aucun paramètre de configuration ou logiciel défini hors du conteneur pour fonctionner correctement ?"
  - "Quelle est la différence entre les options `-C` et `-c` d’Apptainer en termes d’isolation des systèmes de fichiers et des ressources ?"
  - "Pourquoi et comment doit‑on utiliser l’option `-W` (ou `--workdir`) pour définir un répertoire de travail sur les grappes, notamment avec `${SLURM_TMPDIR}` ?"
  - "Quelles options (`--nv` ou `--rocm`) sont nécessaires pour activer les GPU dans un conteneur Apptainer et quels changements apportent‑elles au bind mount et aux variables d’environnement ?"
  - "Quels sont les rôles des options `--nv` et `--rocm` dans les commandes Apptainer ?"
  - "Comment ces options influencent‑elles le bind‑mount des entrées du répertoire `/dev` à l’intérieur du conteneur ?"
  - "De quelle façon les bibliothèques GPU sont‑elles localisées et la variable d’environnement `LD_LIBRARY_PATH` configurée grâce à ces options ?"
  - "Comment configurer correctement un conteneur Apptainer pour utiliser le GPU, notamment quels bind mounts et options de ligne de commande sont nécessaires ?"
  - "Quelle est la différence entre les commandes `apptainer run` et `apptainer exec`, et pourquoi recommande‑t‑on généralement d’utiliser `apptainer run` ?"
  - "Comment compiler et exécuter un programme C++ à l’intérieur d’un conteneur Apptainer, en incluant les options spécifiques (‑C, ‑W, bind mounts, etc.) requises sur les grappes ?"
  - "Quels sont les options de ligne de commande (ex. ‑C, ‑W, ‑B, etc.) à ajouter lors de l’exécution d’un conteneur Apptainer sur les grappes, et à quoi servent‑elles ?"
  - "Comment rendre les modifications d’un overlay persistant sauvegardées dans une session Apptainer, et quelle option doit‑on spécifier ?"
  - "Pourquoi faut‑il utiliser la commande `apptainer instance` pour lancer des démons, et quelles sont les conséquences sur ces démons si la tâche est annulée ou se termine ?"
  - "Quelle est la différence entre les commandes `apptainer run`, `apptainer exec`, `apptainer instance` et `apptainer shell` ?"
  - "Dans quels scénarios est‑il recommandé d’utiliser `apptainer shell` pour travailler de façon interactive dans un conteneur ?"
  - "Comment lancer et utiliser une session interactive avec la commande `apptainer shell` ?"
  - "Qu’est‑ce qu’un « persistent overlay » et comment permet‑il de superposer un système de fichiers en lecture/écriture sur un conteneur immuable ?"
  - "Pourquoi l’utilisation des options `-C` ou `-c` empêche‑t‑elle l’accès à l’espace disque depuis le conteneur ?"
  - "Comment demander explicitement un bind mount pour accéder à l’espace disque extérieur lorsqu’on utilise l’option `-C` dans une tâche ?"
  - "Pourquoi l’option ‑C empêche‑t‑elle l’accès au fichier ./my_data_file.txt depuis le conteneur ?"
  - "Comment l’option ‑B doit‑elle être utilisée pour monter correctement des répertoires ou des fichiers (ex. ‑B ./my_data_file.txt:/special/input.dat) et quels sont les bénéfices de monter les systèmes de fichiers de niveau supérieur comme /project ou /scratch ?"
  - "Quelles sont les recommandations concernant le bind‑mount du répertoire /home et l’évitement du bind‑mount de CVMFS dans un conteneur Apptainer ?"
  - "Que sont les « overlays persistants » dans Apptainer et où peut‑on consulter leur documentation détaillée ?"
  - "Quelle section de la documentation officielle doit‑on lire avant de construire une image Apptainer ?"
  - "Quels sont les prérequis ou recommandations à suivre, selon le lien fourni, avant de créer des images ou des overlays avec Apptainer ?"
  - "Quelle est la différence principale entre une image Apptainer au format SIF et un répertoire bac à sable, et dans quels cas chaque type est recommandé ?"
  - "Pourquoi l’utilisation d’un fichier SIF est‑elle généralement préférable en termes de performances et de gestion des quotas sur les grappes de calcul ?"
  - "Quelles sont les exigences de permissions (root, --fakeroot) pour créer ou modifier des images Apptainer sur les grappes, et comment peut‑on contourner ces limitations ?"
  - "Pourquoi peut‑on généralement construire et exécuter une image Docker sans les permissions root ni l’option --fakeroot ?"
  - "Dans quelles situations est‑il nécessaire d’obtenir les permissions root pour modifier une image Docker, par exemple lors de l’utilisation d’un gestionnaire de paquets ?"
  - "Pourquoi les exemples fournis supposent‑ils l’utilisation d’une image Docker « telle quelle » ?"
  - "Quelle commande faut‑il utiliser pour construire une image SIF à partir d’une image Docker, par exemple busybox ?"
  - "Quelles sont les différences majeures entre un fichier SIF et un bac à sable, et dans quels cas recommande‑t‑on d’utiliser l’un plutôt que l’autre ?"
  - "Quelles options de ligne de commande et quels modules doivent être chargés pour exploiter correctement les GPU (NVIDIA ou AMD) ou MPI avec Apptainer ?"
  - "Quels sont les deux modèles d’exécution MPI avec Apptainer et lequel est recommandé ?"
  - "Pourquoi la version de MPI installée dans le conteneur doit‑être compatible avec le module chargé sur l’hôte, et comment doit‑on charger ce module avant d’exécuter Apptainer ?"
  - "Quelles sont les étapes nécessaires pour créer une image Apptainer à partir d’un Dockerfile lorsqu’on ne dispose pas de Docker sur les grappes ?"
  - "Quelle est la méthode la plus simple pour exécuter une application MPI avec Apptainer ?"
  - "Comment le script de tâche SLURM doit‑il être configuré pour allouer les ressources nécessaires à une exécution MPI sur un seul nœud ?"
  - "Quelle commande permet de lancer le programme MPI à l’intérieur du conteneur Apptainer dans l’exemple fourni ?"
  - "Pourquoi Docker n’est‑il pas installé sur les grappes mentionnées dans le texte ?"
  - "Quelles permissions sont nécessaires sur l’ordinateur pour pouvoir utiliser Docker puis Apptainer ?"
  - "Quelle procédure le texte décrit‑il pour construire une image Apptainer à partir d’un Dockerfile ?"
  - "Quelles permissions sont nécessaires pour exécuter Docker et créer des conteneurs Apptainer sans rencontrer d’erreurs ?"
  - "Quelles sont les étapes exactes, depuis la construction d’une image Docker jusqu’à l’obtention d’un fichier SIF Apptainer, en incluant les options « --fakeroot » ou « sudo » ?"
  - "Comment configurer et nettoyer les répertoires de cache et temporaires d’Apptainer à l’aide des variables d’environnement APPTAINER_CACHEDIR et APPTAINER_TMPDIR ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

## Documentation officielle pour Apptainer

Cette page ne décrit pas toutes les fonctionnalités et ne remplace pas la [documentation officielle d'Apptainer](http://apptainer.org/docs). Nous décrivons ici l'utilisation de base, abordons certains aspects de l'utilisation sur nos systèmes et présentons des exemples. Nous vous recommandons de lire la documentation officielle sur les fonctionnalités que vous utilisez.

Pour installer Apptainer sur votre ordinateur, [consultez cette page](http://apptainer.org/docs/user/main/quick_start.html#quick-installation). Si vous utilisez une récente version de Windows, [installez d'abord WSL](https://learn.microsoft.com/fr-ca/windows/wsl/install) puis installez Apptainer dans le sous-système. Si vous utilisez macOS, installez d'abord une distribution Linux dans une machine virtuelle sur votre ordinateur, puis installez Apptainer dans la machine virtuelle.

## Si vous utilisez Singularity

Nous vous recommandons d'utiliser Apptainer plutôt que Singularity. La Fondation Linux a adopté SingularityCE (jusqu'à v3.9.5) et l'a renommé Apptainer, avec les modifications suivantes :

*   ajout du support pour [DMTCP (*Distributed MultiThreaded Checkpointing*)](https://dmtcp.sourceforge.io/) ;
*   abandon du support pour l'option de ligne de commande `--nvccli` ;
*   abandon du support pour `apptainer build --remote` ;
*   remplacement du point de chute distant SylabsCloud par un point de chute DefaultRemote, sans définition du serveur pour `library://` ;
    *   au besoin, vous pouvez [restaurer le point de chute distant SylabsCloud](https://apptainer.org/docs/user/1.0/endpoint.html#restoring-pre-apptainer-library-behavior) ;
*   remplacement du terme `singularity` par `apptainer` dans tous les noms d'exécutables, de chemins, etc. ;
    *   p.ex., la commande `singularity` est changée pour `apptainer`,
    *   p.ex., le répertoire `~/.singularity` est changé pour `~/.apptainer` ;
*   remplacement du terme `SINGULARITY` par `APPTAINER` dans toutes les variables d'environnement.

Apptainer version 1 étant compatible avec Singularity, vous pouvez utiliser les mêmes scripts.

## Autres technologies de conteneurs Linux

Les grappes de calcul haute performance utilisent habituellement Apptainer. En réponse à plusieurs qui demandent s'il existe d'autres technologies de conteneurs Linux, voici nos commentaires sur quelques-uns :
*   [Podman](https://podman.io/)
    *   comme Apptainer, supporte l'utilisation des conteneurs normaux (*rootless*) ;
    *   est disponible sous forme de paquet pour les distributions Linux qui supportent RPM, et pour quelques autres ;
    *   même si c'est une technologie de conteneurs Linux, [Podman peut être installé sur des ordinateurs Windows et macOS](https://github.com/containers/podman/blob/main/docs/tutorials/mac_win_client.md) ;
    *   Podman version 4 supporte les fichiers Apptainer .SIF.
*   [Docker](https://www.docker.com/)
    *   Docker ne peut être utilisé sécuritairement sur les systèmes multi-utilisateurs. Il n'est donc pas offert sur nos grappes ;
    *   dans plusieurs cas, vous pouvez construire une image Apptainer à partir d'une image Docker (voir Construire une image SIF ci-dessous) ;
    *   vous pouvez installer Docker sur votre ordinateur et créer une image Apptainer qui sera ensuite téléversée sur une grappe de calcul haute performance comme décrit ci-dessous.

## Autres sujets
### Généralités
*   Vous devez d'abord avoir une **image** de votre conteneur, c'est-à-dire un fichier .sif ou un répertoire servant de bac à sable (*sandbox*). Si ce n'est pas le cas, voir Construire une image Apptainer ci-dessous.
*   En plus d'avoir installé Apptainer, vous avez aussi besoin d'installer ou de construire tous les logiciels nécessaires pour travailler dans le conteneur. Plusieurs logiciels sont déjà installés sur nos grappes et vous pouvez les utiliser sans créer de conteneur.

### `sudo`
Les sites web et la documentation font souvent référence à `sudo` pour l'obtention de permissions de superutilisateur (*root*), mais ceci n'est pas possible sur nos grappes. Si vous devez utiliser `sudo`, vos options sont :

*   Installez Linux, Apptainer et `sudo` dans une machine virtuelle sur un ordinateur que vous contrôlez, ce qui vous donnera un accès `sudo`. Construisez votre ou vos images dans cette machine et téléversez-les sur une de nos grappes.
*   Au besoin, demandez l'assistance du [soutien technique](../../support/technical_support.md) pour construire votre image. S'il n'est pas possible de le faire pour vous avec `sudo`, nous pourrons peut-être vous proposer d'autres solutions.
*   À partir de la version 1.1.x, le support pour l'utilisation implicite ou explicite de `--fakeroot` rend possible des choses qui n'étaient pas possibles avec les versions antérieures ou avec Singularity, par exemple la possibilité de construire des images à partir de fichiers de définition .def ou de construire des images sans avoir recours à `sudo`. Ceci dit, il faut se rappeler que ce ne sont pas toutes les images qui peuvent être construites sans `sudo` ou sans les permissions *root*.

### Construire des images ou des overlays
Pour construire vos propres images ou overlays :
*   ne construisez pas une image d'un bac à sable avec `--fakeroot` dans un système de fichiers réseau ; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs) ;
*   configurez `APPTAINER_CACHEDIR` pour indiquer un endroit dans un système de fichiers qui n'est pas en réseau ; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs) ;
*   configurez `APPTAINER_TMPDIR` pour indiquer un endroit dans un système de fichiers qui n'est pas de type Lustre/GPFS ; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs) ;
*   n'utilisez pas les systèmes de fichiers qui sont de type Lustre/GPFS parce qu'ils n'offrent pas les fonctionnalités nécessaires pour la construction de conteneurs (en particulier `--fakeroot`) ; voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

# Charger le module Apptainer
Pour utiliser la version disponible par défaut, lancez
```bash
$ module load apptainer
```

Pour connaître toutes les versions disponibles, lancez
```bash
$ module spider apptainer
```

# Exécuter des programmes dans un conteneur

## Options de ligne de commande à retenir

Les logiciels exécutés dans un conteneur se trouvent dans un environnement qui utilise des bibliothèques et outils différents de ceux installés dans le système hôte. Il est donc important que les programmes exécutés dans un conteneur **n'utilisent pas de paramètres de configuration ou de logiciels définis hors du conteneur**. Cependant, Apptainer adopte par défaut l'environnement de l'interpréteur de l'hôte, ce qui peut causer des problèmes à l'exécution de certains programmes. Les options suivantes utilisées avec `apptainer run`, `apptainer shell`, `apptainer exec`, et/ou `apptainer instance` évitent ces problèmes.

| Option | Description |
| :----- | :---------- |
| `-C`   | Isole le conteneur actif de **tous les systèmes de fichiers**, du PID parent, des IPC et de l'environnement. Pour accéder aux systèmes de fichiers à l'extérieur du conteneur, vous devez utiliser des bind mounts. |
| `-c`   | Isole le conteneur actif de **la plupart des systèmes de fichiers** en n'utilisant qu'un répertoire `/dev` minimal, un répertoire `/tmp` vide et un répertoire `/home` vide. Pour accéder aux systèmes de fichiers à l'extérieur du conteneur, vous devez utiliser des bind mounts. |
| `-e`   | Supprime certaines variables de l'environnement de l'interpréteur avant le lancement des commandes et configure les paramètres pour une meilleure compatibilité OCI/Docker. Cette option ajoute implicitement `--containall`, `--no-init`, `--no-umask` et `--writable-tmpfs`. |

Une autre importante option est `-W` ou `--workdir`. Sur nos grappes et avec la plupart des systèmes Linux, les systèmes de fichiers semblables à `/tmp` utilisent la mémoire RAM et non l'espace sur disque. Les tâches exécutées sur nos grappes disposent habituellement de peu de mémoire RAM et elles sont annulées si elles consomment plus de mémoire que ce qui a été alloué. Pour contourner ce problème, Apptainer doit utiliser un disque physique pour son répertoire de travail (`workdir`). Pour ce faire, on utilise l'option `-W` suivie du chemin vers un disque où Apptainer peut lire et écrire des fichiers temporaires. Dans l'exemple suivant, la commande myprogram dans l'image du conteneur `myimage.sif` spécifie le répertoire de travail `/path/to/a/workdir`.
apptainer run -C -B /project -W /path/to/a/workdir myimage.sif myprogram

```bash
apptainer run -C -B /project -W /path/to/a/workdir myimage.sif myprogram
```

où
*   l'option `workdir` peut être supprimée si aucun conteneur actif ne l'utilise.
*   quand Apptainer est utilisé dans une tâche lancée avec `salloc`, `sbatch`, ou JupyterHub sur nos grappes, le répertoire de travail doit être `${SLURM_TMPDIR}`, par exemple `-W ${SLURM_TMPDIR}`.
    *   **Note :** Aucun programme intensif (incluant Apptainer) ne doit être exécuté sur les nœuds de connexion. Utilisez plutôt `salloc` pour démarrer une tâche interactive.
*   les bind mounts ne fonctionnent pas de la même manière sur toutes nos grappes ; consultez Bind mounts et overlays persistants ci-dessous pour savoir comment accéder à `/home`, `/project`, et `/scratch`.

## Utiliser des GPU

Tenez compte des points suivants quand votre logiciel dans un conteneur requiert l'utilisation de GPU :
*   Assurez-vous de passer `--nv` (pour le matériel NVIDIA) et `--rocm` (pour le matériel AMD) aux commandes Apptainer.
    *   Ces options font en sorte que les entrées appropriées dans `/dev` soient incluses dans le bind mount à l'intérieur du conteneur.
    *   Ces options localisent les bibliothèques pour les GPU et les attachent à l'hôte, en plus de configurer la variable d'environnement `LD_LIBRARY_PATH` pour que les bibliothèques fonctionnent dans le conteneur.
*   Assurez-vous que l'application qui utilise le GPU dans le conteneur a été correctement compilée pour pouvoir utiliser le GPU et ses bibliothèques.
*   Pour utiliser OpenCL dans le conteneur, utilisez les options précédentes et ajoutez le bind mount `-B /etc/OpenCL`.

Voyez l'exemple sous Travailler avec des GPU ci-dessous.

## Aide avec `apptainer run-help`

Les conteneurs Apptainer construits à partir de [fichiers de définition](http://apptainer.org/docs/user/main/definition_files.html) ont souvent une fonctionnalité `%help` appelée comme suit
```bash
apptainer run-help your-container-name.sif
```

où
*   `your-container-name.sif` est le nom du conteneur.

Si votre conteneur a aussi des applications, lancez
```bash
apptainer run-help --app appname your-container-name.sif
```

où
*   `appname` est le nom de l'application
*   `your-container-name.sif` est le nom du conteneur

Pour obtenir la liste des applications qui se trouvent dans le conteneur, lancez
```bash
apptainer inspect --list-apps your-container-name.sif
```

où
*   `your-container-name.sif` est le nom du conteneur.

## Lancer un logiciel avec `apptainer run` ou `apptainer exec`

La commande `apptainer run` lance le conteneur, exécute le script `%runscript` défini pour ce conteneur (s'il y en a un), puis lance la commande spécifiée.
Pour sa part, la commande `apptainer exec`, ne va pas exécuter le script, même s'il est défini dans le conteneur.

Nous recommandons de toujours utiliser `apptainer run`.

Supposons maintenant que vous voulez compiler avec `g++` le programme C++ `myprog.cpp` qui se trouve dans un conteneur, pour ensuite lancer le programme. Vous pouvez utiliser
```bash
apptainer run your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
apptainer run your-container-name.sif ./a.out
```

où
*   `your-container-name.sif` est le nom du fichier .SIF
*   `g++ -O2 -march=broadwell ./myprog.cpp` est la commande à exécuter dans le conteneur.

Sur nos grappes, vous devrez ajouter des options après `run`, mais avant `your-container-name.sif`, dont `-C`, `-c`, `-e` et `-W` en plus de certaines options bind mount pour que l'espace disque soit disponible pour les programmes dans le conteneur, par exemple

```bash
apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch your-container-name.sif g++ -O2 -march=broadwell ./myprog.cpp
apptainer run -C -W $SLURM_TMPDIR -B /project -B /scratch ./a.out
```

Pour plus d'information, consultez

*   Options de ligne de commande à retenir
*   Utiliser des GPU
*   Bind mounts et overlays persistants

Consultez aussi la [documentation officielle pour Apptainer](http://apptainer.org/docs/user/main/index.html).

## Interactivité avec `apptainer shell`

Les commandes `apptainer run`, `apptainer exec` et `apptainer instance` exécutent immédiatement les programmes, ce qui est parfait dans les scripts de tâches pour BASH et Slurm. Il peut parfois être nécessaire de travailler interactivement dans un conteneur ; pour ce faire, utilisez la commande `apptainer shell`.

Par exemple
```bash
apptainer shell your-container-name.sif
```

où
*   `your-container-name.sif` est le nom de votre fichier SIF

Quand le conteneur est prêt, l'invite `Apptainer>` s'affichera (ou `Singularity>` dans le cas des versions antérieures). Entrez alors les commandes pour l'interpréteur, puis entrez `exit` et appuyez sur la touche Enter/Return pour sortir du conteneur.

Sur nos grappes, vous devrez ajouter des options après `run`, mais avant `your-container-name.sif`, dont `-C`, `-c`, `-e` et `-W` en plus de certaines options bind mount pour que l'espace disque soit disponible pour les programmes dans le conteneur, par exemple

```bash
apptainer shell -C -W $SLURM_TMPDIR -B /home:/cluster_home -B /project -B /scratch your-container-name.sif
```

Pour plus d'information, consultez

*   Options de ligne de commande à retenir
*   Utiliser des GPU
*   Bind mounts et overlays persistants

Consultez aussi la [documentation officielle d'Apptainer](http://apptainer.org/docs/user/main/index.html).

!!! important "Important"
    Si vous utilisez une image d'un overlay persistant (dans un fichier SIF ou un fichier distinct) et que vous voulez que cette image reflète les modifications, il faut, en plus des options nommées ci-dessus, passer au conteneur l'option `-w` ou `--writable`, autrement les modifications faites dans la session `apptainer shell` ne seront pas sauvegardées.

## Utiliser des démons avec `apptainer instance`

Apptainer est conçu pour exécuter correctement des démons pour des tâches de calcul sur des grappes, en partie à l'aide de la commande `apptainer instance`. Voir les détails dans [Running Services](http://apptainer.org/docs/user/main/running_services.html) de la documentation officielle.

!!! note "Remarque 1"
    N'exécutez pas manuellement un démon sans utiliser `apptainer instance` et les autres commandes reliées. Apptainer fonctionne bien avec d'autres outils comme l'ordonnanceur Slurm employé sur nos grappes. Quand une tâche plante, est annulée ou se termine de toute autre façon, les démons lancés avec `apptainer instance` ne seront pas bloqués et ne laisseront pas de processus défunts. Aussi, la commande `apptainer instance` vous permet de contrôler les démons et les programmes qui sont exécutés dans un même conteneur.

!!! note "Remarque 2"
    Les démons ne sont exécutés que lorsque la tâche est en marche. Si l'ordonnanceur annule la tâche, tous les démons qui lui sont rattachés seront aussi annulés. Si vous avez besoin de démons qui restent actifs au-delà du temps d'exécution, vous pouvez à la place les exécuter dans une machine virtuelle, dans un nuage ; contactez alors le soutien technique.

# Bind mounts et overlays persistants

Apptainer offre les fonctionnalités suivantes :
*   **bind mounts**, pour avoir accès à l'espace disque à l'extérieur du conteneur ;
*   **persistent overlays**, pour superposer un système de fichiers en lecture/écriture à un conteneur immuable (lecture seulement).

## Bind mounts

L'utilisation des options `-C` ou `-c` avec un conteneur empêche l'accès à votre espace disque. Pour y pallier, il faut explicitement demander le bind mount de cet espace. Supposons que l'option `-C` est utilisée dans une tâche

```bash
apptainer run -C -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

où `./my_data_file.txt` est un fichier dans le répertoire courant de l'hôte, c'est-à-dire que le fichier n'est pas situé dans le conteneur. L'option `-C` fait en sorte que le programme `wc` dans le conteneur n'aura pas accès au fichier et une erreur d'accès surviendra. Pour éviter ceci, il faut faire un bind mount du répertoire courant

```bash
apptainer run -C -B . -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

où `-B .` fait le bind mount du répertoire courant `.`.

Même s'il est possible de créer plusieurs bind mount, il est souvent plus simple de faire le bind mount du répertoire de niveau supérieur sous lequel les répertoires sont situés. Par exemple, sur nos grappes, vous pouvez utiliser

```bash
apptainer run -C -B /project -B /scratch -W $SLURM_TMPDIR a-container.sif wc -l ./my_data_file.txt
```

où
*   `-B /project` fait le bind mount du système de fichiers /project
*   `-B /scratch` fait le bind mount du système de fichiers /scratch

Ceci est particulièrement utile
*   pour avoir accès aux fichiers des autres membres de votre équipe,
*   pour avoir accès aux fichiers et répertoires dont certains sont des `symlinks` vers différents endroits et qui pourraient être inaccessibles si le bind mount n'est pas fait pour le système de fichiers au complet.

Si les bind mount ne fonctionnent pas sur la grappe que vous utilisez, lancez le script suivant pour obtenir les options qui doivent être passées à Apptainer.

```bash
/home/preney/public/apptainer-scripts/get-apptainer-options.sh
```

Le bind mount ne doit pas nécessairement être au même endroit dans le conteneur. Vous pouvez faire le bind mount d'un fichier ou d'un répertoire ailleurs, par exemple

```bash
apptainer run -C -B ./my_data_file.txt:/special/input.dat -W $SLURM_TMPDIR a-container.sif wc -l /special/input.dat
```

où le bind mount `-B ./my_data_file.txt:/special/input.dat` associe le fichier `./my_data_file.txt` au fichier `/special/input.dat` dans le conteneur, pour être traité avec la commande `wc`. Ceci est utile quand des programmes ou des scripts dans un conteneur contiennent des chemins figés dans le code (*hard coded*) vers des fichiers ou des répertoires qui sont situés ailleurs.

Si vous avez besoin de faire le bind mount du système de fichiers /home dans votre conteneur, utilisez un autre répertoire de destination comme

*   `-B /home:/cluster_home`

Ceci fait en sorte que les fichiers de configuration et les programmes qui sont dans votre répertoire /home n'interféreront pas avec les logiciels dans votre conteneur. À l'inverse, si vous utilisez `-B /home`, les programmes dans `$HOME/bin` et les paquets Python dans `$HOME/.local/lib/python3.x` pourraient être utilisés plutôt que les fichiers correspondants du conteneur.

!!! warning "Évitez de faire le bind mount de CVMFS dans vos conteneurs"
    Les programmes fournis par CVMFS peuvent être incompatibles avec vos conteneurs. L'objectif d'un conteneur est de fournir un environnement complet qui ne dépend pas de logiciels externes. Les programmes exécutés dans un conteneur devraient s'y trouver en entier et ceux qui ne sont pas nécessaires ne devraient pas y être ajoutés.

## Overlays persistants

Voir les détails dans [Persistent Overlays](https://apptainer.org/docs/user/main/persistent_overlays.html) de la documentation officielle.

# Construire une image Apptainer

!!! warning "Attention"
    Lisez d'abord les recommandations ci-dessus dans Construire des images ou des overlays ci-dessus.

Une image Apptainer peut être

*   un fichier `SIF` ou
*   un répertoire servant de bac à sable (*sandbox*).

Un fichier SIF peut contenir un ou plusieurs systèmes de fichiers `squashfs` compressés et en lecture seule. Il est aussi possible qu'un fichier `SIF` contienne des fichiers en lecture-écriture et/ou des images overlay, mais nous n'abordons pas ces cas ici ; consultez plutôt [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs). À moins d'employer des méthodes plus complexes pour créer une image, la commande Apptainer `build` produit un fichier SIF composé d'un système de fichiers `squashfs` en lecture seule. Ceci est la meilleure option, car l'image en lecture seule restera telle quelle et elle sera plus compacte ; il faut se rappeler que les opérations de lecture de cette image se font à très grande vitesse.

**Un répertoire bac à sable** est un répertoire ordinaire qui est vide au début et auquel Apptainer ajoute les fichiers et les répertoires au fur et à mesure que l'image est construite. L'accès au répertoire et sa mise à jour doivent se faire uniquement via Apptainer. Un bac à sable est utile quand il faut accéder à l'image en lecture-écriture pour la modifier. Par contre, si les modifications sont peu fréquentes, il est préférable d'utiliser un fichier `SIF`. Il est possible de construire une image, faire des modifications puis construire un nouveau fichier `SIF` pour l'image modifiée, par exemple

```bash
$ cd $HOME
$ mkdir mynewimage.dir
$ apptainer build mynewimage.dir myimage.sif
$ apptainer shell --writable mynewimage.dir
Apptainer> # Run commands to update mynewimage.dir here.
Apptainer> exit
$ apptainer build newimage.sif mynewimage.dir
$ rm -rf mynewimage.dir
```

L'utilisation d'un fichier `SIF` est recommandée car la performance à partir de l'image du conteneur est plus rapide que lorsque chaque fichier est stocké séparément dans les systèmes de fichiers de nos grappes, qui sont optimisés pour traiter des fichiers de grande taille et pour les opérations parallèles de lecture et d'écriture. Aussi, contrairement à une image SIF, un bac à sable aura un impact important sur le nombre de fichiers que vous stockez, alors que ce nombre est limité par un quota. (Certaines images peuvent contenir des milliers de fichiers et de répertoires.)

Les permissions *root* sont requises pour l'utilisation des gestionnaires de paquets des distributions Linux ; un simple utilisateur ne peut donc pas construire des images sur nos grappes de calcul avec Apptainer 1.0.x et les versions Singularity précédentes. Au besoin, écrivez au soutien technique pour de l'assistance dans la création de votre image ou utilisez un ordinateur où Apptainer est installé et où vous avez les permissions *root*.

L'option `--fakeroot` d'Apptainer est utilisée pour créer et manipuler des images. Avec les versions antérieures à 1.1, il faut contacter le soutien technique et demander qu'un administrateur accorde la permission d'utiliser `--fakeroot` sur la grappe utilisée, ce qui n'est pas toujours possible. Avec Apptainer version 1.1, `--fakeroot` peut être utilisée sans permission supplémentaire.

Certains conteneurs ne peuvent être créés si vous n'avez pas les permissions *root*. De tels conteneurs ne peuvent pas être construits sur nos grappes.

Si tout ce dont vous avez besoin est une image Docker telle quelle, vous pourrez souvent la construire et l'exécuter facilement sans les permissions *root* et sans l'utilisation de `--fakeroot`. Si par la suite vous devez modifier l'image, vous devrez peut-être avoir les permissions *root*, par exemple pour utiliser un gestionnaire de paquets. Pour cette raison, les exemples suivants supposent l'utilisation d'une image Docker telle quelle.

## Construire une image SIF

!!! warning "Attention"
    Veuillez tenir compte des recommandations faites dans Construire des images ou des overlays ci-dessus.

Pour construire l'image d'un fichier SIF avec la plus récente image busybox de Docker, lancez
```bash
$ apptainer build bb.sif docker://busybox
```

Pour des fonctions plus avancées, voir [la documentation officielle d'Apptainer](https://apptainer.org/docs/admin/main/installation.html#lustre-gpfs).

## Construire un bac à sable

!!! warning "Attention"
    Veuillez tenir compte des recommandations faites dans Construire des images ou des overlays ci-dessus.

Pour construire un bac à sable plutôt qu'un fichier SIF, remplacez le nom du fichier SIF par `--sandbox DIR_NAME` ou `-s DIR_NAME` où `DIR_NAME` est le nom du répertoire à créer pour le bac à sable. Par exemple, pour créer un fichier SIF avec `apptainer build`, la commande est
```bash
$ apptainer build bb.sif docker://busybox
```
Remplacez `bb.sif` par un nom de répertoire, par exemple `bb.dir`, avec l'option `--sandbox`.
```bash
$ apptainer build --sandbox bb.dir docker://busybox
```

Rappelons les différences entre un fichier SIF et un bac à sable :

*   l'image du conteneur est contenue dans un seul fichier SIF compressé, en lecture seule,
*   les fichiers individuels formant l'image du conteneur sont placés dans un répertoire servant de bac à sable. Ces fichiers ne sont pas compressés, peuvent être nombreux (plusieurs milliers) et sont accessibles en lecture-écriture.

L'utilisation d'un bac à sable entame significativement vos quotas d'espace disque et de nombre de fichiers. Si vous n'avez pas besoin d'un accès en lecture et en écriture fréquent à l'image du conteneur, il est recommandé d'utiliser un fichier SIF. Ce dernier offre aussi un accès plus rapide.

# Cas d'usage

## Travailler avec Conda

!!! attention "Contenu manquant"
    Le contenu de la section "Travailler avec Conda dans Apptainer" est transclus d'une autre page MediaWiki (Using Conda in Apptainer/fr). Ce contenu devrait être inséré ici.

## Travailler avec des GPU

Pour utiliser des GPU dans Apptainer, assurez-vous que le logiciel pour le ou les types de GPU utilisés dans le conteneur sont installés dans le conteneur, autrement il est peu probable que le logiciel de votre conteneur puisse utiliser des GPU.

Pour utiliser les GPU NVIDIA, assurez-vous que
*   l'option en ligne de commande `--nv` se trouve après la commande `apptainer exec` ou `apptainer run` (avant le fichier .sif) ;
*   les modules appropriés pour les GPU sont chargés, par exemple `module load cuda/13.3`.

Pour utiliser les GPU AMD, assurez-vous que
*   l'option en ligne de commande `--rocm` se trouve après la commande `apptainer exec` ou `apptainer run` (avant le fichier .sif) ;
*   les modules appropriés pour les GPU sont chargés.

## Travailler avec MPI

La façon la plus simple d'exécuter une application MPI dans Apptainer est de la limiter à un seul nœud. Votre script de tâche ressemblera alors à celui d'une tâche multifils (*multithread*) s'exécutant sur un seul nœud, par exemple

```bash
#!/bin/bash
#SBATCH --mem-per-cpu=1024M
#SBATCH --time=0-00:05
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
apptainer exec -c mpirun ./your-mpi-program args
```

Remarquez que `mpirun` s'exécute *dans* le conteneur.

Si vous devez exécuter une application MPI sur plusieurs nœuds et que vous pouvez le faire sans Apptainer, nous recommandons de ne pas utiliser Apptainer. Exécuter une application MPI dans un conteneur sur plusieurs nœuds génère souvent des erreurs.

Pour exécuter une application MPI avec Apptainer sur plusieurs nœuds, la [documentation Apptainer](http://apptainer.org/docs/user/main/mpi.html) décrit deux méthodes :
1.  le [modèle hybride](https://apptainer.org/docs/user/latest/mpi.html#hybrid-model),
2.  le [modèle de liaison](https://apptainer.org/docs/user/latest/mpi.html#bind-model).
Nous recommandons le modèle hybride.

Points importants
*   La version de MPI installée dans le conteneur **doit être compatible** avec le module chargé avec `module load` pour pouvoir exécuter des tâches sur plusieurs nœuds ; ceci inclut le type précis de réseautique (par exemple InfiniBand).
*   La version de MPI sur l'hôte doit être chargée avec `module load` **avant** de lancer la commande `apptainer` qui exécute la tâche MPI.

En supposant que votre tâche MPI utilise un fil par rang MPI (c'est-à-dire que ce n'est pas une tâche hybride à mémoire partagée), vous pouvez alors spécifier le nombre de rangs comme le étant le nombre de tâches dans votre script de tâche. Par exemple, s'il y a quatre rangs,

```bash
#!/bin/bash
#SBATCH --mem-per-cpu=3G
#SBATCH --time=0-00:05
#SBATCH --ntasks=4
module load openmpi apptainer
# Ce « for loop » assure que toutes les variables spéciales OMPI (OpenMPI) définies dans l'environnement de l'hôte
# sont correctement exportées pour être utilisées dans le conteneur :
for v in "${!OMPI_@}" ; do
    export APPTAINERENV_${v}=${!v}
done
mpirun -np ${SLURM_NTASKS} -- apptainer exec -e YOUR_CONTAINER.sif ./your-mpi-program args
```

Cet exemple sera différent selon les variables OpenMPI qui cont configurées. Celles-ci peuvent être identifiées par le préfixe `OMPI`. Pour connaître les variables définies dans l'environnement de l'hôte pour un module donné, lancez la commande `module show` pour ce module, par exemple `module show openmpi`.

Nos tests indiquent que vous aurez probablement besoin d'au moins une des options d'environnement propre. Si un problème survient à l'utilisation de ces options, écrivez à [support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca).

Il faut savoir qu'un script de tâche qui fonctionne sur un seul nœud peut facilement échouer lorsqu'il est exécuté sur plusieurs nœuds ; effectuez donc des tests avec plus d'un nœud. Par exemple, si votre test comporte quatre tâches, vous pouvez forcer son exécution sur deux nœuds ou plus en spécifiant
`#SBATCH --nodes 2-4` dans le script de la tâche.

## Créer un conteneur Apptainer à partir de Dockerfile

!!! tip "Remarque"
    Il faut d'abord installer Docker et Apptainer sur un ordinateur où vous disposez des permissions nécessaires. Les commandes présentées ici ne fonctionnent pas sur nos grappes.

Malheureusement, certains projets logiciels offrent un fichier d'instructions Dockerfile mais pas d'image de conteneur. Il faut alors créer une image à partir du fichier Dockerfile. Cependant, Docker n'est pas installé sur nos grappes. Ceci dit, si vous pouvez travailler avec un ordinateur où Docker et Apptainer sont installés et où vous avez les permissions suffisantes (accès *root* ou `sudo`, ou appartenance au groupe `docker` et permission `--fakeroot`), les commandes suivantes vous permettront d'utiliser Docker puis Apptainer pour construire une image Apptainer sur cet ordinateur.

Remarque : Docker pourrait planter si vous ne faites pas partie du groupe `docker`. Il pourrait aussi s'avérer impossible de créer certains conteneurs sans les permissions *root*, `sudo` ou `--fakeroot`. Vérifiez que vous possédez les permissions nécessaires.

Si vous n'avez qu'un Dockerfile et que vous voulez créer une image Apptainer, lancez la commande suivante sur un ordinateur où Docker et Apptainer sont installés et où vous disposez des permissions nécessaires.

```bash
docker build -f Dockerfile -t your-tag-name
docker save your-tag-name -o your-tarball-name.tar
docker image rm your-tag-name
apptainer build --fakeroot your-sif-name.sif docker-archive://your-tarball-name.tar
rm your-tarball-name.tar
```

où

*   `your-tag-name` est le nom à donner au conteneur Docker,
*   `your-tarball-name.tar` est le nom à donner au fichier dans lequel Docker sauvegardera le contenu généré pour le conteneur,
*   `--fakeroot` peut être omis si c'est optionnel ; pour utiliser plutôt `sudo`, omettez `--fakeroot` et ajoutez `sudo` en préfixe à la ligne,
*   `your-sif-name.sif` est le nom du fichier SIF pour le conteneur Apptainer.

Le fichier SIF résultant est un conteneur Apptainer correspondant aux instructions Dockerfile. Copiez le fichier SIF sur la ou les grappes que vous voulez utiliser.

!!! tip "Remarque"
    Il est possible que le Dockerfile ajoute des couches additionnelles ; vous n'avez qu'à les supprimer avec

    ```bash
    docker images
    ```

    puis `docker image rm ID` (où ID est l'identifiant de l'image obtenue par la commande `docker images`). Ceci libère l'espace disque occupé par les couches additionnelles.

# Sujets divers

## Vider le répertoire cache

Pour trouver les fichiers du répertoire cache, lancez

```bash
apptainer cache list
```

Supprimez les fichiers avec

```bash
apptainer cache clean
```

## Modifier les répertoires par défaut

Avant de lancer Apptainer, configurez les variables d'environnement suivantes pour utiliser d'autres répertoires temporaires et cache que ceux désignés par défaut.

*   `APPTAINER_CACHEDIR` : répertoire où les fichiers sont téléchargés et mis en cache par Apptainer
*   `APPTAINER_TMPDIR` : répertoire où Apptainer enregistre les fichiers temporaires, incluant pour la création d'images `squashfs`

Par exemple, pour qu'Apptainer utilise votre espace /scratch pour la cache et les fichiers temporaires (ce qui est probablement le meilleur endroit), utilisez

```bash
$ mkdir -p /scratch/$USER/apptainer/{cache,tmp}
$ export APPTAINER_CACHEDIR="/scratch/$USER/apptainer/cache"
$ export APPTAINER_TMPDIR="/scratch/$USER/apptainer/tmp"
```

avant de lancer Apptainer.