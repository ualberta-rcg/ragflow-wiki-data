---
title: "FreeSurfer/fr"
slug: "freesurfer"
lang: "fr"

source_wiki_title: "FreeSurfer/fr"
source_hash: "13b7cd8596ac6b52af8c2ee5d31fdd01"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:08:15.282895+00:00"

tags:
  []

keywords:
  - "EasyBuild"
  - "répertoire d'installation"
  - "FreeSurfer"
  - "fichier du module"
  - "script d'exécution"
  - "recon-all"
  - "imagerie cérébrale"
  - "module"
  - "espace partagé"
  - "installation"
  - "répertoire"

questions:
  - "À quoi sert le groupe d'outils FreeSurfer et quel type de données permet-il d'analyser ?"
  - "Pourquoi les versions 6.0 et ultérieures de FreeSurfer ne sont-elles plus disponibles comme modules centraux et comment doit-on les installer ?"
  - "Quelle est la procédure pour obtenir et configurer la clé de licence nécessaire à l'utilisation des versions récentes de FreeSurfer ?"
  - "Quelles sont les étapes requises pour partager l'accès à l'application FreeSurfer avec tous les membres d'un groupe d'utilisateurs ?"
  - "Comment télécharger et installer le module MATLAB précompilé nécessaire à l'analyse de l'hippocampe et du tronc cérébral ?"
  - "Comment configurer un script de soumission de tâche (Slurm) pour FreeSurfer et quelles sont les durées d'exécution estimées pour les différentes commandes recon-all ?"
  - "Quel est l'avantage principal d'utiliser EasyBuild pour installer FreeSurfer selon le texte ?"
  - "Dans quel répertoire spécifique le logiciel FreeSurfer est-il installé dans l'exemple fourni ?"
  - "Quel est le chemin d'accès exact du répertoire où le module de l'utilisateur est installé ?"
  - "Quelles sont les étapes requises pour partager l'accès à l'application FreeSurfer avec tous les membres d'un groupe d'utilisateurs ?"
  - "Comment télécharger et installer le module MATLAB précompilé nécessaire à l'analyse de l'hippocampe et du tronc cérébral ?"
  - "Comment configurer un script de soumission de tâche (Slurm) pour FreeSurfer et quelles sont les durées d'exécution estimées pour les différentes commandes recon-all ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction
Le groupe d’outils [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki) sert à l'analyse et à la visualisation des données d’imagerie cérébrale structurelle et fonctionnelle. FreeSurfer offre un flux d'imagerie structurelle entièrement automatique pour le traitement des données transversales et longitudinales.

# Notre module FreeSurfer 5.3
Le module à charger est `freesurfer/5.3.0`.

FreeSurfer construit le script `FreeSurferEnv.sh` qui est requis pour configurer correctement les variables d’environnement comme PATH et PERL5LIB.

```bash
module load freesurfer/5.3.0
source $EBROOTFREESURFER/FreeSurferEnv.sh
```

# FreeSurfer 6.0 et versions ultérieures
En raison des conditions liées à la licence pour ces versions, FreeSurfer n’est plus disponible comme module central; vous devez l’installer avec EasyBuild dans vos répertoires `/home` ou `/project` comme décrit ci-dessous. Si vous avez besoin d’assistance, contactez le [soutien technique](../../support/technical_support.md).

## Téléchargement
Sélectionnez une version (6.0.0 ou plus) dans la [liste des versions](https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/) et téléchargez le fichier `[...].tar.gz` sur la grappe que vous voulez utiliser.

## Installation avec EasyBuild dans votre répertoire /home

!!! note
    L’installation pourrait échouer par manque de mémoire, car les nœuds de connexion sont limités en termes de taille des paquets de mémoire. Pour contourner ce problème, vous devrez probablement utiliser une [tâche interactive](../../running-jobs/running_jobs.md) et demander environ 8 Go.

La procédure suivante installe FreeSurfer 6.0.0 dans `/home/$USER/.local/easybuild/software/2020/Core/freesurfer/6.0.0/`.

1.  Repérez le répertoire qui contient le fichier archive `freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz`.
2.  Désactivez les modules actifs avec `module purge`.
3.  Installez avec [EasyBuild](../../programming/easybuild.md) en utilisant `eb FreeSurfer-6.0.0-centos6_x86_64.eb --disable-enforce-checksums`.
4.  Inscrivez-vous pour obtenir la clé de licence [ici](https://surfer.nmr.mgh.harvard.edu/registration.html).
5.  Enregistrez la licence dans le fichier `/home/$USER/.license`.

    ```bash
    module load freesurfer/6.0.0
    cd $FREESURFER_HOME
    ```

    Avec `nano` ou un autre éditeur de texte, créez le fichier `/home/$USER/.license` sur le modèle suivant :

    ```
    name.name@university.ca
    12345
    *A1BCdEfGHiJK
    ABCd0EFgHijKl
    ```

    Chargez le module avec :

    ```bash
    module load freesurfer/6.0.0
    ```

En date d’août 2020, la version la plus récente disponible était la 6.0.1. Il existe cependant [des versions plus récentes](https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer).

## Recettes EasyBuild
Les recettes sont disponibles sur [GitHub](https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer) ou par ligne de commande sur toutes nos grappes avec `eb -S FreeSurfer`. Si la version que vous cherchez n’est pas listée, vous pouvez installer l’application avec l’option `--try-software-version=<la nouvelle version>`. En cas de problème, contactez le [soutien technique](../../support/technical_support.md).

## Installation dans un répertoire partagé
Avec EasyBuild, FreeSurfer peut être installé dans un espace partagé (comme un répertoire `/project`) afin que tous les membres d’un groupe puissent y avoir accès. Dans l’exemple suivant, FreeSurfer est installé dans le répertoire `/home/$USER/projects/def-someuser/$USER/software` et le module est installé dans le répertoire `/home/$USER/.local/easybuild/modules/2020/Core/freesurfer` de l’utilisateur.

```bash
newgrp def-someuser
installdir=/home/$USER/projects/def-someuser/$USER
moduledir=/home/$USER/.local/easybuild/modules/2020
pathtosrc=/home/$USER/software
eb FreeSurfer-6.0.1-centos6_x86_64.eb --installpath-modules=${moduledir} --prefix=${installdir} --sourcepath=${pathtosrc}
```

Si le contrôle d'intégrité (`checksums`) pose problème, ajoutez l'option `--disable-enforce-checksums` à la commande `eb`.

Deux étapes supplémentaires sont requises pour que tous les membres du groupe puissent avoir accès à l’application :

*   Chaque membre du groupe doit avoir accès en lecture et en exécution au répertoire d’installation `/home/$USER/projects/def-someuser/$USER` (voir [Changer les permissions de fichiers existants](../../storage-and-data/sharing_data.md#changer-les-permissions-de-fichiers-existants)).
*   Chaque membre doit copier le fichier du module dans son répertoire `/home`. Le fichier du module `6.0.1.lua` se trouve sous :
    ```bash
    /home/$USER/.local/easybuild/modules/2020/Core/freesurfer/
    ```

Chaque membre du groupe doit créer le répertoire `/home/$USER/.local/easybuild/modules/2020/Core/freesurfer` et y copier le fichier `6.0.1.lua`.

```bash
mkdir -p /home/$USER/.local/easybuild/modules/2020/Core/freesurfer
cp 6.0.1.lua /home/$USER/.local/easybuild/modules/2020/Core/freesurfer/
```

Ces directives installent le module (c'est-à-dire seulement le fichier du module qui pointe vers le répertoire d'installation) dans leurs répertoires `/project`.

Les utilisateurs doivent également charger le module à partir de leur compte avec :

```bash
module load freesurfer/6.0.1
```

## Analyse de l’hippocampe et du tronc cérébral
À partir du site web de FreeSurfer, téléchargez et installez la version 2012b du module MATLAB précompilé.

```bash
module load freesurfer/6.0.0
cd $FREESURFER_HOME
curl "http://surfer.nmr.mgh.harvard.edu/fswiki/MatlabRuntime?action=AttachFile&do=get&target=runtime2012bLinux.tar.gz" -o "matlab_runtime2012bLinux.tar.gz"
tar xvf matlab_runtime2012bLinux.tar.gz
```

## Exemple de script pour FreeSurfer versions 6.0.0 et ultérieures
```bash title="mysub.sh"
#!/bin/bash

#SBATCH --account=def-someuser
#SBATCH --mem=16G
#SBATCH --time=10:00:00

# Load the module:

module load freesurfer/6.0.0

# set the variables:

export SUBJECTS_DIR=<User_Defined_DIR>
source $EBROOTFREESURFER/FreeSurferEnv.sh

echo "Starting run at: `date`"

recon-all command

echo "Program finished with exit code $? at: `date`"
```

## Exemples de durées d'exécution

*   `recon-all -all` : `#SBATCH --time=08:00:00`
*   `recon-all -qcache` : `#SBATCH --time=00:20:00`
*   `recon-all -base -tp1 -tp2` : `#SBATCH --time=10:00:00`
*   `recon-all -long subjid -base base` : `#SBATCH --time=10:00:00`
*   `recon-all -hippocampal-subfields-T1` : `#SBATCH --time=00:40:00`
*   `recon-all -brainstem-structures` : `#SBATCH --time=00:30:00`