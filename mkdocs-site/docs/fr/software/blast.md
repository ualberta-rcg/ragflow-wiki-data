---
title: "BLAST/fr"
slug: "blast"
lang: "fr"

source_wiki_title: "BLAST/fr"
source_hash: "eb29decbf13044525113969823adf2d5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:42:31.235991+00:00"

tags:
  - software

keywords:
  - "Slurm"
  - "cpus-per-task"
  - "module load"
  - "base de données FASTA"
  - "SBATCH"
  - "mem-per-cpu"
  - "requête BLAST"
  - "task array"
  - "BLAST"
  - "bases de données"
  - "vecteur de tâches"
  - "alignement de séquences"
  - "paralléliser"
  - "GNU Parallel"
  - "makeblastdb"

questions:
  - "À quoi sert l'outil BLAST et quels types de séquences permet-il d'aligner ?"
  - "Comment doit-on préparer une base de données de référence avec la commande makeblastdb avant d'exécuter une recherche ?"
  - "Quelle méthode est recommandée pour accélérer la recherche BLAST en utilisant la division de fichiers et les vecteurs de tâches ?"
  - "Comment soumettre une tâche BLAST avec SLURM pour qu'elle s'exécute automatiquement après la création de la base de données ?"
  - "Quel est l'avantage d'utiliser GNU Parallel pour traiter des requêtes BLAST et comment gère-t-il la taille des blocs de données ?"
  - "Quelles sont les astuces supplémentaires recommandées pour optimiser l'exécution de BLAST, notamment concernant le stockage local et le filtrage des résultats ?"
  - "What are the specific hardware and time resource limits allocated for each task in this script?"
  - "How many total tasks are configured to run in this job array, and what is their index range?"
  - "Which specific software modules and versions are loaded to set up the environment for this job?"
  - "Comment soumettre une tâche BLAST avec SLURM pour qu'elle s'exécute automatiquement après la création de la base de données ?"
  - "Quel est l'avantage d'utiliser GNU Parallel pour traiter des requêtes BLAST et comment gère-t-il la taille des blocs de données ?"
  - "Quelles sont les astuces supplémentaires recommandées pour optimiser l'exécution de BLAST, notamment concernant le stockage local et le filtrage des résultats ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

BLAST (pour *Basic Local Alignment Search Tool*) permet de trouver les régions similaires entre deux ou plusieurs séquences de nucléotides ou d'acides aminés, et de réaliser un alignement de ces régions homologues.

## Manuel de l'utilisateur
Vous trouverez plus d'information sur les arguments dans le [manuel de l'utilisateur](https://www.ncbi.nlm.nih.gov/books/NBK279684/) ou en lançant la commande :

```bash
blastn -help
```

## Bases de données
Certaines bases de données de séquences fréquemment utilisées se trouvent sur nos grappes dans `/cvmfs/bio.data.computecanada.ca/content/databases/Core/blast_dbs/2022_03_23/`.

Les plus récentes versions des bases de données se trouvent :

*   pour `nr` (*protéines non redondantes du NCBI*), dans `/cvmfs/bio.data.computecanada.ca/content/databases/Core/blast_dbs/2025_06_21/nr/nr`
*   pour `nt` (*nucléotides non redondants*), dans `/cvmfs/bio.data.computecanada.ca/content/databases/Core/blast_dbs/2025_06_21/nt/nt`

## Accélérer la recherche
Dans les exemples qui suivent, le fichier `ref.fa` est utilisé comme base de référence au format FASTA et le fichier `seq.fa` pour les requêtes à faire.

### `makeblastdb`
Avant d'exécuter une recherche, il faut préparer la base de données. Ceci peut se faire par une tâche de prétraitement, avec les autres tâches dépendantes du résultat de la tâche `makeblastdb`.
Voici un exemple d'un script de soumission :

```bash title="makeblastdb.sh"
#!/bin/bash

#SBATCH --account=def-<utilisateur>  # Le compte à utiliser
#SBATCH --time=00:02:00       # La durée au format HH:MM:SS
#SBATCH --cpus-per-task=1     # Le nombre de cœurs
#SBATCH --mem=512M            # Mémoire totale pour cette tâche

module load gcc/7.3.0 blast+/2.9.0

# Création de la base de données de nucléotides à partir de `ref.fa`.
makeblastdb -in ref.fa -title reference -dbtype nucl -out ref.fa
```

### Vecteur de tâches
Le parallélisme des données peut grandement améliorer la recherche; il s'agit de diviser le fichier de requêtes en plusieurs requêtes à la base de données.

#### Prétraitement
Pour accélérer la recherche, le fichier `seq.fa` doit être divisé en plusieurs petites parts. Ces parts devraient être d'au moins `1Mo`; des parts plus petites pourraient nuire au système de fichiers parallèle.

Avec l'utilitaire `faSplit`,
```bash
module load kentutils/20180716
```
```bash
faSplit sequence seqs.fa 10 seq
```
créent 10 fichiers nommés `seqN.fa` où `N` représente `[0..9]` pour 10 requêtes (séquences).

#### Soumettre une tâche
Une fois que les requêtes sont séparées, vous pouvez créer une tâche pour chaque fichier `seq.fa.N` avec un vecteur de tâches. L'identifiant de la tâche contenu dans le vecteur correspondra au nom du fichier où se trouvent les requêtes à exécuter.

Avec cette solution, l'ordonnanceur peut utiliser les ressources de la grappe qui sont disponibles pour exécuter les plus petites tâches.

```bash title="blastn_array.sh"
#!/bin/bash

#SBATCH --account=def-<utilisateur>  # Le compte à utiliser
#SBATCH --time=00:02:00       # La durée au format HH:MM:SS pour chaque tâche du vecteur
#SBATCH --cpus-per-task=1     # Le nombre de cœurs pour chaque tâche du vecteur
#SBATCH --mem-per-cpu=512M    # La mémoire par cœur pour chaque tâche du vecteur
#SBATCH --array=0-9           # Le nombre de tâches : 10

module load gcc/7.3.0 blast+/2.9.0

# En utilisant l'index de la tâche actuelle, fourni par `$SLURM_ARRAY_TASK_ID`, exécuter la requête correspondante et écrire le résultat.
blastn -db ref.fa -query seq.fa.${SLURM_ARRAY_TASK_ID} > seq.ref.${SLURM_ARRAY_TASK_ID}
```

Avec le script ci-dessus, vous pouvez soumettre votre requête BLAST et elle sera exécutée après que la base de données aura été créée.
```bash
sbatch --dependency=afterok:$(sbatch makeblastdb.sh) blastn_array.sh
```

Quand toutes les tâches du vecteur sont terminées, concaténez les résultats avec :
```bash
cat seq.ref.{0..9} > seq.ref
```
où les 10 fichiers sont concaténés dans `seq.ref`.
Ceci peut s'effectuer à partir du nœud de connexion ou comme tâche indépendante une fois que toutes les tâches du vecteur sont terminées.

### GNU Parallel
`GNU Parallel` est un bon outil pour grouper plusieurs petites tâches en une et la paralléliser. Cette solution réduit les problèmes qui se produisent avec plusieurs petits fichiers dans un système de fichiers parallèle avec des requêtes sur des blocs de taille fixe dans `seq.fa` avec un cœur et plusieurs nœuds.

Par exemple, pour le fichier `seq.fa` de `100Mo`, vous pourriez lire des blocs de `10Mo` et GNU Parallel créerait 3 tâches, utilisant ainsi 3 cœurs; en demandant 10 cœurs, ce sont 7 cœurs qui auraient été gaspillés.

!!! warning "La taille des blocs est donc importante."
    On peut aussi laisser GNU Parallel décider, comme dans l'exemple ci-dessous.

Voir aussi [Travailler avec des fichiers volumineux](gnu-parallel.md#travailler-avec-des-fichiers-volumineux) dans la page sur GNU Parallel.

#### Utiliser plusieurs cœurs dans un nœud
```bash title="blastn_gnu.sh"
#!/bin/bash

#SBATCH --account=def-<utilisateur>  # Le compte à utiliser
#SBATCH --time=00:02:00       # La durée au format HH:MM:SS
#SBATCH --cpus-per-task=4     # Le nombre de cœurs
#SBATCH --mem-per-cpu=512M    # La mémoire par cœur

module load gcc/7.3.0 blast+/2.9.0

cmd='blastn -db ref.fa -query - '

# En utilisant la notation `::::`, fournir le fichier de séquences à GNU Parallel.
# où :
#   --jobs nombre de cœurs à utiliser, égal à $SLURM_CPUS_PER_TASK (le nombre de cœurs demandé)
#   --keep-order conserver le même ordre que celui donné en entrée
#   --block -1 laisser GNU Parallel évaluer la taille du bloc et s'adapter
#   --recstart début de l'enregistrement, ici l'identifiant de la séquence `>`
#   --pipepart assembler les parties de $cmd.
#              `--pipepart` est plus rapide que `--pipe` (qui est limité à 500Mo/s) car `--pipepart` peut facilement atteindre 5Go/s selon Ole Tange.
# et rediriger les résultats vers `seq.ref`.
parallel --jobs $SLURM_CPUS_PER_TASK --keep-order --block -1 --recstart '>' --pipepart $cmd :::: seq.fa > seq.ref
```

!!! note "Attention : Le fichier ne doit pas être compressé."

##### Soumettre une tâche
Avec le script ci-dessus, vous pouvez soumettre votre requête BLAST et elle sera exécutée après que la base de données aura été créée.
```bash
sbatch --dependency=afterok:$(sbatch makeblastdb.sh) blastn_gnu.sh
```

### Conseils supplémentaires
*   Si le stockage local du nœud le permet, copiez votre base de données FASTA dans l'espace local /scratch (`$SLURM_TMPDIR`).
*   Si votre recherche s'y prête, réduisez le nombre de réponses (`-max_target_seqs, -max_hsps`).
*   Si votre recherche s'y prête, limitez la liste des réponses avec des filtres `-evalue` pour ne conserver que les réponses quasi identiques.