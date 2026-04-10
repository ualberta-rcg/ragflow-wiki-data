---
title: "Points de contrôle"
slug: "points_de_contrôle"
lang: "base"

source_wiki_title: "Points de contrôle"
source_hash: "8653f19854a575ae5cf9882f99098a5a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:56:43.831637+00:00"

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

Running a program can sometimes take too long for the maximum duration allowed by the job submission systems on the clusters. The execution of a long program is also subject to system instabilities. A program with a short execution time can be easily restarted. However, when a program's execution becomes very long, it is preferable to implement checkpoints to minimize the risk of losing several weeks of computation. Checkpoints will then allow the program to be restarted.

## Creation and Loading of a Checkpoint
Checkpoint creation and loading might already be implemented in an application you are using. In that case, simply use this functionality and consult the relevant documentation as needed.

However, if you have access to the application's source code and/or are its author, you can implement checkpoint creation and loading. Fundamentally:

*   Checkpoint files should be created periodically. We suggest intervals of 2 to 24 hours.
*   While writing the file, keep in mind that the computation task can be interrupted at any time for various technical reasons. Therefore:
    *   It is preferable not to overwrite the previous checkpoint when creating a new one.
    *   Writing can be made *atomic* by performing an operation that confirms the completion of the checkpoint write. For example, you can initially name the file based on the date and time, and finally create a symbolic link "latest-version" to the new, uniquely named checkpoint file. Another more advanced method is to create a second file containing a hash sum of the checkpoint, allowing validation of the checkpoint's integrity upon eventual loading.
    *   Once the atomic write is complete, you can decide whether or not to delete old checkpoints.

## Resubmitting a Long-Running Job
If a long computation is expected to be broken down into several Slurm tasks, the [two recommended methods](running-jobs.md#resubmitting-a-long-running-job) are:
*   [using Slurm job arrays](running-jobs.md#restarting-with-job-arrays);
*   [resubmitting from the end of the script](running-jobs.md#resubmitting-from-a-script).