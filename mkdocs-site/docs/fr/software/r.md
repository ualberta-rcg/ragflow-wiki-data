---
title: "R/fr"
slug: "r"
lang: "fr"

source_wiki_title: "R/fr"
source_hash: "23670861b516ec12ef0031cd2584c136"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:46:28.651000+00:00"

tags:
  - software

keywords:
  - "paquets R"
  - "tâche en lots"
  - "module gcc"
  - "performance"
  - "SBATCH"
  - "exécution de scripts"
  - "parallel computing"
  - "sbatch"
  - "système dorsal"
  - "foreach"
  - "script R"
  - "mpirun"
  - "sbatch job.sh"
  - "doParallel"
  - "Appels système"
  - "installation de paquets"
  - "makeCluster"
  - "glm"
  - "Dépendances"
  - "module load"
  - "nœuds de calcul"
  - "mémoire par coeur CPU"
  - "Arguments de script R"
  - "Installation de paquets R"
  - "parallélisation"
  - "nombre de cœurs"
  - "script job.sh"
  - "variable"
  - "programmation parallèle"
  - "problèmes de performance"
  - "mpi.remote.exec"
  - "supercalculateurs"
  - "Rmpi"
  - "calcul statistique"
  - "langage R"
  - "compilateurs GNU"
  - "SLURM"
  - "Modules"
  - "Rscript"
  - "processus MPI"
  - "paramètres"
  - "itérations de façon séquentielle"
  - "arguments"
  - "soumettre des tâches"
  - "script"
  - "OpenMPI"

questions:
  - "Qu'est-ce que le langage R et comment parvient-il à offrir de bonnes performances sur un nœud de calcul malgré sa conception initiale ?"
  - "Quelle est la procédure pour exécuter des scripts R de manière non interactive et soumettre des tâches de longue durée à l'ordonnanceur ?"
  - "Quelles sont les contraintes et les recommandations spécifiques à suivre lors de l'installation de nouveaux paquets R sur les grappes de calcul ?"
  - "Comment doit-on procéder pour configurer l'environnement, installer un paquet R et gérer ses dépendances logicielles sur la grappe de calcul ?"
  - "Quelle syntaxe spécifique est recommandée pour effectuer des appels système dans R afin d'éviter les problèmes liés à la variable d'environnement ?"
  - "Comment peut-on passer des paramètres en argument à un script R lors de son exécution en ligne de commande pour éviter de modifier le code source ?"
  - "Pourquoi est-il impossible d'installer des paquets R lors d'une tâche en lots ou interactive sur les nœuds de calcul ?"
  - "Quel module spécifique est-il recommandé de charger avant de procéder à l'installation de ces paquets ?"
  - "Quelle précaution doit-on prendre concernant la version du compilateur lors de l'installation des paquets R ?"
  - "Quel est l'avantage principal de passer des paramètres à un script R via la ligne de commande plutôt que de les modifier dans le code ?"
  - "Quelle est la syntaxe utilisée pour exécuter un script R en lui fournissant des arguments externes ?"
  - "Quels sont les types et les rôles spécifiques attendus pour les deux arguments dans le dernier exemple présenté ?"
  - "Comment un script R peut-il lire et traiter les arguments passés en ligne de commande ?"
  - "Quelles optimisations du code séquentiel sont recommandées avant d'entreprendre la parallélisation d'un script R ?"
  - "Quel est le rôle de l'interface `foreach` et pourquoi est-il crucial d'enregistrer le système dorsal avant de l'utiliser ?"
  - "Quelle est la méthode générale et la syntaxe requise pour utiliser la fonction foreach en parallèle dans un script R ?"
  - "Comment utiliser les variables d'environnement de SLURM pour définir dynamiquement le nombre de cœurs alloués à une tâche avec registerDoParallel ?"
  - "Comment configurer et enregistrer une grappe de calcul multi-nœuds de type PSOCK en utilisant doParallel et makeCluster ?"
  - "Dans quel type de situation la fonction foreach rencontre-t-elle des problèmes de performance connus ?"
  - "Quelle information précise doit être indiquée lors de l'enregistrement du système dorsal ?"
  - "Que se passe-t-il lors de l'exécution de foreach si le système dorsal n'a pas été préalablement enregistré ?"
  - "How is the parallel computing cluster set up and registered in the provided code?"
  - "What specific data manipulation is performed on the `iris` dataset before running the trials?"
  - "What statistical model and sampling method are being executed inside the parallel `foreach` loop?"
  - "Comment configurer un script SLURM pour soumettre une tâche R et forcer la répartition des processus sur différents nœuds ?"
  - "Quelles sont les étapes et les modules nécessaires pour installer manuellement le paquet Rmpi dans un environnement de grappe de calcul ?"
  - "Comment le code R utilisant la bibliothèque Rmpi doit-il être structuré pour créer des processus esclaves et exécuter des commandes à distance ?"
  - "Quel est le but des fonctions MPI exécutées dans le code R fourni ?"
  - "Quelles ressources de calcul sont demandées via les directives SBATCH dans le script job.sh ?"
  - "Quelle action l'utilisateur doit-il effectuer avec le code bash présenté dans les instructions ?"
  - "Comment soumettre le script de tâche à l'ordonnanceur selon les instructions fournies ?"
  - "Quels modules spécifiques et variables d'environnement doivent être configurés avant l'exécution du code ?"
  - "Quelle commande est utilisée pour lancer l'exécution du script R avec MPI ?"
  - "Comment soumettre le script de tâche à l'ordonnanceur selon les instructions fournies ?"
  - "Quels modules spécifiques et variables d'environnement doivent être configurés avant l'exécution du code ?"
  - "Quelle commande est utilisée pour lancer l'exécution du script R avec MPI ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

R est un outil de calcul statistique et de graphiques. Il s'agit d'un langage de programmation additionné d'un environnement graphique, d'un débogueur, de l'accès à certaines fonctions de système et de la possibilité d'exécuter des scripts.

Même si R n'a pas été développé pour le calcul de haute performance, sa popularité au sein de plusieurs disciplines scientifiques incluant le génie, les mathématiques, la statistique et la bio-informatique, en fait un outil essentiel sur les supercalculateurs dédiés à la recherche universitaire. Certaines fonctionnalités étant écrites en C, compilées et parallélisées par fils d'exécution, permettent d'atteindre des performances raisonnables sur un seul nœud de calcul. Grâce à la nature modulaire de R, les utilisateurs peuvent personnaliser leur configuration en installant des paquets dans leur répertoire personnel à partir du *Comprehensive R Archive Network* ([CRAN](https://cran.r-project.org/)).

Vous trouverez peut-être des informations utiles dans le billet de blogue de l'utilisatrice Julie Fortin intitulé [*Comment exécuter son script R avec Calcul Canada*](https://medium.com/the-nature-of-food/how-to-run-your-r-script-with-compute-canada-c325c0ab2973).

## Interpréteur
Chargez d'abord un module R. Comme plusieurs versions sont disponibles, consultez la liste en lançant la commande

```bash
module spider r
```

Pour charger un module R particulier, utilisez une variante de la commande

```bash
module load r/4.5.0
```

Pour plus d'information, consultez [Utiliser des modules](../programming/utiliser_des_modules.md).

Vous pouvez maintenant démarrer l'interpréteur et entrer le code R dans cet environnement.

```r
R
```

```text title="Sortie"
R version 4.5.0 (2025-04-11) -- "How About a Twenty-Six"
Copyright (C) 2025 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> values <- c(3,5,7,9)
> values[1]
[1] 3
> q()
```

Pour exécuter des scripts R de manière non interactive, utilisez la commande `Rscript` suivie du fichier contenant les commandes R :

```bash
Rscript computation.R
```

Cette commande passera automatiquement les options appropriées pour un traitement en lot, soit `--slave` et `--no-restore` à l'interpréteur R. Ces options empêcheront la création de fichiers d'espace de travail inutiles avec `--no-save` lors d'un traitement en lot.

!!! attention "Considération importante"
    Les calculs d'une durée de plus de deux ou trois minutes ne devraient pas être exécutés par un nœud de calcul, mais être soumis à l'ordonnanceur.

Voici un exemple de script simple :
```bash title="job.sh"
#!/bin/bash
#SBATCH --account=def-someacct   # replace this with your own account
#SBATCH --mem-per-cpu=2000M      # memory; default unit is megabytes
#SBATCH --time=0-00:15           # time (DD-HH:MM)
module load StdEnv/2023 r/4.5.0  # Adjust version as needed

Rscript computation.R
```

Pour plus d'information, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

## Installation des paquets R

### install.packages()

Pour installer des paquets du [CRAN](https://cran.r-project.org/), vous pouvez utiliser `install.packages` dans une session R interactive sur un nœud de connexion. Puisque les nœuds de calcul de la plupart de nos grappes n'ont pas accès à l'internet, il n'est pas possible d'installer les paquets R dans une tâche en lots ou dans une tâche interactive. Parce que plusieurs paquets R sont développés avec la famille de compilateurs GNU, nous vous recommandons de [charger un module `gcc`](../programming/utiliser_des_modules.md) avant de les installer et de toujours utilisez la même version du `gcc`.

```bash
module load gcc/12.3.0 r/4.5.0
```

#### Installation pour une version particulière de R
Par exemple, pour installer le paquet `sp` qui offre des classes et des méthodes pour les données spatiales, utilisez cette commande sur un nœud de connexion.

```r
R
```

```text title="Sortie"
[...]
> install.packages('sp', repos='https://cloud.r-project.org/')
```

Si l'argument `repos` n'est pas spécifié, on vous demandera de sélectionner un miroir pour le téléchargement. Idéalement, ce miroir sera géographiquement proche de la grappe que vous utilisez.

Avant l'installation, certains paquets requièrent la définition de la variable d'environnement `TMPDIR`.

#### Installation pour une ou plusieurs versions de R
Indiquez le répertoire local, selon le module de R qui est chargé.
```bash
mkdir -p ~/.local/R/$EBVERSIONR/
export R_LIBS=~/.local/R/$EBVERSIONR/
```

Installez le paquet.
```r
R -e 'install.packages("sp", repos="https://cloud.r-project.org/")'
```

Dans le script de soumission, vous devez ensuite charger le module R que vous voulez et configurer le répertoire local pour la bibliothèque avec `export R_LIBS=~/.local/R/$EBVERSIONR/`.

### Dépendances
Certains paquets utilisent des bibliothèques qui sont déjà installées sur nos grappes. Si la bibliothèque se trouve dans la liste des [logiciels disponibles](../programming/available_software.md), chargez le [module](../programming/utiliser_des_modules.md) approprié avant d'installer le paquet.

Par exemple, le paquet `rgdal` utilise la bibliothèque `gdal`. En lançant la commande `module spider gdal/2.2.1` nous voyons que les modules `nixpkgs` et `gcc` sont requis. Pour savoir comment charger ce module, entrez la commande `module spider gdal/3.9.1`.

Si l'installation d'un paquet échoue, portez attention au message d'erreur qui pourrait indiquer d'autres modules qui seraient requis. Pour plus d'information sur les commandes de `module`, consultez [Utiliser des modules](../programming/utiliser_des_modules.md).

### Téléchargement de paquets
Si vous cherchez à installer un paquet que vous avez téléchargé, c'est-à-dire que vous n'avez pas utilisé `install.packages()`, vous pouvez l'installer comme suit. Par exemple, avec le paquet `archive_package.tgz`, vous exécuteriez la commande suivante dans l'interpréteur (*shell*)

```bash
R CMD INSTALL -l 'path for your local (home) R library' archive_package.tgz
```

## Appels système

La commande R `system()` permet d'exécuter des commandes dans l'environnement actif, à l'intérieur de R; ceci risque de causer des problèmes sur nos grappes parce que R donne une valeur incorrecte à la variable d'environnement `LD_LIBRARY_PATH`. Utilisez plutôt la syntaxe `system("LD_LIBRARY_PATH=$RSNT_LD_LIBRARY_PATH <my system call>")` dans vos appels système.

## Arguments passés à un script R
Il peut parfois être utile de passer des paramètres en argument à un script R pour éviter d'avoir à modifier le script pour plusieurs tâches semblables ou de devoir gérer plusieurs copies d'un même script. Ceci peut servir pour spécifier des paramètres numériques ou le nom des fichiers en entrée ou en sortie. Par exemple, au lieu d'employer une syntaxe comme
```r
filename = "input.csv"
iterations = 5
```

et de changer le code à chaque fois qu'un paramètre est modifié, les paramètres peuvent être passés au script au début avec

```bash
Rscript myscript.R input_1.csv 5
```

et par la suite

```bash
Rscript myscript.R input_2.csv 10
```

Dans le prochain exemple, il doit y avoir précisément deux arguments. Le premier devrait être une chaîne de caractères représentant le **nom** de la variable et le deuxième devrait **numéro** de la variable.
```r title="arguments_test.R"
args = commandArgs(trailingOnly=TRUE)

# test if there is at least two arguments: if not, return an error
if (length(args)<2) {
  stop("At least two arguments must be supplied ('name' (text) and 'numer' (integer) )", call.=FALSE)
}

name      <- args[1]                # read first argument as string
number    <- as.integer( args[2] )  # read second argument as integer

print(paste("Processing with name:'", name, "' and number:'", number,"'", sep = ''))
```

Ce script peut être utilisé comme suit
```bash
Rscript arguments_test.R Hello 42
```

```text title="Sortie"
[1] "Processing with name:'Hello' and number:'42'"
```

## Parallélisation

Si les processeurs de nos grappes sont on ne peut plus ordinaires, ce qui rend ces *supercalculateurs* intéressants, c'est qu'ils offrent des milliers de CPU sur un réseau très performant. Pour profiter de cet avantage, vous devez utiliser la programmation parallèle. Cependant, avant d'allouer beaucoup de temps et d'effort à paralléliser votre code R, assurez-vous que votre implémentation séquentielle est aussi efficiente que possible. Comme dans tout langage interprété, d'importants *goulots d'étranglement* sont causés par les boucles et particulièrement les boucles imbriquées, ce qui a un impact sur la performance. Lorsque possible, essayez d'utiliser les fonctions vectorielles et les autres éléments plus fonctionnels comme la famille des fonctions `apply` et la fonction `ifelse`. Vous obtiendrez souvent un gain de performance en éliminant une boucle plutôt que de paralléliser son exécution avec plusieurs cœurs CPU.

La page [CRAN Task View on High-Performance and Parallel Computing with R](https://cran.r-project.org/web/views/HighPerformanceComputing.html) mentionne un grand nombre de paquets pouvant être utilisés avec R pour la programmation parallèle.
Vous trouverez une excellente vue d'ensemble et des conseils dans le contenu du [colloque de Calcul Ontario du 11 octobre 2023 intitulé *High-Performance Computing in R*](https://education.scinet.utoronto.ca/course/view.php?id=1333) ([diapositives](https://education.scinet.utoronto.ca/mod/resource/view.php?id=2887)).

Vous trouverez d'autres renseignements et exemples dans les sous-sections ci-dessous.

!!! info "Terminologie"
    Dans notre documentation, les termes *nœud* et *hôte* sont quelquefois employés pour désigner un ordinateur distinct; un regroupement de *nœuds* ou d'*hôtes* constitue une *grappe*.
    *nœud* désigne souvent un *processus de travail* (worker process); un regroupement de ces processus constitue une *grappe*. Prenons comme exemple la citation suivante : « Following **snow**, a pool of worker processes listening *via* sockets for commands from the master is called a 'cluster' of nodes. »[^1].

### doParallel et foreach
#### Utilisation
`foreach` peut être vu comme une interface unifiée pour tous les *systèmes dorsaux* comme `doMC`, `doMPI`, `doParallel`, `doRedis`, etc. et fonctionne sur toutes les plateformes pourvu que le système dorsal soit fonctionnel. `doParallel` agit comme interface entre `foreach` et le paquet parallèle et peut être chargé seul. Certains [problèmes de performance connus](extensibilite.md) surviennent avec `foreach` lors de l'exécution d'un très grand nombre de très petites tâches. Notez que l'exemple simple qui suit n'utilise pas l'appel `foreach()` de façon optimale.

Enregistrez le système dorsal en lui indiquant le nombre de cœurs disponibles. Si le système dorsal n'est pas enregistré, `foreach` assume que le nombre de cœurs est 1 et exécute les itérations de façon séquentielle.

La méthode générale pour utiliser `foreach` est :
1.  chargez `foreach` et le paquet dorsal;
2.  enregistrez le paquet dorsal;
3.  appelez `foreach()` en le laissant sur la même ligne que l'opérateur `%do%` (série) ou `%dopar%`.

#### Exécution
1.  Placez le code R dans un fichier script, ici le fichier *test_foreach.R*.

```r title="test_foreach.R"
# library(foreach) # optionnel si doParallel est utilisé
library(doParallel) #

# a very simple function
test_func <- function(var1, var2) {
    # some heavy workload
    sum <- 0
    for (i in c(1:3141593)) {
        sum <- sum + var1 * sin(var2 / i)
    }
    return(sqrt(sum))
}

# nous allons itérer selon deux ensembles de valeurs que vous pouvez modifier pour tester le fonctionnement de foreach
var1.v = c(1:8)
var2.v = seq(0.1, 1, length.out = 8)

# La variable d'environnement SLURM_CPUS_PER_TASK contient le nombre de coeurs par tâche.
# Elle est définie par SLURM.
# Évitez de fixer un nombre de coeurs manuellement dans le code source.
ncores = Sys.getenv("SLURM_CPUS_PER_TASK")

registerDoParallel(cores=ncores) # Demande ncores "Parallel Workers"
print(ncores) # Affiche le nombre de coeurs disponibles et demandé
getDoParWorkers() # Affiche le nombre de "Parallel Workers" actuel

# attention! foreach() et %dopar% doivent être sur la même ligne de code!
foreach(var1=var1.v, .combine=rbind) %:% foreach(var2=var2.v, .combine=rbind) %dopar% {test_func(var1=var1, var2=var2)}
```

Copiez ce qui suit dans le script *job_foreach.sh*.

```bash title="job_foreach.sh"
#!/bin/bash
#SBATCH --account=def-someacct   # replace this with your supervisors account
#SBATCH --nodes=1                # number of node MUST be 1
#SBATCH --cpus-per-task=4        # number of processes
#SBATCH --mem-per-cpu=2048M      # memory; default unit is megabytes
#SBATCH --time=0-00:15           # time (DD-HH:MM)

module load StdEnv/2023 r/4.5.0

export R_LIBS=~/local/R_libs/
R CMD BATCH --no-save --no-restore test_foreach.R
```

3.  Soumettez la tâche.

```bash
sbatch job_foreach.sh
```

Pour plus d'information sur comment soumettre des tâches, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

### doParallel et makeCluster
#### Utilisation
Il faut enregistrer le système dorsal en lui donnant le nom des nœuds, multiplié par le nombre voulu de processus. Par exemple, nous créerions une grappe composée des hôtes `node1 node1 node2 node2`. Le type de grappe *PSOCK* exécute des commandes par des connexions SSH vers les nœuds.

#### Exécution
1.  Placer le code R dans un fichier script, ici `test_makecluster.R`.
```r title="test_makecluster.R"
library(doParallel)

# Create an array from the NODESLIST environnement variable
nodeslist = unlist(strsplit(Sys.getenv("NODESLIST"), split=" "))

# Create the cluster with the nodes name. One process per count of node name.
# nodeslist = node1 node1 node2 node2, means we are starting 2 processes on node1, likewise on node2.
cl = makeCluster(nodeslist, type = "PSOCK")
registerDoParallel(cl)

# Compute (Source : https://cran.r-project.org/web/packages/doParallel/vignettes/gettingstartedParallel.pdf)
x <- iris[which(iris[,5] != "setosa"), c(1,5)]
trials <- 10000

foreach(icount(trials), .combine=cbind) %dopar%
    {
    ind <- sample(100, 100, replace=TRUE)
    result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
    coefficients(result1)
    }

# Don't forget to release resources
stopCluster(cl)
```

2.  Copiez les lignes suivantes dans un script pour soumettre la tâche, ici `job_makecluster.sh`.
```bash title="job_makecluster.sh"
#!/bin/bash
#SBATCH --account=def-someacct  # à remplacer par un compte approprié
#SBATCH --ntasks=4              # nombre de processus
#SBATCH --mem-per-cpu=512M      # mémoire par coeur CPU; valeur en Mo par défaut
#SBATCH --time=00:05:00         # temps (HH:MM:SS)

module load StdEnv/2023 r/4.5.0

# Export the nodes names.
# If all processes are allocated on the same node, NODESLIST contains : node1 node1 node1 node1
# Cut the domain name and keep only the node name
export NODESLIST=$(echo $(srun hostname | cut -f 1 -d '.'))
R -f test_makecluster.R
```

Dans cet exemple, l'ordonnanceur pourrait placer les quatre processus sur un seul nœud.
Ceci peut convenir, mais si vous voulez prouver que la même tâche peut être traitée si les processus
sont placés sur des nœuds différents, ajoutez la ligne `#SBATCH --ntasks-per-node=2`.

3.  Soumettez la tâche avec

```bash
sbatch job_makecluster.sh
```

Pour plus d'information sur comment soumettre une tâche, voyez [Exécuter des tâches](../running-jobs/running_jobs.md).

### Rmpi

#### Installation
La procédure suivante installe [Rmpi](https://cran.r-project.org/web/packages/Rmpi/index.html), une interface pour les routines MPI qui permet d'exécuter R en parallèle.

1.  Voyez les modules R disponibles avec la commande
```bash
module spider r
```

2.  Sélectionnez la version de R et chargez le module OpenMPI approprié.
```bash
module load gcc/12.3
module load openmpi/4.1.5
module load r/4.5.0
```

3.  Téléchargez [la dernière version de Rmpi](https://cran.r-project.org/web/packages/Rmpi/index.html) en remplaçant le numéro de la version selon le cas.
```bash
wget https://cran.r-project.org/src/contrib/Rmpi_0.7-3.3.tar.gz
```

4.  Indiquez le répertoire dans lequel vous voulez copier les fichiers; vous devez avoir une permission d'écriture pour ce répertoire. Le nom du répertoire peut être modifié.
```bash
mkdir -p ~/local/R_libs/
export R_LIBS=~/local/R_libs/
```

5.  Lancez la commande d'installation.
```bash
R CMD INSTALL --configure-args="--with-Rmpi-include=$EBROOTOPENMPI/include --with-Rmpi-libpath=$EBROOTOPENMPI/lib --with-Rmpi-type='OPENMPI' " Rmpi_0.7-3.3.tar.gz
```

Portez attention au message d'erreur qui s'affiche quand l'installation d'un paquet échoue; il pourrait indiquer d'autres modules qui seraient nécessaires.

#### Exécution
1.  Placez le code R dans un fichier script, ici le fichier *test.R*.

```r title="test.R"
#Tell all slaves to return a message identifying themselves.
library("Rmpi")
sprintf("TEST mpi.universe.size() =  %i", mpi.universe.size())
ns <- mpi.universe.size() - 1
sprintf("TEST attempt to spawn %i slaves", ns)
mpi.spawn.Rslaves(nslaves=ns)
mpi.remote.exec(paste("I am",mpi.comm.rank(),"of",mpi.comm.size()))
mpi.remote.exec(paste(mpi.comm.get.parent()))
#Send execution commands to the slaves
x<-5
#These would all be pretty correlated one would think
x<-mpi.remote.exec(rnorm,x)
length(x)
x
mpi.close.Rslaves()
mpi.quit()
```

2.  Copiez ce qui suit dans le script *job.sh*.

```bash title="job.sh"
#!/bin/bash
#SBATCH --account=def-someacct   # à remplacer par un compte approprié
#SBATCH --ntasks=5               # nombre de processus MPI
#SBATCH --mem-per-cpu=2048M      # mémoire par coeur CPU; valeur en Mo par défaut
#SBATCH --time=0-00:15           # temps (JJ-HH:MM)

module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 r/4.5.0

export R_LIBS=~/local/R_libs/
mpirun -np 1 R CMD BATCH test.R test.txt
```

3.  Soumettez la tâche.

```bash
sbatch job.sh
```

Pour plus d'information sur comment soumettre des tâches, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

[^1]: https://stat.ethz.ch/R-manual/R-devel/library/parallel/doc/parallel.pdf