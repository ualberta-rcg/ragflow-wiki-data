---
title: "Computational chemistry/fr"
slug: "computational_chemistry"
lang: "fr"

source_wiki_title: "Computational chemistry/fr"
source_hash: "44a1183d9681d25579b7633617836b56"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:43:45.839799+00:00"

tags:
  - computationalchemistry

keywords:
  - "systèmes moléculaires"
  - "VASP"
  - "modélisation moléculaire"
  - "Visualisation"
  - "Logiciels disponibles"
  - "chimie quantique"
  - "XTB"
  - "chimie computationnelle"
  - "Molden"
  - "Chimie computationnelle"
  - "Méthodes ab initio"
  - "visualisation tridimensionnelle"
  - "Fonctionnelle de la densité"
  - "Logiciels"
  - "Mécanique moléculaire"

questions:
  - "Qu'est-ce que la chimie computationnelle et quel est son objectif principal ?"
  - "Quelles sont les différences en termes de coût, de précision et d'application entre les méthodes ab initio, semi-empiriques, de la fonctionnelle de la densité et de mécanique moléculaire ?"
  - "Quels types de systèmes et de matériaux peuvent être étudiés à l'aide des logiciels et outils de visualisation listés dans le document ?"
  - "Quels sont les logiciels mentionnés dans le texte pour la visualisation et l'analyse tridimensionnelle des systèmes moléculaires ?"
  - "Quelles bibliothèques de développement sont proposées pour des domaines spécifiques comme la chimie quantique ou la théorie de la fonctionnelle de la densité ?"
  - "Quels outils polyvalents peuvent être utilisés pour la conversion de données moléculaires, l'exploration des pharmacophores ou l'apprentissage machine ?"
  - "Quels sont les exemples de logiciels de calcul ou de modélisation mentionnés dans le texte ?"
  - "Sur quelle page peut-on consulter la liste complète et à jour de toutes les versions des logiciels ?"
  - "Quel est le rôle principal de l'outil Molden et avec quels autres programmes est-il utilisé ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

La [chimie computationnelle](https://fr.wikipedia.org/wiki/Chimie_num%C3%A9rique) est une branche de la chimie qui utilise les lois de la chimie théorique exploitées dans des programmes informatiques afin de calculer les structures et les propriétés des molécules et des solides.

La plupart des logiciels spécialisés proposent plusieurs méthodes qui varient en termes d'application, de précision et de coûts.

*   Les méthodes [*ab initio*](https://fr.wikipedia.org/wiki/M%C3%A9thode_ab_initio_de_chimie_quantique) basées sur la chimie quantique sont largement applicables, mais utilisent un nombre limité de particules et s'avèrent très coûteuses en termes de temps de calcul.
*   Les méthodes [semi-empiriques](https://fr.wikipedia.org/wiki/M%C3%A9thode_quantique_semi-empirique) produisent des résultats plus précis, mais pour un plus petit nombre d'applications; elles sont généralement plus rapides que les méthodes *ab initio*.
*   Les méthodes de la [fonctionnelle de la densité](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_fonctionnelle_de_la_densit%C3%A9) peuvent être vues comme étant un compromis en termes de coûts. Le ratio coût-précision est très bon et les méthodes de la fonctionnelle de la densité sont aujourd'hui beaucoup plus utilisées.
*   Les méthodes de [mécanique moléculaire](https://fr.wikipedia.org/wiki/M%C3%A9canique_mol%C3%A9culaire) sont plus rapides, mais valent pour des champs d'applications limités. Elles sont basées sur un champ de force qui est optimisé en utilisant des données *ab initio* et/ou expérimentales pour reproduire les propriétés des matériaux.

!!! note "Simulation biomoléculaire"
    Les méthodes de mécanique moléculaire sont extrêmement utiles à l'étude des systèmes biologiques. Voyez [Simulation biomoléculaire](../molecular-sim/biomolecular_simulation.md) pour la liste des logiciels dans ce domaine; notez toutefois que la distinction est artificielle et que plusieurs outils s'emploient autant pour les systèmes biologiques que non biologiques.

Les différentes méthodes peuvent être utilisées pour la simulation des verres, métaux, liquides, liquides surfondus, matériaux granulaires, matériaux complexes, etc.

## Ressources disponibles

### Logiciels

*   [ABINIT](../abinit.md)
*   [ADF](../adf.md)/[AMS](../ams.md)
*   [AMBER](../amber.md)
*   [CP2K](../cp2k.md)
*   [CPMD](../cpmd.md)
*   [Dalton](dalton.md)
*   [deMon](http://www.demon-software.com/public_html/program.html)
*   [DL_POLY](../dl_poly.md)
*   [GAMESS-US](../gamess-us.md)
*   [Gaussian](../gaussian.md)
*   [GPAW](../gpaw.md)
*   [GROMACS](../gromacs.md)
*   [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
*   [LAMMPS](../lammps.md)
*   [MRCC](../mrcc.md)
*   [NAMD](../namd.md)
*   [NBO](https://nbo7.chem.wisc.edu/) est inclus dans plusieurs de nos modules [Gaussian](../gaussian.md#remarques).
*   [NWChem](http://www.nwchem-sw.org)
*   [OpenKIM](https://openkim.org/)
*   [OpenMM](https://simtk.org/home/openmm)
*   [ORCA](../orca.md)
*   [PLUMED](http://www.plumed-code.org)
*   [PSI4](http://www.psicode.org/)
*   [Quantum ESPRESSO](../quantum_espresso.md)
*   [Rosetta](https://www.rosettacommons.org)
*   [SIESTA](http://departments.icmab.es/leem/siesta)
*   [VASP](../vasp.md)
*   [XTB (Extended Tight Binding)](https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb)

!!! note "Logiciels disponibles"
    La liste à jour de toutes les versions se trouve à la page [Logiciels disponibles](../../programming/available_software.md).

### Visualisation

*   [Molden](https://www.theochem.ru.nl/molden/), un outil de visualisation utilisé avec GAMESS, Gaussian et autres.
*   [VMD](../visualization.md#vmd), logiciel libre pour visualiser, animer et analyser les grands systèmes moléculaires en mode tridimensionnel.
*   [VisIt](../visualization.md#visit), un outil d'analyse et de visualisation tridimensionnelle (la [galerie](https://wci.llnl.gov/simulation/computer-codes/visit/gallery) présente des exemples du domaine de la chimie).

!!! note "Visualisation"
    Pour plus d'information, voyez la page [Visualisation](../visualization.md).

### Autres outils

*   [CheMPS2](https://github.com/SebWouters/CheMPS2), une bibliothèque contenant une implémentation adaptée de la technique DMRG (*density matrix renormalization group*) pour la chimie quantique *ab initio*.
*   [Libxc](http://www.tddft.org/programs/octopus/wiki/index.php/Libxc), une bibliothèque pour le développement avec la théorie de la fonctionnelle de la densité.
*   [Open3DQSAR](http://open3dqsar.sourceforge.net/?Home), un outil pour l'exploration des pharmacophores par l'analyse chimiométrique des interactions entre molécules.
*   [Open Babel](../open_babel.md), un ensemble d'outils pour l'exploration, la conversion, l'analyse et le stockage de données avec la modélisation moléculaire, la chimie, les matériaux solides et la biochimie.
*   [PCMSolver](https://pcmsolver.readthedocs.org), une bibliothèque pour le développement avec les méthodes PCM (*polarizable continuum model*); certaines applications offrent explicitement cette fonctionnalité.
*   [RDKit](rdkit.md) est un ensemble d'applications pour la chimie computationnelle et l'apprentissage machine qui sont écrites en C++ et en Python.
*   [Spglib](https://github.com/atztogo/spglib), une bibliothèque pour le développement relatif à la symétrie des cristaux.