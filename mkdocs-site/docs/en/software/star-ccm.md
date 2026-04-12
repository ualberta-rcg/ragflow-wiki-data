---
title: "Star-CCM+/en"
slug: "star-ccm"
lang: "en"

source_wiki_title: "Star-CCM+/en"
source_hash: "aab0cf5f5f8d029e118112700e5ddc05"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:35:58.492611+00:00"

tags:
  - software

keywords:
  - "java macros"
  - "SBATCH"
  - "Siemens PoD Key"
  - "CDLMD_LICENSE_FILE"
  - "License server configuration"
  - "memory per node"
  - "starccm+"
  - "Slurm"
  - "License server"
  - "VNC Viewer"
  - "Open OnDemand"
  - "institutional license server"
  - "granite"
  - "Cluster batch job submission"
  - "module load"
  - "starccm"
  - "Process Options"
  - "license server"
  - "CPU vendor"
  - "NARVAL"
  - "PoD license"
  - "Power-on-Demand license"
  - "openmpi"
  - "Slurm scripts"
  - "sim filename"
  - "FLEXIBLAS"
  - "JupyterHub"
  - "SLURM"
  - "RORQUAL"
  - "STAR-CCM+"
  - "bash script"
  - "MPI"
  - "SLURM_TMPDIR"
  - "Software Modules"
  - "JupyterLab"

questions:
  - "What is the STAR-CCM+ software suite and what types of engineering simulations is it used to model?"
  - "What are the two main licensing options available for researchers to use STAR-CCM+ on the clusters?"
  - "How must a user configure their account files and environment variables to successfully submit a batch job using a Power-on-Demand (PoD) license?"
  - "What specific hardware resources and node constraints are requested using the SBATCH directives?"
  - "Which software environment and specific application modules are actively loaded by this script?"
  - "What alternative versions of the STAR-CCM+ software are listed as available in the script's comments?"
  - "How does the script configure STAR-CCM+ to use a Siemens Power-on-Demand (PoD) license versus a local institutional license?"
  - "What specific MPI and FlexiBLAS parameters are dynamically set based on whether the detected CPU vendor is Intel or AMD?"
  - "How does the script handle SLURM resource allocations and temporary directory redirection for the simulation job?"
  - "How is the input simulation filename and the execution macro specified in this configuration?"
  - "What is the purpose of the LM_PROJECT variable, and under what condition should it be modified?"
  - "Why is the STARCCM_TMP environment variable exported to redirect temporary files to $SLURM_TMPDIR?"
  - "How does the script dynamically configure the MPI and FLEXIBLAS environment variables based on the CPU vendor?"
  - "What is the difference in the execution command and setup when using a Siemens Power on Demand (PoD) license versus an institutional license?"
  - "How are the Slurm job parameters and SSH tunnels configured to allocate resources and connect to the remote license server in the Trillium environment?"
  - "How does the provided bash script handle potential license failures when attempting to start STAR-CCM+?"
  - "What specific configurations and environment variables must be set by research groups using a POD license before launching the software in graphical mode?"
  - "What are the recommended platforms for running STAR-CCM+ graphically, and how do the module load commands differ based on the software version?"
  - "How does the script configure the SSH tunnel and environment variables to establish a connection with the license server?"
  - "What specific SLURM variables are multiplied together to calculate the total number of cores (NCORE) for the job?"
  - "How is the machine file generated and formatted for the STAR-CCM+ execution environment?"
  - "What are the specific commands and process options used to run starccm+ in serial versus parallel mode?"
  - "How does a user initiate a JupyterHub desktop session according to the text?"
  - "What are the specific web addresses provided for accessing JupyterHub on the FIR and NARVAL clusters?"
  - "How do you load and launch the STAR-CCM+ module using the JupyterHub interface on RORQUAL?"
  - "What specific configuration steps must be taken in the \"Create a File\" panel to run STAR-CCM+ with multiple cores?"
  - "What are the legacy terminal commands required to load and execute different versions of STAR-CCM+ through a VncViewer client?"
  - "How do you load and launch the STAR-CCM+ module using the JupyterHub interface on RORQUAL?"
  - "What specific configuration steps must be taken in the \"Create a File\" panel to run STAR-CCM+ with multiple cores?"
  - "What are the legacy terminal commands required to load and execute different versions of STAR-CCM+ through a VncViewer client?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[STAR-CCM+](https://mdx.plm.automation.siemens.com/star-ccm-plus) is a multidisciplinary engineering simulation suite to model acoustics, fluid dynamics, heat transfer, rheology, multiphase flows, particle flows, solid mechanics, reacting flows, electrochemistry, and electromagnetics. It is developed by Siemens.

## License Limitations
The Alliance has the authorization to host STAR-CCM+ binaries on the clusters. However, you will need to purchase a licence from [Siemens](https://www.plm.automation.siemens.com/global/en/buy/) in order to use this software. There are two [options](https://community.sw.siemens.com/s/article/How-faculty-members-in-academic-institutions-can-get-access-to-Simcenter-STAR-CCM). Most research groups purchase a remotely hosted [Power-on-Demand (PoD)](https://community.sw.siemens.com/s/question/0D54O00006FKu39SAD/licensing-how-power-on-demand-pod-licensing-for-starccm-works) licence since it simply requires a licence key to use. Alternatively, a locally hosted licence server can be set up and managed at your institution provided it can be accessed through the firewall from the cluster where jobs will be run.

## Configuring Your Account
To configure your account to use a licence server with the Star-CCM+ module, create a licence file `$HOME/.licenses/starccm.lic` with the following layout:

```text title="starccm.lic"
SERVER <server> ANY <port>
USE_SERVER
```

where `<server>` and `<port>` should be changed to specify the hostname (or IP address) and the static vendor port of the licence server respectively. Note that manually setting `CDLMD_LICENSE_FILE` equal to `<port>@<server>` in your Slurm script is not required; instead, when a Star-CCM+ module is loaded, this variable is automatically set to your *$HOME/.licenses/starccm.lic* file.

### PoD Licence File

To run jobs, researchers with a Power-on-Demand (PoD) licence must manually set the `LM_PROJECT` environment variable to your *22digit-PoD-License-Key* as shown in the sample Slurm scripts below. Also, a `~/.licenses/starccm.lic` file should be configured on each cluster where jobs are to be run as follows:

```text title="starccm.lic"
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

## Cluster Batch Job Submission

Before submitting jobs on a cluster, you must set up a `~/.licenses/starccm.lic` file on each cluster where you will run jobs. If you have a PoD licence then the required firewall changes have already been done on all of the Alliance clusters. If however you will be using a local institutional licence server then you will need to submit a problem ticket to [technical support](../support/technical_support.md) to request the one-time network firewall changes be made between the cluster(s) and your local licence server. If you have problems getting the licensing to work then try removing or renaming file `~/.flexlmrc` since previous search paths and/or licence server settings may be stored in it.

!!! note
    Temporary output files from Star-CCM+ jobs may accumulate in hidden directories named `~/.star-version_number`, consuming valuable quota space. These can be removed by periodically running `rm -ri ~/.starccm*` and replying yes when prompted.

## Slurm Scripts

=== "Nibi"
    ```bash title="starccm_job-nibi-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    #SBATCH --constraint=granite  # Use intel cpu only base nodes
    #SBATCH --switches=1          # Use 1 network switch (optional)

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Load 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using a local institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > "$SLURM_TMPDIR"/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Checking $CDLMD_LICENSE_FILE ..."
    server=$(head -n1 "$CDLMD_LICENSE_FILE" | awk '{print $2}')
    port=$(cat "$CDLMD_LICENSE_FILE" | grep -Eo '[0-9]+$')
    nmap "$server" -Pn -p "$port" | grep -v '^$'; echo

    CPU_VENDOR=$(lscpu | awk '/Vendor ID/{print $3}')
    echo "CPU_VENDOR= $CPU_VENDOR"
    if [ "$CPU_VENDOR" == GenuineIntel ]; then
      if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
        STAR_UCX="-xsystemucx"
        export FLEXIBLAS=StarMKL
      else
        STAR_FLEXIBLAS="-flexiblaslib MKL"
      fi
      STAR_MPI="-mpi intel"
      STAR_FABRIC="-fabric tcp"
    elif [ "$CPU_VENDOR" == AuthenticAMD ]; then
      if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
        STAR_UCX="-xsystemucx"
        export FLEXIBLAS=StarAOCL
      else
        STAR_FLEXIBLAS="-flexiblaslib AOCL" 
        STAR_PRELOAD="-ldpreload /usr/lib64/libdrm_amdgpu.so.1" 
      fi
      STAR_MPI="-mpi openmpi40"
    fi

    if [ -n "$LM_PROJECT" ]; then
       echo "Siemens PoD license server ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -power -podkey "$LM_PROJECT" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$JAVA_FILE" "$SIM_FILE" "$STAR_MPI" "$STAR_UCX" "$STAR_FABRIC" "$STAR_FLEXIBLAS" "$STAR_PRELOAD"
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$JAVA_FILE" "$SIM_FILE" "$STAR_MPI" "$STAR_UCX" "$STAR_FABRIC" "$STAR_FLEXIBLAS" "$STAR_PRELOAD"
    fi
    ```

=== "Fir/Narval/Rorqual"
    ```bash title="starccm_job-fnr-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=16    # Specify cores per node (192 max)
    #SBATCH --mem=64G             # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using an institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    slurm_hl2hl.py --format STAR-CCM+ > "$SLURM_TMPDIR"/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Checking $CDLMD_LICENSE_FILE ..."
    server=$(head -n1 "$CDLMD_LICENSE_FILE" | awk '{print $2}')
    port=$(cat "$CDLMD_LICENSE_FILE" | grep -Eo '[0-9]+$')
    nmap "$server" -Pn -p "$port" | grep -v '^$'; echo

    export FLEXIBLAS=NETLIB
    STAR_MPI="-mpi openmpi"
    if [ "$RSNT_CPU_VENDOR_ID" == intel ]; then
      export FLEXIBLAS=StarMKL
      STAR_MPI="-mpi intel"
    elif [ "$RSNT_CPU_VENDOR_ID" == amd ]; then
      export FLEXIBLAS=StarAOCL
    fi
    echo "FLEXIBLAS=$FLEXIBLAS"

    if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
      STAR_UCX="-xsystemucx"
    fi

    if [ -n "$LM_PROJECT" ]; then
       echo "Siemens PoD license server ..."
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -power -podkey "$LM_PROJECT" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$SIM_FILE" "$STAR_MPI" "$STAR_UCX"
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$SIM_FILE" "$STAR_MPI" "$STAR_UCX"
    fi
    ```

=== "Trillium"
    ```bash title="starccm_job-trillium-nogpu.sh"
    #!/bin/bash

    #SBATCH --account=def-group   # Specify some account
    #SBATCH --time=00-01:00       # Time limit: dd-hh:mm
    #SBATCH --nodes=1             # Specify 1 or more nodes
    #SBATCH --cpus-per-task=192   # Specify cores per node (192 max)
    #SBATCH --mem=0               # Specify memory per node (0 max)
    #SBATCH --ntasks-per-node=1   # Do not change this value
    #SBATCH --output=slurm-%j.out # Writes to slurm-$SLURM_JOB_ID.out

    cd "$SLURM_SUBMIT_DIR"          # Submit from $SCRATCH/some/dir

    module load StdEnv/2023

    #module load starccm/20.06.010-R8    # Specify 18.04.009, 18.06.007, 19.04.009,
    module load starccm-mixed/20.06.010  # 19.06.009, 20.02.008, 20.04.007 or newer
    module list

    SIM_FILE='mySample.sim'        # Specify your input sim filename
    #BATCH_CMD='myMacro.java,run'  # Uncomment to specify java macros, mesh, run, step

    # Comment the next line when using an institutional license server
    LM_PROJECT='22digit-PoD-License-Key'  # Specify your Siemens PoD Key here

    # These settings are used instead of your ~/.licenses/starccm.lic
    # (settings shown will use the cd-adapco pod license server)
    FLEXPORT=1999                    # Specify server static flex port
    VENDPORT=2099                    # Specify server static vendor port
    LICSERVER=flex.cd-adapco.com     # Specify license server hostname

    # ------- no changes required below this line --------

    # Redirect from ~/.star-VERSION# to $SLURM_TMPDIR
    export STARCCM_TMP="$SLURM_TMPDIR"

    export CDLMD_LICENSE_FILE="$FLEXPORT@127.0.0.1"
    ssh tri-gw -L "$FLEXPORT":"$LICSERVER":"$FLEXPORT" -L "$VENDPORT":"$LICSERVER":"$VENDPORT" -N -f

    slurm_hl2hl.py --format STAR-CCM+ > "$SLURM_TMPDIR"/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    export FLEXIBLAS=StarAOCL
    echo "FLEXIBLAS=$FLEXIBLAS"
    STAR_MPI="-mpi openmpi"

    if [ "${EBVERSIONSTARCCM:0:2}" -lt 20 ]; then
      STAR_UCX="-xsystemucx"
    fi
     
    # Workaround for license failures: 
    # until the exit status is equal to 0, we try to get Star-CCM+ to start (here, for at least 5 times).
    i=1
    RET=-1
    while [ "$i" -le 5 ] && [ "$RET" -ne 0 ]; do
            [ "$i" -eq 1 ] || sleep 5
              echo "Attempt number: "$i
              if [ -n "$LM_PROJECT" ]; then
              echo "Siemens PoD license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -power -podkey "$LM_PROJECT" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$SIM_FILE" "$STAR_MPI" "$STAR_UCX"
            else
              echo "Institutional license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch "$BATCH_CMD" -np "$NCORE" -nbuserdir "$SLURM_TMPDIR" -machinefile "$SLURM_TMPDIR"/machinefile "$SIM_FILE" "$STAR_MPI" "$STAR_UCX"
            fi
            RET=$?
            i=$((i+1))
    done
    exit "$RET"
    ```

## Graphical Use

To run starccm+ in graphical mode it is recommended to use an [OnDemand](https://docs.alliancecan.ca/wiki/nibi#access-through-open-ondemand-ood) or JupyterLab system to start a remote desktop. In addition to configuring `~/.licenses/starccm.lic`, research groups with a PoD licence should also run `export LM_PROJECT='22digit-PoD-License-Key'` before starting `starccm+` as shown below. Additional command line options such as **-power** may also need to be appended depending on your licence type. Note that running `module avail starccm` will display all *mixed* and *R8* versions that are available to load within the `StdEnv/version` you currently have loaded, i.e., 2020 or 2023. Alternatively, running `module spider starccm` will show all *mixed* and *R8* module versions available to load within both StdEnv module versions that could be loaded, i.e., 2020 and 2023.

### OnDemand
1. To start an OnDemand desktop session, click one of the following OnDemand links:
   - [NIBI](https://docs.alliancecan.ca/wiki/nibi#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
   - TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2. Open a new terminal window in your desktop and run one of:
   - **STAR-CCM+ 18.04.008 (or newer versions)**
     - `module load StdEnv/2023` (default)
     - `module load starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8`
     - `starccm+ -rr server` (Process Options="Serial")
     - `starccm+ -rr server -np 2 -mpi openmpi40` (Process Options="Parallel on Local Host")
   - **STAR-CCM+ 15.04.010** → **17.06.008 (version range)**
     - `module load StdEnv/2020` (retired)
     - `module load starccm-mixed/17.06.008` **OR** `starccm/17.06.008-R8`
     - `starccm+` (Process Options="Serial")
     - `starccm+ -np 2` (Process Options="Parallel on Local Host")

### JupyterLab
1. Start a JupyterHub desktop session by clicking one of the following JupyterHub links:
   - FIR: `https://jupyterhub.fir.alliancecan.ca`
   - NARVAL: `https://portail.narval.calculquebec.ca/`
   - RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2. Click the hexagon shaped Software Modules gear icon located at the bottom of the leftmost vertical icon selector menu.
3. Highlight a starccm module such as `starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8` and click Load.
4. Click the rectangular `StarCCM+ Mixed(VNC)` **OR** `StarCCM (VNC)` icon that appears in desktop.
5. To run StarCCM+ with multiple cores for compute purposes ...
   - Click File -> New and a *Create a File* configurator panel should appear.
   - Change the default Serial Process Option by instead ticking the **Parallel on Local Host** radio button.
   - Add `-mpi openmpi40` to the end of the **Command:** string located at the bottom of the panel.
   - Finally click the **OK** button and the starccm+ GUI should appear.

### VncViewer

!!! warning
    These instructions are retained for legacy purposes only.

1. Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md).
2. Open a new terminal window in your desktop and run one of:
   - **STAR-CCM+ 18.04.008 (or newer versions)**
     - `module load StdEnv/2023` (default)
     - `module load starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8`
     - `starccm+ -rr server` **OR** `starccm+ -rr server -np 2 -mpi openmpi40`
   - **STAR-CCM+ 15.04.010** → **17.06.008 (version range)**
     - `module load StdEnv/2020` (retired)
     - `module load starccm-mixed/17.06.008` **OR** `starccm/17.06.008-R8`
     - `starccm+`