---
title: "Allocations and compute scheduling/fr"
slug: "allocations_and_compute_scheduling"
lang: "fr"

source_wiki_title: "Allocations and compute scheduling/fr"
source_hash: "6771cd2a4a638031ddfdb581cea6f5dd"
last_synced: "2026-11-08T02:07:32.985064+00:00"
last_processed: "2026-11-08T02:46:12.304688+00:00"

tags:
  - slurm

keywords:
  - "consommation moyenne"
  - "utilisation cible"
  - "SLURM Raw Usage"
  - "part cible"
  - "équivalent-cœur"
  - "utilisation cumulative"
  - "tâches en cours"
  - "survol"
  - "cœurs‑année et GPU‑année"
  - "tâches terminées"
  - "utilisation moyenne"
  - "projet sélectionné"
  - "Slurm"
  - "Queued jobs"
  - "bundle GPU"
  - "cœur simple"
  - "équivalent‑cœur"
  - "modifier l'image"
  - "Include running jobs"
  - "Select system and dates"
  - "12 cœurs"
  - "équivalent‑CPU"
  - "CPU et GPU"
  - "projet (RAPI)"
  - "UGR‑années"
  - "allocation de ressources"
  - "Légende de l'image"
  - "Running total)"
  - "panneaux de gauche"
  - "icônes"
  - "parts brutes SLURM"
  - "CCDB"
  - "cœurs par UGR"
  - "Select user’s account"
  - "mémoire"
  - "mémoire associée"
  - "Narval"
  - "quantité d'utilisation"
  - "équivalents-UGR"
  - "ordonnanceur de tâches"
  - "modèles GPU"
  - "288GB"
  - "Bundle par GPU"
  - "équivalents‑UGR"
  - "cible allouée"
  - "SLURM account"
  - "Zoom"
  - "mémoire par UGR"
  - "Utilisation par un compte particulier"
  - "H100-80gb"
  - "compte Slurm"
  - "priorité des tâches"
  - "GPU en unités GPU de référence (UGR)"
  - "ordonnanceur"
  - "Utilisation par utilisateur"
  - "métriques (CPU"
  - "portail"
  - "score combiné"
  - "utilisation par ressource de calcul"
  - "unités GPU de référence (UGR)"
  - "ratio de performance en FP16"
  - "allocation 2027"
  - "valeurs UGR"
  - "GPU"
  - "ratio de performance en FP32"
  - "bundle"
  - "sommation (Total"
  - "instance GPU"
  - "Utilisation sur une base mensuelle"
  - "ratios dans les bundles"
  - "technologie GPU multi‑instances"
  - "Unités GPU de référence (UGR)"
  - "Display allocation target by default"
  - "Recommendation par GPU"
  - "instance MIG"
  - "GPU‑années"
  - "UGR"
  - "sélection"
  - "utilisation brute SLURM"
  - "projection de l'utilisation"
  - "etc.)"
  - "tâches soumises"
  - "surutilisation de ressources"
  - "demande supérieure"
  - "cœurs"
  - "surutilisation d’une allocation"

questions:
  - "Quelle différence existe‑t‑il entre une allocation de stockage (définie comme un maximum) et une allocation de ressources partagées telles que les cœurs‑année ou GPU‑année (définie comme une moyenne d’utilisation) ?"
  - "Comment l’ordonnanceur calcule‑t‑il la priorité des tâches en se basant sur la consommation récente d’un groupe par rapport à la cible d’allocation qui lui a été attribuée ?"
  - "Quelles sont les conséquences pour un groupe qui sur‑utilise son allocation CPU ou GPU, notamment concernant la priorité des tâches soumises ultérieurement ?"
  - "Quels critères d'évaluation et quels poids sont utilisés pour calculer les UGR des GPU ?"
  - "Comment les scores UGR (FP32, FP16, mémoire et combiné) sont‑ils attribués aux différents modèles de GPU entiers présentés ?"
  - "De quelle manière la technologie GPU multi‑instances (MIG) modifie‑t‑elle l’allocation des ressources GPU pour les travaux à partir de 2025‑2027 ?"
  - "Pourquoi la demande a-t-elle été refusée selon le texte ?"
  - "Quelle doit être votre utilisation moyenne de ressources pendant la période d’allocation ?"
  - "Le texte indique-t-il qu’il est possible d’accomplir plus de travail que votre allocation ne le permet, et pourquoi ce scénario est‑il considéré comme peu probable ?"
  - "Qu'entend‑on par « instance GPU » ou « instance MIG » dans le cadre d’une allocation de ressources ?"
  - "Comment les valeurs UGR des instances sont‑elles estimées à partir des performances d’un GPU entier et de la fraction qu’occupe l’instance ?"
  - "Où et comment choisir les modèles de GPU ou les instances sur le formulaire CCDB lors d’une demande d’allocation pour 2027 ?"
  - "Quels sont les modèles de GPU disponibles pour le concours 2027, leurs fractions de GPU et leurs valeurs UGR associées ?"
  - "Comment la quantité d’unités GPU de référence (UGR) est‑elle calculée à partir des GPU‑année demandés et conservée lors d’un déplacement d’allocation vers une autre grappe ?"
  - "Quels critères déterminent la priorité des tâches de calcul et comment le scheduler définit‑il un « équivalent‑cœur » (bundle) ?"
  - "Qu’est‑ce qu’un « équivalent‑cœur » tel que décrit dans le texte ?"
  - "Quel terme est employé pour désigner l’ensemble d’un cœur simple et de la mémoire qui lui est associée ?"
  - "Outre le cœur, quelle autre ressource le bundle comprend‑il selon la description ?"
  - "Comment le système d’équivalents‑cœur détermine‑t‑il la priorité d’une tâche lorsqu’elle sollicite davantage de cœurs que de mémoire ?"
  - "En quoi la prise en compte de portions d’équivalents‑cœur complique‑t‑elle le calcul du pointage de répartition des ressources ?"
  - "Comment les équivalents‑UGR sont‑ils intégrés dans le calcul de priorité lorsqu’une demande comprend des GPU, des cœurs et de la mémoire ?"
  - "Comment l’ordonnanceur calcule‑t‑il la demande en équivalents‑UGR lorsqu’une requête utilise plus de cœurs ou de mémoire que le bundle GPU prévu ?"
  - "Quel nombre d’équivalents‑UGR est attribué aux bundles contenant respectivement un GPU V100‑32 GB et un GPU A100‑40 GB selon les figures 8 et 9 ?"
  - "Quels sont les ratios « cœurs par UGR » et « mémoire par UGR (en GB) » pour les grappes Fir, Narval, Nibi, Rorqual et Trillium ?"
  - "Comment l'ordonnanceur calcule-t-il la priorité lorsqu’un usager demande plusieurs types de ressources (GPU, cœurs, mémoire) ?"
  - "Pourquoi la demande de 2 GPU nécessite‑t‑elle 2 bundles alors que les cœurs et la mémoire n’en requièrent qu’un seul ?"
  - "Que signifie la notion d’« équivalents‑UGR » dans le cadre de l’allocation des ressources ?"
  - "Quel GPU présente l’indice UGR le plus élevé dans le tableau ?"
  - "Quelles sont les spécifications en nombre de cœurs et capacité mémoire pour chaque modèle de GPU répertorié ?"
  - "Quelle est la configuration « Bundle » et la recommandation associées à chaque GPU ?"
  - "Quelles sont les spécifications (cœurs, mémoire GPU et RAM) des nœuds H100‑3g.40 GB pour les clusters Narval, Nibi, Rorqual et Trillium ?"
  - "Comment l’ordonnanceur détermine‑t‑il la priorité des demandes de plusieurs GPU sur un même nœud en tenant compte des ratios physiques ?"
  - "Comment un utilisateur peut‑il visualiser l’utilisation de ses ressources (CPU, GPU, etc.) via le portail Slurm d’Alliance CAN ?"
  - "Comment sélectionner les options dans les panneaux de gauche pour modifier l'image ?"
  - "Quelles sont les étapes pour choisir le système, les dates et les paramètres dans l'interface ?"
  - "Comment consulter et interpréter l’utilisation d’un compte SLURM spécifique à l’aide du tableau présenté ?"
  - "Comment sélectionner un compte dans le menu « Select user’s account » et quel impact cela a‑t‑il sur l’image affichée et les informations du panneau « Allocation Information » ?"
  - "Quelles sont les différentes options proposées dans la légende (SLURM Raw Usage, SLURM Raw Shares, CCDB allocation, Queued jobs, total quotidien) et comment les activer ou les désactiver ?"
  - "Quels outils interactifs Plotly (téléchargement, zoom, pan, sélection, réinitialisation) sont disponibles pour manipuler le graphique et que révèle le texte d’infobulle lorsqu’on survole une barre ?"
  - "Quels sont les icônes disponibles (Download plot as a png, Zoom, Pan, Box Select, Lasso Select, Zoom in, Zoom out, Autoscale, Reset axes) et quelles actions permettent‑elles d’effectuer sur le graphique ?"
  - "Que révèle le texte affiché lorsqu’on survole une partie de la barre du graphique ?"
  - "Cette valeur affichée correspond‑elle à la quantité d’utilisation totale pour la journée ou uniquement à celle de l’utilisateur pointé ?"
  - "Quelle est la différence entre les parts brutes SLURM et l'utilisation brute SLURM, et comment chaque mesure influence la priorité d’un compte ?"
  - "Comment le portail SLURM projette‑t‑il l’utilisation future lorsqu’une date de fin future est renseignée, et quelles hypothèses sont faites pour les tâches en cours et en attente ?"
  - "Quels effets ont les sélections des menus « Metric », « Summation » et « Include running jobs » sur la visualisation des données d’utilisation ?"
  - "Comment le graphique « Total cumulé » permet‑il d’évaluer le respect de la part cible d’un compte sur les 30 derniers jours ?"
  - "Quelles sont les différentes vues proposées dans la section « Utilisation par le groupe » du CCDB et quelles informations chacune d’elles affiche‑t‑elle ?"
  - "Comment les consommations de GPU sont‑elles présentées en GPU‑années et en unités GPU de référence (UGR) pour chaque projet ?"
  - "Comment la fonction « Display allocation target by default » influence‑t‑elle l’affichage du total cumulé de l’utilisation cible ?"
  - "Quel est l’impact du réglage « Include running jobs » lorsqu’on choisit « No » par rapport à « Yes » sur les tâches affichées ?"
  - "Pourquoi le texte indique‑t‑il qu’il faut consulter la section suivante pour en savoir plus sur ces paramètres ?"
  - "Quels éléments (titre du projet, propriétaire, sommaires d’allocation et d’utilisation) sont présentés dans le tableau récapitulatif d’un projet ?"
  - "Comment l’utilisation des GPU est‑elle exprimée dans le rapport, notamment en unités GPU de référence (UGR) ?"
  - "Où se trouve le tableau détaillant l’utilisation des GPU par modèle pour chaque projet RAPI, et quelles unités y sont utilisées ?"
  - "Quel type d'information la vue « Utilisation par utilisateur » présente‑t‑elle pour chaque compte ?"
  - "Comment accéder à la répartition de l’utilisation d’un utilisateur par grappe en cliquant sur son nom ?"
  - "Comment activer l’option « Utilisation sur une base mensuelle » pour afficher les données mensuelles ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page connexe de [Politique d'ordonnancement des tâches](job_scheduling_policies.md)*

# Allocations pour le calcul haute performance

**Une *allocation* est l’attribution d’une quantité de ressources à un groupe de recherche pour une période donnée, habituellement un an.** Il s'agit soit d'un maximum comme dans le cas du stockage, soit d'une moyenne d'utilisation sur une période donnée comme c'est le cas pour les ressources partagées que sont les cœurs de calcul.

L’allocation des ressources de stockage attribue un maximum déterminé d’espace réservé à l’usage exclusif d’un groupe de recherche. Pour sa part, l’allocation des ressources partagées que sont les cœurs-année et les GPU-année est plus complexe puisque ces ressources sont partagées par l’ensemble des groupes et que l’allocation tient compte de l’utilisation moyenne de chaque groupe.

La durée de l’allocation est une valeur de référence utilisée pour calculer la moyenne de la consommation des ressources au cours de la période pendant laquelle celles-ci sont disponibles. Par exemple, si les grappes ne sont pas disponibles pour une semaine dû à des opérations de maintenance, les groupes de recherche touchés n’obtiennent pas une semaine additionnelle en compensation à la fin de la période. De la même manière, si la période d’allocation est allongée, les groupes n’y perdent pas en utilisation.

Notons qu’une allocation de cœurs-année et de GPU-année en ressources partagées considère la moyenne d’utilisation cible dans le temps; un groupe est donc plus susceptible d’atteindre et même de dépasser ses cibles en utilisant ses ressources de façon régulière sur la période qu’en soumettant des tâches en rafale (*burst*) ou en les reportant à plus tard.

## De l'allocation à l'ordonnancement par priorité

Les ressources de calcul par cœurs-année et par GPU-année reçoivent des tâches qui sont immédiatement prises en charge par l’ordonnanceur. Rappelons qu’une tâche se compose d’une application logicielle et de la liste des ressources pour l’exécuter. L’ordonnanceur est aussi une application logicielle dont le rôle est de calculer la priorité de chaque tâche et de lui attribuer les ressources nécessaires selon leur disponibilité et en accord avec les règles de priorisation.

À l’aide d’algorithmes spécialisés, l’ordonnanceur tient compte des cibles de chaque groupe et compare la consommation récente du groupe à l’utilisation qui lui était allouée. Un des facteurs déterminants est la consommation à l’intérieur de la période. Le facteur qui possède cependant le plus de poids est la consommation (ou la non-consommation) récente, ceci en vue d’offrir une opération plus stable aux groupes dont l’utilisation réelle se rapproche des ressources qui leur étaient allouées. Cette façon de procéder assure une meilleure répartition du parc de ressources pour l’ensemble des groupes et fait en sorte qu’il est théoriquement possible pour tous les groupes d’atteindre leurs cibles.

## Conséquences d'une surutilisation d'une allocation CPU ou GPU

!!! note "Conséquences de la surutilisation d'une allocation"
    Si la demande en ressources de calcul est basse et que vous avez des tâches en attente, l'ordonnanceur pourrait les exécuter même si vous dépassez votre allocation cible. La principale conséquence est que vos prochaines tâches pourraient se voir attribuer une priorité plus faible que celles soumises par des groupes n'ayant pas encore atteint leur niveau d'utilisation cible. Aucune tâche n'est refusée pour cause de surutilisation, et votre utilisation moyenne devrait rester proche de votre cible d'allocation sur la période.

Il se pourrait qu’au cours d’un mois ou d’une année vous puissiez accomplir plus de travail que votre allocation ne semblerait le permettre, mais ce scénario est peu probable puisque la demande est plus élevée que la quantité de ressources dont nous disposons.

# Unités GPU de référence (UGR)

La performance des GPU a considérablement augmenté ces dernières années et continue sa progression. Par le passé et jusqu'au concours de 2023, nous considérions tous les GPU comme étant équivalents les uns aux autres. Ceci posait des problèmes à la fois dans le processus d'attribution et lors de l'exécution des tâches. Pour contrer ceci, nous avons créé pour l'année 2024 l'unité GPU de référence (UGR) qui permet de classer tous les modèles de GPU en production. Depuis la période d'allocation de 2025-2026, nous devons aussi tenir compte de [la technologie des GPU multi-instances](../programming/multi-instance_gpu.md) qui rend la situation un peu plus complexe.

Parce qu'environ la moitié des tâches utilisent principalement des opérations à virgule flottante simple précision ([FP32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)), que les autres utilisent des opérations à virgule flottante demi-précision ([FP16](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)), et que la plupart des utilisateurs sont limités par la quantité de mémoire des GPU, nous classons les modèles de GPU selon les critères d'évaluation avec leur poids correspondant :

| Critère d'évaluation                                                | Poids |
| :------------------------------------------------------------------ | :---- |
| ratio de performance en FP32 (matrices denses sur les cœurs GPU réguliers) | 40%   |
| ratio de performance en FP16 (matrices denses sur les [cœurs Tensor](https://www.techspot.com/article/2049-what-are-tensor-cores/)) | 40%   |
| ratio de quantité de mémoire GPU                                    | 20%   |

Nous utilisons le GPU **A100-40gb** de NVidia comme modèle de référence, auquel nous assignons une valeur 4 UGR (pour des raisons historiques). Ses ratios de quantité de mémoire et de performance FP32 et FP16 sont fixés à 1.0. En multipliant les pourcentages dans le tableau précédent par 4, nous obtenons les coefficients nécessaires pour calculer le score de chaque composante (FP32, FP16, mémoire). Ainsi, les UGR des modèles disponibles sont :

### Scores UGR pour les GPU entiers, par modèle

| Modèle        | score, FP32 | score, FP16 | score, mémoire | score combiné | alloué par concours |
| :------------ | :---------- | :---------- | :------------- | :------------ | :------------------ |
| **A100-40gb** | **1.60**    | **1.60**    | **0.80**       | **4.0**       | oui                 |
| A100-80gb     | 1.60        | 1.60        | 1.60           | 4.8           | non                 |
| H100-80gb     | 5.48        | 5.08        | 1.60           | 12.2          | oui                 |
| B200-180gb    | 6.16        | 11.28       | 3.60           | 21.0          | oui                 |

Le [renouvellement de l'infrastructure](../clusters/infrastructure_renewal.md) en 2025 a permis de planifier une fraction d'un GPU à l'aide de la [technologie GPU multi-instances](../programming/multi-instance_gpu.md). Différents travaux, appartenant potentiellement à différents utilisateurs, pourront s'exécuter sur le même GPU en même temps. Selon la terminologie de NVidia, une fraction d'un GPU allouée à un seul travail est appelée une *instance GPU*, (parfois *instance MIG*).

Le tableau suivant montre les modèles de GPU ou instances que vous pouvez sélectionner sur le formulaire dans CCDB pour votre demande d'allocation pour 2027. Les valeurs UGR des instances sont estimées à partir des valeurs de performance d'un GPU entier et de la fraction du GPU qu'occupe l'instance.

### Modèles et instances disponibles pour le concours de 2027

| Modèle / Instance | Fraction du GPU          | UGR  |
| :---------------- | :----------------------- | :--- |
| **A100-40gb**     | GPU entier ⇒ 100%        | 4.0  |
| A100-1g.5gb       | max(1g/7g, 5GB/40GB) ⇒ 14% | 0.6  |
| A100-2g.10gb      | max(2g/7g, 10GB/40GB) ⇒ 28% | 1.1  |
| A100-3g.20gb      | max(3g/7g, 20GB/40GB) ⇒ 50% | 2.0  |
| **H100-80gb**     | GPU entier ⇒ 100%        | 12.2 |
| H100-1g.10gb      | max(1g/7g, 40GB/80GB) ⇒ 14% | 1.7  |
| H100-2g.20gb      | max(2g/7g, 40GB/80GB) ⇒ 28% | 3.5  |
| H100-3g.40gb      | max(3g/7g, 40GB/80GB) ⇒ 50% | 6.1  |
| **B200-180gb**    | GPU entier ⇒ 100%        | 21.0 |

!!! note
    Une instance GPU ayant le profil **1g** vaut un septième (1/7) d'un GPU A100 ou H100. Le profil **3g** tient compte de la quantité de mémoire additionnelle par **g**. Les profils **4g** ne sont pas disponibles sur nos grappes.

## Constance des allocations en UGR

*   Dans le cadre du concours pour l'allocation de ressources, toute demande de GPU doit spécifier le modèle de GPU préféré pour le projet. Ensuite, dans le formulaire CCDB, la quantité d'unités GPU de référence (UGR) sera automatiquement calculée à partir de la quantité demandée de GPU-année par année de projet.
    *   Par exemple, si vous sélectionnez la ressource *narval-gpu* et demandez 13 GPU-année du modèle A100-40gb, la quantité correspondante en UGR serait de 13 * 4,0 = 52. Le comité d’allocation des ressources attribuerait alors jusqu'à 52 UGR en fonction du score de la proposition. Si votre allocation doit être déplacée vers une autre grappe, le comité attribuera des GPU-année à cette autre ressource tout en conservant la même quantité en UGR.

# Effet détaillé de l'utilisation des ressources sur la priorité

Le principe gouverneur dans notre façon de déterminer la priorité des tâches de calcul se base sur les ressources qu’une tâche rend **non disponibles aux autres utilisateurs** plutôt que sur les ressources effectivement utilisées.

Le cas de cœurs non utilisés qui influent sur le calcul des priorités se produit souvent lorsqu’une tâche est soumise en demandant plusieurs cœurs, mais n’en consomme effectivement qu’une partie à l’exécution. C’est le nombre de cœurs demandés par une tâche qui a une incidence sur la priorisation des prochaines tâches puisque la tâche bloque les cœurs non utilisés pendant son exécution.

Un autre cas fréquent de cœurs non utilisés se pose lorsqu’une tâche exige plus de mémoire que celle demandée pour un cœur. Sur une grappe où chaque cœur serait doté de 4Go de mémoire, une tâche qui demanderait un seul cœur et 8Go de mémoire bloquerait donc 2 cœurs et le deuxième cœur ne serait pas disponible pour les tâches des autres groupes de recherche.

## Équivalents-cœurs utilisés par l'ordonnanceur

Un équivalent-cœur se compose d’**un cœur simple et d’une certaine quantité de mémoire**; pour le nommer, nous utilisons le terme *bundle*. En plus du cœur, le *bundle* contient aussi la mémoire considérée comme étant associée à ce cœur.

Présentement, nos grappes offrent surtout des cœurs de 4Go puisque ceci est le ratio mémoire:cœur pour le type de nœuds le plus commun. L’utilisation des ressources par une tâche est comptabilisée à raison de 4Go par cœur, comme mentionné ci-dessus.

Le suivi des cibles s’avère relativement simple quand les ressources demandées sont des cœurs et des quantités de mémoire qui correspondent à un équivalent-cœur entier, plutôt qu’à une portion d’équivalent-cœur. Les choses se compliquent parce que l’utilisation de portions d’équivalents-cœur risque d’augmenter le pointage servant au calcul de la juste part du groupe de recherche. En pratique, la méthode appliquée résout le problème d'équité ou de perception d'équité, mais cette méthode n’est pas intuitive au début.

Dans les exemples qui suivent, la mémoire est de 4Go.

**Comptabilisation par équivalents-cœur**

Examinons le cas où nous avons un *bundle* composé de 1 cœur et 4Go de mémoire.

*   Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de mémoire, c’est-à-dire plus que le ratio 1cœur/4Go.
    *   Par exemple, si on demande 2 cœurs et 2Go par cœur pour une mémoire totale de 4Go; la tâche exige 2 équivalents-cœur pour les cœurs, mais un seul *bundle* pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-cœurs.

*   La mémoire est comptabilisée si un groupe utilise plus de mémoire que le ratio de 1 cœur/4Go.
    *   Un autre exemple, si on demande 2 cœurs et 5Go par cœur pour une mémoire totale de 10Go; la tâche exige 2.5 *bundles* pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2.5 équivalents-cœurs.

## Équivalents-UGR utilisés par l'ordonnanceur

L’utilisation des GPU et leurs ressources associées suit les mêmes principes que ceux décrits pour les équivalents-cœurs, sauf qu’une UGR est ajoutée au *bundle* avec de la mémoire et plusieurs cœurs. Ceci signifie que la comptabilisation de l’utilisation de la cible pour l’allocation de GPU doit inclure l’UGR. Tout comme le système de points utilisé dans l’expression de l’utilisation de la ressource en équivalents-cœurs, nous utilisons aussi un système de points pour les équivalents-UGR.

Le calcul de priorité se fait en fonction du nombre maximum de *bundles* UGR-cœurs-mémoire demandés. Examinons le cas où nous avons un *bundle* de 1 UGR, 3 cœurs et 4Go de mémoire.

*   Les UGR sont comptabilisés si un groupe utilise plus de UGR que de cœurs OU de mémoire par *bundle*. Prenons l'exemple d'un utilisateur qui demande 2 GPU (de 1 UGR chacun), 3 cœurs et 4Go de mémoire. La tâche exige donc l'équivalent de 2 *bundles* pour les GPU, mais un seul pour les cœurs et la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-UGR.

*   Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de UGR OU plus de mémoire par *bundle* avec GPU. Par exemple, si l'on demande 1 GPU de 1 UGR, 5 cœurs et 5Go; la requête exige donc 1.66 *bundles* avec GPU pour les cœurs, mais un seul *bundle* pour le GPU et 1.25 *bundle* pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue donc la demande à 1.66 équivalents-UGR.

*   La mémoire est comptabilisée si un groupe utilise plus de mémoire que de UGR OU de cœurs par *bundle* avec GPU. Un autre cas est si l'on demande 1 GPU de 1 UGR, 2 cœurs et 6Go; la requête exige donc 1.5 *bundle* avec GPU pour la mémoire, mais un seul *bundle* pour les GPU et 0.66 pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 1.5 équivalents-GPU.

*   Considérons sur une grappe fictive un *bundle* comprenant un GPU V100-32gb, 7.8 cœurs et 10.4 Go de mémoire vive vaudrait 2.6 équivalents-UGR.

*   De même, sur cette grappe fictive, un *bundle* comprenant un GPU A100-40gb, 12 cœurs et 16 Go de mémoire vive vaudrait 4.0 équivalents-UGR.

### Ratios dans les bundles

Les différents *bundles* UGR-cœur-mémoire et GPU-cœur-mémoire des systèmes de l'Alliance ont les caractéristiques suivantes (un seul ratio par grappe) :

| Grappe                                | Cœurs par UGR | Mémoire par UGR (en GB) |
| :------------------------------------ | :------------ | :---------------------- |
| [Fir](../software/fir.md)   | 0.98          | 23.6                    |
| [Narval](../clusters/narval.md) | 3.00          | 31.1                    |
| [Nibi](../clusters/nibi.md) | 1.15          | 20.5                    |
| [Rorqual](../clusters/rorqual.md) | 1.31          | 10.2                    |
| [Trillium](../clusters/trillium.md) | 1.97          | 15.4                    |

Caractéristiques des *bundles*

| Grappe                                | Modèle ou instance | UGR par GPU | Bundle par GPU       | Recommendation par GPU |
| :------------------------------------ | :----------------- | :---------- | :------------------- | :--------------------- |
| [Fir](../software/fir.md)   | **H100-80gb**      | **12.2**    | **12 cœurs, 288GB**  | **12 cœurs, 280GB**    |
| [Fir](../software/fir.md)   | H100-1g.10gb       | 1.74        | 1.7 cœurs, 41GB      | 1 cœur, 35GB           |
| [Fir](../software/fir.md)   | H100-2g.20gb       | 3.48        | 3.4 cœurs, 82GB      | 3 cœurs, 70GB          |
| [Fir](../software/fir.md)   | H100-3g.40gb       | 6.1         | 6 cœurs, 144GB       | 6 cœurs, 140GB         |
| [Narval](../clusters/narval.md) | **A100-40gb**      | **4.0**     | **12 cœurs, 124.5GB** | **12 cœurs, 124GB**    |
| [Narval](../clusters/narval.md) | A100-1g.5gb        | 0.57        | 1.7 cœurs, 17.7GB    | 1 cœur, 15GB           |
| [Narval](../clusters/narval.md) | A100-2g.10gb       | 1.14        | 3.4 cœurs, 35.4GB    | 3 cœurs, 31GB          |
| [Narval](../clusters/narval.md) | A100-3g.20gb       | 2.0         | 6.0 cœurs, 62.2GB    | 6 cœurs, 62GB          |
| [Nibi](../clusters/nibi.md)   | **H100-80gb**      | **12.2**    | **14 cœurs, 250GB**  | **14 cœurs, 250GB**    |
| [Nibi](../clusters/nibi.md)   | H100-1g.10gb       | 1.74        | 2 cœurs, 35.7GB      | 2 cœurs, 31GB          |
| [Nibi](../clusters/nibi.md)   | H100-2g.20gb       | 3.48        | 4 cœurs, 71.4GB      | 4 cœurs, 62GB          |
| [Nibi](../clusters/nibi.md)   | H100-3g.40gb       | 6.1         | 7 cœurs, 125GB       | 6 cœurs, 124GB         |
| [Rorqual](../clusters/rorqual.md) | **H100-80gb**      | **12.2**    | **16 cœurs, 124.5GB** | **16 cœurs, 124GB**    |
| [Rorqual](../clusters/rorqual.md) | H100-1g.10gb       | 1.74        | 2.3 cœurs, 17.7GB    | 2 cœurs, 15GB          |
| [Rorqual](../clusters/rorqual.md) | H100-2g.20gb       | 3.48        | 4.5 cœurs, 35.4GB    | 4 cœurs, 31GB          |
| [Rorqual](../clusters/rorqual.md) | H100-3g.40gb       | 6.1         | 8 cœurs, 62.2GB      | 8 cœurs, 62GB          |
| [Trillium](../clusters/trillium.md) | **H100-80gb**      | **12.2**    | **24 cœurs, 188GB**  | **24 cœurs, 188GB**    |
| [Trillium](../clusters/trillium.md) | **B200-180gb**     | **21.0**    | **12 cœurs, 250GB**  | **12 cœurs, 250GB**    |

!!! note
    Si l'ordonnanceur établit la priorité sur la base de l'utilisation calculée avec les *bundles*, une demande de plusieurs GPU sur un même nœud doit aussi tenir compte des ratios physiques.

# Visionner l'utilisation des ressources dans le portail

Le portail [portal.alliancecan.ca/slurm](https://portal.alliancecan.ca/slurm) offre une interface interactive qui montre l'utilisation des ressources par les tâches soumises sur nos grappes nationales. Par défaut, la vue initiale affiche les jours CPU utilisés par tous vos projets sur une grappe donnée. Si vous n'utilisez pas cette grappe, le message *No Data or usage too small to have a meaningful plot* est affiché. Pour personnaliser l'affichage, sélectionnez des options dans les panneaux de gauche :

*   Sélectionner le système et les dates
*   Paramètres
*   Compte SLURM

## Utilisation par un compte particulier

Si vous avez accès à plusieurs [comptes Slurm](running_jobs.md), sélectionnez celui qui vous intéresse dans la liste sous **Compte SLURM --> Sélectionner le compte de l'utilisateur**. Si le champ **Sélectionner le compte de l'utilisateur** est vide, l'interface affiche l'utilisation de tous vos comptes sur la grappe sélectionnée pour la période spécifiée. Le menu déroulant **Sélectionner le compte de l'utilisateur** liste tous les comptes pour lesquels des tâches ont été exécutées durant la période. Les autres comptes auxquels vous avez accès, mais qui n'ont pas utilisé la grappe sélectionnée durant cette période, sont également listés, mais ils sont grisés et non sélectionnables, car ils ne généreront pas de graphique. Lorsque vous sélectionnez un seul compte de projet, l'affichage est mis à jour et les détails du compte apparaissent dans le panneau **Informations sur l'allocation**. La hauteur de chaque barre représente la mesure quotidienne (par exemple, les jours pour les équivalents CPU) pour tous les utilisateurs du compte sur le système sélectionné. L'utilisation des sept principaux utilisateurs est indiquée par une couleur spécifique pour chacun, tandis que la couleur grise empilée en dessous représente l'utilisation par tous les autres utilisateurs. Vous pouvez interagir avec le graphique en utilisant les outils [Plotly](https://plotly.com/graphing-libraries/) (zoom, panoramique, etc.) dont les icônes apparaissent en haut à droite lorsque votre souris survole le graphique. Vous pouvez aussi utiliser la légende à droite pour manipuler l'affichage en cliquant sur un élément pour le masquer ou le montrer de nouveau, ou en double-cliquant pour masquer ou montrer tous les autres éléments.

## Options de la légende

La légende offre des options d'affichage permettant d'activer ou de désactiver des variables supplémentaires. En plus des couleurs d'utilisation par utilisateur, la légende permet de voir l'**Utilisation brute SLURM**, les **Parts brutes SLURM**, l'**Allocation CCDB**, les ressources en attente pour les **Tâches en attente**, et le total quotidien. L'**Utilisation brute SLURM** et les **Parts brutes SLURM** sont dérivées des parts de chaque compte sur les grappes. L'**Allocation CCDB** représente les parts brutes SLURM dans le profil du compte CCDB. Les fines barres grises des colonnes pour les **Tâches en attente** illustrent la quantité de ressources demandées par jour pour les tâches en file. Le texte au-dessus de chaque barre indique le total quotidien pour tous les utilisateurs. Un simple clic sur un élément de la légende l'active ou le désactive. Un double-clic active ou désactive tous les autres éléments.

## Cible d'allocation et ressources en attente

Lorsqu'un seul compte est sélectionné, les parts brutes Slurm apparaissent sous forme de ligne rouge horizontale. Vous pouvez les masquer ou les afficher de nouveau en cliquant sur **Afficher la cible d'allocation par défaut** dans le panneau **Paramètres**, ou sur **Parts brutes SLURM** dans la légende. Pour afficher l'utilisation des ressources demandées pour les tâches en attente, cliquez sur **Tâches en attente** dans la légende.

## Options graphiques

Les options natives de Plotly s'affichent en haut à droite lorsque votre souris survole le graphique. Les icônes **Télécharger le graphique en PNG**, **Zoom**, **Panoramique**, **Sélection par boîte**, **Sélection par lasso**, **Zoom avant**, **Zoom arrière**, **Mise à l'échelle automatique** et **Réinitialiser les axes** permettent de modifier la sélection et l'échelle. Lorsque vous survolez une section de barre, une info-bulle affiche le nom de l'utilisateur, la date et la quantité d'utilisation de l'élément ciblé (il s'agit de l'utilisation spécifique à l'utilisateur, et non de la somme pour tous les utilisateurs ce jour-là).

## Parts brutes et utilisation brute par défaut

Les parts brutes SLURM d'un compte d'allocation rrg-* ou rpp-* sont une ligne droite correspondant à l'allocation de ressources du compte sur la grappe. Pour les comptes par défaut, les parts brutes SLURM évoluent dans le temps en fonction du nombre de comptes actifs sur la grappe. Tracer les parts brutes SLURM d'un compte par défaut sur une grappe spécifique permet de déterminer facilement l'utilisation attendue d'un compte par défaut sur cette grappe.

L'utilisation brute SLURM est une mesure utilisée par l'ordonnanceur pour déterminer la priorité des comptes. Elle correspond à la somme cumulée de l'utilisation des comptes en unités de facturation, plus une période de décroissance. Tracer l'utilisation brute SLURM d'un compte permet d'évaluer l'influence de l'utilisation passée sur la priorité du compte au fil du temps. En règle générale, si l'utilisation brute SLURM est 10 fois supérieure aux parts brutes SLURM, l'utilisation du compte est équivalente à sa part cible (par exemple, le taux d'utilisation que la planification vise à maintenir pour le compte).

## Grappe et dates de début et de fin

Le menu déroulant **Système** affiche les grappes actives utilisant l'ordonnanceur Slurm. Vous pouvez spécifier un intervalle de temps à l'aide des champs **Date de début (incl.)** et **Date de fin (incl.)**. Si vous entrez une date de fin future, une projection de l'utilisation sera affichée. Le résultat inclura les tâches **en cours** (R) et **en attente** (PD) pour la durée demandée.

## Projection de l'utilisation

L'entrée d'une date de fin future déclenche l'affichage d'une bande rouge verticale qui délimite les résultats de la projection. Pour cette projection, nous partons du principe que toutes les tâches en cours seront exécutées dans les limites de temps spécifiées. Pour les tâches en attente, nous supposons qu'elles commenceront à la date de fin demandée (c'est-à-dire "maintenant") et continueront pour la durée demandée. Il est important de noter que ce résultat n'est en aucun cas une prévision des événements futurs réels.

## Métriques, sommation et tâches en cours d'exécution

Dans le menu déroulant **Métriques**, vous pouvez sélectionner parmi les indicateurs suivants : CPU, équivalent-CPU, UGR, équivalent-UGR, mémoire, comptabilisation, GPU et tous les modèles de GPU disponibles sur la grappe sélectionnée.

Le menu déroulant **Sommation** permet de basculer entre **Total** et **Total cumulé**. Si vous sélectionnez **Total**, chaque barre représente l'utilisation totale pour cette journée. Si vous sélectionnez **Total cumulé**, chaque barre représente la somme de l'utilisation pour cette journée et de tous les jours précédents jusqu'au début de la période spécifiée. Si l'option **Afficher la cible d'allocation par défaut** est réglée sur **Oui**, la cible est ajustée de la même manière pour afficher le total cumulé de l'utilisation cible. Consultez la section suivante pour plus de détails.

Dans le menu **Inclure les tâches en cours**, cliquez sur **Non** pour afficher l'utilisation par les tâches terminées et sur **Oui** pour inclure l'utilisation par les tâches en cours.

## Total cumulé

Le graphique illustre l'écart entre l'utilisation d'un compte et sa part cible pour la période sélectionnée. Les valeurs affichées sont la somme cumulée sur plusieurs jours, basée sur la vue de sommation totale de l'utilisation et de la cible d'allocation. Si une tâche soumise dépasse la part cible du compte, on s'attend à ce que la somme cumulée de l'utilisation fluctue autour de cette part cible, à condition que l'ordonnanceur applique correctement le principe de la juste part. Puisque l'ordonnanceur tient compte d'une période de décroissance pour l'utilisation passée, un intervalle d'affichage des 30 derniers jours est idéal pour évaluer sa performance à maintenir la juste part.

# Visionner l'utilisation des ressources dans CCDB

Vous pouvez consulter les données d'utilisation des ressources de votre groupe en sélectionnant **Mon compte --> Utilisation par le groupe** dans la base de données CCDB.

Les valeurs d'utilisation pour les CPU (cœurs-année) et les GPU-année sont calculées en fonction des ressources allouées aux tâches exécutées sur les grappes. Il est important de noter que les valeurs présentées dans ces rapports ne représentent pas les équivalents-cœur; par conséquent, l'utilisation des tâches nécessitant beaucoup de mémoire ne correspondra pas toujours à l'utilisation du compte telle qu'interprétée par l'ordonnanceur de la grappe.

La première barre d’onglets offre les vues suivantes :
*   **Par ressource de calcul**; nom de la grappe sur laquelle les tâches ont été soumises,
*   **Par projet (RAPI)**; projets auxquels les tâches ont été soumises,
*   **Par utilisateur**; utilisatrice ou utilisateur ayant soumis les tâches,
*   **Utilisation du stockage**; voyez [Stockage et gestion des fichiers](../storage-and-data/storage_and_file_management.md).

## Utilisation par ressource de calcul

Cette vue montre l’utilisation par ressource de calcul par grappe, pour tous les groupes desquels vous êtes propriétaire ou membre, pour l’année d’allocation en cours qui commence le 1er avril. Les données représentent l’utilisation à jour et supposent que cette utilisation restera la même jusqu’à la fin de l’année d’allocation.

Dans la colonne **Informations supplémentaires**, cliquez sur **Utilisation sur une base mensuelle** pour obtenir la répartition mensuelle de la ressource correspondante. En cliquant sur **Utilisation par utilisateur**, la répartition est présentée par l'utilisateur ou l'utilisatrice ayant soumis les tâches.

## Utilisation par projet

Pour cette vue, une troisième barre d'onglets permet de sélectionner l'identifiant de projet pour l'année d'allocation choisie. Le tableau montre les détails pour chaque projet ainsi que les ressources utilisées sur toutes les grappes. Dans le haut de la vue, on trouve le nom du compte (par exemple def-, rrg- ou rpp-*, etc.), le titre du projet et le ou la propriétaire, ainsi que les sommaires de l'allocation et de l'utilisation.

## Utilisation des GPU en unités GPU de référence (UGR)

Pour chaque projet (RAPI) ayant une utilisation de GPU, le détail d'utilisation par modèle de GPU est donné en GPU-années et en UGR-années dans une table située au bas de la page.

## Utilisation par utilisateur

Cette vue montre l'utilisation par utilisatrices et utilisateurs ayant soumis des tâches pour le projet sélectionné (comptes de groupes), par système. En cliquant sur le nom d'une personne en particulier, vous obtiendrez son utilisation répartie par grappe. Tout comme les sommaires pour les groupes, vous pouvez utiliser l'option **Utilisation sur une base mensuelle**.