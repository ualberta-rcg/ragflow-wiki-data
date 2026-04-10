---
title: "Materials Studio/fr"
slug: "materials_studio"
lang: "fr"

source_wiki_title: "Materials Studio/fr"
source_hash: "7a795e9be20207d6513600c4858ce62a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:28:23.018563+00:00"

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

L'Alliance n'a pas la permission d'installer Materials Studio de façon centrale sur toutes les grappes. Si vous disposez d'une licence, suivez ces directives pour installer l'application dans votre compte. Notez que ces directives sont valides pour les environnements logiciels moins récents; si vous utilisez présentement l'environnement 2020 par défaut, vous devrez utiliser une commande comme `module load StdEnv/2016.4` avant de commencer (voir [Environnements logiciels standards](standard-software-environments.md)).

## Installation de Materials Studio 2020

!!! note "Remarque"
    Ces directives ont été testées avec Materials Studio 2020.

Si vous avez accès à Materials Studio 2020, vous avez besoin
* du fichier archive `BIOVIA_2020.MaterialsStudio2020.tar` qui contient l'installeur;
* de l'adresse IP (ou le nom du DNS) et le port du serveur de licence préconfiguré auquel vous voulez vous connecter.

Téléversez maintenant le fichier `BIOVIA_2020.MaterialsStudio2020.tar` dans votre répertoire `/home` sur la grappe que vous voulez utiliser. Lancez ensuite les commandes

```bash
export MS_LICENSE_SERVER=<port>@<server>
```

et

```bash
eb MaterialsStudio-2020.eb --sourcepath=$HOME
```

Une fois que la commande est terminée, déconnectez-vous de la grappe et connectez-vous de nouveau. Vous devriez alors pouvoir charger le module avec

```bash
module load materialsstudio/2020
```

Pour avoir accès au serveur de licence à partir d'un nœud de connexion, [contactez le soutien technique](technical-support.md) pour que nous configurions nos pare-feu de façon à permettre au logiciel d'avoir accès à votre serveur de licence.

## Installation de Materials Studio 2018

!!! note "Remarque"
    Ces directives ont été testées avec Materials Studio 2018.

Si vous avez accès à Materials Studio 2018, vous aurez besoin
* du fichier d'archive (`MaterialsStudio2018.tgz`) qui contient l'installeur,
* de l'adresse IP (ou du nom DNS) et du port d'un serveur de licence déjà configuré auquel vous voulez vous connecter.

Téléchargez ensuite le fichier `MaterialsStudio2018.tgz` dans votre répertoire `/home` de la grappe et lancez les commandes

```bash
export MS_LICENSE_SERVER=<port>@<server>
```

et

```bash
eb /cvmfs/soft.computecanada.ca/easybuild/easyconfigs/m/MaterialsStudio/MaterialsStudio-2018.eb --disable-enforce-checksums --sourcepath=$HOME
```

Lorsque l'opération est terminée, déconnectez-vous de la grappe et connectez-vous de nouveau. Vous devriez alors pouvoir charger le module avec

```bash
module load materialsstudio/2018
```

Pour accéder au serveur de licence à partir d'un nœud de calcul, contactez le [soutien technique](technical-support.md) pour que nos pare-feu soient configurés en conséquence.

### Installation pour un groupe

Si vous êtes chercheur principal et disposez d'une licence, vous n'avez qu'à installer l'application une fois pour tous les utilisateurs de votre groupe. Comme les travaux d'une équipe sont habituellement enregistrés dans l'espace `/project`, déterminez lequel des répertoires de cet espace vous voulez utiliser. Par exemple, s'il s'agit de `~/projects/A_DIRECTORY`, vous devrez connaître ces deux valeurs :

1.  Déterminez le chemin pour `A_DIRECTORY` avec
    ```bash
    PI_PROJECT_DIR=$(readlink -f ~/projects/A_DIRECTORY)
    echo $PI_PROJECT_DIR
    ```
2.  Déterminez le groupe pour `A_DIRECTORY` avec
    ```bash
    PI_GROUP=$(stat -c%G $PI_PROJECT_DIR)
    echo $PI_GROUP
    ```

Avec ces deux valeurs, installez Materials Studio comme suit :

1.  Remplacez le groupe par défaut par le groupe de l'équipe `def-`.
    ```bash
    newgrp $PI_GROUP
    ```
2.  Configurez les permissions pour donner accès au groupe.
    ```bash
    chmod g+rsx $PI_PROJECT_DIR
    ```
3.  Créez un répertoire dans `/project` pour l'installation.
    ```bash
    mkdir $PI_PROJECT_DIR/MatStudio2018
    ```
4.  Installez l'application.
    ```bash
    MS_LICENSE_SERVER=<port>@<server> eb MaterialsStudio-2018-dummy-dummy.eb --installpath=$PI_PROJECT_DIR/MatStudio2018 --sourcepath=$HOME
    ```

Avant de lancer l'application :

1.  Lancez la commande
    ```bash
    module use $PI_PROJECT_DIR/MatStudio2018/modules/2017/Core/
    ```
    *   Les membres de l'équipe peuvent ajouter ceci à leur fichier `~/.bashrc`.
2.  Chargez le module materialsstudio.
    ```bash
    module load materialsstudio
    ```

!!! attention "À noter"
    Assurez-vous de toujours remplacer les variables `PI_GROUP` et `PI_PROJECT_DIR` par les valeurs appropriées.

## Exemples de scripts pour l'ordonnanceur Slurm

Les exemples suivants sont valides pourvu que vous ayez suivi les directives d'installation ci-dessus.

````bash title="Script Slurm (DMol3)"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --time=12:00:00

module load materialsstudio/2018

# Create a list of nodes to be used for the job
DSD_MachineList="machines.LINUX"
slurm_hl2hl.py --format HP-MPI > $DSD_MachineList
export DSD_MachineList

# Job to run
RunDMol3.sh -np $SLURM_CPUS_PER_TASK Brucite001f
````

Le script suivant utilise la commande Materials Studio `RunCASTEP.sh`.

````bash title="Script Slurm (CASTEP)"
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1M
#SBATCH --time=0-12:00

module load materialsstudio/2018

DSD_MachineList="mpd.hosts"
slurm_hl2hl.py --format MPIHOSTLIST >$DSD_MachineList
export DSD_MachineList

RunCASTEP.sh -np $SLURM_CPUS_PER_TASK castepjob

if [ -f castepjob_NMR.param ]; then
  cp castepjob.check castepjob_NMR.check
  RunCASTEP.sh -np $SLURM_CPUS_PER_TASK castepjob_NMR
fi
````

## Installation de versions antérieures

Pour utiliser une version de Materials Studio antérieure à 2018, vous devez l'installer dans un conteneur [Apptainer](apptainer.md).

1.  Créez un conteneur Apptainer dans lequel est installée une distribution compatible de Linux.
2.  Installez Materials Studio dans ce conteneur.
3.  Téléversez le conteneur Apptainer vers votre compte.
    *   **NOTE :** Pour accéder au serveur de licence à partir d'un nœud de calcul, contactez le [soutien technique](technical-support.md) pour que nos pare-feu soient configurés en conséquence.

Comme il se peut que la version de MPI dans le conteneur ne puisse pas être utilisée sur plusieurs nœuds, il est possible que vos tâches soient limitées à des nœuds entiers (nœud unique).