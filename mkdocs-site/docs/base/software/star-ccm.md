---
title: "Star-CCM+"
slug: "star-ccm"
lang: "base"

source_wiki_title: "Star-CCM+"
source_hash: "d2c0e0dbcc6c1878b6087ec65cd7770f"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T01:05:11.169751+00:00"

tags:
  - software

keywords:
  - "JupyterLab"
  - "bash script"
  - "SBATCH directives"
  - "PoD Key"
  - "Siemens PoD license"
  - "R8 module"
  - "SLURM_SUBMIT_DIR"
  - "StdEnv"
  - "license server"
  - "STAR-CCM+"
  - "module load"
  - "Slurm scripts"
  - "MPI"
  - "Parallel on Local Host"
  - "quota space"
  - "NIBI"
  - "Power-on-Demand license"
  - "hidden directories"
  - "OnDemand"
  - "TRILLIUM"
  - "Fir/Narval/Rorqual"
  - "job submission"
  - "Slurm job script"
  - "SBATCH"
  - "JupyterHub"
  - "batch script"
  - "StdEnv module"
  - "starccm_job-fnr-nogpu.sh"
  - "OnDemand desktop session"
  - "starccm"
  - "SLURM"
  - "VncViewer"
  - "engineering simulation"
  - "License server"
  - "Bash script"

questions:
  - "What is STAR-CCM+ and what types of engineering simulations can it model?"
  - "What are the two licensing options available for researchers, and how do their network and firewall requirements differ?"
  - "How must a user configure their account files and Slurm script environment variables to run a job using a Power-on-Demand (PoD) license?"
  - "Why is it necessary to periodically remove the hidden directories named `~/.star-version_number`?"
  - "What specific command should be executed to delete the accumulated Star-CCM+ files and free up quota space?"
  - "Which `#SBATCH` parameters are configured in the provided Slurm script example?"
  - "How are the Slurm job resources, such as nodes, memory, and CPU cores, configured in the script?"
  - "How does the script differentiate between Intel and AMD CPUs to configure the appropriate MPI and FlexiBLAS settings?"
  - "What is the difference in the STAR-CCM+ execution command when using a Siemens Power-on-Demand (PoD) license key versus a local institutional license server?"
  - "What specific environment variables and software components are being passed to the execution command in the first part of the text?"
  - "For which specific high-performance computing clusters and hardware configurations is this bash script intended?"
  - "What are the exact Slurm resource allocation parameters requested in the script's header?"
  - "How are the computational resources, such as CPU cores and memory, specified in the SLURM batch script for the STAR-CCM+ job?"
  - "What is the difference in the execution command when using a Siemens Power-on-Demand (PoD) license key versus an institutional license server?"
  - "How does the script dynamically adjust the MPI and FLEXIBLAS environment variables based on the detected CPU vendor?"
  - "How do you configure the license settings and server ports in the script to run STAR-CCM+?"
  - "Why does the provided script include a while loop that attempts to start the STAR-CCM+ job up to five times?"
  - "What are the recommended methods and necessary configuration steps for running STAR-CCM+ in graphical mode?"
  - "What is the purpose of the variable \"e\" and why must its value remain unchanged?"
  - "How does the script configure the naming convention for the Slurm job output file?"
  - "Which specific software environments and versions are loaded to run the application?"
  - "Which StdEnv module versions support the loading of R8 module versions?"
  - "What is the first step required to start an OnDemand desktop session?"
  - "What are the specific URLs provided for accessing the NIBI and TRILLIUM systems via OnDemand?"
  - "How do the terminal commands for launching STAR-CCM+ differ between version 18.04.008 (or newer) and the older 15.04.010 to 17.06.008 version range?"
  - "What are the specific steps required to configure and run STAR-CCM+ with multiple cores within a JupyterLab session?"
  - "What is the legacy procedure for connecting to a node and launching the software using a VncViewer client?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[STAR-CCM+](https://mdx.plm.automation.siemens.com/star-ccm-plus) is a multidisciplinary engineering simulation suite to model acoustics, fluid dynamics, heat transfer, rheology, multiphase flows, particle flows, solid mechanics, reacting flows, electrochemistry, and electromagnetism. It is developed by Siemens.

## License limitations
The Alliance is authorized to host STAR-CCM+ binaries on its clusters. Researchers will need to purchase a license from [Siemens](https://www.plm.automation.siemens.com/global/en/buy/) in order to use the software. There are two [options](https://community.sw.siemens.com/s/article/How-faculty-members-in-academic-institutions-can-get-access-to-Simcenter-STAR-CCM). Most research groups will purchase a [Power-on-Demand (PoD)](https://community.sw.siemens.com/s/question/0D54O00006FKu39SAD/licensing-how-power-on-demand-pod-licensing-for-starccm-works) license which simply connects to a remotely hosted license server and requires only a license key to use. The second option is more complex and requires setting up and then managing a locally hosted institutional license server along with the purchase of a Simcenter STAR-CCM+ academic pack. For this to work, the local firewall will need to be opened by the local network administrator so the servers flex and static vendor ports are both reachable from the NAT nodes of the Alliance cluster(s) where jobs are to be run. To get a list of NAT nodes [submit a ticket](../support/technical_support.md) including the names of the Alliance cluster(s) you will be using, your license server hostname or IP address, and its flex and static vendor port numbers. The outbound firewall from the cluster(s) may also need to be opened. This will be done automatically for you as part of the ticket process if it's determined to be required.

### Configuring your account
To configure your account to use a license server with the Star-CCM+ module, create a license file `$HOME/.licenses/starccm.lic` with the following layout:

```text title="starccm.lic"
SERVER <server> ANY <flexport>
USE_SERVER
```

where `<server>` and `<flexport>` should be changed to specify the hostname (or IP address) and the static vendor port of the license server respectively. Note that manually setting `CDLMD_LICENSE_FILE` equal to `<port>@<server>` in your Slurm script is not required since this variable is automatically set whenever a starccm module is loaded.

#### PoD license file
To run jobs, researchers with a Power-on-Demand (PoD) license must manually set the `LM_PROJECT` environment variable to your *22digit-PoD-License-Key* as shown in the sample Slurm scripts below. The following `~/.licenses/starccm.lic` file must also be configured on each cluster where jobs are to be run:

```text title="starccm.lic"
SERVER flex.cd-adapco.com ANY 1999
USE_SERVER
```

## Cluster batch job submission
Before submitting jobs on a cluster, you must set up a `~/.licenses/starccm.lic` file on each cluster where you will run jobs. If you have a PoD license then the required firewall changes have already been done on all of the Alliance clusters. If however you will be using a local institutional license server then you will need to [submit a problem ticket](../support/technical_support.md) to request the one-time network firewall changes be made between the cluster(s) and your local license server. If you have problems getting the licensing to work then try removing or renaming file `~/.flexlmrc` since previous search paths and/or license server settings may be stored in it.

!!! warning
    Temporary output files from starccm jobs runs may accumulate in hidden directories named `~/.star-version_number` consuming valuable quota space. These can be removed by periodically running `rm -ri ~/.starccm*` and replying yes when prompted.

### Slurm scripts

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

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Checking $CDLMD_LICENSE_FILE ..."
    server=$(head -n1 $CDLMD_LICENSE_FILE | awk '{print $2}')
    port=$(cat $CDLMD_LICENSE_FILE | grep -Eo '[0-9]+$')
    nmap $server -Pn -p $port | grep -v '^$'; echo

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
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $JAVA_FILE $SIM_FILE $STAR_MPI $STAR_UCX $STAR_FABRIC $STAR_FLEXIBLAS $STAR_PRELOAD
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

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
    NCORE=$((SLURM_NNODES * SLURM_CPUS_PER_TASK * SLURM_NTASKS_PER_NODE))

    echo "Checking $CDLMD_LICENSE_FILE ..."
    server=$(head -n1 $CDLMD_LICENSE_FILE | awk '{print $2}')
    port=$(cat $CDLMD_LICENSE_FILE | grep -Eo '[0-9]+$')
    nmap $server -Pn -p $port | grep -v '^$'; echo

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
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
    else
       echo "Institutional license server ..."
       [ $(command -v lmutil) ] && lmutil lmstat -c ~/.licenses/starccm.lic -a | egrep "license1|UP|use|$USER"; echo
       starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
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

    cd $SLURM_SUBMIT_DIR          # Submit from $SCRATCH/some/dir

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
    ssh tri-gw -L $FLEXPORT:$LICSERVER:$FLEXPORT -L $VENDPORT:$LICSERVER:$VENDPORT -N -f

    slurm_hl2hl.py --format STAR-CCM+ > $SLURM_TMPDIR/machinefile
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
    while [ $i -le 5 ] && [ $RET -ne 0 ]; do
            [ $i -eq 1 ] || sleep 5
              echo "Attempt number: "$i
              if [ -n "$LM_PROJECT" ]; then
              echo "Siemens PoD license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -power -podkey $LM_PROJECT -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            else
              echo "Institutional license server ..."
              starccm+ -jvmargs "-Xmx4G -Djava.io.tmpdir=$SLURM_TMPDIR" -batch $BATCH_CMD -np $NCORE -nbuserdir $SLURM_TMPDIR -machinefile $SLURM_TMPDIR/machinefile $SIM_FILE $STAR_MPI $STAR_UCX
            fi
            RET=$?
            i=$((i+1))
    done
    exit $RET
    ```

## Graphical use
To run starccm+ in graphical mode, it is recommended to use an [OnDemand](https://docs.alliancecan.ca/wiki/nibi#access_through_open_ondemand_(ood)) or JupyterLab system to start a remote desktop. In addition to configuring `~/.licenses/starccm.lic`, research groups with a POD license should also run `export LM_PROJECT='22digit-PoD-License-Key'` before starting `starccm+` as shown below. Additional command-line options such as **-power** may also need to be appended depending on your license type. Note that running `module avail starccm` will display all *mixed* and *R8* versions that are available to load within the StdEnv/version you currently have loaded (e.g., 2020 or 2023). Alternatively, running `module spider starccm` will show all *mixed* and *R8* module versions available to load within both StdEnv module versions that could be loaded (e.g., 2020 and 2023).

### OnDemand
1.  To start an OnDemand desktop session click one of the following OnDemand links:
    *   [NIBI](https://docs.alliancecan.ca/wiki/nibi#access_through_open_ondemand_(ood)): `https://ondemand.sharcnet.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Open a new terminal window in your desktop and run one of:
    *   **STAR-CCM+ 18.04.008 (or newer versions)**
        *   `module load StdEnv/2023` (default)
        *   `module load starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8`
        *   `starccm+ -rr server` (Process Options="Serial")
        *   `starccm+ -rr server -np 2 -mpi openmpi40` (Process Options="Parallel on Local Host")
    *   **STAR-CCM+ 15.04.010 -> 17.06.008 (version range)**
        *   `module load StdEnv/2020` (retired)
        *   `module load starccm-mixed/17.06.008` **OR** `starccm/17.06.008-R8`
        *   `starccm+` (Process Options="Serial")
        *   `starccm+ -np 2` (Process Options="Parallel on Local Host")

### JupyterLab
1.  Start a JupyterHub desktop session by clicking one of the following JupyterHub links:
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
2.  Click the hexagon-shaped **Software Modules** gear icon located at the bottom of the leftmost vertical icon selector menu.
3.  Highlight a starccm module such as `starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8` and click **Load**.
4.  Click the rectangular `StarCCM+ Mixed(VNC)` **OR** `StarCCM (VNC)` icon that appears in desktop.
5.  To run StarCCM+ with multiple cores for compute purposes:
    *   Click **File -> New** and a *Create a File* configurator panel should appear.
    *   Change the default Serial Process Option by instead ticking the **Parallel on Local Host** radio button.
    *   Add `-mpi openmpi40` to the end of the **Command:** string located at the bottom of the panel.
    *   Finally, click the **OK** button and the starccm+ GUI should appear.

### VncViewer
These instructions are retained for legacy purposes only:

1.  Connect with a VncViewer client to a login or compute node by following [TigerVNC](../interactive/vnc.md).
2.  Open a new terminal window in your desktop and run one of:
    *   **STAR-CCM+ 18.04.008 (or newer versions)**
        *   `module load StdEnv/2023` (default)
        *   `module load starccm-mixed/20.06.010` **OR** `starccm/20.06.010-R8`
        *   `starccm+ -rr server` **OR** `starccm+ -rr server -np 2 -mpi openmpi40`
    *   **STAR-CCM+ 15.04.010 -> 17.06.008 (version range)**
        *   `module load StdEnv/2020` (retired)
        *   `module load starccm-mixed/17.06.008` **OR** `starccm/17.06.008-R8`
        *   `starccm+`