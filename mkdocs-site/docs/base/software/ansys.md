---
title: "Ansys"
slug: "ansys"
lang: "base"

source_wiki_title: "Ansys"
source_hash: "522ed9dd26ada1060385a03b992e55f5"
last_synced: "2026-08-15T23:22:43.108655+00:00"
last_processed: "2026-08-15T23:29:01.168159+00:00"

tags:
  - software

keywords:
  - "SHARCNET"
  - "pkill -9 -u $USER -f \"ansys\""
  - "SHARCNET Ansys license"
  - "service pack"
  - "version compatibility"
  - "roberpj"
  - "Ansys license file"
  - "separate modules"
  - "Additive project"
  - "Ansys Educator Hub"
  - "simultaneous 16 jobs"
  - "elec_solve_hfss"
  - "license server configuration"
  - "Ansys HowTo videos"
  - "local server firewall"
  - "elec_solve_level2"
  - "275 licenses issued"
  - "X over SSH"
  - "module load ansys"
  - "512 per user limit"
  - "Ansys"
  - "resource utilization"
  - "OnDemand login node session"
  - "scaling tests"
  - "reduce job size"
  - "Ansys 2023R"
  - "ansys.lic"
  - "ansys.lic configuration"
  - "lmutil license query"
  - "Ansys 2024R1"
  - "400-core parallel job"
  - "license usage"
  - "license tie‑up"
  - "lmutil lmstat"
  - "LICSERVER"
  - "Service Pack Details"
  - "1 license in use"
  - "Ansys-related processes"
  - "X11 forwarding"
  - "512 HPC cores"
  - "license server"
  - "pkill -9 -e -u $USER -f \"ansys|mwrpcss|mwfwrapper|ENGINE\""
  - "Ansys documentation"
  - "ANSYS"
  - "elec_solve_level1"
  - "ans hpc licenses"
  - "cfd_solve_level1"
  - "overcommitted"
  - "slow GUI startup"
  - "future versions"
  - "FLEXPORT and VENDPORT ports"
  - "lmstat"
  - "Ansys Developer Portal"
  - "FLEXPORT"
  - "rogue processes"
  - "NAT nodes"
  - "Ansys licenses"
  - "Additive Manufacturing ACT extension"
  - "Ansys module"
  - "remote cluster"
  - "Ansys Webinar series"
  - "network outage or hung filesystem"
  - "Slurm script"
  - "salloc --x11"

questions:
  - "What steps must be taken to create and configure the $HOME/.licenses/ansys.lic file for accessing an Ansys license on Alliance clusters?"
  - "How does using the pre‑configured SHARCNET license server differ from using a local institutional Ansys license server in terms of setup and required information?"
  - "What firewall and network configuration actions are needed when a local Ansys license server has never been connected to an Alliance cluster before?"
  - "What actions should you take with the NAT node IP addresses once they are sent back to you?"
  - "Which firewall ports (FLEXPORT and VENDPORT) need to be opened, and why must they allow connections from all the provided IP addresses?"
  - "What specific entry in the Ansys license file must be checked to ensure the <servername> value is correctly resolvable from the remote cluster?"
  - "How can you verify that your ansys.lic file is correctly configured and working with the license server on a cluster?"
  - "What does the forward‑compatibility rule for Ansys versions imply for loading and running simulation files created with older or newer releases?"
  - "How are service packs for Ansys releases handled in the module system, and how can users load the latest version with the appropriate service pack?"
  - "What are the permitted academic uses and prohibited commercial uses of the SHARCNET Ansys license?"
  - "What are the current per‑researcher core and job limits for the SHARCNET Ansys license, and how will these limits change after April 1 2026?"
  - "How should a user configure the ansys.lic file and query the number of Ansys licenses in use on the Alliance clusters?"
  - "Why might some user groups choose to keep using an earlier Ansys release or service pack instead of upgrading?"
  - "How can users find a detailed description of what each service pack does in Ansys 2024R1?"
  - "What is the benefit of providing separate modules for each Ansys service pack?"
  - "What occurs when a 400‑core parallel job is submitted while only four anshpc licenses are free?"
  - "What are the two options a user can take when there are not enough anshpc licenses for their job?"
  - "Why can the actual number of anshpc licenses available to a user be significantly lower than the advertised 512‑license per‑user limit?"
  - "What are the IDs, remaining times, and allocated nodes/CPUs for the two running jobs shown in the squeue output?"
  - "How many total ANSYS licenses are issued for each feature (e.g., anshpc, cfd_solve_level1) and how many of those licenses are currently in use?"
  - "On which compute nodes (e.g., c630, c627) are the user's ANSYS license sessions running, and what are the corresponding process IDs?"
  - "How many total licenses have been issued for each of the elec_solve products listed?"
  - "How many licenses are currently in use for each of those products?"
  - "What does the HTML formatting (e.g., `<div style=\"font-size:85%; background-color: #E0FFFF; ...>`) suggest about how this information is displayed?"
  - "How can you release Ansys licenses that remain occupied by rogue processes on a desktop or compute node?"
  - "What are the required steps to download, install, and load the Additive Manufacturing ACT extension on a cluster?"
  - "Which commands and actions should be used to run a single Additive Manufacturing job in an OnDemand session and verify that no lingering Ansys processes are consuming resources?"
  - "What command does the text recommend for terminating rogue Ansys‑related processes?"
  - "Why can lingering Ansys GUI processes consume valuable licenses on an OnDemand login node?"
  - "In which situations might the Ansys processes become unkillable until disk access is restored?"
  - "What steps must be taken in Workbench before submitting an Additive project to a Slurm queue, and how can the simulation file be preserved between test runs?"
  - "How can you monitor the resource utilization of a running Additive job on the compute nodes, and what does the sample `srun` output indicate about CPU usage?"
  - "After a job finishes, how are wall‑clock times used to perform scaling tests, and what criterion suggests that adding more cores will be beneficial?"
  - "What is required to access older versions such as Ansys 2023R[1|2]?"
  - "Where can users find the official Ansys developer documentation?"
  - "Which learning resources are listed for gaining additional Ansys knowledge?"
  - "What are the main performance drawbacks of using X forwarding over SSH compared to VNC for running GUI applications on a cluster?"
  - "Which prerequisites and configuration steps are necessary to set up X forwarding (e.g., X server, SSH options, resource allocation) before launching a program?"
  - "In what scenarios might a user still prefer X over SSH despite its slower startup times and interactive response delays?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: false
  qa_generated: false
---

[Ansys](http://www.ansys.com/) is a software suite for engineering simulation and 3-D design. It includes packages such as [Ansys Fluent](https://www.ansys.com/products/fluids/ansys-fluent) and [Ansys CFX](http://www.ansys.com/products/fluids/ansys-cfx).

Please also refer to:
* [Graphical use of Ansys](../general/graphical_use_of_ansys.md)
* [Cluster batch job submission with Ansys](../running-jobs/cluster_batch_job_submission_with_ansys.md)

## Licensing
The Alliance is a hosting provider for Ansys. This means that we have the software installed on our clusters, but we do not provide a generic license accessible to everyone. However, many institutions, faculties, and departments already have licenses that can be used on our clusters. Once the legal aspects are worked out for licensing, there will be remaining technical aspects. The license server on your end will need to be reachable by our compute nodes. This will require our technical team to get in touch with the technical people managing your license software. In some cases, this has already been done. You should then be able to load the Ansys module, and it should find its license automatically. If this is not the case, please contact our [technical support](../support/technical_support.md) to arrange this.

### Configuring your license file
Our module for Ansys is designed to look for license information in a few places. One of those places is your `/home` folder. You can specify your license server by creating a file named `$HOME/.licenses/ansys.lic` as shown below. Customize the file by replacing FLEXPORT and LICSERVER with the appropriate values for your server.

```
FILE: ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "**FLEXPORT**@LICSERVER")
```

The following table provides established values for the SHARCNET license server.

| License | System/Cluster              | LICSERVER                  | FLEXPORT | NOTES            |
| :------ | :-------------------------- | :------------------------- | :------- | :--------------- |
| SHARCNET | Nibi/Fir/Narval/Rorqual/Trillium | `license1.computecanada.ca` | `1055`   | currently operational |

### Local license servers
Before a local institutional Ansys license server can be used on our clusters, firewall changes will need to be done on both the server and the cluster sides. For many Ansys servers, this work has already been done and they can be used by following the steps in [Ready to use](#ready-to-use) below. For Ansys servers that have never been used on our clusters, an additional step must be done as shown under [Setup required](#additional-steps), also below.

#### Ready to use
To use a local institutional Ansys license server with an Alliance cluster whose network/firewall connections have already been set up, contact your Ansys server administrator and get the following pieces of information for the license server:
1. the Ansys flex port (FLEXPORT) number, commonly 1055
2. the fully qualified hostname (LICSERVER)

Now, configure your `~/.licenses/ansys.lic` file by plugging in the values, and you are done.

#### Additional steps
To use a local Ansys license server with an Alliance cluster whose network/firewall connection have never been set up before, you will also need to get the following from your Ansys server administrator:
3. the statically configured Ansys vendor port (VENDPORT) number.

Send items 1 -> 3 by email to [technical support](../support/technical_support.md) and mention which Alliance cluster you want to run Ansys jobs on. An Alliance system administrator will then open the outbound cluster firewall (if necessary) so license checkout requests can reach your license server from the cluster's compute nodes. A range of IP addresses (known as cluster NAT nodes) will then be sent back to you. Give these IP addresses to your local network administrator and request the local server firewall FLEXPORT and VENDPORT ports be opened to allow connections from all of them. Also ask the administrator to check that the line containing `SERVER <servername> <host id> <lmgrd port>` found at the top of the Ansys license file contains either LICSERVER or IP_ADDRESS for the `<servername>` value as this must be resolvable from the remote cluster.

## Checking out a license
To test if your `ansys.lic` is configured and working properly with your license server, run the following sequence of commands on the cluster where you will be submitting jobs.

```bash
[login-node:~] cd /tmp
[login-node:/tmp] salloc --time=1:0:0 --mem=1000M --account=def-YOURUSERID
[compute-node/tmp] module load StdEnv/2023; module load ansys/2025R2.04
[compute-node:/tmp] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil lmstat -c $ANSYSLMD_LICENSE_FILE | grep "ansyslmd: UP" 1> /dev/null && echo Success || echo Fail
```
`Success` output indicates license checkouts should work when jobs are submitted to the queue.
`Fail` output indicates a problem with the licensing setup somewhere, and jobs will likely fail.

If there is an Ansys license server checkout problem, the following message will appear in Slurm output files when Fluent jobs are started by Slurm scripts in the queue *OR* when Fluent is started interactively, simply by doing the following:

```bash
[compute-node:/tmp] fluent -g 2d -n 2
```
```text
Connected License Server List:	<Shared_Web_License_Server>
Hit return to exit.
```

## Version compatibility
Ansys simulations are typically forward compatible, but **NOT** backward compatible. This means that simulations created using an older version of Ansys can be expected to load and run fine with any newer version. For example, a simulation created and saved with `ansys/2022R2` should load and run smoothly with `ansys/2023R2`, but **NOT** the other way around. While it may be possible to start a simulation running with an older version, random error messages or crashing will likely occur. Regarding Fluent simulations, if you cannot recall which version of Ansys was used to create your case file, try grepping it as follows to look for clues:

```bash
$ grep -ia fluent combustor.cas
```
```text
   (0 "fluent15.0.7  build-id: 596")
```

```bash
$ grep -ia fluent cavity.cas.h5
```
```text
   ANSYS_FLUENT 24.1 Build 1018
```

### Platform support
Ansys provides [detailed platform support information](https://www.ansys.com/it-solutions/platform-support/previous-releases) describing software/hardware compatibility for the current and previous releases. This is of special interest since it shows which packages are supported under Windows, but not under Linux, and thus not on the Alliance clusters (e.g., SpaceClaim).

### What's new
Information for the latest Ansys release can be found [here](https://www.ansys.com/products/release-highlights) (Ansys 2026 R1, as of May 2026). Posts for previous releases can be found on the [Ansys blog](https://www.ansys.com/blog) and then scrolling down to the FILTERS search bar. Inputting for example *What’s New Fluent 2024 GPU* should pull up a document containing the latest GPU support information for that release. The [Press Release](https://www.ansys.com/news-center/press-releases) search bar is also a good way to find release-specific information.

### Service packs
Starting with Ansys 2024, a separate Ansys module will appear on the clusters with a decimal and two digits following the release number whenever a service pack is installed over the initial release. For example, the initial 2024 release with no service pack applied may be loaded with `module load ansys/2024R1` while a module with service pack 3 applied will be loaded with `module load ansys/2024R1.03`. If a service pack is already available by the time a new release is to be installed, only a module for that service pack number will most likely be installed, unless a request to install the initial release is also received.

Most users will likely want to load the latest module version equipped with the latest installed service pack, which can be achieved with `module load ansys`. While it's not expected service packs will impact numerical results, the changes they make are extensive and so, if computations have already been done with the initial release or an earlier service pack, some groups may prefer to continue using it. Having separate modules for each service pack makes this possible. Starting with Ansys 2024R1, a detailed description of what each service pack does can be found by searching this [link](https://storage.ansys.com/staticfiles/cp/Readme/release2024R1/info_combined.pdf) for *Service Pack Details*. Future versions will presumably be similarly searchable by manually modifying the version number.

## Site-specific usage

### SHARCNET license
The SHARCNET Ansys license is free for academic use by **any** Alliance researcher on **any** Alliance system. The installed software does not have any solver or geometry limits. The SHARCNET license may be used for ***Publishable Academic Research***, but not for any private/commercial purposes as this is strictly prohibited by the license terms. The SHARCNET Ansys license is based on the Multiphysics Campus Solution and includes products such as: HF, EM, Electronics HPC, Mechanical, CFD, ROCKY and LS-DYNA as described [here](https://www.ansys.com/academic/educator-tools/academic-product-portfolio). Lumerical software is included in recent Ansys module versions, however it is NOT covered by the SHARCNET license. SpaceClaim software is not installed with any Ansys module since there is no Linux version available; it is technically covered by the SHARCNET license however.

!!! tip "Scaling Tests and Resource Utilization"
    ⚙️ Scaling tests should be run before launching long jobs to determine the optimal scalable job size so that the limited licenses and hardware is used as efficiently as possible, and total job run and startup times are minimized. Parallel jobs that do not achieve at least 50% CPU utilization will probably be flagged by the system, resulting in a follow up by an Alliance team member.

#### License limits
The SHARCNET Ansys license is made available on a first come first serve basis. It currently permits each researcher to run a maximum of simultaneous 16 jobs using a total of up to 512 HPC cores across all clusters, therefore any of the following maximum job size combinations can be run simultaneously: 1x512, 2x256, 4x128, 8x64, 16x32 or more commonly one of these full node combinations: 1x384, 2x192 or 1x192 cores. Note however that the SHARCNET license is oversubscribed so there is potential for jobs to fail on startup if all (or nearly all) of the 1986 `anshpc` licenses in the SHARCNET license pool are in use. Should this occur, you will need to manually resubmit your job to the queue. As there have been an increasing number of license shortage (DENIED) instances where jobs fail on startup, the total `anshpc` core limit per researcher will be decreased from 512 to 384 on April 1, 2026. If you need to use more than 384 HPC cores for your research, either use the local Ansys License server at your institution if one is available, OR open a ticket to request purchasing additional licenses for the SHARCNET license and these would be reserved for your own or your groups exclusive use.

#### License file
As of February 2026, the `license3.sharcnet.ca` license server has been permanently shut down. To use the SHARCNET Ansys license on any Alliance cluster, simply configure your `ansys.lic` file as follows:

```bash
[username@cluster:~] cat ~/.licenses/ansys.lic
setenv("ANSYSLMD_LICENSE_FILE", "1055@license1.computecanada.ca")
```

#### License query
To show the number of Ansys licenses in use by your username and the total in use by all users, run:

```bash
ssh nibi.alliancecan.ca
module load ansys
$EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil \
lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
```

#### Example
Consider the case where a user submits an 8-core Fluent job and 32-core Fluent job. Once both jobs start running, the user runs the `lmutil` query command and the output shown below is generated. Here, we see that a total of (8-4) + (32-4) = 32 `anshpc` licenses are used by the two jobs. As a result the total number of licenses increases from 1568 to 1600 so that only (1986-1600) = 386 of them remain available for additional jobs submitted by all users. Therefore, if a 400-core parallel job attempts to start at that moment, it will fail to start since (400-4) = 396 `anshpc` licenses would be required. The user has two options, either wait for a sufficient number of licenses to come available OR reduce the job size to 390 cores or less and resubmit immediately. This example focuses on the `anshpc` feature since it is most generously overcommitted to allow any user to submit the largest job possible, but it also shows that the actual number of licenses available per user may sometimes be far less than the 512 per user limit would suggest.

```text
[l2(nibi):~] sq
            JOBID     USER        ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS MIN_MEM NODELIST (REASON)
         10161023  roberpj   cc-debug_cpu script-flu-int   R    2:57:19     4    8     N/A      4G c[630-633] (None)
         10161033  roberpj   cc-debug_cpu script-flu-int   R    2:58:25    16   32     N/A      4G c[627-628,630-633,637,642,645,655,657,662,665,667,669,682] (None)
[l2(nibi):~]
[l2(nibi):~] module load ansys
[l2(nibi):~]
[l2(nibi):~] $EBROOTANSYS/v$(echo ${EBVERSIONANSYS:2:2}${EBVERSIONANSYS:5:1})/licensingclient/linx64/lmutil  \
              lmstat -c $ANSYSLMD_LICENSE_FILE -a | grep "Users of\|$USER" | grep -v " Total of 0 licenses in use"
 Users of anshpc:  (Total of 1986 licenses issued;  Total of 1600 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 2579), start Wed 3/11 16:46, 4 licenses, PID: 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 5716), start Wed 3/11 16:48, 28 licenses, PID: 510058
 Users of cfd_base:  (Total of 275 licenses issued;  Total of 19 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10327), start Wed 3/11 16:46, PID: 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 7171), start Wed 3/11 16:47, PID: 510058
 Users of cfd_preppost:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of cfd_preppost_pro:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of cfd_solve_level1:  (Total of 275 licenses issued;  Total of 18 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 7994), start Wed 3/11 16:46, PID: 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 6200), start Wed 3/11 16:47, PID: 510058
 Users of cfd_solve_level2:  (Total of 275 licenses issued;  Total of 18 licenses in use)
    roberpj c630 c630.nibi.sharcnet 1238925 (v2025.0506) (license1.computecanada.ca/1055 10520), start Wed 3/11 16:46, PID: 1239140
    roberpj c627 c627.nibi.sharcnet 509821 (v2025.0506) (license1.computecanada.ca/1055 375), start Wed 3/11 16:47, PID: 510058
 Users of elec_solve_hfss:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of elec_solve_level1:  (Total of 275 licenses issued;  Total of 1 license in use)
 Users of elec_solve_level2:  (Total of 275 licenses issued;  Total of 1 license in use)
```

!!! warning "Rogue Processes"
    🕵️ A rare situation can occur where the output from the license query command reveals there are some Ansys licenses unexpectedly still in use by your username on some desktop or compute node. This would happen if for instance an Ansys GUI program run on a remote desktop node was not shut down cleanly, leaving some Ansys processes still running, or an Ansys program crashes on a cluster compute node inside an `salloc` session that was being run interactively from the command line, once again leaving some rogue Ansys processes still running. To kill all potentially responsible Ansys rogue processes, either close the desktop, `scancel` the `salloc` session, or simply open a terminal window on the affected node and issue the `pkill -9 -e -u $USER -f "ansys"` command. Any Ansys licenses that were being held open should immediately be returned to the SHARCNET license server and become available for use again by yourself or other researchers.

## Additive Manufacturing
To get started, configure your `~/.licenses/ansys.lic` file to point to a license server that has a valid Ansys Mechanical license. This must be done on all systems where you plan to run the software.

### Enabling Additive
This section describes how to make the Ansys Additive Manufacturing ACT extension available for use in your project. The steps must be performed on each cluster for each Ansys module version where the extension will be used. Any extensions needed by your project will also need to be installed on the cluster as described below. If you get warnings about missing un-needed extensions (such as ANSYSMotion), uninstall them from your project.

#### Downloading extensions
* download `AdditiveWizard.wbex` from https://catalog.ansys.com/,
* upload `AdditiveWizard.wbex` to the cluster where it will be used.

#### Starting Workbench
* see the Workbench section in [Graphical use of Ansys](../general/graphical_use_of_ansys.md),
* `File -> Open` your project file (ending in `.wbpj`) into the Workbench GUI.

#### Opening the extensions manager
* click on the ACT start page and the ACT home page tab will open,
* click `Manage Extensions` and the extensions manager will open.

#### Installing extensions
* click on the box with the large `+` sign under the search bar,
* navigate to select and install your `AdditiveWizard.wbex` file.

#### Loading extensions
* click to highlight the `AdditiveWizard` box (loads the AdditiveWizard extension for the current session only),
* click on the lower right corner arrow in the `AdditiveWizard` box and select *Load extension* (loads the extension for current AND future sessions).

#### Unloading extensions
* click to un-highlight the `AdditiveWizard` box (unloads extension for the current session only),
* click on the lower right corner arrow in the `AdditiveWizard` box and select *Do not load as default* (extension will not load for future sessions).

### Running Additive

#### OnDemand
You can run a single Ansys Additive Manufacturing job in a graphical OnDemand session by following these steps:

* Start Workbench as described above in Enabling Additive;
* click on `File -> Open`, select *test.wbpj* and click on `Open`;
* click on `View -> reset workspace` if you get a grey screen;
* start Mechanical, clear generated data, tick `Distributed`, specify cores;
* click on `File -> Save Project -> Solve`.

**Check utilization**
```bash
# Open another terminal and run
top -u $USER
# OR
ps u -u $USER | grep ansys

# Kill rogue processes from previous runs with
pkill -9 -e -u $USER -f "ansys|mwrpcss|mwfwrapper|ENGINE"
```

Please note that rogue Ansys-related processes can persistently tie up valuable licenses inside a running OnDemand login node session if an Ansys GUI session (Fluent, Workbench, Mechanical, etc.) is not cleanly terminated or is terminated unexpectedly by a network outage or a hung filesystem. If the latter is to blame, the processes may not be killable until normal disk access is restored.

#### Cluster
**Project preparation**

Before submitting a newly uploaded Additive project to a cluster queue (with `sbatch scriptname`), certain preparations must be done. To begin, open your simulation with the Workbench GUI (as described in the Cluster Batch Job Submission - WORKBENCH section above) in the same directory that your job will be submitted from and then save it again. Be sure to use the same Ansys module version that will be used for the job. Next, create a Slurm script (as explained in the Cluster Batch Job Submission - WORKBENCH section above). To perform parametric studies, change `Update()` to `UpdateAllDesignPoints()` in the Slurm script. Determine the optimal number of cores and memory by submitting several short test jobs. To avoid needing to manually clear the solution **and** recreate all the design points in Workbench between each test run, either 1) change `Save(Overwrite=True)` to `Save(Overwrite=False)` or 2) save a copy of the original `YOURPROJECT.wbpj` file and corresponding `YOURPROJECT_files` directory. Optionally, create and then manually run a replay file on the cluster in the respective test case directory between each run, noting that a single replay file can be used in different directories by opening it in a text editor and changing the internal `FilePath` setting.

```bash
module load ansys/2019R3
rm -f test_files/.lock
runwb2 -R myreplay.wbjn
```

**Resource utilization**

Once your Additive job has been running for a few minutes, a snapshot of its resource utilization on the compute node(s) can be obtained with the `srun` command. Sample output corresponding to an eight-core submission script is shown next. We see that two nodes were selected by the scheduler:

```bash
[gra-login1:~] srun --overlap --jobid=myjobid top -bn1 -u $USER | grep R | grep -v top
```
```text
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
 22843 demo   20   0 2272124 256048  72796 R  88.0  0.2  1:06.24  ansys.e
 22849 demo   20   0 2272118 256024  72822 R  99.0  0.2  1:06.37  ansys.e
 22838 demo   20   0 2272362 255086  76644 R  96.0  0.2  1:06.37  ansys.e
   PID USER   PR  NI    VIRT    RES    SHR S  %CPU %MEM    TIME+  COMMAND
  4310 demo   20   0 2740212 271096 101892 R 101.0  0.2  1:06.26  ansys.e
  4311 demo   20   0 2740416 284552  98084 R  98.0  0.2  1:06.55  ansys.e
  4304 demo   20   0 2729516 268824 100388 R 100.0  0.2  1:06.12  ansys.e
  4305 demo   20   0 2729436 263204 100932 R 100.0  0.2  1:06.88  ansys.e
  4306 demo   20   0 2734720 431532  95180 R 100.0  0.3  1:06.57  ansys.e
```

**Scaling tests**

After a job completes, its wall-clock time can be obtained with `seff myjobid`. Using this value, scaling tests can be performed by submitting short test jobs with an increasing number of cores. If the wall-clock time decreases by ~50% when the number of cores is doubled, additional cores may be considered.

## Help resources
The official full documentation for recent versions Ansys 202[4|5]R[1|2] is available [here](https://ansyshelp.ansys.com/public/account/secured?returnurl=/Views/Secured/main_page.html?lang=en). Documentation for older versions such as Ansys 2023R[1|2] however requires [login](https://ansyshelp.ansys.com/login). Developer documentation can be found in the [Ansys Developer Portal](https://developer.ansys.com). Additional learning resources include the [Ansys HowTo videos](https://www.youtube.com/@AnsysHowTo/videos), the [Ansys Educator Hub](https://innovationspace.ansys.com/educator-hub/) and the [Ansys Webinar series](https://www.ansys.com/events/ansys-academic-webinar-series).

!!! warning "XoverSSH Legacy Note"
    **XoverSSH Legacy Note**: Some programs can be run remotely on a cluster compute node by forwarding X over SSH to your local desktop. Unlike VNC, this approach is not tested and not supported since it relies on a properly set up X display server for your particular operating system OR the selection, installation and configuration of a suitable X client emulator package such as MobaXterm. Most users will find interactive response times unacceptably slow for basic menu tasks, let alone for more complex tasks such as those involving graphics rendering. Startup times for GUI programs can also be very slow depending on your Internet connection. For example, in one test it took 40 minutes to fully start the GUI over SSH while starting it with vncviewer required only 34 seconds. Despite the potential slowness, using this method to connect may still be of interest if your only goal is to open a simulation and perform some basic menu operations or run some calculations, and response delays can be tolerated. The basic steps are given here as a starting point:
    1. `ssh -Y username@alliancecan.ca`
    2. `salloc --x11 --time=1:00:00 --mem=16G --cpus-per-task=4 [--gpus-per-node=1] --account=def-mygroup`
    3. once connected onto a compute node, try running `xclock`. If the clock appears on your desktop, proceed to load the desired Ansys.