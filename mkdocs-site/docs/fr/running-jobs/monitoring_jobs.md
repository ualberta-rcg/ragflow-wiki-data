---
title: "Monitoring jobs/fr"
slug: "monitoring_jobs"
lang: "fr"

source_wiki_title: "Monitoring jobs/fr"
source_hash: "d36236ad760a1ce7adc12347e0ed2395"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:59:25.790341+00:00"

tags:
  []

keywords:
  - "scontrol"
  - "Job Wall-clock time"
  - "GPU"
  - "srun"
  - "COMPLETED"
  - "tmux"
  - "MaxRSS"
  - ".bat+"
  - "reportseff"
  - "Slurm output logs"
  - "sacct"
  - "sbatch"
  - "efficiency"
  - "NVTOP/fr"
  - "job IDs"
  - "--format"
  - "CPU Efficiency"
  - "NVTOP"
  - "Utilisation de GPU"
  - "nvidia-smi"
  - ".ext+"
  - "cycles CPU"
  - "tâche interactive"
  - "squeue"
  - "Voir"
  - "ReqMem"
  - "Memory Utilized"
  - "seff"

questions:
  - "Quels outils et commandes recommandez‑vous pour surveiller efficacement les tâches en cours sans surcharger l’ordonnanceur ?"
  - "Comment configurer les notifications par courriel pour être informé des changements d’état d’une tâche soumise avec sbatch ?"
  - "Quelle méthode utiliser pour obtenir un résumé de l’efficacité CPU et mémoire d’une tâche terminée, et comment obtenir des détails supplémentaires avec sacct ?"
  - "What does the reported CPU efficiency of 99.72 % (of 02:49:26 core‑walltime) tell us about how the job utilized the allocated CPU?"
  - "Why is the memory efficiency so low (0.17 % of 125 GB) even though the job used only 213.85 MB of memory?"
  - "How can you retrieve more detailed information about this completed task using the SLURM `sacct` command and its `--format` option?"
  - "Quelle est la différence entre les étapes .bat+, .ext+ et .0 affichées par la commande sacct, et comment chacune consomme‑t‑elle les ressources ?"
  - "Comment obtenir l’ensemble des enregistrements d’une tâche, y compris les éventuelles relances, en utilisant l’option --duplicates de sacct ?"
  - "Quelles sont les principales options de reportseff pour surveiller l’efficacité de plusieurs jobs et comment les appliquer ?"
  - "How can you use `reportseff` to add the `ReqMem` and `MaxRSS` columns when querying jobs from the past three days?"
  - "What commands are recommended for monitoring GPU usage of a running job, and how can they be run together using `tmux`?"
  - "What precautions should be observed when launching extra processes with `srun` on a node that is already executing a job?"
  - "What is the purpose of the `--format` option in the `reportseff` command and how is it used?"
  - "How does `reportseff` automatically identify job IDs when it is executed inside a directory containing Slurm output logs?"
  - "What does the example “Check efficiency for all jobs in the current directory” demonstrate about the functionality of `reportseff`?"
  - "Quel type d'informations trouve-t-on dans la section « Utilisation de GPU » de la page NVTOP ?"
  - "Comment NVTOP permet‑il de surveiller l’utilisation du GPU sur un système ?"
  - "Pourquoi est‑il important de consulter la documentation sur l’utilisation du GPU avec NVTOP ?"
  - "Pourquoi les cycles CPU ralentissent‑ils une tâche ?"
  - "Pourquoi la commande <code>srun</code> ne fonctionne que pour les tâches soumises avec <code>sbatch</code> ?"
  - "Comment suivre une tâche interactive en ouvrant plusieurs fenêtres <code>tmux</code> et en lançant les processus dans des fenêtres distinctes ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Un aspect important de votre responsabilité est de vous assurer que vos tâches utilisent efficacement les ressources qui leur sont attribuées, surtout lorsque vous utilisez un nouveau programme ou que vous apportez des modifications substantielles à une tâche.

Le meilleur outil pour obtenir des données sur la performance des tâches est le service web (portail) Metric sur chacune de nos grappes. Pour plus d'information, consultez notre [page wiki sur Metric](../software/metrix.md).

Le contenu de *la présente page* décrit d'autres méthodes pour évaluer l'efficacité des tâches.

## Tâches en cours

Par défaut, [squeue](https://slurm.schedmd.com/squeue.html) affiche toutes les tâches gérées par l'ordonnanceur à ce moment. L'exécution sera beaucoup plus rapide si vous n'incluez que vos propres tâches.

```bash
squeue -u $USER
```

L'utilitaire `sq` fait la même chose, mais vous permet d'entrer moins de texte.

Vous pouvez faire afficher uniquement les tâches en cours ou les tâches en attente.

```bash
squeue -u <nom-utilisateur> -t RUNNING
squeue -u <nom-utilisateur> -t PENDING
```

Pour l'information détaillée sur une tâche en particulier, utilisez [scontrol](https://slurm.schedmd.com/scontrol.html).

```bash
scontrol show job -dd <ID-tâche>
```

!!! warning "Avertissement : Utilisation de `squeue`"
    N'exécutez pas `squeue` à partir d'un script ou d'un programme à une fréquence élevée (par exemple, toutes les quelques secondes). Répondre à `squeue` augmente la charge de l'ordonnanceur et peut interférer avec sa performance ou son bon fonctionnement.

### Notification par courriel

Il est possible de recevoir une notification par courriel en rapport avec certaines conditions d'une tâche en ajoutant des options à `sbatch`.

```bash
#SBATCH --mail-user=votre.courriel@exemple.com
#SBATCH --mail-type=ALL
```

Pour la liste complète des options, consultez la [documentation de SchedMD sur `mail-type`](https://slurm.schedmd.com/sbatch.html#OPT_mail-type).

### Résultats en mémoire tampon

Normalement, les résultats d'une tâche non interactive sont mis en mémoire tampon (*buffered*), ce qui veut dire qu'il y a habituellement un temps d'attente entre le moment où les données de la tâche sont enregistrées et celui où vous pouvez voir les résultats dans un nœud de connexion. Ce temps d'attente dépend de l'application que vous utilisez et de la charge exercée sur le système de fichiers; il peut varier de moins d'une seconde à jusqu'à ce que la tâche se termine.

!!! tip "Conseil : Suivi en temps réel"
    Il existe des façons de réduire ou même d'éliminer ce temps d'attente, mais elles ne sont pas recommandées parce que l'utilisation de la mémoire tampon assure la bonne performance générale du système de fichiers. Si vous avez besoin de faire le suivi des résultats d'une tâche *en temps réel*, utilisez plutôt une [tâche interactive](#surveillance-dune-tache-en-cours).

## Tâches terminées

### Surveillance d'une tâche unique avec `seff`

Pour un sommaire de l'efficacité des CPU et de la mémoire, utilisez `seff`.

```bash
seff 12345678
```

```text
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
sacct -j <ID-tâche>
sacct -j <ID-tâche> --format=JobID,JobName,MaxRSS,Elapsed
```

Le résultat de `sacct` inclut généralement des enregistrements `.bat+` et `.ext+`, et possiblement aussi `.0, .1, .2, ...`.
L'étape *batch* (`.bat+`) est votre script de soumission; pour plusieurs tâches, c'est ici que s'effectue la plus grande part du travail et que les ressources sont consommées.
Si vous utilisez `srun` dans votre script de soumission, une étape `.0` serait créée, ce qui consommerait presque toutes les ressources.
L'étape externe (`.ext+`) est surtout en prologue et en épilogue et ne consomme habituellement pas une grande quantité de ressources.

S'il y a défaillance d'un nœud au cours de l'exécution d'une tâche, celle-ci peut être lancée à nouveau. `sacct` montre normalement le dernier enregistrement pour la dernière exécution (présumée réussie). Pour consulter tous les enregistrements relatifs à une tâche, ajoutez l'option `--duplicates`.

Le champ `MaxRSS` donne la quantité de mémoire utilisée par une tâche; il retourne la valeur du plus grand [resident set size](https://fr.wikipedia.org/wiki/Resident_set_size). Pour connaître la tâche et le nœud en cause, imprimez aussi les champs `MaxRSSTask` et `MaxRSSNode`.

La commande [sstat](https://slurm.schedmd.com/sstat.html) fournit des renseignements sur l'état d'une tâche en cours d'exécution et la commande [sacct](https://slurm.schedmd.com/sacct.html) est utilisée pour les tâches qui sont terminées.

### Surveillance de plusieurs tâches avec `reportseff`

[`reportseff`](https://github.com/troycomi/reportseff) est un enrobage Python autour de `sacct` qui fournit un sommaire tabulaire et codé par couleur de l'efficacité des tâches Slurm. Alors que `seff` est limité à l'inspection d'une seule tâche à la fois, `reportseff` interroge les enregistrements de comptabilité dans un seul appel par lots pour évaluer l'utilisation du CPU, de la mémoire et du temps *wall-clock* sur des tableaux de tâches, des répertoires de journaux de sortie, ou des historiques d'utilisateurs complets.

#### Utilisation

`reportseff` accepte les identifiants de tâche (Job IDs), les identifiants de tableau (array IDs), les chemins vers les fichiers de sortie Slurm, ou les filtres utilisateur/temps :

*   **Balayage du répertoire courant :** L'exécution de `reportseff` sans arguments balaye le répertoire de travail à la recherche de fichiers de sortie Slurm standards (par exemple, `slurm-%j.out` ou `%x_%A_%a.out`) et affiche les métriques pour les tâches correspondantes.
*   **Tâches ou tableaux spécifiques :** Passez un ou plusieurs identifiants de tâche (`reportseff 123456`), des tâches de tableau (`123456_1`), ou des noms de fichiers journaux directement.
*   **Filtrage par utilisateur et par temps :** Utilisez `-u <nom-utilisateur>` pour interroger les tâches récentes d'un utilisateur, et `--since` pour limiter la fenêtre de temps (accepte les formats de date `sacct` standards ou des raccourcis comme `j=3,h=2`).
*   **Colonnes personnalisées :** Ajoutez ou remplacez les champs `sacct` et d'efficacité en utilisant `--format` (par exemple, `--format +MaxRSS,ReqMem,GPUEff`).

#### Exemples

##### Vérifier l'efficacité de toutes les tâches dans le répertoire courant

L'appel de `reportseff` à l'intérieur d'un répertoire de projet contenant les journaux de sortie Slurm analyse automatiquement les identifiants de tâche (Job IDs) à partir des noms de fichiers :

```console
$ reportseff
   JobID      State          Elapsed   TimeEff   CPUEff   MemEff  
 39481020   COMPLETED       01:12:44    60.6%    98.2%    45.1%   
 39481021_1 COMPLETED       00:45:10    37.6%    94.0%    12.3%   
 39481021_2 COMPLETED       00:48:02    40.0%    95.1%    14.0%   
 39481021_3 OUT_OF_MEMORY   00:19:55    16.6%    88.4%   100.0%   
```

##### Interroger les tâches des 3 derniers jours avec des colonnes de mémoire supplémentaires

Pour auditer toutes les tâches exécutées par votre utilisateur au cours des trois derniers jours et ajouter la mémoire demandée (`ReqMem`) et l'empreinte mémoire maximale (`MaxRSS`) au tableau par défaut :

```console
$ reportseff -u $USER --since j=3 --format +ReqMem,MaxRSS
   JobID      State       Elapsed   TimeEff   CPUEff   MemEff   ReqMem   MaxRSS 
 39500112   COMPLETED    04:15:22    85.1%    99.1%    78.4%     16G     12.5G  
 39500489   TIMEOUT      12:00:10   100.0%    49.8%    22.0%     64G     14.1G  
 39501004   COMPLETED    00:08:14     6.9%    12.5%     3.1%     32G      1.0G  
```

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

!!! warning "Avertissement : Partage des ressources avec `srun`"
    Les processus lancés avec `srun` partagent les ressources utilisées par la tâche en question. Il faut donc éviter de lancer des processus qui utiliseraient les ressources au détriment de la tâche. Dans les cas où les processus utilisent trop de ressources, la tâche pourrait être arrêtée; le fait d'utiliser trop de cycles CPU ralentit une tâche.

!!! note "Note"
    Dans les exemples précédents, `srun` fonctionne uniquement sur des tâches soumises avec `sbatch`. Pour faire le suivi d'une tâche interactive, ouvrez plusieurs fenêtres avec `tmux` et démarrez les processus dans des fenêtres distinctes.

## Suivi des tâches qui utilisent un GPU

Consultez [Utilisation de GPU](../programming/nvtop.md).