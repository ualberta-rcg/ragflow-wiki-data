---
title: "LS-DYNA/fr"
slug: "ls-dyna"
lang: "fr"

source_wiki_title: "LS-DYNA/fr"
source_hash: "6e5a1f7c023096a37e228c022b30a973"
last_synced: "2026-09-20T00:48:35.777859+00:00"
last_processed: "2026-09-20T01:44:42.031397+00:00"

tags:
  - software

keywords:
  - "tâche à nœud unique"
  - "mem-per-cpu"
  - "solveur mpp simple précision"
  - "~/.licenses/ls-dyna.lic"
  - "analyse explicite"
  - "module spider ls-dyna"
  - "MPI"
  - "licence hébergée"
  - "ls-dyna_s"
  - "jobs multi‑nœuds (MPI)"
  - "module ls-dyna"
  - "ls-dyna-mpi"
  - "8 cœurs"
  - "nœud de calcul"
  - "tâches LS-DYNA SMP"
  - "export ANSYSLMD_LICENSE_FILE"
  - "Test de performance"
  - "SBATCH"
  - "export LSTC_LICENSE"
  - "LS‑PrePost"
  - "ls-dyna_mpp"
  - "nombre de cœurs"
  - "serveur de licences"
  - "scalabilité LS‑DYNA"
  - "licence Ansys"
  - "analyse implicite"
  - "licence SHARCNET"
  - "commande seff"
  - "licence LSTC"
  - "75 % de la RAM"
  - "128 Go"
  - "ls-dyna_d"
  - "paramètres identiques"
  - "mémoire1"
  - "serveur de licence LSTC"
  - "mémoire2"
  - "solveur mpp double précision"
  - "mémoire 1500M (12 Go)"
  - "sbatch"
  - "LS-DYNA"
  - "nombre maximal de cœurs"
  - "VncViewer"
  - "nombre de nœuds"
  - "LSTC_MEMORY=AUTO"

questions:
  - "Quels types de licences LS‑DYNA sont proposés (licence serveur LSTC vs licence serveur Ansys) et quelles sont leurs différences principales ?"
  - "Comment créer et placer le fichier `ls-dyna.lic` ainsi que définir les variables d’environnement nécessaires pour configurer correctement votre licence sur les grappes ?"
  - "Quelle commande ou procédure utiliser pour tester le bon fonctionnement d’une licence LS‑DYNA avant de lancer des simulations ?"
  - "Pourquoi est‑il recommandé de charger le module <code>ls-dyna</code> ou <code>ls-dyna-mpi</code> lorsqu’on possède une licence hébergée sur un serveur de licence LSTC ?"
  - "Comment cette approche assure‑t‑elle que les paramètres identiques sont automatiquement utilisés par toutes les tâches soumises sur la grappe ?"
  - "Quelles seraient les conséquences de devoir spécifier manuellement les paramètres dans chaque script ou les définir dans l’environnement à la place de cette méthode ?"
  - "Quelles variables d'environnement faut‑il définir pour utiliser une licence LS‑Dyna hébergée sur un serveur de licence réseau, et comment doivent‑elles être formatées ?"
  - "Comment configurer correctement la licence ANSYS pour LS‑Dyna, et quelles versions de module sont compatibles avec ce type de licence ?"
  - "Quelles sont les limitations et les conditions d’utilisation de la licence SHARCNET pour les tâches LS‑Dyna, notamment concernant les types de tâches (SMP vs MPP) et le nombre de cœurs autorisés ?"
  - "Quels modules faut‑il charger pour exécuter des tâches LS‑Dyna sur un nœud unique ?"
  - "Quelle commande utilise‑t‑on pour soumettre un script SMP à la file d’attente ?"
  - "Combien de cœurs le script d’exemple demande‑t‑il sur un nœud de calcul unique ?"
  - "Comment l’option AUTO de la variable d’environnement LSTC_MEMORY influence‑t‑elle l’allocation dynamique de mémoire pour les analyses explicites versus implicites sous LS‑DYNA ?"
  - "Comment déterminer les valeurs appropriées du paramètre memory (en méga‑mots) pour les solveurs simple précision et double précision à partir d’une estimation de la mémoire totale du solveur en gigaoctets ?"
  - "Quelles sont les exigences de mémoire et les bonnes pratiques de configuration (mémoire par processeur, nombre de cœurs, utilisation de 75 % de la RAM) pour exécuter des tâches LS‑DYNA sur plusieurs nœuds avec la version MPP (MPI) ?"
  - "Quelle différence y a‑t‑il entre l’utilisation de `--nodes` et `--ntasks` pour spécifier respectivement le nombre de nœuds et le nombre de cœurs dans les scripts SLURM présentés ?"
  - "Comment la valeur de `mem-per-cpu` doit‑elle être choisie afin d’assurer une bonne répartition de la mémoire pour le solveur LS‑DYNA ?"
  - "Quels modules et variables d’environnement doivent être chargés pour exécuter correctement les solveurs LS‑DYNA simple précision (`ls-dyna_s`) et double précision (`ls-dyna_d`) ?"
  - "Quelle proportion de la RAM d’un nœud doit être réservée pour la mémoire attendue afin d’obtenir de meilleurs résultats ?"
  - "Comment déterminer les valeurs maximales de mémoire1 et mémoire2 sur un nœud de calcul de 128 Go selon l’exemple fourni ?"
  - "Pourquoi est‑il important de maintenir la somme de toute la mémoire attendue par nœud dans les 75 % de la RAM réservée ?"
  - "Quel est le but de la condition `if [ \"$EBVERSIONNIXPKGS\" == 16.09 ]` dans le script présenté ?"
  - "Quelle différence d’utilisation entre `mpirun` et `srun` est décrite pour l’exécution de `ls-dyna_d` ?"
  - "Que signifient les notations `ls-dyna_s` et `ls-dyna_d` concernant le solveur MPP et leurs précisions respectives ?"
  - "Pourquoi est‑il recommandé d’effectuer des tests de scalabilité avant de lancer des simulations LS‑DYNA de longue durée ?"
  - "Quels outils ou commandes permettent d’extraire les statistiques de performance (temps d’exécution, efficacité CPU, efficacité mémoire) d’un travail LS‑DYNA ?"
  - "Comment accéder et lancer LS‑PrePost en mode graphique via OnDemand ou VNC sur les nœuds du système ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

## Introduction
Le logiciel [LS-DYNA](http://www.lstc.com) est disponible sur toutes nos grappes. Il a [plusieurs applications](http://www.lstc.com/applications) en multiphysique, en mécanique des fluides, en transfert thermique et en dynamique des fluides. Les analyses peuvent s'effectuer sur des phénomènes distincts ou sur des simulations de phénomènes multiples comme le stress thermique ou l'interaction fluide-structure. LSTC a été acquis par Ansys et LS-DYNA pourrait éventuellement être offert uniquement via le module Ansys. Pour le moment, nous recommandons l'utilisation que nous décrivons ici.

## Licence
!!! note
Nous fournissons l'hébergement pour LS-DYNA; le logiciel est installé par des modules sur nos grappes, mais nous n'avons pas de licence LS-DYNA fournissant l'accès à tous, ni de service d'hébergement pour LS-DYNA. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes. Si aucune licence locale n'est disponible, SHARCNET octroie un nombre limité de licences gratuites, attribuées selon le principe du premier arrivé, premier servi, comme décrit ci-dessous.
!!!

### Configuration initiale et test
Si votre serveur de licences n'a jamais été utilisé sur une grappe, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](../support/technical_support.md) le numéro du port et l'adresse IP de votre serveur de licence flottante. Pour vérifier le bon fonctionnement du fichier de licence, utilisez les commandes suivantes :

```bash
touch ~/.licenses/ls-dyna.lic
module load ls-dyna
export LSTC_LICENSE=network|ansys
export LSTC_LICENSE_SERVER=<port>@<server>, or
export ANSYSLMD_LICENSE_FILE=<port>@<server>
ls-dyna_s, or ls-dyna_d
```

Il n'est pas nécessaire de spécifier un fichier d'entrée ou des arguments pour exécuter ce test. L'en-tête de sortie doit contenir une valeur (non vide) pour `Licensed to:`. Appuyez sur ^C pour quitter le programme et revenir en ligne de commande.

## Configuration de votre licence
En 2019, Ansys a acheté Livermore Software Technology Corporation (LSTC), développeur de LS-DYNA. Les licences LS-DYNA émises par Ansys depuis cette date utilisent des **serveurs de licences Ansys**. Les licences moins récentes de LSTC utilisant un **serveur de licences LSTC** sont maintenant disponibles via Ansys. Nous expliquons ici comment configurer votre compte ou votre script de tâche dans chacun de ces cas.

### Licence LSTC
Les options suivantes s'offrent à vous si vous avez une licence pour utilisation sur un serveur de licence LSTC.

!!! tip "Option 1 : Fichier de licence recommandé"
Spécifiez votre serveur de licence en créant un petit fichier nommé `ls-dyna.lic` ayant le contenu suivant :

```bash title="~/.licenses/ls-dyna.lic"
#LICENSE_TYPE: network
#LICENSE_SERVER:<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte de votre serveur de licence LSTC. Placez ce fichier dans le répertoire `~/.licenses/` de chaque grappe sur laquelle vous prévoyez soumettre des tâches. Les valeurs du fichier sont récupérées par LS-DYNA lors de son exécution. Cela se produit parce que notre système de modules définit `LSTC_FILE=/home/$USER.licenses/ls-dyna.lic` chaque fois que vous chargez le module `ls-dyna` ou `ls-dyna-mpi`. Cette approche est recommandée si vous disposez d'une licence hébergée sur un serveur de licence LSTC car (par rapport à l'option suivante) les paramètres identiques seront automatiquement utilisés par toutes les tâches que vous soumettez sur la grappe, sans qu'il soit nécessaire de les spécifier dans chaque script ou de les définir dans votre environnement.
!!!

**Option 2 : Variables d'environnement**
Spécifiez votre serveur de licence en définissant les deux variables d'environnement suivantes dans vos scripts :

```bash
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER=<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence LSTC. Ces variables auront la priorité sur toutes les valeurs spécifiées dans votre fichier `~/.licenses/ls-dyna.lic` qui doit exister (même s'il est vide) pour que tout module `ls-dyna` ou `ls-dyna-mpi` soit correctement chargé; pour vous assurer qu'il existe, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande pour chaque grappe sur laquelle vous soumettrez des tâches. Pour plus de détails, consultez [la documentation officielle](https://lsdyna.ansys.com/download-install-overview/).

### Licence Ansys
Si votre licence LS-DYNA est hébergée sur un serveur de licence Ansys, définissez les deux variables d'environnement suivantes dans vos scripts :

```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=<port>@<server>
```
où `<port>` est un nombre entier et `<server>` est le nom d'hôte ou l'adresse IP de votre serveur de licence Ansys. Ces variables ne peuvent pas être définies dans votre fichier `~/.licenses/ls-dyna.lic`. Le fichier doit cependant exister (même s'il est vide) pour que tout module `ls-dyna` puisse se charger. Pour vous en assurer, exécutez `touch ~/.licenses/ls-dyna.lic` en ligne de commande (ou à chaque fois dans vos scripts). Notez que seules les versions de module >= 12.2.1 fonctionneront avec les serveurs de licence Ansys.

**SHARCNET**

!!! note "Licence SHARCNET"
La licence de SHARCNET permet d'exécuter des tâches LS-DYNA SMP sur **un seul nœud** ou des tâches MPP avec de nombreux cœurs grâce à la fonctionnalité `dysmp` de la licence. Cependant, elle ne permet pas d'exécuter des tâches LS-DYNA MPP à mémoire distribuée sur plusieurs nœuds, car elle ne dispose pas de la fonctionnalité `mppdyna` requise. Vous pouvez utiliser librement la licence SHARCNET pour exécuter jusqu'à 5 tâches lsdyna simultanées avec 288 cœurs, sans aucune limitation logicielle interne, contrairement aux licences étudiantes ou pédagogiques. Ces limites peuvent être modifiées en fonction de la charge sur la licence afin d'optimiser la disponibilité et seront mises à jour ici le cas échéant. Par exemple, vous pouvez soumettre et exécuter présentement une tâche sur un nœud complet de 192 cœurs et une tâche sur la moitié d'un nœud de 96 cœurs, avec une taille de maillage illimitée. La licence SHARCNET est exclusivement réservée à la recherche académique et aux publications associées. Pour utiliser la licence SHARCNET sur la grappe pour exécuter des tâches LS-DYNA, ajoutez les lignes suivantes à votre script Slurm :

```bash
export LSTC_LICENSE=ansys
export ANSYSLMD_LICENSE_FILE=1055@license1.computecanada.ca
```
!!!

## Soumettre des tâches sur une grappe
LS-DYNA offre des binaires pour faire exécuter des tâches sur des nœuds uniques (SMP, *Shared Memory Parallel* avec OpenMP) ou sur plusieurs nœuds (MPP, *Message Passing Parallel* avec MPI). Vous trouverez ci-dessous des scripts pour chacun des types de tâches.

### Tâches à nœud unique
Pour connaître les modules pour faire exécuter les tâches sur un nœud unique, utilisez `module spider ls-dyna`. Pour soumettre des tâches à la file d'attente, utilisez `sbatch script-smp.sh`. Le script suivant demande 8 cœurs sur un nœud de calcul unique.

!!! info "Option `LSTC_MEMORY=AUTO`"
En ce qui concerne l'option `AUTO` de la variable d'environnement `LSTC_MEMORY`, ce paramètre permet d'étendre dynamiquement la mémoire au-delà du paramètre `memory=1500M` spécifié lorsqu'il est adapté à une analyse explicite telle que les simulations de formage de métal, mais pas à une analyse de collision. Étant donné qu'il y a 4 octets/mot pour le solveur à simple précision et 8 octets/mot pour le solveur à double précision, le paramètre `1500M` dans l'exemple ci-dessous équivaut soit à 1) une quantité maximale de (1500M mots \* 8 octets/mot) = 12 Go de mémoire avant que LS-DYNA s'arrête automatiquement lors de la résolution d'un problème implicite ou 2) une quantité de départ de 12 Go de mémoire avant de l'étendre (jusqu'à 25 % si nécessaire) lors de la résolution d'un problème explicite en supposant que `LSTC_MEMORY=AUTO` n'est pas commenté. Notez que 12 Go représentent 75 % du total `mem=16G` réservé pour le travail et sont considérés comme étant parfaits pour les travaux implicites sur un seul nœud. En résumé, pour les analyses implicites et explicites, une fois qu'une estimation de la mémoire totale du solveur est déterminée en Go, le paramètre de mémoire totale pour l’ordonnanceur peut être déterminé en multipliant par 25 % tandis que la valeur du paramètre de mémoire en mégamots peut être calculée comme (0,75 \* memGo / 8 octets/mot) \* 1000M et (0,75 \* memGo / 4 octets/mot) \* 1000M pour les solutions à double et simple précision respectivement.
!!!

```bash title="script-smp.sh"
#!/bin/bash
#SBATCH --account=def-account   # Spécifiez votre compte
#SBATCH --time=0-03:00          # J-HH:MM
#SBATCH --cpus-per-task=8       # Spécifiez le nombre de cœurs
#SBATCH --mem=16G               # Spécifiez la mémoire totale
#SBATCH --nodes=1               # Ne pas modifier

#module load StdEnv/2020        # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2
#module load intel/2020.1.217
#module load ls-dyna/13.1.1

module load StdEnv/2023         # Version 12.2.1
module load intel/2023.2.1
module load ls-dyna/12.2.1

#export LSTC_LICENSE=ansys      # Spécifiez un serveur de licence Ansys
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO        # Optionnel, pour l'explicite seulement

ls-dyna_d ncpu=$SLURM_CPUS_ON_NODE i=airbag.deploy.k memory=1500M
```
où
*   `ls-dyna_s` = solveur SMP simple précision
*   `ls-dyna_d` = solveur SMP double précision

### Tâches multi-nœuds
Plusieurs modules sont installés pour exécuter des tâches sur plusieurs nœuds à l'aide de la version MPP (*Message Passing Parallel*) de LS-DYNA. La méthode est basée sur MPI et peut s'adapter à de très nombreux cœurs (8 ou plus). Les modules peuvent être répertoriés en exécutant `module spider ls-dyna-mpi`. Les exemples de scripts ci-dessous montrent comment utiliser ces modules pour soumettre des tâches à un nombre spécifié de nœuds entiers **OU** à un nombre total spécifié de cœurs à l'aide de `sbatch script-mpp-bynode.sh` ou `sbatch script-mpp-bycore.sh` respectivement. La version MPP nécessite une quantité de mémoire suffisamment importante (`memory1`) pour que le premier cœur (processeur 0) du nœud maître puisse décomposer et simuler le modèle. Cette quantité peut être satisfaite en spécifiant une valeur de mémoire par processeur légèrement supérieure à la mémoire (`memory2`) requise par cœur pour la simulation, puis en plaçant suffisamment de cœurs sur le nœud principal pour faire en sorte que leur somme différentielle (mémoire par processeur moins `memory2`) soit supérieure ou égale à `memory1`. Comme avec le modèle à nœud unique, pour de meilleurs résultats, maintenez la somme de toute la mémoire attendue par nœud dans les 75 % de la RAM réservée sur un nœud. Ainsi, dans le premier script ci-dessous, en supposant un nœud de calcul de mémoire complète de 128 Go, `memory1` peut être de 6 000 Mo (48 Go) maximum et `memory2` de 200 Mo (48 Go/31 cœurs). (0,75 \* mémoireGo / 4 octets/s) \* 1 000 Mo pour les solutions double précision et simple précision respectivement.

### Spécifier le nombre de nœuds
Le script suivant demande un nombre spécifique de **nœuds de calcul entiers**.

```bash title="script-mpp-bynode.sh"
#!/bin/bash
#SBATCH --account=def-account    # Spécifiez votre compte
#SBATCH --time=0-03:00           # J-HH:MM
#SBATCH --ntasks-per-node=192    # Spécifiez tous les cœurs par nœud (Narval/Nibi/Fir/Trillium 192)
#SBATCH --nodes=1                # Spécifiez le nombre de nœuds de calcul (1 ou plus)
#SBATCH --mem=0                  # Utilisez toute la mémoire par nœud de calcul (ne pas modifier)
##SBATCH --constraint=cascade    # Décommentez pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2023          # Versions 12.2.1, 12.2.2
#module load intel/2023.2.1       # Modules <=12.2.1 utilisent des libs non partagées
#module load ls-dyna-mpi/12.2.2   # Modules >=12.2.2 utilisent des bibliothèques partagées
# -----------------------------
module load StdEnv/2023           # Versions 13.2.0, 14.2.0, 15.0.2, 16.2.0, 17.0.1
module load intel/2025.2.0        # Modules >= 13.2.0 utilisent des binaires avx512
module load ls-dyna-mpp/17.0.1    # Modules >= 13.2.0 sont nommés ls-dyna-mpp

# Décommentez les deux prochaines lignes pour spécifier un serveur de licence Ansys
#export LSTC_LICENSE=ansys                   # Ne pas modifier
#export ANSYSLMD_LICENSE_FILE=PORT@HOSTNAME  # Spécifiez le numéro de PORT et le HOSTNAME

#export LSTC_MEMORY=AUTO          # Optionnel, pour l'explicite seulement

INPUTFILE="airbag.deploy.k"       # Spécifiez un nom de fichier d'entrée
MPPSOLVER="ls-dyna_d"             # Spécifiez ls-dyna_s OU ls-dyna_d

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $NCORES -hostfile /tmp/mpihostlist-$SLURM_JOB_ID $MPPSOLVER i=$INPUTFILE memory=200M
else
 srun $MPPSOLVER i=$INPUTFILE memory=200M
fi
```
où
*   `ls-dyna_s` = solveur MPP simple précision
*   `ls-dyna_d` = solveur MPP double précision

### Spécifier le nombre de cœurs
Les tâches peuvent être soumises à un nombre arbitraire de nœuds de calcul en spécifiant le nombre de cœurs. Ceci permet à l'ordonnanceur de déterminer le nombre optimal de nœuds de calcul pour minimiser le temps d'attente dans la file d'attente. Comme la limite de mémoire s'applique aux cœurs, la valeur de `mem-per-cpu` doit être assez élevée pour permettre au processeur principal de bien décomposer et gérer les calculs; pour les détails, référez-vous au premier paragraphe de la présente section.

```bash title="script-mpp-bycore.sh"
#!/bin/bash
#SBATCH --account=def-account     # Spécifiez votre compte
#SBATCH --time=0-03:00            # J-HH:MM
#SBATCH --ntasks=64               # Spécifiez un nombre total de cœurs
#SBATCH --mem-per-cpu=2G          # Spécifiez la mémoire par cœur
##SBATCH --constraint=cascade     # Décommentez pour spécifier un type de nœud spécifique à la grappe

#module load StdEnv/2020          # Versions 12.0, 13.0, 13.1.1
#export RSNT_ARCH=avx2            # Décommentez sur Beluga, Nibi, Rorqual
#export load intel/2020.1.217
#module load openmpi/4.0.3
#module load ls-dyna-mpi/13.1.1

module load StdEnv/2023           # Version 12.2.1 (plus de versions ajoutées sur demande)
module load intel/2023.2.1
module load ls-dyna-mpi/12.2.1

#export LSTC_LICENSE=ansys        # Spécifiez un serveur de licence Ansys
#export ANSYSLMD_LICENSE_FILE=<port>@<server>

#export LSTC_MEMORY=AUTO          # Optionnel, pour l'explicite seulement

if [ "$EBVERSIONNIXPKGS" == 16.09 ]; then
 slurm_hl2hl.py --format MPIHOSTLIST > /tmp/mpihostlist-$SLURM_JOB_ID
 mpirun -np $SLURM_NTASKS -hostfile /tmp/mpihostlist-$SLURM_JOB_ID ls-dyna_d i=airbag.deploy.k memory=200M
else
 srun ls-dyna_d i=airbag.deploy.k memory=200M
fi
```
où
*   `ls-dyna_s` = solveur MPP simple précision
*   `ls-dyna_d` = solveur MPP double précision

## Tests de performance
!!! tip "Conseil pour les tests de scalabilité"
Selon la simulation, LS-DYNA peut ne pas pouvoir utiliser efficacement un très grand nombre de cœurs en parallèle. Il est donc conseillé de toujours exécuter des tests de scalabilité avant de soumettre des longues tâches. Ceci aidera à déterminer le nombre maximal de cœurs pouvant être utilisés avant que la performance ne commence à se dégrader.
!!!

Pour extraire les statistiques des travaux de test telles que le temps d'exécution total, l'efficacité CPU et l'efficacité de la mémoire, on peut utiliser soit la commande `seff jobnumber`, soit un portail tel que [celui-ci](https://portal.nibi.sharcnet.ca). Par le passé, les tests pour le problème standard des coussins gonflables ont montré des caractéristiques de performance très différentes selon la grappe sur laquelle ils étaient exécutés. Cependant, ces tests étaient assez petits, utilisant seulement 6 cœurs sur un seul nœud avec le module ls-dyna/12.2.1 et 6 cœurs répartis uniformément sur deux nœuds avec le module ls-dyna-mpi/12.2.1. Les tests de scalabilité devraient plutôt être effectués en utilisant la simulation réelle et la grappe où les exécutions de production complètes seront réalisées afin d'obtenir des résultats fiables.

## Utilisation graphique
Le programme [LS-PrePost](https://www.lstc.com/products/ls-prepost) permet le prétraitement et le post-traitement des [modèles LS-DYNA](https://www.dynaexamples.com/). Il est disponible via un autre module et vous n'avez pas besoin de licence. Utilisez Abaqus en mode graphique sur un bureau à distance avec OnDemand (recommandé) ou VNC Viewer, comme décrit ci-dessous.

### Nœuds VDI
1.  Avec le navigateur de votre ordinateur, connectez-vous à un système OnDemand avec l'une des URL suivantes :
    *   [NIBI](../clusters/nibi.md) : `https://ondemand.sharcnet.ca`
    *   FIR : `https://jupyterhub.fir.alliancecan.ca`
    *   RORQUAL : `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez :
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OU lspp49
    ```

### VNC Viewer
1.  Avec un client VNC Viewer, connectez-vous à un nœud de calcul ou à un nœud de connexion avec [TigerVNC](../interactive/vnc.md#connexion).
2.  Sur votre ordinateur, ouvrez une nouvelle fenêtre de terminal et lancez :
    ```bash
    module load StdEnv/2020
    module load ls-prepost/4.9
    lsprepost OU lspp49