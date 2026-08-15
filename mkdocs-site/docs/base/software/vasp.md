---
title: "VASP"
slug: "vasp"
lang: "base"

source_wiki_title: "VASP"
source_hash: "c4f3e6f0012288bd62473a8f95deee74"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:36:15.130880+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "pseudopotential files"
  - "Slurm job script"
  - "SBATCH directives"
  - "lmpi/2021.9.0"
  - "HDF5"
  - "vasp/6.4.2"
  - "Wannier Function"
  - "6.2.1"
  - "VASP job script"
  - "whole-node scheduling"
  - "memory"
  - "GPU type p100"
  - "VASP version 6.4.2"
  - "hdf5/1.14.2"
  - "py4vasp"
  - "GPU benchmark"
  - "vasp_gpu_job.sh"
  - "VASP version 5.4.4"
  - "prebuilt VASP modules"
  - "VASP executable files"
  - "time"
  - "Trillium Quickstart"
  - "pseudopotentials"
  - "Included Libraries"
  - "5.4.4"
  - "6.3.0"
  - "vasp_gpu"
  - "VASP licensing"
  - "StdEnv/2020"
  - "VASP"
  - "memory requirement estimation"
  - "vasp_std"
  - "EasyBuild VASP recipes"
  - "gpu:p100"

questions:
  - "What are the licensing requirements and steps to request access to VASP for a research group?"
  - "How can a licensed user load and run the prebuilt VASP modules on the Fir, Nibi, and Trillium clusters?"
  - "Where are the VASP pseudopotential files located after loading the VASP module on Fir and Nibi?"
  - "How do I load the necessary modules (lmpi, hdf5, and VASP) for using Trillium?"
  - "Where are the VASP pseudopotential files located on the Fir and Nibi systems?"
  - "Where can I find the Trillium Quickstart page for general usage instructions?"
  - "What executable files are provided for each VASP version and calculation mode (standard NVT, NPT, gamma vs. non‑gamma, with or without CUDA support)?"
  - "How does the benchmark described for Vasp‑GPU illustrate the performance impact of using one or two GPUs, and what recommendation is given to users?"
  - "What are the essential directives and parameters shown in the example Slurm job scripts for running VASP on CPU‑only nodes and on GPU‑enabled nodes?"
  - "How can I request specific resources such as CPU cores, memory, and GPU type for a VASP job in the provided job script?"
  - "What are the steps to build and install a custom version of VASP using EasyBuild, including selecting the appropriate recipe and source files?"
  - "Which methods should I use to estimate the memory requirements for a VASP job, and how can I obtain accurate memory estimates from interactive or completed jobs?"
  - "What is the purpose of the `#SBATCH --gres=gpu:p100:1` directive in the provided VASP GPU job script?"
  - "How does the script specify the amount of memory and runtime allocated for the job?"
  - "Which section of the documentation should be consulted to select the appropriate executable for each VASP version?"
  - "Which VASP versions in the table are marked as CPU‑compatible and available for use?"
  - "What libraries (e.g., Wannier Function, HDF5, LibXC, ELPA, Libmbd, dft4) are included with each listed VASP version?"
  - "Where can users access the official VASP tutorial and the py4vasp Python interface mentioned in the external links?"
  - "Which VASP versions are provided for the StdEnv/2020 environment?"
  - "What are the exact package filenames (.tgz) associated with each listed VASP version?"
  - "Do all the listed VASP packages indicate CPU support and have both “yes” flags enabled?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

*The Vienna ab initio Simulation Package (VASP) is a computer program for atomic scale materials modelling, e.g. electronic structure calculations and quantum mechanical molecular dynamics, from first principles.
Reference: [VASP website](https://www.vasp.at/)

## Licensing
VASP can only be used by research groups that have been licensed by the developers, VASP Software GmbH. Your PI (principal investigator, professor) must register at the [VASP website](https://www.vasp.at/) and obtain a license.

Once you have a license, if you wish to use the prebuilt VASP binaries on [Fir](fir.md), [Nibi](../clusters/nibi.md), or [Trillium](../clusters/trillium.md), contact [Technical support](../support/technical_support.md) requesting access to VASP with the following information:
*   Include license holder (your PI) information:
    *   Name
    *   Email address
    *   Department and institution (university)
*   Include license information:
    *   Version of the VASP license (**VASP version 5 or version 6**)
    *   **License number**
    *   Provide an updated list of who is allowed to use your VASP license. For example, forward to us the most recent email from the VASP license administrator that contains the list of licensed users.

If you are licensed for version 6 you may also use version 5, but a version 5 license does not permit you to use version 6.

You may also choose to install VASP yourself, according to the terms of your license. See [Building VASP yourself](#building-vasp-yourself) below.

### Why?
VASP Software GmbH will only grant licenses to groups that are hired by a single legal entity, which is incompatible with the way we operate. We have tried to negotiate an agreement with the licensor which would let us install the software everywhere on our infrastructure, but without success. Please read the terms of your own license, as you are likely subject to the same restriction. This limits the support we can offer to users who need help installing the software.

Simon Fraser University, the University of Waterloo, and the University of Toronto own Fir, Nibi, and Trillium, respectively, and have licenses with VASP. Some of their employees are therefore allowed to install specific versions of VASP on those clusters and provide limited support.

## Using prebuilt VASP

To load prebuilt VASP on [Fir](fir.md) and [Nibi](../clusters/nibi.md), please do the following:

For **vasp/5.4.4**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load vasp/5.4.4
```
For **vasp/6.4.2**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load vasp/6.4.2
```
1.  Run `module spider vasp` to see which versions are available.
2.  Choose your version and run `module spider vasp/<version>` to see which dependencies you need to load for this particular version.
3.  Load the dependencies and the VASP module, for example:
    ```bash
    module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
    module load vasp/6.4.2
    ```
See [Using modules](../programming/modules.md) for more information.

To use VASP on [Trillium](../clusters/trillium.md), modules may be loaded as follows:

For **vasp/5.4.4**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0
module load imkl/2023.2.0
module use /opt/software/commercial/modules
module load vasp/5.4.4
```

For **vasp/6.4.2**
```bash
module load StdEnv/2023 intel/2023.2.1 intelmpi/2021.9.0 hdf5/1.14.2
module use /opt/software/commercial/modules
module load vasp/6.4.2
```

For **vasp/6.4.2-gpu** on the **Trillium GPU** subcluster
```bash
module load StdEnv/2023 nvhpc/25.1 cuda/12.6 nccl/2.26.2 imkl/2023.2.0 hdf5/1.14.5
module use /opt/software/commercial/modules
module load vasp/6.4.2-gpu
```

For general usage of Trillium, please see the [Trillium Quickstart](../clusters/trillium_quickstart.md) page.

### Pseudopotential files
All pseudopotentials have been downloaded from the official VASP website and untarred. They are all located in `$EBROOTVASP/pseudopotentials/` on Fir and Nibi and can be accessed once the VASP module is loaded.

### Executable programs

**For VASP-4.6**, executable files are:
*   `vasp` for standard NVT calculations with non gamma k points
*   `vasp-gamma` for standard NVT calculations with only gamma points
*   `makeparam` to estimate how much memory is required to run VASP for a particular cluster

**For VASP-5.4.1, 5.4.4 and 6.1.0 (without CUDA support)**, executable files are:
*   `vasp_std` for standard NVT calculations with non gamma k points
*   `vasp_gam` for standard NVT calculations with only gamma points
*   `vasp_ncl` for NPT calculations with non gamma k points

**For VASP-5.4.4 and 6.1.0 (with CUDA support)**, executable files are:
*   `vasp_gpu` for standard NVT calculations with gamma and non gamma k points
*   `vasp_gpu_ncl` for NPT calculations with gamma and non gamma k points

Two extensions have also been incorporated:
*   [Transition State Tools](http://theory.cm.utexas.edu/vtsttools/)
*   [VASPsol](https://github.com/henniggroup/VASPsol)

If you need a version of VASP that does not appear here, you can either build it yourself (see below) or [write to us](../support/technical_support.md) and ask that it be built and installed.

## Vasp-GPU
Vasp-GPU executable files run on both GPUs and CPUs of a node. Calculation on a GPU is generally more efficient than on a CPU, so it is highly recommended to perform a benchmark using one or two GPUs to ensure maximum performance. For instance, a benchmark of a Si crystal with 256 Si-atoms in the simulation box showed that using 1 or 2 GPUs with 1 CPU core improved performance by more than 5 times compared to using 0 GPUs with 1 CPU core. However, comparing calculations with 1 GPU versus 2 GPUs indicated minimal additional performance gain from the second GPU; monitoring showed its usage was around 50%. Users are therefore recommended to perform a similar benchmark for their specific system to optimize resource utilization and avoid wasting computational resources.

## Example of a VASP job script

The following is a job script to run VASP in parallel using the Slurm job scheduler:

```yaml
title: vasp_job.sh
language: sh
```
```bash
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --ntasks=4             # number of MPI processes
#SBATCH --mem-per-cpu=1024M    # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  intelmpi/2019.7.217 vasp/<VERSION>
mpirun <VASP>
```
*   The above job script requests four CPU cores and 4096MB memory (4x1024MB).
*   `<ACCOUNT>` is a Slurm account name; see [Accounts and projects](../running-jobs/running_jobs.md#accounts-and-projects) to know what to enter there.
*   `<VERSION>` is the number for the VASP version you want to use: 4.6, 5.4.1, 5.4.4 or 6.1.0.
*   Use `module spider vasp/<VERSION>` to see how you can change this particular version.
*   `<VASP>` is the name of the executable. Refer to section **Executable programs** above for the executables you can select for each version.

```yaml
title: vasp_gpu_job.sh
language: sh
```
```bash
#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --cpus-per-task=1      # number of CPU processes
#SBATCH --gres=gpu:p100:1      # Number of GPU type:p100 (valid type only for cedar)
#SBATCH --mem=3GB              # memory
#SBATCH --time=0-00:05         # time (DD-HH:MM)
module load intel/2020.1.217  cuda/11.0  openmpi/4.0.3 vasp/<VERSION>
mpirun <VASP>
```
*   The above job script requests one CPU core and 1024MB memory.
*   The above job script requests one GPU type p100 which is only available on Cedar. For other clusters, please see the [GPU types available](../running-jobs/using_gpus_with_slurm.md).
*   The above job uses `srun` to run VASP.

VASP uses four input files named as INCAR, KPOINTS, POSCAR, POTCAR. It is best to prepare VASP input files in a separate directory for each job. To submit the job from that directory, use:
```bash
sbatch vasp_job.sh
```

If you do not know how much memory you need for your job, prepare all your input files and then run `makeparam` in an [interactive job submission](../running-jobs/running_jobs.md#interactive-jobs). Then use the result as required memory for the next run. However, for a more accurate estimate for future jobs, check the maximum stack size used by [completed jobs](../running-jobs/running_jobs.md) and use this as the memory requirement per processor for the next job.

If you want to use 32 or more cores, please read about [whole-node scheduling](../running-jobs/job_scheduling_policies.md#whole-nodes-versus-cores).

## Building VASP yourself

If you are licensed to use VASP and have access to VASP source code, you can install various versions of VASP in your `/home` directory on all our clusters using the following [EasyBuild](../programming/easybuild.md) commands.

```bash
eb -f [RECIPE NAME] --sourcepath=[SOURCEPATH]
```

where `[SOURCEPATH]` is the directory containing the VASP source code and `[RECIPE NAME]` is the name of the recipe. The first table below shows the list of available recipes along with the corresponding required source files. In this table VTSTtools and vaspSOL are Transition State Tools and VASPsol extensions respectively. The second table shows the list of the libraries that are included with VASP. You may download the source code from the [VASP website](https://www.vasp.at/). Running the command will take some time, perhaps more than an hour. Once it is done, you will be able to load and run VASP using `module` commands just as explained above in [Using prebuilt VASP](#using-prebuilt-vasp).

Alternatively to build a custom version of VASP, please see [Installing software in your home directory](../getting-started/installing_software_in_your_home_directory.md) and [Installing VASP 5](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X) or [Installing VASP 6](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X).

### Recipe Specification and Implementation

| Recipe Name               | Version | Environment | Source file           | CPU/GPU | VTSTtools | vaspSOL |
| :------------------------ | :------ | :---------- | :-------------------- | :------ | :-------- | :------ |
| VASP-5.4.4-iimpi-2020a.eb | 5.4.4   | StdEnv/2020 | vasp.5.4.4.pl2.tgz    | CPU     | yes       | yes     |
| VASP-6.1.2-iimpi-2020a.eb | 6.1.2   | StdEnv/2020 | vasp.6.1.2_patched.tgz | CPU     | yes       | yes     |
| VASP-6.2.1-iimpi-2020a.eb | 6.2.1   | StdEnv/2020 | vasp.6.2.1.tgz        | CPU     | yes       | yes     |
| VASP-6.3.0-iimpi-2020a.eb | 6.3.0   | StdEnv/2020 | vasp.6.3.0.tgz        | CPU     | yes       | yes     |
| VASP-6.3.1-iimpi-2020a.eb | 6.3.1   | StdEnv/2020 | vasp.6.3.1.tgz        | CPU     | yes       | yes     |
| VASP-5.4.4-iimpi-2023a.eb | 5.4.4   | StdEnv/2023 | vasp.5.4.4.pl2.tgz    | CPU     | yes       | yes     |
| VASP-6.4.2-iimpi-2023a.eb | 6.4.2   | StdEnv/2023 | vasp.6.4.2.tar        | CPU     | yes       | yes     |
| VASP-6.4.3-iimpi-2023a.eb | 6.4.3   | StdEnv/2023 | vasp.6.4.3.tar        | CPU     | yes       | yes     |
| VASP-6.5.0-iimpi-2023a.eb | 6.5.0   | StdEnv/2023 | vasp.6.5.0.tgz        | CPU     | No        | No      |
| VASP-6.5.1-iimpi-2023a.eb | 6.5.1   | StdEnv/2023 | vasp.6.5.1.tgz        | CPU     | No        | No      |

### Included Libraries

| Recipe Name               | Wannier Function | Beef | HDF5 | LibXC | ELPA | Libmbd | dft4 |
| :------------------------ | :--------------- | :--- | :--- | :---- | :--- | :----- | :--- |
| VASP-5.4.4-iimpi-2020a.eb | Yes              | Yes  | No   | No    | No   | No     | No   |
| VASP-6.1.2-iimpi-2020a.eb | Yes              | Yes  | No   | No    | No   | No     | No   |
| VASP-6.2.1-iimpi-2020a.eb | Yes              | Yes  | No   | No    | No   | No     | No   |
| VASP-6.3.0-iimpi-2020a.eb | Yes              | Yes  | Yes  | Yes   | No   | No     | No   |
| VASP-6.3.1-iimpi-2020a.eb | Yes              | Yes  | Yes  | Yes   | No   | No     | No   |
| VASP-6.4.2-iimpi-2023a.eb | Yes              | Yes  | Yes  | Yes   | No   | No     | No   |
| VASP-6.4.3-iimpi-2023a.eb | Yes              | Yes  | Yes  | Yes   | No   | No     | Yes  |
| VASP-6.5.0-iimpi-2023a.eb | Yes              | Yes  | Yes  | Yes   | Yes  | Yes    | Yes  |
| VASP-6.5.1-iimpi-2023a.eb | Yes              | Yes  | Yes  | Yes   | Yes  | Yes    | Yes  |

## External links

*   [Getting Started](https://www.vasp.at/tutorials/latest/part1/) guide from the developers' Web site.
*   [py4vasp](https://www.vasp.at/py4vasp/latest/) is a Python interface to extract data from VASP calculations.