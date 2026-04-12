---
title: "Points de contrôle/en"
slug: "points_de_contrôle"
lang: "en"

source_wiki_title: "Points de contrôle/en"
source_hash: "1479206faf68968efa4ce8ff663b2dec"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:25:38.409006+00:00"

tags:
  []

keywords:
  - "Slurm jobs"
  - "long-running jobs"
  - "resubmitting jobs"
  - "job schedulers"
  - "Checkpoints"

questions:
  - "Why is it highly recommended to use checkpoints for long-running programs on computing clusters?"
  - "What are the essential steps and best practices for manually implementing atomic checkpoint creation in a program's source code?"
  - "What are the recommended methods for breaking up and resubmitting a lengthy computation into multiple Slurm jobs?"
  - "Why is it highly recommended to use checkpoints for long-running programs on computing clusters?"
  - "What are the essential steps and best practices for manually implementing atomic checkpoint creation in a program's source code?"
  - "What are the recommended methods for breaking up and resubmitting a lengthy computation into multiple Slurm jobs?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The execution time for a program is sometimes too long for the maximum duration of a job permitted by the job schedulers used on the clusters. Long-running jobs are also subject to all of the risks of system instability due to power outages, hardware defects and so forth. A program with a short execution time can easily be restarted with little concern but for long-running software it is preferable to use checkpoints to minimize the risk of losing several days' worth of computation. These checkpoints take the form of binary disk files from which the program can be restarted at the point in the computation where the checkpoint file was initially created.

## Creating and Loading a Checkpoint

The creation and loading of a checkpoint may already be taken care of by the application you're using. In this case you simply need to read the relevant documentation about how to use this functionality.

However, if you have access to the source code of the software and/or if you are the author, you can implement a checkpoint/restart functionality in the program yourself. The essential steps are:

*   The creation of a checkpoint file is done periodically, with a suggested frequency of every 2 to 24 hours

!!! tip "Atomic Checkpoint Creation"
    When creating a checkpoint file, it's crucial to consider that the program might be interrupted at any moment. To ensure checkpoint integrity and avoid data loss, follow these practices:

    *   It is preferable to not delete the preceding checkpoint when creating the new one.
    *   The creation of the checkpoint file can be made *atomic* by performing an operation which confirms the end of the checkpoint process. For example, the checkpoint file can be initially named based on the date and time and, as the final step, a symbolic link *latest-version* is pointed at this new checkpoint file. Another more advanced method would be to create a second file which contains a hash of the checkpoint file's content by means of which the restart function can verify the integrity of the checkpoint when it is loaded.
    *   Once the atomic write has been completed, one can choose whether or not to delete any older checkpoints.

## Resubmitting a Job for Long-Running Computations

If you plan on breaking up a lengthy computation into several Slurm jobs, there are [two recommended methods](running_jobs.md#resubmitting-jobs-for-long-running-computations):
*   [using Slurm job arrays](running_jobs.md#restarting-using-job-arrays);
*   [resubmission from the end of the job script](running_jobs.md#resubmission-from-the-job-script).