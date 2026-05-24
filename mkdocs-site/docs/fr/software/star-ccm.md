---
title: "Star-CCM+/fr"
slug: "star-ccm"
lang: "fr"

source_wiki_title: "Star-CCM+/fr"
source_hash: "d07cf787f238425da25c89608b2d19df"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:51:36.738293+00:00"

tags:
  - software

keywords:
  - "~/.flexlmrc"
  - "fichiers de sortie"
  - "Mode graphique"
  - "licence PoD"
  - "grappes"
  - "bash"
  - "Slurm"
  - "Fir/Narval/Rorqual"
  - "toutes les versions"
  - "Parallel on Local Host"
  - "JupyterLab"
  - "répertoires cachés"
  - "quota"
  - "Script Bash"
  - "Nibi"
  - "module load"
  - "TRILLIUM"
  - "StarCCM+"
  - "exécution en parallèle"
  - "SBATCH"
  - "Ordonnanceur"
  - "nœud de calcul"
  - "serveur de licence"
  - "Open OnDemand"
  - "starccm.lic"
  - "simulation"
  - "bash script"
  - "starccm_job-fnr-nogpu.sh"
  - "STAR-CCM+"
  - "SLURM"
  - "java macros"
  - "VncViewer"
  - "Siemens PoD Key"
  - "institutional license server"
  - "sim filename"
  - "job script"
  - "MPI"

questions:
  - "Qu'est-ce que le logiciel STAR-CCM+ et dans quels domaines d'ingénierie est-il principalement utilisé ?"
  - "Quelles sont les différences de configuration et d'exigences réseau entre une licence Power-on-Demand (PoD) et un serveur de licence institutionnel local ?"
  - "Quelles étapes doivent être suivies pour soumettre des tâches en lot sur les grappes et comment gérer l'espace disque face à l'accumulation de fichiers cachés ?"
  - "Pourquoi est-il conseillé de renommer le fichier `~/.flexlmrc` ?"
  - "Quel impact les répertoires cachés `.star-version_number` peuvent-ils avoir sur votre espace de stockage ?"
  - "Quelle commande doit-on exécuter pour supprimer les fichiers de sortie accumulés et libérer son quota ?"
  - "Comment configurer les ressources matérielles (nœuds, cœurs, mémoire) dans le script Slurm pour exécuter STAR-CCM+ ?"
  - "De quelle manière le script adapte-t-il les paramètres d'exécution en fonction du fabricant du processeur (Intel ou AMD) ?"
  - "Quelle est la différence de configuration dans le script entre l'utilisation d'une clé de licence Siemens PoD et celle d'un serveur de licence institutionnel ?"
  - "What specific clusters is this SLURM job submission script designed to run on?"
  - "How many nodes and CPUs per task are allocated in the script's compute resource settings?"
  - "What are the maximum time limit and memory constraints defined for this job?"
  - "How does the script dynamically configure the MPI and BLAS environment variables based on the CPU vendor?"
  - "What are the two different licensing methods supported by the script, and how is the Siemens PoD Key specified?"
  - "What specific SLURM directives are required to allocate resources for a STAR-CCM+ job on the Trillium cluster?"
  - "Comment le script fourni gère-t-il les échecs de connexion au serveur de licence lors de l'exécution de STAR-CCM+ en mode batch ?"
  - "Quelles sont les configurations préalables requises pour utiliser STAR-CCM+ en mode graphique avec une licence PoD via Open OnDemand ?"
  - "Quelles commandes doivent être utilisées pour rechercher et charger les versions spécifiques des modules STAR-CCM+ disponibles sur le système ?"
  - "How are the input simulation filename and the batch commands for macros, meshing, and running specified in this script?"
  - "What is the purpose of the LM_PROJECT variable, and what specific information must be provided for it?"
  - "How does this configuration handle license server routing compared to the default ~/.licenses/starccm.lic file, and when should the PoD key line be commented out?"
  - "Quelles sont les adresses web mentionnées pour accéder au système TRILLIUM ?"
  - "Quelles commandes doivent être utilisées pour charger le module et exécuter le logiciel STAR-CCM+ en mode série ou parallèle ?"
  - "Quelles versions spécifiques du logiciel STAR-CCM+ sont couvertes par ces instructions ?"
  - "Comment démarrer et configurer une session STAR-CCM+ pour une exécution en parallèle via JupyterLab ?"
  - "Quelles sont les commandes spécifiques à exécuter dans VncViewer selon la version de STAR-CCM+ choisie ?"
  - "Quels sont les liens d'accès permettant de démarrer une session JupyterHub Desktop sur les différentes grappes de calcul ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[STAR-CCM+](https://mdx.plm.automation.siemens.com/star-ccm-plus) est une suite logicielle de simulation utilisée dans plusieurs spécialités de génie. Elle permet la modélisation dans des domaines variés dont l'acoustique, la dynamique des fluides, le transfert thermique, la rhéologie, l'écoulement polyphasique, le flux de particules, la mécanique des solides, les fluides réactifs, l'électrochimie et l'électromagnétisme.

## Limites de la licence

Nous avons l'autorisation d'héberger les binaires STAR-CCM+ sur nos grappes. Pour utiliser le logiciel, vous devez acquérir une licence auprès de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/). [Deux options sont disponibles](https://community.sw.siemens.com/s/article/How-faculty-members-in-academic-institutions-can-get-access-to-Simcenter-STAR-CCM). La plupart des groupes de recherche opteront pour une [licence Power-on-Demand (PoD)](https://community.sw.siemens.com/s/question/0D54O00006FKu39SAD/licensing-how-power-on-demand-pod-licensing-for-starccm-works), qui se connecte simplement à un serveur de licence distant et ne nécessite qu'une clé de licence. La seconde option est plus complexe et nécessite la configuration et la gestion d'un serveur de licence institutionnel hébergé localement, ainsi que l'achat d'un pack académique Simcenter STAR-CCM+. Votre serveur de licence STAR-CCM+ devra être reconfiguré. Vous devez demander à l'administrateur du serveur de licence de votre établissement d'ouvrir les **deux** ports fournisseurs (flexible et statique) pour qu'ils puissent être rejoints à partir des nœuds NAT (*Network Address Translation*) des grappes que vous voulez utiliser. Pour obtenir la liste des nœuds NAT à fournir à votre administrateur, écrivez au [soutien technique](../support/technical_support.md) en indiquant 1) le nom de la ou des grappes 2) le nom de l'hôte (FQDN) ou l'adresse IP publique du serveur de licence STAR-CCM+ et les numéros des ports flexible et statique.

## Configurer votre compte

Afin de configurer votre compte pour utiliser un serveur de licence avec le module Star-CCM+, créez le fichier `$HOME/.licenses/starccm.lic` comme suit :

```text
::: starccm.lic
SERVER <server> ANY <flexport>
USE_SERVER
```

où `server` et `flexport` sont remplacés respectivement par le nom de l'hôte (ou l'adresse IP) et le port statique du fournisseur du serveur de licence. Il n'est pas nécessaire de définir manuellement `CDLMD_LICENSE_FILE` comme étant égal à <port>@<server> dans votre script slurm puisque cette variable est automatiquement configurée quand un module Star-CCM+ est chargé.

### Fichier pour une licence PoD

Si vous avez acheté une licence POD, votre variable d'environnement `LM_PROJECT` doit être manuellement configurée comme étant égale à *YOUR CD-ADAPCO PROJECT ID* dans votre script slurm. De plus, le fichier `~/.licenses/starccm.lic` doit être configuré comme suit sur toutes les grappes.

```text
::: starccm.lic
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

## Soumettre des tâches en lot sur nos grappes

Avant de soumettre des tâches sur une grappe, vous devez configurer un fichier `~/.licenses/starccm.lic` sur chaque grappe où vous exécuterez des tâches. Si vous disposez d'une licence PoD, les modifications de pare-feu requises ont déjà été effectuées sur toutes nos grappes. Cependant, si vous utilisez un serveur de licence institutionnel local, vous devrez soumettre une [demande d'assistance au soutien technique](../support/technical_support.md) pour demander la modification ponctuelle du pare-feu réseau entre la ou les grappes et votre serveur de licence local. Si vous rencontrez toujours des problèmes pour faire fonctionner la licence, essayez de supprimer ou de renommer le fichier `~/.flexlmrc` car les chemins de recherche et/ou les paramètres précédents du serveur de licence pourraient y être stockés. Notez que des fichiers de sortie de tâches déjà exécutées peuvent s'accumuler dans des répertoires cachés nommés `.star-version_number` et consommer ainsi votre quota. Ceux-ci peuvent être supprimés en exécutant périodiquement `rm -ri ~/.starccm*` et en répondant *oui* à l'affichage de l'invite.

## Scripts pour l'ordonnanceur

=== "Nibi"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    #SBATCH --constraint=granite  # Use intel cpu only base nodes
    #SBATCH --switches=1          # Use 1 network switch (optional)

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Load 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using a local institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

    CPU_VENDOR=$(lscpu | awk '/Vendor ID/{print $3}')
    echo "CPU_VENDOR= $CPU_VENDOR"
    if [ "$CPU_VENDOR" == GenuineIntel ]; then
      if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
        STAR_UCX="-xsystemucx"
        export FLEXIBLAS=StarMKL
      else
        STAR_FLEXIBLAS="-flexiblaslib MKL"
      fi
      STAR_MPI="-mpi intel"
      STAR_FABRIC="-fabric tcp"
    elif [ "$CPU_VENDOR" == AuthenticAMD ]; then
      if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
        STAR_UCX="-xsystemucx"
        export FLEXIBLAS=StarAOCL
      else
        STAR_FLEXIBLAS="-flexiblaslib AOCL"
        STAR_PRELOAD="-ldpreload /usr/lib64/libdrm_amdgpu.so.1"
      fi
      STAR_MPI="-mpi openmpi40"
    fi

    if [ -n "$LM_PROJECT" ]; then
       echo "Siemens PoD license server ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
    fi
    ```

=== "Fir/Narval/Rorqual"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using an institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Checking $CDLMD_LICENSE_FILE ..."
    server=$(head -n1 $CDLMD_LICENSE_FILE | awk '{print $2}')
    port=$(cat $CDLMD_LICENSE_FILE | grep -Eo '[0-9]+$')
    nmap $server -Pn -p $port | grep -v '^$'; echo

    export FLEXIBLAS=NETLIB
    STAR_MPI="-mpi openmpi"
    if [ "$RSNT_CPU_VENDOR_ID" == intel ]; then
      export FLEXIBLAS=StarMKL
      STAR_MPI="-mpi intel"
    elif [ "$RSNT_CPU_VENDOR_ID" == amd ]; then
      export FLEXIBLAS=StarAOCL
    fi
    echo "FLEXIBLAS=$FLEXIBLAS"

    if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
      STAR_UCX="-xsystemucx"
    fi

    if [ -n "$LM_PROJECT" ]; then
       echo "Siemens PoD license server ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
    fi
    ```

=== "Trillium"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=192   # Specify cores per node (192 max)
    #SBATCH --mem=0               # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    #SBATCH --output=slurm-%j.out # Writes to slurm-$SLURM_JOB_ID.out

    ```

=== "Niagara"

    ```bash
    #!/bin/bash

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using an institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # These settings are used instead of your ~/.licenses/starccm.lic
    # (settings shown will use the cd-adapco pod license server)
    FLEXPORT=1999                    # Specify server static flex port
    VENDPORT=2099                    # Specify server static vendor port
    LICSERVER=flex.cd-adapco.com     # Specify license server hostname

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    export CDLMD_LICENSE_FILE="$FLEXPORT@127.0.0.1"
    ssh tri-gw -L $FLEXPORT:$LICSERVER:$FLEXPORT -L $VENDPORT:$LICSERVER:$VENDPORT -N -f

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    export FLEXIBLAS=StarAOCL
    echo "FLEXIBLAS=$FLEXIBLAS"
    STAR_MPI="-mpi openmpi"

    if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
      STAR_UCX="-xsystemucx"
    fi

    # Workaround for license failures:
    # until the exit status is equal to 0, we try to get Star-CCM+ to start (here, for at least 5 times).
    i=1
    RET=-1
    while [ $i -le 5 ] && [ $RET -ne 0 ]; do
            [ $i -eq 1 ] || sleep 5
              echo "Attempt number: "$i
              if [ -n "$LM_PROJECT" ]; then
              echo "Siemens PoD license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            else
              echo "Institutional license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            fi
            RET=$?
            i=$((i+1))
    done
    exit $RET
    ```

## Mode graphique

Pour travailler en mode graphique, nous recommandons d'utiliser un système [OnDemand](../clusters/nibi.md) ou JupyterLab pour démarrer un bureau distant. En plus de configurer `~/.licenses/starccm.lic`, les groupes qui possèdent une licence PoD devraient aussi exécuter `export LM_PROJECT='22digit-PoD-License-Key'` avant `starccm+`, comme dans les exemples ci-dessous; selon le type de licence, il faut aussi ajouter d'autres options comme **-power**. La commande `module avail starccm-mixed` affiche les versions de starccm qui peuvent être chargées dans l'environnement standard (StdEnv) qui est en place (2020 ou 2023). Autrement, la commande `module spider starccm-mixed` affiche toutes les versions *mixed* et *R8* des modules qui peuvent être chargés dans les deux versions des modules d'environnement variable qui peuvent être utilisées (2020 ou 2023).

### OnDemand

1.  Pour démarrer une session de bureau OnDemand, cliquez sur l'un des liens OnDemand suivants :
    *   NIBI: `https://ondemand.sharcnet.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.06.010` **OU** `starccm/20.06.010-R8`
        *   `starccm+ -rr server`   (options, "Serial")
        *   `starccm+ -rr server -np 2 -mpi openmpi40`   (options, "Parallel on Local Host")
    *   **STAR-CCM+ 15.04.010** -> **17.06.008 (toutes les versions)**
        *   `module load StdEnv/2020` (retiré)
        *   `module load starccm-mixed/17.06.008` **OU** `starccm/17.06.008-R8`
        *   `starccm+`   (options, "Serial")
        *   `starccm+ -np 2`   (options, "Parallel on Local Host")

### JupyterLab

1.  Démarrez une session JupyterHub Desktop en cliquant sur l'un des liens JupyterHub suivants :
    *   FIR : `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL : `https://portail.narval.calculquebec.ca/`
    *   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
2.  Cliquez sur l'icône d'engrenage des modules logiciels située en bas du menu de sélection vertical le plus à gauche.
3.  Sélectionnez un module StarCCM tel que `starccm-mixed/20.06.010` **OU** `starccm/20.06.010-R8` et cliquez sur *Load*.
4.  Sélectionnez `StarCCM+ Mixed (VNC)` **OU** Icône StarCCM (VNC) apparaissant sur le bureau.
5.  Pour exécuter StarCCM+ avec plusieurs cœurs :
    *   Cliquez sur *File->New*. Le panneau de configuration *Create a File* devrait apparaître.
    *   Modifiez *Serial Process Option* en cliquant sur le bouton **Parallel on Local Host**.
    *   Ajoutez `-mpi openmpi40` à la fin de la chaîne **Command** située dans le bas du panneau.
    *   Enfin, cliquez sur le bouton **OK**. L’interface graphique de StarCCM+ devrait s’afficher.

### VncViewer

Les instructions suivantes sont valides pour les anciens systèmes.

1.  [Connectez-vous à un nœud de connexion ou un nœud de calcul avec TigerVNC](../interactive/vnc.md).
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez une des commandes suivantes :
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.06.010` **OU** `starccm/20.06.010-R8`
        *   `starccm+ -rr server` **OU** `starccm+ -rr server -np 2 -mpi openmpi40`
    *   **STAR-CCM+ 15.04.010** -> **17.06.008 (toutes les versions)**
        *   `module load StdEnv/2020` (retiré)
        *   `module load starccm-mixed/17.06.008` **OU** `starccm/17.06.008-R8`
        *   `starccm+`