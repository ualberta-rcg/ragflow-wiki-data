---
title: "JupyterLab/fr"
slug: "jupyterlab"
lang: "fr"

source_wiki_title: "JupyterLab/fr"
source_hash: "ce517b54ddadadff760e408663580ac9"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:20:29.145956+00:00"

tags:
  []

keywords:
  - "interface web"
  - "importer des fichiers"
  - "Ansys Mapdl"
  - "Liste des outils"
  - "tensorboard"
  - "Ansys Workbench"
  - "interface utilisateur graphique"
  - "noyau Python"
  - "simulation numérique"
  - "VS Code"
  - "LibreQDA"
  - "licence"
  - "code-server"
  - "OpenRefine"
  - "graphe du modèle"
  - "nbconvert"
  - "grappes"
  - "Visual Studio Code"
  - "Tensorboard"
  - "Environnement de bureau"
  - "Notebook Python"
  - "démarrage de session"
  - "File Browser"
  - "naviguer dans vos espaces"
  - "module"
  - "MLflow"
  - "Ansys CFX"
  - "extensions préinstallées"
  - "scipy-stack"
  - "logiciel commercial"
  - "apprentissage automatique"
  - "dynamique des fluides"
  - "Applications préconstruites"
  - "icône de lancement"
  - "applications Jupyter"
  - "interface utilisateur"
  - "Terminal"
  - "métriques expérimentales"
  - "Noyau Python"
  - "session VNC"
  - "Ansys Fluent"
  - "Star-CCM+"
  - "navigateur"
  - "Modules logiciels"
  - "JupyterHub"
  - "Modules"
  - "plongements lexicaux"
  - "RStudio"
  - "Icônes de lancement"
  - "JupyterLab"

questions:
  - "Quelles sont les principales applications et fonctionnalités offertes par l'interface JupyterLab ?"
  - "Comment peut-on lancer JupyterLab et quelles sont les différences de disponibilité selon les grappes de calcul ?"
  - "De quelle manière l'interface permet-elle de gérer sa session, ses ressources et ses fichiers distants ?"
  - "Comment fonctionne la gestion des modules logiciels (recherche, chargement et affichage) dans l'interface JupyterLab ?"
  - "Quelles sont les méthodes permettant de personnaliser l'environnement Python, notamment pour changer de version ou installer de nouveaux paquets ?"
  - "Quelles sont les caractéristiques et les particularités de l'application préconstruite VS Code accessible depuis le navigateur ?"
  - "À quoi sert la liste des outils située sur le côté gauche de l'interface JupyterLab ?"
  - "Comment peut-on identifier visuellement l'outil \"File Browser\" dans cette liste ?"
  - "Quels espaces de stockage et quelles actions sont accessibles via le \"File Browser\" ?"
  - "Comment l'application code-server est-elle rendue accessible aux utilisateurs ?"
  - "Que contient par défaut la version spécifique de code-server qui a été installée ?"
  - "Quel est le temps d'attente maximal estimé pour le démarrage d'une nouvelle session ?"
  - "Quelles sont les fonctions principales des différents outils (LibreQDA, RStudio, MLflow, OpenRefine, Tensorboard) décrits dans le texte ?"
  - "Comment fonctionne la gestion des sessions pour ces applications et quelle est la procédure exacte pour fermer RStudio afin de libérer les ressources ?"
  - "De quelle manière est-il possible de modifier la version par défaut de certains modules logiciels (tels que RStudio, MLflow ou Tensorboard) avant leur lancement ?"
  - "Quelles sont les différences entre les environnements de bureau virtuels disponibles (Mate et XFCE) et comment fonctionnent-ils directement dans le navigateur ?"
  - "Quelles actions peuvent être effectuées à l'aide du terminal natif intégré à JupyterLab et quelle est la particularité de l'utilisation du raccourci Ctrl+C dans ce contexte ?"
  - "Comment les utilisateurs peuvent-ils accéder à des outils et applications spécifiques supplémentaires, tels que Globus, Metrix, Julia ou la suite Ansys ?"
  - "Quelles sont les principales fonctionnalités et métriques expérimentales que ce logiciel permet de suivre et de visualiser ?"
  - "Comment l'utilisateur peut-il modifier la version par défaut de Tensorboard fournie par le système ?"
  - "Où peut-on consulter des informations supplémentaires et détaillées sur l'utilisation de ce logiciel ?"
  - "Quels sont les différents lanceurs de logiciels de la suite Ansys présentés dans le document ?"
  - "Lequel de ces logiciels propose spécifiquement une interface web ?"
  - "Comment l'utilisateur peut-il accéder à cette interface web mentionnée dans le texte ?"
  - "Quelle action permet de faire apparaître l'icône de lancement des différents logiciels pour les démarrer via une session VNC ?"
  - "Quelle condition indispensable concernant les licences est exigée pour l'utilisation des logiciels commerciaux tels qu'Ansys, COMSOL, MATLAB et StarCCM+ ?"
  - "Où est enregistré le fichier contenant le mot de passe généré automatiquement et requis pour se connecter à Ansys Fluent ?"
  - "Qu'est-ce que le logiciel Star-CCM+ et quel est son domaine d'application principal ?"
  - "Quelles sont les étapes techniques pour charger et lancer l'interface graphique du logiciel via une session VNC ?"
  - "Quelle condition spécifique liée à la licence les utilisateurs doivent-ils remplir pour pouvoir utiliser ce programme ?"
  - "Comment configurer un environnement persistant pour éviter de réinstaller les paquets Python à chaque nouvelle session JupyterLab ?"
  - "Quelles sont les étapes pour convertir un notebook en script Python et le soumettre en tant que tâche non interactive ?"
  - "Quelle commande permet de contourner l'erreur de système de fichiers en lecture seule (OSError [Errno 30]) lors de l'installation d'un paquet avec pip ?"
  - "Comment configurer un environnement persistant pour éviter de réinstaller les paquets Python à chaque nouvelle session JupyterLab ?"
  - "Quelles sont les étapes pour convertir un notebook en script Python et le soumettre en tant que tâche non interactive ?"
  - "Quelle commande permet de contourner l'erreur de système de fichiers en lecture seule (OSError [Errno 30]) lors de l'installation d'un paquet avec pip ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# JupyterLab
JupyterLab est l'interface utilisateur générale recommandée pour JupyterHub.
À partir d'un serveur JupyterLab, vous pouvez gérer vos fichiers et vos répertoires distants et lancer des applications Jupyter comme un terminal, des notebooks (Python 3), RStudio et un bureau Linux.

Vous pouvez ajouter vos propres noyaux (*kernels*) qui seront affichés comme des applications. Pour configurer ces noyaux, voir [Ajouter des noyaux](jupyternotebook.md#ajouter-des-noyaux).

## Lancer JupyterLab
Il existe plusieurs façons de lancer JupyterLab.

Habituellement, on utilise [JupyterHub](jupyterhub.md#jupyterhub-sur-une-grappe), mais des sites ont récemment déployé Open OnDemand, ce qui permet parfois de lancer l'interface montrée un peu plus loin. Le tableau suivant indique si l'interface JupyterLab disponible possède ou non toutes les fonctionnalités. S'il existe un lien, il renvoie au serveur JupyterHub ou Open OnDemand de la grappe.

| Grappe    | **JupyterHub**                           |                      | **Open OnDemand**                                                          |                  |                      |
| :-------- | :--------------------------------------- | :------------------- | :------------------------------------------------------------------------- | :--------------- | :------------------- |
|           | Disponible                               | Toutes les fonctionnalités | Disponible                                                                 | JupyterLab       | Toutes les fonctionnalités |
| Fir       | [oui](https://jupyterhub.fir.alliancecan.ca/) |                      | non                                                                        |                  |                      |
| Killarney | non                                      |                      | non                                                                        |                  |                      |
| Narval    | [oui](https://jupyterhub.narval.alliancecan.ca/) |                      | non                                                                        |                  |                      |
| Nibi      | non                                      |                      | [oui](https://ondemand.sharcnet.ca/)                                       |                  |                      |
| Rorqual   | [oui](https://jupyterhub.rorqual.alliancecan.ca/) |                      | non                                                                        |                  |                      |
| tamIA     | non                                      |                      | non                                                                        |                  |                      |
| Trillium  | non                                      |                      | [oui](http://ondemand.scinet.utoronto.ca/), demander *Jupyter Lab + Alliance software extensions* |                  |                      |
| Vulcan    | non                                      |                      | [oui](https://vulcan.alliancecan.ca/)                                      |                  |                      |

Vous pouvez aussi lancer JupyterLab [l'installant vous-même dans un environnement virtuel](../getting-started/advanced_jupyter_configuration.md), mais cette méthode est déconseillée et vous ne bénéficierez pas des applications préconfigurées décrites ci-dessous.

## Interface JupyterLab

Lorsque vous ouvrez JupyterLab dans une de nos nouvelles grappes, un tableau de bord s'affiche avec des boutons pour lancer des applications. Par défaut, il y a Python 3.11, LibreQDA, Mate Desktop (VNC), OpenRefine, RStudio, VS Code et XFCE4 Desktop (VNC). Vous trouverez également des liens vers la collection Globus de la grappe, son portail de tâches, ainsi que des liens vers les pages de documentation. En chargeant des modules, de nouveaux boutons apparaîtront dans le tableau de bord (voir ci-dessous).

Dans la barre de menu du haut, notez que pour fermer votre session, vous pouvez le faire via le menu *Fichier*.
*   *Panneau de contrôle du Hub* : pour arrêter manuellement le serveur JupyterLab et la tâche sur la grappe; ceci est utile lorsque vous souhaitez démarrer un nouveau serveur JupyterLab avec plus ou moins de ressources.
*   *Déconnexion* : pour fermer la session, ce qui arrête également le serveur JupyterLab et la tâche sur la grappe.
La plupart des autres éléments du menu sont liés aux notebooks et aux applications Jupyter.

### Liste des outils (à gauche)
Sur le côté gauche se trouve la liste des outils qui vous permet de modifier le contenu du cadre de droite. Les plus importants sont :

#### Navigateur de fichiers (*File Browser*) (icône d'un dossier)
C'est ici que vous pouvez naviguer dans vos espaces `/home`, `/project` et `/scratch`. Il est également possible de l'utiliser pour importer des fichiers.

#### Terminaux et noyaux en cours d'exécution (*Running Terminals and Kernels*) (icône d'arrêt)
Cette option permet d'arrêter les sessions de noyau et de terminal.

#### Tableaux de bord GPU (*GPU Dashboards*) (icône de carte GPU)
Si votre tâche utilise des GPU, cette option vous donne accès à certaines options de surveillance des ressources.

#### Modules logiciels (*Software Modules*)
C'est ici que vous pouvez charger ou décharger les [modules logiciels](../programming/available_software.md) disponibles dans notre environnement. Selon les modules chargés, des icônes redirigeant vers les [applications Jupyter](jupyterlab.md#applications-preconstruites) correspondantes apparaîtront sous l'onglet *Lanceur*. Par défaut, nous chargeons plusieurs modules pour vous donner accès aux outils de base.

Le champ de recherche permet de rechercher n'importe quel [module disponible](../programming/available_software.md) et d'afficher le résultat dans le sous-panneau *Modules disponibles*. Remarque : Certains modules sont masqués jusqu'au chargement de leurs dépendances. Nous vous recommandons de rechercher d'abord un module spécifique avec `module spider module_name` à partir d'un terminal.

Le sous-panneau suivant affiche la liste des modules chargés pour la session JupyterLab.

Le dernier sous-panneau affiche la liste des modules disponibles, semblable au résultat de `module avail`. En cliquant sur le nom d'un module, des informations détaillées s'affichent. En cliquant sur le lien *Charger*, le module est chargé et ajouté à la liste des modules chargés.

### Barre d'état (au bas)

*   Cliquez sur les icônes pour aller à l'outil *Terminaux et noyaux en cours d'exécution*.

## Applications préconstruites

JupyterLab offre l'accès à un terminal, un IDE (bureau), une console Python et plusieurs options pour créer des fichiers texte brut et formatés (*markdown*). Nous ne présentons ici que les principales applications qui sont compatibles avec notre pile logicielle.

### Applications disponibles par défaut
Plusieurs modules logiciels sont chargés par défaut pour vous permettre d'y accéder sans aucune action supplémentaire.

#### Python
Un noyau Python, avec la version par défaut, est automatiquement chargé. Cela vous permet de démarrer automatiquement les notebooks Python à l'aide de l'icône.

Nous chargeons une version par défaut de Python, mais vous pouvez en utiliser une autre en chargeant une autre version des modules `ipython-kernel`.

Cet environnement Python n'est pas fourni avec la plupart des paquets préinstallés. Cependant, vous pouvez charger certains modules, comme `scipy-stack`, pour bénéficier de fonctionnalités supplémentaires.

Vous pouvez également installer des paquets Python directement dans l'environnement du notebook, en exécutant

```bash
pip install --no-index package-name
```

dans une cellule de votre notebook, puis en redémarrant votre noyau.

#### VS Code
VS Code (Visual Studio Code) est un éditeur de code initialement développé par Microsoft, mais qui est un standard ouvert sur lequel [code-server](https://github.com/coder/code-server) s'appuie pour rendre l'application accessible par n'importe quel navigateur.

La version que nous avons installée est livrée avec un grand nombre [d'extensions](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/blob/main/2023/code-server/code-server-4.101.2.eb#L27) préinstallées. Pour plus de détails, voir [Visual Studio Code](visual_studio_code.md).

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### LibreQDA
[*LibreQDA*](https://aide.libreqda.org/) est une application d'analyse qualitative, dérivée de [Taguette](https://www.taguette.org/).

Cette icône permet de lancer une version mono-utilisateur du logiciel, utilisable pour l'analyse de texte.

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
    Notez que le simple fait de quitter RStudio ou de fermer les onglets RStudio et JupyterHub dans votre navigateur ne libère pas les ressources (CPU, mémoire, GPU) ni ne met fin à la tâche Slurm sous-jacente. **Veuillez fermer votre session via le menu `Fichier > Déconnexion` dans l'onglet du navigateur JupyterLab**.

#### MLflow
[MLflow](https://mlflow.org/) est une plateforme libre conçue pour aider les praticiens et les équipes d'apprentissage automatique à gérer la complexité du processus. MLflow se concentre sur le cycle de vie complet des projets d'apprentissage automatique, garantissant que chaque phase soit gérable, traçable et reproductible. Une version par défaut de MLflow est chargée, mais vous pouvez en utiliser une autre en chargeant le module `mlflow`. Consultez notre page [MLflow](mlflow.md) pour plus d'informations sur l'utilisation de MLflow pour le suivi de vos expériences d'IA.

#### OpenRefine
[OpenRefine](https://openrefine.org/) est un outil puissant, gratuit et libre permettant de nettoyer les données désordonnées, de les transformer et de les enrichir pour leur apporter plus de valeur.

Il est couramment utilisé pour corriger les fautes de frappe dans les données d'enquête collectées manuellement.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### Tensorboard
[Tensorboard](https://www.tensorflow.org/tensorboard) fournit la visualisation et les outils nécessaires à l'expérimentation en apprentissage automatique. TensorBoard est un outil permettant de réaliser les mesures et visualisations nécessaires au flux de travail d'apprentissage automatique. Il permet de suivre les métriques expérimentales telles que la perte et la précision, de visualiser le graphe du modèle, de projeter les plongements lexicaux dans un espace de dimension inférieure, et bien plus encore. Nous offrons par défaut une version de `tensorboard`, mais si un autre module est disponible, vous pouvez en modifier la version. Consultez [notre page wiki Tensorboard](../software/ai-ml/tensorboard.md) pour plus de détails sur l'utilisation de ce logiciel.

#### Bureau (*Desktop*)
Deux environnements de bureau différents sont disponibles par défaut : [Mate Desktop](https://mate-desktop.org/) et [XFCE Desktop](https://www.xfce.org/). Vous pouvez choisir celui qui vous convient. XFCE offre une interface utilisateur plus moderne, tandis que Mate est plus léger.
Ceux-ci ouvrent ou rouvrent une interface de bureau Linux distante dans un nouvel onglet de navigateur.

Cela est comme exécuter un [serveur VNC sur un nœud de calcul](vnc.md), puis à créer un [tunnel SSH](../getting-started/ssh_tunnelling.md) et enfin à utiliser un [client VNC](vnc.md). Avec JupyterLab, rien de tout cela n'est nécessaire.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### Terminal
JupyterLab vous permet également d'ouvrir une session de terminal native. Cela peut être utile pour exécuter des commandes bash, soumettre des tâches ou modifier des fichiers.

Le terminal exécute un shell (Bash) sur le nœud de calcul distant, sans la nécessité d'une connexion SSH.

*   Donne accès aux systèmes de fichiers distants (`/home`, `/project`, `/scratch`).
*   Permet de lancer des tâches de calcul.
*   Le terminal permet de copier-coller du texte.

Pour copier, sélectionnez le texte et appuyez sur Ctrl+C.

!!! note "Note sur Ctrl+C"
    Généralement, Ctrl+C sert à envoyer un signal SIGINT à un processus en cours d'exécution ou à annuler la commande en cours. Pour obtenir ce comportement dans le terminal de JupyterLab, cliquez dessus pour désélectionner le texte avant d'appuyer sur Ctrl+C.

Pour coller, appuyez sur Ctrl+V.

#### Globus
Si [Globus](../getting-started/globus.md) est disponible sur la grappe que vous utilisez, vous verrez peut-être cette icône. Cela ouvrira votre navigateur et la collection Globus correspondante.

#### Metrix
Si le [portail de tâches Metrix](portail.md) est disponible sur la grappe que vous utilisez, cette icône ouvrira une page qui montre les statistiques de votre tâche.

### Applications disponibles après le chargement d'un module
Plusieurs modules que nous fournissons affichent également une icône de lancement d'une application lors de son chargement, même si elles ne sont pas chargées par défaut.

#### Julia
Le chargement d'un module `ijulia-kernel` vous permettra d'ouvrir un notebook avec le langage Julia.

#### Suite Ansys
La suite Ansys propose plusieurs outils offrant une interface utilisateur graphique. Si vous chargez l'un des modules Ansys, vous accéderez à une série d'icônes de lancement, la plupart fonctionnant via une connexion VNC dans le navigateur.

Notez qu'un mot de passe est requis pour se connecter à Ansys Fluent. Ce mot de passe est généré au lancement et enregistré dans votre dossier personnel, dans le fichier `$HOME/fluent_webserver_token`.

!!! tip "Licence Ansys"
    Notez que pour Ansys, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys](../software/ansys.md).

#### Ansys EDT
[Ansys EDT](https://www.ansys.com/products/electronics) est un module distinct. Charger le module `ansysedt` fera apparaître l'icône de lancement correspondante.

!!! tip "Licence Ansys EDT"
    Notez que pour Ansys EDT, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys EDT](../software/ansysedt.md).

#### COMSOL
[COMSOL](http://www.comsol.com) est un logiciel polyvalent pour modéliser des applications d'ingénierie.

Pour utiliser ce logiciel, vous devez détenir votre propre licence.

Charger un module `comsol` ajoutera une icône de lancement permettant de démarrer l'interface utilisateur graphique de COMSOL via une session VNC. Consultez notre page [COMSOL](../software/comsol.md) pour plus de détails sur l'utilisation de ce logiciel.

#### Matlab
[MATLAB](https://www.mathworks.com/?s_tid=gn_logo) est disponible en chargeant un module `matlab`, ce qui ajoutera une icône de lancement pour démarrer le logiciel via une session VNC. Notez que vous devrez fournir votre propre fichier de licence, comme expliqué sur notre page [MATLAB](../software/matlab.md).

#### NVidia Nsight Systems
[NVidia Nsight Systems](https://developer.nvidia.com/nsight-systems) est un outil d'analyse des performances développé principalement pour le profilage des GPU, mais qui permet également de profiler le code CPU.
Le chargement d'un module `cuda` ou `nvhpc` crée une icône pour lancer l'interface utilisateur graphique dans une session VNC.

#### Octave
[GNU Octave](https://octave.org/) est un langage de programmation scientifique libre largement compatible avec MATLAB. Le chargement d'un module `octave` ajoute une icône pour lancer l'interface utilisateur graphique d'Octave via une session VNC. Consultez notre page sur [Octave](octave.md) pour plus de détails sur l'utilisation de ce logiciel.

#### ParaView
[ParaView](https://www.paraview.org/) est un puissant logiciel libre de visualisation. Le chargement d'un module `paraview` ajoute une icône pour lancer l'interface utilisateur graphique ParaView via une session VNC. Consultez notre page [ParaView](../software/paraview.md) pour plus de détails sur l'utilisation de ce logiciel.

#### QGIS
[QGIS](https://qgis.org/) est un puissant logiciel libre de visualisation et de traitement de données de systèmes d'information géographique (SIG). Le chargement d'un module `qgis` ajoute une icône pour lancer l'interface graphique de QGIS via une session VNC. Consultez notre page [QGIS](qgis.md) pour plus de détails sur ce logiciel.

#### StarCCM+
[Star-CCM+](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/) de Siemens est un logiciel commercial de simulation numérique pour la dynamique des fluides. Il est disponible en chargeant l'un des modules `starccm` ou `starccm-mixed`, qui ajoute une icône pour lancer l'interface graphique de StarCCM+ via une session VNC. Comme pour tous les logiciels commerciaux, vous devrez fournir votre propre licence. Consultez notre page [Star-CCM+](star-ccm+.md) pour plus de détails sur l'utilisation de ce logiciel.

## Informations additionnelles sur l'exécution des notebooks

#### Notebook Python
Si votre notebook requiert l'un des paquets Python scientifiques suivants, avant de l'ouvrir, vous devez charger le module `scipy-stack` depuis l'outil JupyterLab *Modules logiciels* :
*   `ipython`, `ipython_genutils`, `ipykernel`, `ipyparallel`
*   `matplotlib`
*   `numpy`
*   `pandas`
*   `scipy`
*   Pour plus d'information, voir [Pile logicielle SciPy](../software/python.md#pile-logicielle-scipy)

!!! note "Installation de paquets Python"
    Vous pouvez également installer les paquets nécessaires en exécutant, par exemple, la commande suivante dans une cellule : `pip install --no-index numpy`.
    Pour certains paquets (comme plotly, par exemple), vous devrez peut-être redémarrer le noyau du notebook avant d'importer le paquet.
    L'installation des paquets dans l'environnement du noyau Python par défaut est temporaire, le temps de la session JupyterLab; vous devrez réinstaller ces paquets lors du prochain démarrage d'une nouvelle session JupyterLab. Pour un environnement Python persistant, vous devez configurer un **[noyau Python personnalisé](../getting-started/advanced_jupyter_configuration.md#noyau-python)**.

Pour ouvrir un notebook Python existant :
*   Retournez au *Navigateur de fichiers*.
*   Localisez le fichier `*.ipynb`.
*   Double-cliquez sur le fichier `*.ipynb`.
    *   Le notebook Python s'ouvre dans un nouvel onglet JupyterLab.
    *   Un nouveau noyau IPython démarrera en arrière-plan pour le notebook.

Pour ouvrir un notebook Python dans le répertoire courant du *Navigateur de fichiers* :
*   Cliquez sur le bouton *Python 3.x* sous la section *Notebook*;
    *   ceci ouvre un nouveau notebook Python 3 dans un nouvel onglet JupyterLab;
    *   un nouveau noyau IPython démarrera en arrière-plan pour le notebook.

### Exécuter des notebooks en scripts Python
1.  À partir de la console ou dans une nouvelle cellule d'un notebook, installez `nbconvert` :
    ```bash
    pip install --no-index nbconvert
    ```

2.  Convertissez vos notebooks en scripts Python.
    ```bash
    jupyter nbconvert --to python my-current-notebook.ipynb
    ```

3.  Créez [une tâche non interactive](../running-jobs/running_jobs.md#soumettre-des-taches-avec-sbatch) et soumettez-la.

Dans le script de soumission, exécutez le notebook converti avec
```bash
python mynotebook.py
```

et soumettez votre tâche non interactive avec
```bash
sbatch my-submit.sh
```

# Dépannage
## Message *ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system*
Ce message peut survenir dans un notebook quand pip essaie de désinstaller un paquet dans un emplacement en lecture seule.

Dans plusieurs cas, vous pouvez utiliser la commande suivante dans la cellule du notebook :
```bash
pip install --no-index --ignore-installed <package>
```
Cette commande installe le paquet qui est la source de l'erreur, mais **ne réussit pas toujours** pour certains paquets comme `pyarrow`, `opencv`, `mpi4py`.

Si vous avez des questions, contactez [le soutien technique](../support/technical_support.md).