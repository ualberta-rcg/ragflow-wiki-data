---
title: "Slicer/fr"
tags:
  - software

keywords:
  []
---

[3D Slicer](https://www.slicer.org/) est une plateforme logicielle *open source* pour l'imagerie médicale numérique, le traitement de l'image et la visualisation 3D. Développée depuis une vingtaine d'années par l'ensemble de ses utilisateurs et avec le soutien du National Institutes of Health des États-Unis, 3D Slicer met gratuitement des outils multiplateforme puissants au service des médecins, des chercheurs et du public.

**IMPORTANT** : Ne faites jamais un usage intensif sur les nœuds de calcul. Lorsque possible, soumettez les tâches en ligne de commande et si vous devez visualiser les données par l'interface graphique, utilisez un nœud interactif. Un rendu en parallèle avec un nœud de connexion partagé mettra fin à votre session.

## Interface utilisateur graphique 
Assurez-vous que la redirection X11 est activée.

Pour vous connecter avec MobaXTerm, voyez [Connexion à un serveur avec MobaXTerm](connecting_with_mobaxterm-fr.md).

#### Nœuds interactifs 

Comme le temps d'exécution sur les nœuds de connexion est limité, vous devriez demander une [tâche interactive](running_jobs-fr#tâches_interactives.md) pour disposer d'assez de temps pour explorer et visualiser vos données. Le traitement sera aussi plus rapide puisque vous pourrez utiliser plus de cœurs.

Demandez une tâche interactive, soit
  [name@server ~]$ salloc --time=1:0:0 --ntasks=2 --x11 --account=def-someuser

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

Si vous devez exécuter la même tâche avec plusieurs images, 
ou si vous n'avez pas besoin de voir les images traitées à mesure qu'elles sont créées,
vous devriez utiliser l'interface de ligne de commande et des tâches non interactives.
Consultez
* https://discourse.slicer.org/t/rtstruct-to-label-map/2437
* https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863