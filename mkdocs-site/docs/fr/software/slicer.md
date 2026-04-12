---
title: "Slicer/fr"
slug: "slicer"
lang: "fr"

source_wiki_title: "Slicer/fr"
source_hash: "294e655e241b977fb234b8cdd4fa7dff"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:31:27.704725+00:00"

tags:
  - software

keywords:
  - "ligne de commande"
  - "3D Slicer"
  - "traitement de l'image"
  - "imagerie médicale"
  - "nœud interactif"

questions:
  - "Qu'est-ce que le logiciel 3D Slicer et quelles sont ses principales applications ?"
  - "Quelle est la procédure recommandée pour lancer l'interface graphique de 3D Slicer sur un nœud interactif ?"
  - "Dans quels cas d'utilisation est-il préférable d'exécuter 3D Slicer en ligne de commande avec des tâches non interactives ?"
  - "Qu'est-ce que le logiciel 3D Slicer et quelles sont ses principales applications ?"
  - "Quelle est la procédure recommandée pour lancer l'interface graphique de 3D Slicer sur un nœud interactif ?"
  - "Dans quels cas d'utilisation est-il préférable d'exécuter 3D Slicer en ligne de commande avec des tâches non interactives ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[3D Slicer](https://www.slicer.org/) est une plateforme logicielle *open source* pour l'imagerie médicale numérique, le traitement de l'image et la visualisation 3D. Développée depuis une vingtaine d'années par l'ensemble de ses utilisateurs et avec le soutien des Instituts nationaux de la Santé des États-Unis, 3D Slicer met gratuitement des outils multiplateforme puissants au service des médecins, des chercheurs et du public.

!!! warning "Important"
    N'utilisez jamais de manière intensive les nœuds de calcul. Lorsque c'est possible, soumettez les tâches en ligne de commande, et si vous devez visualiser les données par l'interface graphique, utilisez un nœud interactif. Un rendu en parallèle sur un nœud de connexion partagé mettra fin à votre session.

## Interface graphique utilisateur

Assurez-vous que la redirection X11 est activée.

Pour vous connecter avec MobaXTerm, voyez [Connexion à un serveur avec MobaXTerm](../getting-started/connecting_with_mobaxterm.md).

### Nœuds interactifs

Comme le temps d'exécution sur les nœuds de connexion est limité, vous devriez demander une [tâche interactive](../running-jobs/running_jobs.md#tâches-interactives) pour disposer d'assez de temps pour explorer et visualiser vos données. Le traitement sera aussi plus rapide puisque vous pourrez utiliser plus de cœurs.

Demandez une tâche interactive, soit :

```bash
[name@server ~]$ salloc --time=1:0:0 --ntasks=2 --x11 --account=def-someuser
```

Ceci vous connectera à un nœud de calcul. Remarquez l'argument `--x11`.

Vous pouvez maintenant charger Slicer et l'exécuter sur le nœud interactif.

```bash
module load slicer
```

```bash
Slicer
```

Quand vous aurez quitté Slicer, n'oubliez pas de terminer la tâche interactive.

## Ligne de commande

Si vous devez exécuter la même tâche avec plusieurs images, ou si vous n'avez pas besoin de voir les images traitées à mesure qu'elles sont créées, vous devriez utiliser l'interface de ligne de commande et des tâches non interactives.

Consultez :
*   [https://discourse.slicer.org/t/rtstruct-to-label-map/2437](https://discourse.slicer.org/t/rtstruct-to-label-map/2437)
*   [https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863](https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863)