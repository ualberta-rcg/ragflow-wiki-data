---
title: "Using GPUs with Slurm/en"
tags:
  - slurm

keywords:
  []
---

= Introduction =

To request one or more GPUs for a [Slurm](running-jobs.md) job, use this form:
  --gpus-per-node=<model_specifier>:<number>

For example:
  --gpus-per-node=a100:1

This requests a single A100 GPU (unless you also use `--nodes` to specify more than a single node).
See the following section, <i>Available GPUs,</i> for valid model specifiers.

The following form can also be used:
  --gres=gpu:<model_specifier>:<number>
This form may not be supported in the future.  We recommend that you replace it in your scripts with `--gpus-per-node`.

Slurm supports a variety of other directives that you can use to request GPU resources: `--gpus`, `--gpus-per-socket`, `--gpus-per-task`, `--mem-per-gpu`, and `--ntasks-per-gpu`.  Please see the Slurm documentation for [sbatch](https://slurm.schedmd.com/sbatch.html) for more about these.  Our staff do not test all of these; if you try one but don't get the result you expect, [contact technical support](technical-support.md).

For general advice on job scheduling, see [Running jobs](running-jobs.md).

= Available GPUs =
The following table summarizes the available GPU models and their corresponding specifiers:

{| class="wikitable"
|-
! Cluster !! GPU model 
!MIG!! Model specifiers
for Slurm 
!Synonyms for Slurm
|- 
| rowspan=4|[Fir](fir#node_characteristics.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|
|-
| rowspan=5|[Narval](narval-en#node_characteristics.md) || rowspan=5|A100-40gb 
| || a100 
|
|-
|1/8
|  a100_1g.5gb  
|
|-
|2/8
|  a100_2g.10gb 
|
|-
|2/8
|  a100_3g.20gb 
|
|-
|4/8
|  a100_4g.20gb 
|
|- 
| rowspan=5|[Nibi](nibi#node_characteristics.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|h100_1g.10gb h100_1.10 h100_10gb
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|h100_2g.20gb h100_2.20 h100_20gb
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|h100_3g.40gb h100_3.40 h100_40gb
|-
| MI300A-128gb  
| || mi300a 
|
|- 
| rowspan=4|[Rorqual](rorqual-en#node_characteristics.md) || rowspan=4|H100-80gb 
| || h100 
|
|-
|1/8
|   nvidia_h100_80gb_hbm3_1g.10gb 
|h100_1g.10gb h100_1.10 h100_10gb
|-
|2/8
|   nvidia_h100_80gb_hbm3_2g.20gb 
|h100_2g.20gb h100_2.20 h100_20gb
|-
|3/8
|   nvidia_h100_80gb_hbm3_3g.40gb 
|h100_3g.40gb h100_3.40 h100_40gb
|-
| [Trillium](trillium#node_characteristics.md) || H100-80gb 
| || h100 
|
|-
| rowspan=2|[Killarney](killarney#killarney_hardware_specifications.md) || H100-80gb 
| || h100 
|
|-
|  L40S-48gb 
| || l40s 
|
|-
| rowspan=2|[tamIA](tamia-en#node_characteristics.md) || H100-80gb 
| || h100 
|
|-
|  H200 
| || h200 
|
|-
| rowspan=2|[Vulcan](vulcan#vulcan_hardware_specifications.md) || L40S-48gb 
| || l40s 
|
|}

GPU model specifiers (including MIG specifiers) available on any given cluster can be obtained from Slurm with the following command.
This may be useful if the table above has not been updated with the latest changes.

```bash

```
grep gpused 's/gpu://g'sed 's/),/\n/g'cut -d: -f1sortuniq}}

There are short synonyms available for some of the MIG specifiers at certain sites; this command will not provide those synonyms.
Also, the presence of a GPU model does not guarantee that you will be able to use one of the corresponding specifiers in your jobs; there may be 
further restrictions on what model specifiers are available based on (for example) which research group you belong.
For further information see the site-specific page by clicking on the cluster name in the above table, or [contact support](technical-support.md).

If you do not supply a model specifier your job may be rejected or it may be sent to an arbitrary GPU instance.
There are very few programs which can use an arbitrary GPU efficiently,
so we strongly recommend that you always provide a specific GPU model specifier in your job scripts. 

There are GPUs available at Arbutus, but like other cloud resources they cannot be scheduled via Slurm.
See [Cloud resources](cloud-resources.md) for more details.

## Multi-Instance GPUs (MIGs) 
MIG is a technology that partitions a GPU into multiple instances.
Your jobs might be able to use a MIG instance instead of a whole GPU.
Please see [Multi-Instance_GPU](multi-instance_gpu.md) for more about this.

= Requesting CPU cores and system memory =

Along with each GPU instance, your job should have a number of CPU cores (default is `1`) and some amount of system memory. The recommended maximum numbers of CPU cores and gigabytes of system memory per GPU instance are listed in the [table of bundle characteristics](allocations_and_compute_scheduling#ratios_in_bundles.md).

= Examples =

## Single-core job 
If you need only a single CPU core and one GPU:

**`gpu_serial_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1
#SBATCH --mem=4000M               # memory per node
#SBATCH --time=0-03:00
./program                         # you can use 'nvidia-smi' for a test
```

## Multi-threaded job 
For a GPU job which needs multiple CPUs in a single node:

**`gpu_threaded_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus-per-node=a100:1 
#SBATCH --cpus-per-task=6         # CPU cores or threads
#SBATCH --mem=4000M               # memory per node
#SBATCH --time=0-03:00
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./program
```

For each full GPU requested, we recommend
* on Fir, no more than 12 CPU cores;
* on Narval, no more than 12 CPU cores
* on Nibi, no more than 14 CPU cores, 
* on Rorqual, no more than 16 CPU cores

## MPI job 

**`gpu_mpi_job.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gpus=a100:8             # total number of GPUs
#SBATCH --ntasks-per-gpu=1        # total of 8 MPI processes
#SBATCH --cpus-per-task=6         # CPU cores per MPI process
#SBATCH --mem-per-cpu=5G          # host memory per CPU core
#SBATCH --time=0-03:00            # time (DD-HH:MM)
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
srun --cpus-per-task=$SLURM_CPUS_PER_TASK ./program
```

## Whole nodes 
If your application can efficiently use an entire node and its associated GPUs, you will probably experience shorter wait times if you ask Slurm for a whole node. Use one of the following job scripts as a template. 

### Packing single-GPU jobs within one SLURM job

If you need to run four single-GPU programs or two 2-GPU programs for longer than 24 hours, [GNU Parallel](gnu-parallel.md) is recommended. A simple example is:
<pre>
cat params.input | parallel -j4 'CUDA_VISIBLE_DEVICES=$(({%} - 1)) python {} &> {#}.out'
</pre>
In this example, the GPU ID is calculated by subtracting 1 from the slot ID {%} and {#} is the job ID, starting from 1.

A `params.input` file should include input parameters in each line, like this:
<pre>
code1.py
code2.py
code3.py
code4.py
...
</pre>
With this method, you can run multiple tasks in one submission. The `-j4` parameter means that GNU Parallel can run a maximum of four concurrent tasks, launching another as soon as one ends. CUDA_VISIBLE_DEVICES is used to ensure that two tasks do not try to use the same GPU at the same time.

## Profiling GPU tasks 

On [Narval](narval-en.md) and [Rorqual](rorqual-en.md), profiling is possible but requires disabling the
[NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm). This must be done during job submission by setting the `DISABLE_DCGM` environment variable:

```bash

```
1 salloc --accountdef-someuser --gpus-per-nodea100:1 --mem4000M --time03:00}}

Then, in your interactive job, wait until DCGM is disabled on the node: 

```bash

```
 grep 'Hostengine build info:')" ]; do  sleep 5; done}}

Finally, launch your profiler. For more details on profilers, see [Debugging and profiling](debugging-and-profiling.md).

On Fir and Nibi, GPU profiling like the above technique is not available yet.

= See also =
[CUDA](cuda.md)

[Multi-Instance GPU](multi-instance-gpu.md)

[Running jobs](running-jobs.md)

[Metrix monitoring portal](metrix-en.md)

[NVTOP (htop-like monitor for GPUs)](nvtop.md)

[Cuda Multi-Process Service (MPS)](hyper-q---mps.md)