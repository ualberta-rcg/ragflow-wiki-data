---
title: "CESM"
slug: "cesm"
lang: "base"

source_wiki_title: "CESM"
source_hash: "7afc194713d75b8a61853119d48d399f"
last_synced: "2026-11-15T02:27:25.182546+00:00"
last_processed: "2026-11-15T03:25:27.206791+00:00"

tags:
  []

keywords:
  - "CPPDEFS nano timers"
  - "NETCDF_C_PATH"
  - "GMAKE_J"
  - "purge"
  - "CESM 2.1"
  - "OS"
  - "job_submission"
  - "queues"
  - "compiler"
  - "I_MPI_CC"
  - "batch system type"
  - "jobid_pattern"
  - "openmpi"
  - "load"
  - "batch_system type=\"slurm\""
  - "SLIBS linking libraries"
  - "config_machines"
  - "cmake/3.27.7"
  - "check_input_data"
  - "CESM Quickstart Guide"
  - "DOUT_S_ROOT"
  - "config_batch.xml validation"
  - "compset IHistClm50Bgc"
  - "flexiblas"
  - "mkl"
  - "FALSE"
  - "Community Earth System Model"
  - "SLURM"
  - "StdEnv/2023"
  - "NETCDF_FORTRAN_PATH"
  - "intel"
  - "slurm"
  - "netcdf-mpi"
  - "scancel"
  - "sbatch"
  - "intel/2023.2.1"
  - "NODENAME_REGEX"
  - "PROJECT_REQUIRED"
  - "module system"
  - "intel compiler"
  - "create_newcase"
  - "lc_slurm"
  - "MAX_MPITASKS_PER_NODE"
  - "OMP_STACKSIZE"
  - "batch_directive #SBATCH"
  - "config_compilers.xml"
  - "case.build"
  - "CPPDEFS"
  - "Narval"
  - "NETCDF_PATH"
  - "xml-libxml"
  - "nibi"
  - "TRUE"
  - "resource_limits"
  - "COMPILERS"
  - "DIN_LOC_ROOT_CLMFORC"
  - "batch_system"
  - "queue"
  - "xmllint validation"
  - "SCRATCH/cesm/inputdata"
  - "checkout_externals"
  - "git clone"
  - "HAVE_NANOTIME"
  - "CIME_OUTPUT_ROOT"
  - "CESM"
  - "netcdf-fortran-mpi"
  - "module"
  - "BATCH_SYSTEM"
  - "openmpi/4.1.5"
  - "#SBATCH"
  - "NETLIB_LAPACK_PATH"
  - "walltimemax"
  - "gptl"
  - "case.setup"
  - "module_system"
  - "config_machines.xml"

questions:
  - "What are the required commands and additional external‑dependency changes for installing CESM 2.1.5 compared to the older 2.1.3 version?"
  - "How do you run the checkout_externals script to obtain the model components and validate that the download succeeded?"
  - "Which fields in the ~/.cime/config_machines.xml file for the “Fir” machine must be edited before using CESM on that cluster?"
  - "Which modules are loaded for the Intel compiler and the OpenMPI library in this configuration?"
  - "What environment variables are defined for NetCDF paths and Intel MPI compiler wrappers, and what values do they hold?"
  - "What stack size limit is specified under `<resource_limits>`, and how is it expressed in the XML?"
  - "What directory is set for CLM forcing data in the `<DIN_LOC_ROOT_CLMFORC>` tag?"
  - "Which batch system is specified for job scheduling in the configuration?"
  - "What are the maximum numbers of total tasks and MPI tasks allowed per node as defined by `<MAX_TASKS_PER_NODE>` and `<MAX_MPITASKS_PER_NODE>`?"
  - "What operating system is specified for the machine “nibi” in the configuration file?"
  - "Which compilers are listed as available for the “nibi” machine?"
  - "What node name pattern does the `<NODENAME_REGEX>` element define for “nibi”?"
  - "Which batch system is configured and what command is used to launch MPI jobs in this setup?"
  - "Which compiler and MPI‑related modules are loaded in the <module_system> section?"
  - "What environment variables are defined for NetCDF libraries and other runtime settings?"
  - "What directories are specified for the NETCDF_C_PATH and NETLIB_LAPACK_PATH environment variables, and what software do they correspond to?"
  - "What is the purpose of setting the OMP_STACKSIZE environment variable to 256M?"
  - "Which compiler is designated by the I_MPI_CC environment variable in this configuration?"
  - "What compilers and MPI libraries are configured for the Narval machine in the `config_machines.xml` file?"
  - "How does the module system load environment modules for the Intel compiler and the OpenMPI library on Narval?"
  - "Where are the default paths for CIME output (`CIME_OUTPUT_ROOT`) and input data (`DIN_LOC_ROOT`) specified for the Narval configuration?"
  - "What are the directory paths set for NETCDF_FORTRAN, NETCDF_C, and NETLIB_LAPACK in the environment variables?"
  - "Which compilers and MPI library are specified for the Rorqual machine, and how is the MPI run command configured?"
  - "How is the module system initialized and which modules are loaded by default according to the config_machines.xml for Rorqual?"
  - "Which software modules are being loaded in this configuration?"
  - "What specific version of the `netcdf-mpi` module is specified?"
  - "What directory is assigned to the `NETCDF_PATH` environment variable?"
  - "What is the purpose of the `<cmd_path>` entries for the different languages (python, csh, sh) in this configuration?"
  - "Which software modules are being loaded, and what specific versions are specified?"
  - "How does the `compiler=\"intel\"` attribute influence the loading of the listed modules?"
  - "What modules and environment variables are specified in the `<module_system>` and `<environment_variables>` sections for the machine configuration?"
  - "How can you validate the `config_machines.xml` file and verify the machine’s settings using the provided commands?"
  - "What minimal XML content should be placed in `~/.cime/config_batch.xml`, and which key entries does it define for batch submission?"
  - "What are the valid values listed for the batch system type in this configuration?"
  - "What does the PROJECT_REQUIRED entry in the job_submission group control, and what values can it take?"
  - "Which entry defines whether a project identifier is required by default, and what is its default setting?"
  - "What batch system type is set for the machine in the provided `config_batch.xml` files?"
  - "Which SLURM directives and submit arguments are defined for job submission (e.g., job name, nodes, tasks per node, output, exclusivity, and memory)?"
  - "How are job dependencies and email notifications configured in the SLURM batch system configuration?"
  - "What are the walltimemax, nodemin, and nodemax values set for the “nibi” queue in the regular batch system configuration?"
  - "Which batch system type and corresponding submit and cancel commands are defined for the “Narval” configuration?"
  - "How is the placeholder for unknown queue directives represented in the XML snippet?"
  - "What directives and arguments must be defined in ~/.cime/config_batch.xml to correctly configure a Slurm batch system (e.g., job name, nodes, tasks per node, output, memory, etc.)?"
  - "How can you validate that your config_batch.xml file conforms to the CIME XML schema, and what command is used for this validation?"
  - "What minimal XML content should be placed in ~/.cime/config_compilers.xml for a specific machine (such as “fir”) to set compiler flags and NetCDF paths?"
  - "What common compiler settings (such as CPPDEFS, NETCDF_PATH, PIO_FILESYSTEM_HINTS, and SLIBS) are defined for the machines nibi, narval, and rorqual in the config_compilers.xml file?"
  - "How do you validate the ~/.cime/config_compilers.xml file against the CESM schema, and which command is used for this validation?"
  - "Which commands are needed to set up directories and create a new CESM test case with the IHistClm50Bgc compset and f19_g17 resolution?"
  - "What compiler is being defined in the XML snippet?"
  - "Which preprocessor flags are appended for the model \"gptl\" in the CPPDEFS section?"
  - "How is the NetCDF Fortran library path specified in this configuration?"
  - "What is the role of the `create_newcase` script when setting up a new CESM test case?"
  - "Which compset and resolution are specified in the example command for creating the test case?"
  - "What directory structure must be created beforehand, as shown in the commands, and why is it needed?"
  - "What is the purpose of the commands `./case.setup`, `./case.build`, and `./check_input_data --download` in the test_case workflow?"
  - "How do the `./preview_run` and `./case.submit` commands differ from the initial setup commands, and what role do they play in executing the test case?"
  - "Where can users find additional CESM documentation and resources, such as the main website, the Quickstart Guide, and the Coupled Model XML Files?"

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

The configuration files and commands below are designed for a local installation of CESM 2.1. Local installations allow for [source code changes](https://ncar.github.io/CESM-Tutorial/notebooks/sourcemods/sourcemods.html), which may be useful for specific research purposes. Before making the adaptations as described in the sections below, please [download CESM 2.1 from the CESM developers](https://www.cesm.ucar.edu/models/cesm2/download) in your local directory.

=== "Version 2.1.5"

This version is based on the [latest official release](https://github.com/ESCOMP/CESM/releases/latest).

```bash
git clone -b release-cesm2.1.5 https://github.com/ESCOMP/CESM.git /path/to/CESM
```

=== "Version 2.1.3"

This older version has been very popular in the research community, but it may become obsolete because this version is no longer officially supported.

To make this version work, **some external dependencies must be replaced** with newer versions which are no longer exactly matching the 2.1.3 version of CESM; researchers are responsible for confirming validity.

```bash
sed -i 's/cam_cesm2_1_rel_41/cam_cesm2_1_rel_59/g' /path/to/CESM/Externals.cfg
sed -i 's/cime5.6.32/cime5.6.51/g' /path/to/CESM/Externals.cfg
sed -i 's/cism-release-cesm2.1.2_02/cism-release-cesm2.1.2_03/g' /path/to/CESM/Externals.cfg
```

## Checkout externals

Before your first use of CESM, you may checkout the individual model components by running the `checkout_externals` script.

```bash
/path/to/CESM/manage_externals/checkout_externals
```

You may need to accept a certificate from the CESM repository to download input files. To validate, run the same script with `-S`.

```bash
/path/to/CESM/manage_externals/checkout_externals -S
```

See [this documentation page](https://escomp.github.io/CESM/versions/cesm2.1/html/downloading_cesm.html) for an example of a valid output.

## Local machine file

*   Create and edit the file `~/.cime/config_machines.xml` from the following minimal content per cluster; **update both configuration lines** having `def-EDIT_THIS` with the compute account you want to use on the cluster.

    === "Fir"

        !!! example "File: ~/.cime/config_machines.xml"
            ```xml
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

        !!! example "File: ~/.cime/config_machines.xml"
            ```xml
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

        Note: despite the Intel software dependencies, the configuration below works on Narval's AMD processors.

        !!! example "File: ~/.cime/config_machines.xml"
            ```xml
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

    === "Rorqual"

        Note: despite the Intel software dependencies, the configuration below works on Rorqual's AMD processors.

        !!! example "File: ~/.cime/config_machines.xml"
            ```xml
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

*   Validate your XML machine file with the following commands:

    ```bash
    xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_machines.xsd ~/.cime/config_machines.xml
    ```

    ```text
    /home/name/.cime/config_machines.xml validates
    ```

    ```bash
    /path/to/CESM/cime/scripts/query_config --machines current
    ```

    ```text
      rorqual (current) : https://docs.alliancecan.ca/wiki/Rorqual/en
          os              LINUX
          compilers       intel,gnu
          pes/node        192
          max_tasks/node  192
    ```

*   Check the official template for additional parameters:

    ```bash
    less /path/to/CESM/cime/config/xml_schemas/config_machines_template.xml
    ```

## Local batch file

*   Create and edit the file `~/.cime/config_batch.xml` from the following minimal content:

    === "Fir"

        !!! example "File: ~/.cime/config_batch.xml"
            ```xml
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

        !!! example "File: ~/.cime/config_batch.xml"
            ```xml
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

        !!! example "File: ~/.cime/config_batch.xml"
            ```xml
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

    === "Rorqual"

        !!! example "File: ~/.cime/config_batch.xml"
            ```xml
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

*   Validate your XML batch file with the following commands:

    ```bash
    xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_batch.xsd ~/.cime/config_batch.xml
    ```

    ```text
    /home/name/.cime/config_batch.xml validates
    ```

*   Check the documentation for additional **[configuration parameters and examples](https://esmci.github.io/cime/versions/maint-5.6/html/xml_files/cesm.html#cimeroot-config-cesm-machines)**.

## Local compilers file

*   Create and edit the file `~/.cime/config_compilers.xml` from the following minimal content per cluster:

    === "Fir"

        !!! example "File: ~/.cime/config_compilers.xml"
            ```xml
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

        !!! example "File: ~/.cime/config_compilers.xml"
            ```xml
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

        !!! example "File: ~/.cime/config_compilers.xml"
            ```xml
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

    === "Rorqual"

        !!! example "File: ~/.cime/config_compilers.xml"
            ```xml
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

*   Validate your XML compiler file with the following commands:

    ```bash
    xmllint --noout --schema /path/to/CESM/cime/config/xml_schemas/config_compilers_v2.xsd ~/.cime/config_compilers.xml
    ```

    ```text
    /home/name/.cime/config_compilers.xml validates
    ```

## Creating a test case

The following commands assume the default model `cesm` and the `current` machine:

```bash
mkdir -p $SCRATCH/cesm/inputdata
mkdir -p $SCRATCH/cesm/output
/path/to/CESM/cime/scripts/create_newcase --case test_case --compset IHistClm50Bgc --res f19_g17
cd test_case
```

```bash
./case.setup
./case.build
./check_input_data --download
```

```bash
./preview_run
./case.submit
```

## Reference

*   [Main website](https://www.cesm.ucar.edu/)
    *   [CESM Quickstart Guide (CESM2.1)](https://escomp.github.io/CESM/versions/cesm2.1/html/)
    *   [CESM Coupled Model XML Files](https://esmci.github.io/cime/versions/maint-5.6/html/xml_files/cesm.html)