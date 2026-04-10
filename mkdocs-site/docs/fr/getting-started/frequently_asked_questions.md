---
title: "Frequently Asked Questions/fr"
slug: "frequently_asked_questions"
lang: "fr"

source_wiki_title: "Frequently Asked Questions/fr"
source_hash: "4500fae51cbdd1029cbdcd6cc2da28ac"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:26:28.371786+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Mot de passe oublié
Pour réinitialiser votre mot de passe pour accéder aux grappes nationales de l'Alliance, cliquez sur https://ccdb.alliancecan.ca/security/forgot. Il vous est impossible de réinitialiser votre mot de passe tant que votre premier rôle n'est pas approuvé.

## Copier-coller
Dans un terminal Linux, vous ne pouvez pas utiliser [Ctrl]+C pour copier du texte parce [Ctrl]+C signifie Annuler (*Cancel*) ou Interrompre (*Interrupt*) et met fin au programme en cours d'exécution.

Sous Windows et Linux dans la plupart des cas, vous pouvez utiliser plutôt [Ctrl]+[Insert] pour copier et [Shift]+[Insert] pour coller, selon votre programme de terminal.
Sous macOS, utilisez [Cmd]+C et [Cmd]+V comme à l'habitude.

Selon le logiciel de terminal utilisé, sélectionnez simplement le texte pour l'entrer dans le presse-papiers et collez-le ensuite avec un clic de droite ou un clic du milieu (dépendant du paramétrage par défaut).

## Fichiers texte : caractère en fin de ligne
Les systèmes d'exploitation ont des conventions différentes pour signaler la fin de ligne dans un fichier texte brut ASCII. Sous Windows, chacune des lignes se termine par un caractère *retour de chariot* invisible, ce qui entraîne certains problèmes lorsque le fichier est lu dans un environnement Linux. Pour contrer ceci, vous pouvez
* créer et éditer les fichiers texte sur la grappe en utilisant un éditeur standard Linux comme emacs, vim ou nano;
* avec des fichiers texte Windows, lancer la commande `dos2unix <filename>` sur un nœud de connexion pour convertir les caractères de fin de ligne au format approprié.

## Lenteur de sauvegarde avec mon éditeur

### Emacs
Pour sauvegarder les fichiers, Emacs utilise l'appel système `fsync` pour diminuer le risque de perte de données en cas de panne du système. Cet ajout de fiabilité a cependant un inconvénient : plusieurs secondes sont quelquefois nécessaires pour sauvegarder un petit fichier dans un système de fichiers partagé (par exemple `home`, `scratch`, `project`) sur une de nos grappes. Si ce ralentissement nuit à votre travail, vous pouvez améliorer la performance en ajoutant la ligne suivante à votre fichier `~/.emacs` :

```emacs-lisp
(setq write-region-inhibit-fsync t)
```

Pour plus d'information, voir [Customize save in Emacs](https://www.gnu.org/savannah-checkouts/gnu/emacs/manual/html_node/emacs/Customize-Save.html)

## Message d'erreur "sbatch: error: Batch job submission failed: Socket timed out on send/recv operation"
Vous pourriez recevoir ce message d'erreur si l'ordonnanceur est surchargé (voir la page [Exécuter des tâches](running-jobs.md)). Nous tentons toujours d'augmenter la tolérance de Slurm à cet effet et d'éliminer les sources de surcharge ponctuelle, mais ceci est un projet de longue haleine. Notre recommandation est d'attendre environ une minute, puis d'utiliser `squeue -u $USER` pour voir si la tâche soumise paraît. Si la tâche n'est pas listée, soumettez-la de nouveau.

!!! note
    Notez que ce message survient dans certains cas même lorsque Slurm a accepté la tâche.

## Temps d'attente des tâches
Vous pouvez savoir pourquoi vos tâches ont le statut `PD` (*pending* pour en attente), en exécutant la commande `squeue -u <username>`.

La colonne `(REASON)` contient `Resources` ou `Priority`.
*   `Resources` : la grappe est très occupée; vous pouvez soit attendre, soit soumettre une tâche qui exige moins de ressources en termes de CPU/nœud, GPU, mémoire ou temps d’exécution.
*   `Priority` : la tâche est en attente en raison de sa basse priorité, ce qui survient lorsque vous et les autres membres du groupe avez utilisé plus que votre juste part des ressources récemment; vous pouvez faire le suivi de votre utilisation des ressources avec la commande `sshare` (voir [Politique d'ordonnancement des tâches](job-scheduling-policies.md)).

## Messages "Nodes required for job are DOWN, DRAINED or RESERVED for jobs in higher priority partitions" ou "ReqNodeNotAvailable"
Il est possible qu'un de ces messages s’affiche dans le champ `Reason` du fichier de résultat de `squeue` pour une tâche en attente; ceci se produit avec Slurm 19.05 et signifie qu'un ou plusieurs des nœuds que Slurm pouvait utiliser sont en panne, ont été mis hors service, ou encore sont réservés pour d’autres tâches. Ces cas sont fréquents avec les grappes de grande capacité qui connaissent un fort achalandage. Ces messages signifient effectivement la même chose que la raison `Ressources` de la version Slurm 17.11. Ce ne sont pas des messages d'erreur; les tâches sont dans la queue et seront éventuellement traitées.

## Précision de START_TIME avec squeue
Par défaut, la commande `squeue` ne montre pas le moment où une tâche doit être lancée, mais il est possible de le savoir avec une option. Comme les conditions sont constamment en changement, le moment prévu par Slurm pour le lancement d’une tâche n’est jamais exact et donc pas très utile.

L'ordonnanceur [Slurm](running-jobs.md) calcule un moment de début (`START_TIME`) dans le futur pour les tâches en attente qui sont de haute priorité sur la base
* des ressources qui seront libérées à la fin des tâches en cours, et
* des ressources qui seront demandées par les tâches en attente dont la priorité est plus élevée.

La valeur de `START_TIME` n'est plus valide si
* certaines tâches se terminent plus tôt que prévu et libèrent des ressources, ou
* l'ordre de priorité est modifié, par exemple quand des tâches sont annulées ou qu'une nouvelle tâche avec une priorité plus élevée est soumise.

Sur nos grappes d'usage général, de nouvelles tâches sont soumises toutes les cinq secondes environ et de 30 à 50 % des tâches se terminent plus tôt que prévu; Slurm revoit donc souvent l'ordre d'exécution des tâches qui lui sont soumises.

Pour la plupart des tâches en attente, la valeur de `START_TIME` est N/A (*non disponible*), ce qui signifie que Slurm n'essaie pas d'en fixer le moment du début.

Pour les tâches qui sont en cours, la valeur de `START_TIME` obtenue par `squeue` est précise.

## Fichiers .core
Dans certains cas, un fichier binaire avec l'extension `.core` est créé quand un programme se termine anormalement; il contient un instantané de l'état du programme au moment où il s'est terminé. Ce fichier est utile pour le débogage, mais n'est d'aucun intérêt pour les utilisateurs; il n'est qu'un signe d'un problème dans le déroulement du programme, ce qui est généralement indiqué dans le résultat en sortie de la tâche. Les fichiers `.core` peuvent être supprimés; ajoutez la ligne `ulimit -c 0` à la fin du fichier `$HOME/.bashrc` pour que ces fichiers ne soient plus créés.

## Bibliothèque introuvable
À l'exécution, les paquets binaires précompilés qui sont installés dans votre répertoire `$HOME` peuvent produire une erreur semblable à `/lib64/libc.so.6: version 'GLIBC_2.18' not found`. Pour la solution, voir [Installer des paquets binaires](installing-software-in-your-home-directory.md#installer-des-paquets-binaires).

## Quelles sont vos mesures pour la gestion des données sensibles?
Nos grappes ne sont pas spécifiquement conçues pour garantir la sécurité des données personnelles, privées ou sensibles.

Nous appliquons cependant les meilleures pratiques pour les systèmes partagés et accordons beaucoup d’attention à l’intégrité, la confidentialité et la disponibilité des données. Toutefois, certains ensembles de données doivent être traités avec des ressources qui sont certifiées selon des standards de sécurité particuliers et il est de la responsabilité des chercheuses et chercheurs de voir à ce que ces exigences soient respectées. À cet effet, veuillez prendre connaissance de [l'article 5.2 de notre Politique de protection des données et des renseignements personnels et du paragraphe 3.2 des Conditions d'utilisation](https://ccdb.computecanada.ca/agreements/user_index).

Pour plus d'information, voir [Protection des données, confidentialité et respect de la vie privée](data-protection-privacy-and-confidentiality.md).