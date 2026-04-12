---
title: "NVTOP/fr"
slug: "nvtop"
lang: "fr"

source_wiki_title: "NVTOP/fr"
source_hash: "8527bdc8e8f883cd859e14b4d5c502d3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:39:46.032629+00:00"

tags:
  []

keywords:
  - "tâches interactives"
  - "nœud"
  - "tâches non interactives"
  - "utilisation de GPU"
  - "NVTOP"

questions:
  - "Qu'est-ce que l'outil NVTOP et quelle est sa fonction principale ?"
  - "Comment peut-on attacher NVTOP à une tâche en cours (interactive ou non) pour surveiller son utilisation du GPU ?"
  - "Quelle est la procédure pour vérifier l'utilisation des GPU sur un nœud spécifique lors d'une tâche impliquant plusieurs nœuds ?"
  - "Qu'est-ce que l'outil NVTOP et quelle est sa fonction principale ?"
  - "Comment peut-on attacher NVTOP à une tâche en cours (interactive ou non) pour surveiller son utilisation du GPU ?"
  - "Quelle est la procédure pour vérifier l'utilisation des GPU sur un nœud spécifique lors d'une tâche impliquant plusieurs nœuds ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[NVTOP](https://github.com/Syllo/nvtop) (pour *Neat Videocard TOP*) est un outil de type htop et top servant à surveiller l'utilisation des GPU et des accélérateurs.

Une image qui vaut mille mots

# Utilisation des GPU
NVTOP peut gérer un ou plusieurs GPU et afficher leur utilisation ainsi que leur mémoire.
Vous pouvez aussi sélectionner un autre accélérateur à partir du menu (F2 -> Sélection de GPU).

NVTOP est utile pour suivre et vérifier que votre tâche utilise les GPU de manière optimale.

## Tâches non interactives
Si vous avez soumis une tâche non interactive et que vous souhaitez surveiller son utilisation du GPU :

1.  Depuis un nœud de connexion, trouvez l'ID de la tâche.
    ```bash
    sq
    ```

2.  Attachez-vous à la tâche en cours.
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

## Tâches interactives
1.  Lancez votre tâche interactive avec le minimum de ressources possible.

2.  Dans un autre terminal, connectez-vous au nœud de connexion et trouvez l'ID de la tâche.
    ```bash
    sq
    ```

3.  Attachez-vous à la tâche en cours.
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

Vous pourrez ainsi observer l'utilisation en temps réel au fur et à mesure que vos commandes s'exécutent dans le premier terminal.

## Utilisation des GPU sur un nœud particulier
Pour les tâches qui utilisent plusieurs nœuds, vous pouvez vérifier qu'un ou plusieurs GPU sont utilisés le plus efficacement possible.

1.  Depuis un nœud de connexion, trouvez l'ID de la tâche et déterminez le nom des nœuds.
    ```bash
    sq
    srun --jobid JOBID --overlap -n1 -c1 scontrol show hostname
    ```

2.  Attachez-vous à la tâche en cours sur le nœud spécifique.
    ```bash
    srun --pty --overlap --jobid JOBID --nodelist NODENAME nvtop