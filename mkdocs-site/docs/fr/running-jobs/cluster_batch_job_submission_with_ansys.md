---
title: "Cluster batch job submission with Ansys/fr"
slug: "cluster_batch_job_submission_with_ansys"
lang: "fr"

source_wiki_title: "Cluster batch job submission with Ansys/fr"
source_hash: "308383338e80d3361eca9632de8fd177"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:42:53.129267+00:00"

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

Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Trillium, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

## Fluent
La procédure suivante est habituellement utilisée pour exécuter Fluent sur nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *Fichier > Exporter > Cas…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que FFF-1.cas.gz.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *Fichier > Exporter > Données…* ou trouvez-le dans le même répertoire /project (FFF-1.dat.gz).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage). Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que FFF-1.* ou renommez-les au téléversement.
5.  Créez un fichier de journalisation dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancer le solveur et enregistrer les résultats. Voyez les exemples ci-dessous et n'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour les scripts décrits dans la section [Remise en file d'attente pour obtenir la licence](#remise-en-file-dattente-pour-obtenir-la-licence). Cependant, il est important de noter que cette approche peut aussi remettre en attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en attente est ou non due à un problème de licence. Si vous découvrez que la remise en attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `scancel jobid` et corrigez le problème.
7.  Lorsque [la tâche est terminée](running_jobs.md), vous pouvez télécharger le fichier de données et le retourner dans Fluent avec *Fichier > Importer > Données…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale

La plupart des tâches Fluent devraient utiliser le script ''par nœud'' ci-dessous pour minimiser le temps d'attente et maximiser la performance avec le moins de nœuds possible. Les tâches demandant beaucoup de cœurs CPU pourraient attendre moins longtemps dans la file d'attente avec le script ''par cœur'', mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent être une alternative plus robuste si Fluent plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts Intel standards avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de Fluent, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts Intel. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

=== "Plusieurs nœuds (par nœud)"

```bash title="script-flu-bynode-intel.sh"
#!/bin/bash
#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
```

=== "Plusieurs nœuds (par cœur)"

```bash title="script-flu-bycore-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
#SBATCH --ntasks=16           # Specify total number of cores across all nodes
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------
if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
```

=== "Plusieurs nœuds (par nœud, Narval)"

```bash title="script-flu-bynode-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (1 or more)
#SBATCH --ntasks-per-node=64  # Specify number of cores per node (narval 64 or less)
#SBATCH --mem=0               # Do not change (allocate all memory per compute node)
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------
export OPENMPI_ROOT=$EBROOTOPENMPI
slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
else
 export FI_PROVIDER=verbs
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
fi
```

=== "Plusieurs nœuds (par cœur, Narval)"

```bash title="script-flu-bycore-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify number of compute nodes (1 or more)
#SBATCH --ntasks=16           # Specify total number of cores across all nodes
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load StdEnv/2023       # Do not change     
module load ansys/2023R2      # or newer versions

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------
export OPENMPI_ROOT=$EBROOTOPENMPI
slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/mf-$SLURM_JOB_ID
for i in `cat /tmp/mf-$SLURM_JOB_ID | uniq`; do echo "${i}:$(cat /tmp/mf-$SLURM_JOB_ID | grep $i | wc -l)" >> /tmp/machinefile-$SLURM_JOB_ID; done
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pshmem -i $MYJOURNALFILE
else
 export FI_PROVIDER=verbs
 fluent -g $MYVERSION -t $NCORES -mpi=openmpi -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
fi
```

=== "Plusieurs nœuds (par nœud, Trillium)"

```bash title="script-flu-bynode-intel-tri.sh"
#!/bin/bash

#SBATCH --account=def-group      # Specify account name
#SBATCH --time=00-03:00          # Specify time limit dd-hh:mm
#SBATCH --nodes=1                # Specify number of compute nodes (1 or more)
#SBATCH --ntasks-per-node=16     # Specify number cores per node (max 192 on trillium)
##SBATCH --mem=0                 # Do not uncomment (be default trillium uses all memory per node)
#SBATCH --cpus-per-task=1        # Do not change (required parameter)
#SBATCH --output=slurm-%j.out    # Writes to slurm-$SLURM_JOB_ID.out

cd $SLURM_SUBMIT_DIR             # Submit from $SCRATCH/some/dir

module load StdEnv/2023          # Do not change
module load ansys/2025R2.04      # only 2025R2 or newer works on trillium

MYJOURNALFILE=sample.jou         # Specify your journal file name
MYVERSION=3d                     # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ ! -L "$HOME/.ansys" ]; then
  echo "ERROR: A link to a writable .ansys directory does not exist."
  echo 'Remove ~/.ansys if one exists and then run: ln -s $SCRATCH/.ansys ~/.ansys'
  echo "Then try submitting your job again. Aborting the current job now!"
elif [ ! -L "$HOME/.fluentconf" ]; then
  echo "ERROR: A link to a writable .fluentconf directory does not exist."
  echo 'Remove ~/.fluentconf if one exists and run: ln -s $SCRATCH/.fluentconf ~/.fluentconf'
  echo "Then try submitting your job again. Aborting the current job now!"
elif [ ! -L "$HOME/.flrecent" ]; then
  echo "ERROR: A link to a writable .flrecent file does not exist."
  echo 'Remove ~/.flrecent if one exists and then run: ln -s $SCRATCH/.flrecent ~/.flrecent'
  echo "Then try submitting your job again. Aborting the current job now!"
else
  mkdir -pv $SCRATCH/.ansys
  mkdir -pv $SCRATCH/.fluentconf
  touch $SCRATCH/.flrecent
  if [ "$SLURM_NNODES" == 1 ]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
  else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=$SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
  fi
fi
```

#### Remise en file d'attente pour obtenir la licence

!!! attention "Considérations pour la remise en file d'attente de licences"
    Les scripts ci-dessous sont spécifiquement conçus pour les tâches Fluent qui se terminent normalement sans erreurs, mais qui peuvent nécessiter plusieurs tentatives de soumission pour obtenir une licence.

    **Ils ne sont PAS recommandés pour les tâches Fluent qui pourraient :**
    1.  S'exécuter pendant une longue période avant de planter.
    2.  S'exécuter jusqu'à la fin mais contenir des avertissements dans les journaux.

    Dans ces deux scénarios, les simulations seraient répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente (spécifié par la valeur `array`) soit atteint, ce qui entraînerait un gaspillage de temps de calcul. Pour ces types de tâches, il est préférable d'utiliser les [scripts à usage général](#utilisation-generale).

=== "Plusieurs nœuds (par nœud + remise en attente)"

```bash title="script-flu-bynode+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
if [ $? -eq 0 ]; then
    echo "Job completed successfully! Exiting now."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Resubmitting job now …"
    else
       echo "All job attempts failed exiting now."
    fi
fi
```

=== "Plusieurs nœuds (par cœur + remise en attente)"

```bash title="script-flu-bycore+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max) 
#SBATCH --ntasks=16           # Specify total number of cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of requeue attempts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYJOURNALFILE=sample.jou      # Specify your journal file name
MYVERSION=3d                  # Specify 2d, 2ddp, 3d or 3ddp

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
 fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -i $MYJOURNALFILE
else
 if [[ "${CC_CLUSTER}" == nibi ]]; then
   fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 else
   fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOURNALFILE
 fi
fi
if [ $? -eq 0 ]; then
    echo "Job completed successfully! Exiting now."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Job attempt $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT failed due to license or simulation issue!"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Resubmitting job now …"
    else
       echo "All job attempts failed exiting now."
    fi
fi
```

#### Redémarrage

Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, `sample.cas`, `sample.dat` et `sample.jou` doivent être présents. Modifiez le fichier `sample.jou` pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier de journalisation avec `cp sample.jou sample-restart.jou` et modifiez le fichier `sample-restart.jou` pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `;/solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez `sample-restart.jou` en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages qui consomme beaucoup de ressources. Si le premier pas de `sample.jou` est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt + 2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1 + 2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

=== "Plusieurs nœuds (par nœud + redémarrage)"

```bash title="script-flu-bynode+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=07-00:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Specify number of compute nodes (narval 1 node max)
#SBATCH --ntasks-per-node=32  # Specify upto maximum number of cores per compute node
#SBATCH --mem=0               # Specify memory per compute node (0 allocates all memory)
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of solution restarts (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
MYJOUFILE=sample.jou                # Specify your journal filename
MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILE
  else
    fluent -g 2ddp -t $NCORES -mpi=intel -pshmem -i $MYJOUFILERES
  fi
else 
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
   if [[ "${CC_CLUSTER}" == nibi ]]; then
     fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
   else
     fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILE
   fi
  else
   if [[ "${CC_CLUSTER}" == nibi ]]; then
     fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
   else
     fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -ssh -i $MYJOUFILERES
   fi
  fi
fi
if [ $? -eq 0 ]; then
    echo
    echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
    echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
    echo
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
      echo "Restarting job with the most recent output dat file …"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Job completed successfully! Exiting now."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation failed. Exiting …"
fi
```

=== "Plusieurs nœuds (par cœur + redémarrage)"

```bash title="script-flu-bycore+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
##SBATCH --nodes=1            # Uncomment to specify (narval 1 node max)
#SBATCH --ntasks=16           # Specify total number of cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change
#SBATCH --array=1-5%1         # Specify number of restart aka time steps (2 or more, 5 is shown)

module load StdEnv/2023       # Do not change
module load ansys/2023R2      # Specify version (or newer)

MYVERSION=3d                        # Specify 2d, 2ddp, 3d or 3ddp
MYJOUFILE=sample.jou                # Specify your journal filename
MYJOUFILERES=sample-restart.jou     # Specify journal restart filename
MYCASFILERES=sample-restart.cas.h5  # Specify cas restart filename
MYDATFILERES=sample-restart.dat.h5  # Specify dat restart filename

# ------- do not change any lines below --------

if [[ "$CC_CLUSTER" == narval ]]; then
 module load intel/2023 intelmpi
 export INTELMPI_ROOT=$I_MPI_ROOT
 unset I_MPI_ROOT
fi

if [[ ("${EBVERSIONANSYS//R*}" -ge 2025 && "${CC_CLUSTER}" == nibi) || "${CC_CLUSTER}" == narval ]]; then
 export I_MPI_HYDRA_BOOTSTRAP=ssh
 unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
fi

slurm_hl2hl.py --format ANSYS-FLUENT > /tmp/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ "$SLURM_NNODES" == 1 ]; then
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYFILEJOU
  else
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYFILEJOURES
  fi
else 
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    if [[ "${CC_CLUSTER}" == nibi ]]; then
      fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
    else
      fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
    fi
  else
    if [[ "${CC_CLUSTER}" == nibi ]]; then
      fluent -g $MYVERSION -t $NCORES -mpi=intel -peth -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
    else
      fluent -g $MYVERSION -t $NCORES -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
    fi
  fi
fi
if [ $? -eq 0 ]; then
    echo
    echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
    echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
    echo
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
      echo "Restarting job with the most recent output dat file"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Job completed successfully! Exiting now."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation failed. Exiting now."
fi
```

### Fichiers de journalisation

Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface TUI (Text User Interface) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le [guide d'utilisation de Fluent](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html) pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `/file/cff-files yes`.

=== "Fichier de journalisation (stable, cas)"

```
; SAMPLE FLUENT JOURNAL FILE - STEADY SIMULATION
; ----------------------------------------------
; lines beginning with a semicolon are comments

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read input case and data files
/file/read-case-data FFF-in

; Run the solver for this many iterations
/solve/iterate 1000

; Overwrite output files by default
/file/confirm-overwrite n

; Write final output data file
/file/write-case-data FFF-out

; Write simulation report to file (optional)
/report/summary y "My_Simulation_Report.txt"

; Cleanly shutdown fluent
/exit
```

=== "Fichier de journalisation (stable, cas + données)"

```
; SAMPLE FLUENT JOURNAL FILE - STEADY SIMULATION
; ----------------------------------------------
; lines beginning with a semicolon are comments

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read input files
/file/read-case-data FFF-in

; Write a data file every 100 iterations
/file/auto-save/data-frequency 100

; Retain data files from 5 most recent iterations
/file/auto-save/retain-most-recent-files y

; Write data files to output sub-directory (appends iteration)
/file/auto-save/root-name output/FFF-out

; Run the solver for this many iterations
/solve/iterate 1000

; Write final output case and data files
/file/write-case-data FFF-out

; Write simulation report to file (optional)
/report/summary y "My_Simulation_Report.txt"

; Cleanly shutdown fluent
/exit
```

=== "Fichier de journalisation (temporaire)"

```
; SAMPLE FLUENT JOURNAL FILE - TRANSIENT SIMULATION
; -------------------------------------------------
; lines beginning with a semicolon are comments

; Overwrite files by default
/file/confirm-overwrite no

; Preferentially read/write files in legacy format
/file/cff-files no

; Read the input case file
/file/read-case FFF-transient-inp

; For continuation (restart) read in both case and data input files
;/file/read-case-data FFF-transient-inp

; Write a data (and maybe case) file every 100 time steps
/file/auto-save/data-frequency 100
/file/auto-save/case-frequency if-case-is-modified

; Retain only the most recent 5 data (and maybe case) files
/file/auto-save/retain-most-recent-files y

; Write to output sub-directory (appends flowtime and timestep)
/file/auto-save/root-name output/FFF-transient-out-%10.6f

; ##### Settings for Transient simulation :  #####

; Set the physical time step size
/solve/set/time-step 0.0001

; Set the number of iterations for which convergence monitors are reported
/solve/set/reporting-interval 1

; ##### End of settings for Transient simulation #####

; Initialize using the hybrid initialization method
/solve/initialize/hyb-initialization

; Set max number of iters per time step and number of time steps
;/solve/set/max-iterations-per-time-step 75
;/solve/dual-time-iterate 1000 ,
/solve/dual-time-iterate 1000 75

; Write final case and data output files
/file/write-case-data FFF-transient-out

; Write simulation report to file (optional)
/report/summary y Report_Transient_Simulation.txt

; Cleanly shutdown fluent
/exit
```

### Fonctions UDF

La première étape est de transférer vers la grappe votre UDF (''User-Defined Function''), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui, elle, exécute Linux. L'UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *UDFs interprétées* et *Gestionnaire de bibliothèques UDF* ne sont pas configurées pour utiliser un UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interprété

Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Ceci garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

`define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no`

#### Compilé

Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Ceci créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `libudf.so` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quelle autre de nos grappes, à condition que votre compte charge la même version du module d'environnement StdEnv. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (''load'') `libudf` ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes `libudf` (''compile'' et ''load'') ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de build de type ''racetime'' si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *UDFs compilées*, et cliquez sur *Compiler*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

`define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""`

et/ou

`define/user-defined/compiled-functions load libudf`

#### Parallèle

Avant qu'une UDF puisse être utilisée avec une tâche parallèle Fluent (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque Fluent est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, Fluent fonctionnera lentement, au mieux, ou plantera immédiatement, au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque Fluent est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans [Fluent Customization Manual, Part I: Chapter 7: Parallel Considerations](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf_ChapParallelUDFUsage.html?q=parallel%20considerations).

#### DPM
Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour ''Discrete Phase Models'') comme décrit dans 
*   [2024R2 Fluent Users Guide](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/corp/v242/en/flu_ug/flu_ug.html): *Partie III: Mode de Solution | Chapitre 24: Modélisation de la Phase Discrète | 24.2 Étapes pour l'Utilisation des Modèles de Phase Discrète| 24.2.6 Fonctions Définies par l'Utilisateur*, et
*   [2024R2 Fluent Customization Manual](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf.html): *Partie I: Création et Utilisation de Fonctions Définies par l'Utilisateur | Chapitre 2: Macros DEFINE | 2.5 Macros DEFINE du Modèle de Phase Discrète (DPM)*.
<br>
Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Propriétés des points* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Ceci se fait dans l'interface graphique en cliquant sur le panneau *Physique --> Phase Discrète*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées avec le bouton *Créer*. La boîte de dialogue *Définir les propriétés d'injection* contient le menu déroulant *Type d'injection* avec les quatre premiers types disponibles (*simple, groupe, surface, atomiseur à jet plat*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Propriétés des points* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Propriétés des points* est de lire un fichier texte d'injection. Pour ce faire, sélectionnez *Fichier* dans le menu déroulant *Type d'injection*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *Fichier* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Définir les propriétés d'injection*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension `.dpm`) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Sélectionner un fichier*, sélectionnez *Tous les fichiers (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur *OK*. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. En revenant à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Définir les propriétés d'injection* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Modèle de phase discrète* et sélectionnez *Interaction avec la phase continue* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple
 ` /define/models/dpm/interaction/coupled-calculations yes`
 ` /define/models/dpm/injections/delete-injection injection-0:1`
 ` /define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no`
 ` /define/models/dpm/injections/list-particles injection-0:1`
 ` /define/models/dpm/injections/list-injection-properties injection-0:1`
where a basic manually created injection steady file format might look like
 ```
$ cat  zinjection01.inj
(z=4 12)
( x          y        z    u         v    w    diameter  t         mass-flow  mass  frequency  time name )
(( 2.90e-02  5.00e-03 0.0 -1.00e-03  0.0  0.0  1.00e-04  2.93e+02  1.00e-06   0.0   0.0        0.0 ) injection-0:1 )
```
notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans [2024R2 Fluent Customization Manual](https://ansyshelp.ansys.com/public/account/secured?returnurl=//////Views/Secured/corp/v242/en/flu_udf/flu_udf.html) *Partie III: Mode de Solution | Chapitre 24: Modélisation de la Phase Discrète | 24.3. Définition des Conditions Initiales pour la Phase Discrète | 24.3.13 Propriétés des Points pour les Injections de Fichiers | 24.3.13.1 Format de Fichier Stationnaire*.

## CFX

### Scripts pour l'ordonnanceur Slurm

Le résumé des options de ligne de commande peut être affiché avec `cfx5solve -help`. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, `cfx5solve` s'exécute en simple précision (`-single`). Pour exécuter `cfx5solve` en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, `cfx5solve` prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez [Ansys CFX-Solver Manager User's Guide](https://ansyshelp.ansys.com/public/Views/Secured/corp/v251/en/pdf/Ansys_CFX-Solver_Manager_Users_Guide.pdf) pour plus de détails.

=== "Nœud simple"

```bash title="script-cfx-local.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=1             # Do not change
#SBATCH --ntasks-per-node=4   # Specify number of cores
#SBATCH --mem=16G             # Specify total memory
#SBATCH --cpus-per-task=1     # Do not change

#module load StdEnv/2020      # Uncomment to use (deprecated)     
#module load 2021R2           # Specify 2021R2 only

module load StdEnv/2023
module load ansys/2023R2      # Or newer module versions

# append additional cfx5solve command line options as required
if [[ "$CC_CLUSTER" = narval || "$CC_CLUSTER" == fir ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
else
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
fi
```

=== "Plusieurs nœuds"

```bash title="script-cfx-multiple.sh"
#!/bin/bash

#SBATCH --account=def-group   # Specify account name
#SBATCH --time=00-03:00       # Specify time limit dd-hh:mm
#SBATCH --nodes=2             # Specify multiple compute nodes (2 or more)
#SBATCH --ntasks-per-node=192 # Use all cores per compute node (do not change)
#SBATCH --mem=0               # Use all memory on each compute node (do not change)
#SBATCH --cpus-per-task=1     # Do not change

#module load StdEnv/2020      # Uncomment to use (deprecated)     
#module load 2021R2           # Specify 2021R2 only

module load StdEnv/2023
module load ansys/2023R2      # Or newer module versions

NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

# append additional cfx5solve command line options as required
if [[ "$CC_CLUSTER" = narval || "$CC_CLUSTER" == fir ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
else
  export I_MPI_HYDRA_BOOTSTRAP=ssh
  unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
fi
```

## Workbench

Avant de soumettre une tâche Workbench à la file d'attente avec un script Slurm, vous devez l'initialiser une fois, comme décrit dans les étapes suivantes.
1.  Sur la grappe où vous soumettrez les tâches Workbench, [ouvrez un bureau OnDemand](../interactive/open_ondemand.md).
2.  Une fois le bureau affiché, ouvrez une fenêtre de terminal et accédez au répertoire contenant votre fichier `YOURPROJECT.wbpj`.
3.  Supprimez l'ancien répertoire cache de `/project` en exécutant `rm -rf _ProjectScratch`, car il peut être très volumineux suite à des exécutions précédentes.
4.  Ouvrez une fenêtre de terminal et chargez la version du module que vous utiliserez dans votre script Slurm, par exemple `module load ansys/2025R2.04`.
5.  Ouvrez l'interface graphique de Workbench avec votre fichier de `/project`. Pour ce faire, exécutez directement la commande `runwb2 -f YOURPROJECT.wbpj` via la ligne de commande. Si une fenêtre contextuelle apparaît vous demandant ''Voulez-vous récupérer le projet avant de l'ouvrir? (Toutes les modifications apportées depuis la dernière sauvegarde seront perdues.)'', répondez **Non**.
6.  Dans le menu contextuel qui devrait apparaître au centre de la fenêtre *Schéma de projet*, cliquez avec le bouton droit sur *Modèle* et sélectionnez *Réinitialiser*. Lorsqu'Ansys Workbench affiche l'avertissement ''Cette opération supprimera les données locales et générées des opérations'', cliquez sur *OK* pour accepter et continuer.
7.  Dans le menu déroulant de la barre de menu supérieure, sélectionnez **Fichier -> Sauvegarder** puis **Fichier -> Quitter** pour fermer Workbench.
8.  Dans la fenêtre contextuelle Ansys Workbench qui affiche ''Le projet actuel a été modifié. Voulez-vous le sauvegarder?'' cliquez sur **Non**.
9.  Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Puisqu'il est désormais possible de réserver un nœud de calcul doté de jusqu'à 96 cœurs, 768Go de mémoire et 8 heures d'autonomie pour une session de bureau OnDemand, exécutez vos simulations Workbench directement de l'interface graphique native de Workbench lorsque cela est possible; il s'agit d'une option plus intuitive que de soumettre la tâche à la file d'attente via un script Slurm

### Scripts pour l'ordonnanceur Slurm

Pour soumettre un fichier de projet à la file d'attente, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

=== "Nœud simple (StdEnv/2023)"

```bash title="script-wbpj-2023.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Time (DD-HH:MM)
#SBATCH --mem=16G                      # Specify total memory
#SBATCH --ntasks=4                     # Specify number of cores
#SBATCH --nodes=1                      # Do not change (multi-node not supported)
##SBATCH --exclusive                   # Uncomment ONLY for scaling testing
##SBATCH --constraint=broadwell        # Uncomment to specify an available node type

module load StdEnv/2023 ansys/2023R2   # OR newer Ansys module versions

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
else
  MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
fi

rm -fv *_files/.lock
MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"


export KMP_AFFINITY=disabled
export I_MPI_HYDRA_BOOTSTRAP=ssh


runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
```

=== "Nœud simple (StdEnv/2020)"

```bash title="script-wbpj-2020.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Time (DD-HH:MM)
#SBATCH --mem=16G                      # Specify total memory
#SBATCH --ntasks=4                     # Specify number of cores
#SBATCH --nodes=1                      # Do not change (multi-node not supported)
##SBATCH --exclusive                   # Uncomment ONLY for scaling testing
##SBATCH --constraint=broadwell        # Uncomment to specify an available node type

module load StdEnv/2020 ansys/2022R2   # OR older Ansys module versions

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Set to 0 for SMP (shared memory parallel)
else
  MEMPAR=1                             # Set to 1 for DMP (distributed memory parallel)
fi

rm -fv *_files/.lock
MWFILE=~/.mw/Application\ Data/Ansys/`basename $(find $EBROOTANSYS/v* -maxdepth 0 -type d)`/SolveHandlers.xml
sed -re "s/(.AnsysSolution>+)[a-zA-Z0-9]*(<\/Distribute.)/\1$MEMPAR\2/" -i "$MWFILE"
sed -re "s/(.Processors>+)[a-zA-Z0-9]*(<\/MaxNumber.)/\1$SLURM_NTASKS\2/" -i "$MWFILE"
sed -i "s!UserConfigured=\"0\"!UserConfigured=\"1\"!g" "$MWFILE"

export KMP_AFFINITY=disabled
export I_MPI_HYDRA_BOOTSTRAP=ssh

runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
```

Pour ne pas écrire la solution lorsqu'une tâche en cours se termine avec succès, remplacez `Save(Overwrite=True)` par `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera l'évaluation de la mise à l'échelle de la simulation lorsque la valeur de `#SBATCH --ntasks` est augmentée, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical

Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Outils -> Écrire les fichiers d'entrée* et en spécifiant *Nom de fichier :* pour `YOURAPDLFILE.inp` et *Type d'enregistrement :* *Fichiers d'entrée APDL (*.inp)*. Les tâches APDL peuvent ensuite être soumises à la file d'attente avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm

Les lignes qui commencent par `##SBATCH` sont des commentaires.

=== "Mémoire parallèle partagée (CPU)"

```bash title="script-smp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify your account
#SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
#SBATCH --mem=32G               # Specify memory for all cores
#SBATCH --nodes=1               # Do not change
#SBATCH --tasks=8               # Specify number of cores
#SBATCH --cpus-per-task=1       # Do not change

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
```

=== "Mémoire parallèle distribuée (CPU)"

```bash title="script-dmp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Specify your account
#SBATCH --time=00-03:00         # Specify time (DD-HH:MM)
#SBATCH --mem-per-cpu=4G        # Specify memory per core
##SBATCH --nodes=2              # Specify number of nodes (optional)
#SBATCH --ntasks=8              # Specify number of cores
##SBATCH --ntasks-per-node=4    # Specify cores per node (optional)
#SBATCH --cpus-per-task=1       # Do not change

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
if [[ "$CC_CLUSTER" = cedar ]]; then
 ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
 export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
fi

if [[ "$CC_CLUSTER" = beluga  ]]; then
  export KMP_AFFINITY=none
  mapdl -dis -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
else
  mapdl -dis -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
fi
```

=== "Mémoire parallèle partagée (GPU)"

```bash title="script-smp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify your account
#SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
#SBATCH --mem=32G                # Specify memory for all cores
#SBATCH --ntasks=8               # Specify number of cores
#SBATCH --nodes=1                # Do not change
#SBATCH --cpus-per-task=1        # Do not change
#SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
##SBATCH --partition=debug       # Temporarily required on mini-graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

export ANSGPU_PRINTDEVICES=1
mapdl -smp -acc nvidia -na $SLURM_GPUS_ON_NODE -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID  -i YOURAPDLFILE.inp
```

=== "Mémoire parallèle distribuée (GPU)"

```bash title="script-dmp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Specify your account
#SBATCH --time=00-03:00          # Specify time (DD-HH:MM)
#SBATCH --mem-per-cpu=4G         # Specify memory per core
#SBATCH --nodes=1                # Specify number of nodes
#SBATCH --ntasks-per-node=8      # Specify cores per node
#SBATCH --cpus-per-task=1        # Do not change
#SBATCH --gpus-per-node=1        # Specify [gputype:]quantity
##SBATCH --gpus-per-node=h100:1  # Temporarily required on mini-graham
##SBATCH --partition=debug       # Temporarily required on mini-graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
if [[ "$CC_CLUSTER" = cedar ]]; then
 ln -s $EBROOTGCC/../lib/gcc/libstdc++.so.6.0.29 $PWD/outdir-$SLURM_JOBID/libstdc++.so.6.0.29
 export LD_LIBRARY_PATH=$PWD/outdir-$SLURM_JOBID
fi

export ANSGPU_PRINTDEVICES=1
if [[ "$CC_CLUSTER" = beluga  ]]; then 
  export KMP_AFFINITY=none
  mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi intelmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
else
  mapdl -dis -acc nvidia -na $SLURM_GPUS_ON_NODE -mpi openmpi -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
fi
```

Par défaut, Ansys alloue aux tâches APDL 1024Mo de mémoire totale et 1024Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande mapdl des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de mise à l'échelle avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (SMP pour ''Shared Memory Parallel'') offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (DMP pour ''Distributed Memory Parallel'') et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

`[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version`
`! ANSYS input file written by Workbench version 2019 R3`

## Rocky

Nous présentons ici des exemples de scripts Slurm pour résoudre des simulations Rocky autonomes et non couplées dans la file d'attente d'une grappe. Les deux scripts sont configurés avec `RESUME=0`, ce qui par défaut permet de résoudre les simulations depuis le début. Pour redémarrer une simulation partiellement terminée, spécifiez `RESUME=1` et soumettez à nouveau le script à la file d'attente. Pour obtenir la liste complète des options de ligne de commande, exécutez `Rocky -h` après avoir chargé le module Ansys. Un fichier de verrouillage étant généré à chaque lancement de simulation, une seule tâche doit être soumise à la fois dans le même répertoire. Concernant le choix du script, bien que toutes les simulations doivent être testées indépendamment, pour un cas de test simple, le script utilisant uniquement le GPU s'est avéré 3,5 fois plus performant que le script utilisant uniquement le CPU. Des augmentations supplémentaires de ressources au-delà de 6 cœurs (pour le script utilisant uniquement le CPU) ou de 2 cœurs + 1Go (1/7 d'un GPU H100 pour le script utilisant le GPU) n'ont apporté aucun gain de vitesse supplémentaire, d'après les tests de passage à l'échelle pour l'un ou l'autre script. Au vu de ces résultats, il est probable que le script basé sur le GPU offre des temps de calcul nettement plus rapides que l'utilisation exclusive du CPU pour les autres simulations Rocky autonomes. Comme indiqué sur la page wiki de chaque grappe, ou résumé dans la section [Ratios dans les bundles](allocations_and_compute_scheduling.md#ratios-dans-les-bundles), toutes les grappes, à l'exception de Narval, sont équipées de GPU H100. Par conséquent, lors de l'utilisation du script GPU sur Narval, l'option Slurm `--gpus` doit être modifiée pour demander un GPU a100. Veuillez noter qu'en mai 2026, seuls les modules `ansys/2025R2|2.04` de Rocky ont été testés, et non les modules `ansys/2025R1|1.02`.

### Scripts pour l'ordonnanceur Slurm

=== "CPU seulement"

```bash title="script-rocky-cpu.sh"
#!/bin/bash

#SBATCH --account=account      # Specify account (def or rrg)
#SBATCH --time=00-02:00        # Specify time (DD-HH:MM)
#SBATCH --mem=24G              # Specify total memory for cores
#SBATCH --cpus-per-task=6      # Specify number of cores to use
#SBATCH --nodes=1              # Request one node (do not change)

module load StdEnv/2023 ansys/2025R2.04   # Specify 2025R1 or newer versions

INPUTFILE="mySim.rocky"                   # Specify input filename
rm -f $INPUTFILE.lock                     # Removes old lock files

RESUME=0                                  # Specify 0 or 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Removes previous results
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0 $INPUTFILE
fi
```

=== "avec GPU"

```bash title="script-rocky-gpu.sh"
#!/bin/bash

#SBATCH --account=account      # Specify account (def or rrg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=24G              # Specify total memory for cores
#SBATCH --cpus-per-task=2      # Specify number of cores to use
#SBATCH --gpus=h100_1g.10gb:1  # Specify a100_1g.5gb:1 on narval
#SBATCH --nodes=1              # Request one node (do not change)

module load StdEnv/2023 ansys/2025R2.04   # Specify 2025R1 or newer versions

INPUTFILE="mySim.rocky"                   # Specify input filename
rm -f $INPUTFILE.lock                     # Removes old lock files

RESUME=0                                  # Specify 0 or 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Removes previous results
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 $INPUTFILE
fi
```

## Electronics

Voir les exemples de scripts pour l'ordonnanceur dans [notre page wiki AnsysEDT](../software/ansysedt.md).