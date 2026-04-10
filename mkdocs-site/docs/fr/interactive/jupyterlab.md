---
title: "JupyterLab/fr"
slug: "jupyterlab"
lang: "fr"

source_wiki_title: "JupyterLab/fr"
source_hash: "ce517b54ddadadff760e408663580ac9"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:42:30.257204+00:00"

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

# JupyterLab

JupyterLab est l'interface utilisateur générale recommandée pour JupyterHub. À partir d'un serveur JupyterLab, vous pouvez gérer vos fichiers et vos répertoires distants et lancer des applications Jupyter comme un terminal, des calepins (Python 3), RStudio et un bureau Linux.

Vous pouvez ajouter vos propres noyaux (kernels) qui seront affichés comme des applications. Pour configurer ces noyaux, voir [Ajouter des noyaux](jupyter-notebook.md#ajouter-des-noyaux).

## Lancer JupyterLab

Il existe plusieurs façons de lancer JupyterLab.

Habituellement, on utilise [JupyterHub](jupyterhub.md#jupyterhub-sur-une-grappe), mais des sites ont récemment déployé Open OnDemand, ce qui permet parfois de lancer l'interface montrée un peu plus loin. Le tableau suivant indique si l'interface JupyterLab disponible possède ou non toutes les fonctionnalités. S'il existe un lien, il renvoie au serveur JupyterHub ou Open OnDemand de la grappe.

| Grappe    | JupyterHub (Dispo) | JupyterHub (Fonctionnalités complètes) | Open OnDemand (Dispo) | Open OnDemand (JupyterLab)              | Open OnDemand (Fonctionnalités complètes) |
| :-------- | :----------------- | :----------------------------- | :-------------------- | :-------------------------------------- | :----------------------------- |
| Fir       | [oui](https://jupyterhub.fir.alliancecan.ca/) | oui | non                   |                                         |                                |
| Killarney | non                |                                | non                   |                                         |                                |
| Narval    | [oui](https://jupyterhub.narval.alliancecan.ca/) | oui | non                   |                                         |                                |
| Nibi      | non                |                                | [oui](https://ondemand.sharcnet.ca/) |                                         |                                |
| Rorqual   | [oui](https://jupyterhub.rorqual.alliancecan.ca/) | oui | non                   |                                         |                                |
| tamIA     | non                |                                | non                   |                                         |                                |
| Trillium  | non                |                                | [oui](http://ondemand.scinet.utoronto.ca/) | demander *Jupyter Lab + Alliance software extensions* | oui                            |
| Vulcan    | non                |                                | [oui](https://vulcan.alliancecan.ca/) |                                         |                                |

!!! warning "Méthode déconseillée"
    Vous pouvez aussi lancer JupyterLab [l'installant vous-même dans un environnement virtuel](advanced-jupyter-configuration.md), mais cette méthode est déconseillée et vous ne bénéficierez pas des applications préconfigurées décrites ci-dessous.

## Interface JupyterLab

Lorsque vous ouvrez JupyterLab dans une de nos nouvelles grappes, un tableau de bord s'affiche avec des boutons pour lancer des applications. Par défaut, il y a Python 3.11, LibreQDA, Mate Desktop (VNC), OpenRefine, RStudio, VS Code et XFCE4 Desktop (VNC). Vous trouverez également des liens vers la collection Globus de la grappe, son portail de tâches, ainsi que des liens vers les pages de documentation. En chargeant des modules, de nouveaux boutons apparaîtront dans le tableau de bord (voir ci-dessous).

Dans la barre de menu du haut, notez que pour fermer votre session, vous pouvez le faire via le menu *Fichier*.

*   *Panneau de contrôle du Hub* : pour arrêter manuellement le serveur JupyterLab et la tâche sur la grappe; ceci est utile lorsque vous souhaitez démarrer un nouveau serveur JupyterLab avec plus ou moins de ressources.
*   *Déconnexion* : pour fermer la session, ce qui arrête également le serveur JupyterLab et la tâche sur la grappe.

La plupart des autres éléments du menu sont liés aux calepins et aux applications Jupyter.

### Liste des outils (à gauche)

Sur le côté gauche se trouve la liste des outils qui vous permet de modifier le contenu du cadre de droite. Les plus importants sont :

#### Explorateur de fichiers (icône de dossier)

C'est ici que vous pouvez naviguer dans vos espaces `/home`, `/project` et `/scratch`. Il est également possible de l'utiliser pour importer des fichiers.

#### Terminaux et noyaux en cours d'exécution (icône d'arrêt)

Cette option permet d'arrêter les sessions de noyau et de terminal.

#### Tableaux de bord GPU (icône de carte graphique)

Si votre tâche utilise des GPU, cette option vous donne accès à certaines options de surveillance des ressources.

#### Modules logiciels

C'est ici que vous pouvez charger ou décharger les [modules logiciels](available-software.md) disponibles dans notre environnement. Selon les modules chargés, des icônes redirigeant vers les [applications Jupyter](#applications-preconfigurees) correspondantes apparaîtront sous l'onglet *Lanceur*. Par défaut, nous chargeons plusieurs modules pour vous donner accès aux outils de base.

Le champ de recherche permet de rechercher n'importe quel [module disponible](available-software.md) et d'afficher le résultat dans le sous-panneau *Modules disponibles*.

!!! note "Remarque"
    Certains modules sont masqués jusqu'au chargement de leurs dépendances. Nous vous recommandons de rechercher d'abord un module spécifique avec `module spider module_name` à partir d'un terminal.

Le sous-panneau suivant affiche la liste des modules chargés pour la session JupyterLab.

Le dernier sous-panneau affiche la liste des modules disponibles, semblable au résultat de `module avail`. En cliquant sur le nom d'un module, des informations détaillées s'affichent. En cliquant sur le lien *Charger*, le module est chargé et ajouté à la liste des modules chargés.

### Barre d'état (en bas)

*   Cliquez sur les icônes pour aller à l'outil *Terminaux et noyaux en cours d'exécution*.

## Applications préconfigurées

JupyterLab offre l'accès à un terminal, un IDE (bureau), une console Python et plusieurs options pour créer des fichiers texte brut et formatés (markdown). Nous ne présentons ici que les principales applications qui sont compatibles avec notre pile logicielle.

### Applications disponibles par défaut

Plusieurs modules logiciels sont chargés par défaut pour vous permettre d'y accéder sans aucune action supplémentaire.

#### Python

Un noyau Python, avec la version par défaut, est automatiquement chargé. Cela vous permet de démarrer automatiquement les calepins Python à l'aide de l'icône.

Nous chargeons une version par défaut de Python, mais vous pouvez en utiliser une autre en chargeant une autre version des modules `ipython-kernel`.

Cet environnement Python n'est pas fourni avec la plupart des paquets préinstallés. Cependant, vous pouvez charger certains modules, comme `scipy-stack`, pour bénéficier de fonctionnalités supplémentaires.

Vous pouvez également installer des paquets Python directement dans l'environnement du calepin, en exécutant

```bash
pip install --no-index package-name
```

dans une cellule de votre calepin, puis en redémarrant votre noyau.

#### VS Code

VS Code (Visual Studio Code) est un éditeur de code initialement développé par Microsoft, mais qui est un standard ouvert sur lequel [code-server](https://github.com/coder/code-server) s'appuie pour rendre l'application accessible par n'importe quel navigateur.

La version que nous avons installée est livrée avec un grand nombre [d'extensions](https://github.com/ComputeCanada/easybuild-easyconfigs-installed-avx2/blob/main/2023/code-server/code-server-4.101.2.eb#L27) préinstallées. Pour plus de détails, voir [Visual Studio Code](visual-studio-code.md).

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### LibreQDA

[LibreQDA](https://aide.libreqda.org/) est une application d'analyse qualitative, dérivée de [Taguette](https://www.taguette.org/).

Cette icône permet de lancer une version mono-utilisateur du logiciel, utilisable pour l'analyse de texte.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### RStudio

[RStudio](https://posit.co/download/rstudio-desktop/) est un environnement de développement intégré principalement utilisé pour le langage [R](r.md).

Nous chargeons une version par défaut du logiciel R, mais vous pouvez en utiliser une autre en chargeant une autre version des modules `rstudio-server`.

!!! warning
    Veuillez charger une autre version des modules `rstudio-server` **avant** de lancer RStudio, sinon vous devrez peut-être redémarrer JupyterLab.

Ceci ouvre ou ouvre de nouveau une interface RStudio dans un nouvel onglet du navigateur.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

!!! warning "Important"
    Le simple fait de quitter RStudio ou de fermer les onglets RStudio et JupyterHub dans votre navigateur ne libère pas les ressources (CPU, mémoire, GPU) ni ne met fin à la tâche Slurm sous-jacente. **Veuillez fermer votre session via le menu `Fichier > Déconnexion` dans l'onglet du navigateur JupyterLab.**

#### MLflow

[MLflow](https://mlflow.org/) est une plateforme libre conçue pour aider les praticiens et les équipes d'apprentissage automatique à gérer la complexité du processus. MLflow se concentre sur le cycle de vie complet des projets d'apprentissage automatique, garantissant que chaque phase soit gérable, traçable et reproductible. Une version par défaut de MLflow est chargée, mais vous pouvez en utiliser une autre en chargeant le module `mlflow`. Consultez notre page [MLflow](mlflow.md) pour plus d'informations sur l'utilisation de MLflow pour le suivi de vos expériences d'IA.

#### OpenRefine

[OpenRefine](https://openrefine.org/) est un outil puissant, gratuit et libre permettant de nettoyer les données désordonnées, de les transformer et de les enrichir pour leur apporter plus de valeur.

Il est couramment utilisé pour corriger les fautes de frappe dans les données d'enquête collectées manuellement.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### TensorBoard

[TensorBoard](https://www.tensorflow.org/tensorboard) fournit la visualisation et les outils nécessaires à l'expérimentation en apprentissage automatique. TensorBoard est un outil permettant de réaliser les mesures et visualisations nécessaires au flux de travail d'apprentissage automatique. Il permet de suivre les métriques expérimentales telles que la perte et la précision, de visualiser le graphe du modèle, de projeter les plongements lexicaux dans un espace de dimension inférieure, et bien plus encore. Nous offrons par défaut une version de `tensorboard`, mais si un autre module est disponible, vous pouvez en modifier la version. Consultez [notre page wiki TensorBoard](tensorboard.md) pour plus de détails sur l'utilisation de ce logiciel.

#### Bureau

Deux environnements de bureau différents sont disponibles par défaut : [Mate Desktop](https://mate-desktop.org/) et [XFCE Desktop](https://www.xfce.org/). Vous pouvez choisir celui qui vous convient. XFCE offre une interface utilisateur plus moderne, tandis que Mate est plus léger.
Ceux-ci ouvrent ou rouvrent une interface de bureau Linux distante dans un nouvel onglet de navigateur.

Cela est comme exécuter un [serveur VNC sur un nœud de calcul](vnc.md), puis à créer un [tunnel SSH](ssh-tunnelling.md) et enfin à utiliser un [client VNC](vnc.md). Avec JupyterLab, rien de tout cela n'est nécessaire.

Lors d'une nouvelle session, le démarrage peut prendre jusqu'à 3 minutes.

Il est possible de rouvrir une session active après la fermeture de l'onglet du navigateur.

La session se terminera en même temps que la session JupyterLab.

#### Terminal

JupyterLab vous permet également d'ouvrir une session de terminal native. Cela peut être utile pour exécuter des commandes bash, soumettre des tâches ou modifier des fichiers.

Le terminal exécute un shell (Bash) sur le nœud de calcul distant, sans la nécessité d'une connexion SSH.

Donne accès aux systèmes de fichiers distants (`/home`, `/project`, `/scratch`).

Permet de lancer des tâches de calcul.

Le terminal permet de copier-coller du texte.

Pour copier, sélectionnez le texte et appuyez sur `Ctrl+C`.

!!! note "Remarque"
    Généralement, `Ctrl+C` sert à envoyer un signal `SIGINT` à un processus en cours d'exécution ou à annuler la commande en cours. Pour obtenir ce comportement dans le terminal de JupyterLab, cliquez dessus pour désélectionner le texte avant d'appuyer sur `Ctrl+C`.

Pour coller, appuyez sur `Ctrl+V`.

#### Globus

Si [Globus](globus.md) est disponible sur la grappe que vous utilisez, vous verrez peut-être cette icône. Cela ouvrira votre navigateur et la collection Globus correspondante.

#### Metrix

Si le [portail de tâches Metrix](portail.md) est disponible sur la grappe que vous utilisez, cette icône ouvrira une page qui montre les statistiques de votre tâche.

### Applications disponibles après le chargement d'un module

Plusieurs modules que nous fournissons affichent également une icône de lancement d'une application lors de son chargement, même si elles ne sont pas chargées par défaut.

#### Julia

Le chargement d'un module `ijulia-kernel` vous permettra d'ouvrir un calepin avec le langage Julia.

#### Suite Ansys

La suite Ansys propose plusieurs outils offrant une interface utilisateur graphique. Si vous chargez l'un des modules Ansys, vous accéderez à une série d'icônes de lancement, la plupart fonctionnant via une connexion VNC dans le navigateur.

Ansys Fluent dispose également d'une interface web, accessible via l'icône ci-dessous.
Notez qu'un mot de passe est requis pour se connecter à Ansys Fluent. Ce mot de passe est généré au lancement et enregistré dans votre dossier personnel, dans le fichier `$HOME/fluent_webserver_token`.

Notez que pour Ansys, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys](ansys.md).

#### Ansys EDT

[Ansys EDT](https://www.ansys.com/products/electronics) est un module distinct. Charger le module `ansysedt` fera apparaître l'icône de lancement correspondante.

Notez que pour Ansys EDT, vous devrez fournir votre propre licence, comme expliqué sur notre page [Ansys EDT](ansys-edt.md).

#### COMSOL

[COMSOL](http://www.comsol.com) est un logiciel polyvalent pour modéliser des applications d'ingénierie.

Pour utiliser ce logiciel, vous devez détenir votre propre licence.

Charger un module `comsol` ajoutera une icône de lancement permettant de démarrer l'interface utilisateur graphique de COMSOL via une session VNC. Consultez notre page [COMSOL](comsol.md) pour plus de détails sur l'utilisation de ce logiciel.

#### MATLAB

[MATLAB](https://www.mathworks.com/?s_tid=gn_logo) est disponible en chargeant un module `matlab`, ce qui ajoutera une icône de lancement pour démarrer le logiciel via une session VNC. Notez que vous devrez fournir votre propre fichier de licence, comme expliqué sur notre page [MATLAB](matlab.md).

#### NVIDIA Nsight Systems

[NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems) est un outil d'analyse des performances développé principalement pour le profilage des GPU, mais qui permet également de profiler le code CPU.
Le chargement d'un module `cuda` ou `nvhpc` crée une icône pour lancer l'interface utilisateur graphique dans une session VNC.

#### Octave

[GNU Octave](https://octave.org/) est un langage de programmation scientifique libre largement compatible avec MATLAB. Le chargement d'un module `octave` ajoute une icône pour lancer l'interface utilisateur graphique d'Octave via une session VNC. Consultez notre page sur [Octave](octave.md) pour plus de détails sur l'utilisation de ce logiciel.

#### ParaView

[ParaView](https://www.paraview.org/) est un puissant logiciel libre de visualisation. Le chargement d'un module `paraview` ajoute une icône pour lancer l'interface utilisateur graphique ParaView via une session VNC. Consultez notre page [ParaView](paraview.md) pour plus de détails sur l'utilisation de ce logiciel.

#### QGIS

[QGIS](https://qgis.org/) est un puissant logiciel libre de visualisation et de traitement de données de systèmes d'information géographique (SIG). Le chargement d'un module `qgis` ajoute une icône pour lancer l'interface graphique de QGIS via une session VNC. Consultez notre page [QGIS](qgis.md) pour plus de détails sur ce logiciel.

#### Star-CCM+

[Star-CCM+](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/) de Siemens est un logiciel commercial de simulation numérique pour la dynamique des fluides. Il est disponible en chargeant l'un des modules `starccm` ou `starccm-mixed`, qui ajoute une icône pour lancer l'interface graphique de Star-CCM+ via une session VNC. Comme pour tous les logiciels commerciaux, vous devrez fournir votre propre licence. Consultez notre page [Star-CCM+](star-ccm.md) pour plus de détails sur l'utilisation de ce logiciel.

## Informations additionnelles sur l'exécution des calepins

### Calepins Python

Si votre calepin requiert l'un des paquets Python scientifiques suivants, avant de l'ouvrir, vous devez charger le module `scipy-stack` depuis l'outil JupyterLab *Logiciels* :

*   `ipython`, `ipython_genutils`, `ipykernel`, `ipyparallel`
*   `matplotlib`
*   `numpy`
*   `pandas`
*   `scipy`
*   Pour plus d'information, voir [Pile logicielle SciPy](python.md#pile-logicielle-scipy)

!!! note "Remarque"
    Vous pouvez également installer les paquets nécessaires en exécutant, par exemple, la commande suivante dans une cellule :
    ```bash
    pip install --no-index numpy
    ```
    Pour certains paquets (comme plotly, par exemple), vous devrez peut-être redémarrer le noyau du calepin avant d'importer le paquet.
    L'installation des paquets dans l'environnement du noyau Python par défaut est temporaire, le temps de la session JupyterLab; vous devrez réinstaller ces paquets lors du prochain démarrage d'une nouvelle session JupyterLab. Pour un environnement Python persistant, vous devez configurer un **[noyau Python personnalisé](advanced-jupyter-configuration.md#noyau-python)**.

Pour ouvrir un calepin Python existant :

*   Retournez à l'Explorateur de fichiers.
*   Localisez le fichier `*.ipynb`.
*   Double-cliquez sur le fichier `*.ipynb`.
    *   Le calepin Python s'ouvre dans un nouvel onglet JupyterLab.
    *   Un nouveau noyau IPython démarrera en arrière-plan pour le calepin.

Pour ouvrir un calepin Python dans le répertoire courant de l'Explorateur de fichiers :

*   Cliquez sur le bouton "Python 3.x" sous la section Calepin;
    *   ceci ouvre un nouveau calepin Python 3 dans un nouvel onglet JupyterLab;
    *   un nouveau noyau IPython démarrera en arrière-plan pour le calepin.

### Exécuter des calepins en scripts Python

1.  À partir de la console ou dans une nouvelle cellule d'un calepin, installez `nbconvert` :

    ```bash
    !pip install --no-index nbconvert
    ```

2.  Convertissez vos calepins en scripts Python.

    ```bash
    !jupyter nbconvert --to python my-current-calepin.ipynb
    ```

3.  Créez [une tâche non interactive](running-jobs.md#soumettre-des-taches-avec-sbatch) et soumettez-la.

Dans le script de soumission, exécutez le calepin converti avec

```bash
python mynotebook.py
```

et soumettez votre tâche non interactive avec

```bash
sbatch my-submit.sh
```

# Dépannage

## Message d'erreur : ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system

Ce message peut survenir dans un calepin quand pip essaie de désinstaller un paquet dans un emplacement en lecture seule.

Dans plusieurs cas, vous pouvez utiliser la commande suivante dans la cellule du calepin :

```bash
pip install --no-index --ignore-installed <package>
```

Cette commande installe le paquet qui est la source de l'erreur, mais **ne réussit pas toujours** pour certains paquets comme `pyarrow`, `opencv`, `mpi4py`.

Si vous avez des questions, contactez [le soutien technique](technical-support.md).