---
title: "BUSCO/fr"
slug: "busco"
lang: "fr"

source_wiki_title: "BUSCO/fr"
source_hash: "9fefb1c642155716acd1e62d6d998b07"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:54:20.430254+00:00"

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

BUSCO (pour *Benchmarking Universal Single-Copy Orthologs*) est une application qui permet d'évaluer la complétude de l'assemblage et de l'annotation de génomes.

Pour plus d'information, consultez [le manuel de l'utilisateur](https://busco.ezlab.org/busco_userguide.html).

## Versions disponibles
Les versions récentes sont disponibles dans des *wheels*, et les plus anciennes versions sont dans un module (voir la section [Modules](#modules) ci-dessous).

Pour connaître la dernière version disponible, lancez :

```bash
avail_wheels busco
```

## Wheels Python
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

**3.** Installez le *wheel* et ses dépendances.

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
**6.** Avant de soumettre une tâche, les ensembles de données doivent être téléchargés à partir de [BUSCO data](https://busco-data.ezlab.org/v5/data/).

Pour connaître les ensembles de données disponibles, entrez `busco --list-datasets` dans votre terminal.

Vous pouvez utiliser l'une des deux commandes suivantes :
*   `busco`
*   `wget`

##### **6.1** Téléchargement avec la commande `busco`
Cette option est recommandée. Entrez la commande suivante dans votre répertoire de travail pour télécharger l’ensemble de données, par exemple :

```bash
busco --download bacteria_odb10
```

Il est aussi possible de télécharger plusieurs ensembles de données en une opération en ajoutant les arguments `all`, `prokaryota`, `eukaryota` ou `virus`, par exemple :

```bash
busco --download virus
```

Ceci permet de :
1.  créer une hiérarchie pour les ensembles de données,
2.  télécharger les ensembles de données appropriés,
3.  décompresser le ou les fichiers,
4.  si plusieurs fichiers sont téléchargés, ils seront automatiquement ajoutés au répertoire des lignées.

La hiérarchie sera semblable à :

```text
busco_downloads/
├── information/
│   └── lineages_list.2021-12-14.txt
├── lineages/
│   ├── bacteria_odb10
│   ├── actinobacteria_class_odb10
│   └── actinobacteria_phylum_odb10
└── placement_files/
    └── list_of_reference_markers.archaea_odb10.2019-12-16.txt
```

Tous les fichiers de lignées se trouveront alors dans **busco_downloads/lineages/**. La présence de `--download_path busco_downloads/` dans la ligne de commande BUSCO indiquera où trouver l’argument `--lineage_dataset bacteria_odb10` pour l'ensemble de données. Si *busco_downloads* n’est pas votre répertoire de travail, il faudra fournir le chemin complet.

##### **6.2** Téléchargement avec la commande `wget` {#6.2-telechargement-avec-la-commande-wget}
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

Pour plusieurs génomes, le répertoire `genome/` doit se trouver dans le répertoire courant, autrement il faut donner le chemin complet :

```bash
busco --offline --in genome/ --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/
```

La commande pour un seul génome devrait être exécutée en moins de 60 secondes. Les tâches de production qui nécessitent plus de temps doivent être [soumises à l'ordonnanceur](running-jobs.md).

##### Conseils pour BUSCO {#busco-tips}
Utilisez `--in genome.fna` pour analyser un seul fichier.

Utilisez `--in genome/` pour analyser plusieurs fichiers.

##### Conseils pour Slurm
Utilisez `--offline` pour éviter l'utilisation de l’internet.

Utilisez `--cpu` avec `$SLURM_CPUS_PER_TASK` dans le script de la tâche pour utiliser le nombre alloué de CPU.

Utilisez `--restart` pour reprendre une tâche interrompue.

#### Soumettre une tâche {#job-submission}
Vous pouvez soumettre le script suivant avec `sbatch run_busco.sh`.

```bash title="run_busco.sh"
#!/bin/bash

#SBATCH --job-name=busco9_run
#SBATCH --account=def-someprof    # ajustez ceci pour qu'il corresponde au groupe de facturation que vous utilisez pour soumettre des tâches
#SBATCH --time=01:00:00           # ajustez ceci pour qu'il corresponde au temps d'exécution maximale de votre tâche
#SBATCH --cpus-per-task=8         # ajustez en fonction de la taille du ou des génomes/protéines/transcriptomes
#SBATCH --mem=20G                 # ajustez ceci en fonction de la mémoire dont vous avez besoin

# Chargez les dépendances des modules.
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06

# Générez votre environnement virtuel dans $SLURM_TMPDIR.
virtualenv --no-download ${SLURM_TMPDIR}/env
source ${SLURM_TMPDIR}/env/bin/activate

# Installez busco et ses dépendances.
pip install --no-index --upgrade pip
pip install --no-index --requirement ~/busco-requirements.txt

# Modifiez avec les arguments appropriés, exécutez vos commandes.
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

## Modules {#modules}

!!! warning "Cette section est obsolète."
    Veuillez utiliser les *wheels* qui sont disponibles.

**1.** Chargez les modules nécessaires.

```bash
module load StdEnv/2018.3 gcc/7.3.0 openmpi/3.1.4 busco/3.0.2 r/4.0.2
```

Ceci charge aussi les modules pour Augustus, BLAST+, HMMER et d'autres paquets requis par BUSCO.

**2.** Copiez le fichier de configuration :

```bash
cp -v $EBROOTBUSCO/config/config.ini.default $HOME/busco_config.ini
```

ou

```bash
wget -O $HOME/busco_config.ini https://gitlab.com/ezlab/busco/raw/master/config/config.ini.default
```

**3.** Modifiez le fichier de configuration. Les endroits où se trouvent les outils externes sont définis dans la dernière section.

```text title="partial_busco_config.ini"
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