---
title: "OpenMM/fr"
slug: "openmm"
lang: "fr"

source_wiki_title: "OpenMM/fr"
source_hash: "54a0c29d37dd6d96ae089504e84017e5"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:34:29.297457+00:00"

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

OpenMM (site web officiel : [openmm.org](https://openmm.org/)) est une boîte d'outils conçue pour la simulation moléculaire. On peut l'utiliser seule comme application pour effectuer des simulations ou comme bibliothèque que vous appelez à partir de votre code. OpenMM est un paquet unique de par sa très grande flexibilité des champs de force personnalisés et des algorithmes de résolution (ou d’intégration), son ouverture et son excellente performance, en particulier avec les GPU récents.

## Points forts

*   Interface Python flexible avec des classes de haut niveau et un accès API de bas niveau pour les flux de travail personnalisés.
*   Cadre d'extension (plugin framework) de haut niveau pour les potentiels basés sur l'apprentissage automatique et les simulations hybrides.
*   Exécution efficace sur les CPU et les GPU, adaptée aux plateformes de calcul de haute performance (CPH).
*   Prise en charge native des principaux formats biomoléculaires (AMBER, GROMACS, CHARMM).
*   Logiciel libre (open-source) avec un écosystème actif de plugins pour l'apprentissage automatique et les champs de force avancés.

## Points faibles

*   Plus lent que les moteurs MM classiques hautement optimisés (GROMACS, AMBER) pour les simulations de production à grande échelle.
*   La flexibilité peut ajouter de la complexité pour les simulations hybrides apprentissage automatique/mécanique moléculaire (ML/MM).
*   L'analyse de trajectoires spécialisées peut nécessiter des outils externes.

# Modules d'environnement

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0
```

!!! note
    Le module `ambertools` est facultatif et n'est requis que si vous comptez simuler des systèmes préparés avec AMBER.

Optionnellement, créez un environnement virtuel Python si vous désirez installer des paquets supplémentaires (par exemple, des potentiels d'apprentissage automatique).

# Préparation des fichiers d'entrée

OpenMM peut lire directement les fichiers de topologie et de coordonnées/redémarrage d'Amber si vous simulez des systèmes AMBER.

Assurez-vous que votre système est équilibré et minimisé avec Amber ou un autre logiciel avant de transférer les fichiers vers le CPH.

Pour les systèmes GROMACS ou CHARMM, OpenMM peut lire leurs formats respectifs sans AmberTools.

# Soumettre une tâche

Le script suivant est pour une tâche de simulation qui utilise un GPU.

```sh linenums="1"
#!/bin/bash
#SBATCH --cpus-per-task=1 
#SBATCH --gpus=h100:1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-01:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0

python openmm_input.py
```
Ici, `openmm_input.py` est un script Python qui charge des fichiers Amber, crée le système de simulation OpenMM, configure l'intégration et exécute les dynamiques (pour un exemple, voir [ici](https://mdbench.ace-net.ca/mdbench/idbenchmark/?q=129)).

```python linenums="1"
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

## Performance et étalonnage

Le guide [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec AMBER, GROMACS et NAMD.

Sur la plateforme CUDA, OpenMM n'a besoin que d'un CPU par GPU parce que les CPU ne sont pas utilisés pour les calculs. OpenMM peut utiliser plusieurs GPU dans un nœud, mais il est plus efficace de faire les simulations avec un seul GPU. Comme le démontrent les [essais sur Narval](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Narval&gpu_model=&cpu_model=&arch=&dataset=6n4o) et [ceux sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=V100-SXM2&cpu_model=&arch=&dataset=6n4o), la vitesse de simulation avec plusieurs GPU est légèrement augmentée sur les nœuds avec NvLink où les GPU sont directement connectés. Sans NvLink, la vitesse de simulation augmente très peu avec des GPU P100 ([essais sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=P100-PCIE&cpu_model=&arch=&dataset=6n4o)).