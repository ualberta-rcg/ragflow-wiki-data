---
title: "VMD/fr"
tags:
  - software
  - biomolecularsimulation

keywords:
  []
---

VMD est un programme de visualisation moléculaire permettant d'afficher, d'animer et d'analyser de grands systèmes biomoléculaires à l'aide de graphiques 3D et de scripts intégrés. Voir  [le site Web VMD](https://www.ks.uiuc.edu/Research/vmd/).

<span id="Using_a_pre-installed_version"></span>
## Version préinstallée 

Pour activer les fonctionnalités graphiques, connectez-vous à une grappe avec [VNC](vnc-fr.md) en utilisant `ssh -X` ou `ssh -Y`. Nous recommandons VNC pour une meilleure performance.

La version par défaut est présentement `1.9.4a57`.
Pour l'utiliser :

```bash
vmd
```

Pour plus d'information sur la commande `module`, voir [Utiliser des modules](utiliser-des-modules.md), qui décrit aussi comment trouver et utiliser les autres versions préinstallées.

<span id="Installing_version_1.9.4_Alpha"></span>
## Installation de la version Alpha 1.9.4 

1. Téléchargez le dernier fichier *tar* Alpha 1.9.4 de [http://www.ks.uiuc.edu/](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD)  en sélectionnant LINUX_64 (vous devez vous enregistrer).

2. Copiez le fichier dans le répertoire /home de la grappe que vous voulez utiliser.

3. Décompactez le fichier.

 tar xvf vmd-1.9.4*.opengl.tar.gz

4. Positionnez-vous dans le répertoire créé.

 cd vmd-1.9.4*

5. Créez deux nouveaux répertoires pour y enregistrer les fichiers.

 mkdir ~/vmd_install
 mkdir ~/vmd_library

5. Modifiez le fichier `configure` comme suit, en remplaçant chaque occurrence de  `your_user_name` avec votre propre nom d'utilisateur.

 # Directory where VMD startup script is installed, should be in users' paths.
 $install_bin_dir="/home/your_user_name/vmd_install";
 
 # Directory where VMD files and executables are installed
 $install_library_dir="/home/your_user_name/vmd_library";

6. Lancez `configure` et `make`:

 ./configure
 cd src
 make install

7. Ajoutez l'exécutable créé au chemin.
 export PATH=~/vmd_install:$PATH

8. Utilisez `setrpaths.sh` pour modifier les exécutables VMD afin qu'ils utilisent les bibliothèques de CVMFS.
 cd ~/vmd_library/
 setrpaths.sh  --path .

Sous Mac, si la fenêtre est vide, essayez de lancer

 defaults write org.macosforge.xquartz.X11 enable_iglx -bool true

<span id="Installing_plugins"></span>
## Installation de plugiciels 

Plusieurs plugiciels sont disponibles. Vous pouvez les installer dans votre propre espace.  
Dans l'exemple suivant, nous installons le [plugiciel CaFE](https://github.com/HuiLiuCode/CaFE_Plugin),
avec les directives détaillées qui se trouvent dans [cette page](https://github.com/HuiLiuCode/CaFE_Plugin/blob/master/doc/manual.pdf)&nbsp;:

 wget https://github.com/HuiLiuCode/CaFE_Plugin/archive/refs/heads/master.zip
 unzip master.zip
 cd CaFE_Plugin-master
 mv src cafe1.0
 mv cafe1.0 ~
 cd

Modifiez le fichier `.vmdrc` avec votre éditeur préféré (`nano, vim, emacs`, etc.) et ajoutez la ligne suivante&bnsp;:

 set auto_path [linsert $auto_path 0 {~/cafe1.0}]

Chargez ensuite le module `vmd` et tout autre module requis; le plugiciel CaFE devrait être disponible.

<span id="Links"></span>
## Liens 

* Webinaires WestGrid (en anglais)
** [Molecular visualization with VMD](https://www.youtube.com/watch?v=_skmrS6X4Ys) 
** [Advanced VMD: Trajectories, movies, scripting](https://www.youtube.com/watch?v=Jce5JN2fLuo)