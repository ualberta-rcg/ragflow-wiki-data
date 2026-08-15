---
title: "Graphical use of Ansys"
slug: "graphical_use_of_ansys"
lang: "base"

source_wiki_title: "Graphical use of Ansys"
source_hash: "abc0e3cdf4f6c88fb82316395cc5dab6"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:40:09.047086+00:00"

tags:
  []

keywords:
  - "GPU node vs Mesa"
  - "mpiexec bootstrap_proxy error"
  - "intelmpi"
  - "Fluent Launcher"
  - "GPU resource"
  - "I_MPI_HYDRA_BOOTSTRAP=ssh"
  - "Fluent"
  - "Workbench"
  - "JupyterHub desktop"
  - "cfx5 -graphics ogl"
  - "I_MPI_HYDRA_BOOTSTRAP"
  - "Workbench (VNC)"
  - "OOD Compute Desktop"
  - "runwb2 desktop icon"
  - "HOOPS_PICTURE"
  - "Nibi"
  - "Ansys Fluent"
  - "runwb2"
  - "ansys/2025R1"
  - "HOOPS_PICTURE=opengl2-mesa"
  - "Nibi cluster"
  - "Fluid Flow (Fluent)"
  - "OnDemand desktop"

questions:
  - "What steps must be followed to launch Ansys Fluent on an OnDemand desktop, including module loading and environment variable configuration?"
  - "How do the required HOOPS_PICTURE environment variable values differ between a compute node with a GPU and one without a GPU?"
  - "Why is the variable I_MPI_HYDRA_BOOTSTRAP=ssh mandatory on Nibi, and what error occurs if it is not set?"
  - "What are the common reasons for the “Unable to run bstrap_proxy” error in mpiexec on the Nibi cluster, and what steps can be taken to troubleshoot or fix it?"
  - "How should CFX be started from an OnDemand desktop when a GPU has been requested versus when no GPU was requested?"
  - "What are the required module loads, commands, and environment variable settings to launch Workbench (and optionally Fluent) on a compute node with or without a GPU on the Nibi cluster?"
  - "What environment variable must be manually set when running Fluent on Nibi with Intel MPI?"
  - "What specific error occurs if the I_MPI_HYDRA_BOOTSTRAP variable is not set while starting Fluent inside OOD Compute Desktop sessions?"
  - "What corrective actions should be taken if Fluent crashes due to the missing environment variable?"
  - "How do you start Fluent from within Workbench and navigate to the “Fluent Launcher” panel?"
  - "Which options in the left‑hand “Analysis” menu must be selected before clicking “Setup” for a Fluid Flow simulation?"
  - "What environment variable needs to be set on the Nibi cluster, and where should it be entered?"
  - "What steps are required to create and use the custom “workbench‑mesa.desktop” icon for launching Workbench in Mesa mode on a compute node without a GPU?"
  - "How should the modules and environment variables be loaded to run Ensight in graphical mode as described in the guide?"
  - "Which module load command starts Rocky in graphical mode, and what are the distinct purposes of the RockySolver and RockySchedular commands?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

To run [Ansys](../software/ansys.md) programs in graphical mode using an OnDemand or JupyterHub desktop, click on one of the following links:

*   [NIBI](../clusters/nibi.md#access-through-open-ondemand-ood): `https://ondemand.sharcnet.ca`
*   [FIR](../software/fir.md): `https://jupyterhub.fir.alliancecan.ca`
*   [RORQUAL](../clusters/rorqual.md): `https://jupyterhub.rorqual.alliancecan.ca`
*   [Narval](../clusters/narval.md): `https://jupyterhub.narval.alliancecan.ca/`
*   TRILLIUM: `https://ondemand.scinet.utoronto.ca`

A job submission web page will appear. Configure the resources required for your interactive desktop session and click on *Launch* or *Start*. If either accelerated graphics or computations will be conducted from within your desktop session, be sure to specify a GPU resource. Load an Ansys module on the desktop. If you started a JupyterLab-powered desktop, this can be done by clicking in the menu on the left; however, if you started an OnDemand desktop manually, type `module load ansys/version` on the command line. To start one of the common Ansys programs such as Fluent, CFX, Workbench, and so forth, refer to the following sections which provide advice for setting environment variables and arguments required by VirtualGL or Mesa-based graphical environments, depending on whether a node with a GPU resource was specified or not.

## Fluent

To start Ansys Fluent from the command line on an OnDemand desktop, open a terminal window and run:

```bash
module load StdEnv/2023 ansys/2025R2.04
fluent
```

When the *Fluent Launcher* popup selector panel appears, click on the *Environment* tab and copy/paste the environment variable settings from one of the following two subsections, depending on whether you started your OnDemand session with a GPU for graphical acceleration. Do not include the text in parentheses as these are comments, and do not put `export` in front of any variable name. If the graphics console window becomes corrupted when starting the GUI, restart Fluent, setting `HOOPS_PICTURE=null` to disable the creation of the graphics panel.

### Compute node (no GPU requested)

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # required on Nibi w/ Intel MPI
HOOPS_PICTURE=opengl2-mesa # version 2025R1 or newer
HOOPS_PICTURE=x11/lin # version 2024R2.04 or older
```
Click on the *Start* button.

### Compute node (with GPU requested)

To use hardware accelerated graphics with Fluent on Nibi, choose a t4 (15GB) from the GPU selector pulldown list. Doing this ensures that the environment variables used by VirtualGL to enable accelerated OpenGL graphics calls are automatically set up inside your desktop environment for the current session. Once your desktop appears, open a terminal window and start Workbench as follows:

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # required on Nibi
HOOPS_PICTURE=opengl2 # version 2025R1 or newer
HOOPS_PICTURE=opengl # version 2024R2.04 or older
```
Click on the *Start* button.

!!! warning "Nibi and Intel MPI"
    When running Fluent on Nibi, the environment variable `I_MPI_HYDRA_BOOTSTRAP=ssh` must be manually set; otherwise, Fluent will crash when started inside OOD Compute Desktop sessions when Intel MPI is used. Error output such as the following will be created. Should this occur, completely exit Fluent, cleanly shut down Workbench and start over.

    ```
    [mpiexec@g4.nibi.sharcnet] Error: Unable to run bstrap_proxy on g4.nibi.sharcnet (pid 2251587, exit code 256)
    [mpiexec@g4.nibi.sharcnet] poll_for_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:157): check exit codes error
    [mpiexec@g4.nibi.sharcnet] HYD_dmx_poll_wait_for_proxy_event (../../../../../src/pm/i_hydra/libhydra/demux/hydra_demux_poll.c:206): poll for  event error
    [mpiexec@g4.nibi.sharcnet] HYD_bstrap_setup (../../../../../src/pm/i_hydra/libhydra/bstrap/src/intel/i_hydra_bstrap.c:1063): error waiting for event
    [mpiexec@g4.nibi.sharcnet] Error setting up the bootstrap proxies
    ```

## CFX

When starting CFX from an OnDemand desktop, the following arguments may be specified on the terminal window command line. Use `ogl` if you requested a GPU when the desktop was started and use `mesa` if you did not.

```bash
cfx5 -graphics mesa # no GPU requested
cfx5 -graphics ogl # with GPU requested
```

## Mapdl

The following steps for starting the Mechanical APDL GUI from the command line of a terminal window should work regardless of whether you have started your OnDemand desktop on a compute node with or without a GPU.

```bash
module load StdEnv/2023 ansys/2022R2 # or newer versions
```
*   `mapdl -g`
*   or, `launcher` then click on the `RUN` button

## Workbench

This section shows how to start Workbench (and optionally Fluent) on either an OnDemand desktop or a JupyterLab desktop.

### OnDemand desktop

#### Compute node (no GPU requested) or basic desktop

If accelerated graphics are not required, specify *GPU Node* to select a compute node without a GPU. Doing this uses Mesa software emulation for OpenGL calls, instead of running on a more expensive and difficult to reserve GPU node.

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

To start Fluent from within Workbench, click on *Fluid Flow (Fluent)* or *Fluent with Fluent Meshing* in the *Analysis* menu on the left, and click on *Setup* in the centre canvas *Fluid Flow (Fluent)* popup. Once the *Fluent Launcher* selector panel popup appears, click on the *Environment* tab and copy/paste the following environment variable settings:

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # required on the Nibi cluster only when using Intel MPI
HOOPS_PICTURE=opengl2-mesa # optional for 2025R1 or newer
```
Click on the *Start* button.

#### Compute node (with GPU requested)

If accelerated graphics are required on the Nibi cluster, choose t4 (15GB) from the GPU selector pulldown list. Doing this will ensure that the environment variables used by VirtualGL to enable accelerated OpenGL graphics calls are automatically set up inside your desktop environment for the current session. Once your desktop appears, open a terminal window and start Workbench as follows:

```bash
module load StdEnv/2023 ansys/2025R2.04
runwb2
```

To start Fluent from within Workbench, click on *Fluid Flow (Fluent)* or *Fluent with Fluent Meshing* in the left-hand *Analysis* menu, and click on *Setup* in the centre canvas *Fluid Flow Fluent* popup. Once the *Fluent Launcher* selector panel popup appears, click on the *Environment* tab and copy/paste the following environment variable settings.

```bash
I_MPI_HYDRA_BOOTSTRAP=ssh # required on the Nibi cluster only
HOOPS_PICTURE=opengl2 # optional for 2025R1 or newer
```
Click on the *Start* button.

### JupyterHub desktop

#### Compute node (no GPU requested)

1.  Click to load `ansys/2025R1` (or newer version) in the desktop menu on the left.
2.  Click on the *Workbench (VNC)* icon.

    !!! note "Addressing Corrupted Graphics in Workbench Applications"
        If the graphics of any application (such as Fluent) started within Workbench appear unusable because they seem corrupted, you can try setting `HOOPS_PICTURE=opengl2-mesa` in the *Fluent Launcher* window.

        Alternatively, you can create a custom `runwb2` desktop icon to start Workbench in Mesa mode. Follow these steps:

        1.  Exit Workbench and open a terminal window. Copy/paste `cd ~/Desktop; cp -p $(realpath workbench.desktop) workbench-mesa.desktop` into the *Remote Clipboard*.
        2.  Open the newly created file in a text editor such as nano with:
            ```bash
            nano ~/Desktop/workbench-mesa.desktop
            ```
        3.  Change all instances of `runwb2` in the file. Save the changes and exit the editor.
        4.  Now refresh the Jupyter desktop by pressing the key combination *Control-R*. The new icon will now appear in the desktop. Double-click on it to start Workbench. The new icon will persist for future sessions until manually deleted with:
            ```bash
            rm -f ~/Desktop/workbench-mesa.desktop
            ```

#### Compute node (with GPU requested)

1.  Click to load `ansys/2025R1` (or newer version) in the desktop menu.
2.  Click the *Workbench (VNC)* icon.

## Ensight

```bash
module load StdEnv/2023 ansys/2022R2; A=222; B=5.12.6
export LD_LIBRARY_PATH=$EBROOTANSYS/v$A/CEI/apex$A/machines/linux_2.6_64/qt-$B/lib
ensight -X
```

## Rocky

Load the following modules:

```bash
module load StdEnv/2023 ansys/2025R2.04 # or 2025R1, 2025R1.02, 2025R2
```
*   The `Rocky` command starts Rocky in graphical mode.
*   The `RockySolver` command runs the solver directly from the command line.
*   The `RockyScheduler` GUI starts a GUI to submit/run jobs on the current node.

## Electronics

See [our AnsysEDT wiki page](../software/ansysedt.md).