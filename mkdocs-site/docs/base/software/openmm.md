---
title: "OpenMM"
slug: "openmm"
lang: "base"

source_wiki_title: "OpenMM"
source_hash: "db963c109f74c1efeb1816f0d4a23c31"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:33:30.498486+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Introduction
[OpenMM](https://openmm.org/) is an open-source molecular dynamics toolkit designed for flexibility and programmability. It is used via Python, offering both application-level classes for running simulations and a lower-level API that allows users to integrate OpenMM directly into their own code for custom workflows. OpenMM can natively read and simulate systems prepared with AMBER, GROMACS, and CHARMM, enabling seamless reuse of existing biomolecular setups. Its plugin architecture supports integration with machine-learning potentials, including TorchMD-Net, MACE, TorchANI, AIMNet2, and DeepMD for general-purpose or hybrid ML/MM simulations.

## Strengths
* Flexible Python interface with both high-level classes and low-level API access for custom workflows.
* High-level plugin framework for ML-driven potentials and hybrid simulations.
* Efficient execution on CPUs and GPUs, suitable for HPC platforms.
* Native support for major biomolecular formats (AMBER, GROMACS, CHARMM).
* Open-source with an active ecosystem of plugins for ML and advanced force fields.

## Weak points
* Slower than highly optimized classical MM engines (GROMACS, AMBER) for large-scale production runs.
* Flexibility can add complexity for hybrid ML/MM simulations.
* Specialized trajectory analysis may require external tools.

# Environment modules

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0
```

!!! note
    The ambertools module is optional and required only if you plan to simulate AMBER-prepared systems.

Optionally, create a Python virtual environment if you want to install extra packages (e.g., ML potentials).

# Preparing Input Files

OpenMM can directly read Amber topology and coordinate/restart files if simulating AMBER systems.

Ensure your system is equilibrated and minimized in Amber or another package before transferring files to HPC.

For GROMACS or CHARMM systems, OpenMM can read their respective formats without AmberTools.

# Job submission
Below is a job script for a simulation using one GPU.

```bash title="submit_openmm.cuda.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1 
#SBATCH --gpus=h100:1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-01:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0

python openmm_input.py
```

# Python simulation script
The example Python script below loads Amber parameter and restart files, builds the OpenMM simulation system, sets up the integrator, and runs the dynamics.

```python title="openmm_input.py"
import os, sys, time
import openmm.app as app
from openmm import app, unit, Platform, LangevinMiddleIntegrator, MonteCarloBarostat
from parmed import load_file
from parmed.openmm import RestartReporter, NetCDFReporter

# Simulation parameters
nsteps = 6000
dt = 2.0 * unit.femtoseconds
temperature = 310 * unit.kelvin
pressure = 1 * unit.atmosphere
cutoff = 8.0 * unit.angstroms

# Load AMBER topology and restart (only for AMBER systems)
amber_sys=load_file("prmtop.parm7", "restart.rst7")
ncrst=app.amberinpcrdfile.AmberInpcrdFile("restart.rst7")

# Create OpenMM system
system=amber_sys.createSystem(
            nonbondedMethod=app.PME,
            ewaldErrorTolerance=0.0005,
            nonbondedCutoff=cutoff,
            constraints=app.HBonds,
            removeCMMotion = True,
)

# Langevin integrator
integrator = LangevinMiddleIntegrator(temperature, 1.0/unit.picoseconds, dt)

# Monte Carlo barostat
barostat = MonteCarloBarostat(pressure, temperature, 50)
system.addForce(barostat)

# CUDA platform properties
platform = Platform.getPlatformByName("CUDA")

prop = dict(
    CudaPrecision="mixed",
    UseCpuPme='false',
    DeterministicForces="false",
    DeviceIndex=os.environ["CUDA_VISIBLE_DEVICES"],
   )

# Create simulation object
sim = app.Simulation(amber_sys.topology, system, integrator, platform, prop)
sim.context.setPositions(amber_sys.positions)
sim.context.setVelocities(ncrst.velocities)

# Reporters
sim.reporters.append(
        app.StateDataReporter(
            sys.stdout,
            1000,
            step=True,
            time=False,
            potentialEnergy=True,
            kineticEnergy=True,
            temperature=True,
            volume=True
        )
)

sim.reporters.append(NetCDFReporter("trajectory.nc", 50000, crds=True))
sim.reporters.append(RestartReporter("restart.nc", 50000, netcdf=True))

# Run dynamics
print("Running dynamics")
start = time.time()
sim.step(nsteps)
elapsed=time.time() - start
simulated_ns = (nsteps * dt).value_in_unit(unit.nanoseconds)
ns_per_day = simulated_ns / (elapsed / 86400)
print(f"Elapsed time: {elapsed} sec\nBenchmark time: {ns_per_day} ns/day ")
```

# Performance and benchmarking

A team at [ACENET](https://www.ace-net.ca/) has created a [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/) for Alliance clusters.
It can help you determine optimal conditions for AMBER, GROMACS, NAMD, and OpenMM jobs. The present section focuses on OpenMM performance.

OpenMM on the CUDA platform requires only one CPU per GPU because it does not use CPUs for calculations. While OpenMM can use several GPUs in one node, the most efficient way to run simulations is to use a single GPU. As you can see from [Narval benchmarks](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Narval&gpu_model=&cpu_model=&arch=&dataset=6n4o) and [Cedar benchmarks](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=V100-SXM2&cpu_model=&arch=&dataset=6n4o), on nodes with NvLink (where GPUs are connected directly), OpenMM runs slightly faster on multiple GPUs. Without NvLink there is a very little speedup of simulations on P100 GPUs ([Cedar benchmarks](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=P100-PCIE&cpu_model=&arch=&dataset=6n4o)).