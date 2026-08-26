---
title: "Graphical use of Ansys/fr"
slug: "graphical_use_of_ansys"
lang: "fr"

source_wiki_title: "Graphical use of Ansys/fr"
source_hash: "e880c250ac98cafd3c42f5d1ca6ba746"
last_synced: "2026-08-26T10:16:11.334907+00:00"
last_processed: "2026-08-26T11:24:42.827812+00:00"

tags:
  []

keywords:
  - "Ansys"
  - "I_MPI_HYDRA_BOOTSTRAP=ssh"
  - "versions 2025R1"
  - "module load StdEnv/2023 ansys/2025R2.04"
  - "HOOPS_PICTURE=opengl2"
  - "versions 2024R2.04"
  - "GPU"
  - "HOOPS_PICTURE=opengl2-mesa"
  - "Fluent sur Nibi"
  - "VirtualGL"
  - "HOOPS_PICTURE=opengl"
  - "HOOPS_PICTURE"
  - "session OnDemand"
  - "Fluent Launcher"
  - "Workbench (VNC)"
  - "sélection du GPU"
  - "runwb2"
  - "accélération OpenGL"
  - "mode graphique"
  - "module load ansys"
  - "accélération graphique GPU"
  - "bureau OnDemand"

questions:
  - "Comment lancer un programme Ansys en mode graphique en utilisant les portails Open OnDemand ou JupyterHub des clusters mentionnés ?"
  - "Quelles variables d’environnement doivent être définies pour exécuter Fluent sur un nœud de calcul sans GPU et sur un nœud avec GPU, en fonction des versions d’Ansys ?"
  - "Que faire si la fenêtre de la console graphique de Fluent est corrompue au démarrage, et comment choisir la valeur appropriée de HOOPS_PICTURE selon la version et la présence d’un GPU ?"
  - "Quelle variable d’environnement doit être définie manuellement pour éviter que Fluent ne plante sur Nibi lorsqu’on utilise IntelMPI, et comment la configurer dans Workbench ?"
  - "Comment choisir entre les options graphiques « mesa » et « ogl » lors du lancement de CFX, et dans quels cas chaque option doit‑elle être utilisée ?"
  - "Quelles sont les étapes pour démarrer Workbench (et Fluent) sur un bureau OnDemand, en distinguant les procédures pour un nœud de calcul sans GPU et avec GPU ?"
  - "Quelle variable d'environnement doit être définie pour le bootstrap MPI sur Nibi ?"
  - "Quelle valeur doit prendre la variable HOOPS_PICTURE selon la version de Workbench utilisée ?"
  - "Quelle action finale doit‑on effectuer pour démarrer Workbench après avoir configuré les variables ?"
  - "Comment le GPU est‑il sélectionné pour votre session de bureau OnDemand ?"
  - "Quel est le rôle des variables d’environnement configurées par VirtualGL dans l’accélération des appels OpenGL ?"
  - "Quelle commande doit‑on exécuter, après le chargement des modules, pour lancer Workbench dans le terminal ?"
  - "Quels paramètres de variables d'environnement doivent être définis dans l’onglet « Environment » du « Fluent Launcher », et dans quelles situations sont‑ils obligatoires ou optionnels ?"
  - "Comment créer une icône personnalisée « runwb2 » sur le bureau JupyterHub pour démarrer Workbench en mode Mesa, en détaillant les étapes de copie, modification du fichier desktop et actualisation du bureau ?"
  - "Quelles sont les procédures distinctes pour lancer Workbench (et les applications associées comme Ensight ou Rocky) sur un nœud de calcul avec GPU versus sans GPU, et quelles commandes spécifiques sont indiquées pour Ensight et Rocky ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Pour utiliser un programme [Ansys](../software/ansys.md) en mode graphique, cliquez sur un des liens ci-dessous.

*   [Nibi](../clusters/nibi.md), `https://ondemand.sharcnet.ca`
*   [Fir](../software/fir.md), `https://jupyterhub.fir.alliancecan.ca`
*   Rorqual, `https://jupyterhub.rorqual.alliancecan.ca`
*   [Narval](../clusters/narval.md), `https://jupyterhub.narval.alliancecan.ca/`
*   [Trillium](../interactive/trillium_open_ondemand_quickstart.md), `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâche devrait s'afficher dans votre navigateur. Configurez les ressources nécessaires à votre session de bureau interactive et cliquez sur **Lancer** ou **Démarrer**. Si vous prévoyez d'effectuer des calculs ou des rendus graphiques accélérés dans votre session de bureau, spécifiez une ressource GPU. Chargez un module Ansys sur le bureau. Si vous avez lancé un bureau JupyterLab, sélectionnez l'icône correspondante dans le menu de gauche; si vous avez lancé un bureau OnDemand manuellement, entrez `module load ansys/version` dans la ligne de commande. Pour lancer l'un des programmes Ansys courants tels que Fluent, CFX, Workbench, etc., reportez-vous aux sections suivantes qui fournissent des conseils sur la configuration des variables d'environnement et des arguments requis par les environnements graphiques VirtualGL ou Mesa, selon qu'un nœud avec GPU a été spécifié ou non.

## Fluent

Pour utiliser Ansys Fluent à partir de la ligne de commande sur un bureau OnDemand, ouvrez une fenêtre de terminal et exécutez :

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```

Lorsque le panneau de sélection du lanceur Fluent apparaît, cliquez sur l'onglet **Environnement** et copiez-collez les paramètres des variables d'environnement de l'une des deux sous-sections suivantes, selon que vous ayez démarré votre session OnDemand avec un GPU ou non. N'incluez pas le texte entre parenthèses, car il s'agit de commentaires, et n'ajoutez pas `export` devant le nom d'une variable. Si la fenêtre de la console graphique est corrompue au démarrage de l'interface graphique, redémarrez Fluent en définissant `HOOPS_PICTURE=null` pour désactiver la création du panneau graphique.

### Nœud de calcul (sans GPU)

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh   # (requis sur Nibi avec intelmpi)
HOOPS_PICTURE=opengl2-mesa  # (versions 2025R1 et suivantes)
HOOPS_PICTURE=x11/lin       # (versions 2024R2.04 ou précédentes)
```
Cliquez sur le bouton **Démarrer**.

### Nœud de calcul (avec GPU)

Pour utiliser l'accélération graphique avec Fluent sur Nibi, sélectionnez un t4 (15Go) dans la liste déroulante de sélection du GPU pour votre session de bureau OnDemand. Ceci fait en sorte que les variables d'environnement utilisées par VirtualGL pour activer l'accélération des appels OpenGL sont automatiquement configurées dans votre environnement de bureau pour la session en cours. Une fois votre bureau affiché, ouvrez une fenêtre de terminal et lancez Workbench comme suit :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # (requis sur Nibi)
HOOPS_PICTURE=opengl2     # (versions 2025R1 ou suivantes)
HOOPS_PICTURE=opengl      # (versions 2024R2.04 ou précédentes)
```
Cliquez sur le bouton **Démarrer**.

!!! note "Remarque"
    Lors de l'exécution de Fluent sur Nibi, la variable d'environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être définie manuellement, autrement Fluent plantera au démarrage dans les sessions OOD si IntelMPI est utilisé. Un message d’erreur similaire au suivant sera généré. Si cela se produit, quittez complètement Fluent, fermez Workbench proprement et redémarrez-le.
    ```text
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

## CFX

Au lancement de CFX à partir d'un bureau OnDemand, les arguments suivants peuvent être spécifiés dans la ligne de commande de la fenêtre de terminal. Utilisez `ogl` si vous avez demandé un GPU au démarrage du bureau et `mesa` dans le cas contraire.

```bash
cfx5 -graphics mesa   # (sans  GPU )
cfx5 -graphics ogl    # (avec GPU)
```

## Mapdl

Pour démarrer l'interface graphique de Mechanical APDL à partir de la ligne de commande d'une fenêtre de terminal, les étapes suivantes devraient fonctionner, que vous ayez démarré votre bureau OnDemand sur un nœud de calcul avec ou sans GPU.

```bash
module load StdEnv/2023 ansys/2022R2 # (ou versions plus récentes)
```
*   `mapdl -g`
*   **Ou bien** `launcher` puis cliquez sur le bouton **Exécuter**.

## Workbench

Nous décrivons ici comment démarrer Workbench (et éventuellement Fluent) sur un bureau OnDemand ou un bureau JupyterLab.

### Bureau OnDemand

#### Nœud de calcul (sans GPU) ou bureau de base

Si l'accélération graphique n'est pas requise pour votre session de bureau, spécifiez **Nœud GPU** pour sélectionner un nœud de calcul sans GPU pour votre session OOD. Ceci utilise l'émulation logicielle Mesa pour les appels OpenGL, au lieu d'exécuter le programme sur un nœud GPU plus coûteux et plus difficile à réserver.

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

Pour lancer Fluent à partir de Workbench, cliquez sur **Fluid Flow (Fluent)** ou **Fluent with Fluent Meshing** dans le menu de gauche **Analyse** puis cliquez sur **Configuration** au centre de la fenêtre contextuelle **Fluid Flow (Fluent)**. Dans le panneau de sélection **Lanceur Fluent** affiché, cliquez sur l'onglet **Environnement** et copiez-collez les paramètres de variables d'environnement suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh   # (requis uniquement sur Nibi pour l'utilisation d'IntelMPI)
HOOPS_PICTURE=opengl2-mesa  # (facultatif pour 2025R1 ou versions suivantes)
```
Cliquez sur le bouton **Démarrer**.

#### Nœud de calcul (avec GPU)

Pour utiliser l'accélération graphique sur Nibi, sélectionnez un t4 (15Go) dans la liste déroulante de sélection du GPU pour votre session de bureau OnDemand. Ceci fait en sorte que les variables d'environnement utilisées par VirtualGL pour activer l'accélération des appels OpenGL sont automatiquement configurées dans votre environnement de bureau pour la session en cours. Une fois votre bureau affiché, ouvrez une fenêtre de terminal et lancez Workbench comme suit :

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

Pour lancer Fluent à partir de Workbench, cliquez sur **Fluid Flow (Fluent)** ou **Fluent with Fluent Meshing** dans le menu de gauche **Analyse** puis cliquez sur **Configuration** au centre de la fenêtre contextuelle **Fluid Flow (Fluent)**. Dans le panneau de sélection **Lanceur Fluent** affiché, cliquez sur l'onglet **Environnement** et copiez-collez les paramètres de variables d'environnement suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh   # (requis uniquement sur Nibi)
HOOPS_PICTURE=opengl2-mesa  # (facultatif pour 2025R1 ou versions suivantes)
```
Cliquez sur le bouton **Démarrer**.

### Bureau JupyterHub

#### Nœud de calcul (sans GPU)

1.  Dans le menu du bureau à gauche, sélectionnez Ansys/2025R1 (ou une version plus récente) pour le charger.
2.  Sélectionnez l'icône **Workbench (VNC)** située dans la fenêtre centrale de JupyterLab.

    Si l'affichage d'une application (comme Fluent) lancée depuis Workbench semble corrompu et inutilisable, suivez les étapes suivantes pour créer une icône personnalisée `runwb2` sur le bureau afin de pouvoir démarrer Workbench en mode Mesa.

    **OU BIEN**, si Fluent est l'une des applications que vous allez lancer dans Workbench, vous pouvez aussi essayer de :
    *   définir la variable `HOOPS_PICTURE=opengl2-mesa` dans la fenêtre **Lanceur Fluent** au lancement de Fluent.

3.  Quittez Workbench et ouvrez une fenêtre de terminal. Copiez/collez la commande suivante dans le **Presse-papiers distant** situé en haut à droite de votre bureau Jupyter :
    ```bash
    cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop
    ```
4.  Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que nano avec :
    ```bash
    nano ~/Desktop/workbench-mesa.desktop
    ```
5.  Modifiez la ligne `Exec=` dans le fichier `.desktop` pour ajouter l'option `-mesa` à la commande `runwb2` (par exemple, si la ligne est `Exec=/path/to/runwb2`, changez-la en `Exec=/path/to/runwb2 -mesa`). Fermez l'éditeur en enregistrant les modifications.
6.  Actualisez le bureau Jupyter en appuyant sur la combinaison de touches *Ctrl+R*. La nouvelle icône devrait maintenant apparaître sur le bureau, à côté de l'icône Workbench d'origine. Double-cliquez dessus pour démarrer Workbench. La nouvelle icône restera affichée pour les sessions suivantes jusqu'à ce que vous la supprimiez manuellement avec :
    ```bash
    rm -f ~/Desktop/workbench-mesa.desktop
    ```

#### Nœud de calcul (avec GPU)

*   Dans le menu du bureau, sélectionnez ansys/2025R1 (ou versions suivantes).
*   Dans le menu au centre du bureau Jupyter, sélectionnez l'icône **Workbench (VNC)**.

## Ensight

```bash
module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6
export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib
ensight -X
```

## Rocky

Chargez les modules suivants :
```bash
module load StdEnv/2023 ansys/2025R2.04 # (ou 2025R1, 2025R1.02, 2025R2)
```
*   La commande `Rocky` lance Rocky en mode graphique.
*   La commande `RockySolver` exécute le solveur directement sur la ligne de commande.
*   La commande `RockyScheduler` lance une interface graphique pour soumettre et exécuter des tâches sur le nœud actif.

## Electronics

Voir notre page wiki [AnsysEDT](../software/ansysedt.md).