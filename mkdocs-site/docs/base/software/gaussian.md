---
title: "Gaussian"
slug: "gaussian"
lang: "base"

source_wiki_title: "Gaussian"
source_hash: "9fa5037928eee10d64055141f4385ca8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:32:59.821827+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "blank line"
  - "SBATCH"
  - "input file"
  - "job submission"
  - "computational chemistry"
  - "keywords line"
  - "error messages"
  - "restart input"
  - "Slurm scheduler"
  - "memory"
  - "run scripts"
  - "runtime files"
  - "Nibi and Fir clusters"
  - "restart jobs"
  - "#p restart"
  - "interactive jobs"
  - "run time"
  - "cpus-per-task"
  - "gaussian/g16"
  - "SLURM"
  - "rwf file"
  - "NBO7"
  - "Gaussian"

questions:
  - "What are the limitations regarding parallel execution and node usage when running Gaussian on the Nibi and Fir clusters?"
  - "What specific conditions must users agree to in order to obtain a license and access the Gaussian software?"
  - "What are the recommended resource limits and best practices for submitting a Gaussian job script using the Slurm scheduler?"
  - "How does the choice between the `g16` and `G16` commands affect where temporary runtime files are stored during a job?"
  - "What is the recommended procedure and command sequence for running an interactive Gaussian job for testing purposes on a compute node?"
  - "What specific modifications must be made to the Gaussian input file to successfully restart a job from a previous `.rwf` file?"
  - "How are the memory and CPU allocations in the SLURM script related to the parameters defined in the Gaussian input file?"
  - "What is the expected execution time limit set for this batch job?"
  - "Which commands are required to load the Gaussian 16 environment and execute the simulation?"
  - "What specific file from a previous run is required to initiate a restart?"
  - "How must the keywords line and the end of the input file be formatted to properly execute the restart?"
  - "According to the sample input, what additional resource allocations and file paths can be defined during the restart process?"
  - "Where can users locate the example input files and run scripts for the various Gaussian versions?"
  - "Which specific versions of Gaussian are required to run NBO6 and NBO7?"
  - "Where can users find suggestions and resolutions for error messages produced by the software?"
  - "Where can users locate the example input files and run scripts for the various Gaussian versions?"
  - "Which specific versions of Gaussian are required to run NBO6 and NBO7?"
  - "Where can users find suggestions and resolutions for error messages produced by the software?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*See also [Gaussian error messages](chemistry/gaussian_error_messages.md).*

Gaussian is a computational chemistry application produced by [Gaussian, Inc.](http://gaussian.com/)

## Limitations

We currently support Gaussian on [Nibi](../clusters/nibi.md) and [Fir](fir.md).

[Cluster/network parallel execution](https://gaussian.com/running/?tabid=4) of Gaussian, also known as "Linda parallelism", is not supported at any of our national systems. Only ["shared-memory multiprocessor parallel execution"](https://gaussian.com/running/?tabid=4) is supported.
Therefore no Gaussian job can use more than a single compute node.

## License agreement

In order to use Gaussian you must agree to certain conditions. Please [contact support](../support/technical_support.md) with a copy of the following statement:
1.  I am not a member of a research group developing software competitive to Gaussian.
2.  I will not copy the Gaussian software, nor make it available to anyone else.
3.  I will properly acknowledge Gaussian Inc. and [the Alliance](https://alliancecan.ca/en/services/advanced-research-computing/acknowledging-alliance) in publications.
4.  I will notify the Alliance of any change in the above acknowledgement.
If you are a sponsored user, your sponsor (PI) must also have such a statement on file with us.

We will then grant you access to Gaussian.

## Running Gaussian on Fir and Nibi
The `gaussian` module is installed on [Nibi](../clusters/nibi.md) and [Fir](fir.md). To check what versions are available use the `module spider` command as follows:

```bash
module spider gaussian
```

For module commands, please see [Using modules](../programming/utiliser_des_modules.md).

### Job submission
The national clusters use the Slurm scheduler; for details about submitting jobs, see [Running jobs](../running-jobs/running_jobs.md).

Since only the "shared-memory multiprocessor" parallel version of Gaussian is supported, your jobs can use only one node and up to the maximum cores per node. However due to the scalability of Gaussian, we recommend that you *use no more than 32 CPUs per job unless you have good evidence that you can use them efficiently!* The new clusters Nibi and Fir have 192 CPUs per node. Please do not simply run full-node Gaussian jobs on these clusters; it will be inefficient. If your jobs are limited by the amount of available memory on a single node, be aware that there are a few nodes at each site with more than the usual amount of memory. Please refer to the pages [Fir](fir.md#node-characteristics) and [Nibi](../clusters/nibi.md#node-characteristics) for the number and capacity of such nodes.

Besides your input file (in our example, "name.com"), you have to prepare a job script to define the compute resources for the job; both input file and job script must be in the same directory.

There are two options to run your Gaussian job on the clusters, based on the location of the default runtime files and the job size.

#### G16 (G09, G03)

This option will save the default runtime files (unnamed .rwf, .inp, .d2e, .int, .skr files) to `/scratch/username/jobid/`. Those files will stay there when the job is unfinished or failed for whatever reason, you could locate the .rwf file for restart purpose later.

The following example is a G16 job script:

!!! note
    Note that for coherence, we use the same name for each files, changing only the extension (name.sh, name.com, name.log).

```bash title="mysub.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --mem=32G             # memory, roughly 2 times %mem defined in the input name.com file
#SBATCH --time=02-00:00       # expect run time (DD-HH:MM)
#SBATCH --cpus-per-task=32    # No. of cpus for the job as defined by %nprocs in the name.com file
module load gaussian/g16.c01
G16 name.com            # G16 command, input: name.com, output: name.log
```

To use Gaussian 09 or Gaussian 03, simply modify the `module load gaussian/g16.c01` to `gaussian/g09.e01` or `gaussian/g03.d01`, and change `G16` to `G09` or `G03`. You can modify the `--mem`, `--time`, `--cpus-per-task` to match your job's requirements for compute resources.

#### g16 (g09, g03)

This option will save the default runtime files (unnamed .rwf, .inp, .d2e, .int, .skr files) temporarily in `$SLURM_TMPDIR` (`/localscratch/username.jobid.0/`) on the compute node where the job was scheduled to run. Gaussian jobs will run faster when using the `/localscratch`. These files will be automatically removed by the scheduler when the job finishes, whether successfully or not. If you plan to use the .rwf file to restart the job in a later time, you must explicitly specify and name your own .rwf file in the Gaussian input file.

`/localscratch` is ~3TB shared by all jobs running on the same node. If your job files would be bigger than or close to that size range, you would instead use the G16 (G09, G03) option.

The following example is a g16 job script:

```bash title="mysub.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --mem=32G             # memory, roughly 2 times %mem defined in the input name.com file
#SBATCH --time=02-00:00       # expect run time (DD-HH:MM)
#SBATCH --cpus-per-task=32    # No. of cpus for the job as defined by %nprocs in the name.com file
module load gaussian/g16.c01
g16 < name.com >& name.log              # g16 command, input: name.com, output: name.log
```

#### Submit the job
```bash
sbatch mysub.sh
```

### Interactive jobs
You can run interactive Gaussian job for testing purpose on the clusters. It's not a good practice to run interactive Gaussian jobs on a login node. You can start an interactive session on a compute node with salloc, the example for an hour, 8 cpus and 10G memory Gaussian job is like
Goto the input file directory first, then use salloc command:

```bash
salloc --time=1:0:0 --cpus-per-task=8 --mem=10g
```

Then use either

```bash
module load gaussian/g16.c01
G16 g16_test2.com    # G16 saves runtime file (.rwf etc.) to /scratch/yourid/93288/
```

or

```bash
module load gaussian/g16.c01
g16 < g16_test2.com >& g16_test2.log &   # g16 saves runtime file to /localscratch/yourid/
```

### Restart jobs
Gaussian jobs can always be restarted from the previous `rwf` file.

Geometry optimization can be restarted from the `chk` file as usual.
One-step computation, such as Analytic frequency calculations, including properties like ROA and VCD with ONIOM; CCSD and EOM-CCSD calculations; NMR; Polar=OptRot; CID, CISD, CCD, QCISD and BD energies, can be restarted from the `rwf` file.

To restart a job from previous `rwf` file, you need to know the location of this `rwf` file from your previous run.

The restart input is simple: first you need to specify `%rwf` path to the previous `rwf` file, secondly change the keywords line to be `#p restart`, then leave a blank line at the end.

A sample restart input is like:
```text title="restart.com"
%rwf=/scratch/yourid/jobid/name.rwf
%NoSave
%chk=name.chk
%mem=5000mb
%nprocs=16
#p restart
(one blank line)
```

### Examples
An example input file and the run scripts `*.sh` can be found in
`/opt/software/gaussian/version/examples/`
where version is either g03.d10, g09.e01, or g16.b01

## Notes
1.  NBO7 is included in g16.c01 version only, both `nbo6` and `nbo7` keywords will run NBO7 in g16.c01
2.  NBO6 is available in g09.e01 and g16.b01 versions.

## Errors
Some of the error messages produced by Gaussian have been collected, with suggestions for their resolution. See [Gaussian error messages](chemistry/gaussian_error_messages.md).