---
title: "Monitoring jobs/fr"
slug: "monitoring_jobs"
lang: "fr"

source_wiki_title: "Monitoring jobs/fr"
source_hash: "14485b087dd9fa1cc71b1b2aa08ed6be"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:58:02.045231+00:00"

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

Un aspect important de votre responsabilité est de vous assurer que vos tâches utilisent efficacement les ressources qui leur sont attribuées, surtout lorsque vous utilisez un nouveau programme ou que vous apportez des modifications substantielles à une tâche. Nous décrivons ici différentes méthodes d'évaluation de l'efficacité des tâches, qu'elles soient en cours d'exécution ou terminées.

## Tâches en cours

Par défaut, [squeue](https://slurm.schedmd.com/squeue.html) affiche toutes les tâches gérées par l'ordonnanceur à ce moment. L'exécution sera beaucoup plus rapide si vous n'incluez que vos propres tâches.

```bash
squeue -u $USER
```

L'utilitaire `sq` fait la même chose, mais vous permet d'entrer moins de texte.

Vous pouvez faire afficher uniquement les tâches en cours ou les tâches en attente.

```bash
squeue -u <username> -t RUNNING
```

```bash
squeue -u <username> -t PENDING
```

Pour l'information détaillée sur une tâche en particulier, utilisez [scontrol](https://slurm.schedmd.com/scontrol.html).

```bash
scontrol show job -dd <jobid>
```

!!! warning "Ne pas utiliser `squeue` fréquemment"
    N'exécutez pas `squeue` à partir d'un script ou d'un programme à une fréquence élevée (par exemple, toutes les quelques secondes). Répondre à `squeue` augmente la charge de l'ordonnanceur et peut interférer avec sa performance ou son bon fonctionnement.

### Notification par courriel

Il est possible de recevoir une notification par courriel en rapport avec certaines conditions d'une tâche en ajoutant des options à `sbatch`.

```bash
#SBATCH --mail-user=your.email@example.com
#SBATCH --mail-type=ALL
```

Pour la liste complète des options, voir [la documentation de SchedMD](https://slurm.schedmd.com/sbatch.html#OPT_mail-type).

### Résultats en mémoire tampon

Normalement, les résultats d'une tâche non interactive sont mis en mémoire tampon (*buffered*), ce qui veut dire qu'il y a habituellement un temps d'attente entre le moment où les données de la tâche sont enregistrées et celui où vous pouvez voir les résultats dans un nœud de connexion. Ce temps d'attente dépend de l'application que vous utilisez et de la charge exercée sur le système de fichiers; il peut varier de moins d'une seconde à jusqu'à ce que la tâche se termine.

Il existe des façons de réduire ou même d'éliminer ce temps d'attente, mais elles ne sont pas recommandées parce que l'utilisation de la mémoire tampon assure la bonne performance générale du système de fichiers. Si vous avez besoin de faire le suivi des résultats d'une tâche *en temps réel*, utilisez plutôt une [tâche interactive](#tâches-interactives), comme décrit ci-dessus.

## Tâches terminées

Pour un sommaire de l'efficacité des CPU et de la mémoire, utilisez `seff`.

```bash
seff 12345678
```

```
Job ID: 12345678
Cluster: cedar
User/Group: jsmith/jsmith
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 02:48:58
CPU Efficiency: 99.72% of 02:49:26 core-walltime
Job Wall-clock time: 02:49:26
Memory Utilized: 213.85 MB
Memory Efficiency: 0.17% of 125.00 GB
```

Pour l'information détaillée sur une tâche qui est terminée, utilisez [sacct](https://slurm.schedmd.com/sacct.html); en option, il est possible de déterminer le contenu affiché avec `--format`.

```bash
sacct -j <jobid>
```

```bash
sacct -j <jobid> --format=JobID,JobName,MaxRSS,Elapsed
```

Le résultat de `sacct` inclut généralement des enregistrements `.bat+` et `.ext+`, et possiblement aussi `.0`, `.1`, `.2`, ...
L'étape *batch* (`.bat+`) est votre script de soumission; pour plusieurs tâches, c'est ici que s'effectue la plus grande part du travail et que les ressources sont consommées.
Si vous utilisez `srun` dans votre script de soumission, une étape `.0` serait créée, ce qui consommerait presque toutes les ressources.
L'étape externe (`.ext+`) est surtout en prologue et en épilogue et ne consomme habituellement pas une grande quantité de ressources.

S'il y a défaillance d'un nœud au cours de l'exécution d'une tâche, celle-ci peut être lancée à nouveau. `sacct` montre normalement le dernier enregistrement pour la dernière exécution (présumée réussie). Pour consulter tous les enregistrements relatifs à une tâche, ajoutez l'option `--duplicates`.

Le champ MaxRSS donne la quantité de mémoire utilisée par une tâche; il retourne la valeur du plus grand [*resident set size*](https://fr.wikipedia.org/wiki/Resident_set_size). Pour connaître la tâche et le nœud en cause, imprimez aussi les champs MaxRSSTask et MaxRSSNode.

La commande [sstat](https://slurm.schedmd.com/sstat.html) fournit des renseignements sur l'état d'une tâche en cours d'exécution et la commande [sacct](https://slurm.schedmd.com/sacct.html) est utilisée pour les tâches qui sont terminées.

## Surveillance d'une tâche en cours

Il est possible de se connecter à un nœud sur lequel une tâche est en cours et d'y exécuter de nouveaux processus. Ceci est utile en particulier pour des opérations de dépannage ou pour suivre le déroulement d'une tâche.

L'utilitaire [`nvidia-smi`](https://developer.nvidia.com/nvidia-system-management-interface) est employé pour surveiller l'utilisation d'un GPU sur un nœud où une tâche est en cours d'exécution. L'exemple suivant exécute `watch` sur le nœud qui à son tour lance `nvidia-smi` toutes les 30 secondes et affiche le résultat au terminal.

```bash
srun --jobid 123456 --overlap --pty watch -n 30 nvidia-smi
```

Plusieurs commandes peuvent être lancées avec [`tmux`](https://fr.wikipedia.org/wiki/Tmux). L'exemple suivant exécute `htop` et `nvidia-smi` dans des fenêtres distinctes pour faire le suivi de l'activité sur le nœud où la tâche est exécutée.

```bash
srun --jobid 123456 --overlap --pty tmux new-session -d 'htop -u $USER' \; split-window -h 'watch nvidia-smi' \; attach
```

!!! note "Partage de ressources avec `srun`"
    Les processus lancés avec `srun` partagent les ressources utilisées par la tâche en question. Il faut donc éviter de lancer des processus qui utiliseraient les ressources au détriment de la tâche. Dans les cas où les processus utilisent trop de ressources, la tâche pourrait être arrêtée; le fait d'utiliser trop de cycles CPU ralentit une tâche.

!!! tip "Note sur `srun` et les tâches interactives"
    Dans les exemples précédents, `srun` fonctionne uniquement sur des tâches soumises avec `sbatch`. Pour faire le suivi d'une tâche interactive, ouvrez plusieurs fenêtres avec `tmux` et démarrez les processus dans des fenêtres distinctes.

## Suivi des tâches qui utilisent un GPU

Voir [Utilisation de GPU](nvtop.md#utilisation-de-gpu).