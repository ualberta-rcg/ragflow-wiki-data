---
title: "Accessing CVMFS/fr"
slug: "accessing_cvmfs"
lang: "fr"

source_wiki_title: "Accessing CVMFS/fr"
source_hash: "634044d02b6227e2ec2a620057883865"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T02:26:28.911876+00:00"

tags:
  - cvmfs

keywords:
  - "CC_CLUSTER"
  - "Ubuntu bash script"
  - "RSNT_INTERCONNECT"
  - "LD_LIBRARY_PATH"
  - "RPM package query"
  - "serveurs proxies HTTP"
  - "libnvidia-cfg1"
  - "dbus"
  - "5 à 10 Go"
  - "RSNT_CUDA_DRIVER_VERSION"
  - "RSNT_ARCH"
  - "dépôts de logiciels"
  - "service d'annonces"
  - "pilotes NVidia"
  - "libnvidia"
  - "exigences de l'environnement logiciel"
  - "hiérarchie centrale"
  - "configurer un client"
  - "RSNT_LOCAL_MODULEPATHS"
  - "CVMFS"
  - "stockage local"
  - "installation et configuration"
  - "mise en place du logiciel"
  - "paramètres du client"
  - "exigences techniques"
  - "modules"
  - "OpenMPI"
  - "cache externe"
  - "FORCE_CC_CVMFS"
  - "cache locale"
  - "logiciels sous licence"
  - "dépôt soft.computecanada.ca"
  - "LMOD_SYSTEM_DEFAULT_MODULES"
  - "grappe de calcul"
  - "cache"
  - "EasyBuild"
  - "symbolic link creation"
  - "pilotes NVIDIA"
  - "bibliothèques introuvables"
  - "MODULERCFILE"
  - "versions des modules CUDA"
  - "accès HTTP"
  - "options du protocole de transport"
  - "NVIDIA driver version"
  - "Cache Settings"
  - "apt --no-install-recommends"
  - "/opt/software/easybuild"
  - "CVMFS_REPOSITORIES"

questions:
  - "Comment installer et configurer le client CVMFS sur votre propre ordinateur ou votre grappe ?"
  - "Quelles sont les exigences techniques (système d’exploitation, FUSE, espace de cache, accès réseau) pour utiliser CVMFS sur un système personnel ?"
  - "Pourquoi et comment s’abonner au service d’annonces cvmfs‑announce@gw.alliancecan.ca ?"
  - "Quelles sont les exigences matérielles et logicielles minimales pour déployer des clients CVMFS sur les différents systèmes d’exploitation (Linux, Windows, macOS) ?"
  - "Pourquoi recommande‑t‑on d’utiliser au moins deux serveurs proxy HTTP avec cache externe et comment cela améliore‑t‑il la résilience du déploiement ?"
  - "Quelles sont les étapes clés à suivre avant et pendant l’installation de CVMFS, notamment la localisation du cache local et la synchronisation du compte de service « cvmfs » ?"
  - "Quelle taille de cache locale est recommandée pour une utilisation restreinte sur un ordinateur personnel ?"
  - "Où peut‑on consulter la documentation détaillée sur les paramètres de cache de CVMFS ?"
  - "Quels types d’accès HTTP sont évoqués pour se connecter à Internet ou à des serveurs proxy locaux ?"
  - "Quels documents en ligne sont indiqués pour configurer le logiciel et les paramètres du client CVMFS ?"
  - "Quel dépôt est fourni avec la configuration et comment l’ajouter à la variable CVMFS_REPOSITORIES ?"
  - "À quoi sert le dépôt `soft.computecanada.ca` une fois inclus dans la configuration du client ?"
  - "Comment vérifier que les dépôts CVMFS sont actifs et correctement configurés avant de les monter ?"
  - "Quels sont les moyens d’activer ou de forcer l’activation de l’environnement logiciel CVMFS dans une session, notamment pour les utilisateurs dont l’identifiant est inférieur à 1000 ?"
  - "Comment personnaliser l’environnement en définissant les variables d’environnement CC_CLUSTER, RSNT_ARCH, RSNT_INTERCONNECT et RSNT_CUDA_DRIVER_VERSION ?"
  - "Que se passe‑t‑il si aucune bibliothèque n’est présente dans `/usr/lib64/nvidia` concernant la compatibilité avec CUDA 10.2 ?"
  - "Comment configurer correctement la variable d’environnement `RSNT_LOCAL_MODULEPATHS` pour intégrer un arbre de modules local installé via EasyBuild, et quel effet ont les options `--priority 1` et `--priority -1` sur la priorité des arbres de modules ?"
  - "Quels répertoires sont automatiquement ajoutés au `MODULEPATH` ou au `PATH` par défaut, et comment les variables `LMOD_SYSTEM_DEFAULT_MODULES` et `MODULERCFILE` influencent le chargement et la version des modules ?"
  - "Quelle fonction remplit la variable qui déclenche des options différentes du protocole de transport pour OpenMPI ?"
  - "À quoi sert la variable <code>RSNT_CUDA_DRIVER_VERSION</code> et comment détermine‑t‑elle les versions des modules CUDA à afficher ou masquer ?"
  - "Que se passe‑t‑il lorsque la variable <code>RSNT_CUDA_DRIVER_VERSION</code> n’est pas définie ?"
  - "Quels sont les critères pour que les modules installés soient reconnus par la hiérarchie centrale du système de calcul ?"
  - "Où peut‑on trouver des informations détaillées et l’implémentation concernant ces modules ?"
  - "Quelle procédure faut‑il suivre pour installer des modules additionnels, notamment le choix du répertoire d’installation et la configuration de la variable d’environnement RSNT_LOCAL_MODULEPATHS ?"
  - "Pourquoi recommande‑t‑on de définir la variable d’environnement RSNT_LOCAL_MODULEPATHS dans le profil commun de la grappe avant d’installer des paquets avec EasyBuild ?"
  - "Quelles précautions un administrateur doit‑il prendre lors d’opérations système ou de mise à jour de CVMFS pour éviter que sa session ne dépende de l’environnement logiciel ?"
  - "Comment résoudre les incompatibilités possibles entre les bibliothèques CUDA installées dans /usr/lib64 et l’environnement logiciel, notamment en créant des liens symboliques dans /usr/lib64/nvidia ?"
  - "What is the purpose of the `VER=\"570\"` variable and how is it used in the script?"
  - "Which NVIDIA driver packages are listed in the `nv_pkg` array, and what architecture are they targeting?"
  - "What does the `rpm -ql` loop with `ln -snf` accomplish for files located in `/usr/lib64`?"
  - "Pourquoi l’utilisation de <code>LD_LIBRARY_PATH</code> est‑elle déconseillée dans cet environnement ?"
  - "Comment le script crée‑t‑il les liens symboliques vers les bibliothèques NVIDIA dans <code>/usr/lib64/nvidia</code> ?"
  - "Dans quels cas doit‑on installer <code>dbus</code> localement sur le système hôte ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
Les dépôts de logiciels et de données que nous offrons sont accessibles via le [CVMFS (''CERN Virtual Machine File System'')](cvmfs.md). Puisque CVMFS est préconfiguré pour vous, vous pouvez utiliser ses dépôts directement. Pour plus d’information sur notre environnement logiciel, consultez les pages wiki [Logiciels disponibles](../../programming/available_software.md), [Utiliser des modules](../../programming/utiliser_des_modules.md), [Python](../python.md), [R](../r.md) et Installation de logiciels dans votre répertoire /home.

Nous décrivons ici comment installer et configurer CVMFS sur *votre propre ordinateur ou grappe*; vous aurez ainsi accès aux mêmes dépôts et environnements logiciels que ceux de nos systèmes.

Nous utilisons comme exemple [l'environnement logiciel présenté à la conférence PEARC 2019](https://ssl.linklings.net/conferences/pearc/pearc19_program/views/includes/files/pap139s3-file1.pdf), *Practices and Experience in Advanced Research Computing*.

## Avant de commencer

!!! note
    Si vous êtes membre de nos équipes techniques, lisez la [documentation interne](https://wiki.alliancecan.ca/wiki/CVMFS_client_setup).

!!! important "Important"
    **Veuillez vous abonner au [service d'annonces](#sabonnner-au-service-dannonces) et remplir ce [formulaire d'enregistrement](https://docs.google.com/forms/d/1eDJEeaMgooVoc4lTkxcZ9y65iR8hl4qeXMOEU9slEck/viewform) (en anglais). Si vous utilisez notre environnement logiciel dans votre recherche, veuillez reconnaître notre contribution selon [ces directives](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/reconnaissance-de-lalliance).**

    Nous vous remercions de mentionner aussi [notre présentation](https://ssl.linklings.net/conferences/pearc/pearc19_program/views/includes/files/pap139s3-file1.pdf).

## S'abonner au service d'annonces
Des modifications peuvent être apportées au CVMFS ou aux logiciels et autre contenu des dépôts que nous fournissons; ces modifications *touchent les utilisateurs ou nécessitent l’intervention de l’administrateur* pour assurer la continuité du service.

Abonnez-vous à la liste de diffusion cvmfs-announce@gw.alliancecan.ca afin de recevoir les annonces importantes occasionnelles. Vous pouvez vous abonner en écrivant à [cvmfs-announce+subscribe@gw.alliancecan.ca](mailto:cvmfs-announce+subscribe@gw.alliancecan.ca) et en répondant au courriel de confirmation qui vous sera envoyé.
Les membres de nos équipes techniques peuvent aussi [s'abonner ici](https://groups.google.com/u/0/a/gw.alliancecan.ca/g/cvmfs-announce/).

## Conditions d’utilisation et soutien technique
Le logiciel client CVMFS est fourni par le CERN. Nos dépôts CVMFS sont offerts **sans aucune forme de garantie**. Votre accès aux dépôts et à l’environnement logiciel peut être limité ou bloqué si vous contrevenez aux [conditions d’utilisation](https://ccdb.alliancecan.ca/agreements/user_aup_2021/user_display), ou à notre discrétion.

## Exigences techniques
### Pour un seul système
Pour installer CVMFS sur un ordinateur personnel, les exigences sont :
*   un système d’exploitation compatible (voir [Exigences de base](#exigences-de-base) ci-dessous);
*   le [logiciel libre FUSE](https://en.wikipedia.org/wiki/Filesystem_in_Userspace);
*   environ 50Go d’espace de stockage local pour la cache; une cache plus ou moins grande peut convenir, selon les circonstances. Pour une utilisation restreinte sur un ordinateur personnel, de 5 à 10Go peuvent suffire. Pour plus d'information, voyez [*Cache Settings*](https://cvmfs.readthedocs.io/en/stable/cpt-configure/#cache-settings).
*   l’accès HTTP vers l’internet,
    *   ou l’accès HTTP vers un ou plusieurs serveurs proxies locaux.

Si ces conditions ne sont pas respectées ou que vous avez d’autres restrictions, considérez cette [autre option](https://cvmfs.readthedocs.io/en/stable/cpt-hpc/).

### Pour plusieurs systèmes
Pour déployer plusieurs clients CVMFS, par exemple sur une grappe, dans un laboratoire, sur un campus ou autre, chacun des systèmes doit satisfaire les exigences particulières énoncées ci-dessus. Tenez compte en plus des points suivants :
*   Pour améliorer la performance, nous vous recommandons de déployer sur votre site des serveurs proxies HTTP avec cache externe (*forward caching*), particulièrement si vous avez plusieurs clients (voir [*Setting up a Local Squid Proxy*](https://cvmfs.readthedocs.io/en/stable/cpt-squid/)).
    *   Le fait de ne disposer que d’un seul serveur proxy est un point de défaillance unique. Règle générale, vous devriez disposer d’au moins deux serveurs proxies locaux et préférablement un ou plusieurs autres serveurs proxies supplémentaires à proximité pour prendre la relève en cas de problème.
*   Nous vous recommandons de synchroniser l’identité du compte de service `cvmfs` de tous les nœuds clients avec LDAP ou autrement.
    *   Ceci facilitera l’utilisation d’une [cache externe](https://cvmfs.readthedocs.io/en/stable/cpt-configure/#alien-cache) et devrait être fait **avant que CVMFS ne soit installé**. Même si l’utilisation d’une cache externe n’est pas prévue, il est plus facile de synchroniser les comptes dès le départ que d’essayer de les changer plus tard.

## Exigences de l’environnement logiciel
### Exigences de base
*   **Système d’exploitation :**
    *   **Linux :** avec noyau 2.6.32 ou plus pour les environnements 2016 et 2018; noyau 3.2 ou plus pour l'environnement 2020,
    *   **Windows :** avec la version 2 du sous-système Windows pour Linux (WSL) et une distribution Linux avec noyau 2.6.32 ou plus,
    *   **Mac OS :** par instance virtuelle seulement;
*   **CPU :** x86, pour jeux d’instructions SSE3, AVX, AVX2 ou AVX512.

### Pour une utilisation optimale
*   **Ordonnanceur :** Slurm ou Torque, pour une intégration étroite avec les applications OpenMPI;
*   **Interconnexion réseau :** Ethernet, InfiniBand ou OmniPath, pour les applications parallèles;
*   **GPU :** NVidia avec pilotes CUDA 7.5 ou plus, pour les applications CUDA (voir la mise en garde ci-dessous);
*   Un minimum de paquets Linux, pour éviter les risques de conflits.

## Installer CVMFS
Si vous voulez utiliser [Ansible](https://docs.ansible.com/ansible/latest/index.html), il existe un [rôle client CVMFS](https://github.com/cvmfs-contrib/ansible-cvmfs-client) pour la configuration de base d’un client CVMFS avec un système RPM. Des [scripts](https://github.com/ComputeCanada/CVMFS/tree/main/cvmfs-cloud-scripts) sont disponibles pour installer facilement CVMFS sur une instance infonuagique.
Autrement, suivez les directives ci-dessous.

## Préinstallation
Nous recommandons que la cache locale CVMFS (située par défaut dans `/var/lib/cvmfs` et configurable avec le paramètre `CVMFS_CACHE_BASE`) soit localisée dans un système de fichiers dédié afin que le stockage ne soit pas partagé avec celui d’autres applications. Vous devriez donc avoir ce système de fichiers **avant** d’installer CVMFS.

## Installation et configuration

Voir les directives pour l'installation dans [*Getting the Software*](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart/#getting-the-software).

Pour configurer un client, voir [*Setting up the Software*](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart/#setting-up-the-software) et [*Client parameters*](https://cvmfs.readthedocs.io/en/stable/apx-parameters/#client-parameters).

Le dépôt `soft.computecanada.ca` est fourni avec la configuration et vous pouvez ainsi y accéder; vous pouvez l'inclure dans votre configuration client `CVMFS_REPOSITORIES`.

## Test
Puisque les dépôts CVMFS utilisent habituellement la fonctionnalité automount, ils ne seront pas montés s'ils ne sont pas actifs.

*   Assurez-vous d'abord que les dépôts à tester se trouvent dans `CVMFS_REPOSITORIES`.
*   Vérifiez les dépôts.
    ```bash
    cvmfs_config probe
    ```
*   Validez la configuration et testez les connexions du proxy.
    ```bash
    cvmfs_config chksetup
    ```
*   Assurez-vous de régler les avertissements ou erreurs qui pourraient survenir.

En cas de problème, ce [guide de débogage](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart/#troubleshooting) pourrait vous être utile.

## Activer notre environnement dans votre session
Une fois que le dépôt CVMFS est monté, notre environnement est activé dans votre session en utilisant le script `/cvmfs/soft.computecanada.ca/config/profile/bash.sh`. Celui-ci chargera des modules par défaut. Si vous désirez avoir les modules par défaut d'une grappe de calcul en particulier, définissez la variable `CC_CLUSTER` en choisissant l'une des valeurs suivantes `fir`, `nibi` ou `rorqual`, avant d'utiliser le script. Par exemple
```bash
export CC_CLUSTER=rorqual
```
```bash
source /cvmfs/soft.computecanada.ca/config/profile/bash.sh
```

Cette commande **n’exécutera rien si votre identifiant d’utilisateur est sous 1000**. Il s’agit d’une mesure de sécurité parce que vous ne devriez pas vous attendre à ce que notre environnement logiciel vous procure des privilèges de fonctionnement. Si vous voulez quand même activer notre environnement, vous pouvez d’abord définir la variable `FORCE_CC_CVMFS=1` avec la commande
```bash
export FORCE_CC_CVMFS=1
```
ou, si vous voulez que notre environnement soit actif en permanence, vous pouvez créer le fichier `$HOME/.force_cc_cvmfs` dans votre répertoire `/home` avec
```bash
touch $HOME/.force_cc_cvmfs
```

Si vous voulez au contraire ne pas activer notre environnement, vous pouvez définir `SKIP_CC_CVMFS=1` ou créer le fichier `$HOME/.skip_cc_cvmfs` pour faire en sorte que notre environnement ne soit jamais activé dans cet environnement particulier.

## Personnaliser votre environnement
Par défaut, certaines fonctionnalités de votre système seront automatiquement détectées par l’activation de notre environnement et les modules requis seront chargés. Ce comportement par défaut peut être modifié par la définition préalable des variables d’environnement particulières décrites ci-dessous.

### Variables d’environnement
#### `CC_CLUSTER`
Cette variable identifie la grappe. Elle achemine des renseignements au journal du système et définit le comportement à adopter selon la licence du logiciel. Sa valeur par défaut est `computecanada`. Vous pourriez définir sa valeur pour que les journaux soient identifiés par le nom de votre système.

#### `RSNT_ARCH`
Cette variable identifie le jeu d’instructions CPU pour le système. Par défaut, elle est détectée automatiquement selon `/proc/cpuinfo`. Vous pouvez cependant utiliser un autre jeu d’instructions en définissant la variable avant d’activer l’environnement. Les jeux possibles sont
*   sse3
*   avx
*   avx2
*   avx512

#### `RSNT_INTERCONNECT`
Cette variable identifie le type d’interconnexion réseau du système. Elle est détectée automatiquement selon la présence de `/sys/module/opa_vnic` pour OmniPath ou de `/sys/module/ib_core` pour InfiniBand. La valeur de remplacement est `ethernet`. Les valeurs possibles sont
*   omnipath
*   infiniband
*   ethernet

La valeur de la variable déclenche des options différentes du protocole de transport pour OpenMPI.

#### `RSNT_CUDA_DRIVER_VERSION`

Cette variable est utilisée pour cacher ou montrer des versions de nos modules CUDA selon la version requise pour les pilotes NVidia, [comme documenté ici](https://docs.nvidia.com/deploy/cuda-compatibility/index.html). Si la variable n’est pas définie, les fichiers dans `/usr/lib64/nvidia` déterminent les versions à cacher ou à montrer.

Si aucune bibliothèque ne se trouve dans `/usr/lib64/nvidia`, nous supposons que les versions du pilote sont suffisantes pour CUDA 10.2. Ceci est pour assurer la compatibilité avec les versions antérieures puisque cette fonctionnalité a été rendue disponible à la sortie de CUDA 11.0.

Définir la variable d’environnement `RSNT_CUDA_DRIVER_VERSION=0.0` cache toutes les versions de CUDA.

#### `RSNT_LOCAL_MODULEPATHS`
!!! warning "ATTENTION"
    Cette variable d'environnement doit être utilisée uniquement avec des arbres de modules hiérarchiques qui sont installés via EasyBuild, pour que leur structure soit comme celle de nos modules.

    Pour ajouter un chemin local à un arbre plat, placez la commande *après* l'appel du script.
    ```bash
    module use --priority 1 /path/to/your/flat/module/tree
    ```
    Ici, `--priority 1` fera en sorte que votre arbre de modules aura la priorité sur notre arborescence.
    Pour que notre arborescence soit prioritaire, utilisez `--priority -1`
    ```bash
    module use --priority -1 /path/to/your/flat/module/tree
    ```

Cette variable identifie les endroits où se trouvent les arbres de modules locaux et les intègre à notre arborescence centrale. Définissez d'abord
```bash
export RSNT_LOCAL_MODULEPATHS=/opt/software/easybuild/modules
```
et installez ensuite votre recette [EasyBuild](../../programming/easybuild.md) avec
```bash
eb --installpath /opt/software/easybuild <your recipe>.eb
```

Notre nomenclature de modules sera employée pour installer localement votre recette qui sera utilisée dans la hiérarchie des modules. Par exemple, si la recette utilise la chaîne de compilation `iompi,2018.3`, le module sera disponible après que les modules `intel/2018.3` et `openmpi/3.1.2` auront été chargés.

#### `LMOD_SYSTEM_DEFAULT_MODULES`
Cette variable identifie les modules à charger par défaut. Si elle n’est pas définie, notre environnement charge par défaut le module `StdEnv` qui à son tour charge par défaut une version du compilateur Intel ainsi qu’une version OpenMPI.

#### `MODULERCFILE`
Cette variable est utilisée par Lmod pour définir la version par défaut des modules et alias. Vous pouvez définir votre propre fichier `modulerc` et l'ajouter à `MODULERCFILE`. Ceci aura préséance sur ce qui est défini dans notre environnement.

### Chemin des fichiers
Notre environnement logiciel est conçu pour dépendre le moins possible du système d’exploitation hôte; cependant, il doit reconnaître certains chemins afin de faciliter les interactions avec les outils qui y sont installés.

#### `/opt/software/modulefiles`
S’il existe, ce chemin est automatiquement ajouté au `MODULEPATH` par défaut. Ceci permet l’utilisation de notre environnement en conservant les modules installés localement.

#### `$HOME/modulefiles`
S’il existe, ce chemin est automatiquement ajouté au `MODULEPATH` par défaut. Ceci permet l’utilisation de notre environnement en permettant l’installation de modules dans les répertoires `/home`.

#### `/opt/software/slurm/bin`, `/opt/software/bin`, `/opt/slurm/bin`
Ces chemins sont automatiquement ajoutés au `PATH` par défaut. Il permet l'ajout de votre exécutable dans le chemin de recherche.

## Installation locale de logiciels
Depuis juin 2020, il est possible d'installer des modules additionnels sur votre grappe de calcul; ces modules seront par la suite reconnus par notre hiérarchie centrale. Pour plus d'information, voyez la [discussion et l'implémentation à ce sujet](https://github.com/ComputeCanada/software-stack/issues/11).

Pour installer des modules additionnels, identifiez d'abord un chemin où installer les logiciels, par exemple `/opt/software/easybuild`. Assurez-vous que ce dossier existe. Exportez ensuite la variable d'environnement `RSNT_LOCAL_MODULEPATHS` :
```bash
export RSNT_LOCAL_MODULEPATHS=/opt/software/easybuild/modules
```

Si vous voulez que vos utilisateurs puissent trouver cette branche, nous vous recommandons de définir cette variable d'environnement dans le profil commun de la grappe. Installez ensuite les paquets logiciels que vous voulez avec [EasyBuild](../../programming/easybuild.md) :
```bash
eb --installpath /opt/software/easybuild <some easyconfig recipe>
```

Les logiciels seront installés localement selon notre hiérarchie de nomenclature de modules. Ils seront automatiquement présentés aux utilisateurs quand ils chargent notre compilateur, MPI et CUDA.

## Mises en garde
## Utilisation de l’environnement logiciel par un administrateur
Si vous effectuez des opérations de système avec des privilèges ou des opérations en rapport avec CVMFS, [assurez-vous que votre session *ne dépend pas de l’environnement logiciel*](#activer-notre-environnement-dans-votre-session). Par exemple, si vous faites la mise à jour de CVMFS avec YUM pendant que votre session utilise un module Python chargé à partir de CVMFS, YUM pourrait être exécuté en utilisant ce même module et en perdre l’accès par la mise à jour qui serait alors bloquée. De même, si votre environnement dépend de CVMFS et que vous reconfigurez CVMFS de façon à ce que l'accès à CVMFS soit temporairement interrompu, votre session pourrait nuire aux opérations de CVMFS ou être suspendue. Tenant compte de ceci, la mise à jour ou la reconfiguration de CVMFS peut se faire sans interruption de service dans la plupart des cas, car l'opération réussirait en raison de l'absence d'une dépendance circulaire.

## Paquets logiciels non disponibles
Nous mettons plusieurs logiciels du commerce à votre disposition, sous condition de la licence de ces produits. Ces logiciels ne sont pas disponibles ailleurs qu’avec nos ressources et vous n’y aurez pas droit d’accès même si vous suivez les directives pour installer et configurer CVMFS. Prenons l’exemple des compilateurs d’Intel et du Portland Group : si les modules pour ces compilateurs sont disponibles, vous n’avez accès qu’aux parties redistribuables, habituellement les objets partagés. Vous pourrez exécuter des applications compilées, mais il ne vous sera pas possible de compiler de nouvelles applications.

## Localisation de CUDA
Dans le cas des paquets CUDA, notre environnement logiciel utilise des bibliothèques de pilotes installées dans `/usr/lib64/nvidia`. Cependant, avec certaines plateformes, les récents pilotes NVidia installent les bibliothèques `/usr/lib64` dans `LD_LIBRARY_PATH` sans emprunter de toutes les bibliothèques du système, ce qui pourrait créer des incompatibilités avec notre environnement logiciel; nous vous recommandons donc de créer des liens symboliques dans `/usr/lib64/nvidia` pour rediriger vers les bibliothèques NVidia qui sont installées. Le script suivant sert à installer les pilotes et créer les liens symboliques (remplacez le numéro de version par celui que vous désirez).

```bash title="script_for_redhat.sh"
NVIDIA_DRV_VER="410.48"
nv_pkg=( "nvidia-driver" "nvidia-driver-libs" "nvidia-driver-cuda" "nvidia-driver-cuda-libs" "nvidia-driver-NVML" "nvidia-driver-NvFBCOpenGL" "nvidia-modprobe" )
yum -y install ${nv_pkg[@]/%/-${NVIDIA_DRV_VER}}
for file in $(rpm -ql ${nv_pkg[@]}); do
  [ "${file%/*}" = '/usr/lib64' ] && [ ! -d "${file}" ] && \ 
  ln -snf "$file" "${file%/*}/nvidia/${file##*/}"
done
```

```bash title="script_for_ubuntu.sh"
#! /usr/bin/bash
# Use the 'major series' number for the package name
VER="570"
nv_pkg=( "libnvidia-cfg1-${VER}-server:amd64"
    		"libnvidia-compute-${VER}-server:amd64"
		"libnvidia-decode-${VER}-server:amd64"
		"libnvidia-encode-${VER}-server:amd64"
		"libnvidia-extra-${VER}-server:amd64"
		"libnvidia-fbc1-${VER}-server:amd64"
		"libnvidia-gl-${VER}-server:amd64"
		"xserver-xorg-video-nvidia-${VER}-server" )
# apt --no-install-recommends install ${nv_pkg[*]}
[ -d "/usr/lib64/nvidia/" ] || mkdir "/usr/lib64/nvidia/"
for file in $(dpkg --listfiles "${nv_pkg[@]}"); do
	[ "${file%/*}" = '/usr/lib/x86_64-linux-gnu' ] && \
	[ ! -d "${file}" ] && \
	ln -snf "$file" "/usr/lib64/nvidia/${file##*/}"
done
```

## `LD_LIBRARY_PATH`
[Il n'est pas recommandé d'utiliser `LD_LIBRARY_PATH`](https://gms.tf/ld_library_path-considered-harmful.html) ce qui pourrait nuire au fonctionnement de l'environnement.

## Bibliothèques introuvables
Puisque nous ne définissons pas `LD_LIBRARY_PATH` et que nos bibliothèques ne sont pas installées dans des localisations Linux par défaut, les paquets binaires comme Anaconda ont souvent de la difficulté à trouver les bibliothèques dont ils ont besoin. Consultez notre documentation sur l’installation de paquets binaires.

## dbus
Pour certaines applications, `dbus` doit être installé localement, sur le système d’exploitation hôte.