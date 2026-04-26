---
title: "AnsysEDT/en"
slug: "ansysedt"
lang: "en"

source_wiki_title: "AnsysEDT/en"
source_hash: "3f0a8813c83a4a6c44ced0f322cd9f91"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:16:17.774112+00:00"

tags:
  - software

keywords:
  - "AnsysEDT"
  - "Validation Check"
  - "ansysedt"
  - "Ansys EDT"
  - "HFSS"
  - "electromagnetics simulation"
  - "Open OnDemand"
  - "AEDT file"
  - "Simulation setup"
  - "Alliance cluster"
  - "Slurm batch script"
  - "license server"
  - "simulation"
  - "ansys.lic"
  - "SHARCNET ANSYS License"
  - "Antennas examples"
  - "Graphical mode"
  - "Single node"
  - "Slurm scripts"
  - "SLURM"
  - "cluster batch job"
  - "bash script"
  - "batchsolve"

questions:
  - "What simulation solutions and workflows are bundled within the AnsysEDT software?"
  - "How do users configure and access the necessary licenses to use AnsysEDT on the cluster?"
  - "What are the steps and commands required to submit an AnsysEDT batch job using Slurm scripts?"
  - "What are the necessary Slurm directives and commands to run an Ansys Electronics Desktop simulation in batch mode?"
  - "How can a user access and launch the Ansys Electronics Desktop graphical interface using an OnDemand or JupyterLab system?"
  - "What specific steps must be taken within the graphical interface to configure HPC settings and run a sample antenna simulation?"
  - "What is the purpose of the `-batchoptions` flag and its associated parameters, such as license type and GPU settings, in the provided command?"
  - "How does the script utilize Slurm environment variables like `$SLURM_NTASKS` and `$SLURM_TMPDIR` to configure the simulation environment?"
  - "What role do the `#SBATCH` directives play in scheduling and allocating resources for this job on the cluster?"
  - "What terminal commands are required to set up the directory structure and copy the HFSS Antennas examples to the user's folder?"
  - "How do you perform a validation check on an opened .aedt example file within the software?"
  - "What is the exact menu navigation sequence to reset the Mesh/Solution options to their defaults before running the simulation?"
  - "How do you start a simulation and exit without saving the converged solution in AnsysEDT?"
  - "What specific commands should be executed if the AnsysEDT application crashes and fails to restart?"
  - "How must the license file be configured to utilize the SHARCNET Ansys license for free on an Alliance cluster?"
  - "How do you start a simulation and exit without saving the converged solution in AnsysEDT?"
  - "What specific commands should be executed if the AnsysEDT application crashes and fails to restart?"
  - "How must the license file be configured to utilize the SHARCNET Ansys license for free on an Alliance cluster?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[AnsysEDT](https://www.ansys.com/products/electronics) bundles electromagnetics simulation solutions such as Ansys HFSS, Ansys Maxwell, Ansys Q3D Extractor, Ansys SIwave, and Ansys Icepak using electrical CAD (ECAD) and mechanical CAD (MCAD) workflows. AnsysEDT also integrates with the complete Ansys portfolio of thermal, fluid, and mechanical solvers for comprehensive multiphysics analysis.

## Licensing

The Alliance is a hosting provider for AnsysEDT. This means we have the software installed on our clusters, but do not provide a generic license accessible to everyone. However, many institutions, faculties, and departments already have license servers that can be used if the legal aspects can be worked out. Network changes would need to be made to enable the license server to be reached from the cluster compute nodes. The Ansys software would then be able to check out licenses after loading the `ansysedt` module. For help contact [technical support](../support/technical_support.md).

### Configuring your license file

Specify your AnsysEDT license server by creating a file named `$HOME/.licenses/ansys.lic` consisting of two lines. See [Configuring your license file](ansys.md) on the Ansys wiki page for further details.

## Cluster batch job submission

AnsysEDT can be run interactively in batch (non-GUI) mode by first starting an `salloc` session with options `salloc --time=3:00:00 --tasks=8 --mem=16G --account=def-account` and then copy-pasting the full `ansysedt` command found in the last line of *script-local-cmd.sh*, being sure to manually specify `$YOUR_AEDT_FILE`.

### Slurm scripts

Jobs may be submitted to a cluster queue with the `sbatch script-name.sh` command using either of the following single node scripts. Please note these scripts are generic and may require modifications on various clusters. Before using them, specify the simulation time, memory, number of cores, and replace `YOUR_AEDT_FILE` with your input file name. A full listing of command line options can be obtained by starting AnsysEDT in [graphical mode](ansys.md#graphical-use) with commands `ansysedt -help` or `ansysedt -Batchoptionhelp` to obtain scrollable graphical popups.

=== "Single node (command line)"

```bash title="script-local-cmd.sh"
#!/bin/bash

#SBATCH --account=account      # Specify your account (def or rrg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=16G              # Specify memory (set to 0 to use all compute node memory)
#SBATCH --ntasks=8             # Specify number of cores to be used on a single node
#SBATCH --nodes=1              # Request one node (Do Not Change)

module load StdEnv/2023
#module load ansysedt/2023R2
module load ansysedt/2024R2.1

# Uncomment next line to run a test example:
#cp -f $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
cp -f $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

# Specify input file such as:
YOUR_AEDT_FILE="TransientGeoRadar.aedt"

# Remove previous output:
rm -rf "$YOUR_AEDT_FILE".* "${YOUR_AEDT_FILE}"results

# ---- do not change anything below this line ---- #

echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
echo -e "SLURM_TMPDIR= $SLURM_TMPDIR on $SLURMD_NODENAME\n"

export KMP_AFFINITY=disabled
ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:"$SLURM_NTASKS" \
-batchoptions "TempDirectory=$SLURM_TMPDIR HPCLicenseType=pool HFSS/EnableGPU=0" -batchsolve "$YOUR_AEDT_FILE"
```

=== "Single node (options file)"

```bash title="script-local-opt.sh"
#!/bin/bash

#SBATCH --account=account      # Specify your account (def or rrg)
#SBATCH --time=00-01:00        # Specify time (DD-HH:MM)
#SBATCH --mem=16G              # Specify memory (set to 0 to allocate all compute node memory)
#SBATCH --ntasks=8             # Specify number of cores to be used on a single node
#SBATCH --nodes=1              # Request one node (Do Not Change)

module load StdEnv/2023
#module load ansysedt/2023R2
module load ansysedt/2024R2.1

# Uncomment next line to run a test example:
#cp -f $EBROOTANSYSEDT/v232/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .
cp -f $EBROOTANSYSEDT/v242/Linux64/Examples/HFSS/Antennas/TransientGeoRadar.aedt .

# Specify input filename such as:
YOUR_AEDT_FILE="TransientGeoRadar.aedt"

# Remove previous output:
rm -rf "$YOUR_AEDT_FILE".* "${YOUR_AEDT_FILE}"results

# Specify options filename:
OPTIONS_TXT="Options.txt"

# Write sample options file
rm -f "$OPTIONS_TXT"
cat > "$OPTIONS_TXT" <<EOF
\$begin 'Config'
'TempDirectory'='$SLURM_TMPDIR'
'HPCLicenseType'='pool'
'HFSS/EnableGPU'=0
\$end 'Config'
EOF

# ---- do not change anything below this line ---- #

echo -e "\nANSYSLI_SERVERS= $ANSYSLI_SERVERS"
echo "ANSYSLMD_LICENSE_FILE= $ANSYSLMD_LICENSE_FILE"
echo -e "SLURM_TMPDIR= $SLURM_TMPDIR on $SLURMD_NODENAME\n"

export KMP_AFFINITY=disabled

ansysedt -monitor -UseElectronicsPPE -ng -distributed -machinelist list=localhost:1:"$SLURM_NTASKS" \
-batchoptions "$OPTIONS_TXT" -batchsolve "$YOUR_AEDT_FILE"
```

## Graphical use

To run AnsysEDT in graphical mode, use an [OnDemand](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)) or JupyterLab system to start a remote desktop as follows:

### OnDemand

1.  Connect to an OnDemand system using one of the following URLs in your laptop browser:
    *   [NIBI](https://docs.alliancecan.ca/wiki/Nibi#Access_through_Open_OnDemand_(OOD)): `https://ondemand.sharcnet.ca`
    *   FIR: `https://jupyterhub.fir.alliancecan.ca`
    *   NARVAL: `https://portail.narval.calculquebec.ca/`
    *   RORQUAL: `https://jupyterhub.rorqual.alliancecan.ca`
    *   TRILLIUM: `https://ondemand.scinet.utoronto.ca`
2.  Open a new terminal window in your desktop and run:
    *   `module load StdEnv/2023` (default)
    *   `module load ansysedt/2024R2.1` **OR** `ansysedt/2023R2`
    *   Type `ansysedt` in the terminal and wait for the GUI to start.
3.  Verify the following settings:
    *   The following only needs to be done once:
        *   Click `Tools -> Options -> HPC and Analysis Options -> Edit`.
        *   When the Analysis Configuration panel appears, untick `Use Automatic Settings`.
        *   Ensure the settings in the `Machine` tab correspond to requested desktop resources, such as:
            `| Tasks 1 | Cores 4 | Allocated_Cores | GPUs 0 | RAM 90 | tick Enabled |`
        *   Click the **OK** button to save any changes and close the `Analysis Configuration` panel.
        *   Click the **OK** button to close the `HPC and Analysis` Options panel.
4.  To retrieve the 2024R2.1 Antennas examples, copy its directory under your account as follows:
    ```bash
    module load ansysedt/2024R2.1
    mkdir -p ~/Ansoft/$EBVERSIONANSYSEDT; rm -rf ~/Ansoft/$EBVERSIONANSYSEDT/Antennas
    cp -a "$EBROOTANSYSEDT"/v242/Linux64/Examples/HFSS/Antennas ~/Ansoft/"$EBVERSIONANSYSEDT"
    ```
5.  Now to run the example:
    *   Open one of the Antennas examples `.aedt` files then click `HFSS -> Validation Check`.
    *   Click `Simulation -> Setup -> Advanced -> Mesh/Solution options -> Use Defaults`.
    *   Start simulation running by clicking `Simulation -> Analyze All`.
    *   To quit without saving the converged solution, click `File -> Close -> No`.
6.  If AnsysEDT crashes and will not restart, try running the following commands:
    ```bash
    pkill -9 -u "$USER" -f "ansys*|mono|mwrpcss|apip-standalone-service"
    rm -rf ~/.mw # AnsysEDT will re-run first-time configuration on startup
    ```

## Site-Specific

### SHARCNET license

The usage terms of the SHARCNET ANSYS License (which includes AnsysEDT) along with other various details may be found in the SHARCNET license section of the Ansys wiki and will not be repeated here.

#### License file

The SHARCNET Ansys license can be used for the AnsysEDT modules on any Alliance cluster by any researcher for free, by configuring your `ansys.lic` file as follows:

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license3.sharcnet.ca")
setenv("ANSYSLI_SERVERS", "2325@license3.sharcnet.ca")