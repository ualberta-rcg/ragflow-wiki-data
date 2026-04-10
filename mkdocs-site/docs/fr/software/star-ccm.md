---
title: "Star-CCM+/fr"
slug: "star-ccm"
lang: "fr"

source_wiki_title: "Star-CCM+/fr"
source_hash: "93552744a0dd69b54ca99a596f1f4aac"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:26:38.660679+00:00"

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

[STAR-CCM+](https://mdx.plm.automation.siemens.com/star-ccm-plus) est une suite logicielle de simulation utilisée dans plusieurs spécialités de génie. Elle permet la modélisation dans des domaines variés dont l'acoustique, la dynamique des fluides, le transfert thermique, la rhéologie, l'écoulement polyphasique, le flux de particules, la mécanique des solides, les fluides réactifs, l'électrochimie et l'électromagnétisme.

!!! attention "Limites de la licence"
    Les binaires STAR-CCM+ sont installés sur nos serveurs, mais nous n'avons pas de licence d'utilisation générale; vous devez donc posséder votre propre licence.

    Vous pouvez acheter une licence POD (*Power On Demand*) directement de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/). Autrement, vous pouvez utiliser une licence locale hébergée par votre établissement pourvu que le pare-feu permette à la grappe où les tâches seront exécutées d'y accéder.

## Configurer votre compte
Afin de configurer votre compte pour utiliser un serveur de licence avec le module Star-CCM+, créez le fichier `~/.licenses/starccm.lic` comme suit :
```text title="starccm.lic"
SERVER <server> ANY <port>
USE_SERVER
```
où `server` et `port` sont remplacés respectivement par le nom d'hôte (ou l'adresse IP) et le port statique du fournisseur du serveur de licence. Il n'est pas nécessaire de définir manuellement `CDLMD_LICENSE_FILE` comme étant égal à `<port>@<server>` dans votre script Slurm; au lieu de cela, lorsqu'un module Star-CCM+ est chargé, cette variable est automatiquement spécifiée dans votre fichier *~/.licenses/starccm.lic*.

### Fichier pour une licence POD

Si vous avez acheté une licence POD de [Siemens](https://www.plm.automation.siemens.com/global/en/buy/), votre variable d'environnement `LM_PROJECT` doit être manuellement configurée comme étant égale à *YOUR CD-ADAPCO PROJECT ID* dans votre script Slurm. De plus, le fichier `~/.licenses/starccm.lic` doit être configuré comme suit sur toutes les grappes.
```text title="starccm.lic"
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

## Soumettre des tâches en lot sur nos grappes

!!! important
    Quand vous soumettez des tâches sur une grappe pour la première fois, vous devrez configurer votre environnement pour l’utilisation de votre licence. Si vous utilisez le serveur de licences distant *pay-on-usage* de Siemens, créez le fichier `~/.licenses/starccm.lic` comme décrit ci-dessus dans *Fichier pour une licence POD*; ceci devrait fonctionner immédiatement. Par contre, si vous utilisez un serveur de licence de votre établissement, créez d'abord le fichier `~/.licenses/starccm.lic` et soumettez une demande d'assistance au [soutien technique](technical-support.md). Nous vous aiderons à coordonner les modifications du pare-feu réseau nécessaires pour y accéder (en supposant que le serveur n'a jamais été configuré pour communiquer via la grappe de l'Alliance que vous voulez utiliser). Si vous rencontrez toujours des problèmes pour faire fonctionner la licence, essayez de supprimer ou de renommer le fichier `~/.flexlmrc` car les chemins de recherche et/ou les paramètres précédents du serveur de licence pourraient y être stockés. Notez que des fichiers de sortie de tâches déjà exécutées peuvent s'accumuler dans des répertoires cachés nommés `.star-version_number` et consommer ainsi votre quota. Ceux-ci peuvent être supprimés périodiquement en exécutant `rm -ri ~/.starccm*` et en répondant *oui* à l'affichage de l'invite.

## Scripts pour l'ordonnanceur

:::: tabs
::: tab title="Nibi"
```bash title="starccm_job-nibi-nogpu.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez un compte
#SBATCH --time=00-01:00       # Limite de temps : jj-hh:mm
#SBATCH --nodes=1             # Spécifiez 1 ou plus de nœuds
#SBATCH --cpus-per-task=16    # Spécifiez le nombre de cœurs par nœud (192 max.)
#SBATCH --mem=64G             # Spécifiez la mémoire par nœud (0 max.)
#SBATCH --ntasks-per-node=1   # Ne modifiez pas cette valeur
#SBATCH --constraint=granite  # Utilisez les nœuds de calcul Intel (sans GPU)
#SBATCH --switches=1          # Utilisez 1 commutateur réseau (facultatif)

module load StdEnv/2023

#module load starccm/20.04.007-R8    # Spécifiez 18.04.009, 18.06.007, 19.04.009,
module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 ou plus récent
module list

SIM_FILE='mysample.sim'       # Spécifiez le nom de votre fichier d'entrée sim
#JAVA_FILE='mymacros.java'    # Décommentez pour spécifier un nom de fichier Java d'entrée

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
   echo "Serveur de licences Siemens PoD..."
   starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
else
   echo "Serveur de licences institutionnel..."
   [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
   starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
fi
```
:::
::: tab title="Fir/Narval/Rorqual"
```bash title="starccm_job-fnr-nogpu.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez un compte
#SBATCH --time=00-01:00       # Limite de temps : jj-hh:mm
#SBATCH --nodes=1             # Spécifiez 1 ou plus de nœuds
#SBATCH --cpus-per-task=16    # Spécifiez le nombre de cœurs par nœud (192 max.)
#SBATCH --mem=64G             # Spécifiez la mémoire par nœud (0 max.)
#SBATCH --ntasks-per-node=1   # Ne modifiez pas cette valeur
##SBATCH --constraint=genoa   # Décommentez sur Rorqual (facultatif)

module load StdEnv/2023

#module load starccm/20.04.007-R8    # Spécifiez 18.04.009, 18.06.007, 19.04.009,
module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 ou plus récent
module list

SIM_FILE='mysample.sim'       # Spécifiez le nom de votre fichier d'entrée sim
#JAVA_FILE='mymacros.java'    # Décommentez pour spécifier un nom de fichier Java d'entrée

# Commentez la ligne suivante si vous utilisez un serveur de licences institutionnel
LM_PROJECT='my22digitpodkey'  # Spécifiez votre clé Siemens Power on Demand (PoD)

# ------- aucune modification requise en dessous de cette ligne --------

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
   echo "Serveur de licences Siemens PoD..."
   starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
else
   echo "Serveur de licences institutionnel..."
   [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
   starccm+ -jvmargs -Xmx4G -jvmargs -Djava.io.tmpdir=$SLURM_TMPDIR -batch -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_FABRIC
fi
```
:::
::: tab title="Trillium"
```bash title="starccm_job-trillium-nogpu.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez un compte
#SBATCH --time=00-01:00       # Limite de temps : jj-hh:mm
#SBATCH --nodes=1             # Spécifiez 1 ou plus de nœuds
#SBATCH --cpus-per-task=192   # Spécifiez le nombre de cœurs par nœud (192 max.)
#SBATCH --mem=0               # Spécifiez la mémoire par nœud (0 max.)
#SBATCH --ntasks-per-node=1   # Ne modifiez pas cette valeur
```
:::
::: tab title="Niagara"
```bash title="starccm_job.sh"
#!/bin/bash

module load StdEnv/2023

#module load starccm/20.04.007-R8    # Spécifiez 18.04.009, 18.06.007, 19.04.009,
module load starccm-mixed/20.04.007  # 19.06.009, 20.02.008, 20.04.007 ou plus récent
module list

SIM_FILE='mysample.sim'       # Spécifiez le nom du fichier d'entrée sim
#JAVA_FILE='mymacros.java'    # Décommentez pour spécifier un nom de fichier Java d'entrée

# Commentez la ligne suivante si vous utilisez un serveur de licences institutionnel
LM_PROJECT='my22digitpodkey'  # Spécifiez votre clé Siemens Power on Demand (PoD)

# Ces paramètres sont utilisés à la place de votre ~/.licenses/starccm.lic
# (les paramètres affichés utiliseront le serveur de licences cd-adapco PoD)
FLEXPORT=1999                    # Spécifiez le port statique flex du serveur
VENDPORT=2099                    # Spécifiez le port statique du vendeur du serveur
LICSERVER=flex.cd-adapco.com     # Spécifiez le nom d'hôte du serveur de licences

# ------- aucune modification requise en dessous de cette ligne --------

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
 
# Solution de contournement pour les échecs de licence : 
# Tant que le statut de sortie n'est pas 0, nous essayons de démarrer Star-CCM+ (ici, pour au moins 5 fois).
i=1
RET=-1
while [ $i -le 5 ] && [ $RET -ne 0 ]; do
        [ $i -eq 1 ] || sleep 5
          echo "Tentative numéro : "$i
          if [ -n "$LM_PROJECT" ]; then
          echo "Serveur de licences Siemens PoD..."
          starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
        else
          echo "Serveur de licences institutionnel..."
          starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
        fi
        RET=$?
        i=$((i+1))
done
exit $RET
```
:::
::::

## Mode graphique

Pour travailler en mode graphique, nous recommandons d'utiliser un système [OnDemand](nibi.md#accès-via-open-ondemand-ood) ou JupyterLab pour démarrer un bureau distant. En plus de configurer `~/.licenses/starccm.lic`, les groupes qui possèdent une licence POD devraient aussi exécuter `export LM_PROJECT='CD-ADAPCO PROJECT ID'` avant `starccm+`, comme dans les exemples ci-dessous; selon le type de licence, il faut aussi ajouter d'autres options comme **-power**. La commande `module avail starccm-mixed` affiche les versions de Star-CCM+ qui sont disponibles dans l'environnement standard (StdEnv) que vous avez chargé. Autrement, la commande `module spider starccm-mixed` affiche toutes les versions de modules qui sont disponibles dans toutes les versions de modules StdEnv.

### OnDemand
1.  Sur votre ordinateur, connectez-vous à un système OnDemand en saisissant l'une des adresses URL dans votre navigateur :
    *   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)) : `https://ondemand.sharcnet.ca`
    *   FIR : `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL : `https://portail.narval.calculquebec.ca/`
    *   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2.  Sur votre ordinateur, ouvrez une fenêtre de terminal avec l'une des commandes suivantes :
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
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez l'une des commandes suivantes :
    *   **STAR-CCM+ 18.04.008 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load starccm-mixed/20.04.007` **OU** `starccm/20.04.007-R8`
        *   `starccm+ -rr server`
    *   **STAR-CCM+ 15.04.010 --> 18.02.008 (plage de versions)**
        *   `module load StdEnv/2020` (non pris en charge)
        *   `module load starccm-mixed/17.02.007` **OU** `starccm/17.02.007-R8`
        *   `starccm+`