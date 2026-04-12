---
title: "Job scheduling policies/fr"
slug: "job_scheduling_policies"
lang: "fr"

source_wiki_title: "Job scheduling policies/fr"
source_hash: "7bd884d2b43f9f0cbdeac9c33c39dcd1"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:13:17.717468+00:00"

tags:
  - slurm

keywords:
  - "Ordonnancement des tâches"
  - "Remplissage"
  - "partitions"
  - "priorisation selon la juste part"
  - "partition-stats"
  - "LevelFS"
  - "cœurs individuels"
  - "utilisation des ressources"
  - "utilisation"
  - "tâches en attente"
  - "exécuter des tâches"
  - "Slurm"
  - "cœurs"
  - "nœuds"
  - "ressources"
  - "partition"
  - "temps réel d'exécution"
  - "Durée maximale"
  - "ordonnancement"
  - "grappe"
  - "allocation de ressources"
  - "politique d'ordonnancement"
  - "nœuds entiers"
  - "statut du projet"
  - "EffectvUsage"
  - "compte inactif"
  - "GPU uniques"
  - "NormShares"
  - "Partitionnement des grappes"
  - "temps d'exécution"
  - "cible"
  - "RawShares"
  - "tâches"
  - "Nœuds entiers"
  - "priorité des tâches"
  - "cible d'utilisation"
  - "priorité"

questions:
  - "Comment la priorité des tâches est-elle déterminée par l'algorithme Fair Tree et la politique de juste part ?"
  - "Quelles sont les différences entre les types de comptes de projets (comme rrg-, rpp- et def-) en ce qui concerne l'allocation des ressources et la cible d'utilisation ?"
  - "Comment la commande sshare permet-elle d'analyser l'utilisation des ressources d'un groupe et d'anticiper la priorité de ses futures tâches ?"
  - "Quelles sont les valeurs de partage et d'utilisation des ressources de la grappe données en exemple pour ce projet ?"
  - "Pourquoi la valeur de « LevelFS » atteint-elle un niveau assez élevé pour ce groupe ?"
  - "Quelle est la conséquence de cette sous-utilisation des ressources allouées sur la priorité des prochaines tâches soumises ?"
  - "Comment la valeur de \"LevelFS\" influence-t-elle la priorité des nouvelles tâches soumises par un utilisateur ou un projet ?"
  - "Que représentent les colonnes \"RawShares\" et \"NormShares\" en termes d'allocation de ressources pour les projets et leurs membres ?"
  - "De quelle manière l'utilisation passée des ressources (RawUsage et EffectvUsage) est-elle calculée et pondérée dans le temps ?"
  - "Quelle est la valeur approximative attribuée à un compte considéré comme inactif ?"
  - "Comment la valeur de LevelFS se comporte-t-elle lorsqu'un projet utilise sa cible de manière régulière ?"
  - "De quelle manière le dépassement ou la sous-utilisation de la cible influence-t-il la valeur de LevelFS et la priorité des nouvelles tâches ?"
  - "Quelles sont les recommandations et les restrictions concernant l'allocation de nœuds entiers par rapport à l'utilisation de cœurs individuels ?"
  - "Comment la durée maximale d'une tâche influence-t-elle son ordonnancement et sa répartition dans les différentes partitions des grappes de calcul ?"
  - "Comment fonctionne le mécanisme de remplissage (backfilling) et comment les nœuds sont-ils catégorisés pour optimiser l'utilisation des ressources ?"
  - "Comment le temps réel d'exécution demandé influence-t-il l'accès aux ressources pour une tâche ?"
  - "Quelles sont les informations spécifiques affichées par l'utilitaire partition-stats concernant l'état des nœuds et des tâches ?"
  - "Comment doit-on interpréter la notation avec un deux-points (comme 12:170 ou 5:14) dans le tableau généré par l'utilitaire ?"
  - "Comment les tâches soumises sont-elles initialement réparties dans les différentes catégories ?"
  - "Quels types de tâches se voient réserver l'utilisation de nœuds entiers au sein d'une même catégorie ?"
  - "Quelle est la différence entre les partitions appelées « par nœud » et « par cœur » en matière d'allocation des ressources ?"
  - "Quelles sont les spécifications matérielles et temporelles exigées par le groupe principal de 170 tâches en attente ?"
  - "Combien de tâches nécessitent l'allocation d'un nœud entier équipé de GPU pour une durée maximale de 3 heures ?"
  - "Quelle est la ressource informatique spécifique demandée par le groupe de 14 tâches actuellement en attente ?"
  - "Comment les partitions de nœuds sont-elles organisées en fonction de leur durée d'exécution dans le système décrit ?"
  - "Quelles sont les limites de l'utilitaire partition-stats en termes d'informations fournies et de charge sur l'ordonnanceur ?"
  - "Quelle est la limite maximale de tâches qu'un compte normal peut avoir en exécution ou en attente simultanément sur les grappes comme Narval, Nibi et Rorqual ?"
  - "Comment les partitions de nœuds sont-elles organisées en fonction de leur durée d'exécution dans le système décrit ?"
  - "Quelles sont les limites de l'utilitaire partition-stats en termes d'informations fournies et de charge sur l'ordonnanceur ?"
  - "Quelle est la limite maximale de tâches qu'un compte normal peut avoir en exécution ou en attente simultanément sur les grappes comme Narval, Nibi et Rorqual ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Exécuter des tâches](running-jobs.md)*

Beaucoup de travail peut être accompli sur nos grappes en [soumettant des tâches](running-jobs.md) qui ne spécifient que le nombre de cœurs requis et la durée maximale d'exécution. Si par contre vous voulez soumettre plusieurs tâches ou des tâches qui nécessitent une grande quantité de ressources, vous gagnerez sans doute en productivité avec une bonne connaissance de notre politique d'ordonnancement.

## Priorisation selon la juste part

Les tâches sont traitées en ordre de **priorité** déterminée par l'algorithme [Fair Tree](https://slurm.schedmd.com/fair_tree.html). Voir [cette page](https://slurm.schedmd.com/fair_tree.html) et [ce document](https://slurm.schedmd.com/SC14/BYU_Fair_Tree.pdf).

Chaque tâche est facturée à un projet d'allocation de ressources. Le projet est défini par l'argument `--account` passé à `sbatch`.
*   Pour un projet auquel du temps CPU ou GPU a été alloué dans le cadre du [concours d'allocation de ressources](https://www.computecanada.ca/page-daccueil-du-portail-de-recherche/acces-aux-ressources/concours-dallocation-des-ressources/?lang=fr), le code du compte commence généralement par `rrg-` ou `rpp-`.
*   Pour un projet utilisant le service d'accès rapide, le nom du compte commence généralement par `def-`.

Pour savoir quel code utiliser, consultez la section *Comptes et projets* de la page [Exécuter des tâches](running-jobs.md).

À chaque projet est attribuée une cible d'utilisation (*target usage level*).
*   Les projets auxquels des ressources sont allouées via le concours ont une cible d'utilisation qui dépend de la quantité de CPU-années ou de GPU-années qui a été allouée.
*   Les projets qui n'ont pas de ressources allouées (c.-à-d. les comptes `def-`) ont tous la même cible d'utilisation; elle est ajustée à quelques minutes d'intervalle en fonction du nombre de projets qui sont actifs dans la grappe.

Comme exemple, déterminons les renseignements sur l'utilisation et le partage pour un groupe fictif ayant le code de compte `def-prof1`. Les noms d'utilisateurs pour les membres de ce groupe sont `prof1`, `grad2` et `postdoc3`. Nous pouvons voir l'information sur l'utilisation et le partage avec la commande `sshare` comme montré ci-dessous. Notez qu'il faut ajouter `_cpu` ou `_gpu` à la fin du code de compte puisque les deux sont comptabilisés individuellement.

!!! note "Sortie de `sshare`"
    La première ligne de la sortie ci-dessous, concernant l'ensemble du projet, était en rouge dans le document original pour mettre en évidence son importance pour l'ordonnancement.

```bash
prof1@gra-login4 ~]$ sshare -l -A def-prof1_cpu -u prof1,grad2,postdoc3
       Account       User  RawShares  NormShares  RawUsage  ... EffectvUsage  ...    LevelFS  ...
-------------- ---------- ---------- -----------  --------  ... ------------  ... ----------  ...
def-prof1_cpu                 434086    0.001607   1512054  ...     0.000043  ...  37.357207  ...
def-prof1_cpu      prof1          1    0.100000         0  ...     0.000000  ...        inf  ...   
def-prof1_cpu      grad2          1    0.100000     54618  ...     0.036122  ...   2.768390  ...
def-prof1_cpu   postdoc3          1    0.100000    855517  ...     0.565798  ...   0.176741  ...
```

Nous avons retiré de l'exemple plusieurs champs qui ne concernent pas notre propos.
La première ligne est la plus importante pour l'ordonnancement; elle décrit le statut du projet par rapport aux autres projets qui utilisent la grappe.
Dans notre exemple, la valeur pour le partage est 0.1607% et l'utilisation des ressources de la grappe se situe à 0.0043%. À 37, la valeur de *LevelFS* est assez élevée car le groupe n'a utilisé qu'une petite part des ressources qui lui sont allouées. On peut s'attendre à ce que les tâches soumises par ce groupe aient une priorité plutôt haute.

Les lignes du tableau montrent les valeurs pour chaque utilisateur par rapport aux autres utilisateurs **du même projet**. Sur la 3e ligne, on voit que `grad2` possède 1 part, ce qui représente 10% des ressources allouées au groupe; son utilisation compte pour seulement 3.6122% de l’utilisation récente par le groupe et la valeur de *LevelFS* pour cet utilisateur est la plus élevée. Les tâches soumises par `grad2` devraient donc avoir une priorité légèrement supérieure à celle pour `postdoc3`, mais moindre que celle pour `prof1`. Le niveau de priorité pour les tâches du groupe `def-prof1` par rapport à celle pour les autres groupes de recherche est uniquement déterminé par la valeur de *LevelFS* pour le groupe et non par celle des utilisateurs qui forment le groupe.

La documentation Slurm nomme *association* le projet par lui-même ou l'utilisateur dans un projet.
*   La colonne *Account* contient le nom du projet avec le suffixe `_cpu` ou `_gpu`.
*   Dans la colonne *User*, la première ligne n'a pas de nom d'utilisateur.
*   Le contenu de la colonne *RawShares* est proportionnel au nombre de CPU-années de la grappe alloué au projet dans le cadre du concours d'allocation de ressources. Les comptes qui n'ont pas de ressources allouées par concours ont un petit nombre égal de parts. Pour des raisons numériques, les comptes inactifs (ceux qui n'ont pas de tâche en cours ou en attente) reçoivent une seule part. L'activité fait l'objet d'un suivi périodique; si vous soumettez une tâche avec un compte inactif, il peut y avoir un délai allant jusqu'à 15 minutes avant que les valeurs de *RawShares* et *LevelFS* soient mises à jour.
*   Le contenu de la colonne *NormShares* montre le nombre de parts assignées à l'utilisateur ou au compte, divisé par le nombre total des parts assignées pour ce niveau. Sur la première ligne, la valeur 0.001607 est la fraction des parts détenues par le projet par rapport à tous les projets. Sur les autres lignes, la valeur 0.10000 est la fraction des parts détenue par chacun des membres du projet, par rapport aux autres membres; il y a dix membres, mais nous avons seulement demandé l'information pour trois d'entre eux.
*   Le contenu de la colonne *RawUsage* représente une pondération du nombre total de secondes-ressources (c'est-à-dire temps CPU, temps GPU et mémoire) facturées au compte. L'usage passé est diminué d'une [demi-vie](https://fr.wikipedia.org/wiki/Demi-vie) d'une semaine; l'utilisation datant de plus de quelques semaines n'aura donc qu'un effet minime sur la priorisation.
*   La colonne *EffectvUsage* montre l'utilisation de l'association par rapport à son parent, soit l'utilisation du projet par rapport aux autres projets et l'utilisation de chacun des utilisateurs par rapport à l'ensemble des utilisateurs. Dans cet exemple, l'utilisation de `postdoc3` est de 56.6% et celle de `grad2` est de 3.6%.
*   La colonne *LevelFS* montre la valeur de la juste part (FS pour *fair share*) exprimée par *NormShares / EffectvUsage*. Un résultat entre 0 et 1 signale une association qui reçoit de l'ordonnanceur plus de ressources que mérité; un résultat plus grand que 1 signale une association qui reçoit de l'ordonnanceur moins de ressources que mérité. Pour un compte inactif (comme décrit sous *RawShares*), la valeur est un nombre infime près de 0.0001.

Un projet pour lequel la cible est utilisée de façon régulière verra sa valeur pour *LevelFS* proche de 1.0. Si la cible est dépassée, *LevelFS* sera sous 1.0. et les nouvelles tâches pour le projet recevront aussi une basse priorité. Si l'utilisation est inférieure à la cible, *LevelFS* sera plus grand que 1.0 et les nouvelles tâches bénéficieront d'une priorité élevée.

**Voir aussi** [Allocation et ordonnancement des tâches de calcul](allocations-and-compute-scheduling.md).

## Nœuds entiers ou cœurs

Les applications pouvant utiliser de façon efficace plus de cœurs qu'on trouve dans un nœud simple pourraient être mieux servies avec des nœuds entiers. Certaines grappes réservent des nœuds pour les tâches nécessitant plus qu'un nœud complet. Pour plus d'information et des exemples de scripts, voyez la section [Nœuds entiers](advanced-mpi-scheduling.md#nœuds-entiers) de la page [Contrôle de l'ordonnancement avec MPI](advanced-mpi-scheduling.md).

Prenez note que le fait de demander un nombre inefficace de processeurs dans le simple but de profiter de tout avantage conféré par l'ordonnancement pour un nœud entier sera interprété comme étant un abus injustifié des ressources. Par exemple, pour un programme ayant un temps d'exécution semblable sur 192 cœurs et 64 cœurs, la requête devrait être de 64 cœurs et non de 192 cœurs.

Si vous avez une grande quantité de tâches en série et que vous pouvez bien utiliser [META-Farm](meta-farm.md), [GNU Parallel](gnu-parallel.md), [GLOST](glost.md) ou [d'autres techniques](https://docs.scinet.utoronto.ca/index.php/Running_Serial_Jobs_on_Niagara) pour rassembler ces tâches pour un seul nœud, nous vous invitons à le faire.

## Durée maximale

[Trillium](trillium.md) peut accommoder des tâches avec des temps d'exécution pouvant aller jusqu'à 24 heures. La durée maximale avec [Fir](fir.md), [Narval](narval.md), [Nibi](nibi.md) et [Rorqual](rorqual.md) est de 7 jours. Ces durées sont à la discrétion des administrateurs de systèmes et elles sont sujettes à changement.

Avec les grappes d'usage général, les tâches de longue durée ne peuvent utiliser qu'une portion de la grappe par partitionnement. Il y a des partitions pour des tâches ayant des temps d'exécution de
*   3 heures ou moins,
*   12 heures ou moins,
*   24 heures ou moins,
*   72 heures ou moins,
*   7 jours ou moins

Un temps d'exécution de 3 heures étant plus court que 12 heures ou plus, les tâches aux durées plus courtes peuvent toujours être exécutées dans les partitions ayant les durées maximales plus grandes. Une tâche plus courte sera donc susceptible d'être ordonnancée plus rapidement qu'une tâche plus longue dont les autres caractéristiques sont identiques.

## Remplissage (*backfilling*)

L'ordonnanceur optimise l'utilisation des ressources avec le [backfilling](https://slurm.schedmd.com/sched_config.html).

Sans remplissage, chaque partition est ordonnancée strictement par priorité, ce qui minimise généralement l'utilisation et le temps de réponse des ressources. Le remplissage fait en sorte que les tâches de basse priorité sont lancées pourvu que les tâches de plus haute priorité ne soient pas retardées. Puisque le moment prévu pour le lancement des tâches en attente dépend de la complétion des tâches courantes, le bon fonctionnement de la technique de remplissage nécessite des durées d'exécution maximales raisonnablement exactes.

Le remplissage avantage les tâches dont la durée maximale est plus courte, soit moins de 3 heures.

## Pourcentages des nœuds disponibles

Nous présentons ici une description du partitionnement des grappes d'usage général (Fir, Narval, Nibi et Rorqual).

D'abord, il y a quatre catégories de nœuds :
*   les nœuds de type *base* (4 à 8Go de mémoire par cœur)
*   les nœuds de type *large* (16 à 96Go de mémoire par cœur)
*   les nœuds de type *GPU base*

Les tâches soumises sont dirigées vers la catégorie appropriée selon les ressources requises.

Ensuite, parmi les nœuds d'une même catégorie, certains sont réservés aux tâches qui peuvent utiliser des nœuds entiers, soit celles qui font usage de toutes les ressources disponibles sur les nœuds alloués. Si une tâche utilise peu de cœurs ou même un seul cœur sur un même nœud, seul un sous-ensemble des nœuds lui sera alloué. On appelle ces partitions "par nœud" (*by-node*) et "par cœur" (*by-core*).

Enfin, le temps réel d'exécution joue aussi un rôle. Les tâches plus courtes ont accès à plus de ressources. Par exemple, une tâche requérant un temps réel d'exécution de moins de 3 heures peut se retrouver sur n'importe lequel nœud qui permet des temps réels de 12 heures, mais certains nœuds qui acceptent des tâches de 3 heures **n'accepteront pas** des tâches de 12 heures.

L'utilitaire `partition-stats` montre
*   dans chaque partition, combien de tâches sont en attente dans une queue d'exécution,
*   combien de tâches sont en cours d'exécution,
*   combien de nœuds sont inactifs,
*   combien de nœuds sont assignés à chacune des partitions.

Voici un exemple :

```bash
user@login1 ~]$ partition-stats

Node type |                     Max walltime
          |     3 hr   |   12 hr   |   24 hr   |   72 hr   |   168 hr  |
----------|-------------------------------------------------------------
       Number of Queued Jobs by partition Type (by node:by core)
----------|-------------------------------------------------------------
Regular   |    12:170  |   69:7066 |   70:7335 |  386:961  |   59:509  |
Large Mem |     0:0    |    0:0    |    0:0    |    0:15   |    0:1    |
GPU       |     5:14   |    3:8    |   21:1    |  177:110  |    1:5    |
----------|-------------------------------------------------------------
      Number of Running Jobs by partition Type (by node:by core)
----------|-------------------------------------------------------------
Regular   |     8:32   |   10:854  |   84:10   |   15:65   |    0:674  |
Large Mem |     0:0    |    0:0    |    0:0    |    0:1    |    0:0    |
GPU       |     5:0    |    2:13   |   47:20   |   19:18   |    0:3    |
----------|-------------------------------------------------------------
        Number of Idle nodes by partition Type (by node:by core)
----------|-------------------------------------------------------------
Regular   |    16:9    |   15:8    |   15:8    |    7:0    |    2:0    |
Large Mem |     3:1    |    3:1    |    0:0    |    0:0    |    0:0    |
GPU       |     0:0    |    0:0    |    0:0    |    0:0    |    0:0    |
----------|-------------------------------------------------------------
       Total Number of nodes by partition Type (by node:by core)
----------|-------------------------------------------------------------
Regular   |   871:431  |  851:411  |  821:391  |  636:276  |  281:164  |
Large Mem |    27:12   |   27:12   |   24:11   |   20:3    |    4:3    |
GPU       |   156:78   |  156:78   |  144:72   |  104:52   |   13:12   |
----------|-------------------------------------------------------------
```

Dans le haut du tableau, les valeurs `12:170`, `0:0` et `5:14` signifient que
*   12 tâches sont en attente; ces tâches ont demandé
    *   des nœuds entiers,
    *   moins de 8Go de mémoire par cœur et
    *   un temps d'exécution de 3 heures ou moins.
*   170 tâches sont en attente; ces tâches ont demandé
    *   moins que des nœuds entiers et sont donc en attente pour des cœurs individuels,
    *   moins de 8Go de mémoire par cœur et
    *   un temps d'exécution de 3 heures ou moins.
*   5 tâches sont en attente; ces tâches ont demandé
    *   un nœud entier avec GPU
    *   un temps d'exécution de 3 heures ou moins.
*   14 tâches sont en attente; ces tâches ont demandé
    *   des GPU uniques
    *   un temps d'exécution de 3 heures ou moins.

Aucune tâche en attente ou en exécution ne demande un nœud de type *large* et 3 heures d'exécution.

Au bas du tableau se trouve la répartition des ressources par politique; ceci ne tient pas compte des tâches en cours. Il y a donc 871 nœuds de type *base* appelés ici *regular*, soit des nœuds ayant de 4 à 8 Go par cœur qui peuvent recevoir des tâches sur nœuds entiers d'une durée de moins de 3 heures. De ces 871,
*   431 peuvent aussi recevoir des tâches *par cœur* de moins de 3 heures
*   851 peuvent recevoir des tâches sur nœuds entiers d'une durée de moins de 12 heures
*   ainsi de suite.

Les partitions sont organisées un peu comme des [poupées russes](https://fr.wikipedia.org/wiki/Poup%C3%A9e_russe). La partition pour 3 heures contient un sous-ensemble de nœuds pour la partition pour 12 heures; la partition pour 12 heures contient un sous-ensemble de nœuds pour la partition pour 24 heures; et ainsi de suite.

L'utilitaire `partition-stats` ne donne aucun renseignement sur le nombre de cœurs utilisés par les tâches en cours ou en attente; le nombre de cœurs libres dans les partitions par cœur des nœuds partiellement assignés; et la mémoire disponible associée avec les cœurs libres dans les partitions *par cœur*.

Le fait d'exécuter `partition-stats` exige beaucoup de l'ordonnanceur. Évitez donc de faire des appels automatiques de façon répétitive dans vos scripts. Si vous croyez qu'il serait avantageux d'utiliser `partition-stats`, contactez le [soutien technique](technical-support.md) pour savoir comment procéder.

## Nombre de tâches

Il est possible qu'une limite soit imposée au nombre de tâches exécutées au même moment.

Pour [Narval](narval.md), [Nibi](nibi.md) et [Rorqual](rorqual.md), un compte normal ne peut avoir plus de 1000 tâches en exécution ou en attente au même moment. Dans [un vecteur de tâches](job-arrays.md), chacune compte pour une tâche. Le paramètre Slurm [MaxSubmit](https://slurm.schedmd.com/sacctmgr.html) en fixe la limite.

## Changements à nos politiques d'ordonnancement

La page [Mise à jour de nos politiques d'ordonnancement](scheduling-policy-updates.md) liste des changements susceptibles de modifier le résultat de vos scripts.