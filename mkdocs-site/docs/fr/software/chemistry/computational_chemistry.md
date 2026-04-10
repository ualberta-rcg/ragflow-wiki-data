---
title: "Computational chemistry/fr"
tags:
  - computationalchemistry

keywords:
  []
---

La [chimie computationnelle](https://fr.wikipedia.org/wiki/Chimie_num%C3%A9rique) est une branche de la chimie qui utilise les lois de la chimie théorique exploitées dans des programmes informatiques afin de calculer les structures et les propriétés des molécules et des solides. 

La plupart des logiciels spécialisés proposent plusieurs méthodes qui varient en termes d'application, de précision et de coûts. 
*Les méthodes [*ab initio*](https://fr.wikipedia.org/wiki/M%C3%A9thode_ab_initio_de_chimie_quantique) basées sur la chimie quantique sont largement applicables, mais utilisent un nombre limité de particules et s'avèrent très coûteuses en termes de temps de calcul.
*Les méthodes [semi-empiriques](https://fr.wikipedia.org/wiki/M%C3%A9thode_quantique_semi-empirique) produisent des résultats plus précis, mais pour un plus petit nombre d'applications; elles sont généralement plus rapides que les méthodes *ab initio*.
*Les méthodes de la [fonctionnelle de la densité](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_fonctionnelle_de_la_densit%C3%A9) peuvent être vues comme étant un compromis en termes de coûts. Le ratio coût-précision est très bon et les méthodes de la fonctionnelle de la densité sont aujourd'hui beaucoup plus utilisées.
*Les méthodes de [mécanique moléculaire](https://fr.wikipedia.org/wiki/M%C3%A9canique_mol%C3%A9culaire) sont plus rapides, mais valent pour des champs d'applications limités. Elles sont basées sur un champ de force qui est optimisé en utilisant des données *ab initio* et/ou expérimentales pour reproduire les propriétés des matériaux.

Les méthodes de mécanique moléculaire sont extrêmement utiles à l'étude des systèmes biologiques. Voyez [Simulation biomoléculaire](biomolecular-simulation-fr.md) pour la liste des logiciels dans ce domaine; notez toutefois que la distinction est artificielle et que plusieurs outils s'emploient autant pour les systèmes biologiques que non biologiques. Les différentes méthodes peuvent être utilisées pour la simulation des verres, métaux, liquides, liquides surfondus, matériaux granulaires, matériaux complexes, etc.

### Ressources disponibles 

#### Logiciels 

* [ABINIT](abinit-fr.md)
* [ADF](adf-fr.md)/[AMS](ams-fr.md) 
* [AMBER](amber-fr.md)
* [CP2K](cp2k-fr.md) 
* [CPMD](cpmd-fr.md)
* [Dalton](dalton-fr.md)
* [deMon](http://www.demon-software.com/public_html/program.html)
* [DL_POLY](dl_poly-fr.md)
* [GAMESS-US](gamess-us-fr.md)
* [Gaussian](gaussian-fr.md)
* [GPAW](gpaw-fr.md)   
* [GROMACS](gromacs-fr.md)
* [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
* [LAMMPS](lammps-fr.md)
* [MRCC](mrcc-fr.md)
* [NAMD](namd-fr.md)
* [NBO](https://nbo7.chem.wisc.edu/) est inclus dans plusieurs de nos modules [Gaussian](gaussian-fr#remarques.md).
* [NWChem](http://www.nwchem-sw.org)
* [OpenKIM](https://openkim.org/)
* [OpenMM](https://simtk.org/home/openmm)
* [ORCA](orca-fr.md)
* [PLUMED](http://www.plumed-code.org)
* [PSI4](http://www.psicode.org/)
* [Quantum ESPRESSO](quantum-espresso-fr.md)
* [Rosetta](https://www.rosettacommons.org)
* [SIESTA](http://departments.icmab.es/leem/siesta)
* [VASP](vasp-fr.md)
* [XTB (Extended Tight Binding)](https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb)

La liste à jour de toutes les versions offertes par Calcul Canada se trouve à la page [Logiciels disponibles](available-software-fr.md).

#### Visualisation
*[Molden](https://www.theochem.ru.nl/molden/), un outil de visualisation utilisé avec GAMESS, Gaussian et autres.
*[VMD](visualization-fr#vmd.md), logiciel libre pour visualiser, animer et analyser les grands systèmes moléculaires en mode tridimensionnel.
*[VisIt](visualization#visit.md), un outil d'analyse et de visualisation tridimensionnelle (la [galerie](https://wci.llnl.gov/simulation/computer-codes/visit/gallery) présente des exemples du domaine de la chimie).
Pour plus d'information, voyez la page [Visualisation](visualization-fr.md).

#### Autres outils 
* [CheMPS2](https://github.com/SebWouters/CheMPS2), une bibliothèque contenant une implémentation adaptée de la technique DMRG (*density matrix renormalization group*) pour la chimie quantique *ab initio*.
* [Libxc](http://www.tddft.org/programs/octopus/wiki/index.php/Libxc), une bibliothèque pour le développement avec la théorie de la fonctionnelle de la densité.
* [Open3DQSAR](http://open3dqsar.sourceforge.net/?Home), un outil pour l'exploration des pharmacophores par l'analyse chimiométrique des interactions entre molécules.
* [Open Babel](open-babel-fr.md), un ensemble d'outils pour l'exploration, la conversion, l'analyse et le stockage de données avec la modélisation moléculaire, la chimie, les matériaux solides et la biochimie.
* [PCMSolver](https://pcmsolver.readthedocs.org), une bibliothèque pour le développement avec les méthodes PCM (*polarizable continuum model*); certaines applications offrent explicitement cette fonctionnalité. 
* [RDKit](rdkit-fr.md) est un ensemble d'applications pour la chimie computationnelle et l'apprentissage machine qui sont écrites en C++ et en Python.
* [Spglib](https://github.com/atztogo/spglib), une bibliothèque pour le développement relatif à la symétrie des cristaux.