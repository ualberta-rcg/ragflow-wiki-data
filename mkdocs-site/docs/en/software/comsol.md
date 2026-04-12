---
title: "COMSOL/en"
slug: "comsol"
lang: "en"

source_wiki_title: "COMSOL/en"
source_hash: "08f0b9a812d2f8364f5c5788189cb4d5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:00:08.356390+00:00"

tags:
  - software

keywords:
  - "large simulations"
  - "ansys"
  - "SLURM batch script"
  - "Parameter sweeps"
  - "job submission"
  - "lmutil lmstat"
  - "compute node"
  - "Java heap memory"
  - "Cluster sweep"
  - "restarting interrupted jobs"
  - "Open OnDemand"
  - "COMSOL job"
  - "CMC license"
  - "sbatch slurmscript"
  - "batch mode"
  - "COMSOL"
  - "Slurm script"
  - "compute clusters"
  - "desktop session"
  - "module load"
  - "license server"
  - "comsol.lic"
  - "compute nodes"
  - "Graphical mode"
  - "JupyterHub"
  - "COMSOL Multiphysics"
  - "Batch sweep"
  - "cluster login node"
  - "JupyterLab"

questions:
  - "How can users obtain a valid license to use COMSOL on the clusters, given that a generic license is not provided?"
  - "What are the necessary steps and information required to configure a local institutional license server or a CMC license file?"
  - "How can researchers check the number of COMSOL licenses currently checked out by their running jobs?"
  - "On which type of node can the module be executed?"
  - "What is the standard file path used to define the license server?"
  - "Why might the license check command take a minute to return a result?"
  - "How can a user verify which COMSOL modules are licensed and check the exact software version installed on the cluster?"
  - "What is the recommended procedure and Slurm script configuration for submitting a COMSOL batch job on a single compute node?"
  - "Why should users test the core scaling of their simulation before deciding to distribute a COMSOL job across multiple compute nodes?"
  - "How do you configure the SLURM batch script and load the appropriate environment modules to run a COMSOL job?"
  - "What steps should be taken to troubleshoot a multiple-node job that crashes on startup with a Java segmentation fault?"
  - "How can a user access and launch the COMSOL graphical user interface (GUI) using remote desktop environments like Open OnDemand or JupyterLab?"
  - "What type of simulations is this COMSOL script best suited for, and how does it distribute its computational resources?"
  - "How does the script handle interrupted jobs and the allocation of large temporary files?"
  - "What specific memory configuration option is available to users to modify below the script?"
  - "How is the COMSOL application launched within the remote Jupyter desktop environment?"
  - "What approach should be used to perform parameter sweeps interactively within the COMSOL GUI?"
  - "How do you submit a parameter sweep job to the cluster scheduler, and which graphical interface feature is currently unsupported for this?"
  - "What is the default command used to load the COMSOL 6.1 module?"
  - "Which URLs are provided to start a JupyterHub desktop session for the FIR, NARVAL, and RORQUAL clusters?"
  - "How do you select a specific COMSOL module within the JupyterLab interface?"
  - "How is the COMSOL application launched within the remote Jupyter desktop environment?"
  - "What approach should be used to perform parameter sweeps interactively within the COMSOL GUI?"
  - "How do you submit a parameter sweep job to the cluster scheduler, and which graphical interface feature is currently unsupported for this?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# COMSOL

COMSOL is a general-purpose software for modelling engineering applications. We would like to thank COMSOL, Inc. for allowing its software to be hosted on our clusters via a special agreement.

We recommend that you consult the documentation included with the software under *File > Help > Documentation* prior to attempting to use COMSOL on one of our clusters. Links to the COMSOL blog, Knowledge Base, Support Centre and Documentation can be found at the bottom of the [COMSOL home page](http://www.comsol.com). Searchable online COMSOL documentation is also available [here](https://doc.comsol.com/).

# Licensing

We are a hosting provider for COMSOL. This means that we have COMSOL software installed on our clusters, but we do not provide a generic license accessible to everyone. Many institutions, faculties, and departments already have licenses that can be used on our clusters. Alternatively, you can purchase a license from [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) for use anywhere in Canada. Once the legal aspects are worked out for licensing, there will be remaining technical aspects. The license server on your end will need to be reachable by our compute nodes. This will require our technical team to get in touch with the technical people managing your license software. If you have purchased a CMC license and will be connecting to the CMC license server, this has already been done. Once the license server work is done and your *~/.licenses/comsol.lic* has been created, you can load any COMSOL module and begin using the software. If this is not the case, please contact our [technical support](technical-support.md).

## Configuring your own license file

Our COMSOL module is designed to look for license information in a few places, one of which is your *~/.licenses* directory. If you have your own license server then specify it by creating a text file `$HOME/.licenses/comsol.lic` with the following information:

```bash
# comsol.lic
SERVER <server> ANY <port>
USE_SERVER
```

Where `<server>` is your license server hostname and `<port>` is the flex port number of the license server.

### Local license setup

For researchers wanting to use a new local institutional license server, firewall changes will need to be done to the network on both the Alliance (system/cluster) side and the institutional (server) side. To arrange this, send an email to [technical support](technical-support.md) containing 1) the COMSOL lmgrd TCP flex port number (typically 1718 default) and 2) the static LMCOMSOL TCP vendor port number (typically 1719 default) and finally 3) the fully qualified hostname of your COMSOL license server. Once this is complete, create a corresponding *comsol.lic* text file as shown above.

### CMC license setup

Researchers who own a COMSOL license subscription from CMC should use the following preconfigured public IP settings in their *comsol.lic* file:

*   Fir: SERVER 172.26.0.101 ANY 6601
*   Nibi: SERVER 10.25.1.56 ANY 6601
*   Narval/Rorqual: SERVER 10.100.64.10 ANY 6601
*   Trillium: SERVER scinet-cmc ANY 6601

For example, a license file created on Nibi cluster would look as follows:

```bash
[l2 (login node):~] cat ~/.licenses/comsol.lic
SERVER 10.25.1.56 ANY 6601
USE_SERVER
```

If initial license checkout attempts fail, create a support case with [CMC](https://www.cmc.ca/support/)

## Checking license use

To determine the number of licenses checked out by your running COMSOL job(s) it is necessary to query the license server you are using. As described [here](https://www.comsol.com/support/knowledgebase/1142), this maybe done using the `lmstat` command. However, as this command is not installed with COMSOL by default, the following one liner workaround which uses `lmutil` from the latest installed ansys module may be run on any cluster login node instead. As long as you rely upon the standard `~/.licenses/comsol.lic` to define which license server you are using, it should work, but may take a minute to return if the server is busy.

```bash
[l2 (login-node):~] module load ansys; $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c ~/.licenses/comsol.lic -a | sed '/^$/d' | egrep 'License|UP|$USER|Total of'  | grep -v 'Total of 0'
```

## Installed products

To check which [modules and products](https://www.comsol.com/products) are available for use, start COMSOL in [graphical mode](#graphical-use) and then click *Options -> Licensed and Used Products* on the upper pull-down menu. For a more detailed explanation, click [here](https://doc.comsol.com/6.0/docserver/#!/com.comsol.help.comsol/comsol_ref_customizing.16.09.html). If a module/product is missing or reports being unlicensed, contact [technical support](technical-support.md) as a reinstall of the CVMFS module you are using may be required.

## Installed versions

To check the full version number either start COMSOL in [GUI](#graphical-use) mode and inspect the lower right corner messages window OR more simply login to a cluster and run COMSOL in batch mode as follows:

```bash
[login-node:~] salloc --time=0:01:00 --nodes=1 --cores=1 --mem=1G --account=def-someuser
[login-node:~] module load comsol/6.2
[login-node:~] comsol batch -version
COMSOL Multiphysics 6.2.0.290
```

which corresponds to COMSOL 6.2 Update 1. In other words, when a new [COMSOL release](https://www.comsol.com/release-history) is installed, it will use the abbreviated 6.X version format but for convenience will contain the latest available update at the time of installation. As additional [product updates](https://www.comsol.com/product-update) are released they will instead utilize the full 6.X.Y.Z version format. For example, [Update 3](https://www.comsol.com/product-update/6.2) can be loaded on a cluster with the `module load comsol/6.2.0.415` OR `module load comsol` commands. We recommend using the most recent update to take advantage of all the latest improvements. That said, if you want to continue using any module version (6.X or 6.X.Y.Z), you can be assured by definition that the software contained in these modules will remain exactly the same.

To check which versions are available in the standard environment you have loaded (typically `StdEnv/2023`) run the `module avail comsol` command. Lastly, to check which versions are available in ALL available standard environments, use the `module spider comsol` command.

A module `comsol/6.3` corresponding to version [6.3.0.290](https://www.comsol.com/product-download/6.3) is now available on all clusters.

# Submit jobs

## Single compute node

Sample submission script to run a COMSOL job with eight cores on a single compute node:

```bash
# mysub1.sh
#!/bin/bash
#SBATCH --time=0-03:00             # Specify (d-hh:mm)
#SBATCH --account=def-group        # Specify (some account)
#SBATCH --mem=32G                  # Specify (0 to use all memory on each node)
#SBATCH --cpus-per-task=8          # Specify (max value of all cores on a node)
#SBATCH --nodes=1                  # Do not change
#SBATCH --ntasks-per-node=1        # Do not change

INPUTFILE="ModelToSolve.mph"       # Specify input filename
OUTPUTFILE="SolvedModel.mph"       # Specify output filename

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

comsol batch -inputfile ${INPUTFILE} -outputfile ${OUTPUTFILE} -np $SLURM_CPUS_ON_NODE
```

Depending on the complexity of the simulation, COMSOL may not be able to efficiently use very many cores. Therefore, it is advisable to test the scaling of your simulation by gradually increasing the number of cores. If near-linear speedup is obtained using all cores on a compute node, consider running the job over multiple full nodes using the next Slurm script.

## Multiple compute nodes

Sample submission script to run a COMSOL job with eight cores distributed evenly over two compute nodes. Ideal for very large simulations (that exceed the capabilities of a single compute node), this script supports restarting interrupted jobs, allocating large temporary files to /scratch and utilizing the default *comsolbatch.ini* file settings. There is also an option to modify the Java heap memory described below the script.

```bash
# script-dis.sh
#!/bin/bash
#SBATCH --time=0-03:00             # Specify (d-hh:mm)
#SBATCH --account=def-account      # Specify (some account)
#SBATCH --mem=16G                  # Specify (0 to use all memory on each node)
#SBATCH --cpus-per-task=4          # Specify (max value of all cores on a node)
#SBATCH --nodes=2                  # Specify (the number of compute nodes to use for the job)
#SBATCH --ntasks-per-node=1        # Do not change

INPUTFILE="ModelToSolve.mph"       # Specify input filename
OUTPUTFILE="SolvedModel.mph"       # Specify output filename

# module load StdEnv/2020          # Versions <= 6.1
module load StdEnv/2023            # Versions >= 6.2
module load comsol/6.4

RECOVERYDIR=$SCRATCH/comsol/recoverydir
mkdir -p $RECOVERYDIR

cp -f ${EBROOTCOMSOL}/bin/glnxa64/comsolbatch.ini comsolbatch.ini
cp -f ${EBROOTCOMSOL}/mli/startup/java.opts java.opts

# export I_MPI_COLL_EXTERNAL=0      # Uncomment this line on narval

comsol batch -inputfile $INPUTFILE -outputfile $OUTPUTFILE -np $SLURM_CPUS_ON_NODE -nn $SLURM_NNODES \
-recoverydir $RECOVERYDIR -tmpdir $SLURM_TMPDIR -comsolinifile comsolbatch.ini -alivetime 15 \
# -recover -continue                # Uncomment this line to restart solving from latest recovery files
```

!!! note "Java Heap Memory"
    If your multiple node job crashes on startup with a Java segmentation fault, try increasing the Java heap by adding the following two `sed` lines after the two `cp -f` lines. If it does not help, try further changing both 4g values to 8g. For further information see [Out of Memory](https://www.comsol.ch/support/knowledgebase/1243).

    ```bash
    sed -i 's/-Xmx2g/-Xmx4g/g' comsolbatch.ini
    sed -i 's/-Xmx768m/-Xmx4g/g' java.opts
    ```

!!! tip "Job runs slow or hangs"
    If a job runs slow or hangs during startup when submitted to a single node with the above *script-smp.sh* script, try using the above multiple node *script-dis.sh* script instead with `#SBATCH --nodes=1` and then please open a ticket to report the problem including the job number and cluster name.

# Graphical use

To run COMSOL in graphical mode open a remote desktop on an [OnDemand](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)) or JupyterLab system by clicking one of the following links. Note that the old approach of using a [TigerVNC](vnc.md) client/server pair should still work but is no longer recommended or supported. For either approach `~/.licenses/comsol.lic` must first be configured. Note that running command `module avail comsol` will display which COMSOL versions are available within the StdEnv version that you currently have loaded ie) `StdEnv/2023`. If you find the upper menu items are greyed out and not clickable after starting COMSOL in GUI mode then your *~/.comsol* maybe corrupted so try deleting it.

## OnDemand

1.  Start an OnDemand desktop session by clicking one of the following OnDemand links
    [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Open a new terminal window in your desktop and run one of:
    **COMSOL 6.2 (or newer versions)**
    ```bash
    module load StdEnv/2023
    module load comsol/6.4
    comsol
    ```
    **COMSOL 6.1 (or older versions)**
    ```bash
    module load StdEnv/2020
    module load comsol/6.1
    comsol
    ```

## JupyterLab

1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links
    [FIR](https://jupyterhub.fir.alliancecan.ca): `https://jupyterhub.fir.alliancecan.ca`
    [NARVAL](https://portail.narval.calculquebec.ca/): `https://portail.narval.calculquebec.ca/`
    [RORQUAL](https://jupyterhub.rorqual.alliancecan.ca): `https://jupyterhub.rorqual.alliancecan.ca`
2.  Highlight a COMSOL module such as `comsol/6.4` in the left hand side Available Module section
3.  Click Load for the highlighted module and a `Comsol (VNC)` Icon will appear in desktop
4.  Click the Icon and COMSOL should automatically be started in a remote Jupyter desktop

# Parameter sweeps

## Batch sweep

When working interactively in the COMSOL GUI, parametric problems may be solved using the [Batch Sweep](https://www.comsol.com/blogs/the-power-of-the-batch-sweep/) approach. Multiple parameter sweeps maybe carried out as shown in [this video](https://www.comsol.com/video/performing-parametric-sweep-study-comsol-multiphysics). Speedup due to [Task Parallelism](https://www.comsol.com/blogs/added-value-task-parallelism-batch-sweeps/) may also be realized.

## Cluster sweep

To run a parameter sweep on a cluster, a job must be submitted to the scheduler from the command line using `sbatch slurmscript`. For a discussion regarding additional required arguments, see [here](https://www.comsol.com/support/knowledgebase/1250) and [here](https://www.comsol.com/blogs/how-to-use-job-sequences-to-save-data-after-solving-your-model/) for details. Support for submitting parametric simulations to the cluster queue from the graphical interface using a [Cluster Sweep node](https://www.comsol.com/blogs/how-to-use-the-cluster-sweep-node-in-comsol-multiphysics/) is not available at this time.