---
title: "JupyterNotebook/fr"
slug: "jupyternotebook"
lang: "fr"

source_wiki_title: "JupyterNotebook/fr"
source_hash: "4c350c2b1b624a7170604b01842ab5bd"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:34:46.034518+00:00"

tags:
  []

keywords:
  - "Project Jupyter"
  - "Julia"
  - "activation de l'environnement virtuel"
  - "ajouter des noyaux"
  - "services web mandataires"
  - "Pkg.add(\"IJulia\")"
  - "Jupyter Notebook"
  - "module Python"
  - "ipykernel"
  - "tunnel SSH"
  - "poste de travail"
  - "IRkernel"
  - "virtualenv"
  - "port local"
  - "grappe"
  - "source $HOME/jupyter_py3/bin/activate"
  - "sshuttle"
  - "module load julia"
  - "environnement virtuel Python"
  - "module R"
  - "mkdir -p ~/.local/share/jupyter/kernels"
  - "nbserverproxy"
  - "module d'extension jupyterlmod"
  - "TensorBoard"
  - "serveur Jupyter"
  - "MobaXTerm"
  - "RStudio Launcher"

questions:
  - "Quelles sont les étapes détaillées pour installer Jupyter Notebook dans un environnement virtuel Python sur le serveur ?"
  - "Pourquoi l’article conseille‑t‑il d’utiliser JupyterLab plutôt que Jupyter Notebook, et où peut‑on accéder à un environnement Jupyter préconfiguré ?"
  - "Comment installer et activer les extensions Jupyter Lmod et nbserverproxy afin d’enrichir les fonctionnalités de Jupyter Notebook ?"
  - "À quoi sert la commande `jupyter serverextension enable --py jupyterlmod --sys-prefix` ?"
  - "Quel est le rôle de `nbserverproxy` pour accéder aux services web démarrés dans un serveur Jupyter ?"
  - "Pourquoi un proxy est‑il nécessaire pour utiliser des services locaux tels que TensorBoard depuis Jupyter ?"
  - "Quelles sont les étapes d’installation et d’activation de nbserverproxy et nbrsessionproxy pour rendre les services accessibles via le chemin /proxy/ dans Jupyter Notebook ?"
  - "Comment démarrer une session RStudio depuis Jupyter Notebook à l’aide du RStudio Launcher, et quels environnements logiciels sont requis pour que cela fonctionne ?"
  - "Quelle est la procédure complète pour lancer Jupyter Notebook sur le cluster (allocation de ressources, activation de l’environnement) et s’y connecter depuis un poste local en créant un tunnel SSH ?"
  - "Comment lancer Jupyter Notebook sur un nœud distant en utilisant sshuttle et quelle URL doit‑on copier dans le navigateur ?"
  - "Quelle procédure suivre sous Windows avec MobaXTerm pour créer un tunnel SSH et accéder à Jupyter Notebook via localhost ?"
  - "Quelles sont les étapes nécessaires pour ajouter un nouveau noyau (par exemple Julia) à Jupyter Notebook sur le cluster ?"
  - "Quel est l'objectif de créer un tunnel SSH entre la grappe et votre poste de travail ?"
  - "Quel paquet Python est recommandé d’utiliser sous Linux ou macOS X pour établir ce tunnel ?"
  - "Quelle commande doit‑être lancée dans le terminal de votre poste de travail pour créer le tunnel ?"
  - "Quelles sont les étapes détaillées pour créer, activer et installer un noyau Python 3.5 dans Jupyter Notebook ?"
  - "Comment installer et configurer le noyau R (IRkernel) ainsi que son environnement virtuel pour Jupyter Notebook ?"
  - "Où peut‑on consulter la documentation supplémentaire mentionnée pour IJulia, ipykernel et IRKernel ?"
  - "Quelle est la fonction de la commande `mkdir -p ~/.local/share/jupyter/kernels` mentionnée au début du texte ?"
  - "Quelles sont les trois étapes décrites pour installer le noyau Julia dans Jupyter Notebook ?"
  - "Comment active-t-on l’environnement virtuel Jupyter avant d’installer le paquet IJulia ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Contenu avancé"
Cette page est destinée aux utilisateurs expérimentés. Veuillez plutôt consulter [JupyterHub](jupyterhub.md).

## Introduction

[Project Jupyter](http://jupyter.org/) est un projet *open source* sans but lucratif dont la mission est de servir le calcul scientifique et la science des données interactives. Initié en 2014 dans le cadre du IPython Project, la portée de Project Jupyter s'étend à plusieurs autres langages de programmation.
<small>http://jupyter.org/about.html</small>

L'application web Jupyter Notebook rend possibles la création et le partage de documents contenant aussi bien du code, des équations et des visualisations que du texte.
<small>http://www.jupyter.org/</small>

Jupyter Notebook fonctionne sur un nœud de calcul ou sur un nœud de connexion (non recommandé). Dans le cas du nœud de connexion, diverses limites sont imposées tant pour l'utilisateur que pour les processus, et les applications sont parfois terminées quand elles utilisent trop de temps CPU ou de mémoire. Dans le cas du nœud de calcul, la tâche est soumise avec la spécification du nombre de CPU ou de GPU à utiliser, la quantité de mémoire et le temps d'exécution. Les directives qui suivent concernent la soumission d'une tâche Jupyter Notebook.

**Autre information :**
*   Jupyter Notebook n'étant pas la plus récente interface de Jupyter, nous vous suggérons d'installer plutôt **[JupyterLab](../getting-started/advanced_jupyter_configuration.md)**.
*   Pour utiliser un environnement Jupyter préconfiguré, voyez la page **[Jupyter](../software/jupyter.md)**.

## Installation

Ces directives permettent d'installer Jupyter Notebook avec la commande `pip` dans un [environnement virtuel Python](../software/python.md) dans votre répertoire personnel (*home*). Les directives sont valides pour la version 3.7 de Python, mais vous pouvez installer l'application pour d'autres versions en chargeant le module Python approprié.

1.  Chargez le module Python.
    ```bash
    module load python/3.7
    ```
2.  Créez un nouvel environnement virtuel Python.
    ```bash
    virtualenv $HOME/jupyter_py3
    ```
3.  Activez votre nouvel environnement virtuel Python.
    ```bash
    source $HOME/jupyter_py3/bin/activate
    ```
4.  Installez Jupyter Notebook dans votre nouvel environnement virtuel Python.
    ```bash
    (jupyter_py3)_[name@server ~]$ pip install --no-index --upgrade pip
    (jupyter_py3)_[name@server ~]$ pip install --no-index jupyter
    ```
5.  Dans votre nouvel environnement virtuel, créez un script d'encapsulation pour lancer Jupyter Notebook.
    ```bash
    (jupyter_py3)_[name@server ~]$ echo -e '#!/bin/bash\nexport JUPYTER_RUNTIME_DIR=$SLURM_TMPDIR/jupyter\njupyter notebook --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/notebook.sh
    ```
6.  Enfin, rendez le script exécutable.
    ```bash
    (jupyter_py3)_[name@server ~]$ chmod u+x $VIRTUAL_ENV/bin/notebook.sh
    ```

## Installer des modules d'extension

Les modules d'extension ajoutent des fonctionnalités et peuvent modifier l'interface utilisateur de l'application.

### Jupyter Lmod

[Jupyter Lmod](https://github.com/cmd-ntrf/jupyter-lmod) est un module d'extension permettant d'interagir avec les modules d'environnement avant le lancement des noyaux (*kernels*). Il utilise l'interface Python de Lmod pour accomplir des tâches reliées aux modules comme le chargement, le déchargement, la sauvegarde des collections, etc.

```bash
(jupyter_py3)_[name@server ~]$ pip install jupyterlmod
(jupyter_py3)_[name@server ~]$ jupyter nbextension install --py jupyterlmod --sys-prefix
(jupyter_py3)_[name@server ~]$ jupyter nbextension enable --py jupyterlmod --sys-prefix
(jupyter_py3)_[name@server ~]$ jupyter serverextension enable --py jupyterlmod --sys-prefix
```

### Services web mandataires (*proxy*)

[nbserverproxy](https://github.com/jupyterhub/nbserverproxy) permet d'accéder à des services web mandataires démarrés dans un serveur Jupyter. Ceci est utile dans le cas de services web qui n'écoutent que sur un port du serveur local, par exemple [TensorBoard](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard).

```bash
(jupyter_py3)_[name@server ~]$ pip install nbserverproxy
(jupyter_py3)_[name@server ~]$ jupyter serverextension enable --py nbserverproxy --sys-prefix
```

#### Exemple

Avec Jupyter, un service web est démarré via le *Terminal* dans la liste déroulante *Nouveau*.

```bash
tensorboard --port=8008
```

Le service est disponible via `/proxy/` sur `https://address.of.notebook.server/user/theuser/proxy/8008`.

### RStudio Launcher

Jupyter Notebook peut démarrer une session RStudio qui utilise le système d'authentification par jeton de Jupyter Notebook. RStudio Launcher crée l'option *Session RStudio* dans la liste déroulante *Nouveau* de Jupyter Notebook.

!!! note
    La procédure suivante fonctionne uniquement avec les environnements logiciels `StdEnv/2016.4` et `StdEnv/2018.3`.

```bash
(jupyter_py3)_[name@server ~]$ pip install nbserverproxy
(jupyter_py3)_[name@server ~]$ pip install https://github.com/jupyterhub/nbrsessionproxy/archive/v0.8.0.zip
(jupyter_py3)_[name@server ~]$ jupyter serverextension enable --py nbserverproxy --sys-prefix
(jupyter_py3)_[name@server ~]$ jupyter nbextension install --py nbrsessionproxy --sys-prefix
(jupyter_py3)_[name@server ~]$ jupyter nbextension enable --py nbrsessionproxy --sys-prefix
(jupyter_py3)_[name@server ~]$ jupyter serverextension enable --py nbrsessionproxy --sys-prefix
```

## Activer l'environnement

Une fois que Jupyter Notebook est installé, vous n'aurez qu'à recharger le module Python associé à votre environnement lorsque vous vous connectez à la grappe.

```bash
module load python/3.7
```

Activez ensuite l'environnement virtuel dans lequel Jupyter Notebook est installé.

```bash
source $HOME/jupyter_py3/bin/activate
```

### RStudio Server (optionnel)

Pour utiliser [RStudio Launcher](#rstudio-launcher), chargez le module RStudio Server.

```bash
(jupyter_py3)_[name@server ~]$ module load rstudio-server
```

## Lancer Jupyter Notebook

Pour lancer l'application, soumettez une tâche interactive. Ajustez les paramètres selon vos besoins. Pour plus d'information, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

```bash
(jupyter_py3)_[name@server ~]$ salloc --time=1:0:0 --ntasks=1 --cpus-per-task=2 --mem-per-cpu=1024M --account=def-yourpi srun $VIRTUAL_ENV/bin/notebook.sh
```
```text
salloc: Granted job allocation 1422754
salloc: Waiting for resource configuration
salloc: Nodes cdr544 are ready for job
[I 14:07:08.661 NotebookApp] Serving notebooks from local directory: /home/fafor10
[I 14:07:08.662 NotebookApp] 0 active kernels
[I 14:07:08.662 NotebookApp] The Jupyter Notebook is running at:
[I 14:07:08.663 NotebookApp] http://cdr544.int.cedar.computecanada.ca:8888/?token=7ed7059fad64446f837567e32af8d20efa72e72476eb72ca
[I 14:07:08.663 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 14:07:08.669 NotebookApp]

Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://cdr544.int.cedar.computecanada.ca:8888/?token=7ed7059fad64446f837567e3
```

## Se connecter à Jupyter Notebook

Puisque les nœuds de calcul ne sont pas directement accessibles par l'Internet, vous devez créer un [tunnel SSH](../getting-started/ssh_tunnelling.md) entre la grappe et votre poste de travail pour que votre fureteur web puisse avoir accès à Jupyter Notebook opérant sur un nœud de calcul.

### Sous Linux ou macOS X

Nous recommandons le paquet Python [sshuttle](https://sshuttle.readthedocs.io).

Sur votre poste de travail, ouvrez une nouvelle fenêtre terminal et lancez la commande `sshuttle` pour créer le tunnel.

```bash
[name@my_computer ~]$ sshuttle --dns -Nr <username>@<cluster>.alliancecan.ca
```

Dans la commande précédente, remplacez `<username>` par votre nom d'utilisateur et `<cluster>` par la grappe à laquelle vous vous êtes connecté pour lancer Jupyter Notebook.

Puis copiez-collez l'adresse URL dans votre fureteur. Avec l'exemple précédent, le résultat serait
```text
http://cdr544.int.cedar.computecanada.ca:8888/?token=7ed7059fad64446f837567e3
```

### Sous Windows

Pour créer un [tunnel SSH](../getting-started/ssh_tunnelling.md), utilisez [MobaXTerm](../getting-started/connecting_with_mobaxterm.md) comme suit, ce qui fonctionne aussi avec Unix (macOS, Linux, etc.).

1.  Dans MobaXTerm, ouvrez un premier onglet *Terminal* (session 1) et connectez-vous à une grappe. Suivez ensuite les directives de la section [Lancer Jupyter Notebook](#lancer-jupyter-notebook) ci-dessus. L'adresse URL suivante devrait s'afficher.
    ```text
    http://cdr544.int.cedar.computecanada.ca:8888/?token=7ed7059fad64446f837567e3
           └────────────────┬───────────────────┘         └──────────┬───────────┘
                  nom du serveur:port                              jeton
    ```
2.  Dans MobaXTerm, ouvrez un second onglet *Terminal* (session 2). Dans la commande suivante, remplacez `<nom du serveur:port>` par la valeur correspondante dans la structure de l'adresse URL obtenue à la session 1 ci-dessus; remplacez `<username>` par votre nom d'utilisateur et; remplacez `<cluster>` par la grappe à laquelle vous vous êtes connecté à la session 1. Lancez la commande.
    ```bash
    [name@my_computer ~]$ ssh -L 8888:<hostname:port> <username>@<cluster>.alliancecan.ca
    ```
3.  Par votre fureteur, allez à
    ```text
    http://localhost:8888/?token=<jeton>
    ```
    Remplacez `<jeton>` par la valeur obtenue à la session 1.

## Fermer Jupyter Notebook

Pour fermer le serveur Jupyter Notebook avant la fin du temps d'exécution, appuyez deux fois sur `CTRL-C` dans le terminal où la tâche interactive a été lancée.

Si le tunnel a été créé avec MobaXTerm, appuyez sur `CTRL-D` dans la session 2 pour fermer le tunnel.

## Ajouter des noyaux (*kernels*)

Il est possible d'ajouter des noyaux pour d'autres langages de programmation ou pour des versions de Python différentes de celle dans laquelle fonctionne Jupyter Notebook. Pour plus d'information, consultez [Making kernels for Jupyter](http://jupyter-client.readthedocs.io/en/latest/kernels.html).

L'installation se fait en deux étapes :
1.  Installation des paquets permettant à l'interpréteur de communiquer avec Jupyter Notebook.
2.  Création du fichier pour que Jupyter Notebook puisse créer un canal de communication avec l'interpréteur : il s'agit du fichier de configuration du noyau.

Chacun des fichiers de configuration du noyau doit être créé dans son propre sous-répertoire dans un répertoire de votre répertoire personnel (*home*) par le chemin `~/.local/share/jupyter/kernels`. Jupyter Notebook ne crée pas ce fichier; dans tous les cas, la première étape est de le créer avec la commande `mkdir -p ~/.local/share/jupyter/kernels`.

Les prochaines sections présentent des exemples de procédures d'installation d'un noyau.

### Julia

1.  Chargez le module [Julia](../software/julia.md).
    ```bash
    module load julia
    ```
2.  Activez l'environnement virtuel Jupyter Notebook.
    ```bash
    source $HOME/jupyter_py3/bin/activate
    ```
3.  Installez IJulia.
    ```bash
    (jupyter_py3)_[name@server ~]$ echo 'Pkg.add("IJulia")' | julia
    ```

Pour plus d'information, consultez la [documentation IJulia](https://github.com/JuliaLang/IJulia.jl).

### Python

1.  Chargez le module Python.
    ```bash
    module load python/3.5
    ```
2.  Créez un nouvel environnement Python.
    ```bash
    virtualenv $HOME/jupyter_py3.5
    ```
3.  Activez le nouvel environnement Python.
    ```bash
    source $HOME/jupyter_py3.5/bin/activate
    ```
4.  Installez la bibliothèque `ipykernel`.
    ```bash
    (jupyter_py3.5)_[name@server ~]$ pip install ipykernel
    ```
5.  Générez le fichier de configuration du noyau. Remplacez `<unique_name>` par un nom unique pour votre noyau.
    ```bash
    (jupyter_py3.5)_[name@server ~]$ python -m ipykernel install --user --name <unique_name> --display-name "Python 3.5 Kernel"
    ```
6.  Désactivez l'environnement virtuel.
    ```bash
    (jupyter_py3.5)_[name@server ~]$ deactivate
    ```

Pour plus d'information, voyez la [documentation ipykernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).

### R

1.  Chargez le module R.
    ```bash
    module load r
    ```
2.  Activez l'environnement virtuel Jupyter Notebook.
    ```bash
    source $HOME/jupyter_py3/bin/activate
    ```
3.  Installez les dépendances du noyau.
    ```bash
    (jupyter_py3)_[name@server ~]$ R -e "install.packages(c('crayon', 'pbdZMQ', 'devtools'), repos='http://cran.us.r-project.org')"
    ```
4.  Installez le noyau R.
    ```bash
    (jupyter_py3)_[name@server ~]$ R -e "devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))"
    ```
5.  Installez le fichier de configuration du noyau R.
    ```bash
    (jupyter_py3)_[name@server ~]$ R -e "IRkernel::installspec()"
    ```

Pour plus d'information, consultez la [documentation IRKernel](https://irkernel.github.io/docs/).

## Références