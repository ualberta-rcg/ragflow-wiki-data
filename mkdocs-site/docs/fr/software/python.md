---
title: "Python/fr"
slug: "python"
lang: "fr"

source_wiki_title: "Python/fr"
source_hash: "2d19d4051797fcdd7bcd6fe15d7452db"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:39:35.336718+00:00"

tags:
  - software

keywords:
  - "paquets"
  - "$SCRATCH"
  - "Dépannage"
  - "Débogueur Python"
  - "pip"
  - "exécution"
  - "wheel local"
  - "mappage"
  - "protobuf"
  - "répertoire /home"
  - "module multiprocessing"
  - "plusieurs nœuds"
  - "environnement virtuel"
  - "Environnement virtuel"
  - "environnement logiciel"
  - "parallélisation"
  - ".whl"
  - "pdb"
  - "SLURM"
  - "version incompatible"
  - "évalue l'expression"
  - "--no-index"
  - "requirements.txt"
  - "keras"
  - "installer plusieurs paquets"
  - "environnements virtuels Python"
  - "wheels"
  - "code source"
  - "fonction actuelle"
  - "architecture CPU"
  - "pip install"
  - "h5py"
  - "créer un environnement virtuel"
  - "py-spy"
  - "python"
  - "Installation de paquets"
  - "computecanada"
  - "nœud de connexion"
  - "Python"
  - "numpy"
  - "fichier de requis"
  - "--no-binary"
  - "PyPI"
  - "point d'arrêt"
  - "installer des paquets"
  - "paquets Python"
  - "Github"
  - "nœud de calcul"
  - "problèmes de dépendance"
  - "fichier des requis"
  - "répertoires /project"
  - "brise l'ABI"
  - "script de soumission"
  - "module Python"
  - "programmation parallèle"
  - "wheel"
  - "prétélécharger des paquets"
  - "Paquets Python"
  - "dépôt à distance"
  - "wheels Python"
  - "wheels disponibles"
  - "cœurs"
  - "paquet"
  - "multiprocessing"
  - "pip download"
  - "version Python"
  - "netCDF4"
  - "Pile logicielle SciPy"
  - "classe Pool"
  - "boucle"
  - "avail_wheels"
  - "installation locale"
  - "Numpy"
  - "débogage"
  - "tensorboardX"
  - "Interpréteur Python"
  - "paquets locaux"
  - "dépendances"

questions:
  - "Pourquoi les paquets Python développés par des tiers ne sont-ils pas installés par défaut sur les grappes ?"
  - "Comment peut-on chercher et charger une version spécifique de l'interpréteur Python ou la pile logicielle SciPy ?"
  - "Quel est le rôle des environnements virtuels et dans quels répertoires est-il conseillé ou déconseillé de les créer ?"
  - "Quels sont les répertoires recommandés pour créer des environnements virtuels Python ?"
  - "Quelle est la troisième option mentionnée pour la création d'un environnement virtuel ?"
  - "Pourquoi est-il fortement déconseillé de créer un environnement virtuel dans le répertoire $SCRATCH ?"
  - "Quelles sont les étapes à suivre pour créer, activer et quitter un environnement virtuel Python ?"
  - "Comment procède-t-on pour installer un nouveau paquet Python, tel que NumPy, dans un environnement virtuel actif ?"
  - "Pourquoi est-il fortement recommandé d'utiliser l'option `--no-index` avec la commande pip sur ces grappes de serveurs ?"
  - "Quel problème peut survenir si la version la plus récente d'un paquet provient de PyPI plutôt que des paquets locaux ?"
  - "Quelle option de la commande pip faut-il utiliser pour ignorer les paquets préconstruits (wheels) ?"
  - "Comment le paquet est-il installé lorsque l'option --no-binary est activée ?"
  - "Pourquoi est-il souvent plus efficace de créer un environnement virtuel Python directement sur le disque local du nœud de calcul plutôt que d'utiliser le système de fichiers parallèles ?"
  - "Quelle est la procédure recommandée pour générer le fichier `requirements.txt` sur un nœud de connexion avant de soumettre une tâche ?"
  - "Quelle recommandation particulière s'applique à la création et à l'activation d'environnements virtuels spécifiquement sur la grappe Trillium ?"
  - "What is the significance of the `+computecanada` suffix attached to the version numbers of these Python packages?"
  - "Based on the inclusion of packages like Keras, NumPy, and h5py, what type of computational tasks is this environment primarily configured for?"
  - "How can a user replicate or install this specific list of dependencies in a different Python environment?"
  - "Que doit-on faire si un paquet requis n'est pas disponible dans les wheels Python fournis par le système ?"
  - "Comment configurer et activer correctement un environnement virtuel Python lors de l'exécution d'une tâche sur plusieurs nœuds ?"
  - "Quelles informations la commande `avail_wheels` affiche-t-elle par défaut concernant les paquets Python disponibles sur la grappe ?"
  - "Comment utiliser les opérateurs de format pip avec la commande avail_wheels pour filtrer les versions d'un paquet ?"
  - "Quelle est la méthode pour vérifier quels paquets d'un fichier requirements.txt sont disponibles ou manquants ?"
  - "Comment prétélécharger un paquet Python sur un nœud de connexion pour une installation ultérieure sur un nœud de calcul ?"
  - "Quels éléments définissent la compatibilité des versions avec le système en cours d'utilisation ?"
  - "Quelle commande permet de rechercher la liste des wheels contenant une chaîne de caractères spécifique dans leur nom ?"
  - "Quelles informations précises sont renvoyées par la commande de recherche pour chaque wheel listé ?"
  - "Quel est l'objectif principal de la procédure décrite concernant le paquet tensorboardX ?"
  - "Quelle commande exacte doit être utilisée pour télécharger le paquet dans le répertoire de travail ?"
  - "À quelle autre commande la syntaxe de « pip download » est-elle identique selon le texte ?"
  - "Que faut-il faire si le nom d'un fichier wheel se termine par linux_x86_64 ou manylinux*_x86_64 au lieu de none-any ?"
  - "Pourquoi est-il fortement recommandé d'utiliser un tag ou un identifiant de validation (commit ID) lors de l'installation d'un paquet à partir d'un dépôt distant ?"
  - "Quelles sont les étapes pour créer et installer un wheel local à partir d'un code source que l'on a préalablement modifié ?"
  - "Quel module et quelle classe Python sont présentés pour exécuter des calculs en parallèle sur des données multiples ?"
  - "Quelles sont les conséquences sur les performances et les ressources si le nombre de processus exécutés ne correspond pas au nombre de cœurs alloués par l'ordonnanceur ?"
  - "Comment peut-on configurer dynamiquement le script Python pour qu'il récupère et utilise le nombre exact de cœurs définis par la tâche SLURM ?"
  - "Comment peut-on installer un paquet local au format `.whl` dans un environnement virtuel à l'aide de pip ?"
  - "De quelle manière peut-on inclure un fichier `.whl` spécifique directement dans un fichier `requirements.txt` ?"
  - "Quelle option doit-on utiliser pour geler l'état de l'environnement virtuel lors de la création d'un fichier de requis ?"
  - "Comment le script Python utilise-t-il le module multiprocessing pour calculer les cubes de la liste de données ?"
  - "De quelle manière le code détermine-t-il le nombre de processeurs à allouer au pool via les variables d'environnement ?"
  - "Quelle est la différence conceptuelle entre l'approche \"Avec une boucle\" utilisant apply_async et l'approche \"Par mappage\" suggérée par les onglets ?"
  - "Pourquoi faut-il vérifier si les fonctions externes utilisées sont déjà parallélisées avant de lancer de multiples processus avec le module multiprocessing ?"
  - "Quelles solutions alternatives sont suggérées pour paralléliser un code sur plusieurs nœuds de calcul au lieu d'un seul ?"
  - "Quelles sont les étapes et les commandes principales pour déboguer un script Python de manière interactive à l'aide de pdb ?"
  - "Comment peut-on s'attacher à un processus Python en cours d'exécution pour le déboguer avec PDB ?"
  - "Quels outils peuvent être utilisés pour inspecter et diagnostiquer un script Python qui reste suspendu ou bloqué ?"
  - "Quelles sont les solutions recommandées pour résoudre les erreurs courantes de dépendances ou de paquets introuvables lors de l'utilisation de pip ?"
  - "Quelle commande doit-on utiliser pour continuer l'exécution du programme jusqu'à ce qu'il rencontre un point d'arrêt ?"
  - "Comment est-il possible d'évaluer une expression et d'afficher sa valeur dans le contexte actuel ?"
  - "Quelle commande permet d'afficher le code source du fichier en cours d'analyse ?"
  - "Comment peut-on consulter la liste des \"wheels\" disponibles ?"
  - "Quelle est la méthode recommandée pour installer plusieurs paquets ?"
  - "Pourquoi est-il préférable d'installer plusieurs paquets avec une seule commande ?"
  - "Pourquoi un environnement virtuel peut-il cesser de fonctionner soudainement et comment peut-on prévenir ce problème ?"
  - "Quelles sont les causes fréquentes d'une erreur d'importation de module ou d'incompatibilité de paquet (wheel), et quelles vérifications permettent de les résoudre ?"
  - "Comment doit-on gérer les erreurs d'attributs ou d'importation spécifiquement liées aux différentes versions de la bibliothèque Numpy ?"
  - "Quelle est la cause principale de l'erreur mentionnée concernant la dépendance à Numpy ?"
  - "Quel problème technique spécifique la version 2.0 de Numpy provoque-t-elle ?"
  - "Quelle commande exacte doit-on exécuter pour résoudre le conflit entre un wheel construit avec la version 1.x et une installation de la version 2.x ?"
  - "Pourquoi le message « Defaulting to user installation... » s'affiche-t-il lors de l'utilisation de pip ?"
  - "Quels sont les risques et les problèmes engendrés par une installation locale de paquets Python ?"
  - "Comment procéder pour supprimer correctement une installation locale et éviter les conflits de dépendances ?"
  - "Pourquoi le message « Defaulting to user installation... » s'affiche-t-il lors de l'utilisation de pip ?"
  - "Quels sont les risques et les problèmes engendrés par une installation locale de paquets Python ?"
  - "Comment procéder pour supprimer correctement une installation locale et éviter les conflits de dépendances ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

!!! note "Formation"
Cliquez ici pour connaître les événements affichés par [Explora](https://explora.alliancecan.ca/events?q=Python).

## Description
[Python](http://www.python.org/) est un langage de programmation interprété dont la philosophie de design repose principalement sur la lisibilité du code. Sa syntaxe est simple et expressive et sa bibliothèque de modules standards est très étendue.

Les capacités du langage Python peuvent être étendues à l'aide de paquets développés par des tiers. En général, nous n'installons pas les paquets de tiers dans le répertoire de logiciels disponibles afin de simplifier le plus possible les opérations; il vous revient donc de les installer. En revanche, nous mettons à votre disposition plusieurs versions de l'interpréteur Python et les outils nécessaires pour que vous puissiez facilement installer les paquets dont vous avez besoin.

Les sections suivantes présentent l'interpréteur Python et expliquent comment installer et utiliser les paquets.

## Charger l'interpréteur

### Version par défaut
Une version est disponible quand vous vous connectez à nos grappes, mais vous aurez souvent besoin d'une version différente, surtout si vous voulez installer des paquets. Trouvez la version de Python dont vous avez besoin et [chargez le module approprié](../programming/utiliser_des_modules.md). En cas de doute, vous pouvez utiliser la plus récente version disponible.mpi4py comme dépendance d'un autre paquet.

### Charger un module Python
Pour connaître les versions disponibles, utilisez
```bash
module avail python
```

Vous pouvez ensuite charger la version de votre choix avec la commande `module load`, par exemple,
```bash
module load python/X.Y
```
où `X.Y` représente la version, par exemple `3.13`.

### Version prise en charge
En règle générale dans l'écosystème Python, la transition vers des versions plus modernes s'accélère et plusieurs paquets ne supportent que les quelques dernières versions de Python 3.x. Dans notre cas, nous offrons uniquement des paquets préconstruits ([wheels Python](../programming/available_python_wheels.md)) pour les trois versions les plus récentes disponibles sur nos systèmes. Des problèmes de dépendance se présenteront quand vous tentez d'installer ces paquets avec les plus anciennes versions de Python. Voir [la section Dépannage](#message-package-x-requires-a-different-python-xyz-not-in-xy).

### Pile logicielle SciPy

En plus du module Python de base, le paquet [SciPy](https://www.scipy.org/) est aussi disponible comme [module d'environnement](../programming/utiliser_des_modules.md). Le module `scipy-stack` comprend
* NumPy
* SciPy
* Matplotlib
  * dateutil
  * pytz
* IPython
  * pyzmq
  * tornado
* pandas
* Sympy
* nose

Pour utiliser un de ces paquets, chargez une version de Python, puis `module load scipy-stack`.

Pour la liste et les numéros de version des paquets contenus dans `scipy-stack`, lancez `module spider scipy-stack/2020a`, en remplaçant `2020a` par la version que vous voulez.

## Créer et utiliser un environnement virtuel

Avec chaque version de Python vient l'outil [virtualenv](http://pypi.python.org/pypi/virtualenv) qui permet de créer des environnements virtuels à l'intérieur desquels vous pourrez installer facilement vos paquets Python. Ces environnements permettent par exemple d'installer plusieurs versions d'un même paquet, ou encore de compartimenter les installations en fonction des besoins ou des expériences à réaliser. Vous devriez habituellement créer vos environnements virtuels Python dans votre répertoire /home ou dans un de vos répertoires /project. Pour une troisième option, voyez ci-dessous la section *Créer un environnement virtuel dans vos tâches*.

!!! warning "Où créer un environnement virtuel"
    Ne créez pas votre environnement virtuel dans `$SCRATCH` à cause du risque qu'il soit en partie détruit.
    Voyez plutôt [Créer un environnement virtuel dans vos tâches](#créer-un-environnement-virtuel-dans-vos-tâches) ci-dessous.

Pour créer un environnement virtuel, sélectionnez d'abord une version de Python avec `module load python/X.Y.Z`, comme indiqué ci-dessus dans *Charger un module Python*. Si vous voulez utiliser les paquets listés dans *Pile logicielle SciPy*, lancez aussi `module load scipy-stack/X.Y.Z`. Entrez ensuite la prochaine commande, où `ENV` est le nom du répertoire pour votre nouvel environnement.
```bash
virtualenv --no-download ~/ENV
```

Une fois l'environnement virtuel créé, il ne vous reste plus qu'à l'activer avec
```bash
source ~/ENV/bin/activate
```

Vous devriez aussi faire la mise à jour de `pip` dans l'environnement.

```bash
pip install --no-index --upgrade pip
```

Pour quitter l'environnement virtuel, entrez simplement la commande
```bash
deactivate
```

Pour réutiliser l'environnement virtuel :
1.  Chargez les mêmes modules d'environnement que vous avez chargés quand l'environnement virtuel a été créé, soit `module load python scipy-stack`.
2.  Activez l'environnement avec `source ENV/bin/activate`.

### Installer des paquets

Une fois que vous avez chargé un environnement virtuel, vous pouvez lancer la commande [pip](http://www.pip-installer.org/). Cette commande prend en charge la compilation et l'installation de la plupart des paquets Python et de leurs dépendances. Consultez [l'index complet des paquets Python](https://pypi.python.org/pypi).

Les commandes disponibles sont expliquées dans le [manuel d'utilisation pip](https://pip.pypa.io/en/stable/user_guide/). Nous mentionnons ici les commandes les plus importantes en présentant un exemple d'installation du paquet [NumPy](http://numpy.scipy.org/).

Chargeons d'abord l'interpréteur Python avec
```bash
module load python/X.Y
```
où `X.Y` représente la version, par exemple `3.13`.

Ensuite, activons l'environnement virtuel créé précédemment avec la commande `virtualenv`.
```bash
source ~/ENV/bin/activate
```
Enfin, nous pouvons installer la dernière version stable de NumPy avec
```bash
pip install numpy --no-index
```

La commande `pip` peut installer des paquets à partir de plusieurs sources, dont PyPI et les paquets de distribution préconstruits appelés [Python wheels](https://pythonwheels.com/). Nous fournissons des wheels Python pour plusieurs paquets. Dans l'exemple ci-dessus, l'option [--no-index](https://pip.pypa.io/en/stable/reference/pip_wheel/#cmdoption-no-index) demande à `pip` de *ne pas installer* à partir de PyPI, mais plutôt de n'installer qu'à partir de paquets de source locale, soit de nos wheels.

Si un de nos wheels est disponible pour un paquet que vous voulez, nous vous recommandons fortement de l'utiliser avec l'option `--no-index`. Contrairement aux paquets de PyPI, les wheels compilés par notre personnel évitent les problèmes de dépendances manquantes ou conflictuelles et sont de plus optimisés pour nos grappes et nos bibliothèques. Voyez [Wheels disponibles](#wheels-disponibles).

Si vous omettez l'option `--no-index`, `pip` cherchera les paquets PyPI et les paquets locaux et utilisera la version la plus récente. Si celle-ci est de PyPI, elle sera installée plutôt que la nôtre et vous aurez possiblement des problèmes. Si vous préférez télécharger un paquet PyPI plutôt que d'utiliser un wheel, utilisez l'option `--no-binary` qui demande à `pip` de ne considérer aucun paquet préconstruit; ainsi, les wheels distribués via PyPI ne seront pas considérés et le paquet sera toujours compilé de la source.

Pour savoir d'où provient le paquet Python installé par `pip`, ajoutez l'option `-vvv`. Lorsque vous installez plusieurs paquets Python, il est préférable de les installer en une seule étape, puisque `pip` peut alors résoudre les dépendances croisées.

### Créer un environnement virtuel dans vos tâches

**Attention :** Sur Trillium, il est recommandé de créer un environnement virtuel sur un nœud de connexion dans /home et d'activer cet environnement (avec `source`) dans le script de la tâche.

Les systèmes de fichiers parallèles comme ceux qui sont installés sur nos grappes sont très efficaces lorsqu'il s'agit de lire ou d'écrire de grandes portions de données, mais pas pour une utilisation intensive de petits fichiers. Pour cette raison, le lancement d'un logiciel et le chargement de bibliothèques peuvent être lents, ce qui se produit quand on lance Python et qu'on charge un environnement virtuel.

Pour contrer ce genre de ralentissement, particulièrement pour les tâches Python sur un nœud unique, vous pouvez créer votre environnement virtuel à l'intérieur de votre tâche en utilisant le disque local du nœud de calcul. Il peut sembler déraisonnable de recréer votre environnement pour chacune de vos tâches, mais c'est souvent plus rapide et plus efficace que d'utiliser le système de fichiers parallèles. Il faut créer un virtualenv localement sur chacun des nœuds utilisés par la tâche puisque l'accès à virtualenv se fait par nœud. Le script suivant en est un exemple.

```sh title="submit_venv.sh"
#!/bin/bash
#SBATCH --account=def-compte
#SBATCH --mem-per-cpu=1500M     # à augmenter au besoin
#SBATCH --time=1:00:00

module load python/3.11
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt
python ...
```
où le fichier `requirements.txt` aura été créé dans un environnement de test. Par exemple, pour créer un environnement pour [TensorFlow](tensorflow.md), utilisez les commandes suivantes dans un nœud de connexion :
```bash
module load python/3.11
```
```bash
ENVDIR=/tmp/$RANDOM
```
```bash
virtualenv --no-download $ENVDIR
```
```bash
source $ENVDIR/bin/activate
```
```bash
pip install --no-index --upgrade pip
```
```bash
pip install --no-index tensorflow
```
```bash
pip freeze --local > requirements.txt
```
```bash
deactivate
```
```bash
rm -rf $ENVDIR
```

Ceci produit le fichier `requirements.txt` dont le contenu ressemble à ceci :
```text title="requirements.txt"
absl_py==1.2.0+computecanada
astunparse==1.6.3+computecanada
cachetools==5.2.0+computecanada
certifi==2022.6.15+computecanada
charset_normalizer==2.1.0+computecanada
flatbuffers==1.12+computecanada
gast==0.4.0+computecanada
google-pasta==0.2.0+computecanada
google_auth==2.9.1+computecanada
google_auth_oauthlib==0.4.6+computecanada
grpcio==1.47.0+computecanada
h5py==3.6.0+computecanada
idna==3.3+computecanada
keras==2.9.0+computecanada
Keras-Preprocessing==1.1.2+computecanada
libclang==14.0.1+computecanada
Markdown==3.4.1+computecanada
numpy==1.23.0+computecanada
oauthlib==3.2.0+computecanada
opt-einsum==3.3.0+computecanada
packaging==21.3+computecanada
protobuf==3.19.4+computecanada
pyasn1==0.4.8+computecanada
pyasn1-modules==0.2.8+computecanada
pyparsing==3.0.9+computecanada
requests==2.28.1+computecanada
requests_oauthlib==1.3.1+computecanada
rsa==4.8+computecanada
six==1.16.0+computecanada
tensorboard==2.9.1+computecanada
tensorboard-data-server==0.6.1+computecanada
tensorboard_plugin_wit==1.8.1+computecanada
tensorflow==2.9.0+computecanada
tensorflow_estimator==2.9.0+computecanada
tensorflow_io_gcs_filesystem==0.23.1+computecanada
termcolor==1.1.0+computecanada
typing_extensions==4.3.0+computecanada
urllib3==1.26.11+computecanada
Werkzeug==2.1.2+computecanada
wrapt==1.13.3+computecanada
```

Ce fichier fait en sorte que votre environnement puisse être reproduit pour les autres tâches.

Remarquez que les directives ci-dessus exigent que tous les paquets dont vous avez besoin soient disponibles dans les wheels Python que nous fournissons. Si ce n'est pas le cas, vous pouvez le prétélécharger (voir *Prétélécharger des paquets* ci-dessous). Si vous croyez que les wheels devraient être fournis, faites-en la demande au [soutien technique](../support/technical_support.md)

#### Créer un environnement virtuel dans vos tâches (plusieurs nœuds)

Pour que vos scripts utilisent plusieurs nœuds, chacun doit avoir son propre environnement activé.

1.  Dans votre script de soumission de la tâche, créez l'environnement virtuel pour chacun des nœuds alloués.
```bash
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r requirements.txt

EOF
```

2.  Activez l'environnement virtuel du nœud principal.
```bash
source $SLURM_TMPDIR/env/bin/activate;
```

3.  Exécutez le script avec
```bash
srun python myscript.py;
```

#### Exemple (plusieurs nœuds)
```bash title="submit-nnodes-venv.sh"
#!/bin/bash
#SBATCH --account=<your account>
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=2000M

module load StdEnv/2023 python/3.11 mpi4py/4.0.3

# create the virtual environment on each allocated node
srun --ntasks $SLURM_NNODES --tasks-per-node=1 bash << EOF
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r requirements.txt
EOF

# activate only on the main node                                                               
source $SLURM_TMPDIR/env/bin/activate;
# srun exports the current env, which contains $VIRTUAL_ENV and $PATH variables
srun python myscript-mpi.py;
```

### Wheels disponibles
Les wheels présentement disponibles sont listés sur la page [Wheels Python](../programming/available_python_wheels.md). Vous pouvez aussi utiliser la commande `avail_wheels` sur la grappe.
Par défaut, cette commande montre seulement
* la **plus récente version** d'un paquet en particulier, à moins qu'une version particulière n'ait été spécifiée;
* les versions compatibles avec le module Python chargé ou l'environnement virtuel activé; autrement, toutes les versions sont affichées;
* les versions compatibles avec l'architecture CPU et l'environnement logiciel (StdEnv) que vous utilisez à ce moment.

#### Noms
Pour la liste des wheels qui contiennent `cdf` (insensible à la casse) dans leur nom, lancez
```bash
avail_wheels "*cdf*"
```
```text
name      version    python    arch
--------  ---------  --------  -------
h5netcdf  0.7.4      py2,py3   generic
netCDF4   1.5.8      cp39      avx2
netCDF4   1.5.8      cp38      avx2
netCDF4   1.5.8      cp310     avx2
```

ou utilisez le nom exact, par exemple
```bash
avail_wheels numpy
```
```text
name    version    python    arch
------  ---------  --------  -------
numpy   1.23.0     cp39      generic
numpy   1.23.0     cp38      generic
numpy   1.23.0     cp310     generic
```

#### Version
Pour la liste d'une version particulière, vous pouvez utiliser le même format qu'avec `pip` :
```bash
avail_wheels numpy==1.23
```
```text
name    version    python    arch
------  ---------  --------  -------
numpy   1.23.0     cp39      generic
numpy   1.23.0     cp38      generic
numpy   1.23.0     cp310     generic
```
ou employer la version plus longue, comme
```bash
avail_wheels numpy --version 1.23
```
```text
name    version    python    arch
------  ---------  --------  -------
numpy   1.23.0     cp39      generic
numpy   1.23.0     cp38      generic
numpy   1.23.0     cp310     generic
```
Avec le format `pip`, vous pouvez utiliser différents opérateurs : `==`, `<`, `>`, `~=`, `<=`, `>=`, `!=`, pour lister par exemple les versions précédentes,
```bash
avail_wheels 'numpy<1.23'
```
```text
name    version    python    arch
------  ---------  --------  -------
numpy   1.22.2     cp39      generic
numpy   1.22.2     cp38      generic
numpy   1.22.2     cp310     generic
```
et pour lister toutes les versions disponibles,
```bash
avail_wheels "*cdf*" --all-version
```
```text
name      version    python    arch
--------  ---------  --------  -------
h5netcdf  0.7.4      py2,py3   generic
netCDF4   1.5.8      cp39      avx2
netCDF4   1.5.8      cp38      avx2
netCDF4   1.5.8      cp310     avx2
netCDF4   1.5.6      cp38      avx2
netCDF4   1.5.6      cp37      avx2
netCDF4   1.5.4      cp38      avx2
netCDF4   1.5.4      cp37      avx2
netCDF4   1.5.4      cp36      avx2
```

#### Python
Pour lister une version particulière de Python, lancez
```bash
avail_wheels 'numpy<1.23' --python 3.9
```
```text
name    version    python    arch
------  ---------  --------  -------
numpy   1.22.2     cp39      generic
```
La colonne *python* montre la version de Python pour laquelle le wheel est disponible, où `cp39` est utilisé pour `cpython 3.9`.

#### Fichier de requis
Pour savoir si les wheels disponibles incluent ceux qui sont indiqués dans le fichier `requirements.txt`, lancez
```bash
avail_wheels -r requirements.txt
```
```text
name       version    python    arch
---------  ---------  --------  -------
packaging  21.3       py3       generic
tabulate   0.8.10     py3       generic
```
Pour la liste de ceux qui ne sont pas disponibles, la commande est
```bash
avail_wheels -r requirements.txt --not-available
```
```text
name       version    python    arch
---------  ---------  --------  -------
packaging  21.3       py3       generic
pip
tabulate   0.8.10     py3       generic
```

### Prétélécharger des paquets

La procédure suivante prétélécharge le paquet `tensorboardX` sur un nœud de connexion et l'installe sur un nœud de calcul :

1.  Lancez `pip download --no-deps tensorboardX` pour télécharger le paquet `tensorboardX-1.9-py2.py3-none-any.whl` (ou semblable) dans le répertoire de travail. La syntaxe pour `pip download` est la même que celle pour `pip install`.
2.  Si le nom du fichier ne se termine pas par `none-any`, mais par `linux_x86_64` ou `manylinux*_x86_64`, il est possible que le wheel ne fonctionne pas correctement. Contactez le [soutien technique](../support/technical_support.md) pour que nous le compilions et qu'il soit rendu disponible sur nos superordinateurs.
3.  À l'installation, utilisez le chemin du fichier `pip install tensorboardX-1.9-py2.py3-none-any.whl`.

### Installer à partir d'un dépôt à distance (Github)

Dans certains cas, le paquet source ne se trouve pas dans l'index PyPI, mais est disponible dans un autre dépôt distant.
Ce dépôt distant peut être Git, Subversion, Bazaar ou Mercurial; nous traitons ici de Git.

En utilisant l'URL pour le dépôt distant, vous pouvez spécifier
* un nom de branche (*the-best-feature*)
* un *tag* (*v1.0.1*)
* un identifiant de validation court ou long (*da39a3ee5e6b4b0d3255bfef95601890afd80709*)
* une référence, par exemple une requête *pull* (*refs/pull/123/head*)

Dans un environnement virtuel activé,
```bash
pip install git+https://git.example.com/MyProject.git@v1.0
```

Il est **important** d'utiliser un *tag* (version) ou un ID de validation pour obtenir une installation pouvant être reproduite.
Si vous utilisez le `HEAD` du dépôt, cela pourrait fonctionner mais vous risquez d'avoir éventuellement des problèmes puisque des modifications ont été faites.

Sur Github, les *tags* ou versions se trouvent dans la section *Releases* dans le panneau de gauche.

Pour plus d'information sur l'installation à partir d'un système de contrôle de versions (VCS), voir [vcs-support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support).

### Créer un wheel local

Dans certains contextes,
* certains paquets ne sont disponibles que depuis un dépôt distant (par exemple GitHub) sans indication de version, d’étiquette ni de mise en production;
* ou bien, vous devez modifier le code source.
Dans ce cas, vous pouvez créer un wheel local pour pouvoir reproduire vos tâches.

En vous basant sur [Installer à partir d'un dépôt à distance (Github)](#installer-à-partir-dun-dépôt-à-distance-github), vous pouvez créer un wheel local à partir d'un dépôt distant, avec un environnement virtuel activé :
```bash
pip wheel --no-deps -w $HOME git+https://git.example.com/MyProject.git@<commit id>
```
Cette commande clone et extrait le dépôt à l'emplacement indiqué (tag, identifiant de commit, etc.), puis pip crée un wheel dans le répertoire wheel (`$HOME`).

Pour modifier les fichiers source, clônez d'abord le dépôt.
```bash
git clone https://git.example.com/MyProject.git
```
```bash
cd MyProject
```
```bash
git checkout <commit id>
```
```bash
... # make any edits
```
Créez ensuite le wheel local.
```bash
pip wheel --no-deps -w $HOME .
```

Enfin, avec le wheel local, vous pouvez l'installer dans votre environnement virtuel.
```bash
pip install $HOME/MyProject-1.0.0-py3-none.whl
```
Ou encore, l'ajouter au fichier des requis.
```text title="requirements.txt"
~/MyProject-1.0.0-py3-none.whl
torch-2.11.0+computecanada-cp314-cp314-linux_x86_64.whl
```

Pour créer un fichier de requis, utilisez `--no-index` et *gelez* l'état de votre environnement virtuel.
```bash
pip install --no-index $HOME/MyProject-1.0.0-py3-none.whl
```
```bash
pip freeze --local > ~/requirements.txt
```
Voir aussi [Créer un environnement virtuel dans vos tâches](#créer-un-environnement-virtuel-dans-vos-tâches).

## Programmation parallèle avec le module `multiprocessing`

La programmation parallèle avec Python est un moyen facile d'obtenir des résultats plus rapidement, ce qui est habituellement accompli avec l'utilisation du module [multiprocessing](https://sebastianraschka.com/Articles/2014_multiprocessing.html). La classe `Pool` de ce module est particulièrement intéressante car elle permet de contrôler le nombre de processus lancés en parallèle pour exécuter le même calcul avec des données multiples. Supposons que nous voulons calculer le `cube` d'une liste de nombres; le code série serait semblable à :
=== "Avec une boucle"
```python title="cubes_sequential.py"
def cube(x):
    return x**3

data = [1, 2, 3, 4, 5, 6]
cubes = [cube(x) for x in data]
print(cubes)
```
=== "Par mappage"
```python title="cubes_sequential.py"
def cube(x):
    return x**3

data = [1, 2, 3, 4, 5, 6]
cubes = list(map(cube,data))
print(cubes)
```

Avec la classe `Pool` le code parallèle devient :
=== "Avec une boucle"
```python title="cubes_parallel.py"
import multiprocessing as mp

def cube(x):
    return x**3

pool = mp.Pool(processes=4)
data = [1, 2, 3, 4, 5, 6]
results = [pool.apply_async(cube, args=(x,)) for x in data]
cubes = [p.get() for p in results]
print(cubes)
```
=== "Par mappage"
```python title="cubes_parallel.py"
import multiprocessing as mp

def cube(x):
    return x**3

pool = mp.Pool(processes=4)
data = [1, 2, 3, 4, 5, 6]
cubes = pool.map(cube, data)
print(cubes)
```

Dans les exemples précédents, nous sommes toutefois limités à quatre processus. Avec une grappe, il est très important d'utiliser les cœurs qui sont alloués à la tâche. Si le nombre de processus exécutés dépasse le nombre de cœurs demandé pour la tâche, les calculs s'effectueront plus lentement et le nœud de calcul sera possiblement surchargé. Si le nombre de processus exécutés est inférieur au nombre de cœurs demandé, certains cœurs resteront inactifs et les ressources ne seront pas utilisées de façon optimale. Votre code devrait faire appel à autant de cœurs que la quantité de ressources demandées à l'ordonnanceur. Par exemple, pour exécuter le même calcul sur des dizaines de données ou plus, il serait sensé d'utiliser tous les cœurs d'un nœud. Dans ce cas, le script de soumission de la tâche aurait l'en-tête suivant :
```bash title="submit.sh"
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32

python cubes_parallel.py
```
Le code serait alors :
=== "Avec une boucle"
```python title="cubes_parallel.py"
import multiprocessing as mp
import os

def cube(x):
    return x**3

ncpus = int(os.environ.get('SLURM_CPUS_PER_TASK',default=1))
pool = mp.Pool(processes=ncpus)
data = [1, 2, 3, 4, 5, 6]
results = [pool.apply_async(cube, args=(x,)) for x in data]
cubes = [p.get() for p in results]
print(cubes)
```
=== "Par mappage"
```python title="cubes_parallel.py"
import multiprocessing as mp
import os

def cube(x):
    return x**3

ncpus = int(os.environ.get('SLURM_CPUS_PER_TASK',default=1))
pool = mp.Pool(processes=ncpus)
data = [1, 2, 3, 4, 5, 6]
cubes = pool.map(cube, data)
print(cubes)
```

Remarquez que dans cet exemple, la fonction `cube` est en elle-même séquentielle. Il est possible qu'une fonction appelée d'une bibliothèque externe comme `numpy` soit en elle-même parallèle. Pour distribuer des processus avec la technique précédente, vérifiez d'abord si les fonctions appelées sont en elles-mêmes parallèles et si c'est le cas, vous devrez contrôler le nombre de fils qu'elles utiliseront. Si comme dans l'exemple les fonctions utilisent la totalité des cœurs disponibles (ici 32) et que vous lancez 32 processus, votre code sera plus lent et le nœud sera possiblement surchargé.

Comme le module `multiprocessing` ne peut utiliser qu'un seul nœud de calcul, le gain en performance est habituellement limité au nombre de cœurs CPU du nœud. Si vous voulez dépasser cette limite et utiliser plusieurs nœuds, considérez mpi4py ou [PySpark](apache_spark.md#pyspark). Il existe [d'autres méthodes de parallélisation](https://wiki.python.org/moin/ParallelProcessing), mais elles ne peuvent pas toutes être utilisées avec nos grappes. Souvenez-vous toutefois qu'un code de qualité fournira toujours la meilleure performance; avant de le paralléliser, assurez-vous donc que votre code est optimal. Si vous doutez de l'efficacité de votre code, contactez le [soutien technique](../support/technical_support.md).

## Anaconda
Voir la page sur [Anaconda](anaconda.md).

## Jupyter
Voir la page sur [Jupyter Notebook](../interactive/jupyternotebook.md).

## Débogage

Déboguer votre code Python n'est pas toujours évident. Des méthodes simples, comme l'ajout d'un `print` ou d'une assertion (`assert`), peuvent vous aider à corriger certaines erreurs.

Toutefois, il est souvent nécessaire d'explorer le code et son contexte plus en profondeur; l'utilisation d'un débogueur comme `pdb` est alors plus simple.

Vous pouvez déboguer votre code Python grâce à [une petite tâche interactive](../running-jobs/running_jobs.md#tâches-interactives).

1.  Ajoutez `import pdb; pdb.set_trace()` au début de votre fichier ou ajoutez `breakpoint()` à l'endroit approprié.
2.  Exécutez votre code (`python ...`).
3.  Vous vous trouverez alors dans le débogueur où vous pourrez analyser et évaluer les expressions.

**Commandes utiles**
| Commande | Description                                                                                                                                              |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| w (pour *where*) | Affiche une trace de la pile d'exécution, avec la plus récente fenêtre dans le bas. Une flèche (>) indique la fenêtre actuelle, ce qui détermine le contexte de la plupart des commandes. |
| b (pour *break*) | Avec un argument `lineno`, insère un saut au numéro de ligne dans le fichier actuel.                                                                   |
| s (pour *step*) | Exécute la ligne actuelle, s'arrête à la première occasion (soit dans une fonction appelée, soit sur la ligne suivante dans la fonction actuelle).    |
| n (pour *next*) | Continue l'exécution jusqu'à ce que la ligne suivante de la fonction actuelle soit atteinte ou qu'elle retourne à la ligne précédente.                  |
| r (pour *return*) | Continue l'exécution jusqu'à la fin de la fonction actuelle.                                                                                           |
| c (pour *continue*) | Continue l'exécution et s'arrête uniquement à un point d'arrêt (*breakpoint*).                                                                       |
| p exp    | Évalue l'expression dans le contexte actuel et affiche sa valeur.                                                                                          |
| l (pour *list*) | Affiche le code source du fichier actuel.                                                                                                                |
| q (pour *quit*) | Quitte le débogueur. Le programme en cours d'exécution est arrêté.                                                                                    |

En général, on utilise `w`, `s`, `l`, `p`, `n` pour déboguer un fichier.

Pour plus d'information, voir [*The Python Debugger*](https://docs.python.org/3/library/pdb.html).

## S'attacher à un processus en cours
Avec **Python 3.14 et versions plus récentes**, il est possible de s'attacher à un processus en cours et de lancer PDB à l'étape en cours. Dans un autre terminal, lancez
```bash
python -m pdb --pid <process id>
```

## Dépannage

### Script Python suspendu

Avec le module [faulthandler](https://docs.python.org/3.8/library/faulthandler.html), vous pouvez modifier votre script pour qu'une trace de l'origine du problème soit fournie après une certaine durée; voir l'information sur la commande `faulthandler.dump_traceback_later(timeout, repeat=False, file=sys.stderr, exit=False)`.

Vous pouvez aussi inspecter un processus Python pendant l'exécution d'une tâche sans avoir à le modifier au préalable avec [py-spy](https://pythonrepo.com/repo/benfred-py-spy-python-debugging-tools) :

1.  Installez py-spy dans un environnement virtuel de votre répertoire /home.
2.  Connectez-vous à une tâche en cours avec `srun --overlap --pty --jobid JOBID bash`.
3.  Trouvez l'ID de la tâche du script Python avec `htop -u $USER`.
4.  Activez l'environnement virtuel où py-spy est installé.
5.  Lancez `py-spy top --pid PID` pour visionner en direct les endroits où le code utilise beaucoup de temps.
6.  Lancez `py-spy dump --pid PID` pour obtenir une trace de l'état de votre code.

### 'Package 'X' requires a different Python: X.Y.Z not in '>=X.Y' '
En installant un paquet, vous pourriez avoir une erreur comme `ERROR: Package 'X' requires a different Python: 3.6.10 not in '>=3.7'`.

Dans ce cas, le module Python 3.6.10 qui est chargé n'est pas supporté par le paquet. Vous pouvez utiliser une version de Python plus récente, comme le dernier module disponible, ou encore installer une version moins récente du paquet X.

### 'Package has requirement X, but you'll have Y which is incompatible '
En installant un paquet, vous pourriez avoir une erreur comme
`ERROR: Package has requirement X, but you'll have Y which is incompatible.`.

Pour utiliser le nouveau résolveur de dépendances, installez la plus récente version de `pip` ou une version supérieure à [21.3](https://pip.pypa.io/en/stable/news/#v21-3).
```bash
pip install --no-index --upgrade pip
```
Lancez ensuite de nouveau la commande d'installation.

### 'No matching distribution found for X'
À l'installation d'un paquet, vous pouvez obtenir un message semblable à
```bash
pip install X
```
```text
ERROR: Could not find a version that satisfies the requirement X (from versions: none)
ERROR: No matching distribution found for X
```
`pip` n'a trouvé aucun paquet à installer qui rencontre les exigences (nom, version ou tags).
Assurez-vous que le nom et la version sont corrects.
Sachez aussi que les wheels `manylinux_x_y` sont ignorés.

Vous pouvez aussi vérifier si le paquet est disponible avec la commande [avail_wheels](#wheels-disponibles) ou en consultant la page [Wheels disponibles](../programming/available_python_wheels.md).

### Installer plusieurs paquets
Lorsque possible, il est préférable d'installer plusieurs paquets avec une seule commande.
```bash
pip install --upgrade pip
```
```bash
pip install package1 package2 package3 package4
```
Ainsi, `pip` peut résoudre plus facilement les problèmes de dépendance.

### 'My virtual environment was working yesterday but not anymore'
Les fréquentes mises à jour des paquets font en sorte qu'un environnement virtuel ne peut souvent être reproduit.

Il est possible aussi qu'un environnement virtuel créé dans `$SCRATCH` soit partiellement détruit lors de la purge automatique de ce système de fichiers, ce qui empêcherait l'environnement virtuel de bien fonctionner.

Pour contrer ceci, gelez les paquets et leurs versions avec
```bash
pip install --upgrade pip
```
```bash
pip install --no-index 'package1==X.Y' 'package2==X.Y.Z' 'package3<X.Y' 'package4>X.Y'
```
et créez ensuite un [fichier de requis](#créer-un-environnement-virtuel-dans-vos-tâches) qui sera utilisé pour installer ces paquets dans votre tâche.

### 'X is not a supported wheel on this platform'
À l'installation d'un paquet, vous pourriez obtenir une erreur comme `ERROR: package-3.8.1-cp311-cp311-manylinux_2_28_x86_64.whl is not a supported wheel on this platform.`.

Certains paquets peuvent être incompatibles ou non pris en charge par nos systèmes.
Deux cas fréquents sont :
* installation d'un paquet `manylinux`
* ou un paquet Python construit pour une autre version de Python (par exemple, installer un paquet construit pour Python 3.11 quand vous avez Python 3.9).

Certains paquets `manylinux` peuvent se trouver parmi nos [wheels Python](../programming/available_python_wheels.md).

### 'AttributeError: module ‘numpy’ has no attribute ‘X’'
À l'installation d'un whell, la plus récente version de Numpy est installée si aucune version spécifique n'est demandée.
Plusieurs attributs ont été déclarés obsolètes dans Numpy v1.20 et [ne sont plus offerts dans v1.24](https://numpy.org/devdocs/release/1.24.0-notes.html#expired-deprecations).

Dépendant de l'attribut, une erreur comme `AttributeError: module ‘numpy’ has no attribute ‘bool’` pourrait survenir.

Ceci est résolu avec l'installation d'une version précédente de Numpy avec `pip install --no-index 'numpy<1.24'`.

### 'ModuleNotFoundError: No module named 'X''
Il est possible qu'un module Python que vous voulez importer ne soit pas trouvé. Il y a plusieurs explications pour ceci, mais les plus fréquentes sont que
* le paquet n'est pas installé ou encore il n'est pas visible pour l'interpréteur Python;
* le nom du module ne correspond pas au nom réel;
* l'environnement virtuel est défectueux.

Pour contrer ceci, évitez de
* modifier la variable d'environnement `PYTHONPATH`;
* modifier la variable d'environnement `PATH`;
* charger un module alors qu'un environnement virtuel est activé; chargez d'abord tous les modules avant d'activer l'environnement virtuel.

Si vous avez ce problème,
* avec `pip list`, vérifiez si le paquet est installé;
* vérifiez encore si le nom que vous entrez correspond exactement au nom du module (majuscules, minuscules, traits de soulignement, etc.);
* vérifiez si le module est importé au bon niveau quand il provient de son répertoire source.

Dans le doute, recommencez avec un nouvel environnement.

### 'ImportError: numpy.core.multiarray failed to import'

Ce message peut survenir quand vous tentez d'importer un module Python qui dépend de Numpy.

Ceci se produit quand une version incompatible de Numpy est installée ou utilisée; vous devez installer une version compatible.

Le cas type est [la version 2.0 de Numpy qui brise l'ABI.](https://numpy.org/devdocs/dev/depending_on_numpy.html#numpy-2-0-specific-advice)
Dans le cas d'un wheel construit avec une version 1.x mais installé avec une version 2.x, vous devez installer une version antérieure avec `pip install --no-index 'numpy<2.0'`.

### 'Defaulting to user installation because normal site-packages is not writeable'
À l'installation d'un paquet peut s'afficher le message `Defaulting to user installation because normal site-packages is not writeable`.

Il s'agit du comportement par défaut de `pip` en dehors d'un environnement virtuel.
Cela signifie qu'aucun environnement virtuel n'a été trouvé ni activé et que `pip` a essayé d'installer à un endroit où il ne dispose pas des permissions nécessaires.

Ceci causera des [installations locales](#installation-locale) pouvant causer des problèmes.

### Installation locale
Une installation locale peut se produire de manière inattendue (si une erreur se produit avec votre environnement virtuel ou des problèmes de permission) ou par une installation définie avec (`pip install --user`).

Une installation locale est essentiellement le transfert des dépendances dans un espace partagé, ce qui n'est pas du tout souhaitable. Cela crée des problèmes d'importation ou d'exécution étranges avec vos paquets Python, ou encore des conflits de versions pouvant engendrer un véritable *enfer de dépendances*.

Il est préférable d'utiliser un [environnement virtuel](#créer-et-utiliser-un-environnement-virtuel) pour isoler, reproduire et gérer les différentes versions dans vos projets.

#### Supprimer une installation locale
Pour bien supprimer une installation locale, lancez
```bash
rm -vr ~/.local/bin ~/.local/lib/python*
```
Vous devrez peut-être spécifier les binaires directement si vous utilisez `~/.local/bin` pour des binaires locaux dans des paquets autres que Python.

Quand les installations locales sont supprimées, recommencez avec [un nouvel environnement virtuel jamais utilisé](#créer-et-utiliser-un-environnement-virtuel).