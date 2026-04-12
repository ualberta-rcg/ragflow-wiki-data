---
title: "Quantum ESPRESSO/fr"
slug: "quantum_espresso"
lang: "fr"

source_wiki_title: "Quantum ESPRESSO/fr"
source_hash: "aa563e8489a3130581e8d575762329e1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T10:43:36.742627+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "théorie de la fonctionnelle de la densité"
  - "modélisation de matériaux"
  - "pseudopotentiels"
  - "Quantum ESPRESSO"
  - "calcul de structures électroniques"

questions:
  - "Qu'est-ce que la suite Quantum ESPRESSO et sur quels principes théoriques est-elle basée ?"
  - "Comment charge-t-on les modules nécessaires et soumet-on une tâche Quantum ESPRESSO via un script SLURM ?"
  - "Quels sont les problèmes connus concernant les fichiers de pseudopotentiels et les paramètres de Grimme-D3 ?"
  - "Qu'est-ce que la suite Quantum ESPRESSO et sur quels principes théoriques est-elle basée ?"
  - "Comment charge-t-on les modules nécessaires et soumet-on une tâche Quantum ESPRESSO via un script SLURM ?"
  - "Quels sont les problèmes connus concernant les fichiers de pseudopotentiels et les paramètres de Grimme-D3 ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Quantum ESPRESSO](http://www.quantum-espresso.org/) est une suite de codes *open source* pour le calcul de structures électroniques et la modélisation de matériaux à l'échelle atomique ou microscopique. Les codes sont basés sur la théorie de la fonctionnelle de la densité, les ondes planes et les pseudopotentiels.

Les codes indépendants et interopérables sont distribués sur le modèle *open source*. Un ensemble de routines ou de bibliothèques permettant d'effectuer des tâches plus avancées s'ajoute au noyau de composants d'origine, en plus de quelques paquets produits par d'autres contributeurs.

## Utilisation

Pour utiliser la suite Quantum ESPRESSO, vous devez charger un module (voir [Utiliser un module](utiliser-des-modules.md)).
Utilisez `module avail quantumespresso` ou `module spider quantumespresso` pour voir les versions disponibles.
Chargez le module avec, par exemple, `module load quantumespresso/6.6`.

```sh title="qe_ex1.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --time=0-1:00           # DD-HH:MM
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32     # MPI tasks
#SBATCH --mem=0                 # all memory on node
module load StdEnv/2020  intel/2020.1.217  openmpi/4.0.3
module load quantumespresso/6.6
srun pw.x < si.scf.in > si.scf.out
```

Dans cet exemple, on demande 32 processus, ce qui est plus que ce qui est nécessaire dans le cas du tutoriel avec le silicium.

!!! tip
    Rappelez-vous qu'il est compliqué de déterminer le nombre de processus à demander, mais que c'est vous qui devez choisir un nombre approprié. Voir aussi [Contrôle de l'ordonnancement avec MPI](advanced-mpi-scheduling.md).

## Problèmes connus

### Absence de fichiers de pseudopotentiels

!!! warning "Absence de fichiers de pseudopotentiels"
    Nos grappes n'ont aucun répertoire de pseudopotentiels pour Quantum ESPRESSO. Vous devez trouver ou créer vos propres fichiers et les enregistrer vous-même.

### Erreur de paramètre avec Grimme-D3

!!! warning "Erreur de paramètre avec Grimme-D3"
    Des résultats incorrects peuvent être obtenus quand vous utilisez Grimme-3 avec le baryum (Ba). Cette erreur est due à une valeur incorrecte pour l'un des coefficients du baryum, soit le paramètre `r2r4` dans le fichier du code source `dft-d3/core.f90`. En effet, la valeur est de 10.1567952 et non de 0.15679528. Cette erreur est confirmée dans les versions 6.2.1 à 7.1 de Quantum ESPRESSO. [« Wrong r2r4 value for Ba in the dft-d3 code », liste d'envoi de Quantum ESPRESSO, 9 juillet 2022](https://www.mail-archive.com/users@lists.quantum-espresso.org/msg42277.html).