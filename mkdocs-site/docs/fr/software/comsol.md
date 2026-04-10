---
title: "COMSOL/fr"
slug: "comsol"
lang: "fr"

source_wiki_title: "COMSOL/fr"
source_hash: "38eec14cd7b3d1daca54aaa4b9d0b3ea"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:10:16.447321+00:00"

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

## Introduction

[COMSOL](http://www.comsol.com) est un logiciel polyvalent de modélisation en ingénierie. Nous remercions COMSOL Inc. pour l'entente spéciale d'hébergement de son application.

Avant d'utiliser COMSOL avec nos grappes, nous vous recommandons de consulter l'aide sous *Fichier -> Aide -> Documentation*. Au bas de la [page d'accueil de COMSOL](http://www.comsol.com) se trouvent des liens vers le blogue, la base de connaissances, le soutien technique et la documentation. Vous pouvez également [consulter la documentation en ligne](https://doc.comsol.com/).

## Votre licence

Notre organisation fournit l'hébergement pour COMSOL. Dans ce contexte, COMSOL est installé sur nos grappes, mais nous n'avons pas une licence générique fournissant un accès généralisé. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes.

Vous pouvez aussi acheter une licence auprès de [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) pour une utilisation au Canada. Une fois que l'aspect légal de votre licence est réglé, il faut passer à l'aspect technique. Notre équipe technique communiquera avec votre gestionnaire de licence pour que nos nœuds de calcul puissent avoir accès à votre serveur de licence. Si vous avez acheté une licence de CMC et que vous voulez vous connecter au serveur de licence de CMC, cet aspect technique est déjà réglé. Quand le serveur de licence est prêt et que vous avez créé *~/.licenses/comsol.lic*, chargez un module COMSOL que vous pourrez utiliser. Si ceci ne fonctionne pas, contactez notre [soutien technique](technical-support.md).

### Configuration de votre fichier de licence

Notre module COMSOL cherche l'information en rapport avec la licence à différents endroits, dont votre répertoire *~/.licenses*. Si vous avez votre propre serveur de licence, indiquez-le en créant le fichier texte `$HOME/.licenses/comsol.lic` avec les informations suivantes :

```text
SERVER <server> ANY <port>
USE_SERVER
```

où `<server>` est votre serveur de licence et `<port>` est le numéro du port du serveur de licence.

#### Configuration d'une licence locale

Si vous voulez utiliser un nouveau serveur de licence de votre établissement, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](technical-support.md) 1. le numéro du port flex TCP lmgrd de COMSOL (habituellement 1718 par défaut), 2. le numéro du port statique TCP LMCOMSOL propre au vendeur (habituellement 1719 par défaut) et 3. le nom d’hôte pleinement qualifié de votre serveur de licence COMSOL.
Créez ensuite le fichier texte *comsol.lic* tel que montré plus haut.

#### Configuration d'une licence CMC

Si vous avez une licence avec CMC, utilisez les paramètres IP publics préconfigurés dans le fichier *comsol.lic* :

*   Fir: `SERVER 172.26.0.101 ANY 6601`
*   Nibi: `SERVER 10.25.1.56 ANY 6601`
*   Narval/Rorqual: `SERVER 10.100.64.10 ANY 6601`
*   Trillium: `SERVER scinet-cmc ANY 6601`

Par exemple, un fichier de licence créé sur la grappe Nibi ressemblerait à ceci :
```bash
cat ~/.licenses/comsol.lic
```
```text
SERVER 10.25.1.56 ANY 6601
USE_SERVER
```

Si vous ne pouvez pas obtenir la licence, demandez de l'assistance en cliquant sur [https://www.cmc.ca/fr/soutien/](https://www.cmc.ca/fr/soutien/).

### Vérifier l'utilisation des licences

Pour déterminer le nombre de licences utilisées par vos tâches COMSOL en cours d'exécution, il faut interroger le serveur de licences. Comme indiqué [ici](https://www.comsol.com/support/knowledgebase/1142), cela peut se faire à l'aide de la commande `lmstat`. Cependant, cette commande n'étant pas installée par défaut avec COMSOL, la solution de contournement suivante, qui utilise la commande `lmutil` du module Ansys le plus récent, peut être exécutée sur n'importe quel nœud de connexion. Si vous utilisez le fichier standard `~/.licenses/comsol.lic` pour identifier le serveur de licences, cette méthode devrait fonctionner, mais le délai de réponse peut atteindre une minute si le serveur est occupé.

```bash
module load ansys; $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c ~/.licenses/comsol.lic -a | sed '/^$/d' | egrep 'License|UP|$USER|Total of'  | grep -v 'Total of 0'
```

### Produits installés

Pour connaître les [modules et produits](https://www.comsol.com/products) que vous pouvez utiliser, lancez COMSOL [en mode graphique](comsol.md#mode-graphique) et cliquez sur *Options -> Produits licenciés et utilisés* dans le menu déroulant du haut. Pour l'explication détaillée, [cliquez ici](https://doc.comsol.com/6.0/docserver/#!/com.comsol.help.comsol/comsol_ref_customizing.16.09.html). Si un module ou un produit est absent ou si la licence n'existe pas, contactez le [soutien technique](technical-support.md), car vous devrez peut-être réinstaller le module CVMFS que vous utilisez.

### Versions installées

Pour vérifier le numéro de version complet d'un module, démarrez COMSOL [en mode graphique](comsol.md#mode-graphique) et regardez dans le coin inférieur droit de la fenêtre de messages OU plus simplement, connectez-vous à une grappe et exécutez les commandes suivantes en mode *batch* :
```bash
salloc --time=0:01:00 --nodes=1 --cores=1 --mem=1G --account=def-someuser
module load comsol/6.2
comsol batch -version
```
```text
COMSOL Multiphysics 6.2.0.290
```
qui dans ce cas correspond à COMSOL 6.2 Mise à jour 1. Autrement dit, quand une [nouvelle version de COMSOL](https://www.comsol.com/release-history) est installée, elle utilise le format abrégé de 6.X mais pour des raisons pratiques, elle contient la plus récente version en date de l'installation. Quand [d'autres versions sont disponibles](https://www.comsol.com/product-update), elles utiliseront le format 6.X.Y.Z. Par exemple, [Mise à jour 3](https://www.comsol.com/product-update/6.2) peut être chargée sur une grappe avec les commandes `module load comsol/6.2.0.415` OU `module load comsol`. Nous vous recommandons d'utiliser la plus récente version pour profiter de la dernière mise à jour. Cependant, si vous voulez continuer d'utiliser une version 6.X ou 6.X.Y.Z, sachez que par définition, le logiciel dans ces modules sera le même.

Pour connaître les versions qui sont disponibles dans l'environnement standard que vous avez chargé (règle générale, il s'agit de `StdEnv/2023`), lancez la commande `module avail comsol`. Pour connaître les versions qui sont disponibles dans TOUS les environnements standards, lancez la commande `module spider comsol`.

Le module `comsol/6.3` correspond à la version [6.3.0.290](https://www.comsol.com/product-download/6.3) et est disponible sur toutes nos grappes.

## Soumettre des tâches

### Exécution sur un seul nœud

Le script suivant utilise huit cœurs sur un seul nœud.

```bash title="mysub1.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Spécifiez (j-hh:mm)
#SBATCH --account=def-group        # Spécifiez (un compte)
#SBATCH --mem=32G                  # Spécifiez (0 pour utiliser toute la mémoire sur chaque nœud)
#SBATCH --cpus-per-task=8          # Spécifiez (valeur max de tous les cœurs sur un nœud)
#SBATCH --nodes=1                  # Ne pas modifier
#SBATCH --ntasks-per-node=1        # Ne pas modifier

INPUTFILE="ModelToSolve.mph"       # indiquer le nom du fichier en entrée
OUTPUTFILE="SolvedModel.mph"       # indiquer le nom du fichier en sortie

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

comsol batch -inputfile ${INPUTFILE} -outputfile ${OUTPUTFILE} -np $SLURM_CPUS_ON_NODE
```

Selon la complexité de la simulation, il est possible que COMSOL n'utilise pas efficacement plusieurs cœurs. Il est donc suggéré de vérifier la scalabilité de la simulation en augmentant graduellement le nombre de cœurs. Si l'accélération est presque linéaire avec tous les cœurs d'un nœud, considérez l'exécution de la tâche avec plusieurs nœuds entiers en ajustant le script ci-dessous.

### Exécution sur plusieurs nœuds

Le script suivant utilise 8 cœurs distribués également sur 2 nœuds. Ce script est idéal pour les très grosses simulations (qui dépassent les capacités d'un simple nœud) et permet de redémarrer des tâches interrompues, d'allouer de gros fichiers temporaires dans l'espace /scratch et d'utiliser les paramètres par défaut du fichier *comsolbatch.ini*. Une option permettant de modifier le monceau Java est décrite sous le script.

```bash title="script-dis.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Spécifiez (j-hh:mm)
#SBATCH --account=def-account      # Spécifiez (un compte)
#SBATCH --mem=16G                  # Spécifiez (0 pour utiliser toute la mémoire sur chaque nœud)
#SBATCH --cpus-per-task=4          # Spécifiez (valeur max de tous les cœurs sur un nœud)
#SBATCH --nodes=2                  # Spécifiez (le nombre de nœuds de calcul à utiliser pour la tâche)
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
    Si votre tâche plante au démarrage en raison d'une erreur de segmentation Java, augmentez le monceau (*heap*), ajoutez les deux lignes `sed` immédiatement après les commandes `cp -f`. Si le problème n'est toujours pas réglé, remplacez 4G par 8G sur les deux lignes.
    Pour plus d'information, voir [Mémoire insuffisante](https://www.comsol.ch/support/knowledgebase/1243).
    ```bash
    sed -i 's/-Xmx2g/-Xmx4g/g' comsolbatch.ini
    sed -i 's/-Xmx768m/-Xmx4g/g' java.opts
    ```

!!! note "Remarque 3"
    Il arrive que certaines tâches soient lentes ou qu'elles gèlent au lancement quand *script-smp.sh* est exécuté sur un seul nœud. Si c'est le cas, utilisez plutôt le script pour nœuds multiples *script-dis.sh* ci-dessus, en y ajoutant `#SBATCH --nodes=1` et créez ensuite un billet d'assistance pour rapporter le problème en indiquant le numéro de la tâche et le nom de la grappe.

## Mode graphique

Pour exécuter COMSOL en mode graphique, ouvrez un bureau distant sur un système [OnDemand](nibi.md#accès-via-open-ondemand-ood) ou JupyterLab en cliquant sur les liens ci-dessous. Remarque : L'ancienne méthode utilisant un client/serveur [TigerVNC](vnc.md) devrait toujours fonctionner, mais elle n'est plus recommandée ni prise en charge. Quelle que soit la méthode utilisée, le fichier `~/.licenses/comsol.lic` doit être configuré d'avance. Notez que la commande `module avail comsol` affichera les versions de COMSOL disponibles dans la version de StdEnv actuellement chargée (par exemple, `StdEnv/2023`). Si vous constatez que les éléments du menu supérieur sont grisés et non cliquables après avoir démarré COMSOL en mode GUI, alors votre fichier *~/.comsol* est peut-être corrompu; essayez donc de le supprimer.

### OnDemand

1.  Sur votre bureau, lancez une session OnDemand en cliquant sur une des URL ci-dessous :
    *   [Nibi](nibi.md#accès-via-open-ondemand-ood) : `https://ondemand.sharcnet.ca`
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

1.  Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Sélectionnez un module COMSOL (par exemple `comsol/6.4`) dans la section *Modules disponibles* de gauche.
3.  Pour le module, cliquez sur *Charger* pour faire afficher l'icône `Comsol (VNC)`.
4.  Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

## Exploration des paramètres

### Exploration en lots

En mode interactif avec l'interface graphique, les problèmes de paramètres peuvent être résolus avec l'approche [Exploration par lot (*Batch Sweep*)](https://www.comsol.com/blogs/the-power-of-the-batch-sweep/). Voyez [cette vidéo démontrant des explorations multiples](https://www.comsol.com/video/performing-parametric-sweep-study-comsol-multiphysics). Il est aussi possible d'obtenir l'accélération [en parallélisant les tâches](https://www.comsol.com/blogs/added-value-task-parallelism-batch-sweeps/).

### Exploration d'une grappe

Pour faire l'exploration d'une grappe, une tâche doit être soumise en ligne de commande à l'ordonnanceur avec `sbatch slurmscript`. Pour connaître les détails en rapport avec les arguments additionnels requis, voyez les pages [Exécution d'explorations paramétriques... (*Running parametric sweeps...*)](https://www.comsol.com/support/knowledgebase/1250) et [Comment utiliser les séquences de tâches... (*How to use Job Sequences...*)](https://www.comsol.com/blogs/how-to-use-job-sequences-to-save-data-after-solving-your-model/). La fonctionnalité permettant de soumettre des simulations des paramètres à la queue d'une grappe à partir de l'interface graphique de COMSOL avec le [nœud d'exploration de grappe (*Cluster Sweep*)](https://www.comsol.com/blogs/how-to-use-the-cluster-sweep-node-in-comsol-multiphysics/) n'est pas offerte présentement.