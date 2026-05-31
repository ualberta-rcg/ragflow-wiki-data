---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "163ca71aca5e63f0a8dbbeb98e09389e"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:39:03.442114+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: true
  qa_generated: false
---

!!! note "Mise à jour (juin 2026)"
Cette page est présentement en cours de révision.

Ansys est une suite logicielle pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

## Licence
La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez l'aspect légal de son utilisation. En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence
Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire `/home`. Pour indiquer votre propre serveur de licence, créez un fichier nommé `` `$HOME/.licenses/ansys.lic` `` qui contient les deux lignes ci-dessous, où vous remplacez FLEXPORT et LICSERVER par les valeurs réelles de votre serveur.

```
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@LICSERVER")
```

Les valeurs correspondant aux serveurs de licence CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un différent serveur, voir [Serveurs de licence locaux](#serveurs-de-licence-locaux) ci-dessous.

### Serveurs de licences préconfigurés

| Licence | Système/Grappe | LICSERVER | FLEXPORT | Commentaires |
| :------ | :------------- | :-------- | :------- | :----------- |
| CMC | Fir | `` `172.26.0.101` `` | `` `6624` `` | **[Ne plus utiliser](https://www.cmc.ca/ansys-academic-research-software/)** (fermeture 2026-04-23) |
| CMC | Narval/Rorqual | `` `10.100.64.10` `` | `` `6624` `` | **[Ne plus utiliser](https://www.cmc.ca/ansys-academic-research-software/)** (fermeture 2026-04-23) |
| CMC | Nibi | `` `10.25.1.56` `` | `` `6624` `` | **[Ne plus utiliser](https://www.cmc.ca/ansys-academic-research-software/)** (fermeture 2026-04-23) |
| CMC | Trillium | `` `scinet-cmc` `` | `` `6624` `` | **[Ne plus utiliser](https://www.cmc.ca/ansys-academic-research-software/)** (fermeture 2026-04-23) |
| SHARCNET | Nibi/Fir/Narval/Rorqual/Trillium | `` `license1.computecanada.ca` `` | `` `1055` `` | |

### Serveurs de licence locaux

Avant que le serveur de licence de votre établissement puisse être utilisé avec nos grappes, les coupe-feu des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans le paragraphe [Prêt à utiliser](#prêt-à-utiliser) ci-dessous. Autrement, référez-vous au paragraphe [Configuration requise](#configuration-requise).

#### Prêt à utiliser
Pour utiliser un serveur de licences Ansys local de votre établissement dont les connexions réseau/pare-feu sont déjà configurées pour nos grappes, contactez votre administrateur de serveur de licence ANSYS et obtenez les deux renseignements suivants :
1) le numéro de port flexible Ansys configuré (FLEXPORT), généralement 1055,
2) le nom d'hôte complet (LICSERVER) du serveur de licence.
Configurez ensuite votre fichier `` `~/.licenses/ansys.lic` `` en y insérant les valeurs de FLEXPORT et LICSERVER dans le modèle **Fichier : ansys.lic** ci-dessus.

#### Configuration requise
Pour utiliser un serveur de licence Ansys local n'ayant jamais été configuré pour nos grappes, vous devrez EN PLUS obtenir les renseignements suivants auprès de votre administrateur de serveur de licence Ansys :
3) le port fournisseur (VENDPORT) configuré statiquement sur le serveur de licence,
4) la confirmation que `` `<servername>` `` correspond à la même adresse IP que LICSERVER sur la grappe.
`` `<servername>` `` se trouve sur la première ligne du fichier de licence, au format `` `SERVER <servername> <host id> <lmgrd port>` ``. Envoyez les éléments 1 à 3 par courriel au [soutien technique](../support/technical_support.md) en précisant la grappe sur laquelle vous souhaitez exécuter des tâches Ansys. Un de nos administrateurs de systèmes ouvrira alors le pare-feu sortant de la grappe afin que les requêtes d'extraction de licence puissent atteindre votre serveur de licence à partir des nœuds de calcul de la grappe. Une plage d'adresses IP vous sera ensuite communiquée. Transmettez-la à votre administrateur réseau local. Demandez-lui d'ouvrir le pare-feu de votre serveur de licence local afin que les connexions de licence Ansys (requêtes d'extraction) puissent atteindre les ports FLEXPORT et VENDPORT de votre serveur sur cette plage d'adresses IP.

## Obtenir une licence
Pour vérifier si `` `ansys.lic` `` est bien configuré et fonctionne correctement avec votre serveur de licence, exécutez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches.

```bash
cd /tmp
salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
module load StdEnv/2023; module load ansys/2025R2.04
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```
`Success` indique que les extractions de licence devraient fonctionner lorsque les tâches sont soumises à la file d'attente.
`Fail` indique un problème avec la configuration de la licence et les tâches échoueront probablement.

En cas de problème d'obtention de licence auprès du serveur Ansys, le message suivant apparaîtra dans les fichiers de sortie Slurm lorsque des tâches Fluent sont lancées par des scripts Slurm en file d'attente *OU* lorsque Fluent est lancé de manière interactive, en procédant comme suit :

```
fluent -g 2d -n 2
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

## Compatibilité des versions
Les simulations Ansys sont typiquement compatibles avec des versions postérieures, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une moins récente version de Ansys devrait pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec ansys/2022R2 devrait fonctionner avec ansys/2023R2, mais **pas dans l'autre sens**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations Fluent, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```
$ grep -ia fluent combustor.cas
  (0 "fluent15.0.7  build-id: 596")
```

```
$ grep -ia fluent cavity.cas.h5
  ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge
Ansys fournit des informations détaillées sur la compatibilité des plateformes, notamment la compatibilité logicielle et matérielle, pour [la version actuelle](https://www.ansys.com/it-solutions/platform-support) et [les versions précédentes](https://www.ansys.com/it-solutions/platform-support/previous-releases). Le document PDF *Platform Support by Application / Product* est particulièrement utile car il indique quels logiciels sont compatibles sous Windows mais pas sous Linux, et donc pas sur l'Alliance (par exemple Spaceclaim).

## Nouveautés
Vous trouverez des informations sur la dernière version d'Ansys [ici](https://www.ansys.com/products/release-highlights), `` `Ansys 2026 R1` `` en date de mai 2026. Les articles relatifs aux versions précédentes sont accessibles sur la page Ansys [ici](https://www.ansys.com/blog) en faisant défiler la page jusqu'à la barre de recherche FILTERS. Saisir par exemple `What’s New Fluent 2024 gpu` devrait afficher un document contenant les dernières informations sur la prise en charge des GPU par cette version. La barre de recherche [ici](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations spécifiques à une version.

## Correctifs
À partir d'Ansys 2024, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *service pack* est installé pour la version initiale. Par exemple, la version initiale pour 2024 sans aucun *service pack* peut être chargée en exécutant `` `module load ansys/2024R1` `` tandis qu'un module avec le *service pack* 3 peut être chargé avec `` `module load ansys/2024R1.03` ``. Si un *service pack* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *service pack* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *service pack* installé en exécutant simplement `` `module load ansys` ``. Bien qu'il ne soit pas prévu que les *service packs* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *service pack* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *service pack* rend cela possible. À partir d'Ansys 2024R1, une description détaillée de ce que fait chaque *service pack* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

## Soumettre des tâches en lot sur nos grappes
Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

## Fluent
La procédure suivante est habituellement utilisée pour exécuter Fluent sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec Fluent du Ansys Workbench jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *Fichier > Exporter > Cas…* ou localisez le répertoire dans lequel Fluent enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `` `FFF-1.cas.gz` ``.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *Fichier > Exporter > Données…* ou trouvez-le dans le même répertoire `/project` (`` `FFF-1.dat.gz` ``).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage) de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `` `FFF-1.*` `` ou renommez-les au téléversement.
5.  Créez un fichier de journalisation dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancez le solveur et enregistrez les résultats. Les exemples ci-dessous montrent comment configurer le fichier de journalisation et lancer le solveur. N'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour le script sous l'onglet *Plusieurs nœuds (par cœur + remise en attente)* plus loin. Cependant, ceci remet aussi en attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en attente est ou non due à un problème de licence. Si vous découvrez que la remise en attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `` `scancel jobid` `` et corrigez le problème.
7.  Lorsque la [tâche est terminée](../running-jobs/running_jobs.md), vous pouvez télécharger le fichier de données et le retourner dans Fluent avec *Fichier > Importer > Données…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale
La plupart des tâches Fluent devraient utiliser le script *par nœud* ci-dessous pour minimiser le temps d'attente et maximiser la performance en utilisant le moins de nœuds possible. Les tâches demandant beaucoup de cœurs CPU pourraient attendre moins longtemps dans la queue avec le script *par cœur*, mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent fournir une alternative plus robuste si Fluent plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts Intel standards avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de Fluent, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts Intel. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

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
Les scripts suivants ne doivent être utilisés qu'avec des tâches Fluent qui sont connues pour se terminer normalement sans générer d'erreurs en sortie, mais qui nécessitent généralement plusieurs tentatives de remise en file d'attente pour obtenir les licences. Ils ne sont pas recommandés pour les tâches Fluent qui peuvent 1) s'exécuter pendant une longue période avant de planter 2) s'exécuter jusqu'à la fin mais contenir des avertissements de journalisation; dans les deux cas, les simulations seront répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente spécifié par la valeur `array` soit atteint. Pour ces types de tâches, les scripts à usage général (ci-dessus) doivent être utilisés.

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
Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de valeur de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de *sample.cas*, *sample.dat* et *sample.jou* doit être présent. Modifiez le fichier *sample.jou* pour qu'il contienne `` `/solve/dual-time-iterate 1` `` et `` `/file/auto-save/data-frequency 1` ``. Créez ensuite un fichier de journalisation avec `` `cp sample.jou sample-restart.jou` `` et modifiez le fichier *sample-restart.jou* pour qu'il contienne `` `/file/read-cas-data sample-restart` `` plutôt que `` `/file/read-cas-data sample` `` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `` `;/solve/initialize/initialize-flow` ``. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez *sample-restart.jou* en spécifiant `` `/solve/dual-time-iterate 2` ``. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de *sample.jou* est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt+2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1+2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `` `#SBATCH --time=07-00:00` `` jours.

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
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYJOUFILE
  else
    fluent -g $MYVERSION -t $NCORES -mpi=intel -pshmem -I $MYJOUFILERES
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
Les fichiers de journalisation peuvent contenir toutes les commandes de l'interface TUI (*Text User Interface*) de Fluent; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier de journalisation. Consultez le guide d'utilisation de Fluent pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `` `/file/cff-file no` `` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à 2019R3. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de 2020R1, la configuration est `` `/file/cff-files yes` ``.

=== "Fichier de journalisation (stable, cas)"
```
; FICHIER DE JOURNALISATION FLUENT EXEMPLE - SIMULATION STABLE
; ----------------------------------------------
; les lignes commençant par un point-virgule sont des commentaires

; Ne pas demander confirmation pour écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire les fichiers de cas et de données en entrée
/file/read-case-data FFF-in

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; Ne pas demander confirmation pour écraser les fichiers de sortie par défaut
/file/confirm-overwrite n

; Écrire le fichier de données de sortie final
/file/write-case-data FFF-out

; Écrire le rapport de simulation dans un fichier (optionnel)
/report/summary y "My_Simulation_Report.txt"

; Arrêter Fluent proprement
/exit
```

=== "Fichier de journalisation (stable, cas + données)"
```
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION STABLE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

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

; écrire le dernier fichier de cas et de données en sortie
/file/write-case-data FFF-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y "My_Simulation_Report.txt"

; fermez correctement Fluent
exit
```

=== "Fichier de journalisation (temporaire)"
```
; EXEMPLE DE FICHIER DE JOURNALISATION - SIMULATION TEMPORAIRE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

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

; ##### Fin des paramètres #####

; initialiser avec la méthode hybride
/solve/initialize/hyb-initialization

; indiquer le nombre maximal d'itérations par pas et le nombre de pas
;/solve/set/max-iterations-per-time-step 75
;/solve/dual-time-iterate 1000 ,
/solve/dual-time-iterate 1000 75

; enregistrer les derniers fichiers en sortie pour les cas et les données
/file/write-case-data FFF-transient-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y Report_Transient_Simulation.txt

; Cleanly shutdown fluent
/exit
```

### Fonctions UDF
La première étape est de transférer vers la grappe votre UDF (*User-Defined Function*), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine Windows, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon Fluent ne pourra pas lire correctement le fichier sur la grappe qui elle exécute Linux. L'UDF doit être placée dans le répertoire où résident vos fichiers de journalisation, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier de journalisation avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *UDFs interprétées* et *Gestionnaire de bibliothèques UDF* ne sont pas configurées pour utiliser un UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier de journalisation auront le contrôle.

#### Interprété
Pour indiquer à Fluent d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier de journalisation, ouvrez votre fichier cas dans l'interface graphique Fluent, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de Fluent. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilé
Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `` `libudf.so` `` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter Fluent au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quel autre de nos grappes, à condition que votre compte charge la même version du module d'environnement StdEnv. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (load) libudf ci-dessous dans votre fichier de journalisation quand une tâche est soumise. Les deux lignes libudf (compile et load) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de build de type « racetime » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier de journalisation pour construire votre UDF, l'interface graphique de Fluent peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *UDFs compilées*, et cliquez sur *Construire*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

```
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```

et/ou

```
define/user-defined/compiled-functions load libudf
```

#### Parallèle
Avant qu'une UDF puisse être utilisée avec une tâche parallèle Fluent (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque Fluent est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, Fluent fonctionnera lentement au mieux ou plantera immédiatement au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque Fluent est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans *Fluent Customization Manual, Part I: Chapter 7: Parallel Considerations* qui se trouve dans la [Documentation en ligne](#aide-et-ressources).

#### DPM
Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour *Discrete Phase Models*) comme décrit dans *2024R2 Fluent Users Guide, Part III: Solution Mode, Chapter 24: Modeling Discrete Phase, 24.2 Steps for Using the Discrete Phase Models,* et dans *2024R2 Fluent Customization Manual, Part I: Creating and Using User Defined Functions, Chapter 2: DEFINE Macros, 2.5 Discrete Phase Model (DPM) DEFINE Macros*. Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Propriétés de point* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physique --> Phase discrète*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Créer*. La boîte de dialogue *Définir les propriétés d'injection* contient le menu déroulant *Type d'injection* avec les quatre premiers types disponibles (*simple, groupe, surface, pulvérisateur à jet plat*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Propriétés de point* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Propriétés de point* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *Fichier* dans le menu déroulant *Type d'injection*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *Fichier* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Définir les propriétés d'injection*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension `.dpm`) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Sélectionner un fichier*, sélectionnez *Tous les fichiers (\*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur le bouton *OK*. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans Fluent. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Définir les propriétés d'injection* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Modèle de phase discrète* et sélectionnez *Interaction avec la phase continue* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier de journalisation comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier de journalisation après l'initialisation de la solution, par exemple :
```
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```
où un format de fichier stable d'injection de base créé manuellement pourrait ressembler à :
```bash title="zinjection01.inj"
$ cat zinjection01.inj
(z=4 12)
( x y z u v w diamètre t débit massique fréquence massique temps nom )
(( 2.90e-02 5.00e-03 0.0 -1,00e-03 0,0 0,0 1,00e-04 2,93e+02 1,00e-06 0,0 0,0 0,0 ) injection-0:1 )
```
notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans *2024R2 Fluent Customization Manual, Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format*.

## CFX

### Scripts pour l'ordonnanceur Slurm
Le résumé des options de ligne de commande peut être affiché avec **cfx5solve -help**. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, `cfx5solve` s'exécute en simple précision (`-single`). Pour exécuter `cfx5solve` en double précision, ajoutez l'option `` `-double` ``, sachant que cela doublera également les besoins en mémoire. Par défaut, `cfx5solve` prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `` `-large` ``. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'ANSYS CFX-Solver Manager pour plus de détails.

=== "Nœud simple"
```bash title="script-local.sh"
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
Avant de soumettre une tâche Workbench à la file d'attente avec un script Slurm, vous devez l'initialiser une fois, comme décrit dans les étapes suivantes :
1.  Sur la grappe où vous soumettrez les tâches Workbench, ouvrez un bureau [Open OnDemand (OOD)](https://docs.alliancecan.ca/wiki/Open_OnDemand#Logging_into_the_Open_OnDemand_portal) desktop.
2.  Une fois le bureau affiché, ouvrez une fenêtre de terminal et accédez au répertoire contenant votre fichier `` `VOTREPROJET.wbpj` ``.
3.  Supprimez l'ancien répertoire cache de `/projet` en exécutant `` `rm -rf _ProjectScratch` ``, car il peut être très volumineux suite à des exécutions précédentes.
4.  Ouvrez une fenêtre de terminal et chargez la version du module que vous utiliserez dans votre script Slurm, par exemple `` `module load ansys/2025R2.04` ``.
5.  Ouvrez l'interface graphique de Workbench avec votre fichier de `/projet`. Pour ce faire, exécutez directement la commande `` `runwb2 -f VOTREPROJET.wbpj` `` via la ligne de commande. Si une fenêtre contextuelle apparaît vous demandant *Voulez-vous récupérer le projet avant de l'ouvrir ? (Toutes les modifications apportées depuis la dernière sauvegarde seront perdues.)*, répondez Non.
    Dans le menu contextuel qui devrait apparaître au centre de la fenêtre *Schéma du projet*, cliquez avec le bouton droit sur *Modèle* et sélectionnez *Réinitialiser*. Lorsqu'Ansys Workbench affiche l'avertissement *Cette opération supprimera les données locales et générées de l'opération*, cliquez sur OK pour accepter et continuer.
6.  Dans le menu déroulant de la barre de menu supérieure, sélectionnez *Fichier -> Enregistrer* puis *Fichier -> Quitter* pour fermer Workbench.
7.  Dans la fenêtre contextuelle Ansys Workbench qui affiche *Le projet actuel a été modifié. Voulez-vous l'enregistrer ?* cliquez sur le bouton *Non*.
8.  Quittez Workbench et soumettez la tâche avec un des scripts ci-dessous.

Puisqu'il est désormais possible de réserver un nœud de calcul doté de jusqu'à 96 cœurs, 768 Go de mémoire et 8 heures d'autonomie pour une session de bureau OnDemand, exécutez vos simulations Workbench directement depuis l'interface graphique native de Workbench lorsque cela est possible; il s'agit d'une option plus intuitive que de soumettre la tâche à la file d'attente via un script Slurm.

### Scripts pour l'ordonnanceur Slurm
Pour soumettre un fichier de projet à la queue, personnaliser les scripts suivants et lancer la commande `` `sbatch script-wbpj-202X.sh` ``.

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

runwb2 -B -E "Update()" -F YOURPROJECT.wbpj
#runwb2 -B -E "Update();Save(Overwrite=True)" -F YOURPROJECT.wbpj
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

module load StdEnv/2020 ansys/2021R2   # OR newer Ansys module versions

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

Pour ne pas écrire la solution lorsqu'une tâche en cours se termine avec succès, remplacez `` `Save(Overwrite=True)` `` par `` `Save(Overwrite=False)` `` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera l'évaluation de la mise à l'échelle de la simulation lorsque la valeur de `` `#SBATCH --ntasks` `` est augmentée, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical
Le fichier d'entrée peut être généré dans votre session interactive Workbench Mechanical en cliquant sur *Solution -> Outils -> Écrire les fichiers d'entrée* et en spécifiant `` `Nom du fichier :` `` pour `YOURAPDLFILE.inp` et `` `Enregistrer sous le type :` `` pour les fichiers APDL en entrée (*.inp*). Les tâches APDL peuvent ensuite être soumises à la queue avec la commande `` `sbatch script-name.sh` ``.

### Scripts pour l'ordonnanceur Slurm
Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `` `##SBATCH` `` sont suivies d'un commentaire.

=== "Mémoire partagée parallèle (CPU)"
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

=== "Mémoire distribuée parallèle (CPU)"
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

=== "Mémoire partagée parallèle (GPU)"
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

Par défaut, Ansys alloue aux tâches APDL 1024 Mo de mémoire totale et 1024 Mo de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `` `-m 1024` `` et/ou `` `-db 1024` `` sur la dernière ligne de commande `mapdl` des scripts ci-dessus. Si vous utilisez à distance un serveur de licence de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `` `-p aa_r` `` ou `` `-ppf anshpc` ``, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de mise à l'échelle avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire partagée parallèle (SMP pour *Shared Memory Parallel*) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (DMP pour *Distributed Memory Parallel*) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```
! ANSYS input file written by Workbench version 2019 R3
```

## Rocky
Cette section fournit des scripts Slurm pour résoudre des simulations Rocky autonomes non couplées dans une file d'attente de grappe. Les deux scripts sont configurés avec `` `RESUME=0` `` afin que les simulations soient résolues depuis le début par défaut. Pour redémarrer une simulation partiellement terminée, définissez `` `RESUME=1` `` et soumettez à nouveau le script à la file d'attente. Pour obtenir une liste complète des options de ligne de commande, exécutez `` `Rocky -h` `` sur la ligne de commande après avoir chargé le module Ansys. Puisqu'un fichier de verrouillage est généré chaque fois qu'une simulation est démarrée, une seule tâche doit être soumise à la fois à partir du même répertoire. Concernant le script à utiliser, bien que toutes les simulations doivent être testées indépendamment, pour un cas de test de base, le script basé sur GPU s'est avéré surpasser le script basé sur CPU d'un facteur de 3,5x. Des augmentations supplémentaires des ressources au-delà de 6 CPU (pour le script CPU uniquement) ou 2 CPU + 1 GPU (1/7 d'un GPU H100 pour le script basé sur GPU) n'ont pas fourni d'accélération supplémentaire, selon les tests de mise à l'échelle pour les deux scripts. Compte tenu de ces résultats, il semble probable que le script basé sur GPU fournira des temps de résolution significativement plus rapides par rapport à l'utilisation uniquement de CPU pour d'autres simulations Rocky autonomes. Comme indiqué sur chaque page wiki de grappe ou comme résumé sous [Ratios dans les paquets](../running-jobs/allocations_and_compute_scheduling.md), toutes les grappes sauf Narval ont des GPU H100. Par conséquent, lors de l'utilisation du script GPU sur Narval, l'option Slurm `` `--gpus` `` doit être modifiée pour demander un GPU A100. Notez qu'en mai 2026, seul Rocky avec les modules `` `ansys/2025R2|2.04` `` a été testé, mais pas encore les modules `` `ansys/2025R1|1.02` ``.

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

=== "Basé sur GPU"
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

## Électronique
Des scripts Slurm pour utiliser AnsysEDT sont fournis dans [cette page](ansysedt.md).

## Mode graphique
Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [NIBI](../clusters/nibi.md) : `` `https://ondemand.sharcnet.ca` ``
*   [FIR](fir.md) : `` `https://jupyterhub.fir.alliancecan.ca` ``
*   [RORQUAL](../clusters/rorqual.md) : `` `https://jupyterhub.rorqual.alliancecan.ca` ``
*   [Narval](../clusters/narval.md) : `` `https://jupyterhub.narval.alliancecan.ca/` ``
*   TRILLIUM : `` `https://ondemand.scinet.utoronto.ca` ``

Une page web de soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources requises pour votre session de bureau interactive et cliquez sur *Lancer* ou *Démarrer*. Si des graphiques accélérés ou des calculs seront effectués à partir de votre session de bureau, assurez-vous de spécifier une ressource GPU. Chargez un module Ansys sur le bureau. Si vous avez démarré un bureau propulsé par JupyterLab, cela peut être fait en cliquant sur le menu de gauche, ou si vous avez démarré un bureau OnDemand manuellement, tapez `` `module load ansys/version` `` sur la ligne de commande. Pour démarrer l'un des programmes Ansys courants tels que Fluent, CFX, Workbench, etc., reportez-vous à la section suivante qui fournit des conseils pour définir les variables d'environnement et les arguments requis par les environnements graphiques basés sur VirtualGL ou Mesa, selon qu'un nœud avec une ressource GPU a été spécifié ou non.

### Fluent
Pour démarrer Ansys Fluent depuis la ligne de commande sur un bureau OnDemand, ouvrez une fenêtre de terminal et exécutez :

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```

Lorsque le panneau de sélection contextuel *Lanceur Fluent* apparaît, cliquez sur l'onglet *Environnement* et copiez/collez les paramètres de variable d'environnement suivants, selon que vous avez démarré votre session OnDemand avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses, car ce sont des commentaires, et ne mettez pas `export` devant le nom d'une variable. Si la fenêtre de la console graphique devient corrompue lors du démarrage de l'interface graphique, redémarrez Fluent en définissant `` `HOOPS_PICTURE=null` `` pour désactiver la création du panneau graphique.

**Nœud de calcul (sans GPU)**

*   `` `I_MPI_HYDRA_BOOTSTRAP=ssh` `` (requis sur nibi avec intelmpi)
*   `` `HOOPS_PICTURE=opengl2-mesa` `` (version 2025R1 ou plus récente)
*   `` `HOOPS_PICTURE=x11/lin` `` (version 2024R2.04 ou plus ancienne)
*   Cliquez sur le bouton *Démarrer*.

```
slurm_hl2hl.py --format ANSYS-FLUENT > machinefile
NCORES=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

fluent 3d -t $NCORES -cnf=machinefile -mpi=intel -affinity=0 -g -i sample.jou
```

NOTE: Lors de l'exécution de Fluent sur Nibi, la variable d'environnement `` `I_MPI_HYDRA_BOOTSTRAP=ssh` `` doit être définie manuellement; sinon, Fluent se bloquera au démarrage des sessions de bureau de calcul OOD lorsque `intelmpi` est utilisé. Un message d'erreur tel que le suivant sera généré :
```
[mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
[mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
[mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
[mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
[mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
```
Si cela se produit, quittez complètement Fluent, arrêtez proprement Workbench et recommencez.

### CFX
Lors du démarrage de CFX à partir d'un bureau OnDemand, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal, selon qu'un GPU a été demandé ou non lors du démarrage du bureau.

*   `` `module load StdEnv/2023 ansys/2025R1` `` (ou plus ancien)
*   `` `cfx5 -graphics mesa` `` (aucun GPU demandé)
*   `` `cfx5 -graphics ogl` `` (avec GPU demandé)

### Mapdl
Les étapes suivantes pour démarrer l'interface graphique de Mechanical APDL depuis la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre bureau OnDemand sur un nœud de calcul avec ou sans GPU.

*   `` `module load StdEnv/2023 ansys/2022R2` `` (ou versions plus récentes)
*   `` `mapdl -g` ``, ou
*   `` `launcher` `` puis cliquez sur le bouton *Lancer*.

### Workbench
Cette section montre comment démarrer Workbench (et éventuellement Fluent) sur un bureau OnDemand ou un bureau JupyterLab.

#### Bureau OnDemand

**Nœud de calcul (sans GPU demandé) ou Bureau de base**

*   `` `module load CcEnv StdEnv/2023` ``
*   `` `module load ansys/2025R1` `` (ou versions plus récentes)
*   `` `runwb2` `` (non disponible sur le serveur de licence SHARCNET avant sa mise à jour)

#### Bureau Jupyterhub

**Nœud de calcul (sans GPU)**

*   Cliquez pour charger ansys/2025R1 (ou version plus récente) dans le menu de gauche du bureau.
*   Cliquez sur l'icône *Workbench (VNC)* située au centre de la fenêtre du bureau JupyterLab.
*   Si les graphiques de toute application (comme Fluent) démarrée dans Workbench semblent inutilisables car corrompus, essayez les étapes suivantes. Elles créeront une icône de bureau `runwb2` personnalisée afin que Workbench puisse être démarré en mode Mesa. Si l'une des applications que vous démarrez dans Workbench est Fluent, vous pouvez également essayer de définir la variable `` `HOOPS_PICTURE=opengl2-mesa` `` dans la fenêtre du Lanceur Fluent lorsque celui-ci démarre.
*   Pour continuer, quittez Workbench et ouvrez une fenêtre de terminal. Copiez/collez la commande suivante dans le *Presse-papiers distant* situé dans le coin supérieur droit de votre bureau Jupyter.
*   Maintenant, les commandes peuvent être collées dans le terminal, c'est-à-dire : `` `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop` ``
*   Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que `nano` en faisant : `` `nano ~/Desktop/workbench-mesa.desktop` ``. Changez toutes les instances de `` `runwb2` `` en `` `runwb2 -oglmesa` `` et quittez l'éditeur, en sauvegardant les modifications. Maintenant, ACTUALISEZ le bureau Jupyter en appuyant sur la combinaison de touches *Ctrl-R*. La nouvelle icône devrait maintenant apparaître sur le bureau avec l'icône Workbench d'origine. Double-cliquez dessus pour démarrer Workbench.
*   La nouvelle icône persistera pour les sessions futures jusqu'à ce qu'elle soit supprimée manuellement avec la commande `` `rm -f ~/Desktop/workbench-mesa.desktop` ``.

**Nœud de calcul (avec GPU)**

*   Cliquez pour charger ansys/2025R1 (ou version plus récente) dans le menu de gauche du bureau.
*   Cliquez sur l'icône *Workbench (VNC)* située au centre de la fenêtre du bureau JupyterLab.

### Ensight
*   `` `module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6` ``
*   `` `export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib` ``
*   `` `ensight -X` ``

### Rocky
*   `` `module load StdEnv/2023 ansys/2025R2.04` `` (ou 2025R1, 2025R1.02, 2025R2)
*   `` `Rocky` `` La commande Rocky démarre Rocky en mode GUI autonome.
*   `` `RockySolver` `` Exécute le solveur directement depuis la ligne de commande (non testé).
*   `` `RockySchedular` `` Interface graphique pour soumettre/exécuter interactivement des tâches sur le nœud actuel (non testé).
*   Le module ansys gère la lecture de votre fichier `` `~/licenses/ansys.lic` ``.
*   La licence ansys de SHARCNET inclut Rocky, donc son utilisation est gratuite pour la recherche.

## Électronique
Des informations décrivant comment exécuter AnsysEDT en mode graphique peuvent être trouvées [dans cette page](ansysedt.md).

## Particularités selon le site d'utilisation

### Licence SHARCNET
La licence Ansys de SHARCNET est gratuite pour une utilisation académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de ***recherche universitaire publiable***; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la Solution Campus Multiphysics en mai 2020 et inclut les produits suivants : HF, EM, Electronics HPC, Mechanical et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Rocky et LS-DYNA sont aussi maintenant inclus dans la licence SHARCNET. Lumerical acquis par ANSYS en 2020 n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. SpaceClaim sous Linux n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences `anshpc` de 1986 est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50% en CPU seront probablement signalées par le système et examinées par notre équipe technique.

```bash
unset SLURM_GTIDS
```

*   `` `module load CcEnv StdEnv/2023` ``
*   `` `module load ansys/2025R1` `` (ou versions plus récentes)
*   `` `runwb2` `` (non disponible sur le serveur de licence SHARCNET avant sa mise à jour)
*   ------------------------------------------------------------------

Depuis décembre 2022, chaque utilisateur peut exécuter 4 travaux en utilisant un total de 252 `anshpc` (plus 4 `anshpc` par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon ( (252 + 4\*nombre de tâches) / nombre de tâches). **MISE À JOUR :** En octobre 2024, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

#### Fichier du serveur de licence
Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `` `ansys.lic` `` comme suit :
```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
```

#### Vérification de la licence
Pour connaître le nombre de licences utilisées qui sont associées à votre nom d'utilisateur et le nombre de licences utilisées par tous les utilisateurs, lancez :
```bash
ssh nibi.alliancecan.ca
module load ansys
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil \
lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
```

### Exemple
```bash
#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-06:00       # Specify time limit dd-hh:mm
#SBATCH --ntasks=16           # Specify total number cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change
```

```bash
module load ansys/2020R1
```

```
[l2(nibi):~] sq
            JOBID     USER        ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS MIN_MEM NODELIST (REASON)
         10161023  roberpj   cc-debug_cpu script-flu-int   R    2:57:19     4    8     N/A      4G c[630-633] (None)
         10161033  roberpj   cc-debug_cpu script-flu-int   R    2:58:25    16   32     N/A      4G c[627-628,630-633,637,642,645,655,657,662,665,667,669,682] (None)
[l2(nibi):~]
[l2(nibi):~] module load ansys
[l2(nibi):~]
[l2(nibi):~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil  \
              lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total de 0 licences utilisées"
Utilisateurs de anshpc :  (Total de 1986 licences émises;  Total de 1600 licences utilisées)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 2579), début mer. 3/11 16:46, 4 licences, PID : 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 5716), début mer. 3/11 16:48, 28 licences, PID : 510058
Utilisateurs de cfd_base :  (Total de 275 licences émises;  Total de 19 licences utilisées)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10327), début mer. 3/11 16:46, PID : 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 7171), début mer. 3/11 16:47, PID : 510058
Utilisateurs de cfd_preppost :  (Total de 275 licences émises;  Total de 1 licence utilisée)
Utilisateurs de cfd_preppost_pro :  (Total de 275 licences émises;  Total de 1 licence utilisée)
Utilisateurs de cfd_solve_level1 :  (Total de 275 licences émises;  Total de 18 licences utilisées)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 7994), début mer. 3/11 16:46, PID : 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 6200), début mer. 3/11 16:47, PID : 510058
Utilisateurs de cfd_solve_level2 :  (Total de 275 licences émises;  Total de 18 licences utilisées)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10520), début mer. 3/11 16:46, PID : 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 375), début mer. 3/11 16:47, PID : 510058
Utilisateurs de elec_solve_hfss :  (Total de 275 licences émises;  Total de 1 licence utilisée)
Utilisateurs de elec_solve_level1 :  (Total de 275 licences émises;  Total de 1 licence utilisée)
Utilisateurs de elec_solve_level2 :  (Total de 275 licences émises;  Total de 1 licence utilisée)
```

Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur `gra-vdi`), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `` `pkill -9 -e -u $USER -f "ansys"` `` pour libérer vos licences. Prenez note que `gra-vdi` possède deux nœuds (`gra-vdi3` et `gra-vdi4`) qui vous sont assignés au hasard quand vous vous connectez avec `tigervnc`; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (`gra-vdi3.sharcnet.ca` ou `grav-vdi4.sharcnet.ca`) quand vous vous connectez.

## Fabrication additive
Configurez d'abord votre fichier `` `~/.licenses/ansys.lic` `` pour l'orienter vers le serveur de licence où se trouve une licence valide pour Ansys Mechanical. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

### Activer la fabrication additive
Nous décrivons ici comment obtenir l'extension ACT de Ansys Additive Manufacturing pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple `ANSYSMotion`, désinstallez-les à partir de votre projet.

#### Télécharger l'extension
*   téléchargez `AdditiveWizard.wbex` à partir de [https://catalog.ansys.com/](https://catalog.ansys.com/)
*   téléversez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser

#### Lancer Workbench
*   Voir la section Workbench dans [Mode graphique](#mode-graphique) plus haut.
*   Dans l'interface Workbench, ouvrez votre fichier de projet avec *Fichier -> Ouvrir*.

#### Ouvrir le gestionnaire d'extensions
*   Cliquez sur la page *Démarrer ACT* pour faire afficher l'onglet de la page *Accueil ACT*.
*   Cliquez sur *Gérer les extensions* pour ouvrir le gestionnaire d'extensions.

#### Installer l'extension
*   Cliquez sur la boîte avec le signe `+` sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

#### Charger l'extension
*   Cliquez pour sélectionner la boîte AdditiveWizard, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Charger l'extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

#### Supprimer l'extension
*   Cliquez pour désélectionner la boîte AdditiveWizard, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte AdditiveWizard et sélectionnez *Ne pas charger par défaut*, ce qui empêche le chargement de l'extension pour les futures sessions.

### Exécuter la fabrication additive

#### OnDemand
Vous pouvez exécuter une seule tâche Ansys Additive Manufacturing dans une session graphique OnDemand comme suit :

*   Lancez Workbench comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*.
*   Cliquez sur *Fichier -> Ouvrir* et sélectionnez *test.wbpj* puis cliquez sur *Ouvrir*.
*   Cliquez sur *Vue -> Réinitialiser l'espace de travail* si votre écran est gris.
*   Lancez *Mechanical, Effacer les données générées*, sélectionnez *Distribué*, spécifiez *Cœurs*.
*   Cliquez sur *Fichier -> Enregistrer le projet -> Résoudre*.

Vérifiez l'utilisation :
*   Ouvrez un autre terminal et lancez `` `top -u $USER` `` OU `` `ps u -u $USER | grep ansys` ``.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `` `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"` ``.

Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion `gra-vdi` ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur `gra-vdi`. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (Fluent, Workbench, etc.) n'est pas correctement terminée avant que `vncviewer` ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

#### Grappe

##### Préparation du projet
Certaines préparations doivent être effectuées avant de soumettre un projet Additive nouvellement téléchargé dans la file d'attente d'une grappe avec `` `sbatch scriptname` ``. Pour commencer, ouvrez votre simulation avec l'interface graphique de Workbench (comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour Workbench dans la section *Soumettre des tâches en lot sur nos grappes* ci-dessus). Pour effectuer des études paramétriques, remplacez `` `Update()` `` par `` `UpdateAllDesignPoints()` `` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans Workbench entre chaque exécution de test, soit 1. remplacez `` `Save(Overwrite=True)` `` par `` `Save(Overwrite=False)` ``; ou 2. enregistrez une copie du fichier *YOURPROJECT.wbpj* d'origine et du répertoire *YOURPROJECT_files* correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne FilePath.

```
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

##### Utilisation des ressources
Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `` `srun` ``. Le script pour 8 cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

```
[gra-login1:~] srun --overlap --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
 22843 demo   20   0 2272124 256048  72796 R  88.0  0.2  1:06.24  ansys.e
 22849 demo   20   0 2272118 256024  72822 R  99.0  0.2  1:06.37  ansys.e
 22838 demo   20   0 2272362 255086  76644 R  96.0  0.2  1:06.37  ansys.e
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
  4310 demo   20   0 2740212 271096 101892 R 101.0  0.2  1:06.26  ansys.e
  4311 demo   20   0 2740416 284552  98084 R  98.0  0.2  1:06.55  ansys.e
  4304 demo   20   0 2729516 268824 100388 R 100.0  0.2  1:06.12  ansys.e
  4305 demo   20   0 2729436 263204 100932 R 100.0  0.2  1:06.88  ansys.e
  4306 demo   20   0 2734720 431532  95180 R 100.0  0.3  1:06.57  ansys.e
```

##### Tests de scalabilité
Une fois la tâche complétée, son *temps d'exécution réel (Wall-clock time)* peut être obtenu avec `` `seff jobid` ``. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le Wall-clock time diminue d'environ 50%, vous pouvez continuer de doubler le nombre de cœurs.

## Aide et ressources
La documentation officielle complète pour les versions récentes Ansys 202[4|5]R[1|2] est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles qu'Ansys 2023R[1|2] nécessite cependant une [connexion](https://ansyshelp.ansys.com/). La documentation pour les développeurs se trouve dans le [Portail des développeurs Ansys](https://developer.ansys.com). Les ressources d'apprentissage supplémentaires comprennent les [Vidéos Ansys HowTo](https://www.youtube.com/@AnsysHowTo/videos), le [Centre de ressources pour les éducateurs Ansys](https://innovationspace.ansys.com/educator-hub/) et la [Série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

```bash
#module load ansys/2021R1
module load ansys/2021R2