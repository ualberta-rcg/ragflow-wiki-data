---
title: "Ansys/fr"
slug: "ansys"
lang: "fr"

source_wiki_title: "Ansys/fr"
source_hash: "d387bd7d1e99574441ecdf3f96fe54b3"
last_synced: "2026-05-17T14:59:09.465984+00:00"
last_processed: "2026-05-17T15:12:03.769659+00:00"

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
  qa_generated: true
---

Ansys

[Ansys](http://www.ansys.com/) est une suite logicielle pour la conception 3D et la simulation. La suite comprend des applications comme [Ansys Fluent](http://www.ansys.com/Products/Fluids/ANSYS-Fluent) et [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

## Licence

La suite Ansys est hébergée sur nos grappes, mais nous n'avons pas une licence qui permet un accès généralisé. Toutefois, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes; vérifiez les modalités d'utilisation. Sur le plan technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licences. Si ce n'est pas déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licences. Quand tout sera en place, vous pourrez charger le module Ansys qui localisera de lui-même la licence. En cas de difficulté, communiquez avec le [soutien technique](../support/technical_support.md).

## Configurez votre propre fichier de licence

Notre module Ansys cherche l'information sur la licence à différents endroits, dont votre répertoire personnel.
Pour indiquer votre propre serveur de licences, créez un fichier nommé ` ~/.licenses/ansys.lic` qui contient les deux lignes ci-dessous, où vous remplacez `FLEXPORT`, `INTEPORT` et `LICSERVER` par les valeurs de votre serveur.

```yaml title="ansys.lic"
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@LICSERVER")
```

Les valeurs correspondant aux serveurs de licences CMC et SHARCNET se trouvent dans le tableau ci-dessous. Pour utiliser un serveur différent, voir [Serveurs de licences locaux](#serveurs-de-licences-locaux) ci-dessous.

| Licence | Grappe                    | LICSERVER                | FLEXPORT | INTEPORT | VENDPORT | Remarques                               |
| :------ | :------------------------ | :----------------------- | :------- | :------- | :------- | :-------------------------------------- |
| CMC     | Béluga                    | `10.20.73.21`            | `6624`   | `2325`   | sans objet | aucune                                  |
| CMC     | Cedar                     | `172.16.0.101`           | `6624`   | `2325`   | sans objet | aucune                                  |
| CMC     | Graham                    | `10.25.1.56`             | `6624`   | `2325`   | sans objet | nouvelle adresse IP le 21 février 2025  |
| CMC     | Narval                    | `10.100.64.10`           | `6624`   | `2325`   | sans objet | aucune                                  |
| SHARCNET | Béluga/Cedar/Graham/gra-vdi/Nibi/Narval/Rorqual | `license3.sharcnet.ca`   | `1055`   | `2325`   | non applicable | aucune                                  |
| SHARCNET | Niagara                   | `localhost`              | `1055`   | `2325`   | `1793`   | aucune                                  |

### Serveurs de licences locaux

Avant que le serveur de licences de votre établissement puisse être utilisé, les pare-feux des deux parties doivent être configurés. Dans plusieurs cas, ce travail est déjà fait; suivez les directives dans le paragraphe *Prêt à l'emploi* ci-dessous. Autrement, référez-vous au paragraphe *Configuration requise* un peu plus bas.

#### Prêt à l'emploi

Pour utiliser un serveur de licences Ansys déjà configuré pour être utilisé sur la grappe où vous allez soumettre des tâches, contactez votre administrateur des licences Ansys et obtenez les trois éléments d'information suivants :
1.  le nom d'hôte complet (`LICSERVER`) du serveur
2.  le port Flex (`FLEXPORT`) pour Ansys, habituellement `1055`
3.  le port d'interconnexion (`INTEPORT`), habituellement `2325`
Une fois les trois éléments d'information collectés, configurez votre fichier `~/.licenses/ansys.lic` en entrant les valeurs de `LICSERVER`, `FLEXPORT` et `INTEPORT` dans le modèle `ansys.lic` ci-dessus.

#### Configuration requise

Si votre serveur de licences Ansys local n'a jamais été configuré pour être utilisé sur la ou les grappes où vous allez soumettre des tâches, en plus des 3 éléments ci-dessus, vous devrez ÉGALEMENT obtenir les éléments suivants auprès de l'administrateur :
4.  le numéro de port statique du fournisseur (`VENDPORT`)
5.  confirmation que `<servername>` se résoudra à la même adresse IP que `LICSERVER` sur nos grappes
où `<servername>` peut être trouvé dans la première ligne du fichier de licence avec le format *SERVER `<servername>` `<host id>` `<lmgrd port>`*. L'élément 5 est obligatoire sinon les extractions de licences Ansys ne fonctionneront sur aucune grappe distante. S'il s'avère que `<servername>` ne répond pas à cette exigence, demandez à votre administrateur de licences de remplacer `<servername>` par le même nom d'hôte complet que `LICSERVER` ou au moins par un nom d'hôte qui se résoudra à la même adresse IP que `LICSERVER` à distance.

## Vérifier la licence

Pour vérifier si `ansys.lic` est bien configuré et fonctionne correctement, copiez et collez la séquence de commandes suivantes sur la grappe où vous voulez soumettre des tâches. La seule différence est de spécifier `YOURUSERID`. Si le logiciel n’est pas à jour sur le serveur de licences distant, un problème peut survenir si la dernière version du module Ansys est chargée pour effectuer des tests. Pour que la licence fonctionne quand des tâches sont soumises, assurez-vous que la même version du module Ansys qui est chargé par votre script est utilisée dans les commandes ci-dessous.

```bash
[gra-login:~] cd /tmp
[gra-login:~] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[gra-login:~] module load StdEnv/2023; module load ansys/2023R2
[gra-login:~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE 1> /dev/null && echo Success || echo Fail
```

```bash
[login-node:~] cd /tmp
[login-node:/tmp] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[compute-node/tmp] module load StdEnv/2023; module load ansys/2025R2.04
[compute-node:/tmp] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```

`Success` indique que les extractions de licences devraient fonctionner lorsque les tâches sont soumises à la file d'attente.
`Fail` indique un problème avec la configuration de la licence et les tâches échoueront probablement.

!!! note "Remarque 1"
    Pour les modules Ansys installés localement, la commande `runwb2` de `SnEnv` utilise par défaut le serveur de licences SHARCNET, tel que défini dans le fichier du module Ansys que vous chargez. Pour utiliser un serveur distant, lancez plutôt *Workbench* avec `runwb2-gui`, car ce script enveloppant (*wrapper*) lira votre fichier `~/.licenses/ansys.lic` comme les modules disponibles sous `StdEnv/2023`. De plus, l'option interactive d'utilisation du serveur CMC (acheminé via le serveur SHARCNET CMC CadPASS) sera proposée, éliminant ainsi la nécessité de le configurer dans votre fichier `ansys.lic`.

!!! note "Remarque 2"
    Lorsque vous démarrez *Fluent* à partir de *Workbench* avec la version `2025R1`, avant de cliquer sur le bouton *Start*, cliquez sur l'onglet *Environment* du panneau de lancement de *Fluent Launcher* et copiez/collez `HOOPS_PICTURE=opengl` dans le champ de saisie vide. Vous pouvez aussi définir `export HOOPS_PICTURE=opengl` dans votre environnement avant de démarrer *Workbench*. L'une ou l'autre de ces actions empêchera le message suivant, qui apparaîtrait dans les messages de démarrage de l'interface utilisateur : `Warning: Software rasterizer found, hardware acceleration will be disabled.`

!!! note "Remarque 3"
    Lorsque vous exécutez *Mechanical* dans *Workbench* sur `gra-vdi`, assurez-vous de cocher *Distributed* dans le panneau *Solver* du ruban supérieur et de spécifier une valeur maximale de **24 cœurs**. Lorsque vous exécutez *Fluent* sur `gra-vdi`, ne cochez pas *Distributed* et spécifiez une valeur maximale de **12 cœurs**. N'essayez pas d'utiliser plus de `128Go` de mémoire, sinon Ansys atteindra la limite et sera arrêté. Si vous avez besoin de plus de cœurs ou de mémoire, utilisez un nœud de calcul sur une grappe pour exécuter votre session graphique (comme décrit dans la section *Nœuds de calcul* ci-dessus). Lorsque vous effectuez une ancienne tâche de prétraitement ou de post-traitement avec Ansys sur `gra-vdi` et que vous n'exécutez pas de calcul, utilisez uniquement **4 cœurs**, sinon les licences HPC seront extraites inutilement.

!!! note "Remarque 4"
    Dans de très rares cas, l'interface graphique de *Workbench* ou de certains programmes qu'il exécute se bloquent ou ne démarrent pas correctement, notamment si `vnsviewer` se déconnecte avant que Ansys soit fermé correctement. En général, si Ansys ne fonctionne pas correctement, ouvrez une nouvelle fenêtre de terminal sur `gra-vdi` et exécutez `pkill -9 -e -u $USER -f "ansys|fluent|mwrpcss|mwfwrapper|ENGINE|mono"` pour arrêter complètement tous les processus Ansys. Si le problème persiste et que vous utilisiez l'interface graphique sur des nœuds de calcul avant de travailler sur `gra-vdi`, essayez d'exécuter `rm -rf .ansys`. Si le problème concerne `/home`, `/project` ou `/scratch` (la commande `df` bloque), il est fort probable qu'Ansys recommence à fonctionner normalement une fois le problème de stockage résolu.

```bash
[compute-node:/tmp] fluent -g 2d -n 2
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

## Compatibilité des versions

Les simulations Ansys sont typiquement compatibles avec des versions plus récentes, mais **ce n'est pas le cas** avec les versions antérieures. Ceci signifie que des simulations faites avec une version antérieure de Ansys devraient pouvoir être chargées et exécutées sans problème avec une version plus récente. Par exemple, une simulation créée et sauvegardée avec `ansys/2022R2` devrait fonctionner avec `ansys/2023R2`, mais **pas l'inverse**. Il est toujours possible de lancer une simulation créée avec une version antérieure, mais il est fort possible que la simulation plante ou que vous obteniez des messages d'erreur. Quant aux simulations *Fluent*, si vous ne vous souvenez pas du numéro de la version Ansys que vous avez utilisée pour créer le fichier cas, vous trouverez des indices avec les lignes suivantes.

```bash
$ grep -ia fluent combustor.cas
```

```text
(0 "fluent15.0.7 build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
```

```text
ANSYS_FLUENT 24.1 Build 1018
```

## Plateformes prises en charge

## Ansys Fluent

Voici la procédure habituelle pour utiliser *Fluent* avec les grappes de Calcul Canada :

## Nouveautés

Ansys publie régulièrement des *packs de services* pour regrouper plusieurs mises à jour apportant différents correctifs et améliorations à ses versions majeures. Des informations similaires pour les versions précédentes peuvent généralement être trouvées sur [le blogue Ansys](https://www.ansys.com/blog), en utilisant la barre de recherche *FILTERS*. Par exemple, la recherche de `What’s New Fluent 2024 gpu` affichera le document `[What’s New for Ansys Fluent in 2024 R1?](https://www.ansys.com/blog/fluent-2024-r1)` qui contient une multitude d'informations sur la prise en charge des GPU. Spécifier un numéro de version dans le champ de recherche [Communiqués de presse](https://www.ansys.com/news-center/press-releases) est également un bon moyen de trouver des informations sur les nouvelles versions. Le module `ansys/2025R1.02` pour la dernière version de Ansys a été installé récemment; pour l'utiliser cependant, vous avez besoin d'un serveur de licences comme celui de CMC. La mise à jour du serveur de licences de SHARCNET est en cours et tant que ce travail ne sera pas terminé, seules les versions `ansys/2024R2.04` ou moins récentes seront prises en charge. Si un module pose problème ou pour demander l'installation d'une nouvelle version, écrivez au [soutien technique](../support/technical_support.md).

## Correctifs

À partir d'Ansys `2024`, un module Ansys distinct sera identifié avec une décimale et deux chiffres après le numéro de version, chaque fois qu'un *pack de services* est installé pour la version initiale. Par exemple, la version initiale pour `2024` sans aucun *pack de services* peut être chargée en exécutant `module load ansys/2024R1` tandis qu'un module avec le *pack de services* 3 peut être chargé avec `module load ansys/2024R1.03`. Si un *pack de services* est déjà disponible au moment où une nouvelle version doit être installée, il est fort probable que seulement un module pour ce numéro de *pack de services* sera installé, à moins qu'une demande soit faite pour l'installation de la version initiale.

La plupart du temps, vous voudrez probablement charger la dernière version du module équipé du dernier *pack de services* installé en exécutant simplement `module load ansys`. Bien qu'il ne soit pas prévu que les *packs de services* aient un impact sur les résultats numériques, les modifications qu'ils apportent sont importantes et donc si des calculs ont déjà été effectués avec la version initiale ou un *pack de services* antérieur, certains groupes préféreront peut-être continuer à l'utiliser. Le fait d'avoir des modules distincts pour chaque *pack de services* rend cela possible. À partir d'Ansys `2024R1`, une description détaillée de ce que fait chaque *pack de services* se trouve dans [la documentation officielle](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) (les versions futures pourront probablement être consultées de la même manière en modifiant le numéro de version contenu dans le lien).

## Soumettre des tâches par lots sur nos grappes

Plusieurs implémentations MPI incluses dans la suite Ansys permettent le calcul parallèle, mais aucune n'est compatible avec l'ordonnanceur Slurm (voir [Exécuter des tâches](../running-jobs/running_jobs.md)). Pour cette raison, il faut utiliser des directives particulières à chaque paquet Ansys pour lancer une tâche parallèle. Vous trouverez ci-dessous quelques scripts de soumission pour ce faire. Ils fonctionneront sur toutes les grappes, mais sur Niagara, vous devrez peut-être [faire certains ajustements](https://docs.scinet.utoronto.ca/index.php).

### Ansys Fluent

La procédure suivante est habituellement utilisée pour exécuter *Fluent* sur une de nos grappes :

1.  Sur votre ordinateur, préparez votre tâche avec *Fluent* du *Ansys Workbench* jusqu'au point où les calculs seraient exécutés.
2.  Exportez le fichier de cas avec *File > Export > Case…* ou localisez le répertoire dans lequel *Fluent* enregistre les fichiers pour votre projet. Le nom des fichiers de cas a souvent un format tel que `FFF-1.cas.gz`.
3.  Si vous voulez poursuivre avec des données d'un calcul effectué précédemment, exportez aussi un fichier de données avec *File > Export > Data…* ou trouvez-le dans le même répertoire `/project` (`FFF-1.dat.gz`).
4.  [Transférez](../getting-started/transferring_data.md) le fichier de cas (et le fichier de données s'il y a lieu) dans le système de fichiers [/project](../storage-and-data/project_layout.md) ou [/scratch](../storage-and-data/storage_and_file_management.md#types-de-stockage) de la grappe. Quand les fichiers sont exportés, sauvegardez-les avec des noms plus faciles à repérer que `FFF-1.*` ou renommez-les au téléchargement.
5.  Créez un fichier journal dont le but est de charger les fichiers de cas (et le fichier de données s'il y a lieu), lancez le solveur et enregistrez les résultats. Voyez les exemples ci-dessous et n'oubliez pas d'ajuster les noms des fichiers et le nombre d'itérations.
6.  S'il arrive fréquemment que les tâches ne démarrent pas en raison d'un manque de licence (et que de les soumettre de nouveau manuellement ne convient pas), vous pouvez modifier votre script pour que votre tâche soit remise en file d'attente (au plus 4 fois) comme c'est le cas pour le script sous l'onglet *Plusieurs nœuds (par cœur + remise en attente)* plus loin. Cependant, ceci remet aussi en file d'attente les simulations qui ont échoué pour d'autres raisons que l'absence de licence (par exemple la divergence), gaspillant ainsi du temps de calcul. Il est donc fortement recommandé de vérifier les fichiers de sortie de l'ordonnanceur pour savoir si chaque tentative de remise en file d'attente est ou non due à un problème de licence. Si vous découvrez que la remise en file d'attente est due à un problème avec la simulation, annulez immédiatement la tâche avec `scancel jobid` et corrigez le problème.
7.  Lorsque la [tâche est terminée](../running-jobs/running_jobs.md), vous pouvez télécharger le fichier de données et le retourner dans *Fluent* avec *File > Import > Data…*.

### Scripts pour l'ordonnanceur Slurm

#### Utilisation générale

La plupart des tâches *Fluent* devraient utiliser le script *par nœud* ci-dessous pour minimiser le temps d'attente et maximiser la performance en utilisant le moins de nœuds possible. Les tâches demandant beaucoup de cœurs de processeurs pourraient attendre moins longtemps dans la file d'attente avec le script *par cœur*, mais le démarrage d’une tâche utilisant plusieurs nœuds peut prendre beaucoup plus de temps, ce qui en diminue l'intérêt. Il faut aussi tenir compte du fait qu'exécuter des tâches intensives sur un nombre indéterminé de nœuds pouvant être très élevé fait en sorte que ces tâches seront beaucoup plus susceptibles de planter si un des nœuds de calcul fait défaut pendant la simulation. Les scripts suivants utilisent la mémoire partagée pour les tâches utilisant un seul nœud et la mémoire distribuée (avec MPI et l’interconnexion CHP appropriée) pour les tâches en utilisant plusieurs.

Les deux onglets pour Narval peuvent fournir une alternative plus robuste si *Fluent* plante pendant la phase initiale de partitionnement automatique du maillage lors de l'utilisation des scripts *Intel* standards avec le solveur parallèle. L'autre option serait d'effectuer manuellement le partitionnement du maillage dans l'interface graphique de *Fluent*, puis d'essayer d'exécuter à nouveau la tâche sur la grappe avec les scripts *Intel*. Ainsi, vous pouvez inspecter les statistiques de partitionnement et spécifier la méthode pour obtenir un résultat optimal. Le nombre de partitions de maillage doit être un multiple entier du nombre de cœurs; pour une efficacité optimale, assurez-vous d'avoir au moins 10 000 cellules par cœur.

```tabs
```tab "Plusieurs nœuds (par nœud)"
```bash title="script-flu-bynode-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (Narval 1 nœud maximum)
#SBATCH --ntasks-per-node=32  # Spécifiez le nombre maximum de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne changez pas

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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

```tab "Plusieurs nœuds (par cœur)"
```bash title="script-flu-bycore-intel.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval 1 nœud maximum)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne changez pas

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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

```tab "Plusieurs nœuds (par nœud, Narval)"
```bash title="script-flu-bynode-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=64  # Spécifiez le nombre de cœurs par nœud (Narval 64 ou moins)
#SBATCH --mem=0               # Ne changez pas (allouer toute la mémoire par nœud de calcul)
#SBATCH --cpus-per-task=1     # Ne changez pas

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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

```tab "Plusieurs nœuds (par cœur, Narval)"
```bash title="script-flu-bycore-openmpi.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
##SBATCH --nodes=1            # Décommentez pour spécifier le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs sur tous les nœuds
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne changez pas

module load StdEnv/2023       # Ne changez pas     
module load ansys/2023R2      # ou versions plus récentes

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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

```tab "Plusieurs nœuds (par nœud, Trillium)"
```bash title="script-flu-bynode-intel-tri.sh"
#!/bin/bash

#SBATCH --account=def-group      # Spécifiez le nom du compte
#SBATCH --time=00-03:00          # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --ntasks-per-node=16     # Spécifiez le nombre de cœurs par nœud (maximum 192 sur Trillium)
##SBATCH --mem=0                 # Ne décommentez pas (par défaut Trillium utilise toute la mémoire par nœud)
#SBATCH --cpus-per-task=1        # Ne changez pas (paramètre requis)

cd $SLURM_SUBMIT_DIR             # Soumettez depuis $SCRATCH/un/répertoire

module load StdEnv/2023          # Ne changez pas
module load ansys/2025R2.04      # seulement 2025R2 ou plus récent fonctionne sur Trillium

MYJOURNALFILE=sample.jou         # Spécifiez le nom de votre fichier journal
MYVERSION=3d                     # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

slurm_hl2hl.py --format ANSYS-FLUENT > $SLURM_SUBMIT_DIR/machinefile-$SLURM_JOB_ID
NCORES=$SLURM_NTASKS

if [ ! -L "$HOME/.ansys" ]; then
  echo "ERREUR : Un lien vers un répertoire .ansys accessible en écriture n'existe pas."
  echo 'Supprimez ~/.ansys s’il existe, puis exécutez : ln -s $SCRATCH/.ansys ~/.ansys'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
elif [ ! -L "$HOME/.fluentconf" ]; then
  echo "ERREUR : Un lien vers un répertoire .fluentconf accessible en écriture n'existe pas."
  echo 'Supprimez ~/.fluentconf s’il existe et exécutez : ln -s $SCRATCH/.fluentconf ~/.fluentconf'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
elif [ ! -L "$HOME/.flrecent" ]; then
  echo "ERREUR : Un lien vers un fichier .flrecent accessible en écriture n'existe pas."
  echo 'Supprimez ~/.flrecent s’il existe, puis exécutez : ln -s $SCRATCH/.flrecent ~/.flrecent'
  echo "Puis réessayez de soumettre votre tâche. Annulation de la tâche actuelle !"
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
```

#### Remise en file d'attente pour obtenir la licence

Les scripts suivants ne doivent être utilisés qu'avec des tâches *Fluent* qui sont connues pour se terminer normalement sans générer d'erreurs en sortie, mais qui nécessitent généralement plusieurs tentatives de remise en file d'attente pour obtenir les licences. Ils ne sont pas recommandés pour les tâches *Fluent* qui peuvent 1) s'exécuter pendant une longue période avant de planter 2) s'exécuter jusqu'à la fin mais contenir des avertissements de journalisation; dans les deux cas, les simulations seront répétées depuis le début jusqu'à ce que le nombre maximal de tentatives de remise en file d'attente spécifié par la valeur `array` soit atteint. Pour ces types de tâches, les scripts à usage général (ci-dessus) doivent être utilisés.

```tabs
```tab "Plusieurs nœuds (par nœud + remise en file d'attente)"
```bash title="script-flu-bynode+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (Narval 1 nœud maximum)
#SBATCH --ntasks-per-node=32  # Spécifiez le nombre maximum de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne changez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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
    echo "Tâche terminée avec succès ! Sortie maintenant."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT a échoué en raison d'un problème de licence ou de simulation !"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Nouvelle soumission de la tâche en cours..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie maintenant."
    fi
fi
```

```tab "Plusieurs nœuds (par cœur + remise en file d'attente)"
```bash title="script-flu-bycore+requeue.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval 1 nœud maximum)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne changez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de tentatives de remise en file d'attente (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYJOURNALFILE=sample.jou      # Spécifiez le nom de votre fichier journal
MYVERSION=3d                  # Spécifiez 2d, 2ddp, 3d ou 3ddp

# ------- Ne changez aucune ligne ci-dessous --------

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
    echo "Tâche terminée avec succès ! Sortie maintenant."
    scancel $SLURM_ARRAY_JOB_ID
else
    echo "Tentative de tâche $SLURM_ARRAY_TASK_ID sur $SLURM_ARRAY_TASK_COUNT a échoué en raison d'un problème de licence ou de simulation !"
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
       echo "Nouvelle soumission de la tâche en cours..."
    else
       echo "Toutes les tentatives de tâche ont échoué, sortie maintenant."
    fi
fi
```
```

#### Redémarrage

Les deux scripts suivants automatisent le redémarrage de tâches intensives qui exigent plus que le maximum de sept jours d'exécution permis sur la plupart des grappes. Le redémarrage se fait à partir des fichiers de pas de temps les plus récemment sauvegardés. Une exigence de base est que le premier pas puisse être terminé avant la fin du temps demandé dans le vecteur de tâches (défini dans le haut du script) quand une simulation est lancée à partir d'un champ initialisé. Nous supposons que la valeur du pas est fixe. Pour commencer, un groupe de `sample.cas`, `sample.dat` et `sample.jou` doit être présent. Modifiez le fichier `sample.jou` pour qu'il contienne `/solve/dual-time-iterate 1` et `/file/auto-save/data-frequency 1`. Créez ensuite un fichier journal avec `cp sample.jou sample-restart.jou` et modifiez le fichier `sample-restart.jou` pour qu'il contienne `/file/read-cas-data sample-restart` plutôt que `/file/read-cas-data sample` et mettez en commentaire la ligne pour l'initialisation en la précédant d’un point-virgule, par exemple `; /solve/initialize/initialize-flow`. Si votre deuxième pas et les pas qui suivent sont exécutés deux fois plus vite que le pas initial, modifiez `sample-restart.jou` en spécifiant `/solve/dual-time-iterate 2`. De cette façon, la solution ne sera redémarrée qu'après que les deux pas suivant le pas initial soient terminés. Un fichier de résultats pour chaque pas sera enregistré dans le sous-répertoire de sortie. La valeur 2 est arbitraire, mais elle devrait être utilisée pour que la durée de deux pas soit moindre que la durée allouée au vecteur de tâches. Ceci limitera le nombre de redémarrages, ce qui consomme beaucoup de ressources. Si le premier pas de `sample.jou` est fait à partir d'une solution précédente, choisissez 1 plutôt que 2 puisque tous les pas auront probablement besoin du même temps d'exécution. En supposant que 2 est choisi, la durée totale de la simulation sera `1*Dt+2*Nrestart*Dt` où `Nrestart` est le nombre de redémarrages défini dans le script Slurm. Le nombre total de pas (de même que le nombre de fichiers de résultats générés) sera ainsi `1+2*Nrestart`. La valeur pour le temps demandé devrait être choisie afin que le pas initial et les pas suivants se terminent dans la fenêtre de temps de Slurm, qui peut aller jusqu'à `#SBATCH --time=07-00:00` jours.

```tabs
```tab "Plusieurs nœuds (par nœud + redémarrage)"
```bash title="script-flu-bynode+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=07-00:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1             # Spécifiez le nombre de nœuds de calcul (Narval 1 nœud maximum)
#SBATCH --ntasks-per-node=32  # Spécifiez le nombre maximum de cœurs par nœud de calcul
#SBATCH --mem=0               # Spécifiez la mémoire par nœud de calcul (0 alloue toute la mémoire)
#SBATCH --cpus-per-task=1     # Ne changez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de redémarrages de solution (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYVERSION=3d                        # Spécifiez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Spécifiez le nom de votre fichier journal
MYJOUFILERES=sample-restart.jou     # Spécifiez le nom du fichier journal de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Spécifiez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Spécifiez le nom du fichier dat de redémarrage

# ------- Ne changez aucune ligne ci-dessous --------

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
      echo "Redémarrage de la tâche avec le fichier de données de sortie le plus récent..."
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Tâche terminée avec succès ! Sortie maintenant."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie..."
fi
```

```tab "Plusieurs nœuds (par cœur + redémarrage)"
```bash title="script-flu-bycore+restart.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
##SBATCH --nodes=1            # Décommentez pour spécifier (Narval 1 nœud maximum)
#SBATCH --ntasks=16           # Spécifiez le nombre total de cœurs
#SBATCH --mem-per-cpu=4G      # Spécifiez la mémoire par cœur
#SBATCH --cpus-per-task=1     # Ne changez pas
#SBATCH --array=1-5%1         # Spécifiez le nombre de redémarrages, aussi appelés pas de temps (2 ou plus, 5 est affiché)

module load StdEnv/2023       # Ne changez pas
module load ansys/2023R2      # Spécifiez la version (ou plus récente)

MYVERSION=3d                        # Spécifiez 2d, 2ddp, 3d ou 3ddp
MYJOUFILE=sample.jou                # Spécifiez le nom de votre fichier journal
MYJOUFILERES=sample-restart.jou     # Spécifiez le nom du fichier journal de redémarrage
MYCASFILERES=sample-restart.cas.h5  # Spécifiez le nom du fichier cas de redémarrage
MYDATFILERES=sample-restart.dat.h5  # Spécifiez le nom du fichier dat de redémarrage

# ------- Ne changez aucune ligne ci-dessous --------

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
  #export I_MPI_HYDRA_BOOTSTRAP=ssh    # décommentez sur Béluga ou Cedar
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -i $MYJOUFILE
  else
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pshmem -i $MYJOUFILERES
  fi
else 
  if [ "$SLURM_ARRAY_TASK_ID" == 1 ]; then
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILE
  else
    fluent -g $MYVERSION -t $NCORES -affinity=0 -mpi=intel -pib -cnf=/tmp/machinefile-$SLURM_JOB_ID -i $MYJOUFILERES
  fi
fi
if [ $? -eq 0 ]; then
    echo
    echo "SLURM_ARRAY_TASK_ID  = $SLURM_ARRAY_TASK_ID"
    echo "SLURM_ARRAY_TASK_COUNT = $SLURM_ARRAY_TASK_COUNT"
    echo
    if [ $SLURM_ARRAY_TASK_ID -lt $SLURM_ARRAY_TASK_COUNT ]; then
      echo "Redémarrage de la tâche avec le fichier de données de sortie le plus récent"
      ln -sfv output/$(ls -ltr output | grep .cas | tail -n1 | awk '{print $9}') $MYCASFILERES
      ln -sfv output/$(ls -ltr output | grep .dat | tail -n1 | awk '{print $9}') $MYDATFILERES
      ls -lh cavity* output/*
    else
      echo "Tâche terminée avec succès ! Sortie maintenant."
      scancel $SLURM_ARRAY_JOB_ID
     fi
else
     echo "Simulation échouée. Sortie maintenant."
fi
```
```

### Fichiers de journalisation

Les fichiers journaux peuvent contenir toutes les commandes de l'interface TUI (*Text User Interface*) de *Fluent*; elles peuvent être utilisées pour modifier des paramètres de simulation comme la température, la pression ou la vitesse du flux. Vous pouvez ainsi effectuer une série de simulations sous différentes conditions simplement en modifiant les paramètres du fichier journal. Consultez le guide d'utilisation de *Fluent* pour plus d'information ainsi que pour connaître la liste des commandes. Les fichiers qui suivent sont configurés avec `/file/cff-file no` pour utiliser les formats de fichiers `.cas/.dat` qui sont les formats par défaut pour les modules jusqu'à `2019R3`. Pour utiliser les formats `.cas.h5/.dat.h5` plus efficaces des versions à partir de `2020R1`, la configuration est `/file/cff-files yes`.

```tabs
```tab "Fichier journal (stable, cas)"
```text title="sample1.jou"
; FICHIER JOURNAL FLUENT D'EXEMPLE - SIMULATION STABLE
; ----------------------------------------------
; les lignes commençant par un point-virgule sont des commentaires

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire les fichiers de cas et de données en entrée
/file/read-case-data FFF-in

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; Écraser les fichiers de sortie par défaut
/file/confirm-overwrite n

; Écrire le fichier de données de sortie final
/file/write-case-data FFF-out

; Écrire le rapport de simulation dans un fichier (optionnel)
/report/summary y "My_Simulation_Report.txt"

; Arrêter Fluent proprement
/exit
```

```tab "Fichier journal (stable, cas + données)"
```text title="sample2.jou"
; EXEMPLE DE FICHIER JOURNAL - SIMULATION STABLE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire les fichiers d'entrée
/file/read-case-data FFF-in

; Écrire un fichier de données toutes les 100 itérations
/file/auto-save/data-frequency 100

; Conserver les fichiers de données des 5 itérations les plus récentes
/file/auto-save/retain-most-recent-files y

; Écrire les fichiers de données dans le sous-répertoire de sortie (ajoute l'itération)
/file/auto-save/root-name output/FFF-out

; Exécuter le solveur pour ce nombre d'itérations
/solve/iterate 1000

; écrire le dernier fichier de cas et de données en sortie
/file/write-case-data FFF-out

; enregistrer le rapport de la simulation (optionnel)
/report/summary y "My_Simulation_Report.txt"

; fermer correctement Fluent
exit
```

```tab "Fichier journal (temporaire)"
```text title="sample3.jou"
; EXEMPLE DE FICHIER JOURNAL - SIMULATION TEMPORAIRE
; ----------------------------------------------
; le point-virgule en début de ligne signale un commentaire

; Écraser les fichiers par défaut
/file/confirm-overwrite no

; Préférer la lecture/écriture des fichiers au format hérité
/file/cff-files no

; Lire le fichier de cas d'entrée
/file/read-case FFF-transient-inp

; Pour la continuation (redémarrage), lire les fichiers d'entrée de cas et de données
;/file/read-case-data FFF-transient-inp

; Écrire un fichier de données (et peut-être de cas) toutes les 100 pas de temps
/file/auto-save/data-frequency 100
/file/auto-save/case-frequency if-case-is-modified

; Ne conserver que les 5 fichiers de données (et peut-être de cas) les plus récents
/file/auto-save/retain-most-recent-files y

; Écrire dans le sous-répertoire de sortie (ajoute le temps de flux et le pas de temps)
/file/auto-save/root-name output/FFF-transient-out-%10.6f

; ##### Paramètres pour la simulation transitoire :  #####

; Définir la taille du pas de temps physique
/solve/set/time-step 0.0001

; Définir le nombre d'itérations pour lesquelles les moniteurs de convergence sont rapportés
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

; Arrêter Fluent proprement
/exit
```
```

### Fonctions UDF

La première étape est de transférer vers la grappe votre UDF (*User-Defined Function*), soit le fichier source `sampleudf.c` et tous les fichiers de dépendance supplémentaires. Lors du téléchargement à partir d'une machine *Windows*, assurez-vous que le mode texte de votre client de transfert est utilisé, sinon *Fluent* ne pourra pas lire correctement le fichier sur la grappe qui elle exécute *Linux*. L'UDF doit être placée dans le répertoire où résident vos fichiers journaux, cas et dat. Ajoutez ensuite l'une des commandes suivantes dans votre fichier journal avant les commandes qui lisent vos fichiers de simulation cas/dat. Que vous utilisiez l'approche UDF interprétée ou compilée, avant de télécharger votre fichier de cas, vérifiez que les boîtes de dialogue *Interpreted UDFs* et *UDF Library Manager* ne sont pas configurées pour utiliser une UDF; ceci garantira que lorsque les tâches sont soumises, seules les commandes du fichier journal auront le contrôle.

#### Interprété

Pour indiquer à *Fluent* d'interpréter votre UDF au moment de l'exécution, ajoutez la ligne de commande suivante dans votre fichier journal avant que les fichiers cas/dat ne soient lus ou initialisés. Remplacez le nom de fichier `sampleudf.c` par le nom de votre fichier source. La commande reste la même, que la simulation soit exécutée séquentiellement ou en parallèle. Pour vous assurer que l'UDF se trouve dans le même répertoire que le fichier journal, ouvrez votre fichier cas dans l'interface graphique *Fluent*, supprimez toutes les définitions gérées et réenregistrez-le. Cela garantira que seule la commande/méthode suivante est en contrôle lors de l'exécution de *Fluent*. Pour utiliser une UDF interprétée avec des tâches parallèles, elle devra être parallélisée comme décrit dans la section ci-dessous.

```bash
define/user-defined/interpreted-functions "sampleudf.c" "cpp" 10000 no
```

#### Compilé

Pour utiliser cette approche, votre UDF doit être compilée sur une de nos grappes au moins une fois. Cela créera une structure de sous-répertoire `libudf` contenant la bibliothèque partagée `libudf.so` requise. Le répertoire `libudf` ne peut pas être simplement copié d'un système distant (comme votre ordinateur portable) vers l'Alliance car les dépendances de la bibliothèque partagée ne seront pas satisfaites, ce qui fera planter *Fluent* au démarrage. Cela dit, une fois que vous avez compilé votre UDF sur une de nos grappes, vous pouvez transférer la `libudf` nouvellement créée vers n'importe quelle autre de nos grappes, à condition que votre compte charge la même version du module d'environnement *StdEnv*. Une fois copiée, l'UDF peut être utilisée en supprimant le commentaire de la deuxième ligne (load) `libudf` ci-dessous dans votre fichier journal quand une tâche est soumise. Les deux lignes `libudf` (compile et load) ne doivent pas être laissées sans commentaire lors de la soumission de tâches, sinon votre UDF sera automatiquement (re)compilée pour chaque tâche. Non seulement cette méthode est très inefficace, mais elle peut également entraîner des conflits de *build* de type « *racetime* » si plusieurs tâches sont exécutées à partir du même répertoire. Outre la configuration de votre fichier journal pour construire votre UDF, l'interface graphique de *Fluent* (exécutée sur n'importe quel nœud de calcul ou sur `gra-vdi`) peut également être utilisée. Pour ce faire, ajoutez le fichier source UDF dans la boîte de dialogue *Compiled UDFs*, et cliquez sur *Build*. Lorsque vous utilisez une UDF compilée avec des tâches parallèles, votre fichier source doit être parallélisé comme indiqué dans la section ci-dessous.

```bash
define/user-defined/compiled-functions compile libudf yes sampleudf.c "" ""
```
et/ou
```bash
define/user-defined/compiled-functions load libudf
```

#### Parallèle

Avant qu'une UDF puisse être utilisée avec une tâche parallèle *Fluent* (SMP à nœud unique et MPI à nœuds multiples), elle doit être parallélisée. En procédant ainsi, nous contrôlons comment/quels processus (hôte et/ou calcul) exécutent des parties spécifiques du code UDF lorsque *Fluent* est exécuté en parallèle sur la grappe. La procédure d'instrumentation consiste à ajouter des directives de compilation, des prédicats et des macros de réduction dans votre UDF séquentielle. Si vous ne le faites pas, *Fluent* fonctionnera lentement au mieux ou plantera immédiatement au pire. Le résultat final sera une UDF unique qui s'exécute efficacement lorsque *Fluent* est utilisé à la fois en mode séquentiel et en mode parallèle. Le sujet est décrit en détail dans *Fluent Customization Manual, Part I: Chapter 7: Parallel Considerations* qui se trouve dans la [Documentation en ligne](#documentation-en-ligne).

#### DPM

Les UDF peuvent être utilisées pour personnaliser les modèles de phase discrète (DPM pour *Discrete Phase Models*) comme décrit dans *2024R2 Fluent Users Guide, Part III: Solution Mode, Chapter 24: Modeling Discrete Phase, 24.2 Steps for Using the Discrete Phase Models,* et dans *2024R2 Fluent Customization Manual, Part I: Creating and Using User Defined Functions, Chapter 2: DEFINE Macros, 2.5 Discrete Phase Model (DPM) DEFINE Macros*. Avant qu'une UDF basée sur DMP puisse être utilisée dans une simulation, l'injection d'un ensemble de particules doit être définie en spécifiant des *Point Properties* avec des variables telles que la position de la source, la trajectoire initiale, le débit massique, la durée, la température, etc., en fonction du type d'injection. Cela peut être fait dans l'interface graphique en cliquant sur le panneau *Physics --> Discrete Phase*, puis en cliquant sur le bouton *Injections*. Cela ouvrira la boîte de dialogue *Injections* dans laquelle une ou plusieurs injections peuvent être créées en cliquant sur le bouton *Create*. La boîte de dialogue *Set Injection Properties* contient le menu déroulant *Injection Type* avec les quatre premiers types disponibles (*single, group, surface, flat-fan-atomizer*). Si vous sélectionnez l'un de ces types, vous pouvez alors sélectionner l'onglet *Point Properties* pour saisir les champs de valeurs correspondants. Une autre façon de spécifier les *Point Properties* serait de lire un fichier texte d'injection. Pour ce faire, sélectionnez *File* dans le menu déroulant *Injection Type*, spécifiez le nom de l'injection à créer, puis cliquez sur le bouton *File* (situé à côté du bouton *OK* en bas de la boîte de dialogue *Set Injection Properties*). Ici, vous pouvez sélectionner un fichier d'échantillon d'injection (avec l'extension `.dpm`) ou un fichier texte d'injection créé manuellement. Pour ce faire, dans la boîte de dialogue *Select File*, sélectionnez *All Files (*)*, puis mettez en surbrillance le fichier qui pourrait avoir n'importe quel nom arbitraire mais qui a généralement une extension `.inj`; cliquez sur le bouton *OK*. En supposant qu'il n'y ait aucun problème avec le fichier, aucun message d'erreur ou d'avertissement de la console n'apparaîtra dans *Fluent*. Lorsque vous serez retourné à la boîte de dialogue *Injection*, vous devriez voir le même nom d'injection que celui que vous avez spécifié dans la boîte de dialogue *Set Injection Properties* et pouvoir répertorier ses particules et propriétés dans la console. Ouvrez ensuite la boîte de dialogue *Discrete Phase Model* et sélectionnez *Interaction with Continuous Phase* qui permettra de mettre à jour les termes sources DPM à chaque itération de flux. Ce paramètre peut être enregistré dans votre fichier cas ou ajouté via le fichier journal comme indiqué. Une fois que l'injection est confirmée comme fonctionnant dans l'interface graphique, les étapes peuvent être automatisées en ajoutant des commandes au fichier journal après l'initialisation de la solution, par exemple :

```bash
/define/models/dpm/interaction/coupled-calculations yes
/define/models/dpm/injections/delete-injection injection-0:1
/define/models/dpm/injections/create injection-0:1 no yes file no zinjection01.inj no no no no
/define/models/dpm/injections/list-particles injection-0:1
/define/models/dpm/injections/list-injection-properties injection-0:1
```
où un format de fichier stable d'injection de base créé manuellement pourrait ressembler à :
```text
$ cat zinjection01.inj
(z=4 12)
( x y z u v w diamètre t débit massique fréquence massique temps nom )
(( 2.90e-02 5.00e-03 0.0 -1,00e-03 0,0 0,0 1,00e-04 2,93e+02 1,00e-06 0,0 0,0 0,0 ) injection-0:1 )
```
notant que les fichiers d'injection pour les simulations DPM sont généralement configurés pour un suivi stationnaire ou instable de particules, le format du premier étant décrit dans *2024R2 Fluent Customization Manual, Part III: Solution Mode | Chapter 24: Modeling Discrete Phase | 24.3. Setting Initial Conditions for the Discrete Phase | 24.3.13 Point Properties for File Injections | 24.3.13.1 Steady File Format*.

## CFX

### Scripts pour l'ordonnanceur Slurm

Le résumé des options de ligne de commande peut être affiché avec `cfx5solve -help`. La version du module chargée dans votre script pour l'ordonnanceur doit d'abord être chargée manuellement. Par défaut, `cfx5solve` s'exécute en simple précision (`-single`). Pour exécuter `cfx5solve` en double précision, ajoutez l'option `-double`, sachant que cela doublera également les besoins en mémoire. Par défaut, `cfx5solve` prend en charge les maillages jusqu'à 80 millions d'éléments structurés ou 200 millions d'éléments non structurés. Pour les maillages plus grands (jusqu'à 2 milliards d'éléments), ajoutez l'option `-large`. Différentes combinaisons de ces options peuvent être utilisées pour le partitionneur, l'interpolateur ou le solveur. Consultez le guide d'*ANSYS CFX-Solver Manager* pour plus de détails.

```tabs
```tab "Nœud simple"
```bash title="script-local.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=1             # Spécifiez un seul nœud de calcul (ne changez pas)
#SBATCH --ntasks-per-node=4   # Spécifiez le nombre de cœurs (maximum : Graham 44, Cedar 32 ou 48, Béluga 40, Narval 64)
#SBATCH --mem=16G             # Spécifiez la mémoire du nœud (optionnellement à 0 pour allouer toute la mémoire du nœud)
#SBATCH --cpus-per-task=1     # Ne changez pas

#module load StdEnv/2020      # Décommentez pour utiliser (obsolète)     
#module load 2021R2           # Spécifiez 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Ou versions de module plus récentes

# Ajoutez des options de ligne de commande cfx5solve supplémentaires au besoin
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
else
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Local Parallel" -part $SLURM_CPUS_ON_NODE
fi
```

```tab "Plusieurs nœuds"
```bash title="script-cfx-multiple.sh"
#!/bin/bash

#SBATCH --account=def-group   # Spécifiez le nom du compte
#SBATCH --time=00-03:00       # Spécifiez la durée JJ-HH:MM
#SBATCH --nodes=2             # Spécifiez plusieurs nœuds de calcul (2 ou plus)
#SBATCH --ntasks-per-node=64  # Spécifiez tous les cœurs par nœud (maximum : Graham 44, 48, Béluga 40, Narval 64)
#SBATCH --mem=0               # Utilisez toute la mémoire par nœud de calcul (ne changez pas)
#SBATCH --cpus-per-task=1     # Ne changez pas

#module load StdEnv/2020      # Décommentez pour utiliser (obsolète)     
#module load 2021R2           # Spécifiez 2021R2 seulement

module load StdEnv/2023
module load ansys/2023R2      # Spécifiez 2022R2 ou versions de module plus récentes

NNODES=$(slurm_hl2hl.py --format ANSYS-CFX)

# Ajoutez des options de ligne de commande cfx5solve supplémentaires au besoin
if [[ "$CC_CLUSTER" = narval ]]; then
  cfx5solve -def YOURFILE.def -start-method "Open MPI Distributed Parallel" -par-dist $NNODES
else
  export I_MPI_HYDRA_BOOTSTRAP=ssh
  unset I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS
  cfx5solve -def YOURFILE.def -start-method "Intel MPI Distributed Parallel" -par-dist $NNODES
fi
```
```

## Workbench

Il est possible d'exécuter vos simulations *Workbench* directement à partir de l'interface graphique native de *Workbench* pour une option plus intuitive, plutôt que de soumettre la tâche à la file d'attente avec un script Slurm. Une session de bureau *OnDemand* peut maintenant être réservée sur un nœud de calcul avec jusqu'à 96 cœurs, 768 Go de mémoire et 8 heures d'exécution.

Initialisez le fichier de projet avant de le soumettre pour la première fois.
1.  Connectez-vous à la grappe avec [TigerVNC](../interactive/vnc.md#nœuds-de-calcul).
2.  Dans le même répertoire où se trouve le fichier de projet (`YOURPROJECT.wbpj`), lancez *Workbench* avec la même version du module Ansys qui a servi à créer le projet.
3.  Dans *Workbench*, ouvrez le projet avec *File -> Open*.
4.  Dans la fenêtre principale, faites un clic droit sur *Setup* et sélectionnez *Clear All Generated Data*.
5.  Dans la liste déroulante de la barre de menus du haut, cliquez sur *File -> Exit* pour sortir de *Workbench*.
6.  Dans la fenêtre contextuelle *Ansys Workbench* qui affiche *The current project has been modified. Do you want to save it ?* cliquez sur le bouton *No*.
7.  Quittez *Workbench* et soumettez la tâche avec un des scripts ci-dessous.

### Scripts pour l'ordonnanceur Slurm

Pour soumettre un fichier de projet à la file d'attente, personnalisez les scripts suivants et lancez la commande `sbatch script-wbpj-202X.sh`.

```tabs
```tab "Nœud unique (StdEnv/2023)"
```bash title="script-wbpj-2023.sh"
#!/bin/bash

#SBATCH --account=def-account      # Spécifiez le compte
#SBATCH --time=00-03:00            # Durée (JJ-HH:MM)
#SBATCH --mem=16G                  # Mémoire totale (0 pour toute la mémoire du nœud)
#SBATCH --ntasks=4                 # Nombre de cœurs
#SBATCH --nodes=1                  # Ne changez pas (multi-nœuds non pris en charge)
##SBATCH --exclusive               # Décommentez pour les tests de scalabilité
##SBATCH --constraint=broadwell    # Applicable à Graham ou Cedar

module load StdEnv/2023 ansys/2023R2   # OU versions de module Ansys plus récentes

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Définir à 0 pour SMP (mémoire parallèle partagée)
else
  MEMPAR=1                             # Définir à 1 pour DMP (mémoire parallèle distribuée)
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

```tab "Nœud unique (StdEnv/2020)"
```bash title="script-wbpj-2020.sh"
#!/bin/bash

#SBATCH --account=def-account
#SBATCH --time=00-03:00                # Durée (JJ-HH:MM)
#SBATCH --mem=16G                      # Spécifiez la mémoire totale
#SBATCH --ntasks=4                     # Spécifiez le nombre de cœurs
#SBATCH --nodes=1                      # Ne changez pas (multi-nœuds non pris en charge)
##SBATCH --exclusive                   # Décommentez UNIQUEMENT pour les tests de scalabilité
##SBATCH --constraint=broadwell        # Décommentez pour spécifier un type de nœud disponible

module load StdEnv/2020 ansys/2021R2   # OU versions de module Ansys plus récentes

if [ "$SLURM_NNODES" == 1 ]; then
  MEMPAR=0                             # Définir à 0 pour SMP (mémoire parallèle partagée)
else
  MEMPAR=1                             # Définir à 1 pour DMP (mémoire parallèle distribuée)
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
```

Pour éviter d'écrire la solution lorsqu'une tâche en cours d'exécution se termine avec succès, changez `Save(Overwrite=True)` en `Save(Overwrite=False)` dans la dernière ligne du script Slurm ci-dessus. Cela facilitera la détermination de la scalabilité de la simulation lorsque `#SBATCH --ntasks` est augmenté, car la solution initialisée ne sera pas écrasée par chaque tâche de test.

## Mechanical

Le fichier d'entrée peut être généré dans votre session interactive *Workbench Mechanical* en cliquant sur *Solution -> Tools -> Write Input Files* et en spécifiant *File name:* pour `YOURAPDLFILE.inp` et *Save as type:* pour les fichiers APDL en entrée (`*.inp`). Les tâches APDL peuvent ensuite être soumises à la file d'attente avec la commande `sbatch script-name.sh`.

### Scripts pour l'ordonnanceur Slurm

Les scripts suivants ont été testés sur Graham, Narval, Cedar et Béluga. Les lignes qui commencent par `##SBATCH` sont suivies d'un commentaire.

```tabs
```tab "Mémoire parallèle partagée (CPU)"
```bash title="script-smp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez votre compte
#SBATCH --time=00-03:00         # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem=32G               # Spécifiez la mémoire pour tous les cœurs
#SBATCH --nodes=1               # Ne changez pas
#SBATCH --tasks=8               # Spécifiez le nombre de cœurs
#SBATCH --cpus-per-task=1       # Ne changez pas

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

mapdl -smp -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID -i YOURAPDLFILE.inp
```

```tab "Mémoire parallèle distribuée (CPU)"
```bash title="script-dmp-2023-cpu.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez votre compte
#SBATCH --time=00-03:00         # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G        # Spécifiez la mémoire par cœur
##SBATCH --nodes=2              # Spécifiez le nombre de nœuds (optionnel)
#SBATCH --ntasks=8              # Spécifiez le nombre de cœurs
##SBATCH --ntasks-per-node=4    # Spécifiez les cœurs par nœud (optionnel)
#SBATCH --cpus-per-task=1       # Ne changez pas

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

```tab "Mémoire parallèle partagée (GPU)"
```bash title="script-smp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez votre compte
#SBATCH --time=00-03:00          # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem=32G                # Spécifiez la mémoire pour tous les cœurs
#SBATCH --ntasks=8               # Spécifiez le nombre de cœurs
#SBATCH --nodes=1                # Ne changez pas
#SBATCH --cpus-per-task=1        # Ne changez pas
#SBATCH --gpus-per-node=1        # Spécifiez [typeGPU:]quantité
##SBATCH --gpus-per-node=h100:1  # Requis temporairement sur Mini-Graham
##SBATCH --partition=debug       # Requis temporairement sur Mini-Graham

module load StdEnv/2023
#module load ansys/2023R2
module load ansys/2024R1.03

mkdir outdir-$SLURM_JOBID
[[ "$CC_CLUSTER" = cedar ]] && export LD_LIBRARY_PATH=$EBROOTGCC/../lib/gcc

export ANSGPU_PRINTDEVICES=1
mapdl -smp -acc nvidia -na $SLURM_GPUS_ON_NODE -b nolist -np $SLURM_NTASKS -dir outdir-$SLURM_JOBID  -i YOURAPDLFILE.inp
```

```tab "Mémoire parallèle distribuée (GPU)"
```bash title="script-dmp-2023-gpu.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez votre compte
#SBATCH --time=00-03:00          # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem-per-cpu=4G         # Spécifiez la mémoire par cœur
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds
#SBATCH --ntasks-per-node=8      # Spécifiez les cœurs par nœud
#SBATCH --cpus-per-task=1        # Ne changez pas
#SBATCH --gpus-per-node=1        # Spécifiez [typeGPU:]quantité
##SBATCH --gpus-per-node=h100:1  # Requis temporairement sur Mini-Graham
##SBATCH --partition=debug       # Requis temporairement sur Mini-Graham

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
```

Par défaut, Ansys alloue aux tâches APDL `1024Mo` de mémoire totale et `1024Mo` de mémoire pour les bases de données. Ces valeurs peuvent être définies manuellement (ou modifiées) avec l'ajout des arguments `-m 1024` et/ou `-db 1024` sur la dernière ligne de commande `mapdl` des scripts ci-dessus. Si vous utilisez à distance un serveur de licences de votre établissement qui a plusieurs licences Ansys, il pourrait être nécessaire d'ajouter des arguments comme `-p aa_r` ou `-ppf anshpc`, selon le module que vous utilisez. Comme d'habitude, effectuez des tests détaillés de scalabilité avant de lancer des tâches en production pour vous assurer que vous utilisez le nombre optimal de cœurs et la bonne quantité minimale de mémoire. Les scripts pour nœud simple avec mémoire parallèle partagée (SMP pour *Shared Memory Parallel*) offriront une meilleure performance que les scripts pour plusieurs nœuds avec mémoire parallèle distribuée (DMP pour *Distributed Memory Parallel*) et devraient être utilisés autant que possible. Pour prévenir les problèmes de compatibilité, le module qui est chargé dans votre script devrait idéalement correspondre à la version employée pour générer le fichier en entrée.

```bash
[gra-login2:~/testcase] cat YOURAPDLFILE.inp | grep version
```

```text
! ANSYS input file written by Workbench version 2019 R3
```

## Rocky

Cette section fournit des exemples de scripts Slurm pour résoudre des simulations *Rocky* autonomes non couplées dans une file d'attente de grappe. Les deux scripts sont configurés avec `RESUME=0` afin que les simulations soient résolues depuis le début par défaut. Pour redémarrer une simulation partiellement terminée, définissez `RESUME=1` et soumettez à nouveau le script à la file d'attente. Pour obtenir une liste complète des options de ligne de commande, exécutez `Rocky -h` sur la ligne de commande après avoir chargé le module Ansys. Puisqu'un fichier de verrouillage est généré chaque fois qu'une simulation est démarrée, une seule tâche doit être soumise à la fois à partir du même répertoire. Concernant le script à utiliser, bien que toutes les simulations doivent être testées indépendamment, pour un cas de test de base, le script uniquement basé sur le GPU a été jugé plus performant que le script uniquement basé sur le CPU par un facteur de 3,5x. Des augmentations supplémentaires des ressources au-delà de `6cpu` (pour le script uniquement CPU) ou `2cpu + 1g` (1/7 d'un GPU `H100` pour le script basé sur le GPU) n'ont pas fourni d'accélération supplémentaire selon les tests de scalabilité pour l'un ou l'autre script. Compte tenu de ces résultats, il semble probable que le script basé sur le GPU fournira des temps de solution significativement plus rapides que l'utilisation de seulement des processeurs pour d'autres simulations *Rocky* autonomes. Comme indiqué sur chaque page wiki de grappe ou résumé sur [https://docs.alliancecan.ca/wiki/Allocations_and_compute_scheduling#Ratios_in_bundles](https://docs.alliancecan.ca/wiki/Allocations_and_compute_scheduling#Ratios_in_bundles), toutes les grappes sauf Narval ont des GPU `H100`. Par conséquent, lors de l'utilisation du script GPU sur Narval, l'option Slurm `--gpus` devrait être modifiée pour demander un GPU `a100` à la place. Notez qu'à l'heure actuelle, seul *Rocky* avec les modules `ansys/2025R2|2.04` a été testé, mais pas encore les modules `ansys/2025R1|1.02`.

### Scripts pour l'ordonnanceur Slurm

```tabs
```tab "CPU seulement"
```bash title="script-rocky-cpu.sh"
#!/bin/bash

#SBATCH --account=account      # Spécifiez votre compte (def ou rrg)
#SBATCH --time=00-02:00        # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem=24G              # Spécifiez la mémoire totale pour les cœurs
#SBATCH --cpus-per-task=6      # Spécifiez le nombre de cœurs à utiliser
#SBATCH --nodes=1              # Demandez un nœud (ne changez pas)

module load StdEnv/2023 ansys/2025R1       # ou versions plus récentes
export PATH=$EBROOTANSYS/v251/rocky:$PATH

Rocky --simulate “mysim.rocky” --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=0
```

```tab "Avec GPU"
```bash title="script-rocky-gpu.sh"
#!/bin/bash

#SBATCH --account=account      # Spécifiez votre compte (def ou reg)
#SBATCH --time=00-01:00        # Spécifiez la durée (JJ-HH:MM)
#SBATCH --mem=24G              # Spécifiez la mémoire (0 pour utiliser toute la mémoire du nœud)
#SBATCH --cpus-per-task=6      # Spécifiez les cœurs (Graham 32 ou 44 pour utiliser tous les cœurs)
#SBATCH --gres=gpu:v100:2      # Spécifiez le type de GPU : la quantité de GPU
#SBATCH --nodes=1              # Demandez un nœud (ne changez pas)

# Le module rocky2023R2 sur Graham a été renommé ansysrocky/2023R2 le 24 avril 2025
#module load ansysrocky/2023R2 StdEnv/2020 ansys/2023R2       # disponible uniquement sur Graham
module load ansysrocky/2024R2.0 StdEnv/2023 ansys/2024R2.04   # disponible uniquement sur Graham

RESUME=0                                  # Spécifiez 0 ou 1
if [ $RESUME -eq 0 ]; then
  rm -rf $INPUTFILE.files/simulation      # Supprime les résultats précédents
  Rocky --headless --simulate --resume=0 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE $INPUTFILE
else
  Rocky --headless --simulate --resume=1 --ncpus=$SLURM_CPUS_PER_TASK --use-gpu=1 --gpu-num=$SLURM_GPUS_ON_NODE $INPUTFILE
fi
```
```

## Electronics

Les scripts Slurm pour utiliser *Ansys EDT* sont fournis sur une page wiki séparée [ici](ansysedt.md).

## Mode graphique

Les programmes Ansys fonctionnent interactivement en mode graphique sur les nœuds de calcul des grappes ou sur les nœuds VDI de Graham.

*   [NIBI](https://docs.alliancecan.ca/wiki/nibi.md#access-through-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
*   [FIR](https://docs.alliancecan.ca/wiki/fir.md) : `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](https://jupyterhub.rorqual.alliancecan.ca) : `https://jupyterhub.rorqual.alliancecan.ca`
*   [NARVAL](https://jupyterhub.narval.alliancecan.ca/) : `https://jupyterhub.narval.alliancecan.ca/`
*   [TRILLIUM](https://docs.scinet.utoronto.ca/index.php/Open_OnDemand_Quickstart) : `https://ondemand.scinet.utoronto.ca`

Une page web de soumission de tâches devrait apparaître dans votre navigateur. Configurez les ressources requises pour votre session de bureau interactive et cliquez sur *Launch* ou *Start*. Si des graphiques accélérés ou des calculs seront effectués depuis votre session de bureau, assurez-vous de spécifier une ressource GPU. Une fois le bureau chargé, chargez un module Ansys. Si vous avez démarré un bureau alimenté par *Jupyter Lab*, cela peut être fait en cliquant sur le menu de gauche, ou si vous avez démarré un bureau *OnDemand*, tapez manuellement `module load ansys/version` sur la ligne de commande. Pour démarrer l'un des programmes Ansys courants tels que *Fluent*, *CFX*, *Workbench* et ainsi de suite, reportez-vous à la section suivante qui fournit des conseils pour la définition des variables d'environnement et des arguments requis par les environnements graphiques basés sur *VirtualGL* ou *Mesa*, selon qu'une ressource GPU a été spécifiée ou non.

### Fluent

Pour démarrer *Ansys Fluent* à partir de la ligne de commande d'un bureau *OnDemand*, ouvrez une fenêtre de terminal et exécutez les commandes :

```bash
module load StdEnv/2023 ansys/2025R1
fluent
```

Lorsque le panneau de sélection contextuel *Fluent Launcher* apparaît, cliquez sur l'onglet *Environment* et copiez/collez les paramètres de variables d'environnement suivants, selon que vous avez démarré votre session *OnDemand* avec un GPU pour l'accélération graphique. N'incluez pas le texte entre parenthèses (car ce sont des commentaires) et ne mettez pas `export` devant les noms de variables. Si la fenêtre de la console graphique est corrompue au démarrage de l'interface graphique, redémarrez *Fluent* en définissant `HOOPS_PICTURE=null` pour désactiver la création du panneau *Graphics*.

**Nœud de calcul (aucun GPU demandé)**

*   `I_MPI_HYDRA_BOOTSTRAP=ssh` (requis sur Nibi)
*   `HOOPS_PICTURE=opengl2-mesa` (version `2025R1` ou plus récente)
*   `HOOPS_PICTURE=null` (version `2024R2` ou plus ancienne)
*   Cliquez sur le bouton *Start*.

!!! note
    Lorsque vous exécutez *Fluent* sur la grappe Nibi, la variable d'environnement `I_MPI_HYDRA_BOOTSTRAP=ssh` doit être définie manuellement ; sinon, *Fluent* plantera au démarrage à l'intérieur des sessions de bureau de calcul *OOD* lorsque `intelmpi` est utilisé. Un message d'erreur tel que le suivant sera créé. Si cela se produit, quittez complètement *Fluent*, arrêtez *Workbench* proprement et recommencez.
    ```text
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

### CFX

Lors du démarrage de *CFX* à partir d'un bureau *OnDemand*, les arguments suivants peuvent être spécifiés sur la ligne de commande de la fenêtre de terminal selon qu'un GPU a été demandé ou non au démarrage du bureau.

*   `module load StdEnv/2023 ansys/2025R1` (ou plus ancien)
*   `cfx5 -graphics mesa` (aucun GPU demandé)
*   `cfx5 -graphics ogl` (avec GPU demandé)

### Mapdl

Les étapes suivantes pour démarrer l'interface graphique *Mechanical APDL* à partir de la ligne de commande d'une fenêtre de terminal devraient fonctionner, que vous ayez démarré votre bureau *OnDemand* sur un nœud de calcul avec ou sans GPU.

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `mapdl -g`, ou
*   `launcher` puis cliquez sur le bouton *RUN*

### Workbench

Cette section montre comment démarrer *Workbench* (et éventuellement *Fluent*) sur un bureau *OnDemand* ou *Jupyter Lab*.

*   `module load StdEnv/2023 ansys/2022R2` (ou versions plus récentes)
*   `xfwm4 --replace &` (nécessaire seulement si vous utilisez Ansys *Mechanical*)
*   `export QTWEBENGINE_DISABLE_SANDBOX=1` (nécessaire seulement si vous utilisez *CFD-Post*)
*   `runwb2`

!!! note
    Quand vous exécutez en parallèle un programme d'analyse comme *Mechanical* ou *Fluent* sur un nœud simple, ne cochez pas la case *Distributed* et indiquez un nombre de cœurs égal à votre **session salloc, moins 1**. Les menus déroulants du *Ansys Mechanical Workbench* ne répondent pas correctement. Comme solution, lancez `xfwm4 --replace` sur la ligne de commande avant de démarrer *Workbench*. Pour avoir `xfwm4` par défaut, modifiez `~/.vnc/xstartup` et remplacez `mate-session` par `xfce4-session`.

**Nœud de calcul (aucun GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu latéral gauche du bureau.
*   Cliquez sur l'icône "Workbench (VNC)" située dans la fenêtre centrale du bureau *Jupyter Lab*.
    *   Si les graphiques d'une application (telle que *Fluent*) démarrée dans *Workbench* apparaissent inutilisables en raison de graphiques corrompus, essayez d'effectuer les étapes suivantes. Elles créeront une icône de bureau `runwb2` personnalisée afin que *Workbench* puisse être démarré en mode *Mesa*. Si l'une des applications que vous allez démarrer dans *Workbench* est *Fluent*, alors lorsque le *Fluent launcher* démarre, vous pouvez également essayer de définir la variable `HOOPS_PICTURE=opengl2-mesa` dans la fenêtre *Fluent Launcher*.
*   Pour continuer, quittez *Workbench* puis ouvrez une fenêtre de terminal. Copiez-collez la commande suivante dans le presse-papiers distant situé dans le coin supérieur droit de votre bureau *Jupyter*.
*   Maintenant, les commandes peuvent être collées dans le terminal, c'est-à-dire :
    `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop`
*   Ouvrez le fichier nouvellement créé dans un éditeur de texte tel que `nano` en faisant ce qui suit :
    `nano ~/Desktop/workbench-mesa.desktop`. Modifiez toutes les instances de `runwb2` en `runwb2 -oglmesa` puis quittez l'éditeur en sauvegardant les modifications. Maintenant, ACTUALISEZ le bureau *Jupyter* en appuyant sur la combinaison de touches *Ctrl-R*. La nouvelle icône devrait maintenant apparaître sur le bureau avec l'icône *Workbench* d'origine. Double-cliquez dessus pour démarrer *Workbench*. La nouvelle icône persistera pour les futures sessions jusqu'à ce qu'elle soit supprimée manuellement avec la commande `rm -f ~/Desktop/workbench-mesa.desktop`.

**Nœud de calcul (avec GPU demandé)**

*   Cliquez pour charger `ansys/2025R1` (ou une version plus récente) dans le menu latéral gauche du bureau.
*   Cliquez sur l'icône *Workbench (VNC)* située dans la fenêtre centrale du bureau *Jupyter Lab*.

### Ansys EDT

*   Ouvrez une fenêtre de terminal et chargez le module avec
    *   `module load SnEnv ansysedt/2023R2`, ou
    *   `module load SnEnv ansysedt/2021R2`
*   Dans le terminal, entrez `ansysedt` et attendez que l'interface s'affiche.
*   Ceci doit être fait une seule fois :
    *   sélectionnez *Tools -> Options -> HPC and Analysis Options -> Options*
    *   dans le menu déroulant, changez *HPC License* pour **Pool** (pour utiliser plus de 4 cœurs)
    *   cliquez sur *OK*
*   ---------- EXEMPLES ----------
*   Pour copier dans votre compte les exemples *Antennas* de `2023R2` :
    *   connectez-vous à une grappe (par exemple Graham)
    *   `module load ansysedt/2023R2`
    *   `mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; cd ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf Antennas`
    *   `cp -a $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas ~/Ansoft/$EBVERSIONANSYSEDT`
*   Pour faire exécuter un exemple :
    *   ouvrez un fichier `.aedt` et cliquez sur *HFSS -> Validation Check*
    *   (si la validation produit une erreur, fermez et ouvrez de nouveau la simulation autant de fois que nécessaire)
    *   pour lancer la simulation, cliquez sur *Project -> Analyze All*
    *   pour quitter sans sauvegarder la solution, cliquez sur *File -> Close -> No*
*   si le programme plante et ne repart pas, essayez les commandes suivantes :
    *   `pkill -9 -u $USER -f "ansys*|mono|mwrpcss|apip-standalone-service"`
    *   `rm -rf ~/.mw` (au lancement, `ansysedt` utilisera la configuration initiale)

### Ensight

*   `module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6`
*   `export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib`
*   `ensight -X`

## Problèmes avec SSH

Certains programmes d'interface graphique Ansys peuvent être exécutés à distance sur un nœud de calcul d'une de nos grappes par redirection X via SSH vers votre ordinateur local. Contrairement à VNC, cette approche n'est ni testée ni prise en charge car elle repose sur un serveur d'affichage X correctement configuré pour votre système d'exploitation particulier OU sur la sélection, l'installation et la configuration d'un paquet d'émulateur client X approprié tel que *MobaXterm*. La plupart d'entre vous trouverez les temps de réponse interactifs inacceptables pour les tâches de menu de base, sans parler de l'exécution de tâches plus complexes telles que celles nécessitant du rendu graphique. Les temps d'attente pour démarrer des programmes avec interface graphique peuvent également être très longs, dépendant de votre connexion Internet. Dans un test par exemple, il a fallu 40 minutes pour obtenir l'interface graphique avec SSH alors que `vncviewer` n'a pris que 34 secondes. Malgré la lenteur potentielle lors de la connexion via SSH pour exécuter des programmes avec interface graphique, cela peut toujours être intéressant si votre seul objectif est d'ouvrir une simulation et d'effectuer des opérations de menu de base ou d'exécuter des calculs. Ces étapes de base sont un point de départ : 1) `ssh -Y username@graham.computecanada.ca`; 2) `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task =4 [--gpus-per-node=1] --account=def-mygroup`; 3) une fois connecté à un nœud de calcul, essayez d'exécuter `xclock`. Si l'horloge apparaît sur votre bureau, chargez le module Ansys souhaité et essayez d'exécuter le programme.

### Fluids

*   `module load CcEnv StdEnv/2023`
*   `module load ansys/2024R2.04` (ou versions moins récentes)
*   `unset SESSION_MANAGER`
*   `fluent | cfx5 | icemcfd`
    *   La commande `unset SESSION_MANAGER` permet d'éviter le message d'erreur suivant au lancement de *Fluent*.
    *   `Qt: Session management error: None of the authentication protocols specified are supported`
    *   Si le message suivant est affiché au lancement de `icemcfd`...
    *   `Error segmentation violation - exiting after doing an emergency save`
    *   ... ne cliquez pas sur le bouton *OK*, autrement `icemcfd` va planter. Faites plutôt ce qui suit (une seule fois) :
    *   sélectionnez *Settings Tab -> Display -> tick X11 -> Apply -> OK -> File -> Exit*
    *   L'erreur ne devrait pas se produire quand vous démarrez de nouveau `icemcfd`.

### Workbench

### Rocky

*   `module load clumod ansysrocky/2023R2 CcEnv StdEnv/2020 ansys/2023R2`, ou
*   `module load clumod ansysrocky/2024R2.0 CcEnv StdEnv/2023 ansys/2024R2.04`, ou
*   `module load CcEnv StdEnv/2023 ansys/2025R1`
*   `Rocky` Le module Ansys lit `~/licenses/ansys.lic`.
*   `Rocky-gui` Cette option des modules locaux `ansysrocky` permet de sélectionner un serveur CMC ou SHARCNET.
*   `RockySolver` Lance le solveur directement de la ligne de commande (l'ajout de `-h` pour *help* n'est pas testé).
*   `RockyScheduler`, gestionnaire de ressources pour soumettre plusieurs tâches sur le nœud courant (non testé).
*   Les versions `2024R2` ou moins récentes ne fonctionnent que sur `gra-vdi` et les grappes Graham; l'installation sur les autres grappes est prévue pour juin.
*   Les versions `2025R1` et plus récentes sont fournies dans le module Ansys sur toutes les grappes (pas encore prises en charge par le serveur de licences SHARCNET).
*   Le serveur de licences SHARCNET inclut *Rocky*; son utilisation est gratuite pour la recherche.
*   *Rocky* prend en charge le calcul accéléré avec GPU (non testé, non documenté).
*   Pour demander un nœud de calcul sur Graham pour utilisation interactive avec 4 processeurs et 1 GPU pour un maximum de 8 heures, lancez
    `salloc --time=08:00:00 --nodes=1 --cpus-per-task=4 --gres=gpu:v100:1 --mem=32G --account=someaccount`

### Mapdl

*   `module load CcEnv StdEnv/2023`
*   `ansys/2024R2.04` (ou versions plus anciennes)
*   `mapdl -g` (pour démarrer l'interface graphique directement), ou
*   `unset SESSION_MANAGER; launcher -> click RUN button`

## Particularités selon le site d'utilisation

### Licence SHARCNET

La licence Ansys de SHARCNET est gratuite pour un usage académique par les chercheurs et chercheuses de l'Alliance sur les systèmes de l'Alliance. Le logiciel installé n'a pas de limites de solveur ou de géométrie. La licence SHARCNET peut **uniquement** être utilisée à des fins de **recherche universitaire publiable**; la production de résultats à des fins commerciales privées est strictement interdite, comme stipulé par la licence. La licence Ansys a été mise à niveau selon la *Solution Campus Multiphysique* en mai `2020` et inclut les produits suivants : HF, EM, Électronique HPC, Mécanique et CFD [comme décrit ici](https://www.ansys.com/academic/educator-tools/academic-product-portfolio).
*Rocky* et *LS-DYNA* sont aussi maintenant inclus dans la licence SHARCNET. *Lumerical* acquis par Ansys en `2020` n'est pas disponible en ce moment, mais est installé avec les modules Ansys récents et peut donc être utilisé avec d'autres serveurs Ansys configurés en conséquence. *SpaceClaim* sous *Linux* n'est pas installé sur nos systèmes, mais peut techniquement être utilisé avec la licence SHARCNET. Un groupe de licences `anshpc` de `1986` est inclus dans la licence SHARCNET pour prendre en charge les grandes tâches parallèles avec la plupart des produits Ansys. Avant d'exécuter de longues tâches, il est préférable d'effectuer des tests de scalabilité. Les tâches parallèles qui utilisent moins de 50 % des processeurs seront probablement signalées par le système et examinées par notre équipe technique.

```bash
unset SLURM_GTIDS
```

!!! attention "Mise à jour"
    Depuis décembre `2022`, chaque utilisateur peut exécuter 4 travaux en utilisant un total de `252 anshpc` (plus `4 anshpc` par tâche). Ainsi, les combinaisons de taille de tâches uniformes suivantes sont possibles : une tâche de 256 cœurs, deux tâches de 130 cœurs, trois tâches de 88 cœurs ou quatre tâches de 67 cœurs selon ( (252 + 4 * nombre de tâches) / nombre de tâches). MISE À JOUR : En octobre `2024`, la limite a été portée à 8 tâches et 512 cœurs HPC par utilisateur (collectivement sur toutes les grappes pour toutes les applications) pour une période de test afin de permettre plus de flexibilité pour l'exploration de paramètres et l'exécution de problèmes de plus grande envergure. Comme la licence sera beaucoup moins utilisée, certains cas d'échec de tâche au démarrage pourront rarement se produire, mais les tâches devront être soumises à nouveau. Néanmoins, en supposant que la plupart continuent à exécuter une ou deux tâches en utilisant 128 cœurs en moyenne au total, cela ne devrait pas poser de problème. Cela dit, il sera utile de fermer les applications Ansys immédiatement après l'achèvement de toute tâche liée à l'interface graphique afin de libérer toutes les licences qui peuvent être consommées pendant que l'application est inactive, pour que d'autres puissent les utiliser.

#### Fichier du serveur de licence

Pour utiliser la licence de SHARCNET sur nos grappes, configurez votre fichier `ansys.lic` comme suit :

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")
```

#### Vérification de la licence

Pour connaître le nombre de licences utilisées qui sont associées à votre nom d'utilisateur et le nombre de licences utilisées par tous les utilisateurs, lancez

```bash
ssh graham.computecanada.ca
module load ansys
lmutil lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER"
```

```text
#SBATCH --account=def-group   # Specify account
#SBATCH --time=00-06:00       # Specify time limit dd-hh:mm
#SBATCH --ntasks=16           # Specify total number cores
#SBATCH --mem-per-cpu=4G      # Specify memory per core
#SBATCH --cpus-per-task=1     # Do not change

module load ansys/2020R1  

[l2(nibi):~] sq
           JOBID     USER        ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS MIN_MEM NODELIST (REASON) 
        10161023  roberpj   cc-debug_cpu script-flu-int   R    2:57:19     4    8     N/A      4G c[630-633] (None) 
        10161033  roberpj   cc-debug_cpu script-flu-int   R    2:58:25    16   32     N/A      4G c[627-628,630-633,637,642,645,655,657,662,665,667,669,682] (None) 
[l2(nibi):~]
[l2(nibi):~] module load ansys
[l2(nibi):~]
[l2(nibi):~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil  \
             lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
Users of anshpc:  (Total of 1986 licenses issued;  Total of 1600 licenses in use)
   roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 2579), start Wed 3/11 16:46, 4 licenses, PID: 1239140 
   roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 5716), start Wed 3/11 16:48, 28 licenses, PID: 510058 
Users of cfd_base:  (Total of 275 licenses issued;  Total of 19 licenses in use)
   roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10327), start Wed 3/11 16:46, PID: 1239140 
   roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 7171), start Wed 3/11 16:47, PID: 510058 
Users of cfd_preppost:  (Total of 275 licenses issued;  Total of 1 license in use)
Users of cfd_preppost_pro:  (Total of 275 licenses issued;  Total of 1 license in use)
Users of cfd_solve_level1:  (Total of 275 licenses issued;  Total of 18 licenses in use)
   roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 7994), start Wed 3/11 16:46, PID: 1239140 
   roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 6200), start Wed 3/11 16:47, PID: 510058 
Users of cfd_solve_level2:  (Total of 275 licenses issued;  Total of 18 licenses in use)
   roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10520), start Wed 3/11 16:46, PID: 1239140 
   roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 375), start Wed 3/11 16:47, PID: 510058 
Users of elec_solve_hfss:  (Total of 275 licenses issued;  Total of 1 license in use)
Users of elec_solve_level1:  (Total of 275 licenses issued;  Total of 1 license in use)
Users of elec_solve_level2:  (Total of 275 licenses issued;  Total of 1 license in use)
```

Si vous remarquez que des licences sont utilisées sans justification avec votre nom d'utilisateur (ce qui peut se produire si Ansys n'a pas été correctement fermé sur `gra-vdi`), connectez-vous au nœud en cause, ouvrez une fenêtre de terminal et mettez fin au processus avec `pkill -9 -e -u $USER -f "ansys"` pour libérer vos licences. Prenez note que `gra-vdi` possède deux nœuds (`gra-vdi3` et `gra-vdi4`) qui vous sont assignés au hasard quand vous vous connectez avec `tigervnc`; ainsi, avant de lancer `pkill`, il est nécessaire d'indiquer le nom complet de l'hôte (`gra-vdi3.sharcnet.ca` ou `grav-vdi4.sharcnet.ca`) quand vous vous connectez.

## Fabrication additive

Configurez d'abord votre fichier `~/.licenses/ansys.lic` pour l'orienter vers le serveur de licences où se trouve une licence valide pour Ansys *Mechanical*. Vous devez faire ceci sur tous les systèmes où vous utiliserez le logiciel.

### Activer la fabrication additive

Nous décrivons ici comment obtenir l'extension ACT de *Ansys Fabrication additive* pour l'utiliser dans votre projet. Les étapes suivantes doivent être effectuées pour chaque version de module Ansys sur chacune des grappes où l'extension sera utilisée. Les extensions nécessaires à votre projet doivent aussi être installées sur la ou les grappes, tel que décrit ci-dessous. Si vous recevez des avertissements à l'effet que des extensions dont vous n'avez pas besoin sont manquantes, par exemple `ANSYSMotion`, désinstallez-les à partir de votre projet.

#### Télécharger l'extension

*   téléchargez `AdditiveWizard.wbex` à partir de [https://catalog.ansys.com/](https://catalog.ansys.com/)
*   téléchargez `AdditiveWizard.wbex` sur la grappe où vous allez l'utiliser

#### Lancer Workbench

*   Voir la section *Workbench* dans [Mode graphique](#mode-graphique) plus haut.
*   Dans l'interface *Workbench*, ouvrez votre fichier de projet avec *File -> Open*.

#### Ouvrir le gestionnaire d'extensions

*   Cliquez sur la page *ACT Start* pour faire afficher l'onglet de la page *ACT Home*.
*   Cliquez sur *Manage Extensions* pour ouvrir le gestionnaire d'extensions.

#### Installer l'extension

*   Cliquez sur la boîte avec le signe `+` sous la barre de recherche.
*   Sélectionnez et installez votre fichier `AdditiveWizard.wbex`.

#### Charger l'extension

*   Cliquez pour sélectionner la boîte *AdditiveWizard*, ce qui charge l'extension uniquement pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte *AdditiveWizard* et sélectionnez *Load extension*, ce qui charge l'extension pour la session en cours et pour les sessions futures.

#### Supprimer l'extension

*   Cliquez pour désélectionner la boîte *AdditiveWizard*, ce qui supprime l'extension pour la session en cours.
*   Cliquez sur la flèche dans le coin droit au bas de la boîte *AdditiveWizard* et sélectionnez *Do not load as default*, ce qui empêche le chargement de l'extension pour les futures sessions.

### Exécuter la fabrication additive

#### Sur Gra-vdi

Vous pouvez exécuter une seule tâche Ansys *Fabrication additive* sur `gra-vdi` en utilisant jusqu'à 16 cœurs comme suit :

*   Lancez *Workbench* sur `gra-vdi` comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*.
*   Cliquez sur *File -> Open* et sélectionnez `test.wbpj` puis cliquez sur *Open*.
*   Cliquez sur *View -> Reset workspace* si votre écran est gris.
*   Lancez *Mechanical, Clear Generated Data*, sélectionnez *Distributed*, spécifiez *Cores*.
*   Cliquez sur *File -> Save Project -> Solve*.

Vérifiez l'utilisation :
*   Ouvrez un autre terminal et lancez `top -u $USER` OU `ps u -u $USER | grep ansys`.
*   Terminez les processus non nécessaires créés par des tâches précédentes avec `pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"`.

Veuillez noter que des processus persistants peuvent bloquer les licences entre les sessions de connexion `gra-vdi` ou provoquer d'autres erreurs inhabituelles lors de la tentative de démarrage de l'interface graphique sur `gra-vdi`. Bien que cela soit rare, un processus peut rester en mémoire si une session d'interface graphique Ansys (*Fluent*, *Workbench*, etc.) n'est pas correctement terminée avant que `vncviewer` ne soit terminé manuellement ou de manière inattendue, par exemple en raison d'une panne de réseau temporaire ou d'un système de fichiers bloqué. Dans ce dernier cas, les processus peuvent ne pas être tués tant que l'accès normal au disque n'est pas rétabli.

#### Sur la grappe

**Préparation du projet**

Certaines préparations doivent être effectuées avant de soumettre un projet *Additive* nouvellement téléchargé dans la file d'attente d'une grappe avec `sbatch scriptname`. Pour commencer, ouvrez votre simulation avec l'interface graphique de *Workbench* (comme décrit ci-dessus dans *Fabrication additive -> Activer la fabrication additive*) dans le même répertoire que celui à partir duquel votre tâche sera soumise, puis enregistrez-la à nouveau. Assurez-vous d'utiliser la même version du module Ansys qui sera utilisé pour la tâche. Créez ensuite un script Slurm (comme expliqué dans le paragraphe pour *Workbench* dans la section *Soumettre des tâches par lots sur nos grappes* ci-dessus). Pour effectuer des études paramétriques, remplacez `Update()` par `UpdateAllDesignPoints()` dans le script Slurm. Déterminez le nombre optimal de cœurs et de mémoire en soumettant plusieurs courtes tâches de test. Pour éviter d'avoir à effacer manuellement la solution **et** recréer tous les points de conception dans *Workbench* entre chaque exécution de test, soit 1. remplacez `Save(Overwrite=True)` par `Save (Overwrite=False)`; ou 2. enregistrez une copie du fichier `YOURPROJECT.wbpj` d'origine et du répertoire `YOURPROJECT_files` correspondant. Vous pouvez aussi créer puis exécuter manuellement un fichier de relecture sur la grappe dans le répertoire de cas de test entre chaque exécution, en notant qu'un seul fichier de relecture peut être utilisé dans différents répertoires en l'ouvrant dans un éditeur de texte et en modifiant le paramètre interne *FilePath*.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

**Utilisation des ressources**

Après quelques minutes, vous pouvez obtenir un instantané de l'utilisation des ressources par la tâche en cours d'exécution sur le ou les nœuds de calcul avec la commande `srun`. Le script pour 8 cœurs ci-dessous produit le résultat suivant où on remarque que l'ordonnanceur a choisi 2 nœuds.

```text
[gra-login1:~] srun --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
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

**Tests de scalabilité**

Une fois la tâche complétée, son *Temps réel d'exécution de la tâche* peut être obtenu avec `seff jobid`. Cette valeur peut être utilisée pour effectuer des tests de scalabilité en soumettant de courtes tâches d'abord puis en doublant le nombre de cœurs. Tant que le temps réel d'exécution diminue d'environ 50 %, vous pouvez continuer de doubler le nombre de cœurs.

## Aide

La documentation officielle complète pour les versions récentes Ansys `202[4|5]R[1|2]` est disponible [ici](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). La documentation pour les versions plus anciennes telles qu'Ansys `2023R[1|2]` nécessite cependant une [connexion requise](https://ansyshelp.ansys.com/). La documentation pour les développeurs peut être trouvée sur le [Portail](https://developer.ansys.com) des développeurs Ansys. Des ressources d'apprentissage supplémentaires incluent les [vidéos didacticielles Ansys](https://www.youtube.com/@AnsysHowTo/videos), le [Carrefour des éducateurs Ansys](https://innovationspace.ansys.com/educator-hub/) et la [série de webinaires Ansys](https://www.ansys.com/events/ansys-academic-webinar-series).

```bash
#module load ansys/2021R1
module load ansys/2021R2