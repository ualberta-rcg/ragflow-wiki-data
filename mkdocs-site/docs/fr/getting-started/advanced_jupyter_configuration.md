---
title: "Advanced Jupyter configuration/fr"
tags:
  []

keywords:
  []
---

= Introduction =

* <b>Project Jupyter</b> est un projet open-source sans but lucratif issu en 2014 du IPython Project pour que tous les langages de programmation puissent être utilisés pour la science des données interactives et le calcul scientifique.<ref> Voir https://jupyter.org/about.html.</ref>
* <b>JupyterLab</b> est un environnement de développement web interactif pour les notebooks, le code et les données. La souplesse de son interface permet la configuration et l'utilisation des flux de travail en science des données, en calcul scientifique, en journalisme computationnel et en apprentissage automatique. Sa conception modulaire permet l'ajout d'extensions qui enrichissent ses fonctionnalités.<ref>Voir https://jupyter.org/.</ref>

Un serveur JupyterLab devrait toujours se trouver sur un nœud de calcul ou sur une instance infonuagique. Les nœuds de connexion ne sont pas un bon choix parce qu'ils imposent des limites qui peuvent interrompre une application qui consommerait trop de temps CPU ou de mémoire vive. Pour obtenir un nœud de calcul, vous pouvez réserver des ressources en [soumettant une tâche](running_jobs-fr.md) qui demande un nombre prédéterminé de CPU ou de GPU, une certaine quantité de mémoire et un temps limite d'exécution. <b>Nous décrivons ici comment configurer et soumettre une tâche JupyterLab sur nos grappes nationales.</b>

Si vous recherchez un environnement Jupyter préconfiguré, consultez la page [Jupyter](jupyter-fr.md).

<span id="Installing_JupyterLab"></span>
= Installer JupyterLab =

Ces directives installent JupyterLab avec la commande `pip` dans un
[environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md).

<ol>
<li>Si vous n'avez pas déjà un environnement virtuel Python, créez-en un, puis activez-le.
<ol>
<li>Chargez le module Python par défaut (comme démontré ci-dessous) ou chargez une version spécifique (voir les versions disponibles avec `module avail python`).
```bash
module load python
```

<b>Si vous avez l'intention d'utiliser RStudio Server</b>, chargez d'abord `rstudio-server` avec
```bash
module load rstudio-server python
```

</li><li>Créez un nouvel environnement virtuel Python.
```bash
virtualenv --no-download $HOME/jupyter_py3
```

</li><li>Activez le nouvel environnement virtuel.
```bash
source $HOME/jupyter_py3/bin/activate
```

</li>
</ol>
</li><li>Installez JupyterLab dans votre nouvel environnement virtuel (ceci prendra quelques minutes).
```bash
pip install --no-index jupyterlab
```

</li><li>Dans l'environnement virtuel, créez un script enveloppeur (<i>wrapper</i>) pour le lancement automatique de JupyterLab.
```bash
echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/jupyterlab.sh
```

</li><li>Enfin, rendez ce script exécutable.
```bash
chmod u+x $VIRTUAL_ENV/bin/jupyterlab.sh
```

</li>
</ol>
<span id="Installing_extensions"></span>
= Installer des modules d'extension =

Les modules d'extension ajoutent des fonctionnalités et peuvent modifier l'interface utilisateur de JupyterLab. 

### Jupyter Lmod 

[Jupyter Lmod](https://github.com/cmd-ntrf/jupyter-lmod) est un module d'extension permettant d'interagir avec les modules d'environnement avant le lancement des noyaux (<i>kernels</i>). Il utilise l'interface Python de Lmod pour accomplir des tâches reliées aux modules comme le chargement, le déchargement, la sauvegarde des collections, etc.

Les commandes suivantes installeront et activeront l'extension Jupyter Lmod dans votre environnement (la troisième commande prendra quelques minutes).

```bash
jupyter labextension install jupyterlab-lmod
```

Vous trouverez dans la page [JupyterHub](jupyterhub-fr#jupyterlab.md) les directives pour gérer les <i>modules chargés</i> dans l'interface JupyterLab.

### RStudio Server 

RStudio Server vous permet de développer du code R dans un environnement RStudio, sous un onglet de votre navigateur. Il y a quelques différences avec [la procédure d'installation de JupyterLab](advanced-jupyter-configuration-fr#installer_jupyterlab.md).

<ol>
<li><b>Avant de charger le module `python` et avant de créer un nouvel environnement virtuel</b>, chargez le module `rstudio-server`.
```bash
module load rstudio-server python
```

</li><li>Une fois que [JupyterLab est installé dans le nouvel environnement virtuel](advanced-jupyter-configuration-fr#installer_jupyterlab.md), installez le serveur mandataire (<i>proxy</i>) Jupyter RSession.
```bash
pip install --no-index jupyter-rsession-proxy
```

</li>
</ol>
Toutes les autres étapes de configuration et d'utilisation sont les mêmes. Vous devriez voir une application RStudio sous l'onglet <i>Launcher</i>.

<span id="Using_your_installation"></span>
= Utiliser votre installation =

<span id="Activating_the_environment"></span>
## Activer l'environnement 

Assurez-vous que l'environnement virtuel Python dans lequel vous avez installé JupyterLab est activé. Par exemple, quand vous vous connectez à la grappe, vous devez l'activer à nouveau avec
```bash
source $HOME/jupyter_py3/bin/activate
```

Pour vérifier que votre environnement est prêt, vous pouvez obtenir une liste des paquets `jupyter*` installés avec la commande
```bash

```
 grep jupyter
|result=
jupyter-client==7.1.0+computecanada
jupyter-core==4.9.1+computecanada
jupyter-server==1.9.0+computecanada
jupyterlab==3.1.7+computecanada
jupyterlab-pygments==0.1.2+computecanada
jupyterlab-server==2.3.0+computecanada
}}
<span id="Starting_JupyterLab"></span>
## Lancer JupyterLab 

Pour démarrer un serveur JupyterLab, soumettez une tâche interactive avec `salloc`. Ajustez les paramètres selon vos besoins. Pour plus d'information, voyez [Exécuter des tâches](running-jobs-fr.md).

```bash

```
1:0:0 --ntasks1 --cpus-per-task2 --mem-per-cpu1024M --accountdef-yourpi srun $VIRTUAL_ENV/bin/jupyterlab.sh
|result=
...
[I 2021-12-06 10:37:14.262 ServerApp] jupyterlab  extension was successfully linked.
...
[I 2021-12-06 10:37:39.259 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2021-12-06 10:37:39.356 ServerApp]

    To access the server, open this file in a browser:
        file:///home/name/.local/share/jupyter/runtime/jpserver-198146-open.html
    Or copy and paste one of these URLs:
        http://node_name.int.cluster.computecanada.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
     or http://127.0.0.1:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
}}
<span id="Connecting_to_JupyterLab"></span>
## Se connecter à JupyterLab 

Pour avoir accès au serveur JupyterLab dans un nœud de calcul à partir de votre navigateur web, vous devez créer un [tunnel SSH](ssh-tunnelling-fr.md) de votre ordinateur vers la grappe puisque les nœuds de calcul ne sont pas accessibles directement à partir de l'internet.

<span id="From_Linux_or_macOS"></span>
### Sous Linux ou macOS 

Nous recommandons l'utilisation du paquet Python [sshuttle](https://sshuttle.readthedocs.io).

Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et créez le tunnel SSH avec la commande `sshuttle` où vous remplacerez <code><username></code> par le nom d'utilisateur pour votre compte avec l'Alliance et <code><cluster></code> par la grappe sur laquelle vous avez lancé JupyterLab.

```bash
sshuttle --dns -Nr <username>@<cluster>.alliancecan.ca
```

Copiez et collez la première adresse HTTP dans votre navigateur web; dans l'exemple `salloc` ci-dessus, ce serait
<pre>
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c3688298e78ab554ef86d93a196deaf5bcd2728fad4eb
</pre>
<span id="From_Windows"></span>
### Sous Windows 

Pour créer un [tunnel SSH](ssh-tunnelling-fr.md) à partir de Windows, utilisez [MobaXTerm](connecting_with_mobaxterm-fr.md) ou n’importe quel terminal qui supporte la commande `ssh`.

<ol>
<li>Une fois que JupyterLab est lancé sur un nœud de calcul (voir [Lancer JupyterLab](advanced-jupyter-configuration-fr#lancer_jupyterlab.md)), vous pouvez extraire le `hostname:port` et le `token` de la première adresse HTTP fournie, par exemple<pre>
http://node_name.int.cluster.alliancecan.ca:8888/lab?token=101c368829...2728fad4eb
       └────────────────────┬────────────────────┘           └──────────┬──────────┘
                      hostname:port                                   token
</pre>
</li><li>Ouvrez un nouvel onglet <i>Terminal</i> dans MobaXTerm. Dans la commande suivante, remplacez <code><hostname:port></code> par la valeur correspondante (voir l'image ci-dessus); remplacez <code><username></code> par le nom d'utilisateur pour votre compte avec l'Alliance; remplacez <code><cluster></code> par la grappe sur laquelle vous avez lancé JupyterLab.
```bash
ssh -L 8888:<hostname:port> <username>@<cluster>.alliancecan.ca
```

</li><li>Ouvrez votre navigateur web et allez à l'adresse suivante, où <code><token></code> doit être remplacé par la valeur alphanumérique provenant de l'adresse illustrée ci-dessus.<pre>
http://localhost:8888/?token=<token>
</pre>
</li>
</ol>
<span id="Shutting_down_JupyterLab"></span>
## Fermer JupyterLab 

Pour arrêter le serveur JupyterLab avant la fin du temps d'exécution, appuyez deux fois sur <b>CTRL-C</b> dans le terminal où la tâche interactive a été lancée.

Si vous avez utilisé MobaXterm pour créer un tunnel SSH, appuyez sur <b>Ctrl-D</b> pour fermer le tunnel.

<span id="Adding_kernels"></span>
= Ajouter des noyaux =

Il est possible d'ajouter des noyaux pour d'autres langages de programmation, pour une version différente de Python ou pour un environnement virtuel persistant qui a tous les paquets et bibliothèques nécessaires à votre projet. Pour plus d'information, voyez [Making kernels for Jupyter](http://jupyter-client.readthedocs.io/en/latest/kernels.html).

L'installation d'un nouveau noyau se fait en deux étapes&nbsp;:
# Installation des paquets qui permettent à l'interpréteur du langage de communiquer avec l'interface Jupyter. 
# Création d'un fichier qui indique à JupyterLab comment amorcer un canal de communication avec l'interpréteur du langage. Ce fichier de configuration du noyau (<i>kernel spec file</i>) est sauvegardé dans un sous-répertoire de `~/.local/share/jupyter/kernels`.

Les prochaines sections présentent des exemples de procédures d'installation d'un noyau.

<span id="Julia_Kernel"></span>
## Noyau Julia 

Prérequis :
# La configuration d'un noyau Julia dépend d'un environnement virtuel Python et d'un répertoire `kernels`. Si vous n'avez pas ces dépendances, assurez-vous de suivre les quelques premières directives dans <b>la section <i>Noyau Python</i> ci-dessous</b> (un noyau Python n'est pas requis).
# Puisque l'installation des paquets Julia nécessite un accès à l'internet, la configuration d'un noyau Julia doit se faire <b>[à l'invite de commande sur un nœud de connexion](ssh-fr.md)</b>.

Une fois que l'environnement virtuel Python est disponible et activé, vous pouvez configurer le noyau Julia.

<ol>
<li>Chargez le module <b>[Julia](julia.md)</b>.
```bash
module load julia
```

</li><li>Installez IJulia.
```bash

```
 julia
}}
</li><li><b>Important</b> : Avant d'utiliser le noyau Julia, démarrez ou redémarrez une nouvelle session JupyterLab.</li>
</ol>

Pour plus d'information, consultez la [documentation sur IJulia](https://github.com/JuliaLang/IJulia.jl).

<span id="Installing_more_Julia_packages"></span>
### Installer d'autres paquets Julia 

Comme pour la procédure d'installation ci-dessus, il faut installer les paquets Julia à partir d'un nœud de connexion, mais l'environnement virtuel Python peut rester désactivé.

<ol>
<li>Assurez-vous que le même module Julia est chargé.
```bash
module load julia
```

</li><li>Installez les paquets nécessaires, par exemple `Glob`.
```bash

```
 julia
}}
</li><li>Les paquets Julia nouvellement installés devraient être utilisés dans un notebook exécuté par le noyau Julia.</li>
</ol>

<span id="Python_kernel"></span>
## Noyau Python 

Dans un terminal avec une session active sur un serveur distant,
vous pouvez configurer un  [environnement virtuel Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md) avec tous les [modules Python](available_python_wheels-fr.md) nécessaires et un noyau Python adapté à JupyterLab.
La configuration la plus simple de Jupyter dans un nouvel environnement virtuel Python se fait comme suit&nbsp;:

<ol>
<li>Si vous n'avez pas déjà un environnement virtuel Python, créez-en un, puis activez-le.</li>
<ol>
<li>Commencez à partir d'un environnement Bash vierge (ceci n'est nécessaire que si vous utilisez le <i>Terminal</i> Jupyter via [JupyterHub](jupyterhub-fr.md) pour créer et configurer le noyau Python).
```bash

```
$HOME bash -l
}}
</li><li>Chargez un module Python.
```bash
module load python
```

</li><li>Créez un nouvel environnement virtuel Python.
```bash
virtualenv --no-download $HOME/jupyter_py3
```

</li><li>Activez le nouvel environnement virtuel.
```bash
source $HOME/jupyter_py3/bin/activate
```

</ol>
</li><li>Créez le répertoire commun `kernels` qui est utilisé par tous les noyaux que vous voulez installer.
```bash
mkdir -p ~/.local/share/jupyter/kernels
```

</li><li>Enfin, installez le noyau Python.
<ol>
<li>Installez la bibliothèque `ipykernel`.
```bash
pip install --no-index ipykernel
```

</li><li>Générez le fichier des spécifications du noyau. Remplacez <code><unique_name></code> par un nom spécifique à votre noyau.
```bash
python -m ipykernel install --user --name <unique_name> --display-name "Python 3.x Kernel"
```

</li>
</ol>
</li><li><b>Important</b> : Avant d'utiliser le noyau Python, démarrez ou redémarrez une nouvelle session JupyterLab.</li>
</ol>

Pour plus d'information, consultez la [documentation IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html).

<span id="Installing_more_Python_libraries"></span>
### Installer d'autres bibliothèques Python 

Selon l'environnement virtuel Python configuré dans la section précédente&nbsp;:

<ol><i>Terminal</i> Jupyter via [JupyterHub](jupyterhub-fr.md), assurez-vous que l'environnement virtuel Python est activé et se trouve dans un environnement Bash vierge. Voir la section ci-dessus pour les détails.</li>
<li>Installez une bibliothèque qui serait requise, par exemple `numpy`.
```bash
pip install --no-index numpy
```

</li><li>Vous pouvez maintenant importer les bibliothèques Python dans un notebook exécuté par le `Python 3.x Kernel`.</li>
</ol>

<span id="R_Kernel"></span>
## Noyau R 

Prérequis :
# La configuration d'un noyau R dépend d'un environnement virtuel Python et d'un répertoire `kernels`. Si vous n'avez pas ces dépendances, assurez-vous de suivre les quelques premières directives dans <b>la section <i>Noyau Python</i> ci-dessus</b> (un noyau Python n'est pas requis).
# Puisque l'installation de paquets R nécessite un accès à <b>[CRAN](https://cran.r-project.org/)</b>, la configuration d'un noyau R doit se faire <b>[à l'invite de commande sur un nœud de connexion](ssh-fr.md)</b>.

Une fois que l'environnement virtuel Python est disponible et activé, vous pouvez configurer le noyau R.

<ol>
<li>Chargez un module R.
```bash
module load r/4.1
```

</li><li>Installez les dépendances du noyau R, soit `crayon`, `pbdZMQ` et `devtools`; ceci pourrait prendre jusqu'à 10 minutes et les paquets devraient être installés dans un répertoire local tel que `~/R/x86_64-pc-linux-gnu-library/4.1`.
```bash
R --no-save
```

```
> install.packages(c('crayon', 'pbdZMQ', 'devtools'), repos
</li><li>Installez le noyau R.
```bash
devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))
```

</li><li>Installez le fichier des spécifications du noyau R.
```bash
IRkernel::installspec()
```

</li><li><b>Important</b> : Avant d'utiliser le noyau R, démarrez ou redémarrez une nouvelle session JupyterLab.</li>
</ol>

Pour plus d'information, consultez la [documentation IRkernel](https://irkernel.github.io/docs/).

<span id="Installing_more_R_packages"></span>
### Installer d'autres paquets R 

L'installation de paquets R ne peut se faire à partir de notebooks parce qu'il n'y a pas d'accès à CRAN. Comme dans la procédure d'installation ci-dessus, il faut installer les paquets R dans un nœud de connexion, mais l'environnement virtuel Python peut rester désactivé.

<ol>
<li>Assurez-vous que le même module R module est chargé.
```bash
module load r/4.1
```

</li><li>Démarrez l'interpréteur R et installez les paquets requis. Voici un exemple avec `doParallel`&nbsp;:
```bash
R --no-save
```

```
> install.packages('doParallel', repos
</li><li>Les paquets R nouvellement installés devraient déjà pouvoir être utilisés dans un notebook exécuté par le noyau R.</li>
</ol>

= Exécution de notebooks en scripts Python =
Pour des tâches ou des analyses plus longues, soumettez [une tâche interactive](running_jobs-fr#soumettre_des_tâches_avec_sbatch.md). Il faut alors convertir le notebook en un script Python, créer le script et le soumettre.

1. Dans un nœud de connexion, créez et activez [un environnement virtuel](python-fr#créer_et_utiliser_un_environnement_virtuel.md), installez ensuite <tt>nbconvert</tt> si ce n'est pas déjà installé.

```bash
pip install --no-index nbconvert
```

2. Convertissez le ou les notebooks en scripts Python avec 

```bash
jupyter nbconvert --to python mynotebook.ipynb
```

3. Créez le script et soumettez la tâche.

Dans le script de soumission, exécutez le notebook converti avec
<syntaxhighlight lang="bash">python mynotebook.py</syntaxhighlight>

Soumettez votre tâche non interactive avec

```bash
sbatch my-submit.sh
```

= Références =