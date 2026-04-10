---
title: "Allocations and compute scheduling/fr"
slug: "allocations_and_compute_scheduling"
lang: "fr"

source_wiki_title: "Allocations and compute scheduling/fr"
source_hash: "ad07300d0355335a030b0b1232a8d452"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:08:38.636210+00:00"

tags:
  - slurm

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

*Page enfant de [Politique d'ordonnancement des tâches](politique-dordonnancement-des-taches.md)*

# Allocations pour le calcul haute performance

**Une *allocation* est l’attribution d’une quantité de ressources à un groupe de recherche pour une période donnée, habituellement un an.** Il s'agit soit d'un maximum comme dans le cas du stockage, soit d'une moyenne d'utilisation sur une période donnée comme c'est le cas pour les ressources partagées que sont les cœurs de calcul.

L’allocation des ressources de stockage attribue un maximum déterminé d’espace réservé à l’usage exclusif d’un groupe de recherche. Pour sa part, l’allocation des ressources partagées que sont les cœurs-année et les GPU-année est plus complexe puisque ces ressources sont partagées par l’ensemble des groupes et que l’allocation tient compte de l’utilisation moyenne de chaque groupe.

La durée de l’allocation est une valeur de référence utilisée pour calculer la moyenne de la consommation des ressources au cours de la période pendant laquelle celles-ci sont disponibles. Par exemple, si les grappes ne sont pas disponibles pour une semaine dû à des opérations de maintenance, les groupes de recherche touchés n’obtiennent pas une semaine additionnelle en compensation à la fin de la période. De la même manière, si la période d’allocation est allongée, les groupes n’y perdent pas en utilisation.

Notons qu’une allocation de cœurs-année et de GPU-année en ressources partagées considère la moyenne d’utilisation cible dans le temps; un groupe est donc plus susceptible d’atteindre et même de dépasser ses cibles en utilisant ses ressources de façon régulière sur la période qu’en soumettant des tâches en rafale (*burst*) ou en les reportant à plus tard.

## De l'allocation à l'ordonnancement par priorité

Les ressources de calcul par cœurs-année et par GPU-année reçoivent des tâches qui sont immédiatement prises en charge par l’ordonnanceur. Rappelons qu’une tâche se compose d’une application logicielle et de la liste des ressources pour l’exécuter. L’ordonnanceur est aussi une application logicielle dont le rôle est de calculer la priorité de chaque tâche et de lui attribuer les ressources nécessaires selon leur disponibilité et en accord avec les règles de priorisation.

À l’aide d’algorithmes spécialisés, l’ordonnanceur tient compte des cibles de chaque groupe et compare la consommation récente du groupe à l’utilisation qui lui était allouée. Un des facteurs déterminants est la consommation à l’intérieur de la période. Le facteur qui possède cependant le plus de poids est la consommation (ou la non-consommation) récente, ceci en vue d’offrir une opération plus stable aux groupes dont l’utilisation réelle se rapproche des ressources qui leur étaient allouées. Cette façon de procéder assure une meilleure répartition du parc de ressources pour l’ensemble des groupes et fait en sorte qu’il est théoriquement possible pour tous les groupes d’atteindre leurs cibles.

## Conséquences d'une surutilisation d'une allocation CPU ou GPU

Si vous avez des tâches en attente et qu’à ce moment la demande en ressources de calcul est basse, l’ordonnanceur pourrait faire exécuter vos tâches même si vous dépassez la quantité cible de votre allocation. Tout ce qui peut se produire alors serait que les prochaines tâches que vous soumettrez se voient attribuer un plus bas niveau de priorité que celles soumises par des groupes qui n’ont pas encore atteint leur niveau cible d’utilisation. Aucune tâche soumise à l’ordonnanceur n’est refusée en raison d’une surutilisation de ressources et votre utilisation moyenne de ressources sur la période d’allocation devrait se situer proche de la cible qui vous a été allouée.

Il se pourrait qu’au cours d’un mois ou d’une année vous puissiez accomplir plus de travail que votre allocation ne semblerait le permettre, mais ce scénario est peu probable puisque la demande est plus élevée que la quantité de ressources dont nous disposons.

# Unités GPU de référence (UGR)

La performance des GPU a considérablement augmenté ces dernières années et continue sa progression. Par le passé et jusqu'au concours de 2023, nous considérions tous les GPU comme étant équivalents les uns aux autres. Ceci posait des problèmes à la fois dans le processus d'attribution et lors de l'exécution des tâches. Pour contrer ceci, nous avons créé pour l'année 2024 l'unité GPU de référence (UGR) qui permet de classer tous les modèles de GPU en production. Depuis la période d'allocation de 2025-2026, nous devons aussi tenir compte de [la technologie des GPU multi-instances](multi-instance-gpu.md) qui rend la situation un peu plus complexe.

Parce qu'environ la moitié des tâches utilisent principalement des opérations à virgule flottante simple précision ([FP32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)), que les autres utilisent des opérations à virgule flottante demi-précision ([FP16](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)), et que la plupart des utilisateurs sont limités par la quantité de mémoire des GPU, nous classons les modèles de GPU selon les critères d'évaluation avec leur poids correspondant&nbsp;:

| Critère d'évaluation | Poids |
| :------------------- | :---- |
| score FP32 (matrices denses sur les cœurs GPU réguliers) | 40% |
| score FP16 (matrices denses sur les [cœurs Tensor](https://www.techspot.com/article/2049/what-are-tensor-cores/)) | 40% |
| score mémoire GPU | 20% |

Nous utilisons le GPU **A100-40gb** de NVidia comme modèle de référence, auquel nous assignons la valeur UGR de 4 (pour des raisons historiques). Sa mémoire et ses performances FP32 et FP16 sont fixées à 1.0. En multipliant les pourcentages dans le tableau précédent par 4, nous obtenons les coefficients et les valeurs UGR pour les autres modèles.

**Scores UGR pour les GPU entiers, par modèle**

| Modèle | Score FP32 (Coefficient 1.6) | Score FP16 (Coefficient 1.6) | Score mémoire (Coefficient 0.8) | Score combiné (UGR) | Disponible (Présentement) | Disponible (Pour 2026) | Alloué par concours (Concours de 2026) |
| :----- | :--------------------------- | :--------------------------- | :------------------------------ | :------------------ | :------------------------ | :----------------------- | :------------------------------------- |
| H100-80gb | 3.44 | 3.17 | 2.0 | 12.2 | oui | oui | oui |
| A100-80gb | 1.00 | 1.00 | 2.0 | 4.8 | ? | ? | non |
| A100-40gb | **1.00** | **1.00** | **1.0** | **4.0** | oui | oui | oui |
| V100-32gb | 0.81 | 0.40 | 0.8 | 2.6 | non | non | non |
| V100-16gb | 0.81 | 0.40 | 0.4 | 2.2 | non | ? | non |
| T4-16gb | 0.42 | 0.21 | 0.4 | 1.3 | non | non | non |
| P100-16gb | 0.48 | 0.03 | 0.4 | 1.1 | non | non | non |
| P100-12gb | 0.48 | 0.03 | 0.3 | 1.0 | non | non | non |

Le [renouvellement de l'infrastructure](infrastructure-renewal.md) en 2025 permettra de planifier une fraction d'un GPU à l'aide de la [technologie GPU multi-instances](multi-instance-gpu.md). Différents travaux, appartenant potentiellement à différents utilisateurs, pourront s'exécuter sur le même GPU en même temps. Selon la terminologie de NVidia, une fraction d'un GPU allouée à un seul travail est appelée une *instance GPU*, (parfois *instance MIG*).

Le tableau suivant montre les modèles de GPU ou instances que vous pouvez sélectionner sur le formulaire dans CCDB pour votre demande d'allocation pour 2026. Les valeurs UGR des instances sont estimées à partir des valeurs de performance d'un GPU entier et de la fraction du GPU qu'occupe l'instance.

**Modèles et instances disponibles pour la période d'allocations 2025-2026**

| Modèle / Instance | Fraction du GPU | UGR |
| :---------------- | :-------------- | :-- |
| A100-40gb | GPU entier ⇒ 100% | 4.0 |
| A100-1g.5gb | max(1g/7g, 5GB/40GB) ⇒ 14% | 0.6 |
| A100-2g.10gb | max(2g/7g, 10GB/40GB) ⇒ 28% | 1.1 |
| A100-3g.20gb | max(3g/7g, 20GB/40GB) ⇒ 50% | 2.0 |
| H100-80gb | GPU entier ⇒ 100% | 12.2 |
| H100-1g.10gb | max(1g/7g, 40GB/80GB) ⇒ 14% | 1.7 |
| H100-2g.20gb | max(2g/7g, 40GB/80GB) ⇒ 28% | 3.5 |
| H100-3g.40gb | max(3g/7g, 40GB/80GB) ⇒ 50% | 6.1 |

Remarque : Une instance GPU ayant le profil **1g** vaut un septième (1/7) d'un GPU A100 ou H100. Le profil **3g** tient compte de la quantité de mémoire additionnelle par **g**. Par souci de simplicité, les profils **4g** ne sont pas disponibles sur nos grappes.

## Choisir les modèles de GPU pour votre projet

Les scores relatifs du précédent tableau devraient vous aider à sélectionner les modèles les plus convenables. Les exemples suivants présentent des cas extrêmes.

*   Si vos applications font surtout des opérations FP32, le modèle A100-40gb devrait être deux fois plus rapide que le P100-12gb, mais l'utilisation des ressources sera considérée comme étant quatre fois plus grande. En conséquence, pour le même nombre d'UGR, le modèle P100-12gb devrait vous permettre d'exécuter deux fois plus de calculs.
*   Si vos applications font surtout des opérations FP16 (ce qui est le cas en intelligence artificielle et avec les opérations à précision mixte ou utilisant [d'autres formats à virgule flottante](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)), l'utilisation d'un A100-40gb sera calculée comme utilisant quatre fois les ressources d'un P100-12gb, mais pourra faire ~30 fois plus de calculs dans la même période, ce qui vous permettrait d'exécuter ~7.5 fois plus de calculs.

## Constance des allocations en UGR

*   Dans le cadre du concours pour l'allocation de ressources, toute demande de GPU doit spécifier le modèle de GPU préféré pour le projet. Ensuite, dans le formulaire CCDB, la quantité d'unités GPU de référence (UGR) sera automatiquement calculée à partir de la quantité demandée de GPU-année par année de projet.
    *   Par exemple, si vous sélectionnez la ressource *narval-gpu* et demandez 13 GPU-année du modèle A100-40gb, la quantité correspondante en UGR serait de 13 * 4,0 = 52. Le comité d’allocation des ressources attribuerait alors jusqu'à 52 UGR en fonction du score de la proposition. Si votre allocation doit être déplacée vers une autre grappe, le comité attribuera des GPU-année à cette autre ressource tout en conservant la même quantité en UGR.

# Effet détaillé de l'utilisation des ressources sur la priorité

Le principe gouverneur dans notre façon de déterminer la priorité des tâches de calcul se base sur les ressources qu’une tâche rend **non disponibles aux autres utilisateurs** plutôt que sur les ressources effectivement utilisées.

Le cas de cœurs non utilisés qui influent sur le calcul des priorités se produit souvent lorsqu’une tâche est soumise en demandant plusieurs cœurs, mais n’en consomme effectivement qu’une partie à l’exécution. C’est le nombre de cœurs demandés par une tâche qui a une incidence sur la priorisation des prochaines tâches puisque la tâche bloque les cœurs non utilisés pendant son exécution.

Un autre cas fréquent de cœurs non utilisés se pose lorsqu’une tâche exige plus de mémoire que celle demandée pour un cœur. Sur une grappe où chaque cœur serait doté de 4Go de mémoire, une tâche qui demanderait un seul cœur et 8Go de mémoire bloquerait donc 2 cœurs et le deuxième cœur ne serait pas disponible pour les tâches des autres groupes de recherche

## Équivalents-cœurs utilisés par l'ordonnanceur

Un équivalent-cœur se compose d’**un cœur simple et d’une certaine quantité de mémoire**; pour le nommer, nous utilisons le terme *bundle*. En plus du cœur, le bundle contient aussi la mémoire considérée comme étant associée à ce cœur.

Présentement, nos grappes offrent surtout des cœurs de 4Go puisque ceci est le ratio mémoire:cœur pour le type de nœuds le plus commun. L’utilisation des ressources par une tâche est comptabilisée à raison de 4Go par cœur, comme mentionné ci-dessus (voir la Figure 1).

Le suivi des cibles s’avère relativement simple quand les ressources demandées sont des cœurs et des quantités de mémoire qui correspondent à un équivalent-cœur entier, plutôt qu’à une portion d’équivalent-cœur. Les choses se compliquent parce que l’utilisation de portions d’équivalents-cœur risque d’augmenter le pointage servant au calcul de la juste part du groupe de recherche. En pratique, la méthode appliquée résout le problème d'équité ou de perception d'équité, mais cette méthode n’est pas intuitive au début.

Dans les exemples qui suivent, la mémoire est de 4Go.

**Comptabilisation par équivalents-cœur**

Examinons le cas où nous avons un bundle composé de 1 cœur et 4Go de mémoire.

- Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de mémoire, c’est-à-dire plus que le ratio 1cœur/4Go.
    - Dans la figure 2, on demande 2 cœurs et 2Go par cœur pour une mémoire totale de 4Go; la tâche exige 2 équivalents-cœur pour les cœurs, mais un seul bundle pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-cœurs.

- La mémoire est comptabilisée si un groupe utilise plus de mémoire que le ratio de 1 cœur/4Go.
    - Dans la figure 3, on demande 2 cœurs et 5Go par cœur pour une mémoire totale de 10Go; la tâche exige 2.5 bundles pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2.5 équivalents-cœurs.

## Équivalents-UGR utilisés par l'ordonnanceur

L’utilisation des GPU et leurs ressources associées suit les mêmes principes que ceux décrits pour les équivalents-cœurs, sauf qu’une UGR est ajoutée au bundle avec de la mémoire et plusieurs cœurs. Ceci signifie que la comptabilisation de l’utilisation de la cible pour l’allocation de GPU doit inclure l’UGR. Tout comme le système de points utilisé dans l’expression de l’utilisation de la ressource en équivalents-cœurs, nous utilisons aussi un système de points pour les équivalents-UGR.

Le calcul de priorité se fait en fonction du nombre maximum de bundles UGR-coeurs-mémoire demandés. Examinons le cas où nous avons un bundle de 1 UGR, 3 cœurs et 4Go de mémoire.

*   Les UGR sont comptabilisés si un groupe utilise plus de UGR que de cœurs OU de mémoire par bundle. Prenons l'exemple d'un usager demandant 2 GPU (de 1 UGR chacun), 3 cœurs et 4Go de mémoire. La tâche exige donc l'équivalent de 2 bundles pour les GPU, mais un seul pour les cœurs et la mémoire. Pour calculer la priorité, l’ordonnanceur évalue la demande à 2 équivalents-UGR.

*   Les cœurs sont comptabilisés si un groupe utilise plus de cœurs que de UGR OU plus de mémoire par bundle avec GPU. Dans la figure 6, on demande 1 GPU de 1 UGR, 5 cœurs et 5Go; la requête exige donc 1.66 bundles avec GPU pour les cœurs, mais un seul bundle pour le GPU et 1.25 bundle pour la mémoire. Pour calculer la priorité, l’ordonnanceur évalue donc la demande à 1.66 équivalents-UGR.

*   La mémoire est comptabilisée si un groupe utilise plus de mémoire que de UGR OU de cœurs par bundle avec GPU. Dans la figure 7, on demande 1 GPU de 1 UGR, 2 cœurs et 6Go; la requête exige donc 1.5 bundle avec GPU pour la mémoire, mais un seul bundle pour les GPU et 0.66 pour les cœurs. Pour calculer la priorité, l’ordonnanceur évalue la demande à 1.5 équivalents-GPU.

*   Sur la même grappe fictive, un bundle comprenant un GPU V100-32gb, 7.8 cœurs et 10.4 Go de mémoire vive vaudrait 2.6 équivalents-UGR :

*   Sur la même grappe fictive, un bundle comprenant un GPU A100-40gb, 12 cœurs et 16 Go de mémoire vive vaudrait 4.0 équivalents-UGR :

### Ratios dans les bundles
Les différents bundles UGR-coeur-mémoire et GPU-coeur-mémoire des systèmes de l'Alliance ont les caractéristiques suivantes (un seul ratio par grappe)&nbsp;:

**Caractéristiques des bundles**

| Grappe | Cœurs par UGR | Mémoire par UGR (en GB) |
| :----- | :------------ | :---------------------- |
| [Fir](fir.md#caracteristiques-des-noeuds) | 0.98 | 23.6 |
| [Narval](narval.md#caracteristiques-des-noeuds) | 3.00 | 31.1 |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | 1.15 | 20.5 |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | 1.31 | 10.2 |
| [Trillium](trillium.md#caracteristiques-des-noeuds) | 1.97 | 15.4 |

**Caractéristiques des bundles**

| Grappe | Modèle ou instance | UGR par GPU | Bundle par GPU | Recommendation par GPU |
| :----- | :----------------- | :---------- | :------------- | :--------------------- |
| [Fir](fir.md#caracteristiques-des-noeuds) | **H100-80gb** | **12.2** | **12 cœurs, 288GB** | **12 cœurs, 280GB** |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-1g.10gb | 1.74 | 1.7 cœurs, 41GB | 1 cœurs, 35GB |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-2g.20gb | 3.48 | 3.4 cœurs, 82GB | 3 cœurs, 70GB |
| [Fir](fir.md#caracteristiques-des-noeuds) | H100-3g.40gb | 6.1 | 6 cœurs, 144GB | 6 cœurs, 140GB |
| [Narval](narval.md#caracteristiques-des-noeuds) | **A100-40gb** | **4.0** | **12 cœurs, 124.5GB** | **12 cœurs, 124GB** |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-1g.5gb | 0.57 | 1.7 cœurs, 17.7GB | 1 cœur, 15GB |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-2g.10gb | 1.14 | 3.4 cœurs, 35.4GB | 3 cœurs, 31GB |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-3g.20gb | 2.0 | 6.0 cœurs, 62.2GB | 6 cœurs, 62GB |
| [Narval](narval.md#caracteristiques-des-noeuds) | A100-4g.20gb | 2.3 | 6.9 cœurs, 71.5GB | 6 cœurs, 62GB |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | **H100-80gb** | **12.2** | **14 cœurs, 250GB** | **14 cœurs, 250GB** |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-1g.10gb | 1.74 | 2 cœurs, 35.7GB | 2 cœurs, 31GB |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-2g.20gb | 3.48 | 4 cœurs, 71.4GB | 4 cœurs, 62GB |
| [Nibi](nibi.md#caracteristiques-des-noeuds) | H100-3g.40gb | 6.1 | 7 cœurs, 125GB | 6 cœurs, 124GB |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | **H100-80gb** | **12.2** | **16 cœurs, 124.5GB** | **16 cœurs, 124GB** |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-1g.10gb | 1.74 | 2.3 cœurs, 17.7GB | 2 cœurs, 15GB |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-2g.20gb | 3.48 | 4.5 cœurs, 35.4GB | 4 cœurs, 31GB |
| [Rorqual](rorqual.md#caracteristiques-des-noeuds) | H100-3g.40gb | 6.1 | 8 cœurs, 62.2GB | 8 cœurs, 62GB |
| [Trillium](trillium.md#caracteristiques-des-noeuds) | **H100-80gb** | **12.2** | **24 cœurs, 188GB** | **24 cœurs, 188GB** |

**Remarque :** Si l'ordonnanceur établit la priorité sur la base de l'utilisation calculée avec les bundles, une demande de plusieurs GPU sur un même nœud doit aussi tenir compte des ratios physiques.

# Visionner l'utilisation des ressources dans le portail

Le portail [portal.alliancecan.ca/slurm](https://portal.alliancecan.ca/slurm) offre une interface qui montre l'utilisation des ressources par les tâches soumises sur nos grappes nationales. Par défaut, l'image sur la page d'accueil affiche les jours CPU utilisés par tous vos projets sur une grappe quelconque. Si vous n'utilisez pas cette grappe, le message *No Data or usage too small to have a meaningful plot* est affiché. Pour modifier l'image, sélectionnez des options dans les panneaux de gauche.
*   Sélectionner le système et les dates
*   Paramètres
*   Compte SLURM

## Utilisation par un compte particulier

Si vous avez accès à plusieurs [comptes Slurm](running-jobs.md#comptes-et-projets), sélectionnez celui qui vous intéresse dans la liste sous *Compte SLURM* --> *Sélectionner le compte de l'utilisateur*. Si *Sélectionner le compte de l'utilisateur* est vide, l'image montre l'utilisation faite par tous vos comptes sur la grappe sélectionnée et au cours de la période spécifiée. Le menu déroulant *Sélectionner le compte de l'utilisateur* liste tous les comptes pour lesquels des tâches ont été exécutées au cours de la période. Les autres comptes auxquels vous avez accès mais qui n'ont pas utilisé la grappe sélectionnée au cours de la période spécifiée sont aussi listés; cependant, puisque ces comptes ne généreront pas d'image, ils sont grisés et ne peuvent pas être sélectionnés. Lorsque vous sélectionnez un seul compte de projet, l'image est mise à jour et les détails du compte sont affichés dans le panneau *Allocation Information*. La hauteur de chaque barre correspond à la mesure de ce jour (par exemple, les jours pour les équivalents CPU) pour tous les utilisateurs du compte dans le système sélectionné. L'utilisation par les sept principaux utilisateurs est représentée par une couleur spécifique à chacun. La couleur grise sur laquelle les autres couleurs sont empilées représente l'utilisation par tous les autres utilisateurs. Vous pouvez parcourir l'image avec les outils [Plotly](https://plotly.com/graphing-libraries/) (zoom, panorama, etc.) dont les icônes paraissent en haut à droite quand votre souris survole l'image. Vous pouvez également utiliser la légende sur le côté droit pour manipuler l'image. Cliquez sur un des éléments dans l'image pour le cacher ou le montrer de nouveau. Double-cliquer sur un élément cache ou montre tous les autres éléments dans l'image.

## Options de la légende

La légende propose des options d'affichage, plus précisément, des variables supplémentaires qui peuvent être activées ou désactivées. Outre l'affichage de la couleur de chaque utilisateur, la légende permet d'afficher l'utilisation brute SLURM, les parts brutes SLURM, l'allocation CCDB, les ressources en attente pour les tâches en file d'attente et le total quotidien. L'Utilisation brute SLURM (*Utilisation brute SLURM*) et les Parts brutes SLURM (*Parts brutes SLURM*) sont obtenues à partir des parts pour chaque compte sur les grappes. L'Allocation CCDB (*Allocation CCDB*) correspond à la représentation des parts brutes SLURM dans le profil du compte dans CCDB. Les fines barres grises des colonnes des Tâches en attente (*Tâches en attente*) représentent la quantité de ressources pour les tâches dans la file d'attente, par jour. Le texte en haut de chaque barre indique le total quotidien par tous les utilisateurs pour la journée. Un simple clic sur un élément de la légende permet de l'activer ou le désactiver. Un double-clic permet d'activer ou de désactiver tous les autres éléments.

## Cible d'allocation et ressources en attente

Lorsqu'un seul compte a été sélectionné, les parts brutes Slurm sont affichées sous forme d'une ligne rouge horizontale. Elles peuvent être cachées ou montrées de nouveau en cliquant sur *Afficher la cible d'allocation par défaut* dans le panneau *Paramètres*, ou sur *Parts brutes SLURM* dans la légende à droite de l'image.

Pour faire afficher l'utilisation des ressources demandées pour les tâches en attente, cliquez sur *Tâches en attente* dans la légende en haut à droite.

## Options graphiques

Les options natives de Plotly apparaissent en haut à droite lorsque le pointeur de la souris survole l'image. Les icônes *Télécharger le graphique en PNG*, *Zoom*, *Déplacer*, *Sélection rectangulaire*, *Sélection au lasso*, *Zoom avant*, *Zoom arrière*, *Mise à l'échelle automatique* et *Réinitialiser les axes* permettent de modifier la sélection et l'échelle. Lorsque vous survolez une partie de la barre, un texte indique le nom de l'utilisateur, la journée et la quantité d'utilisation de l'élément pointé (notez que cela montre la quantité d'utilisation pour l'utilisateur spécifique et non la somme pour les utilisateurs pour cette journée).

## Parts brutes et utilisation brute par défaut

Les parts brutes SLURM d'un compte d'allocation rrg-* ou rpp-* sont une ligne droite correspondant à l'allocation de ressources du compte sur la grappe. Pour les comptes par défaut, les parts brutes SLURM évoluent dans le temps en fonction du nombre de comptes actifs sur la grappe. Tracer les parts brutes SLURM d'un compte par défaut sur une grappe spécifique permet de déterminer facilement l'utilisation attendue d'un compte par défaut sur cette grappe.

L'utilisation brute SLURM est une mesure utilisée par l'ordonnanceur pour déterminer la priorité des comptes. Elle correspond à la somme cumulée de l'utilisation des comptes en unités de facturation, plus une période de décroissance. Tracer l'utilisation brute SLURM d'un compte permet d'évaluer l'influence de l'utilisation passée sur la priorité du compte au fil du temps. En règle générale, si l'utilisation brute SLURM est 10 fois supérieure aux parts brutes SLURM, l'utilisation du compte est équivalente à sa part cible (par exemple, le taux d'utilisation que la planification vise à maintenir pour le compte).

## Grappe et dates de début et de fin

Le menu déroulant *Système* montre les grappes actives qui utilisent l'ordonnanceur Slurm. Vous pouvez utiliser les champs *Date de début (incl.)* et *Date de fin (incl.)* pour indiquer un intervalle de temps; l'entrée d'une date de fin dans le futur fera afficher une projection de l'utilisation. Le résultat montrera les tâches en cours d'exécution (R) et en attente (PD), pour la durée demandée.

## Projection de l'utilisation

L'entrée d'une date de fin dans le futur fait afficher une bande rouge verticale qui délimite les résultats de la projection. Nous supposons ici que chacune des tâches en cours sera exécutée à l'intérieur de la limite de temps demandée. Dans le cas des tâches en attente, nous supposons que chacune commencera à la date de fin demandée (c'est-à-dire maintenant) et se poursuivra pour la durée demandée. Le résultat n'est aucunement une prévision des événements qui pourraient se produire.

## Métriques, sommation et tâches en cours d'exécution

Dans le menu déroulant *Indicateur* vous pouvez sélectionner parmi les indicateurs suivants&nbsp;: CPU, équivalent-CPU, UGR, équivalent-UGR, mémoire, comptabilisation, GPU et tous les modèles de GPU disponibles sur la grappe sélectionnée.

Le menu déroulant *Sommation* permet de basculer entre *Total* et *Total cumulé*. Si vous sélectionnez *Total*, chaque barre représente l'utilisation totale pour cette journée. Si vous sélectionnez *Total cumulé*, chaque barre représente la somme de l'utilisation pour cette journée plus tous les jours précédents jusqu'au début de la période spécifiée. Si l'*Afficher la cible d'allocation par défaut* est *Oui*, elle est ajustée de la même manière pour afficher le total cumulé de l'utilisation cible. Consultez la section suivante pour en savoir plus.

Dans le menu *Inclure les tâches en cours d'exécution*, cliquez sur *Non* pour faire afficher l'utilisation par les tâches terminées et sur *Oui* pour inclure l'utilisation par les tâches en cours.

## Total cumulé

Le graphique montre comment un compte s'écarte de sa part cible dans la période sélectionnée. Les valeurs utilisées sont la somme cumulée sur plusieurs jours à partir de la vue de sommation totale de l'utilisation et la cible d'allocation. Lorsqu'une tâche soumise demande plus que la part cible du compte, on s'attend que la somme cumulée de l'utilisation oscille au-dessus et en dessous de la part cible si l'ordonnanceur gère correctement le principe de la juste part. Étant donné que l'ordonnanceur utilise une période de décroissance pour l'utilisation passée, un bon intervalle pour déterminer sa performance dans le maintien de la juste part est de faire afficher les 30 derniers jours.

# Visionner l'utilisation des ressources dans CCDB

Vous pouvez visionner les données d’utilisation des ressources par votre groupe en sélectionnant *Mon compte* --> *Utilisation par le groupe* dans la base de données CCDB.

Les valeurs pour l’utilisation des CPU (cœurs-année) et des GPU-année sont calculées selon la quantité des ressources allouées aux tâches exécutées sur les grappes. Notez que les valeurs employées dans les graphiques ne représentent pas les équivalents-cœur; ainsi, l’utilisation par les tâches qui exigent beaucoup de mémoire ne correspond pas à l’utilisation du compte représentée par l’ordonnanceur de la grappe.

La première barre d’onglets offre les vues suivantes&nbsp;:
- **Par ressource de calcul**; nom de la grappe sur laquelle les tâches ont été soumises,
- **Par projet (RAPI)**; projets auxquels les tâches ont été soumises,
- **Par utilisateur**; utilisatrice ou utilisateur ayant soumis les tâches,
- **Utilisation du stockage**; voyez [Stockage et gestion des fichiers](storage-and-file-management.md).

## Utilisation par ressource de calcul

Cette vue montre l’utilisation par ressource de calcul par grappe, pour tous les groupes desquels vous êtes propriétaire ou membre, pour l’année d’allocation en cours qui commence le 1er avril. Les données représentent l’utilisation à jour et supposent que cette utilisation restera la même jusqu’à la fin de l’année d’allocation.

Dans la colonne *Infos supplémentaires*, cliquez sur *Utilisation sur une base mensuelle* pour obtenir la répartition mensuelle pour la ressource correspondante. En cliquant sur *Utilisation par utilisateur*, la répartition se fait par utilisateur ou utilisatrice ayant soumis les tâches.

## Utilisation par projet

Pour cette vue, une troisième barre d'onglets permet de sélectionner l'identifiant de projet pour l'année d'allocation choisie. Le tableau montre les détails pour chaque projet ainsi que les ressources utilisées sur toutes les grappes. Dans le haut de la vue, on trouve le nom du compte (par exemple def-, rrg- ou rpp-*, etc.), le titre du projet et le ou la propriétaire, ainsi que les sommaires de l'allocation et de l'utilisation.

## Utilisation des GPU en unités GPU de référence (UGR)

Pour chaque projet (RAPI) ayant une utilisation de GPU, le détail d'utilisation par modèle de GPU est donné en GPU-années et en UGR-années dans une table située au bas de la page.

## Utilisation par utilisateur

Cette vue montre l'utilisation par utilisatrices et utilisateurs ayant soumis des tâches pour le projet sélectionné (comptes de groupes), par système. En cliquant sur le nom d'une personne en particulier, vous obtiendrez son utilisation répartie par grappe. Tout comme les sommaires pour les groupes, vous pouvez utiliser l'option *Utilisation sur une base mensuelle*.