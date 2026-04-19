---
title: "Gurobi/fr"
slug: "gurobi"
lang: "fr"

source_wiki_title: "Gurobi/fr"
source_hash: "7618c1fe172dfe3d4a0107aa6c8bf9ec"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:50:26.897178+00:00"

tags:
  - software

keywords:
  - "documentation Gurobi"
  - "paramètres"
  - "grappes"
  - "environnement unique"
  - "Knowledge Base"
  - "gurobi"
  - "python"
  - "file d'attente"
  - "soumission de tâches"
  - "allocations interactives"
  - "licence"
  - "Gurobi"
  - "installation"
  - "StdEnv"
  - "scripts Python"
  - "module load"
  - "Fils d'exécution"
  - "fichier wheel"
  - "optimisation"
  - "tâches parallèles"
  - "scripts Slurm"
  - "erreur de segmentation"
  - "ligne de commande"
  - "environnements standards"
  - "modules"
  - "installation pip"
  - "Gurobi pour Python"
  - "environnement virtuel"
  - "Script Slurm"
  - "Environnements virtuels"
  - "StdEnv/2023"
  - "script Slurm"
  - "Java"
  - "jeton de licence unique"
  - "gurobipy"
  - "module gurobi"
  - "serveur de licences"
  - "ordonnanceur Slurm"
  - "notebooks Jupyter"
  - "valeurs optimales"
  - "Python"
  - "gurobi_cl"

questions:
  - "Quelles sont les conditions et la procédure à suivre pour obtenir l'accès à la licence académique de Gurobi sur les grappes ?"
  - "Comment peut-on tester la validité de sa licence Gurobi et quelles sont les étapes de dépannage en cas d'échec ?"
  - "Pourquoi est-il important de minimiser les requêtes au serveur de licences lors de l'utilisation de Gurobi et comment optimiser son code en ce sens ?"
  - "Comment peut-on soumettre de nombreuses tâches Gurobi en boucle tout en évitant de surcharger le serveur de licences ?"
  - "Quelles sont les étapes pour allouer des ressources interactives et utiliser Gurobi via la ligne de commande ou l'interpréteur ?"
  - "Comment soumettre une tâche en lots sur une grappe avec Slurm et configurer les paramètres du modèle Gurobi ?"
  - "Comment peut-on configurer Python pour utiliser un environnement et un jeton de licence uniques pour plusieurs modèles Gurobi ?"
  - "Quel problème spécifique peut survenir lors de l'exécution simultanée de nombreuses tâches parallèles ?"
  - "Quels autres programmes, en dehors de Python, sont mentionnés comme étant susceptibles de rencontrer ce problème de licence avec Gurobi ?"
  - "Quel outil en ligne de commande est mentionné pour être utilisé avec des arguments simples ?"
  - "Comment peut-on déterminer les meilleurs paramètres et les valeurs optimales pour un problème spécifique ?"
  - "Quelles sections de la documentation Gurobi et de la base de connaissances sont recommandées pour optimiser les performances et la recherche ?"
  - "Pourquoi est-il crucial de paramétrer le nombre de fils d'exécution dans un fichier gurobi.env lors de l'utilisation de Gurobi avec l'ordonnanceur Slurm ?"
  - "Quelle est la procédure recommandée pour utiliser Gurobi conjointement avec des paquets Python tiers tels que NumPy ou Pandas ?"
  - "Comment peut-on vérifier quelles versions de Python sont supportées par une version spécifique de Gurobi dans les environnements standards ?"
  - "Quelle est la différence de méthode d'installation recommandée pour Python entre les versions de Gurobi 10 (et antérieures) et les versions 11 (et ultérieures) ?"
  - "Comment contourner l'erreur de système de fichiers en lecture seule lors de l'installation de gurobipy pour les versions 10.0.3 et moins récentes ?"
  - "Pourquoi est-il conseillé d'utiliser la version 11.0.1 de Gurobi plutôt que la version 11.0.0 lors de la configuration de l'environnement virtuel ?"
  - "Comment charge-t-on les environnements standards et les modules Gurobi correspondants via la ligne de commande ?"
  - "Quel est le chemin d'accès au répertoire contenant les bibliothèques de Gurobi ?"
  - "Quelles versions de Python sont disponibles pour Gurobi 8.1.1 par rapport à Gurobi 9.5.2 selon les environnements chargés ?"
  - "Quelles sont les étapes préalables requises pour configurer et activer l'environnement virtuel ?"
  - "Pourquoi la version 11.0.0 est-elle spécifiquement évitée au profit de la version 11.0.1 ?"
  - "Quelles commandes exactes doivent être saisies dans le terminal pour charger les modules et créer l'environnement ?"
  - "Pourquoi l'installation standard de gurobipy avec pip échoue-t-elle sur ces systèmes Linux et quelle solution de contournement est proposée ?"
  - "Comment doit-on procéder pour récupérer et convertir le fichier wheel approprié lors de l'installation d'une nouvelle version de Gurobi ?"
  - "Quelles sont les étapes préalables requises, en termes de chargement de modules et d'activation d'environnement, pour exécuter avec succès un script Python utilisant Gurobi ?"
  - "Comment exécuter les scripts d'exemple fournis avec le module Gurobi ?"
  - "Quelle commande permet de lancer un script Python dans l'environnement virtuel Gurobi ?"
  - "Comment soumettre des scripts Python personnalisés en tant que tâches à la file d'attente via Slurm ?"
  - "Comment configurer et soumettre une tâche Slurm pour exécuter un script Python utilisant Gurobi ?"
  - "Quelle configuration supplémentaire est requise lors de l'exécution de Gurobi avec Java pour que les bibliothèques soient correctement localisées ?"
  - "Quelles sont les ressources disponibles pour apprendre à utiliser Gurobi avec des notebooks Jupyter et pour obtenir du support technique ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Gurobi](http://www.gurobi.com/) est une suite logicielle commerciale qui permet de résoudre des problèmes complexes d'optimisation. Nous abordons ici son utilisation sur nos grappes.

## Limites de la licence

Nous dispensons le soutien technique pour la licence gratuite disponible sur [Nibi](../clusters/nibi.md), [Fir](fir.md), [Rorqual](../clusters/rorqual.md) et [Trillium](../clusters/trillium.md). Cette licence permet 4096 utilisations simultanées (avec jetons) et l'optimisation distribuée sur un maximum de 100 nœuds. Plusieurs tâches peuvent être exécutées en simultané.
Vous devez cependant accepter certaines conditions. Faites parvenir un courriel au [soutien technique](../support/technical_support.md) avec l'entente (*Academic Usage Agreement*) dûment complétée; vous pourrez ensuite utiliser les applications après un délai de quelques jours.

### Entente d'utilisation académique

My Alliance username is "_______" and I am a member of the academic institution "_____________________." This message confirms that I will only use the Gurobi license provided on Digital Research Alliance of Canada systems for the purpose of non-commercial research project(s) to be published in publicly available article(s).

### Configurer votre compte
Il n'est pas nécessaire de créer le fichier `~/.licenses/gurobi.lic`. Les paramètres pour l'utilisation de notre licence Gurobi sont configurés par défaut quand un module Gurobi est chargé sur une grappe.

### Tester votre licence
Pour vous assurer que votre nom d'utilisateur a bien été ajouté à la licence Gurobi, lancez la commande suivante :

```bash
module load gurobi
gurobi_cl 1> /dev/null && echo Success || echo Fail
```

Si vous obtenez **Success**, vous pouvez utiliser Gurobi immédiatement. Si vous obtenez **Fail**, vérifiez s'il existe un fichier nommé *~/.license/gurobi*; si c'est le cas, supprimez ce fichier, chargez le module Gurobi de nouveau et refaites le test.

Si vous obtenez encore **Fail**, vérifiez si une variable d'environnement définit GUROBI dans vos fichiers *~/.bashrc* ou *~/.bash_profile*; si c'est le cas, supprimez la ou les lignes correspondantes ou mettez-les en commentaire, déconnectez-vous et connectez-vous de nouveau, chargez le module Gurobi de nouveau et refaites le test.

Si vous obtenez toujours **Fail**, contactez le [soutien technique](../support/technical_support.md) pour de l'assistance.

### Utiliser un minimum de licences

Veuillez noter que toutes les demandes de licence Gurobi sont gérées par un serveur de licences unique situé en Ontario. Il est donc important de limiter au maximum les tentatives de demande de licence. Plutôt que de demander une licence à chaque invocation de Gurobi dans une tâche (ce qui peut se produire des dizaines, voire des centaines de fois), assurez-vous que votre programme, quel que soit le langage ou l'environnement utilisé, n'effectue qu'une seule demande de licence et réutilise ensuite ce jeton de licence pendant toute la vie de la tâche. Cela améliorera les performances de votre tâche, car contacter un serveur de licence distant est très coûteux en temps. De plus, la réactivité de notre serveur sera également améliorée.

!!! warning "Utilisation des licences"
    Une utilisation incorrecte de Gurobi à cet égard peut entraîner des échecs aléatoires et intermittents. Si cela se produit, nous vous contacterons pour vous inviter à interrompre toutes vos tâches jusqu'à ce que votre programme soit corrigé et testé afin de garantir la résolution du problème. Voyez [la documentation pour les programmes en C++](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license). Cette documentation explique comment créer un environnement Gurobi unique utilisable pour tous vos modèles. [Pour Python, consultez cette page](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license) qui explique comment mettre en œuvre ce même principe d'environnement unique, et donc d'un jeton de licence unique, pour plusieurs modèles. D'autres programmes utilisant Gurobi, comme R, peuvent également facilement déclencher ce problème lors d'une exécution lorsque de nombreuses tâches parallèles sont soumises et/ou exécutées simultanément.

Si vous soumettez de nombreuses tâches Gurobi en boucle à l'ordonnanceur, utilisez l'exemple de script suivant (ou un équivalent) pour assurer un démarrage progressif. Cela permettra de minimiser la fréquence d'utilisation des licences et, par conséquent, la charge sur notre serveur de licences Gurobi. Le script utilise l'option de dépendance `after` de [l'ordonnanceur Slurm](https://slurm.schedmd.com/sbatch.html) qui est décrite dans [Soumettre une tâche : Fonctions avancées](../running-jobs/advanced_job_submission.md). Nous limitons à 10 000 le nombre d'utilisations de licences Gurobi par grappe, sur une période de 24 heures. Si votre programme Gurobi utilise un algorithme nécessitant l'utilisation de deux licences par tâche, cela correspond à un maximum de 5 000 tâches soumises par jour.

```bash
# Exemple de soumission progressive avec Slurm
# [l2(nibi):~] cat submit.sh
i=1; jobid=$(sbatch --parsable --output=slurm-%j-$i.out script.sh)
for i in {2..1000}; do
 jobid=$(sbatch --parsable --dependency=after:$jobid --output=slurm-%j-$i.out script.sh)
 [ "$?" -ne 0 ] && exit 1
done
```

## Allocations interactives

### Ligne de commande

```bash
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
gurobi_cl Record=1 Threads=8 Method=2 ResultFile=p0033.sol LogFile=p0033.log $GUROBI_HOME/examples/data/p0033.mps
gurobi_cl --help
```

### Interpréteur interactif

```bash
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
echo "Record 1" > gurobi.env # Voir la référence [1]
gurobi.sh
```

```text
gurobi> m = read('/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/gurobi/8.1.1/examples/data/glass4.mps') 
gurobi> m.Params.Threads = 8               # Voir la référence [2]
gurobi> m.Params.Method = 2
gurobi> m.Params.ResultFile = "glass4.sol"
gurobi> m.Params.LogFile = "glass4.log"
gurobi> m.optimize()
gurobi> m.write('glass4.lp')
gurobi> m.status                           # Voir la référence [3]
gurobi> m.runtime                          # Voir la référence [4]
gurobi> help()
```

Références :
1.  [Enregistrement des appels API](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)
2.  [Description des paramètres](https://www.gurobi.com/documentation/8.1/refman/parameter_descriptions.html)
3.  [Codes d'état d'optimisation](https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html)
4.  [Attributs](https://www.gurobi.com/documentation/8.1/refman/attributes.html)

### Répéter des appels API
Il est possible d'enregistrer des appels API et de rejouer l'enregistrement avec :

```bash
gurobi_cl recording000.grbr
```

Référence : [https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)

## Soumettre une tâche en lots sur une grappe

Une fois que votre script Slurm est prêt, vous pouvez le soumettre à la file d'attente avec la commande `sbatch script-name.sh`. Vous pouvez vérifier l'état de vos tâches dans la file d'attente avec la commande `sq`. Les scripts suivants solutionnent deux problèmes qui se trouvent dans le répertoire `examples` de chaque module Gurobi.

### Exemple de données

Le script Slurm suivant utilise l'[interface en ligne de commande](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_the_model_using_th.html) pour résoudre un [modèle simple de production de pièces](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_a_simple_model_the.html) écrit en [format LP](https://www.gurobi.com/documentation/9.5/refman/lp_format.html). La dernière ligne montre comment des [paramètres](https://www.gurobi.com/documentation/9.5/refman/parameters.html) peuvent être passés directement à l'outil en ligne de commande `gurobi_cl` avec des arguments simples. Pour sélectionner les meilleurs [paramètres](https://www.gurobi.com/documentation/9.5/refman/parameters.html) pour un problème particulier et pour choisir les valeurs optimales, voyez les sections *Performance and Parameters* et *Algorithms and Search* dans la [Base de connaissances](https://support.gurobi.com/hc/en-us/categories/360000840331-Knowledge-Base) et dans la [documentation Gurobi](https://www.gurobi.com/documentation/).

```bash linenums="1" title="script-lp_coins.sh"
#!/bin/bash
#SBATCH --account=def-group   # un compte quelconque
#SBATCH --time=0-00:30        # spécifiez la limite de temps (J-HH:MM)
#SBATCH --cpus-per-task=8     # spécifiez le nombre de fils
#SBATCH --mem=4G              # spécifiez la mémoire totale
#SBATCH --nodes=1             # ne pas modifier

#module load StdEnv/2016      # pour les versions < 9.0.3 
module load StdEnv/2020       # pour les versions > 9.0.2

module load gurobi/9.5.0

rm -f coins.sol
gurobi_cl Threads=$SLURM_CPUS_ON_NODE Method=2 ResultFile=coins.sol ${GUROBI_HOME}/examples/data/coins.lp
```

### Exemple avec Python

Le script Slurm suivant solutionne un [modèle simple d'emplacement d'installations](https://www.gurobi.com/documentation/9.5/examples/a_list_of_the_grb_examples.html) avec [Gurobi Python](https://www.gurobi.com/documentation/9.5/examples/facility_py.html). L'exemple montre comment [paramétrer les fils](https://www.gurobi.com/documentation/9.5/refman/parameters.html#sec:Parameters) en nombre égal à celui des cœurs alloués à la tâche en générant un fichier [gurobi.env](https://www.gurobi.com/documentation/9.5/quickstart_linux/using_a_grb_env_file.html) dans le répertoire de travail quand vous utilisez [l'interface Gurobi Python](https://www.gurobi.com/documentation/9.5/refman/python_parameter_examples.html).
Ceci doit être fait pour chaque tâche soumise, autrement Gurobi lancera par défaut autant de [fils d'exécution](https://www.gurobi.com/documentation/9.5/refman/threads.html#parameter:Threads) qu'il y a de cœurs physiques dans le nœud de calcul plutôt que d'utiliser le nombre de cœurs physiques alloués à la tâche par l'ordonnanceur, ce qui risque de ralentir la tâche et nuire aux tâches exécutées sur le même nœud par les autres utilisateurs.

```bash linenums="1" title="script-facility.sh"
#!/bin/bash
#SBATCH --account=def-group   # indiquez le nom du compte
#SBATCH --time=0-00:30        # indiquez la limite de temps (jj-hh:mm)
#SBATCH --cpus-per-task=4     # indiquez le nombre de fils
#SBATCH --mem=4G              # demandez toute la mémoire
#SBATCH --nodes=1             # ne pas modifier

#module load StdEnv/2020      # versions < 10.0.3
module load StdEnv/2023       # versions > 10.0.3

module load gurobi/11.0.1

echo "Threads ${SLURM_CPUS_ON_NODE:-1}" > gurobi.env

gurobi.sh ${GUROBI_HOME}/examples/python/facility.py
```

## Environnements virtuels Python

Gurobi a sa propre version de Python qui ne contient aucun autre paquet de tiers autre que Gurobi. Pour utiliser Gurobi avec d'autres paquets Python comme NumPy, Matplotlib, Pandas et autres, il faut [créer un environnement virtuel Python](python.md) dans lequel seront installés `gurobipy` et par exemple `pandas`.

Avant de commencer, il faut décider quelle combinaison des versions Gurobi et Python nous voulons utiliser. La liste suivante montre les versions de Python supportées par les versions principales de Gurobi dans les environnements standards (StdEnv).

```bash
module load StdEnv/2016; module load gurobi/8.1.1; cd $EBROOTGUROBI/lib; ls -d python*
# python2.7  python2.7_utf16  python2.7_utf32  python3.5_utf32  python3.6_utf32  python3.7_utf32
```

```bash
module load StdEnv/2020; module load gurobi/9.5.2; cd $EBROOTGUROBI/lib; ls -d python*
# python2.7_utf16  python2.7_utf32  python3.10_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32
```

```bash
module load StdEnv/2023; module load gurobi/10.0.3; cd $EBROOTGUROBI/lib; ls -d python*
# python3.10_utf32  python3.11_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32
```

```bash
module load StdEnv/2023; module load gurobi/11.0.1; cd $EBROOTGUROBI/lib; ls -d python*
# python3.11
```

### Installer Gurobi pour Python

Tel que mentionné vers la fin de [Comment installer Gurobi pour Python ?](http://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), la méthode précédemment recommandée pour installer Gurobi pour Python avec `setup.py` est désormais obsolète et ne peut être utilisée qu'avec les versions Gurobi 10 (et plus anciennes). La section *Versions Gurobi 11.0.0 (et plus récentes)* montre comment télécharger simultanément une roue binaire compatible à partir de [pypi.org](https://pypi.org/project/gurobipy/) et la convertir dans un format utilisable avec la nouvelle commande recommandée.

### Versions Gurobi 10.0.3 et moins récentes

Il faut suivre les étapes suivantes une fois sur chaque système avec StdEnv/2023 et moins récents. Chargez d'abord les modules pour [créer l'environnement virtuel](python.md), puis activez cet environnement.

```bash
# [name@server ~] $
module load gurobi/10.0.3 python
virtualenv --no-download  ~/env_gurobi
source ~/env_gurobi/bin/activate
```

Installez les paquets que vous voulez utiliser, ici `pandas`. Par exemple :

```bash
# (env_gurobi) [name@server ~] $
pip install --no-index  pandas
```

Installez maintenant `gurobipy` dans l'environnement. À partir de StdEnv/2023, il n'est plus possible de l'installer dans `$EBROOTGUROBI` avec la commande `python setup.py build --build-base /tmp/${USER} install`, ce qui causerait une erreur fatale et le message `error: could not create 'gurobipy.egg-info': Read-only file system`. Copiez les fichiers ailleurs (par exemple dans `/tmp/$USER`) où l'installation sera faite, comme ci-dessous :

```bash
# (env_gurobi) [name@server ~] $
mkdir /tmp/$USER
cp -r $EBROOTGUROBI/{lib,setup.py} /tmp/$USER
cd /tmp/$USER
python setup.py install
# (env_gurobi) [roberpj@gra-login1:/tmp/roberpj] python setup.py install
# /home/roberpj/env_gurobi/lib/python3.11/site-packages/setuptools/_core_metadata.py:158: SetuptoolsDeprecationWarning: Invalid config.
# !!
#
#         ********************************************************************************
#         newlines are not allowed in `summary` and will break in the future
#         ********************************************************************************
#
# !!
#   write_field('Summary', single_line(summary))
# removing /tmp/roberpj/build
# (env_gurobi) [roberpj@gra-login1:/tmp/roberpj]
deactivate
# [name@server ~]
```

### Versions Gurobi 11.0.0 (et plus récentes)

Encore une fois, les étapes suivantes doivent être effectuées une fois pour chaque système sous StdEnv/2023 et les versions antérieures. Chargez d'abord les modules dans [Créer et utiliser un environnement virtuel](python.md), puis activez-le. La version 11.0.0 est ignorée car il a été observé qu'elle produit une erreur de segmentation dans au moins un exemple, comparé à la version 11.0.1 qui fonctionne sans problème.

```bash
# [name@server ~] $
module load gurobi/11.0.1 python
virtualenv --no-download  ~/env_gurobi
source ~/env_gurobi/bin/activate
```

Comme précédemment, installez tous les paquets Python nécessaires. Étant donné que l'exemple suivant nécessite `numpy`, nous installons le paquet `pandas`.

```bash
# (env_gurobi) [name@server ~] $
pip install --no-index  pandas
```

Installez ensuite `gurobipy` dans l'environnement. Comme mentionné ci-dessus et dans [cet article](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), l'utilisation de `setup.py` pour installer Gurobi pour Python est déconseillée à partir de Gurobi 11. Pip et Conda sont tous deux proposés comme alternatives; cependant, comme Conda ne doit pas être utilisé sur nos systèmes, l'approche avec Pip sera démontrée ici. L'installation de `gurobipy` est légèrement compliquée car nos systèmes Linux sont configurés avec le préfixe Gentoo. En conséquence, ni A) la commande recommandée pour télécharger et installer l'extension `gurobipy` depuis le serveur public PyPI `pip install gurobipy==11.0.1` mentionnée dans l'article, ni B) la commande hors ligne pour installer la roue avec `python -m pip install --find-links <wheel-dir> --no-index gurobipy` ne fonctionneront. Au lieu de cela, nous avons préparé un script pour télécharger et convertir simultanément la roue existante dans un format utilisable avec un nouveau nom. Il y a une mise en garde; pour chaque nouvelle version de Gurobi, vous devez vous rendre sur [https://pypi.org/project/gurobipy/11.0.1/#history](https://pypi.org/project/gurobipy/11.0.1/#history), cliquer sur la version souhaitée et cliquer sur le bouton **Télécharger les fichiers** situé dans le menu de gauche. Enfin, cliquez pour copier le lien HTTPS du fichier wheel (nommé *gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl* dans le cas de Gurobi 11.0.1) et collez-le comme argument `--url` comme ci-dessous.

```bash
# (env_gurobi) [name@server ~] $
wget https://raw.githubusercontent.com/ComputeCanada/wheels_builder/main/unmanylinuxize.sh
chmod u+rx unmanylinuxize.sh
./unmanylinuxize.sh --package gurobipy --version 11.0.1 --url https://files.pythonhosted.org/packages/1c/96/4c800e7cda4a1688d101a279087646912cf432b0f61ff5c816f0bc8503e0/gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
ls
# gurobipy-11.0.1-cp311-cp311-linux_x86_64.whl  unmanylinuxize.sh
python -m pip install --find-links $PWD --no-index gurobipy
deactivate
# [name@server ~]
```

### Travailler dans l'environnement avec Gurobi

Une fois créé, notre environnement Gurobi peut être activé et utilisé à tout moment. Pour démontrer cela, nous chargeons également Gurobi (donc `$EBROOTGUROBI` est défini) et `scipy-stack` (donc SciPy est disponible). Les deux sont nécessaires pour exécuter l'exemple de matrice (avec NumPy qui était déjà installé dans notre environnement via Pandas avec pip dans une étape précédente).

```bash
# [name@server ~] $
module load gurobi/11.0.1 scipy-stack
source ~/env_gurobi/bin/activate
# (env_gurobi) [name@server ~]
```

Les scripts Python comme les exemples fournis avec le module Gurobi peuvent alors être exécutés dans l'environnement virtuel avec Python.

```bash
# (env_gurobi) [name@server ~] $
python $EBROOTGUROBI/examples/python/matrix1.py
```

De même, des scripts Python personnalisés tels que les suivants peuvent être soumis en tant que tâches à la file d'attente en écrivant des scripts Slurm qui chargent votre environnement virtuel.

```bash
# [name@server ~] $ cat my_gurobi_script.py
import pandas as pd
import numpy as np
import gurobipy as gurobi
from gurobipy import *
# etc
```

Soumettez le script dans la file d'attente avec `sbatch my_slurm_script.sh`.

```bash linenums="1" title="my_slurm_script.sh"
#!/bin/bash
#SBATCH --account=def-somegrp  # indiquez le nom du compte
#SBATCH --time=0-00:30         # indiquez la limite de temps (jj-hh:mm)
#SBATCH --nodes=1              # utiliser un (1) nœud
#SBATCH --cpus-per-task=4      # indiquez le nombre de CPU
#SBATCH --mem=4000M            # demandez toute la mémoire

module load StdEnv/2023
module load gurobi/11.0.1
# module load scipy-stack      # décommentez si nécessaire

echo "Threads ${SLURM_CPUS_ON_NODE:-1}" > gurobi.env

source ~/env_gurobi/bin/activate
python my_gurobi_script.py
```

Pour plus d'information sur la création et l'utilisation des environnements virtuels Python, voir [Créer un environnement virtuel dans vos tâches](python.md).

## Utiliser Gurobi avec Java

Vous devez aussi charger un module Java et ajouter une option à la commande Java pour permettre à l'environnement virtuel Java de localiser les bibliothèques Gurobi, comme dans l'exemple suivant.

```bash linenums="1" title="gurobi-java.sh"
#!/bin/bash
#SBATCH --time=0-00:30        # limite de temps (J-HH:MM)
#SBATCH --cpus-per-task=1     # nombre de CPU (fils) à utiliser	
#SBATCH --mem=4096M           # mémoire par CPU (en Mo)

module load java/14.0.2
module load gurobi/9.1.2

java -Djava.library.path=$EBROOTGUROBI/lib -Xmx4g -jar my_java_file.jar
```

## Utiliser Gurobi avec des notebooks Jupyter

Vous trouverez de l'information sur les [Ressources](https://www.gurobi.com/resources/), les [Exemples de code et de modélisation](https://www.gurobi.com/resources/?category-filter=code-example) et l'[Optimisation avec Python – Exemples de modélisation avec Jupyter Notebook](https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/). Sur le site [support.gurobi.com](https://support.gurobi.com/), faites une recherche avec *Jupyter Notebooks*.

Voir aussi cette [démonstration, à 38 min 28 s de la vidéo](https://youtu.be/Qk3Le5HBxeg?t=2310).

## Comment citer Gurobi

Voir [« Comment citer le logiciel Gurobi pour une publication académique ? »](https://support.gurobi.com/hc/en-us/articles/360013195592-How-do-I-cite-Gurobi-software-for-an-academic-publication-).

## Obtenir de l'aide

Le Centre d'aide général de Gurobi est situé [ici](https://support.gurobi.com/hc/en-us).
Gurobot, un nouvel agent d'IA Gurobi, est disponible [ici](https://portal.gurobi.com/iam/chat).
La documentation officielle en ligne de Gurobi est [ici](https://docs.gurobi.com/13.0/).
Pour obtenir de l'aide concernant l'utilisation de Gurobi sur la grappe de l'Alliance, [soumettez un billet](../support/technical_support.md).