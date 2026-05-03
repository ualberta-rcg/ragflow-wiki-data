---
title: "OpenMM/fr"
slug: "openmm"
lang: "fr"

source_wiki_title: "OpenMM/fr"
source_hash: "9832157761155560acd3689e39b51d37"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:45:51.664566+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "DeviceIndex"
  - "AMBER"
  - "simulation moléculaire"
  - "Python"
  - "CudaPrecision"
  - "OpenMM"
  - "CUDA platform"
  - "Langevin integrator"
  - "Plateforme CUDA"
  - "Simulation"
  - "Performance et étalonnage"
  - "Monte Carlo barostat"
  - "GPU"

questions:
  - "Qu'est-ce qu'OpenMM et quels sont ses principaux avantages et inconvénients pour la simulation moléculaire ?"
  - "Comment doit-on préparer les fichiers d'entrée et charger les modules d'environnement nécessaires pour utiliser OpenMM ?"
  - "Comment configurer et soumettre un script de tâche pour exécuter une dynamique moléculaire avec OpenMM sur un GPU ?"
  - "Comment le script Python fourni configure-t-il les rapporteurs de données et calcule-t-il la vitesse de la simulation en nanosecondes par jour ?"
  - "Pourquoi est-il recommandé de n'allouer qu'un seul CPU par GPU lors de l'utilisation d'OpenMM sur la plateforme CUDA ?"
  - "Selon le guide de performance, comment la présence ou l'absence de la technologie NvLink influence-t-elle l'efficacité des simulations réparties sur plusieurs GPU ?"
  - "What type of integrator is initialized to govern the system's dynamics and temperature?"
  - "Which method is applied to the system to control and maintain its pressure?"
  - "What specific properties and configurations are defined for the CUDA platform to execute the simulation?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction

OpenMM ([Site Web OpenMM](https://openmm.org/)) est une boîte à outils conçue pour la simulation moléculaire. On peut l'utiliser seule comme application pour effectuer des simulations ou comme bibliothèque que vous appelez à partir de votre code. OpenMM est un paquet unique de par sa très grande flexibilité des champs de force personnalisés et des algorithmes de résolution (ou d’intégration), son ouverture et son excellente performance, en particulier avec les GPU récents.

## Points forts

*   Interface Python flexible avec des classes de haut niveau et un accès API de bas niveau pour des flux de travail personnalisés.
*   Cadre d'extension de haut niveau pour les potentiels basés sur l'apprentissage automatique et les simulations hybrides.
*   Exécution efficace sur les CPU et les GPU, adaptée aux plateformes de calcul haute performance (CHP).
*   Prise en charge native des principaux formats biomoléculaires (AMBER, GROMACS, CHARMM).
*   Logiciel libre avec un écosystème actif d'extensions pour l'apprentissage automatique et les champs de force avancés.

## Points faibles

*   Plus lent que les moteurs MM classiques hautement optimisés (GROMACS, AMBER) pour les simulations de production à grande échelle.
*   La flexibilité peut ajouter de la complexité pour les simulations hybrides AM/MM.
*   L'analyse de trajectoire spécialisée peut nécessiter des outils externes.

# Modules d'environnement

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0
```

!!! note "Remarque"
    Le module `ambertools` est facultatif et n'est requis que si vous prévoyez de simuler des systèmes préparés avec AMBER.

!!! tip "Conseil"
    Vous pouvez créer un environnement virtuel Python si vous souhaitez installer des paquets supplémentaires (par exemple, des potentiels d'apprentissage automatique).

# Préparation des fichiers d'entrée

OpenMM peut lire directement les fichiers de topologie et de coordonnées/redémarrage d'Amber si vous simulez des systèmes AMBER.

Assurez-vous que votre système est équilibré et minimisé dans Amber ou un autre logiciel avant de transférer les fichiers vers le système de calcul haute performance (CHP).

Pour les systèmes GROMACS ou CHARMM, OpenMM peut lire leurs formats respectifs sans AmberTools.

# Soumettre une tâche

Le script suivant est pour une tâche de simulation utilisant un GPU.

```bash linenums="1" title="submit_openmm.cuda.sh"
#!/bin/bash
#SBATCH --cpus-per-task=1 
#SBATCH --gpus=h100:1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=0-01:00:00

module purge
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0

python openmm_input.py
```

Ici, `openmm_input.py` est un script Python qui charge des fichiers Amber, crée le système de simulation OpenMM, configure l'intégration et exécute les dynamiques ([voir cet exemple](https://mdbench.ace-net.ca/mdbench/idbenchmark/?q=129)).

```python linenums="1" title="openmm_input.py"
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

Le guide [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter des tâches sur nos grappes avec AMBER, GROMACS et NAMD.

Sur la plateforme CUDA, OpenMM n'a besoin que d'un CPU par GPU parce que les CPU ne sont pas utilisés pour les calculs. OpenMM peut utiliser plusieurs GPU dans un nœud, mais il est plus efficace de faire les simulations avec un seul GPU. Comme le démontrent les [essais sur Narval](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Narval&gpu_model=&cpu_model=&arch=&dataset=6n4o) et les [essais sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=V100-SXM2&cpu_model=&arch=&dataset=6n4o), la vitesse de simulation avec plusieurs GPU est légèrement augmentée sur les nœuds avec NvLink où les GPU sont directement connectés. Sans NvLink, la vitesse de simulation augmente très peu avec des GPU P100 ([essais sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=P100-PCIE&cpu_model=&arch=&dataset=6n4o)).