---
title: "JupyterLab/fr"
slug: "jupyterlab"
lang: "fr"

source_wiki_title: "JupyterLab/fr"
source_hash: "a879e126a84292d10aa13ddee256ed1c"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:53:49.176562+00:00"

tags:
  []

keywords:
  - "OpenRefine"
  - "entissage automatique"
  - "JupyterLab"
  - "modules logiciels"
  - "nbconvert"
  - "métriques expérimentales"
  - "Liste des outils"
  - "dynamique des fluides"
  - "naviguer"
  - "interface graphique"
  - "navigateur"
  - "File Browser"
  - "licence"
  - "applications préconstruites"
  - "icône de lancement"
  - "Grappe"
  - "Visual Studio Code"
  - "VS Code"
  - "plongements lexicaux"
  - "importer des fichiers"
  - "extensions préinstallées"
  - "Terminal"
  - "Ansys Mapdl"
  - "Ansys CFX"
  - "Modules"
  - "simulation numérique"
  - "Notebook Python"
  - "session VNC"
  - "graphe du modèle"
  - "interface web"
  - "Icônes de lancement"
  - "Environnements de bureau"
  - "noyau Python"
  - "JupyterHub"
  - "Ansys Fluent"
  - "Tensorboard"
  - "Star-CCM+"
  - "RStudio"
  - "code-server"
  - "scipy-stack"
  - "Ansys Workbench"
  - "Interface utilisateur"
  - "charger un module"
  - "LibreQDA"
  - "démarrage de session"
  - "tensorboard"
  - "Open OnDemand"
  - "MLflow"

questions:
  - "Quelles sont les principales fonctionnalités de JupyterLab et quelles applications peut-on y lancer ?"
  - "Quelles sont les méthodes recommandées pour démarrer JupyterLab et comment vérifier sa disponibilité sur les différentes grappes ?"
  - "Comment est structurée l'interface de JupyterLab et à quoi servent le tableau de bord principal et la liste des outils à gauche ?"
  - "Comment fonctionne la gestion (recherche, chargement et dépendances) des modules logiciels dans l'interface JupyterLab ?"
  - "Quelle est la procédure recommandée pour installer des paquets Python supplémentaires qui ne sont pas inclus dans l'environnement par défaut ?"
  - "Quelles sont les caractéristiques et les particularités de lancement de l'application VS Code intégrée à cet environnement ?"
  - "À quoi sert la liste des outils située sur le côté gauche de l'interface JupyterLab ?"
  - "Quels sont les espaces de stockage dans lesquels il est possible de naviguer grâce au « File Browser » ?"
  - "Quelle autre action, en dehors de la navigation, peut-on effectuer à l'aide du « File Browser » ?"
  - "Comment l'application code-server est-elle rendue accessible aux utilisateurs ?"
  - "Quelle est la particularité de la version de code-server installée en ce qui concerne les extensions ?"
  - "Quel est le temps d'attente maximal estimé pour le démarrage d'une nouvelle session ?"
  - "Quels sont les différents outils logiciels présentés dans le texte et quelles sont leurs fonctions principales ?"
  - "Comment fonctionne la gestion des sessions pour ces applications et quelle étape est nécessaire pour libérer correctement les ressources sous RStudio ?"
  - "De quelle manière les utilisateurs peuvent-ils modifier les versions par défaut des modules chargés (comme RStudio, MLflow ou Tensorboard) avant leur lancement ?"
  - "Quelles sont les différences entre les environnements de bureau Mate et XFCE, et comment simplifient-ils l'accès par rapport à une configuration VNC traditionnelle ?"
  - "Quelles fonctionnalités le terminal natif de JupyterLab offre-t-il et comment faut-il utiliser les raccourcis de copier-coller pour éviter d'interrompre un processus en cours ?"
  - "Comment peut-on accéder aux interfaces graphiques d'applications spécifiques, telles que Julia ou la suite Ansys, qui ne sont pas chargées par défaut dans la session ?"
  - "Quelles sont les principales fonctionnalités et métriques que ce logiciel permet de suivre et de visualiser ?"
  - "Comment est-il possible de modifier la version par défaut de Tensorboard proposée par le système ?"
  - "Où peut-on consulter des informations supplémentaires pour apprendre à utiliser ce logiciel en détail ?"
  - "Quels sont les différents logiciels de la suite Ansys dont les lanceurs sont illustrés dans le document ?"
  - "Quelle interface alternative est spécifiquement proposée pour le logiciel Ansys Fluent ?"
  - "Comment l'utilisateur peut-il accéder à l'interface web d'Ansys Fluent ?"
  - "Quels sont les logiciels listés dans le document qui exigent que l'utilisateur fournisse sa propre licence pour les utiliser ?"
  - "Quelle est la procédure commune décrite pour faire apparaître l'icône de lancement et démarrer l'interface graphique de ces logiciels via une session VNC ?"
  - "Où le mot de passe généré automatiquement pour se connecter à Ansys Fluent est-il sauvegardé ?"
  - "À quoi sert le logiciel Star-CCM+ de Siemens ?"
  - "Comment peut-on lancer l'interface graphique de Star-CCM+ sur le système ?"
  - "Quelle est la condition requise concernant la licence pour pouvoir utiliser ce logiciel ?"
  - "Comment doit-on procéder pour charger ou installer les paquets scientifiques nécessaires à l'exécution d'un notebook Python ?"
  - "Quelles sont les étapes à suivre pour convertir un notebook en script Python et le soumettre comme une tâche non interactive ?"
  - "Comment peut-on contourner l'erreur de système de fichiers en lecture seule (OSError [Errno 30]) lors de l'installation d'un paquet avec pip ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# JupyterLab

JupyterLab est l'interface utilisateur générale recommandée pour JupyterHub. À partir d'un serveur JupyterLab, vous pouvez gérer vos fichiers et vos répertoires distants et lancer des applications Jupyter comme un terminal, des notebooks (Python 3), RStudio et un bureau Linux.

Vous pouvez ajouter vos propres noyaux (*kernels*) qui seront affichés comme des applications. Pour configurer ces noyaux, voir [Ajouter des noyaux](jupyternotebook.md).

## Lancer JupyterLab

Il existe plusieurs façons de lancer JupyterLab.

Habituellement, on utilise [JupyterHub](jupyterhub.md#jupyterhub-sur-une-grappe), mais des sites ont récemment déployé Open OnDemand, ce qui permet parfois de lancer l'interface principale. Le tableau suivant indique si l'interface JupyterLab disponible possède ou non toutes les fonctionnalités. S'il existe un lien, il renvoie au serveur JupyterHub ou Open OnDemand de la grappe.

| Grappe    | JupyterHub (Disponible)                                  | JupyterHub (Toutes les fonctionnalités) | Open OnDemand (Disponible)                                                               | Open OnDemand (JupyterLab) | Open OnDemand (Toutes les fonctionnalités) |
| :-------- | :------------------------------------------------------- | :-------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------- | :------------------------------------------ |
| Fir       | [oui](https://jupyterhub.fir.alliancecan.ca/)            | oui                                     | non                                                                                      | non                        | non                                         |
| Killarney | non                                                      | non                                     | non                                                                                      | non                        | non                                         |
| Narval    | [oui](https://jupyterhub.narval.alliancecan.ca/)         | oui                                     | non                                                                                      | non                        | non                                         |
| Nibi      | non                                                      | non                                     | [oui](https://ondemand.sharcnet.ca/)                                                     | oui                        | oui                                         |
| Rorqual   | [oui](https://jupyterhub.rorqual.alliancecan.ca/)        | oui                                     | non                                                                                      | non                        | non                                         |
| tamIA     | non                                                      | non                                     | non                                                                                      | non                        | non                                         |
| Trillium  | non                                                      | non                                     | [oui](http://ondemand.scinet.utoronto.ca/), demander *Jupyter Lab + Alliance software extensions* | oui                        | oui                                         |
| Vulcan    | non                                                      | non                                     | [oui](https://vulcan.alliancecan.ca/)                                                    | oui                        | oui                                         |

Vous pouvez aussi lancer JupyterLab [l'installant vous-même dans un environnement virtuel](../getting-started/advanced_jupyter_configuration.md), mais cette méthode est déconseillée et vous ne bénéficierez pas des applications préconfigurées décrites ci-dessous.

## Interface JupyterLab

Lorsque vous ouvrez JupyterLab dans une de nos nouvelles grappes, un tableau de bord s'affiche avec des boutons pour lancer des applications. Par défaut, il y a Python 3.11, LibreQDA, Mate Desktop (VNC), OpenRefine, RStudio, VS Code et XFCE4 Desktop (VNC). Vous trouverez également des liens vers la collection Globus de la grappe, son portail de tâches, ainsi que des liens vers les pages de documentation. En chargeant des modules, de nouveaux boutons apparaîtront dans le tableau de bord (voir ci-dessous).

Dans la barre de menu du haut, notez que pour fermer votre session, vous pouvez le faire via le menu *Fichier*.
*   **Panneau de contrôle du Hub** : pour arrêter manuellement le serveur JupyterLab et la tâche sur la grappe; ceci est utile lorsque vous souhaitez démarrer un nouveau serveur JupyterLab avec plus ou moins de ressources.
*   **Déconnexion** : pour fermer la session, ce qui arrête également le serveur JupyterLab et la tâche sur la grappe.
La plupart des autres éléments du menu sont liés aux notebooks et aux applications Jupyter.

### Liste des outils (à gauche)

Sur le côté gauche se trouve la liste des outils qui vous permet de modifier le contenu du cadre de droite. Les plus importants sont :

#### **Explorateur de fichiers** (icône de dossier)

C'est ici que vous pouvez naviguer dans vos espaces /home, /project et /scratch. Il est également possible de l'utiliser pour importer des fichiers.

#### **Terminaux et noyaux actifs** (icône d'arrêt)

Cette option permet d'arrêter les sessions de noyau et de terminal.

#### **Tableaux de bord GPU** (icône de carte GPU)

Si votre tâche utilise des GPU, cette option vous donne accès à certaines options de surveillance des ressources.

#### **Modules logiciels**

C'est ici que vous pouvez charger ou décharger les [modules logiciels](../programming/available_software.md) disponibles dans notre environnement. Selon les modules chargés, des icônes redirigeant vers les [applications Jupyter](#applications-preconstruites) correspondantes apparaîtront sous l'onglet *Lanceur*. Par défaut, nous chargeons plusieurs modules pour vous donner accès aux outils de base.

Le champ de recherche permet de rechercher n'importe quel [module disponible](../programming/available_software.md) et d'afficher le résultat dans le sous-panneau *Modules disponibles*. Remarque : Certains modules sont masqués jusqu'au chargement de leurs dépendances. Nous vous recommandons de rechercher d'abord un module spécifique avec `module spider module_name` à partir d'un terminal.

Le sous-panneau suivant affiche la liste des modules chargés pour la session JupyterLab.

Le dernier sous-panneau affiche la liste des modules disponibles, semblable au résultat de `module avail`. En cliquant sur le nom d'un module, des informations détaillées s'affichent. En cliquant sur le lien *Charger*, le module est chargé et ajouté à la liste des modules chargés.

### Barre d'état (au bas)

*   Cliquez sur les icônes pour aller à l'outil **Terminaux et noyaux actifs**.

## Applications préconstruites

JupyterLab offre l'accès à un terminal, un IDE (bureau), une console Python et plusieurs options pour créer des fichiers texte brut et formatés (*markdown*). Nous ne présentons ici que les principales applications qui sont compatibles avec notre pile logicielle.

### Applications disponibles par défaut

Plusieurs modules logiciels sont chargés par défaut pour vous permettre d'y accéder sans aucune action supplémentaire.

#### Python

Un noyau Python, avec la version par défaut, est automatiquement chargé. Cela vous permet de démarrer automatiquement les notebooks Python.

Nous chargeons une version par défaut de Python, mais vous pouvez en utiliser une autre en chargeant une autre version des modules `ipython-kernel`.

Cet environnement Python n'est pas fourni avec la plupart des paquets préinstallés. Cependant, vous pouvez charger certains modules, comme `scipy-stack`, pour bénéficier de fonctionnalités supplémentaires.

Vous pouvez également installer des paquets Python directement dans l'environnement du notebook, en exécutant

`pip install --no-index package-name`

dans une cellule de votre notebook, puis en redémarrant votre noyau.

#### VS Code

VS Code (Visual Studio Code) est un éditeur de code initialement développé par Microsoft, mais qui est un standard ouvert sur lequel [code-server](https://github.com/coder/code-server) s'appuie pour rendre l'application accessible par n'importe quel navigateur.

La version que nous avons installée est livrée avec un grand nombre [d'extensions](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/blob/main/2023/code-server/code-server-4.101.2.eb#L27) préinstallées. Pour plus de détails, voir [Visual Studio Code](visual_studio_code.md).

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### LibreQDA

*[LibreQDA](https://aide.libreqda.org/)* est une application d'analyse qualitative, dérivée de [Taguette](https://www.taguette.org/).

Cette application permet de lancer une version mono-utilisateur du logiciel, utilisable pour l'analyse de texte.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### RStudio

[RStudio](https://posit.co/download/rstudio-desktop/) est un environnement de développement intégré principalement utilisé pour le langage [R](../software/r.md).

Nous chargeons une version par défaut du logiciel R, mais vous pouvez en utiliser une autre en chargeant une autre version des modules `rstudio-server`. Veuillez le faire **avant** de lancer RStudio, sinon vous devrez peut-être redémarrer JupyterLab.

Ceci ouvre ou ouvre de nouveau une interface RStudio dans un nouvel onglet du navigateur.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

!!! warning "Important : Fermeture de session RStudio"
    Notez que le simple fait de quitter RStudio ou de fermer les onglets RStudio et JupyterHub dans votre navigateur ne libère pas les ressources (CPU, mémoire, GPU) ni ne met fin à la tâche Slurm sous-jacente. **Veuillez fermer votre session via le menu `Fichier > Déconnexion` dans l'onglet du navigateur JupyterLab.**

#### MLflow

[MLflow](https://mlflow.org/) est une plateforme libre conçue pour aider les praticiens et les équipes d'apprentissage automatique à gérer la complexité du processus. MLflow se concentre sur le cycle de vie complet des projets d'apprentissage automatique, garantissant que chaque phase soit gérable, traçable et reproductible. Une version par défaut de MLflow est chargée, mais vous pouvez en utiliser une autre en chargeant le module `mlflow`. Consultez notre page MLflow pour plus d'informations sur l'utilisation de MLflow pour le suivi de vos expériences d'IA.

#### OpenRefine

[OpenRefine](https://openrefine.org/) est un outil puissant, gratuit et libre permettant de nettoyer les données désordonnées, de les transformer et de les enrichir pour leur apporter plus de valeur.

Il est couramment utilisé pour corriger les fautes de frappe dans les données d'enquête collectées manuellement.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### Tensorboard

[Tensorboard](https://www.tensorflow.org/tensorboard/) fournit la visualisation et les outils nécessaires à l'expérimentation en apprentissage automatique. TensorBoard est un outil permettant de réaliser les mesures et visualisations nécessaires au flux de travail d'apprentissage automatique. Il permet de suivre les métriques expérimentales telles que la perte et la précision, de visualiser le graphe du modèle, de projeter les plongements lexicaux dans un espace de dimension inférieure, et bien plus encore. Nous offrons par défaut une version de `tensorboard`, mais si un autre module est disponible, vous pouvez en modifier la version. Consultez [notre page wiki Tensorboard](../software/ai-ml/tensorboard.md) pour plus de détails sur l'utilisation de ce logiciel.

#### Bureau

Deux environnements de bureau différents sont disponibles par défaut : [Mate Desktop](https://mate-desktop.org/) et [XFCE Desktop](https://www.xfce.org/). Vous pouvez choisir celui qui vous convient. XFCE offre une interface utilisateur plus moderne, tandis que Mate est plus léger.
Ceux-ci ouvrent ou rouvrent une interface de bureau Linux distante dans un nouvel onglet de navigateur.

Cela est comme exécuter un [serveur VNC sur un nœud de calcul](vnc.md), puis à créer un [tunnel SSH](../getting-started/ssh_tunnelling.md) et enfin à utiliser un [client VNC](vnc.md). Avec JupyterLab, rien de tout cela n'est nécessaire.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### Terminal

JupyterLab vous permet également d'ouvrir une session de terminal native. Cela peut être utile pour exécuter des commandes bash, soumettre des tâches ou modifier des fichiers.

*   Le terminal exécute un shell (Bash) sur le nœud de calcul distant, sans la nécessité d'une connexion SSH.
*   Donne accès aux systèmes de fichiers distants (`/home`, `/project`, `/scratch`).
*   Permet de lancer des tâches de calcul.
*   Le terminal permet de copier-coller du texte.
*   Pour copier, sélectionnez le texte et appuyez sur Ctrl+C.

!!! tip "Copier/Coller dans le Terminal JupyterLab"
    Remarque : Généralement, Ctrl+C sert à envoyer un signal SIGINT à un processus en cours d'exécution ou à annuler la commande en cours. Pour obtenir ce comportement dans le terminal de JupyterLab, cliquez dessus pour désélectionner le texte avant d'appuyer sur Ctrl+C.

*   Pour coller, appuyez sur Ctrl+V.

#### Globus

Si [Globus](../getting-started/globus.md) est disponible sur la grappe que vous utilisez, une icône correspondante s'affichera. Cela ouvrira votre navigateur et la collection Globus correspondante.

#### Metrix

Si le portail de tâches Metrix est disponible sur la grappe que vous utilisez, une icône correspondante s'affichera, ouvrant une page qui montre les statistiques de votre tâche.

### Applications disponibles après le chargement d'un module

Plusieurs modules que nous fournissons rendent une icône de lancement d'application disponible lors de leur chargement, même si elles ne sont pas chargées par défaut.

#### Julia

Le chargement d'un module `ijulia-kernel` vous permettra d'ouvrir un notebook avec le langage Julia.

#### Suite Ansys

La suite Ansys propose plusieurs outils offrant une interface utilisateur graphique. Si vous chargez l'un des modules Ansys, une série d'icônes de lancement s'affichera, la plupart fonctionnant via une connexion VNC dans le navigateur.
Ces icônes correspondent aux applications Ansys CFX, Ansys Fluent, Ansys Mapdl et Ansys Workbench.
Ansys Fluent dispose également d'une interface web, accessible via une icône spécifique.
Notez qu'un mot de passe est requis pour se connecter à Ansys Fluent. Ce mot de passe est généré au lancement et enregistré dans votre dossier personnel, dans le fichier `$HOME/fluent_webserver_token`.

Notez que pour Ansys, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys](../software/ansys.md).

#### Ansys EDT

[Ansys EDT](https://www.ansys.com/products/electronics) est un module distinct. Charger le module `ansysedt` fera apparaître une icône de lancement correspondante.

Notez que pour Ansys EDT, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys EDT](../software/ansysedt.md).

#### COMSOL

[COMSOL](http://www.comsol.com) est un logiciel polyvalent pour modéliser des applications d'ingénierie.

Pour utiliser ce logiciel, vous devez détenir votre propre licence.

Charger un module `comsol` ajoutera une icône de lancement qui permet de démarrer l'interface utilisateur graphique de COMSOL via une session VNC. Consultez notre page [COMSOL](../software/comsol.md) pour plus de détails sur l'utilisation de ce logiciel.

#### Matlab

[MATLAB](https://www.mathworks.com/?s_tid=gn_logo) est disponible en chargeant un module `matlab`. Une icône de lancement sera ajoutée pour démarrer le logiciel via une session VNC. Notez que vous devrez fournir votre propre fichier de licence, comme expliqué sur notre page [MATLAB](../software/matlab.md).

#### NVidia Nsight Systems

[NVidia Nsight Systems](https://developer.nvidia.com/nsight-systems) est un outil d'analyse des performances développé principalement pour le profilage des GPU, mais qui permet également de profiler le code CPU.

Le chargement d'un module `cuda` ou `nvhpc` rend disponible une icône pour lancer l'interface utilisateur graphique dans une session VNC.

#### Octave

[GNU Octave](https://octave.org/) est un langage de programmation scientifique libre largement compatible avec MATLAB. Le chargement d'un module `octave` ajoute une icône pour lancer l'interface utilisateur graphique d'Octave via une session VNC. Consultez notre page sur Octave pour plus de détails sur l'utilisation de ce logiciel.

#### ParaView

[ParaView](https://www.paraview.org/) est un puissant logiciel libre de visualisation. Le chargement d'un module `paraview` ajoute une icône pour lancer l'interface utilisateur graphique ParaView via une session VNC. Consultez notre page [ParaView](../software/paraview.md) pour plus de détails sur l'utilisation de ce logiciel.

#### QGIS

[QGIS](https://qgis.org/) est un puissant logiciel libre de visualisation et de traitement de données de systèmes d'information géographique (SIG). Le chargement d'un module `qgis` ajoute une icône pour lancer l'interface graphique de QGIS via une session VNC. Consultez notre page QGIS pour plus de détails sur ce logiciel.

#### Star-CCM+

[Star-CCM+](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/) de Siemens est un logiciel commercial de simulation numérique pour la dynamique des fluides. Il est disponible en chargeant l'un des modules `starccm` ou `starccm-mixed`. Une icône sera ajoutée pour lancer l'interface graphique de Star-CCM+ via une session VNC. Comme pour tous les logiciels commerciaux, vous devrez fournir votre propre licence. Consultez notre page [Star-CCM+](../software/star-ccm.md) pour plus de détails sur l'utilisation de ce logiciel.

## Informations additionnelles sur l'exécution des notebooks

#### Notebook Python

Si votre notebook requiert l'un des paquets Python scientifiques suivants, avant de l'ouvrir, vous devez charger le module `scipy-stack` depuis l'outil JupyterLab *Modules logiciels* :
*   `ipython`, `ipython_genutils`, `ipykernel`, `ipyparallel`
*   `matplotlib`
*   `numpy`
*   `pandas`
*   `scipy`
*   Pour plus d'information, voir [Pile logicielle SciPy](../software/python.md)

!!! note "Installation de paquets Python"
    Remarque : Vous pouvez également installer les paquets nécessaires en exécutant, par exemple, la commande suivante dans une cellule : `pip install --no-index numpy`.
    Pour certains paquets (comme plotly, par exemple), vous devrez peut-être redémarrer le noyau du notebook avant d'importer le paquet.

L'installation des paquets dans l'environnement du noyau Python par défaut est temporaire, le temps de la session JupyterLab; vous devrez réinstaller ces paquets lors du prochain démarrage d'une nouvelle session JupyterLab. Pour un environnement Python persistant, vous devez configurer un **[noyau Python personnalisé](../getting-started/advanced_jupyter_configuration.md#noyau-python)**.

Pour ouvrir un notebook Python existant :
*   Retournez à l'**Explorateur de fichiers**.
*   Localisez le fichier `*.ipynb`.
*   Double-cliquez sur le fichier `*.ipynb`.
    *   Le notebook Python s'ouvre dans un nouvel onglet JupyterLab.
    *   Un nouveau noyau IPython démarrera en arrière-plan pour le notebook.

Pour ouvrir un notebook Python dans le répertoire courant de l'**Explorateur de fichiers** :
*   Cliquez sur le bouton **Python 3.x** sous la section **Notebook**;
    *   ceci ouvre un nouveau notebook Python 3 dans un nouvel onglet JupyterLab;
    *   un nouveau noyau IPython démarrera en arrière-plan pour le notebook.

### Exécuter des notebooks en scripts Python

1.  À partir de la console ou dans une nouvelle cellule d'un notebook, installez `nbconvert` :

    ```bash
    !pip install --no-index nbconvert
    ```

2.  Convertissez vos notebooks en scripts Python.

    ```bash
    !jupyter nbconvert --to python my-current-notebook.ipynb
    ```

3.  Créez [une tâche non interactive](../running-jobs/running_jobs.md) et soumettez-la.

Dans le script de soumission, exécutez le notebook converti avec

```bash
python mynotebook.py
```

et soumettez votre tâche non interactive avec

```bash
sbatch my-submit.sh
```

## Dépannage

### Message d'erreur : *ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system*

Ce message peut survenir dans un notebook quand pip essaie de désinstaller un paquet dans un emplacement en lecture seule.

Dans plusieurs cas, vous pouvez utiliser la commande suivante dans la cellule du notebook :

```bash
pip install --no-index --ignore-installed <package>
```

Cette commande installe le paquet qui est la source de l'erreur, mais **ne réussit pas toujours** pour certains paquets comme `pyarrow`, `opencv`, `mpi4py`.

Si vous avez des questions, contactez [le soutien technique](../support/technical_support.md).