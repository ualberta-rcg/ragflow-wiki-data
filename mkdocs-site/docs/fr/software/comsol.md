---
title: "COMSOL/fr"
slug: "comsol"
lang: "fr"

source_wiki_title: "COMSOL/fr"
source_hash: "38eec14cd7b3d1daca54aaa4b9d0b3ea"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:01:04.300356+00:00"

tags:
  - software

keywords:
  - "SBATCH"
  - "serveur de licence"
  - "versions installées"
  - "lmutil"
  - "Exploration des paramètres"
  - "Exploration d'une grappe"
  - "produits installés"
  - "CMC"
  - "COMSOL"
  - "serveur de licences"
  - "fichier corrompu"
  - "ModelToSolve.mph"
  - "grappes de calcul"
  - "exécution sur un seul nœud"
  - "nœuds de calcul"
  - "simulation"
  - "module avail comsol"
  - "lmstat"
  - "~/.licenses/comsol.lic"
  - "INPUTFILE"
  - "mode graphique"
  - "cpus-per-task"
  - "fichier de licence"
  - "script batch"
  - "mode GUI"
  - "OnDemand"
  - "Ansys"
  - "OUTPUTFILE"
  - "soumettre des tâches"
  - "JupyterLab"

questions:
  - "Comment fonctionne le système de licence pour pouvoir utiliser le logiciel COMSOL sur les grappes de calcul de l'organisation ?"
  - "Quelles sont les étapes techniques requises pour configurer correctement le fichier de licence selon que l'on utilise un serveur d'établissement local ou une licence CMC ?"
  - "Quelle est la méthode de contournement recommandée pour vérifier le nombre de licences actuellement utilisées par vos tâches en cours d'exécution ?"
  - "Pourquoi une solution de contournement est-elle nécessaire pour remplacer la commande lmstat lors de l'utilisation de COMSOL ?"
  - "Quelle commande alternative issue du module Ansys peut être utilisée sur n'importe quel nœud de connexion ?"
  - "Quel fichier standard permet d'identifier le serveur de licences et quel délai de réponse peut survenir si ce dernier est occupé ?"
  - "Comment peut-on vérifier la liste des modules et produits COMSOL installés et utilisables ?"
  - "Quelles commandes permettent de connaître la version exacte de COMSOL et de lister les versions disponibles sur les grappes ?"
  - "Comment doit-on configurer un script de soumission de tâche pour exécuter COMSOL sur un seul nœud de calcul ?"
  - "Comment configurer et exécuter une simulation COMSOL sur plusieurs nœuds de calcul lorsque les capacités d'un seul nœud sont dépassées ?"
  - "Quelle est la solution recommandée si la tâche plante au démarrage à cause d'une erreur de segmentation Java ?"
  - "Quelles sont les méthodes recommandées et les prérequis pour lancer et utiliser COMSOL en mode graphique ?"
  - "What are the specific hardware resource allocations, such as memory and CPUs, defined in this batch script?"
  - "What are the names of the input and output files designated for the model?"
  - "What constraints are placed on the number of nodes and tasks per node?"
  - "Quelles sont les commandes requises pour charger et lancer les différentes versions de COMSOL via une session OnDemand ?"
  - "Quelles sont les étapes à suivre pour démarrer automatiquement COMSOL sur un bureau à distance à l'aide de JupyterLab ?"
  - "Comment doit-on soumettre une tâche pour l'exploration d'une grappe et quelle fonctionnalité de l'interface graphique n'est actuellement pas disponible ?"
  - "Quel fichier doit être obligatoirement configuré au préalable avant d'utiliser COMSOL ?"
  - "Quelle commande permet d'afficher les versions de COMSOL disponibles dans l'environnement actuellement chargé ?"
  - "Que faut-il faire si les éléments du menu supérieur sont grisés et inactifs lors du démarrage en mode interface graphique ?"
  - "Quelles sont les commandes requises pour charger et lancer les différentes versions de COMSOL via une session OnDemand ?"
  - "Quelles sont les étapes à suivre pour démarrer automatiquement COMSOL sur un bureau à distance à l'aide de JupyterLab ?"
  - "Comment doit-on soumettre une tâche pour l'exploration d'une grappe et quelle fonctionnalité de l'interface graphique n'est actuellement pas disponible ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

[COMSOL](http://www.comsol.com) est un logiciel polyvalent pour la modélisation en ingénierie. Nous remercions COMSOL Inc. pour l'entente d'hébergement spéciale de son application.

Avant d'utiliser COMSOL sur nos grappes, nous vous recommandons de consulter la section d'aide sous *Fichier -> Aide -> Documentation*. Au bas de la [page d'accueil de COMSOL](http://www.comsol.com) se trouvent des liens vers le blogue, la base de connaissances, le soutien technique et la documentation. Vous pouvez également [consulter la documentation en ligne](https://doc.comsol.com/).

## Votre licence

Notre organisation assure l'hébergement du logiciel COMSOL. Dans ce contexte, COMSOL est installé sur nos grappes, mais nous n'avons pas une licence générique offrant un accès généralisé. Cependant, plusieurs établissements, facultés et départements détiennent des licences qui peuvent être utilisées sur nos grappes.
Vous pouvez aussi acheter une licence auprès de [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) pour utilisation au Canada. Une fois que l'aspect légal de votre licence est finalisé, il faut passer à l'aspect technique. Notre équipe technique communiquera avec votre gestionnaire de licence pour que nos nœuds de calcul puissent accéder à votre serveur de licence. Si vous avez acheté une licence de CMC et que vous voulez vous connecter au serveur de licence de CMC, cet aspect technique est déjà géré. Lorsque le serveur de licence est prêt et que vous avez créé *~/.licenses/comsol.lic*, chargez un module COMSOL que vous pourrez utiliser. Si cela ne fonctionne pas, contactez notre [soutien technique](../support/technical_support.md).

### Configuration de votre fichier de licence

Notre module COMSOL cherche l'information relative à la licence à différents endroits, dont votre répertoire *~/.licenses*. Si vous avez votre propre serveur de licence, indiquez-le en créant le fichier texte `$HOME/.licenses/comsol.lic` avec les informations suivantes :

```text title="comsol.lic"
SERVER <server> ANY <port>
USE_SERVER
```

où `<server>` est votre serveur de licence et `<port>` est le numéro de port du serveur de licence.

### Configuration d'une licence locale

Si vous voulez utiliser un nouveau serveur de licence de votre établissement, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](../support/technical_support.md) 1. le numéro de port TCP lmgrd pour COMSOL (habituellement 1718 par défaut), 2. le numéro de port TCP statique LMCOMSOL du fournisseur (habituellement 1719 par défaut) et 3. le nom d’hôte entièrement qualifié de votre serveur de licence COMSOL.
Créez ensuite le fichier texte *comsol.lic* comme illustré plus haut.

### Configuration d'une licence CMC

Si vous avez une licence avec CMC, utilisez les paramètres IP publics préconfigurés dans le fichier *comsol.lic* :

*   Fir: `SERVER 172.26.0.101 ANY 6601`
*   Nibi: `SERVER 10.25.1.56 ANY 6601`
*   Narval/Rorqual: `SERVER 10.100.64.10 ANY 6601`
*   Trillium: `SERVER scinet-cmc ANY 6601`

Par exemple, un fichier de licence créé sur la grappe Nibi ressemblerait à ceci :

```text title="~/.licenses/comsol.lic (exemple sur Nibi)"
SERVER 10.25.1.56 ANY 6601
USE_SERVER
```

Si vous ne pouvez pas obtenir la licence, demandez de l'assistance en cliquant [ici](https://www.cmc.ca/fr/soutien/).

## Vérifier l'utilisation des licences

Pour déterminer le nombre de licences utilisées par vos tâches COMSOL en cours d'exécution, il faut interroger le serveur de licences. Comme indiqué [ici](https://www.comsol.com/support/knowledgebase/1142), cela peut se faire à l'aide de la commande `lmstat`. Cependant, cette commande n'étant pas installée par défaut avec COMSOL, la solution de rechange suivante, qui utilise la commande `lmutil` du module Ansys le plus récent, peut être exécutée sur n'importe quel nœud d'accès. Si vous utilisez le fichier standard `~/.licenses/comsol.lic` pour identifier le serveur de licences, cette méthode devrait fonctionner, mais le délai de réponse peut aller jusqu'à une minute si le serveur est occupé.

```bash
module load ansys; $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c ~/.licenses/comsol.lic -a | sed '/^$/d' | egrep 'License|UP|$USER|Total of'  | grep -v 'Total of 0'
```

## Produits installés

Pour connaître les [modules et produits](https://www.comsol.com/products) que vous pouvez utiliser, démarrez COMSOL [en mode graphique](#mode-graphique) et cliquez sur *Options -> Produits sous licence et utilisés* dans le menu déroulant supérieur. Pour l'explication détaillée, [cliquez ici](https://doc.comsol.com/6.0/docserver/#!/com.comsol.help.comsol/comsol_ref_customizing.16.09.html). Si un module ou un produit manque ou si la licence n'existe pas, contactez le [soutien technique](../support/technical_support.md), car il se pourrait que vous deviez réinstaller le module CVMFS que vous utilisez.

## Versions installées

Pour vérifier le numéro de version complet d'un module, démarrez COMSOL [en mode graphique](#mode-graphique) et regardez dans le coin inférieur droit de la fenêtre de messages OU plus simplement, connectez-vous à une grappe et exécutez les commandes suivantes en mode de traitement par lots :

```bash
salloc --time=0:01:00 --nodes=1 --cores=1 --mem=1G --account=def-someuser
module load comsol/6.2
comsol batch -version
```
```text
COMSOL Multiphysics 6.2.0.290
```

ce qui, dans ce cas, correspond à COMSOL 6.2 Mise à jour 1. Autrement dit, lorsqu'une [nouvelle version de COMSOL](https://www.comsol.com/release-history) est installée, elle utilise le format abrégé de 6.X mais pour des raisons pratiques, elle contient la version la plus récente au moment de l'installation. Lorsque [d'autres versions sont disponibles](https://www.comsol.com/product-update), elles utiliseront le format 6.X.Y.Z. Par exemple, la [Mise à jour 3](https://www.comsol.com/product-update/6.2) peut être chargée sur une grappe avec les commandes `module load comsol/6.2.0.415` OU `module load comsol`. Nous vous recommandons d'utiliser la version la plus récente afin de profiter de la dernière mise à jour. Cependant, si vous voulez continuer d'utiliser une version 6.X ou 6.X.Y.Z, sachez que, par définition, le logiciel contenu dans ces modules sera le même.

Pour connaître les versions qui sont disponibles dans l'environnement standard que vous avez chargé (généralement, il s'agit de `StdEnv/2023`), lancez la commande `module avail comsol`. Pour connaître les versions qui sont disponibles dans TOUS les environnements standards, lancez la commande `module spider comsol`.

Le module `comsol/6.3` correspond à la version [6.3.0.290](https://www.comsol.com/product-download/6.3) et est disponible sur toutes nos grappes.

## Soumettre des tâches

### Exécution sur un seul nœud

Le script suivant utilise huit cœurs sur un seul nœud.

```bash title="mysub1.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Spécifier (j-hh:mm)
#SBATCH --account=def-group        # Spécifier (un compte)
#SBATCH --mem=32G                  # Spécifier (0 pour utiliser toute la mémoire sur chaque nœud)
#SBATCH --cpus-per-task=8          # Spécifier (valeur maximale de tous les cœurs sur un nœud)
#SBATCH --nodes=1                  # Ne pas modifier
#SBATCH --ntasks-per-node=1        # Ne pas modifier

INPUTFILE="ModelToSolve.mph"       # indiquer le nom du fichier en entrée
OUTPUTFILE="SolvedModel.mph"       # indiquer le nom du fichier en sortie

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

comsol batch -inputfile ${INPUTFILE} -outputfile ${OUTPUTFILE} -np $SLURM_CPUS_ON_NODE
```

Selon la complexité de la simulation, il est possible que COMSOL n'exploite pas efficacement plusieurs cœurs. Il est donc suggéré de vérifier la mise à l'échelle de la simulation en augmentant progressivement le nombre de cœurs. Si l'accélération est quasi linéaire avec tous les cœurs d'un nœud, envisagez l'exécution de la tâche sur plusieurs nœuds complets en ajustant le script ci-dessous.

### Exécution sur plusieurs nœuds

Le script suivant utilise 8 cœurs distribués également sur 2 nœuds. Ce script est idéal pour les très grosses simulations (qui dépassent les capacités d'un simple nœud) et permet de redémarrer des tâches interrompues, d'allouer des fichiers temporaires volumineux dans l'espace `/scratch` et d'utiliser les paramètres par défaut du fichier *comsolbatch.ini*. Une option permettant de modifier le tas Java est décrite sous le script.

```bash title="script-dis.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Spécifier (j-hh:mm)
#SBATCH --account=def-account      # Spécifier (un compte)
#SBATCH --mem=16G                  # Spécifier (0 pour utiliser toute la mémoire sur chaque nœud)
#SBATCH --cpus-per-task=4          # Spécifier (valeur maximale de tous les cœurs sur un nœud)
#SBATCH --nodes=2                  # Spécifier (le nombre de nœuds de calcul à utiliser pour la tâche)
#SBATCH --ntasks-per-node=1        # Ne pas modifier

INPUTFILE="ModelToSolve.mph"       # indiquer le nom du fichier en entrée
OUTPUTFILE="SolvedModel.mph"       # indiquer le nom du fichier en sortie

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

RECOVERYDIR=$SCRATCH/comsol/recoverydir
mkdir -p $RECOVERYDIR

cp -f ${EBROOTCOMSOL}/bin/glnxa64/comsolbatch.ini comsolbatch.ini
cp -f ${EBROOTCOMSOL}/mli/startup/java.opts java.opts

#export I_MPI_COLL_EXTERNAL=0       # supprimer cette ligne sur Narval

comsol batch -inputfile $INPUTFILE -outputfile $OUTPUTFILE -np $SLURM_CPUS_ON_NODE -nn $SLURM_NNODES \
-recoverydir $RECOVERYDIR -tmpdir $SLURM_TMPDIR -comsolinifile comsolbatch.ini -alivetime 15 \
# -recover -continue                # supprimer cette ligne pour redémarrer à partir du dernier fichier récupéré
```

!!! note "Remarque 1"
    Si votre tâche se bloque au démarrage en raison d'une erreur de segmentation Java, augmentez le tas (*heap*), ajoutez les deux lignes `sed` immédiatement après les commandes `cp -f`. Si le problème n'est toujours pas résolu, remplacez 4G par 8G sur les deux lignes. Pour plus d'informations, consultez [Problèmes de mémoire](https://www.comsol.ch/support/knowledgebase/1243).

    ```bash
    sed -i 's/-Xmx2g/-Xmx4g/g' comsolbatch.ini
    sed -i 's/-Xmx768m/-Xmx4g/g' java.opts
    ```

!!! note "Remarque 3"
    Il arrive que certaines tâches soient lentes ou qu'elles se bloquent au lancement lorsque `script-dis.sh` est exécuté sur un seul nœud. Si c'est le cas, utilisez plutôt le script pour nœuds multiples `script-dis.sh` ci-dessus, en y ajoutant `#SBATCH --nodes=1` et créez ensuite une demande de soutien pour signaler le problème en précisant le numéro de la tâche et le nom de la grappe.

## Mode graphique

Pour exécuter COMSOL en mode graphique, ouvrez une session de bureau à distance sur un système [OnDemand](../clusters/nibi.md#acces-via-open-ondemand-ood) ou JupyterLab en cliquant sur les liens ci-dessous.

!!! note "Remarque"
    L'ancienne méthode utilisant un client/serveur [TigerVNC](../interactive/vnc.md) devrait toujours fonctionner, mais elle n'est plus recommandée ni prise en charge. Quelle que soit la méthode utilisée, le fichier `~/.licenses/comsol.lic` doit être configuré au préalable. Veuillez noter que la commande `module avail comsol` affichera les versions de COMSOL disponibles dans la version de StdEnv actuellement chargée (par exemple, `StdEnv/2023`). Si vous constatez que les éléments du menu supérieur sont grisés et non sélectionnables après avoir démarré COMSOL en mode interface graphique, votre fichier *~/.comsol* est peut-être corrompu; essayez donc de le supprimer.

### OnDemand

1.  Sur votre bureau, démarrez une session OnDemand en cliquant sur une des URL ci-dessous :
    *   [Nibi](../clusters/nibi.md#acces-via-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2.  Sur le bureau, ouvrez une nouvelle fenêtre de terminal et lancez les commandes correspondantes pour :
    *   **COMSOL 6.2 (ou versions plus récentes)**
        *   `module load StdEnv/2023` (par défaut)
        *   `module load comsol/6.4`
        *   `comsol`
    *   **COMSOL 6.1 (ou versions moins récentes)**
        *   `module load StdEnv/2020` (par défaut)
        *   `module load comsol/6.1`
        *   `comsol`

### JupyterLab

1.  Sur votre bureau, démarrez une session JupyterHub en cliquant sur une URL ci-dessous.
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6.4`) dans la section *Module disponible* à gauche.
3.  Pour le module, cliquez sur *Charger* pour afficher l'icône `Comsol (VNC)`.
4.  Cliquez sur l'icône et COMSOL devrait démarrer automatiquement sur un bureau Jupyter à distance.

## Exploration des paramètres

### Exploration en lots

En mode interactif avec l'interface graphique, les problèmes de balayage de paramètres peuvent être résolus avec [l'approche par balayage de lots (*Batch Sweep*)](https://www.comsol.com/blogs/the-power-of-the-batch-sweep/). Voyez [cette vidéo démontrant des balayages de paramètres multiples](https://www.comsol.com/video/performing-parametric-sweep-study-comsol-multiphysics). Il est aussi possible d'obtenir l'accélération [en parallélisant les tâches](https://www.comsol.com/blogs/added-value-task-parallelism-batch-sweeps/).

### Exploration d'une grappe

Pour faire l'exploration d'une grappe, une tâche doit être soumise en ligne de commande à l'ordonnanceur via `sbatch slurmscript`. Pour connaître les détails concernant les arguments supplémentaires requis, voyez [l'exécution de balayages de paramètres...](https://www.comsol.com/support/knowledgebase/1250) et [l'utilisation des séquences de tâches...](https://www.comsol.com/blogs/how-to-use-job-sequences-to-save-data-after-solving-your-model/). La fonctionnalité permettant de soumettre des simulations de balayage de paramètres à la file d'attente d'une grappe depuis l'interface graphique de COMSOL à l'aide du [nœud de balayage de grappe (*Cluster Sweep*)](https://www.comsol.com/blogs/how-to-use-the-cluster-sweep-node-in-comsol-multiphysics/) n'est pas offerte actuellement.