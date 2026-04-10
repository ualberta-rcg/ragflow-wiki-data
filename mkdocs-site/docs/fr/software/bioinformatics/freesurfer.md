---
title: "FreeSurfer/fr"
slug: "freesurfer"
lang: "fr"

source_wiki_title: "FreeSurfer/fr"
source_hash: "13b7cd8596ac6b52af8c2ee5d31fdd01"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:25:07.042844+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Introduction

Le groupe d’outils [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki) sert à l'analyse et à la visualisation des données d’imageries cérébrales structurelles et fonctionnelles. FreeSurfer offre un flux d'imagerie structurelle entièrement automatique pour le traitement des données transversales et longitudinales.

## Notre module FreeSurfer 5.3

Le module à charger est `freesurfer/5.3.0`.

FreeSurfer construit le script `FreeSurferEnv.sh` qui est requis pour configurer correctement les variables d’environnement comme PATH et PERL5LIB.

```bash
module load freesurfer/5.3.0
source $EBROOTFREESURFER/FreeSurferEnv.sh
```

## FreeSurfer 6.0 et plus

En raison des conditions liées à la licence pour ces versions, FreeSurfer n’est plus disponible comme module central; vous devez l’installer avec EasyBuild dans vos répertoires `/home` ou `/project` comme décrit ci-dessous. Si vous avez besoin d’assistance, contactez le [soutien technique](technical-support.md).

### Téléchargement

Sélectionnez une version (6.0.0 ou plus) dans la [liste des versions](https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/) et téléchargez le fichier `[...].tar.gz` sur la grappe que vous voulez utiliser.

### Installation avec EasyBuild dans votre répertoire /home

La procédure suivante installe FreeSurfer 6.0.0 dans `/home/$USER/.local/easybuild/software/2020/Core/freesurfer/6.0.0/`. L’installation pourrait échouer par manque de mémoire, car les nœuds de connexion sont limités en termes de la quantité de mémoire allouée. Pour contourner ce problème, vous devrez probablement utiliser une [tâche interactive](running-jobs.md#taches-interactives) et demander environ 8Go.

1.  Localisez le répertoire qui contient le fichier archive `freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz`.
2.  Purgez les modules présents avec `module purge`.
3.  Installez avec [EasyBuild](easybuild.md) en utilisant `eb FreeSurfer-6.0.0-centos6_x86_64.eb --disable-enforce-checksums`.
4.  Enregistrez-vous pour obtenir la clé pour la licence [enregistrez-vous ici](https://surfer.nmr.mgh.harvard.edu/registration.html).
5.  Enregistrez la licence.

```bash
module load freesurfer/6.0.0
cd $FREESURFER_HOME
```

Avec `nano` ou un autre éditeur de texte, créez le fichier `/home/$USER/.license` sur le modèle de :

```
name.name@university.ca
12345
*A1BCdEfGHiJK
ABCd0EFgHijKl
```

Chargez le module avec `module load freesurfer/6.0.0`.

En date d’août 2020, la plus récente version disponible était 6.0.1. Il existe cependant [des versions plus récentes](https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer).

### Recettes EasyBuild

Les recettes sont disponibles sur [GitHub](https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer) ou par ligne de commande sur toutes nos grappes avec `eb -S FreeSurfer`. Si la version que vous cherchez n’est pas listée, vous pouvez installer l’application avec l’option `--try-software-version=<the new version>`. En cas de problème, contactez le [soutien technique](technical-support.md).

### Installation dans un répertoire partagé

Avec EasyBuild, FreeSurfer peut être installé dans un espace partagé (comme /project) pour que les membres d’un groupe puissent y avoir accès. Dans l’exemple suivant, FreeSurfer est installé dans le répertoire `/home/$USER/projects/def-someuser/$USER/software` et le module est installé dans le répertoire `/home/$USER/.local/easybuild/modules/2020/Core/freesurfer` de l’utilisateur.

```bash
newgrp def-someuser
installdir=/home/$USER/projects/def-someuser/$USER
moduledir=/home/$USER/.local/easybuild/modules/2020
pathtosrc=/home/$USER/software
eb FreeSurfer-6.0.1-centos6_x86_64.eb --installpath-modules=${moduledir} --prefix=${installdir} --sourcepath=${pathtosrc}
```

Si **checksums** pose problème, ajoutez l'option `--disable-enforce-checksums` à la commande `eb`.

Deux autres étapes sont requises pour que tous les membres du groupe puissent avoir accès à l’application :

*   Chaque membre du groupe doit avoir accès en lecture et en exécution au répertoire d’installation `/home/$USER/projects/def-someuser/$USER` (voir [Changer les permissions de fichiers existants](sharing-data.md#changer-les-permissions-de-fichiers-existants)).
*   Chaque membre doit enregistrer le fichier du module dans leur répertoire /home. Le fichier du module `6.0.1.lua` se trouve sous :

```
/home/$USER/.local/easybuild/modules/2020/Core/freesurfer/
```

Chaque membre du groupe doit créer le répertoire `/home/$USER/.local/easybuild/modules/2020/Core/freesurfer` et y enregistrer le fichier `6.0.1.lua`.

```bash
mkdir -p /home/$USER/.local/easybuild/modules/2020/Core/freesurfer
cp 6.0.1.lua /home/$USER/.local/easybuild/modules/2020/Core/freesurfer/
```

Ces directives installent le module (uniquement le fichier du module qui pointe sur le répertoire d’installation) dans leurs espaces /project.

Les utilisateurs doivent aussi charger le module à partir de leur compte avec :

```bash
module load freesurfer/6.0.1
```

### Analyse de l’hippocampe et du tronc cérébral

À partir du site web de FreeSurfer, téléchargez et installez la version 2012b du module MATLAB précompilé.

```bash
module load freesurfer/6.0.0
cd $FREESURFER_HOME
curl "http://surfer.nmr.mgh.harvard.edu/fswiki/MatlabRuntime?action=AttachFile&do=get&target=runtime2012bLinux.tar.gz" -o "matlab_runtime2012bLinux.tar.gz"
tar xvf matlab_runtime2012bLinux.tar.gz
```

### Exemple de script pour versions FreeSurfer >= 6.0.0

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

### Exemples de durée d'exécution

*   `recon-all -all` : `#SBATCH --time=08:00:00`
*   `recon-all -qcache` : `#SBATCH --time=00:20:00`
*   `recon-all -base -tp1 -tp2` : `#SBATCH --time=10:00:00`
*   `recon-all -long subjid -base base` : `#SBATCH --time=10:00:00`
*   `recon-all -hippocampal-subfields-T1` : `#SBATCH --time=00:40:00`
*   `recon-all -brainstem-structures` : `#SBATCH --time=00:30:00`