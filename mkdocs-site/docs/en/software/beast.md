---
title: "BEAST/en"
slug: "beast"
lang: "en"

source_wiki_title: "BEAST/en"
source_hash: "f76fa6089004d0af667a2201667cb985"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:40:44.846582+00:00"

tags:
  - software

keywords:
  - "Bayesian MCMC analysis"
  - "package manager"
  - "Jobscript"
  - "Bash script"
  - "beagle-lib"
  - "Memory"
  - "SBATCH"
  - "SLURM"
  - "phylogenies"
  - "BEAGLE library"
  - "Java command"
  - "BEAST"
  - "BEAST packages"

questions:
  - "What is the primary purpose of the BEAST software and what analytical methods does it utilize for molecular sequence analysis?"
  - "How do users install and manage additional packages or add-ons across different versions of the BEAST software?"
  - "What are the required commands and dependencies for loading and executing a BEAST job script in a cluster environment?"
  - "How are the Slurm cluster resources, such as execution time and memory limits, configured for this job?"
  - "What is the required relationship between the Slurm memory allocation and the Java virtual machine memory defined in the script?"
  - "Which software modules and external libraries are loaded to construct and execute the final BEAST Java command?"
  - "Where can users find more information on managing BEAST packages for server machines?"
  - "What are the necessary SLURM directives and commands to execute a simple BEAST jobscript?"
  - "How is a jobscript configured differently when running BEAST with higher memory requirements?"
  - "How are the Slurm cluster resources, such as execution time and memory limits, configured for this job?"
  - "What is the required relationship between the Slurm memory allocation and the Java virtual machine memory defined in the script?"
  - "Which software modules and external libraries are loaded to construct and execute the final BEAST Java command?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Description

BEAST ([BEAST2 Homepage](http://beast2.org/)) is a cross-platform program for Bayesian MCMC analysis of molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability.

BEAST can use the beagle-lib ([Beagle-lib Homepage](https://github.com/beagle-dev/beagle-lib)), which is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages.

## Usage

Loading the BEAST module with: `module load beast`, will automatically load its dependencies, namely the `beagle-lib` and `java` modules, and set the environment variable `EBROOTBEAST` to point to the directory where BEAST's program files are located.

### Managing BEAST Packages/Add-ons

BEAST has been installed without any packages (add-ons). You can use the `packagemanager` command (for BEAST v2.5.1 and newer; in older versions of BEAST, the command is `addonmanager`) to install the desired packages within your home directory.

=== "BEAST ≥ 2.5.x"

```bash
$ module load beast/2.5.1
$ packagemanager -list
```

| Name    | Installation Status | Latest Version | Dependencies | Description                       |
| :------ | :------------------ | :------------- | :----------- | :-------------------------------- |
| BEAST   | 2.5.1               | 2.5.0          |              | BEAST core                        |
| bacter  | NA                  | 2.2.0          |              | Bacterial ARG inference.          |
| BADTRIP | NA                  | 1.0.0          |              | Infer transmission time for [...] |
| [...]   |                     |                |              |                                   |
| SNAPP   | NA                  | 1.4.1          |              | SNP and AFLP Phylogenies          |
| [...]   |                     |                |              |                                   |

```bash
$ packagemanager -add SNAPP
```

Package SNAPP is installed in `~/.beast/2.5/SNAPP`.

```bash
$ packagemanager -list
```

| Name    | Installation Status | Latest Version | Dependencies | Description                |
| :------ | :------------------ | :------------- | :----------- | :------------------------- |
| BEAST   | 2.5.1               | 2.5.0          |              | BEAST core                 |
| [...]   |                     |                |              |                            |
| SNAPP   | 1.4.1               | 1.4.1          |              | SNP and AFLP Phylogenies   |
| [...]   |                     |                |              |                            |

=== "BEAST ≤ 2.4.x"

```bash
$ module load beast/2.4.0
$ addonmanager -list
```

| Name    | Installation Status | Latest Version | Dependencies | Description                             |
| :------ | :------------------ | :------------- | :----------- | :-------------------------------------- |
| BEAST   | 2.4.0               | 2.4.8          |              | BEAST core                              |
| bacter  | not installed       | 1.2.3          |              | Bacterial ARG inference.                |
| BASTA   | not installed       | 2.3.2          |              | Bayesian structured coalescent approximation |
| [...]   |                     |                |              |                                         |
| SNAPP   | not installed       | 1.3.0          |              | SNP and AFLP Phylogenies                |
| [...]   |                     |                |              |                                         |

```bash
$ addonmanager -add SNAPP
```

Package SNAPP is installed in `~/.beast/2.4/SNAPP`.

```bash
$ addonmanager -list
```

| Name    | Installation Status | Latest Version | Dependencies | Description                 |
| :------ | :------------------ | :------------- | :----------- | :-------------------------- |
| BEAST   | 2.4.0               | 2.4.8          |              | BEAST core                  |
| [...]   |                     |                |              |                             |
| SNAPP   | 1.3.0               | 1.3.0          |              | SNP and AFLP Phylogenies    |
| [...]   |                     |                |              |                             |

For more information on how to manage BEAST packages, please read the section "Server machines" at: [http://www.beast2.org/managing-packages/](http://www.beast2.org/managing-packages/).

### Simple Jobscript for BEAST

```bash linenums="1" hl_lines="2-4" title="simple_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=2000M

module load beast/2.6.3

beast input_beast.xml
```

### Jobscript for BEAST with more Memory

!!! warning
    The `BEAST_MEM` value in the script should be approximately 250M lower than the `--mem-per-cpu` allocated by Slurm.

```bash linenums="1" hl_lines="2-4 8" title="high_memory_beast_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=3:00:00
#SBATCH --mem-per-cpu=4000M

# Increase Maximum memory here if necessary:
# "BEAST_MEM" needs to be 250M lower than "--mem="
BEAST_MEM="-Xmx3750M"

module load beast/2.6.3

# Define variables where to find BEAST and BEAGLE-lib
BEAST_LIB="${EBROOTBEAST}/lib"
BEAST_EXTRA_LIBS="${BEAST_LIB}:${BEAGLE_LIB}"
export LD_LIBRARY_PATH="${BEAGLE_LIB}:${LD_LIBRARY_PATH}"

# Build a long java command:
CMD="java -Xms256m ${BEAST_MEM}"                                           # set memory
CMD="$CMD -Djava.library.path=${BEAST_EXTRA_LIBS}"                         # point to libraries
CMD="$CMD -cp ${BEAST_LIB}/launcher.jar beast.app.beastapp.BeastLauncher" # which program to execute

echo ".................................."
echo "The Java command is \"${CMD}\""
echo ".................................."

# Run the command:
$CMD -beagle  input_beast.xml
```

## References

*   [BEAST2 Homepage](http://beast2.org/)
*   [Beagle-lib Homepage](https://github.com/beagle-dev/beagle-lib)