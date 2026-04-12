---
title: "What is a scheduler?/fr"
slug: "what_is_a_scheduler"
lang: "fr"

source_wiki_title: "What is a scheduler?/fr"
source_hash: "aaa5ecf6de642081f66ed7496c8cba04"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:54:12.775514+00:00"

tags:
  []

keywords:
  - "tâche"
  - "Slurm"
  - "ressources"
  - "compte"
  - "spécifier les paramètres"
  - "temps ou mémoire"
  - "script de tâche"
  - "sbatch"
  - "file d'attente"
  - "ordonnanceur de tâches"
  - "fichier de sortie"

questions:
  - "Quelles sont les principales différences entre l'exécution d'un programme via une interface graphique et la soumission d'une tâche sur les serveurs de l'Alliance ?"
  - "Quel est le rôle de l'ordonnanceur de tâches (comme Slurm) et quelles sont ses principales fonctions dans la gestion des calculs ?"
  - "Pourquoi est-il crucial d'estimer et de spécifier avec précision les ressources (temps, mémoire, processeurs) demandées dans un script de tâche ?"
  - "Comment soumettre une tâche avec Slurm et que signifient les états \"PD\" et \"R\" lors du suivi de celle-ci ?"
  - "Quelles sont les options permettant de personnaliser le nom du fichier de résultat et de séparer les erreurs de la sortie standard ?"
  - "Pourquoi est-il obligatoire d'associer chaque tâche à un compte de projet et comment doit-on le spécifier ?"
  - "Pourquoi est-il crucial de définir avec précision les paramètres d'une tâche avant son exécution ?"
  - "Que se passe-t-il si les valeurs de temps ou de mémoire spécifiées sont inférieures aux exigences des calculs ?"
  - "Quelles sont les conséquences sur la file d'attente et le système si les paramètres alloués sont supérieurs aux besoins réels ?"
  - "Comment soumettre une tâche avec Slurm et que signifient les états \"PD\" et \"R\" lors du suivi de celle-ci ?"
  - "Quelles sont les options permettant de personnaliser le nom du fichier de résultat et de séparer les erreurs de la sortie standard ?"
  - "Pourquoi est-il obligatoire d'associer chaque tâche à un compte de projet et comment doit-on le spécifier ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Qu'est-ce qu'une tâche (*job*)?
Notre expérience avec les ordinateurs passe le plus souvent par les interfaces utilisateur (GUI pour *interface utilisateur graphique*). Par des fenêtres, des menus et des boutons, nous n'avons qu'à cliquer pour obtenir une réaction. L'environnement n'est pas le même avec les serveurs de l'Alliance. D'abord, il ne s'agit pas de cliquer, mais d'entrer les commandes via une console, ce qui s'appelle une interface en ligne de commande; pour une description de ce type d'interface, consultez la page [Introduction à Linux](linux-introduction.md). Une autre différence importante est que vos programmes ne s'exécutent pas toujours immédiatement, mais sont placés dans une file d'attente; les tâches sont exécutées quand les cœurs CPU sont disponibles pour éviter le risque d'interférence et la baisse de performance.

Utiliser cette interface comprend les étapes suivantes :
- vous préparez un script qui indique le programme à exécuter, la source des données et la destination du résultat;
- vous soumettez ce script à un logiciel ordonnanceur qui détermine le moment et l'endroit où il sera exécuté;
- vous pouvez récupérer le résultat lorsque la tâche est terminée.
Vous n'avez habituellement pas d'interaction avec le programme pendant que la tâche est en exécution, mais vous pouvez cependant vous informer de sa progression.

Voici un script des plus simples :

```bash title="simple_job.sh"
#!/bin/bash
#SBATCH --time=00:01:00
echo 'Hello, world!'
sleep 30
```
Il y a deux programmes (`echo` et `sleep`), aucune donnée en entrée, et le résultat en sortie ira à la destination par défaut. Les lignes commençant par `#SBATCH` sont des directives décrivant ce que l'ordonnanceur doit connaître de la tâche à exécuter. Dans notre exemple, le temps d'exécution n'est que de une minute (00:01:00).

## Ordonnanceur de tâches
L'ordonnanceur accomplit plusieurs fonctions :
- entretenir une base de données relative aux tâches;
- appliquer les règles quant aux limites et aux priorités;
- empêcher que les ressources soient surchargées, par exemple en assignant un cœur CPU à une tâche à la fois;
- déterminer quelles sont les tâches à exécuter et quels sont les nœuds de calcul à utiliser;
- lancer les tâches sur les nœuds appropriés;
- procéder à un nettoyage chaque fois qu'une tâche est complétée.

Pour nos grappes, nous avons adopté la solution d'ordonnancement [Slurm Workload Manager](https://en.wikipedia.org/wiki/Slurm_Workload_Manager) (la version anglaise de cette page est plus étoffée). Ici, les exemples et la syntaxe sont pour Slurm.

## Demander des ressources
Pour demander les ressources nécessaires à l'exécution d'un calcul, vous utilisez un script de tâche. Les paramètres d'une tâche sont le temps d'exécution et le nombre de processeurs. Dans l'exemple montré plus haut, le script demande une minute de temps d'exécution et puisqu'aucun nombre de processeurs n'est spécifié, un seul processeur sera alloué par défaut. Consultez les [exemples de scripts](running-jobs.md#exemples-de-scripts) pour d'autres types de requêtes avec processeurs multiples, quantité de mémoire et processeurs spéciaux comme les [GPUs](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) (la version anglaise de cette page est plus étoffée).

!!! warning "Important : Bien spécifier les ressources"
    Il est crucial de bien spécifier les paramètres des ressources. Si les valeurs sont inférieures à celles exigées par les calculs et que la tâche dépasse le temps ou la mémoire spécifiée, elle sera arrêtée. Inversement, si les valeurs sont supérieures aux besoins, la tâche pourrait rester en file d'attente plus longtemps que nécessaire et son exécution utiliserait des ressources qui ne seraient donc pas disponibles pour d'autres tâches.

## Tâche simple avec Slurm

Soumettons maintenant le script `simple_job.sh` avec la commande [sbatch](https://slurm.schedmd.com/sbatch.html) :

```bash
[someuser@host ~]$ sbatch simple_job.sh
Submitted batch job 1234
[someuser@host ~]$ sq
        JOBID     USER      ACCOUNT      NAME  ST  TIME_LEFT NODES CPUS    GRES MIN_MEM NODELIST (REASON)
    1234 someuser def-someprof  simple_j   R       0:33     1    1  (null)    256M blg9876 (None)
[someuser@host ~]$ cat slurm-1234.out
Hello, world!
```

Suite à la commande `sq`, la colonne ST (*état*) indique l'état de la tâche (voir la section *Suivi des tâches* dans [Exécuter des tâches](running-jobs.md)). Les états les plus communs sont PD (*en attente*) et R (*en cours*). Si la tâche est complétée, la colonne ST (*état*) est vide.

Remarquez que chaque tâche qui est soumise reçoit un identifiant unique; 1234 dans notre exemple. Si vous avez plusieurs tâches possédant le même nom, cet identifiant permet de les distinguer. Comme l'endroit où placer le résultat n'est pas spécifié, ce dernier est enregistré dans un fichier nommé avec l'identifiant de la tâche, ici `slurm-1234.out`.

La ligne de commande peut aussi définir les options pour `sbatch`. Par exemple, avec
```bash
[someuser@host ~]$ sbatch --time=00:30:00 simple_job.sh
```
la durée d'exécution devient 30 minutes. Toutes les options peuvent ainsi être modifiées.

## Enregistrer le résultat
Pour donner au fichier de sortie un nom plus significatif que `slurm-1234.out`, modifiez-le avec `--output`.
Le prochain script définit le nom de la tâche (*job name*) à paraître dans `squeue` et enregistre le résultat dans un fichier identifié par le *job name* comme préfixe ainsi que l'identifiant de la tâche.

```bash title="name_output.sh"
#!/bin/bash
#SBATCH --time=00:01:00
#SBATCH --job-name=test
#SBATCH --output=test-%J.out
echo 'Hello, world!'
```

Le même fichier comprendrait aussi les erreurs, tout comme si les commandes étaient données interactivement. Il est cependant possible de séparer le canal stderr (pour *erreur standard*) du canal stdout (pour *sortie standard*) en utilisant l'option `-e` pour spécifier les noms des fichiers.

## Comptes et projets
Les renseignements sur la tâche sont enregistrés pour que nous puissions faire un suivi de la qualité de nos services et faire rapport de la bonne utilisation des fonds aux organismes subventionnaires; ces renseignements relatifs aux tâches comprennent le temps en file d'attente, la durée d'exécution et le nombre de cœurs utilisés. Chaque tâche doit être associée à un nom de compte correspondant à un projet; voir la rubrique [RAP (projet d'allocation de ressources)](frequently-asked-questions-about-the-ccdb.md#rap-projet-dallocation-de-ressources).

```bash
#SBATCH --account=def-user-ab
```

Si vous soumettez une tâche avec `sbatch` sans spécifier de nom de compte alors que ceci est requis, vous devrez choisir parmi la liste de noms de comptes valides qui sera affichée.