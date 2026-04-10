---
title: "NVTOP/fr"
slug: "nvtop"
lang: "fr"

source_wiki_title: "NVTOP/fr"
source_hash: "8527bdc8e8f883cd859e14b4d5c502d3"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:07:42.576300+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[NVTOP](https://github.com/Syllo/nvtop) (pour *Neat Videocard TOP*) est un outil de type htop et top servant à surveiller l'utilisation de GPU et d'accélérateurs.

Une image qui vaut mille mots

## Utilisation de GPU
NVTOP peut gérer un ou plusieurs GPU et montrer leur utilisation et leur mémoire. Vous pouvez aussi sélectionner un autre accélérateur à partir du menu (F2 -> Sélection GPU).

NVTOP est utile pour suivre et vérifier que votre tâche fait la meilleure utilisation des GPU.

### Tâches non interactives
Si vous avez soumis une tâche qui n'est pas interactive et voulez voir son utilisation du GPU,

1.  Depuis un nœud de connexion, trouvez l'ID de la tâche.
    ```bash
    sq
    ```

2.  Attachez-vous à la tâche en cours.
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

### Tâches interactives
1.  Lancez votre tâche interactive avec le moins de ressources possible.

2.  Dans un autre terminal, connectez-vous au nœud de connexion et trouvez l'ID de la tâche.
    ```bash
    sq
    ```

3.  Attachez-vous à la tâche en cours.
    ```bash
    srun --pty --overlap --jobid JOBID nvtop
    ```

Vous pouvez voir l'utilisation en temps réel au fur et à mesure que vos commandes sont exécutées dans le premier terminal.

### Utilisation de GPU sur un nœud particulier
Avec les tâches qui utilisent plusieurs nœuds, vous pouvez vérifier qu'un ou plusieurs GPU sont utilisés le plus efficacement possible.

1.  Depuis un nœud de connexion, trouvez l'ID de la tâche et trouvez le nom des nœuds.
    ```bash
    sq
    srun --jobid JOBID --overlap -n1 -c1 scontrol show hostname
    ```

2.  Attachez-vous à la tâche en cours sur le nœud spécifique.
    ```bash
    srun --pty --overlap --jobid JOBID --nodelist NODENAME nvtop