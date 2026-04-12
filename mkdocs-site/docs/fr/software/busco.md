---
title: "BUSCO/fr"
slug: "busco"
lang: "fr"

source_wiki_title: "BUSCO/fr"
source_hash: "9fefb1c642155716acd1e62d6d998b07"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:45:13.637273+00:00"

tags:
  - software

keywords:
  - "Dépannage"
  - "DendroPy"
  - "Augustus config path"
  - "fichier de configuration"
  - "chemin complet"
  - "Erreur"
  - "exécution"
  - "installation"
  - "Téléchargement"
  - "run_BUSCO.py"
  - "Slurm"
  - "AUGUSTUS_CONFIG_PATH"
  - "Augustus"
  - "décompressés"
  - "SEPP"
  - "environnement virtuel"
  - "busco_downloads"
  - "ordonnanceur"
  - "BUSCO"
  - "commande wget"
  - "ensembles de données"
  - "génome"
  - "tâches de production"
  - "Wheel Python"
  - "assemblage de génomes"
  - "répertoire config"

questions:
  - "À quoi sert l'application BUSCO et quel est son objectif principal ?"
  - "Quelles sont les étapes requises pour installer une version récente de BUSCO à l'aide d'un environnement virtuel Python ?"
  - "Quelles sont les deux méthodes expliquées pour télécharger les ensembles de données nécessaires avant de soumettre une tâche ?"
  - "Quelle commande doit être utilisée pour décompresser les fichiers téléchargés ?"
  - "Quel outil en ligne de commande est présenté dans la section 6.2 pour effectuer les téléchargements ?"
  - "Quel est le chemin du répertoire à créer avant de lancer le téléchargement de la base de données bactérienne ?"
  - "Comment doit-on formuler la commande BUSCO pour analyser un seul génome par rapport à plusieurs génomes ?"
  - "Quelles sont les étapes et les paramètres recommandés pour soumettre une tâche BUSCO à l'ordonnanceur Slurm ?"
  - "Comment configurer les paramètres avancés tels qu'Augustus et SEPP pour une utilisation avec BUSCO ?"
  - "Comment activer l'environnement virtuel pour utiliser SEPP suite à une installation locale ?"
  - "Quelles modifications doivent être apportées au fichier de configuration de BUSCO pour lier correctement les outils externes ?"
  - "Comment configurer le répertoire d'Augustus et valider le bon fonctionnement de l'installation avec un test ?"
  - "Depuis quel endroit spécifique doit-on effectuer l'installation locale de SEPP dans l'environnement virtuel ?"
  - "Quelle commande permet d'activer l'environnement virtuel BUSCO requis pour cette procédure ?"
  - "Quelle dépendance logicielle doit être installée avec une version spécifique avant de télécharger SEPP ?"
  - "Quel est le message d'erreur spécifique abordé dans cette section de dépannage ?"
  - "Où doit-on copier le répertoire de configuration d'Augustus pour résoudre ce problème ?"
  - "Quelle variable d'environnement doit être exportée pour corriger cette erreur ?"
  - "Quel est le temps d'exécution maximum attendu pour la commande `run_BUSCO.py` présentée ?"
  - "Quelle procédure doit être suivie pour les tâches de production nécessitant un temps d'exécution plus long ?"
  - "Quels paramètres et variables d'environnement sont utilisés pour configurer et exécuter ce test BUSCO ?"
  - "Quel est le message d'erreur spécifique abordé dans cette section de dépannage ?"
  - "Où doit-on copier le répertoire de configuration d'Augustus pour résoudre ce problème ?"
  - "Quelle variable d'environnement doit être exportée pour corriger cette erreur ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

BUSCO (pour *Benchmarking Universal Single-Copy Orthologs*) est une application qui permet d'évaluer la complétude de l'assemblage et de l'annotation de génomes.

Pour plus d'information, consultez [le manuel de l'utilisateur](https://busco.ezlab.org/busco_userguide.html).

## Versions disponibles
Les versions récentes sont disponibles dans des *wheels* et les plus anciennes versions sont dans un module (voir la section [Modules](#modules) ci-dessous).

Pour connaître la dernière version disponible, lancez
```bash
avail_wheels busco
```

## Wheel Python
### Installation
**1.** Chargez les modules requis.
```bash
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06
```

**2.** Créez l'environnement virtuel.
```bash
virtualenv ~/busco_env
source ~/busco_env/bin/activate
```

**3.** Installez le wheel et ses dépendances.
```bash
(busco_env) $ pip install --no-index busco==6.0.0
```

**4.** Validez l'installation.
```bash
(busco_env) $ busco --help
```

**5.** Gelez l’environnement et le fichier *requirements.txt* pour utiliser ce fichier, voir le script bash montré au point 8.

```bash
(busco_env) $ pip freeze > ~/busco-requirements.txt
```

### Utilisation
#### Ensembles de données
**6.** Avant de soumettre une tâche, les ensembles de données doivent être téléchargés depuis [BUSCO data](https://busco-data.ezlab.org/v5/data/).

Pour connaître les ensembles de données disponibles, entrez `busco --list-datasets` dans votre terminal.

Vous pouvez utiliser l'une des deux commandes suivantes :
*   `busco`
*   `wget`

#### 6.1 Téléchargement avec la commande `busco`
Cette option est recommandée. Entrez la commande suivante dans votre répertoire de travail pour télécharger l’ensemble de données, par exemple
```bash
busco --download bacteria_odb10
```

Il est aussi possible de télécharger plusieurs ensembles de données en une opération en ajoutant les arguments `all`, `prokaryota`, `eukaryota` ou `virus`, par exemple

```bash
busco --download virus
```
Ceci permet de
1.  créer une hiérarchie pour les ensembles de données,
2.  télécharger les ensembles de données appropriés,
3.  décompresser le ou les fichiers,
4.  si plusieurs fichiers sont téléchargés, ils seront automatiquement ajoutés au répertoire des lignées.

La hiérarchie sera semblable à

> * busco_downloads/
>
>   * information/
>
>     * lineages_list.2021-12-14.txt
>
>   * lineages/
>
>     * bacteria_odb10
>
>     * actinobacteria_class_odb10
>
>     * actinobacteria_phylum_odb10
>
>   * placement_files/
>
>     * list_of_reference_markers.archaea_odb10.2019-12-16.txt

Tous les fichiers de lignées se trouveront alors dans **busco_downloads/lineages/**. La présence de `--download_path busco_downloads/` dans la ligne de commande BUSCO indiquera où trouver l’argument `--lineage_dataset bacteria_odb10` pour l'ensemble de données. Si *busco_download* n’est pas votre répertoire de travail, il faudra fournir le chemin complet.

#### 6.2 Téléchargement avec la commande `wget`

Tous les fichiers doivent être décompressés avec `tar -xvf file.tar.gz`.
```bash
mkdir -p busco_downloads/lineages
cd busco_downloads/lineages
wget https://busco-data.ezlab.org/v5/data/lineages/bacteria_odb10.2020-03-06.tar.gz
tar -xvf bacteria_odb10.2020-03-06.tar.gz
```

#### Test
**7.** Téléchargement des fichiers de génome.

```bash
wget https://gitlab.com/ezlab/busco/-/raw/master/test_data/bacteria/genome.fna
```

**8.** Exécution.

Pour un seul génome :

```bash
busco --offline --in genome.fna --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/
```

Pour plusieurs génomes, le répertoire genome/ doit se trouver dans le répertoire courant, autrement il faut donner le chemin complet :

```bash
busco --offline --in genome/ --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/
```

La commande pour un seul génome devrait être exécutée en moins de 60 secondes. Les tâches de production qui nécessitent plus de temps doivent être [soumises à l'ordonnanceur](running-jobs.md).

#### Conseils pour BUSCO

Utilisez `--in genome.fna` pour analyser un seul fichier.

Utilisez `--in genome/` pour analyser plusieurs fichiers.

#### Conseils pour Slurm
Utilisez `--offline` pour éviter l'utilisation de l’internet.

Utilisez `--cpu` avec `$SLURM_CPUS_PER_TASK` dans le script de la tâche pour utiliser le nombre alloué de CPU.

Utilisez `--restart` pour reprendre une tâche interrompue.

#### Soumettre une tâche

Vous pouvez soumettre le script suivant avec `sbatch run_busco.sh`.

```bash linenums="1"
#!/bin/bash

#SBATCH --job-name=busco9_run
#SBATCH --account=def-someprof    # adjust this to match the accounting group you are using to submit jobs
#SBATCH --time=01:00:00           # adjust this to match the walltime of your job
#SBATCH --cpus-per-task=8         # adjust depending on the size of the genome(s)/protein(s)/transcriptome(s)
#SBATCH --mem=20G                 # adjust this according to the memory you need

# Load modules dependencies.
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06

# Generate your virtual environment in $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Install busco and its dependencies.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/busco-requirements.txt

# Edit with the proper arguments, run your commands.
busco --offline --in genome.fna --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/
```

#### Paramètres Augustus
**9.** Si vous avez plus d'expérience, vous pouvez utiliser les paramètres Augustus : `--augustus_parameters="--yourAugustusParameter"`.

*   Copiez le répertoire *config* d'Augustus à un endroit où la lecture est possible.
```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

*   Assurez-vous de définir la variable d'environnement `AUGUSTUS_CONFIG_PATH`.
```bash
export AUGUSTUS_CONFIG_PATH=$HOME/augustus_config
```

#### Paramètres SEPP
**10.** Pour utiliser ces paramètres, SEPP doit être installé localement dans votre environnement virtuel, ce que vous devez faire à partir du nœud de connexion.

**10.1.** Activez votre environnement virtuel BUSCO.
```bash
source busco_env/bin/activate
```

**10.2.** Installez DendroPy.
```bash
pip install 'dendropy<4.6'
```

**10.3.** Installez SEPP.
```bash
git clone https://github.com/smirarab/sepp.git
cd sepp
python setup.py config
python setup.py install
```

**10.4.** Validez l'installation.
```bash
cd
run_sepp.py -h
```

**10.5.** Puisque SEPP est installé localement, vous ne pouvez pas utiliser le script ci-dessus pour créer votre environnement virtuel. Pour activer votre environnement virtuel, ajoutez la commande suivante sur la ligne qui suit la commande de chargement du module.
```bash
source ~/busco_env/bin/activate
```

## Modules

!!! warning "Cette section est obsolète."
    Veuillez utiliser les wheels qui sont disponibles.

**1.** Chargez les modules nécessaires.
```bash
module load StdEnv/2018.3 gcc/7.3.0 openmpi/3.1.4 busco/3.0.2 r/4.0.2
```
Ceci charge aussi les modules pour Augustus, BLAST+, HMMER et d'autres paquets requis par BUSCO.

**2.** Copiez le fichier de configuration
```bash
cp -v $EBROOTBUSCO/config/config.ini.default $HOME/busco_config.ini
```
ou
```bash
wget -O $HOME/busco_config.ini https://gitlab.com/ezlab/busco/raw/master/config/config.ini.default
```

**3.** Modifiez le fichier de configuration. Les endroits où se trouvent les outils externes sont définis dans la dernière section.
```ini
[tblastn]
# path to tblastn
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/blast+/2.7.1/bin/

[makeblastdb]
# path to makeblastdb
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/blast+/2.7.1/bin/

[augustus]
# path to augustus
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/bin/

[etraining]
# path to augustus etraining
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/bin/

# path to augustus perl scripts, redeclare it for each new script
[gff2gbSmallDNA.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/
[new_species.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/
[optimize_augustus.pl]
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/augustus/3.3/scripts/

[hmmsearch]
# path to HMMsearch executable
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/hmmer/3.1b2/bin/

[Rscript]
# path to Rscript, if you wish to use the plot tool
path = /cvmfs/soft.computecanada.ca/easybuild/software/2017/avx512/Compiler/gcc7.3/r/4.0.2/bin/
```

**4.** Copiez le répertoire `config` d’Augustus à un endroit où la lecture est possible.
```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

**5.** Vérifiez si tout fonctionne bien.

```bash
export BUSCO_CONFIG_FILE=$HOME/busco_config.ini
export AUGUSTUS_CONFIG_PATH=$HOME/augustus_config
run_BUSCO.py --in $EBROOTBUSCO/sample_data/target.fa --out TEST --lineage_path $EBROOTBUSCO/sample_data/example --mode genome
```

La commande `run_BUSCO.py` devrait être exécutée en moins de 60 secondes. Les tâches de production qui nécessitent plus de temps doivent être [soumises à l'ordonnanceur](running-jobs.md).

## Dépannage
### Erreur : *Cannot write to Augustus config path*
Assurez-vous d’avoir copié le répertoire *config* d’Augustus à un endroit où la lecture est possible et d’avoir exporté la variable `AUGUSTUS_CONFIG_PATH`.