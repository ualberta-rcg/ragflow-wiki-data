---
title: "Points de contrôle"
slug: "points_de_contrôle"
lang: "base"

source_wiki_title: "Points de contrôle"
source_hash: "8653f19854a575ae5cf9882f99098a5a"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:25:19.808304+00:00"

tags:
  []

keywords:
  - "working directory"
  - "Slurm"
  - "Redémarrage du programme"
  - "dmtcp_restart_script.sh"
  - "Resoumettre une tâche"
  - "DMTCP"
  - "simulation"
  - "restart"
  - "resoumission à partir d'un script"
  - "Grappes de calcul"
  - "vecteurs de tâches"
  - "checkpoint file"
  - "Exécution longue"
  - "calcul de longue durée"
  - "Points de contrôle"

questions:
  - "Pourquoi est-il crucial d'utiliser des points de contrôle pour les programmes ayant une longue durée d'exécution sur des grappes de calcul ?"
  - "Quelles sont les bonnes pratiques à suivre lors de l'écriture du code source pour garantir la création sécuritaire et atomique d'un point de contrôle ?"
  - "Comment fonctionne le logiciel DMTCP pour effectuer des sauvegardes et redémarrer un programme sans nécessiter sa recompilation ?"
  - "Quelles sont les deux méthodes recommandées pour morceler et resoumettre un calcul de longue durée dans Slurm ?"
  - "Quel est le rôle de la commande `dmtcp_launch` et de ses paramètres dans l'extrait de script fourni ?"
  - "Comment la technique de resoumission à la fin du script se différencie-t-elle de l'utilisation des vecteurs de tâches (job arrays) ?"
  - "What information does the script log before attempting to run the simulation step?"
  - "How does the script determine whether to restart an existing simulation or start a new one?"
  - "What specific command and argument are executed if a checkpoint file is found?"
  - "Quelles sont les deux méthodes recommandées pour morceler et resoumettre un calcul de longue durée dans Slurm ?"
  - "Quel est le rôle de la commande `dmtcp_launch` et de ses paramètres dans l'extrait de script fourni ?"
  - "Comment la technique de resoumission à la fin du script se différencie-t-elle de l'utilisation des vecteurs de tâches (job arrays) ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Program execution is sometimes too long for the duration allowed by the cluster's job submission systems. Long program executions are also subject to system instabilities. A program with a short execution time can be easily restarted. However, when program execution becomes very long, it is preferable to use checkpoints to minimize the chances of losing several weeks of computation. These checkpoints will subsequently allow the program to be restarted.

## Creating and Loading a Checkpoint
Checkpoint creation and loading may already be implemented in an application you are using. In this case, simply use this functionality and consult the relevant documentation as needed.

However, if you have access to the application's source code and/or are its author, you can implement checkpoint creation and loading. Fundamentally:

*   A checkpoint file should be created periodically. Periods of 2 to 24 hours are suggested.
*   While writing the file, keep in mind that the computation task can be interrupted at any time, for any technical reason. Therefore:
    *   It is preferable not to overwrite the previous checkpoint when creating a new one.
    *   Writing can be made *atomic* by performing an operation that confirms the completion of the checkpoint write. For example, you can initially name the file based on the date and time, and finally create a symbolic link "latest-version" to the new, uniquely named checkpoint file. Another more advanced method: you can create a second file containing a hash sum of the checkpoint, allowing validation of the checkpoint's integrity upon eventual loading.
    *   Once the atomic write is complete, you can decide whether or not to delete old checkpoints.

!!! note
    To avoid reinventing the wheel, especially if modifying the source code is not an option, we suggest using [DMTCP](http://dmtcp.sourceforge.net/).

### DMTCP
The [DMTCP](http://dmtcp.sourceforge.net/) (Distributed Multithreaded CheckPointing) software allows you to checkpoint programs without having to recompile them. The first execution is performed with the `dmtcp_launch` program, specifying the time between save intervals. Restarting is done by executing the `dmtcp_restart_script.sh` script. By default, this script and the program restart files are written to the location where the program was launched. You can change the location of the checkpoint files with the `--ckptdir <checkpoint-directory>` option. You can use `dmtcp_launch --help` to get all options. Note that DMTCP does not currently work with MPI-parallelized software.

An example script:
```bash title="job_with_dmtcp.sh"
#!/bin/bash
# ---------------------------------------------------------------------
# SLURM script for job resubmission on a Compute Canada cluster.
# ---------------------------------------------------------------------
#SBATCH --job-name=job_chain
#SBATCH --account=def-someuser
#SBATCH --cpus-per-task=1
#SBATCH --time=0-10:00
#SBATCH --mem=100M
# ---------------------------------------------------------------------
echo "Current working directory: $(pwd)"
echo "Starting run at: $(date)"
# ---------------------------------------------------------------------
# Run your simulation step here...

if test -e "dmtcp_restart_script.sh"; then
     # There is a checkpoint file, restart;
     ./dmtcp_restart_script.sh -h $(hostname)
else
     # There is no checkpoint file, start a new simulation.
     dmtcp_launch --rm  -i 3600 -q <programme> <arg1> ... <argn>
fi

# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: $(date)"
# ---------------------------------------------------------------------
```

## Resubmitting a Long-Running Job
If a long computation is expected to be broken down into several Slurm tasks, the [two recommended methods](running_jobs.md#resubmitting-a-long-running-job) are:
*   [using Slurm job arrays](running_jobs.md#restarting-with-job-arrays);
*   [resubmitting from the end of the script](running_jobs.md#resubmitting-from-a-script).