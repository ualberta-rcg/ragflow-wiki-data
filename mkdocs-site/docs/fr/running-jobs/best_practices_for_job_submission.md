---
title: "Best practices for job submission/fr"
slug: "best_practices_for_job_submission"
lang: "fr"

source_wiki_title: "Best practices for job submission/fr"
source_hash: "1f036c83d57acd34d23d441b22d44834"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:47:59.570321+00:00"

tags:
  []

keywords:
  - "Parallélisme"
  - "Temps d'exécution"
  - "Ordonnanceur"
  - "effet négatif"
  - "trop de cœurs"
  - "outils de surveillance"
  - "Économiser les ressources"
  - "Environnement virtuel Python"
  - "Soumission de tâches"
  - "Points de contrôle"
  - "opérations d'écriture"
  - "opérations de lecture"
  - "commande seff"
  - "Efficacité du CPU"
  - "Consommation de la mémoire"
  - "même nœud"
  - "stockage local"
  - "nœuds de calcul"
  - "GPU"
  - "Scalabilité"
  - "cœurs CPU"
  - "tâche"
  - "optimisation"
  - "Durée estimée"
  - "Ressources"
  - "Mémoire"
  - "Script de tâche"
  - "temps en attente"
  - "ralentir le programme"
  - "MPI"
  - "TensorFlow"
  - "Cœurs CPU"
  - "durée réelle"
  - "Apptainer"

questions:
  - "Pourquoi est-il important de demander des valeurs appropriées pour les ressources lors de la soumission d'une tâche ?"
  - "Quelle méthode est recommandée pour estimer correctement le temps et la mémoire nécessaires pour une nouvelle analyse ?"
  - "Comment doit-on procéder si les calculs prévus s'effectuent en moins d'une heure afin de ne pas surcharger l'ordonnanceur ?"
  - "Pourquoi une tâche risque-t-elle de rester plus longtemps en attente si l'on ne spécifie pas une durée précise ?"
  - "Que doit-on utiliser pour connaître la durée réelle d'exécution d'une tâche terminée ?"
  - "Quelle commande et quel champ spécifique permettent d'obtenir le temps exact d'exécution d'une tâche ?"
  - "Pourquoi est-il fortement recommandé d'utiliser des points de contrôle pour les tâches dont la durée estimée dépasse 48 heures ?"
  - "Quel est le pourcentage idéal d'efficacité de la mémoire à viser et quelles sont les conséquences de demander un nœud à très grande capacité de mémoire ?"
  - "Pourquoi l'ajout de cœurs supplémentaires n'accélère-t-il pas nécessairement l'exécution d'un programme et comment déterminer si un logiciel supporte le parallélisme ?"
  - "Comment optimiser la répartition des processus parallèles sur les nœuds CPU pour maximiser l'efficacité des calculs ?"
  - "Comment évaluer si l'utilisation d'un nœud GPU est justifiée et performante pour une tâche spécifique par rapport à un nœud CPU ?"
  - "Quelles sont les recommandations en matière de gestion d'environnements et de scripts pour économiser les ressources des grappes ?"
  - "Quelle est la contrainte principale concernant le nombre de cœurs pouvant être alloués sur un même nœud ?"
  - "Pourquoi la stratégie consistant à demander systématiquement le maximum de cœurs n'est-elle pas toujours la meilleure approche ?"
  - "Comment l'analogie des cuisiniers illustre-t-elle l'impact négatif d'une surutilisation des cœurs CPU sur les performances d'un programme ?"
  - "Quelles opérations spécifiques doivent être optimisées selon le texte ?"
  - "Quelle méthode est recommandée pour améliorer les performances de ces opérations ?"
  - "Sur quel type de composant ou d'infrastructure le stockage local doit-il être utilisé ?"
  - "Quel outil est suggéré pour accompagner l'utilisation de TensorFlow ?"
  - "Quelle est la règle générale concernant la commande sleep dans un script de tâche ?"
  - "Quelles sont les alternatives recommandées pour remplacer Conda et ses variantes sur les grappes ?"
  - "Quelles opérations spécifiques doivent être optimisées selon le texte ?"
  - "Quelle méthode est recommandée pour améliorer les performances de ces opérations ?"
  - "Sur quel type de composant ou d'infrastructure le stockage local doit-il être utilisé ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Quand vous soumettez une tâche sur une de nos grappes, il est important de choisir les valeurs appropriées pour les différents paramètres pour éviter le gaspillage des ressources et ne pas causer de problèmes pour vous-même ou pour les autres utilisateurs et utilisatrices. Ce faisant, vous vous assurez aussi que votre tâche sera exécutée plus rapidement et qu’elle sera plus susceptible de se terminer avec succès et de produire les résultats auxquels vous vous attendez pour faire progresser votre recherche.

Pour les premières tâches d’une simulation ou d’une analyse, vous aurez sans doute de la difficulté à estimer le temps et la quantité de mémoire à demander. L’information contenue ici devrait vous être utile.

!!! warning "Problèmes courants"
*   Plus une tâche exige de ressources (temps d’exécution, mémoire, cœurs CPU, GPU), plus il est difficile pour l’ordonnanceur de rassembler ces ressources, ce qui fait que la tâche restera plus longtemps en file d'attente.
*   Par contre, si vous ne demandez pas assez de ressources pour exécuter la tâche, elle pourrait être arrêtée, car elle exigerait davantage que la limite que vous aurez demandée.
*   Une estimation des ressources requises qui se base sur la performance d’un ordinateur local risque d’être trompeuse, car le type de processeur et la vitesse d’exécution ne sont pas les mêmes que sur nos grappes.
*   Le script peut démarrer des tâches qui gaspillent les ressources.
    *   Le programme n’a pas une scalabilité suffisante pour le nombre de cœurs CPU demandés.
    *   Le programme n’est pas conçu pour une utilisation avec plusieurs nœuds.
    *   Les processeurs sont en attente lors des opérations de lecture-écriture.

!!! tip "Quelques astuces"
Nous vous suggérons de soumettre d’abord en test quelques tâches relativement brèves, par exemple une ou deux heures, avec une quantité de mémoire standard (`#SBATCH --mem-per-cpu=2G`).
*   Idéalement, vous devriez connaître à l’avance les résultats attendus, ce qui vous permettra de savoir si le logiciel fonctionne correctement.
*   Si la tâche est interrompue parce qu’elle excède la limite de temps demandée, doublez cette limite et répétez jusqu’à ce que le temps demandé permette l’exécution complète de la tâche.
*   Si la tâche est interrompue parce qu’elle excède la limite de mémoire demandée, vous obtiendrez un message d’erreur *OOM [out-of-memory] event*. Doublez alors la quantité de mémoire demandée et répétez jusqu’à ce que la limite permette l’exécution complète de la tâche.

En effectuant ces tests, vous vous familiariserez avec la durée et la mémoire requises pour certaines analyses, ce qui vous permettra de faire des estimations plus éclairées.

## Durée des tâches

*   La durée des tâches autres que les tests devrait être d’**au moins une heure**.
    *   Si vos calculs s’effectuent en moins d’une heure, nous vous suggérons d’utiliser des outils comme [GLOST](glost.md), [META](meta-farm.md) ou [GNU Parallel](gnu_parallel.md) pour grouper plusieurs calculs dans une même tâche d’une durée d’au moins une heure. L’ordonnanceur sera ainsi moins sollicité que par des centaines ou des milliers de très courtes tâches.
*   Il est aussi important que votre **estimation de la durée de la tâche soit relativement précise**.
    *   Si vous indiquez une durée de cinq jours quand les calculs prennent 16 heures, votre tâche sera beaucoup plus longtemps en attente que si vous demandez une durée plus précise.
*   **Utilisez des [outils de surveillance](running_jobs.md#taches-termines) pour connaître la durée réelle d’une tâche**
    *   avec par exemple la valeur du champ `Job Wall-clock time` dans le résultat de la commande `seff`.

```bash
seff 1234567
```

```text
Job ID: 1234567
Cluster: beluga
User/Group: jdoe/jdoe
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 16
CPU Utilized: 58-22:54:16
CPU Efficiency: 96.14% of 61-07:41:20 core-walltime
Job Wall-clock time: 3-19:58:50
Memory Utilized: 14.95 GB (estimated maximum)
Memory Efficiency: 11.68% of 128.00 GB (8.00 GB/core)
```

*   **Ajoutez une marge de 5 ou 10 % de temps à la durée estimée**.
    *   C’est normal de laisser une marge d’erreur dans vos estimations, mais vous gagnerez à indiquer la durée la plus précise possible.
*   Pour les tâches qui ont une durée de plus de 48 heures, envisagez l’utilisation de [points de contrôle](points-de-controle.md) si votre logiciel le permet.
    *   Un instantané de l’état du programme est sauvegardé sur disque à chaque point de contrôle. Si un problème survient, par exemple une panne ou une quelconque interruption, le programme peut être repris dans l’état où il se trouvait au dernier point de contrôle. Vous perdrez relativement peu de travail avec des points de contrôle aux 6 ou 8 heures.

## Consommation de la mémoire

*   La valeur de `Memory Efficiency` dans le résultat de la commande `seff` devrait être d’**au moins 80 à 85 %** dans la plupart des cas.
    *   S’assurer que la mémoire demandée est suffisante est aussi important que la durée que vous demandez. De même, une certaine marge d’erreur devrait aussi être ajoutée.
*   Si vous voulez utiliser un nœud entier, il est normal d’utiliser toute sa mémoire avec la ligne `#SBATCH --mem=0` dans le script.
    *   Cependant, la plupart de nos grappes ont des nœuds de mémoire variable et il est possible qu’un nœud avec moins de mémoire soit assigné à votre tâche.
*   Si vos tests indiquent que vous avez besoin d’un nœud de calcul à grande capacité de mémoire, vous devriez utiliser une ligne comme `#SBATCH --mem=1500G` pour obtenir 1500Go (ou 1.46To) de mémoire.
    *   Il y a peu de nœuds à grande capacité de mémoire, ce qui fait que votre tâche sera en attente plus longtemps avant d’être exécutée; vérifiez que toute la mémoire que vous demandez est vraiment nécessaire.

## Parallélisme

*   Par défaut, un seul cœur sur un nœud sera assigné à une tâche, ce qui est raisonnable étant donné que la plupart des logiciels fonctionnent séquentiellement et ne peuvent utiliser qu’un seul cœur.
    *   Demander plus de cœurs ou de nœuds n’augmentera pas la vitesse d’exécution d’un programme séquentiel. Pour être exécutable en parallèle, le code source d’un tel programme doit d’abord être modifié. Cette réécriture peut représenter un effort important et beaucoup de temps pour l’équipe de développement du programme.
*   Comment déterminer si le logiciel que vous utilisez peut fonctionner en parallèle?
    *   Le meilleur moyen de le savoir est de consulter sa documentation. Si vous ne trouvez pas de référence à l’exécution en parallèle, il est fort probable que le logiciel ne fonctionne que séquentiellement.
    *   Vous pouvez contacter l’équipe de développement du programme pour demander si vous pouvez l’exécuter en parallèle. Si ce n’est pas le cas, vous pouvez demander que cette fonctionnalité soit ajoutée.

*   Pour un programme qui fonctionne en parallèle, nous devons savoir combien de cœurs utiliser.
    *   Plusieurs techniques de programmation pour paralléliser un logiciel se basent sur l’emploi d’un *environnement de mémoire partagé*, c'est-à-dire que plusieurs cœurs peuvent être utilisés, mais ils doivent être sur le même nœud. Dans ce cas, vous ne pouvez utiliser plus de cœurs que le nœud n’en contient.
    *   Il est tentant de simplement demander le plus de cœurs possible, mais ce n’est pas toujours la bonne approche. Le chaos peut facilement s’installer quand plusieurs cuisiniers travaillent sur le même plat dans une petite cuisine et le même effet négatif peut se produire et ralentir le programme quand trop de cœurs CPU sont utilisés.
    *   Le fait de connaître la [scalabilité d’un logiciel](scalability.md) permet de choisir le nombre optimal de cœurs CPU.

*   Une autre difficulté survient avec l’utilisation de plusieurs nœuds; le logiciel utilisé doit supporter le *parallélisme avec mémoire distribuée*.
    *   La plupart des logiciels capables de fonctionner avec plus d’un nœud se basent sur le standard [MPI](../software/mpi.md); si la documentation du programme ne mentionne pas MPI ou qu’il est question de fils d’exécution et de parallélisme par fils, le programme est limité à un seul nœud.
    *   Les programmes qui ont été parallélisés pour travailler sur plusieurs nœuds devraient être lancés avec `srun` plutôt qu’avec `mpirun`.

*   Évitez d’éparpiller les processus parallèles sur plus de nœuds que nécessaire; une distribution plus compacte de ces processus favorise généralement une meilleure performance.
    *   Les tâches parallèles très fragmentées ont souvent une faible performance en plus de compliquer le travail de l’ordonnanceur. Vous devriez donc tenter de soumettre des tâches pour lesquelles le nombre de processus parallèles est un multiple intégral du nombre de cœurs par nœud, en supposant que le logiciel parallèle utilisé puisse fonctionner ainsi.
    *   Par exemple, avec une grappe de 40 cœurs par nœud, vous devriez toujours soumettre vos tâches en demandant un nombre de processus égal à 40, 80, 120, 160, 240, etc. Dans l’entête de script suivant, le total des 120 processus MPI est assigné de la manière la plus compacte possible, en utilisant trois nœuds entiers.

```bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=40
```

*   L’objectif ultime est de faire en sorte que l’efficacité du ou des CPU se rapproche le plus possible de 100 %; vérifiez le contenu du champ `CPU Efficiency` dans le résultat de la commande `seff`.
    *   Une efficacité de CPU sous 90 % est faible et signifie que le ou les logiciels utilisés par votre tâche doivent être améliorés.

## Travailler avec des GPU

Puisqu'il y a peu de nœuds GPU, les tâches qui requièrent leur utilisation attendent généralement longtemps.
*   Assurez-vous d’utiliser le plus efficacement possible le GPU pour lequel vous avez attendu si longtemps et assurez-vous qu’il augmente la performance de vos tâches.
    *   Plusieurs logiciels offrent une option GPU dont [NAMD](../software/namd.md) et [GROMACS](../software/gromacs.md), mais ce ne sont pas toutes les fonctions de ces logiciels qui sont capables de tirer parti des GPU. Il est donc sage de faire de courts tests avec et sans GPU et de vérifier l’effet sur la vitesse d’exécution.
    *   Comme le coût d’un nœud GPU est élevé, une tâche qui utilise un seul GPU devrait s’exécuter beaucoup plus rapidement qu’avec un nœud CPU entier. Si ce n’est pas le cas de votre tâche, utilisez plutôt un nœud CPU.
    *   Si votre tâche se termine seulement 5 à 10 % plus rapidement avec un nœud GPU, utilisez plutôt un nœud CPU. L’attente significativement plus élevée pour l’obtention d’un nœud GPU n’en vaut pas la peine.
*   Pour suivre l'efficacité des tâches avec GPU, utilisez des outils comme [nvidia-smi](https://developer.nvidia.com/nvidia-system-management-interface), `nvtop` ou encore l’utilitaire [TensorBoard](../software/tensorflow.md#tensorboard) si vous travaillez avec [TensorFlow](../software/tensorflow.md).

## Économiser les ressources

*   En règle générale, la commande `sleep` ne devrait pas se trouver dans un script de tâche.
*   Nous recommandons fortement d’éviter d’utiliser [Conda](../software/anaconda.md) et ses variantes sur nos grappes; utilisez plutôt des solutions comme un [environnement virtuel Python](../software/python.md#creer-et-utiliser-un-environnement-virtuel) ou [Apptainer](../software/containers/apptainer.md).

*   Les opérations de lecture et d’écriture devraient être optimisées par l’[utilisation du stockage local](../storage-and-data/using_node-local_storage.md) sur les nœuds de calcul.