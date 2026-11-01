---
title: "LS-DYNA/fr"
slug: "ls-dyna"
lang: "fr"

source_wiki_title: "LS-DYNA/fr"
source_hash: "aa49a4090599eb7c434cdc755e8201a0"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:32:37.967136+00:00"

tags:
  - software

keywords:
  - "module spider"
  - "sharcnet.ca"
  - "licence SHARCNET"
  - "scalabilité"
  - "mémoire=1500M"
  - "~/.licenses/ls-dyna.lic"
  - "script bash"
  - "module ls-dyna"
  - "LS-DYNA double précision"
  - "mem-per-cpu"
  - "binaires avx512"
  - "TigerVNC"
  - "test de performance"
  - "RAM réservée"
  - "LS-DYNA"
  - "ls-prepost/4.9"
  - "jupyterhub"
  - "versions >= 13.2.0"
  - "grappe"
  - "Message Passing Parallel (MPP)"
  - "licence hébergée sur un serveur de licence LSTC"
  - "fichier ls-dyna.lic"
  - "simple précision"
  - "Abaqus"
  - "serveur de licences Ansys"
  - "LS-PrePost"
  - "licence LSTC"
  - "option AUTO de LSTC_MEMORY"
  - "VDI"
  - "dyna-mpp"
  - "sharelib"
  - "LS-DYNA simple précision"
  - "nombre de nœuds de calcul"
  - "export ANSYSLMD_LICENSE_FILE"
  - "paramètres identiques"
  - "mémoire"
  - "grappes SHARCNET"
  - "OnDemand"
  - "nœud"
  - "ls-dyna-mpp"
  - "MPI"
  - "module load StdEnv/2020"
  - "VncViewer"
  - "LS-DYNA 12.2.1"
  - "double précision"
  - "tâches MPP"
  - "export LSTC_LICENSE"
  - "ls-dyna-mpi"
  - "tâches SMP"
  - "sbatch"

questions:
  - "Comment configurer et tester le serveur de licences LS‑DYA sur les grappes ?"
  - "Quelle est la différence entre les licences LSTC et les licences Ansys pour LS‑DYA, et comment les configurer correctement ?"
  - "Que faire lorsqu’aucune licence locale n’est disponible pour LS‑DYA sur les grappes ?"
  - "Comment configurer les variables d’environnement pour un serveur de licence LS‑Dyna en mode réseau et garantir l’existence du fichier ~/.licenses/ls-dyna.lic ?"
  - "Quelles sont les différences de configuration entre une licence LS‑Dyna hébergée sur un serveur ANSYS et une licence réseau LS‑Dyna, notamment les variables d’environnement requises et les versions de module compatibles ?"
  - "Quelles sont les limites et les possibilités d’utilisation de la licence SHARCNET pour les tâches LS‑Dyna SMP et MPP, et comment l’intégrer correctement dans un script Slurm ?"
  - "Pourquoi recommande‑t‑on de charger le module <code>ls-dyna</code> ou <code>ls-dyna-mpi</code> ?"
  - "Quels bénéfices apporte une licence hébergée sur un serveur de licence LSTC par rapport à l’option suivante ?"
  - "Comment cette approche évite‑t‑elle de devoir spécifier ou définir les paramètres dans chaque script ou environnement lors de la soumission des tâches sur la grappe ?"
  - "Quels sont les deux types de tâches mentionnés et comment se différencient-ils ?"
  - "Quelle commande permet d’afficher les modules disponibles pour exécuter LS‑DYNA sur un nœud unique ?"
  - "Comment soumettre un job SMP qui demande 8 cœurs sur un nœud de calcul unique ?"
  - "Comment l’option LSTC_MEMORY=AUTO influence‑t‑elle l’allocation dynamique de mémoire pour les analyses explicites et implicites sous LS‑DYNA ?"
  - "Quelle formule doit‑on appliquer pour déterminer les valeurs de « memory=… » et du paramètre de mémoire total de l’ordonnanceur en fonction de la mémoire totale du solveur, selon qu’on utilise la précision simple ou double ?"
  - "Dans un job MPP, comment répartir correctement la mémoire entre « memory1 » et « memory2 » afin de garantir que le cœur maître dispose de suffisamment de mémoire tout en respectant la limite de 75 % de la RAM du nœud ?"
  - "Comment le nom du module LS‑DYNA évolue‑t‑il à partir de la version 13.2.0 et quels binaires (avx512, sharelib) sont alors utilisés ?"
  - "Pourquoi les versions 12.2.1 et 12.2.2 doivent‑elles être exécutées dans $SLURM_TMPDIR sur le cluster Narval, et quelles sont les conséquences sur les performances ?"
  - "Quelle est la différence entre spécifier le nombre de nœuds et le nombre de cœurs dans les scripts SLURM, et comment cela influence‑t‑il la gestion de la mémoire et le temps d’attente en file d’attente ?"
  - "Quelle proportion de la RAM d’un nœud doit être réservée pour la somme de toute la mémoire attendue par nœud ?"
  - "Dans l’exemple d’un nœud de calcul de 128 Go, quelles sont les valeurs maximales recommandées pour mémoire1 et mémoire2 ?"
  - "Quelle formule est utilisée pour déterminer la taille maximale de la mémoire (en Mo) en fonction du nombre de cœurs et du type de précision (double ou simple) ?"
  - "Quelles versions de dyna‑mpp sont compatibles avec le script présenté ?"
  - "Quels types de binaires et de bibliothèques partagées (sharelib) les modules utilisent‑ils ?"
  - "Quels paramètres de soumission SLURM (account, time, ntasks, nodes) sont définis dans le script ?"
  - "Quels modules et versions de LS‑Dyna doivent être chargés en fonction du type de nœud (granite, AVX2 vs AVX512) et du cluster (Narval ou autre) ?"
  - "Pourquoi est‑il recommandé d’effectuer des tests de scalabilité avant de lancer des simulations LS‑Dyna en production, et comment extraire les statistiques de performance (temps d’exécution, efficacité CPU, efficacité mémoire) ?"
  - "Comment accéder à l’interface graphique LS‑PrePost ou à Abaqus via OnDemand ou VNC, et quelles sont les étapes pour se connecter à un nœud VDI ?"
  - "Quel est le moyen recommandé pour utiliser Abaqus en mode graphique sur un bureau à distance selon le texte ?"
  - "Comment accéder aux nœuds VDI via le navigateur en utilisant le système OnDemand ?"
  - "Est‑il nécessaire d’obtenir une licence supplémentaire pour le module mentionné contenant les modèles LS‑DYNA ?"
  - "Quels sont les URL indiqués pour accéder aux environnements JupyterHub de FIR, RORQUAL et TRILLIUM ?"
  - "Quelles sont les commandes à exécuter dans le terminal pour charger le module StdEnv/2020 et le module ls‑prepost version 4.9 ?"
  - "Comment se connecter à un nœud de calcul ou de connexion en utilisant le client VncViewer selon les instructions fournies ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
Le logiciel [LS-DYNA](http://www.lstc.com) est disponible sur toutes nos grappes. Il a [plusieurs applications](http://www.lstc.com/applications) en multiphysique, en mécanique des fluides, en transfert thermique et en dynamique des fluides. Les analyses peuvent s'effectuer sur des phénomènes distincts ou sur des simulations de phénomènes multiples comme le stress thermique ou l'interaction fluide-structure. LSTC a été acquis par Ansys et LS-DYNA pourrait éventuellement être offert uniquement via le module Ansys. Pour le moment, nous recommandons l'utilisation que nous décrivons ici.

## Licence
Nous fournissons l'hébergement pour LS-DYNA; le logiciel est installé par des modules sur nos grappes, mais nous n'avons pas de licence LS-DYNA fournissant l'accès à tous, ni de service d'hébergement pour LS-DYNA. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes. Si aucune licence locale n'est disponible, SHARCNET octroie un nombre limité de licences gratuites, attribuées selon le principe du premier arrivé, premier servi, comme décrit ci-dessous.

### Configuration initiale et test

Si votre serveur de licences n'a jamais été utilisé sur une grappe, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](../support/technical_support.md) le numéro du port et l'adresse IP de votre serveur de licence flottante. Pour vérifier le bon fonctionnement du fichier de licence, utilisez les commandes suivantes :

```bash
touch ~/.licenses/ls-dyna.lic
module load ls-dyna
export LSTC_LICENSE=network|ansys
export LSTC_LICENSE_SERVER=<port>@<server>
# ou
export ANSYSLMD_LICENSE_FILE=<port>@<server>
ls-dyna_s # ou
ls-dyna_d
```

Il n'est pas nécessaire de spécifier un fichier d'entrée ou des arguments pour exécuter ce test. L'entête de sortie doit contenir une valeur (non vide) pour `Licensed to:`. Appuyez sur ^C pour quitter le programme et revenir en ligne de commande.

## Configuration de votre licence

En 2019, Ansys a acheté Livermore Software Technology Corporation (LSTC), développeur de LS-DYNA. Les licences LS-DYNA émises par Ansys depuis cette date utilisent des **serveurs de licences Ansys**. Les licences moins récentes de LSTC utilisant un **serveur de licences LSTC** sont maintenant disponibles via ANSYS. Nous expliquons ici comment configurer votre compte ou votre script de tâche dans chacun de ces cas.

### Licence LSTC

Les options suivantes s'offrent à vous si vous avez une licence pour utilisation sur un serveur de licence LSTC.

1.  Spécifiez votre serveur de licence en créant un petit fichier nommé `ls-dyna.lic` ayant le contenu suivant :
    ```bash title="ls-dyna.lic"
    #LICENSE_TYPE: network
    #LICENSE_SERVER:<port>@<server>
    ```
    où `<port>` est un nombre entier et `<server>` est le nom d'hôte de votre serveur de licence LSTC. Placez ce fichier dans le répertoire `$HOME/.licenses/` de chaque grappe sur laquelle vous prévoyez soumettre des tâches. Les valeurs du fichier sont récupérées par LS-DYNA lors de son exécution. Cela se produit parce que notre système de modules définit `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` chaque fois que vous chargez le module `ls-dyna` ou `ls-dyna-mpi`. Cette approche est recommandée si vous disposez d'une licence hébergée sur un serveur de licence LSTC, car (par rapport à l'option suivante) les paramètres identiques seront automatiquement utilisés par toutes les tâches que vous soumettez sur la grappe, sans qu'il soit nécessaire de les spécifier dans chaque script ou de les définir dans votre environnement.

2.  Spécifiez votre serveur de licence en définissant les deux variables d'environnement suivantes dans vos scripts :
    ```bash
    export LSTC_LICENSE=network
    export LSTC_LICENSE_SERVER=<port>@<server>
    ```
    où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence LSTC. Ces variables auront la priorité sur toutes les valeurs spécifiées dans votre fichier `~/.licenses/ls-dyna.lic` qui doit exister (même s'il est vide) pour que tout module `ls-dyna` ou `ls-dyna-mpi` soit correctement chargé; pour vous assurer qu'il existe, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande pour chaque grappe sur laquelle vous soumettrez des tâches. Pour plus de détails, consultez [la documentation officielle](https://lsdyna.ansys.com/download-install-overview/).

### Licence ANSYS

Si votre licence LS-DYNA est hébergée sur un serveur de licence Ansys, définissez les deux variables d'environnement suivantes dans vos scripts :
```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence Ansys. Ces variables ne peuvent pas être définies dans votre fichier `~/.licenses/ls-dyna.lic`. Le fichier doit cependant exister (même s'il est vide) pour que tout module `ls-dyna` puisse se charger. Pour vous en assurer, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande (ou à chaque fois dans vos scripts). Notez que seules les versions de module >= 12.2.1 fonctionneront avec les serveurs de licence Ansys.

**SHARCNET**

La licence de SHARCNET permet d'exécuter des tâches LS-DYNA SMP sur **un seul nœud** ou des tâches MPP avec de nombreux cœurs grâce à la fonctionnalité `dysmp` de la licence. Cependant, elle ne permet pas d'exécuter des tâches LS-DYNA MPP à mémoire distribuée sur plusieurs nœuds, car elle ne dispose pas de la fonctionnalité `mppdyna` requise. Vous pouvez utiliser librement la licence SHARCNET pour exécuter jusqu'à 5 tâches lsdyna simultanées avec 288 cœurs, sans aucune limitation logicielle interne, contrairement aux licences étudiantes ou pédagogiques. Ces limites peuvent être modifiées en fonction de la charge sur la licence afin d'optimiser la disponibilité et seront mises à jour ici le cas échéant. Par exemple, vous pouvez soumettre et exécuter présentement une tâche sur un nœud complet de 192 cœurs et une tâche sur la moitié d'un nœud de 96 cœurs, avec une taille de maillage illimitée. La licence SHARCNET est exclusivement réservée à la recherche académique et aux publications associées. Pour utiliser la licence SHARCNET sur la grappe pour exécuter des tâches LS-DYNA, ajoutez les lignes suivantes à votre script Slurm :

```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca
```

## Soumettre des tâches sur une grappe

LS-DYNA offre des binaires pour faire exécuter des tâches sur des nœuds uniques (SMP, *Shared Memory Parallel* avec OpenMP) ou sur plusieurs nœuds (MPP, *Message Passing Parallel* avec MPI). Vous trouverez ci-dessous des scripts pour chacun des types de tâches.

### Tâches SMP

Pour connaître les modules pour faire exécuter les tâches sur un nœud unique, utilisez `module spider ls-dyna`. Pour soumettre des tâches à la queue, utilisez `sbatch script-smp.sh`. Le script suivant demande 8 cœurs sur un nœud de calcul unique.

Pour ce qui est de l’option AUTO de la variable d'environnement LSTC_MEMORY, ce paramètre permet d'étendre dynamiquement la mémoire au-delà du paramètre `memory=1500M` spécifié lorsqu'il est adapté à une analyse explicite telle que les simulations de formage de métal, mais pas à une analyse de collision. Étant donné qu'il y a 4 octets/mot pour le solveur à simple précision et 8 octets/mot pour le solveur à double précision, le paramètre 1500M dans l'exemple ci-dessous équivaut soit à 1) une quantité maximale de (1500Mw*8octets/mot) = 12 Go de mémoire avant que LSDYNA s'arrête automatiquement lors de la résolution d'un problème implicite ou 2) une quantité de départ de 12 Go de mémoire avant de l'étendre (jusqu'à 25% si nécessaire) lors de la résolution d'un problème explicite en supposant que `LSTC_MEMORY=AUTO` n'est pas commenté. Notez que 12 Go représentent 75% du total mem=16 Go réservé pour le travail et sont considérés comme étant parfaits pour les travaux implicites sur un seul nœud. En résumé, pour les analyses implicites et explicites, une fois qu'une estimation de la mémoire totale du solveur est déterminée en Go, le paramètre de mémoire totale pour l’ordonnanceur peut être déterminé en multipliant par 25% tandis que la valeur du paramètre de mémoire en mégamots peut être calculée comme (0,75*memGB/88octets/mot))*1000M et (0,75*memGB/4 octets/mot)*1000M pour les solutions à double et simple précision respectivement.

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez
#SBATCH --time=0-03:00          # J-HH:MM
#SBATCH --cpus-per-task=8       # Spécifiez le nombre de cœurs
#SBATCH --mem=16G               # Spécifiez la mémoire totale
#SBATCH --nodes=1               # Ne modifiez pas

module load StdEnv/2023         # Versions 12.2.1, 12.2.2 :
module load intel/2023.2.1      # disponible sur toutes les grappes,
module load ls-dyna/12.2.1      # utilise le binaire smp ifort160_sse2

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne modifiez pas ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D_HÔTE

#export LSTC_MEMORY=AUTO        # Optionnel pour les calculs explicites seulement

INPUTFILE="airbag.deploy.k"     # Spécifiez un nom de fichier d'entrée
SMPSOLVER="ls-dyna_d"           # Spécifiez ls-dyna_s OU ls-dyna_d

$SMPSOLVER ncpu=$SLURM_CPUS_ON_NODE i=$INPUTFILE memory=1500M
```
où
*   `ls-dyna_s` = simple précision
*   `ls-dyna_d` = double précision

### Tâches MPP

Plusieurs modules sont installés pour exécuter des tâches sur plusieurs nœuds à l'aide de la version MPP (*Message Passing Parallel*) de LS-DYNA. La méthode est basée sur MPI et peut s'adapter à de très nombreux cœurs (8 ou plus). Les modules peuvent être répertoriés en exécutant `module spider ls-dyna-mpi`. Les exemples de scripts ci-dessous montrent comment utiliser ces modules pour soumettre des tâches à un nombre spécifié de nœuds entiers *OU* à un nombre total spécifié de cœurs à l'aide de `sbatch script-mpp-bynode.sh` ou `sbatch script-mpp-bycore.sh` respectivement. La version MPP nécessite une quantité de mémoire suffisamment importante (memory1) pour que le premier cœur (processeur 0) du nœud maître puisse décomposer et simuler le modèle. Cette quantité peut être satisfaite en spécifiant une valeur de mémoire par processeur légèrement supérieure à la mémoire (memory2) requise par cœur pour la simulation, puis en plaçant suffisamment de cœurs sur le nœud principal pour faire en sorte que leur somme différentielle (mémoire par processeur moins memory2) soit supérieure ou égale à memory1. Comme avec le modèle à nœud unique, pour de meilleurs résultats, maintenez la somme de toute la mémoire attendue par nœud dans les 75 % de la RAM réservée sur un nœud. Ainsi, dans le premier script ci-dessous, en supposant un nœud de calcul de mémoire complète de 128 Go, mémoire1 peut être de 6 000 Mo (48 Go) maximum et mémoire2 de 200 Mo (48 Go/31 cœurs). (0,75\*mémoireGo/4 octets/s)\*1 000 Mo pour les solutions double précision et simple précision respectivement.

#### Spécifier le nombre de nœuds

Le script suivant demande un nombre spécifique de **nœuds de calcul entiers**.

!!! info
    Dans le script ci-dessous, le nom des modules est passé de `ls-dyna-mpi` à `ls-dyna-mpp` pour toutes les versions >= 13.2.0. De plus, ces modules utilisent des binaires `avx512` et `sharelib`.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez
#SBATCH --time=0-03:00           # J-HH:MM
#SBATCH --ntasks-per-node=192    # Spécifiez tous les cœurs par nœud (narval/nibi/fir/trillium 192, narval 64)
#SBATCH --mem=0                  # Mettez à 0 pour utiliser toute la mémoire par nœud de calcul
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds de calcul (1 ou plus)
##SBATCH --constraint=granite    # Décommentez pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # disponible sur toutes les grappes,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 utilise le binaire ifort160_avx2_openmpi405
#module load ls-dyna-mpi/12.2.2   # 12.2.2 utilise le binaire ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # disponible sur toutes les grappes sauf narval,
module load ls-dyna-mpp/17.2.0    # toutes les versions ifort190_avx512_openmpi405_sharelib

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne modifiez pas ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D_HÔTE

#export LSTC_MEMORY=AUTO          # Optionnel pour les calculs explicites seulement

INPUTFILE="airbag.deploy.k"       # Spécifiez un nom de fichier d'entrée
MPPSOLVER="ls-dyna_d"             # Spécifiez ls-dyna_s OU ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```
où
*   `ls-dyna_s` = solveur MPP en simple précision
*   `ls-dyna_d` = solveur MPP en double précision
Pour utiliser la version 12.2.1 ou 12.2.2 sur Narval, le script ci-dessus devra probablement être modifié afin d'exécuter les calculs dans `$SLURM_TMPDIR`; autrement, les performances pourraient être environ 100 fois inférieures à celles observées sur d'autres grappes. Sur Narval, seuls les modules LS-DYNA 12.2.1 et 12.2.2 sont installés, car tous ses serveurs font partie d'une architecture plus ancienne de type `AVX2`. Les versions plus récentes qui utilisent des binaires `AVX512`, ne sont donc disponibles que sur les autres grappes.

#### Spécifier le nombre de cœurs

Les tâches peuvent être soumises à un nombre arbitraire de nœuds de calcul en spécifiant le nombre de cœurs. Cette approche permet à l'ordonnanceur de déterminer le nombre optimal de nœuds de calcul pour minimiser le temps d'attente des tâches dans la queue. Les limites de mémoire s'appliquent par cœur; il faut donc spécifier une valeur suffisamment grande de `mem-per-cpu` pour que le processeur principal puisse décomposer et traiter correctement ses calculs, comme expliqué dans la présente section.

!!! info
    Notez que le nom des modules est passé de `ls-dyna-mpi` à `ls-dyna-mpp` pour toutes les versions >= 13.2.0 dans le script ci-dessous. De plus, ces modules utilisent des binaires `avx512` et `sharelib`.

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Spécifiez
#SBATCH --time=0-03:00            # J-HH:MM
#SBATCH --ntasks=64               # Spécifiez n'importe quel nombre total de cœurs
##SBATCH --nodes=1                # Décommentez pour spécifier le nombre de nœuds de calcul (1 ou plus)
##SBATCH --constraint=granite     # Décommentez pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # disponible sur toutes les grappes,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 utilise le binaire ifort160_avx2_openmpi405
#module load ls-dyna-mpi/12.2.2   # 12.2.2 utilise le binaire ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # disponible sur toutes les grappes sauf narval,
module load ls-dyna-mpp/17.2.0    # toutes les versions ifort190_avx512_openmpi405_sharelib

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne modifiez pas ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D_HÔTE

#export LSTC_MEMORY=AUTO          # Optionnel pour les calculs explicites seulement

INPUTFILE="airbag.deploy.k"       # Spécifiez un nom de fichier d'entrée
MPPSOLVER="ls-dyna_d"             # Spécifiez ls-dyna_s OU ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```
où
*   `ls-dyna_s` = solveur MPP en simple précision
*   `ls-dyna_d` = solveur MPP en double précision
Pour utiliser la version 12.2.1 ou 12.2.2 sur Narval, le script ci-dessus devra probablement être modifié afin d'exécuter les calculs avec `$SLURM_TMPDIR`; dans le cas contraire, les performances pourraient être environ 100 fois inférieures à celles observées sur d'autres grappes. Sur Narval, seuls les modules LS-DYNA 12.2.1 et 12.2.2 sont installés, car tous ses serveurs font partie d'une architecture plus ancienne de type `AVX2`. Les versions plus récentes, qui utilisent des binaires `AVX512`, ne sont donc disponibles que sur les autres grappes.

### Test de performance

Selon la simulation, LS-DYNA peut ne pas pouvoir utiliser efficacement un très grand nombre de cœurs en parallèle. Il est donc conseillé de toujours exécuter des tests de scalabilité avant de soumettre des longues tâches. Ceci aidera à déterminer le nombre maximal de cœurs pouvant être utilisés avant que la performance ne commence à se dégrader. Pour extraire les statistiques des travaux de test telles que le temps d'exécution total, l'efficacité CPU et l'efficacité de la mémoire, on peut utiliser soit la commande `seff jobnumber`, soit un portail tel que [celui-ci](https://portal.nibi.sharcnet.ca). Par le passé, les tests pour le problème standard des coussins gonflables ont montré des caractéristiques de performance très différentes selon la grappe sur laquelle ils étaient exécutés. Cependant, ces tests étaient assez petits, utilisant seulement 6 cœurs sur un seul nœud avec le module `ls-dyna/12.2.1` et 6 cœurs répartis uniformément sur deux nœuds avec le module `ls-dyna-mpi/12.2.1`. Les tests de scalabilité devraient plutôt être effectués en utilisant la simulation réelle et la grappe où les exécutions de production complètes seront réalisées afin d'obtenir des résultats fiables.

## Mode graphique

Le programme [LS-PrePost](https://www.lstc.com/products/ls-prepost) permet le prétraitement et le post-traitement des [modèles LS-DYNA](https://www.dynaexamples.com/). Il est disponible via un autre module et vous n'avez pas besoin de licence. Utilisez Abaqus en mode graphique sur un bureau à distance avec OnDemand (recommandé) ou VncViewer, comme décrit ci-dessous.

### Nœuds VDI
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

### VncViewer
1.  Avec un client VncViewer, connectez-vous à un nœud de calcul ou à un nœud de connexion avec [TigerVNC](../interactive/vnc.md#connexion).
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OU lspp49