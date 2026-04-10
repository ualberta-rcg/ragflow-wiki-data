---
title: "Biomolecular simulation/fr"
tags:
  - biomolecularsimulation

keywords:
  []
---

## Généralités 

La simulation biomoléculaire<ref name="ARB_2012">Ron O. Dror, Robert M. Dirks, J.P. Grossman, Huafeng Xu, and David E. Shaw. "Biomolecular Simulation: A Computational Microscope for Molecular Biology." *Annual Review of Biophysics*,  41:429-452, 2012. https://doi.org/10.1146/annurev-biophys-042910-155245</ref>  est l'application de la simulation en dynamique moléculaire à la recherche biochimique. Parmi les processus qui peuvent être modélisés, on trouve le repliement des protéines, les liaisons médicamenteuses, le transport membranaire et les modifications conformationnelles essentielles à la fonction protéinique.

La simulation biomoléculaire est considérée comme étant un sous-domaine de la chimie computationnelle; son champ d'action est cependant assez spécialisé pour que nous disposions d'une équipe d'experts dédiés. Consultez aussi la liste des ressources disponibles en [chimie computationnelle](computational-chemistry-fr.md).

## Logiciels 

Les paquets logiciels suivants sont disponibles via avec nos ressources.

* [AMBER](amber-fr.md)
* [GROMACS](gromacs-fr.md)
* [NAMD](namd-fr.md)
* [DL_POLY](http://www.scd.stfc.ac.uk/SCD/44516.aspx)
* [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
* [LAMMPS](lammps.md)
* [OpenKIM](https://openkim.org/) (*Knowledgebase of Interatomic Models*)
* [OpenMM](openmm-fr.md)
* [PLUMED](https://www.plumed.org), bibliothèque de code pour le développement relatif au calcul de l'énergie libre dans les simulations en dynamique moléculaire (voir aussi [GROMACS](gromacs-fr.md))
* [Rosetta](https://www.rosettacommons.org)
* [DSSP](https://swift.cmbi.umcn.nl/gv/dssp/)
* [VMD](vmd-fr.md)

### Wheels Python 

Calcul Canada offre des [wheels Python](available_python_wheels-fr.md) qui peuvent être installés dans des [environnements virtuels Python](python-fr#créer_et_utiliser_un_environnement_virtuel.md); ces wheels sont très utiles en simulation biomoléculaire et dynamique moléculaire.

La liste suivante contient une sélection des wheels les plus utiles, mais ne doit pas être considérée comme complète :

* [ACPYPE: AnteChamber PYthon Parser interfacE](acpype.md) outil servant à générer des topologies de composés chimiques.
* [MDAnalysis](https://www.mdanalysis.org/), bibliothèque Python orientée objet pour l'analyse de trajectoires dans les simulations de dynamique moléculaires dans plusieurs formats.
* [MDTraj](http://mdtraj.org/), qui peut aussi lire, écrire et analyser des trajectoires par quelques lignes de code Python, dans une grande variété de formats. 
* [Biopython](https://biopython.org/), ensemble d'outils gratuits pour les calculs biologiques.
* [foyer](https://foyer.mosdef.org/), paquet pour déterminer le type des atomes et appliquer et disséminer les champs de force.
* [mBuild](https://mbuild.mosdef.org/), langage hiérarchique pour construire des molécules basées sur des composantes.
* [mdsynthesis](https://mdsynthesis.readthedocs.io/), ensemble d’outils de manipulation et d'analyse des données de dynamique moléculaire.
* [nglview](http://nglviewer.org/), collection d'outils en ligne pour la visualisation en moléculaire. 
* [ParmEd](http://parmed.github.io/ParmEd/), outil général pour l'analyse des systèmes biomoléculaires avec des paquets de simulation populaires.
* [PyRETIS](pyretis.md), bibliothèque Python pour les simulations d'événements rares, avec une emphase sur l'échantillonnage d'interfaces de transition et d'interfaces de transition avec échange de réplication.

Voyez [liste des wheels disponibles](available_python_wheels-fr#wheels_disponibles.md) et la commande [commande <tt>avail_wheels</tt>](python-fr#wheels_disponibles.md) pour savoir ce qui est disponible.

Si vous avez besoin d'autres paquets Python ou des versions plus récentes, [contactez le soutien technique](technical_support-fr.md).

## Formation 

Des ateliers de formation sont donnés par notre équipe nationale pour la modélisation et la simulation moléculaires; les dates seront annoncées à l'avance.

Vous pouvez aussi prendre connaissance du matériel de formation par les liens suivants&nbsp;:

# [Practical considerations for Molecular Dynamics](https://computecanada.github.io/molmodsim-md-theory-lesson-novice/)
# [Visualizing Structures with VMD](https://computecanada.github.io/molmodsim-vmd-visualization/)
# [Running Molecular Dynamics with Amber on our clusters](https://computecanada.github.io/molmodsim-amber-md-lesson/)
# [Analyzing Molecular Dynamics Data with PYTRAJ](https://computecanada.github.io/molmodsim-pytraj-analysis/)

## Performance et étalonnage <i>benchmarking</i>

Le guide <i>[Molecular Dynamics Performance Guide](https://mdbench.ace-net.ca/mdbench/)</i> a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter aussi des tâches sur nos grappes avec AMBER, GROMACS, NAMD et OpenMM.

## Références 
[Biomolecular Simulation: A Computational Microscope for Molecular Biology](http://www.annualreviews.org/doi/10.1146/annurev-biophys-042910-155245)