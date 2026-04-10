---
title: "VMD/fr"
slug: "vmd"
lang: "fr"

source_wiki_title: "VMD/fr"
source_hash: "3d3b2ee0384e2597a54a0eff3d556f7a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T12:34:13.050932+00:00"

tags:
  - software
  - biomolecularsimulation

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

VMD est un programme de visualisation moléculaire permettant d'afficher, d'animer et d'analyser de grands systèmes biomoléculaires à l'aide de graphiques 3D et de scripts intégrés. Voyez [le site Web de VMD](https://www.ks.uiuc.edu/Research/vmd/).

## Version préinstallée

Pour activer les fonctionnalités graphiques, connectez-vous à un cluster avec [VNC](vnc.md) en utilisant `ssh -X` ou `ssh -Y`.

!!! tip "Recommandation"
    Pour une meilleure performance graphique, nous recommandons de vous connecter via VNC.

La version par défaut est actuellement `1.9.4a57`.
Pour l'utiliser :

```bash
module load vmd
vmd
```

Pour plus d'information sur la commande `module`, voyez [Utiliser des modules](utiliser-des-modules.md), qui décrit aussi comment trouver et utiliser les autres versions préinstallées.

## Installation de la version Alpha 1.9.4

1.  Téléchargez le plus récent fichier *tar* Alpha 1.9.4 à partir de [http://www.ks.uiuc.edu/](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) en sélectionnant LINUX_64 (vous devez vous inscrire).

2.  Copiez le fichier dans le répertoire /home du cluster que vous voulez utiliser.

3.  Décompactez le fichier.

    ```bash
    tar xvf vmd-1.9.4*.opengl.tar.gz
    ```

4.  Positionnez-vous dans le répertoire créé.

    ```bash
    cd vmd-1.9.4*
    ```

5.  Créez deux nouveaux répertoires pour y enregistrer les fichiers.

    ```bash
    mkdir ~/vmd_install
    mkdir ~/vmd_library
    ```

6.  Modifiez le fichier `configure` comme suit, en remplaçant chaque occurrence de `your_user_name` par votre propre nom d'utilisateur.

    ```perl
    # Directory where VMD startup script is installed, should be in users' paths.
    $install_bin_dir="/home/your_user_name/vmd_install";

    # Directory where VMD files and executables are installed
    $install_library_dir="/home/your_user_name/vmd_library";
    ```

7.  Lancez `configure` et `make` :

    ```bash
    ./configure
    cd src
    make install
    ```

8.  Ajoutez l'exécutable créé au chemin (PATH).

    ```bash
    export PATH=~/vmd_install:$PATH
    ```

9.  Utilisez `setrpaths.sh` pour modifier les exécutables de VMD afin qu'ils utilisent les bibliothèques de CVMFS.

    ```bash
    cd ~/vmd_library/
    setrpaths.sh --path .
    ```

Sous Mac, si la fenêtre est vide, essayez d'exécuter la commande suivante :

```bash
defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
```

## Installation de modules d'extension

Plusieurs modules d'extension sont disponibles. Vous pouvez les installer dans votre propre espace.
Dans l'exemple suivant, nous installons le [module d'extension CaFE](https://github.com/HuiLiuCode/CaFE_Plugin), avec les directives détaillées qui se trouvent dans [ce manuel (PDF)](https://github.com/HuiLiuCode/CaFE_Plugin/blob/master/doc/manual.pdf) :

```bash
wget https://github.com/HuiLiuCode/CaFE_Plugin/archive/refs/heads/master.zip
unzip master.zip
cd CaFE_Plugin-master
mv src cafe1.0
mv cafe1.0 ~
cd
```

Modifiez le fichier `.vmdrc` avec votre éditeur préféré (`nano`, `vim`, `emacs`, etc.) et ajoutez la ligne suivante :

```tcl
set auto_path [linsert $auto_path 0 {~/cafe1.0}]
```

Chargez ensuite le module `vmd` et tout autre module requis; le module d'extension CaFE devrait alors être disponible.

## Liens utiles

*   Webinaires de WestGrid (en anglais)
    *   [Molecular visualization with VMD](https://www.youtube.com/watch?v=_skmrS6X4Ys)
    *   [Advanced VMD: Trajectories, movies, scripting](https://www.youtube.com/watch?v=Jce5JN2fLuo)