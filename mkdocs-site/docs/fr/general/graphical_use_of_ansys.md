---
title: "Graphical use of Ansys/fr"
slug: "graphical_use_of_ansys"
lang: "fr"

source_wiki_title: "Graphical use of Ansys/fr"
source_hash: "5d212623dd7ddcbc900fce3a6142b0ab"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T23:14:56.058273+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

Pour utiliser un programme Ansys en mode graphique, cliquez sur un des liens ci-dessous.

*   [NIBI](../clusters/nibi.md), `https://ondemand.sharcnet.ca`
*   [FIR](../software/fir.md), `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](../clusters/rorqual.md), `https://jupyterhub.rorqual.alliancecan.ca`
*   [Narval](../clusters/narval.md), `https://jupyterhub.narval.alliancecan.ca/`
*   TRILLIUM, `https://ondemand.scinet.utoronto.ca`

Une page web pour la soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources nécessaires pour votre session de bureau interactif et cliquez sur *Lancer* ou *Démarrer*. Si des graphiques accélérés ou des calculs seront effectués à partir de votre session de bureau, assurez-vous de spécifier une ressource GPU. Chargez un module Ansys sur le bureau. Si vous avez démarré un bureau propulsé par JupyterLab, cela peut être fait en cliquant dans le menu de gauche; cependant, si vous avez démarré un bureau OnDemand manuellement, tapez `module load ansys/version` sur la ligne de commande. Pour démarrer un des programmes Ansys courants tels que Fluent, CFX, Workbench, etc., référez-vous aux sections suivantes qui fournissent des conseils pour la configuration des variables d'environnement et des arguments requis par les environnements graphiques basés sur VirtualGL ou Mesa, selon qu'un nœud avec une ressource GPU a été spécifié ou non.

## Fluent

Pour démarrer Ansys Fluent à partir de la ligne de commande sur un bureau OnDemand, ouvrez une fenêtre de terminal et exécutez :

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```

Quand le panneau de sélection contextuel du *Lanceur Fluent* apparaît, cliquez sur l'onglet *Environnement* et copiez/collez les paramètres des variables d'environnement de l'une des deux sous-sections suivantes, selon si vous avez démarré votre session OnDemand avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses, car ce sont des commentaires, et ne mettez pas `export` devant le nom d'aucune variable. Si la fenêtre de la console graphique devient corrompue au démarrage de l'interface graphique (GUI), redémarrez Fluent en configurant `HOOPS_PICTURE=null` pour désactiver la création du panneau graphique.

### Nœud de calcul (sans GPU)

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # (requis sur Nibi avec intelmpi)
HOOPS_PICTURE=opengl2-mesa # (version 2025R1 ou plus récente)
HOOPS_PICTURE=x11/lin # (version 2024R2.04 ou plus ancienne)
```

Cliquez sur le bouton *Démarrer*.

### Nœud de calcul (avec GPU)

Pour utiliser des graphiques accélérés par le matériel avec Fluent sur Nibi, choisissez un t4 (15 Go) dans la liste déroulante du sélecteur de GPU pour votre session de bureau OnDemand. Ceci assure que les variables d'environnement utilisées par VirtualGL pour activer les appels graphiques OpenGL accélérés sont automatiquement configurées dans votre environnement de bureau pour la session actuelle. Une fois votre bureau apparu, ouvrez une fenêtre de terminal et démarrez Workbench comme suit :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # (requis sur Nibi)
HOOPS_PICTURE=opengl2 # (version 2025R1 ou plus récente)
HOOPS_PICTURE=opengl # (version 2024R2.04 ou plus ancienne)
```

Cliquez sur le bouton *Démarrer*.

!!! attention "Note importante"
    Lorsque vous exécutez Fluent sur Nibi, la variable d'environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être configurée manuellement; sinon, Fluent plantera lors du démarrage dans les sessions de bureau de calcul OOD si intelmpi est utilisé. Un message d'erreur comme celui-ci sera généré. Si cela se produit, quittez complètement Fluent, fermez proprement Workbench et recommencez.
    ```
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

## CFX

Lorsque vous démarrez CFX à partir d'un bureau OnDemand, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal. Utilisez `ogl` si vous avez demandé un GPU lors du démarrage du bureau et utilisez `mesa` si ce n'était pas le cas.

```bash
cfx5 -graphics mesa # (sans GPU demandé)
cfx5 -graphics ogl # (avec GPU demandé)
```

## MAPDL

Les étapes suivantes pour démarrer l'interface graphique (GUI) de Mechanical APDL à partir de la ligne de commande d'une fenêtre de terminal devraient fonctionner, peu importe si vous avez démarré votre bureau OnDemand sur un nœud de calcul avec ou sans GPU.

```bash
module load StdEnv/2023 ansys/2022R2 # (ou des versions plus récentes)
mapdl -g
# ou
launcher # puis cliquez sur le bouton Lancer
```

## Workbench

Cette section explique comment démarrer Workbench (et optionnellement Fluent) sur un bureau OnDemand ou un bureau JupyterLab.

### Bureau OnDemand

#### Nœud de calcul (sans GPU demandé) ou bureau de base

Si les graphiques accélérés ne sont pas requis pour votre session de bureau, spécifiez « Nœud GPU » pour sélectionner un nœud de calcul sans GPU pour votre session OOD. Ceci utilise l'émulation logicielle Mesa pour les appels OpenGL, au lieu de fonctionner sur un nœud GPU plus coûteux et plus difficile à réserver.

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

Pour démarrer Fluent depuis Workbench, cliquez sur « Fluid Flow (Fluent) » ou « Fluent with Fluent Meshing » dans le menu « Analyse » à gauche, et cliquez sur « Configuration » dans le panneau contextuel « Fluid Flow (Fluent) » du canevas central. Une fois que le panneau de sélection contextuel du « Lanceur Fluent » apparaît, cliquez sur l'onglet « Environnement » et copiez/collez les paramètres des variables d'environnement suivants :

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # (requis sur le cluster Nibi seulement lors de l'utilisation d'intelmpi)
HOOPS_PICTURE=opengl2-mesa # (optionnel pour 2025R1 ou plus récente)
```

Cliquez sur le bouton *Démarrer*.

#### Nœud de calcul (avec GPU)

Si des graphiques accélérés sont requis sur le cluster Nibi, choisissez un t4 (15 Go) dans la liste déroulante du sélecteur de GPU pour votre session de bureau OnDemand. Ceci garantira que les variables d'environnement utilisées par VirtualGL pour activer les appels graphiques OpenGL accélérés sont automatiquement configurées dans votre environnement de bureau pour la session actuelle. Une fois votre bureau apparu, ouvrez une fenêtre de terminal et démarrez Workbench comme suit :

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

Pour démarrer Fluent depuis Workbench, cliquez sur « Fluid Flow (Fluent) » ou « Fluent with Fluent Meshing » dans le menu « Analyse » de gauche, et cliquez sur « Configuration » dans le panneau contextuel « Fluid Flow Fluent » du canevas central. Une fois que le panneau de sélection contextuel du « Lanceur Fluent » apparaît, cliquez sur l'onglet « Environnement » et copiez/collez les paramètres des variables d'environnement suivants.

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # (requis sur le cluster Nibi seulement)
HOOPS_PICTURE=opengl2 # (optionnel pour 2025R1 ou plus récente)
```

Cliquez sur le bouton *Démarrer*.

### Bureau JupyterHub

#### Nœud de calcul (sans GPU)

#### Nœud de calcul (avec GPU demandé)

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

*   La commande `Rocky` démarre Rocky en mode graphique.
*   La commande `RockySolver` exécute le solveur directement depuis la ligne de commande.
*   L'interface graphique (GUI) de `RockyScheduler` démarre une interface pour soumettre/exécuter des tâches sur le nœud actuel.

## Électronique

Consultez [notre page wiki AnsysEDT](../software/ansysedt.md).