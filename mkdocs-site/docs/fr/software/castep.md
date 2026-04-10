---
title: "CASTEP/fr"
slug: "castep"
lang: "fr"

source_wiki_title: "CASTEP/fr"
source_hash: "2353a5d9c34df13139bca78da3f9c873"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:03:46.347027+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Installation
Par exemple avec la version `20.11` :
1.  [**Trouvez le fichier archive qui contient l'installateur**](http://www.castep.org/get_castep); le fichier devrait se nommer `CASTEP-20.11.tar.gz`.
2.  Téléversez le fichier `CASTEP-20.11.tar.gz` dans votre répertoire `/home/$USER` sur la grappe que vous voulez utiliser.
3.  Sur la grappe, lancez la commande :
    ```bash
    eb CASTEP-20.11-iofbf-2020a.eb --sourcepath=$HOME --disable-enforce-checksums
    ```
Une fois que la commande est terminée, déconnectez-vous de la grappe et connectez-vous de nouveau.

## Utilisation
Vous devriez pouvoir charger le module avec :
```bash
module load castep
```
Sur un nœud de calcul, l'exécutable CASTEP peut être utilisé comme une [application MPI](running-jobs.md#taches-mpi) :
```bash
srun castep.mpi seedname
```
où les fichiers d'entrée seraient `seedname.cell` et `seedname.param` (un autre mot peut remplacer *seedname*).

## Référence
*   [Documentation de CASTEP](https://castep-docs.github.io/castep-docs/)