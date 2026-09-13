---
title: "GRRM"
slug: "grrm"
lang: "base"

source_wiki_title: "GRRM"
source_hash: "b94e541e2cab4fe9e15c217f51015ae3"
last_synced: "2026-09-13T00:40:43.713374+00:00"
last_processed: "2026-09-13T01:32:48.420189+00:00"

tags:
  - software

keywords:
  - "GRRM23"
  - "environment variables"
  - "Gaussian G16"
  - "export LD_LIBRARY_PATH"
  - "checkpoint file"
  - "STLM_SERVER_ADDRESS"
  - "GRRMroot"
  - "Slurm script"
  - "HPC SYSTEMS Inc."
  - "floating license"
  - "STLM_SERVER_PORT"
  - "Intel MPI"
  - "installation script"
  - "license policies"

questions:
  - "What is the primary function of the GRRM23 program and which quantum‑chemistry packages can it interface with?"
  - "How does the floating‑license system for GRRM23 operate, and what options are available for setting up a license server?"
  - "What are the essential steps and environment‑variable settings required to install and run GRRM23 after obtaining a license?"
  - "How should the environment variables be defined and the .bashrc file be sourced before running GRRM23?"
  - "What are the required directives and commands in a SLURM script to execute a single‑node GRRM23 job using Gaussian 16?"
  - "Why is GRRM23 limited to a single compute node when it is used together with Gaussian 16?"
  - "What values should replace the placeholders XXX in STLM_SERVER_ADDRESS and STLM_SERVER_PORT for the license configuration?"
  - "How does a user obtain the correct server address and port information from HPC SYSTEMS Inc.?"
  - "Which environment variables are set by the script (PATH, LD_LIBRARY_PATH, GRRMroot) and what purpose does each serve?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The global reaction route mapping [GRRM®](https://global.hpc.co.jp/products/grrm23/) program is a commercial software developed for the analysis of chemical reaction pathways. This program is capable of exhaustively exploring the potential energy surface of a collection of atoms, automatically finding molecular geometries of reactants, transition states, and products. GRRM23 works in conjunction with quantum chemistry software such as, but not limited to, Gaussian 16.

## License Agreement
To obtain a license (and pricing), please submit a request at <https://global.hpc.co.jp/contact/>. Alternatively, contact [Kenshiro Kimura](mailto:ke-kimura@hpc.co.jp) for GRRM23 application instructions. GRRM23 uses a floating license approach for validating users; it requires the setup of a license server. For this, HPC SYSTEMS Inc., the company that sells GRRM23, allows users to connect to license servers at their company site in Japan at no additional costs. Alternatively, a license server can be set up at the user’s university in Canada; for this option, please contact technical support at HPC SYSTEMS Inc.

## Installation Instructions
After buying a license, users will receive a link and instructions to download a compressed `tar.bz2` file. Download the file and follow the instructions below (substitute the path to your actual home directory where `/home/user` is mentioned).

In your home directory, create a directory for the installation and another one for the executables:

```bash
mkdir GRRM23_Installation
mkdir GRRM23_RUN
```

Move the compressed GRRM23 file to `$HOME/GRRM23_Installation` and extract it there:

```bash
cd GRRM23_Installation
tar xjf GRRM23.tar.bz2
```

The extraction of the `tar.bz2` should generate an installation script (`install.sh`); from `/home/user/GRRM23_Installation`, execute the script as follows:

```bash
./install.sh /home/user/GRRM23_RUN
```

The installation will display the following configuration summary:

```console
Installation configuration:
GRRMroot = /home/user/GRRM23_RUN
Intel MPI installation prefix = /home/user/GRRM23_RUN/mpi-rt
Are you sure to start installation? [Y/n]
```

Type “Y” and press “Enter” to proceed with the installation. Once the installation is finished, a “GRRM INSTALLATION DONE” message should appear:

```console
Installing Intel MPI ... done successfully.
Installing GRRM binary ...done successfully.
Installing STLib ...done successfully.

GRRM INSTALLATION DONE.
IMPORTANT[1]: Before using GRRM, please insert lines below to your shell (/bin/bash) configuration file.
IMPORTANT[2]: Please consult your system administrator about the STLM server IP address and port number.

source /home/user/GRRM23_RUN/mpi-rt/mpi/2021.6.0/env/vars.sh
export PATH="/home/user/GRRM23_RUN:${PATH}"
export LD_LIBRARY_PATH="/home/user/GRRM23_RUN:${LD_LIBRARY_PATH}"
export GRRMroot="/home/user/GRRM23_RUN"
export subgrr="GRRM23.out"
export subgau=""
export subchk=""
export subuchk=""
export submol=""
export subsiesta=""
export submpi="mpirun"
export I_MPI_FABRICS="shm:tcp"
export I_MPI_FALLBACK=0
export I_MPI_HYDRA_BOOTSTRAP="ssh"
export STLM_SERVER_ADDRESS="XXX.XXX.XXX.XXX"
export STLM_SERVER_PORT=XXXXX
```

!!! important "Configuration File Update"
    Before using GRRM, please insert the lines provided in the installation output into your shell (`/bin/bash`) configuration file (e.g., `~/.bashrc`).

!!! important "STLM Server Details"
    Please consult your system administrator about the STLM server IP address and port number. This information is crucial for license validation.

Copy the last lines (from “`source`” to the last “`export`” line) into your `.bashrc` in your home directory. Since G16 is not loaded on the Alliance's login nodes, you need to manually add `g16`, `formchk`, and `unfchk` into the corresponding lines below (`subgau`, `subchk`, and `subuchk`, respectively). For validating your license, please replace the `XXX` values at `STLM_SERVER_ADDRESS` and `STLM_SERVER_PORT` with the information provided by HPC SYSTEMS Inc. for your license (HPC SYSTEMS Inc. will send users this information via email):

```bash
source /home/user/GRRM23_RUN/mpi-rt/mpi/2021.6.0/env/vars.sh
export PATH="/home/user/GRRM23_RUN:${PATH}"
export LD_LIBRARY_PATH="/home/user/GRRM23_RUN:${LD_LIBRARY_PATH}"
export GRRMroot="/home/user/GRRM23_RUN"
export subgrr="GRRM23.out"
export subgau="g16"
export subchk="formchk"
export subuchk="unfchk"
export submol=""
export subsiesta=""
export submpi="mpirun"
export I_MPI_FABRICS="shm:tcp"
export I_MPI_FALLBACK=0
export I_MPI_HYDRA_BOOTSTRAP="ssh"
export STLM_SERVER_ADDRESS="XXX.XXX.XXX.XXX"
export STLM_SERVER_PORT=XXXXX
```

Source your `.bashrc` file and logout:

```bash
source /home/user/.bashrc
exit
```

After login, type `GRRM23p` on the terminal. If the installation was successful, the following text should appear:

```console
USAGE: GRRMp [input file name] (-p[Nproc]) (-h[Hour]) (-w/xxx/xxx) 
(-f[machine_file]) (-c[Ncore])
```

Fir and Nibi have G16 installed for their users. Compute nodes on both systems can connect to the Internet for the purpose of connecting to any required license servers.

## Running GRRM
For input examples, please refer to the GRRM23 user manual. In general, GRRM23 requires only one input file (`Job.com`) with the Cartesian coordinates of a molecule plus methodology options; in some cases, GRRM23 will require the output of a previous GRRM23 job.

### Sample Slurm Script for a Single Node
For a single node (`-N 1`) and 12 cores (`-n 12`), running from the user’s `/scratch` directory:

```bash
#!/bin/bash
#SBATCH -t 1-00:00
#SBATCH -J Job_SLURM
#SBATCH -o Job.SLURMout
#SBATCH -e Job.SLURMerr
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=Job

cd /home/user/scratch/

module load gaussian/g16.c01
export GAUSS_SCRDIR=/home/user/scratch/

GRRM23p ${input} -p1 -s80000
```

*   `-p1`: number of parallel processes;
*   `-s80000`: signals when to create a checkpoint file (in seconds); you must tell GRRM23 when to create the checkpoint files so that an interrupted/killed job can be restarted properly.

### Example Using ORCA

```bash
#!/bin/bash
#SBATCH -t 0-18:00
#SBATCH -J glucose_SLURM
#SBATCH -o glucose.SLURMout
#SBATCH -e glucose.SLURMerr
#SBATCH -N 1
#SBATCH -n 16
#SBATCH --mem-per-cpu=4000M
#SBATCH --account=def-users_account

input=glucose

cd /home/user/scratch/Pyrolysis_of_Models/glucose

module load StdEnv/2023  gcc/12.3  openmpi/4.1.5
module load orca/6.0.0

GRRM23p ${input} -p1 -h15
```

### Sample Slurm Script for Multiple Nodes
At this moment, since we are using GRRM23 with G16 primarily, we can only use a single node, as per Gaussian 16 license policies.

## External Resources
[GRRM User Manuals](https://afir.sci.hokudai.ac.jp/manual/)

## Acknowledgements
This documentation was contributed by Eduardo Romero Montalvo.