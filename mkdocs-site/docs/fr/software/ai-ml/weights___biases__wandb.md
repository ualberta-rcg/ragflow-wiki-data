---
title: "Weights & Biases (wandb)/fr"
slug: "weights___biases__wandb"
lang: "fr"

source_wiki_title: "Weights & Biases (wandb)/fr"
source_hash: "ca208b0df558f35bfed050cebfa74a59"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:53:07.369735+00:00"

tags:
  - ai-and-machine-learning

keywords:
  - "Slurm"
  - "journalisation des métriques"
  - "httpproxy"
  - "nœuds de calcul"
  - "Weights & Biases"
  - "grappes"
  - "mode hors ligne"
  - "synchronisation"
  - "apprentissage machine"
  - "Comet.ml"
  - "suivi d'expériences"
  - "wandb"

questions:
  - "Qu'est-ce que la plateforme Weights & Biases (wandb) et quelles sont ses principales fonctionnalités pour l'apprentissage machine ?"
  - "Quelles sont les restrictions d'accès et de disponibilité de wandb sur les différentes grappes de calcul de l'Alliance ?"
  - "Quelle méthode permet d'utiliser wandb sur les grappes bloquant l'accès à Google Cloud Storage (comme Narval, Rorqual et TamIA) sans provoquer de plantage ?"
  - "Quelles sont les ressources matérielles (CPU, mémoire) recommandées dans le script Slurm pour exécuter un processus Weights & Biases ?"
  - "Comment le script Python configure-t-il l'initialisation du projet et la journalisation des métriques avec la bibliothèque wandb ?"
  - "Quelle commande doit-on utiliser pour synchroniser et envoyer les données au serveur une fois l'entraînement terminé en mode hors ligne ?"
  - "Sur quelles grappes de calcul le produit Comet.ml peut-il être utilisé ?"
  - "Quel outil l'exemple présenté utilise-t-il pour le suivi d'expériences en mode hors ligne ?"
  - "Quel module doit être chargé sur les grappes pour permettre l'exécution de wandb en mode en ligne ?"
  - "Quelles sont les ressources matérielles (CPU, mémoire) recommandées dans le script Slurm pour exécuter un processus Weights & Biases ?"
  - "Comment le script Python configure-t-il l'initialisation du projet et la journalisation des métriques avec la bibliothèque wandb ?"
  - "Quelle commande doit-on utiliser pour synchroniser et envoyer les données au serveur une fois l'entraînement terminé en mode hors ligne ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Weights & Biases (wandb)](https://wandb.ai) est une *plateforme de méta-apprentissage machine* qui permet de construire des modèles pour des applications concrètes. La plateforme permet de suivre, comparer, décrire et reproduire les expériences d'apprentissage machine.

## Utilisation sur nos grappes

### Disponibilité sur les nœuds de calcul

L'utilisation de toutes les fonctionnalités de `wandb` sur les nœuds de calcul nécessite un accès Internet ainsi qu'un accès à Google Cloud Storage, qui peuvent tous deux ne pas être disponibles selon la grappe :

| Grappe | Wandb disponible | Commentaire |
| :----- | :--------------- | :---------- |
| Narval | limité ❌        | **réservées aux membres de Mila et autres groupes admissibles** via `httpproxy` |
| Rorqual | limité ❌        | **réservées aux membres de Mila et autres groupes admissibles** via `httpproxy` |
| TamIA | limité ❌        | **réservées aux membres de Mila et autres groupes admissibles** via `httpproxy` |
| Fir | oui ✅           | `httpproxy` non requis |
| Nibi | oui ✅          | `httpproxy` non requis |
| Trillium | non ❌           | accès internet désactivé pour les nœuds de calcul |
| Vulcan | oui ✅           | `httpproxy` non requis |
| Killarney | oui ✅           | `httpproxy` non requis |

## Membres de Mila et autres groupes admissibles

Les membres de l'Institut québécois d’intelligence artificielle Mila peuvent utiliser `wandb` sur n'importe laquelle de nos grappes offrant un accès Internet, à condition d'utiliser un compte **Mila-org** valide pour se connecter à la plateforme. Veuillez consulter le tableau ci-dessus pour plus d'informations sur les modules requis pour utiliser `wandb` sur chaque grappe.

D'autres groupes ont pris des dispositions avec Weights & Biases pour contourner les appels à l'API Google Cloud Storage. Contactez votre chercheuse principale ou votre chercheur principal pour savoir si c'est le cas pour votre groupe.

## Narval, Rorqual et TamIA

Bien qu'il soit possible de télécharger des métriques de base vers Weights&Biases lors d'une tâche sur Narval, Rorqual et TamIA, le paquet wandb tentera automatiquement de télécharger les informations relatives à votre environnement vers un *bucket* Google Cloud Storage, ce qui n'est pas autorisé sur les nœuds de calcul de ces grappes et qui causera un plantage pendant ou à la toute fin d'une tâche. Votre tâche peut également se bloquer jusqu'à ce qu'elle atteigne son temps mort, gaspillant ainsi des ressources. Il n'est actuellement pas possible de désactiver ce comportement. Notez que le téléchargement d'artéfacts vers W&B avec `wandb.save()` nécessite également un accès à Google Cloud Storage et bloquera ou fera planter votre tâche.

Vous pouvez quand même utiliser wandb en activant les modes [`offline`](https://docs.wandb.ai/library/cli#wandb-offline) ou [`dryrun`](https://docs.wandb.ai/library/init#save-logs-offline). Avec ces modes, wandb écrit toutes les métriques, journalisations et artéfacts sur le disque local, sans synchronisation avec le service Internet Weights&Biases. Une fois les tâches terminées, vous pouvez faire la synchronisation avec la commande [`wandb sync`](https://docs.wandb.ai/ref/cli#wandb-sync) sur le nœud de connexion.

Remarquez que le produit [Comet.ml](comet.ml.md) est très semblable à Weights & Biases et qu'il fonctionne sur Narval, Rorqual et TamIA.

## Exemple

Voici un exemple d'utilisation de wandb pour faire le suivi d'expériences en mode hors ligne. Pour exécuter en ligne, chargez le module `httpproxy` sur les grappes et tenez compte des commentaires dans le script ci-dessous.

```bash title="wandb-test.sh"
#!/bin/bash
#SBATCH --account=YOUR_ACCOUNT
#SBATCH --cpus-per-task=2 # Nous recommandons au moins 2 CPU (un pour le processus principal et un autre pour le processus wandB)
#SBATCH --mem=4G       
#SBATCH --time=0-03:00
#SBATCH --output=%N-%j.out


module load python
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index wandb

### sauvegardez votre clé wandb API dans votre .bash_profile ou remplacez $API_KEY par votre propre clé API. Supprimez la ligne ci-dessous et identifiez wandb offline en commentaire si vous exécutez en mode en ligne. ###

#wandb login $API_KEY 

wandb offline

python wandb-test.py
```

Le script wandb-test.py est un exemple simple de journalisation des métriques. Pour d'autres options, voyez [la documentation complète de W&B](https://docs.wandb.ai).

```python title="wandb-test.py"
import wandb

wandb.init(project="wandb-pytorch-test", settings=wandb.Settings(start_method="fork"))

for my_metric in range(10):
    wandb.log({'my_metric': my_metric})
```

Après que l'entraînement a été effectué en mode hors ligne, vous aurez le nouveau répertoire `./wandb/offline-run*`. Pour envoyer les métriques au serveur, utilisez la commande `wandb sync ./wandb/offline-run*` où l'astérisque synchronise toutes les exécutions.