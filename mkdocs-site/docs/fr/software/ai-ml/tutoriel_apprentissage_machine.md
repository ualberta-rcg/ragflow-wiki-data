---
title: "Tutoriel Apprentissage machine/fr"
slug: "tutoriel_apprentissage_machine"
lang: "fr"

source_wiki_title: "Tutoriel Apprentissage machine/fr"
source_hash: "0570cf6ed360f25828e7e6faefee06da"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:13:55.168288+00:00"

tags:
  []

keywords:
  - "soumettre vos tâches"
  - "apprentissage automatique"
  - "tâches interactives"
  - "automatisées"
  - "tâche scriptée"
  - "Morcellement de tâche"
  - "déboguer"
  - "Script de soumission"
  - "tâche interactive"
  - "environnement virtuel"
  - "Ressources demandées"
  - "scripts sbatch"
  - "Checkpoint"
  - "ensemble de données"
  - "Commandes bash"

questions:
  - "Pourquoi est-il fortement recommandé d'archiver son ensemble de données (par exemple au format \"tar\") avant de l'utiliser sur les grappes de calcul ?"
  - "Quel est le rôle principal d'une tâche interactive (salloc) dans le processus de préparation et de débogage d'un modèle d'apprentissage automatique ?"
  - "Comment doit-on adapter le code de son programme concernant les résultats visuels, étant donné que l'affichage graphique n'est pas pris en charge ?"
  - "Quelles sont les recommandations générales concernant l'allocation des ressources (CPU, GPU, mémoire et temps) pour soumettre une tâche sur la grappe de calcul ?"
  - "Quelles sont les étapes essentielles à inclure dans les commandes bash du script de soumission pour préparer l'environnement, transférer les données et lancer l'exécutable ?"
  - "Comment doit-on procéder pour morceler une tâche de longue durée à l'aide de points de contrôle (checkpoints) afin d'améliorer sa priorité et respecter les limites de temps ?"
  - "Pourquoi est-il nécessaire de soumettre les tâches à l'aide de scripts sbatch ?"
  - "Quel est le rôle spécifique des tâches interactives par rapport aux tâches automatisées ?"
  - "Quels sont les éléments importants qui doivent figurer dans un script sbatch ?"
  - "Quelles sont les recommandations générales concernant l'allocation des ressources (CPU, GPU, mémoire et temps) pour soumettre une tâche sur la grappe de calcul ?"
  - "Quelles sont les étapes essentielles à inclure dans les commandes bash du script de soumission pour préparer l'environnement, transférer les données et lancer l'exécutable ?"
  - "Comment doit-on procéder pour morceler une tâche de longue durée à l'aide de points de contrôle (checkpoints) afin d'améliorer sa priorité et respecter les limites de temps ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Cette page constitue un guide de démarrage pour porter une tâche d'apprentissage automatique (Machine Learning) sur une de nos grappes.

## Étape 1 : Enlever tout affichage graphique

Modifiez votre programme afin qu'il n'utilise pas d'affichage graphique. Tout résultat graphique devra être écrit sur le disque dans un fichier et visualisé sur votre ordinateur personnel, une fois la tâche terminée. Par exemple, si vous affichez des graphiques avec Matplotlib, vous devez [enregistrer les graphiques sous forme de fichiers, au lieu de les afficher à l'écran](https://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab).

## Étape 2 : Archivage d'un ensemble de données

Les stockages partagés sur nos grappes ne sont pas optimisés pour gérer un grand nombre de petits fichiers (ils sont plutôt optimisés pour les très gros fichiers). Assurez-vous que l'ensemble de données dont vous aurez besoin pour votre entraînement se trouve dans un fichier archive (tel que "tar"), que vous transférerez sur votre nœud de calcul au début de votre tâche.

!!! attention "Important : Gestion des petits fichiers"
    Si vous ne le faites pas, vous risquez de causer des lectures de fichiers à haute fréquence du nœud de stockage vers votre nœud de calcul, nuisant ainsi à la performance globale du système.

Si vous voulez apprendre davantage sur la gestion des grands ensembles de fichiers, on vous recommande la lecture de [cette page](https://docs.alliancecan.ca/wiki/Handling_large_collections_of_files/fr).

En supposant que les fichiers dont vous avez besoin sont dans le dossier `mydataset` :

```bash
$ tar cf mydataset.tar mydataset/*
```

La commande ci-haut ne compresse pas les données. Si vous croyez que ce serait approprié, vous pouvez utiliser `tar czf`.

## Étape 3 : Préparation de l'environnement virtuel

[Créez un environnement virtuel](../python.md) dans votre espace personnel.

Pour les détails d'installation et d'utilisation des différents frameworks d'apprentissage automatique, référez-vous à notre documentation :

*   [PyTorch](../pytorch.md)
*   [TensorFlow](../tensorflow.md)

## Étape 4 : Tâche interactive (salloc)

Nous vous recommandons d'essayer votre tâche dans une [tâche interactive](../../running-jobs/running_jobs.md) avant de la soumettre avec un script (voir la section suivante). Vous pourrez ainsi diagnostiquer plus rapidement les problèmes. Voici un exemple de la commande pour soumettre une tâche interactive :

```bash
$ salloc --account=def-someuser --gres=gpu:1 --cpus-per-task=3 --mem=32000M --time=1:00:00
```

Une fois la tâche lancée :

*   Activez votre environnement virtuel Python.
*   Tentez d'exécuter votre programme.
*   Installez les paquets manquants, si nécessaire. Les nœuds de calcul n'ayant pas d'accès à Internet, vous devrez faire l'installation à partir d'un nœud de connexion. Référez-vous à notre [documentation sur les environnements virtuels Python](../python.md) pour plus de détails.
*   Notez les étapes qui ont été nécessaires pour faire fonctionner votre programme.

!!! info "Recommandation importante : Stockage local"
    Maintenant est un bon moment pour vérifier que votre tâche lit et écrit le plus possible dans le stockage local au nœud de calcul (`$SLURM_TMPDIR`), et le moins possible sur les [systèmes de fichiers partagés (personnel, *scratch*, projet)](../../storage-and-data/storage_and_file_management.md).

## Étape 5 : Tâche scriptée (sbatch)

Vous devez [soumettre vos tâches](../../running-jobs/running_jobs.md) à l'aide de scripts `sbatch`, afin qu'elles puissent être entièrement automatisées. Les tâches interactives servent uniquement à préparer et à déboguer des tâches qui seront ensuite exécutées entièrement et/ou à grande échelle en utilisant `sbatch`.

### Éléments importants d'un script `sbatch`

1.  Compte sur lequel les ressources seront facturées.
2.  Ressources demandées :
    *   Nombre de *CPU* : 6 (suggestion)
    *   Nombre de *GPU* : 1 (suggestion)
        !!! warning "Important : Utilisation des GPU"
            Utilisez un (1) seul *GPU*, à moins d'être certain que votre programme en utilise plusieurs. Par défaut, TensorFlow et PyTorch utilisent un seul *GPU*.
    *   Quantité de mémoire : `32000M` (suggestion)
    *   Durée (Maximum Béluga : 7 jours, Graham et Cedar : 28 jours).
3.  Commandes *Bash* :
    *   Préparation de l'environnement (modules, environnement virtuel).
    *   Transfert des données vers le nœud de calcul.
    *   Lancement de l'exécutable.

### Exemple de script

```bash title="ml-test.sh"
#!/bin/bash
#SBATCH --gres=gpu:1       # Request GPU "generic resources"
#SBATCH --cpus-per-task=3  # Refer to cluster's documentation for the right CPU/GPU ratio
#SBATCH --mem=32000M       # Memory proportional to GPUs: 32000 Cedar, 47000 Béluga, 64000 Graham.
#SBATCH --time=0-03:00     # DD-HH:MM:SS

module load python/3.6 cuda cudnn

SOURCEDIR=~/ml-test

# Prepare virtualenv
source ~/my_env/bin/activate
# You could also create your environment here, on the local storage ($SLURM_TMPDIR), for better performance. See our docs on virtual environments.

# Prepare data
mkdir $SLURM_TMPDIR/data
tar xf ~/projects/def-xxxx/data.tar -C $SLURM_TMPDIR/data

# Start training
python $SOURCEDIR/train.py $SLURM_TMPDIR/data
```

### Morcellement d'une longue tâche

Nous vous recommandons de morceler vos tâches en blocs de 24 heures. Demander des tâches plus courtes améliore votre priorité. En créant une chaîne de tâches, il est possible de dépasser la limite de 7 jours sur Béluga.

1.  Modifiez votre script de soumission (ou votre programme) afin que votre tâche puisse être interrompue et continuée. Votre programme doit pouvoir accéder au *point de sauvegarde* le plus récent. (Voir l'exemple de script ci-dessous.)
2.  Vérifiez combien d'epochs (ou d'itérations) peuvent être effectuées à l'intérieur de 24 heures.
3.  Calculez combien de blocs de 24 heures vous aurez besoin : `n_blocs = n_epochs_total / n_epochs_par_24h`.
4.  Utilisez l'argument `--array 1-<n_blocs>%1` pour demander une chaîne de `n_blocs` tâches.

Le script de soumission ressemblera à ceci :

```bash title="ml-test-chain.sh"
#!/bin/bash
#SBATCH --array=1-10%1   # 10 is the number of jobs in the chain
#SBATCH ...

module load python/3.6 cuda cudnn

# Prepare virtualenv
...

# Prepare data
...

# Get most recent checkpoint
CHECKPOINT_EXT='*.h5'  # Replace by *.pt for PyTorch checkpoints
CHECKPOINTS=~/scratch/checkpoints/ml-test
LAST_CHECKPOINT=$(find $CHECKPOINTS -maxdepth 1 -name "$CHECKPOINT_EXT" -print0 | xargs -r -0 ls -1 -t | head -1)

# Start training
if [ -z "$LAST_CHECKPOINT" ]; then
    # $LAST_CHECKPOINT is null; start from scratch
    python $SOURCEDIR/train.py --write-checkpoints-to $CHECKPOINTS ...
else
    python $SOURCEDIR/train.py --load-checkpoint $LAST_CHECKPOINT --write-checkpoints-to $CHECKPOINTS ...
fi