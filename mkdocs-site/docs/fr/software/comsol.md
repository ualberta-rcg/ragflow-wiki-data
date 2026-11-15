---
title: "COMSOL/fr"
slug: "comsol"
lang: "fr"

source_wiki_title: "COMSOL/fr"
source_hash: "75070edaf6487c1267aa8ed450080529"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:26:10.155500+00:00"

tags:
  - software

keywords:
  - "menu supérieur grisé"
  - "Cluster Sweep"
  - "fichier comsol.lic"
  - "~/.comsol corrompu"
  - "produits installés"
  - "licence"
  - "mode graphique"
  - "#SBATCH --nodes=1"
  - "module avail comsol"
  - "Batch Sweep"
  - "versions de COMSOL"
  - "vérifier l'utilisation des licences"
  - "module comsol"
  - "script-dis.sh"
  - "#SBATCH --cpus-per-task=8"
  - "OnDemand"
  - "versions installées"
  - "répertoire de récupération"
  - "serveur COMSOL"
  - "#SBATCH --mem=32G"
  - "INPUTFILE=\"ModelToSolve.mph\""
  - "serveur de licence"
  - "scalabilité de la simulation"
  - "~/.licenses/comsol.lic"
  - "soumission de tâches"
  - "licence COMSOL"
  - "commande"
  - "licence CMC"
  - "COMSOL"
  - "terminal d'un nœud de connexion"
  - "OUTPUTFILE=\"SolvedModel.mph\""
  - "JupyterHub"
  - "comsol batch"

questions:
  - "Comment créer et configurer le fichier ~/.licenses/comsol.lic pour se connecter à un serveur de licence COMSOL ou CMC ?"
  - "Quelles démarches sont nécessaires pour obtenir, valider et activer une licence COMSOL au sein de notre organisation ou via CMC ?"
  - "Comment vérifier le nombre de licences COMSOL actuellement utilisées sur les nœuds de calcul ?"
  - "Quelle tâche accomplit la commande à copier‑coller dans le terminal d’un nœud de connexion ?"
  - "Quel fichier la commande lit‑elle pour déterminer le serveur COMSOL utilisé ?"
  - "Sur quels nœuds de connexion (Nibi, Narval, Rorqual, Trillium) et sous quelles conditions la commande peut‑elle ne pas fonctionner selon la configuration des serveurs des établissements ?"
  - "Comment vérifier les licences disponibles et actives pour les produits COMSOL sur le système ?"
  - "Quelle commande permet d’afficher les versions de COMSOL installées et de choisir la version la plus récente ?"
  - "Comment soumettre une tâche COMSOL sur un seul nœud en utilisant le script d’exemple fourni ?"
  - "Quels paramètres faut‑il ajuster dans le script pour exécuter une simulation COMSOL sur plusieurs nœuds et répartir les cœurs correctement ?"
  - "Comment corriger les erreurs de segmentation Java ou les problèmes de mémoire en modifiant les fichiers comsolbatch.ini et java.opts ?"
  - "Quelles sont les méthodes recommandées pour lancer COMSOL en mode graphique sur le cluster et quelles précautions prendre concernant le fichier de licence et le fichier ~/.comsol ?"
  - "Quelle quantité de mémoire est allouée à chaque nœud dans ce script SLURM ?"
  - "Combien de cœurs CPU sont réservés pour chaque tâche ?"
  - "Quels sont les noms des fichiers d'entrée et de sortie spécifiés dans le script ?"
  - "Comment lancer une session OnDemand depuis le bureau et charger le module COMSOL correspondant à la version souhaitée ?"
  - "Quelle est la procédure pour démarrer COMSOL via JupyterHub, incluant la sélection et le chargement du module ?"
  - "Quelles sont les méthodes d’exploration des paramètres proposées (Batch Sweep vs. Cluster Sweep) et comment soumettre un sweep sur une grappe avec `sbatch` ?"
  - "Quelle configuration doit être effectuée sur le fichier <code>~/.licenses/comsol.lic</code> avant d’utiliser COMSOL ?"
  - "Quelle commande permet d’afficher les versions de COMSOL disponibles dans la version de StdEnv actuellement chargée ?"
  - "Que faut‑il faire si les éléments du menu supérieur sont grisés et non cliquables après le démarrage de COMSOL en mode GUI ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction
[COMSOL](http://www.comsol.com) est un logiciel d'usage général pour la modélisation en ingénierie. Nous remercions COMSOL Inc. pour l'entente spéciale d'hébergement de son application.

Avant d'utiliser COMSOL avec nos grappes, nous vous recommandons de consulter l'aide sous *Fichier -> Aide -> Documentation*. Au bas de la [page d'accueil de COMSOL](http://www.comsol.com) se trouvent des liens vers le blogue, la base de connaissances, le soutien technique et la documentation. Vous pouvez également [consulter la documentation en ligne](https://doc.comsol.com/).

## Votre licence
Notre organisation fournit l'hébergement pour COMSOL. Dans ce contexte, COMSOL est installé sur nos grappes, mais nous n'avons pas une licence générique fournissant un accès généralisé. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes.
Vous pouvez aussi acheter une licence auprès de [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) pour une utilisation au Canada. Une fois que l'aspect légal de votre licence est réglé, il faut passer à l'aspect technique. Notre équipe technique communiquera avec votre gestionnaire de licence pour que nos nœuds de calcul puissent avoir accès à votre serveur de licence. Si vous avez acheté une licence de CMC et que vous voulez vous connecter au serveur de licence de CMC, cet aspect technique est déjà réglé. Quand le serveur de licence est prêt et que vous avez créé *~/.licenses/comsol.lic*, chargez un module COMSOL que vous pourrez utiliser. Si ceci ne fonctionne pas, contactez notre [soutien technique](../support/technical_support.md).

### Configuration de votre fichier de licence
Notre module COMSOL cherche l'information en rapport avec la licence à différents endroits, dont votre répertoire *~/.licenses*. Si vous avez votre propre serveur de licence, indiquez-le en créant le fichier texte `$HOME/.licenses/comsol.lic` avec les informations suivantes :

```bash linenums="1" title="comsol.lic"
SERVER <server> ANY <port>
USE_SERVER
```

où `<server>` est votre serveur de licence et `<port>` est le numéro du port du serveur de licence.

#### Configuration d'une licence locale

Si vous voulez utiliser un nouveau serveur de licence de votre établissement, des modifications devront être apportées du côté de l'Alliance et de celui de l'établissement. Pour ce faire, faites parvenir à notre [soutien technique](../support/technical_support.md) 1. le numéro du port flex TCP lmgrd de COMSOL (habituellement 1718 par défaut), 2. le numéro du port statique TCP LMCOMSOL propre au vendeur (habituellement 1719 par défaut) et 3. le nom d’hôte pleinement qualifié de votre serveur de licence COMSOL.
Créez ensuite le fichier texte *comsol.lic* tel que montré plus haut.

#### Configuration d'une licence CMC

Si vous avez une licence avec CMC, utilisez les paramètres IP publics préconfigurés dans le fichier *comsol.lic* :

*   Fir: `SERVER 172.26.0.101 ANY 6601`
*   Nibi: `SERVER 10.25.1.56 ANY 6601`
*   Narval/Rorqual: `SERVER 10.100.64.10 ANY 6601`
*   Trillium: `SERVER scinet-cmc ANY 6601`

Par exemple, un fichier de licence créé sur la grappe Nibi ressemblerait à ceci :

```text linenums="1" title="~/.licenses/comsol.lic"
SERVER 10.25.1.56 ANY 6601
USE_SERVER
```

Si vous ne pouvez pas obtenir la licence, demandez de l'assistance en cliquant sur [https://www.cmc.ca/fr/soutien/](https://www.cmc.ca/fr/soutien/).

### Vérifier l'utilisation des licences

Pour déterminer le nombre de licences utilisées par vos tâches COMSOL en cours d'exécution, il faut interroger le serveur de licences. Comme décrit dans [https://www.comsol.com/supportknowledgebase/1142](https://www.comsol.com/supportknowledgebase/1142), ceci peut se faire avec la commande `lmutil`. Cependant, cette commande n'étant pas installée par défaut avec COMSOL, vous pouvez utiliser la commande ci-dessous. Pour ce faire, copiez-collez simplement cette commande dans la fenêtre de terminal d'un nœud de connexion et appuyez sur Entrée. La commande lira `~/.licenses/comsol.lic` pour déterminer le serveur COMSOL utilisé et peut prendre environ 30 secondes. Bien qu'elle fonctionne sur tous les nœuds de connexion de Nibi, Narval, Rorqual ou Trillium si vous avez une licence CMC, elle peut ne pas fonctionner dépendant de la configuration des serveurs des différents établissements.

```bash
touch ~/.licenses/ansys.lic; module load ansys; $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c ~/.licenses/comsol.lic -a | sed '/^$/d' | egrep 'License|UP|$USER|Total of'  | grep -v 'Total of 0'; module unload ansys
```

### Produits installés

Pour connaître les [modules et produits](https://www.comsol.com/products) que vous pouvez utiliser, lancez COMSOL [en mode graphique](comsol.md#mode-graphique) et cliquez sur *Options -> Produits sous licence et utilisés* dans le menu déroulant du haut. Pour l'explication détaillée, [cliquez ici](https://doc.comsol.com/6.0/docserver/#!/com.comsol.help.comsol/comsol_ref_customizing.16.09.html). Si un module ou un produit est absent ou si la licence n'existe pas, contactez le [soutien technique](../support/technical_support.md), car vous devrez peut-être réinstaller le module CVMFS que vous utilisez.

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

```bash linenums="1" title="mysub1.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Specify (d-hh:mm)
#SBATCH --account=def-group        # Specify (some account)
#SBATCH --mem=32G                  # Specify (0 to use all memory on each node)
#SBATCH --cpus-per-task=8          # Specify (max value of all cores on a node)
#SBATCH --nodes=1                  # Do not change
#SBATCH --ntasks-per-node=1        # Do not change

INPUTFILE="ModelToSolve.mph"       # indiquer le nom du fichier en entrée
OUTPUTFILE="SolvedModel.mph"       # indiquer le nom du fichier en sortie

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

RECOVERYDIR=$SCRATCH/comsol/recoverydir
mkdir -p $RECOVERYDIR

comsol batch -inputfile ${INPUTFILE} -outputfile ${OUTPUTFILE} -np $SLURM_CPUS_ON_NODE \
-tmpdir $SLURM_TMPDIR -recoverydir $RECOVERYDIR \
# -recover
```

Selon la complexité de la simulation, il est possible que COMSOL n'utilise pas efficacement plusieurs cœurs. Il est donc suggéré de vérifier la scalabilité de la simulation en augmentant graduellement le nombre de cœurs. Si l'accélération est presque linéaire avec tous les cœurs d'un nœud, considérez l'exécution de la tâche avec plusieurs nœuds entiers en ajustant le script ci-dessous.

### Exécution sur plusieurs nœuds

Le script suivant utilise 8 cœurs distribués également sur 2 nœuds. Ce script est idéal pour les très grosses simulations (qui dépassent les capacités d'un simple nœud) et permet de redémarrer des tâches interrompues, d'allouer de gros fichiers temporaires dans l'espace /scratch et d'utiliser les paramètres par défaut du fichier *comsolbatch.ini*. Une option permettant de modifier le monceau Java est décrite sous le script.

```bash linenums="1" title="script-dis.sh"
#!/bin/bash
#SBATCH --time=0-03:00             # Specify (d-hh:mm)
#SBATCH --account=def-account      # Specify (some account)
#SBATCH --mem=16G                  # Specify (0 to use all memory on each node)
#SBATCH --cpus-per-task=4          # Specify (max value of all cores on a node)
#SBATCH --nodes=2                  # Specify (the number of compute nodes to use for the job)
#SBATCH --ntasks-per-node=1        # Do not change

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

comsol batch -inputfile $INPUTFILE -outputfile $OUTPUTFILE -np $SLURM_CPUS_ON_NODE \
-nn $SLURM_NNODES -comsolinifile comsolbatch.ini -alivetime 15 \
-tmpdir $SLURM_TMPDIR -recoverydir $RECOVERYDIR \
# -recover
```

!!! warning "Remarque 1"
    Si votre tâche plante au démarrage en raison d'une erreur de segmentation Java, augmentez le monceau (*heap*). Pour ce faire, ajoutez les deux lignes `sed` suivantes immédiatement après les commandes `cp -f`. Si le problème n'est toujours pas réglé, remplacez `4G` par `8G` sur les deux lignes. Pour plus d'information, consultez [Panne de mémoire](https://www.comsol.ch/support/knowledgebase/1243).

```bash
sed -i 's/-Xmx2g/-Xmx4g/g' comsolbatch.ini
sed -i 's/-Xmx768m/-Xmx4g/g' java.opts
```

!!! tip "Remarque 3"
    Il arrive que certaines tâches soient lentes ou qu'elles gèlent au lancement quand le script `script-smp.sh` est exécuté sur un seul nœud. Si c'est le cas, utilisez plutôt le script pour nœuds multiples `script-dis.sh` ci-dessus, en y ajoutant `#SBATCH --nodes=1`. Créez ensuite un billet d'assistance pour rapporter le problème, en indiquant le numéro de la tâche et le nom de la grappe.

## Mode graphique

Pour exécuter COMSOL en mode graphique, ouvrez un bureau distant sur un système [OnDemand](../clusters/nibi.md) ou JupyterLab en cliquant sur les liens ci-dessous. L'ancienne méthode utilisant un client/serveur [TigerVNC](../interactive/vnc.md) devrait toujours fonctionner, mais elle n'est plus recommandée ni prise en charge. Quelle que soit la méthode utilisée, le fichier `~/.licenses/comsol.lic` doit être configuré au préalable. Notez que la commande `module avail comsol` affichera les versions de COMSOL disponibles dans la version de StdEnv actuellement chargée (par exemple, `StdEnv/2023`). Si vous constatez que les éléments du menu supérieur sont grisés et non cliquables après avoir démarré COMSOL en mode GUI, alors votre fichier *~/.comsol* est peut-être corrompu; essayez donc de le supprimer.

### OnDemand
1. Sur votre bureau, lancez une session OnDemand en cliquant sur une des URL ci-dessous :
    *   [Nibi](../clusters/nibi.md) : `https://ondemand.sharcnet.ca`
    *   TRILLIUM : `https://ondemand.scinet.utoronto.ca`
2. Sur le bureau, ouvrez une nouvelle fenêtre de terminal et lancez les commandes correspondantes pour :
    *   **COMSOL 6.2 (ou versions plus récentes)**
        ```bash
        module load StdEnv/2023
        module load comsol/6.4
        comsol
        ```
    *   **COMSOL 6.1 (ou versions moins récentes)**
        ```bash
        module load StdEnv/2020
        module load comsol/6.1
        comsol
        ```

### JupyterLab
1. Sur votre bureau, lancez une session JupyterHub en cliquant sur une URL ci-dessous.
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2. Sélectionnez un module COMSOL (par exemple `comsol/6.4`) dans la section *Module disponible* de gauche.
3. Pour le module, cliquez sur *Charger* pour faire afficher l'icône `Comsol (VNC)`.
4. Cliquez sur l'icône et COMSOL devrait automatiquement démarrer sur un bureau Jupyter à distance.

## Exploration des paramètres

### Exploration en lots

En mode interactif avec l'interface graphique, les problèmes de paramètres peuvent être résolus avec l'approche [*Batch Sweep*](https://www.comsol.com/blogs/the-power-of-the-batch-sweep/). Voyez [cette vidéo démontrant des explorations multiples](https://www.comsol.com/video/performing-parametric-sweep-study-comsol-multiphysics). Il est aussi possible d'obtenir l'accélération [en parallélisant les tâches](https://www.comsol.com/blogs/added-value-task-parallelism-batch-sweeps/).

### Exploration d'une grappe

Pour faire l'exploration d'une grappe, une tâche doit être soumise en ligne de commande à l'ordonnanceur avec `sbatch slurmscript`. Pour connaître les détails en rapport avec les arguments additionnels requis, voyez les pages [*Running parametric sweeps...*](https://www.comsol.com/support/knowledgebase/1250) et [*How to use Job Sequences...*](https://www.comsol.com/blogs/how-to-use-job-sequences-to-save-data-after-solving-your-model/). La fonctionnalité permettant de soumettre des simulations des paramètres à la queue d'une grappe à partir de l'interface graphique de COMSOL avec le [nœud *Cluster Sweep*](https://www.comsol.com/blogs/how-to-use-the-cluster-sweep-node-in-comsol-multiphysics/) n'est pas offerte présentement.