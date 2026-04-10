---
title: "Nextflow/fr"
slug: "nextflow"
lang: "fr"

source_wiki_title: "Nextflow/fr"
source_hash: "a3179b66e3f1da77a3de9727b6e0f589"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:15:20.731460+00:00"

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

[Nextflow](https://www.nextflow.io) est un logiciel permettant d'exécuter des flux de travail scientifiques reproductibles. Le terme *Nextflow* est utilisé pour décrire à la fois le langage spécifique au domaine (DSL) dans lequel les pipelines sont écrits et le logiciel utilisé pour interpréter ces flux de travail.

## Utilisation
Chargez le module Nextflow avec `module load nextflow`.

Bien que vous puissiez créer votre propre flux de travail, vous pouvez également utiliser les pipelines [nf-core](https://nf-co.re/) qui sont publiés. Nous décrivons ici une configuration simple qui vous permettra d'exécuter des pipelines nf-core sur nos systèmes et vous aidera à configurer correctement Nextflow pour vos propres pipelines.

Dans notre exemple, nous utilisons le pipeline `nf-core/rnaseq` en 5 étapes :

*   Étape 1 : Préparer le fichier de configuration
*   Étape 2 : Installer nf-core
*   Étape 3 : Télécharger les images du conteneur et le pipeline
*   Étape 4 : Préparer les données en entrée
*   Étape 5 : Créer un script pour la tâche

### Étape 1 : Préparer le fichier de configuration

Vous pouvez obtenir de [nf-core](https://github.com/nf-core/configs/blob/master/conf/alliance_canada.config) un fichier de configuration pour nos grappes et le placer dans `~/.nextflow/config` comme suit :

```bash
curl -o ~/.nextflow/config https://raw.githubusercontent.com/nf-core/configs/refs/heads/master/conf/alliance_canada.config
```

Configurez la variable d'environnement `$SLURM_ACCOUNT` pour un nom de compte que vous pouvez utiliser; ceci devrait ressembler à `def-pname` et se faire dans le fichier `~/.bashrc`.

```bash
export SLURM_ACCOUNT=def-pname
```

Cette configuration contient des profils pour Fir, Narval, Nibi, Rorqual et Trillium. Si vous utilisez ce fichier de configuration sur Fir, vous devez charger le profil avec l'indicateur `-profile fir` de la commande `nextflow`.
Sur les autres sites, le profil approprié est sélectionné automatiquement en fonction du nom de l'hôte. Il garantit qu'il n'y a pas plus de 100 tâches dans la file d'attente Slurm et que 60 tâches maximum sont soumises par minute. Il contient des informations spécifiques à la grappe qui sont nécessaires à Nextflow, par exemple que les machines Rorqual disposent de 192 cœurs et de 750 Go de RAM, avec une durée maximale d'une semaine (168 heures).

!!! warning "Important"
    Il n'est pas recommandé d’exécuter des pipelines nf-core ou tout autre pipeline Nextflow générique sur Trillium. Ceux-ci devraient être exécutés sur [Trillium](trillium.md) uniquement s’ils ont été conçus spécifiquement pour Trillium.

La configuration est liée au système sur lequel se fait l'exécution, mais elle est également liée au pipeline lui-même. Dans cet exemple rnaseq, `cpu = 1` est la valeur par défaut, mais certaines étapes du pipeline peuvent en utiliser plus. Cela peut devenir assez compliqué et les étiquettes dans le fichier `nf-core-rnaseq_3.21.0/3_21_0/conf/base.config` sont utilisées par le pipeline à l'interne pour identifier une étape avec une configuration autre que celle par défaut. Nous n'abordons pas ce sujet ici, mais sachez qu'en modifiant ces étiquettes, vous pourriez observer des différences importantes dans le temps de mise en file d'attente et le temps d'exécution du pipeline.

### Étape 2 : Installer nf-core

Pour utiliser les pipelines nf-core sur une de nos grappes, il est nécessaire de les télécharger sur un nœud de connexion, car certaines grappes ne permettent pas l'accès à Internet à partir des nœuds de calcul.
Exécutez la commande suivante **sur un nœud de connexion** pour installer `nf-core`.
```bash
module purge
module load python/3.11
module load rust         # New nf-core installations will error out if rust hasn't been loaded
module load postgresql   # Python modules which list psycopg2 as a dependency may crash without postgresql here.
python -m venv nf-core-env
source nf-core-env/bin/activate
python -m pip install nf_core==2.13
```

Pour faciliter la configuration, nous utilisons `pip` pour installer un paquet [Python](python.md). L'installation des outils nf-core peut être longue; cette étape peut prendre plusieurs minutes.

### Étape 3 : Télécharger les images du conteneur et le pipeline

Définissez le nom du pipeline à tester, puis chargez Nextflow et l'utilitaire [Apptainer](apptainer.md).
Nextflow s'intègre parfaitement à Apptainer.
Comme indiqué précédemment, nous utilisons le pipeline `rnaseq` à titre d'exemple.

```bash
export NFCORE_PL=rnaseq
export PL_VERSION=3.21.0
module load nextflow
module load apptainer
```

Créez un répertoire qui servira de cache.

```bash
mkdir /project/<def-group>/NXF_SINGULARITY_CACHEDIR
export NXF_SINGULARITY_CACHEDIR=/project/<def-group>/NXF_SINGULARITY_CACHEDIR
```

Nextflow stockera les images dans le répertoire indiqué par `$NXF_SINGULARITY_CACHEDIR`; comme Apptainer est dérivé de Singularity, le nom de la variable n'a pas changé.
Les images de flux de travail étant généralement volumineuses, ne les stockez pas dans votre espace personnel (`$HOME`) en raison de sa capacité limitée.
Stockez-les plutôt dans `/project`.

Partagez ce dossier avec les membres de votre groupe qui utiliseront Nextflow avec Apptainer, afin de réduire la duplication et utiliser moins d'espace.
De plus, vous pouvez ajouter la commande `export` à votre `~/.bashrc` pour plus de commodité.

Pour télécharger le pipeline `rnaseq` et les images du conteneur, lancez :

```bash
cd ~/scratch
mkdir -p nf-test && cd nf-test
nf-core download --container-cache-utilisation amend --container-system singularity --compress none -l docker.io -r ${PL_VERSION} -p 6 ${NFCORE_PL}
```

À la question « Include the nf-core's default institutional configuration files into the download? (Y/n) », répondez Y.

!!! important "Important"
    Ceci télécharge deux composantes de `rnaseq` :

    1.  Les fichiers des images du conteneur vont dans `$NXF_SINGULARITY_CACHEDIR`.
    2.  Les fichiers de pipelines vont dans le répertoire `~/scratch/nf-test/nf-core-${NFCORE_PL}_${PL_VERSION}` avec le numéro de version `X_X_X`. Dans notre exemple, le pipeline est stocké dans `~/scratch/nf-test/nf-core-rnaseq_3.21.0/3_21_0`. Notez que le nom de répertoire `nf-core-rnaseq_3.21.0/3_21_0` doit être inclus quand `nextflow run` est appelé dans le script de la tâche (voir l'étape 5 ci-dessous).

Au lancement du pipeline, Nextflow tiendra compte du fichier `nextflow.config` dans le répertoire de travail ainsi que du fichier `~/.nextflow/config` (s'il existe) dans votre répertoire personnel afin de contrôler l'exécution du flux.
Les pipelines nf-core ont tous une configuration par défaut, une configuration de test et des configurations de conteneurs (Singularity, Podman, etc.).

### Étape 4 : Préparer les fichiers d'entrée

Nextflow utilise en entrée des fichiers de séquences et une feuille d'échantillons (''sample sheet'').
Pour télécharger les fichiers de séquences nécessaires à notre exemple `rnaseq`, exécutez :

```bash
cd ~/scratch/nf-test
mkdir -p input && cd input
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357070_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357070_2.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357071_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357071_2.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357072_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357072_2.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357073_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357074_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357075_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357076_1.fastq.gz
wget https://raw.githubusercontent.com/nf-core/test-datasets/rnaseq/testdata/GSE110004/SRR6357076_2.fastq.gz
```

Pour préparer un exemple de feuille, copiez et collez le code suivant dans `~/scratch/nf-test/samplesheet.csv`, puis remplacez le nom de l'utilisateur par le vôtre.

```text
sample,fastq_1,fastq_2,strandedness
WT_REP1,/home/<username>/scratch/nf-test/input/SRR6357070_1.fastq.gz,/home/<username>/scratch/nf-test/input/SRR6357070_2.fastq.gz,reverse
WT_REP1,/home/<username>/scratch/nf-test/input/SRR6357071_1.fastq.gz,/home/<username>/scratch/nf-test/input/SRR6357071_2.fastq.gz,reverse
WT_REP2,/home/<username>/scratch/nf-test/input/SRR6357072_1.fastq.gz,/home/<username>/scratch/nf-test/input/SRR6357072_2.fastq.gz,reverse
RAP1_UNINDUCED_REP1,/home/<username>/scratch/nf-test/input/SRR6357073_1.fastq.gz,,reverse
RAP1_UNINDUCED_REP2,/home/<username>/scratch/nf-test/input/SRR6357074_1.fastq.gz,,reverse
RAP1_UNINDUCED_REP2,/home/<username>/scratch/nf-test/input/SRR6357075_1.fastq.gz,,reverse
RAP1_IAA_30M_REP1,/home/<username>/scratch/nf-test/input/SRR6357076_1.fastq.gz,/home/<username>/scratch/nf-test/input/SRR6357076_2.fastq.gz,reverse
```

Vous pouvez bien sûr utiliser vos propres données.
Pour en savoir plus sur l'exemple et les feuilles `rnaseq`, voir [la documentation](https://nf-co.re/rnaseq/3.2/docs/usage).

### Étape 5 : Créer un script de tâche

Voici un exemple de script à utiliser sur Fir.
Adaptez-le pour utiliser les éléments suivants :
*   pipeline (`NFCORE_PL`) et version (`PL_VERSION, FD_VERSION`)
*   chemin de la cache Apptainer (`NXF_SINGULARITY_CACHEDIR`)
*   compte Slurm (`SLURM_ACCOUNT`)
*   grappe (`-profile ...,fir`)
*   chemins pour `--input` et `--output`

```bash
#!/bin/bash
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

module load python/3.11
source nf-core-env/bin/activate
module load apptainer
module load nextflow
export NFCORE_PL=rnaseq
export PL_VERSION=3.21.0
export FD_VERSION=3_21_0
export NXF_SINGULARITY_CACHEDIR=/project/<def-group>/NXF_SINGULARITY_CACHEDIR
export SLURM_ACCOUNT=def-pname

nextflow run nf-core-${NFCORE_PL}_${PL_VERSION}/${FD_VERSION}/ \
 -profile test,singularity,fir \
 --input ~/scratch/nf-test/input/samplesheet.csv --outdir ~/scratch/nf-test/output
```

Enregistrez le script de tâche dans `~/scratch/nf-test/nextflow_test.sh`, puis soumettez-le avec `sbatch nextflow_test.sh` pour lancer l'exécution du test.

Nextflow est maintenant démarré sur le nœud de calcul. Ceci achemine les tâches à l'ordonnanceur Slurm quand elles sont prêtes à être traitées.

Vous pouvez suivre la progression du pipeline dans le fichier journal `nextflow_test.<job_ID>.out`. Vous pouvez également examiner les tâches dans la file d'attente Slurm avec `sq` ou `squeue -u $USER`.

Pour plus d'information sur les configurations et les profils, voir :
*   [Configuration](https://www.nextflow.io/docs/latest/config.html)
*   [Configuration du pipeline](https://nf-co.re/docs/usage/getting_started/configuration#basic-configuration-profiles)

## Problèmes connus

Notez que Nextflow est principalement écrit en Java, un langage qui consomme beaucoup de mémoire virtuelle. Sur certaines grappes, cela peut poser problème lors de l'exécution à partir d'un nœud de connexion.

Prenez garde si vous avez une configuration AWS dans votre répertoire `~/.aws`, car Nextflow pourrait signaler qu'il ne peut pas télécharger l'ensemble de données de test du pipeline avec votre identifiant par défaut.

### Message : *« unable to create native thread »*

Nous avons constaté l'erreur suivante :
```
java.lang.OutOfMemoryError: unable to create native thread: possibly out of memory or process/resource limits reached
[error][gc,task] GC Failed to create worker thread
```
Nous croyons que l'erreur se produit quand Java tente de créer autant de fils que le nombre de cœurs physiques de l'ordinateur.
Il semble que l'erreur est résolue quand `nextflow` est exécuté avec `export NXF_OPTS='-XX:ActiveProcessorCount=1'`.

### SIGBUS

Des erreurs `SIGBUS` du processus principal de Nextflow ont été signalées.
Nous soupçonnons que c'est à cause des problèmes Nextflow suivants :
*   [https://github.com/nextflow-io/nextflow/issues/842](https://github.com/nextflow-io/nextflow/issues/842)
*   [https://github.com/nextflow-io/nextflow/issues/2774](https://github.com/nextflow-io/nextflow/issues/2774)
Le fait de définir la variable d'environnement `NXF_OPTS="-Dleveldb.mmap=false"` à l'exécution de `nextflow` semble résoudre le problème.