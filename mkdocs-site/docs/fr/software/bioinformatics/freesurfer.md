---
title: "FreeSurfer/fr"
tags:
  []

keywords:
  []
---

=Introduction=
Le groupe d’outils [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki) sert à l'analyse et à visualisation des données d’imageries cérébrales structurelles et fonctionnelles. FreeSurfer offre un flux d'imagerie structurelle entièrement automatique pour le traitement des données transversales et longitudinales.

=Notre module FreeSurfer 5.3 =
Le module à charger est <tt>freesurfer/5.3.0.</tt>. 

FreeSurfer construit le script <tt>FreeSurferEnv.sh</tt> qui est requis pour configurer correctement les variables d’environnement comme PATH et PERL5LIB.

```bash
source $EBROOTFREESURFER/FreeSurferEnv.sh
```

=FreeSurfer 6.0 et plus=
En raison des conditions liées à la licence pour ces versions, FreeSurfer n’est plus disponible comme module central; vous devez l’installer avec EasyBuild dans vos répertoires /home ou /project comme décrit ci-dessous. Si vous avez besoin d’assistance, contactez le [soutien technique](technical-support-fr.md). 

## Téléchargement
Sélectionnez une version (6.0.0 ou plus) dans la [liste des versions](https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/) et téléchargez le fichier `[...].tar.gz` sur la grappe que vous voulez utiliser.

## Installation avec EasyBuild dans votre répertoire /home
La procédure suivante installe FreeSurfer 6.0.0 dans `/home/$USER/.local/easybuild/software/2020/Core/freesurfer/6.0.0/`. L’installation pourrait échouer par manque de mémoire car les nœuds de connexion sont limités en termes de la taille des paquets de mémoire. Pour contourner ce problème, vous devrez probablement utiliser une [tâche interactive](running_jobs-fr#tâches_interactives.md) et demander environ 8Go. 

# Localisez le répertoire qui contient le fichier archive `freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz`.
# Purgez les modules présents avec `module purge`.
# Installez avec [EasyBuild](easybuild-fr.md) en utilisant `eb FreeSurfer-6.0.0-centos6_x86_64.eb --disable-enforce-checksums`.
# Enregistrez-vous pour obtenir la clé pour la licence.[# Enregistrez la licence dans 

```bash
cd $FREESURFER_HOME
```

Avec nano ou un autre éditeur de texte, créez le fichier `/home/$USER/.license` sur le modèle de
<pre>
name.name@university.ca
12345
*A1BCdEfGHiJK
ABCd0EFgHijKl
</pre>
Chargez le module avec
`module load freesurfer/6.0.0`.

En date d’août 2020, la plus récente version disponible était 6.0.1. Il existe cependant [https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer des versions plus récentes](https://surfer.nmr.mgh.harvard.edu/registration.html]).

## Recettes EasyBuild
Les recettes sont disponibles sur [GitHub](https://github.com/ComputeCanada/easybuild-easyconfigs/tree/computecanada-master/easybuild/easyconfigs/f/FreeSurfer)  ou par ligne de commande sur toutes nos grappes avec <tt>eb -S FreeSurfer</tt>. Si la version que vous cherchez n’est pas listée, vous pouvez installer l’application avec l’option <tt> y--try-software-version=<the new version></tt>. En cas de problème, contactez le [soutien technique](technical-support-en.md).

## Installation dans un répertoire partagé
Avec EasyBuild, FreeSurfer peut être installé dans un espace partagé (comme /project) pour que les membres d’un groupe puissent y avoir accès. Dans l’exemple suivant, FreeSurfer est installé dans le répertoire <tt>/home/$USER/projects/def-someuser/$USER/software</tt> et le module est installé dans le répertoire <tt>/home/$USER/.local/easybuild/modules/2020/Core/freesurfer</tt> de l’utilisateur. 

<pre>
newgrp def-someuser
installdir=/home/$USER/projects/def-someuser/$USER
moduledir=/home/$USER/.local/easybuild/modules/2020
pathtosrc=/home/$USER/software
eb FreeSurfer-6.0.1-centos6_x86_64.eb --installpath-modules=${moduledir} --prefix=${installdir} --sourcepath=${pathtosrc}
</pre>
Si **checksums** pose problème, ajoutez l'option `--disable-enforce-checksums` à la commande `eb`.

Deux autres étapes sont requises pour que tous les membres du groupe puissent avoir accès à l’application&nbsp;:

* chaque membre du groupe doit avoir accès en lecture et en exécution au répertoire d’installation  `/home/$USER/projects/def-someuser/$USER` (voir [Changer les permissions de fichiers existants](sharing-data-fr#changer_les_permissions_de_fichiers_existants.md)).
* chaque membre doit enregistrer le fichier du module dans leur répertoire /home. Le fichier du module `6.0.1.lua` se trouve sous 
<pre>
/home/$USER/.local/easybuild/modules/2020/Core/freesurfer/</code>
</pre>

Chaque membre du groupe doit créer le répertoire `/home/$USER/.local/easybuild/modules/2020/Core/freesurfer` et y enregistrer le fichier `6.0.1.lua`.

```bash
cp 6.0.1.lua /home/$USER/.local/easybuild/modules/2020/Core/freesurfer/
```

Ces directives installent le module (uniquement le fichier du module qui pointe sur le répertoire d’installation) dans leurs espaces /project.

Les utilisateurs doivent aussi charger le module à partir de leur compte avec

```bash
module load freesurfer/6.0.1
```

## Analyse de l’hippocampe et du tronc cérébral
À partir du site web de FreeSurfer, téléchargez et installez la version 2012b du module MATLAB précompilé.
<pre>
module load freesurfer/6.0.0
cd $FREESURFER_HOME
curl "http://surfer.nmr.mgh.harvard.edu/fswiki/MatlabRuntime?action=AttachFile&do=get&target=runtime2012bLinux.tar.gz" -o "matlab_runtime2012bLinux.tar.gz"
tar xvf matlab_runtime2012bLinux.tar.gz 
</pre>
==Exemple de script pour versions FreeSurfer >= 6.0.0 ==

**`mysub.sh`**
```bash
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

## Exemples de durée d'exécution

* recon-all -all : `#SBATCH --time=08:00:00`
* recon-all -qcache : `#SBATCH --time=00:20:00`
* recon-all -base -tp1 -tp2 : `#SBATCH --time=10:00:00`
* recon-all -long subjid -base base : `#SBATCH --time=10:00:00`
* recon-all -hippocampal-subfields-T1 : `#SBATCH --time=00:40:00`
* recon-all -brainstem-structures: `#SBATCH --time=00:30:00`