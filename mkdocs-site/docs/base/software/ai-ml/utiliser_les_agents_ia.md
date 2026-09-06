---
title: "Utiliser les agents IA"
slug: "utiliser_les_agents_ia"
lang: "base"

source_wiki_title: "Utiliser les agents IA"
source_hash: "362f1824ee2650907a052bc561e3616e"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T03:03:38.230401+00:00"

tags:
  - ai-and-machine-learning
  - software
  - running-jobs

keywords:
  - "tâches batch SLURM"
  - "ticket de soutien"
  - "allocation SLURM"
  - "code MFA"
  - "permissions utilisateurs"
  - "grappes de l'Alliance"
  - "authentification multifacteur"
  - "SLURM_JOB_ID"
  - "allocation interactive SLURM"
  - "SLURM_CPUS_PER_TASK"
  - "planificateur SLURM"
  - "bonnes pratiques de calcul haute performance"
  - "agents d'intelligence artificielle"
  - "nœuds d’automatisation"
  - "modèle de langage"
  - "jeton d’API"
  - "mot de passe"
  - "bonnes pratiques"
  - "données sensibles"
  - "srun --pty bash"
  - "sbatch"
  - "sécurité des données"
  - "agent IA"
  - "clé privée"

questions:
  - "Quels sont les deux composants principaux à distinguer lorsqu’on utilise un agent IA sur les grappes de l’Alliance ?"
  - "Quels emplacements sont recommandés ou déconseillés pour exécuter un agent IA, et quelles en sont les raisons ?"
  - "Quelles bonnes pratiques faut‑il suivre pour lancer un agent IA en mode interactif ou batch avec SLURM ?"
  - "Quelles précautions doit‑on prendre avant d’utiliser un agent IA pour éviter de transmettre des données sensibles ou des secrets à un service externe ?"
  - "Comment les permissions d’accès aux fichiers diffèrent‑elles lorsqu’un agent est lancé par un autre utilisateur versus lorsqu’il est lancé par son propre compte ?"
  - "Quelles mesures de contrôle humain et de sécurité doivent être appliquées lors de l’utilisation d’un agent IA, notamment concernant les actions exécutées, l’utilisation des nœuds de calcul et la gestion des clés SSH/MFA ?"
  - "Comment vérifier que votre session est bien dans une allocation SLURM après avoir lancé `srun --pty bash` ?"
  - "Quels sont les avantages d’utiliser une tâche batch avec `sbatch` pour des expériences longues ou reproductibles ?"
  - "Pourquoi faut‑il vérifier chaque directive `#SBATCH` avant de soumettre le script, même si un agent aide à le préparer ?"
  - "Quelles informations sensibles (clé privée, mot de passe, code MFA, jeton d’API) sont interdites d’être jointes à un ticket de soutien ?"
  - "Quelles sont les exigences de Calcul Québec concernant l’utilisation des nœuds d’automatisation ?"
  - "Pourquoi le déploiement persistant d’un agent IA sur un nœud d’automatisation n’est‑il pas considéré comme approprié par Calcul Québec ?"
  - "Quelles architectures sont recommandées pour héberger l’agent IA (poste local, VM, allocation interactive ou tâche batch SLURM) ?"
  - "Quelles bonnes pratiques faut‑il appliquer concernant l’usage des nœuds, SLURM, la gestion des secrets et la reproductibilité des travaux ?"
  - "Quelles informations précises doivent être fournies dans un ticket de soutien lorsqu’un problème lié à l’agent IA apparaît ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**Artificial Intelligence (AI) agents** can help read and explain code, modify files, execute commands, prepare submission scripts, analyze logs, and assist with debugging. On a shared computing infrastructure, their use requires a clear distinction between the agentic process, the computing resources, and the model service used.

This page presents **general technical principles** for using AI agents on the Alliance clusters. It does not constitute institutional endorsement of any particular product or vendor.

!!! important
    To date, the Alliance has not formulated a general recommendation for or against the use of AI agents on its clusters. The subject is still under review. Site-specific or regional partner positions must be distinguished from general Alliance policies.

## Understanding Where an AI Agent Runs

At least two components must be distinguished:

*   The **agentic client**, which runs in the environment where the agent is launched.
*   The **language model**, which can be provided locally or by an external service, depending on the configuration used.

An agent launched with a user's account generally acts with the permissions granted to that account. Therefore, depending on its authorization mode, it can read files, execute commands, or prepare context for the model.

If the agent is launched on a login node, its process runs on that node. If it is launched within an interactive SLURM allocation, its process runs on the allocated compute node. This distinction is important for adhering to high-performance computing best practices.

## Where to Run an AI Agent?

| Location                            | Recommended Use                                             | Notes                                                                                                                                              |
| :---------------------------------- | :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local workstation or virtual machine | Often the simplest option for hosting the agent.            | The agent operates outside the cluster, and the user then connects to resources using authorized SSH, MFA, and SLURM mechanisms.                   |
| Login node                          | Limit to very light operations.                             | Prolonged use or costly agentic commands are not suitable for a login node.                                                                        |
| Compute node in an interactive allocation | Suitable for development, small tests, validation, and interactive debugging. | Use remains subject to local policies and available network connectivity on compute nodes.                                                           |
| SLURM batch job                     | Standard method for reproducible, long, or costly computations. | The agent can help prepare or analyze the job, but the computation is managed by SLURM.                                                            |
| Automation node                     | Site-dependent.                                             | At Calcul Québec, these nodes are intended for deterministic platforms entirely controlled by the user; an AI agent does not fit this definition. |

## Using AI Agents with SLURM

Compute-intensive workloads must be executed on compute nodes using the scheduler. See [Running Jobs](../../running-jobs/running_jobs.md) and [What is a Scheduler?](../../running-jobs/what_is_a_scheduler.md).

For interactive use, first request an allocation, for example:

```bash
salloc \
  --account=<account> \
  --time=01:00:00 \
  --cpus-per-task=2 \
  --mem=4G
```

Then open a shell within the allocation:

```bash
srun --pty bash
```

Next, verify that the session is indeed within an allocation:

```bash
hostname
echo "$SLURM_JOB_ID"
echo "$SLURM_CPUS_PER_TASK"
```

For long or reproducible experiments, prioritize a batch job with `sbatch`. The agent can help prepare the script, but each `#SBATCH` directive should be verified by the user before submission.

!!! note "Session End"
    Exit the agent and the interactive shell when they are no longer needed, then check that no unnecessary allocations remain active with:

    ```bash
    squeue -u "$USER"
    ```

## Security, Confidentiality, and Data Protection

### Sensitive Data

The Alliance's general computing resources are not suitable for storing sensitive data. Before using an AI agent, consult [Data Protection, Privacy, and Confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md) as well as the requirements of your institution and project.

The use of an AI agent does not change the classification or applicable obligations for data.

### Permissions Between Users

An agent launched by another user does not automatically bypass file system permissions. Standard Unix controls still apply.

The situation is different when a user launches an agent themselves: the agent can then access resources that the account can read or modify, to the extent permitted by its authorization mode.

!!! important "Important Distinction"
    `"another user cannot read my files"` and `"my own agent can access files that my account can read"` are two different issues.

### Data Transmitted to an External Service

If the model is provided by an external service, some context elements necessary for processing may leave the local infrastructure, depending on the tool's configuration.

Before any use:

*   Do not provide secrets, passwords, private keys, tokens, or MFA codes in a prompt.
*   Limit the agent to the necessary project directory.
*   Avoid exposing files unrelated to the task.
*   Examine requested permissions and proposed commands.
*   Verify the policies of the provider, institution, and project.
*   Do not use the agent with data for which external use conditions are not clearly established.

## Permissions and Human Control

The user remains responsible for the commands, modifications, and computations they authorize.

A cautious configuration should notably impose the following principles:

1.  Explain planned actions before execution.
2.  Do not launch compute-intensive tasks on login nodes.
3.  Use SLURM for compute workloads.
4.  Request confirmation before modifying files.
5.  Request confirmation before installing software.
6.  Request confirmation before submitting or cancelling jobs.
7.  Never delete data without explicit approval.
8.  Do not browse directories unrelated to the project.
9.  Never display or modify credentials or secrets.
10. Summarize actions performed.

## SSH, Public Keys, and Multifactor Authentication

SSH keys and multifactor authentication may correspond to distinct authentication steps. An accepted public key does not mean that the MFA step should be bypassed or disabled.

See [SSH](../../getting-started/ssh.md), [SSH Keys](../../getting-started/ssh_keys.md), [Multifactor Authentication](../../getting-started/multifactor_authentication.md), and [Automation in the Context of Multifactor Authentication](../../getting-started/automation_in_the_context_of_multifactor_authentication.md).

When an agent or application encapsulates an SSH connection, it is necessary to verify that the tool can manage an interactive session and the MFA challenge. If a classic SSH connection works but the application's integration fails, the problem may stem from how that application handles SSH interaction or the terminal.

To diagnose the connection from the same environment as the agent:

```bash
ssh -v <username>@<cluster>.alliancecan.ca
```

Never attach a private key, password, MFA code, or API token to a support ticket.

## Automation Nodes

Rules applicable to automation nodes may vary by site.

At Calcul Québec, the communicated position is that these nodes should be used by deterministic platforms entirely controlled by the user. An AI agent is not considered to meet this definition. Therefore, a persistent deployment of an agent on this type of node is not appropriate at Calcul Québec.

Preferred architectures are rather:

*   A local workstation or VM hosting the agent, with connection to the cluster via supported mechanisms.
*   An interactive SLURM allocation for interactive tests on a compute node, where policies and connectivity permit.
*   SLURM batch jobs for reproducible or costly computations.

## Best Practices

*   Do not use login nodes for compute-intensive tasks or agentic activity.
*   Use SLURM for CPU or GPU jobs.
*   Limit the agent to the necessary project directory.
*   Maintain human control over modifications, installations, deletions, and job submissions.
*   Never provide secrets to the agent or in a support ticket.
*   Verify applicable data rules before using an external model or service.
*   Independently validate the code, scientific results, and SLURM resources suggested by the agent.
*   Document tool, library, and environment versions to ensure reproducibility.
*   Close interactive allocations when they are no longer needed.

## Information to Provide in a Support Ticket

When reporting an issue related to an AI agent, provide the following information if possible:

*   The name of the cluster.
*   The location where the agent is running: local workstation, VM, login node, or compute node.
*   The operating system and tool version.
*   The SSH connection method used.
*   Whether a SLURM allocation is present or not.
*   The exact error message, without secrets.
*   Relevant output from a read-only diagnostic.
*   The observed difference between a classic SSH connection and the connection initiated by the agent, if applicable.

## See Also

*   [Running Jobs](../../running-jobs/running_jobs.md)
*   [Best Practices for Job Submission](../../running-jobs/best_practices_for_job_submission.md)
*   [Data Protection, Privacy, and Confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md)
*   [Multifactor Authentication](../../getting-started/multifactor_authentication.md)
*   [Automation in the Context of Multifactor Authentication](../../getting-started/automation_in_the_context_of_multifactor_authentication.md)
*   [SSH](../../getting-started/ssh.md)
*   Claude on Alliance Clusters