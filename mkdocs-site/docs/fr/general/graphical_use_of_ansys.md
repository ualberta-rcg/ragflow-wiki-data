---
title: "Graphical use of Ansys/fr"
slug: "graphical_use_of_ansys"
lang: "fr"

source_wiki_title: "Graphical use of Ansys/fr"
source_hash: "044d72d29928f4392e89cf4db13c506f"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:41:22.912044+00:00"

tags:
  []

keywords:
  - "HOOPS_PICTURE=opengl2"
  - "I_MPI_HYDRA_BOOTSTRAP=ssh"
  - "versions 2024R2.04"
  - "Workbench (VNC)"
  - "versions 2025R1"
  - "OnDemand"
  - "Open OnDemand"
  - "Fluent"
  - "VirtualGL"
  - "runwb2"
  - "Fluent Launcher"
  - "HOOPS_PICTURE=opengl2-mesa"
  - "session de bureau OnDemand"
  - "HOOPS_PICTURE=opengl"
  - "Ansys"
  - "GPU"
  - "HOOPS_PICTURE"
  - "Mesa"
  - "accélération OpenGL"
  - "module load StdEnv/2023 ansys/2025R2.04"

questions:
  - "Quels sont les liens et plateformes recommandés pour lancer un programme Ansys en mode graphique via Open OnDemand ou JupyterHub ?"
  - "Comment doit‑on configurer les variables d’environnement pour exécuter Fluent sur un nœud de calcul avec ou sans GPU ?"
  - "Quelles étapes sont nécessaires pour charger le module Ansys et démarrer une session de bureau interactive, notamment en cas d’utilisation d’un GPU pour l’accélération graphique ?"
  - "Quelle variable d’environnement doit être définie manuellement sur Nibi pour éviter que Fluent ne plante lorsqu’on utilise IntelMPI, et comment doit‑elle être renseignée dans Workbench ?"
  - "Comment choisir entre un nœud de calcul avec ou sans GPU lors du lancement d’un bureau OnDemand, et quelles sont les commandes à utiliser pour démarrer Workbench/Fluent dans chaque cas ?"
  - "Quelles sont les lignes de commande à employer pour lancer CFX et MAPDL depuis un terminal OnDemand, en fonction de la présence ou non d’un GPU ?"
  - "Pourquoi faut‑il définir la variable I_MPI_HYDRA_BOOTSTRAP=ssh sur la machine Nibi avant de lancer Workbench ?"
  - "Quelle valeur doit‑on attribuer à la variable HOOPS_PICTURE pour les versions 2025R1 ou ultérieures de Workbench ?"
  - "Comment choisir entre les paramètres HOOPS_PICTURE=opengl2 et HOOPS_PICTURE=opengl en fonction de la version de Workbench utilisée ?"
  - "Comment sélectionner le GPU approprié pour votre session de bureau OnDemand afin d’activer l’accélération OpenGL ?"
  - "Quelles variables d’environnement VirtualGL sont configurées automatiquement lors du lancement du bureau ?"
  - "Quelle commande doit‑être exécutée dans le terminal pour charger les modules nécessaires avant de lancer Workbench ?"
  - "Quels paramètres de variables d'environnement doivent être définis dans le panneau « Fluent Launcher » pour lancer Fluent, et dans quelles situations sont-ils requis ou optionnels ?"
  - "Comment créer une icône personnalisée « runwb2 » sur le bureau JupyterHub pour démarrer Workbench en mode Mesa, et quelles sont les étapes pour la supprimer ultérieurement ?"
  - "Quelles sont les commandes et modules à charger pour exécuter Ensight et Rocky sur le nœud de calcul, et quelles différences existent entre leurs modes d’utilisation (graphique vs ligne de commande) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

Pour utiliser un programme [Ansys](../software/ansys.md) en mode graphique, cliquez sur un des liens ci-dessous :

*   [NIBI](../clusters/nibi.md) : `https://ondemand.sharcnet.ca`
*   [FIR](../software/fir.md) : `https://jupyterhub.fir.alliancecan.ca`
*   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
*   [Narval](../clusters/narval.md) : `https://jupyterhub.narval.alliancecan.ca/`
*   TRILLIUM : `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâche devrait s'afficher dans votre navigateur. Configurez les ressources nécessaires à votre session de bureau interactive et cliquez sur 'Lancer' ou 'Démarrer'. Si vous prévoyez d'effectuer des calculs ou des rendus graphiques accélérés dans votre session de bureau, spécifiez une ressource GPU. Chargez un module Ansys sur le bureau. Si vous avez lancé un bureau JupyterLab, cliquez sur l'icône correspondante dans le menu de gauche; autrement, si vous avez lancé un bureau OnDemand manuellement, entrez `module load ansys/version` dans la ligne de commande. Pour lancer l'un des programmes Ansys courants tels que Fluent, CFX, Workbench, etc., reportez-vous aux sections suivantes qui fournissent des conseils sur la configuration des variables d'environnement et des arguments requis par les environnements graphiques VirtualGL ou Mesa, selon qu'un nœud avec GPU a été spécifié ou non.

## Fluent

Pour utiliser Ansys Fluent à partir de la ligne de commande sur un bureau OnDemand, ouvrez une fenêtre de terminal et exécutez :

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```

Lorsque le panneau de sélection du lanceur Fluent apparaît, cliquez sur l'onglet 'Environnement' et copiez-collez les paramètres des variables d'environnement de l'une des deux sous-sections suivantes, selon que vous ayez démarré votre session OnDemand avec un GPU ou non. N'incluez pas le texte entre parenthèses, car il s'agit de commentaires, et n'ajoutez pas `export` devant le nom d'une variable. Si la fenêtre de la console graphique est corrompue au démarrage de l'interface graphique, redémarrez Fluent en définissant `HOOPS_PICTURE=null` pour désactiver la création du panneau graphique.

### Nœud de calcul (sans GPU)

Appliquez les paramètres suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh  # requis sur Nibi avec intelmpi
HOOPS_PICTURE=opengl2-mesa # versions 2025R1 et suivantes
HOOPS_PICTURE=x11/lin      # versions 2024R2.04 ou précédentes
```

Cliquez sur le bouton 'Démarrer'.

### Nœud de calcul (avec GPU)

Pour utiliser l'accélération graphique avec Fluent sur Nibi, sélectionnez un t4 (15Go) dans la liste déroulante de sélection du GPU pour votre session de bureau OnDemand. Ceci fait en sorte que les variables d'environnement utilisées par VirtualGL pour activer l'accélération des appels OpenGL sont automatiquement configurées dans votre environnement de bureau pour la session en cours. Une fois votre bureau affiché, ouvrez une fenêtre de terminal et lancez Workbench comme suit :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # requis sur Nibi
HOOPS_PICTURE=opengl2     # versions 2025R1 ou suivantes
HOOPS_PICTURE=opengl      # versions 2024R2.04 ou précédentes
```

Cliquez sur le bouton 'Démarrer'.

!!! warning "Remarque"
    Lors de l’exécution de Fluent sur Nibi, la variable d’environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être définie manuellement, autrement Fluent plantera au démarrage dans les sessions OOD si IntelMPI est utilisé. Un message d’erreur similaire au suivant sera généré. Si cela se produit, quittez complètement Fluent, fermez Workbench proprement et redémarrez-le.

    ```
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

## CFX

Au lancement de CFX à partir d'un bureau OnDemand, les arguments suivants peuvent être spécifiés dans la ligne de commande de la fenêtre de terminal. Utilisez `ogl` si vous avez demandé un GPU au démarrage du bureau et `mesa` dans le cas contraire.

```bash
cfx5 -graphics mesa # sans GPU
cfx5 -graphics ogl  # avec GPU
```

## Mapdl

Pour démarrer l'interface graphique de Mechanical APDL à partir de la ligne de commande d'une fenêtre de terminal, les étapes suivantes devraient fonctionner, que vous ayez démarré votre bureau OnDemand sur un nœud de calcul avec ou sans GPU.

1.  Chargez le module Ansys :
    ```bash
    module load StdEnv/2023 ansys/2022R2 # ou versions plus récentes
    ```
2.  Lancez l'interface graphique avec :
    ```bash
    mapdl -g
    ```
3.  Ou, lancez le lanceur et cliquez sur le bouton 'Exécuter' :
    ```bash
    launcher
    ```

## Workbench

Nous décrivons ici comment démarrer Workbench (et éventuellement Fluent) sur un bureau OnDemand ou un bureau JupyterLab.

### Bureau OnDemand

#### Nœud de calcul (sans GPU) ou bureau de base

Si l'accélération graphique n'est pas requise pour votre session de bureau, spécifiez 'Nœud GPU' pour sélectionner un nœud de calcul sans GPU pour votre session OOD. Ceci utilise l'émulation logicielle Mesa pour les appels OpenGL, au lieu d'exécuter le programme sur un nœud GPU plus coûteux et plus difficile à réserver.

1.  Chargez le module Ansys :
    ```bash
    module load StdEnv/2023 ansys/2025R2.04
    ```
2.  Démarrez Workbench :
    ```bash
    runwb2
    ```

Pour lancer Fluent à partir de Workbench, cliquez sur 'Écoulement de fluide (Fluent)' ou 'Fluent avec maillage Fluent' dans le menu de gauche 'Analyse' puis cliquez sur 'Configuration' au centre de la fenêtre contextuelle 'Écoulement de fluide (Fluent)'. Dans le panneau de sélection 'Lanceur Fluent' affiché, cliquez sur l'onglet 'Environnement' et copiez-collez les paramètres de variables d'environnement suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh  # requis uniquement sur Nibi pour l'utilisation d'IntelMPI
HOOPS_PICTURE=opengl2-mesa # facultatif pour 2025R1 ou versions suivantes
```

Cliquez sur le bouton 'Démarrer'.

#### Nœud de calcul (avec GPU)

Pour utiliser l'accélération graphique sur Nibi, sélectionnez un t4 (15Go) dans la liste déroulante de sélection du GPU pour votre session de bureau OnDemand. Ceci fait en sorte que les variables d'environnement utilisées par VirtualGL pour activer l'accélération des appels OpenGL sont automatiquement configurées dans votre environnement de bureau pour la session en cours. Une fois votre bureau affiché, ouvrez une fenêtre de terminal et lancez Workbench comme suit :

1.  Chargez le module Ansys :
    ```bash
    module load StdEnv/2023 ansys/2025R2.04
    ```
2.  Démarrez Workbench :
    ```bash
    runwb2
    ```

Pour lancer Fluent à partir de Workbench, cliquez sur 'Écoulement de fluide (Fluent)' ou 'Fluent avec maillage Fluent' dans le menu de gauche 'Analyse' puis cliquez sur 'Configuration' au centre de la fenêtre contextuelle 'Écoulement de fluide (Fluent)'. Dans le panneau de sélection 'Lanceur Fluent' affiché, cliquez sur l'onglet 'Environnement' et copiez-collez les paramètres de variables d'environnement suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh  # requis uniquement sur Nibi
HOOPS_PICTURE=opengl2-mesa # facultatif pour 2025R1 ou versions suivantes
```

Cliquez sur le bouton 'Démarrer'.

### Bureau JupyterHub

#### Nœud de calcul (sans GPU)

1.  Dans le menu du bureau à gauche, cliquez pour charger Ansys/2025R1 (ou une version plus récente).
2.  Cliquez sur l'icône 'Workbench (VNC)' située dans la fenêtre centrale de JupyterLab.
    Si l'affichage d'une application (comme Fluent) lancée depuis Workbench semble corrompu et inutilisable, suivez les étapes suivantes pour créer une icône personnalisée pour lancer Workbench en mode Mesa. Si l'une des applications que vous lancez dans Workbench est Fluent, vous pouvez également essayer de définir la variable `HOOPS_PICTURE=opengl2-mesa` dans la fenêtre du 'Lanceur Fluent' au moment du lancement.
3.  Quittez Workbench et ouvrez une fenêtre de terminal. Copiez/collez la commande suivante dans le 'Presse-papiers distant' situé en haut à droite de votre bureau Jupyter :
    ```bash
    cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop
    ```
4.  Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que nano avec :
    ```bash
    nano ~/Desktop/workbench-mesa.desktop
    ```
5.  Modifiez toutes les occurrences de `runwb2` et fermez l'éditeur en enregistrant les modifications.
6.  Actualisez le bureau Jupyter en appuyant sur la combinaison de touches <kbd>Ctrl</kbd>+<kbd>R</kbd>. La nouvelle icône devrait maintenant apparaître sur le bureau, à côté de l'icône Workbench d'origine. Double-cliquez dessus pour démarrer Workbench. La nouvelle icône restera affichée pour les sessions suivantes jusqu'à ce que vous la supprimiez manuellement avec :
    ```bash
    rm -f ~/Desktop/workbench-mesa.desktop
    ```

#### Nœud de calcul (avec GPU)

1.  Dans le menu du bureau, cliquez sur ansys/2025R1 (ou versions suivantes).
2.  Dans le menu au centre du bureau Jupyter, cliquez sur l'icône Workbench (VNC).

## Ensight

```bash
module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6
export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib
ensight -X
```

## Rocky

Chargez les modules suivants :

```bash
module load StdEnv/2023 ansys/2025R2.04 # ou 2025R1, 2025R1.02, 2025R2
```

*   La commande `Rocky` lance Rocky en mode graphique.
*   La commande `RockySolver` exécute le solveur directement sur la ligne de commande.
*   La commande `RockySchedular` lance une interface graphique pour soumettre et exécuter des tâches sur le nœud actif.

## Electronics

Voir notre page [AnsysEDT](../software/ansysedt.md).