---
title: "VMD/fr"
slug: "vmd"
lang: "fr"

source_wiki_title: "VMD/fr"
source_hash: "3d3b2ee0384e2597a54a0eff3d556f7a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:33:25.599162+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "VMD"
  - "systèmes biomoléculaires"
  - "visualisation moléculaire"
  - "plugiciels"
  - "installation"

questions:
  - "Qu'est-ce que le programme VMD et comment peut-on lancer sa version préinstallée sur une grappe de calcul ?"
  - "Quelles sont les étapes requises pour télécharger, configurer et installer manuellement la version Alpha 1.9.4 de VMD dans son répertoire personnel ?"
  - "Comment doit-on procéder pour installer un plugiciel supplémentaire, comme CaFE, et le rendre accessible via le fichier de configuration de VMD ?"
  - "Qu'est-ce que le programme VMD et comment peut-on lancer sa version préinstallée sur une grappe de calcul ?"
  - "Quelles sont les étapes requises pour télécharger, configurer et installer manuellement la version Alpha 1.9.4 de VMD dans son répertoire personnel ?"
  - "Comment doit-on procéder pour installer un plugiciel supplémentaire, comme CaFE, et le rendre accessible via le fichier de configuration de VMD ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

VMD est un programme de visualisation moléculaire permettant d'afficher, d'animer et d'analyser de grands systèmes biomoléculaires à l'aide de graphiques 3D et de scripts intégrés. Voir [le site Web VMD](https://www.ks.uiuc.edu/Research/vmd/).

## Version préinstallée

Pour activer les fonctionnalités graphiques, connectez-vous à une grappe avec [VNC](../interactive/vnc.md) en utilisant `ssh -X` ou `ssh -Y`. Nous recommandons VNC pour une meilleure performance.

La version par défaut est présentement `1.9.4a57`.
Pour l'utiliser :

```bash
module load vmd
vmd
```

Pour plus d'information sur la commande `module`, voir [Utiliser des modules](../programming/utiliser_des_modules.md), qui décrit aussi comment trouver et utiliser les autres versions préinstallées.

## Installation de la version Alpha 1.9.4

1.  Téléchargez le dernier fichier *tar* Alpha 1.9.4 de [http://www.ks.uiuc.edu/](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) en sélectionnant LINUX_64 (vous devez vous enregistrer).

2.  Copiez le fichier dans le répertoire `/home` de la grappe que vous voulez utiliser.

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

6.  Modifiez le fichier `configure` comme suit, en remplaçant chaque occurrence de `your_user_name` avec votre propre nom d'utilisateur.

    ```text
    # Directory where VMD startup script is installed, should be in users' paths.
    $install_bin_dir="/home/your_user_name/vmd_install";
    
    # Directory where VMD files and executables are installed
    $install_library_dir="/home/your_user_name/vmd_library";
    ```

7.  Lancez `configure` et `make`:

    ```bash
    ./configure
    cd src
    make install
    ```

8.  Ajoutez l'exécutable créé au chemin.

    ```bash
    export PATH=~/vmd_install:$PATH
    ```

9.  Utilisez `setrpaths.sh` pour modifier les exécutables VMD afin qu'ils utilisent les bibliothèques de CVMFS.

    ```bash
    cd ~/vmd_library/
    setrpaths.sh --path .
    ```

!!! tip "Dépannage pour macOS"
    Sous Mac, si la fenêtre est vide, essayez de lancer :

    ```bash
    defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
    ```

## Installation de plugiciels

Plusieurs plugiciels sont disponibles. Vous pouvez les installer dans votre propre espace.
Dans l'exemple suivant, nous installons le [plugiciel CaFE](https://github.com/HuiLiuCode/CaFE_Plugin), avec les directives détaillées qui se trouvent dans [cette page](https://github.com/HuiLiuCode/CaFE_Plugin/blob/master/doc/manual.pdf) :

```bash
wget https://github.com/HuiLiuCode/CaFE_Plugin/archive/refs/heads/master.zip
unzip master.zip
cd CaFE_Plugin-master
mv src cafe1.0
mv cafe1.0 ~
cd
```

Modifiez le fichier `.vmdrc` avec votre éditeur préféré (`nano, vim, emacs`, etc.) et ajoutez la ligne suivante :

```tcl
set auto_path [linsert $auto_path 0 {~/cafe1.0}]
```

Chargez ensuite le module `vmd` et tout autre module requis; le plugiciel CaFE devrait être disponible.

## Liens

*   Webinaires WestGrid (en anglais)
    *   [Visualisation moléculaire avec VMD](https://www.youtube.com/watch?v=_skmrS6X4Ys)
    *   [VMD avancé : Trajectoires, films, scripts](https://www.youtube.com/watch?v=Jce5JN2fLuo)