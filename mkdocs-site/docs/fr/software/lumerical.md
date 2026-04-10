---
title: "Lumerical/fr"
slug: "lumerical"
lang: "fr"

source_wiki_title: "Lumerical/fr"
source_hash: "8a5edcbbba94ec0a386eedce4cb5aa18"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:58:29.911177+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[Lumerical](https://www.lumerical.com/) est une suite logicielle pour la modélisation d'appareils [nanophotoniques](https://en.wikipedia.org/wiki/Nanophotonics); elle contient les applications [FDTD Solutions](https://www.lumerical.com/tcad-products/fdtd/).

# Installation
Les applications FDTD Solutions sont maintenant intégrées au paquet Lumerical. Il n'y a pas d'installation centrale de ces logiciels sur l'infrastructure nationale, mais si vous disposez d'une licence, vous pouvez les installer en suivant les directives ci-dessous.

Si vous avez téléchargé la suite Lumerical au complet (fichier `Lumerical-2020a-r1-d316eeda68.tar.gz`), voyez les sections *Installer Lumerical* et *Utiliser le module Lumerical*.
Si vous avez téléchargé seulement Lumerical (fichier `FDTD_Solutions-8.19.1438.tar.gz`), voyez les sections *Installer FDTD Solutions* et *Utiliser le module fdtd_solutions*.

## Installer Lumerical
### Si la version de l'installateur correspond exactement à celle de la recette
Pour installer la suite Lumerical, lancez

```bash
eb Lumerical-2020a-r1-d316eeda68.eb --sourcepath=<path> --disable-enforce-checksums
```

où `path` est le chemin vers le répertoire qui contient le fichier `.tar.gz` pour installer Lumerical sous Linux.

### Si la version de l'installateur ne correspond pas exactement à celle de la recette
Avec une version 2020a différente de 2020a-r1-d316eeda68, lancez

```bash
eb Lumerical-2020a-r1-d316eeda68.eb --try-software-version=<version> --sourcepath=<path> --disable-enforce-checksums
```

Par exemple, si `Lumerical-2020a-r1-d316eeda68.eb.tar.gz` a été téléchargé dans `$HOME/scratch`, la commande suivante installera Lumerical dans votre répertoire `$HOME/.local`.

```bash
eb Lumerical-2020a-r1-d316eeda68.eb --try-software-version=2020a-r6-aabbccdd --sourcepath=$HOME/scratch --disable-enforce-checksums
```

La version de la recette (année suivie de "a" ou "b") doit être la même que celle de l'installateur.
Si l'année ou la lettre est différente (par exemple recette 2020a et installateur 2020b), nous devrons adapter le script d'installation.

En date du 1er avril 2020, les recettes suivantes sont disponibles :

| Recette pour l'installation | Version de l'installeur | Version compatible |
| :------------------------------------------------ | :---------------------------------------------------- | :------------------------------------- |
| `Lumerical-2019b-r6-1db3676.eb` | `Lumerical-2019b-r6-1db3676.tar.gz` | `Lumerical-2019b-*.tar.gz` |
| `Lumerical-2020a-r1-d316eeda68.eb` | `Lumerical-2020a-r1-d316eeda68.tar.gz` | `Lumerical-2020a-*.tar.gz` |
| `Lumerical-2021-R2.5-2885-27742aa972.eb` | `Lumerical-2021-R2.5-2885-27742aa972.tar.gz` | `Lumerical-2021-*.tar.gz` |
| `Lumerical-2022-R1.3-3016-2c0580a.eb` | `Lumerical-2022-R1.3-3016-2c0580a.tar.gz` | `Lumerical-2022-*.tar.gz` |

Si ces directives ne fonctionnent pas, contactez le [soutien technique](technical-support.md) et nous adapterons une recette pour l'installation de votre version.

Une fois l'installation terminée, vous devez vous déconnecter et vous reconnecter au serveur. Chargez ensuite le module Lumerical avec

```bash
module load lumerical
```

### Configurer le fichier de licence

Le module Lumerical cherchera le fichier `$HOME/.licenses/lumerical.lic` pour savoir comment contacter le serveur de licence.
Créez le fichier avec le contenu suivant, en ajustant `27011@license01.example.com` en fonction du port et du *hostname* de votre serveur de licence.

Copiez la ligne suivante dans le fichier **$HOME/.licenses/lumerical.lic** :

```
setenv("LUMERICAL_LICENSE_FILE", "27011@license01.example.com")
```

## Installer FDTD Solutions
Pour installer FDTD Solutions, lancez la commande

```bash
eb FDTD_Solutions-8.19.1438.eb --sourcepath=<path> --disable-enforce-checksums
```

où `path` est le chemin vers le répertoire qui contient le fichier `.tar.gz` pour l'installation sous Linux.

Si vous avez une autre version que 8.19.1438, utilisez

```bash
eb FDTD_Solutions-8.19.1438.eb --try-software-version=<version> --sourcepath=<path> --disable-enforce-checksums
```

Par exemple, si `FDTD_Solutions-8.19.1466.tar` a été téléchargé dans `$HOME/Downloads`, la commande suivante installera FDTD Solutions
à l'intérieur du dossier `$HOME/.local`.

```bash
eb FDTD_Solutions-8.19.1438.eb --try-software-version=8.19.1466 --sourcepath=$HOME/Downloads --disable-enforce-checksums
```

En cas de difficulté, communiquez avec le [soutien technique](technical-support.md) qui adaptera un script d'installation pour votre version.

Après l'installation, il faut se déconnecter du serveur et se connecter de nouveau. Pour charger le module, utilisez

```bash
module load fdtd_solutions
```

Vous devez aussi configurer votre installation pour utiliser votre serveur de licence. Démarrez l'application d'abord sur un nœud de connexion et on vous demandera l'information sur votre serveur de licence; il ne sera pas nécessaire de répéter cette opération.

# Utilisation
Le module `lumerical` possède plus d'outils que le module `fdtd_solutions`, mais la principale différence est que la variable d'environnement qui contient l'emplacement pour l'installation se nomme `EBROOTLUMERICAL` dans un cas et `EBROOTFDTD_SOLUTIONS` dans l'autre. Les scripts doivent donc être ajustés en fonction du module utilisé en indiquant le nom correspondant du module dans la ligne `module load ...` et `EBROOTFDTD_SOLUTIONS` par `EBROOTLUMERICAL`, selon le cas.

## Utiliser le module Lumerical

L'implémentation MPI fournie par Lumerical ne fonctionne pas étroitement avec notre ordonnanceur; pour cette raison, utilisez les options `--ntasks-per-node=1` et `--cpus-per-task=32` quand vous soumettrez une tâche.

L'exemple suivant est un script qui demande 2 nœuds pour une durée de 30 minutes; vous pouvez adapter ce script selon vos besoins.

````sh linenums="1" hl_lines="" title="lumrical_job.sh"
#!/bin/bash
#SBATCH --time=0:30:00            # time limit (D-HH:MM:SS)
#SBATCH --ntasks-per-node=1       # do not change this number
#SBATCH --cpus-per-task=32        # adjust to number of cores per node
#SBATCH --ntasks=2       # the same number as nodes, one task per node
#SBATCH --nodes=2
#SBATCH --mem=0          # special value, requests all memory on node
module load lumerical

MPI=$EBROOTLUMERICAL/mpich2/nemesis/bin/mpiexec
MY_PROG=$EBROOTLUMERICAL/bin/fdtd-engine-mpich2nem

INPUT="avalanche_photodetector_optical.fsp"
NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

$MPI -n $NCORE $MY_PROG ./${INPUT}
````

## Utiliser le module fdtd_solutions
L'implémentation MPI fournie par FDTD ne fonctionne pas étroitement avec notre ordonnanceur; pour cette raison, utilisez les options `--ntasks-per-node=1` et `--cpus-per-task=32` quand vous soumettez une tâche.

Dans notre exemple de script, on demande deux nœuds pour une heure; vous pouvez utiliser ce script en remplaçant les valeurs de durée et de nombre de nœuds, selon vos besoins.

````sh linenums="1" hl_lines="" title="fdtd_solutions.sh"
#!/bin/bash
#SBATCH --time=0:30:00            # time limit (D-HH:MM:SS)
#SBATCH --ntasks-per-node=1    # do not change this number
#SBATCH --cpus-per-task=32     # do not change this number
#SBATCH --ntasks=2    # the same number as nodes, one task per node
#SBATCH --nodes=2
#SBATCH --mem=0       # special value, requests all memory on node
module load fdtd_solutions
MPI=$EBROOTFDTD_SOLUTIONS/mpich2/nemesis/bin/mpiexec
MY_PROG=$EBROOTFDTD_SOLUTIONS/bin/fdtd-engine-mpich2nem

INPUT="benchmark2.fsp"
NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))
$MPI -n $NCORE $MY_PROG ./${INPUT}
````

## Gabarits de scripts

!!! note
    Cette section a été rédigée pour le module `fdtd_solutions` et n'est pas adaptée au module `lumerical`.

Si vous avez plusieurs simulations à faire exécuter, il ne serait pas très efficace d'avoir à modifier le script pour chacune d'elles. Vous pouvez alors utiliser un gabarit de script.

Par exemple,
*   Créez le répertoire `$HOME/bin` et enregistrez-y le script `fdtd-run.sh` (voir ci-dessous).
*   Créez le répertoire `$HOME/bin/templates` et enregistrez-y les gabarits de scripts `fdtd-mpi-template.sh` et `fdtd-process-template.sh`.

`fdtd-mpi-template.sh` est en fait un interpréteur (*shell*) du script `fdtd_solutions.sh` présenté ci-dessus et `fdtd-process-template.sh` indique les ressources de calcul dont vous avez besoin.

Pour soumettre une tâche, utilisez

```bash
fdtd-run.sh fsp1 [fsp2 ...]
```

Ceci utilisera 32 cœurs sur un seul nœud standard. Pour utiliser plus de cœurs, demandez plusieurs nœuds comme suit

```bash
fdtd-run.sh -nn <nodes> fsp1 [fsp2 ...]
```

````sh linenums="1" hl_lines="" title="fdtd-run.sh"
#!/bin/bash
# This script will create a Slurm-style job submission script for
# FDTD Solutions project files using the template provided in
# templates/fdtd-mpi-template.sh. Certain tags in the template
# file are replaced with values extracted from the project file.
#
# The calling convention for this script is:
#
# fdtd-run.sh [-nn <nodes>] fsp1 [fsp2 ... fspN]
#
# The arguments are as follows:
#
# -nn       The number of nodes to use for the job(s).
#           If no argument is given one node is used.
#
# fsp*      An FDTD Solutions project file. One is required, but
#           multiple can be specified on one command line.
#
##########################################################################

# Locate the directory of this script so we can find
# utility scripts and templates relative to this path.
module load fdtd_solutions
SCRIPTDIR=$EBROOTFDTD_SOLUTIONS/bin

# The location of the template file to use when submitting jobs.
# The line below can be changed to use your own template file.
TEMPLATE=../bin/templates/fdtd-mpi-template.sh

# Number of processes per node.
PROCS=32

# Number of nodes to use. Default is 1 if no -nn argument is given.
NODES=1
if [ "$1" = "-nn" ]; then
    NODES=$2
    shift
    shift
fi

# For each fsp file listed on the command line, generate the
# submission script and submit it with sbatch.
while(( $# > 0 ))
do

    # Generate the submission script by replacing the tokens in the template.
    # Additional arguments can be added to fdtd-process-template to fine-tune
    # the memory and time estimates. See comments in that file for details.
    SHELLFILE=${1%.fsp}.sh
    ../bin/templates/fdtd-process-template.sh -ms 500 $1 $TEMPLATE $((PROCS)) > $SHELLFILE
    TOTAL_MEM=$(head -n 1 $SHELLFILE)
    sed -i -e '1,1d' $SHELLFILE

    # Submit the job script.
    echo Submitting: $SHELLFILE
    echo Total Memory Required = $TOTAL_MEM
    sbatch --nodes=${NODES} --ntasks=${NODES} --cpus-per-task=${PROCS} --mem=${TOTAL_MEM} $SHELLFILE

    shift
done
````

````sh linenums="1" hl_lines="" title="fdtd-mpi-template.sh"
#!/bin/bash
#SBATCH --time=<hours>:<minutes>:<seconds>
#SBATCH --ntasks-per-node=1

module load fdtd_solutions
MPI=$EBROOTFDTD_SOLUTIONS/mpich2/nemesis/bin/mpiexec
MY_PROG=$EBROOTFDTD_SOLUTIONS/bin/fdtd-engine-mpich2nem

INPUT="<filename>"
NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))
$MPI -n $NCORE $MY_PROG ./${INPUT}
````

````sh linenums="1" hl_lines="" title="fdtd-process-template.sh"
#!/bin/bash
# This script is used to replace tags in a submission script template with
# actual values from an FDTD Solutions project file. The script is called
# with the following arguments:
#
# fdtd-process-template.sh [options] <fsp file> <template file> <#processes>
#
# Valid options are:
#
# -r <rate>            The simulation rate in MNodes/s used in time estimates.
#                      If no option is given the default is 4MNodes/s/process
#                      which is very conservative.
#
# -tm <min_time>       The minimum time in seconds that the simulation can take.
#                      If no option is given the default is 600 seconds.
#
# -ms <memory_safety>  A multiplicative factor to apply to the memory estimate in %.
#                      If no option is given the default value is 110.
#
# -mm <memory_min>     The minimum memory that a process can use.
#                       If no option is given the default is 20MB.
#
# The script will replace the following tokens in the template file with specified values:
#
# Token                Value
# <total_memory>       The total memory required by all processes
# <processor_memory>   The memory required for each simulation process
# <hours>              The total hours required for the simulation
# <minutes>            The total minutes required for the simulation
# <seconds>            The total seconds required for the simulation
# <n>                  The number of processes to use
# <dir_fsp>            The path of the fsp project file
# <filename>           The name of the fsp project file, without a leading path
#
############################################################################################

#Rate default
RATE=4

#Minimum time default
TIME_MIN=600

#Memory safety default
MEMORY_SAFETY=110

#Minimum memory default
MEMORY_MIN=20

#Process command line options
while [ $# -gt 3 ] ; do
    case $1 in
        -r) RATE=$2
        ;;
        -tm) TIME_MIN=$2
        ;;
        -ms) MEMORY_SAFETY=$2
        ;;
        -mm) MEMORY_MIN=$2
        ;;
    esac
    shift
    shift
done

#Number of processes
PROCS=$3

#Path of fsp file
DIRFSP=`dirname $1`

#fsp file name without path
FILENAME=`basename $1`

#Run FDTD to get stats from project file
module load fdtd_solutions
SCRIPTDIR=$EBROOTFDTD_SOLUTIONS/bin
$SCRIPTDIR/fdtd-engine-mpich2nem -mr $1 > $1.tmp

#Estimated memory
ESTMEM=`grep memory $1.tmp | sed 's/^.*=//'`

#Total memory required
TOTALMEM=$(( ESTMEM * MEMORY_SAFETY / 100 ))

#Memory required per process
PROCMEM=$((TOTALMEM / PROCS))
if [ "$PROCMEM" -lt "$MEMORY_MIN" ]; then
    PROCMEM=$MEMORY_MIN
fi

#Gridpoints
GRIDPTS=`grep gridpoints $1.tmp | sed 's/^.*=//'`

#Timesteps
TIMESTEPS=`grep time_steps $1.tmp | sed 's/^.*=//'`

#Estimated time
TIME=$(( GRIDPTS * TIMESTEPS / PROCS / RATE / 10000000 ))
if [ "$TIME" -lt "$TIME_MIN" ]; then
    TIME=$TIME_MIN
fi

HOUR=$((TIME / 3600))
MINSEC=$((TIME - HOUR * 3600))
MIN=$((MINSEC / 60))
SEC=$((MINSEC - MIN * 60))

echo $TOTALMEM

#The replacements
sed -e "s#<total_memory>#$TOTALMEM#g" \
    -e "s#<processor_memory>#$PROCMEM#g" \
    -e "s#<hours>#$HOUR#g" \
    -e "s#<minutes>#$MIN#g" \
    -e "s#<seconds>#$SEC#g" \
    -e "s#<n>#$PROCS#g" \
    -e "s#<dir_fsp>#$DIRFSP#g" \
    -e "s#<filename>#$FILENAME#g" \
    $2
`