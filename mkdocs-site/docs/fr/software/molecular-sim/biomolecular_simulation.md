---
title: "Biomolecular simulation/fr"
slug: "biomolecular_simulation"
lang: "fr"

source_wiki_title: "Biomolecular simulation/fr"
source_hash: "b473e0fc19e8f987e2ed545f23c5f2c5"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:49:55.714942+00:00"

tags:
  - biomolecularsimulation

keywords:
  - "dynamique moléculaire"
  - "PyRETIS"
  - "formation"
  - "wheels disponibles"
  - "échantillonnage d'interfaces de transition"
  - "simulation moléculaire"
  - "étalonnage"
  - "wheels Python"
  - "simulations d'événements rares"
  - "chimie computationnelle"
  - "simulation biomoléculaire"
  - "bibliothèque Python"
  - "logiciels"
  - "modélisation"

questions:
  - "Qu'est-ce que la simulation biomoléculaire et quels types de processus biochimiques permet-elle de modéliser ?"
  - "Quels sont les principaux logiciels de simulation biomoléculaire mis à disposition par ces ressources ?"
  - "Quelle est l'utilité des \"wheels Python\" offerts par Calcul Canada et quels outils spécifiques incluent-ils pour la dynamique moléculaire ?"
  - "Que doit faire un utilisateur s'il a besoin de paquets Python supplémentaires ou de versions plus récentes ?"
  - "Quelles ressources et opportunités de formation sont offertes pour apprendre la modélisation et la simulation moléculaires ?"
  - "Quel guide est recommandé pour connaître les conditions optimales d'exécution des tâches avec des logiciels tels que AMBER, GROMACS, NAMD et OpenMM ?"
  - "Qu'est-ce que la bibliothèque Python PyRETIS et quel est son objectif principal ?"
  - "Quelles sont les méthodes d'échantillonnage spécifiques sur lesquelles PyRETIS met l'accent ?"
  - "Quelle commande ou ressource permet de consulter la liste des \"wheels\" Python disponibles ?"
  - "Que doit faire un utilisateur s'il a besoin de paquets Python supplémentaires ou de versions plus récentes ?"
  - "Quelles ressources et opportunités de formation sont offertes pour apprendre la modélisation et la simulation moléculaires ?"
  - "Quel guide est recommandé pour connaître les conditions optimales d'exécution des tâches avec des logiciels tels que AMBER, GROMACS, NAMD et OpenMM ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Généralités

La simulation biomoléculaire est l'application de la simulation en dynamique moléculaire à la recherche biochimique. Parmi les processus qui peuvent être modélisés, on trouve le repliement des protéines, les liaisons médicamenteuses, le transport membranaire et les modifications conformationnelles essentielles à la fonction protéinique.

La simulation biomoléculaire est considérée comme un sous-domaine de la chimie computationnelle; son champ d'action est cependant assez spécialisé pour que nous disposions d'une équipe d'experts dédiés. Consultez aussi la liste des ressources disponibles en [chimie computationnelle](../chemistry/computational_chemistry.md).

## Logiciels

Les paquets logiciels suivants sont disponibles avec nos ressources.

*   [AMBER](../amber.md)
*   [GROMACS](../gromacs.md)
*   [NAMD](../namd.md)
*   [DL_POLY](http://www.scd.stfc.ac.uk/SCD/44516.aspx)
*   [HOOMD-blue](http://glotzerlab.engin.umich.edu/hoomd-blue/)
*   [LAMMPS](../lammps.md)
*   [OpenKIM](https://openkim.org/) (*Knowledgebase of Interatomic Models*)
*   [OpenMM](../openmm.md)
*   [PLUMED](https://www.plumed.org), bibliothèque de code pour le développement relatif au calcul de l'énergie libre dans les simulations en dynamique moléculaire (voir aussi [GROMACS](../gromacs.md))
*   [Rosetta](https://www.rosettacommons.org)
*   [DSSP](https://swift.cmbi.umcn.nl/gv/dssp/)
*   [VMD](../vmd.md)

### Wheels Python

Calcul Canada offre des [wheels Python](../../programming/available_python_wheels.md) qui peuvent être installés dans des [environnements virtuels Python](../python.md); ces wheels sont très utiles en simulation biomoléculaire et dynamique moléculaire.

La liste suivante contient une sélection des wheels les plus utiles, mais ne doit pas être considérée comme complète :

*   ACPYPE: AnteChamber PYthon Parser interfacE, outil servant à générer des topologies de composés chimiques.
*   [MDAnalysis](https://www.mdanalysis.org/), bibliothèque Python orientée objet pour l'analyse de trajectoires dans les simulations de dynamique moléculaires dans plusieurs formats.
*   [MDTraj](http://mdtraj.org/), qui peut aussi lire, écrire et analyser des trajectoires par quelques lignes de code Python, dans une grande variété de formats.
*   [Biopython](https://biopython.org/), ensemble d'outils gratuits pour les calculs biologiques.
*   [foyer](https://foyer.mosdef.org/), paquet pour déterminer le type des atomes et appliquer et disséminer les champs de force.
*   [mBuild](https://mbuild.mosdef.org/), langage hiérarchique pour construire des molécules basées sur des composantes.
*   [mdsynthesis](https://mdsynthesis.readthedocs.io/), ensemble d’outils de manipulation et d'analyse des données de dynamique moléculaire.
*   [nglview](http://nglviewer.org/), collection d'outils en ligne pour la visualisation en moléculaire.
*   [ParmEd](http://parmed.github.io/ParmEd/), outil général pour l'analyse des systèmes biomoléculaires avec des paquets de simulation populaires.
*   [PyRETIS](../pyretis.md), bibliothèque Python pour les simulations d'événements rares, avec une emphase sur l'échantillonnage d'interfaces de transition et d'interfaces de transition avec échange de réplication.

Voyez la [liste des wheels disponibles](../../programming/available_python_wheels.md) et la [commande `avail_wheels`](../python.md) pour savoir ce qui est disponible.

Si vous avez besoin d'autres paquets Python ou des versions plus récentes, [contactez le soutien technique](../../support/technical_support.md).

## Formation

Des ateliers de formation sont donnés par notre équipe nationale pour la modélisation et la simulation moléculaires; les dates seront annoncées à l'avance.

Vous pouvez aussi prendre connaissance du matériel de formation par les liens suivants :

1.  [Considérations pratiques pour la dynamique moléculaire](https://computecanada.github.io/molmodsim-md-theory-lesson-novice/)
2.  [Visualisation des structures avec VMD](https://computecanada.github.io/molmodsim-vmd-visualization/)
3.  [Exécution de la dynamique moléculaire avec Amber sur nos grappes](https://computecanada.github.io/molmodsim-amber-md-lesson/)
4.  [Analyse des données de dynamique moléculaire avec PYTRAJ](https://computecanada.github.io/molmodsim-pytraj-analysis/)

## Performance et étalonnage

Le guide [*Molecular Dynamics Performance Guide*](https://mdbench.ace-net.ca/mdbench/) a été créé par une équipe [d'ACENET](https://www.ace-net.ca/). Le guide décrit les conditions optimales pour exécuter des tâches sur nos grappes avec AMBER, GROMACS, NAMD et OpenMM.

## Références

[Biomolecular Simulation: A Computational Microscope for Molecular Biology](http://www.annualreviews.org/doi/10.1146/annurev-biophys-042910-155245)