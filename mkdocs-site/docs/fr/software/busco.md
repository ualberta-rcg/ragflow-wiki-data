---
title: "BUSCO/fr"
tags:
  - software

keywords:
  []
---

BUSCO (pour <i>Benchmarking Universal Single-Copy Orthologs</i>) est une application qui permet d'évaluer la complétude de l'assemblage et de l'annotation de génomes.

Pour plus d'information, consultez [le manuel de l'utilisateur](https://busco.ezlab.org/busco_userguide.html).

## Versions disponibles 
Les versions récentes sont disponibles dans des <i>wheels</i> et les plus anciennes versions sont dans un module (voir la section [Modules](busco-fr#modules.md) ci-dessous).

Pour connaître la dernière version disponible, lancez

```bash
avail_wheels busco
```

## Wheel Python 
### Installation 
<b>1.</b> Chargez les modules requis.

```bash
module load StdEnv/2023 gcc python/3.11 augustus/3.5.0 hmmer/3.4 blast+/2.15 metaeuk/7 prodigal/2.6.3 r bbmap/39.06
```

<b>2.</b> Créez l'environnement virtuel.

```bash
source ~/busco_env/bin/activate
```

<b>3.</b> Installez le wheel et ses dépendances.

```bash

```
6.0.0
}}

<b>4.</b> Validez l'installation.

```bash
busco --help
```

<b>5.</b>  Gelez l’environnement et le fichier <i>requirements.txt</i> pour utiliser ce fichier, voir le script bash montré au point 8.

```bash
pip freeze > ~/busco-requirements.txt
```

### Utilisation 
#### Ensembles de données 
<b>6.</b> Avant de soumettre une tâche, les ensembles de données doivent être téléchargés de 
[BUSCO data](https://busco-data.ezlab.org/v5/data/).

Pour connaître les ensembles de données disponibles, entrez `busco --list-datasets` dans votre terminal.

Vous pouvez utiliser l'une des deux commandes suivantes :
*`busco`
*`wget`

===== <b>6.1</b>  Téléchargement avec la commande `busco` =====
Cette option est recommandée. Entrez la commande suivante dans votre répertoire de travail pour télécharger l’ensemble de données, par exemple

```bash
busco --download bacteria_odb10
```

Il est aussi possible de télécharger plusieurs ensembles de données en une opération en ajoutant les arguments `all`, `prokaryota`, `eukaryota` ou `virus`, par exemple

```bash
busco --download virus
```

Ceci permet de
::1. créer une hiérarchie pour les ensembles de données,
::2. télécharger les ensembles de données appropriés,
::3. décompresser le ou les fichiers,
::4. si plusieurs fichiers sont téléchargés, ils seront automatiquement ajoutés au répertoire des lignées. 

La hiérarchie sera semblable à
<blockquote>
* busco_downloads/

::* information/

::::lineages_list.2021-12-14.txt

::* lineages/

::::bacteria_odb10

::::actinobacteria_class_odb10

::::actinobacteria_phylum_odb10

::* placement_files/

::::list_of_reference_markers.archaea_odb10.2019-12-16.txt
</blockquote>

Tous les fichiers de lignées se trouveront alors dans <b>busco_downloads/lineages/</b>. La présence de `--download_path busco_downloads/` dans la ligne de commande BUSCO indiquera où trouver l’argument `--lineage_dataset bacteria_odb10` pour l'ensemble de données. Si <i>busco_download</i> n’est pas votre répertoire de travail, il faudra fournir le chemin complet.

<span id="6.2_Using_the_wget_command"></span>
=====<b>6.2</b> Téléchargement avec la commande `wget`  =====

Tous les fichiers doivent être décompressés avec `tar -xvf file.tar.gz`.

```bash
tar -xvf bacteria_odb10.2020-03-06.tar.gz
```

#### Test 
<b>7.</b> Téléchargement des fichiers de génome.

```bash
wget https://gitlab.com/ezlab/busco/-/raw/master/test_data/bacteria/genome.fna
```

<b>8.</b> Exécution.

Pour un seul génome :

{{Command|busco --offline --in genome.fna --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/}}

Pour plusieurs génomes, le répertoire genome/ doit se trouver dans le répertoire courant, autrement il faut donner le chemin complet&nbsp;:

{{Command|busco --offline --in genome/ --out TEST --lineage_dataset bacteria_odb10 --mode genome --cpu ${SLURM_CPUS_PER_TASK:-1} --download_path busco_download/}}

La commande pour un seul génome devrait être exécutée sous les 60 secondes. Les tâches de production qui nécessitent plus de temps doivent être [soumises à l'ordonnanceur](running-jobs-fr.md).

<span id="BUSCO_tips"></span>
===== Conseils pour BUSCO =====

Utilisez `--in genome.fna` pour analyser un seul fichier. 

Utilisez `--in genome/` pour analyser plusieurs fichiers.

===== Conseils pour Slurm  =====
Utilisez `--offline` pour éviter l'utilisation de l’internet.

Utilisez `--cpu` avec `$SLURM_CPUS_PER_TASK` dans le script de la tâche pour utiliser le nombre alloué de CPU.

Utilisez `--restart` pour reprendre une tâche interrompue.

<span id="Job_submission"></span>
#### Soumettre une tâche

Vous pouvez soumettre le script suivant avec `sbatch run_busco.sh`.

{{File
  |name=run_busco.sh
  |lang="bash"
  |contents=

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

}}

#### Paramètres Augustus 
<b>9.</b> Si vous avez plus d'expérience, vous pouvez utiliser les paramètres Argutus :  `--augustus_parameters="--yourAugustusParameter"`.

*Copiez le répertoire <i>config</i> d'Augustus à un endroit où la lecture est possible.

```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

*Assurez-vous de définir la variable d'environnement  `AUGUSTUS_CONFIG_PATH`.

```bash

```
$HOME/augustus_config}}

#### Paramètres SEPP 
<b>10.</b> Pour utiliser ces paramètres, SEPP doit être installé localement dans votre environnement virtuel, ce que vous devez faire à partir du nœud de connexion.

<b>10.1.</b> Activez votre environnement virtuel BUSCO.

```bash
source busco_env/bin/activate
```

<b>10.2.</b> Installez DendroPy.

```bash
pip install 'dendropy<4.6'
```

<b>10.3.</b> Installez SEPP.

```bash
python setup.py install
```

<b>10.4.</b> Validez l'installation.

```bash
run_sepp.py -h
```

<b>10.5.</b> Puisque SEPP est installé localement, vous ne pouvez pas utiliser le script ci-dessus pour créer votre environnement virtuel. Pour activer votre environnement virtuel, ajoutez la commande suivante sur la ligne qui suit la commande de chargement du module.

```bash
source ~/busco_env/bin/activate
```

== Modules == 

<b>1.</b> Chargez les modules nécessaires.

```bash
module load StdEnv/2018.3 gcc/7.3.0 openmpi/3.1.4 busco/3.0.2 r/4.0.2
```

Ceci charge aussi les modules pour Augustus, BLAST+, HMMER et d'autres paquets requis par BUSCO.

<b>2.</b> Copiez le fichier de configuration

```bash
cp -v $EBROOTBUSCO/config/config.ini.default $HOME/busco_config.ini
```

ou

```bash
wget -O $HOME/busco_config.ini https://gitlab.com/ezlab/busco/raw/master/config/config.ini.default
```

<b>3.</b> Modifiez le fichier de configuration. Les endroits où se trouvent les outils externes sont définis dans la dernière section.

**`partial_busco_config.ini`**
```text
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

<b>4.</b>  Copiez le répertoire `config` d’Augustus à un endroit où la lecture est possible. 

```bash
cp -r $EBROOTAUGUSTUS/config $HOME/augustus_config
```

<b>5.</b> Vérifiez si tout fonctionne bien.

```bash

```
$HOME/busco_config.ini
|export AUGUSTUS_CONFIG_PATH$HOME/augustus_config
|run_BUSCO.py --in $EBROOTBUSCO/sample_data/target.fa --out TEST --lineage_path $EBROOTBUSCO/sample_data/example --mode genome
}}

La commande `run_BUSCO.py` devrait être exécutée sous les 60 secondes. Les tâches de production qui nécessitent plus de temps doivent être [soumises à l'ordonnanceur](running-jobs-fr.md).

= Dépannage =
## Erreur : <i>Cannot write to Augustus config path</i> 
Assurez-vous d’avoir copié le répertoire <i>config</i> d’Augustus à un endroit où la lecture est possible et d’avoir exporté la variable `AUGUSTUS_CONFIG_PATH`.