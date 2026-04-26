---
title: "VASP/en"
slug: "vasp"
lang: "en"

source_wiki_title: "VASP/en"
source_hash: "e6fbc39c0b4c66ba7c5b4cdfa73d65ea"
last_synced: "2026-04-25T23:42:08.699101+00:00"
last_processed: "2026-04-26T00:24:26.294284+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "EasyBuild"
  - "iimpi-2023a"
  - "VASP license"
  - "gamma points"
  - "GPU type p100"
  - "benchmark"
  - "job submission"
  - "source code"
  - "StdEnv/2023"
  - "pseudopotential files"
  - "Included Libraries"
  - "executable programs"
  - "CPU"
  - "py4vasp"
  - "Vasp-GPU"
  - "Cedar"
  - "NVT calculations"
  - "input files"
  - "prebuilt VASP binaries"
  - "Vienna ab initio Simulation Package"
  - "software versions"
  - "Slurm job script"
  - "pseudopotentials"
  - "Software"
  - "executable files"
  - "CPU core and memory"
  - "VASP"
  - "Computational Chemistry"

questions:
  - "What specific information and steps are required for a research group to obtain access to the prebuilt VASP binaries on the clusters?"
  - "Why is the global installation and support of VASP restricted across the computing infrastructure?"
  - "How do users load the appropriate modules and access pseudopotential files to run specific versions of VASP on clusters like Fir, Nibi, and Trillium?"
  - "How can users access the downloaded VASP pseudopotentials on the Cedar and Graham clusters?"
  - "What is the specific use case for the standard `vasp` executable in VASP-4.6?"
  - "When should a user run the `vasp-gamma` executable instead of the standard one?"
  - "What are the specific purposes of the different VASP executable files provided for versions with and without CUDA support?"
  - "Why does the documentation strongly recommend performing a benchmark before scaling VASP calculations across multiple GPUs?"
  - "How do the Slurm job script configurations differ when setting up a VASP job for a CPU-only run versus a GPU-accelerated run?"
  - "What are the four essential input files required to run a VASP job?"
  - "How can a user estimate the required memory for their VASP jobs if they are unsure?"
  - "What is the process for building and installing VASP from source in a user's home directory using EasyBuild?"
  - "What specific CPU, memory, and GPU resources are requested by the job script described in the text?"
  - "Which software modules and versions must be loaded into the environment before running VASP?"
  - "On which specific cluster is the p100 GPU available, and what commands are mentioned for executing the VASP application?"
  - "Which specific libraries are included in the VASP 6.5.0 and 6.5.1 versions that are not present in earlier versions?"
  - "Starting from which VASP version are the HDF5 and LibXC libraries first included in the build?"
  - "What is the purpose of the py4vasp tool mentioned in the external links section?"
  - "What versions of the VASP software are included in this list?"
  - "What standard environment and hardware architecture are targeted for these builds?"
  - "Which specific VASP version is marked with \"No\" for its configuration flags compared to the others?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*The Vienna *ab initio* Simulation Package (VASP) is a computer program for atomic-scale materials modelling, e.g., electronic structure calculations and quantum mechanical molecular dynamics, from first principles.*
Reference: [VASP website](https://www.vasp.at/)

## Licensing

VASP can only be used by research groups that have been licenced by the developers, VASP Software GmbH. Your PI (principal investigator, professor) must register at the [VASP website](https://www.vasp.at/) and obtain a licence.

Once you have a licence, if you wish to use the prebuilt VASP binaries on [Fir](fir.md), [Nibi](../clusters/nibi.md), or [Trillium](../clusters/trillium.md), contact [Technical support](../support/technical_support.md) requesting access to VASP with the following information:
*   Include licence holder (your PI) information:
    *   Name
    *   Email address
    *   Department and institution (university)
*   Include licence information:
    *   Version of the VASP licence (**VASP version 4 or version 5**)
    *   **Licence number**
    *   Provide an updated list of who is allowed to use your VASP licence. For example, forward to us the most recent email from the VASP licence administrator that contains the list of licenced users.

If you are licenced for version 5, you may also use version 4, but a version 4 licence does not permit you to use version 5. The same applies for version 6; if you are licenced for version 6, you may also use versions 5 and 4.

You may also choose to install VASP yourself, according to the terms of your licence. See [Building VASP yourself](#building-vasp-yourself) below.

### Why?

VASP Software GmbH will only grant licences to groups that are employed by a single legal entity, which is incompatible with our operational model. We have tried to negotiate an agreement with the licensor which would let us install the software everywhere on our infrastructure, but without success. Please read the terms of your own licence, as you are likely subject to the same restriction. This limits the support we can offer to users who need help installing the software.

Simon Fraser University, the University of Waterloo, and the University of Toronto own Fir, Nibi, and Trillium, respectively, and have licences with VASP. Some of their employees are therefore allowed to install specific versions of VASP on those clusters and provide limited support.

## Using Prebuilt VASP

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
For general usage of Trillium, please see the [Trillium Quickstart](../clusters/trillium_quickstart.md) page.

### Pseudopotential Files

All pseudopotentials have been downloaded from the official VASP website and untarred. They are all located in `$EBROOTVASP/pseudopotentials/` on Cedar and Graham and can be accessed once the VASP module is loaded.

### Executable Programs

**For VASP-4.6**, executable files are:
*   `vasp` for standard NVT calculations with non-gamma k-points
*   `vasp-gamma` for standard NVT calculations with only gamma points
*   `makeparam` to estimate how much memory is required to run VASP for a particular cluster

**For VASP-5.4.1, 5.4.4 and 6.1.0 (without CUDA support)**, executable files are:
*   `vasp_std` for standard NVT calculations with non-gamma k-points
*   `vasp_gam` for standard NVT calculations with only gamma points
*   `vasp_ncl` for NPT calculations with non-gamma k-points

**For VASP-5.4.4 and 6.1.0 (with CUDA support)**, executable files are:
*   `vasp_gpu` for standard NVT calculations with gamma and non-gamma k-points
*   `vasp_gpu_ncl` for NPT calculations with gamma and non-gamma k-points

Two extensions have also been incorporated:
*   [Transition State Tools](http://theory.cm.utexas.edu/vtsttools/)
*   [VASPsol](https://github.com/henniggroup/VASPsol)

If you need a version of VASP that does not appear here, you can either build it yourself (see below) or [write to us](../support/technical_support.md) and ask that it be built and installed.

## VASP-GPU

VASP-GPU executable files run on both GPUs and CPUs of a node. Fundamentally, GPU-based calculations are significantly more resource-intensive than CPU-based calculations; therefore, we highly recommend performing a benchmark using one or two GPUs to ensure maximum performance. A benchmark of a Si crystal containing 256 Si-atoms in the simulation box showed the following: performance for GPU=1,2 and CPU=1 was more than 5 times better compared to GPU=0 and CPU=1. However, a comparison of calculations with GPU=1 and GPU=2 indicated that there was not much performance gain from GPU=1 to GPU=2. In fact, GPU utilization for GPU=2 was around 50% in our monitoring system. Therefore, we recommend users to first perform a benchmark like this for their own system to ensure they are not wasting any computer resources.

## Example of a VASP Job Script

The following is a job script to run VASP in parallel using the Slurm job scheduler:

```bash title="vasp_job.sh"
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
*   `<VASP>` is the name of the executable. Refer to section *Executable programs* above for the executables you can select for each version.

```bash title="vasp_gpu_job.sh"
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

## Building VASP Yourself

If you are licenced to use VASP and have access to VASP source code, you can install various versions of VASP in your `/home` directory on all our clusters using the following [EasyBuild](../programming/easybuild.md) commands.

`` `eb -f [RECIPE NAME] --sourcepath=[SOURCEPATH]` ``

where `[SOURCEPATH]` is the directory containing the VASP source code and `[RECIPE NAME]` is the name of the recipe. The first tab of the table below shows the list of available recipes along with the corresponding required source files. In this table, VTSTtools and VASPsol are Transition State Tools and VASPsol extensions respectively. The second tab of this table shows the list of the libraries that are included in VASP. You may download the source code from the [VASP website](https://www.vasp.at/). Running the command will take some time, perhaps more than an hour. Once it is done, you will be able to load and run VASP using `module` commands just as explained above in [Using Prebuilt VASP](#using-prebuilt-vasp).

Alternatively, to build a custom version of VASP, please see [Installing software in your home directory](../getting-started/installing_software_in_your_home_directory.md) and [Installing VASP 5](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X) or [Installing VASP 6](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X).

=== "Recipe Specification and Implementation"

| Recipe Name               | Version | Environment | Source file          | CPU/GPU | VTSTtools | VASPsol |
| :------------------------ | :------ | :---------- | :------------------- | :------ | :-------- | :------ |
| VASP-5.4.4-iimpi-2020a.eb | 5.4.4   | StdEnv/2020 | vasp.5.4.4.pl2.tgz   | CPU     | yes       | yes     |
| VASP-6.1.2-iimpi-2020a.eb | 6.1.2   | StdEnv/2020 | vasp.6.1.2_patched.tgz | CPU     | yes       | yes     |
| VASP-6.2.1-iimpi-2020a.eb | 6.2.1   | StdEnv/2020 | vasp.6.2.1.tgz       | CPU     | yes       | yes     |
| VASP-6.3.0-iimpi-2020a.eb | 6.3.0   | StdEnv/2020 | vasp.6.3.0.tgz       | CPU     | yes       | yes     |
| VASP-6.3.1-iimpi-2020a.eb | 6.3.1   | StdEnv/2020 | vasp.6.3.1.tgz       | CPU     | yes       | yes     |
| VASP-5.4.4-iimpi-2023a.eb | 5.4.4   | StdEnv/2023 | vasp.5.4.4.pl2.tgz   | CPU     | yes       | yes     |
| VASP-6.4.2-iimpi-2023a.eb | 6.4.2   | StdEnv/2023 | vasp.6.4.2.tar       | CPU     | yes       | yes     |
| VASP-6.4.3-iimpi-2023a.eb | 6.4.3   | StdEnv/2023 | vasp.6.4.3.tar       | CPU     | yes       | yes     |
| VASP-6.5.0-iimpi-2023a.eb | 6.5.0   | StdEnv/2023 | vasp.6.5.0.tgz       | CPU     | No        | No      |
| VASP-6.5.1-iimpi-2023a.eb | 6.5.1   | StdEnv/2023 | vasp.6.5.1.tgz       | CPU     | No        | No      |

=== "Included Libraries"

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

## External Links

*   [Getting Started](https://www.vasp.at/tutorials/latest/part1/) guide from the developers' website.
*   [py4vasp](https://www.vasp.at/py4vasp/latest/) is a Python interface to extract data from VASP calculations.