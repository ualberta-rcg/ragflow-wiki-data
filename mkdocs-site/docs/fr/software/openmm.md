---
title: "OpenMM/fr"
slug: "openmm"
lang: "fr"

source_wiki_title: "OpenMM/fr"
source_hash: "59bd91a31d13c1dcfd112abcc411277c"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:48:37.773745+00:00"

tags:
  - software
  - biomolecularsimulation

keywords:
  - "vitesse de simulation"
  - "Simulation object"
  - "GPU"
  - "CUDA platform"
  - "Monte Carlo barostat"
  - "system"
  - "étalonnage"
  - "AMBER"
  - "simulation moléculaire"
  - "OpenMM"
  - "Python"
  - "plateforme CUDA"
  - "CudaPrecision"

questions:
  - "Quels sont les principaux avantages et inconvénients d'OpenMM par rapport aux moteurs de simulation classiques comme GROMACS ou AMBER ?"
  - "Quels formats de fichiers biomoléculaires OpenMM prend-il en charge et comment doit-on préparer le système avant de lancer la simulation ?"
  - "Comment doit-on configurer les scripts (SLURM et Python) pour soumettre et exécuter une tâche de simulation OpenMM accélérée par GPU ?"
  - "Comment le script configure-t-il les rapporteurs de données et évalue-t-il la vitesse de la simulation en nanosecondes par jour ?"
  - "Pourquoi l'utilisation d'OpenMM sur la plateforme CUDA ne requiert-elle qu'un seul processeur (CPU) par carte graphique (GPU) ?"
  - "De quelle manière la présence ou l'absence de la technologie NvLink influence-t-elle les performances d'une simulation exécutée sur plusieurs GPU ?"
  - "What parameters are used to initialize the Monte Carlo barostat in the provided code?"
  - "How are the CUDA platform properties configured for this simulation?"
  - "What arguments are passed to the constructor to create the final simulation object?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# Introduction
OpenMM [Site Web OpenMM](https://openmm.org/) est une boîte d'outils conçue pour la simulation moléculaire. On peut l'utiliser seule comme application pour effectuer des simulations ou comme bibliothèque que vous appelez à partir de votre code. OpenMM est un paquet unique de par sa très grande flexibilité des champs de force personnalisés et des algorithmes de résolution (ou d’intégration), son ouverture et son excellente performance, en particulier avec les GPU récents.

## Points forts
*   Interface Python flexible avec des classes de haut niveau et un accès API de bas niveau pour des flux de travail personnalisés.
*   Cadre de greffons (plugins) de haut niveau pour les potentiels basés sur l'apprentissage machine (ML) et les simulations hybrides.
*   Exécution efficace sur les unités centrales (UC) et les unités de traitement graphique (GPU), adaptée aux plateformes de calcul haute performance (CHP).
*   Prise en charge native des principaux formats biomoléculaires (AMBER, GROMACS, CHARMM).
*   Logiciel libre (open-source) avec un écosystème actif de greffons (plugins) pour l'apprentissage machine (ML) et les champs de force avancés.

## Points faibles
*   Plus lent que les moteurs MM classiques hautement optimisés (GROMACS, AMBER) pour les exécutions de production à grande échelle.
*   La flexibilité peut ajouter de la complexité pour les simulations hybrides ML/MM.
*   L'analyse de trajectoire spécialisée peut nécessiter des outils externes.

# Modules d'environnement

```bash
module load StdEnv/2023 gcc/12.3 openmpi/4.1.5 cuda/12.6 openmm/8.4.0 ambertools/25.0
```

!!! note
    Le module ambertools est facultatif, sauf si vous voulez simuler des systèmes préparés par AMBER.

Vous pouvez aussi créer un environnement virtuel Python si vous souhaitez installer des paquets supplémentaires (p. ex., des potentiels d'apprentissage machine (ML)).

# Préparation des fichiers d'entrée

OpenMM peut lire directement les fichiers de topologie et de coordonnées/redémarrage d'Amber si vous simulez des systèmes AMBER.

Assurez-vous que votre système est équilibré et minimisé avec Amber ou autre, avant de transférer des fichiers à une grappe de calcul.

OpenMM peut lire les formats de GROMACS ou CHARMM sans AmberTools.

# Soumission d'une tâche
Le script suivant est pour une tâche de simulation qui utilise un GPU.

``` file:submit_openmm.cuda.sh
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
Voici le script Python qui charge les paramètres Amber, relance les fichiers, construit le système de simulation OpenMM, configure l'intégrateur et exécute la dynamique.

``` python file:openmm_input.py
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

Le guide [*Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec AMBER, GROMACS et NAMD.

Sur la plateforme CUDA, OpenMM n'a besoin que d'un UC par GPU parce que les UC ne sont pas utilisées pour les calculs. OpenMM peut utiliser plusieurs GPU dans un nœud, mais il est plus efficace de faire les simulations avec un seul GPU. Comme le démontrent les [essais sur Narval](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Narval&gpu_model=&cpu_model=&arch=&dataset=6n4o) et [ceux sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=V100-SXM2&cpu_model=&arch=&dataset=6n4o), la vitesse de simulation avec plusieurs GPU est légèrement augmentée sur les nœuds avec NvLink où les GPU sont directement connectés. Sans NvLink, la vitesse de simulation augmente très peu avec des GPU P100 ([essais sur Cedar](https://mdbench.ace-net.ca/mdbench/bform/?software_contains=OPENMM.cuda&software_id=&module_contains=&module_version=&site_contains=Cedar&gpu_model=P100-PCIE&cpu_model=&arch=&dataset=6n4o)).