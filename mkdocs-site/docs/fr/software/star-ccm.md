---
title: "Star-CCM+/fr"
slug: "star-ccm"
lang: "fr"

source_wiki_title: "Star-CCM+/fr"
source_hash: "93552744a0dd69b54ca99a596f1f4aac"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:36:41.598410+00:00"

tags:
  - software

keywords:
  - "répertoires cachés"
  - "SBATCH"
  - "TigerVNC"
  - "supprimer périodiquement"
  - "Siemens PoD Key"
  - "serveur de licence"
  - "memory per node"
  - "logiciel de simulation"
  - "Slurm"
  - "licence"
  - "fichiers de sortie"
  - "nœud de calcul"
  - "Scripts pour l'ordonnanceur"
  - "Mode graphique"
  - "TRILLIUM"
  - "ntasks-per-node"
  - "module load"
  - "starccm"
  - "license server"
  - "Fir/Narval/Rorqual"
  - "LICSERVER"
  - "commandes"
  - "Siemens Power on Demand"
  - "VncViewer"
  - "FLEXPORT"
  - "fenêtre de terminal"
  - "quota"
  - "SLURM"
  - "MPI"
  - "STAR-CCM+"
  - "Nibi"
  - "OnDemand"
  - "starccm.lic"
  - "licence POD"
  - "soumission de tâches"
  - "Job submission"

questions:
  - "Qu'est-ce que la suite logicielle STAR-CCM+ et dans quels domaines de l'ingénierie permet-elle de faire de la modélisation ?"
  - "Quelles sont les différentes options de licence disponibles pour les utilisateurs et comment doivent-ils configurer leur compte pour les utiliser ?"
  - "Quelles sont les étapes de dépannage et d'entretien recommandées lors de la soumission de tâches en lot, notamment pour la gestion des licences et de l'espace disque ?"
  - "Quels types d'informations ou de paramètres liés au serveur de licence peuvent être stockés dans ces emplacements ?"
  - "Comment l'accumulation des fichiers de sortie dans les répertoires cachés affecte-t-elle le quota de l'utilisateur ?"
  - "Quelle commande spécifique doit être exécutée pour supprimer les fichiers obsolètes et comment faut-il répondre à l'invite ?"
  - "Quels sont les paramètres de configuration Slurm recommandés pour allouer les ressources à une tâche STAR-CCM+ ?"
  - "Quels modules d'environnement doivent être chargés pour utiliser le logiciel STAR-CCM+ sur les grappes de calcul ?"
  - "Comment le script différencie-t-il l'exécution du programme selon le type de serveur de licence (institutionnel ou Siemens PoD) ?"
  - "What memory and task configurations are specified for the nodes in this script?"
  - "Which software modules and specific versions are being loaded into the environment?"
  - "What optional constraint is mentioned for users running jobs on the rorqual cluster?"
  - "How does the script specify the input simulation and Java macro files for the STAR-CCM+ job?"
  - "What is the difference in the script's execution when using a Siemens Power on Demand (PoD) key versus an institutional license server?"
  - "How does the script dynamically adjust the MPI and FLEXIBLAS environment variables based on the CPU vendor?"
  - "Comment le script fourni gère-t-il les échecs de connexion au serveur de licence lors du lancement de STAR-CCM+ ?"
  - "Quelles configurations spécifiques (fichiers et variables d'environnement) sont nécessaires pour utiliser une licence POD en mode graphique ?"
  - "Quelles sont les étapes pour démarrer une session graphique STAR-CCM+ via Open OnDemand sur les différentes grappes de calcul ?"
  - "What environment variable is used to specify the Siemens Power on Demand (PoD) Key?"
  - "Which default license file is bypassed when these server settings are applied?"
  - "What are the specific port numbers and hostname required to connect to the cd-adapco pod license server?"
  - "Quelle est l'URL fournie pour accéder au système TRILLIUM ?"
  - "Quelles commandes de chargement de modules doivent être exécutées pour configurer l'environnement STAR-CCM+ ?"
  - "Quelle est la commande finale à utiliser dans le terminal pour démarrer le serveur STAR-CCM+ ?"
  - "Quels modules d'environnement doivent être chargés pour utiliser les versions de STAR-CCM+ antérieures et postérieures à la version 18.04.008 ?"
  - "Quelles sont les étapes préalables à suivre pour se connecter et préparer l'environnement graphique via VncViewer ou TigerVNC ?"
  - "Quelles options de ligne de commande (telles que \"-mesa\" ou \"-rr server\") doivent être spécifiées lors du lancement de STAR-CCM+ selon la plage de versions choisie ?"
  - "Quels modules d'environnement doivent être chargés pour utiliser les versions de STAR-CCM+ antérieures et postérieures à la version 18.04.008 ?"
  - "Quelles sont les étapes préalables à suivre pour se connecter et préparer l'environnement graphique via VncViewer ou TigerVNC ?"
  - "Quelles options de ligne de commande (telles que \"-mesa\" ou \"-rr server\") doivent être spécifiées lors du lancement de STAR-CCM+ selon la plage de versions choisie ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

STAR-CCM+ est une suite logicielle de simulation utilisée dans plusieurs spécialités de génie. Elle permet la modélisation dans des domaines variés, dont l'acoustique, la dynamique des fluides, le transfert thermique, la rhéologie, l'écoulement polyphasique, le flux de particules, la mécanique des solides, les fluides réactifs, l'électrochimie et l'électromagnétisme.

## Limites des licences
Les binaires STAR-CCM+ sont installés sur nos serveurs, mais nous n'avons pas de licence pour utilisation générale; vous devez donc posséder votre propre licence.
Vous pouvez acheter une licence POD (*Power On Demand*) directement de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/). Autrement, vous pouvez utiliser une licence locale hébergée par votre établissement pourvu que le pare-feu permette à la grappe où les tâches seront exécutées d'y accéder.

## Configurer votre compte
Afin de configurer votre compte pour utiliser un serveur de licences avec le module Star-CCM+, créez le fichier `$HOME/.licenses/starccm.lic` comme suit :

```text title="starccm.lic"
SERVER <server> ANY <port>
USE_SERVER
```

où `server` et `port` sont remplacés respectivement par le nom de l'hôte (ou l'adresse IP) et le port statique du fournisseur du serveur de licences. Il n'est pas nécessaire de définir manuellement `CDLMD_LICENSE_FILE` comme étant égal à `<port>@<server>` dans votre script Slurm; au lieu de cela, lorsqu'un module Star-CCM+ est chargé, cette variable est automatiquement spécifiée dans votre fichier *`$HOME/.licenses/starccm.lic`*.

### Fichier pour une licence POD
Si vous avez acheté une licence POD de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/), votre variable d'environnement `LM_PROJECT` doit être manuellement configurée comme étant égale à *VOTRE ID DE PROJET CD-ADAPCO* dans votre script Slurm. De plus, le fichier `~/.licenses/starccm.lic` doit être configuré comme suit sur toutes les grappes.

```text title="starccm.lic"
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

## Soumettre des tâches en lot sur nos grappes
Quand vous soumettez des tâches sur une grappe pour la première fois, vous devrez configurer votre environnement pour l’utilisation de votre licence. Si vous utilisez le serveur de licences distant à *paiement à l'usage* de Siemens, créez le fichier `~/.licenses/starccm.lic` comme décrit ci-dessus dans *Fichier pour une licence POD*; ceci devrait fonctionner immédiatement. Par contre, si vous utilisez un serveur de licences de votre établissement, créez d'abord le fichier `~/.licenses/starccm.lic` et soumettez une demande d'assistance au [soutien technique](technical-support.md). Nous vous aiderons à coordonner les modifications du pare-feu réseau nécessaires pour y accéder (en supposant que le serveur n'a jamais été configuré pour communiquer via la grappe de l'Alliance que vous voulez utiliser). Si vous rencontrez toujours des problèmes pour faire fonctionner la licence, essayez de supprimer ou de renommer le fichier `~/.flexlmrc` car les chemins de recherche et/ou les paramètres précédents du serveur de licences pourraient y être stockés.

!!! warning "Attention"
    Notez que des fichiers de sortie de tâches déjà exécutées peuvent s'accumuler dans des répertoires cachés nommés `.star-version_number` et consommer ainsi votre quota. Ceux-ci peuvent être supprimés périodiquement en exécutant `rm -ri ~/.starccm*` et en répondant *oui* à l'invite.

## Scripts pour l'ordonnanceur

=== "Nibi" title="starccm_job-nibi-nogpu.sh"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    #SBATCH --constraint=granite  # Use intel compute nodes (no gpu)
    #SBATCH --switches=1          # Use 1 network switch (optional)

    module load StdEnv/2023

    #module load starccm/20.04.007-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mysample.sim'       # Specify your input sim filename
    #JAVA_FILE='mymacros.java'    # Uncomment to specify an input java filename

    export STARCCM_TMP="${SCRATCH}/.starccm-${EBVERSIONSTARCCM}"
    mkdir -p "$STARCCM_TMP"

    slurm_hl2hl.py --format STAR-CCM+ > machinefile-$SLURM_JOB_ID

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    NCORE=$((SLURM_NTASKS * SLURM_CPUS_PER_TASK))

    export FLEXIBLAS=StarMKL
    echo "FLEXIBLAS=$FLEXIBLAS"
    STAR_MPI="-mpi intel"
    STAR_FABRIC="-fabric tcp"

    if [ -n "$LM_PROJECT" ]; then
       echo "Serveur de licences Siemens PoD ..."
       starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
    else
       echo "Serveur de licences institutionnel ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
    fi
    ```

=== "Fir/Narval/Rorqual" title="starccm_job-fnr-nogpu.sh"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    ##SBATCH --constraint=genoa   # Uncomment on rorqual (optional)

    module load StdEnv/2023

    #module load starccm/20.04.007-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mysample.sim'       # Specify your input sim filename
    #JAVA_FILE='mymacros.java'    # Uncomment to specify an input java filename

    # Comment the next line when using an institutional license server
    LM_PROJECT='my22digitpodkey'  # Specify your Siemens Power on Demand (PoD) Key

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Vérification de $CDLMD_LICENSE_FILE ..."
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
       echo "Serveur de licences Siemens PoD ..."
       starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
    else
       echo "Serveur de licences institutionnel ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
    fi
    ```

=== "Trillium" title="starccm_job-trillium-nogpu.sh"

    ```bash
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=192   # Specify cores per node (192 max)
    #SBATCH --mem=0               # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    ```

=== "Niagara" title="starccm_job.sh"

    ```bash
    #!/bin/bash

    module load StdEnv/2023

    #module load starccm/20.04.007-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mysample.sim'       # Specify input sim filename
    #JAVA_FILE='mymacros.java'    # Uncomment to specify an input java filename

    # Comment the next line when using an institutional license server
    LM_PROJECT='my22digitpodkey'  # Specify your Siemens Power on Demand (PoD) Key

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
              echo "Tentative numéro : "$i
              if [ -n "$LM_PROJECT" ]; then
              echo "Serveur de licences Siemens PoD ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            else
              echo "Serveur de licences institutionnel ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            fi
            RET=$?
            i=$((i+1))
    done
    exit $RET
    ```

## Mode graphique
Pour travailler en mode graphique, nous recommandons d'utiliser un système [OnDemand](nibi.md#accès-via-open-ondemand-ood) ou JupyterLab pour démarrer un bureau distant. En plus de configurer `~/.licenses/starccm.lic`, les groupes qui possèdent une licence POD devraient aussi exécuter `export LM_PROJECT='ID DE PROJET CD-ADAPCO'` avant `starccm+`, comme dans les exemples ci-dessous; selon le type de licence, il faut aussi ajouter d'autres options comme **-power**. La commande `module avail starccm-mixed` affiche les versions de Star-CCM+ qui sont disponibles dans l'environnement standard (StdEnv) que vous avez chargé. Autrement, la commande `module spider starccm-mixed` affiche toutes les versions de modules qui sont disponibles dans toutes les versions de modules StdEnv.

### OnDemand
1.  Sur votre ordinateur, connectez-vous à un système OnDemand en entrant une des adresses URL dans le navigateur :
    *   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Sur votre ordinateur, ouvrez une fenêtre de terminal avec une des commandes suivantes :
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.04.007` **OU** `starccm/20.04.007-R8`
        *   `starccm+ -rr server`
    *   **STAR-CCM+ 15.04.010 --> 18.02.008 (plages de versions)**
        *   `module load StdEnv/2020` (non pris en charge)
        *   `module load starccm-mixed/15.04.010` **OU** `starccm/15.04.010-R8`
        *   `starccm+ -mesa`

### VncViewer
1.  [Connectez-vous à un nœud de connexion ou un nœud de calcul avec TigerVNC](vnc.md).
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez une des commandes suivantes :
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.04.007` **OU** `starccm/20.04.007-R8`
        *   `starccm+ -rr server`
    *   **STAR-CCM+ 15.04.010 --> 18.02.008 (plage de versions)**
        *   `module load StdEnv/2020` (non pris en charge)
        *   `module load starccm-mixed/17.02.007` **OU** `starccm/17.02.007-R8`
        *   `starccm+`