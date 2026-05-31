---
title: "OpenMM/fr"
slug: "openmm"
lang: "fr"

source_wiki_title: "OpenMM/fr"
source_hash: "f2ee73621e69eeb9e7dfb8c223c5f43d"
last_synced: "2026-05-31T00:03:42.418098+00:00"
last_processed: "2026-05-31T00:51:14.811160+00:00"

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
  ragflow_synced: true
  qa_generated: false
---

# Introduction
OpenMM ([Page d'accueil d'OpenMM](https://openmm.org/)) est une boîte à outils de dynamique moléculaire *open source* conçue pour offrir flexibilité et programmabilité. Utilisée via Python, elle propose des classes applicatives pour l'exécution de simulations ainsi qu'une API de bas niveau permettant d'intégrer OpenMM directement dans le code pour des flux de travail personnalisés. OpenMM peut lire et simuler nativement des systèmes préparés avec AMBER, GROMACS et CHARMM, permettant ainsi une réutilisation en continu des configurations biomoléculaires existantes. Son architecture de plugiciels prend en charge l'intégration avec des outils d'apprentissage automatique, tels que TorchMD-Net, MACE, TorchANI, AIMNet2 et DeepMD, pour des simulations ML/MM à usage général ou hybrides.

## Points forts
* Interface Python flexible offrant à la fois des classes de haut niveau et un accès API de bas niveau pour des flux de travail personnalisés.
* Framework de plugiciels de haut niveau pour les potentiels pilotés par l'apprentissage automatique et les simulations hybrides.
* Exécution efficace avec CPU et GPU, adaptée aux plateformes de calcul haute performance.
* Prise en charge native des principaux formats biomoléculaires (AMBER, GROMACS, CHARMM).
* Logiciel libre avec un écosystème actif de plugiciels pour l'apprentissage automatique et les champs de force avancés.

## Points faibles
* Plus lent que les moteurs MM classiques hautement optimisés (GROMACS, AMBER) pour les simulations de grande envergure.
* La flexibilité peut ajouter de la complexité pour les simulations hybrides ML/MM.
* L'analyse de trajectoires spécialisée peut nécessiter des outils externes.

# Modules d'environnement

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0
```

!!! note
    Le module `ambertools` est optionnel, sauf si vous voulez simuler des systèmes préparés par AMBER.

Si vous voulez utiliser plus de paquets (par exemple MLPotential), vous pouvez aussi créer un environnement virtuel Python.

# Préparation des fichiers d'entrée

OpenMM peut lire directement les fichiers de topologie et de coordonnées/redémarrage Amber lors de la simulation de systèmes AMBER.

Assurez-vous que votre système est équilibré et minimisé avec Amber ou autre, avant de transférer des fichiers à une grappe de calcul.

OpenMM peut lire les formats de GROMACS ou CHARMM sans AmberTools.

# Soumettre une tâche
Le script suivant est pour une tâche de simulation qui utilise un GPU.

```sh title="submit_openmm.cuda.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1 
#SBATCH --gpus=h100:1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-01:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0

python openmm_input.py
```

# Script de simulation Python
Ici, le script Python qui charge les paramètres Amber, relance les fichiers, construit le système de simulation OpenMM, configure l'intégrateur et exécute les dynamiques.

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

## Performance et étalonnage *benchmarking*

Le guide [*Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter des tâches sur nos grappes avec AMBER, GROMACS et NAMD.

Sur la plateforme CUDA, OpenMM n'a besoin que d'un CPU par GPU parce que les CPU ne sont pas utilisés pour les calculs. OpenMM peut utiliser plusieurs GPU dans un nœud, mais il est plus efficace de faire les simulations avec un seul GPU. Comme le démontrent les [essais sur Narval](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Narval&gpu_model=&cpu_model=&arch=&dataset=6n4o) et [ceux sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=V100-SXM2&cpu_model=&arch=&dataset=6n4o), la vitesse de simulation avec plusieurs GPU est légèrement augmentée sur les nœuds avec NvLink où les GPU sont directement connectés. Sans NvLink, la vitesse de simulation augmente très peu avec des GPU P100 ([essais sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=P100-PCIE&cpu_model=&arch=&dataset=6n4o)).