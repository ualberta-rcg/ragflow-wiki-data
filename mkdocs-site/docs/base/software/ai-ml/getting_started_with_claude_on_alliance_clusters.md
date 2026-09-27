---
title: "Getting started with Claude on Alliance clusters"
slug: "getting_started_with_claude_on_alliance_clusters"
lang: "base"

source_wiki_title: "Getting started with Claude on Alliance clusters"
source_hash: "cd6491322069f83031607e256afb2bdf"
last_synced: "2026-09-27T01:10:57.242992+00:00"
last_processed: "2026-09-27T01:54:52.815013+00:00"

tags:
  - ai-and-machine-learning
  - software
  - running-jobs

keywords:
  - "job monitoring with squeue"
  - "Claude Science"
  - "Claude"
  - "automation node"
  - "salloc command"
  - "Claude scientific workflow"
  - "sbatch script"
  - "connection issue"
  - "installation"
  - "authentication"
  - "HPC best practices"
  - "ssh -v"
  - "embedded SSH client"
  - "Slurm output error files"
  - "SLURM allocation"
  - "standard SSH"
  - "SLURM script"
  - "diagnostic steps"
  - "Claude Code"
  - "Alliance clusters"
  - "Duo MFA"
  - "SLURM"
  - "#SBATCH directive"

questions:
  - "What preparatory checks and policies should be verified before installing and using Claude Code on an Alliance cluster?"
  - "How can Claude Code be installed (natively or via npm) on a shared cluster, and which commands confirm a successful installation?"
  - "Which authentication options are available for Claude Code, and what is the recommended login workflow for cluster environments?"
  - "What are the required commands to request a SLURM allocation, open an interactive shell, and launch Claude within a project directory?"
  - "How should a SLURM batch script be created, reviewed, and submitted to run a Python program such as hello_cluster.py, including resource specifications and log handling?"
  - "What best‑practice guidelines are given for limiting Claude’s access to project files, monitoring job execution, and troubleshooting SSH connections with Duo MFA?"
  - "What #SBATCH directives are required for the Alliance cluster script, and what does each directive do?"
  - "What does the latest Slurm output and error indicate as the likely cause of failure, and which diagnostic steps should be taken before any modifications?"
  - "Which elements of the workflow (CPU, memory, GPU, walltime, filesystem usage, Slurm directives) violate HPC best‑practice guidelines, and how should they be corrected?"
  - "What diagnostic steps should be performed to investigate why the Duo MFA prompt is not displayed when Claude Science connects to the Alliance resource?"
  - "How can you determine whether Claude Science is using an embedded SSH client versus the system ssh command during the connection attempt?"
  - "Which specific details from the ssh ‑v output should be captured (while omitting any secret information) to help identify the cause of the connection behavior?"
  - "Why does Claude fail to start when standard SSH works but the application integration does not present the Duo MFA challenge?"
  - "What are the recommended methods for running Claude on the cluster, given that it cannot be installed on automation nodes?"
  - "Which troubleshooting steps should be followed for common Claude issues such as “command not found,” authentication failures, or excessive resource requests?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

**Claude Code** is a command-line coding agent developed by Anthropic. It can read and explain code, modify files, run shell commands, prepare SLURM scripts, analyse logs, and support debugging.

This page describes the installation and use of Claude Code in the context of Alliance clusters. For general principles that apply to all AI agents including execution location, SLURM, security, data, permissions, and MFA (see [Using AI Agents](using_ai_agents.md)).

**Terminology:** The term “Claude” on this page refers to Claude Code or an environment built on top of Claude Code. An interface such as “Claude Science” may wrap Claude Code, but its SSH connection or authentication mechanism may differ.

## Before you begin

Before using Claude on a cluster:

*   determine where the Claude client will run;
*   avoid prolonged use on a login node;
*   use SLURM for computational workloads;
*   verify the data policy applicable to the project;
*   verify that the required network connectivity is available;
*   maintain human oversight of proposed commands and modifications.

For interactive use on the cluster, a SLURM allocation is the preferred technical architecture when local policies and connectivity allow it.

## Installing Claude Code

Before installing Claude, check whether the executable is already available:

```bash
which claude
claude --version
```

### Native installation

[Anthropic documentation recommends native installation on Linux](https://code.claude.com/docs/en/setup). In an environment where external downloads are permitted:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

The launcher is generally installed in user space. If needed, add the corresponding directory to `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
claude --version
claude doctor
```

!!! note
    **Check locally:** outbound network and software installation policies may differ between systems. Do not use `sudo` to bypass permissions on a shared cluster.

### Installation with npm

Installation with npm is also possible. First verify the available versions:

```bash
node --version
npm --version
```

Then install the package in an appropriate user-space location:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

Do not use `sudo npm install -g` on a shared cluster.

### Verifying the installation

The following commands can be used to verify the installation:

```bash
claude --version
claude doctor
```

`claude doctor` provides read-only diagnostics about the installation and configuration.

## Authentication and network connectivity

Claude Code must authenticate with the configured model service. Depending on the environment, authentication may use an authorized Claude account, the Anthropic Console/API, or an infrastructure provider supported by the organization.

On first launch:

```bash
claude
```

Claude Code can be used with your Claude subscription or billed based on API usage through your Console account.

**Select login method:**
1.  **Claude account with subscription** · Pro, Max, Team, or Enterprise
2.  **Anthropic Console account** · API usage billing
3.  **3rd-party platform** · Amazon Bedrock, Microsoft Foundry, or Vertex AI

The client normally opens the appropriate sign-in flow.

Claude Code also requires network connectivity to the configured service. The executable may therefore work in one environment while the session fails in another if outbound network rules differ.

!!! tip
    **The easiest login method on clusters:** Select option 2, **Anthropic Console account**, and sign in with your Console account. This option uses usage-based API billing. After signing in through your browser, you may be prompted to copy a temporary authorization code and paste it into the terminal to complete authentication. Once authentication succeeds, Claude Code is ready to use. Start with a simple prompt about your current folder, such as: “Describe the files and subdirectories in this folder.”

## Starter prompts

The following examples can be used for controlled tests.

### Understand the project

```bash
Read the project and explain:
1. the directory structure;
2. the main entry points;
3. the dependencies;
4. how the program is expected to run.
Do not modify files.
```

### Create a SLURM script

```bash
Review this program and propose a Slurm script for an Alliance cluster.
Explain every #SBATCH directive before creating the file.
Do not submit the job.
```

### Analyse logs

```bash
Read the most recent Slurm output and error files.
Identify the likely cause of failure.
Propose diagnostic steps before proposing modifications.
Do not modify files.
```

### HPC review

```bash
Review this workflow for HPC best practices.
Check CPU, memory, GPU, walltime, filesystem usage and Slurm directives.
Explain any issue you find.
Do not change files and do not submit jobs.
```

## Run Claude in an interactive execution with SLURM (Optional)

First request an allocation:

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

Then move to the project directory and launch Claude:

```bash
cd /path/to/project
claude
```

Exit Claude and the allocation when they are no longer needed. Check active jobs with:

```bash
squeue -u "$USER"
```

## Example test on a cluster

The following example illustrates a controlled test. It can be adapted to another cluster.

### Project structure

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

### Explore the project without modifying it

Example prompt:

```bash
Read the current project.
Explain the directory structure.
Do not modify any file.
```

### Create a small Python program

Example prompt:

```bash
Create a Python program called hello_cluster.py.

The program should:
- print the hostname
- print the current date
- print the Python version

Explain the code before creating it.
```

Example program:

```python title="hello_cluster.py"
import platform
import socket
from datetime import datetime

print("Hostname:", socket.gethostname())
print("Date:", datetime.now())
print("Python:", platform.python_version())
```

### Prepare a SLURM script

Example prompt:

```bash
Create a Slurm script to execute hello_cluster.py.

Requirements:
- 1 CPU
- 1 GB RAM
- execution time: 5 minutes
- save logs in logs/

Explain the script before creating it.
```

Example script:

```bash title="run_hello.sh"
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

### Submit and monitor the job

After manually reviewing the script:

```bash
sbatch scripts/run_hello.sh
squeue -u "$USER"
sacct -j <jobid> --format=JobID,JobName,State,Elapsed,AllocCPUS,ReqMem,MaxRSS,ExitCode
```

### Analyse the results

Example prompt:

```bash
Read the newest Slurm output.
Explain whether the execution succeeded.
Identify errors, if any.
Do not modify any files.
```

!!! note
    **Principle:** Claude can accelerate development and analysis, but it does not replace scientific validation, code review, or understanding of the requested resources.

## Claude and batch jobs

For a long, reproducible, or computationally expensive experiment, Claude's role should remain focused on preparation, review, and analysis. Scientific execution remains managed by SLURM.

1.  Ask Claude to read the program and estimate the required resources.
2.  Have Claude generate a SLURM script and review every `#SBATCH` directive.
3.  Submit the job with `sbatch` after human validation.
4.  Use `squeue` and `sacct` to monitor execution.
5.  Ask Claude to analyse logs and results, then independently validate the scientific conclusion.

## Restricting Claude's access to the project

Before launching Claude, check the directory permissions:

```bash
ls -ld /path/to/project
ls -l /path/to/project
```

Then move into the smallest directory required:

```bash
cd /project/<account>/my_project
claude
```

In its manual mode, Claude Code uses a permission model in which write operations and many commands require user approval. The user remains responsible for the safety of the commands and code they approve.

## Claude Science, SSH, and Duo MFA

A support case showed a situation in which SSH worked normally from a terminal using a public key, while a connection initiated by Claude Science to an Alliance resource did not correctly present the Duo MFA step.

To diagnose this type of issue, run the test from the same environment as Claude Science:

```bash
ssh -v <username>@narval.alliancecan.ca
```

Then verify:

*   whether Claude Science uses an embedded SSH client or the system `ssh` command;
*   the operating system and Claude version;
*   whether the connection waits indefinitely or exits immediately;
*   the relevant part of the `ssh -v` output, without sharing secrets.

If standard SSH works but the application integration does not present the Duo challenge, the problem is likely related to how the application handles the interactive SSH session or terminal rather than to the Alliance account itself.

An SSH public key and Duo MFA correspond to distinct authentication steps. Duo should not be bypassed.

## Automation nodes

Automation nodes are intended for deterministic platforms fully controlled by the user. Claude, as an AI agent, does not meet this definition.

Claude should therefore not be requested as a persistent service on an automation node.

Preferred options are:

*   Claude on a local workstation or VM, connecting to the cluster through supported mechanisms;
*   Claude inside an interactive SLURM allocation for interactive tests when permitted;
*   SLURM batch jobs for reproducible or computationally expensive workloads.

## Troubleshooting

| Symptom | Check | Action |
| :------ | :---- | :----- |
| `claude: command not found` | `which claude` and `echo $PATH` | Check the user-space installation and the `~/.local/bin` directory. |
| Claude works in one environment but not another | `claude --version`, `claude doctor`, environment variables, and network connectivity | Compare `PATH`, authentication, and network access. |
| Authentication fails | `claude doctor` | Check the authentication method; never publish tokens. |
| Standard SSH works but Claude Science fails | `ssh -v` from the same environment | Check how the application handles the interactive session, terminal, and MFA challenge. |
| A generated job requests too many resources | Review the `#SBATCH` directives | Adjust resources before `sbatch` and validate the program's requirements. |

## Frequently asked questions

### Can I launch Claude directly after connecting to Narval with SSH?

A very lightweight test can be performed to verify the installation. For prolonged use or use that may execute commands, request a SLURM allocation and use a compute node, subject to site policies and connectivity.

### Does Claude use the cluster GPUs to generate its responses?

In the standard use of Claude Code with an external model service, model inference is not performed on the cluster GPUs. Cluster GPUs are used by user programs submitted through SLURM.

### Does an SSH public key replace Duo?

No. An SSH public key and MFA may correspond to separate authentication steps. Duo should not be bypassed.

### Can I install Claude on an automation node?

Not on Calcul Québec automation nodes, according to the position communicated by Calcul Québec.

### Does the Alliance officially recommend Claude?

To date, no general recommendation for or against the use of AI agents has been established. This page is a technical guide and not an institutional endorsement of the product.

### Can I use Claude with sensitive data?

Alliance general-purpose computing resources are not designed for storing sensitive data. Consult [Data protection, privacy, and confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md) and your institution's requirements before use.

## See also

*   [Using AI Agents](using_ai_agents.md)
*   [Running jobs](../../running-jobs/running_jobs.md)
*   [Best practices for job submission](../../running-jobs/best_practices_for_job_submission.md)
*   [Data protection, privacy, and confidentiality](../../storage-and-data/data_protection__privacy__and_confidentiality.md)
*   [Multifactor authentication](../../getting-started/multifactor_authentication.md)
*   [Automation in the context of multifactor authentication](../../getting-started/automation_in_the_context_of_multifactor_authentication.md)
*   [SSH](../../getting-started/ssh.md)

## External references

*   [Anthropic — Claude Code](https://docs.anthropic.com/en/docs/claude-code)
*   [Anthropic — Claude Code security](https://docs.anthropic.com/en/docs/claude-code/security)