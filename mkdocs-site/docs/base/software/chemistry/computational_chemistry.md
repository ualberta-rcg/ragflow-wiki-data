---
title: "Computational chemistry"
slug: "computational_chemistry"
lang: "base"

source_wiki_title: "Computational chemistry"
source_hash: "cf6ad0d0cd7e118ad73e0e74a173d19e"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:29:50.338131+00:00"

tags:
  - computationalchemistry

keywords:
  - "cheminformatics"
  - "Open Babel"
  - "Ab initio"
  - "Density functional"
  - "RDKit"
  - "CheMPS2"
  - "Open3DQSAR"
  - "Libxc"
  - "density-functional models"
  - "quantum chemistry"
  - "Molecular dynamics"
  - "PCMSolver"
  - "Computational chemistry"
  - "Molecular mechanics"
  - "Spglib"

questions:
  - "What is computational chemistry and what is its primary purpose?"
  - "How do the main computational chemistry methods differ in terms of accuracy, computational cost, and applicability?"
  - "What categories of software tools are typically used to conduct and visualize computational chemistry simulations?"
  - "What are the primary functions and scientific fields supported by the Open Babel toolset?"
  - "Which programming languages are utilized in the RDKit collection for cheminformatics and machine learning?"
  - "What specific scientific models and structural properties are PCMSolver and Spglib designed to help developers analyze?"
  - "What is the primary function of the CheMPS2 library in the context of quantum chemistry?"
  - "In what type of computational models is the Libxc library typically utilized?"
  - "How does the Open3DQSAR tool facilitate pharmacophore exploration?"
  - "What are the primary functions and scientific fields supported by the Open Babel toolset?"
  - "Which programming languages are utilized in the RDKit collection for cheminformatics and machine learning?"
  - "What specific scientific models and structural properties are PCMSolver and Spglib designed to help developers analyze?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Computational chemistry](https://en.wikipedia.org/wiki/Computational_chemistry) is a branch of chemistry that incorporates the results of theoretical chemistry into computer programs to calculate the structures and properties of molecules and solids.

Most computer programs in the field offer a large number of methods, which can be broadly grouped in terms of the trade-off between accuracy, applicability, and cost.
*   [ab initio](https://en.wikipedia.org/wiki/Ab_initio_quantum_chemistry_methods) methods, based entirely on first principles, tend to be broadly applicable but very costly in terms of CPU time; they are therefore mostly applied to systems with a small number of particles.
*   [Semi-empirical](https://en.wikipedia.org/wiki/Semi-empirical_quantum_chemistry_method) methods give accurate results for a narrower range of cases, but are also typically much faster than *ab initio* methods.
*   [Density functional](https://en.wikipedia.org/wiki/Density_functional_theory) methods may be thought of as a compromise in cost between *ab initio* and semi-empirical methods. The cost-accuracy trade-off is very good and density functional methods have therefore become very widely used in recent years.
*   [Molecular mechanics](https://en.wikipedia.org/wiki/Molecular_mechanics) methods, based on classical mechanics instead of quantum mechanics, are faster but more narrowly applicable. They use a force field that can be optimized using *ab initio* and/or experimental data to reproduce the properties of the materials. Because of the low cost, molecular mechanics methods are frequently used for molecular dynamics calculations and can be applied to systems of thousands or even millions of particles.

!!! note
    Molecular dynamics calculations are extremely useful in the study of biological systems. Please see the [Biomolecular simulation](biomolecular-simulation.md) page for a list of the resources relevant to this area of research, but bear in mind that the distinction is artificial and many tools are applicable to both biological and non-biological systems. They can be used to simulate glasses, metals, liquids, supercooled liquids, granular materials, complex materials, etc.

### Notes on installed software

#### Applications

*   [ABINIT](abinit.md)
*   [ADF](adf.md)/[AMS](ams.md)
*   [AMBER](amber.md)
*   [CP2K](cp2k.md)
*   [CPMD](cpmd.md)
*   [Dalton](dalton.md)
*   [deMon](http://www.demon-software.com/public_html/program.html)
*   [DL_POLY](dl-poly.md)
*   [GAMESS-US](gamess-us.md)
*   [Gaussian](gaussian.md)
*   [GPAW](gpaw.md)
*   [GROMACS](gromacs.md)
*   [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
*   [LAMMPS](lammps.md)
*   [MRCC](mrcc.md)
*   [NAMD](namd.md)
*   [NBO](https://nbo7.chem.wisc.edu/) is included in several of our [Gaussian](gaussian.md#notes) modules.
*   [NWChem](http://www.nwchem-sw.org)
*   [OpenKIM](https://openkim.org/)
*   [OpenMM](https://simtk.org/home/openmm)
*   [ORCA](orca.md)
*   [PLUMED](http://www.plumed-code.org)
*   [PSI4](http://www.psicode.org/)
*   [Quantum ESPRESSO](quantum-espresso.md)
*   [Rosetta](https://www.rosettacommons.org)
*   [SIESTA](http://departments.icmab.es/leem/siesta)
*   [VASP](vasp.md)
*   [XTB (Extended Tight Binding)](https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb)

An automatically generated list of all the versions installed on Compute Canada systems can be found on [Available software](available-software.md).

#### Visualization tools

*   [Molden](https://www.theochem.ru.nl/molden/), a visualization tool for use in conjunction with GAMESS, Gaussian and other applications.
*   [VMD](visualization.md#vmd), an open-source molecular visualization program for displaying, animating, and analyzing large biomolecular systems in 3D.
*   [VisIt](visualization.md#visit), a general-purpose 3D visualization tool (a [gallery](https://wci.llnl.gov/simulation/computer-codes/visit/gallery) presents examples from chemistry).
See [Visualization](visualization.md) for more about producing visualizations on Compute Canada clusters.

#### Other tools

*   [CheMPS2](https://github.com/SebWouters/CheMPS2), a "library which contains a spin-adapted implementation of the density matrix renormalization group (DMRG) for *ab initio* quantum chemistry."
*   [Libxc](http://www.tddft.org/programs/octopus/wiki/index.php/Libxc), a library used in density-functional models.
*   [Open3DQSAR](http://open3dqsar.sourceforge.net/?Home), a "tool aimed at pharmacophore exploration by high-throughput chemometric analysis of molecular interaction fields."
*   [Open Babel](open-babel.md), a set of tools to enable one "to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas."
*   [PCMSolver](https://pcmsolver.readthedocs.org), a tool for code development related to the Polarizable Continuum Model. Some applications listed above offer built-in capabilities related to the PCM.
*   [RDKit](rdkit.md), a collection of cheminformatics and machine-learning software written in C++ and Python.
*   [Spglib](https://github.com/atztogo/spglib), a library for development relating to the symmetry of crystals.