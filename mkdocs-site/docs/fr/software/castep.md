---
title: "CASTEP/fr"
tags:
  - software
  - computationalchemistry

keywords:
  []
---

## Installation
Par exemple avec la version `20.11`%nbsp;:
# ['''Trouvez le fichier archive qui contient l'installateur'''](http://www.castep.org/get_castep); le fichier devrait se nommer `CASTEP-20.11.tar.gz`.
# Téléversez le fichier `CASTEP-20.11.tar.gz` dans votre répertoire `/home/$USER` sur la grappe que vous voulez utiliser.
# Sur la grappe, lancez la commande
 [name@server ~]$ eb CASTEP-20.11-iofbf-2020a.eb --sourcepath=$HOME --disable-enforce-checksums
Une fois que la commande est terminée, déconnectez-vous de la grappe et connectez-vous de nouveau.

## Utilisation
Vous devriez pouvoir charger le module avec
 [name@server ~]$ module load castep
Sur un nœud de calcul, l'exécutable CASTEP peut être utilisé comme une [application MPI](running_jobs-fr#tâches_mpi.md)
 [name@server ~]$ srun castep.mpi seedname
où les fichiers d'entrée seraient `seedname.cell` et `seedname.param` (un autre mot peur remplacer *seedname*).

## Référence
* [Documentation de CASTEP](https://castep-docs.github.io/castep-docs/)