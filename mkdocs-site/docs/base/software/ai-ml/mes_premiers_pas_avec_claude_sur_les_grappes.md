---
title: "Mes premiers pas avec Claude sur les grappes"
slug: "mes_premiers_pas_avec_claude_sur_les_grappes"
lang: "base"

source_wiki_title: "Mes premiers pas avec Claude sur les grappes"
source_hash: "76c7c452e3678a738385ec6734b8ed05"
last_synced: "2026-09-06T00:43:13.954271+00:00"
last_processed: "2026-09-06T03:02:50.358513+00:00"

tags:
  - ai-and-machine-learning
  - software
  - running-jobs

keywords:
  - "nœud de calcul"
  - "clé SSH publique"
  - "sécurité des commandes"
  - "Claude"
  - "allocation SLURM"
  - "diagnostiquer"
  - "authentification"
  - "clé API"
  - "SSH"
  - "GPU de la grappe"
  - "authentification multifacteur"
  - "hello_cluster.py"
  - "salloc"
  - "Duo"
  - "analyse des résultats"
  - "Duo MFA"
  - "grappes de l’Alliance"
  - "Claude Code"
  - "nœuds d’automatisation de Calcul Québec"
  - "politiques du site"
  - "clé SSH privée"
  - "Claude Science"
  - "SLURM"
  - "données sensibles"
  - "squeue"
  - "srun --pty bash"
  - "programmes soumis via SLURM"
  - "script SLURM"
  - "installation native"
  - "permissions du répertoire"

questions:
  - "Quelles vérifications préalables doivent être effectuées avant de lancer Claude Code sur une grappe de l’Alliance ?"
  - "Quels sont les deux procédés d’installation de Claude Code (natif et via npm) et quelles précautions spécifiques faut‑il observer sur une grappe partagée ?"
  - "Comment authentifier Claude Code, garantir la connectivité réseau requise et sécuriser les secrets lors d’une exécution interactive avec SLURM ?"
  - "Pourquoi ne faut‑il jamais placer une clé API, un mot de passe, une clé SSH privée ou un code MFA dans un fichier partagé, un script SLURM, un dépôt Git ou un ticket de soutien ?"
  - "Quelle est la séquence de commandes recommandée pour demander d’abord une allocation puis ouvrir un shell interactif avec SLURM ?"
  - "Quels sont les paramètres spécifiés dans l’exemple de commande `salloc` (compte, temps, CPU, mémoire) et quelle est leur fonction respective ?"
  - "Quels sont les étapes essentielles pour créer, soumettre et suivre une tâche SLURM avec l’aide de Claude ?"
  - "Comment garantir la sécurité et les permissions appropriées lorsqu’on utilise Claude dans le répertoire d’un projet sur le cluster ?"
  - "Quelles sont les limites de Claude concernant la validation scientifique, la revue de code et l’estimation des ressources ?"
  - "Quels éléments faut‑il vérifier (client SSH, OS, version, sortie `ssh -v`, etc.) lorsqu’une connexion SSH via Claude Science échoue alors que le SSH classique fonctionne ?"
  - "Pourquoi les nœuds d’automatisation de Calcul Québec ne sont pas adaptés pour héberger Claude en tant que service persistant, et quelles alternatives (poste local/VM, allocation interactive SLURM, batch SLURM) sont recommandées ?"
  - "Quelles actions de dépannage sont suggérées pour chaque symptôme répertorié (commande introuvable, problème d’authentification, échec de connexion SSH depuis Claude, ressources excessives, etc.) ?"
  - "Qui est responsable de la sécurité des commandes et du code approuvé selon le texte ?"
  - "Quel problème a été observé lorsqu’une connexion SSH initiée par Claude Science n’a pas affiché correctement l’étape Duo MFA ?"
  - "Quelle procédure est recommandée pour diagnostiquer ce type de dysfonctionnement ?"
  - "Une clé SSH publique peut‑elle remplacer l’authentification multifacteur Duo ?"
  - "Est‑il autorisé d’installer Claude sur les nœuds d’automatisation de Calcul Québec ?"
  - "Peut‑on utiliser Claude pour traiter des données sensibles sur les ressources de calcul de l’Alliance ?"
  - "Quelles sont les conditions et les politiques à respecter pour demander une allocation SLURM et utiliser un nœud de calcul ?"
  - "Pourquoi la génération des réponses de Claude ne s’effectue‑t‑elle pas sur les GPU de la grappe lorsqu’on utilise Claude Code avec un service de modèle externe ?"
  - "Comment les GPU de la grappe sont‑ils employés par les programmes soumis par les utilisateurs via SLURM dans ce contexte ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Getting Started with Claude on Clusters

**[Claude Code](https://claude.com/product/claude-code)** is a command-line coding agent developed by Anthropic. It can read and explain code, modify files, execute shell commands, prepare SLURM scripts, analyze logs, and support debugging.

This page describes the installation and use of Claude Code in the context of Alliance clusters. For general principles applicable to all AI agents: execution location, SLURM, security, data, permissions, and MFA, see [Using AI Agents](using_ai_agents.md).

**Terminology:** The term "Claude" here refers to Claude Code or an environment that relies on Claude Code. An interface like "Claude Science" may encapsulate Claude Code, but its SSH connection or authentication mechanism may differ.

## Before You Begin

Before using Claude on a cluster:

*   determine where the Claude client will run;
*   avoid prolonged use on a login node;
*   use SLURM for compute workloads;
*   check the applicable project data policy;
*   verify that the required network connectivity is available;
*   maintain human control over proposed commands and modifications.

For interactive use on the cluster, a SLURM allocation is the preferred technical architecture when local policies and connectivity permit.

## Installing Claude Code

Before installing Claude, check if the executable is already available:

```bash
which claude
claude --version
```

### Native Installation

Anthropic's documentation recommends a native installation on Linux. In an environment where external downloads are allowed:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

The launcher is usually installed in the user's home directory. If necessary, add the corresponding directory to the `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
claude --version
claude doctor
```

!!! warning "Local Verification"
    Outbound network and software installation policies may vary between systems. Do not use `sudo` to bypass permissions on a shared cluster.

### Installation with npm

An installation with npm is also possible. First, check available versions:

```bash
node --version
npm --version
```

Then install the package in an appropriate user space:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

!!! warning
    Do not use `sudo npm install -g` on a shared cluster.

### Installation Verification

The following commands can be used to verify the installation:

```bash
claude --version
claude doctor
```

`claude doctor` provides read-only diagnostics on the installation and configuration.

## Authentication and Network Connectivity

Claude Code must be authenticated with the configured model service. Depending on the context, authentication may be through an authorized Claude account, the Anthropic Console/API, or an infrastructure provider supported by the organization.

Upon first launch:

```bash
claude
```

the client normally opens the appropriate login flow.

Claude Code also requires network connectivity to the configured service. Therefore, it's possible for the executable to work in one environment but for the session to fail in another if outbound network rules differ.

!!! warning "Secrets"
    Never place an API key, password, private SSH key, or MFA code in a shared file, SLURM script, Git repository, or support ticket.

## Interactive Execution with SLURM

First, request an allocation:

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

Verify the environment:

```bash
hostname
echo "$SLURM_JOB_ID"
echo "$SLURM_CPUS_PER_TASK"
```

Then navigate to the project directory and launch Claude:

```bash
cd /path/to/project
claude
```

Exit Claude and the allocation when no longer needed. Check active jobs with:

```bash
squeue -u "$USER"
```

## Example Test on Narval

The following example illustrates a controlled test. It can be adapted to another cluster.

### Project Structure

```
claude_science_test/
├── config/
├── logs/
├── results/
├── scripts/
├── src/
├── environment.sh
├── REPORT.md
└── TUTORIAL.md
```

### Explore the Project Without Modification

Example prompt:

```
Read the current project.
Explain the directory structure.
Do not modify any file.
```

### Create a Small Python Program

Example prompt:

```
Create a Python program called hello_cluster.py.

The program should:
- print the hostname
- print the current date
- print the Python version

Explain the code before creating it.
```

Example program:

```python
import platform
import socket
from datetime import datetime

print("Hostname:", socket.gethostname())
print("Date:", datetime.now())
print("Python:", platform.python_version())
```

### Prepare a SLURM Script

Example prompt:

```
Create a Slurm script to execute hello_cluster.py.

Requirements:
- 1 CPU
- 1 GB RAM
- execution time: 5 minutes
- save logs in logs/

Explain the script before creating it.
```

Example script:

```bash
#!/bin/bash
#SBATCH --job-name=claude_hello
#SBATCH --account=<account>
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

module load python
python src/hello_cluster.py
```

### Submit and Track the Job

After human verification of the script:

```bash
sbatch scripts/run_hello.sh
squeue -u "$USER"
sacct -j <jobid> --format=JobID,JobName,State,Elapsed,AllocCPUS,ReqMem,MaxRSS,ExitCode
```

### Analyze Results

Example prompt:

```
Read the newest Slurm output.
Explain whether the execution succeeded.
Identify errors, if any.
Do not modify any files.
```

!!! tip "Principle"
    Claude can accelerate development and analysis but does not replace scientific validation, code review, or understanding of requested resources.

## Claude and Batch Jobs

For a long, reproducible, or costly experiment, Claude's role should remain focused on preparation, review, and analysis. Scientific execution remains managed by SLURM.

1.  Ask Claude to read the program and estimate the necessary resources.
2.  Have a SLURM script generated and verify each `#SBATCH` directive.
3.  Submit the job with `sbatch` after human validation.
4.  Use `squeue` and `sacct` to track execution.
5.  Ask Claude to analyze logs and results, then scientifically validate the conclusion.

## Limiting Claude's Project Access

Before launching Claude, check directory permissions:

```bash
ls -ld /path/to/project
ls -l /path/to/project
```

Then navigate to the minimal necessary directory:

```bash
cd /project/<account>/my_project
claude
```

In its manual mode, Claude Code uses a permission model where write operations and many commands require user approval. The user remains responsible for the security of the commands and code they approve.

## Claude Science, SSH, and Duo MFA

A support case revealed a situation where SSH worked normally from a terminal with a public key, but a connection initiated by Claude Science to an Alliance resource did not properly present the Duo MFA step.

To diagnose this type of issue, run the test from the same environment as Claude Science:

```bash
ssh -v <username>@narval.alliancecan.ca
```

Then check:

*   if Claude Science uses an integrated SSH client or the system's `ssh` command;
*   the operating system and Claude version;
*   if the connection hangs indefinitely or terminates immediately;
*   the relevant part of the `ssh -v` output, without sharing secrets.

If classic SSH works but the application's integration does not present the Duo challenge, the problem is likely related to how the application handles the interactive SSH session or terminal, rather than the Alliance account itself.

!!! warning
    A public SSH key and Duo MFA address distinct authentication steps. Do not attempt to bypass Duo.

## Calcul Québec Automation Nodes

Calcul Québec has indicated that its automation nodes are intended for deterministic platforms fully controlled by the user. Claude, as an AI agent, does not meet this definition.

!!! warning
    Therefore, you should not request to host Claude as a persistent service on a Calcul Québec automation node.

The preferred options are:

*   Claude on a local workstation or VM, connecting to the cluster via supported mechanisms;
*   Claude in an interactive SLURM allocation for interactive testing when permitted;
*   SLURM batch for reproducible or costly computations.

## Troubleshooting

| Symptom                               | Check                                                                        | Action                                                                                                 |
| :------------------------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| `` `claude: command not found` ``      | `` `which claude` `` and `` `echo $PATH` ``                                 | Verify user installation and the `` `~/.local/bin` `` directory.                                      |
| Claude works in one environment but not in another | `` `claude --version` ``, `` `claude doctor` ``, environment variables, and network connectivity | Compare `PATH`, authentication, and network access.                                                    |
| Authentication impossible             | `` `claude doctor` ``                                                        | Verify authentication method; never publish tokens.                                                    |
| Classic SSH connection functional but fails from Claude Science | `` `ssh -v` `` from the same environment                                     | Verify the application's handling of the interactive session, terminal, and MFA challenge.             |
| A generated job requests too many resources | Review `#SBATCH` directives                                                 | Adjust resources before `` `sbatch` `` and validate program requirements.                              |

## Starting Prompts

The following examples can be used for controlled tests.

### Understand the Project

```
Read the project and explain:
1. the directory structure;
2. the main entry points;
3. the dependencies;
4. how the program is expected to run.
Do not modify files.
```

### Create a SLURM Script

```
Review this program and propose a Slurm script for an Alliance cluster.
Explain every #SBATCH directive before creating the file.
Do not submit the job.
```

### Analyze Logs

```
Read the most recent Slurm output and error files.
Identify the likely cause of failure.
Propose diagnostic steps before proposing modifications.
Do not modify files.
```

### HPC Review

```
Review this workflow for HPC best practices.
Check CPU, memory, GPU, walltime, filesystem usage and Slurm directives.
Explain any issue you find.
Do not change files and do not submit jobs.
```

## Frequently Asked Questions

### Can I launch Claude directly after an SSH connection to Narval?

A very light test can be performed to verify the installation. For prolonged use or use that may launch commands, request a SLURM allocation and use a compute node, subject to site policies and connectivity.

### Does Claude use cluster GPUs to generate its responses?

In standard use of Claude Code with an external model service, model generation does not occur on cluster GPUs. Cluster GPUs are used by user programs submitted via SLURM.

### Does a public SSH key replace Duo?

No. A public SSH key and MFA can correspond to distinct steps. Do not attempt to bypass Duo.

### Can I install Claude on an automation node?

Not on Calcul Québec automation nodes, according to the position communicated by Calcul Québec.

### Does the Alliance officially recommend Claude?

To date, no general recommendation for or against the use of AI agents has been established. This page is a technical guide and not an institutional endorsement of the product.

### Can I use Claude with sensitive data?

The Alliance's general computing resources are not designed for storing sensitive data. Consult [Data Protection, Privacy, and Confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md) and your institution's requirements before any use.

## See Also

*   AI Agents on Alliance Clusters
*   [Running Jobs](../../running-jobs/running_jobs.md)
*   [Best Practices for Job Submission](../../running-jobs/best_practices_for_job_submission.md)
*   [Data Protection, Privacy, and Confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md)
*   [Multifactor Authentication](../../getting-started/multifactor_authentication.md)
*   [Automation in the Context of Multifactor Authentication](../../getting-started/automation_in_the_context_of_multifactor_authentication.md)
*   [SSH](../../getting-started/ssh.md)

## External References

*   [Anthropic — Claude Code](https://docs.anthropic.com/en/docs/claude-code)
*   [Anthropic — Claude Code Security](https://docs.anthropic.com/en/docs/claude-code/security)