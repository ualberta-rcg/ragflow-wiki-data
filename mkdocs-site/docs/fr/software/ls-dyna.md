---
title: "LS-DYNA/fr"
slug: "ls-dyna"
lang: "fr"

source_wiki_title: "LS-DYNA/fr"
source_hash: "5e4364933b50edf6aae65ca357704b06"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:28:37.285949+00:00"

tags:
  - software

keywords:
  - "LSTC"
  - "tâches sur la grappe"
  - "environnement"
  - "nombre de nœuds"
  - "mémoire"
  - "processeur"
  - "Serveur de licences"
  - "serveurs de licence Ansys"
  - "serveur de licence"
  - "nœud unique"
  - "allocation de mémoire"
  - "LS-DYNA"
  - "mpirun"
  - "MPP"
  - "serveur de licence LSTC"
  - "nœud de calcul"
  - "Grappes de calcul"
  - "grappe"
  - "modèle à nœud unique"
  - "LS-PrePost"
  - "solveur MPP"
  - "LSTC_FILE"
  - "nœuds de calcul"
  - "plusieurs nœuds"
  - "Test de performance"
  - "tests de scalabilité"
  - "nombre de cœurs"
  - "mode graphique"
  - "module ls-dyna"
  - "SMP"
  - "variables d'environnement"
  - "SLURM"
  - "OnDemand"
  - "Ansys"
  - "solveur mpp"
  - "ls-dyna"
  - "licence Ansys"
  - "RAM réservée"

questions:
  - "Quelles sont les principales applications et capacités de simulation du logiciel LS-DYNA mentionnées dans le document ?"
  - "Quelles sont les différentes options disponibles pour les utilisateurs afin d'obtenir une licence valide pour utiliser LS-DYNA sur les grappes de calcul ?"
  - "Quelle est la procédure technique recommandée pour configurer et tester une licence LSTC dans l'environnement de l'utilisateur ?"
  - "Quelle variable ou quel fichier doit être configuré lors du chargement des modules ls-dyna ou ls-dyna-mpi ?"
  - "Dans quelle situation précise cette méthode de configuration est-elle recommandée ?"
  - "Quels sont les avantages de cette approche lors de la soumission de tâches sur la grappe ?"
  - "Quelles variables d'environnement doivent être définies dans les scripts pour configurer les différents serveurs de licence (LSTC, Ansys ou CMC) ?"
  - "Quel est le rôle du fichier `~/.licenses/ls-dyna.lic` et comment s'assurer de sa création avant le chargement d'un module ?"
  - "Quels sont les deux types de tâches (SMP et MPP) proposés par LS-DYNA pour l'exécution sur les grappes de calcul ?"
  - "Quelle version minimale du module est nécessaire pour assurer la compatibilité avec les serveurs de licence Ansys ?"
  - "Quelles sont les différences entre les binaires SMP et MPP offerts par LS-DYNA pour l'exécution des tâches sur une grappe ?"
  - "Quels types de scripts sont mis à disposition à la suite du texte pour faciliter la soumission des tâches ?"
  - "Comment doit-on calculer et configurer les paramètres de mémoire pour les tâches sur un nœud unique selon le type d'analyse et la précision du solveur ?"
  - "Quelle est la particularité de la gestion de la mémoire pour le premier cœur du nœud maître lors de l'exécution de tâches sur plusieurs nœuds avec la version MPP ?"
  - "Quelles commandes doivent être utilisées pour rechercher les modules LS-DYNA appropriés et soumettre les scripts à l'ordonnanceur pour les deux types d'environnements ?"
  - "Quelle est la différence entre la soumission d'une tâche par nœuds entiers et celle par nombre de cœurs en termes d'optimisation par l'ordonnanceur ?"
  - "Pourquoi est-il crucial d'ajuster le paramètre de mémoire par cœur (mem-per-cpu) lors de la soumission par cœurs ?"
  - "Quelle est la distinction entre les solveurs exécutés par les commandes ls-dyna_s et ls-dyna_d dans les scripts fournis ?"
  - "Quelle condition mathématique doit être respectée entre le processeur, memory1 et memory2 ?"
  - "Quel pourcentage de la RAM réservée sur un nœud ne doit pas être dépassé par la somme de la mémoire attendue pour garantir de meilleurs résultats ?"
  - "Dans l'exemple d'un nœud de calcul de 128 Go, quelles sont les limites maximales définies pour mémoire1 et mémoire2 ?"
  - "Comment le script choisit-il entre l'utilisation de `mpirun` et `srun` pour exécuter la tâche SLURM ?"
  - "Quelle est la différence fondamentale entre les solveurs `ls-dyna_s` et `ls-dyna_d` ?"
  - "Quels sont les paramètres d'entrée (fichier et mémoire) spécifiés pour le lancement de la simulation ?"
  - "Pourquoi est-il nécessaire d'effectuer des tests de scalabilité sur la grappe de production avant de lancer de longues simulations avec LS-DYNA ?"
  - "Comment peut-on extraire les statistiques de performance, telles que l'efficacité CPU et mémoire, suite à un travail de test ?"
  - "Quelles sont les méthodes recommandées et les commandes à exécuter pour utiliser le programme LS-PrePost en mode graphique ?"
  - "Pourquoi est-il nécessaire d'effectuer des tests de scalabilité sur la grappe de production avant de lancer de longues simulations avec LS-DYNA ?"
  - "Comment peut-on extraire les statistiques de performance, telles que l'efficacité CPU et mémoire, suite à un travail de test ?"
  - "Quelles sont les méthodes recommandées et les commandes à exécuter pour utiliser le programme LS-PrePost en mode graphique ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction
Le logiciel [LS-DYNA](http://www.lstc.com) est disponible sur toutes nos grappes. Il a [plusieurs applications](http://www.lstc.com/applications) en multiphysique, en mécanique des fluides, en transfert thermique et en dynamique des fluides. Les analyses peuvent s'effectuer sur des phénomènes distincts ou sur des simulations de phénomènes multiples comme le stress thermique ou l'interaction fluide-structure. LSTC a été acquis par Ansys et LS-DYNA pourrait éventuellement être offert uniquement via le module Ansys. Pour le moment, nous recommandons l'utilisation que nous décrivons ici.

# Licence
Nous fournissons l'hébergement pour LS-DYNA; le logiciel est installé sur nos grappes, mais nous n'avons pas une licence générique fournissant l'accès à tous, ni de service d'hébergement de licences. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes. Avant d'utiliser ces licences, il peut être nécessaire d'effectuer des modifications de réseau pour garantir son accessibilité à partir des nœuds de calcul. Dans les cas où une licence a déjà été utilisée sur une grappe en particulier, ces modifications ont peut-être déjà été effectuées. Si vous ne parvenez pas à localiser ou à obtenir une licence de votre campus, contactez le [Soutien technique de CMC Microsystems](https://www.cmc.ca/support/). Les licences achetées auprès de CMC n'ont pas de frais généraux liés à l'hébergement d'un serveur de licences local puisqu'elles sont hébergées sur un système de serveur distant que CMC gère avec l'avantage supplémentaire d'être utilisables n'importe où. Si vous avez votre propre serveur et avez besoin d'un devis pour une licence gérée localement, vous pouvez contacter [Simutech](https://simutechgroup.com) ou contacter Ansys directement. SHARCNET ne fournit actuellement pas de licence LS-DYNA gratuite, ni aucun service d'hébergement de licence.

### Configuration initiale et test

Si votre serveur de licences n'a jamais été utilisé sur la grappe où vos tâches seront exécutées, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](../support/technical_support.md) le numéro du port et l'adresse IP de votre serveur de licence flottante. Pour vérifier le fonctionnement du fichier de licence, lancez

```bash
module load ls-dyna
ls-dyna_s ou ls-dyna_d
```

Il n'est pas nécessaire de spécifier un fichier d'entrée ou des arguments pour exécuter ce test. L'entête de sortie doit contenir une valeur (non vide) pour `Licensed to:`, à l'exception des serveurs de licences CMC. Appuyez sur `^C` pour quitter le programme et revenir en ligne de commande.

## Configuration de votre licence

Ansys a acheté en 2019 Livermore Software Technology Corporation (LSTC), développeur de LS-DYNA. Les licences LS-DYNA émises par Ansys depuis cette date utilisent des **serveurs de licences Ansys**. Les licences émises par LSTC peuvent toujours utiliser un **serveur de licences LSTC**. Une licence LS-DYNA peut aussi être obtenue de [CMC Microsystems](https://www.cmc.ca/). Nous expliquons ici comment configurer votre compte ou votre script de tâche dans chacun de ces cas.

### Licence LSTC

Les options suivantes s'offrent à vous si vous avez une licence pour utilisation sur un serveur de licence LSTC.

Option 1) Spécifiez votre serveur de licence en créant un petit fichier nommé `ls-dyna.lic` ayant le contenu suivant :
```text title="~/.licenses/ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte de votre serveur de licence LSTC. Placez ce fichier dans le répertoire `$HOME/.licenses/` de chaque grappe sur laquelle vous prévoyez soumettre des tâches. Les valeurs du fichier sont récupérées par LS-DYNA lors de son exécution. Cela se produit parce que notre système de modules définit `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` chaque fois que vous chargez le module `ls-dyna` ou `ls-dyna-mpi`.

!!! tip "Conseil pour la licence LSTC"
    Cette approche est recommandée si vous disposez d'une licence hébergée sur un serveur de licence LSTC car (par rapport à l'option suivante) les paramètres identiques seront automatiquement utilisés par toutes les tâches que vous soumettez sur la grappe, sans qu'il soit nécessaire de les spécifier dans chaque script ou de les définir dans votre environnement.

Option 2) Spécifiez votre serveur de licence en définissant les deux variables d'environnement suivantes dans vos scripts :
```bash
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER=<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence LSTC. Ces variables auront la priorité sur toutes les valeurs spécifiées dans votre fichier `~/.licenses/ls-dyna.lic` qui doit exister (même s'il est vide) pour que tout module `ls-dyna` ou `ls-dyna-mpi` soit correctement chargé; pour vous assurer qu'il existe, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande pour chaque grappe sur laquelle vous soumettrez des tâches. Pour plus de détails, consultez [la documentation officielle](https://lsdyna.ansys.com/download-install-overview/).

### Licence Ansys

Si votre licence LS-DYNA est hébergée sur un serveur de licence Ansys, définissez les deux variables d'environnement suivantes dans vos scripts :
```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence Ansys. Ces variables ne peuvent pas être définies dans votre fichier `~/.licenses/ls-dyna.lic`. Le fichier doit cependant exister (même s'il est vide) pour que tout module `ls-dyna` puisse se charger. Pour vous en assurer, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande (ou à chaque fois dans vos scripts).

!!! note "Important"
    Seules les versions de module >= 12.2.1 fonctionneront avec les serveurs de licence Ansys.

#### SHARCNET

La licence Ansys de SHARCNET prend en charge l'exécution de tâches SMP (*Shared Memory Parallel*) et MPP (*Message Passing Parallel*) de LS-DYNA. Elle peut être utilisée librement par n'importe qui (sur une base limitée au nombre de cœurs et de tâches) sur la grappe Nibi en ajoutant les lignes suivantes dans votre script :
```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca
```

### Licence CMC

Si votre licence a été achetée de CMC, définissez les deux variables d'environnement suivantes selon la grappe utilisée :
```bash
export LSTC_LICENSE=ansys
# Fir :      export ANSYSLMD_LICENSE_FILE=6624@172.26.0.101
# Nibi :     export ANSYSLMD_LICENSE_FILE=6624@10.25.1.56
# Narval :   export ANSYSLMD_LICENSE_FILE=6624@10.100.64.10
# Rorqual :  export ANSYSLMD_LICENSE_FILE=6624@10.100.64.10
# Trillium:  export ANSYSLMD_LICENSE_FILE=6624@scinet-cmc
```
où les différentes adresses IP correspondent aux serveurs CADpass respectifs. Aucune modification du pare-feu n'est requise pour utiliser une licence CMC sur une grappe, car elles ont déjà été effectuées. Étant donné que le serveur CMC distant qui héberge les licences LS-DYNA est basé sur Ansys, ces variables ne peuvent pas être définies dans votre fichier `~/.licenses/ls-dyna.lic`. Le fichier doit cependant exister (même s'il est vide) pour que tout module `ls-dyna` puisse se charger. Pour vous assurer que c'est le cas, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande (ou à chaque fois dans vos scripts).

!!! note "Important"
    Seules les versions de module >= 13.1.1 fonctionneront avec les serveurs de licence Ansys.

# Soumettre des tâches sur une grappe

LS-DYNA offre des binaires pour faire exécuter des tâches sur des nœuds uniques (SMP, *Shared Memory Parallel* avec OpenMP) ou sur plusieurs nœuds (MPP, *Message Passing Parallel* avec MPI). Vous trouverez ci-dessous des scripts pour chacun des types de tâches.

## Tâches avec un nœud unique

Pour connaître les modules pour faire exécuter les tâches sur un nœud unique, utilisez `module spider ls-dyna`. Pour soumettre des tâches à la queue, utilisez `sbatch script-smp.sh`. Le script suivant demande 8 cœurs sur un nœud de calcul unique.

Pour ce qui est de l’option AUTO de la variable d'environnement LSTC_MEMORY, ce paramètre permet d'étendre dynamiquement la mémoire au-delà du paramètre `memory=1500M` spécifié lorsqu'il est adapté à une analyse explicite telle que les simulations de formage de métal, mais pas à une analyse de collision. Étant donné qu'il y a 4 octets/mot pour le solveur à simple précision et 8 octets/mot pour le solveur à double précision, le paramètre 1500M dans l'exemple ci-dessous équivaut soit à 1) une quantité maximale de (1500Mw*8octets/mot) = 12 Go de mémoire avant que LSDYNA s'arrête automatiquement lors de la résolution d'un problème implicite ou 2) une quantité de départ de 12 Go de mémoire avant de l'étendre (jusqu'à 25% si nécessaire) lors de la résolution d'un problème explicite en supposant que `LSTC_MEMORY=AUTO` n'est pas commenté. Notez que 12 Go représentent 75% du total mem=16 Go réservé pour le travail et sont considérés comme étant parfaits pour les travaux implicites sur un seul nœud. En résumé, pour les analyses implicites et explicites, une fois qu'une estimation de la mémoire totale du solveur est déterminée en Go, le paramètre de mémoire totale pour l’ordonnanceur peut être déterminé en multipliant par 25% tandis que la valeur du paramètre de mémoire en mégamots peut être calculée comme (0,75*memGB/8 octets/mot))*1000M et (0,75*memGB/4 octets/mot)*1000M pour les solutions à double et simple précision respectivement.

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifier
#SBATCH --time=0-03:00          # J-HH:MM
#SBATCH --cpus-per-task=8       # Spécifier le nombre de cœurs
#SBATCH --mem=16G               # Spécifier la mémoire totale
#SBATCH --nodes=1               # Ne pas changer

#module load StdEnv/2020        # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2
#module load intel/2020.1.217
#module load ls-dyna/13.1.1

module load StdEnv/2023         # Version 12.2.1
module load intel/2023.2.1
module load ls-dyna/12.2.1

#export LSTC_LICENSE=ansys      # Spécifier un serveur de licence Ansys
#export ANSYSLMD_LICENSE_FILE=<port>@<serveur>

#export LSTC_MEMORY=AUTO        # Optionnel, pour l'explicite seulement

ls-dyna_d ncpu=$SLURM_CPUS_ON_NODE i=airbag.deploy.k memory=1500M
```
où
*   `ls-dyna_s` = solveur smp simple précision
*   `ls-dyna_d` = solveur smp double précision

## Tâches avec plusieurs nœuds

Plusieurs modules sont installés pour exécuter des tâches sur plusieurs nœuds à l'aide de la version MPP (*Message Passing Parallel*) de LS-DYNA. La méthode est basée sur mpi et peut s'adapter à de très nombreux cœurs (8 ou plus). Les modules peuvent être répertoriés en exécutant `module spider ls-dyna-mpi`. Les exemples de scripts ci-dessous montrent comment utiliser ces modules pour soumettre des tâches à un nombre spécifié de nœuds entiers *OU* à un nombre total spécifié de cœurs à l'aide de `sbatch script-mpp-bynode.sh` ou `sbatch script-mpp-bycore.sh` respectivement.

!!! note "Prérequis mémoire pour MPP"
    La version MPP nécessite une quantité de mémoire suffisamment importante (memory1) pour que le premier cœur (processor 0) du nœud maître puisse décomposer et simuler le modèle. Cette quantité peut être satisfaite en spécifiant une valeur de mémoire par processeur légèrement supérieure à la mémoire (memory2) requise par cœur pour la simulation, puis en plaçant suffisamment de cœurs sur le nœud principal pour faire en sorte que leur somme différentielle (mémoire par processeur moins memory2) soit supérieure ou égale à memory1. Comme avec le modèle à nœud unique, pour de meilleurs résultats, maintenez la somme de toute la mémoire attendue par nœud dans les 75 % de la RAM réservée sur un nœud. Ainsi, dans le premier script ci-dessous, en supposant un nœud de calcul de mémoire complète de 128 Go, mémoire1 peut être de 6 000 Mo (48 Go) maximum et mémoire2 de 200 Mo (48 Go/31 cœurs). (0,75*mémoireGo/4 octets/s)*1 000 Mo pour les solutions double précision et simple précision respectivement.

### Spécifier le nombre de nœuds

Le script suivant demande un nombre spécifique de **nœuds de calcul entiers**.
```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifier
#SBATCH --time=0-03:00           # J-HH:MM
#SBATCH --ntasks-per-node=192    # Spécifier tous les cœurs par nœud (narval/nibi/fir/trillium 192)
#SBATCH --nodes=1                # Spécifier le nombre de nœuds de calcul (1 ou plus)
#SBATCH --mem=0                  # Utiliser toute la mémoire par nœud de calcul (ne pas changer)
##SBATCH --constraint=cascade    # Décommenter pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2020         # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2
#module load intel/2020.1.217
#module load openmpi/4.0.3
#module load ls-dyna-mpi/13.1.1

module load StdEnv/2023          # Version 12.2.1
module load intel/2023.2.1
module load ls-dyna-mpi/12.2.1

#export LSTC_LICENSE=ansys       # Spécifier un serveur de licence Ansys
#export ANSYSLMD_LICENSE_FILE=<port>@<serveur>

#export LSTC_MEMORY=AUTO         # Optionnel, pour l'explicite seulement

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $NCORES -hostfile /tmp/mpihostlist-$SLURM_JOB_ID ls-dyna_d i=airbag.deploy.k memory=200M
else
 srun ls-dyna_d i=airbag.deploy.k memory=200M
fi
```
où
*   `ls-dyna_s` = solveur mpp simple précision
*   `ls-dyna_d` = solveur mpp double précision

### Spécifier le nombre de cœurs

Les tâches peuvent être soumises à un nombre arbitraire de nœuds de calcul en spécifiant le nombre de cœurs. Ceci permet à l'ordonnanceur de déterminer le nombre optimal de nœuds de calcul pour minimiser le temps d'attente dans la queue. Comme la limite de mémoire s'applique aux cœurs, la valeur de `mem-per-cpu` doit être assez élevée pour permettre au processeur principal de bien décomposer et gérer les calculs; pour les détails, référez-vous au premier paragraphe de la présente section.

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Spécifier
#SBATCH --time=0-03:00            # J-HH:MM
#SBATCH --ntasks=64               # Spécifier n'importe quel nombre total de cœurs
#SBATCH --mem-per-cpu=2G          # Spécifier la mémoire par cœur
##SBATCH --constraint=cascade     # Décommenter pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2020          # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2            # Décommenter sur beluga, nibi, rorqual
#export load intel/2020.1.217
#module load openmpi/4.0.3
#module load ls-dyna-mpi/13.1.1

module load StdEnv/2023           # Version 12.2.1 (plus de versions ajoutées sur demande)
module load intel/2023.2.1
module load ls-dyna-mpi/12.2.1

#export LSTC_LICENSE=ansys        # Spécifier un serveur de licence Ansys
#export ANSYSLMD_LICENSE_FILE=<port>@<serveur>

#export LSTC_MEMORY=AUTO          # Optionnel, pour l'explicite seulement

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $SLURM_NTASKS -hostfile /tmp/mpihostlist-$SLURM_JOB_ID ls-dyna_d i=airbag.deploy.k memory=200M
else
 srun ls-dyna_d i=airbag.deploy.k memory=200M
fi
```
où
*   `ls-dyna_s` = solveur mpp simple précision
*   `ls-dyna_d` = solveur mpp double précision

## Test de performance

Selon la simulation, LS-DYNA peut ne pas pouvoir utiliser efficacement un très grand nombre de cœurs en parallèle.

!!! tip "Conseil pour les tests de performance"
    Il est donc conseillé de toujours exécuter des tests de scalabilité avant de soumettre des longues tâches. Ceci aidera à déterminer le nombre maximal de cœurs pouvant être utilisés avant que la performance ne commence à se dégrader.

Pour extraire les statistiques des travaux de test telles que le temps d'exécution total, l'efficacité CPU et l'efficacité de la mémoire, on peut utiliser soit la commande `seff jobnumber`, soit [ce portail](https://portal.nibi.sharcnet.ca). Par le passé, les tests pour le problème standard des coussins gonflables ont montré des caractéristiques de performance très différentes selon la grappe sur laquelle ils étaient exécutés. Cependant, ces tests étaient assez petits, utilisant seulement 6 cœurs sur un seul nœud avec le module ls-dyna/12.2.1 et 6 cœurs répartis uniformément sur deux nœuds avec le module ls-dyna-mpi/12.2.1. Les tests de scalabilité devraient plutôt être effectués en utilisant la simulation réelle et la grappe où les exécutions de production complètes seront réalisées afin d'obtenir des résultats fiables.

# Mode graphique

Le programme [LS-PrePost](https://www.lstc.com/products/ls-prepost) permet le prétraitement et le post-traitement des [modèles LS-DYNA](https://www.dynaexamples.com/). Il est disponible via un autre module et vous n'avez pas besoin de licence. Utilisez Abaqus en mode graphique sur un bureau à distance avec OnDemand (recommandé) ou VncViewer, comme décrit ci-dessous.

## Nœuds VDI
1.  Avec le navigateur de votre ordinateur, connectez-vous à un système OnDemand avec l'une des URL suivantes :
    *   [NIBI](../clusters/nibi.md) : `https://ondemand.sharcnet.ca`
    *   FIR : `https://jupyterhub.fir.alliancecan.ca`
    *   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OU lspp49
    ```

## VncViewer
1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou à un nœud de connexion avec [TigerVNC](../interactive/vnc.md#connexion).

2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OU lspp49