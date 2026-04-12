---
title: "Biomolecular simulation"
slug: "biomolecular_simulation"
lang: "base"

source_wiki_title: "Biomolecular simulation"
source_hash: "dff8db034e15ab8dec8b69e17d2890ac"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:49:09.188240+00:00"

tags:
  - biomolecularsimulation

keywords:
  - "Alliance clusters"
  - "Amber"
  - "ACENET"
  - "PYTRAJ"
  - "workshops"
  - "Biomolecular simulation"
  - "Python wheels"
  - "Molecular dynamics"
  - "Molecular Dynamics"
  - "Software packages"
  - "VMD"
  - "self-study"
  - "Performance and benchmarking"
  - "Computational chemistry"

questions:
  - "What is biomolecular simulation and what specific biochemical processes can be modeled using this technique?"
  - "What software packages and Python libraries are available on the HPC resources for molecular dynamics simulations and analysis?"
  - "Where can users find workshops and self-study training materials for learning about molecular dynamics and related software tools?"
  - "Which organization created the Molecular Dynamics Performance Guide for Alliance clusters?"
  - "What is the main purpose of using the Molecular Dynamics Performance Guide?"
  - "Which specific molecular dynamics software packages does the guide help optimize?"
  - "Where will announcements for future workshops be published?"
  - "How can individuals access the workshop materials if they want to study on their own?"
  - "What specific topics and software tools are covered in the provided self-study links?"
  - "Which organization created the Molecular Dynamics Performance Guide for Alliance clusters?"
  - "What is the main purpose of using the Molecular Dynamics Performance Guide?"
  - "Which specific molecular dynamics software packages does the guide help optimize?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## General

Biomolecular simulation[^1] is the application of molecular dynamics simulations to biochemical research questions. Processes that can be modelled include, but are not limited to, protein folding, drug binding, membrane transport, and the conformational changes critical to protein function.

While biomolecular simulation could be considered a sub-field of computational chemistry, it is sufficiently specialized that we have a Biomolecular Simulations National Team that supports this area. There is nevertheless some overlap of software tools between the two fields. See [Computational chemistry](computational-chemistry.md) for an annotated list of available software packages in that area.

## Software Packages

The following software packages are available on our HPC resources:

*   [AMBER](amber.md)
*   [GROMACS](gromacs.md)
*   [NAMD](namd.md)
*   [DL_POLY](http://www.scd.stfc.ac.uk/SCD/44516.aspx)
*   [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
*   [LAMMPS](lammps.md)
*   [OpenKIM](https://openkim.org/), the Knowledgebase of Interatomic Models
*   [OpenMM](openmm.md)
*   [PLUMED](https://www.plumed.org), a library for code development related to the calculation of free energy in molecular dynamics simulations. See also [GROMACS](gromacs.md).
*   [Rosetta](https://www.rosettacommons.org)
*   [DSSP](https://swift.cmbi.umcn.nl/gv/dssp/)
*   [VMD](vmd.md)

### Python Packages (Python Wheels)

Our [Wheelhouse](available-python-wheels.md) contains a number of Python Wheels that can be installed within a [virtual Python environment](python.md#creating-and-using-a-virtual-environment) and are useful in the domain of biomolecular simulation/molecular dynamics.

This list contains a selection of useful wheels, but is not to be considered complete:

*   [ACPYPE: AnteChamber PYthon Parser interfacE](acpype.md) is a tool to generate topologies for chemical compounds.
*   [MDAnalysis](https://www.mdanalysis.org/) is an object-oriented Python library to analyze trajectories from molecular dynamics (MD) simulations in many popular formats.
*   [MDTraj](http://mdtraj.org/) can also read, write and analyze MD trajectories with only a few lines of Python code with wide MD format support.
*   [Biopython](https://biopython.org/) is a set of freely available tools for biological computation.
*   [foyer](https://foyer.mosdef.org/) is a package for atom-typing as well as applying and disseminating force fields.
*   [mBuild](https://mbuild.mosdef.org/) is a hierarchical, component based molecule builder.
*   [mdsynthesis](https://mdsynthesis.readthedocs.io/) is a persistence engine for molecular dynamics data.
*   [nglview](http://nglviewer.org/): NGL Viewer is a collection of tools for web-based molecular graphics.
*   [ParmEd](http://parmed.github.io/ParmEd/) is a general tool for aiding in investigations of biomolecular systems using popular molecular simulation packages.
*   [PyRETIS](pyretis.md) is a Python library for rare event molecular simulations with emphasis on methods based on transition interface sampling and replica exchange transition interface sampling.

Please check the [list of available wheels](available-python-wheels.md) and use the [avail_wheels command](python.md#listing-available-wheels) on our clusters to see what is available.

If you require additional Python packages or newer versions, please [contact Support](technical-support.md).

## Workshops and Training Material

The *Molecular Modelling and Simulation National Team* is offering Molecular Dynamics workshops. Future workshops will be announced in our Newsletters.

The workshop material is also available for self-study:

1.  [Practical considerations for Molecular Dynamics](https://computecanada.github.io/molmodsim-md-theory-lesson-novice/)
2.  [Visualizing Structures with VMD](https://computecanada.github.io/molmodsim-vmd-visualization/)
3.  [Running Molecular Dynamics with Amber on our clusters](https://computecanada.github.io/molmodsim-amber-md-lesson/)
4.  [Analyzing Molecular Dynamics Data with PYTRAJ](https://computecanada.github.io/molmodsim-pytraj-analysis/)

## Performance and benchmarking

A team at [ACENET](https://www.ace-net.ca/) has created a [Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/) for Alliance clusters. It can help you determine optimal conditions for Amber, GROMACS, NAMD, and OpenMM jobs.

## References

[^1]: Ron O. Dror, Robert M. Dirks, J.P. Grossman, Huafeng Xu, and David E. Shaw. "Biomolecular Simulation: A Computational Microscope for Molecular Biology." *Annual Review of Biophysics*, 41:429-452, 2012. https://doi.org/10.1146/annurev-biophys-042910-155245