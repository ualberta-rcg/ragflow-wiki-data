---
title: "LS-DYNA/fr"
slug: "ls-dyna"
lang: "fr"

source_wiki_title: "LS-DYNA/fr"
source_hash: "6165fc54c91052ff0a10fbfdb5212bb7"
last_synced: "2026-10-25T00:54:39.630071+00:00"
last_processed: "2026-10-25T01:37:36.045063+00:00"

tags:
  - software

keywords:
  - "serveur de licences LSTC"
  - "128 Go"
  - "ls-dyna_d"
  - "mémoire1"
  - "mémoire2"
  - "licences Ansys"
  - "ANSYSLMD_LICENSE_FILE"
  - "Message Passing Parallel"
  - "LSTC_LICENSE"
  - "LSTC_MEMORY=AUTO"
  - "nombre de nœuds de calcul"
  - "configuration initiale"
  - "ls-dyna_mpp"
  - "ls-dyna-mpp/17.2.0"
  - "VncViewer"
  - "test de performance"
  - "paramètres identiques"
  - "nombre de cœurs"
  - "ls-dyna-mpi"
  - "LSTC_MEMORY"
  - "licence SHARCNET"
  - "grappe"
  - "serveur de licence ANSYS"
  - "mémoire dynamique"
  - "module ls-dyna"
  - "scalabilité"
  - "MPP (Message Passing Parallel)"
  - "LS-PrePost"
  - "simple précision"
  - "tâches SMP"
  - "sbatch script-smp.sh"
  - "module load intel/2025.2.0"
  - "LS-DYNA"
  - "ANSYS License Server"
  - "serveur de licence"
  - "8 cœurs"
  - "75 % de la RAM"
  - "licences gratuites SHARCNET"
  - "module spider ls-dyna"
  - "mémoire par nœud"
  - "MPI"
  - "module load"
  - "licence hébergée sur serveur LSTC"

questions:
  - "Comment configurer et tester le serveur de licences LS‑Dyna sur les grappes ?"
  - "Quelle différence existe‑t‑il entre les licences LSTC et les licences Ansys pour LS‑Dyna depuis l’acquisition par Ansys ?"
  - "Quelle est la procédure recommandée pour utiliser une licence serveur LSTC (création du fichier ls‑dyna.lic, emplacement, etc.) ?"
  - "Quel module faut‑il charger pour profiter d’une licence hébergée sur un serveur LSTC ?"
  - "Comment l’utilisation du module <code>ls-dyna</code> ou <code>ls-dyna-mpi</code> simplifie‑t‑elle la gestion des paramètres lors de la soumission de tâches sur la grappe ?"
  - "Pourquoi cette méthode est‑elle préférée à l’alternative qui nécessite de spécifier les paramètres dans chaque script ou dans l’environnement ?"
  - "Quelles variables d'environnement devez‑vous exporter pour spécifier un serveur de licence LS‑Dyna de type « network » et comment garantir que le fichier ~/.licenses/ls‑dyna.lic existe ?"
  - "Comment configurer la licence LS‑Dyna lorsqu’elle est hébergée sur un serveur de licence ANSYS, et quelles versions de module sont requises pour que cela fonctionne ?"
  - "Quelles sont les limitations de la licence SHARCNET concernant les tâches SMP et MPP, et quelles conditions d’utilisation doivent être respectées sur le cluster ?"
  - "Quels modules faut‑il charger pour exécuter des tâches LS‑Dyna en mode SMP sur un nœud unique ?"
  - "Quelle commande utilise‑t‑on pour soumettre un job SMP à la file d’attente, et quel script est indiqué dans l’exemple ?"
  - "Combien de cœurs le script d’exemple demande‑t‑il et sur combien de nœuds de calcul ?"
  - "Comment l’option `LSTC_MEMORY=AUTO` affecte‑t‑elle la gestion dynamique de la mémoire pour les analyses explicites et implicites sous LS‑DYNA ?"
  - "Comment calculer la valeur du paramètre `memory` en mégamots à partir de la mémoire totale du solveur (en Go) en tenant compte de la précision simple ou double ?"
  - "Quels sont les critères de configuration de la mémoire (memory1, memory2) et du nombre de cœurs lors de la soumission d’une tâche MPP LS‑DYNA sur plusieurs nœuds ?"
  - "Comment spécifier le nombre de nœuds de calcul dans le script `script-mpp-bynode.sh` et quels paramètres SLURM (‑‑nodes, ‑‑ntasks‑per‑node, ‑‑mem) doivent être ajustés ?"
  - "Quelle est la différence entre les solveurs `ls-dyna_s` (précision simple) et `ls-dyna_d` (précision double), et comment choisir celui qui convient à son analyse ?"
  - "Quels modules, versions et contraintes (ex. `--constraint=cascade`) doivent être chargés pour exécuter LS‑DYNA sur les différents clusters (Narval vs. les autres) et comment gérer le serveur de licences ANSYS ?"
  - "Quelle proportion de la RAM d’un nœud doit être réservée pour la somme de toute la mémoire attendue par nœud ?"
  - "Dans l’exemple d’un nœud de calcul de 128 Go, comment sont déterminées les valeurs maximales de mémoire1 (6 000 Mo) et de mémoire2 (200 Mo) ?"
  - "À quoi sert la formule « (0,75*mémoireGo/4 octets/s)*1 000 Mo » et comment s’applique‑t‑elle aux solutions en double précision et en simple précision ?"
  - "What modules are loaded by the script and on which clusters are they available?"
  - "How can the ANSYS License Server be enabled using the commented‑out export lines?"
  - "What does setting the `LSTC_MEMORY` environment variable to `AUTO` accomplish?"
  - "Comment modifier le script pour exécuter les jobs sous $SLURM_TMPDIR sur le cluster Narval afin d’éviter la perte de performance ?"
  - "Pourquoi est‑il recommandé de réaliser des tests de scalabilité avec la simulation réelle avant de lancer des tâches de production LS‑DYNA, et comment extraire les métriques de performance ?"
  - "Quelles sont les étapes pour lancer LS‑PrePost en mode graphique via OnDemand ou VNC sur les nœuds VDI ?"

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
export LSTC_LICENSE_SERVER=<port>@<server>, or
export ANSYSLMD_LICENSE_FILE=<port>@<server>
ls-dyna_s, or ls-dyna_d
```

Il n'est pas nécessaire de spécifier un fichier d'entrée ou des arguments pour exécuter ce test. L'entête de sortie doit contenir une valeur (non vide) pour `Licensed to:`. Appuyez sur ^C pour quitter le programme et revenir en ligne de commande.

## Configuration de votre licence

En 2019, Ansys a acheté Livermore Software Technology Corporation (LSTC), développeur de LS-DYNA. Les licences LS-DYNA émises par Ansys depuis cette date utilisent des **serveurs de licences Ansys**. Les licences moins récentes de LSTC utilisant un **serveur de licences LSTC** sont maintenant disponibles via Ansys. Nous expliquons ici comment configurer votre compte ou votre script de tâche dans chacun de ces cas.

### Licence LSTC

Les options suivantes s'offrent à vous si vous avez une licence pour utilisation sur un serveur de licence LSTC.

Option 1) Spécifiez votre serveur de licence en créant un petit fichier nommé `ls-dyna.lic` ayant le contenu suivant :

```bash title="ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```

où `<port>` est un nombre entier et `<server>` est le nom d'hôte de votre serveur de licence LSTC. Placez ce fichier dans le répertoire `$HOME/.licenses/` de chaque grappe sur laquelle vous prévoyez soumettre des tâches. Les valeurs du fichier sont récupérées par LS-DYNA lors de son exécution. Cela se produit parce que notre système de modules définit `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` chaque fois que vous chargez le module `ls-dyna` ou `ls-dyna-mpi`. Cette approche est recommandée si vous disposez d'une licence hébergée sur un serveur de licence LSTC, car (par rapport à l'option suivante) les paramètres identiques seront automatiquement utilisés par toutes les tâches que vous soumettez sur la grappe, sans qu'il soit nécessaire de les spécifier dans chaque script ou de les définir dans votre environnement.

Option 2) Spécifiez votre serveur de licence en définissant les deux variables d'environnement suivantes dans vos scripts :

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

Pour connaître les modules pour faire exécuter les tâches sur un nœud unique, utilisez `module spider ls-dyna`. Pour soumettre des tâches à la file d'attente, utilisez `sbatch script-smp.sh`. Le script suivant demande 8 cœurs sur un nœud de calcul unique.

Pour ce qui est de l’option AUTO de la variable d'environnement `LSTC_MEMORY`, ce paramètre permet d'étendre dynamiquement la mémoire au-delà du paramètre `memory=1500M` spécifié lorsqu'il est adapté à une analyse explicite telle que les simulations de formage de métal, mais pas à une analyse de collision. Étant donné qu'il y a 4 octets/mot pour le solveur à simple précision et 8 octets/mot pour le solveur à double précision, le paramètre 1500M dans l'exemple ci-dessous équivaut soit à 1) une quantité maximale de (1500Mw*8octets/mot) = 12 Go de mémoire avant que LSDYNA s'arrête automatiquement lors de la résolution d'un problème implicite ou 2) une quantité de départ de 12 Go de mémoire avant de l'étendre (jusqu'à 25% si nécessaire) lors de la résolution d'un problème explicite en supposant que `LSTC_MEMORY=AUTO` n'est pas commenté. Notez que 12 Go représentent 75% du total mem=16 Go réservé pour le travail et sont considérés comme étant parfaits pour les travaux implicites sur un seul nœud. En résumé, pour les analyses implicites et explicites, une fois qu'une estimation de la mémoire totale du solveur est déterminée en Go, le paramètre de mémoire totale pour l’ordonnanceur peut être déterminé en multipliant par 25% tandis que la valeur du paramètre de mémoire en mégamots peut être calculée comme (0,75*memGB/88octets/mot))*1000M et (0,75*memGB/4 octets/mot)*1000M pour les solutions à double et simple précision respectivement.

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez
#SBATCH --time=0-03:00          # J-HH:MM
#SBATCH --cpus-per-task=8       # Spécifiez le nombre de cœurs
#SBATCH --mem=16G               # Spécifiez la mémoire totale
#SBATCH --nodes=1               # Ne pas modifier

module load StdEnv/2023         # Version 12.2.1 :
module load intel/2023.2.1      # disponible sur toutes les grappes,
module load ls-dyna/12.2.1      # utilise le binaire smp ifort160_sse2

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne pas modifier ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D'HÔTE

#export LSTC_MEMORY=AUTO        # Optionnel pour les analyses explicites seulement

INPUTFILE="airbag.deploy.k"     # Spécifiez un nom de fichier d'entrée
SMPSOLVER="ls-dyna_d"           # Spécifiez ls-dyna_s OU ls-dyna_d

$SMPSOLVER ncpu=$SLURM_CPUS_ON_NODE i=$INPUTFILE memory=1500M
```

où
*   `ls-dyna_s` : simple précision
*   `ls-dyna_d` : double précision

### Tâches MPP

Plusieurs modules sont installés pour exécuter des tâches sur plusieurs nœuds à l'aide de la version MPP (*Message Passing Parallel*) de LS-DYNA. La méthode est basée sur MPI et peut s'adapter à de très nombreux cœurs (8 ou plus). Les modules peuvent être répertoriés en exécutant `module spider ls-dyna-mpi`. Les exemples de scripts ci-dessous montrent comment utiliser ces modules pour soumettre des tâches à un nombre spécifié de nœuds entiers OU à un nombre total spécifié de cœurs à l'aide de `sbatch script-mpp-bynode.sh` ou `sbatch script-mpp-bycore.sh` respectivement. La version MPP nécessite une quantité de mémoire suffisamment importante (mémoire1) pour que le premier cœur (processeur 0) du nœud maître puisse décomposer et simuler le modèle. Cette quantité peut être satisfaite en spécifiant une valeur de mémoire par processeur légèrement supérieure à la mémoire (mémoire2) requise par cœur pour la simulation, puis en plaçant suffisamment de cœurs sur le nœud principal pour faire en sorte que leur somme différentielle (mémoire par processeur moins mémoire2) soit supérieure ou égale à mémoire1. Comme avec le modèle à nœud unique, pour de meilleurs résultats, maintenez la somme de toute la mémoire attendue par nœud dans les 75 % de la RAM réservée sur un nœud. Ainsi, dans le premier script ci-dessous, en supposant un nœud de calcul de mémoire complète de 128 Go, mémoire1 peut être de 6 000 Mo (48 Go) maximum et mémoire2 de 200 Mo (48 Go/31 cœurs). (0,75*mémoireGo/4 octets/s)*1 000 Mo pour les solutions double précision et simple précision respectivement.

#### Spécifier le nombre de nœuds

Le script suivant demande un nombre spécifique de **nœuds de calcul entiers**.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez
#SBATCH --time=0-03:00           # J-HH:MM
#SBATCH --ntasks-per-node=192    # Spécifiez tous les cœurs par nœud (Narval/Nibi/Fir/Trillium 192)
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --mem=0                  # Utilisez toute la mémoire par nœud de calcul (ne pas modifier)
##SBATCH --constraint=cascade    # Décommentez pour spécifier un type de nœud spécifique à une grappe

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # disponible sur toutes les grappes,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 utilise le binaire ifort160_avx2_openmpi405
#module load ls-dyna-mpi/12.2.2   # 12.2.2 utilise ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # disponible sur toutes les grappes sauf Narval,
module load ls-dyna-mpp/17.2.0    # toutes les versions ifort190_avx512_openmpi405_sharelib

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne pas modifier ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D'HÔTE

#export LSTC_MEMORY=AUTO          # Optionnel pour les analyses explicites seulement

INPUTFILE="airbag.deploy.k"       # Spécifiez un nom de fichier d'entrée
MPPSOLVER="ls-dyna_d"             # Spécifiez ls-dyna_s OU ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```

où
*   `ls-dyna_s` : solveur MPP à simple précision
*   `ls-dyna_d` : solveur MPP à double précision

!!! attention
    Pour utiliser la version 12.2.1 ou 12.2.2 sur Narval, le script ci-dessus devra probablement être modifié pour exécuter les tâches sous `$SLURM_TMPDIR`, sinon la performance pourrait être environ 100 fois plus lente que sur d'autres grappes. Narval ne dispose que des modules lsdyna pour les versions 12.2.1 et 12.2.2, car tous ses serveurs sont basés sur l'ancienne architecture AVX2. Les versions plus récentes ont été installées avec des binaires AVX512 et ne sont donc disponibles que sur les autres grappes.

#### Spécifier le nombre de cœurs

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Spécifiez
#SBATCH --time=0-03:00            # J-HH:MM
#SBATCH --ntasks=64               # Spécifiez n'importe quel nombre total de cœurs
#SBATCH --mem-per-cpu=2G          # Spécifiez la mémoire par cœur
##SBATCH --constraint=cascade     # Décommentez pour spécifier un type de nœud spécifique à une grappe

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2 :
#module load intel/2023.2.1       # disponible sur toutes les grappes,
#module load ls-dyna-mpi/12.2.1   # 12.2.1 utilise le binaire ifort160_avx2_openmpi405
#module load ls-dyna-mpi/12.2.2   # 12.2.2 utilise ifort160_avx2_openmpi405_sharelib
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.2.0 :
module load intel/2025.2.0        # disponible sur toutes les grappes sauf Narval,
module load ls-dyna-mpp/17.2.0    # toutes les versions ifort190_avx512_openmpi405_sharelib

# Décommentez les deux lignes suivantes pour utiliser un serveur de licences ANSYS
#export LSTC_LICENSE=ansys                   # Ne pas modifier ce paramètre
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le PORT et le NOM_D'HÔTE

#export LSTC_MEMORY=AUTO          # Optionnel pour les analyses explicites seulement

INPUTFILE="airbag.deploy.k"       # Spécifiez un nom de fichier d'entrée
MPPSOLVER="ls-dyna_d"             # Spécifiez ls-dyna_s OU ls-dyna_d

srun $MPPSOLVER i=$INPUTFILE memory=200M
```

où
*   `ls-dyna_s` : solveur MPP à simple précision
*   `ls-dyna_d` : solveur MPP à double précision

!!! attention
    Pour utiliser la version 12.2.1 ou 12.2.2 sur Narval, le script ci-dessus devra probablement être modifié pour exécuter les tâches sous `$SLURM_TMPDIR`, sinon la performance pourrait être environ 100 fois plus lente que sur d'autres grappes. Narval ne dispose que des modules lsdyna pour les versions 12.2.1 et 12.2.2, car tous ses serveurs sont basés sur l'ancienne architecture AVX2. Les versions plus récentes ont été installées avec des binaires AVX512 et ne sont donc disponibles que sur les autres grappes.

## Test de performance

Selon la simulation, LS-DYNA peut ne pas pouvoir utiliser efficacement un très grand nombre de cœurs en parallèle. Il est donc conseillé de toujours exécuter des tests de scalabilité avant de soumettre des longues tâches. Ceci aidera à déterminer le nombre maximal de cœurs pouvant être utilisés avant que la performance ne commence à se dégrader. Pour extraire les statistiques des travaux de test telles que le temps d'exécution total, l'efficacité CPU et l'efficacité de la mémoire, on peut utiliser soit la commande `seff jobnumber`, soit un [portail tel que celui-ci](https://portal.nibi.sharcnet.ca). Par le passé, les tests pour le problème standard des coussins gonflables ont montré des caractéristiques de performance très différentes selon la grappe sur laquelle ils étaient exécutés. Cependant, ces tests étaient assez petits, utilisant seulement 6 cœurs sur un seul nœud avec le module ls-dyna/12.2.1 et 6 cœurs répartis uniformément sur deux nœuds avec le module ls-dyna-mpi/12.2.1. Les tests de scalabilité devraient plutôt être effectués en utilisant la simulation réelle et la grappe où les exécutions de production complètes seront réalisées afin d'obtenir des résultats fiables.

## Mode graphique

Le programme [LS-PrePost](https://www.lstc.com/products/ls-prepost) permet le prétraitement et le post-traitement des [modèles LS-DYNA](https://www.dynaexamples.com/). Il est disponible via un autre module et vous n'avez pas besoin de licence. Utilisez Abaqus en mode graphique sur un bureau à distance avec OnDemand (recommandé) ou VncViewer, comme décrit ci-dessous.

### Nœuds VDI

1.  Avec le navigateur de votre ordinateur, connectez-vous à un système OnDemand avec l'une des URL suivantes :
    *   [NIBI : Accès via OnDemand](../clusters/nibi.md) : `https://ondemand.sharcnet.ca`
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