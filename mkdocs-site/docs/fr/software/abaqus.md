---
title: "Abaqus/fr"
slug: "abaqus"
lang: "fr"

source_wiki_title: "Abaqus/fr"
source_hash: "e4f6cbbe5416d52b2e9683f951040d27"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:30:37.122964+00:00"

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

[Abaqus FEA](https://www.3ds.com/products-services/simulia/products/abaqus/) est un progiciel commercial pour l'analyse d'éléments finis et l'ingénierie assistée par ordinateur.

# Licence

Les modules logiciels Abaqus sont disponibles sur les grappes de l'Alliance. Toutefois, vous devez fournir votre propre licence. Il existe deux types de serveurs de licences, chacun ayant des procédures de configuration différentes décrites ci-dessous.

## Utiliser votre licence

Des modules Abaqus sont disponibles sur nos grappes, mais vous devez posséder votre propre licence. Pour configurer votre compte sur les grappes que vous voulez utiliser, connectez-vous et créez sur chacune un fichier `$HOME/.licenses/abaqus.lic` qui contient la ligne ci-dessous. Remplacez ensuite `port@server` par le numéro du port FlexLM et l'adresse IP (ou le nom complet du domaine) de votre serveur de licence Abaqus. Si vous voulez utiliser la version 6.14.1, remplacez ABAQUSLM_LICENSE_FILE par LM_LICENSE_FILE.

```text title="abaqus.lic"
prepend_path("ABAQUSLM_LICENSE_FILE","port@server")
```

```bash
[l2 (nœud de connexion):~/.licenses] cat abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","LMGRD-PORT-NUMBER@FLEXnet-SERVER-HOSTNAME")
```

```bash
rm -f testsp1* testsp2*
/cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testsp1 input=mystd-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
#  gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
```

## Serveurs FLEXnet et DSLS

Comme c'était le cas avec les modules déjà installés, `abaqus/2026` est configuré pour fonctionner avec le serveur de licence Simulia `FLEXnet` par défaut, tout comme le serveur de licence gratuit de SHARCNET. Pour utiliser un serveur de licence `DSLS` de votre établissement, vous devez créer les fichiers texte `abaqus_v6.env` et `DSLicSrv.txt` dans le répertoire utilisé pour soumettre votre simulation (voir le code ci-dessous). Ils seront lus automatiquement au lancement d'Abaqus et la reconfiguration se fera en conséquence.

```bash
[l2 (nœud de connexion):~ ] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="/home/<username>/DSLicSrv.txt"
```

```bash
[l2 (nœud de connexion):~ ] cat DSLicSrv.txt
DSLS-SERVER-HOSTNAME:LICENSING-CLIENT-PORT-NUMBER
```

```bash
[l2 (nœud de connexion):~/mysimdir] cat abaqus_v6.env
license_server_type=DSLS
dsls_license_config="DSLicSrv.txt"
```

```text
[l2 (nœud de connexion):~/mysimdir] DSLicSrv.txt
YOUR-SERVER-HOSTNAME:PORT-NUMBER
```

Si votre serveur de licences n'a jamais été configuré pour être utilisé sur une grappe de l'Alliance, des modifications de configuration supplémentaires devront être effectuées par l'administrateur système de l'Alliance et votre administrateur système local. Ces modifications sont nécessaires pour garantir que les ports TCP requis de votre serveur Abaqus sont accessibles depuis tous les nœuds de calcul de la grappe. Pour obtenir de l'aide, veuillez écrire au [soutien technique](../support/technical_support.md) et assurez-vous d'inclure les éléments suivants :

*   le numéro de port FlexLM et le numéro de port statique du fournisseur (serveur FLEXnet),
*   le numéro de port administratif et le numéro de port client de la licence (serveur DSLS),
*   le nom de domaine complet ou l'adresse IPV4 de votre nouveau serveur Abaqus.

Une liste d'adresses IP des grappes (connues sous le nom de nœuds NAT) vous sera envoyée afin que votre administrateur puisse ouvrir le pare-feu du serveur local pour permettre les connexions depuis la grappe sur les deux ports. Veuillez noter qu'une entente de licence spéciale doit généralement être négociée et signée par SIMULIA et votre institution avant qu'une licence campus ne puisse être légalement utilisée sur le matériel de l'Alliance situé à distance dans une autre institution.

## File d'attente de licences

La configuration par défaut du serveur de licences est de mettre en file d'attente les tâches démarrées sur la grappe par Slurm si le nombre de jetons est insuffisant. Il existe deux options pour modifier ce comportement, c'est-à-dire pour que les tâches ne restent pas inactives sur un nœud de calcul de la grappe en attendant indéfiniment une licence, gaspillant ainsi des ressources précieuses. La première option est de terminer une tâche immédiatement si le nombre de licences est insuffisant, ne la faisant ainsi jamais entrer dans une file d'attente. Pour spécifier ce paramètre, créez un fichier texte nommé `abaqus_v6.env` dans votre répertoire `/home` OU votre répertoire de travail (de soumission) contenant la ligne : `lmlicensequeuing=OFF`. La deuxième option consiste à spécifier un temps d'attente limité, par exemple 1 minute, pendant lequel la tâche peut entrer dans un état d'attente sur le serveur de licences en ajoutant la ligne : `lmhanglimit=1`. Si, dans un délai d'une minute, un nombre suffisant de licences n'est pas disponible, la tâche sera retirée de la file d'attente par le serveur de licences et sera à son tour terminée par Slurm. Pour chaque option, des messages seront imprimés à la fin du fichier de sortie Slurm, comme indiqué dans [l'exemple ci-dessous](#exemple).

# Compatibilité des versions

## Nouveau module

!!! warning "Nouveau module Abaqus/2026"
    Un nouveau module pour `abaqus/2026` est installé dans l'environnement par défaut `StdEnv/2023`. La nouvelle version résout la source de l'erreur **buffer overflow detected** qui survenait sur toutes les récentes grappes avec `abaqus/2021`. Les scripts Slurm présentés dans cette page ont été adaptés pour fonctionner avec `abaqus/2026` et `abaqus/2021` lorsque possible; vous devez donc modifier tous les scripts Slurm que vous utilisez. Le module `abaqus/2026` contient la version initiale *Abaqus 2026 Golden*. Un autre module nommé `abaqus/2026.2606` contient les mises à niveau *Abaqus 2026 FP.CFA.2606* et sera installé prochainement.

# Soumettre des tâches en lots

Vous trouverez ci-dessous des prototypes de scripts Slurm pour soumettre des simulations parallèles sur un ou plusieurs nœuds de calcul en utilisant des fils et MPI. Dans la plupart des cas, il suffira d'utiliser un des **scripts du répertoire /project** dans une des sections pour un nœud simple. Dans la dernière ligne des scripts, l'argument `memory=` est optionnel et sert aux tâches qui demandent beaucoup de mémoire ou qui posent problème; la valeur de déplacement de 3072 Mo pourrait nécessiter un ajustement. Pour obtenir la liste des arguments en ligne de commande, chargez un module Abaqus et lancez `abaqus -help | less`.

Pour une tâche sur un nœud simple d'une durée de moins de 24 heures, le *script du répertoire /project* sous le premier onglet devrait suffire. Pour une tâche de plus longue durée, utilisez un script de redémarrage.

Il est préférable que les tâches qui créent des fichiers de redémarrage volumineux écrivent sur le disque local via l'utilisation de la variable d'environnement `SLURM_TMPDIR` utilisée dans les **scripts de répertoire temporaire** sous les deux onglets les plus à droite des sections d'analyse standard et explicite à nœud unique. Les scripts de redémarrage présentés ici poursuivront les tâches qui ont été interrompues prématurément pour une quelconque raison. De telles interruptions peuvent se produire si une tâche atteint son temps d'exécution maximal demandé avant de se terminer et est arrêtée par la file d'attente ou si le nœud de calcul sur lequel la tâche était exécutée a planté en raison d'une défaillance matérielle inattendue. D'autres types de redémarrage sont possibles en modifiant davantage le fichier d'entrée (non illustré) pour continuer une tâche avec des étapes supplémentaires ou modifier l'analyse (consultez la documentation pour plus de détails sur la version).

Les tâches qui exigent beaucoup de mémoire ou beaucoup de ressources de calcul (plus que la capacité d'un nœud simple) devraient utiliser les scripts MPI dans les sections pour nœuds multiples afin de distribuer le calcul sur un ensemble de nœuds arbitraires déterminé automatiquement par l'ordonnanceur. Avant de lancer des tâches de longue durée, il est recommandé d'exécuter de courts tests présentant peu de scalabilité pour déterminer la durée réelle d'exécution (et les exigences en mémoire) en fonction du nombre optimal de cœurs (2, 4, 8, etc.).

## Analyse standard

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des scripts pour redémarrer une tâche qui utilise des nœuds multiples ne sont pas illustrés pour l'instant.

### Scripts pour un nœud simple

:::: tabs
::: tab "script pour le répertoire /project"

```bash title="scriptsp1.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testsp1* testsp2*

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testsp1 input=mystd-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testsp1 input=mystd-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
fi
```

Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir
`*RESTART, WRITE, OVERLAY, FREQUENCY=12`
Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage
`egrep -i "step|start" testsp*.com testsp*.msg testsp*.sta`
Certaines simulations peuvent être améliorées en ajoutant au bas du script la commande Abaqus
`order_parallel=OFF`

:::
::: tab "script de redémarrage pour le répertoire /project"

```bash title="scriptsp2.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testsp2* testsp1.lck

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testsp2 oldjob=testsp1 input=mystd-sim-restart.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
fi
```

Le fichier en entrée pour le redémarrage doit contenir
`*HEADING`
`*RESTART, READ`

:::
::: tab "script pour répertoire temporaire"

```bash title="scriptst1.txt"
#!/bin/bash
#SBATCH --account=def-group     # Spécifier le compte
#SBATCH --time=00-06:00         # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4       # Spécifier le nombre de cœurs
#SBATCH --mem=8G                # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1               # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre


module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
echo "SLURM_TMPDIR = " $SLURM_TMPDIR

rm -f testst1* testst2*

mkdir $SLURM_TMPDIR/scratch
cd $SLURM_TMPDIR
while sleep 6h; do
   echo "Sauvegarde des données en raison de la limite de temps..."
   cp -fv * $SLURM_SUBMIT_DIR 2>/dev/null
done &
WPID=$!

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
   scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim.inp \
   scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
fi

{ kill $WPID && wait $WPID; } 2>/dev/null
cp -fv * $SLURM_SUBMIT_DIR
```

Pour écrire les données de redémarrage en incréments de N=12, le fichier en entrée doit contenir
`*RESTART, WRITE, OVERLAY, FREQUENCY=12`
Pour écrire les données de redémarrage pour un total de 12 incréments, entrez plutôt
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage
`egrep -i "step|start" testst*.com testst*.msg testst*.sta`

:::
::: tab "script de redémarrage pour le répertoire temporaire"

```bash title="scriptst2.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
#SBATCH --cpus-per-task=4      # Spécifier le nombre de cœurs
#SBATCH --mem=8G               # Spécifier la mémoire totale > 5G
#SBATCH --nodes=1              # Ne pas modifier !
##SBATCH --constraint=granite   # Décommenter pour spécifier un type de nœud
##SBATCH --gpus-per-node=h100:1 # Décommenter pour spécifier [type:]nombre

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
echo "SLURM_TMPDIR = " $SLURM_TMPDIR

rm -f testst2* testst1.lck
cp testst1* $SLURM_TMPDIR
mkdir $SLURM_TMPDIR/scratch
cd $SLURM_TMPDIR
while sleep 6h; do
   echo "Sauvegarde des données en raison de la limite de temps..."
   cp -fv testst2* $SLURM_SUBMIT_DIR 2>/dev/null
done &
WPID=$!

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
   scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testst2 oldjob=testst1 input=$SLURM_SUBMIT_DIR/mystd-sim-restart.inp \
   scratch=$SLURM_TMPDIR/scratch cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB" \
   #gpus=$SLURM_GPUS_ON_NODE  # décommenter cette ligne pour utiliser le GPU
fi

{ kill $WPID && wait $WPID; } 2>/dev/null
cp -fv testst2* $SLURM_SUBMIT_DIR
```

Le fichier en entrée pour le redémarrage doit contenir
`*HEADING`
`*RESTART, READ`

:::
::::

### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas illustré, car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement Abaqus/2026 et versions plus récentes.

```bash title="scriptsp1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
##SBATCH --nodes=2             # Décommenter pour spécifier (optionnel)
#SBATCH --ntasks=8             # Spécifier le nombre de cœurs
#SBATCH --mem-per-cpu=4G       # Spécifier la mémoire par cœur
##SBATCH --tasks-per-node=4    # Décommenter pour spécifier (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026         # Dernière version

unset SLURM_GTIDS
#export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testsp1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testsp1-mpi input=mystd-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # nombre de processus dmp par nœud >= 1 (décommenter pour spécifier)
```

## Analyse explicite

Les solveurs prennent en charge la parallélisation avec fils et avec MPI. Des scripts pour chaque mode sont présentés sous les onglets pour l'utilisation d'un nœud simple et celle de nœuds multiples. Des modèles de scripts pour redémarrer une tâche qui utilise des nœuds multiples nécessitent plus de tests et ne sont pas illustrés pour l'instant.

### Scripts pour un nœud simple

:::: tabs
::: tab "script pour le répertoire /project"

```bash title="scriptep1.txt"
#!/bin/bash
#SBATCH --account=def-group    # indiquer le nom du compte
#SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
#SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
#SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testep1* testep2*

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testep1 input=myexp-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testep1 input=myexp-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
fi
```

Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage
`egrep -i "step|restart" testep*.com testep*.msg testep*.sta`

:::
::: tab "script de redémarrage pour le répertoire /project"

```bash title="scriptep2.txt"
#!/bin/bash
#SBATCH --account=def-group    # indiquer le nom du compte
#SBATCH --time=00-06:00        # indiquer la limite de temps (jours-heures:minutes)
#SBATCH --mem=8000M            # indiquer la mémoire totale > 5M
#SBATCH --cpus-per-task=4      # indiquer le nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testep2* testep1.lck
for f in testep1*; do [[ -f ${f} ]] && cp -a "$f" "testep2${f#testep1}"; done

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testep2 input=myexp-sim.inp recover \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testep2 input=myexp-sim.inp recover \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
fi
```

Le fichier en entrée ne requiert aucune modification pour le redémarrage de l'analyse.

:::
::: tab "script pour le répertoire temporaire"

```bash title="scriptet1.txt"
#!/bin/bash
#SBATCH --account=def-group    # spécifier le compte
#SBATCH --time=00-06:00        # jours-heures:minutes
#SBATCH --mem=8000M            # mémoire du nœud > 5G
#SBATCH --cpus-per-task=4      # nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
echo "SLURM_TMPDIR = " $SLURM_TMPDIR

rm -f testet1* testet2*
cd $SLURM_TMPDIR
while sleep 6h; do
   cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
done &
WPID=$!

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testet1 input=$SLURM_SUBMIT_DIR/myexp-sim.inp \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
fi

{ kill $WPID && wait $WPID; } 2>/dev/null
cp -f * $SLURM_SUBMIT_DIR
```

Pour écrire les données de redémarrage pour un total de 12 incréments, le fichier en entrée doit contenir
`*RESTART, WRITE, OVERLAY, NUMBER INTERVAL=12, TIME MARKS=NO`
Pour vérifier l'information complète sur le redémarrage
`egrep -i "step|restart" testet*.com testet*.msg testet*.sta`

:::
::: tab "script de redémarrage pour le répertoire temporaire"

```bash title="scriptet2.txt"
#!/bin/bash
#SBATCH --account=def-group    # spécifier le compte
#SBATCH --time=00-06:00        # jours-heures:minutes
#SBATCH --mem=8000M            # mémoire du nœud > 5G
#SBATCH --cpus-per-task=4      # nombre de cœurs > 1
#SBATCH --nodes=1              # ne pas modifier

module load abaqus/2026         # Dernière version
#module load StdEnv/2020        # Version héritée
#module load abaqus/2021        # Ne plus utiliser

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"
echo "SLURM_SUBMIT_DIR =" $SLURM_SUBMIT_DIR
echo "SLURM_TMPDIR = " $SLURM_TMPDIR

rm -f testet2* testet1.lck
for f in testet1*; do cp -a "$f" $SLURM_TMPDIR/"testet2${f#testet1}"; done
cd $SLURM_TMPDIR
while sleep 3h; do
   cp -f * $SLURM_SUBMIT_DIR 2>/dev/null
done &
WPID=$!

if [[ $EBVERSIONABAQUS -eq 2021 ]]; then
   /cvmfs/soft.computecanada.ca/gentoo/2023/x86-64-v3/usr/bin/unshare \
   --fork --pid --mount-proc --user --map-user $USER \
   abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
elif [[ $EBVERSIONABAQUS -ge 2026 ]]; then
   abaqus job=testet2 input=$SLURM_SUBMIT_DIR/myexp-sim.inp recover \
   scratch=$SLURM_TMPDIR cpus=$SLURM_CPUS_ON_NODE interactive \
   mp_mode=threads memory="$((${SLURM_MEM_PER_NODE}-3072))MB"
fi

{ kill $WPID && wait $WPID; } 2>/dev/null
cp -f  * $SLURM_SUBMIT_DIR
```

Le fichier en entrée ne requiert aucune modification pour le redémarrage de l'analyse.

:::
::::

### Script pour nœuds multiples

Si vous disposez d'une licence qui vous permet d'exécuter des tâches nécessitant beaucoup de mémoire et de calcul, le script suivant pourra effectuer le calcul avec MPI en utilisant un ensemble de nœuds arbitraires idéalement déterminé automatiquement par l'ordonnanceur. Un script modèle pour redémarrer des tâches sur nœuds multiples n'est pas illustré, car son utilisation présente des limitations supplémentaires. Avec ce script, vous pouvez utiliser uniquement Abaqus/2026 et versions plus récentes.

```bash title="scriptep1-mpi.txt"
#!/bin/bash
#SBATCH --account=def-group    # Spécifier le compte
#SBATCH --time=00-06:00        # Spécifier jours-heures:minutes
#SBATCH --ntasks=8             # Spécifier le nombre de cœurs
#SBATCH --mem-per-cpu=16000M   # Spécifier la mémoire par cœur
# SBATCH --nodes=2             # Spécifier le nombre de nœuds (optionnel)
#SBATCH --cpus-per-task=1      # Ne pas modifier !

module load abaqus/2026        # Dernière version

unset SLURM_GTIDS
export MPI_IC_ORDER='tcp'
#export I_MPI_HYDRA_TOPOLIB=ipl
echo "LM_LICENSE_FILE=$LM_LICENSE_FILE"
echo "ABAQUSLM_LICENSE_FILE=$ABAQUSLM_LICENSE_FILE"

rm -f testep1-mpi*

unset hostlist
nodes="$(slurm_hl2hl.py --format MPIHOSTLIST | xargs)"
for i in `echo "$nodes" | xargs -n1 | uniq`; do hostlist=${hostlist}$(echo "['${i}',$(echo "$nodes" | xargs -n1 | grep $i | wc -l)],"); done
hostlist="$(echo "$hostlist" | sed 's/,$//g')"
mphostlist="mp_host_list=[$(echo "$hostlist")]"
export $mphostlist
echo "$mphostlist" > abaqus_v6.env

abaqus job=testep1-mpi input=myexp-sim.inp \
scratch=$SLURM_TMPDIR cpus=$SLURM_NTASKS interactive mp_mode=mpi \
#mp_host_split=1  # nombre de processus dmp par nœud >= 1 (décommenter pour spécifier)
```

## Estimer le besoin en termes de mémoire

### Processus simple

Une estimation de la mémoire totale pour un nœud (`--mem=`) requise par Slurm pour qu'une simulation soit effectuée uniquement en mémoire vive (sans être virtualisée sur le disque `scratch`) se trouve dans le fichier de sortie Abaqus `test.dat`. Dans l'exemple suivant, la simulation exige une assez grande quantité de mémoire.

```bash
                   E S T I M A T I O N   D E   L A   M É M O I R E
  
 PROCESSUS    OPÉRATIONS EN VIRGULE   MÉMOIRE MINIMALE     MÉMOIRE POUR
              FLOTTANTE PAR           REQUISE              MINIMISER LES E/S
              ITÉRATION                 (Mo)                 (Mo)
  
     1          1.89E+14             3612              96345
```

Une estimation de la mémoire totale pour un processus avec fils sur un nœud unique peut aussi être obtenue en exécutant la simulation de manière interactive sur un nœud de calcul, puis en surveillant la consommation de mémoire à l'aide des commandes `ps` ou `top`.
1.  Connectez-vous d'abord à une grappe avec SSH et obtenez une allocation sur un nœud de calcul (comme gra100) et démarrez votre simulation avec :

    ```bash
    salloc --time=0:30:00 --cpus-per-task=8 --mem=64G --account=def-piname
    module load StdEnv/2020
    module load abaqus/2021
    unset SLURM_GTIDS
    abaqus job=test input=Sample.inp scratch=$SLURM_TMPDIR cpus=8 mp_mode=threads interactive
    ```

2.  Ensuite, via SSH, connectez-vous au nœud de calcul et lancez top.

    ```bash
    ssh c50
    top -u $USER
    ```

3.  Observez les colonnes VIRT et RES jusqu'à ce que des valeurs de mémoire maximales stables soient atteintes.

Pour satisfaire complètement la valeur recommandée pour `MÉMOIRE NÉCESSAIRE POUR MINIMISER LES E/S` (MRMIO), au moins la même quantité de mémoire physique non échangée (`RES`) doit être disponible pour Abaqus. Étant donné que la `RES` sera en général inférieure à la mémoire virtuelle (`VIRT`) d'une quantité relativement constante pour une simulation donnée, il est nécessaire de surallouer légèrement la mémoire du nœud demandée (`--mem=`). Dans l'exemple de script ci-dessus, cette surallocation a été codée en dur à une valeur prudente de 3072 Mo sur la base des tests initiaux du solveur Abaqus standard. Pour éviter les longs temps d'attente associés aux valeurs élevées de MRMIO, il peut être utile d'étudier l'impact sur les performances de simulation associées à la réduction de la mémoire `RES` mise à disposition d'Abaqus de manière significative en dessous de la MRMIO. Cela peut être fait en diminuant la valeur de `--mem=` qui à son tour définira une valeur artificiellement basse de `memory=` dans la commande Abaqus (trouvée dans la dernière ligne du script). En faisant cela, il faut s'assurer que `RES` ne descende pas en dessous de `MÉMOIRE MINIMALE REQUISE` (MMR) sinon Abaqus fermera à cause d'une mémoire insuffisante (OOM). Par exemple, si votre MRMIO est de 96 Go, essayez d'exécuter une série de tâches de test courtes avec `#SBATCH --mem=8G, 16G, 32G, 64G` jusqu'à ce qu'un impact minimal acceptable sur les performances soit trouvé, en notant que des valeurs plus petites entraîneront un espace `/scratch` de plus en plus grand pour les fichiers temporaires.

### Processus multiples

Pour déterminer la mémoire Slurm requise pour les scripts Slurm multi-nœuds, les estimations de mémoire (par processus de calcul) nécessaires pour minimiser les entrées/sorties sont fournies dans le fichier de sortie .dat pour les tâches terminées. Si `mp_host_split` n'est pas spécifié (ou est égal à 1), le nombre total de processus de calcul sera égal au nombre de nœuds. La valeur de `mem-per-cpu` peut alors être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis en divisant par le nombre de tâches (`ntasks`). En revanche, si une valeur pour `mp_host_split` est spécifiée (supérieure à 1), la valeur de `mem-per-cpu` peut être estimée en multipliant l'estimation de mémoire la plus élevée par le nombre de nœuds, puis par la valeur de `mp_host_split`, et en divisant le résultat par le nombre de tâches. Notez que `mp_host_split` doit être inférieur ou égal au nombre de cœurs par nœud attribués par Slurm lors de l'exécution, autrement Abaqus fermera. Ce scénario peut être contrôlé en supprimant le commentaire pour la ligne qui permet de spécifier une valeur pour `tasks-per-node`. Le message suivant, présent dans chaque fichier de sortie, est mentionné ici à titre de référence :

> LE MAXIMUM DE MÉMOIRE POUVANT ÊTRE ALLOUÉ PAR ABAQUS DÉPEND EN GÉNÉRAL DE LA VALEUR DU PARAMÈTRE `MÉMOIRE` ET DE LA QUANTITÉ DE MÉMOIRE PHYSIQUE DISPONIBLE SUR LA MACHINE. VEUILLEZ CONSULTER LE MANUEL D'UTILISATION D'ABAQUS ANALYSIS POUR PLUS DE DÉTAILS. L'UTILISATION RÉELLE DE LA MÉMOIRE ET DE L'ESPACE DISQUE POUR LES DONNÉES DE `/SCRATCH` DÉPENDRA DE CETTE LIMITE SUPÉRIEURE AINSI QUE DE LA `MÉMOIRE REQUISE POUR MINIMISER LES E/S`. SI LA LIMITE SUPÉRIEURE DE MÉMOIRE EST SUPÉRIEURE À LA `MÉMOIRE REQUISE POUR MINIMISER LES E/S`, L'UTILISATION RÉELLE DE LA MÉMOIRE SERA PROCHE DE LA VALEUR ESTIMÉE DE `MEMORY TO MINIMIZE I/O` ET L'UTILISATION DU DISQUE DE TRAVAIL SERA PROCHE DE ZÉRO. AUTREMENT, LA MÉMOIRE RÉELLE UTILISÉE SERA PROCHE DE LA LIMITE DE MÉMOIRE MENTIONNÉE PRÉCÉDEMMENT, ET L'UTILISATION DU DISQUE `/SCRATCH` SERA À PEU PRÈS PROPORTIONNELLE À LA DIFFÉRENCE ENTRE `MEMORY TO MINIMIZE I/O` ESTIMÉE ET LA LIMITE SUPÉRIEURE DE LA MÉMOIRE. TOUTEFOIS, IL EST IMPOSSIBLE D'ÉVALUER AVEC PRÉCISION L'ESPACE `/SCRATCH` DU DISQUE.

# Utilisation graphique

Nous recommandons d'utiliser Open OnDemand ou Jupyter pour travailler avec des applications graphiques.

## OnDemand

1.  Lancez une session OnDemand sur votre bureau en cliquant sur le lien approprié.
    NIBI : <https://ondemand.sharcnet.ca>
    TRILLIUM : <https://ondemand.scinet.utoronto.ca>

2.  Ouvrez une nouvelle fenêtre de terminal et chargez :
    ```bash
    module load abaqus/2026
    ```

3.  Lancez l'application en mode graphique avec l'option `cae`. Si vous êtes sur un nœud sans GPU ou sur un nœud avec GPU où VirtualGL n'est pas pris en charge, ajoutez l'option `mesa`.
    ```bash
    abaqus cae -mesa
    ```

4.  Si vous avez besoin d'une meilleure performance graphique et êtes sur un nœud avec GPU où VirtualGL est pris en charge, lancez Abaqus sans l'option `mesa`. Dans Nibi Desktop, sélectionnez h100 (80 Go) dans le menu déroulant.
    ```bash
    abaqus cae
    ```

5.  Pour lancer Abaqus en mode graphique, il faut au moins une licence de calcul non utilisée, selon :
    ```bash
    abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of cae"
    ```

## JupyterLab

1.  Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    FIR: `https://jupyterhub.fir.alliancecan.ca`
    NARVAL: `https://portail.narval.calculquebec.ca/`
    RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6`) dans la section *Module disponible* de gauche.
3.  Pour le module sélectionné, cliquez sur *Charger* pour faire afficher l'icône `Comsol (VNC)` sur le bureau.
4.  Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

## VncViewer

!!! warning "Approche obsolète"
    Cette approche est obsolète. Veuillez utiliser un bureau OnDemand ou JupyterLab comme décrit ci-dessus.

1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou de connexion sans GPU, comme décrit dans [TigerVNC](../interactive/vnc.md).
2.  Ouvrez une nouvelle fenêtre de terminal et entrez :
    ```bash
    module load abaqus/2026
    ```
3.  Lancez l'application avec :
    ```bash
    abaqus cae -mesa
    ```

# Utilisation spécifique au site

## Licence SHARCNET

La licence SHARCNET a été renouvelée jusqu'au 17 janvier 2026. Elle offre une licence gratuite limitée comprenant 2 jetons de calcul et 35 jetons d'exécution, avec des limites d'utilisation de 10 jetons par utilisateur et 15 jetons par groupe. Pour les groupes ayant acquis des jetons dédiés, les limites d'utilisation des jetons gratuits sont ajoutées à leur réservation. Les jetons gratuits sont attribués selon le principe du premier arrivé, premier servi et sont principalement destinés aux tests et à une utilisation légère avant de décider d'acheter ou non des jetons dédiés. Le coût des jetons dédiés (en 2021) était d'environ 110 $ CA par jeton de calcul et 400 $ CA par jeton d'interface graphique : écrivez au [soutien technique](../support/technical_support.md) pour obtenir un devis officiel. La licence peut être utilisée avec un compte de l'Alliance, mais uniquement sur le matériel SHARCNET. Les groupes qui achètent des jetons dédiés pour le serveur de licences SHARCNET ne peuvent les utiliser que sur le matériel SHARCNET, notamment le système SHARCNET [OOD](../clusters/nibi.md#accès_via_open_ondemand_(ood)) (pour le mode graphique) ou les grappes Nibi/Dusky (pour soumettre des tâches de calcul par lots à la file d'attente). Avant d'utiliser la licence, vous devez contacter le [soutien technique](../support/technical_support.md) et demander l'accès. Dans votre courriel, veuillez 1) préciser que la demande est destinée à une utilisation sur les systèmes SHARCNET et 2) copier coller l'accord de licence suivant, en indiquant vos nom et prénom ainsi que votre nom d'utilisateur aux emplacements prévus.

!!! note
    Veuillez noter que chaque utilisateur doit effectuer cette démarche; elle ne peut être effectuée une seule fois pour un groupe, y compris pour les chercheuses principales et chercheurs principaux ayant acheté leurs propres jetons dédiés.

### Entente

```text
----------------------------------------------------------------------------------
Sujet: Entente d'utilisateur de la licence académique Abaqus SHARCNET

Ce courriel confirme que je "_____________" avec le nom d'utilisateur "___________"
utiliserai le "logiciel académique SIMULIA" avec les jetons du serveur de licences
SHARCNET uniquement aux fins suivantes:

1) sur le matériel SHARCNET où le logiciel est déjà installé
2) en affiliation avec un établissement d'enseignement canadien délivrant des diplômes
3) à des fins d'éducation, institutionnelles ou d'enseignement et non à des fins
   commerciales ou contractuelles dont les résultats ne sont pas publables
4) de recherche expérimentale, théorique et/ou numérique, entreprise principalement
   pour acquérir de nouvelles connaissances sur les fondements sous-jacents des
   phénomènes et des faits observables, jusqu'à la preuve de concept en laboratoire
-----------------------------------------------------------------------------------
```

### Configurer le fichier de licence

Configurez votre fichier de licence comme suit (uniquement sur les systèmes SHARCNET comme les grappes Nibi et Dusky ou sur le système de bureau OOD de SHARCNET). Pour utiliser la licence SHARCNET gratuite, vous devez mettre à jour votre fichier `abaqus.lic` comme suit, puisque le serveur `license3.sharcnet.ca` est définitivement fermé.

```bash
[l2 (nœud de connexion Nibi):~] cat ~/.licenses/abaqus.lic
prepend_path("ABAQUSLM_LICENSE_FILE","27050@license1.computecanada.ca")
```

Si votre tâche se termine anormalement avec le message d'erreur **ABAQUS/eliT_CheckLicense rank 0 terminated by signal 11 (Segmentation fault)**, vérifiez si votre fichier `abaqus.lic` contient `ABAQUSLM_LICENSE_FILE` pour Abaqus/202X.
Si le message d'erreur est **License server machine is down or not responding etc.** et que vous utilisez Abaqus/6.14.1, remplacez ABAQUSLM_LICENSE_FILE par LM_LICENSE_FILE.

### Interroger le serveur de licences

Connectez-vous à Nibi, chargez Abaqus et exécutez une des commandes suivantes :
```bash
ssh nibi.alliancecan.ca
module load StdEnv/2020
module load abaqus
```

I) Vérifiez s'il y a des tâches lancées et des tâches en file d'attente pour le serveur de licence SHARCNET.
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
```
II) Vérifiez s'il y a des tâches lancées et des tâches en file d'attente pour le serveur de licence SHARCNET et s'il indique des réservations de produits par groupe d'acquisition.
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued|RESERVATION"
```
III) Vérifiez si le serveur de licences SHARCNET montre une disponibilité explicite pour le produit standard pour le calcul.
```bash
abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | grep "Users of" | egrep "cae|standard|explicit"
```

Lorsque le résultat de la requête I) ci-dessus indique qu'une tâche associée à un nom d'utilisateur donné est en file d'attente, cela signifie que la tâche est passée à l'état *R (running)* pour `squeue -j jobid` ou `sacct -j jobid` et qu'elle est donc inactive sur un nœud de calcul, en attente d'une licence. Cela aura le même impact sur la priorité de votre compte que si la tâche effectuait des calculs et consommait du temps CPU. La tâche en file d'attente démarrera dès que suffisamment de licences seront disponibles.

#### Exemple

L'exemple suivant illustre la situation où un utilisateur soumet successivement deux tâches pour 6 cœurs, nécessitant chacune 12 jetons. L'ordonnanceur a ensuite lancé chaque tâche sur un nœud différent, dans l'ordre de leur soumission. L'utilisateur disposant de 10 jetons Abaqus, la première tâche (27527287) a pu obtenir exactement les 10 jetons nécessaires au démarrage du solveur. La seconde tâche (27527297), n'ayant plus accès à des jetons, est restée en attente (comme le montre la sortie de *lmstat*) jusqu'à la fin de la première, gaspillant ainsi les ressources disponibles et réduisant la juste part de l'utilisateur.

```text
[l2 (nœud de connexion Nibi):~] sq
            JOBID     USER              ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (RAISON)
         27530366  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:56:13     1    6        N/A      8G     c107  (Aucune)
         27530407  roberpj         cc-debug_cpu  scriptsp2.txt   R    9:59:37     1    6        N/A      8G     c292  (Aucune)

[l2 (nœud de connexion Nibi):~] abaqus licensing lmstat -c $ABAQUSLM_LICENSE_FILE -a | egrep "Users|start|queued"
 Users of abaqus:  (Total of 78 licenses issued;  Total of 53 licenses in use)
    roberpj c107 /dev/tty (v62.6) (license3.sharcnet.ca/27050 1042), start Mon 11/25 17:15, 10 licenses
    roberpj c292 /dev/tty (v62.6) (license3.sharcnet.ca/27050 125) en file d'attente pour 10 licences
```

Pour éviter les problèmes de pénurie de licences lors de la soumission de plusieurs tâches avec des jetons Abaqus coûteux, utilisez soit [une dépendance](../running-jobs/running_jobs.md#annulation_de_tâches_dont_les_conditions_de_dépendance_ne_sont_pas_satisfaites), [un vecteur](../running-jobs/job_arrays.md), soit au moins configurez [une notification par courriel Slurm](../running-jobs/monitoring_jobs.md#notification_par_courriel) pour savoir quand votre tâche est terminée avant d'en soumettre une autre manuellement.

1.  Désactiver le démarrage des tâches non interactives (analyse) sur un nœud de calcul de la grappe après leur soumission à la file d'attente et leur mise en inactivité (lorsque le nombre de jetons est insuffisant, comportement par défaut). Créez un fichier texte dans votre répertoire de soumission (avant de soumettre la tâche) avec le contenu d'une seule ligne suivant et la tâche se terminera immédiatement.

    ```bash
    [l2 (nœud de connexion Nibi):~/submitdirectory] cat abaqus_v6.env
    lmlicensequeuing=OFF
    ```

    Lorsqu'une tâche se termine immédiatement (sans entrer en état `QUEUED` pour attendre une licence), la fin du fichier de sortie Slurm correspondant contiendra des messages tels que :

    ```text
    Abaqus 2026
    Le processus de vérification dépasse le MAX spécifié dans le fichier d'options.
    Erreur de licence FlexNet:-87,147
    Nombre de licences demandées : 14
    Nombre total de licences :     78
    Nombre de licences utilisées :    14
    Nombre de licences disponibles : 64
    Ceci peut être dû à un nombre insuffisant de licences.
    ValueError: pas assez de valeurs à déballer (attendu 2, obtenu 1)
    Lors de la gestion de l'exception ci-dessus, une autre exception s'est produite :
    Exception: DriverLM: impossible d'analyser l'hôte/le port de l'umbrella
    Erreur Abaqus: Erreur lors de la vérification de la licence Abaqus.
    Abaqus/Analysis s'est terminé avec des erreurs
    ```

2.  Spécifiez un paramètre en minutes pour qu'une tâche démarrée entre dans un état `QUEUED` pour attendre une licence avant d'être automatiquement `DEQUEUED` et de se terminer si une licence ne devient pas disponible à temps.

    ```bash
    [l2 (nœud de connexion Nibi):~/submitdirectory] cat abaqus_v6.env
    lmhanglimit=1
    ```

    Lorsqu'une tâche se termine de cette manière, après avoir été mise en file d'attente et qu'aucune licence n'est devenue disponible dans le temps spécifié selon la valeur de `lmhanglimit` (1 minute dans cet exemple), les messages à la fin du fichier de sortie Slurm apparaîtront plutôt comme suit :

    ```text
    Abaqus 2026
    Requête de licence "standard" mise en file d'attente pour le serveur de licences sur license1.computecanada.ca.
    Temps total en file d'attente: 0 secondes.
    Requête de licence "standard" mise en file d'attente pour le serveur de licences sur license1.computecanada.ca.
    Temps total en file d'attente: 30 secondes.
    Requête de licence "standard" mise en file d'attente pour le serveur de licences sur license1.computecanada.ca.
    Temps total en file d'attente: 60 secondes.
    La limite de temps en file d'attente a été dépassée. Sortie.
    Ceci peut être dû à un nombre insuffisant de licences.
    ValueError: pas assez de valeurs à déballer (attendu 2, obtenu 1)
    Lors de la gestion de l'exception ci-dessus, une autre exception s'est produite :
    Exception: DriverLM: impossible d'analyser l'hôte/le port de l'umbrella
    Erreur Abaqus: Erreur lors de la vérification de la licence Abaqus.
    Abaqus/Analysis s'est terminé avec des erreurs
    ```

### Spécifier les ressources de la tâche

Pour garantir une utilisation optimale de vos jetons Abaqus et de nos ressources, il est important de spécifier soigneusement la mémoire et le nombre de CPU requis dans votre script Slurm. Les valeurs peuvent être déterminées en soumettant quelques tâches de test courtes à la file d'attente, puis en vérifiant leur utilisation. Pour les tâches **terminées**, utilisez `seff JobNumber` pour afficher l'*Utilisation de la mémoire* totale et l'*Efficacité de la mémoire*. Si l'*Efficacité de la mémoire* est inférieure à ~90%, diminuez la valeur du paramètre `#SBATCH --mem=` dans votre script Slurm en conséquence. Notez que la commande `seff JobNumber` affiche également l'*Utilisation du CPU (temps)* totale et l'*Efficacité du CPU*. Si l'*Efficacité du CPU* est inférieure à ~90%, effectuez des tests de mise à l'échelle pour déterminer le nombre optimal de CPU pour des performances optimales, puis mettez à jour la valeur de `#SBATCH --cpus-per-task=` dans votre script Slurm. Pour les tâches **en cours d'exécution**, utilisez la commande `srun --overlap --jobid=29821580 --pty top -d 5 -u $USER` pour observer le `%CPU`, le `%MEM` et la `RES` pour chaque processus parent Abaqus sur le nœud de calcul. Les colonnes `%CPU` et `%MEM` affichent le pourcentage d'utilisation par rapport au total disponible sur le nœud, tandis que la colonne `RES` affiche la taille de la mémoire résidente par processus (au format lisible par l'homme pour les valeurs supérieures à 1 Go). Des informations supplémentaires sur la façon de [surveiller les tâches](../running-jobs/monitoring_jobs.md) sont disponibles sur notre wiki de documentation.

### Correspondance cœur-jeton

| Jetons | Cœurs |
|--------|-------|
| 5      | 1     |
| 6      | 2     |
| 7      | 3     |
| 8      | 4     |
| 10     | 6     |
| 12     | 8     |
| 14     | 12    |
| 16     | 16    |
| 19     | 24    |
| 21     | 32    |
| 25     | 48    |
| 28     | 64    |
| 34     | 96    |
| 38     | 128   |

où TOKENS = `floor[5 X CORES^0.422]`

Chaque GPU nécessite un jeton additionnel.

## Licence de Western

!!! warning "Avertissement : Licence Western obsolète"
    Le fichier `abaqus.lic` ci-dessous ne fonctionne plus, car la machine `license4` a été mise hors service définitivement. Par conséquent, toutes les demandes d'accès à une licence Abaqus sur la grappe Dusky à partir du serveur de licences Abaqus Western/Robarts échoueront. Un serveur de remplacement pour `license4` est en préparation. Dès qu'il sera en fonction, le fichier `abaqus.lic` sera mis à jour avec le nouveau nom du serveur et ce message d'avertissement rouge sera supprimé. En attendant, la licence SHARCNET peut être utilisée en suivant la procédure de demande d'accès ci-dessus.

La licence Western est réservée aux chercheurs et chercheuses de Western et ne peut être utilisée que sur du matériel situé sur le campus. Actuellement, seule la grappe Dusky remplit cette condition. Les systèmes Nibi et SHARCNET OOD sont exclus, car ils se trouvent sur le campus de Waterloo. Pour toute question concernant l'utilisation de la licence Abaqus de Western, veuillez contacter l'administrateur du serveur de licences Abaqus de Western à l'adresse <jmilner@robarts.ca>. Vous devrez fournir votre nom d'utilisateur et éventuellement prévoir l'achat de jetons. Si votre demande d'accès est acceptée, vous pourrez configurer votre fichier `abaqus.lic` pour qu'il pointe vers le serveur de licences de Western.

### Configurer le fichier de licences

```bash
[dus241:~] cat .licenses/abaqus.lic
prepend_path("LM_LICENSE_FILE","27000@license4.sharcnet.ca")
prepend_path("ABAQUSLM_LICENSE_FILE","27000@license4.sharcnet.ca")
```

Par la suite, soumettez votre tâche tel que décrit à la section [Soumettre des tâches en lots](#soumettre-des-tâches-en-lots) ci-dessus. Si un problème survient, écrivez au [soutien technique](../support/technical_support.md) en indiquant que vous utilisez la licence du site Western sur Dusky. Ajoutez le numéro de la tâche qui pose problème et copiez le ou les messages d'erreur s'il y a lieu.