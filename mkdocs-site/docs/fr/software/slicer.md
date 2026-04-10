---
title: "Slicer/fr"
slug: "slicer"
lang: "fr"

source_wiki_title: "Slicer/fr"
source_hash: "294e655e241b977fb234b8cdd4fa7dff"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:21:07.697030+00:00"

tags:
  - software

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

3D Slicer est une plateforme logicielle *à code ouvert* pour l'imagerie médicale numérique, le traitement de l'image et la visualisation 3D. Développée depuis une vingtaine d'années par l'ensemble de ses utilisateurs et avec le soutien du National Institutes of Health des États-Unis, 3D Slicer met gratuitement des outils multiplateforme puissants au service des médecins, des chercheurs et du public.

!!! warning "Avertissement"
    N'utilisez jamais intensivement les nœuds de calcul. Lorsque possible, soumettez les tâches via la ligne de commande et si vous devez visualiser les données par l'interface graphique, utilisez un nœud interactif. Un rendu parallèle sur un nœud de connexion partagé entraînera la fin de votre session.

## Interface graphique utilisateur

Assurez-vous que la redirection X11 est activée.

Pour vous connecter avec MobaXTerm, consultez [Connexion à un serveur avec MobaXTerm](connecting-with-mobaxterm.md).

#### Nœuds interactifs

Puisque le temps d'exécution sur les nœuds de connexion est limité, vous devriez demander une [tâche interactive](running-jobs.md#taches-interactives) pour avoir suffisamment de temps pour explorer et visualiser vos données. Le traitement sera également plus rapide puisque vous pourrez utiliser plus de cœurs.

Pour demander une tâche interactive, utilisez la commande suivante :
```bash
[name@server ~]$ salloc --time=1:0:0 --ntasks=2 --x11 --account=def-someuser
```

Ceci vous connectera à un nœud de calcul. Notez l'argument `--x11`.

Vous pouvez maintenant charger Slicer et l'exécuter sur le nœud interactif.
```bash
module load slicer
```
```bash
Slicer
```

Lorsque vous aurez quitté Slicer, n'oubliez pas de terminer la tâche interactive.

## Ligne de commande

Si vous devez exécuter la même tâche avec plusieurs images, ou si vous n'avez pas besoin de voir les images traitées à mesure qu'elles sont créées, vous devriez utiliser l'interface en ligne de commande et des tâches non-interactives.

Veuillez consulter les ressources suivantes :

*   [https://discourse.slicer.org/t/rtstruct-to-label-map/2437](https://discourse.slicer.org/t/rtstruct-to-label-map/2437)
*   [https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863](https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863)