---
title: "CESM"
slug: "cesm"
lang: "base"

source_wiki_title: "CESM"
source_hash: "b7ba1a44e9d0833ae2a216645053f3f6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:56:38.688854+00:00"

tags:
  []

keywords:
  - "queues"
  - "NETCDF_PATH"
  - "CIME_OUTPUT_ROOT"
  - "BATCH_SYSTEM"
  - "job submission"
  - "OMP_STACKSIZE"
  - "netcdf-fortran-mpi"
  - "lmod"
  - "nibi"
  - "module"
  - "netcdf"
  - "official template"
  - "Narval"
  - "directives"
  - "DIN_LOC_ROOT_CLMFORC"
  - "config_batch.xml"
  - "submit_args"
  - "slurm"
  - "intel"
  - "compiler"
  - "env"
  - "NETLIB_LAPACK_PATH"
  - "NETCDF_C_PATH"
  - "module_system"
  - "Community Earth System Model"
  - "DOUT_S_ROOT"
  - "sbatch"
  - "config_machines.xml"
  - "Coupled Model"
  - "checkout externals"
  - "XML Files"
  - "CESM 2.1"
  - "environment_variables"
  - "ntasks-per-node"
  - "computecanada"
  - "SUPPORTED_BY"
  - "Niagara"
  - "job_id"
  - "I_MPI_CC"
  - "Local batch file"
  - "nodes"
  - "num_nodes"
  - "batch directives"
  - "flexiblas"
  - "job_submission"
  - "NetCDF"
  - "batch_system"
  - "Rorqual"
  - "nano timers"
  - "intel/2023.2.1"
  - "StdEnv/2023"
  - "cvmfs"
  - "netcdf-mpi"
  - "regular queue"
  - "config_compilers.xml"
  - "LINUX"
  - "load"
  - "Quickstart Guide"
  - "batch_mail_type"
  - "Nibi"
  - "config_batch"
  - "configuration files"
  - "sharcnet"
  - "test_case"
  - "batch system"
  - "cmake/3.27.7"
  - "COMPILERS"
  - "Slurm"
  - "Compute Canada"
  - "create_newcase"
  - "environment variables"
  - "xml-libxml"
  - "test case"
  - "init_path"
  - "CIME"
  - "local installation"
  - "config_machines"
  - "config_machines_template.xml"
  - "openmpi"
  - "CESM"
  - "MAX_TASKS_PER_NODE"

questions:
  - "What is the Community Earth System Model (CESM) and what is the primary benefit of performing a local installation?"
  - "What specific modifications must be made to the external dependencies if a researcher chooses to install the older CESM version 2.1.3?"
  - "How do you check out the individual model components and configure the local machine file for a cluster environment?"
  - "What are the specified root directory paths for the input climate forcing data and the archived model output?"
  - "Which batch scheduling system is used, and what is the maximum number of MPI tasks allowed per node?"
  - "What is the designated email address to contact for technical support regarding this system configuration?"
  - "What specific software modules and versions are required to be loaded for the Intel compiler and OpenMPI library in this configuration?"
  - "Which environment variables are explicitly defined to configure the paths for NetCDF libraries and MPI compilers?"
  - "What is the target machine name, operating system, and node name regex defined in this XML configuration snippet?"
  - "What is the documentation URL provided for the machine named \"nibi\" in the configuration file?"
  - "Which operating system and compilers are supported by the Nibi machine according to the XML snippet?"
  - "What regular expression is used to identify the node names associated with this specific machine?"
  - "What are the configured batch system and the maximum number of MPI tasks allowed per node?"
  - "Which specific software modules and versions are required to be loaded for the Intel compiler and OpenMPI environments?"
  - "What are the defined directory paths for storing the model's input data and output archives?"
  - "What type of processors does the Narval machine use, and what is notable about its software dependencies?"
  - "Which specific compiler and MPI library versions are configured to be loaded in the module system for this machine?"
  - "What are the designated root directory paths for input data and output archives defined in the configuration?"
  - "What are the specific directory paths assigned to the NetCDF and LAPACK libraries in this configuration?"
  - "What memory limit is established for the OpenMP stack size?"
  - "Which specific C compiler is designated for use with Intel MPI?"
  - "What specific software modules and their corresponding versions are instructed to be loaded by this configuration?"
  - "Which environment variable is explicitly defined in the snippet, and what is its assigned file path?"
  - "Based on the directory paths and software packages listed, what type of computing infrastructure is this configuration likely designed for?"
  - "What are the specific file paths defined for the NetCDF and LAPACK libraries in the environment variables?"
  - "What are the key system configurations defined for the \"niagara\" machine, such as its batch system, maximum tasks per node, and supported compilers?"
  - "Which specific software modules and versions are required to be loaded when using the Intel compiler?"
  - "What is the base environment module loaded after purging the existing modules?"
  - "Which specific software modules are loaded when the Intel compiler environment is specified?"
  - "Which shell environments are explicitly supported by the command paths defined in the configuration?"
  - "What specific software modules and environment variables are required to be loaded in this configuration?"
  - "What are the defined machine parameters for the \"Rorqual\" cluster, including its batch system and maximum tasks per node?"
  - "How does the configuration structure the user's project accounts and the root directories for input and output data?"
  - "What are the primary attributes and error handling settings defined for the module system?"
  - "Which programming and scripting languages have specific initialization paths provided in the configuration?"
  - "What is the base directory path used to locate the Lmod initialization scripts for the supported languages?"
  - "What specific software modules and environment variables are required in the XML configuration for the Intel and OpenMPI setup?"
  - "Which command-line tools and scripts are used to validate and query the newly created machine configuration file?"
  - "What is the next configuration step required after successfully setting up and validating the machine XML file?"
  - "What type of batch system is configured in this XML file, and what are its primary submit and cancel commands?"
  - "Is a project value required for job submission on this machine according to the configuration?"
  - "What are the maximum walltime and node limits specified for the \"fir\" queue?"
  - "How can a user check the official XML template to find additional configuration parameters?"
  - "What is the required directory path and filename for creating the local batch configuration file?"
  - "What type of initial content should be used when setting up the new local batch file?"
  - "What are the supported batch mail types defined in the configuration?"
  - "Which specific variables are mapped to the time and account submission arguments?"
  - "How are the job name and number of nodes dynamically assigned in the directives section?"
  - "What batch system type is being configured across the different machine environments in the provided XML files?"
  - "What are the maximum node limits (nodemax) specified for the \"nibi\" and \"narval\" queues respectively?"
  - "Which specific hardware constraint directive is uniquely applied to the Niagara machine configuration?"
  - "What specific resource allocation directives and templating variables are defined in this configuration snippet?"
  - "How does the configuration restrict the types of hardware architectures that can be used for the job?"
  - "According to the comment in the snippet, how are unknown queues handled by the system?"
  - "What are the specific Slurm batch directives and queue limits configured for the Rorqual cluster in the config_batch.xml file?"
  - "How can a user validate their newly created XML batch configuration file to ensure it is formatted correctly?"
  - "What environment variables and library paths need to be defined in the config_compilers.xml file for clusters like Fir and Nibi?"
  - "What specific environment variables and library paths need to be defined in the config_compilers.xml file for machines like Narval, Niagara, and Rorqual?"
  - "Which command and schema are used to validate the newly created XML compiler configuration file?"
  - "What steps and script arguments are required to create a new CESM test case in the scratch directory?"
  - "What is the file path and machine name specified in this XML configuration snippet?"
  - "Which C preprocessor flags are appended to the \"gptl\" model to enable nano timers and other system features?"
  - "How is the NetCDF path configured using environment variables in this file?"
  - "What specific shell commands are used to set up the input and output directories for the CESM test case?"
  - "What default model and machine environment are assumed in the instructions for creating a new test case?"
  - "Which parameters are passed to the create_newcase script to define the case name, component set, and resolution?"
  - "What are the specific command-line steps required to set up, build, and submit a test case?"
  - "What is the purpose of the `--download` flag when executing the check_input_data script?"
  - "Which official documentation links and guides are provided as references for the CESM framework?"
  - "What are the specific command-line steps required to set up, build, and submit a test case?"
  - "What is the purpose of the `--download` flag when executing the check_input_data script?"
  - "Which official documentation links and guides are provided as references for the CESM framework?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

The [Community Earth System Model](https://www.cesm.ucar.edu/) is a fully coupled global climate model developed in collaboration with colleagues in the research community. CESM provides state-of-the-art computer simulations of Earth's past, present, and future climate states.

## Porting and Validating

The following configuration files and commands are designed for a local installation of CESM 2.1. Local installations allow for [source code changes](https://ncar.github.io/CESM-Tutorial/notebooks/sourcemods/sourcemods.html) which may be useful for specific research purposes. Before making the adaptations as described in the sections below, please [download CESM 2.1 from the CESM developers](https://www.cesm.ucar.edu/models/cesm2/download) in your local directory.

=== "Version 2.1.5"

This version is based on the [latest official release](https://github.com/ESCOMP/CESM/releases/latest).

```bash
git clone -b release-cesm2.1.5 https://github.com/ESCOMP/CESM.git /path/to/CESM
```

=== "Version 2.1.3"

This older version has been very popular in the research community, but it may become obsolete because this version is no longer officially supported.

```bash
git clone -b release-cesm2.1.3 https://github.com/ESCOMP/CESM.git /path/to/CESM
```

To make this version work, **some external dependencies must be replaced** with newer versions which are no longer exactly matching the 2.1.3 version of CESM; researchers are responsible for confirming validity.

```bash
sed -i 's/cam_cesm2_1_rel_41/cam_cesm2_1_rel_59/g' /path/to/CESM/Externals.cfg
sed -i 's/cime5.6.32/cime5.6.51/g' /path/to/CESM/Externals.cfg
sed -i 's/cism-release-cesm2.1.2_02/cism-release-cesm2.1.2_03/g' /path/to/CESM/Externals.cfg
```

## Checkout Externals

Before your first use of CESM, you may check out the individual model components by running the `checkout_externals` script.

```bash
/path/to/CESM/manage_externals/checkout_externals
```

You may need to accept a certificate from the CESM repository to download input files. To validate, run the same script with `-S`.

```bash
/path/to/CESM/manage_externals/checkout_externals -S
```

See [this documentation page](https://escomp.github.io/CESM/versions/cesm2.1/html/downloading_cesm.html) for an example of valid output.

## Local Machine File

* Create and edit the file `~/.cime/config_machines.xml` from the following minimal content per cluster; **update both configuration lines** having `def-EDIT_THIS` with the compute account you want to use on the cluster.

=== "Fir"

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>

<config_machines version="2.0">
  <machine MACH="fir">
    <DESC>https://docs.alliancecan.ca/wiki/Fir</DESC>
    <NODENAME_REGEX>r.*\.fir\.alliancecan</NODENAME_REGEX>

    <OS>LINUX</OS>
    <COMPILERS>intel,gnu</COMPILERS>
    <MPILIBS>openmpi</MPILIBS>

    <PROJECT>def-EDIT_THIS</PROJECT>
    <CHARGE_ACCOUNT>def-EDIT_THIS</CHARGE_ACCOUNT>

    <CIME_OUTPUT_ROOT>/scratch/$USER/cesm/output</CIME_OUTPUT_ROOT>
    <DIN_LOC_ROOT>/scratch/$USER/cesm/inputdata</DIN_LOC_ROOT>
    <DIN_LOC_ROOT_CLMFORC>${DIN_LOC_ROOT}/atm/datm7</DIN_LOC_ROOT_CLMFORC>
    <DOUT_S_ROOT>$CIME_OUTPUT_ROOT/archive/case</DOUT_S_ROOT>
    <GMAKE>make</GMAKE>
    <GMAKE_J>8</GMAKE_J>
    <BATCH_SYSTEM>slurm</BATCH_SYSTEM>
    <SUPPORTED_BY>support@tech.alliancecan.ca</SUPPORTED_BY>
    <MAX_TASKS_PER_NODE>192</MAX_TASKS_PER_NODE>
    <MAX_MPITASKS_PER_NODE>192</MAX_MPITASKS_PER_NODE>
    <PROJECT_REQUIRED>TRUE</PROJECT_REQUIRED>

    <mpirun mpilib="openmpi">
      <executable>srun</executable>
    </mpirun>
    <module_system type="module" allow_error="true">
      <init_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/perl</init_path>
      <init_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/env_modules_python.py</init_path>
      <init_path lang="csh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/csh</init_path>
      <init_path lang="sh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/sh</init_path>
      <cmd_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod perl</cmd_path>
      <cmd_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod python</cmd_path>
      <cmd_path lang="csh">module</cmd_path>
      <cmd_path lang="sh">module</cmd_path>
      <modules>
      <command name="purge"/>
 	<command name="load">StdEnv/2023</command>
      </modules>
      <modules compiler="intel">
	<command name="load">intel/2023.2.1</command>
	<command name="load">git-annex/10.20231129</command>
	<command name="load">cmake/3.27.7</command>
      </modules>
      <modules mpilib="openmpi">
        <command name="load">openmpi/4.1.5</command>
        <command name="load">hdf5-mpi/1.14.2</command>
        <command name="load">netcdf-c++4-mpi/4.3.1</command>
        <command name="load">netcdf-fortran-mpi/4.6.1</command>
        <command name="load">netcdf-mpi/4.9.2</command>
	<command name="load">xml-libxml/2.0208</command>
	<command name="load">flexiblas/3.3.1</command>
      </modules>
    </module_system>
    <environment_variables>
            <env name="NETCDF_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/pnetcdf/1.12.3</env>
            <env name="NETCDF_FORTRAN_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-fortran-mpi/4.6.1/</env>
            <env name="NETCDF_C_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-c++4-mpi/4.3.1/</env>
            <env name="NETLIB_LAPACK_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/imkl/2023.2.0/mkl/2023.2.0/</env>
	    <env name="OMP_STACKSIZE">256M</env>
            <env name="I_MPI_CC">icc</env>
            <env name="I_MPI_FC">ifort</env>
            <env name="I_MPI_F77">ifort</env>
            <env name="I_MPI_F90">ifort</env>
            <env name="I_MPI_CXX">icpc</env>
    </environment_variables>
    <resource_limits>
      <resource name="RLIMIT_STACK">300000000</resource>
    </resource_limits>
  </machine>
</config_machines>
```

=== "Nibi"

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>

<config_machines version="2.0">
  <machine MACH="nibi">
    <DESC>https://docs.alliancecan.ca/wiki/Nibi</DESC>
    <NODENAME_REGEX>*.nibi.sharcnet</NODENAME_REGEX>

    <OS>LINUX</OS>
    <COMPILERS>intel,gnu</COMPILERS>
    <MPILIBS>openmpi</MPILIBS>

    <PROJECT>def-EDIT_THIS</PROJECT>
    <CHARGE_ACCOUNT>def-EDIT_THIS</CHARGE_ACCOUNT>

    <CIME_OUTPUT_ROOT>/scratch/$USER/cesm/output</CIME_OUTPUT_ROOT>
    <DIN_LOC_ROOT>/scratch/$USER/cesm/inputdata</DIN_LOC_ROOT>
    <DIN_LOC_ROOT_CLMFORC>${DIN_LOC_ROOT}/atm/datm7</DIN_LOC_ROOT_CLMFORC>
    <DOUT_S_ROOT>$CIME_OUTPUT_ROOT/archive/case</DOUT_S_ROOT>
    <GMAKE>make</GMAKE>
    <GMAKE_J>8</GMAKE_J>
    <BATCH_SYSTEM>slurm</BATCH_SYSTEM>
    <SUPPORTED_BY>support@tech.alliancecan.ca</SUPPORTED_BY>
    <MAX_TASKS_PER_NODE>192</MAX_TASKS_PER_NODE>
    <MAX_MPITASKS_PER_NODE>192</MAX_MPITASKS_PER_NODE>
    <PROJECT_REQUIRED>TRUE</PROJECT_REQUIRED>

    <mpirun mpilib="openmpi">
      <executable>srun</executable>
    </mpirun>
    <module_system type="module" allow_error="true">
      <init_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/perl</init_path>
      <init_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/env_modules_python.py</init_path>
      <init_path lang="csh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/csh</init_path>
      <init_path lang="sh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/sh</init_path>
      <cmd_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod perl</cmd_path>
      <cmd_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod python</cmd_path>
      <cmd_path lang="csh">module</cmd_path>
      <cmd_path lang="sh">module</cmd_path>
      <modules>
      <command name="purge"/>
 	<command name="load">StdEnv/2023</command>
      </modules>
      <modules compiler="intel">
	<command name="load">intel/2023.2.1</command>
	<command name="load">git-annex/10.20231129</command>
	<command name="load">cmake/3.27.7</command>
      </modules>
      <modules mpilib="openmpi">
        <command name="load">openmpi/4.1.5</command>
        <command name="load">hdf5-mpi/1.14.2</command>
        <command name="load">netcdf-c++4-mpi/4.3.1</command>
        <command name="load">netcdf-fortran-mpi/4.6.1</command>
        <command name="load">netcdf-mpi/4.9.2</command>
	<command name="load">xml-libxml/2.0208</command>
	<command name="load">flexiblas/3.3.1</command>
      </modules>
    </module_system>
    <environment_variables>
            <env name="NETCDF_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/pnetcdf/1.12.3</env>
            <env name="NETCDF_FORTRAN_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-fortran-mpi/4.6.1/</env>
            <env name="NETCDF_C_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-c++4-mpi/4.3.1/</env>
            <env name="NETLIB_LAPACK_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/imkl/2023.2.0/mkl/2023.2.0/</env>
	    <env name="OMP_STACKSIZE">256M</env>
            <env name="I_MPI_CC">icc</env>
            <env name="I_MPI_FC">ifort</env>
            <env name="I_MPI_F77">ifort</env>
            <env name="I_MPI_F90">ifort</env>
            <env name="I_MPI_CXX">icpc</env>
    </environment_variables>
    <resource_limits>
      <resource name="RLIMIT_STACK">300000000</resource>
    </resource_limits>
  </machine>
</config_machines>
```

=== "Narval"

Note: despite the Intel software dependencies, the following configuration works on Narval's AMD processors.

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>

<config_machines version="2.0">
  <machine MACH="narval">
    <DESC>https://docs.alliancecan.ca/wiki/Narval/en</DESC>
    <NODENAME_REGEX>n[acgl].*.narval.calcul.quebec</NODENAME_REGEX>

    <OS>LINUX</OS>
    <COMPILERS>intel,gnu</COMPILERS>
    <MPILIBS>openmpi</MPILIBS>

    <PROJECT>def-EDIT_THIS</PROJECT>
    <CHARGE_ACCOUNT>def-EDIT_THIS</CHARGE_ACCOUNT>

    <CIME_OUTPUT_ROOT>/scratch/$USER/cesm/output</CIME_OUTPUT_ROOT>
    <DIN_LOC_ROOT>/scratch/$USER/cesm/inputdata</DIN_LOC_ROOT>
    <DIN_LOC_ROOT_CLMFORC>${DIN_LOC_ROOT}/atm/datm7</DIN_LOC_ROOT_CLMFORC>
    <DOUT_S_ROOT>$CIME_OUTPUT_ROOT/archive/case</DOUT_S_ROOT>
    <GMAKE>make</GMAKE>
    <GMAKE_J>8</GMAKE_J>
    <BATCH_SYSTEM>slurm</BATCH_SYSTEM>
    <SUPPORTED_BY>support@tech.alliancecan.ca</SUPPORTED_BY>
    <MAX_TASKS_PER_NODE>64</MAX_TASKS_PER_NODE>
    <MAX_MPITASKS_PER_NODE>64</MAX_MPITASKS_PER_NODE>
    <PROJECT_REQUIRED>TRUE</PROJECT_REQUIRED>

    <mpirun mpilib="openmpi">
      <executable>srun</executable>
    </mpirun>
    <module_system type="module" allow_error="true">
      <init_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/perl</init_path>
      <init_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/env_modules_python.py</init_path>
      <init_path lang="csh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/csh</init_path>
      <init_path lang="sh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/sh</init_path>
      <cmd_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod perl</cmd_path>
      <cmd_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod python</cmd_path>
      <cmd_path lang="csh">module</cmd_path>
      <cmd_path lang="sh">module</cmd_path>
      <modules>
      <command name="purge"/>
 	<command name="load">StdEnv/2023</command>
      </modules>
      <modules compiler="intel">
	<command name="load">intel/2023.2.1</command>
	<command name="load">git-annex/10.20231129</command>
	<command name="load">cmake/3.27.7</command>
      </modules>
      <modules mpilib="openmpi">
        <command name="load">openmpi/4.1.5</command>
        <command name="load">hdf5-mpi/1.14.2</command>
        <command name="load">netcdf-c++4-mpi/4.3.1</command>
        <command name="load">netcdf-fortran-mpi/4.6.1</command>
        <command name="load">netcdf-mpi/4.9.2</command>
	<command name="load">xml-libxml/2.0208</command>
	<command name="load">flexiblas/3.3.1</command>
      </modules>
    </module_system>
    <environment_variables>
            <env name="NETCDF_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/pnetcdf/1.12.3</env>
            <env name="NETCDF_FORTRAN_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-fortran-mpi/4.6.1/</env>
            <env name="NETCDF_C_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-c++4-mpi/4.3.1/</env>
            <env name="NETLIB_LAPACK_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/imkl/2023.2.0/mkl/2023.2.0/</env>
	    <env name="OMP_STACKSIZE">256M</env>
            <env name="I_MPI_CC">icc</env>
            <env name="I_MPI_FC">ifort</env>
            <env name="I_MPI_F77">ifort</env>
            <env name="I_MPI_F90">ifort</env>
            <env name="I_MPI_CXX">icpc</env>
    </environment_variables>
    <resource_limits>
      <resource name="RLIMIT_STACK">300000000</resource>
    </resource_limits>
  </machine>
</config_machines>
```

=== "Niagara"

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>

<config_machines version="2.0">
  <machine MACH="niagara">
    <DESC>https://docs.alliancecan.ca/wiki/Niagara</DESC>
    <NODENAME_REGEX>nia.*.scinet.local</NODENAME_REGEX>

    <OS>LINUX</OS>
    <COMPILERS>intel,gnu</COMPILERS>
    <MPILIBS>openmpi</MPILIBS>

    <PROJECT>def-EDIT_THIS</PROJECT>
    <CHARGE_ACCOUNT>def-EDIT_THIS</CHARGE_ACCOUNT>

    <CIME_OUTPUT_ROOT>/scratch/$USER/cesm/output</CIME_OUTPUT_ROOT>
    <DIN_LOC_ROOT>/scratch/$USER/cesm/inputdata</DIN_LOC_ROOT>
    <DIN_LOC_ROOT_CLMFORC>${DIN_LOC_ROOT}/atm/datm7</DIN_LOC_ROOT_CLMFORC>
    <DOUT_S_ROOT>$CIME_OUTPUT_ROOT/archive/case</DOUT_S_ROOT>
    <GMAKE>make</GMAKE>
    <GMAKE_J>8</GMAKE_J>
    <BATCH_SYSTEM>slurm</BATCH_SYSTEM>
    <SUPPORTED_BY>support@tech.alliancecan.ca</SUPPORTED_BY>
    <MAX_TASKS_PER_NODE>40</MAX_TASKS_PER_NODE>
    <MAX_MPITASKS_PER_NODE>40</MAX_MPITASKS_PER_NODE>
    <PROJECT_REQUIRED>TRUE</PROJECT_REQUIRED>

    <mpirun mpilib="openmpi">
      <executable>srun</executable>
    </mpirun>
    <module_system type="module" allow_error="true">
      <init_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/perl</init_path>
      <init_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/env_modules_python.py</init_path>
      <init_path lang="csh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/csh</init_path>
      <init_path lang="sh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/sh</init_path>
      <cmd_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod perl</cmd_path>
      <cmd_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod python</cmd_path>
      <cmd_path lang="csh">module</cmd_path>
      <cmd_path lang="sh">module</cmd_path>
      <modules>
      <command name="purge"/>
 	<command name="load">StdEnv/2023</command>
      </modules>
      <modules compiler="intel">
	<command name="load">intel/2023.2.1</command>
	<command name="load">git-annex/10.20231129</command>
	<command name="load">cmake/3.27.7</command>
      </modules>
      <modules mpilib="openmpi">
        <command name="load">openmpi/4.1.5</command>
        <command name="load">hdf5-mpi/1.14.2</command>
        <command name="load">netcdf-c++4-mpi/4.3.1</command>
        <command name="load">netcdf-fortran-mpi/4.6.1</command>
        <command name="load">netcdf-mpi/4.9.2</command>
	<command name="load">xml-libxml/2.0208</command>
	<command name="load">flexiblas/3.3.1</command>
      </modules>
    </module_system>
    <environment_variables>
            <env name="NETCDF_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/pnetcdf/1.12.3</env>
            <env name="NETCDF_FORTRAN_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-fortran-mpi/4.6.1/</env>
            <env name="NETCDF_C_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-c++4-mpi/4.3.1/</env>
            <env name="NETLIB_LAPACK_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/imkl/2023.2.0/mkl/2023.2.0/</env>
	    <env name="OMP_STACKSIZE">256M</env>
            <env name="I_MPI_CC">icc</env>
            <env name="I_MPI_FC">ifort</env>
            <env name="I_MPI_F77">ifort</env>
            <env name="I_MPI_F90">ifort</env>
            <env name="I_MPI_CXX">icpc</env>
    </environment_variables>
    <resource_limits>
      <resource name="RLIMIT_STACK">300000000</resource>
    </resource_limits>
  </machine>
</config_machines>
```

=== "Rorqual"

Note: despite the Intel software dependencies, the following configuration works on Rorqual's AMD processors.

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>

<config_machines version="2.0">
  <machine MACH="rorqual">
    <DESC>https://docs.alliancecan.ca/wiki/Rorqual/en</DESC>
    <NODENAME_REGEX>r.*\.rorqual\.calcul\.quebec</NODENAME_REGEX>

    <OS>LINUX</OS>
    <COMPILERS>intel,gnu</COMPILERS>
    <MPILIBS>openmpi</MPILIBS>

    <PROJECT>def-EDIT_THIS</PROJECT>
    <CHARGE_ACCOUNT>def-EDIT_THIS</CHARGE_ACCOUNT>

    <CIME_OUTPUT_ROOT>/scratch/$USER/cesm/output</CIME_OUTPUT_ROOT>
    <DIN_LOC_ROOT>/scratch/$USER/cesm/inputdata</DIN_LOC_ROOT>
    <DIN_LOC_ROOT_CLMFORC>${DIN_LOC_ROOT}/atm/datm7</DIN_LOC_ROOT_CLMFORC>
    <DOUT_S_ROOT>$CIME_OUTPUT_ROOT/archive/case</DOUT_S_ROOT>
    <GMAKE>make</GMAKE>
    <GMAKE_J>8</GMAKE_J>
    <BATCH_SYSTEM>slurm</BATCH_SYSTEM>
    <SUPPORTED_BY>support@tech.alliancecan.ca</SUPPORTED_BY>
    <MAX_TASKS_PER_NODE>192</MAX_TASKS_PER_NODE>
    <MAX_MPITASKS_PER_NODE>192</MAX_MPITASKS_PER_NODE>
    <PROJECT_REQUIRED>TRUE</PROJECT_REQUIRED>

    <mpirun mpilib="openmpi">
      <executable>srun</executable>
    </mpirun>
    <module_system type="module" allow_error="true">
      <init_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/perl</init_path>
      <init_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/env_modules_python.py</init_path>
      <init_path lang="csh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/csh</init_path>
      <init_path lang="sh">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/init/sh</init_path>
      <cmd_path lang="perl">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod perl</cmd_path>
      <cmd_path lang="python">/cvmfs/soft.computecanada.ca/custom/software/lmod/lmod/libexec/lmod python</cmd_path>
      <cmd_path lang="csh">module</cmd_path>
      <cmd_path lang="sh">module</cmd_path>
      <modules>
      <command name="purge"/>
 	<command name="load">StdEnv/2023</command>
      </modules>
      <modules compiler="intel">
	<command name="load">intel/2023.2.1</command>
	<command name="load">git-annex/10.20231129</command>
	<command name="load">cmake/3.27.7</command>
      </modules>
      <modules mpilib="openmpi">
        <command name="load">openmpi/4.1.5</command>
        <command name="load">hdf5-mpi/1.14.2</command>
        <command name="load">netcdf-c++4-mpi/4.3.1</command>
        <command name="load">netcdf-fortran-mpi/4.6.1</command>
        <command name="load">netcdf-mpi/4.9.2</command>
	<command name="load">xml-libxml/2.0208</command>
	<command name="load">flexiblas/3.3.1</command>
      </modules>
    </module_system>
    <environment_variables>
            <env name="NETCDF_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/pnetcdf/1.12.3</env>
            <env name="NETCDF_FORTRAN_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-fortran-mpi/4.6.1/</env>
            <env name="NETCDF_C_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v4/MPI/intel2023/openmpi4/netcdf-c++4-mpi/4.3.1/</env>
            <env name="NETLIB_LAPACK_PATH">/cvmfs/soft.computecanada.ca/easybuild/software/2023/x86-64-v3/Core/imkl/2023.2.0/mkl/2023.2.0/</env>
	    <env name="OMP_STACKSIZE">256M</env>
            <env name="I_MPI_CC">icc</env>
            <env name="I_MPI_FC">ifort</env>
            <env name="I_MPI_F77">ifort</env>
            <env name="I_MPI_F90">ifort</env>
            <env name="I_MPI_CXX">icpc</env>
    </environment_variables>
    <resource_limits>
      <resource name="RLIMIT_STACK">300000000</resource>
    </resource_limits>
  </machine>
</config_machines>
```

* Validate your XML machine file with the following commands:

    ```bash
    [name@server ~]$ xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_machines.xsd ~/.cime/config_machines.xml
    ```
    Output:
    ```
    /home/name/.cime/config_machines.xml validates
    ```

    ```bash
    [name@rorqual ~]$ /path/to/CESM/cime/scripts/query_config --machines current
    ```
    Output:
    ```
      rorqual (current) : https://docs.alliancecan.ca/wiki/Rorqual/en
          os              LINUX
          compilers       intel,gnu
          pes/node        192
          max_tasks/node  192
    ```

* Check the official template for additional parameters:

    ```bash
    [name@server ~]$ less /path/to/CESM/cime/config/xml_schemas/config_machines_template.xml
    ```

## Local Batch File

* Create and edit the file `~/.cime/config_batch.xml` from the following minimal content:

=== "Fir"

```xml title="~/.cime/config_batch.xml"
<?xml version="1.0"?>
<file id="env_batch.xml" version="2.0">
  <header>
      These variables may be changed anytime during a run, they
      control arguments to the batch submit command.
  </header>
  <group id="config_batch">
    <entry id="BATCH_SYSTEM" value="slurm">
      <type>char</type>
      <valid_values>nersc_slurm,lc_slurm,moab,pbs,lsf,slurm,cobalt,cobalt_theta,sge,none</valid_values>
      <desc>The batch system type to use for this machine.</desc>
    </entry>
  </group>
  <group id="job_submission">
    <entry id="PROJECT_REQUIRED" value="TRUE">
      <type>logical</type>
      <valid_values>TRUE,FALSE</valid_values>
      <desc>whether the PROJECT value is required on this machine</desc>
    </entry>
  </group>
  <batch_system type="slurm" >
    <batch_submit>sbatch</batch_submit>
    <batch_cancel>scancel</batch_cancel>
    <batch_directive>#SBATCH</batch_directive>
    <jobid_pattern>(\d+)$</jobid_pattern>
    <depend_string> --dependency=afterok:jobid</depend_string>
    <depend_allow_string> --dependency=afterany:jobid</depend_allow_string>
    <depend_separator>,</depend_separator>
    <batch_mail_flag>--mail-user</batch_mail_flag>
    <batch_mail_type_flag>--mail-type</batch_mail_type_flag>
    <batch_mail_type>none, all, begin, end, fail</batch_mail_type>
    <submit_args>
      <arg flag="--time" name="$JOB_WALLCLOCK_TIME"/>
      <arg flag="--account" name="$CHARGE_ACCOUNT"/>
    </submit_args>
    <directives>
      <directive>--job-name={{ job_id }}</directive>
      <directive>--nodes={{ num_nodes }}</directive>
      <directive>--ntasks-per-node={{ tasks_per_node }}</directive>
      <directive>--output={{ job_id }}</directive>
      <directive>--exclusive</directive>
      <directive>--mem=0</directive>
    </directives>
     <!-- Unknown queues use the batch directives for the regular queue -->
   <unknown_queue_directives>regular</unknown_queue_directives>
    <queues>
     <queue walltimemax="12:00:00" nodemin="1" nodemax="864">fir</queue>
    </queues>
  </batch_system>
</file>
```

=== "Nibi"

```xml title="~/.cime/config_batch.xml"
<?xml version="1.0"?>
<file id="env_batch.xml" version="2.0">
  <header>
      These variables may be changed anytime during a run, they
      control arguments to the batch submit command.
  </header>
  <group id="config_batch">
    <entry id="BATCH_SYSTEM" value="slurm">
      <type>char</type>
      <valid_values>nersc_slurm,lc_slurm,moab,pbs,lsf,slurm,cobalt,cobalt_theta,sge,none</valid_values>
      <desc>The batch system type to use for this machine.</desc>
    </entry>
  </group>
  <group id="job_submission">
    <entry id="PROJECT_REQUIRED" value="TRUE">
      <type>logical</type>
      <valid_values>TRUE,FALSE</valid_values>
      <desc>whether the PROJECT value is required on this machine</desc>
    </entry>
  </group>
  <batch_system type="slurm" >
    <batch_submit>sbatch</batch_submit>
    <batch_cancel>scancel</batch_cancel>
    <batch_directive>#SBATCH</batch_directive>
    <jobid_pattern>(\d+)$</jobid_pattern>
    <depend_string> --dependency=afterok:jobid</depend_string>
    <depend_allow_string> --dependency=afterany:jobid</depend_allow_string>
    <depend_separator>,</depend_separator>
    <batch_mail_flag>--mail-user</batch_mail_flag>
    <batch_mail_type_flag>--mail-type</batch_mail_type_flag>
    <batch_mail_type>none, all, begin, end, fail</batch_mail_type>
    <submit_args>
      <arg flag="--time" name="$JOB_WALLCLOCK_TIME"/>
      <arg flag="--account" name="$CHARGE_ACCOUNT"/>
    </submit_args>
    <directives>
      <directive>--job-name={{ job_id }}</directive>
      <directive>--nodes={{ num_nodes }}</directive>
      <directive>--ntasks-per-node={{ tasks_per_node }}</directive>
      <directive>--output={{ job_id }}</directive>
      <directive>--exclusive</directive>
      <directive>--mem=0</directive>
    </directives>
     <!-- Unknown queues use the batch directives for the regular queue -->
   <unknown_queue_directives>regular</unknown_queue_directives>
    <queues>
     <queue walltimemax="12:00:00" nodemin="1" nodemax="700">nibi</queue>
    </queues>
  </batch_system>
</file>
```

=== "Narval"

```xml title="~/.cime/config_batch.xml"
<?xml version="1.0"?>
  <batch_system type="slurm" >
    <batch_submit>sbatch</batch_submit>
    <batch_cancel>scancel</batch_cancel>
    <batch_directive>#SBATCH</batch_directive>
    <jobid_pattern>(\d+)$</jobid_pattern>
    <depend_string> --dependency=afterok:jobid</depend_string>
    <depend_allow_string> --dependency=afterany:jobid</depend_allow_string>
    <depend_separator>,</depend_separator>
    <batch_mail_flag>--mail-user</batch_mail_flag>
    <batch_mail_type_flag>--mail-type</batch_mail_type_flag>
    <batch_mail_type>none, all, begin, end, fail</batch_mail_type>
    <submit_args>
      <arg flag="--time" name="$JOB_WALLCLOCK_TIME"/>
      <arg flag="--account" name="$CHARGE_ACCOUNT"/>
    </submit_args>
    <directives>
      <directive>--job-name={{ job_id }}</directive>
      <directive>--nodes={{ num_nodes }}</directive>
      <directive>--ntasks-per-node={{ tasks_per_node }}</directive>
      <directive>--output={{ job_id }}</directive>
      <directive>--exclusive</directive>
      <directive>--mem=0</directive>
    </directives>
    <unknown_queue_directives>regular</unknown_queue_directives>
    <queues>
      <queue walltimemax="12:00:00" nodemin="1" nodemax="1145">narval</queue>
    </queues>
  </batch_system>
```

=== "Niagara"

```xml title="~/.cime/config_machines.xml"
<?xml version="1.0"?>
<file id="env_batch.xml" version="2.0">
  <header>
      These variables may be changed anytime during a run, they
      control arguments to the batch submit command.
  </header>
  <group id="config_batch">
    <entry id="BATCH_SYSTEM" value="slurm">
      <type>char</type>
      <valid_values>nersc_slurm,lc_slurm,moab,pbs,lsf,slurm,cobalt,cobalt_theta,sge,none</valid_values>
      <desc>The batch system type to use for this machine.</desc>
    </entry>
  </group>
  <group id="job_submission">
    <entry id="PROJECT_REQUIRED" value="TRUE">
      <type>logical</type>
      <valid_values>TRUE,FALSE</valid_values>
      <desc>whether the PROJECT value is required on this machine</desc>
    </entry>
  </group>
  <batch_system type="slurm" >
    <batch_submit>sbatch</batch_submit>
    <batch_cancel>scancel</batch_cancel>
    <batch_directive>#SBATCH</batch_directive>
    <jobid_pattern>(\d+)$</jobid_pattern>
    <depend_string> --dependency=afterok:jobid</depend_string>
    <depend_allow_string> --dependency=afterany:jobid</depend_allow_string>
    <depend_separator>,</depend_separator>
    <submit_args>
      <arg flag="--time" name="$JOB_WALLCLOCK_TIME"/>
      <arg flag="--account" name="$CHARGE_ACCOUNT"/>
    </submit_args>
    <directives>
      <directive>--job-name={{ job_id }}</directive>
      <directive>--nodes={{ num_nodes }}</directive>
      <directive>--ntasks-per-node={{ tasks_per_node }}</directive>
      <directive>--output={{ job_id }}</directive>
      <directive>--exclusive</directive>
      <directive>--mem=0</directive>
      <directive>--constraint=[skylake|cascade]</directive>
    </directives>
     <!-- Unknown queues use the batch directives for the regular queue -->
   <unknown_queue_directives>regular</unknown_queue_directives>
    <queues>
     <queue walltimemax="12:00:00" nodemin="1" nodemax="2024">niagara</queue>
    </queues>
  </batch_system>
</file>
```

=== "Rorqual"

```xml title="~/.cime/config_batch.xml"
<?xml version="1.0"?>
  <batch_system type="slurm" >
    <batch_submit>sbatch</batch_submit>
    <batch_cancel>scancel</batch_cancel>
    <batch_directive>#SBATCH</batch_directive>
    <jobid_pattern>(\d+)$</jobid_pattern>
    <depend_string> --dependency=afterok:jobid</depend_string>
    <depend_allow_string> --dependency=afterany:jobid</depend_allow_string>
    <depend_separator>,</depend_separator>
    <batch_mail_flag>--mail-user</batch_mail_flag>
    <batch_mail_type_flag>--mail-type</batch_mail_type_flag>
    <batch_mail_type>none, all, begin, end, fail</batch_mail_type>
    <submit_args>
      <arg flag="--time" name="$JOB_WALLCLOCK_TIME"/>
      <arg flag="--account" name="$CHARGE_ACCOUNT"/>
    </submit_args>
    <directives>
      <directive>--job-name={{ job_id }}</directive>
      <directive>--nodes={{ num_nodes }}</directive>
      <directive>--ntasks-per-node={{ tasks_per_node }}</directive>
      <directive>--output={{ job_id }}</directive>
      <directive>--exclusive</directive>
      <directive>--mem=0</directive>
    </directives>
    <!-- Unknown queues use the batch directives for the regular queue -->
    <unknown_queue_directives>regular</unknown_queue_directives>
    <queues>
      <queue walltimemax="12:00:00" nodemin="1" nodemax="670">rorqual</queue>
    </queues>
  </batch_system>
```

* Validate your XML batch file with the following commands:

    ```bash
    [name@server ~]$ xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_batch.xsd ~/.cime/config_batch.xml
    ```
    Output:
    ```
    /home/name/.cime/config_batch.xml validates
    ```

* Check the documentation for additional **[configuration parameters and examples](https://esmci.github.io/cime/versions/maint-5.6/html/xml_files/cesm.html#cimeroot-config-cesm-machines)**.

## Local Compilers File

* Create and edit the file `~/.cime/config_compilers.xml` from the following minimal content per cluster:

=== "Fir"

```xml title="~/.cime/config_compilers.xml"
<?xml version="1.0"?>

	<compiler MACH="fir">
	  <CPPDEFS>
	    <!-- these flags enable nano timers -->
	    <append MODEL="gptl"> -DHAVE_NANOTIME -DBIT64 -DHAVE_VPRINTF -DHAVE_BACKTRACE -DHAVE_SLASHPROC -DHAVE_COMM_F2C -DHAVE_TIMES -DHAVE_GETTIMEOFDAY </append>
	  </CPPDEFS>
	  <NETCDF_PATH>$ENV{NETCDF_FORTRAN_ROOT}</NETCDF_PATH>
	  <PIO_FILESYSTEM_HINTS>lustre</PIO_FILESYSTEM_HINTS>
	  <PNETCDF_PATH>$ENV{PARALLEL_NETCDF_ROOT}</PNETCDF_PATH>
	  <SLIBS>
	    <append>-L$(NETCDF_PATH)/lib -lnetcdff -L$(NETCDF_C_ROOT)/lib -lnetcdf -L$(NETLIB_LAPACK_PATH)/lib/intel64 -lmkl -ldl </append>
	  </SLIBS>
	</compiler>
```

=== "Nibi"

```xml title="~/.cime/config_compilers.xml"
<?xml version="1.0"?>

	<compiler MACH="nibi">
	  <CPPDEFS>
	    <!-- these flags enable nano timers -->
	    <append MODEL="gptl"> -DHAVE_NANOTIME -DBIT64 -DHAVE_VPRINTF -DHAVE_BACKTRACE -DHAVE_SLASHPROC -DHAVE_COMM_F2C -DHAVE_TIMES -DHAVE_GETTIMEOFDAY </append>
	  </CPPDEFS>
	  <NETCDF_PATH>$ENV{NETCDF_FORTRAN_ROOT}</NETCDF_PATH>
	  <PIO_FILESYSTEM_HINTS>lustre</PIO_FILESYSTEM_HINTS>
	  <PNETCDF_PATH>$ENV{PARALLEL_NETCDF_ROOT}</PNETCDF_PATH>
	  <SLIBS>
	    <append>-L$(NETCDF_PATH)/lib -lnetcdff -L$(NETCDF_C_ROOT)/lib -lnetcdf -L$(NETLIB_LAPACK_PATH)/lib/intel64 -lmkl -ldl </append>
	  </SLIBS>
	</compiler>
```

=== "Narval"

```xml title="~/.cime/config_compilers.xml"
<?xml version="1.0"?>

	<compiler MACH="narval">
	  <CPPDEFS>
	    <!-- these flags enable nano timers -->
	    <append MODEL="gptl"> -DHAVE_NANOTIME -DBIT64 -DHAVE_VPRINTF -DHAVE_BACKTRACE -DHAVE_SLASHPROC -DHAVE_COMM_F2C -DHAVE_TIMES -DHAVE_GETTIMEOFDAY </append>
	  </CPPDEFS>
	  <NETCDF_PATH>$ENV{NETCDF_FORTRAN_ROOT}</NETCDF_PATH>
	  <PIO_FILESYSTEM_HINTS>lustre</PIO_FILESYSTEM_HINTS>
	  <PNETCDF_PATH>$ENV{PARALLEL_NETCDF_ROOT}</PNETCDF_PATH>
	  <SLIBS>
	    <append>-L$(NETCDF_PATH)/lib -lnetcdff -L$(NETCDF_C_ROOT)/lib -lnetcdf -L$(NETLIB_LAPACK_PATH)/lib/intel64 -lmkl -ldl </append>
	  </SLIBS>
	</compiler>
```

=== "Niagara"

```xml title="~/.cime/config_compilers.xml"
<?xml version="1.0"?>

	<compiler MACH="niagara">
	  <CPPDEFS>
	    <!-- these flags enable nano timers -->
	    <append MODEL="gptl"> -DHAVE_NANOTIME -DBIT64 -DHAVE_VPRINTF -DHAVE_BACKTRACE -DHAVE_SLASHPROC -DHAVE_COMM_F2C -DHAVE_TIMES -DHAVE_GETTIMEOFDAY </append>
	  </CPPDEFS>
	  <NETCDF_PATH>$ENV{NETCDF_FORTRAN_ROOT}</NETCDF_PATH>
	  <PIO_FILESYSTEM_HINTS>lustre</PIO_FILESYSTEM_HINTS>
	  <PNETCDF_PATH>$ENV{PARALLEL_NETCDF_ROOT}</PNETCDF_PATH>
	  <SLIBS>
	    <append>-L$(NETCDF_PATH)/lib -lnetcdff -L$(NETCDF_C_ROOT)/lib -lnetcdf -L$(NETLIB_LAPACK_PATH)/lib/intel64 -lmkl -ldl </append>
	  </SLIBS>
	</compiler>
```

=== "Rorqual"

```xml title="~/.cime/config_compilers.xml"
<?xml version="1.0"?>

	<compiler MACH="rorqual">
	  <CPPDEFS>
	    <append MODEL="gptl"> -DHAVE_NANOTIME -DBIT64 -DHAVE_VPRINTF -DHAVE_BACKTRACE -DHAVE_SLASHPROC -DHAVE_COMM_F2C -DHAVE_TIMES -DHAVE_GETTIMEOFDAY </append>
	  </CPPDEFS>
	  <NETCDF_PATH>$ENV{NETCDF_FORTRAN_ROOT}</NETCDF_PATH>
	  <PIO_FILESYSTEM_HINTS>lustre</PIO_FILESYSTEM_HINTS>
	  <PNETCDF_PATH>$ENV{PARALLEL_NETCDF_ROOT}</PNETCDF_PATH>
	  <SLIBS>
	    <append>-L$(NETCDF_PATH)/lib -lnetcdff -L$(NETCDF_C_ROOT)/lib -lnetcdf -L$(NETLIB_LAPACK_PATH)/lib/intel64 -lmkl -ldl </append>
	  </SLIBS>
	</compiler>
```

* Validate your XML compiler file with the following commands:

    ```bash
    [name@server ~]$ xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_compilers_v2.xsd ~/.cime/config_compilers.xml
    ```
    Output:
    ```
    /home/name/.cime/config_compilers.xml validates
    ```

## Creating a Test Case

The following commands assume the default model `cesm` and the `current` machine:

```bash
mkdir -p $SCRATCH/cesm/inputdata
mkdir -p $SCRATCH/cesm/output
/path/to/CESM/cime/scripts/create_newcase --case test_case --compset IHistClm50Bgc --res f19_g17
cd test_case
```

```bash
[name@server test_case]$ ./case.setup
[name@server test_case]$ ./case.build
[name@server test_case]$ ./check_input_data --download
```

```bash
[name@server test_case]$ ./preview_run
[name@server test_case]$ ./case.submit
```

## Reference

* [Main website](https://www.cesm.ucar.edu/)
    * [CESM Quickstart Guide (CESM2.1)](https://escomp.github.io/CESM/versions/cesm2.1/html/)
    * [CESM Coupled Model XML Files](https://esmci.github.io/cime/versions/maint-5.6/html/xml_files/cesm.html)