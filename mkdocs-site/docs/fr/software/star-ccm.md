---
title: "Star-CCM+/fr"
slug: "star-ccm"
lang: "fr"

source_wiki_title: "Star-CCM+/fr"
source_hash: "beaa7bc6708990cda09db4c5580498dd"
last_synced: "2026-08-07T19:46:17.777436+00:00"
last_processed: "2026-08-07T22:54:33.746939+00:00"

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

STAR-CCM+ est une suite logicielle de simulation utilisée dans plusieurs spécialités de génie. Elle permet la modélisation dans des domaines variés dont l'acoustique, la dynamique des fluides, le transfert thermique, la rhéologie, l'écoulement polyphasique, le flux de particules, la mécanique des solides, les fluides réactifs, l'électrochimie et l'électromagnétisme.

# Limites de la licence

Nous avons l'autorisation d'héberger les binaires STAR-CCM+ sur nos grappes. Pour utiliser le logiciel, vous devez acquérir une licence auprès de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/). [Deux options sont disponibles](https://community.sw.siemens.com/s/article/How-faculty-members-in-academic-institutions-can-get-access-to-Simcenter-STAR-CCM). La plupart des groupes de recherche opteront pour une [licence Power-on-Demand (PoD)](https://community.sw.siemens.com/s/question/0D54O00006FKu39SAD/licensing-how-power-on-demand-pod-licensing-for-starccm-works), qui se connecte simplement à un serveur de licence distant et ne nécessite qu'une clé de licence. La seconde option est plus complexe et nécessite la configuration et la gestion d'un serveur de licence institutionnel hébergé localement, ainsi que l'achat d'un pack académique Simcenter STAR-CCM+. Votre serveur de licence STAR-CCM+ devra être reconfiguré. Vous devez demander à l'administrateur du serveur de licence de votre établissement d'ouvrir les **deux** ports fournisseurs (flexible et statique) pour qu'ils puissent être rejoints à partir des nœuds NAT (*Network Address Translation*) des grappes que vous voulez utiliser. Pour obtenir la liste des nœuds NAT à fournir à votre administrateur, écrivez au [soutien technique](../support/technical_support.md) en indiquant 1) le nom de la ou des grappes 2) le nom de l'hôte (FQDN) ou l'adresse IP publique du serveur de licence STAR-CCM+ et les numéros des ports flexible et statique.

## Configurer votre compte

Afin de configurer votre compte pour utiliser un serveur de licence avec le module Star-CCM+, créez le fichier `$HOME/.licenses/starccm.lic` comme suit&nbsp;:
```
starccm.lic
SERVER <server> ANY <flexport>
USE_SERVER
```
où `server` et `flexport` sont remplacés respectivement par le nom de l'hôte (ou l'adresse IP) et le port statique du fournisseur du serveur de licence. Il n'est pas nécessaire de définir manuellement `CDLMD_LICENSE_FILE` comme étant égal à `<port>@<server>` dans votre script slurm puisque cette variable est automatiquement configurée quand un module Star-CCM+ est chargé.

### Fichier pour une licence PoD

Si vous avez acheté une licence POD, votre variable d'environnement `LM_PROJECT` doit être manuellement configurée comme étant égale à *YOUR CD-ADAPCO PROJECT ID* dans votre script slurm. De plus, le fichier `~/.licenses/starccm.lic` doit être configuré comme suit sur toutes les grappes.
```
starccm.lic
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

# Soumettre des tâches en lot sur nos grappes

Avant de soumettre des tâches sur une grappe, vous devez configurer un fichier `~/.licenses/starccm.lic` sur chaque grappe où vous exécuterez des tâches. Si vous disposez d'une licence PoD, les modifications de pare-feu requises ont déjà été effectuées sur toutes nos grappes. Cependant, si vous utilisez un serveur de licence institutionnel local, vous devrez soumettre une [demande d'assistance au soutien technique](../support/technical_support.md) pour demander la modification ponctuelle du pare-feu réseau entre la ou les grappes et votre serveur de licence local. Si vous rencontrez toujours des problèmes pour faire fonctionner la licence, essayez de supprimer ou de renommer le fichier `~/.flexlmrc` car les chemins de recherche et/ou les paramètres précédents du serveur de licence pourraient y être stockés. Notez que des fichiers de sortie de tâches déjà exécutées peuvent s'accumuler dans des répertoires cachés nommés `.star-version_number` et consommer ainsi votre quota. Ceux-ci peuvent être supprimés en exécutant périodiquement `rm -ri ~/.starccm*` et en répondant *oui* à l'affichage de l'invite.

## Scripts pour l'ordonnanceur

=== "Nibi"

    ```bash title="starccm_job-nibi-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Spécifiez un compte
    #SBATCH --time=00-01:00       # Limite de temps: jj-hh:mm
    #SBATCH --nodes=1             # Spécifiez 1 nœud ou plus
    #SBATCH --cpus-per-task=16    # Spécifiez les cœurs par nœud (192 max)
    #SBATCH --mem=64G             # Spécifiez la mémoire par nœud (0 max)
    #SBATCH --ntasks-per-node=1   # Ne pas changer cette valeur
    #SBATCH --constraint=granite  # Utiliser uniquement les nœuds de base CPU Intel
    #SBATCH --switches=1          # Utiliser 1 commutateur réseau (optionnel)

    module load StdEnv/2023

    #module load starccm/21.02.008-R8
    module load starccm-mixed/21.02.008
    module list

    SIM_FILE='mySample.sim'        # Spécifiez votre nom de fichier d'entrée sim
    #BATCH_CMD='myMacro.java,run'  # Décommentez pour spécifier les macros java, maillage, exécution, étape

    # Commentez la ligne suivante si vous utilisez un serveur de licence institutionnel local
    LM_PROJECT='22digit-PoD-License-Key'  # Spécifiez votre clé PoD Siemens ici

    # ------- aucune modification requise en dessous de cette ligne --------

    # Rediriger de ~/.star-VERSION# vers $SLURM_TMPDIR
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
       echo "Serveur de licence Siemens PoD ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
    else
       echo "Serveur de licence institutionnel ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
    fi
    ```

=== "Fir/Narval/Rorqual"

    ```bash title="starccm_job-fnr-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Spécifiez un compte
    #SBATCH --time=00-01:00       # Limite de temps: jj-hh:mm
    #SBATCH --nodes=1             # Spécifiez 1 nœud ou plus
    #SBATCH --cpus-per-task=16    # Spécifiez les cœurs par nœud (192 max)
    #SBATCH --mem=64G             # Spécifiez la mémoire par nœud (0 max)
    #SBATCH --ntasks-per-node=1   # Ne pas changer cette valeur

    module load StdEnv/2023

    #module load starccm/21.02.008-R8
    module load starccm-mixed/21.02.008
    module list

    SIM_FILE='mySample.sim'        # Spécifiez votre nom de fichier d'entrée sim
    #BATCH_CMD='myMacro.java,run'  # Décommentez pour spécifier les macros java, maillage, exécution, étape

    # Commentez la ligne suivante si vous utilisez un serveur de licence institutionnel
    LM_PROJECT='22digit-PoD-License-Key'  # Spécifiez votre clé PoD Siemens ici

    # ------- aucune modification requise en dessous de cette ligne --------

    # Rediriger de ~/.star-VERSION# vers $SLURM_TMPDIR
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
       echo "Serveur de licence Siemens PoD ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
    else
       echo "Serveur de licence institutionnel ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
    fi
    ```

=== "Trillium"

    ```bash title="starccm_job-trillium-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Spécifiez un compte
    #SBATCH --time=00-01:00       # Limite de temps: jj-hh:mm
    #SBATCH --nodes=1             # Spécifiez 1 nœud ou plus
    #SBATCH --cpus-per-task=192   # Spécifiez les cœurs par nœud (192 max)
    #SBATCH --mem=0               # Spécifiez la mémoire par nœud (0 max)
    #SBATCH --ntasks-per-node=1   # Ne pas changer cette valeur
    #SBATCH --output=slurm-%j.out # Écrit dans slurm-$SLURM_JOB_ID.out

    ```

=== "Niagara"

    ```bash title="starccm_job.sh"
    #!/bin/bash

    module load StdEnv/2023

    #module load starccm/21.02.008-R8
    module load starccm-mixed/21.02.008
    module list

    SIM_FILE='mySample.sim'        # Spécifiez votre nom de fichier d'entrée sim
    #BATCH_CMD='myMacro.java,run'  # Décommentez pour spécifier les macros java, maillage, exécution, étape

    # Commentez la ligne suivante si vous utilisez un serveur de licence institutionnel
    LM_PROJECT='22digit-PoD-License-Key'  # Spécifiez votre clé PoD Siemens ici

    # Ces paramètres sont utilisés à la place de votre ~/.licenses/starccm.lic
    # (les paramètres affichés utiliseront le serveur de licence PoD cd-adapco)
    FLEXPORT=1999                    # Spécifiez le port flex statique du serveur
    VENDPORT=2099                    # Spécifiez le port vendor statique du serveur
    LICSERVER=flex.cd-adapco.com     # Spécifiez le nom d'hôte du serveur de licence

    # ------- aucune modification requise en dessous de cette ligne --------

    # Rediriger de ~/.star-VERSION# vers $SLURM_TMPDIR
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

    # Solution de contournement pour les échecs de licence :
    # tant que le statut de sortie n'est pas égal à 0, nous essayons de démarrer Star-CCM+ (ici, pendant au moins 5 fois).
    i=1
    RET=-1
    while [ $i -le 5 ] && [ $RET -ne 0 ]; do
            [ $i -eq 1 ] || sleep 5
              echo "Tentative numéro : "$i
              if [ -n "$LM_PROJECT" ]; then
              echo "Serveur de licence Siemens PoD ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            else
              echo "Serveur de licence institutionnel ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            fi
            RET=$?
            i=$((i+1))
    done
    exit $RET
    ```

# Mode graphique

Pour travailler en mode graphique, nous recommandons d'utiliser un système [OnDemand](../clusters/nibi.md) ou JupyterLab pour démarrer un bureau distant. En plus de configurer `~/.licenses/starccm.lic`, les groupes qui possèdent une licence PoD devraient aussi exécuter `export LM_PROJECT='22digit-PoD-License-Key'` avant `starccm+`, comme dans les exemples ci-dessous; selon le type de licence, il faut aussi ajouter d'autres options comme **-power**. La commande `module avail starccm-mixed` affiche les versions de starccm qui peuvent être chargées dans l'environnement standard (StdEnv) qui est en place (2020 ou 2023). Autrement, la commande `module spider starccm-mixed` affiche toutes les versions *mixed* et *R8* des modules qui peuvent être chargés dans les deux versions des modules d'environnement variable qui peuvent être utilisées (2020 ou 2023).

## OnDemand

1.  Pour démarrer une session de bureau OnDemand, cliquez sur l'un des liens OnDemand suivants&nbsp;:<br>
    [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    TRILLIUM: `https://ondemand.scinet.utoronto.ca`
    *   `module load starccm-mixed/20.06.010` **OU** `starccm/21.02.008-R8`
    *   `starccm+ -rr server` &emsp; (options, "Serial")
    *   `starccm+ -rr server -np 2 -mpi openmpi40` &emsp; (options, "Parallel on Local Host")
    **STAR-CCM+ 15.04.010** &rarr; **17.06.008 (toutes les versions)**
    *   `module load StdEnv/2020` (retiré)
    *   `module load starccm-mixed/21.02.008` **OU** `starccm/17.06.008-R8`
    *   `starccm+` &emsp; (options, "Serial")
    *   `starccm+ -np 2` &emsp; (options, "Parallel on Local Host")

## JupyterLab

1.  Démarrez une session JupyterHub Desktop en cliquant sur l'un des liens JupyterHub suivants :<br>
    FIR : `https://jupyterhub.fir.alliancecan.ca`
    NARVAL : `https://portail.narval.calculquebec.ca/`
    RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`<br>
2.  Cliquez sur l'icône d'engrenage des modules logiciels située en bas du menu de sélection vertical le plus à gauche.<br>
3.  Sélectionnez un module StarCCM tel que `starccm-mixed/21.02.008` **OU** `starccm/21.02.008-R8` et cliquez sur *Charger*.<br>
4.  Sélectionnez `StarCCM+ Mixed (VNC)` **OU** Icône StarCCM (VNC) apparaissant sur le bureau.<br>
5.  Pour exécuter StarCCM+ avec plusieurs cœurs&nbsp;:
    *   Cliquez sur *Fichier->Nouveau*. Le panneau de configuration *Créer un fichier* devrait apparaître.
    *   Modifiez *Option de processus séquentiel* en cliquant sur le bouton **Parallèle sur l'hôte local**.
    *   Ajoutez `-mpi openmpi40` à la fin de la chaîne **Commande** située dans le bas du panneau.
    *   Enfin, cliquez sur le bouton **OK**. L’interface graphique de StarCCM+ devrait s’afficher.

## VncViewer

Les instructions suivantes sont valides pour les anciens systèmes.

1.  [Connectez-vous à un nœud de connexion ou un nœud de calcul avec TigerVNC](../interactive/vnc.md).<br>
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez une des commandes suivantes&nbsp;:
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.06.010` **OU** `starccm/20.06.010-R8`
        *   `module load starccm-mixed/21.02.008` **OU** `starccm/21.02.008-R8`
    *   **STAR-CCM+ 15.04.010** &rarr; **17.06.008 (toutes les versions)**
        *   `module load StdEnv/2020` (retiré)
        *   `module load starccm-mixed/17.06.008` **OU** `starccm/17.06.008-R8`
        *   `starccm+`