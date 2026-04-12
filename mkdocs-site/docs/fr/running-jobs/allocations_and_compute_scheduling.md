---
title: "Allocations and compute scheduling/fr"
slug: "allocations_and_compute_scheduling"
lang: "fr"

source_wiki_title: "Allocations and compute scheduling/fr"
source_hash: "ad07300d0355335a030b0b1232a8d452"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T05:01:45.226618+00:00"

tags:
  - slurm

keywords:
  - "allocation CCDB"
  - "tâches en attente"
  - "prévision des événements"
  - "Ressources partagées"
  - "unités GPU de référence"
  - "équivalents-cœurs"
  - "Ratios dans les bundles"
  - "GPU V100-32gb"
  - "Utilisation des GPU"
  - "V100-16gb"
  - "instance GPU"
  - "P100-12gb"
  - "GPU"
  - "Utilisation mensuelle"
  - "T4-16gb"
  - "SLURM"
  - "projection de l'utilisation"
  - "formulaire CCDB"
  - "Utilisation par utilisateur"
  - "équivalents-cœur"
  - "bundle"
  - "ratio"
  - "période d'allocation"
  - "H100"
  - "Groupes"
  - "Total cumulé"
  - "UGR-coeur-mémoire"
  - "Grappe"
  - "allocations en UGR"
  - "ordonnanceur"
  - "Utilisation par ressource de calcul"
  - "V100-32gb"
  - "Unités GPU de référence (UGR)"
  - "utilisation de la mémoire"
  - "cible allouée"
  - "Modèles de GPU"
  - "profil du compte"
  - "GPU multi-instances"
  - "mémoire"
  - "ressources en attente"
  - "Rorqual"
  - "Allocation"
  - "demande de GPU"
  - "GPU A100-40gb"
  - "tâches en cours"
  - "équivalents-UGR"
  - "Année d'allocation"
  - "GB"
  - "allocation des ressources"
  - "Surutilisation"
  - "P100-16gb"
  - "date de fin"
  - "Ressource de calcul"
  - "Ordonnancement par priorité"
  - "mémoire vive"
  - "Stockage et gestion des fichiers"
  - "Utilisation par projet"
  - "parts brutes"
  - "Unités GPU de référence"
  - "portail Slurm"
  - "tâches en file d'attente"
  - "Utilisation des ressources"
  - "modèles de GPU"
  - "utilisation brute"
  - "CCDB"
  - "résultats de la projection"
  - "calcul de priorité"
  - "utilisation des ressources"
  - "quantité de ressources"
  - "Slurm"
  - "cœurs"
  - "Mémoire des GPU"
  - "CPU et GPU"
  - "Calcul haute performance"
  - "surutilisation de ressources"
  - "utilisation moyenne"
  - "compte Slurm"
  - "allocation de ressources"
  - "Caractéristiques des nœuds"
  - "Opérations à virgule flottante"
  - "priorité des tâches"
  - "grappe fictive"

questions:
  - "Qu'est-ce qu'une allocation de ressources en calcul haute performance et quelle est la différence entre l'allocation de stockage et celle des ressources partagées ?"
  - "De quelle manière l'ordonnanceur calcule-t-il la priorité des tâches pour assurer une répartition équitable des ressources entre les groupes ?"
  - "Que se passe-t-il lorsqu'un groupe de recherche dépasse la cible d'utilisation de son allocation CPU ou GPU ?"
  - "Pourquoi les Unités GPU de référence (UGR) ont-elles été créées et quel problème visent-elles à résoudre dans l'attribution des ressources ?"
  - "Quels sont les trois critères d'évaluation, ainsi que leurs poids respectifs, utilisés pour calculer le score UGR d'un modèle de GPU ?"
  - "Quel modèle de GPU sert de référence standard pour le calcul des UGR et quelle valeur de base lui est historiquement attribuée ?"
  - "Quelle doit être l'utilisation moyenne des ressources par rapport à la cible allouée sur la période donnée ?"
  - "Est-il possible d'accomplir plus de travail que ce que l'allocation initiale permet théoriquement ?"
  - "Pourquoi est-il peu probable qu'un utilisateur puisse bénéficier de ressources supplémentaires au-delà de son allocation ?"
  - "Quels sont les différents modèles de cartes graphiques comparés dans ce fragment de tableau ?"
  - "Quelles sont les différences de valeurs numériques attribuées aux modèles V100 par rapport aux modèles P100 ?"
  - "Que signifient les critères évalués par \"oui\" ou \"non\" pour ces différents équipements matériels ?"
  - "Qu'est-ce que la technologie GPU multi-instances et comment modifie-t-elle l'utilisation des ressources selon le renouvellement de l'infrastructure prévu en 2025 ?"
  - "Comment le type d'opérations d'une application (FP32 par rapport à FP16) influence-t-il le choix du modèle de GPU le plus rentable en termes de performance et d'UGR ?"
  - "De quelle manière la quantité d'unités GPU de référence (UGR) est-elle calculée et attribuée lors d'une demande d'allocation dans le formulaire CCDB ?"
  - "Quelle information spécifique concernant le matériel doit être indiquée lors d'une demande de GPU ?"
  - "Dans quel formulaire le calcul des unités GPU de référence (UGR) s'effectue-t-il automatiquement ?"
  - "Quelles sont les données utilisées pour calculer la quantité d'UGR allouée à un projet ?"
  - "Comment le comité d'allocation gère-t-il les Unités de Gestion des Ressources (UGR) lors de l'attribution ou du transfert de GPU entre différentes grappes ?"
  - "Sur quel principe fondamental se base le système pour déterminer la priorité des tâches de calcul par rapport aux ressources demandées et non utilisées ?"
  - "Qu'est-ce qu'un « équivalent-cœur » et comment l'ordonnanceur l'utilise-t-il pour comptabiliser l'utilisation des ressources selon le ratio cœur/mémoire ?"
  - "Comment l'ordonnanceur calcule-t-il la priorité d'une demande de ressources en utilisant le système d'équivalents-UGR ?"
  - "Dans quels cas spécifiques l'évaluation de la demande se base-t-elle sur les cœurs ou la mémoire plutôt que sur le nombre de GPU (UGR) demandés ?"
  - "Qu'est-ce qu'un \"bundle\" de ressources et comment sa composition influence-t-elle le calcul des équivalents pour différents matériels comme les GPU V100 ou A100 ?"
  - "Comment l'ordonnanceur calcule-t-il la priorité d'une tâche spécifique qui demande 2 cœurs et 4 Go de mémoire totale ?"
  - "À partir de quel ratio précis la mémoire est-elle comptabilisée dans l'utilisation des ressources d'un groupe ?"
  - "Quelle est la distinction entre les \"équivalents-cœur\" et les bundles de mémoire lors de l'évaluation d'une demande ?"
  - "Combien d'équivalents-UGR sont associés au GPU V100-32gb selon la Figure 8 ?"
  - "Quelles sont les spécifications techniques (cœurs et mémoire vive) du bundle incluant le GPU A100-40gb ?"
  - "Quelle est la valeur totale en équivalents-UGR pour la configuration basée sur le GPU A100-40gb sur cette grappe fictive ?"
  - "Quelles sont les caractéristiques en termes de cœurs et de mémoire par UGR pour les différentes grappes de l'Alliance ?"
  - "Comment les ressources (cœurs et mémoire) sont-elles allouées et recommandées par GPU pour les modèles H100 et A100 selon les grappes ?"
  - "Quelle est la différence de ratio UGR par GPU entre une instance complète (comme H100-80gb) et une instance fractionnée (comme H100-1g.10gb) ?"
  - "Quelles sont les spécifications techniques (cœurs et mémoire) du nœud H100-80gb sur le système Rorqual ?"
  - "Comment les ressources matérielles diffèrent-elles entre les modèles H100-2g.20gb et H100-3g.40gb ?"
  - "Quelles sont toutes les variantes de configurations de GPU H100 listées dans ce document ?"
  - "Comment le portail permet-il de visualiser l'utilisation des ressources et quelles options de filtrage sont disponibles sur la page d'accueil ?"
  - "De quelle manière le graphique détaille-t-il l'utilisation des ressources entre les différents utilisateurs d'un compte Slurm spécifique ?"
  - "Quelles informations supplémentaires et métriques (telles que l'allocation CCDB ou les tâches en file d'attente) peuvent être affichées ou masquées à l'aide de la légende ?"
  - "Que représentent les fines barres grises dans les colonnes des ressources en attente ?"
  - "Quelle information est indiquée par le texte situé en haut de chaque barre ?"
  - "Comment peut-on interagir avec les éléments de la légende à l'aide des clics simples et doubles ?"
  - "Comment les parts brutes et l'utilisation brute SLURM influencent-elles la priorité des comptes et comment sont-elles représentées graphiquement ?"
  - "Quelles options interactives l'interface graphique offre-t-elle pour explorer en détail les données d'utilisation des ressources ?"
  - "Comment le système calcule-t-il et affiche-t-il la projection de l'utilisation future lorsqu'une date de fin ultérieure est saisie ?"
  - "Quelle est la différence entre les options de sommation \"Total\" et \"Total cumulé\" dans le portail Slurm, et comment cette dernière aide-t-elle à évaluer la juste part d'un compte ?"
  - "Comment peut-on accéder aux données d'utilisation des ressources de son groupe dans la base de données CCDB et quelles sont les différentes vues d'onglets proposées ?"
  - "De quelle manière les valeurs d'utilisation des CPU et GPU sont-elles calculées dans la CCDB, et quelle période l'affichage par ressource de calcul couvre-t-il ?"
  - "Quel indicateur visuel apparaît à l'écran lorsqu'une date de fin dans le futur est saisie ?"
  - "Quelles sont les hypothèses appliquées par le système pour le traitement des tâches en cours et en attente ?"
  - "Pourquoi les résultats de cette projection ne doivent-ils pas être interprétés comme une prévision réelle des événements futurs ?"
  - "Quelles informations sont affichées dans la vue concernant l'utilisation par ressource de calcul et les groupes d'utilisateurs ?"
  - "Quelle est la date de début de l'année d'allocation en cours prise en compte pour ces statistiques ?"
  - "Quelle hypothèse est utilisée pour projeter les données d'utilisation à jour jusqu'à la fin de l'année d'allocation ?"
  - "Comment peut-on accéder à la répartition mensuelle de l'utilisation pour une ressource ou un utilisateur spécifique ?"
  - "Quelles informations sont présentées dans l'en-tête et le tableau de la vue \"Utilisation par projet\" ?"
  - "Quelles sont les unités de mesure utilisées pour détailler l'utilisation des GPU par modèle dans le tableau récapitulatif ?"
  - "Comment peut-on accéder à la répartition mensuelle de l'utilisation pour une ressource ou un utilisateur spécifique ?"
  - "Quelles informations sont présentées dans l'en-tête et le tableau de la vue \"Utilisation par projet\" ?"
  - "Quelles sont les unités de mesure utilisées pour détailler l'utilisation des GPU par modèle dans le tableau récapitulatif ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de Politique d'ordonnancement des tâches*

# Allocations pour le calcul haute performance

**Une *allocation* est l’attribution d’une quantité de ressources à un groupe de recherche pour une période donnée, habituellement un an.** Il s'agit soit d'un maximum comme dans le cas du stockage, soit d'une moyenne d'utilisation sur une période donnée comme c'est le cas pour les ressources partagées que sont les cœurs de calcul.

L’allocation des ressources de stockage attribue un maximum déterminé d’espace réservé à l’usage exclusif d’un groupe de recherche. Pour sa part, l’allocation des ressources partagées que sont les cœurs-année et les GPU-année est plus complexe puisque ces ressources sont partagées par l’ensemble des groupes et que l’allocation tient compte de l’utilisation moyenne de chaque groupe.

La durée de l’allocation est une valeur de référence utilisée pour calculer la moyenne de la consommation des ressources au cours de la période pendant laquelle celles-ci sont disponibles. Par exemple, si les grappes ne sont pas disponibles pour une semaine dû à des opérations de maintenance, les groupes de recherche touchés n’obtiennent pas une semaine additionnelle en compensation à la fin de la période. De la même manière, si la période d’allocation est allongée, les groupes n’y perdent pas en utilisation.

!!! note
    Une allocation de cœurs-année et de GPU-année en ressources partagées considère la moyenne d’utilisation cible dans le temps; un groupe est donc plus susceptible d’atteindre et même de dépasser ses cibles en utilisant ses ressources de façon régulière sur la période qu’en soumettant des tâches en rafale (*burst*) ou en les reportant à plus tard.

## De l'allocation à l'ordonnancement par priorité

Les ressources de calcul par cœurs-année et par GPU-année reçoivent des tâches qui sont immédiatement prises en charge par l’ordonnanceur. Rappelons qu’une tâche se compose d’une application logicielle et de la liste des ressources pour l’exécuter. L’ordonnanceur est aussi une application logicielle dont le rôle est de calculer la priorité de chaque tâche et de lui attribuer les ressources nécessaires selon leur disponibilité et en accord avec les règles de priorisation.

À l’aide d’algorithmes spécialisés, l’ordonnanceur tient compte des cibles de chaque groupe et compare la consommation récente du groupe à l’utilisation qui lui était allouée. Un des facteurs déterminants est la consommation à l’intérieur de la période. Le facteur qui possède cependant le plus de poids est la consommation (ou la non-consommation) récente, ceci en vue d’offrir une opération plus stable aux groupes dont l’utilisation réelle se rapproche des ressources qui leur étaient allouées. Cette façon de procéder assure une meilleure répartition du parc de ressources pour l’ensemble des groupes et fait en sorte qu’il est théoriquement possible pour tous les groupes d’atteindre leurs cibles.

## Conséquences d'une surutilisation d'une allocation CPU ou GPU

Si vous avez des tâches en attente et qu’à ce moment la demande en ressources de calcul est basse, l’ordonnanceur pourrait faire exécuter vos tâches même si vous dépassez la quantité cible de votre allocation. Tout ce qui peut se produire alors serait que les prochaines tâches que vous soumettrez se voient attribuer un plus bas niveau de priorité que celles soumises par des groupes qui n’ont pas encore atteint leur niveau cible d’utilisation. Aucune tâche soumise à l’ordonnanceur n’est refusée en raison d’une surutilisation de ressources et votre utilisation moyenne de ressources sur la période d’allocation devrait se situer proche de la cible qui vous a été allouée.

Il se pourrait qu’au cours d’un mois ou d’une année vous puissiez accomplir plus de travail que votre allocation ne semblerait le permettre, mais ce scénario est peu probable puisque la demande est plus élevée que la quantité de ressources dont nous disposons.

# Unités GPU de référence (UGR)

La performance des GPU a considérablement augmenté ces dernières années et continue sa progression. Par le passé et jusqu'au concours de 2023, nous considérions tous les GPU comme étant équivalents les uns aux autres. Ceci posait des problèmes à la fois dans le processus d'attribution et lors de l'exécution des tâches. Pour contrer ceci, nous avons créé pour l'année 2024 l'unité GPU de référence (UGR) qui permet de classer tous les modèles de GPU en production. Depuis la période d'allocation de 2025-2026, nous devons aussi tenir compte de [la technologie des GPU multi-instances](../programming/multi-instance_gpu.md) qui rend la situation un peu plus complexe.

Parce qu'environ la moitié des tâches utilisent principalement des opérations à virgule flottante simple précision ([FP32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)), que les autres utilisent des opérations à virgule flottante demi-précision ([FP16](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)), et que la plupart des utilisateurs sont limités par la quantité de mémoire des GPU, nous classons les modèles de GPU selon les critères d'évaluation avec leur poids correspondant :

| Critère d'évaluation | Poids |
| :------------------- | :---- |
| score FP32 <small>(matrices denses sur les cœurs GPU réguliers)</small> | 40% |
| score FP16 <small>(matrices denses sur les [*cœurs Tensor*](https://www.techspot.com/article/2049-what-are-tensor-cores/))</small> | 40% |
| score mémoire GPU | 20% |

Nous utilisons le GPU **A100-40gb** de NVidia comme modèle de référence, auquel nous assignons la valeur UGR de 4 (pour des raisons historiques). Sa mémoire et ses performances FP32 et FP16 sont fixées à 1.0. En multipliant les pourcentages dans le tableau précédent par 4, nous obtenons les coefficients et les valeurs UGR pour les autres modèles.

**Scores UGR pour les GPU entiers, par modèle**

| Coefficient | Score FP32 | Score FP16 | Score mémoire | Score combiné (UGR) | Disponible Présentement | Disponible Pour 2026 | Alloué par concours 2026 |
| :---------- | :--------- | :--------- | :------------ | :------------------ | :-------------------- | :------------------ | :--------------------- |
| **1.6**     | **1.6**    | **0.8**    |             |                     |                     |                     |                        |
| H100-80gb   | 3.44       | 3.17       | 2.0         | 12.2                | oui                 | oui                 | oui                    |
| A100-80gb   | 1.00       | 1.00       | 2.0         | 4.8                 | ?                   | ?                   | non                    |
| **A100-40gb** | **1.00**   | **1.00**   | **1.0**     | **4.0**             | oui                 | oui                 | oui                    |
| V100-32gb   | 0.81       | 0.40       | 0.8         | 2.6                 | non                 | non                 | non                    |
| V100-16gb   | 0.81       | 0.40       | 0.4         | 2.2                 | non                 | ?                   | non                    |
| T4-16gb     | 0.42       | 0.21       | 0.4         | 1.3                 | non                 | non                 | non                    |
| P100-16gb   | 0.48       | 0.03       | 0.4         | 1.1                 | non                 | non                 | non                    |
| P100-12gb   | 0.48       | 0.03       | 0.3         | 1.0                 | non                 | non                 | non                    |

Le [renouvellement de l'infrastructure](../clusters/infrastructure_renewal.md) en 2025 permettra de planifier une fraction d'un GPU à l'aide de la [technologie GPU multi-instances](../programming/multi-instance_gpu.md). Différents travaux, appartenant potentiellement à différents utilisateurs, pourront s'exécuter sur le même GPU en même temps. Selon la terminologie de NVidia, une fraction d'un GPU allouée à un seul travail est appelée une *instance GPU*, (parfois *instance MIG*).

Le tableau suivant montre les modèles de GPU ou instances que vous pouvez sélectionner sur le formulaire dans CCDB pour votre demande d'allocation pour 2026. Les valeurs UGR des instances sont estimées à partir des valeurs de performance d'un GPU entier et de la fraction du GPU qu'occupe l'instance.

**Modèles et instances disponibles pour la période d'allocations 2025-2026**

| Modèle / Instance | Fraction du GPU | UGR  |
| :---------------- | :-------------- | :--- |
| **A100-40gb**     | GPU entier ⇒ 100% | 4.0  |
| A100-1g.5gb       | max(1g/7g, 5GB/40GB) ⇒ 14% | 0.6  |
| A100-2g.10gb      | max(2g/7g, 10GB/40GB) ⇒ 28% | 1.1  |
| A100-3g.20gb      | max(3g/7g, 20GB/40GB) ⇒ 50% | 2.0  |
| **H100-80gb**     | GPU entier ⇒ 100% | 12.2 |
| H100-1g.10gb      | max(1g/7g, 40GB/80GB) ⇒ 14% | 1.7  |
| H100-2g.20gb      | max(2g/7g, 40GB/80GB) ⇒ 28% | 3.5  |
| H100-3g.40gb      | max(3g/7g, 40GB/80GB) ⇒ 50% | 6.1  |

!!! note
    Une instance GPU ayant le profil **1g** vaut un septième (1/7) d'un GPU A100 ou H100. Le profil **3g** tient compte de la quantité de mémoire additionnelle par **g**. Par souci de simplicité, les profils **4g** ne sont pas disponibles sur nos grappes.

## Choisir les modèles de GPU pour votre projet

Les scores relatifs du précédent tableau devraient vous aider à sélectionner les modèles les plus convenables. Les exemples suivants présentent des cas extrêmes.

*   Si vos applications font surtout des opérations FP32, le modèle A100-40gb devrait être deux fois plus rapide que le P100-12gb, mais l'utilisation des ressources sera considérée comme étant quatre fois plus grande. En conséquence, pour le même nombre d'UGR, le modèle P100-12gb devrait vous permettre d'exécuter deux fois plus de calculs.
*   Si vos applications font surtout des opérations FP16 (ce qui est le cas en intelligence artificielle et avec les opérations à précision mixte ou utilisant [d'autres formats à virgule flottante](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)), l'utilisation d'un A100-40gb sera calculée comme utilisant quatre fois les ressources d'un P100-12gb, mais pourra faire ~30 fois plus de calculs dans la même période, ce qui vous permettrait d'exécuter ~7.5 fois plus de calculs.

## Constance des allocations en UGR

*   Dans le cadre du concours pour l'allocation de ressources, toute demande de GPU doit spécifier le modèle de GPU préféré pour le projet. Ensuite, dans le formulaire CCDB, la quantité d'unités GPU de référence (UGR) sera automatiquement calculée à partir de la quantité demandée de GPU-année par année de projet.
    *   Par exemple, si vous sélectionnez la ressource *narval-gpu* et demandez 13 GPU-année du modèle A100-40gb, la quantité correspondante en UGR serait de 13 \* 4,0 = 52. Le comité d’allocation des ressources attribuerait alors jusqu'à 52 UGR en fonction du score de la proposition. Si votre allocation doit être déplacée vers une autre grappe, le comité attribuera des GPU-année à cette autre ressource tout en conservant la même quantité en UGR.

# Effet détaillé de l'utilisation des ressources sur la priorité

Le principe gouverneur dans notre façon de déterminer la priorité des tâches de calcul se base sur les ressources qu’une tâche rend **non disponibles aux autres utilisateurs** plutôt que sur les ressources effectivement utilisées.

Le cas de cœurs non utilisés qui influent sur le calcul des priorités se produit souvent lorsqu’une tâche est soumise en demandant plusieurs cœurs, mais n’en consomme effectivement qu’une partie à l’exécution. C’est le nombre de cœurs demandés par une tâche qui a une incidence sur la priorisation des prochaines tâches puisque la tâche bloque les cœurs non utilisés pendant son exécution.

Un autre cas fréquent de cœurs non utilisés se pose lorsqu’une tâche exige plus de mémoire que celle demandée pour un cœur. Sur une grappe où chaque cœur serait doté de 4Go de mémoire, une tâche qui demanderait un seul cœur et 8Go de mémoire bloquerait donc 2 cœurs et le deuxième cœur ne serait pas disponible pour les tâches des autres groupes de recherche

## Équivalents-cœurs utilisés par l'ordonnanceur

Un équivalent-cœur se compose d’**un cœur simple et d’une certaine quantité de mémoire**; pour le nommer, nous utilisons le terme *bundle*. En plus du cœur, le bundle contient aussi la mémoire considérée comme étant associée à ce cœur.

Figure 1 – *Équivalent-cœur*

Présentement, nos grappes offrent surtout des cœurs de 4Go puisque ceci est le ratio mémoire:cœur pour le type de nœuds le plus commun. L’utilisation des ressources par une tâche est comptabilisée à raison de 4Go par cœur, comme mentionné ci-dessus (voir la Figure 1).

Le suivi des cibles s’avère relativement simple quand les ressources demandées sont des cœurs et des quantités de mémoire qui correspondent à un équivalent-cœur entier, plutôt qu’à une portion d’équivalent-cœur. Les choses se compliquent parce que l’utilisation de portions d’équivalents-cœur risque d’augmenter le pointage servant au calcul de la juste part du groupe de recherche. En pratique, la méthode appliquée résout le problème d'équité ou de perception d'équité, mais cette méthode n’est pas intuitive au début.

Dans les exemples qui suivent, la mémoire est de 4Go.

**Comptabilisation par équivalents-cœur**

Examinons le cas où nous avons un bundle composé de 1 cœur et 4Go de mémoire.

*   Figure 2 *– Deux équivalents-cœurs* Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de mémoire, c’est-à-dire plus que le ratio 1cœur/4Go.
    *   Dans la figure 2, on demande 2 cœurs et 2Go par cœur pour une mémoire totale de 4Go; la tâche exige 2 équivalents-cœur pour les cœurs, mais un seul bundle pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-cœurs.

*   Figure 3 – *2.5 équivalents-cœur* La mémoire est comptabilisée si un groupe utilise plus de mémoire que le ratio de 1 cœur/4Go.
    *   Dans la figure 3, on demande 2 cœurs et 5Go par cœur pour une mémoire totale de 10Go; la tâche exige 2.5 bundles pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2.5 équivalents-cœurs.

## Équivalents-UGR utilisés par l'ordonnanceur

L’utilisation des GPU et leurs ressources associées suit les mêmes principes que ceux décrits pour les équivalents-cœurs, sauf qu’une UGR est ajoutée au bundle avec de la mémoire et plusieurs cœurs. Ceci signifie que la comptabilisation de l’utilisation de la cible pour l’allocation de GPU doit inclure l’UGR. Tout comme le système de points utilisé dans l’expression de l’utilisation de la ressource en équivalents-cœurs, nous utilisons aussi un système de points pour les équivalents-UGR.

Le calcul de priorité se fait en fonction du nombre maximum de bundles UGR-cœurs-mémoire demandés. Examinons le cas où nous avons un bundle de 1 UGR, 3 cœurs et 4Go de mémoire.
Figure 4 - *1 équivalent-UGR*

*   Les UGR sont comptabilisés si un groupe utilise plus de UGR que de cœurs OU de mémoire par bundle. Prenons l'exemple d'un usager demandant 2 GPU (de 1 UGR chacun), 3 cœurs et 4Go de mémoire. La tâche exige donc l'équivalent de 2 bundles pour les GPU, mais un seul pour les cœurs et la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-UGR.
Figure 5 – *2 équivalents-UGR*

*   Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de UGR OU plus de mémoire par bundle avec GPU. Dans la figure 6, on demande 1 GPU de 1 UGR, 5 cœurs et 5Go; la requête exige donc 1.66 bundles avec GPU pour les cœurs, mais un seul bundle pour le GPU et 1.25 bundle pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue donc la demande à 1.66 équivalents-UGR.
Figure 6 – *1.66 équivalents-GPU (cœurs)*

*   La mémoire est comptabilisée si un groupe utilise plus de mémoire que de UGR OU de cœurs par bundle avec GPU. Dans la figure 7, on demande 1 GPU de 1 UGR, 2 cœurs et 6Go; la requête exige donc 1.5 bundle avec GPU pour la mémoire, mais un seul bundle pour les GPU et 0.66 pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 1.5 équivalents-GPU.
Figure 7 – *1.5 équivalents-GPU (mémoire)*

*   Sur la même grappe fictive, un bundle comprenant un GPU V100-32gb, 7.8 cœurs et 10.4 Go de mémoire vive vaudrait 2.6 équivalents-UGR :
Figure 8 - *2.6 équivalents-UGR, basés sur le GPU V100-32gb*

*   Sur la même grappe fictive, un bundle comprenant un GPU A100-40gb, 12 cœurs et 16 Go de mémoire vive vaudrait 4.0 équivalents-UGR :
Figure 9 - *4.0 équivalents-UGR, basés sur le GPU A100-40gb*

### Ratios dans les bundles

Les différents bundles UGR-cœur-mémoire et GPU-cœur-mémoire des systèmes de l'Alliance ont les caractéristiques suivantes (un seul ratio par grappe) :

| Grappe | Cœurs par UGR | Mémoire par UGR (en GB) |
| :----- | :------------ | :---------------------- |
| [Fir](../software/fir.md) | 0.98 | 23.6 |
| [Narval](../clusters/narval.md) | 3.00 | 31.1 |
| [Nibi](../clusters/nibi.md) | 1.15 | 20.5 |
| [Rorqual](../clusters/rorqual.md) | 1.31 | 10.2 |
| [Trillium](../clusters/trillium.md) | 1.97 | 15.4 |

Caractéristiques des bundles

| Grappe | Modèle ou instance | UGR par GPU | Bundle par GPU | Recommandation par GPU |
| :----- | :----------------- | :---------- | :------------- | :--------------------- |
| [Fir](../software/fir.md) | **H100-80gb** | **12.2** | **12 cœurs, 288GB** | **12 cœurs, 280GB** |
| | H100-1g.10gb | 1.74 | 1.7 cœurs, 41GB | 1 cœurs, 35GB |
| | H100-2g.20gb | 3.48 | 3.4 cœurs, 82GB | 3 cœurs, 70GB |
| | H100-3g.40gb | 6.1 | 6 cœurs, 144GB | 6 cœurs, 140GB |
| [Narval](../clusters/narval.md) | **A100-40gb** | **4.0** | **12 cœurs, 124.5GB** | **12 cœurs, 124GB** |
| | A100-1g.5gb | 0.57 | 1.7 cœurs, 17.7GB | 1 cœur, 15GB |
| | A100-2g.10gb | 1.14 | 3.4 cœurs, 35.4GB | 3 cœurs, 31GB |
| | A100-3g.20gb | 2.0 | 6.0 cœurs, 62.2GB | 6 cœurs, 62GB |
| | A100-4g.20gb | 2.3 | 6.9 cœurs, 71.5GB | 6 cœurs, 62GB |
| [Nibi](../clusters/nibi.md) | **H100-80gb** | **12.2** | **14 cœurs, 250GB** | **14 cœurs, 250GB** |
| | H100-1g.10gb | 1.74 | 2 cœurs, 35.7GB | 2 cœurs, 31GB |
| | H100-2g.20gb | 3.48 | 4 cœurs, 71.4GB | 4 cœurs, 62GB |
| | H100-3g.40gb | 6.1 | 7 cœurs, 125GB | 6 cœurs, 124GB |
| [Rorqual](../clusters/rorqual.md) | **H100-80gb** | **12.2** | **16 cœurs, 124.5GB** | **16 cœurs, 124GB** |
| | H100-1g.10gb | 1.74 | 2.3 cœurs, 17.7GB | 2 cœurs, 15GB |
| | H100-2g.20gb | 3.48 | 4.5 cœurs, 35.4GB | 4 cœurs, 31GB |
| | H100-3g.40gb | 6.1 | 8 cœurs, 62.2GB | 8 cœurs, 62GB |
| [Trillium](../clusters/trillium.md) | **H100-80gb** | **12.2** | **24 cœurs, 188GB** | **24 cœurs, 188GB** |

**Remarque :** Si l'ordonnanceur établit la priorité sur la base de l'utilisation calculée avec les bundles, une demande de plusieurs GPU sur un même nœud doit aussi tenir compte des ratios physiques.

# Visionner l'utilisation des ressources dans le portail

Page d'accueil du portail (cliquer deux fois sur l'image pour agrandir)
Le portail [portal.alliancecan.ca/slurm](https://portal.alliancecan.ca/slurm) offre une interface qui montre l'utilisation des ressources par les tâches soumises sur nos grappes nationales. Par défaut, l'image sur la page d'accueil affiche les jours CPU utilisés par tous vos projets sur une grappe quelconque. Si vous n'utilisez pas cette grappe, le message *Aucune donnée ou utilisation trop faible pour afficher un graphique pertinent* est affiché. Pour modifier l'image, sélectionnez des options dans les panneaux de gauche.
*   Sélectionner le système et les dates
*   Paramètres
*   Compte SLURM

## Utilisation par un compte particulier

Utilisation par un compte particulier
Si vous avez accès à plusieurs [comptes Slurm](running_jobs.md#comptes-et-projets), sélectionnez celui qui vous intéresse dans la liste sous *Compte SLURM ---> Sélectionner le compte de l'utilisateur*. Si *Sélectionner le compte de l'utilisateur* est vide, l'image montre l'utilisation faite par tous vos comptes sur la grappe sélectionnée et au cours de la période spécifiée. Le menu déroulant *Sélectionner le compte de l'utilisateur* liste tous les comptes pour lesquels des tâches ont été exécutées au cours de la période. Les autres comptes auxquels vous avez accès mais qui n'ont pas utilisé la grappe sélectionnée au cours de la période spécifiée sont aussi listés; cependant, puisque ces comptes ne généreront pas d'image, ils sont grisés et ne peuvent pas être sélectionnés. Lorsque vous sélectionnez un seul compte de projet, l'image est mise à jour et les détails du compte sont affichés dans le panneau *Informations sur l'allocation*. La hauteur de chaque barre correspond à la mesure de ce jour (par exemple, les jours pour les équivalents CPU) pour tous les utilisateurs du compte dans le système sélectionné. L'utilisation par les sept principaux utilisateurs est représentée par une couleur spécifique à chacun. La couleur grise sur laquelle les autres couleurs sont empilées représente l'utilisation par tous les autres utilisateurs. Vous pouvez parcourir l'image avec les outils [Plotly](https://plotly.com/graphing-libraries/) (zoom, panoramique, etc.) dont les icônes paraissent en haut à droite quand votre souris survole l'image. Vous pouvez également utiliser la légende sur le côté droit pour manipuler l'image. Cliquez sur un des éléments dans l'image pour le cacher ou le montrer de nouveau. Double-cliquer sur un élément cache ou montre tous les autres éléments dans l'image.

## Options de la légende

Légende de l'image
La légende propose des options d'affichage, plus précisément, des variables supplémentaires qui peuvent être activées ou désactivées. Outre l'affichage de la couleur de chaque utilisateur, la légende permet d'afficher l'utilisation brute SLURM, les parts brutes SLURM, l'allocation CCDB, les ressources en attente pour les tâches en file d'attente et le total quotidien. L'utilisation brute SLURM (*SLURM Raw Usage*) et les parts brutes SLURM (*SLURM Raw Shares*) sont obtenues à partir des parts pour chaque compte sur les grappes. L'allocation (*CCDB allocation*) correspond à la représentation des parts brutes SLURM dans le profil du compte dans CCDB. Les fines barres grises des colonnes des ressources en attente pour les tâches en file d'attente (*Queued jobs*) représentent la quantité de ressources pour les tâches dans la file d'attente, par jour. Le texte en haut de chaque barre indique le total quotidien par tous les utilisateurs pour la journée. Un simple clic sur un élément de la légende permet de l'activer ou le désactiver. Un double-clic permet d'activer ou de désactiver tous les autres éléments.

## Cible d'allocation et ressources en attente

Cible d'allocation et ressources en attente
Lorsqu'un seul compte a été sélectionné, les parts brutes Slurm sont affichées sous forme d'une ligne rouge horizontale. Elles peuvent être cachées ou montrées de nouveau en cliquant sur *Afficher la cible d'allocation par défaut* dans le panneau *Paramètres*, ou sur *Parts brutes SLURM* dans la légende à droite de l'image.

Pour faire afficher l'utilisation des ressources demandées pour les tâches en attente, cliquez sur *Tâches en file d'attente* dans la légende en haut à droite.

## Options graphiques

Options graphiques avec la souris
Les options natives de Plotly apparaissent en haut à droite lorsque le pointeur de la souris survole l'image. Les icônes *Télécharger le graphique en PNG*, *Agrandir*, *Déplacer*, *Sélection par boîte*, *Sélection au lasso*, *Agrandir*, *Réduire*, *Mise à l'échelle automatique* et *Réinitialiser les axes* permettent de modifier la sélection et l'échelle. Lorsque vous survolez une partie de la barre, un texte indique le nom de l'utilisateur, la journée et la quantité d'utilisation de l'élément pointé (notez que cela montre la quantité d'utilisation pour l'utilisateur spécifique et non la somme pour les utilisateurs pour cette journée).

## Parts brutes et utilisation brute par défaut

Affichage de l'utilisation par défaut du compte, incluant les parts brutes SLURM et l'utilisation brute SLURM
Les parts brutes SLURM d'un compte d'allocation rrg-* ou rpp-* sont une ligne droite correspondant à l'allocation de ressources du compte sur la grappe. Pour les comptes par défaut, les parts brutes SLURM évoluent dans le temps en fonction du nombre de comptes actifs sur la grappe. Tracer les parts brutes SLURM d'un compte par défaut sur une grappe spécifique permet de déterminer facilement l'utilisation attendue d'un compte par défaut sur cette grappe.

L'utilisation brute SLURM est une mesure utilisée par l'ordonnanceur pour déterminer la priorité des comptes. Elle correspond à la somme cumulée de l'utilisation des comptes en unités de facturation, plus une période de décroissance. Tracer l'utilisation brute SLURM d'un compte permet d'évaluer l'influence de l'utilisation passée sur la priorité du compte au fil du temps. En règle générale, si l'utilisation brute SLURM est 10 fois supérieure aux parts brutes SLURM, l'utilisation du compte est équivalente à sa part cible (par exemple, le taux d'utilisation que la planification vise à maintenir pour le compte).

## Grappe et dates de début et de fin

Sélectionner une grappe et un intervalle de temps
Le menu déroulant *Système* montre les grappes actives qui utilisent l'ordonnanceur Slurm. Vous pouvez utiliser les champs *Date de début (incl.)* et *Date de fin (incl.)* pour indiquer un intervalle de temps; l'entrée d'une date de fin dans le futur fera afficher une projection de l'utilisation. Le résultat montrera les tâches en exécution (E) et en attente (A), pour la durée demandée.

## Projection de l'utilisation

La bande horizontale rouge (à droite) délimite les résultats projetés
L'entrée d'une date de fin dans le futur fait afficher une bande rouge verticale qui délimite les résultats de la projection. Nous supposons ici que chacune des tâches en cours sera exécutée à l'intérieur de la limite de temps demandée. Dans le cas des tâches en attente, nous supposons que chacune commencera à la date de fin demandée (c'est-à-dire maintenant) et se poursuivra pour la durée demandée. Le résultat n'est aucunement une prévision des événements qui pourraient se produire.

## Métriques, sommation et tâches en cours d'exécution

Paramètres
Dans le menu déroulant *Métrique* vous pouvez sélectionner parmi les indicateurs suivants : CPU, équivalent-CPU, UGR, équivalent-UGR, mémoire, comptabilisation, GPU et tous les modèles de GPU disponibles sur la grappe sélectionnée.

Le menu déroulant *Sommation* permet de basculer entre *Total* et *Total cumulatif*. Si vous sélectionnez *Total*, chaque barre représente l'utilisation totale pour cette journée. Si vous sélectionnez *Total cumulatif*, chaque barre représente la somme de l'utilisation pour cette journée plus tous les jours précédents jusqu'au début de la période spécifiée. Si l'*Afficher la cible d'allocation par défaut* est *Oui*, elle est ajustée de la même manière pour afficher le total cumulé de l'utilisation cible. Consultez la section suivante pour en savoir plus.

Dans le menu *Inclure les tâches en cours*, cliquez sur *Non* pour faire afficher l'utilisation par les tâches terminées et sur *Oui* pour inclure l'utilisation par les tâches en cours.

## Total cumulé

Total de l'utilisation par le compte
Le graphique montre comment un compte s'écarte de sa part cible dans la période sélectionnée. Les valeurs utilisées sont la somme cumulée sur plusieurs jours à partir de la vue de sommation totale de l'utilisation et la cible d'allocation. Lorsqu'une tâche soumise demande plus que la part cible du compte, on s'attend que la somme cumulée de l'utilisation oscille au-dessus et en dessous de la part cible si l'ordonnanceur gère correctement le principe de la juste part. Étant donné que l'ordonnanceur utilise une période de décroissance pour l'utilisation passée, un bon intervalle pour déterminer sa performance dans le maintien de la juste part est de faire afficher les 30 derniers jours.

# Visionner l'utilisation des ressources dans CCDB

Onglet *Mon compte*, option *Utilisation par le groupe*
Vous pouvez visionner les données d’utilisation des ressources par votre groupe en sélectionnant *Mon compte --> Utilisation par le groupe* dans la base de données CCDB.

Utilisation de CPU et de GPU, par ressource de calcul
Les valeurs pour l’utilisation des CPU (cœurs-année) et des GPU-année sont calculées selon la quantité des ressources allouées aux tâches exécutées sur les grappes. Notez que les valeurs employées dans les graphiques ne représentent pas les équivalents-cœur; ainsi, l’utilisation par les tâches qui exigent beaucoup de mémoire ne correspond pas à l’utilisation du compte représentée par l’ordonnanceur de la grappe.

La première barre d’onglets offre les vues suivantes :
*   **Par ressource de calcul**; nom de la grappe sur laquelle les tâches ont été soumises.
*   **Par projet (RAPI)**; projets auxquels les tâches ont été soumises.
*   **Par utilisateur**; utilisatrice ou utilisateur ayant soumis les tâches.
*   **Utilisation du stockage**; voyez [Stockage et gestion des fichiers](../storage-and-data/storage_and_file_management.md).

## Utilisation par ressource de calcul

Cette vue montre l’utilisation par ressource de calcul par grappe, pour tous les groupes desquels vous êtes propriétaire ou membre, pour l’année d’allocation en cours qui commence le 1er avril. Les données représentent l’utilisation à jour et supposent que cette utilisation restera la même jusqu’à la fin de l’année d’allocation.

Utilisation mensuelle par ressource
Dans la colonne *Extra Info*, cliquez sur *Utilisation sur une base mensuelle* pour obtenir la répartition mensuelle pour la ressource correspondante. En cliquant sur *Utilisation par utilisateur*, la répartition se fait par utilisateur ou utilisatrice ayant soumis les tâches.

## Utilisation par projet

Utilisation par projet, avec répartition mensuelle
Pour cette vue, une troisième barre d'onglets permet de sélectionner l'identifiant de projet pour l'année d'allocation choisie. Le tableau montre les détails pour chaque projet ainsi que les ressources utilisées sur toutes les grappes. Dans le haut de la vue, on trouve le nom du compte (par exemple def-, rrg- ou rpp-*, etc.), le titre du projet et le ou la propriétaire, ainsi que les sommaires de l'allocation et de l'utilisation.

## Utilisation des GPU en unités GPU de référence (UGR)

Sommaire de l'utilisation des GPU et le détail en unités GPU de référence (UGR) par modèle.
Pour chaque projet (RAPI) ayant une utilisation de GPU, le détail d'utilisation par modèle de GPU est donné en GPU-années et en UGR-années dans une table située au bas de la page.

## Utilisation par utilisateur

Utilisation de CPU et GPU
Cette vue montre l'utilisation par utilisatrices et utilisateurs ayant soumis des tâches pour le projet sélectionné (comptes de groupes), par système. En cliquant sur le nom d'une personne en particulier, vous obtiendrez son utilisation répartie par grappe. Tout comme les sommaires pour les groupes, vous pouvez utiliser l'option *Utilisation sur une base mensuelle*.