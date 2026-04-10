---
title: "ABINIT/fr"
slug: "abinit"
lang: "fr"

source_wiki_title: "ABINIT/fr"
source_hash: "2b24c01626fa5232440809dbce43d2d9"
last_synced: "2026-04-10T14:10:18.226633+00:00"
last_processed: "2026-04-10T14:18:29.272613+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "théorie de la fonctionnelle de la densité"
  - "ABINIT"
  - "script de tâche"
  - "propriétés des matériaux"
  - "données atomiques"

questions:
  - "Quelles sont les principales propriétés des matériaux que la suite logicielle ABINIT permet de calculer ?"
  - "Comment les utilisateurs peuvent-ils obtenir et télécharger les fichiers de données atomiques nécessaires à leurs calculs ?"
  - "Quelle est la procédure à suivre pour configurer et soumettre une tâche de calcul ABINIT à l'ordonnanceur Slurm ?"
  - "Quelles sont les principales propriétés des matériaux que la suite logicielle ABINIT permet de calculer ?"
  - "Comment les utilisateurs peuvent-ils obtenir et télécharger les fichiers de données atomiques nécessaires à leurs calculs ?"
  - "Quelle est la procédure à suivre pour configurer et soumettre une tâche de calcul ABINIT à l'ordonnanceur Slurm ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[ABINIT](https://www.abinit.org) est une suite logicielle pour le calcul des propriétés optiques, mécaniques, vibrationnelles et autres propriétés observables des matériaux. Avec les équations de la théorie de la fonctionnelle de la densité (DFT), il est possible d’évoluer vers des applications plus avancées avec les théories des perturbations basées sur la DGT et plusieurs fonctions N-corps de Green (GW et DMFT). ABINIT peut calculer les molécules, les nanostructures et les solides, peu importe leur composition chimique. La suite offre plusieurs tables complètes et fiables de potentiels atomiques.

Pour connaître les versions disponibles, utilisez la commande `module spider abinit`. Exécutez ensuite la même commande avec un numéro de version (par exemple `module spider abinit/8.4.4`) pour savoir si d’autres modules doivent être chargés au préalable. Pour plus d’information, consultez [Utiliser des modules](utiliser-des-modules.md).

## Données atomiques

Nous ne disposons pas de collection de données atomiques pour ABINIT. Pour obtenir les fichiers dont vous avez besoin, référez-vous aux [fichiers de données atomiques](https://www.abinit.org/downloads/atomic-data-files).

Puisque ces fichiers sont habituellement de moins de 1 Mo, ils peuvent être directement téléchargés vers un nœud de connexion avec leur URL et `wget`. L’exemple suivant sert à télécharger le fichier des pseudopotentiels de l’hydrogène.

```bash
wget http://www.pseudo-dojo.org/pseudos/nc-sr-04_pbe_standard/H.psp8.gz
```

## Exemples de scripts

Vous trouverez des fichiers de données pour effectuer des tests et pour suivre les [tutoriels ABINIT](https://docs.abinit.org/tutoriel/) à
`$EBROOTABINIT/share/abinit-test/Psps_for_tests/`
et
`$EBROOTABINIT/share/abinit-test/tutorial`.

## Exemple de script de tâche

Les calculs plus substantiels que les tests ou les exercices du tutoriel devraient être soumis à l’ordonnanceur [Slurm](running-jobs.md). Le script suivant est un exemple d’une tâche qui utilise 64 cœurs CPU sur deux nœuds pendant 48 heures, nécessitant 1024 Mo de mémoire par cœur. Cet exemple peut être adapté selon vos cas particuliers.

```sh title="abinit_job.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --nodes=2                # nombre de nœuds
#SBATCH --ntasks=64               # nombre de processus MPI
#SBATCH --mem-per-cpu=1024M      # utilisation de la mémoire par cœur de CPU; l'unité par défaut est le mégaoctet
#SBATCH --time=2-00:00           # durée (JJ-HH:MM)

module purge
module load abinit/8.2.2
srun abinit < parameters.txt >& output.log