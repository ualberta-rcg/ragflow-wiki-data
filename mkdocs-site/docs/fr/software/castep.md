---
title: "CASTEP/fr"
slug: "castep"
lang: "fr"

source_wiki_title: "CASTEP/fr"
source_hash: "2353a5d9c34df13139bca78da3f9c873"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:54:39.281702+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "Application MPI"
  - "Utilisation"
  - "CASTEP"
  - "Installation"
  - "Grappe"

questions:
  - "Quelles sont les étapes requises pour installer le logiciel CASTEP sur une grappe de calcul ?"
  - "Comment doit-on charger le module et exécuter CASTEP sur un nœud de calcul ?"
  - "Quels sont les formats de fichiers d'entrée nécessaires pour lancer une tâche avec l'exécutable CASTEP ?"
  - "Quelles sont les étapes requises pour installer le logiciel CASTEP sur une grappe de calcul ?"
  - "Comment doit-on charger le module et exécuter CASTEP sur un nœud de calcul ?"
  - "Quels sont les formats de fichiers d'entrée nécessaires pour lancer une tâche avec l'exécutable CASTEP ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Installation

Par exemple avec la version `20.11` :
1.  **Trouvez le fichier archive qui contient l'installateur** ; le fichier devrait se nommer `CASTEP-20.11.tar.gz`.
2.  Téléversez le fichier `CASTEP-20.11.tar.gz` dans votre répertoire `/home/$USER` sur la grappe que vous voulez utiliser.
3.  Sur la grappe, lancez la commande :

    ```bash
    [name@server ~]$ eb CASTEP-20.11-iofbf-2020a.eb --sourcepath=$HOME --disable-enforce-checksums
    ```

    Une fois que la commande est terminée, déconnectez-vous de la grappe et connectez-vous de nouveau.

## Utilisation

Vous devriez pouvoir charger le module avec :

```bash
[name@server ~]$ module load castep
```

Sur un nœud de calcul, l'exécutable CASTEP peut être utilisé comme une [application MPI](../running-jobs/running_jobs.md#taches-mpi) :

```bash
[name@server ~]$ srun castep.mpi seedname
```

où les fichiers d'entrée seraient `seedname.cell` et `seedname.param` (un autre mot peut remplacer *seedname*).

## Référence

*   [Documentation de CASTEP](https://castep-docs.github.io/castep-docs/)