---
title: "Advanced Jupyter configuration/fr"
slug: "advanced_jupyter_configuration"
lang: "fr"

source_wiki_title: "Advanced Jupyter configuration/fr"
source_hash: "9e888ae84e26c71ded8e86cd2bf7fede"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T04:54:42.081319+00:00"

tags:
  []

keywords:
  - "paquets R"
  - "notebooks"
  - "Jupyter"
  - "modules d'extension"
  - "Bibliothèques Python"
  - "CRAN"
  - "sbatch"
  - "environnement virtuel Python"
  - "installation"
  - "Noyau R"
  - "JupyterLab"
  - "Ajouter des noyaux"
  - "MobaXTerm"
  - "nbconvert"
  - "nœud de calcul"
  - "script Python"
  - "tunnel SSH"
  - "langages de programmation"
  - "script exécutable"
  - "RStudio Server"
  - "virtualenv"
  - "kernels"
  - "répertoire commun"
  - "nœud de connexion"
  - "environnement virtuel"
  - "Environnement virtuel"
  - "lancement automatique"
  - "Python"
  - "Noyau Python"
  - "module Python"
  - "server access"
  - "notebook"
  - "Noyau"
  - "Jupyter Lmod"
  - "ServerApp"
  - "noyaux"
  - "Julia"
  - "jupyterlab.sh"
  - "script enveloppeur"

questions:
  - "Pour quels types de tâches l'utilisation de JupyterLab est-elle recommandée et comment doit-on gérer les analyses plus longues ?"
  - "Pourquoi est-il fortement déconseillé d'exécuter un serveur JupyterLab sur un nœud de connexion ?"
  - "Quelles sont les étapes requises pour installer et configurer JupyterLab dans un environnement virtuel Python ?"
  - "Comment installer et configurer des modules d'extension tels que Jupyter Lmod et RStudio Server dans JupyterLab ?"
  - "Quelle est la procédure pour activer et vérifier l'environnement virtuel Python avant d'utiliser JupyterLab ?"
  - "Comment démarrer un serveur JupyterLab en soumettant une tâche interactive avec la commande salloc ?"
  - "Quel est l'objectif principal de la création du script enveloppeur mentionné dans le texte ?"
  - "Quelles commandes spécifiques sont utilisées pour générer le contenu du script de lancement de JupyterLab ?"
  - "Comment doit-on procéder pour rendre le script enveloppeur exécutable une fois qu'il a été créé ?"
  - "What command was executed to start the JupyterLab server?"
  - "How can the user access the running JupyterLab server in a browser?"
  - "What keyboard shortcut must be used to stop the server and shut down all kernels?"
  - "Pourquoi est-il nécessaire de créer un tunnel SSH pour accéder à JupyterLab et comment le configurer sous Linux, macOS ou Windows ?"
  - "Quelle est la procédure à suivre pour arrêter le serveur JupyterLab et fermer le tunnel SSH associé ?"
  - "Dans quel but peut-on ajouter de nouveaux noyaux (kernels) à son environnement JupyterLab ?"
  - "Quelles sont les deux étapes principales requises pour l'installation générale d'un nouveau noyau dans JupyterLab ?"
  - "Quels sont les prérequis et la procédure à suivre pour configurer un noyau Julia et y installer des paquets supplémentaires ?"
  - "Comment doit-on procéder pour créer et activer un environnement virtuel destiné à la configuration d'un noyau Python ?"
  - "Quelle combinaison de touches permet de fermer le tunnel ?"
  - "Quels sont les différents cas d'usage justifiant l'ajout de nouveaux noyaux ?"
  - "Où peut-on consulter la documentation détaillée pour créer des noyaux pour Jupyter ?"
  - "Quelle commande permet de charger un module Python ?"
  - "Comment créer et activer un nouvel environnement virtuel Python ?"
  - "À quoi sert le répertoire commun \"kernels\" mentionné dans les instructions ?"
  - "Comment procéder pour installer un noyau Python personnalisé et y ajouter de nouvelles bibliothèques ?"
  - "Quelles sont les étapes et les dépendances nécessaires pour configurer un noyau R dans cet environnement ?"
  - "Pourquoi est-il obligatoire d'installer les paquets R à partir d'un nœud de connexion plutôt que directement depuis un notebook ?"
  - "Pourquoi l'installation de paquets R ne peut-elle pas être effectuée directement à partir des notebooks ?"
  - "Sur quel type de nœud faut-il se trouver pour pouvoir installer de nouveaux paquets R ?"
  - "Est-il nécessaire d'activer l'environnement virtuel Python lors de l'installation de ces paquets ?"
  - "Comment procéder pour installer et utiliser de nouveaux paquets R dans un notebook ?"
  - "Quel outil faut-il installer et utiliser pour convertir un notebook en script Python ?"
  - "Comment soumettre une tâche non interactive pour exécuter un notebook préalablement converti en script ?"
  - "Comment procéder pour installer et utiliser de nouveaux paquets R dans un notebook ?"
  - "Quel outil faut-il installer et utiliser pour convertir un notebook en script Python ?"
  - "Comment soumettre une tâche non interactive pour exécuter un notebook préalablement converti en script ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! warning "Contenu non recommandé"
    Cette page s'adresse aux utilisateurs d'expérience; l'information qu'elle présente est rarement testée et n'est donc pas recommandée. Utilisez plutôt [JupyterLab](../interactive/jupyterlab.md).

## Introduction

!!! warning "Exécution de notebooks"
    Jupyter Lab et les notebooks conviennent à tes tâches interactives **brèves** pour tester, déboguer ou visualiser rapidement les données (quelques minutes). Pour des analyses plus longues, il faut utiliser [une tâche non interactive avec sbatch](../running-jobs/running_jobs.md#soumettre-des-tâches-avec-sbatch).
    Voir aussi [Exécution de notebooks en scripts Python](#exécution-de-notebooks-en-scripts-python) ci-dessous.

*   **Project Jupyter** est un projet open-source sans but lucratif issu en 2014 du IPython Project pour que tous les langages de programmation puissent être utilisés pour la science des données interactives et le calcul scientifique.
*   **JupyterLab** est un environnement de développement web interactif pour les notebooks, le code et les données. La souplesse de son interface permet la configuration et l'utilisation des flux de travail en science des données, en calcul scientifique, en journalisme computationnel et en apprentissage automatique. Sa conception modulaire permet l'ajout d'extensions qui enrichissent ses fonctionnalités.

Un serveur JupyterLab devrait toujours se trouver sur un nœud de calcul ou sur une instance infonuagique. Les nœuds de connexion ne sont pas un bon choix parce qu'ils imposent des limites qui peuvent interrompre une application qui consommerait trop de temps CPU ou de mémoire vive. Pour obtenir un nœud de calcul, vous pouvez réserver des ressources en [soumettant une tâche](../running-jobs/running_jobs.md) qui demande un nombre prédéterminé de CPU ou de GPU, une certaine quantité de mémoire et un temps limite d'exécution. **Nous décrivons ici comment configurer et soumettre une tâche JupyterLab sur nos grappes nationales.**

Si vous recherchez un environnement Jupyter préconfiguré, consultez la page [Jupyter](../software/jupyter.md).

## Installer JupyterLab

Ces directives installent JupyterLab avec la commande `pip` dans un [environnement virtuel Python](../software/python.md#créer-et-utiliser-un-environnement-virtuel).

1.  Si vous n'avez pas déjà un environnement virtuel Python, créez-en un, puis activez-le.
    1.  Chargez le module Python par défaut (comme démontré ci-dessous) ou chargez une version spécifique (voir les versions disponibles avec `module avail python`).
        ```bash
        module load python
        ```
        **Si vous avez l'intention d'utiliser RStudio Server**, chargez d'abord `rstudio-server` avec
        ```bash
        module load rstudio-server python
        ```
    2.  Créez un nouvel environnement virtuel Python.
        ```bash
        virtualenv --no-download $HOME/jupyter_py3
        ```
    3.  Activez le nouvel environnement virtuel.
        ```bash
        source $HOME/jupyter_py3/bin/activate
        ```
2.  Installez JupyterLab dans votre nouvel environnement virtuel (ceci prendra quelques minutes).
    ```bash
    (jupyter_py3) [name@server ~]$ pip install --no-index --upgrade pip
    (jupyter_py3) [name@server ~]$ pip install --no-index jupyterlab
    ```
3.  Dans l'environnement virtuel, créez un script enveloppeur (*wrapper*) pour le lancement automatique de JupyterLab.
    ```bash
    (jupyter_py3) [name@server ~]$ echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/jupyterlab.sh
    ```
4.  Enfin, rendez ce script exécutable.
    ```bash
    (jupyter_py3) [name@server ~]$ chmod u+x $VIRTUAL_ENV/bin/jupyterlab.sh
    ```

## Installer des modules d'extension

Les modules d'extension ajoutent des fonctionnalités et peuvent modifier l'interface utilisateur de JupyterLab.

### Jupyter Lmod

[Jupyter Lmod](https://github.com/cmd-ntrf/jupyter-lmod) est un module d'extension permettant d'interagir avec les modules d'environnement avant le lancement des noyaux (*kernels*). Il utilise l'interface Python de Lmod pour accomplir des tâches reliées aux modules comme le chargement, le déchargement, la sauvegarde des collections, etc.

Les commandes suivantes installeront et activeront l'extension Jupyter Lmod dans votre environnement (la troisième commande prendra quelques minutes).
```bash
(jupyter_py3) [name@server ~]$ module load nodejs
(jupyter_py3) [name@server ~]$ pip install jupyterlmod
(jupyter_py3) [name@server ~]$ jupyter labextension install jupyterlab-lmod
```
Vous trouverez dans la page [JupyterHub](../interactive/jupyterhub.md#jupyterlab) les directives pour gérer les *modules chargés* dans l'interface JupyterLab.

### RStudio Server

RStudio Server vous permet de développer du code R dans un environnement RStudio, sous un onglet de votre navigateur. Il y a quelques différences avec [la procédure d'installation de JupyterLab](#installer-jupyterlab).

1.  **Avant de charger le module `python` et avant de créer un nouvel environnement virtuel**, chargez le module `rstudio-server`.
    ```bash
    module load rstudio-server python
    ```
2.  Une fois que [JupyterLab est installé dans le nouvel environnement virtuel](#installer-jupyterlab), installez le serveur mandataire (*proxy*) Jupyter RSession.
    ```bash
    (jupyter_py3) [name@server ~]$ pip install --no-index jupyter-rsession-proxy
    ```
Toutes les autres étapes de configuration et d'utilisation sont les mêmes. Vous devriez voir une application RStudio sous l'onglet *Lanceur*.

## Utiliser votre installation

### Activer l'environnement

Assurez-vous que l'environnement virtuel Python dans lequel vous avez installé JupyterLab est activé. Par exemple, quand vous vous connectez à la grappe, vous devez l'activer à nouveau avec
```bash
source $HOME/jupyter_py3/bin/activate
```
Pour vérifier que votre environnement est prêt, vous pouvez obtenir une liste des paquets `jupyter*` installés avec la commande
```bash
(jupyter_py3) [name@server ~]$ pip freeze | grep jupyter
```
```text
jupyter-client==7.1.0+computecanada
jupyter-core==4.9.1+computecanada
jupyter-server==1.9.0+computecanada
jupyterlab==3.1.7+computecanada
jupyterlab-pygments==0.1.2+computecanada
jupyterlab-server==2.3.0+computecanada
```

### Lancer JupyterLab

Pour démarrer un serveur JupyterLab, soumettez une tâche interactive avec `salloc`. Ajustez les paramètres selon vos besoins. Pour plus d'information, voyez [Exécuter des tâches](../running-jobs/running_jobs.md).
```bash
(jupyter_py3) [name@server ~]$ salloc --time=1:0:0 --ntasks=1 --cpus-per-task=2 --mem-per-cpu=1024M --account=def-yourpi srun $VIRTUAL_ENV/bin/jupyterlab.sh
```
```text
...
[I 2021-12-06 10:37:14.262 ServerApp] jupyterlab | extension was successfully linked.
...
[I 2021-12-06 10:37:39.259 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2021-12-06 10:37:39.356 ServerApp]

    To access the server, open this file in a browser:
        file:///home/name/.local/share/jupyter/runtime/jpserver-198146-open.html
    Or copy and paste one of these URLs:
        http://node_name.int.cluster.computecanada.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
     or http://127.0.0.1:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
```

### Se connecter à JupyterLab

Pour avoir accès au serveur JupyterLab dans un nœud de calcul à partir de votre navigateur web, vous devez créer un [tunnel SSH](ssh_tunnelling.md) de votre ordinateur vers la grappe puisque les nœuds de calcul ne sont pas accessibles directement à partir de l'internet.

#### Sous Linux ou macOS

Nous recommandons l'utilisation du paquet Python [sshuttle](https://sshuttle.readthedocs.io).

Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et créez le tunnel SSH avec la commande `sshuttle` où vous remplacerez `<username>` par le nom d'utilisateur pour votre compte avec l'Alliance et `<cluster>` par la grappe sur laquelle vous avez lancé JupyterLab.
```bash
[name@local ~]$ sshuttle --dns -Nr <username>@<cluster>.alliancecan.ca
```
Copiez et collez la première adresse HTTP dans votre navigateur web; dans l'exemple `salloc` ci-dessus, ce serait
```text
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
```

#### Sous Windows

Pour créer un [tunnel SSH](ssh_tunnelling.md) à partir de Windows, utilisez [MobaXTerm](connecting_with_mobaxterm.md) ou n’importe quel terminal qui supporte la commande `ssh`.

1.  Une fois que JupyterLab est lancé sur un nœud de calcul (voir [Lancer JupyterLab](#lancer-jupyterlab)), vous pouvez extraire le `hostname:port` et le `token` de la première adresse HTTP fournie, par exemple
    ```text
    http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c368829...2728fad4eb
           (hostname:port)                                   (token)
    ```
2.  Ouvrez un nouvel onglet *Terminal* dans MobaXTerm. Dans la commande suivante, remplacez `<hostname:port>` par la valeur correspondante (voir ci-dessus); remplacez `<username>` par le nom d'utilisateur pour votre compte avec l'Alliance; remplacez `<cluster>` par la grappe sur laquelle vous avez lancé JupyterLab.
    ```bash
    [name@local ~]$ ssh -L 8888:<hostname:port> <username>@<cluster>.alliancecan.ca
    ```
3.  Ouvrez votre navigateur web et allez à l'adresse suivante, où `<token>` doit être remplacé par la valeur alphanumérique provenant de l'adresse illustrée ci-dessus.
    ```text
    http://localhost:8888/?token=<token>
    ```

### Fermer JupyterLab

Pour arrêter le serveur JupyterLab avant la fin du temps d'exécution, appuyez deux fois sur **CTRL-C** dans le terminal où la tâche interactive a été lancée.

Si vous avez utilisé MobaXterm pour créer un tunnel SSH, appuyez sur **Ctrl-D** pour fermer le tunnel.

## Ajouter des noyaux

Il est possible d'ajouter des noyaux pour d'autres langages de programmation, pour une version différente de Python ou pour un environnement virtuel persistant qui a tous les paquets et bibliothèques nécessaires à votre projet. Pour plus d'information, voyez [Making kernels for Jupyter](http://jupyter-client.readthedocs.io/en/latest/kernels.html).

L'installation d'un nouveau noyau se fait en deux étapes :
1.  Installation des paquets qui permettent à l'interpréteur du langage de communiquer avec l'interface Jupyter.
2.  Création d'un fichier qui indique à JupyterLab comment amorcer un canal de communication avec l'interpréteur du langage. Ce fichier de configuration du noyau (*kernel spec file*) est sauvegardé dans un sous-répertoire de `~/.local/share/jupyter/kernels`.

Les prochaines sections présentent des exemples de procédures d'installation d'un noyau.

### Noyau Julia

Prérequis :
1.  La configuration d'un noyau Julia dépend d'un environnement virtuel Python et d'un répertoire `kernels`. Si vous n'avez pas ces dépendances, assurez-vous de suivre les quelques premières directives dans **la section *Noyau Python* ci-dessous** (un noyau Python n'est pas requis).
2.  Puisque l'installation des paquets Julia nécessite un accès à l'internet, la configuration d'un noyau Julia doit se faire **[à l'invite de commande sur un nœud de connexion](ssh.md)**.

Une fois que l'environnement virtuel Python est disponible et activé, vous pouvez configurer le noyau Julia.

1.  Chargez le module **[Julia](../software/julia.md)**.
    ```bash
    (jupyter_py3) [name@server ~]$ module load julia
    ```
2.  Installez IJulia.
    ```bash
    (jupyter_py3) [name@server ~]$ echo -e 'using Pkg\nPkg.add("IJulia")' | julia
    ```
3.  **Important** : Avant d'utiliser le noyau Julia, démarrez ou redémarrez une nouvelle session JupyterLab.

Pour plus d'information, consultez la [documentation sur IJulia](https://github.com/JuliaLang/IJulia.jl).

#### Installer d'autres paquets Julia

Comme pour la procédure d'installation ci-dessus, il faut installer les paquets Julia à partir d'un nœud de connexion, mais l'environnement virtuel Python peut rester désactivé.

1.  Assurez-vous que le même module Julia est chargé.
    ```bash
    module load julia
    ```
2.  Installez les paquets nécessaires, par exemple `Glob`.
    ```bash
    echo -e 'using Pkg\nPkg.add("Glob")' | julia
    ```
3.  Les paquets Julia nouvellement installés devraient être utilisés dans un notebook exécuté par le noyau Julia.

### Noyau Python

Dans un terminal avec une session active sur un serveur distant, vous pouvez configurer un [environnement virtuel Python](../software/python.md#créer-et-utiliser-un-environnement-virtuel) avec tous les [modules Python](../programming/available_python_wheels.md) nécessaires et un noyau Python adapté à JupyterLab.
La configuration la plus simple de Jupyter dans un nouvel environnement virtuel Python se fait comme suit :

1.  Si vous n'avez pas déjà un environnement virtuel Python, créez-en un, puis activez-le.
    1.  Commencez à partir d'un environnement Bash vierge (ceci n'est nécessaire que si vous utilisez le *Terminal* Jupyter via [JupyterHub](../interactive/jupyterhub.md) pour créer et configurer le noyau Python).
        ```bash
        env -i HOME=$HOME bash -l
        ```
    2.  Chargez un module Python.
        ```bash
        module load python
        ```
    3.  Créez un nouvel environnement virtuel Python.
        ```bash
        virtualenv --no-download $HOME/jupyter_py3
        ```
    4.  Activez le nouvel environnement virtuel.
        ```bash
        source $HOME/jupyter_py3/bin/activate
        ```
2.  Créez le répertoire commun `kernels` qui est utilisé par tous les noyaux que vous voulez installer.
    ```bash
    (jupyter_py3) [name@server ~]$ mkdir -p ~/.local/share/jupyter/kernels
    ```
3.  Enfin, installez le noyau Python.
    1.  Installez la bibliothèque `ipykernel`.
        ```bash
        (jupyter_py3) [name@server ~]$ pip install --no-index ipykernel
        ```
    2.  Générez le fichier des spécifications du noyau. Remplacez `<unique_name>` par un nom spécifique à votre noyau.
        ```bash
        (jupyter_py3) [name@server ~]$ python -m ipykernel install --user --name <unique_name> --display-name "Python 3.x Kernel"
        ```
4.  **Important** : Avant d'utiliser le noyau Python, démarrez ou redémarrez une nouvelle session JupyterLab.

Pour plus d'information, consultez la [documentation IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).

#### Installer d'autres bibliothèques Python

Selon l'environnement virtuel Python configuré dans la section précédente :

Dans un *Terminal* Jupyter via [JupyterHub](../interactive/jupyterhub.md), assurez-vous que l'environnement virtuel Python est activé et se trouve dans un environnement Bash vierge. Voir la section ci-dessus pour les détails.
1.  Installez une bibliothèque qui serait requise, par exemple `numpy`.
    ```bash
    (jupyter_py3) [name@server ~]$ pip install --no-index numpy
    ```
2.  Vous pouvez maintenant importer les bibliothèques Python dans un notebook exécuté par le `Python 3.x Kernel`.

### Noyau R

Prérequis :
1.  La configuration d'un noyau R dépend d'un environnement virtuel Python et d'un répertoire `kernels`. Si vous n'avez pas ces dépendances, assurez-vous de suivre les quelques premières directives dans **la section *Noyau Python* ci-dessus** (un noyau Python n'est pas requis).
2.  Puisque l'installation de paquets R nécessite un accès à [CRAN](https://cran.r-project.org/), la configuration d'un noyau R doit se faire **[à l'invite de commande sur un nœud de connexion](ssh.md)**.

Une fois que l'environnement virtuel Python est disponible et activé, vous pouvez configurer le noyau R.

1.  Chargez un module R.
    ```bash
    (jupyter_py3) [name@server ~]$ module load r/4.1
    ```
2.  Installez les dépendances du noyau R, soit `crayon`, `pbdZMQ` et `devtools`; ceci pourrait prendre jusqu'à 10 minutes et les paquets devraient être installés dans un répertoire local tel que `~/R/x86_64-pc-linux-gnu-library/4.1`.
    ```bash
    (jupyter_py3) [name@server ~]$ R --no-save
    ```
    ```text
    > install.packages(c('crayon', 'pbdZMQ', 'devtools'), repos='http://cran.us.r-project.org')
    ```
3.  Installez le noyau R.
    ```R
    > devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))
    ```
4.  Installez le fichier des spécifications du noyau R.
    ```R
    > IRkernel::installspec()
    ```
5.  **Important** : Avant d'utiliser le noyau R, démarrez ou redémarrez une nouvelle session JupyterLab.

Pour plus d'information, consultez la [documentation IRkernel](https://irkernel.github.io/docs/).

#### Installer d'autres paquets R

L'installation de paquets R ne peut se faire à partir de notebooks parce qu'il n'y a pas d'accès à CRAN. Comme dans la procédure d'installation ci-dessus, il faut installer les paquets R dans un nœud de connexion, mais l'environnement virtuel Python peut rester désactivé.

1.  Assurez-vous que le même module R module est chargé.
    ```bash
    module load r/4.1
    ```
2.  Démarrez l'interpréteur R et installez les paquets requis. Voici un exemple avec `doParallel` :
    ```bash
    R --no-save
    ```
    ```text
    > install.packages('doParallel', repos='http://cran.us.r-project.org')
    ```
3.  Les paquets R nouvellement installés devraient déjà pouvoir être utilisés dans un notebook exécuté par le noyau R.

## Exécution de notebooks en scripts Python

Pour des tâches ou des analyses plus longues, soumettez [une tâche interactive](../running-jobs/running_jobs.md#soumettre-des-tâches-avec-sbatch). Il faut alors convertir le notebook en un script Python, créer le script et le soumettre.

1.  Dans un nœud de connexion, créez et activez [un environnement virtuel](../software/python.md#créer-et-utiliser-un-environnement-virtuel), installez ensuite `nbconvert` si ce n'est pas déjà installé.
    ```bash
    (venv) [name@server ~]$ pip install --no-index nbconvert
    ```
2.  Convertissez le ou les notebooks en scripts Python avec
    ```bash
    (venv) [name@server ~]$ jupyter nbconvert --to python mynotebook.ipynb
    ```
3.  Créez le script et soumettez la tâche.

Dans le script de soumission, exécutez le notebook converti avec
```bash
python mynotebook.py
```

Soumettez votre tâche non interactive avec
```bash
sbatch my-submit.sh
```

## Références