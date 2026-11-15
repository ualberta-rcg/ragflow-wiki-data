---
title: "Gurobi/fr"
slug: "gurobi"
lang: "fr"

source_wiki_title: "Gurobi/fr"
source_hash: "6b32631acea56919912fb140d6eeef60"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:32:48.269024+00:00"

tags:
  - software

keywords:
  - "installation hors ligne"
  - "notebooks Jupyter"
  - "module load gurobi"
  - "virtualenv"
  - "module load gurobi/11.0.1"
  - "enregistrement des appels API"
  - "wheel"
  - "ordonnanceur"
  - "Params.Method"
  - "minimiser les demandes de licence"
  - "interface Gurobi Python"
  - "paramètre Threads"
  - "m.optimize"
  - "my_java_file.jar"
  - "modèles multiples"
  - "jeton de licence unique"
  - "Gurobi licenses"
  - "exécution parallèle"
  - "module load gurobi/9.1.2"
  - "serveur de licences unique"
  - "soumission de tâche Slurm"
  - "environnement virtuel Gurobi"
  - "pip install --no-index pandas"
  - "paramètres Gurobi"
  - "ralentir la tâche"
  - "agent IA Gurobi"
  - "#SBATCH --time=0-00:30"
  - "gurobi-java.sh"
  - "Params.ResultFile"
  - "Gurobi"
  - "Utiliser Gurobi avec des notebooks Jupyter"
  - "sbatch --dependency=after"
  - "ressources Gurobi"
  - "license usage per job"
  - "--url"
  - "pypi.org"
  - "module load gurobi/10.0.3 python"
  - "environnement virtuel"
  - "installation Gurobi pour Python"
  - "licence partagée"
  - "gurobipy"
  - "exemple de modèle LP"
  - "source ~/env_gurobi/bin/activate"
  - "cœurs physiques"
  - "gurobi_cl"
  - "citer Gurobi"
  - "java -Djava.library.path=$EBROOTGUROBI/lib"
  - "Jupyter Notebooks"
  - "4096 utilisations simultanées"
  - "environnement virtuel Python"
  - "pandas"
  - "Params.Threads"
  - "script Slurm"
  - "read glass4.mps"
  - "licence gratuite"
  - "module load StdEnv"
  - "license server overload"
  - "centre d'aide Gurobi"
  - "interactive allocations"

questions:
  - "Quelle est la limite d’utilisation simultanée et le nombre maximal de nœuds autorisés par la licence gratuite de Gurobi sur les grappes mentionnées ?"
  - "Quelles sont les étapes à suivre pour tester et valider que votre compte utilisateur a bien accès à la licence Gurobi après le chargement du module ?"
  - "Comment réduire le nombre de demandes de licence Gurobi dans vos programmes afin d’éviter les échecs aléatoires et d’améliorer les performances ?"
  - "Comment libérer une licence partagée sous Gurobi pour Python en suivant le principe d’environnement unique ?"
  - "Quel est le mécanisme du « jeton de licence unique » permettant d’exécuter plusieurs modèles simultanément avec Gurobi ?"
  - "Quels autres langages ou programmes (par exemple R) peuvent rencontrer le même problème de licence lorsqu’ils soumettent ou exécutent de nombreuses tâches parallèles ?"
  - "What commands can you use to verify that the total number of Gurobi licenses in use across all Alliance clusters stays below the 1000‑license threshold?"
  - "How can you calculate the average number of licenses consumed per running Gurobi job, and what is the recommended maximum average?"
  - "Which Slurm submission script pattern should be employed to submit many Gurobi tasks gradually, and how does the `--dependency=after` option help limit license load?"
  - "Comment enregistrer des appels API Gurobi et les rejouer ultérieurement ?"
  - "Quelle est la marche à suivre pour soumettre un script Slurm qui résout un modèle Gurobi, en précisant les directives de ressources et les options de ligne de commande ?"
  - "Comment paramétrer correctement le nombre de threads dans un script Python Gurobi exécuté sous Slurm afin d’utiliser uniquement les cœurs alloués à la tâche ?"
  - "Which input file is being loaded into the Gurobi model and what format does it have?"
  - "What specific Gurobi parameters are configured before optimization, and what values are assigned to them?"
  - "After calling `m.optimize()`, how does the script retrieve and store the solution and log information?"
  - "Pourquoi faut‑il définir le paramètre Threads de Gurobi pour chaque tâche soumise ?"
  - "Que se passe‑t‑il si le paramètre Threads n’est pas spécifié dans Gurobi ?"
  - "Comment le nombre de fils d’exécution lancé par défaut par Gurobi peut‑il ralentir la tâche et nuire aux autres utilisateurs sur le même nœud ?"
  - "Quels modules et versions de StdEnv doivent être chargés pour utiliser Gurobi 11.0.1 avec Python ?"
  - "Comment créer et activer un environnement virtuel Python afin d’installer gurobipy ainsi que d’autres paquets comme pandas ?"
  - "Quelle est la méthode recommandée pour installer Gurobi pour Python à partir de la version 11.0.0 et ultérieure ?"
  - "Quelle commande permet de charger le module Gurobi version 10.0.3 ainsi que Python sur le serveur ?"
  - "Comment créer un environnement virtuel nommé env_gurobi sans téléchargement, puis l’activer ?"
  - "Après l’activation de l’environnement virtuel, quelle est la prochaine étape pour installer des paquets comme pandas ?"
  - "Pourquoi l'installation de gurobipy avec la commande `python setup.py build --build-base /tmp/${USER} install` échoue-t-elle dans StdEnv/2023 ?"
  - "Quelles sont les étapes complètes pour installer gurobipy dans un environnement virtuel sous Gurobi 11.0.1 sur les systèmes StdEnv/2023 ?"
  - "Comment contourner le problème du préfixe Gentoo lors de l'installation de gurobipy avec pip et où doit‑on récupérer le fichier wheel approprié ?"
  - "Quel est le processus détaillé pour obtenir le lien URL du fichier wheel d’une version spécifique de Gurobi sur PyPI ?"
  - "Où devez‑vous vous rendre et quelles actions devez‑vous effectuer sur la page PyPI pour télécharger le fichier wheel de Gurobi ?"
  - "Comment devez‑vous utiliser le lien URL copié du fichier wheel dans la ligne de commande (argument --url) ?"
  - "Comment activer l’environnement virtuel Gurobi, charger les modules nécessaires et exécuter un script Python fourni avec Gurobi ?"
  - "Quelle est la syntaxe du script Slurm à utiliser pour soumettre un script Python personnalisé qui utilise Gurobi dans l’environnement virtuel ?"
  - "Quelles options et modules doivent être chargés pour faire fonctionner Gurobi avec Java (et quels ajustements sont requis pour les notebooks Jupyter) ?"
  - "Quels sont les paramètres SBATCH spécifiés dans le script et quelle est leur fonction ?"
  - "Comment le script charge‑t‑il les modules Java et Gurobi, puis exécute‑t‑il le fichier JAR avec le chemin de la bibliothèque Gurobi ?"
  - "En quoi ce script est‑il lié à l’utilisation de Gurobi dans des notebooks Jupyter, comme indiqué par le titre « Utiliser Gurobi avec des notebooks Jupyter » ?"
  - "Où peut‑on accéder aux ressources, exemples de code et modèles Gurobi, y compris les notebooks Jupyter en Python ?"
  - "Comment citer correctement le logiciel Gurobi dans une publication académique ?"
  - "Quels services d’assistance Gurobi sont proposés (centre d’aide, agent IA, documentation en ligne, support technique) ?"

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

Nous dispensons le soutien technique pour la licence gratuite disponible sur [Nibi](../clusters/nibi.md), [Fir](fir.md), [Rorqual](../clusters/rorqual.md) et [Trillium](../clusters/trillium.md). Cette licence permet 4096 utilisations simultanées (avec jetons) et l'optimisation distribuée sur un maximum de 100 nœuds. Plusieurs tâches peuvent être exécutées en simultané. Vous devez cependant accepter certaines conditions. Faites parvenir un courriel au [soutien technique](../support/technical_support.md) avec l'entente (*Academic Usage Agreement*) dûment complétée; vous pourrez ensuite utiliser les applications après un délai de quelques jours.

### Entente d'utilisation académique

Mon nom d'utilisateur Alliance est "_______" et je suis membre de l'institution académique "_____________________." Ce message confirme que je n'utiliserai la licence Gurobi fournie sur les systèmes de l'Alliance de recherche numérique du Canada qu'à des fins de projets de recherche non commerciaux qui seront publiés dans des articles accessibles au public.

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

### Minimiser les demandes de licence

Veuillez noter que toutes les demandes de licence Gurobi sont gérées par un serveur de licences unique situé en Ontario. Il est donc important de limiter au maximum les tentatives de demande de licence. Plutôt que de demander une licence à chaque invocation de Gurobi dans une tâche (ce qui peut se produire des dizaines, voire des centaines de fois), assurez-vous que votre programme, quel que soit le langage ou l'environnement utilisé, n'effectue qu'une seule demande de licence et réutilise ensuite ce jeton de licence pendant toute la vie de la tâche. Cela améliorera les performances de votre tâche, car contacter un serveur de licence distant est très coûteux en temps. De plus, la réactivité de notre serveur sera également améliorée.

!!! warning "Utilisation incorrecte de la licence"
    Une utilisation incorrecte de Gurobi à cet égard peut entraîner des échecs aléatoires et intermittents. Si cela se produit, nous vous contacterons pour vous inviter à interrompre toutes vos tâches jusqu'à ce que votre programme soit corrigé et testé afin de garantir la résolution du problème. Pour les programmes en C++, consultez [la documentation](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license). Elle explique comment créer un environnement Gurobi unique utilisable pour tous vos modèles. Pour Python, consultez [cette page](https://support.gurobi.com/hc/en-us/articles/360013417731-How-do-I-release-a-shared-license) qui explique comment mettre en œuvre ce même principe d'environnement unique, et donc d'un jeton de licence unique, pour plusieurs modèles. D'autres programmes utilisant Gurobi, comme R, peuvent également facilement déclencher ce problème lors d'une exécution lorsque de nombreuses tâches parallèles sont soumises et/ou exécutées simultanément.

Il y a deux autres conditions que vos tâches devraient respecter pour éviter de surcharger le serveur de licences. La première est que l'ensemble de vos tâches exécutées sur toutes les grappes de l'Alliance ne consomme pas plus de 1000 licences, étant donné qu'il n'y a que 4096 licences disponibles. Vous pouvez vérifier ceci en vous connectant à n'importe quelle grappe et en exécutant la commande suivante :

```bash
module load gurobi
gurobi_cl --tokens | grep $USER | wc -l  # devrait être < 1000
```

La deuxième condition est que chaque tâche Gurobi en cours d'exécution ne devrait utiliser qu'une seule licence (plus rarement deux). En supposant que toutes vos tâches Gurobi s'exécutent sur la grappe à laquelle vous êtes connecté, l'utilisation moyenne de licences par tâche peut être vérifiée en exécutant :

```bash
module load gurobi
echo "$(gurobi_cl --tokens | grep $USER | wc -l) / $(squeue -h -r -u $USER -t running | wc -l)" | bc -l # devrait être <= 2
```

Si, toutefois, vous exécutez des tâches sur plusieurs grappes, alors cette forme modifiée de la commande précédente (qui est beaucoup plus lente) devrait être utilisée :

```bash
module load gurobi
echo $(for n in $(gurobi_cl --tokens | grep $USER | awk "{print $1}"); do host $n; done | grep address | wc -l) / $(squeue -u $USER -h -t running -r | wc -l) | bc -l # devrait être <= 2
```

Notez que si vous exécutez l'une ou l'autre de ces commandes sur une grappe où aucune tâche Gurobi n'est en cours, un message "Runtime error Divide by zero error" (erreur d'exécution : division par zéro) sera affiché en conséquence.

Si vous soumettez de nombreuses tâches Gurobi en boucle à l'ordonnanceur, utilisez l'exemple de script suivant (ou un équivalent) pour assurer un démarrage progressif. Cela permettra de minimiser la fréquence d'utilisation des licences et, par conséquent, la charge sur notre serveur de licences Gurobi. Le script utilise l'option de dépendance `after` de l'[ordonnanceur Slurm](https://slurm.schedmd.com/sbatch.html) qui est décrite dans [Soumettre une tâche : Fonctions avancées](../running-jobs/advanced_job_submission.md). Nous limitons à 10 000 le nombre d'utilisations de licences Gurobi par grappe, sur une période de 24 heures. Si votre programme Gurobi utilise un algorithme nécessitant l'utilisation de deux licences par tâche, cela correspond à un maximum de 5 000 tâches soumises par jour.

```bash title="Exemple de script de soumission en série"
i=1; jobid=$(sbatch --parsable --output=slurm-%j-$i.out script.sh)
for i in {2..1000}; do
 jobid=$(sbatch --parsable --dependency=after:$jobid --output=slurm-%j-$i.out script.sh)
 [ "$?" -ne 0 ] && exit 1
done
```

## Allocations interactives

### Ligne de commande

```bash title="Exemple d'allocation interactive et de commande Gurobi"
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
gurobi_cl Record=1 Threads=8 Method=2 ResultFile=p0033.sol LogFile=p0033.log $GUROBI_HOME/examples/data/p0033.mps
gurobi_cl --help
```

### Interpréteur interactif

```bash title="Lancer l'interpréteur Gurobi"
salloc --time=1:00:0 --cpus-per-task=8 --mem=1G --account=def-xyz
module load gurobi
echo "Record 1" > gurobi.env # voir *
gurobi.sh
```

```text title="Session interactive Gurobi"
gurobi> m = read('/cvmfs/restricted.computecanada.ca/easybuild/software/2017/Core/gurobi/8.1.1/examples/data/glass4.mps')
gurobi> m.Params.Threads = 8               # voir **
gurobi> m.Params.Method = 2
gurobi> m.Params.ResultFile = "glass4.sol"
gurobi> m.Params.LogFile = "glass4.log"
gurobi> m.optimize()
gurobi> m.write('glass4.lp')
gurobi> m.status                           # voir ***
gurobi> m.runtime                          # voir ****
gurobi> help()
```

Voici les références pour les éléments notés ci-dessus :
*   [Enregistrement des appels API](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)
*   [Descriptions des paramètres](https://www.gurobi.com/documentation/8.1/refman/parameter_descriptions.html)
*   [Codes d'état d'optimisation](https://www.gurobi.com/documentation/8.1/refman/optimization_status_codes.html)
*   [Attributs](https://www.gurobi.com/documentation/8.1/refman/attributes.html)

### Répéter des appels API

Il est possible d'enregistrer des appels API et de rejouer l'enregistrement avec :

```bash
gurobi_cl recording000.grbr
```
Référence : [Recording API Calls](https://www.gurobi.com/documentation/8.1/refman/recording_api_calls.html)

## Soumettre une tâche par lots sur une grappe

Une fois que votre script Slurm est prêt, vous pouvez le soumettre à la file d'attente avec la commande `sbatch script-name.sh`. Vous pouvez vérifier l'état de vos tâches dans la file d'attente avec la commande `sq`. Les scripts suivants résolvent deux problèmes qui se trouvent dans le répertoire `examples` de chaque module Gurobi.

### Exemple de données

Le script Slurm suivant utilise l'[interface ligne de commande](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_the_model_using_th.html) pour résoudre un [modèle simple de production de pièces de monnaie](https://www.gurobi.com/documentation/9.5/quickstart_linux/solving_a_simple_model_the.html) écrit au [format LP](https://www.gurobi.com/documentation/9.5/refman/lp_format.html). La dernière ligne montre comment des [paramètres](https://www.gurobi.com/documentation/9.5/refman/parameters.html) peuvent être passés directement à l'outil ligne de commande `gurobi_cl` avec des arguments simples. Pour sélectionner les meilleurs [paramètres](https://www.gurobi.com/documentation/9.5/refman/parameters.html) pour un problème particulier et pour choisir les valeurs optimales, consultez les sections *Performance and Parameters* et *Algorithms and Search* dans la [Base de connaissances](https://support.gurobi.com/hc/en-us/categories/360000840331-Knowledge-Base) et dans la [documentation Gurobi](https://www.gurobi.com/documentation/).

```bash title="script-lp_coins.sh"
#!/bin/bash
#SBATCH --account=def-group   # un compte
#SBATCH --time=0-00:30        # limite de temps (J-HH:MM)
#SBATCH --cpus-per-task=8     # nombre de fils
#SBATCH --mem=4G              # mémoire totale
#SBATCH --nodes=1             # ne pas modifier

#module load StdEnv/2016      # pour les versions < 9.0.3 
module load StdEnv/2020       # pour les versions > 9.0.2

module load gurobi/9.5.0

rm -f coins.sol
gurobi_cl Threads=$SLURM_CPUS_ON_NODE Method=2 ResultFile=coins.sol ${GUROBI_HOME}/examples/data/coins.lp
```

### Exemple avec Python

Le script Slurm suivant résout un [modèle simple d'emplacement de sites](https://www.gurobi.com/documentation/9.5/examples/a_list_of_the_grb_examples.html) avec [Gurobi Python](https://www.gurobi.com/documentation/9.5/examples/facility_py.html). L'exemple montre comment [paramétrer les fils](https://www.gurobi.com/documentation/9.5/refman/parameters.html#sec:Parameters) en nombre égal à celui des cœurs alloués à la tâche en générant un fichier `gurobi.env` dans le répertoire de travail lorsque vous utilisez l'[interface Gurobi Python](https://www.gurobi.com/documentation/9.5/refman/python_parameter_examples.html). Ceci doit être fait pour chaque tâche soumise, autrement Gurobi lancera par défaut autant de [fils d'exécution](https://www.gurobi.com/documentation/9.5/refman/threads.html#parameter:Threads) qu'il y a de cœurs physiques dans le nœud de calcul plutôt que d'utiliser le nombre de cœurs physiques alloués à la tâche par l'ordonnanceur, ce qui risque de ralentir la tâche et de nuire aux tâches exécutées sur le même nœud par les autres utilisateurs.

```bash title="script-facility.sh"
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

Gurobi a sa propre version de Python qui ne contient aucun autre paquet tiers autre que Gurobi. Pour utiliser Gurobi avec d'autres paquets Python comme NumPy, Matplotlib, Pandas et autres, il faut [créer un environnement virtuel Python](python.md) dans lequel seront installés `gurobipy` et, par exemple, `pandas`.
Avant de commencer, il faut décider quelle combinaison des versions Gurobi et Python nous voulons utiliser. La liste suivante montre les versions de Python supportées par les versions principales de Gurobi dans les environnements standards (StdEnv).

```console
[name@server ~] module load StdEnv/2016; module load gurobi/8.1.1; cd $EBROOTGUROBI/lib; ls -d python*
python2.7  python2.7_utf16  python2.7_utf32  python3.5_utf32  python3.6_utf32  python3.7_utf32
```

```console
[name@server ~] module load StdEnv/2020; module load gurobi/9.5.2; cd $EBROOTGUROBI/lib; ls -d python*
python2.7_utf16  python2.7_utf32  python3.10_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32
```

```console
[name@server ~] module load StdEnv/2023; module load gurobi/10.0.3; cd $EBROOTGUROBI/lib; ls -d python*
python3.10_utf32  python3.11_utf32  python3.7  python3.7_utf32  python3.8_utf32  python3.9_utf32
```

```console
[name@server ~] module load StdEnv/2023; module load gurobi/11.0.1; cd $EBROOTGUROBI/lib; ls -d python*
python3.11
```

### Installer Gurobi pour Python

Tel que mentionné vers la fin de [How do I install Gurobi for Python?](http://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), la méthode précédemment recommandée pour installer Gurobi pour Python avec `setup.py` est désormais obsolète et ne peut être utilisée qu'avec les versions Gurobi 10 (et plus anciennes). La section *Versions Gurobi 11.0.0 (et plus récentes)* montre comment télécharger simultanément une roue binaire compatible à partir de [pypi.org](https://pypi.org/project/gurobipy/) et la convertir dans un format utilisable avec la nouvelle commande recommandée.

### Versions Gurobi 10.0.3 et antérieures

Il faut suivre les étapes suivantes une fois sur chaque système avec StdEnv2023 et les versions antérieures. Chargez d'abord les modules pour [créer l'environnement virtuel](python.md), puis activez cet environnement.

```console
[name@server ~] $ module load gurobi/10.0.3 python
[name@server ~] $ virtualenv --no-download  ~/env_gurobi
[name@server ~] $ source ~/env_gurobi/bin/activate
```

Installez les paquets que vous voulez utiliser, ici `pandas`. Par exemple :

```console
(env_gurobi) [name@server ~] $ pip install --no-index  pandas
```

Installez maintenant gurobipy dans l'environnement. À partir de StdEnv/2023, il n'est plus possible de l'installer dans `$EBROOTGUROBI` avec la commande `python setup.py build --build-base /tmp/${USER} install`, ce qui causerait une erreur fatale et le message `error: could not create 'gurobipy.egg-info': Read-only file system`. Copiez les fichiers ailleurs (par exemple dans /tmp/$USER) où l'installation sera faite, comme ci-dessous :

```console
(env_gurobi) [name@server ~] $ mkdir /tmp/$USER
(env_gurobi) [name@server ~] $ cp -r $EBROOTGUROBI/{lib,setup.py} /tmp/$USER
(env_gurobi) [name@server ~] $ cd /tmp/$USER
(env_gurobi) [name@server ~] $ python setup.py install
/home/roberpj/env_gurobi/lib/python3.11/site-packages/setuptools/_core_metadata.py:158: SetuptoolsDeprecationWarning: Invalid config.
!!

        ********************************************************************************
        newlines are not allowed in `summary` and will break in the future
        ********************************************************************************

!!
  write_field('Summary', single_line(summary))
removing /tmp/roberpj/build
(env_gurobi) [roberpj@gra-login1:/tmp/roberpj] 
(env_gurobi) [name@server ~] $ deactivate
[name@server ~]
```

### Versions Gurobi 11.0.0 et plus récentes

Encore une fois, les étapes suivantes doivent être effectuées une fois pour chaque système sous StdEnv/2023 et les versions antérieures. Chargez d'abord les modules dans [Créer et utiliser un environnement virtuel](python.md), puis activez-le. La version 11.0.0 est ignorée car il a été observé qu'elle produit une erreur de segmentation dans au moins un exemple, comparé à la version 11.0.1 qui fonctionne sans problème.

```console
[name@server ~] $ module load gurobi/11.0.1 python
[name@server ~] $ virtualenv --no-download  ~/env_gurobi
[name@server ~] $ source ~/env_gurobi/bin/activate
```

Comme précédemment, installez tous les paquets Python nécessaires. Étant donné que l'exemple suivant nécessite `numpy` (une dépendance de Pandas), nous installons le paquet `pandas`.

```console
(env_gurobi) [name@server ~] $ pip install --no-index  pandas
```

Installez ensuite gurobipy dans l'environnement. Comme mentionné ci-dessus et dans [cet article](https://support.gurobi.com/hc/en-us/articles/360044290292-How-do-I-install-Gurobi-for-Python), l'utilisation de `setup.py` pour installer Gurobi pour Python est déconseillée à partir de Gurobi 11. Pip et Conda sont tous deux proposés comme alternatives; cependant, comme Conda ne doit pas être utilisé sur nos systèmes, l'approche avec Pip sera démontrée ici. L'installation de `gurobipy` est légèrement compliquée car nos systèmes Linux sont configurés avec le préfixe Gentoo. En conséquence, ni A) la commande recommandée pour télécharger et installer l'extension `gurobipy` depuis le serveur public PyPI (`pip install gurobipy==11.0.1`) mentionnée dans l'article, ni B) la commande hors ligne pour installer la roue avec (`python -m pip install --find-links <wheel-dir> --no-index gurobipy`) ne fonctionneront. Au lieu de cela, nous avons préparé un script pour télécharger et convertir simultanément la roue existante dans un format utilisable avec un nouveau nom. Il y a une mise en garde : pour chaque nouvelle version de Gurobi, vous devez vous rendre sur [https://pypi.org/project/gurobipy/11.0.1/#history](https://pypi.org/project/gurobipy/11.0.1/#history), cliquer sur la version souhaitée et cliquer sur le bouton *Download files* situé dans le menu de gauche. Enfin, cliquez pour copier le lien HTTPS du fichier wheel (nommé `gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl` dans le cas de Gurobi 11.0.1) et collez-le comme argument `--url` comme ci-dessous.

```console
(env_gurobi) [name@server ~] $ wget https://raw.githubusercontent.com/ComputeCanada/wheels_builder/main/unmanylinuxize.sh
(env_gurobi) [name@server ~] $ chmod u+rx unmanylinuxize.sh
(env_gurobi) [name@server ~] $ ./unmanylinuxize.sh --package gurobipy --version 11.0.1 --url https://files.pythonhosted.org/packages/1c/96/4c800e7cda4a1688d101a279087646912cf432b0f61ff5c816f0bc8503e0/gurobipy-11.0.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
(env_gurobi) [name@server ~] $ ls
gurobipy-11.0.1-cp311-cp311-linux_x86_64.whl  unmanylinuxize.sh
(env_gurobi) [name@server ~] $ python -m pip install --find-links $PWD --no-index gurobipy
(env_gurobi) [name@server ~] $ deactivate
[name@server ~]
```

### Travailler dans l'environnement avec Gurobi

Une fois créé, notre environnement Gurobi peut être activé et utilisé à tout moment. Pour démontrer cela, nous chargeons également Gurobi (donc `$EBROOTGUROBI` est défini) et `scipy-stack` (donc `scipy` est disponible). Les deux sont nécessaires pour exécuter l'exemple de matrice (avec `numpy` qui était déjà installé dans notre environnement via `pandas` lors d'une étape précédente).

```console
[name@server ~] $ module load gurobi/11.0.1 scipy-stack
[name@server ~] $ source ~/env_gurobi/bin/activate
(env_gurobi) [name@server ~]
```

Les scripts Python comme les exemples fournis avec le module Gurobi peuvent alors être exécutés dans l'environnement virtuel avec Python.

```console
(env_gurobi) [name@server ~] $ python $EBROOTGUROBI/examples/python/matrix1.py
```

De même, des scripts Python personnalisés tels que le suivant peuvent être soumis en tant que tâches à la file d'attente en écrivant des scripts Slurm qui chargent votre environnement virtuel.

```bash title="Affichage de my_gurobi_script.py"
cat my_gurobi_script.py
```
```python title="my_gurobi_script.py"
import pandas as pd
import numpy as np
import gurobipy as gurobi
from gurobipy import *
# etc.
```

Soumettez le script dans la file d'attente avec `sbatch my_slurm_script.sh`.

```bash title="my_slurm_script.sh"
#!/bin/bash
#SBATCH --account=def-somegrp  # indiquez le nom du compte
#SBATCH --time=0-00:30         # indiquez la limite de temps (jj-hh:mm)
#SBATCH --nodes=1              # utiliser un (1) nœud
#SBATCH --cpus-per-task=4      # indiquez le nombre de CPU
#SBATCH --mem=4000M            # demandez toute la mémoire

module load StdEnv/2023
module load gurobi/11.0.1
# module load scipy-stack      # décommenter si nécessaire

echo "Threads ${SLURM_CPUS_ON_NODE:-1}" > gurobi.env

source ~/env_gurobi/bin/activate
python my_gurobi_script.py
```

Pour plus d'information sur la création et l'utilisation des environnements virtuels Python, voir [Créer un environnement virtuel dans vos tâches](python.md).

## Utiliser Gurobi avec Java

Vous devez aussi charger un module Java et ajouter une option à la commande Java pour permettre à l'environnement virtuel Java de localiser les bibliothèques Gurobi, comme dans l'exemple suivant :

```bash title="gurobi-java.sh"
#!/bin/bash
#SBATCH --time=0-00:30        # limite de temps (J-HH:MM)
#SBATCH --cpus-per-task=1     # nombre de CPU (fils d'exécution) à utiliser
#SBATCH --mem=4096M           # mémoire par CPU (en Mo)

module load java/14.0.2
module load gurobi/9.1.2

java -Djava.library.path=$EBROOTGUROBI/lib -Xmx4g -jar my_java_file.jar
```

## Utiliser Gurobi avec des notebooks Jupyter

Vous trouverez de l'information sur les [ressources](https://www.gurobi.com/resources/), les [exemples de code et de modélisation](https://www.gurobi.com/resources/?category-filter=code-example) et les [exemples de modélisation avec Python dans les notebooks Jupyter](https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/). Sur le site [support.gurobi.com](https://support.gurobi.com/), faites une recherche avec *Jupyter Notebooks*.

Voir aussi cette [démonstration (à 38min 28sec de la vidéo)](https://youtu.be/Qk3Le5HBxeg?t=2310).

## Comment citer Gurobi

Voir [How do I cite Gurobi software for an academic publication?](https://support.gurobi.com/hc/en-us/articles/360013195592-How-do-I-cite-Gurobi-software-for-an-academic-publication/).

## Obtenir de l'aide

Le centre d'aide général de Gurobi se trouve [ici](https://support.gurobi.com/hc/en-us).
Gurobot, un nouvel agent IA de Gurobi, est disponible [ici](https://portal.gurobi.com/iam/chat).
La documentation officielle en ligne de Gurobi se trouve [ici](https://docs.gurobi.com/13.0/).
Pour obtenir de l'aide sur l'utilisation de Gurobi sur l'Alliance, [soumettez un billet](../support/technical_support.md).